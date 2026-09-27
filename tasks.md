# Tasks

## Phase 1 — Foundations
- [x] Verify GitHub auth (personal vs EMU SSH identities)
- [x] Clone hub repo + colocate jj + track main
- [x] Scaffold hub layout + living docs
- [ ] Databricks auth check for `fevm-cjc-ssa-ops3` + catalog-create permission
- [ ] Initial commit + `jj git push`

## Phase 2 — Research Expedition (field-lab)
- [x] Create `lab/expedition-governed-agent-skills/`
- [x] Member trips: behavior-and-traces, uc-securable, optimization-loop, hooks-enforcement, blog-pipeline
- [x] Capture completed research as instrument readouts (validated, 6 events)
- [x] FEVM probes (2026-09-26): UC trace ingestion ✅, `genai.evaluate()` Guidelines scorer ✅ (1.0), UC function ✅ (registered-model wrap deferred to Phase 4)
- [x] Promote keepers to Obsidian (idea note → in-progress) + mirror to `research/governed-agent-skills-findings.md`

## Phase 3 — Skill
- [x] Author `databricks-blog-forge` in `skill/SKILL.md` (full-orchestrator scope: research → draft → verify on FEVM → publish)
- [ ] Review pass (plugin-builder:review-skill was unavailable this session — did a manual structural check; re-review when available)
- [ ] Dual-distribution wiring (vibe marketplace / workspace-UC via reconcile DAB)

## Phase 4 — Databricks build-out
- [x] Schema `cjc_ssa_ops3_catalog.dbx_skills_mgmt` (created Phase 2)
- [x] DAB in `bundle/` — validates `--strict`, deploys to FEVM (`-t fevm -p fevm`), `forge_verify` job
      **ran green** (exact_authority/mean = 1.0). Governance-as-code = a deployable behavior-eval gate.
- [~] Skill-as-UC-registered-model: BLOCKED by metastore model quota (5000/5000). Pivoted to UC-function
      governance (Phase 2) + `register_skill_model.py` kept as reference for when quota frees.
- [n/a] `.config/wt.toml` pre-merge hook — doesn't fire in the jj-merge flow; `bundle validate` is a
      manual pre-merge check per AGENTS.md.
- [ ] Optional: run `optimize_prompts`/GEPA once to close the loop (deferred).

## Phase 5 — Blog pipeline
- [ ] pico.sh account + SSH key (user action)
- [ ] `blog/sync.sh` → prose.sh; first post ("Can a skill be a Unity Catalog securable?")
- [ ] Decide fate of old `cchalc/blog` (archive/repurpose)
