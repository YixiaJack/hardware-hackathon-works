"""Orchestrator.

    python -m pipeline.run                    # full incremental update (all sources)
    python -m pipeline.run --sources devpost  # just one source
    python -m pipeline.run --reclassify       # re-tag existing data after editing taxonomy.toml (no network)
    python -m pipeline.run --max-detail 300   # cap new Devpost detail-page fetches this run

Resilience: if a source fails or returns nothing, the previous projects from that source are kept,
so one flaky site never wipes data. `first_seen` is preserved across runs (powers "new this week").
"""
from __future__ import annotations

import argparse
import re
import time
import traceback

from . import classify as C
from .common import DATA, TODAY, load_json, load_toml, now_iso, normalize_repo, save_json
from .http import STATS, log

ALL_SOURCES = ["devpost", "github", "build18", "hackster", "oshwhub", "adventurex", "hackaday", "curated"]


def load_series() -> tuple[list[dict], dict]:
    cfg = load_toml("events.toml")
    return cfg["series"], cfg


# ───────────────────────────── collectors ─────────────────────────────

def run_devpost(series: list[dict], cfg: dict, args, editions_out: list[dict]) -> list[dict]:
    from .sources import devpost as dp

    import threading
    from concurrent.futures import ThreadPoolExecutor
    budget = {"left": args.max_detail}
    budget_lock = threading.Lock()
    hw_matcher, _ = C.taxonomy()["hw"]

    def wants(dedicated):
        def _w(tile):
            cached = (dp.DETAIL_DIR / f"{tile['url'].rstrip('/').rsplit('/', 1)[-1]}.json").exists()
            if cached:
                return True  # cheap: served from cache unless TTL expired
            head = f"{tile.get('title', '')} {tile.get('tagline', '')}".lower()
            hw_hint = bool(hw_matcher.hits(head))
            ok = dedicated or tile.get("winner") or hw_hint or (tile.get("likes") or 0) >= 10
            with budget_lock:
                if ok and budget["left"] > 0:
                    budget["left"] -= 1
                    return True
            return False
        return _w

    out = []
    known_editions = {}
    jobs = []
    for s in series:
        if not s.get("devpost_search") and not s.get("devpost_galleries"):
            continue
        try:
            eds = dp.discover_editions(s)
        except Exception:  # noqa: BLE001
            log(f"  ! devpost discovery failed for {s['id']}\n{traceback.format_exc()}")
            continue
        eds = [e for e in eds if (e.get("year") or 0) >= s.get("min_year", 2014)]
        for e in eds:
            known_editions[e["url"].rstrip("/")] = e
            editions_out.append(e)
            if e.get("state") not in ("ended", "open", None) and not e.get("winners_announced"):
                continue
            jobs.append((e, s.get("hardware_focus") == "dedicated"))
    # dedicated (hardware-only) editions first so the detail budget goes to them
    jobs.sort(key=lambda j: (not j[1], -(j[0].get("year") or 0)))
    log(f"  devpost: {len(jobs)} editions to collect")

    def one(job):
        e, dedicated = job
        try:
            return dp.collect_edition(e, want_detail=wants(dedicated))
        except Exception:  # noqa: BLE001
            log(f"  ! devpost edition failed {e['name']}\n{traceback.format_exc()}")
            return []

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for res in pool.map(one, jobs):
            out += res

    # newest-first hardware stream across all of Devpost
    stream_cfg = cfg.get("devpost_stream", {})
    if stream_cfg.get("queries"):
        def resolve(subs):
            for sub in subs:
                ed = known_editions.get(sub["url"].rstrip("/"))
                if ed:
                    return ed, sub["awards"]
            if subs:
                sub = subs[0]
                y = re.search(r"20[1-3]\d", sub["name"])
                ed = {"id": "dp-" + re.sub(r"\W+", "-", sub["url"].split("//")[-1].split(".")[0]).lower(),
                      "series_id": None, "name": sub["name"], "url": sub["url"],
                      "year": int(y.group(0)) if y else int(TODAY[:4])}
                return ed, sub["awards"]
            return None, []
        stream = dp.collect_stream(stream_cfg["queries"], args.stream_pages or stream_cfg.get("pages", 5),
                                   min_likes=stream_cfg.get("min_likes", 3), resolve_event=resolve)
        log(f"  devpost stream: {len(stream)} candidate projects")
        out += stream
    log(f"  devpost detail budget left: {budget['left']}")
    return out


def run_github(series, cfg, args, _eds):
    from .sources import github as gh
    return gh.collect(series, cfg.get("github_extra_queries", []))


def run_optional(name):
    def _run(series, cfg, args, eds):
        import importlib
        mod = importlib.import_module(f".sources.{name}", __package__)
        return mod.collect(series, cfg, eds)
    return _run


COLLECTORS = {
    "devpost": run_devpost,
    "github": run_github,
    "build18": run_optional("build18"),
    "hackster": run_optional("hackster"),
    "oshwhub": run_optional("oshwhub"),
    "adventurex": run_optional("adventurex"),
    "hackaday": run_optional("hackaday"),
    "curated": run_optional("curated"),
}


# ───────────────────────────── merge / enrich ─────────────────────────────

def merge(prev: list[dict], fresh_by_source: dict[str, list[dict]]) -> list[dict]:
    prev_by_id = {p["id"]: p for p in prev}
    merged: dict[str, dict] = {}
    for src in ALL_SOURCES:
        items = fresh_by_source.get(src)
        if items is None or (len(items) == 0 and any(p["source"] == src for p in prev)):
            # source skipped or failed → keep last known good data
            items = [p for p in prev if p["source"] == src]
        for p in items:
            old = prev_by_id.get(p["id"])
            if old:
                p["first_seen"] = old.get("first_seen", p["first_seen"])
                # a re-scrape without the detail page (cold cache, budget hit) must not erase known details
                for k in ("zh", "llm", "description", "built_with", "repo", "video", "links", "team", "image",
                          "awards", "event_id", "event_name", "series_id", "year"):
                    if old.get(k) and not p.get(k):
                        p[k] = old[k]
                p["likes"] = max(p.get("likes") or 0, old.get("likes") or 0)
                p["stars"] = max(p.get("stars") or 0, old.get("stars") or 0)
                p["winner"] = p.get("winner") or old.get("winner", False)
            if p["id"] in merged:  # same project from two editions/stream → combine
                a = merged[p["id"]]
                a["awards"] = list(dict.fromkeys(a["awards"] + p["awards"]))
                a["winner"] = a["winner"] or p["winner"]
                for k in ("event_id", "series_id", "event_name", "year", "repo", "video", "image"):
                    a[k] = a.get(k) or p.get(k)
                if not a.get("built_with"):
                    a["built_with"] = p.get("built_with", [])
                continue
            merged[p["id"]] = p

    # de-duplicate: curated → richer scraped page; GitHub repo → any page that links to it
    by_repo = {}
    for p in merged.values():
        r = normalize_repo(p.get("repo"))
        if r and p["source"] not in ("github", "curated"):
            by_repo.setdefault(r, p)
    for weak in ("curated", "github"):
        for pid in [k for k, p in merged.items() if p["source"] == weak]:
            g = merged[pid]
            r = normalize_repo(g.get("repo"))
            host = by_repo.get(r) if r else None
            if host:
                host["stars"] = max(host.get("stars", 0), g.get("stars", 0))
                for k in ("series_id", "event_name", "event_id", "year", "video"):
                    host[k] = host.get(k) or g.get(k)
                host["awards"] = list(dict.fromkeys((host.get("awards") or []) + (g.get("awards") or [])))
                host["winner"] = host.get("winner") or bool(host["awards"])
                if not host.get("description") and g.get("description"):
                    host["description"] = g["description"]
                del merged[pid]
            elif r and weak == "curated":
                by_repo[r] = g
    return list(merged.values())


def apply_picks(projects: list[dict]) -> None:
    picks = load_toml("picks.toml").get("pick", [])
    idx = {}
    for p in projects:
        for key in (p["url"].lower().rstrip("/"), normalize_repo(p.get("repo"))):
            if key:
                idx[key] = p
    for pk in picks:
        tgt = idx.get(pk["match"].lower().rstrip("/")) or idx.get(normalize_repo(pk["match"]) or "")
        if not tgt:
            continue
        tgt["pick"] = True
        for k in ("note_zh", "zh", "vibe"):
            if pk.get(k):
                tgt[k if k != "note_zh" else "pick_note"] = pk[k]
        if pk.get("facets"):
            tgt["facet_override"] = pk["facets"]


GENERIC_NAME = re.compile(
    r"^(make ?mit|make ?uoft|make ?harvard|make ?cu|build ?18|makeathon|treehacks?|hackmit|reality ?hack(athon)?|"
    r"hackathon|hardware ?hack(athon)?|project|team ?\d*|final project|demo|test)[\s_-]*(20\d\d|\d{2})?[\s_-]*(project|team ?\d*)?$", re.I)
JUNK = re.compile(r"\b(tutorial|starter|template|boilerplate|workshop|website|landing page|resources|registration|"
                  r"problem statements?|checkout system|judging( system)?|for hackathons|hackathon (management|platform)|"
                  r"slides|organi[sz]ers?|curated|tracker|awesome|inventory management|in a box|get up to \$\d+)\b", re.I)


def github_quality(p: dict) -> bool:
    """Keep repos that read like an actual build, not event stubs / org tooling."""
    if JUNK.search(p.get("title", "") + " " + p.get("tagline", "")):
        return False
    tagline = (p.get("tagline") or "").strip()
    if GENERIC_NAME.match(p["title"].strip()):
        if 8 <= len(tagline) <= 70 and not GENERIC_NAME.match(tagline):
            p["title"] = tagline  # "MakeMIT2014" + "Robotic Acoustic Guitar Player" → use the tagline as the name
        elif p.get("stars", 0) < 10:
            return False
    text = f"{tagline} {p.get('description', '')}".strip()
    if len(text) >= 140 or p.get("stars", 0) >= 5:
        return True
    hw, _ = C.taxonomy()["hw"]
    return bool(hw.hits(f"{p['title']} {tagline}".lower()))


def finalize(projects: list[dict], series: list[dict]) -> list[dict]:
    sinfo = {s["id"]: s for s in series}
    out = []
    for p in projects:
        s = sinfo.get(p.get("series_id") or "")
        dedicated = bool(s and s.get("hardware_focus") == "dedicated")
        p["hw_score"] = C.hardware_score(p)
        needs_hw = not dedicated or p["source"] == "github"  # repo search hits event websites too
        if needs_hw and not p.get("pick") and p["hw_score"] < C.taxonomy()["hw"][1]:
            continue  # general hackathon / stream / repo without hardware signal
        if needs_hw and not p.get("pick") and (p.get("llm") or {}).get("is_hardware") is False:
            continue  # LLM read the full story and found no physical build
        if p["source"] == "github" and not p.get("pick") and not github_quality(p):
            continue  # event-named stub, starter kit, tutorial or undocumented repo
        if p.get("url") and "devpost.com" in p["url"] and not p.get("tagline") and not p.get("description") and not p.get("winner"):
            continue  # empty placeholder submission
        p["facets"] = C.classify(p)
        if p.get("llm", {}).get("facets"):
            for k, v in p["llm"]["facets"].items():  # LLM refinement wins when present
                if v:
                    p["facets"][k] = v
        for k, v in (p.get("facet_override") or {}).items():  # editor's word is final
            p["facets"][k] = v
        p["award_tier"] = C.award_tier(p)
        p["score"] = C.interest_score(p, dedicated=dedicated)
        p["updated"] = TODAY
        out.append(p)
    out.sort(key=lambda p: (-p["score"], p["title"].lower()))
    return out


def summarize_events(series, editions, projects) -> dict:
    counts, winners = {}, {}
    for p in projects:
        for key in (p.get("event_id"), p.get("series_id")):
            if key:
                counts[key] = counts.get(key, 0) + 1
                winners[key] = winners.get(key, 0) + (1 if p.get("award_tier") else 0)
    seen, eds = set(), []
    for e in editions:
        if e["id"] in seen:
            continue
        seen.add(e["id"])
        eds.append({**e, "projects": counts.get(e["id"], 0), "winners": winners.get(e["id"], 0)})
    ser = []
    for s in series:
        ser.append({k: s.get(k) for k in ("id", "name", "name_zh", "org", "region", "kind", "hardware_focus",
                                           "url", "blurb_zh", "blurb_en")}
                   | {"projects": counts.get(s["id"], 0), "winners": winners.get(s["id"], 0),
                      "editions": sorted([e for e in eds if e["series_id"] == s["id"]],
                                         key=lambda e: -(e.get("year") or 0))})
    ser.sort(key=lambda s: -s["projects"])
    return {"generated": now_iso(), "series": ser}


# ───────────────────────────── main ─────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sources", default=",".join(ALL_SOURCES))
    ap.add_argument("--reclassify", action="store_true", help="no network; re-run classification/scoring/render")
    ap.add_argument("--max-detail", type=int, default=400, help="new Devpost detail pages per run")
    ap.add_argument("--stream-pages", type=int, default=0)
    ap.add_argument("--workers", type=int, default=4, help="parallel Devpost editions (shared per-host rate limit)")
    ap.add_argument("--enrich", action="store_true", help="run optional LLM enrichment (needs ANTHROPIC_API_KEY)")
    ap.add_argument("--enrich-limit", type=int, default=150)
    args = ap.parse_args()

    t0 = time.time()
    series, cfg = load_series()
    prev = load_json(DATA / "projects.json", {}).get("projects", [])
    prev_events = load_json(DATA / "events.json", {"series": []})
    editions = [e for s in prev_events["series"] for e in s.get("editions", [])]

    fresh: dict[str, list[dict]] = {}
    if not args.reclassify:
        new_eds: list[dict] = []
        for src in args.sources.split(","):
            src = src.strip()
            if src not in COLLECTORS:
                continue
            log(f"▶ {src}")
            try:
                fresh[src] = COLLECTORS[src](series, cfg, args, new_eds) or []
                log(f"  {src}: {len(fresh[src])} raw items")
            except ModuleNotFoundError as e:
                log(f"  (skip {src}: {e})")
            except Exception:  # noqa: BLE001
                log(f"  ! {src} failed, keeping previous data\n{traceback.format_exc()}")
        if new_eds:
            ids = {e["id"] for e in new_eds}
            editions = new_eds + [e for e in editions if e["id"] not in ids]

    projects = merge(prev, fresh)

    if not args.reclassify:
        try:
            from .sources import github as gh
            stars = gh.refresh_stars([normalize_repo(p.get("repo")) for p in projects if normalize_repo(p.get("repo"))])
            for p in projects:
                r = normalize_repo(p.get("repo"))
                if r and r in stars:
                    p["stars"] = max(p.get("stars", 0), stars[r])
        except Exception:  # noqa: BLE001
            log(f"  ! star refresh failed\n{traceback.format_exc()}")

    apply_picks(projects)
    projects = finalize(projects, series)

    if args.enrich:
        from . import enrich
        enrich.run(projects, limit=args.enrich_limit)
        projects = finalize(projects, series)

    events = summarize_events(series, editions, projects)
    save_json(DATA / "projects.json", {"generated": now_iso(), "count": len(projects), "projects": projects})
    save_json(DATA / "events.json", events)

    from . import render
    render.all_outputs(projects, events)
    log(f"✔ {len(projects)} projects · {STATS['requests']} requests · {STATS['errors']} errors · {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
