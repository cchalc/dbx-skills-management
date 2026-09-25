# Architecture & design rationale

## The idea

A governance + improvement loop for **agent skills** on Databricks:

1. **Define behavior** — an [Agent Behavior](https://www.agentbehavior.dev/) spec
   (Intent / Evidence / Decision / Execution / Recovery) is the target.
2. **Record traces** — MLflow 3.9+ captures agent runs; traces land in UC (OTel span tables).
3. **Evaluate** — `mlflow.genai.evaluate()` with a **Guidelines scorer** (the behavior spec as an
   LLM-judge rubric) scores the trace.
4. **Optimize** — `mlflow.genai.optimize_prompts()` / GEPA (`optimize_anything`) take the scorer as objective.
5. **Enforce** — Claude Code runtime hooks (`PreToolUse`/`PostToolUse`) block violations locally;
   Databricks-deployed agents enforce via endpoint/Genie ACLs + guardrails.
6. **Govern** — register the vetted skill/prompt as a Unity Catalog asset.

## Honest framing (the blog's thesis)

There is **no first-class "skill/agent/prompt" UC securable** today. Real governance paths:
UC **Functions** (tools), UC **Registered Models** (agents via Agent Framework / serving), and the
emerging **MLflow Prompt Registry**. "Skill as a UC securable" is the frontier — `ai-kitchen-dbx`
is already prototyping it (`workspace-skills/docs/uc-skills-migration.md`). That gap *is* the story.

## Why this hub

Single repo holds research, the skill, the bundle, and blog source so the whole loop is one
reviewable unit and publishable assets sit next to the code that produced them. It **extends**
`ai-kitchen-dbx` (skills DAB + UC-skills migration) rather than reinventing it.

## Key decisions

- Research runs as a **field-lab Expedition** (`deep_research/lab/expedition-governed-agent-skills/`),
  local + dogfooded; keepers promote to the Obsidian vault and mirror into `research/`.
- Blog on **prose.sh** (rsync-over-SSH). `pgit` is not a pico service; use Pages for static if needed.
- FEVM workspace `fevm-cjc-ssa-ops3`; UC catalog `dbx_skills_mgmt` (proposed).
