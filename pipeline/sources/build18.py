"""Build18 Garage (CMU ECE): full list is embedded in the Next.js RSC payload of /garage."""
from __future__ import annotations

import html
import json
import re

from ..common import CACHE, TODAY, clip, load_json, new_project, save_json
from ..http import fetch, log

BASE = "https://www.build18.org"
DESC_CACHE = CACHE / "build18_desc.json"


def _next_flight(page: str) -> str:
    chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)</script>', page, re.S)
    return "".join(json.loads('"' + c + '"') for c in chunks)


def _description(pid: str, cache: dict) -> str:
    if pid in cache:
        return cache[pid]
    h = fetch(f"{BASE}/garage/{pid}") or ""
    m = re.search(r'<div class="grid max-w-\[62ch\][^"]*">(.*?)</div>', h, re.S)
    paras = re.findall(r"<p[^>]*>(.*?)</p>", m.group(1), re.S) if m else []
    txt = "\n".join(html.unescape(re.sub(r"<[^>]+>", "", x)).strip() for x in paras)
    cache[pid] = clip(txt, 1500)
    return cache[pid]


def collect(series, cfg, editions):
    page = fetch(f"{BASE}/garage")
    if not page:
        return []
    rsc = _next_flight(page)
    i = rsc.find('{"projects":')
    if i < 0:
        log("  build18: projects payload not found (site layout changed?)")
        return []
    obj, _ = json.JSONDecoder().raw_decode(rsc, i)
    cache = load_json(DESC_CACHE, {})
    out, years = [], {}
    for p in obj["projects"]:
        award = p.get("award")
        award = None if not award or award == "$undefined" else award
        year = p.get("year")
        years[year] = years.get(year, 0) + 1
        img = (p.get("image") or {}).get("src")
        out.append(new_project(
            id=f"build18:{p['id']}", title=p["title"], tagline="",
            description=_description(p["id"], cache),
            url=f"{BASE}/garage/{p['id']}", source="build18",
            series_id="build18", event_id=f"build18-{year}", event_name=f"Build18 {year}", year=year,
            awards=[award] if award else [], winner=bool(award),
            image=(BASE + img) if img and img.startswith("/") else img,
            team=p.get("team") or [],
        ))
    save_json(DESC_CACHE, cache)
    for y in sorted(years, reverse=True):
        editions.append({"id": f"build18-{y}", "series_id": "build18", "name": f"Build18 {y}", "year": y,
                         "url": f"{BASE}/garage", "dates": f"{y}-01", "state": "ended"})
    return out
