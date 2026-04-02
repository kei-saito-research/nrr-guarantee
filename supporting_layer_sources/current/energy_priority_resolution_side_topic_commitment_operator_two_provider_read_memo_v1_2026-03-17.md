# Energy Priority-Resolution Side-Topic Commitment Operator Two-Provider Read Memo v1

## Status
- Date: 2026-03-17
- Type: cross-provider read memo
- Scope: summarize the tested two-provider read after line-local paired comparisons on Gemini and Anthropic for the frozen `stricter side-topic commitment / explicit side-topic operator` line
- Depends on:
  - `energy_priority_resolution_side_topic_commitment_operator_baseline_vs_operator_comparison_memo_v1_2026-03-17.md`
  - `energy_priority_resolution_side_topic_commitment_operator_anthropic_baseline_vs_operator_comparison_memo_v1_2026-03-17.md`
- Not a manuscript claim memo

## 1. Tested Provider Pair
Tested providers:
- `gemini` with `gemini-2.0-flash`
- `anthropic` with `claude-sonnet-4-20250514`

Shared protocol:
- same frozen `accept_side_first` row set
- same 3 frozen templates
- same 3 frozen scoring labels
- same fixed-handoff episode unit
- same `t=0.0`
- same `reps=4`
- same retained baseline-vs-operator comparison shape

## 2. Aggregate Read

| provider | baseline `appropriate = 1` | operator `appropriate = 1` | delta |
|---|---:|---:|---:|
| `gemini` | 0 / 12 | 12 / 12 | +12 |
| `anthropic` | 0 / 12 | 12 / 12 | +12 |

Supplementary metric split:

| provider | baseline `chosen_side_direction_workstart_present = 1` | operator `chosen_side_direction_workstart_present = 1` | baseline `suspended_main_reference_absent = 1` | operator `suspended_main_reference_absent = 1` |
|---|---:|---:|---:|---:|
| `gemini` | 0 / 12 | 12 / 12 | 0 / 12 | 12 / 12 |
| `anthropic` | 0 / 12 | 12 / 12 | 0 / 12 | 12 / 12 |

## 3. Provider-Specific Baseline Difference
Shared baseline structure:
- after explicit side-first acceptance, both providers keep the original main objective live and work on it on all tested rows

Read:
- unlike the earlier downstream-acceptance line, the baseline failure shape is not split between providers here
- both providers fully fail the stronger side-topic-commitment rubric under the plain assistant condition

## 4. Shared Operator Read
Across both tested providers:
- the explicit side-topic operator produced `12 / 12` on:
  - `chosen_side_direction_workstart_present`
  - `suspended_main_reference_absent`
  - `main_direction_intrusion_absent`
  - `appropriate`

Shared read:
- the frozen explicit side-topic operator reproduced on both tested providers without changing the surface or scoring

## 5. What This Adds
This adds:
- a tested two-provider operator read under the same narrow side-first protocol
- evidence that the current explicit side-topic-commitment shift is not Gemini-only within the tested provider pair

This still does not add:
- broad provider universality
- longer-horizon followthrough or outcome claims
- manuscript-facing Guarantee closure

## 6. Assistant-Side Read
- overall judgment:
  - `adopt`
- reason:
  - the provider-balanced replication now exists as evidence rather than as a planned next line
- current best read:
  - on the tested provider pair, baseline failed the frozen side-topic-commitment rubric while the explicit operator satisfied it completely under otherwise matched conditions
