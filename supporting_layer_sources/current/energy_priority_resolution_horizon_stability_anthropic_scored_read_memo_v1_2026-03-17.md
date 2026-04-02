# Energy Priority-Resolution Horizon Stability Anthropic Scored Read Memo v1

## Status
- Date: 2026-03-17
- Type: scored read memo
- Scope: record the assistant-side annotation read for the Anthropic horizon-stability replication
- Depends on:
  - [energy_priority_resolution_horizon_stability_run_annotation_anthropic_v1_2026-03-17.csv](energy_priority_resolution_horizon_stability_run_annotation_anthropic_v1_2026-03-17.csv)
- Not a manuscript claim memo

## 1. Active Annotation Artifact
- [energy_priority_resolution_horizon_stability_run_annotation_anthropic_v1_2026-03-17.csv](energy_priority_resolution_horizon_stability_run_annotation_anthropic_v1_2026-03-17.csv)

## 2. Template-by-Checkpoint `appropriate`
- `A_trip_planning`
  - `turn7`: `4/4`
  - `turn9`: `4/4`
  - `turn11`: `0/4`
- `B_hiring_packet`
  - `turn7`: `4/4`
  - `turn9`: `0/4`
  - `turn11`: `0/4`
- `C_incident_response`
  - `turn7`: `4/4`
  - `turn9`: `0/4`
  - `turn11`: `0/4`

## 3. Checkpoint Totals
Across all `12` episodes:

- `turn7`
  - `chosen_side_direction_progress_present = 12/12`
  - `user_detail_use_present = 12/12`
  - `unresolved_relation_preserved_or_narrowly_checked = 12/12`
  - `suspended_main_reference_absent = 12/12`
  - `starter_question_repeat_absent = 12/12`
  - `appropriate = 12/12`
- `turn9`
  - `chosen_side_direction_progress_present = 12/12`
  - `user_detail_use_present = 12/12`
  - `unresolved_relation_preserved_or_narrowly_checked = 4/12`
  - `suspended_main_reference_absent = 12/12`
  - `starter_question_repeat_absent = 12/12`
  - `appropriate = 4/12`
- `turn11`
  - `chosen_side_direction_progress_present = 12/12`
  - `user_detail_use_present = 12/12`
  - `unresolved_relation_preserved_or_narrowly_checked = 0/12`
  - `suspended_main_reference_absent = 12/12`
  - `starter_question_repeat_absent = 12/12`
  - `appropriate = 0/12`

## 4. Current Read
The Anthropic scored read is structurally clean and easier to summarize than the repaired Gemini read.

- `turn7` is uniformly stable
- the first degradation for `B/C` appears at `turn9` as unsupported unresolved-relation commitment
- `A` holds through `turn9` and then fails at `turn11` on the same unresolved-relation dimension
- the suspended main objective remains quarantined throughout
