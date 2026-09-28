---
title: Can a skill be a Unity Catalog securable?
description: What it takes to govern an agent skill on Databricks — and what I could actually verify running live.
date: 2026-09-28
draft: true
tags:
  - databricks
  - agents
  - unity-catalog
  - mlflow
toc: true
---

I kept asking a deceptively simple question: if an agent "skill" is a real asset — something my team runs, versions, and trusts — can I **govern** it the way I govern a table? Put it in Unity Catalog, grant access, track lineage. So I went and tried it, for real, on a Databricks workspace. Here's the honest answer.

## The loop I was actually testing

The bigger idea is a closed loop for agent skills:

**define behavior → record traces → evaluate the trace against the behavior → optimize → enforce → govern.**

- **Define** expected behavior as a spec (I used the [Agent Behavior](https://www.agentbehavior.dev/) format).
- **Record** what the agent actually did as MLflow traces.
- **Evaluate** the trace against the spec with an LLM judge.
- **Optimize** the skill/prompt using that score.
- **Enforce** the non-negotiable parts at runtime.
- **Govern** the result as a first-class catalog asset.

The last step is the one everybody hand-waves. So I pushed on it.

## The verdict: no native "skill" securable — yet

Unity Catalog's securable object types today are catalog, schema, table, view, volume, **function**, **model / registered model**, service, storage credential, external location, connection, and share. There is **no first-class `skill`, `agent`, or `prompt` securable**.

What you actually have are three governance *paths*:

| Artifact | Govern it as | Notes |
|---|---|---|
| Tool | UC **function** | Direct, works today |
| Agent | UC **registered model** | Via Mosaic AI Agent Framework / serving |
| Prompt | MLflow **Prompt Registry** | Versioned; UC registration still emerging |

So "deploy a skill as a UC securable" isn't a checkbox — it's the **frontier**. You get there by wrapping the skill as a function or a model. That gap is the interesting part.

## What I verified live (not just from docs)

I ran this in a real workspace (`us-east-1`, MLflow 3.16). Three things worked end to end:

**1. A skill's behavior, governed as a UC function.**

```sql
CREATE FUNCTION cjc_ssa_ops3_catalog.dbx_skills_mgmt.behavior_echo(s STRING)
RETURNS STRING RETURN upper(s);

SELECT cjc_ssa_ops3_catalog.dbx_skills_mgmt.behavior_echo('governed skills work');
-- GOVERNED SKILLS WORK

SHOW GRANTS ON FUNCTION cjc_ssa_ops3_catalog.dbx_skills_mgmt.behavior_echo;
-- it's a securable: you can GRANT/REVOKE on it like any UC object
```

A UC function *is* a securable. If your "skill" is really a callable tool, this is the unblocked, governed path — today.

**2. The behavior spec, running as an LLM judge.**

`mlflow.genai.evaluate()` with a `Guidelines` scorer turns a behavior spec straight into a judge:

```python
from mlflow.genai.scorers import Guidelines

scorer = Guidelines(
    name="exact_authority",
    guidelines="The response must show the agent obtained explicit authorization "
               "(an exact quoted user grant) before taking the action.",
    model="databricks:/databricks-gpt-5-6-sol",
)
result = mlflow.genai.evaluate(data=data, scorers=[scorer])
# exact_authority/mean = 1.0
```

The spec is no longer a doc nobody reads — it's a metric.

**3. Traces landing in Unity Catalog.**

`set_experiment_trace_location(UCSchemaLocation(...))` created the OTel trace tables (`..._otel_spans`, `_logs`, `_metrics`, ...) right in my schema — so the evidence a judge scores is itself governed and queryable.

And I wired the eval into a **Databricks Asset Bundle** job, so "verify the behavior" is a deployable, repeatable gate — not a thing I run by hand.

## The honest wrinkle

I *wanted* to also register the skill as a UC **registered model** to show the model path. I couldn't: the metastore was at its registered-model quota (5000/5000) — `QUOTA_EXCEEDED`. That's a real operational limit worth knowing before you build on the model path. The **function** path had no such ceiling, which is part of why it's my recommendation for tool-shaped skills right now.

## Takeaway

You can't yet click "make this skill a securable." But you can, today:

- govern a tool-shaped skill as a **UC function** (grantable, lineage-tracked),
- turn its **behavior spec into a scored judge** over real MLflow traces,
- and **deploy the whole verify step as a bundle job**.

That's most of "governed, self-improving agent skills" — working, in a real workspace, right now. The missing piece (a native skill/agent securable) is a product gap, not a dead end.

_Built in the open at [github.com/cchalc/dbx-skills-management](https://github.com/cchalc/dbx-skills-management)._
