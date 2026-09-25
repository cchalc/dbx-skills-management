# Checkpoint — where we left off

_Updated 2026-09-25._

## Done
- **Phase 1 auth (verified):** GitHub identities already keyed correctly — `git@github.com` → cchalc
  (personal, `id_ed25519`), `git@github-work` → christopher-chalcraft_data (EMU). No `~/.ssh/config`
  changes needed.
- **Hub repo cloned** to `~/Projects/Databricks/dbx-skills-management`, colocated **jj+git**,
  `main@origin` tracked, authoring as personal gmail identity.
- **Scaffold** created: `research/ skill/ bundle/ blog/posts/` + root living docs.

- **Phase 1.4 FEVM auth (done):** use profile **`fevm`** (valid); `fevm-cjc-ssa-ops3` token expired
  (interactive re-login needed, not blocking). Target **schema `dbx_skills_mgmt` inside
  `cjc_ssa_ops3_catalog`** (no new top-level catalog).

- **Phase 2 research capture (done):** Expedition `lab/expedition-governed-agent-skills/` with 5 member
  trips (behavior-and-traces, uc-securable, optimization-loop, hooks-enforcement, blog-pipeline),
  validated. Promoted to Obsidian idea note (→ in-progress) + mirrored to
  `research/governed-agent-skills-findings.md`.

## Next
- **Phase 2.6 — FEVM hands-on probes** (profile `fevm`): confirm MLflow UC trace-ingestion availability
  (preview/region), a `genai.evaluate()` Guidelines run, and a UC function + registered-model round-trip
  into a `dbx_skills_mgmt` schema under `cjc_ssa_ops3_catalog`. Needs Databricks compute execution.
- Phases 3–5: `databricks-blog-forge` skill, DAB + schema, prose.sh pipeline (pico account = user action).

## Notes / interactive steps still needed from Chris
- prose.sh: create a pico.sh account + register an SSH key (Phase 5).
- Re-auth `fevm-cjc-ssa-ops3` only if we specifically need it — `fevm` covers the same workspace.
- MLflow UC trace ingestion is preview + region-limited — verify FEVM region early (Phase 2 probe).
