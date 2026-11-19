"""Curated source: editor picks from config/picks.toml become projects when no scraper covers them."""
from __future__ import annotations

from ..common import load_toml, new_project, normalize_repo, slugify


def collect(series, cfg, editions):
    out = []
    for pk in load_toml("picks.toml").get("pick", []):
        if not pk.get("title"):
            continue  # pure annotation of an already-scraped project
        url = pk["match"]
        repo = normalize_repo(url)
        out.append(new_project(
            id=f"curated:{slugify(pk['title'])}",
            title=pk["title"], tagline=pk.get("tagline", ""), description=pk.get("description", ""),
            url=url, source="curated", repo=repo,
            series_id=pk.get("series_id"), event_name=pk.get("event_name"),
            event_id=f"{pk['series_id']}-{pk['year']}" if pk.get("series_id") and pk.get("year") else None,
            year=pk.get("year"), awards=pk.get("awards", []), winner=bool(pk.get("awards")),
            image=pk.get("image") or (f"https://opengraph.githubassets.com/1/{repo.split('github.com/')[1]}" if repo else None),
            video=pk.get("video"), built_with=pk.get("built_with", []),
            lang="zh" if pk.get("lang") == "zh" else "en",
        ))
    return out
