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
- [ ] FEVM probes: MLflow UC trace ingestion, `genai.evaluate()` Guidelines scorer, UC function/model round-trip
- [x] Promote keepers to Obsidian (idea note → in-progress) + mirror to `research/governed-agent-skills-findings.md`

## Phase 3 — Skill
- [ ] Author `databricks-blog-forge` in `skill/SKILL.md`
- [ ] Dual-distribution wiring (vibe marketplace / workspace-UC via reconcile DAB)

## Phase 4 — Databricks build-out
- [ ] UC catalog `dbx_skills_mgmt` (schemas: research, traces, skills, models)
- [ ] DAB in `bundle/` extending `reconcile_skills`; validate + deploy `-t fevm -p fevm-cjc-ssa-ops3`

## Phase 5 — Blog pipeline
- [ ] pico.sh account + SSH key (user action)
- [ ] `blog/sync.sh` → prose.sh; first post ("Can a skill be a Unity Catalog securable?")
- [ ] Decide fate of old `cchalc/blog` (archive/repurpose)
