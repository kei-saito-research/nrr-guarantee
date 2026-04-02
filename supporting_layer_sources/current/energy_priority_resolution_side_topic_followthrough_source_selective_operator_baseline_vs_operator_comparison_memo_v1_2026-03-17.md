# Energy Priority-Resolution Side-Topic Followthrough Source-Selective Operator Baseline vs Operator Comparison Memo v1

## Status
- Date: 2026-03-17
- Type: line result memo
- Scope: compare Gemini baseline and Gemini source-selective operator arms on the frozen `source-selective continuation control at turn 7` protocol
- Depends on:
  - `energy_priority_resolution_side_topic_followthrough_source_selective_operator_protocol_freeze_decision_memo_v1_2026-03-17.md`
  - `energy_priority_resolution_side_topic_followthrough_source_selective_operator_run_annotation_baseline_v1_2026-03-17.csv`
  - `energy_priority_resolution_side_topic_followthrough_source_selective_operator_run_annotation_operator_v1_2026-03-17.csv`
- Not a manuscript claim memo

## 1. Run Executed
Gemini baseline output directory:
- `priority_resolution_side_topic_followthrough_probe_20260317T004813Z`

Gemini source-selective operator output directory:
- `priority_resolution_side_topic_followthrough_probe_20260317T004818Z`

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
  - `priority_resolution_side_topic_followthrough_source_selective_operator_arm_system_prompt_v1.txt`

Earlier duplicate baseline artifact retained but excluded from scored comparison:
- `priority_resolution_side_topic_followthrough_probe_20260317T004728Z`

## 2. Aggregate Result

| arm | `continued_side_direction_progress_present = 1` | `suspended_main_reference_absent = 1` | `main_direction_intrusion_absent = 1` | `appropriate = 1` |
|---|---:|---:|---:|---:|
| Gemini baseline | 4 / 12 | 12 / 12 | 12 / 12 | 4 / 12 |
| Gemini source-selective operator | 4 / 12 | 8 / 12 | 12 / 12 | 4 / 12 |
| delta (`operator - baseline`) | 0 | -4 | 0 | 0 |

## 3. Structured Failure Split

| template_id | Gemini baseline `appropriate = 1` | Gemini source-selective operator `appropriate = 1` | delta |
|---|---:|---:|---:|
| `A_trip_planning` | 0 / 4 | 0 / 4 | 0 |
| `B_hiring_packet` | 0 / 4 | 0 / 4 | 0 |
| `C_incident_response` | 4 / 4 | 4 / 4 | 0 |

## 4. Failure-Mode Shift
Observed gain relative to baseline:
- no gain on the frozen turn-7 metric

Observed change:
- the source-selective operator no longer imports suspended hiring-packet detail on `B`
- but it still imports suspended budget detail on all `A` rows
- the total `appropriate` score remains unchanged because `B` stays generic and `A` still fails on wrong-source import

Baseline read:
- baseline remains stable at `4 / 12`
- it fails mainly by repeating the earlier side-topic starter question without using the new answer on `A` and `B`

Source-selective operator read:
- on `C`, the operator remains stably anchored on the user-provided postmortem sections
- on `B`, the operator drops the earlier suspended-main leak but still does not use the tools/team-norms/checklist answer
- on `A`, the operator continues to ask a budget question, which now fails the tightened source-selective scoring rule directly

Behavioral read:
- source-selective wording alone does not rescue the turn-7 line relative to baseline
- the remaining failure is no longer one uniform wrong-source pattern across templates
- `A` still shows suspended-main constraint import, while `B` has shifted back to generic answer nonuse

## 5. Assistant-Side Read
- overall judgment:
  - `adopt`
- reason:
  - the line is informative because it closes the source-selective wording question without widening surface, metric family, or turn horizon
- current best read:
  - first-step side-topic commitment remains locally solved
  - generic continuation control remains a no-gain line
  - answer-conditioned wording alone does not beat baseline
  - source-selective wording alone also does not beat baseline
  - if Energy continues, the next move must be a new narrow line rather than prompt drift on this exact turn-7 wording
