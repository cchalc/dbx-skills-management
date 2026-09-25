# Lessons (append-only)

- **2026-09-25 — GitHub auth was already correct.** `git@github.com` → cchalc (personal key
  `id_ed25519`); `git@github-work` → christopher-chalcraft_data (EMU, `id_ed25519_work`). Clone
  personal repos over plain `github.com`; no new SSH alias needed. `gh` had all 3 accounts logged in.
- **2026-09-25 — prose.sh publishes via rsync/scp over SSH, not git-push.** Keep a local git source of
  truth and sync. `pgit` is NOT a pico.sh service (Pages = static hosting, Patchbin = git patches).
- **2026-09-25 — The loop is real on Databricks.** MLflow 3.9+ UC trace ingestion; `genai.evaluate()`
  Guidelines scorer = behavior spec as LLM-judge; `optimize_prompts()`/GEPA take the scorer as objective.
- **2026-09-25 — No native "skill" UC securable yet.** Wrap as UC function / registered model / MLflow
  prompt; follow `ai-kitchen-dbx/workspace-skills/docs/uc-skills-migration.md`. This gap is the blog thesis.
- **2026-09-25 — Reuse ai-kitchen-dbx.** It already has the skills DAB (`workspace_skills`,
  `reconcile_skills`) and a UC-skills migration in progress. Extend, don't reinvent.
- **2026-09-25 — FEVM auth: use profile `fevm`, not `fevm-cjc-ssa-ops3`.** Both map to
  `fevm-cjc-ssa-ops3.cloud.databricks.com`, but `fevm-cjc-ssa-ops3`'s OAuth refresh token is expired
  (needs interactive `databricks auth login`). `fevm` has valid creds. `fevm-cjc` is a DIFFERENT workspace.
- **2026-09-25 — Catalog plan → schema, not new catalog.** FEVM already has `cjc_ssa_ops3_catalog`
  (MANAGED, Chris's). Create a project **schema** there (e.g. `dbx_skills_mgmt`) instead of a new
  top-level catalog (avoids needing metastore CREATE CATALOG). Other catalogs: ops_data, de_workshop,
  fevm_shared_catalog, system, samples.
