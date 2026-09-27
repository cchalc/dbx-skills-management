# Project summary — governed, self-improving agent skills

_Review snapshot, 2026-09-27. Status: **Phases 1–4 done & pushed; paused before Phase 5 (blog publish, blocked on your pico.sh setup).**_

## What this is

Turning one thesis into real, deployable work **and** a blog series:

> A closed loop for agent skills on Databricks — **define behavior → record MLflow traces →
> evaluate the trace against the behavior spec → optimize (GEPA) → enforce (hooks) → govern as a
> Unity Catalog asset.**

Hub repo: `github.com/cchalc/dbx-skills-management` (this repo). Build workspace: FEVM
(`fevm-cjc-ssa-ops3.cloud.databricks.com`, profile `fevm`). Research: a local field-lab Expedition.

## Program status

| Phase | What | Status |
|---|---|---|
| 1 | Foundations: GitHub auth, hub repo, jj+worktrunk, scaffold | ✅ pushed |
| 2 | Research (5-trip field-lab Expedition) + **live FEVM verification** | ✅ pushed |
| 3 | `databricks-blog-forge` skill (full orchestrator) | ✅ pushed |
| 4 | DAB: validated, deployed, behavior-verify job ran green | ✅ pushed |
| — | Development practice codified in `AGENTS.md` (self-corrected) | ✅ pushed |
| 5 | Blog publish to prose.sh | ⏸️ blocked on your pico.sh account + SSH key |

Commit trail on `main` (newest first): `ceef342` Phase 4 · `b9369a7` Phase 3 · `4a9d689` practice fix ·
`7ef92ac` practice · `d2e1fd9` Phase 2.6 verify · `fe998162` Phase 2 research · `7619357` scaffold.

## What's verified live in FEVM (us-east-1, MLflow 3.16.1)

The loop is **proven**, not just documented:
- **Trace ingestion:** `set_experiment_trace_location` created UC trace tables in
  `cjc_ssa_ops3_catalog.dbx_skills_mgmt` (`..._otel_spans/_logs/_metrics/_metadata/_unified`).
- **Evaluate:** `mlflow.genai.evaluate()` + a Guidelines scorer encoding the `exact-authority`
  behavior spec scored **1.0** — both in a probe (run `0218b551…`) and via the **deployed DAB job**
  `forge_verify` (job `738520750404141`, run `d825e785…`, `TERMINATED SUCCESS`).
- **Govern:** UC **function** `cjc_ssa_ops3_catalog.dbx_skills_mgmt.behavior_echo` created, called,
  `SHOW GRANTS` confirms it's a securable. (54 serving endpoints available as judges.)

## Key findings & decisions (all in `lessons.md`)

- **jj ≠ worktrunk in a colocated repo.** `wt switch --create` makes a *git-only* worktree with no
  `.jj`; jj can't run in it. → jj is the isolation layer here (bookmarks); worktrunk is for git-primary
  repos + sub-agent handoffs. `AGENTS.md` corrected.
- **Metastore at the registered-model quota (5000/5000).** "Skill as a UC *registered model*" is blocked
  here → the securable claim rests on UC **functions**. `bundle/scripts/register_skill_model.py` kept for
  when quota frees.
- **`pgit` is not a pico service.** prose.sh publishes via **rsync/scp over SSH** (not git-push).
- **Claude Code has runtime hooks** (`PreToolUse` can block) → deterministic local enforcement; Databricks
  agents enforce via endpoint/Genie ACLs.
- **FEVM auth:** use profile `fevm` (the `fevm-cjc-ssa-ops3` profile's token is expired).

## The development practice (now in force — `AGENTS.md`)

**regroup → isolate (jj bookmark) → build → check → record → merge.** Every phase followed it; checks
(`bundle validate --strict`, the deployed job, frontmatter/refs) gated each merge; living docs updated
each session; commits carry the org attribution.

## Where things live

- **Repo build:** `research/` (findings mirror), `skill/SKILL.md` (blog-forge), `bundle/` (DAB + scripts),
  `blog/` (prose.sh source + `sync.sh`), living docs at root.
- **Research (local, not synced):** field-lab Expedition
  `../CoWork/deep_research/lab/expedition-governed-agent-skills/` (5 trips).
- **Obsidian vault:** `Research/Topics/Governed Agent Skills on Databricks - Project Idea` (+ MOC link).
- **FEVM scratch (evidence, safe to keep):** schema `cjc_ssa_ops3_catalog.dbx_skills_mgmt`, the
  `behavior_echo` function, experiments `fevm-probe-*` + `dbx-skills-management-forge`, the `forge_verify`
  job, and notebook `/Workspace/Users/christopher.chalcraft@databricks.com/.ai_dev_kit/fevm_mlflow_probe`.

## To resume (next session)

1. **Phase 5 (needs you first):** create a pico.sh account + register an SSH key, then `blog/sync.sh`
   (dry-run, then `--live`). Draft the first post from `research/governed-agent-skills-findings.md`
   — "Can a skill be a Unity Catalog securable?" — embedding the verified evidence above.
2. **Optional loop-closer:** run `optimize_prompts`/GEPA once against the Guidelines scorer.
3. **When metastore quota frees:** `databricks bundle run` a version of `register_skill_model.py`.

See `checkpoint.md` for the live "where we are / next" and `tasks.md` for the phase checklists.
