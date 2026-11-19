"""GitHub collector: hackathon project repos found via search + star counts for linked repos."""
from __future__ import annotations

import base64
import json
import re
import urllib.parse

from ..common import CACHE, TODAY, clip, load_json, new_project, save_json, strip_html, year_from
from ..http import fetch_json, github_headers, log

REPO_CACHE = CACHE / "github_repos.json"
STATS_TTL_DAYS = 7


def _days_ago(n: int) -> str:
    import datetime as dt
    return (dt.date.today() - dt.timedelta(days=n)).isoformat()


def search_repos(query: str, max_results: int = 200) -> list[dict]:
    out = []
    for page in range(1, max_results // 100 + 2):
        url = ("https://api.github.com/search/repositories?q=" + urllib.parse.quote(query)
               + f"&sort=stars&order=desc&per_page=100&page={page}")
        d = fetch_json(url, headers=github_headers())
        items = (d or {}).get("items") or []
        out.extend(items)
        if len(items) < 100 or len(out) >= max_results:
            break
    return out[:max_results]


def readme_text(full_name: str, cache: dict) -> str:
    ent = cache.get(full_name.lower(), {})
    if "readme" in ent:
        return ent["readme"]
    d = fetch_json(f"https://api.github.com/repos/{full_name}/readme", headers=github_headers())
    txt = ""
    if d and d.get("content"):
        try:
            raw = base64.b64decode(d["content"]).decode("utf-8", "replace")
            raw = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", raw)          # images
            raw = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", raw)         # links → text
            raw = re.sub(r"```.*?```", " ", raw, flags=re.S)           # code blocks
            raw = re.sub(r"[#>*_`|-]{1,}", " ", raw)
            txt = clip(strip_html(raw), 1500)
        except Exception:  # noqa: BLE001
            txt = ""
    ent["readme"] = txt
    cache[full_name.lower()] = ent
    return txt


def _image_from_readme(full_name: str, branch: str | None) -> str | None:
    return f"https://opengraph.githubassets.com/1/{full_name}"


def repo_to_project(r: dict, series: dict | None, readme: str) -> dict:
    full = r["full_name"]
    name = r["name"].replace("-", " ").replace("_", " ").strip()
    created = r.get("created_at", "")
    built = list(r.get("topics") or [])
    if r.get("language"):
        built.append(r["language"].lower())
    return new_project(
        id=f"github:{full.lower()}",
        title=name[:1].upper() + name[1:],
        tagline=clip(r.get("description") or "", 220),
        description=readme,
        url=r["html_url"],
        source="github",
        series_id=series and series["id"],
        year=year_from(r.get("name"), r.get("description")) or (int(created[:4]) if created else None),
        image=_image_from_readme(full, r.get("default_branch")),
        repo=r["html_url"].lower(),
        links=[r["homepage"]] if r.get("homepage") else [],
        team=[r["owner"]["login"]],
        built_with=built,
        stars=r.get("stargazers_count") or 0,
    )


def collect(series_list: list[dict], extra_queries: list[dict]) -> list[dict]:
    cache = load_json(REPO_CACHE, {})
    out, seen = [], set()
    jobs = [(q, s) for s in series_list for q in s.get("github_queries", [])]
    jobs += [(q["q"], None) for q in extra_queries]
    for q, s in jobs:
        items = search_repos(q, 200 if s else 100)
        log(f"  github '{q}': {len(items)} repos")
        for r in items:
            key = r["full_name"].lower()
            if key in seen or r.get("fork") or r.get("archived") and not r.get("stargazers_count"):
                continue
            seen.add(key)
            readme = readme_text(r["full_name"], cache)
            p = repo_to_project(r, s, readme)
            p["_query"] = q
            out.append(p)
            cache.setdefault(key, {}).update({"stars": p["stars"], "fetched": TODAY})
    save_json(REPO_CACHE, cache)
    return out


def refresh_stars(repo_urls: list[str]) -> dict[str, int]:
    """Batch star counts with GraphQL (50 repos/query). Cached for STATS_TTL_DAYS."""
    cache = load_json(REPO_CACHE, {})
    want = []
    for u in set(repo_urls):
        m = re.match(r"https://github\.com/([^/]+)/([^/]+)", u or "")
        if not m:
            continue
        key = f"{m.group(1)}/{m.group(2)}".lower()
        ent = cache.get(key, {})
        if ent.get("fetched", "") < _days_ago(STATS_TTL_DAYS):
            want.append((m.group(1), m.group(2), key))
    hdrs = github_headers()
    if "Authorization" in hdrs and want:
        for i in range(0, len(want), 50):
            chunk = want[i:i + 50]
            parts = [f'r{j}: repository(owner: {json.dumps(o)}, name: {json.dumps(n)}) {{ stargazerCount pushedAt }}'
                     for j, (o, n, _) in enumerate(chunk)]
            body = json.dumps({"query": "query {" + " ".join(parts) + "}"}).encode()
            from ..http import fetch
            txt = fetch("https://api.github.com/graphql", headers={**hdrs, "Content-Type": "application/json"}, data=body)
            data = (json.loads(txt).get("data") or {}) if txt else {}
            for j, (_, _, key) in enumerate(chunk):
                node = data.get(f"r{j}")
                ent = cache.setdefault(key, {})
                ent.update({"stars": (node or {}).get("stargazerCount", 0), "fetched": TODAY,
                            "missing": node is None})
        log(f"  github stars refreshed for {len(want)} repos")
    save_json(REPO_CACHE, cache)
    return {f"https://github.com/{k}": v.get("stars", 0) for k, v in cache.items()}
