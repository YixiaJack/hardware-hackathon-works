# AGENTS.md — maintenance protocol for AI agents

This repository is an auto-updating index of **hardware / robotics / embodied-interaction hackathon projects**.
It is the "works" companion to [AlexDrives/hardware-hackathon-radar](https://github.com/AlexDrives/hardware-hackathon-radar), which tracks the *events*.

## 1. Ground rules

1. **Never hand-edit generated files**: `data/projects.json`, `data/events.json`, `site/data.json`, `site/feed.xml`, `README.md`.
   Change the inputs (`config/*.toml`, `pipeline/**`, `pipeline/templates/README.md.tmpl`) and re-run the pipeline.
2. **Never fabricate projects, awards or links.** Every record must come from a scraper or from `config/picks.toml`
   with a real, reachable URL. Awards in picks must be verifiable on the project page or an official announcement.
3. **Don't defeat access controls.** If a site answers 403 / Cloudflare challenge / login wall, record that in §4 and move on.
   No credential harvesting, no headless-browser evasion of bot protection.
4. Always finish with `python -m pipeline.run --reclassify && python scripts/validate.py` (offline, ~5 s).

## 2. Layout

| Path | Role |
| :-- | :-- |
| `config/events.toml` | Competition series. Devpost editions are auto-discovered via `devpost_search` + `devpost_title_regex`. `hardware_focus = "dedicated"` keeps every project; `"track"` keeps only projects that pass the hardware test. Also `[devpost_stream]`, `[[github_extra_queries]]`, `[hackaday]`, `[[hackaday_contests]]`. |
| `config/taxonomy.toml` | The six facets (domain · form · interaction · platform · ai · fab) and the `[hardware]` detector. Keyword rules only — no code. |
| `config/picks.toml` | Editor's picks: Chinese one-liner (`zh`), note (`note_zh`), `vibe`. Entries with `title` also create the project if no scraper found it. |
| `pipeline/sources/*.py` | One collector per source. Each returns records built with `common.new_project()`. |
| `pipeline/run.py` | Orchestrator: collect → merge/dedupe (by id, then by repo URL) → picks → classify → score → render. Keeps last-good data per source on failure. |
| `pipeline/classify.py` | Facet matcher, award tier, interest score (0–100). |
| `pipeline/enrich.py` | Optional Claude pass (Chinese summary, highlight, vibe, refined facets). Constrained to the taxonomy vocabulary via JSON schema. |
| `pipeline/render.py` | `site/data.json`, `site/feed.xml`, `README.md`. |
| `site/` | Static front end (no build). `python -m http.server -d site` to preview. |

## 3. Common tasks

**Add a Devpost-hosted competition series** — append a `[[series]]` block to `config/events.toml`:
```toml
[[series]]
id = "makeabc"                     # kebab-case, unique
name = "MakeABC"
name_zh = "MakeABC（某大学）"
org = "ABC University"
region = "North America"           # China | North America | Europe | Asia | Global
kind = "makeathon"                 # makeathon | hackathon | xr-hack | online-contest | prize | build-fest
hardware_focus = "dedicated"       # or "track"
url = "https://makeabc.org/"
blurb_zh = "一句话说明这个比赛的特点"
blurb_en = "One line on what makes it distinct."
devpost_search = ["makeabc"]       # single words; Devpost's search ORs multi-word queries
devpost_title_regex = '''^makeabc'''
```
Then `python -m pipeline.run --sources devpost` (network) and validate.

**Add a new source** — create `pipeline/sources/<name>.py` exposing `collect(series, cfg, editions) -> list[dict]`,
append editions you discover to `editions`, add `<name>` to `ALL_SOURCES` in `pipeline/run.py`, and add a `[[series]]`.
Use `pipeline.http.fetch / fetch_json` (throttled, retried) — never raw `urllib`.

**Tune classification** — edit `config/taxonomy.toml`, run `--reclassify`, and spot-check with:
```bash
python - <<'EOF'
import json; P=json.load(open("data/projects.json"))["projects"]
for p in P[:40]: print(p["score"], p["title"][:40], p["facets"]["domain"], p["facets"]["form"])
EOF
```

## 4. Source notes (verified 2026-11-19)

| Source | Status | Notes |
| :-- | :-- | :-- |
| Devpost | ✅ | `api/hackathons?search=&per_page=40` (JSON); galleries are HTML with JSON-LD awards; `software/search.json` is newest-first. **Cloudflare blocks requests without an `Accept` header** — `http.py` sends `Accept: */*`. |
| GitHub | ✅ | Search API is 30 req/min (own throttle lane in `http.py`); stars batched over GraphQL. Topics like `makemit` are sparse — name/description search has far higher recall. |
| Build18 | ✅ | Full list embedded in the Next.js RSC payload of `/garage`; details at `/garage/<id>`. |
| AdventureX | ✅ | `POST gallery.adventure-x.cn/api/gallery/public/trpc?trpc-path=public.projects` with body `{"json":{}}` returns every project (mostly software → hardware filter applies). |
| Hackaday.io | ✅ | `/submissions/<slug>/list?page=N` HTML. Winners aren't marked; filtered by likes. New contests auto-discovered from `/contests`. |
| Hackster.io | ⛔ | Contest and submission pages return Cloudflare 403; past-contest GraphQL needs a session token. Needs the official API (OAuth app) — not implemented. |
| OSHWHub 立创开源 | ⚠️ | `api/activities/competition_list` lists contests; no public endpoint lists projects *within* an activity (`/api/competition/getActivitiesProjects` → 401). |
| MakeMIT 2024–2025, HackMIT 2021/22/24/25 | ⚠️ | Not on Devpost; GitHub search partly covers them. |

## 5. Backlog (good next tasks)

- [ ] Hackster: integrate via the official API if a token is provided as a repo secret.
- [ ] OSHWHub: find a public listing for contest entries (e.g. 电赛 / 星火计划) or add hand-verified picks.
- [ ] More Chinese sources: 地瓜机器人黑客松 past works, 全国大学生电子设计竞赛 open-source entries, 华为/大疆 RoboMaster open-source.
- [ ] European / Asian makeathons (TUM Makeathon, ETH, HKUST, NUS/SUTD) once they publish galleries.
- [ ] Per-project "BOM / FSM architecture" deep-dives for the top picks (link from `note_zh`).
