#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CURRENT_DIR="$ROOT/manuscript/current"
MANIFEST="$ROOT/manuscript/checksums_active_review_surface_sha256.txt"

current_files=()
while IFS= read -r file; do
  current_files+=("$file")
done < <(find "$CURRENT_DIR" -maxdepth 1 -type f | LC_ALL=C sort)

if [ "${#current_files[@]}" -ne 2 ]; then
  echo "Active review surface must contain exactly 2 files in $CURRENT_DIR" >&2
  exit 1
fi

cd "$ROOT"
shasum -a 256 -c "$MANIFEST"
