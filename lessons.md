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
- **2026-09-26 — FEVM verification succeeded (us-east-1, MLflow 3.16.1).** UC trace ingestion + trace
  tables work; `genai.evaluate()` Guidelines scorer for `exact-authority` = 1.0 (judge
  `databricks-gpt-5-6-sol`, 54 endpoints); UC function is grantable. define→trace→evaluate proven live.
- **2026-09-26 — Development practice adopted (see AGENTS.md).** regroup → worktree (worktrunk) → jj
  commit → run checks → update living docs → merge. Bootstrap exception: AGENTS.md itself committed
  straight to main (it defines the practice). `.config/wt.toml` pre-merge hooks deferred to Phase 4
  (when `databricks bundle validate` becomes a real gate) rather than adding a hook that can't run yet.
- **2026-09-26 — jj and worktrunk do NOT compose in a colocated repo.** `wt switch --create` makes a
  *git-only* worktree with no `.jj`; `jj -R <worktree>` errors "no jj repo". Verified, then reverted.
  Confirmed via ai-kitchen-dbx: it has no active wt worktrees (`.git/wt/` only holds worktrunk's cache),
  jj runs in the main checkout. **Decision:** for this jj-primary repo, isolate with jj (bookmarks /
  `jj new` / `jj workspace add`), not `wt switch --create`. worktrunk is for git-primary repos + parallel
  sub-agent handoffs (git-only children). AGENTS.md item 2/6 corrected accordingly.
- **2026-09-26 — FEVM metastore is at the registered-model quota (5000/5000).** A DAB
  `registered_models` resource → `QUOTA_EXCEEDED` (POST /unity-catalog/models). So "skill as UC
  registered model" is blocked in this shared metastore. **Pivot:** the "skill as UC securable" claim
  rests on UC **functions** (verified Phase 2, not quota-bound); the bundle deploys a `forge_verify`
  job (Guidelines eval) instead. `scripts/register_skill_model.py` kept as reference for when quota frees.
- **2026-09-26 — `.config/wt.toml` pre-merge hooks don't fit the jj-merge flow.** worktrunk pre-merge
  hooks fire on `wt merge`; we merge via jj fast-forward, so they'd never run. Decision: no wt.toml
  hook; `databricks bundle validate --strict` is a MANUAL pre-merge check per AGENTS.md (ran it: OK).
