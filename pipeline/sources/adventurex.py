"""AdventureX gallery: public tRPC endpoint returns every project in one response."""
from __future__ import annotations

import json

from ..common import clip, new_project
from ..http import fetch, log

API = "https://gallery.adventure-x.cn/api/gallery/public/trpc?trpc-path="
HDRS = {"Content-Type": "application/json", "Origin": "https://gallery.adventure-x.cn", "Accept": "application/json"}


def _call(proc: str, payload):
    txt = fetch(API + proc, data=json.dumps({"json": payload}).encode(), headers=HDRS, timeout=90)
    if not txt:
        return None
    return json.loads(txt)["result"]["data"]["json"]


def collect(series, cfg, editions):
    projects = _call("public.projects", {}) or []
    events = {e.get("slug"): e for e in (_call("public.events", None) or []) if isinstance(e, dict)}
    log(f"  adventurex: {len(projects)} projects, {len(events)} events")
    out, seen_ev = [], set()
    for p in projects:
        if p.get("eventSlug") in (None, "all") or p.get("status") != "public":
            continue
        ev = events.get(p["eventSlug"], {})
        ev_name = ev.get("name") or p["eventSlug"]
        year = int(p["year"]) if str(p.get("year", "")).isdigit() else None
        cover = next((i["url"] for i in p.get("images") or [] if i.get("isCover")), None) or \
            next((i["url"] for i in p.get("images") or []), None)
        awards = []
        for a in p.get("awardDetails") or []:
            if not a.get("award"):
                continue
            if a.get("trackType") == "sponsor" and a.get("sponsor"):
                awards.append(f"{a['award']} · {a['sponsor']} 赞助赛道")
            elif a.get("track"):
                awards.append(f"{a['award']} · {a['track']}")
            else:
                awards.append(a["award"])
        awards = awards or list(p.get("awards") or [])
        videos = p.get("externalVideos") or []
        video = videos[0].get("url") if videos and isinstance(videos[0], dict) else None
        tags = list(dict.fromkeys((p.get("tags") or []) + (p.get("tagsAi") or [])))
        desc = p.get("detailedDescription") or p.get("description") or ""
        out.append(new_project(
            id=f"advx:{p['id']}", title=p.get("name") or p.get("slug"), tagline=clip(p.get("tagline") or "", 220),
            description=clip(desc, 1500), url=f"https://gallery.adventure-x.cn/projects/{p['id']}",
            source="adventurex", series_id="adventurex", event_id=f"advx-{p['eventSlug']}", event_name=ev_name,
            year=year, awards=awards, winner=bool(awards), image=cover, video=video,
            repo=p.get("githubRepo") or None, links=[p["demoLink"]] if p.get("demoLink") else [],
            team=list(p.get("team") or [])[:6], built_with=[t.lower() for t in tags],
            likes=int(p.get("likeCount") or 0), lang="zh",
        ))
        if p["eventSlug"] not in seen_ev:
            seen_ev.add(p["eventSlug"])
            editions.append({"id": f"advx-{p['eventSlug']}", "series_id": "adventurex", "name": ev_name,
                             "year": year, "url": "https://gallery.adventure-x.cn/", "state": "ended"})
    return out
