#!/usr/bin/env bash
# Backward-compatible root entry → Unix migrate launcher.
# Prefer: python3 scripts/run.py migrate   or   scripts/unix/migrate.sh
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec bash "$ROOT/scripts/unix/migrate.sh" "$@"
