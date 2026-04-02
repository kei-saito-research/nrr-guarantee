# Energy Priority-Resolution Horizon Stability Artifact Repair Memo v1

## Status
- Date: 2026-03-17
- Type: artifact repair memo
- Scope: record the audit repair needed after the first Gemini horizon-stability run was found to rely on a malformed CSV serialization
- Not a manuscript claim memo

## 1. Problem
The original row artifact
- `energy_priority_resolution_horizon_stability_run_input_v1_2026-03-17.csv`

serialized natural-language fields with commas without CSV quoting.

As a result:
- `csv.DictReader` produced an extra `None` key
- later-user content was split across unintended columns
- the first Gemini run output inherited an empty-header response artifact

## 2. Consequence
The first Gemini run under:
- `priority_resolution_horizon_stability_probe_20260317T050209Z`

is not audit-clean and should not be used as the active read for this family.

Treat it as superseded by the repaired rerun below.

## 3. Repair
The exact intended frozen row content has been reserialized cleanly as:
- `energy_priority_resolution_horizon_stability_run_input_v2_2026-03-17.csv`

The horizon runner now also rejects malformed extra-column CSV input instead of silently proceeding.

## 4. Repaired Active Run
Repaired Gemini rerun:
- `priority_resolution_horizon_stability_probe_20260317T051637Z`

Use this rerun and its downstream annotation artifacts as the active evidence state for the family.
