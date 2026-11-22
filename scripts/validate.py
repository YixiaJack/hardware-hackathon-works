"""Zero-dependency validator for config + generated data. Exit code 1 on any error."""
from __future__ import annotations

import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []
warnings: list[str] = []


def err(msg):
    errors.append(msg)


def main():
    tx = tomllib.loads((ROOT / "config/taxonomy.toml").read_text(encoding="utf-8"))
    ev = tomllib.loads((ROOT / "config/events.toml").read_text(encoding="utf-8"))
    picks = tomllib.loads((ROOT / "config/picks.toml").read_text(encoding="utf-8"))

    vocab = {}
    for fid, f in tx["facets"].items():
        ids = [t["id"] for t in f["terms"]]
        if len(ids) != len(set(ids)):
            err(f"taxonomy: duplicate term id in facet {fid}")
        for t in f["terms"]:
            for k in ("id", "label", "label_en"):
                if not t.get(k):
                    err(f"taxonomy: {fid} term missing {k}: {t}")
            if not (t.get("kw") or t.get("tags")):
                err(f"taxonomy: {fid}:{t['id']} has neither kw nor tags")
        vocab[fid] = set(ids)

    sids = [s["id"] for s in ev["series"]]
    if len(sids) != len(set(sids)):
        err("events: duplicate series id")
    for s in ev["series"]:
        if s.get("hardware_focus") not in ("dedicated", "track"):
            err(f"events: {s['id']} hardware_focus must be dedicated|track")
        if s.get("devpost_title_regex"):
            try:
                re.compile(s["devpost_title_regex"])
            except re.error as e:
                err(f"events: {s['id']} bad regex: {e}")
    for pk in picks.get("pick", []):
        if not pk.get("match", "").startswith("http"):
            err(f"picks: match must be a URL: {pk}")
        if pk.get("title") and pk.get("series_id") and pk["series_id"] not in sids:
            err(f"picks: unknown series_id {pk['series_id']}")
        for v in pk.get("vibe", []):
            if v not in {"humor", "warmth", "hardcore", "practical", "impact"}:
                err(f"picks: unknown vibe {v}")
        if "pick" in pk and not isinstance(pk["pick"], bool):
            err(f"picks: pick must be true|false: {pk['match']}")
        if pk.get("repo"):
            if not re.match(r"https://github\.com/[\w.-]+/[\w.-]+/?$", pk["repo"]):
                err(f"picks: repo must be https://github.com/<owner>/<repo>: {pk['match']}")
            if pk.get("title"):
                err(f"picks: repo is only for entries without title (a titled entry's repo is its match): {pk['match']}")

    pj = ROOT / "data/projects.json"
    if pj.exists():
        data = json.loads(pj.read_text(encoding="utf-8"))
        seen = set()
        for p in data["projects"]:
            pid = p.get("id")
            if not pid or pid in seen:
                err(f"projects: missing/duplicate id {pid}")
            seen.add(pid)
            if not p.get("title"):
                err(f"projects: {pid} has no title")
            if not str(p.get("url", "")).startswith("http"):
                err(f"projects: {pid} bad url {p.get('url')}")
            if not 0 <= p.get("score", -1) <= 100:
                err(f"projects: {pid} score out of range")
            for fid, vals in (p.get("facets") or {}).items():
                bad = set(vals) - vocab.get(fid, set())
                if bad:
                    err(f"projects: {pid} unknown {fid} tags {bad}")
            if p.get("series_id") and p["series_id"] not in sids:
                warnings.append(f"projects: {pid} series {p['series_id']} not in events.toml")
        print(f"projects.json: {len(data['projects'])} projects checked")
        site = ROOT / "site/data.json"
        if site.exists() and site.stat().st_size > 15 * 1024 * 1024:
            err("site/data.json exceeds 15 MB – trim descriptions in render.compact()")

    for w in warnings[:10]:
        print("warn:", w)
    for e in errors:
        print("ERROR:", e)
    print("OK" if not errors else f"{len(errors)} error(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
