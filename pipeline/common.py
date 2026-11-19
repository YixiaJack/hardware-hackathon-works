"""Shared paths, IO helpers and the canonical project record shape."""
from __future__ import annotations

import datetime as dt
import html
import json
import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config"
DATA = ROOT / "data"
CACHE = DATA / "cache"
SITE = ROOT / "site"

TODAY = dt.date.today().isoformat()


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def load_toml(name: str) -> dict:
    with open(CONFIG / name, "rb") as f:
        return tomllib.load(f)


def load_json(path: Path, default=None):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default


def save_json(path: Path, obj, *, compact: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        if compact:
            json.dump(obj, f, ensure_ascii=False, separators=(",", ":"))
        else:
            json.dump(obj, f, ensure_ascii=False, indent=1, sort_keys=False)
            f.write("\n")
    tmp.replace(path)


def slugify(s: str) -> str:
    s = re.sub(r"[^\w一-鿿]+", "-", s.lower()).strip("-")
    return s or "x"


_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"\s+")


def strip_html(s: str | None) -> str:
    if not s:
        return ""
    s = re.sub(r"<(br|/p|/li|/h\d)[^>]*>", "\n", s, flags=re.I)
    s = _TAG_RE.sub(" ", s)
    s = html.unescape(s)
    return _WS_RE.sub(" ", s).strip()


def clip(s: str, n: int) -> str:
    s = (s or "").strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def year_from(*texts) -> int | None:
    for t in texts:
        if not t:
            continue
        m = re.search(r"(20[0-3]\d)", str(t))
        if m:
            return int(m.group(1))
    return None


def normalize_repo(url: str | None) -> str | None:
    """Return canonical https://github.com/owner/repo or None."""
    if not url:
        return None
    m = re.match(r"https?://(?:www\.)?github\.com/([\w.-]+)/([\w.-]+)", url.strip())
    if not m:
        return None
    owner, repo = m.group(1), re.sub(r"\.git$", "", m.group(2))
    if owner.lower() in {"orgs", "topics", "features", "sponsors", "about"}:
        return None
    return f"https://github.com/{owner}/{repo}".lower()


def new_project(**kw) -> dict:
    """Canonical project shape. Every source must produce this."""
    base = {
        "id": "",              # "<source>:<native-id>"
        "title": "",
        "tagline": "",
        "description": "",     # plain text, clipped
        "url": "",             # primary page (Devpost / GitHub / Hackster …)
        "source": "",
        "event_id": None,      # edition id, e.g. "makemit-2020"
        "series_id": None,     # e.g. "makemit"
        "event_name": None,
        "year": None,
        "awards": [],          # human-readable prize names
        "winner": False,
        "image": None,
        "video": None,
        "repo": None,
        "links": [],
        "team": [],
        "built_with": [],
        "likes": 0,
        "stars": 0,
        "comments": 0,
        "lang": "en",
        "first_seen": TODAY,
        "updated": TODAY,
    }
    base.update({k: v for k, v in kw.items() if v is not None})
    return base
