# Energy Priority-Resolution Side-Topic Followthrough Answer-Conditioned Operator Baseline vs Operator Comparison Memo v1

## Status
- Date: 2026-03-17
- Type: line result memo
- Scope: compare Gemini baseline and Gemini answer-conditioned operator arms on the frozen `answer-conditioned side-topic continuation control at turn 7` protocol
- Depends on:
  - `energy_priority_resolution_side_topic_followthrough_answer_conditioned_operator_protocol_freeze_decision_memo_v1_2026-03-17.md`
  - `energy_priority_resolution_side_topic_followthrough_answer_conditioned_operator_run_annotation_baseline_v1_2026-03-17.csv`
  - `energy_priority_resolution_side_topic_followthrough_answer_conditioned_operator_run_annotation_operator_v1_2026-03-17.csv`
- Not a manuscript claim memo

## 1. Run Executed
Gemini baseline output directory:
- `priority_resolution_side_topic_followthrough_probe_20260317T001737Z`

Gemini answer-conditioned operator output directory:
- `priority_resolution_side_topic_followthrough_probe_20260317T001746Z`

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
  - `priority_resolution_side_topic_followthrough_answer_conditioned_operator_arm_system_prompt_v1.txt`

## 2. Aggregate Result

| arm | `continued_side_direction_progress_present = 1` | `suspended_main_reference_absent = 1` | `main_direction_intrusion_absent = 1` | `appropriate = 1` |
|---|---:|---:|---:|---:|
| Gemini baseline | 4 / 12 | 12 / 12 | 12 / 12 | 4 / 12 |
| Gemini answer-conditioned operator | 4 / 12 | 5 / 12 | 12 / 12 | 4 / 12 |
| delta (`operator - baseline`) | 0 | -7 | 0 | 0 |

## 3. Structured Failure Split

| template_id | Gemini baseline `appropriate = 1` | Gemini answer-conditioned operator `appropriate = 1` | delta |
|---|---:|---:|---:|
| `A_trip_planning` | 0 / 4 | 0 / 4 | 0 |
| `B_hiring_packet` | 0 / 4 | 0 / 4 | 0 |
| `C_incident_response` | 4 / 4 | 4 / 4 | 0 |

## 4. Failure-Mode Shift
Observed gain relative to baseline:
- no gain on the frozen turn-7 metric

Observed change:
- the answer-conditioned operator no longer underperforms baseline on `continued_side_direction_progress_present`
- but it sharply reduces `suspended_main_reference_absent` because it often anchors on suspended-main details instead of the turn-6 side-topic details

Baseline read:
- baseline remains stable at the previously observed `4 / 12`
- it fails mainly by repeating the earlier side-topic starter question without using the new answer on `A` and `B`

Answer-conditioned operator read:
- on `C`, the operator now visibly uses the turn-6 answer on all `4 / 4` rows
- on `A` and most `B` rows, the operator still chooses the wrong source detail and pulls suspended-main framing into the reply

Behavioral read:
- answer-conditioned wording alone is not enough for a full rescue on this frozen Gemini surface
- the unresolved issue is not just `use some detail`
- it is `use detail from the active side-topic answer rather than from suspended-main context`

## 5. Assistant-Side Read
- overall judgment:
  - `adopt`
- reason:
  - the line is informative because it narrows the residual further without widening surface, metric, or horizon
- current best read:
  - first-step side-topic commitment remains locally solved
  - generic continuation control remains a no-gain line
  - answer-conditioned continuation control also does not beat baseline
  - the next unresolved layer is source-selective continuation control at turn 7
