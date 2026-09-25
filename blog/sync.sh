#!/usr/bin/env bash
# Publish the blog to prose.sh (pico.sh) via rsync over SSH.
#
# Prereq (one-time, interactive): create a pico.sh account and register your SSH
# public key — see https://pico.sh/ and https://pico.sh/prose . prose.sh uses the
# same SSH identity as your other pico services; no password/token.
#
# This is NOT git-push. `blog/` (this dir) is the source of truth; running this
# syncs the current posts + config to your prose.sh blog.
set -euo pipefail
cd "$(dirname "$0")"

# Dry-run by default; pass --live to actually publish.
RSYNC_OPTS=(-rv --itemize-changes)
if [[ "${1:-}" != "--live" ]]; then
  RSYNC_OPTS+=(--dry-run)
  echo ">> DRY RUN (pass --live to publish). Files that WOULD sync:"
fi

# prose.sh renders top-level markdown as posts; _readme.md/_footer.md/_styles.css are config.
rsync "${RSYNC_OPTS[@]}" \
  posts/ _readme.md _footer.md \
  $( [[ -f _styles.css ]] && echo _styles.css ) \
  prose.sh:/
