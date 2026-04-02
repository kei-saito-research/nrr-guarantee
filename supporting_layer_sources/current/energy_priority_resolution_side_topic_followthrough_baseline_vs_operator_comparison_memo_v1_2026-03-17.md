# Energy Priority-Resolution Side-Topic Followthrough Baseline vs Operator Comparison Memo v1

## Status
- Date: 2026-03-17
- Type: line result memo
- Scope: compare Gemini baseline and Gemini operator continuation arms on the frozen `longer-horizon side-topic followthrough under the already-supported stronger operator` protocol
- Depends on:
  - `energy_priority_resolution_side_topic_followthrough_protocol_freeze_decision_memo_v1_2026-03-17.md`
  - `energy_priority_resolution_side_topic_followthrough_run_annotation_baseline_v1_2026-03-17.csv`
  - `energy_priority_resolution_side_topic_followthrough_run_annotation_operator_v1_2026-03-17.csv`
- Not a manuscript claim memo

## 1. Run Executed
Gemini baseline output directory:
- `priority_resolution_side_topic_followthrough_probe_20260316T225241Z`

Gemini operator output directory:
- `priority_resolution_side_topic_followthrough_probe_20260316T225240Z`

Shared run conditions:
- provider: `gemini`
- model: `gemini-2.0-flash`
- temperature: `0.0`
- reps: `4`
- templates:
  - `A_trip_planning`
  - `B_hiring_packet`
  - `C_incident_response`
- acceptance variants:
  - `accept_side_first` only
- exact input rows:
  - `energy_priority_resolution_side_topic_followthrough_run_input_v1_2026-03-17.csv`
- fixed turns:
  - turn 3 handoff
  - turn 5 successful side-topic workstart
  - turn 6 user side-topic answer
- scored turn:
  - turn 7 only

Only the assistant condition differed:
- baseline:
  - plain assistant condition
- operator:
  - `priority_resolution_side_topic_followthrough_operator_arm_system_prompt_v1.txt`

## 2. Aggregate Result

| arm | `continued_side_direction_progress_present = 1` | `suspended_main_reference_absent = 1` | `main_direction_intrusion_absent = 1` | `appropriate = 1` |
|---|---:|---:|---:|---:|
| Gemini baseline | 4 / 12 | 12 / 12 | 12 / 12 | 4 / 12 |
| Gemini operator | 1 / 12 | 8 / 12 | 12 / 12 | 1 / 12 |
| delta (`operator - baseline`) | -3 | -4 | 0 | -3 |

## 3. Structured Failure Split

| template_id | Gemini baseline `appropriate = 1` | Gemini operator `appropriate = 1` | delta |
|---|---:|---:|---:|
| `A_trip_planning` | 0 / 4 | 0 / 4 | 0 |
| `B_hiring_packet` | 0 / 4 | 0 / 4 | 0 |
| `C_incident_response` | 4 / 4 | 1 / 4 | -3 |

## 4. Failure-Mode Shift
Observed gain:
- no positive gain on the frozen turn-7 metric

Observed degradation:
- the operator arm scores lower than baseline on both continuation progress and overall appropriateness
- the operator arm also reintroduces suspended-main reference on all `A_trip_planning` rows

Baseline failure read:
- baseline no longer fails by returning to the original main objective
- instead it often stays on the chosen side topic but fails by not using the turn-6 answer, especially on `A` and `B`

Operator-arm read:
- the repaired continuation operator does not improve answer use
- on `A` it leaks the suspended main priority back into the reply
- on `C` it usually falls back to a near-repeat of the turn-5 starter question

Behavioral read:
- the explicit first-step operator does not extend cleanly into second-step continuation control
- the surviving residual at turn 7 is better described as `answer-conditioned followthrough`, not generic side-topic commitment

## 5. Assistant-Side Read
- overall judgment:
  - `adopt`
- reason:
  - the line is informative precisely because the repaired continuation operator still does not help, and the failure mode is narrow and text-auditable
- current best read:
  - first-step side-topic commitment is locally solved on the earlier line
  - one-turn-later continuation remains unresolved on this Gemini surface
  - the active issue is using newly supplied side-topic detail to progress the chosen direction without reintroducing suspended-main framing
