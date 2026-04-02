# Energy Priority-Resolution Side-Topic Followthrough A Answer-Use Completeness Two-Provider Read Memo v1

## Status
- Date: 2026-03-17
- Type: cross-provider read memo
- Scope: summarize the tested two-provider read after line-local paired comparisons on Gemini and Anthropic for the frozen `A_trip_planning answer-use completeness at turn 7 under budget-quarantine-supported surface` line
- Depends on:
  - `energy_priority_resolution_side_topic_followthrough_a_answer_use_completeness_reference_vs_operator_comparison_memo_v1_2026-03-17.md`
  - `energy_priority_resolution_side_topic_followthrough_a_answer_use_completeness_anthropic_reference_vs_operator_comparison_memo_v1_2026-03-17.md`
- Not a manuscript claim memo

## 1. Tested Provider Pair
Tested providers:
- `gemini` with `gemini-2.0-flash`
- `anthropic` with `claude-sonnet-4-20250514`

Shared protocol:
- same frozen `accept_side_first` row set
- same frozen `A_trip_planning` template
- same 3 frozen scoring labels
- same fixed turn-7-only episode unit
- same `t=0.0`
- same `reps=4`
- same retained reference-vs-operator comparison shape

## 2. Aggregate Read

| provider | reference `appropriate = 1` | operator `appropriate = 1` | delta |
|---|---:|---:|---:|
| `gemini` | 2 / 4 | 4 / 4 | +2 |
| `anthropic` | 0 / 4 | 0 / 4 | 0 |

Supplementary metric split:

| provider | reference `continued_side_direction_progress_present = 1` | operator `continued_side_direction_progress_present = 1` | reference `suspended_main_reference_absent = 1` | operator `suspended_main_reference_absent = 1` |
|---|---:|---:|---:|---:|
| `gemini` | 2 / 4 | 4 / 4 | 4 / 4 | 4 / 4 |
| `anthropic` | 0 / 4 | 0 / 4 | 4 / 4 | 4 / 4 |

## 3. Provider-Specific Difference
Shared read across both providers:
- neither provider re-imports suspended-main budget detail on this frozen surface

Provider split:
- Gemini:
  - the answer-use-completeness operator repairs the remaining `A` residual
- Anthropic:
  - both arms repeat the earlier cuisine-starter question and fail to use the seafood/ramen answer

Read:
- the current repair is provider-sensitive rather than provider-balanced
- the second-provider boundary is concrete and local to answer use, not to budget carryover

## 4. What This Adds
This adds:
- a tested two-provider read under the same narrow `A`-only turn-7 protocol
- evidence that the current answer-use-completeness repair is not provider-balanced in the strong sense
- a concrete Anthropic-specific failure mode:
  - repetition of the earlier cuisine-starter question despite the fixed turn-6 answer

This still does not add:
- cross-template validity
- longer-horizon followthrough or outcome claims
- manuscript-facing Guarantee closure

## 5. Assistant-Side Read
- overall judgment:
  - `adopt`
- reason:
  - the provider-balanced replication now exists as evidence rather than as a planned next line, and it exposes a concrete second-provider boundary
- current best read:
  - the `A`-only answer-use-completeness line ends as a mixed two-provider result
  - Gemini shows a clean local repair
  - Anthropic shows no gain under the same frozen prompt pair
