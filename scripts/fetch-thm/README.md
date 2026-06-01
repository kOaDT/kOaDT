# fetch-thm

Local-only tool that fetches TryHackMe data and writes
[`../data/thm.json`](../data/thm.json), which the CI README generator reads.

## Why it can't run in CI

TryHackMe's API is behind **Vercel's Attack Challenge Mode** (`x-vercel-mitigated:
challenge`, HTTP 429). A real browser solves the JS challenge transparently, but
only from a **trusted residential IP**. GitHub Actions runners use datacenter
(Azure) IPs that the challenge blocks — verified: the exact same headless
Chromium returns `200` from a home connection and `429` from a runner. So the
fetch must run on your machine; the result is committed and CI consumes it.

## Process

```bash
cd scripts/fetch-thm
npm install          # first time only (downloads a Chromium)
npm run fetch        # writes ../data/thm.json

cd ../..
git add scripts/data/thm.json
git commit -m "chore: refresh THM data"
git push             # triggers the Update README workflow
```

Pushing `scripts/data/thm.json` triggers
[`update-readme.yml`](../../.github/workflows/update-readme.yml), which
regenerates the README from the committed data plus the private portfolio data.
