#!/usr/bin/env python3
"""Render vault markdown from data/entries.json. JSON is canonical."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENTRIES = json.loads((ROOT / "data" / "entries.json").read_text(encoding="utf-8"))

SLUG = {
    "Việt Nam": "viet-nam",
    "Hà Nội": "ha-noi",
    "Đà Nẵng": "da-nang",
    "Hội An": "hoi-an",
}

LANE_ORDER = ["eat", "drink", "restaurant", "play", "do", "stay", "see", "shop"]


def slug(name: str) -> str:
    return SLUG.get(name, name.lower().replace(" ", "-"))


def md_entry(e: dict) -> str:
    tags = ", ".join(e.get("tags") or [])
    context = ", ".join(e.get("context") or [])
    sources = e.get("sources") or []
    src_lines = "\n".join(f"  - {s}" for s in sources) if sources else "  -"
    return "\n".join(
        [
            f"## {e['title']}",
            "",
            f"- id: `{e['id']}`",
            f"- status: {e.get('status') or 'want'}",
            f"- priority: {e.get('priority') or 'someday'}",
            f"- lane: {e['lane']}",
            f"- category: {e.get('category') or ''}",
            f"- city: {e['city']}",
            f"- country: {e['country']}",
            f"- area: {e.get('area') or ''}",
            f"- location: {e.get('location') or ''}",
            f"- maps: {e.get('maps') or ''}",
            f"- price: {e.get('price') or ''}",
            f"- tags: {tags}",
            f"- context: {context}",
            "- sources:",
            src_lines,
            f"- notes: {e.get('notes') or ''}",
            f"- caveats: {e.get('caveats') or ''}",
            f"- added: {e.get('added') or ''}",
            f"- updated: {e.get('updated') or ''}",
            "",
        ]
    )


def render_lane(city: str, lane: str, items: list[dict]) -> str:
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for e in items:
        by_cat[e.get("category") or "Ungrouped"].append(e)
    counts = " · ".join(f"{cat} ({len(v)})" for cat, v in sorted(by_cat.items()))
    parts = [f"# {city} — {lane}", "", f"Categories: {counts}", ""]
    for cat in sorted(by_cat):
        parts.append(f"### {cat}")
        parts.append("")
        for e in sorted(by_cat[cat], key=lambda x: x["title"].lower()):
            parts.append(md_entry(e))
    return "\n".join(parts).rstrip() + "\n"


def render_index(entries: list[dict]) -> str:
    cities: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for e in entries:
        cities[(e["country"], e["city"])].append(e)
    lines = [
        "# Atlas index",
        "",
        "`data/entries.json` is canonical. This file is a generated view.",
        "",
        f"Total entries: **{len(entries)}**",
        "",
        "| country | city | want | been | skip | next | files |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for country, city in sorted(cities, key=lambda x: (x[0], x[1])):
        items = cities[(country, city)]
        want = sum(1 for e in items if e.get("status") == "want")
        been = sum(1 for e in items if e.get("status") == "been")
        skip = sum(1 for e in items if e.get("status") == "skip")
        nxt = sum(1 for e in items if e.get("priority") == "next")
        lanes = sorted({e["lane"] for e in items}, key=lambda l: LANE_ORDER.index(l) if l in LANE_ORDER else 99)
        files = ", ".join(
            f"[`{lane}.md`](./{slug(country)}/{slug(city)}/{lane}.md)" for lane in lanes
        )
        lines.append(
            f"| {country} | {city} | {want} | {been} | {skip} | {nxt} | {files} |"
        )
    lines += [
        "",
        "## Home city",
        "",
        "Đà Nẵng is home base. Ask: *what's next in Đà Nẵng this week?*",
        "",
        "## How to query",
        "",
        "- `what's good in {city}` — read filed entries first",
        "- `file this` + links — clerk extracts and upserts",
        "- `mark {id} been` — status only, never overwrite been/skip with want",
        "- `next in Đà Nẵng` — priority=next + context=home",
        "",
    ]
    return "\n".join(lines)


def render_next(entries: list[dict]) -> str:
    nxt = [e for e in entries if e.get("priority") == "next" and e.get("status") == "want"]
    lines = [
        "# Next",
        "",
        "Want-list items marked `priority: next`. Generated from JSON.",
        "",
    ]
    if not nxt:
        lines.append("_Nothing queued. Say `next: {id}` to promote one._")
        lines.append("")
        return "\n".join(lines)
    by_city: dict[str, list[dict]] = defaultdict(list)
    for e in nxt:
        by_city[e["city"]].append(e)
    for city in sorted(by_city):
        lines.append(f"## {city}")
        lines.append("")
        for e in sorted(by_city[city], key=lambda x: (x["lane"], x["title"].lower())):
            loc = e.get("location") or ""
            extra = f" — {loc}" if loc else ""
            lines.append(f"- `{e['id']}` · {e['lane']} · **{e['title']}**{extra}")
        lines.append("")
    return "\n".join(lines)


def render_home(entries: list[dict]) -> str:
    home = [e for e in entries if e.get("city") == "Đà Nẵng"]
    lines = [
        "# Đà Nẵng — home base",
        "",
        "Living here. Prefer filing new Đà Nẵng eat / drink / do / stay before more travel lists.",
        "",
        f"Filed so far: **{len(home)}** entries.",
        "",
        "| lane | title | status | priority |",
        "|---|---|---|---|",
    ]
    for e in sorted(home, key=lambda x: (LANE_ORDER.index(x["lane"]) if x["lane"] in LANE_ORDER else 99, x["title"])):
        lines.append(f"| {e['lane']} | {e['title']} | {e['status']} | {e['priority']} |")
    lines += [
        "",
        "Missing lanes: eat, drink, restaurant, do, stay. Drop a Maps pin or a Reels/Threads link and file them.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    grouped: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    for e in ENTRIES:
        grouped[(e["country"], e["city"], e["lane"])].append(e)

    vault = ROOT / "vault"
    for (country, city, lane), items in grouped.items():
        dest = vault / slug(country) / slug(city) / f"{lane}.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render_lane(city, lane, items), encoding="utf-8")

    (vault / "INDEX.md").write_text(render_index(ENTRIES), encoding="utf-8")
    (vault / "_next.md").write_text(render_next(ENTRIES), encoding="utf-8")
    home_dir = vault / slug("Việt Nam") / slug("Đà Nẵng")
    home_dir.mkdir(parents=True, exist_ok=True)
    (home_dir / "README.md").write_text(render_home(ENTRIES), encoding="utf-8")
    print(f"rendered {len(ENTRIES)} entries")


if __name__ == "__main__":
    main()
