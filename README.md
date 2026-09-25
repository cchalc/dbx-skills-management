# dbx-skills-management

Hub repo for the **governed, self-improving agent skills** project and blog series.

The thesis: a closed loop for agent skills on Databricks —
**define expected behavior → record MLflow traces → evaluate the trace against the
behavior spec → optimize (GEPA) → enforce (hooks) → govern as a Unity Catalog asset.**

## Layout

| Path | Purpose |
|------|---------|
| `research/` | Publishable research assets (mirrors of promoted Obsidian notes) |
| `skill/` | The `databricks-blog-forge` skill (research → content → publish) |
| `bundle/` | Databricks Asset Bundle — reconcile job + UC registration (extends `ai-kitchen-dbx`) |
| `blog/` | prose.sh source (markdown posts + `_styles.css`/`_footer.md`/`_readme.md` + `sync.sh`) |

Living docs at root: `architecture.md`, `checkpoint.md`, `tasks.md`, `lessons.md`.

## VCS & identity

- Colocated **jj + git**; publish with `jj git push`.
- Remote uses the **personal** identity: `git@github.com:cchalc/dbx-skills-management.git`
  (`github.com` → `id_ed25519` → cchalc). EMU repos use the `github-work` alias.
- Worktrees managed by **worktrunk** (`wt`), defaults.

## Databricks

- Build-out workspace: **FEVM** (`fevm-cjc-ssa-ops3.cloud.databricks.com`), profile `fevm-cjc-ssa-ops3`.
- Reuses patterns from `ai-kitchen-dbx/workspace-skills/` (skills DAB + UC-skills migration).

## Blog

- Platform: **prose.sh** (pico.sh). Publish via `rsync`/`scp` over SSH (not git-push).
  `blog/` is the source of truth; `blog/sync.sh` pushes to prose.sh.
