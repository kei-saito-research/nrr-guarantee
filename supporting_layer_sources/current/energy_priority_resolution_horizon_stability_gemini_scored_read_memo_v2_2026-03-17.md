# Energy Priority-Resolution Horizon Stability Gemini Scored Read Memo v2

## Status
- Date: 2026-03-17
- Type: repaired scored read memo
- Scope: record the assistant-side annotation read for the repaired Gemini-only horizon-stability execution
- Depends on:
  - [energy_priority_resolution_horizon_stability_artifact_repair_memo_v1_2026-03-17.md](energy_priority_resolution_horizon_stability_artifact_repair_memo_v1_2026-03-17.md)
  - [energy_priority_resolution_horizon_stability_run_annotation_gemini_v2_2026-03-17.csv](energy_priority_resolution_horizon_stability_run_annotation_gemini_v2_2026-03-17.csv)
- Not a provider-balanced memo
- Not a manuscript claim memo

## 1. Active Annotation Artifact
- [energy_priority_resolution_horizon_stability_run_annotation_gemini_v2_2026-03-17.csv](energy_priority_resolution_horizon_stability_run_annotation_gemini_v2_2026-03-17.csv)

## 2. Template-by-Checkpoint `appropriate`
- `A_trip_planning`
  - `turn7`: `2/4`
  - `turn9`: `4/4`
  - `turn11`: `0/4`
- `B_hiring_packet`
  - `turn7`: `4/4`
  - `turn9`: `4/4`
  - `turn11`: `2/4`
- `C_incident_response`
  - `turn7`: `4/4`
  - `turn9`: `0/4`
  - `turn11`: `0/4`

## 3. Checkpoint Totals
Across all `12` episodes:

- `turn7`
  - `chosen_side_direction_progress_present = 10/12`
  - `user_detail_use_present = 12/12`
  - `unresolved_relation_preserved_or_narrowly_checked = 12/12`
  - `suspended_main_reference_absent = 12/12`
  - `starter_question_repeat_absent = 12/12`
  - `appropriate = 10/12`
- `turn9`
  - `chosen_side_direction_progress_present = 12/12`
  - `user_detail_use_present = 12/12`
  - `unresolved_relation_preserved_or_narrowly_checked = 8/12`
  - `suspended_main_reference_absent = 12/12`
  - `starter_question_repeat_absent = 12/12`
  - `appropriate = 8/12`
- `turn11`
  - `chosen_side_direction_progress_present = 7/12`
  - `user_detail_use_present = 10/12`
  - `unresolved_relation_preserved_or_narrowly_checked = 6/12`
  - `suspended_main_reference_absent = 12/12`
  - `starter_question_repeat_absent = 12/12`
  - `appropriate = 2/12`

## 4. Current Read
The repaired Gemini-only scored read is narrower and more usable than the superseded malformed-run read.

What holds:
- the suspended original main objective stays quarantined across all checkpoints
- `turn7` is largely stable in the repaired run
- the family still detects non-uniform degradation depth across templates

Where degradation appears:
- `A` improves through `turn9` and then fails at `turn11`
- `B` stays strong through `turn9` and is mixed at `turn11`
- `C` is the earliest clean failure surface at `turn9`
  - the dominant mode is unsupported ordering commitment

Current family-level read:
- the family is informative because the three templates do not collapse into one trivial error pattern
- by `turn11`, stability is substantially degraded even though the suspended main objective remains quarantined

## 5. Boundary
This repaired scored memo supports:
- using the repaired Gemini evidence as the active provider read
- a narrow judgment about whether one same-family Anthropic replication run is now justified

This repaired scored memo does not support:
- provider-balanced closure by itself
- intervention design choice
- manuscript-facing generalization
