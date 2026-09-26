# AGENTS.md — how we work in this repo

Working agreement for any agent (or human) doing work here. This is a **development
practice**, not a suggestion — follow the loop below for every unit of work.

## The loop (regroup → isolate → build → check → record → merge)

1. **Regroup first.** Before starting a unit of work, restate the goal in one line, read
   `checkpoint.md`, and check state (`jj status`, `jj log`, `wt list`). Decide the *smallest*
   next step. Do not barrel ahead through multiple phases without pausing to reassess.
2. **Isolate the work in a worktree.** Use **worktrunk**: `wt switch --create <branch>` for each
   unit of work so `main` stays clean and parallel work doesn't collide. Keep branches small.
3. **Use jj for version control.** This repo is **colocated jj + git**. Commit small, descriptive
   changes with `jj describe -m "..."`; publish with `jj git push`. Every commit message ends with:
   `Co-authored-by: Isaac <no-reply@databricks.com>`.
4. **Run checks/tests along the way — before committing a decision.** Validate, don't assume:
   - Bundles: `databricks bundle validate` (profile `fevm` for the FEVM workspace).
   - Databricks probes: run the real thing on compute (serverless job) and read the result.
   - Skills: review structure/frontmatter (`plugin-builder:review-skill`) before relying on it.
   - Record *what* you checked and the outcome. A green check is a decision input, not a formality.
5. **Update the living docs every session.** Keep three files current:
   - `checkpoint.md` — where we are / what's next (rewrite the Next section each session).
   - `tasks.md` — check off what's done, add what's discovered.
   - `lessons.md` — append-only; record every non-obvious finding, gotcha, or decision + its why.
6. **Merge deliberately.** After checks pass, merge back (`wt merge`) and push. If a worktrunk hook
   needs approval in a non-interactive run, **stop and ask the human** — never pass `--yes` on their
   behalf (it's a trust decision about running arbitrary commands).

## Repo facts

- **VCS:** colocated jj + git. Remote `git@github.com:cchalc/dbx-skills-management.git` uses the
  **personal `cchalc`** identity (`github.com` → `id_ed25519`). jj authors as the personal gmail identity.
- **Databricks:** FEVM workspace, profile **`fevm`** (not `fevm-cjc-ssa-ops3` — its token is expired).
  Project schema: `cjc_ssa_ops3_catalog.dbx_skills_mgmt`.
- **Research:** runs as a field-lab **Expedition** at `../CoWork/deep_research/lab/expedition-governed-agent-skills/`
  (local, not synced). Keepers promote to the Obsidian vault and mirror into `research/` here.

## Not adopted (deliberately)

- **Spec-driven development:** no `specs/` directory. If we later want acceptance-criteria-driven
  work, run `/spec` and add `specs/PROJECT.md`. Until then, proceed without a spec.

## Why this exists

Going fast ("go wide") without regrouping and checking produces confident-but-wrong decisions and
messy history. This loop keeps changes small, verified, isolated, and documented — so the work is
reviewable and the reasoning survives across sessions.
