# Energy Priority-Resolution Downstream Followthrough Rescue Baseline vs Rescue Comparison Memo v1

## Status
- Date: 2026-03-17
- Type: line result memo
- Scope: compare Gemini baseline and Gemini rescue on the frozen `accepted-direction followthrough rescue` protocol
- Depends on:
  - `energy_priority_resolution_downstream_followthrough_rescue_protocol_freeze_decision_memo_v1_2026-03-17.md`
  - `energy_priority_resolution_downstream_followthrough_rescue_run_annotation_baseline_v1_2026-03-17.csv`
  - `energy_priority_resolution_downstream_followthrough_rescue_run_annotation_rescue_v1_2026-03-17.csv`
- Not a manuscript claim memo

## 1. Run Executed
Gemini baseline output directory:
- `priority_resolution_followthrough_rescue_probe_20260316T213927Z`

Gemini rescue output directory:
- `priority_resolution_followthrough_rescue_probe_20260316T214009Z`

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
  - `accept_main_first`
  - `accept_side_first`
- exact input rows:
  - `energy_priority_resolution_downstream_followthrough_rescue_run_input_v1_2026-03-17.csv`
- fixed turn-3 handoff:
  - template-specific clean choice-question scaffold
- scored turn:
  - turn 5 only

Only the assistant condition differed:
- baseline:
  - plain assistant condition
- rescue:
  - `priority_resolution_followthrough_rescue_arm_system_prompt_v1.txt`

## 2. Aggregate Result

| arm | `accepted_direction_workstart_present = 1` | `rejected_direction_intrusion_absent = 1` | `appropriate = 1` |
|---|---:|---:|---:|
| Gemini baseline | 12 / 24 | 12 / 24 | 12 / 24 |
| Gemini rescue | 12 / 24 | 12 / 24 | 12 / 24 |
| delta (`rescue - baseline`) | +0 | +0 | +0 |

## 3. Structured Failure Split

| acceptance_variant_id | Gemini baseline `appropriate = 1` | Gemini rescue `appropriate = 1` | delta |
|---|---:|---:|---:|
| `accept_main_first` | 12 / 12 | 12 / 12 | +0 |
| `accept_side_first` | 0 / 12 | 0 / 12 | +0 |

Per-template read:

| template_id | Gemini baseline `appropriate = 1` | Gemini rescue `appropriate = 1` | delta |
|---|---:|---:|---:|
| `A_trip_planning` | 4 / 8 | 4 / 8 | +0 |
| `B_hiring_packet` | 4 / 8 | 4 / 8 | +0 |
| `C_incident_response` | 4 / 8 | 4 / 8 | +0 |

## 4. Failure-Mode Shift
Observed gain:
- none on the frozen metric

Observed non-scoring shift:
- on main-accepted rows, rescue tends to realize workstart as a focused question rather than a short forward plan

Observed persistent failure:
- both arms fully fail the side-first acceptance rows
- after explicit side-first acceptance, Gemini still starts the rejected main direction on all `12 / 12` rows

Behavioral read:
- once turn 3 is fixed to a clean handoff, the residual Gemini problem is not mainly generic acknowledgment
- the dominant residual is acceptance-conditioned direction switching

## 5. Assistant-Side Read
- overall judgment:
  - `adopt`
- reason:
  - the line is informative under the frozen protocol because it cleanly shows that this rescue prompt does not move the metric and that the remaining problem is narrower than originally framed
- current best read:
  - `followthrough_rescue_v1` is not an effective rescue for Gemini
  - if Energy continues from here, open a new line around explicit adherence to the user-chosen direction after side-first acceptance rather than rerunning this line on outcomes
