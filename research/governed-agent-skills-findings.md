# Governed agent skills on Databricks — research findings

_Desk research, 2026-09-25. Source of truth: field-lab Expedition
`deep_research/lab/expedition-governed-agent-skills/` (5 trips). **Not yet hands-on-verified in
FEVM** — those probes are the next step. Seeds the first blog post._

## Thesis

A closed loop for agent skills: **define behavior → record traces → evaluate → optimize → enforce → govern.**

## What's confirmed (docs + prior art)

| Loop stage | Mechanism on Databricks | Confidence |
|---|---|---|
| Define behavior | Agent Behavior spec (agentbehavior.dev): Intent/Evidence/Decision/Execution/Recovery | — |
| Record traces | MLflow 3.9+ → UC OTel span tables (`set_experiment_trace_location`); spans carry attributes | docs |
| Evaluate | `mlflow.genai.evaluate()` + **Guidelines scorer** (spec as LLM-judge); `align()` (MemAlign) | docs |
| Optimize | `mlflow.genai.optimize_prompts()` / GEPA / `optimize_anything` take the scorer as objective | docs + skill |
| Enforce | Claude Code runtime hooks (`PreToolUse` can block) locally; endpoint/Genie ACLs on Databricks | mixed |
| Govern | UC **functions** (tools), **registered models** (agents), emerging MLflow **Prompt Registry** | docs |

## The headline (blog thesis)

**There is no first-class "skill/agent/prompt" Unity Catalog securable today.** Governance goes through
UC functions, registered models, and the emerging MLflow Prompt Registry. `ai-kitchen-dbx` already
prototypes skills→UC (`workspace-skills/docs/uc-skills-migration.md`, `catalog.schema.skill-name`).
"Skill as a UC securable" is the **frontier** — and that gap is the story.

## Corrections to earlier assumptions

- **`pgit` is not a pico.sh service.** prose.sh publishes via **rsync/scp over SSH** (not git-push);
  auth is an SSH key on a pico account. Monorepo of posts → this repo's `blog/`.
- **Claude Code has runtime hooks.** `settings.json` `PreToolUse`/`PostToolUse` can block a tool call —
  deterministic local enforcement (an earlier note only found worktrunk *lifecycle* hooks).

## To verify hands-on in FEVM (profile `fevm`)

1. MLflow UC trace ingestion availability (preview, us-east/us-west, 100 traces/s) — confirm FEVM region.
2. A real `mlflow.genai.evaluate()` run with a Guidelines scorer built from a field-lab behavior spec.
3. A UC function + registered-model round-trip (wrap a skill), landing in a `dbx_skills_mgmt` schema
   under `cjc_ssa_ops3_catalog`.
