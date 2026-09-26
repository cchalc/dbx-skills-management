# Checkpoint — where we left off

_Updated 2026-09-25._

## Done
- **Phase 1 auth (verified):** GitHub identities already keyed correctly — `git@github.com` → cchalc
  (personal, `id_ed25519`), `git@github-work` → christopher-chalcraft_data (EMU). No `~/.ssh/config`
  changes needed.
- **Hub repo cloned** to `~/Projects/Databricks/dbx-skills-management`, colocated **jj+git**,
  `main@origin` tracked, authoring as personal gmail identity.
- **Scaffold** created: `research/ skill/ bundle/ blog/posts/` + root living docs.

- **Phase 1.4 FEVM auth (done):** use profile **`fevm`** (valid); `fevm-cjc-ssa-ops3` token expired
  (interactive re-login needed, not blocking). Target **schema `dbx_skills_mgmt` inside
  `cjc_ssa_ops3_catalog`** (no new top-level catalog).

- **Phase 2 research capture (done):** Expedition `lab/expedition-governed-agent-skills/` with 5 member
  trips (behavior-and-traces, uc-securable, optimization-loop, hooks-enforcement, blog-pipeline),
  validated. Promoted to Obsidian idea note (→ in-progress) + mirrored to
  `research/governed-agent-skills-findings.md`.

- **Phase 2.6 FEVM probes (done 2026-09-26):** us-east-1, MLflow 3.16.1. UC trace ingestion ✅ (trace
  tables in `cjc_ssa_ops3_catalog.dbx_skills_mgmt`), `genai.evaluate()` Guidelines scorer for
  `exact-authority` ✅ = 1.0 (judge `databricks-gpt-5-6-sol`), UC function round-trip ✅ (grantable).
  **Phase 2 complete.** Recorded into field-lab trips + research mirror + Obsidian note.

## Working practice (now in force — see AGENTS.md)
regroup → worktree (`wt switch --create`) → jj commit → run checks → update living docs → merge.

## Next
- **Phase 3 — skill (in a worktree):** author `databricks-blog-forge` in `skill/SKILL.md`; review it
  (`plugin-builder:review-skill`) before merging.
- **Phase 4 — DAB:** bundle in `bundle/` extending `reconcile_skills`; register skill/prompt/model +
  MLflow experiment into `cjc_ssa_ops3_catalog.dbx_skills_mgmt`; wrap a skill as a registered model
  (the one deferred probe); optionally run `optimize_prompts`/GEPA once.
- **Phase 5 — blog:** prose.sh (pico account + SSH key = Chris's action); first post from the research.

## FEVM scratch left in place (evidence; safe to keep)
- schema `cjc_ssa_ops3_catalog.dbx_skills_mgmt` + `behavior_echo` function
- experiments `/Users/christopher.chalcraft@databricks.com/fevm-probe-eval` and `-traces` + trace tables
- notebook `/Workspace/Users/christopher.chalcraft@databricks.com/.ai_dev_kit/fevm_mlflow_probe`

## Notes / interactive steps still needed from Chris
- prose.sh: create a pico.sh account + register an SSH key (Phase 5).
- Re-auth `fevm-cjc-ssa-ops3` only if we specifically need it — `fevm` covers the same workspace.
- MLflow UC trace ingestion is preview + region-limited — verify FEVM region early (Phase 2 probe).
