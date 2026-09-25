# bundle/

Databricks Asset Bundle for deploying the skill/prompt + MLflow experiment (and optionally a
model-serving endpoint) into the FEVM workspace under the `dbx_skills_mgmt` catalog.

Extends the `ai-kitchen-dbx` pattern:
`ai-kitchen-dbx/workspace-skills/bundles/skills/databricks.yml` (bundle `workspace_skills`,
serverless `reconcile_skills` job) and the UC-skills migration in
`ai-kitchen-dbx/workspace-skills/docs/uc-skills-migration.md`.

Deploy: `databricks bundle validate` then `databricks bundle deploy -t fevm -p fevm-cjc-ssa-ops3`.
Lands in Phase 4.
