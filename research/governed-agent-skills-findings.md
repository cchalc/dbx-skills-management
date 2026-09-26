# Governed agent skills on Databricks — research findings

_Desk research 2026-09-25; **hands-on verified in FEVM 2026-09-26**. Source of truth: field-lab
Expedition `deep_research/lab/expedition-governed-agent-skills/` (5 trips). Seeds the first blog post._

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

## Verified hands-on in FEVM — 2026-09-26 (profile `fevm`, us-east-1, MLflow 3.16.1)

1. ✅ **UC trace ingestion works.** `set_experiment_trace_location(UCSchemaLocation('cjc_ssa_ops3_catalog','dbx_skills_mgmt'))`
   + an emitted `@mlflow.trace` created the trace tables (`..._otel_spans/_logs/_metrics/_metadata/_unified`).
   The preview is enabled in this us-east-1 workspace.
2. ✅ **Eval works.** `mlflow.genai.evaluate()` with a Guidelines scorer encoding the `exact-authority`
   behavior spec scored a sample **1.0** (judge `databricks:/databricks-gpt-5-6-sol`; 54 endpoints available).
3. ✅ **UC function round-trip.** Created + called `cjc_ssa_ops3_catalog.dbx_skills_mgmt.behavior_echo`;
   `SHOW GRANTS` confirms it's a governable securable. (Registered-model wrap: still to do in Phase 4.)

**Net:** define → trace → evaluate is proven live. The optimize step (`optimize_prompts`/GEPA) consumes
exactly this scorer/score — objective source proven; the optimizer run itself is the one piece not yet executed.
