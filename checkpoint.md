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

## Next
- Phase 1.5: initial commit + `jj git push` (done as part of this checkpoint).
- Phase 2: create field-lab Expedition and capture the completed research as member trips; then FEVM probes.
- Phases 3–5: `databricks-blog-forge` skill, DAB + schema in `cjc_ssa_ops3_catalog`, prose.sh pipeline.

## Notes / interactive steps still needed from Chris
- prose.sh: create a pico.sh account + register an SSH key (Phase 5).
- Re-auth `fevm-cjc-ssa-ops3` only if we specifically need it — `fevm` covers the same workspace.
- MLflow UC trace ingestion is preview + region-limited — verify FEVM region early (Phase 2 probe).
