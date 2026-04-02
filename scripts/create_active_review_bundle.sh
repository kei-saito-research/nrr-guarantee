#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MANIFEST="$ROOT/manuscript/checksums_active_review_surface_sha256.txt"
OUT_ZIP="${1:-/tmp/nrr-guarantee_active_review_surface.zip}"

if [ ! -f "$MANIFEST" ]; then
  echo "Missing active review manifest: $MANIFEST" >&2
  exit 1
fi

mkdir -p "$(dirname "$OUT_ZIP")"

paths=()
while IFS= read -r path; do
  [ -n "$path" ] && paths+=("$path")
done < <(awk '{ $1=""; sub(/^ /, ""); print }' "$MANIFEST")

paths+=("manuscript/checksums_active_review_surface_sha256.txt")

cd "$ROOT"
zip -q -r -FS "$OUT_ZIP" "${paths[@]}"
