# Energy Priority-Resolution Side-Topic Followthrough A Budget Quarantine Baseline vs Operator Comparison Memo v1

## Status
- Date: 2026-03-17
- Type: line result memo
- Scope: compare Gemini baseline and Gemini budget-quarantine operator arms on the frozen `A_trip_planning suspended-main budget quarantine at turn 7` protocol
- Depends on:
  - `energy_priority_resolution_side_topic_followthrough_a_budget_quarantine_protocol_freeze_decision_memo_v1_2026-03-17.md`
  - `energy_priority_resolution_side_topic_followthrough_a_budget_quarantine_run_annotation_baseline_v1_2026-03-17.csv`
  - `energy_priority_resolution_side_topic_followthrough_a_budget_quarantine_run_annotation_operator_v1_2026-03-17.csv`
- Not a manuscript claim memo

## 1. Run Executed
Gemini baseline output directory:
- `priority_resolution_side_topic_followthrough_probe_20260317T020247Z`

Gemini budget-quarantine operator output directory:
- `priority_resolution_side_topic_followthrough_probe_20260317T020305Z`

Shared run conditions:
- provider: `gemini`
- model: `gemini-2.0-flash`
- temperature: `0.0`
- reps: `4`
- template:
  - `A_trip_planning`
- acceptance variant:
  - `accept_side_first` only
- exact input rows:
  - `energy_priority_resolution_side_topic_followthrough_a_budget_quarantine_run_input_v1_2026-03-17.csv`
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
  - `priority_resolution_side_topic_followthrough_a_budget_quarantine_operator_arm_system_prompt_v2.txt`

## 2. Aggregate Result

| arm | `continued_side_direction_progress_present = 1` | `suspended_main_reference_absent = 1` | `main_direction_intrusion_absent = 1` | `appropriate = 1` |
|---|---:|---:|---:|---:|
| Gemini baseline | 0 / 4 | 4 / 4 | 4 / 4 | 0 / 4 |
| Gemini budget-quarantine operator | 3 / 4 | 4 / 4 | 4 / 4 | 3 / 4 |
| delta (`operator - baseline`) | +3 | 0 | 0 | +3 |

## 3. Failure-Mode Shift
Observed gain relative to baseline:
- real gain on the frozen `A`-only turn-7 metric

Observed change:
- baseline keeps repeating the earlier cuisine-starter question and never uses the seafood/ramen answer
- the budget-quarantine operator uses the authorized cuisine detail on three of four rows
- the operator removes suspended-main budget carryover on all four rows
- one operator row still fails because it only acknowledges the answer without producing a next step

Behavioral read:
- budget-quarantine wording is locally effective on the single-template `A` residual
- the remaining miss is no longer budget carryover
- the residual after this line is one-step continuation completeness, not suspended-main budget import

## 4. Assistant-Side Read
- overall judgment:
  - `adopt`
- reason:
  - this line produces a clean local gain on the intended frozen surface without widening provider, template, horizon, or metric family
- current best read:
  - the completed 3-template source-selective line should stay closed as a no-gain line
  - the narrower `A`-only budget-quarantine line shows that the `A` budget carryover is operator-sensitive and mostly fixable
  - this does not justify back-propagating a broader cross-template claim
  - if Energy continues from here, the next line must target the remaining answer-use completeness miss rather than reopen budget quarantine wording
