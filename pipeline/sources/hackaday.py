"""Hackaday.io contests (Hackaday Prize, Supercon add-on, themed challenges): HTML submission lists.

Contests are configured in events.toml under [[hackaday_contests]] (slug of /submissions/<slug>/list).
Winners aren't marked on lists; mark them via `winners = [project urls]` in config when known.
"""
from __future__ import annotations

import html
import re

from ..common import CACHE, TODAY, load_json, new_project, save_json, year_from
from ..http import fetch, log

BASE = "https://hackaday.io"
LIST_DIR = CACHE / "hackaday_lists"  # last good submission list per contest


def _num(pattern, chunk):
    m = re.search(pattern, chunk, re.S)
    if not m:
        return 0
    s = m.group(1).replace(",", "").lower()
    return int(float(s[:-1]) * 1000) if s.endswith("k") else int(s)


def submissions(slug: str, max_pages: int = 30) -> list[dict]:
    out, seen = [], set()
    for page in range(1, max_pages + 1):
        h = fetch(f"{BASE}/submissions/{slug}/list?page={page}")
        if not h:
            break
        new = 0
        for card in re.split(r'<div class="project-item\s*">', h)[1:]:
            href = re.search(r'<a href="(/project/\d+-[^"]+)" class="item-link">', card)
            if not href or href.group(1) in seen:
                continue
            seen.add(href.group(1))
            new += 1
            img = re.search(r"background-image: url\(([^)]*)\)", card)
            title = re.search(r'<h3 class="element-title">\s*<a [^>]*title="([^"]*)"', card)
            author = re.search(r'class="identity-card"[^>]*><a href="(/[^"]+)">(?:<img[^>]*>)?([^<]*)</a>', card)
            summary = re.search(r'<div class="project-item-title[^"]*">\s*(.*?)\s*</div>', card, re.S)
            out.append({
                "url": BASE + href.group(1),
                "title": html.unescape(title.group(1)) if title else href.group(1).split("-", 1)[-1],
                "author": html.unescape(author.group(2).strip()) if author else None,
                "image": (img.group(1).strip("'\"") if img else None),
                "summary": html.unescape(re.sub(r"<[^>]+>", "", summary.group(1))) if summary else "",
                "likes": _num(r'title="Likes">.*?</div>\s*([\d,.]+k?)', card),
                "followers": _num(r'title="Followers">.*?</div>\s*([\d,.]+k?)', card),
            })
        if new == 0:
            break
    return out


def discover(cfg_h: dict) -> list[dict]:
    """Auto-discover recent contests from /contests (newer than min_contest_id); cached."""
    from ..common import CACHE, load_json, save_json
    path = CACHE / "hackaday_contests.json"
    known = load_json(path, {})
    h = fetch(f"{BASE}/contests?page=1&sort=date") or ""
    for cid in dict.fromkeys(re.findall(r'href="/contest/(\d+-[^"/]+)"', h)):
        if int(cid.split("-")[0]) < cfg_h.get("min_contest_id", 10**9) or cid in known:
            continue
        page = fetch(f"{BASE}/contest/{cid}") or ""
        sub = re.search(r"/submissions/([^/\"]+)/list", page)
        title = re.search(r"<title>([^<|]+)", page)
        date = re.search(r"(20[12]\d)-\d\d-\d\d", page)
        if sub:
            known[cid] = {"slug": sub.group(1), "name": html.unescape(title.group(1)).strip() if title else cid,
                          "year": int(date.group(1)) if date else None}
    save_json(path, known)
    return [{"series_id": "hackaday-prize", "min_likes": cfg_h.get("min_likes", 0), **v} for v in known.values()]


def collect(series, cfg, editions):
    cfg_h = cfg.get("hackaday", {})
    contests = list(cfg.get("hackaday_contests", []))
    if cfg_h.get("auto_discover"):
        have = {c["slug"] for c in contests}
        contests += [c for c in discover(cfg_h) if c["slug"] not in have]
    out = []
    for c in contests:
        items = submissions(c["slug"], c.get("max_pages", 30))
        path = LIST_DIR / f"{c['slug']}.json"
        if items:
            save_json(path, {"fetched": TODAY, "items": items})
        elif (cached := load_json(path)) and cached.get("items"):
            # hackaday.io sometimes serves empty lists for a while (2026-11-22: 8 contests at once)
            items = cached["items"]
            log(f"  hackaday {c['name']}: empty list, keeping last good from {cached['fetched']}")
        min_likes = c.get("min_likes", cfg_h.get("min_likes", 0))
        winners = {u.rstrip("/"): a for u, a in (c.get("winners") or {}).items()}
        kept = [it for it in items if it["likes"] >= min_likes or it["url"].rstrip("/") in winners]
        log(f"  hackaday {c['name']}: {len(items)} entries, kept {len(kept)} (likes ≥ {min_likes})")
        year = c.get("year") or year_from(c["name"], c["slug"])
        eid = f"hackaday-{c['slug']}"
        editions.append({"id": eid, "series_id": c.get("series_id", "hackaday-prize"), "name": c["name"],
                         "year": year, "url": f"{BASE}/submissions/{c['slug']}/list", "state": "ended"})
        for it in kept:
            aw = winners.get(it["url"].rstrip("/"))
            out.append(new_project(
                id="hackaday:" + it["url"].rsplit("/project/", 1)[-1].split("-", 1)[0],
                title=it["title"], tagline=it["summary"], url=it["url"], source="hackaday",
                series_id=c.get("series_id", "hackaday-prize"), event_id=eid, event_name=c["name"], year=year,
                awards=[aw] if aw else [], winner=bool(aw), image=it["image"],
                team=[it["author"]] if it["author"] else [], likes=it["likes"],
            ))
    return out
