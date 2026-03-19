#!/usr/bin/env python3
"""Fetch TryHackMe stats and portfolio data, then generate Markdown for the README."""

import json
import os
import re
import sys
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

USERNAME = "kOaDT"
USER_MONGO_ID = "656836cbd2d9d3b0e689a7d1"

BASE = "https://tryhackme.com/api/v2"
PROFILE_URL = f"{BASE}/public-profile?username={USERNAME}"
BADGES_URL = f"{BASE}/public-profile/badges?user={USER_MONGO_ID}&limit=100"
ROOMS_URL = f"{BASE}/public-profile/completed-rooms?user={USER_MONGO_ID}&limit=500"

PRIVATE_REPO = "kOaDT/portfolio-cyber"
DATA_PATH = "src/data"

README_FILE = "README.md"

SECTIONS = {
    "stats": ("<!-- THM_STATS_START -->", "<!-- THM_STATS_END -->"),
    "projects": ("<!-- PROJECTS_START -->", "<!-- PROJECTS_END -->"),
    "cve_discoveries": ("<!-- CVE_DISCOVERIES_START -->", "<!-- CVE_DISCOVERIES_END -->"),
    "poc_cve": ("<!-- POC_CVE_START -->", "<!-- POC_CVE_END -->"),
    "oss": ("<!-- OSS_START -->", "<!-- OSS_END -->"),
    "certifications": ("<!-- CERTIFICATIONS_START -->", "<!-- CERTIFICATIONS_END -->"),
    "certificates": ("<!-- CERTIFICATES_START -->", "<!-- CERTIFICATES_END -->"),
    "badges": ("<!-- THM_BADGES_START -->", "<!-- THM_BADGES_END -->"),
    "rooms": ("<!-- THM_ROOMS_START -->", "<!-- THM_ROOMS_END -->"),
}


def fetch_thm_json(url):
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
            if data.get("status") == "success":
                return data.get("data", {})
    except (URLError, HTTPError, json.JSONDecodeError, KeyError) as e:
        print(f"Warning: failed to fetch {url}: {e}", file=sys.stderr)
    return None


def fetch_private_json(filename):
    token = os.environ.get("PORTFOLIO_TOKEN", "")
    if not token:
        print(f"Warning: PORTFOLIO_TOKEN not set, skipping {filename}", file=sys.stderr)
        return None

    url = f"https://raw.githubusercontent.com/{PRIVATE_REPO}/main/{DATA_PATH}/{filename}"
    try:
        req = Request(url, headers={
            "Authorization": f"token {token}",
            "User-Agent": "Mozilla/5.0",
        })
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except (URLError, HTTPError, json.JSONDecodeError) as e:
        print(f"Warning: failed to fetch {filename}: {e}", file=sys.stderr)
    return None


def fmt(value):
    return str(value) if value else "-"


def build_stats(profile):
    rank = profile.get("rank", "N/A") if profile else "N/A"
    top = profile.get("topPercentage", "N/A") if profile else "N/A"
    streak = profile.get("streak", "N/A") if profile else "N/A"

    rank_str = f"#{rank}" if isinstance(rank, int) else str(rank)
    top_str = f"{top}%" if isinstance(top, (int, float)) else str(top)
    streak_str = f"{streak} days" if isinstance(streak, int) else str(streak)

    return "\n".join([
        "| Global Rank | Top | Streak |",
        "|-------------|-----|--------|",
        f"| {rank_str} | {top_str} | {streak_str} |",
    ])


def build_projects(data):
    if not data:
        return ""
    repos = data.get("repos", [])
    if not repos:
        return ""

    repos.sort(key=lambda r: (
        -r.get("stargazers_count", 0),
        -r.get("views_total", 0),
    ))

    lines = [
        "<br>",
        "",
        "### Projects",
        "",
        "| Project | Description | ⭐ | 🍴 | 👁️ | 📥 |",
        "|:--------|:------------|---:|---:|----:|---:|",
    ]
    for r in repos:
        name = r.get("name", "")
        desc = r.get("description", "") or ""
        url = r.get("html_url", "")
        link = f"[**{name}**]({url})" if url else f"**{name}**"
        lines.append(
            f"| {link} | {desc} "
            f"| {fmt(r.get('stargazers_count', 0))} "
            f"| {fmt(r.get('forks_count', 0))} "
            f"| {fmt(r.get('views_total', 0))} "
            f"| {fmt(r.get('clones_total', 0))} |"
        )
    return "\n".join(lines)


def build_cve_discoveries(data):
    if not data:
        return ""
    items = data.get("items", [])
    if not items:
        return ""

    lines = [
        "<br>",
        "",
        "### CVE Discoveries",
        "",
        "| CVE | Score | Date | Description |",
        "|:----|:------|:-----|:------------|",
    ]
    for item in items:
        cve_id = item.get("cveId", "")
        desc = item.get("description", "")
        cvss = item.get("cvss")
        published = item.get("published", "")
        refs = item.get("references", [])
        advisory = next((r["url"] for r in refs if "advisories" in r.get("url", "")), "")
        if not advisory and refs:
            advisory = refs[0].get("url", "")
        cve_link = f"[{cve_id}]({advisory})" if advisory else cve_id
        cvss_str = f"{cvss:.1f}" if isinstance(cvss, (int, float)) else str(cvss or "")
        date_str = published[:10] if published else ""
        lines.append(f"| {cve_link} | {cvss_str} | {date_str} | {desc} |")
    return "\n".join(lines)


def extract_cve_id(repo_name):
    match = re.search(r"(cve-\d{4}-\d+)", repo_name, re.IGNORECASE)
    return match.group(1).upper() if match else repo_name


def build_poc_cve(data):
    if not data:
        return ""
    repos = data.get("repos", [])
    if not repos:
        return ""

    repos.sort(key=lambda r: -r.get("stargazers_count", 0))

    lines = [
        "<br>",
        "",
        "### CVE Proof of Concepts",
        "",
        "| CVE | Description | ⭐ | 🍴 | 👁️ | 📥 |",
        "|:----|:------------|---:|---:|----:|---:|",
    ]
    for r in repos:
        cve_id = extract_cve_id(r.get("name", ""))
        desc = r.get("description", "") or ""
        url = r.get("html_url", "")
        link = f"[**{cve_id}**]({url})" if url else f"**{cve_id}**"
        lines.append(
            f"| {link} | {desc} "
            f"| {fmt(r.get('stargazers_count', 0))} "
            f"| {fmt(r.get('forks_count', 0))} "
            f"| {fmt(r.get('views_total', 0))} "
            f"| {fmt(r.get('clones_total', 0))} |"
        )
    return "\n".join(lines)


def build_oss(data):
    if not data:
        return ""
    items = data.get("items", [])
    if not items:
        return ""

    items.sort(key=lambda x: (-x.get("isFeatured", 0), -x.get("stars", 0)))

    lines = [
        "<details>",
        f"<summary><b>OSS Contributions ({len(items)})</b></summary>",
        "<br>",
        "",
        "| Repository | Description | ⭐ | 🍴 |",
        "|:-----------|:------------|---:|---:|",
    ]
    for item in items:
        owner = item.get("repoOwner", "")
        name = item.get("repoName", "")
        desc = item.get("description", "") or ""
        stars = fmt(item.get("stars", 0))
        forks = fmt(item.get("forks", 0))
        repo_url = f"https://github.com/{owner}/{name}"
        link = f"[**{owner}/{name}**]({repo_url})"
        lines.append(f"| {link} | {desc} | {stars} | {forks} |")
    lines.append("")
    lines.append("</details>")
    return "\n".join(lines)


def build_certifications(data):
    if not data:
        return ""
    items = data.get("items", [])
    if not items:
        return ""

    lines = [
        "<br>",
        "",
        "### Certifications",
        "",
        "| Certification | Date |",
        "|:--------------|:-----|",
    ]
    for item in items:
        name = item.get("name", "")
        date = item.get("date", "")
        link = item.get("link", "")
        cert_link = f"[{name}]({link})" if link else name
        lines.append(f"| {cert_link} | {date} |")
    return "\n".join(lines)


def build_certificates(data):
    if not data:
        return ""
    items = data.get("items", [])
    if not items:
        return ""

    lines = [
        "<details>",
        f"<summary><b>Certificates ({len(items)})</b></summary>",
        "<br>",
        "",
    ]
    for item in items:
        name = item.get("name", "")
        date = item.get("date", "")
        link = item.get("link", "")
        cert_link = f"[{name}]({link})" if link else name
        lines.append(f"- {cert_link} — _{date}_")
    lines.append("")
    lines.append("</details>")
    return "\n".join(lines)


def build_badges(badges):
    badge_docs = badges.get("docs", []) if badges else []

    lines = [
        "<details>",
        f"<summary><b>TryHackMe Badges ({len(badge_docs)})</b></summary>",
        "<br>",
        "",
    ]
    if badge_docs:
        for b in badge_docs:
            title = b.get("title", "Unknown")
            desc = b.get("description", "")
            img = b.get("image", "")
            entry = f'- <img src="{img}" width="20" height="20"> **{title}**' if img else f"- **{title}**"
            if desc:
                entry += f" — _{desc}_"
            lines.append(entry)
    else:
        lines.append("_No badges available_")
    lines.append("")
    lines.append("</details>")
    return "\n".join(lines)


def build_rooms(rooms):
    room_docs = rooms.get("docs", []) if rooms else []

    lines = [
        "<details>",
        f"<summary><b>TryHackMe Completed Rooms ({len(room_docs)})</b></summary>",
        "<br>",
        "",
    ]
    if room_docs:
        lines.append("| # | Room | Difficulty |")
        lines.append("|---|------|------------|")
        for i, r in enumerate(room_docs, 1):
            title = r.get("title", "Unknown")
            code = r.get("code", "")
            difficulty = r.get("difficulty", "N/A")
            room_link = f"[{title}](https://tryhackme.com/room/{code})" if code else title
            lines.append(f"| {i} | {room_link} | {difficulty} |")
    else:
        lines.append("_No rooms available_")
    lines.append("")
    lines.append("</details>")
    return "\n".join(lines)


def inject_section(content, start_tag, end_tag, snippet):
    pattern = re.compile(
        rf"({re.escape(start_tag)})\n.*?\n({re.escape(end_tag)})",
        re.DOTALL,
    )
    if not pattern.search(content):
        print(f"Warning: markers {start_tag} / {end_tag} not found in {README_FILE}", file=sys.stderr)
        return content
    return pattern.sub(rf"\1\n{snippet}\n\2", content)


def main():
    print("Fetching TryHackMe data...")
    profile = fetch_thm_json(PROFILE_URL)
    badges = fetch_thm_json(BADGES_URL)
    rooms = fetch_thm_json(ROOMS_URL)

    print("Fetching portfolio data...")
    github_repos = fetch_private_json("github-repos.json")
    cve_discoveries = fetch_private_json("cve-discoveries.json")
    poc_cve = fetch_private_json("poc-cve-repos.json")
    oss_contributions = fetch_private_json("oss-contributions.json")
    certifications = fetch_private_json("certifications.json")
    certificates = fetch_private_json("certificates.json")

    snippets = {
        "stats": build_stats(profile),
        "projects": build_projects(github_repos) if github_repos is not None else None,
        "cve_discoveries": build_cve_discoveries(cve_discoveries) if cve_discoveries is not None else None,
        "poc_cve": build_poc_cve(poc_cve) if poc_cve is not None else None,
        "oss": build_oss(oss_contributions) if oss_contributions is not None else None,
        "certifications": build_certifications(certifications) if certifications is not None else None,
        "certificates": build_certificates(certificates) if certificates is not None else None,
        "badges": build_badges(badges),
        "rooms": build_rooms(rooms),
    }

    if not os.path.exists(README_FILE):
        print(f"Error: {README_FILE} not found", file=sys.stderr)
        sys.exit(1)

    with open(README_FILE, "r", encoding="utf-8") as f:
        original = f.read()

    content = original
    for section, (start_tag, end_tag) in SECTIONS.items():
        if snippets[section] is None:
            print(f"Skipping {section} (no data available)")
            continue
        content = inject_section(content, start_tag, end_tag, snippets[section])

    if content == original:
        print("No changes detected, README is up to date.")
    else:
        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("README.md updated successfully.")


if __name__ == "__main__":
    main()
