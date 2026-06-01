#!/usr/bin/env node
/**
 * Local-only fetcher for TryHackMe data.
 *
 * Why this exists: TryHackMe's API sits behind Vercel's Attack Challenge Mode.
 * A real browser solves the JS challenge transparently, but only from a
 * trusted (residential) IP. GitHub Actions runners use datacenter IPs that the
 * challenge blocks with HTTP 429, so the fetch cannot run in CI.
 *
 * Flow: run this on your own machine, it writes scripts/data/thm.json, then you
 * commit & push that file. The CI workflow regenerates the README from it.
 *
 * Usage:
 *   cd scripts/fetch-thm
 *   npm install        # first time only (downloads a Chromium)
 *   npm run fetch
 */

import { writeFile, mkdir } from "node:fs/promises";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import puppeteer from "puppeteer";

const USERNAME = "kOaDT";
const USER_MONGO_ID = "656836cbd2d9d3b0e689a7d1";
const BASE = "https://tryhackme.com/api/v2";

const ENDPOINTS = {
  profile: `${BASE}/public-profile?username=${USERNAME}`,
  badges: `${BASE}/public-profile/badges?user=${USER_MONGO_ID}&limit=100`,
  rooms: `${BASE}/public-profile/completed-rooms?user=${USER_MONGO_ID}&limit=500`,
};

const __dirname = dirname(fileURLToPath(import.meta.url));
const OUTPUT = resolve(__dirname, "../data/thm.json");

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

/** Fetch one endpoint inside the page context, retrying while challenged. */
async function fetchEndpoint(page, name, url, { attempts = 5 } = {}) {
  for (let i = 1; i <= attempts; i++) {
    const result = await page.evaluate(async (u) => {
      try {
        const r = await fetch(u, { headers: { Accept: "application/json" } });
        const text = await r.text();
        let json = null;
        try {
          json = JSON.parse(text);
        } catch {
          /* challenge page -> not JSON */
        }
        return { status: r.status, json, snippet: text.slice(0, 100) };
      } catch (e) {
        return { status: 0, json: null, snippet: String(e) };
      }
    }, url);

    if (result.status === 200 && result.json?.status === "success") {
      return result.json.data ?? {};
    }

    console.warn(
      `  [${name}] attempt ${i}/${attempts} -> status=${result.status} ${result.snippet}`
    );
    await sleep(4000); // give the challenge time to settle, then retry
  }
  throw new Error(`Failed to fetch ${name} (${url}) after ${attempts} attempts`);
}

async function main() {
  console.log("Launching browser (residential IP needed to pass the challenge)...");
  const browser = await puppeteer.launch({
    headless: true,
    args: ["--no-sandbox", "--disable-blink-features=AutomationControlled"],
  });

  try {
    const page = await browser.newPage();
    await page.setUserAgent(
      "Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0"
    );

    // First navigation lets Chromium solve the Vercel challenge and get the cookie.
    console.log("Solving Vercel challenge...");
    await page.goto(ENDPOINTS.profile, {
      waitUntil: "domcontentloaded",
      timeout: 60000,
    });
    await sleep(6000);

    const data = {};
    for (const [name, url] of Object.entries(ENDPOINTS)) {
      console.log(`Fetching ${name}...`);
      data[name] = await fetchEndpoint(page, name, url);
    }

    data._fetchedAt = new Date().toISOString();

    await mkdir(dirname(OUTPUT), { recursive: true });
    await writeFile(OUTPUT, JSON.stringify(data, null, 2) + "\n", "utf-8");

    console.log("\nWrote", OUTPUT);
    console.log(
      `  profile: rank=${data.profile?.rank}, top=${data.profile?.topPercentage}%, streak=${data.profile?.streak}`
    );
    console.log(`  badges:  ${data.badges?.docs?.length ?? 0}`);
    console.log(`  rooms:   ${data.rooms?.docs?.length ?? 0}`);
    console.log("\nNext: git add scripts/data/thm.json && git commit && git push");
  } finally {
    await browser.close();
  }
}

main().catch((e) => {
  console.error("\nERROR:", e.message);
  process.exit(1);
});
