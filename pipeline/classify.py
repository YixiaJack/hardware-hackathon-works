"""Rule-based faceted classifier + award tier + interest score ("有意思指数").

Driven entirely by config/taxonomy.toml so non-programmers can tune it.
An optional LLM pass (pipeline/enrich.py) can later override / extend these tags.
"""
from __future__ import annotations

import math
import re
from functools import lru_cache

from .common import load_toml

CJK = re.compile(r"[一-鿿]")


def _norm_tag(t: str) -> str:
    return re.sub(r"\s+", "-", t.strip().lower())


class Matcher:
    def __init__(self, kws: list[str], tags: list[str]):
        ascii_kws = sorted({k.lower() for k in kws if not CJK.search(k)}, key=len, reverse=True)
        self.cjk = [k for k in kws if CJK.search(k)]
        self.rx = None
        if ascii_kws:
            alt = "|".join(re.escape(k) for k in ascii_kws)
            self.rx = re.compile(rf"(?<![a-z0-9])({alt})(?:s|es)?(?![a-z0-9])")
        self.tags = {_norm_tag(t) for t in tags}

    def hits(self, text: str) -> set[str]:
        found = set(self.rx.findall(text)) if self.rx and text else set()
        found.update(k for k in self.cjk if k in text)
        return found

    def score(self, head: str, body: str, tags: set[str]) -> float:
        h = self.hits(head)
        b = self.hits(body) - h
        t = self.tags & tags
        return 3 * min(len(h), 2) + min(len(b), 4) + 3 * min(len(t), 2)


@lru_cache(maxsize=1)
def taxonomy():
    tx = load_toml("taxonomy.toml")
    facets = {}
    for fid, f in sorted(tx["facets"].items(), key=lambda kv: kv[1].get("order", 99)):
        terms = [(t, Matcher(t.get("kw", []), t.get("tags", []))) for t in f["terms"]]
        facets[fid] = {"meta": f, "terms": terms}
    hw = tx["hardware"]
    return {"facets": facets, "hw": (Matcher(hw["kw"], hw["tags"]), hw.get("threshold", 3))}


def texts(p: dict) -> tuple[str, str, set[str]]:
    head = f"{p.get('title', '')} . {p.get('tagline', '')}".lower()
    tags = {_norm_tag(t) for t in p.get("built_with", [])}
    # tech tags also count as body text, so free-form tags ("soft robotics", "orange pi 3b") match keywords
    body = ((p.get("description") or "")[:1500] + " . " + " ; ".join(p.get("built_with", []))).lower()
    return head, body, tags


def hardware_score(p: dict) -> float:
    m, _ = taxonomy()["hw"]
    head, body, tags = texts(p)
    return m.score(head, body, tags)


def is_hardware(p: dict) -> bool:
    return hardware_score(p) >= taxonomy()["hw"][1]


def classify(p: dict) -> dict[str, list[str]]:
    head, body, tags = texts(p)
    out = {}
    for fid, f in taxonomy()["facets"].items():
        thr, mx = f["meta"].get("threshold", 3), f["meta"].get("max", 3)
        scored = [(m.score(head, body, tags), t["id"], t.get("threshold", thr)) for t, m in f["terms"]]
        keep = sorted([(sc, tid) for sc, tid, th in scored if sc >= th], reverse=True)[:mx]
        out[fid] = [tid for _, tid in keep]
    return out


# ───────────────────────────── awards & score ─────────────────────────────

GRAND = re.compile(
    r"\b(1st|first|grand|overall|best overall|top prize|champion|winner overall|best hack|best in show|"
    r"best project|judges'? (choice|favorite)|一等奖|特等奖|冠军|金奖|最佳)\b|一等奖|特等奖|冠军|金奖", re.I)
PODIUM = re.compile(r"\b(2nd|second|3rd|third|runner[- ]up|finalist|二等奖|三等奖|亚军|季军|银奖|铜奖)\b|二等奖|三等奖|亚军|季军|银奖|铜奖", re.I)
SPONSOR = re.compile(r"\b(by|sponsored|use of|using|powered by|presented by)\b|赞助|\b(mlh|google|amazon|aws|microsoft|"
                     r"intel|nvidia|qualcomm|arduino|digikey|autodesk|wolfram|twilio|godaddy|echo3d|gemini)\b", re.I)


def award_tier(p: dict) -> int:
    """3 = grand / 1st place overall, 2 = podium, track winner or ranked sponsor prize, 1 = sponsor special prize."""
    if not (p.get("awards") or p.get("winner")):
        return 0
    best = 1
    for a in p.get("awards") or []:
        ranked = GRAND.search(a) or PODIUM.search(a)
        sponsored = SPONSOR.search(a)
        if GRAND.search(a) and not sponsored:
            return 3
        if ranked or not sponsored:
            best = max(best, 2)
    return best


def interest_score(p: dict, *, dedicated: bool) -> int:
    """0–100 heuristic: recognition + community signals + documentation depth + hardware depth."""
    tier = p.get("award_tier", 0)
    s = {3: 38, 2: 26, 1: 16, 0: 0}[tier]
    s += min(16, 5.5 * math.log2(1 + (p.get("likes") or 0)))
    s += min(16, 6 * math.log10(1 + (p.get("stars") or 0)) * 1.4)
    s += 6 if p.get("video") else 0
    s += 5 if p.get("repo") else 0
    s += 3 if p.get("image") and "opengraph.githubassets" not in (p.get("image") or "") else 0
    s += min(6, len(p.get("description") or "") / 250)
    s += min(6, p.get("hw_score", 0) / 3)
    s += 4 if dedicated else 0
    s += 22 if p.get("pick") else 0
    return int(round(min(100, s)))
