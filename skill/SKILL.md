---
name: databricks-blog-forge
description: >-
  Research, verify on Databricks, and publish a Databricks/agents blog post end to end.
  Use when the user wants to turn a technical claim or finding into a published prose.sh
  post backed by REAL Databricks evidence: it orchestrates a field-lab research Expedition,
  drafts the post, spins up a FEVM scratch schema + MLflow experiment to verify claims
  (trace ingestion, genai.evaluate, UC functions), then publishes via rsync to prose.sh.
  Triggers on "forge a blog post", "write and verify a Databricks post", "blog this finding",
  "turn this into a verified post". NOT for general Databricks work (use the databricks-*
  skills directly), non-technical writing, or publishing something that has no claim to verify.
compatible-agents: claude-code
---

# Databricks Blog Forge

Turn a technical claim into a **published, evidence-backed** blog post. The whole point:
nothing gets published that wasn't verified on real Databricks compute first.

Follow the repo's development practice in [`AGENTS.md`](../AGENTS.md) throughout:
**regroup → isolate (jj) → build → check → record → merge.** Do each stage on a jj bookmark,
update the living docs, and never publish unverified claims.

## Prerequisites

- **Databricks:** authenticated CLI; FEVM profile **`fevm`** (see `databricks-core`). Verify:
  `databricks auth describe -p fevm`.
- **Publish target:** a pico.sh account with a registered SSH key (one-time, interactive — the user
  does this; see `blog/sync.sh`). If absent, do stages 1–3 and stop before publishing.
- **Research home:** the field-lab skill + its built CLIs; the Expedition lives locally under
  `deep_research/lab/` (not synced).

## The pipeline (4 stages)

### 1. Research — field-lab Expedition
Invoke the **field-lab** skill. Start or continue an Expedition (one Field Trip per claim/thread);
gather source-traced findings; keep the raw log local. Promote the keepers to the Obsidian vault and
mirror the publishable summary into this repo's `research/`. Do **not** synthesize a verdict the
sources don't support — record limits and what remains unverified.

### 2. Draft — the post
Write the post as markdown in `blog/posts/<slug>.md` in prose.sh format (frontmatter: `title`,
`description`, `date`, `draft: true`, optional `tags`). Lead with the claim, keep code blocks real,
and leave explicit **[VERIFY]** placeholders wherever a claim needs Databricks evidence. House voice
matches `blog/_readme.md` / `_footer.md`.

### 3. Verify on Databricks — the non-negotiable stage
For each **[VERIFY]** claim, produce real evidence in a FEVM scratch area, then embed it:
- Create/reuse a scratch schema (default `cjc_ssa_ops3_catalog.dbx_skills_mgmt`) and an MLflow
  experiment. Use `databricks-execution-compute` (serverless job) to run Python and
  `databricks-mlflow-evaluation` for the eval APIs.
- Typical checks: MLflow **UC trace ingestion** (`set_experiment_trace_location`), **`genai.evaluate()`**
  with a `Guidelines` scorer (a behavior spec as an LLM judge), a **UC function** round-trip, or an
  `optimize_prompts`/GEPA run. Read the actual result — a failure or "preview not available in region"
  is itself honest evidence to report, not something to hide.
- Replace each **[VERIFY]** with the concrete result (metric value, table names, run id) and cite how
  it was produced (job run id, notebook path). Keep the probe notebook under
  `/Workspace/Users/<user>/.ai_dev_kit/` and note it.

Guardrail: if a claim can't be verified, soften it to what the evidence supports or cut it. Never
publish an unverified assertion as fact.

### 4. Publish — prose.sh
When the draft is verified and `draft:` flipped to false, run `blog/sync.sh` (dry-run first, then
`--live`). It rsyncs `blog/` to prose.sh over SSH. Publishing is outward-facing — confirm with the
user before the `--live` push.

## After a run
- Update `checkpoint.md` (where we are), `tasks.md` (done/next), `lessons.md` (append findings).
- Commit each stage on its jj bookmark; fast-forward `main` after a review check; `jj git push`.

## Composes these skills
`field-lab` (research) · `databricks-core` (auth/profile) · `databricks-execution-compute` (run code)
· `databricks-mlflow-evaluation` (traces + eval + optimize) · `databricks-unity-catalog` (functions,
grants) · `databricks-dabs` (when the verified asset should be deployed/registered).

## What this skill does NOT do
- General Databricks tasks unrelated to a post → use the `databricks-*` skills directly.
- Publish anything unverified, or fabricate evidence.
- Create a pico.sh account or SSH key (interactive, user-owned).
