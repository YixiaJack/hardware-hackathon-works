"""Optional LLM enrichment: Chinese one-liner, highlight, vibe tags and refined facet tags.

Runs only with `--enrich` and when Anthropic credentials are available (ANTHROPIC_API_KEY in CI).
Results are stored on the project as `p["llm"]` and preserved across runs, so each project is
enriched once (re-enriched only if its text changes). Tags are constrained to the vocabulary in
config/taxonomy.toml via a JSON schema, so the model can't invent new categories.

    pip install anthropic
    ANTHROPIC_API_KEY=... python -m pipeline.run --reclassify --enrich --enrich-limit 50
"""
from __future__ import annotations

import hashlib
import json
import os

from . import classify as C
from .common import TODAY
from .http import log

MODEL = os.environ.get("ENRICH_MODEL", "claude-opus-5-5")
VIBES = ["humor", "warmth", "hardcore", "practical", "impact"]


def _vocab() -> dict[str, list[str]]:
    return {fid: [t["id"] for t, _ in f["terms"]] for fid, f in C.taxonomy()["facets"].items()}


def _system() -> str:
    lines = ["你是硬件黑客松作品的编目员。根据作品信息，输出结构化 JSON：",
             "- summary_zh：一句话中文简介（≤ 40 字），说清『它是什么、解决什么问题』，不要营销腔。",
             "- highlight_zh：一句中文点评（≤ 50 字），说它最有意思/最值得学习的地方；平淡的作品写空字符串。",
             "- is_hardware：作品是否包含真实的物理硬件（电路、传感器、执行器、机械结构、可穿戴、机器人等）。纯软件/纯 App/纯 XR 应用为 false。",
             "- vibe：0–2 个亮点标签：humor 脑洞幽默 | warmth 情感温度 | hardcore 硬核工程 | practical 实用落地 | impact 社会价值。",
             "- facets：每个维度 0–3 个标签，只能从下列词表选择，没有把握就留空：", ""]
    for fid, f in C.taxonomy()["facets"].items():
        m = f["meta"]
        terms = "; ".join(f"{t['id']}={t['label']}/{t['label_en']}" for t, _ in f["terms"])
        lines.append(f"[{fid}] {m['label']} {m['label_en']}: {terms}")
    return "\n".join(lines)


def _schema() -> dict:
    vocab = _vocab()
    return {
        "type": "object",
        "properties": {
            "summary_zh": {"type": "string"},
            "highlight_zh": {"type": "string"},
            "is_hardware": {"type": "boolean"},
            "vibe": {"type": "array", "items": {"type": "string", "enum": VIBES}},
            "facets": {
                "type": "object",
                "properties": {fid: {"type": "array", "items": {"type": "string", "enum": ids}} for fid, ids in vocab.items()},
                "required": list(vocab),
                "additionalProperties": False,
            },
        },
        "required": ["summary_zh", "highlight_zh", "is_hardware", "vibe", "facets"],
        "additionalProperties": False,
    }


def _payload(p: dict) -> str:
    parts = [f"标题: {p['title']}", f"标语: {p.get('tagline', '')}",
             f"赛事: {p.get('event_name') or p.get('series_id') or '未知'} {p.get('year') or ''}",
             f"获奖: {', '.join(p.get('awards') or []) or '无'}",
             f"技术栈: {', '.join(p.get('built_with') or [])}",
             f"介绍: {(p.get('description') or '')[:1800]}"]
    return "\n".join(parts)


def _digest(p: dict) -> str:
    return hashlib.sha1(_payload(p).encode()).hexdigest()[:12]


def run(projects: list[dict], *, limit: int = 150) -> None:
    try:
        import anthropic
    except ImportError:
        log("  enrich: `anthropic` not installed – skipping (pip install anthropic)")
        return
    client = anthropic.Anthropic()
    system, schema = _system(), _schema()
    todo = [p for p in projects if (p.get("llm") or {}).get("digest") != _digest(p)]
    todo.sort(key=lambda p: -p.get("score", 0))
    done = 0
    for p in todo[:limit]:
        try:
            resp = client.beta.messages.create(
                model=MODEL,
                max_tokens=2000,
                system=system,
                cache_control={"type": "ephemeral"},  # system prompt (taxonomy) is identical for every call
                output_config={"effort": "low", "format": {"type": "json_schema", "schema": schema}},
                betas=["server-side-fallback-2026-07-01"],
                fallbacks="default",
                messages=[{"role": "user", "content": _payload(p)}],
            )
        except anthropic.RateLimitError:
            log("  enrich: rate limited – stopping this run, remaining projects will be enriched next time")
            break
        except anthropic.BadRequestError as e:
            log(f"  enrich: bad request for {p['id']}: {e.message}")
            continue
        except anthropic.APIStatusError as e:
            log(f"  enrich: API error {e.status_code} for {p['id']}")
            if e.status_code >= 500:
                continue
            break
        except anthropic.APIConnectionError:
            log("  enrich: network error – stopping this run")
            break
        if resp.stop_reason == "refusal":
            p["llm"] = {"digest": _digest(p), "refused": True, "date": TODAY}
            continue
        text = next((b.text for b in resp.content if b.type == "text"), "")
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            log(f"  enrich: unparseable output for {p['id']}")
            continue
        data["facets"] = {k: v[:3] for k, v in data.get("facets", {}).items()}
        data["vibe"] = data.get("vibe", [])[:2]
        p["llm"] = {**data, "digest": _digest(p), "model": MODEL, "date": TODAY}
        done += 1
    log(f"  enrich: {done} projects enriched with {MODEL} ({max(0, len(todo) - done)} remaining)")
