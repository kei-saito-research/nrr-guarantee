#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CURRENT_DIR="$ROOT/manuscript/current"
MAIN_TEX="$(find "$CURRENT_DIR" -maxdepth 1 -type f -name 'nrr-guarantee_manuscript_v*.tex' | sort -V | tail -n 1)"
OUT_DIR="${1:-/tmp/nrr-guarantee_current_build}"

if [ -z "$MAIN_TEX" ]; then
  echo "No current manuscript TeX found in $CURRENT_DIR" >&2
  exit 1
fi

mkdir -p "$OUT_DIR"
cd "$CURRENT_DIR"

if command -v tectonic >/dev/null 2>&1; then
  if tectonic -X compile --only-cached --outdir "$OUT_DIR" "$(basename "$MAIN_TEX")"; then
    exit 0
  fi
fi

if command -v cupsfilter >/dev/null 2>&1; then
  OUT_PDF="$OUT_DIR/$(basename "${MAIN_TEX%.tex}.pdf")"
  echo "Falling back to source-rendered PDF via cupsfilter (cached TeX resources unavailable)." >&2
  cupsfilter -i text/plain -m application/pdf "$MAIN_TEX" > "$OUT_PDF"
  exit 0
elif command -v latexmk >/dev/null 2>&1; then
  latexmk -pdf -interaction=nonstopmode -halt-on-error -output-directory="$OUT_DIR" "$(basename "$MAIN_TEX")"
else
  echo "No available manuscript build tool (tectonic cache miss, cupsfilter unavailable, and latexmk unavailable)." >&2
  exit 1
fi
