#!/usr/bin/env python3
"""Fetch TryHackMe public stats and generate Markdown snippets for the README."""

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

README_FILE = "README.md"

SECTIONS = {
    "stats": ("<!-- THM_STATS_START -->", "<!-- THM_STATS_END -->"),
    "badges": ("<!-- THM_BADGES_START -->", "<!-- THM_BADGES_END -->"),
    "rooms": ("<!-- THM_ROOMS_START -->", "<!-- THM_ROOMS_END -->"),
}


def fetch_json(url):
    """Fetch a URL and return parsed JSON, or None on failure."""
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
            if data.get("status") == "success":
                return data.get("data", {})
    except (URLError, HTTPError, json.JSONDecodeError, KeyError) as e:
        print(f"Warning: failed to fetch {url}: {e}", file=sys.stderr)
    return None


def build_stats(profile):
    """Build the stats table."""
    rank = profile.get("rank", "N/A") if profile else "N/A"
    top = profile.get("topPercentage", "N/A") if profile else "N/A"
    streak = profile.get("streak", "N/A") if profile else "N/A"

    rank_str = f"#{rank}" if isinstance(rank, int) else str(rank)
    top_str = f"{top}%" if isinstance(top, (int, float)) else str(top)
    streak_str = f"{streak} days" if isinstance(streak, int) else str(streak)

    lines = [
        "| Global Rank | Top | Streak |",
        "|-------------|-----|--------|",
        f"| {rank_str} | {top_str} | {streak_str} |",
    ]
    return "\n".join(lines)


def build_badges(badges):
    """Build the badges details block."""
    badge_docs = badges.get("docs", []) if badges else []
    badge_count = len(badge_docs)

    lines = [
        "<details>",
        f"<summary><b>TryHackMe Badges ({badge_count})</b></summary>",
        "<br>",
        "",
    ]

    if badge_docs:
        for b in badge_docs:
            title = b.get("title", "Unknown")
            desc = b.get("description", "")
            img = b.get("image", "")
            if img:
                entry = f'- <img src="{img}" width="20" height="20"> **{title}**'
            else:
                entry = f"- **{title}**"
            if desc:
                entry += f" — _{desc}_"
            lines.append(entry)
    else:
        lines.append("_No badges available_")

    lines.append("")
    lines.append("</details>")
    return "\n".join(lines)


def build_rooms(rooms):
    """Build the completed rooms details block."""
    room_docs = rooms.get("docs", []) if rooms else []
    room_count = len(room_docs)

    lines = [
        "<details>",
        f"<summary><b>TryHackMe Completed Rooms ({room_count})</b></summary>",
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
    """Replace content between start_tag and end_tag."""
    pattern = re.compile(
        rf"({re.escape(start_tag)})\n.*?\n({re.escape(end_tag)})",
        re.DOTALL,
    )
    if not pattern.search(content):
        print(f"Warning: markers {start_tag} / {end_tag} not found in {README_FILE}", file=sys.stderr)
        return content
    return pattern.sub(rf"\1\n{snippet}\n\2", content)


def main():
    print("Fetching TryHackMe profile...")
    profile = fetch_json(PROFILE_URL)

    print("Fetching badges...")
    badges = fetch_json(BADGES_URL)

    print("Fetching completed rooms...")
    rooms = fetch_json(ROOMS_URL)

    snippets = {
        "stats": build_stats(profile),
        "badges": build_badges(badges),
        "rooms": build_rooms(rooms),
    }

    if not os.path.exists(README_FILE):
        print(f"Error: {README_FILE} not found", file=sys.stderr)
        sys.exit(1)

    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    for section, (start_tag, end_tag) in SECTIONS.items():
        content = inject_section(content, start_tag, end_tag, snippets[section])

    with open(README_FILE, "r", encoding="utf-8") as f:
        original = f.read()

    if content == original:
        print("No changes detected, README is up to date.")
    else:
        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("README.md updated successfully.")


if __name__ == "__main__":
    main()
