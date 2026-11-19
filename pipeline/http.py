"""Polite HTTP helper (stdlib only): desktop UA, per-host throttle, retries with backoff."""
from __future__ import annotations

import gzip
import json
import os
import random
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0 Safari/537.36"
)

# Minimum seconds between two requests to the same host.
HOST_INTERVAL = {
    "devpost.com": 0.5,
    "api.github.com": 0.25,
    "search.api.github.com": 2.2,
    "default": 0.6,
}
_last_hit: dict[str, float] = {}
_lock = threading.Lock()
STATS = {"requests": 0, "errors": 0}


def _throttle(host: str, path: str = "") -> None:
    """Thread-safe per-host rate limit: each caller reserves the next start slot, then sleeps until it."""
    if host == "api.github.com" and path.startswith("/search/"):
        host = "search.api.github.com"  # search API: 30 req/min → separate, slower lane
    base = host if host in HOST_INTERVAL else ".".join(host.split(".")[-2:])
    gap = HOST_INTERVAL.get(host) or HOST_INTERVAL.get(base) or HOST_INTERVAL["default"]
    with _lock:
        now = time.monotonic()
        slot = max(now, _last_hit.get(base, 0) + gap)
        _last_hit[base] = slot
        STATS["requests"] += 1
    wait = slot - now + random.uniform(0, 0.1)
    if wait > 0:
        time.sleep(wait)


def fetch(url: str, *, headers: dict | None = None, data: bytes | None = None,
          retries: int = 3, timeout: int = 30) -> str | None:
    """Return response text, or None on a permanent failure (404/403 after retries)."""
    host = urllib.parse.urlparse(url).netloc
    hdrs = {"User-Agent": UA, "Accept": "*/*", "Accept-Encoding": "gzip"}
    if headers:
        hdrs.update(headers)
    for attempt in range(retries + 1):
        _throttle(host, urllib.parse.urlparse(url).path)
        try:
            req = urllib.request.Request(url, headers=hdrs, data=data)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    raw = gzip.decompress(raw)
                charset = r.headers.get_content_charset() or "utf-8"
                return raw.decode(charset, errors="replace")
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                return None
            if e.code in (403, 429, 500, 502, 503, 504) and attempt < retries:
                retry_after = e.headers.get("Retry-After")
                delay = float(retry_after) if retry_after and retry_after.isdigit() else 2 ** attempt * 3
                time.sleep(min(delay, 60))
                continue
            STATS["errors"] += 1
            log(f"HTTP {e.code} {url}")
            return None
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            if attempt < retries:
                time.sleep(2 ** attempt * 2)
                continue
            STATS["errors"] += 1
            log(f"NETERR {e} {url}")
            return None
    return None


def fetch_json(url: str, **kw):
    kw.setdefault("headers", {})
    kw["headers"].setdefault("Accept", "application/json")
    text = fetch(url, **kw)
    if text is None:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        log(f"bad JSON from {url}: {text[:120]!r}")
        return None


def github_headers() -> dict:
    h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if tok:
        h["Authorization"] = f"Bearer {tok}"
    return h


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)
