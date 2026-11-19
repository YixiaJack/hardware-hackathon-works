"""Render outputs: site/data.json (compact), site/feed.xml (Atom), README.md (from template)."""
from __future__ import annotations

import datetime as dt
import html
import os
from collections import Counter
from pathlib import Path

from . import classify as C
from .common import ROOT, SITE, TODAY, clip, now_iso, save_json

TEMPLATE = Path(__file__).parent / "templates" / "README.md.tmpl"
SITE_URL = os.environ.get("SITE_URL", "https://OWNER.github.io/hardware-hackathon-works/")  # set by CI from the Pages URL


def _facets_meta():
    out = []
    for fid, f in C.taxonomy()["facets"].items():
        m = f["meta"]
        out.append({"id": fid, "label": m["label"], "label_en": m["label_en"],
                    "terms": [{"id": t["id"], "label": t["label"], "label_en": t["label_en"], "icon": t.get("icon", "")}
                              for t, _ in f["terms"]]})
    return out


def compact(p: dict) -> dict:
    d = {
        "i": p["id"], "t": p["title"], "g": clip(p.get("tagline", ""), 200), "d": clip(p.get("description", ""), 420),
        "u": p["url"], "s": p["source"], "e": p.get("event_name"), "ei": p.get("event_id"), "sr": p.get("series_id"),
        "y": p.get("year"), "a": p.get("awards", [])[:4], "w": p.get("award_tier", 0),
        "im": None if "opengraph.githubassets.com" in (p.get("image") or "") else p.get("image"),
        "v": p.get("video"), "r": p.get("repo"), "lk": p.get("likes", 0), "st": p.get("stars", 0),
        "bw": p.get("built_with", [])[:12], "f": {k: v for k, v in p.get("facets", {}).items() if v},
        "sc": p.get("score", 0), "fs": p.get("first_seen"), "tm": p.get("team", [])[:5],
    }
    for k_src, k_dst in (("zh", "zh"), ("pick_note", "pn"), ("vibe", "vb"), ("pick", "pk"), ("lang", "lg")):
        if p.get(k_src) and not (k_src == "lang" and p[k_src] == "en"):
            d[k_dst] = p[k_src]
    if p.get("llm", {}).get("highlight_zh"):
        d["hl"] = p["llm"]["highlight_zh"]
    if p.get("llm", {}).get("summary_zh") and not d.get("zh"):
        d["zh"] = p["llm"]["summary_zh"]
    if p.get("llm", {}).get("vibe") and not d.get("vb"):
        d["vb"] = p["llm"]["vibe"]
    return {k: v for k, v in d.items() if v not in (None, "", [], {}, 0) or k in ("w", "sc")}


def site_data(projects, events) -> dict:
    return {
        "generated": now_iso(),
        "meta": {"repo_url": os.environ.get("REPO_URL"), "site_url": SITE_URL},
        "facets": _facets_meta(),
        "series": [{k: v for k, v in s.items() if k != "editions"} |
                   {"editions": [{"id": e["id"], "name": e["name"], "year": e.get("year"), "url": e.get("url"),
                                  "projects": e.get("projects", 0), "dates": e.get("dates"),
                                  "registrations": e.get("registrations")}
                                 for e in s.get("editions", [])]}
                   for s in events["series"]],
        "projects": [compact(p) for p in projects],
    }


def feed(projects) -> str:
    items = sorted(projects, key=lambda p: (p.get("first_seen", ""), p.get("score", 0)), reverse=True)[:80]
    now = now_iso()
    out = ['<?xml version="1.0" encoding="utf-8"?>',
           '<feed xmlns="http://www.w3.org/2005/Atom">',
           "<title>Hardware Hackathon Works · 硬件黑客松作品雷达</title>",
           f'<link href="{SITE_URL}"/>', f"<updated>{now}</updated>",
           f"<id>{SITE_URL}</id>"]
    for p in items:
        summary = p.get("zh") or p.get("tagline") or ""
        ev = f" · {p['event_name']}" if p.get("event_name") else ""
        aw = f" · 🏆 {', '.join(p['awards'][:2])}" if p.get("awards") else ""
        out += ["<entry>", f"<title>{html.escape(p['title'] + ev)}</title>",
                f'<link href="{html.escape(p["url"])}"/>', f"<id>{html.escape(p['id'])}</id>",
                f"<updated>{p.get('first_seen', TODAY)}T00:00:00Z</updated>",
                f"<summary>{html.escape(summary + aw)}</summary>", "</entry>"]
    out.append("</feed>")
    return "\n".join(out)


# ───────────────────────────── README ─────────────────────────────

def _md_esc(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ")


def _label(fid, tid):
    for t, _ in C.taxonomy()["facets"][fid]["terms"]:
        if t["id"] == tid:
            return f"{t.get('icon', '')} {t['label']}"
    return tid


def _row(p):
    ev = _md_esc(p.get("event_name") or (str(p.get("year")) if p.get("year") else "—"))
    aw = "🏆 " + _md_esc(p["awards"][0]) if p.get("awards") else ""
    tags = " ".join(f"`{_label('domain', d).split(' ', 1)[-1]}`" for d in p.get("facets", {}).get("domain", [])[:2])
    desc = _md_esc(clip(p.get("zh") or p.get("llm", {}).get("summary_zh") or p.get("tagline", ""), 90))
    return f"| [**{_md_esc(p['title'])}**]({p['url']}) | {desc} | {ev} | {tags} {aw} | {p.get('score', 0)} |"


def readme(projects, events) -> str:
    tpl = TEMPLATE.read_text(encoding="utf-8")
    n = len(projects)
    winners = sum(1 for p in projects if p.get("award_tier"))
    series_with = [s for s in events["series"] if s["projects"]]
    editions = sum(1 for s in events["series"] for e in s["editions"] if e.get("projects"))
    week_ago = (dt.date.today() - dt.timedelta(days=7)).isoformat()
    new = [p for p in projects if p.get("first_seen", "") >= week_ago]

    picks = [p for p in projects if p.get("pick")][:12]
    picks_md = "\n".join(["| 作品 | 一句话 | 赛事 | 标签 | 指数 |", "| :-- | :-- | :-- | :-- | --: |"] + [_row(p) for p in picks])

    dom_blocks = []
    dom_count = Counter(d for p in projects for d in p.get("facets", {}).get("domain", []))
    for t, _ in C.taxonomy()["facets"]["domain"]["terms"]:
        items = [p for p in projects if t["id"] in p.get("facets", {}).get("domain", [])][:5]
        if not items:
            continue
        dom_blocks.append(f"<details><summary><b>{t.get('icon', '')} {t['label']} · {t['label_en']}</b>"
                          f" — {dom_count[t['id']]} 件</summary>\n\n"
                          + "\n".join(["| 作品 | 一句话 | 赛事 | 标签 | 指数 |", "| :-- | :-- | :-- | :-- | --: |"]
                                      + [_row(p) for p in items]) + "\n\n</details>")

    ev_rows = ["| 赛事 | 类型 | 地区 | 收录届数 | 作品 | 获奖 |", "| :-- | :-- | :-- | --: | --: | --: |"]
    kind_zh = {"makeathon": "造物赛", "hackathon": "综合黑客松", "xr-hack": "XR 黑客松", "online-contest": "线上挑战",
               "prize": "长周期大奖", "build-fest": "造物节"}
    for s in series_with:
        eds = sum(1 for e in s["editions"] if e.get("projects"))
        focus = "" if s["hardware_focus"] == "dedicated" else " ·硬件赛道"
        ev_rows.append(f"| [{s['name_zh'] or s['name']}]({s['url']}) | {kind_zh.get(s['kind'], s['kind'])}{focus} | "
                       f"{s['region']} | {eds or '—'} | {s['projects']} | {s['winners']} |")

    initial = len(new) > 0.25 * max(n, 1)  # first full crawl: everything is "new"
    new_md = "_首轮全量收录完成；之后每次更新会在这里列出最近 7 天新收录的高分作品。_" if initial else "\n".join(f"- [{_md_esc(p['title'])}]({p['url']}) — {_md_esc(clip(p.get('zh') or p.get('tagline', ''), 70))}"
                       f"{' · ' + _md_esc(p['event_name']) if p.get('event_name') else ''}"
                       for p in sorted(new, key=lambda p: -p.get("score", 0))[:15]) or "_本周暂无新增_"

    fac_rows = []
    for fid, f in C.taxonomy()["facets"].items():
        m = f["meta"]
        cnt = Counter(t for p in projects for t in p.get("facets", {}).get(fid, []))
        top = " · ".join(f"{t.get('icon', '')}{t['label']} {cnt[t['id']]}"
                         for t, _ in sorted(f["terms"], key=lambda x: -cnt[x[0]["id"]])[:6] if cnt[t["id"]])
        fac_rows.append(f"| **{m['label']}** {m['label_en']} | {top} |")

    repl = {
        "TODAY": TODAY, "TODAY_BADGE": TODAY.replace("-", "--"), "COUNT": str(n), "WINNERS": str(winners), "SERIES": str(len(series_with)),
        "EDITIONS": str(editions), "NEW_WEEK": "首轮" if initial else str(len(new)), "SITE_URL": SITE_URL,
        "PICKS_TABLE": picks_md, "DOMAIN_BLOCKS": "\n\n".join(dom_blocks), "EVENTS_TABLE": "\n".join(ev_rows),
        "NEW_LIST": new_md, "FACET_TABLE": "\n".join(["| 维度 | 分布 Top |", "| :-- | :-- |"] + fac_rows),
    }
    for k, v in repl.items():
        tpl = tpl.replace("{{" + k + "}}", v)
    return tpl


def all_outputs(projects, events):
    save_json(SITE / "data.json", site_data(projects, events), compact=True)
    (SITE / "feed.xml").write_text(feed(projects), encoding="utf-8")
    if TEMPLATE.exists():
        (ROOT / "README.md").write_text(readme(projects, events), encoding="utf-8")
