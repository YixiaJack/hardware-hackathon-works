"""Devpost collector.

Three entry points:
  * discover_editions(series)  – find every edition of a hackathon series via /api/hackathons
  * collect_edition(edition)   – scrape the public project gallery (+ JSON-LD awards)
  * collect_stream(queries)    – newest hardware projects across ALL of Devpost (search.json)
Detail pages (built-with tags, repo link, video, story) are cached per slug in
data/cache/devpost/ so each run only fetches what is new.
"""
from __future__ import annotations

import html
import json
import re
import urllib.parse

from ..common import CACHE, TODAY, clip, load_json, new_project, save_json, strip_html, year_from
from ..http import fetch, fetch_json, log

API = "https://devpost.com/api/hackathons"
DETAIL_DIR = CACHE / "devpost"
DETAIL_TTL_DAYS = 45  # likes/awards rarely change after judging; refresh occasionally


# ───────────────────────────── editions ─────────────────────────────

def discover_editions(series: dict, max_pages: int = 5) -> list[dict]:
    """Return Devpost editions whose title matches series['devpost_title_regex'].

    Devpost's `search` is effectively single-word (multi-word = fuzzy OR), so `devpost_search`
    may be a list of terms; results are always filtered by the title regex.
    """
    terms = series.get("devpost_search") or []
    terms = [terms] if isinstance(terms, str) else terms
    rx = re.compile(series.get("devpost_title_regex") or "|".join(map(re.escape, terms)) or "^$", re.I)
    out, seen = [], set()
    for q in terms:
        for page in range(1, max_pages + 1):
            d = fetch_json(f"{API}?search={urllib.parse.quote(q)}&per_page=40&page={page}")
            items = (d or {}).get("hackathons") or []
            for h in items:
                if not rx.search(h.get("title", "").strip()) or h["id"] in seen:
                    continue
                seen.add(h["id"])
                out.append(_edition_from_api(series, h))
            if len(items) < 40:
                break
    # explicit extra galleries listed in config (renamed / oddly-titled editions)
    for g in series.get("devpost_galleries", []):
        if not any(e["gallery_url"] == g for e in out):
            sub = urllib.parse.urlparse(g).netloc.split(".")[0]
            out.append({
                "id": f"{series['id']}-{year_from(sub) or sub}",
                "series_id": series["id"], "name": f"{series['name']} {year_from(sub) or ''}".strip(),
                "year": year_from(sub), "url": f"https://{sub}.devpost.com/", "gallery_url": g,
                "dates": None, "registrations": None, "state": "ended", "thumbnail": None,
            })
    # disambiguate two editions in the same year (e.g. spring + fall)
    ids = {}
    for e in out:
        ids.setdefault(e["id"], []).append(e)
    for dup in (v for v in ids.values() if len(v) > 1):
        for e in dup[1:]:
            e["id"] = f"{e['id']}-{e.get('devpost_id') or urllib.parse.urlparse(e['url']).netloc.split('.')[0]}"
    return out


def _edition_from_api(series: dict, h: dict) -> dict:
    dates = h.get("submission_period_dates") or ""
    ys = re.findall(r"20[1-3]\d", dates)
    year = year_from(h.get("title")) or (int(ys[-1]) if ys else None)
    thumb = h.get("thumbnail_url")
    if thumb and thumb.startswith("//"):
        thumb = "https:" + thumb
    return {
        "id": f"{series['id']}-{year or h['id']}",
        "series_id": series["id"],
        "name": h.get("title"),
        "year": year,
        "url": h.get("url"),
        "gallery_url": h.get("submission_gallery_url") or (h.get("url", "").rstrip("/") + "/project-gallery"),
        "dates": h.get("submission_period_dates"),
        "registrations": h.get("registrations_count"),
        "state": h.get("open_state"),
        "winners_announced": h.get("winners_announced"),
        "thumbnail": thumb,
        "devpost_id": h.get("id"),
    }


# ───────────────────────────── gallery ─────────────────────────────

_ITEM_SPLIT = re.compile(r'<div class="[^"]*gallery-item[^"]*" data-software-id="(\d+)">')


def scrape_gallery(gallery_url: str, max_pages: int = 40) -> list[dict]:
    tiles = []
    for page in range(1, max_pages + 1):
        h = fetch(f"{gallery_url}?page={page}")
        if not h:
            break
        parts = _ITEM_SPLIT.split(h)
        if len(parts) < 3:
            break
        for i in range(1, len(parts), 2):
            tiles.append(_parse_tile(parts[i], parts[i + 1]))
        if (len(parts) - 1) // 2 < 24:  # Devpost shows 24 per page
            break
    return tiles


def _parse_tile(sid: str, chunk: str) -> dict:
    def grab(pat, default=""):
        m = re.search(pat, chunk, re.S)
        return html.unescape(m.group(1).strip()) if m else default

    awards = []
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', chunk, re.S)
    if m:
        try:
            ld = json.loads(m.group(1))
            for a in ld.get("award", []) or []:
                a = re.sub(r"^Winner,\s*", "", a)
                a = re.sub(r"\s+—\s+.*$", "", a)  # drop " — Event Name"
                awards.append(a.strip())
        except json.JSONDecodeError:
            pass
    img = grab(r'class="software_thumbnail_image[^"]*"[^>]*src="([^"]+)"')
    if "thumbnail-placeholder" in img:
        img = ""
    return {
        "software_id": sid,
        "url": grab(r'href="(https://devpost\.com/software/[^"]+)"'),
        "title": strip_html(grab(r"<h5>(.*?)</h5>")),
        "tagline": strip_html(grab(r'<p class="small tagline">(.*?)</p>')),
        "image": img or None,
        "winner": 'class="winner"' in chunk or bool(awards),
        "awards": awards,
        "likes": int(grab(r'data-count="like">.*?</i>\s*(\d+)', "0") or 0),
        "comments": int(grab(r'data-count="comment">.*?</i>\s*(\d+)', "0") or 0),
    }


# ───────────────────────────── detail ─────────────────────────────

def _slug(url: str) -> str:
    return url.rstrip("/").rsplit("/", 1)[-1]


def fetch_detail(url: str, *, force: bool = False) -> dict | None:
    slug = _slug(url)
    path = DETAIL_DIR / f"{slug}.json"
    cached = load_json(path)
    if cached and not force:
        age_ok = cached.get("fetched", "") >= _days_ago(DETAIL_TTL_DAYS)
        if age_ok or cached.get("gone"):
            return None if cached.get("gone") else cached
    h = fetch(url)
    if h is None:
        if cached:
            return cached
        save_json(path, {"slug": slug, "gone": True, "fetched": TODAY})
        return None
    d = parse_detail(h)
    d.update({"slug": slug, "fetched": TODAY})
    save_json(path, d)
    return d


def parse_detail(h: str) -> dict:
    built = [html.unescape(t) for t in re.findall(r'<span class="cp-tag[^"]*">(?:<a [^>]+>)?([^<]+)', h)]
    links = re.findall(r'<ul data-role="software-urls"[^>]*>(.*?)</ul>', h, re.S)
    link_list = re.findall(r'href="([^"]+)"', links[0]) if links else []
    repo = next((u for u in link_list if "github.com/" in u or "gitlab.com/" in u), None)
    video = None
    m = re.search(r"(?:youtube\.com/embed/|youtube-nocookie\.com/embed/)([\w-]{6,})", h)
    if m:
        video = f"https://www.youtube.com/watch?v={m.group(1)}"
    else:
        m = re.search(r"player\.vimeo\.com/video/(\d+)", h)
        if m:
            video = f"https://vimeo.com/{m.group(1)}"
    og = re.search(r'<meta property="og:image" content="([^"]+)"', h)
    # story text: between the media gallery and "Built With"
    story = ""
    a = h.find('id="app-details-left"')
    b = h.find('id="built-with"')
    if a != -1:
        seg = h[a: b if b > a else a + 60000]
        g = seg.find('id="gallery"')
        if g != -1:
            end = seg.find("</ul>", g)
            seg = seg[:g] + seg[end + 5:] if end != -1 else seg
        story = strip_html(seg.split(">", 1)[-1])
    # submissions & awards per event
    subs = []
    s0 = h.find('id="submissions"')
    if s0 != -1:
        s1 = h.find("</section>", s0)
        block = h[s0: s1 if s1 > s0 else s0 + 20000]
        for li in re.split(r'<div class="software-list-content">', block)[1:]:
            ev = re.search(r'<a href="(https://[^"]+)">([^<]+)</a>', li)
            prizes = [strip_html(p) for p in re.findall(r'all-caps">Winner</span>(.*?)</li>', li, re.S)]
            if ev:
                subs.append({"url": ev.group(1), "name": html.unescape(ev.group(2).strip()), "awards": prizes})
    team = list(dict.fromkeys(
        html.unescape(n.strip()) for n in re.findall(r'<a class="user-profile-link" href="https://devpost\.com/[^"]+">([^<]+)</a>', h)
    ))
    likes = re.search(r'<span class="side-count">(\d+)</span>', h)
    tagline = re.search(r'<p class="large">\s*(.*?)\s*</p>', h, re.S)
    title = re.search(r'<h1[^>]*id="app-title"[^>]*>(.*?)</h1>', h, re.S)
    return {
        "title": strip_html(title.group(1)) if title else None,
        "tagline": strip_html(tagline.group(1)) if tagline else None,
        "built_with": [t.strip().lower() for t in built if t.strip()],
        "links": link_list[:8],
        "repo": repo,
        "video": video,
        "image": og.group(1) if og else None,
        "story": clip(story, 1500),
        "submissions": subs,
        "team": team[:8],
        "likes": int(likes.group(1)) if likes else None,
    }


def _days_ago(n: int) -> str:
    import datetime as dt
    return (dt.date.today() - dt.timedelta(days=n)).isoformat()


# ───────────────────────────── assemble ─────────────────────────────

def tile_to_project(tile: dict, edition: dict | None, detail: dict | None) -> dict:
    d = detail or {}
    awards = tile.get("awards") or []
    if not awards and d.get("submissions") and edition:
        for s in d["submissions"]:
            if edition.get("url") and s["url"].rstrip("/") == edition["url"].rstrip("/"):
                awards = s["awards"]
    img = tile.get("image") or d.get("image")
    if img and "medium.jpg" not in img and "/datas/small" in img:
        img = img.replace("/datas/small", "/datas/medium")
    return new_project(
        id=f"devpost:{_slug(tile['url'])}",
        title=tile.get("title") or d.get("title") or _slug(tile["url"]),
        tagline=tile.get("tagline") or d.get("tagline") or "",
        description=d.get("story", ""),
        url=tile["url"],
        source="devpost",
        event_id=edition and edition["id"],
        series_id=edition and edition["series_id"],
        event_name=edition and edition["name"],
        year=(edition and edition.get("year")) or None,
        awards=awards,
        winner=bool(tile.get("winner") or awards),
        image=img,
        video=d.get("video"),
        repo=d.get("repo"),
        links=d.get("links", []),
        team=d.get("team", []),
        built_with=d.get("built_with", []),
        likes=max(tile.get("likes") or 0, d.get("likes") or 0),
        comments=tile.get("comments") or 0,
    )


GALLERY_DIR = CACHE / "devpost_galleries"


def _gallery_ttl(edition: dict) -> int:
    """Recent editions are re-scraped often (judging/likes still moving); old ones rarely."""
    import datetime as dt
    y = edition.get("year") or 0
    if edition.get("state") == "open" or y >= dt.date.today().year:
        return 2
    if y == dt.date.today().year - 1:
        return 14
    return 90


def collect_edition(edition: dict, *, want_detail) -> list[dict]:
    """Scrape one edition. `want_detail(tile)` decides whether to fetch the detail page."""
    path = GALLERY_DIR / f"{edition['id']}.json"
    cached = load_json(path)
    if cached and cached.get("fetched", "") >= _days_ago(_gallery_ttl(edition)):
        tiles = cached["tiles"]
    else:
        tiles = scrape_gallery(edition["gallery_url"])
        if tiles or not cached:
            save_json(path, {"fetched": TODAY, "edition": edition["name"], "tiles": tiles})
        else:
            tiles = cached["tiles"]  # transient failure → keep last good gallery
        log(f"  devpost {edition['name']}: {len(tiles)} projects (fresh)")
    out = []
    for t in tiles:
        if not t.get("url"):
            continue
        det = fetch_detail(t["url"]) if want_detail(t) else load_json(DETAIL_DIR / f"{_slug(t['url'])}.json")
        out.append(tile_to_project(t, edition, det))
    return out


def collect_stream(queries: list[str], pages: int, *, min_likes: int, resolve_event) -> list[dict]:
    """Newest-first hardware stream across all Devpost (search.json default order = newest)."""
    out, seen = [], set()
    for q in queries:
        for page in range(1, pages + 1):
            d = fetch_json(f"https://devpost.com/software/search.json?query={urllib.parse.quote(q)}&page={page}")
            items = (d or {}).get("software") or []
            for s in items:
                if s["url"] in seen:
                    continue
                seen.add(s["url"])
                if not (s.get("winner") or (s.get("like_count") or 0) >= min_likes):
                    continue
                det = fetch_detail(s["url"])
                if not det:
                    continue
                ed, awards = resolve_event(det.get("submissions", []))
                tile = {
                    "url": s["url"], "title": s.get("name"), "tagline": s.get("tagline"),
                    "image": (s.get("photo") or "").replace("/datas/small", "/datas/medium") or None,
                    "winner": s.get("winner") or bool(awards), "awards": awards,
                    "likes": s.get("like_count") or 0, "comments": s.get("comment_count") or 0,
                }
                p = tile_to_project(tile, ed, det)
                if not det.get("built_with"):
                    p["built_with"] = [t.lower() for t in s.get("tags", [])]
                p["via"] = "stream"
                out.append(p)
            if len(items) < 6:
                break
    return out
