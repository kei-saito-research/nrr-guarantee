# Guarantee Phase 2 Downstream-Acceptance NRR vs Ablation Comparison Memo v1

## Status
- Date: 2026-03-21
- Type: provider-first ITT comparison memo
- Scope:
  - compare frozen `NRR` vs `Ablation` as the main Phase 2 comparison
  - keep `Baseline` as the auxiliary read
- Depends on:
  - `guarantee_phase2_priority_resolution_downstream_acceptance_provider_itt_summary_v1_2026-03-21.csv`
  - `guarantee_phase2_priority_resolution_downstream_acceptance_template_delta_table_v1_2026-03-21.csv`
  - `guarantee_phase2_priority_resolution_downstream_acceptance_manipulation_check_table_v1_2026-03-21.csv`
  - `guarantee_phase2_priority_resolution_downstream_acceptance_per_protocol_supplemental_table_v1_2026-03-21.csv`
  - six annotation CSVs written in this same pass
- Not a manuscript claim memo

## 1. Run Executed
Final successful bundles:
- anthropic Baseline:
  - `CURRENT/source_bundles/guarantee_phase2_priority_resolution_downstream_acceptance_20260320T152923Z_anthropic_baseline`
- anthropic NRR:
  - `CURRENT/source_bundles/guarantee_phase2_priority_resolution_downstream_acceptance_20260320T154207Z_anthropic_nrr`
- anthropic Ablation:
  - `CURRENT/source_bundles/guarantee_phase2_priority_resolution_downstream_acceptance_20260320T155028Z_anthropic_ablation`
- gemini Baseline:
  - `CURRENT/source_bundles/guarantee_phase2_priority_resolution_downstream_acceptance_20260320T160227Z_gemini_baseline`
- gemini NRR:
  - `CURRENT/source_bundles/guarantee_phase2_priority_resolution_downstream_acceptance_20260320T160531Z_gemini_nrr`
- gemini Ablation:
  - `CURRENT/source_bundles/guarantee_phase2_priority_resolution_downstream_acceptance_20260320T160853Z_gemini_ablation`

Raw-only execution history retained but excluded from downstream tables:
- `CURRENT/source_bundles/guarantee_phase2_priority_resolution_downstream_acceptance_20260320T152851Z_anthropic_baseline`
  - raw lines: `0`

Use rule:
- exclude the raw-only Anthropic Baseline history artifact from ITT, per-protocol, and all downstream tables
- use only the final successful bundle for each authorized wrapper

## 2. In Scope / Out of Scope
In scope:
- whether visible comparative evaluation in `Ablation` degrades accepted-branch downstream continuation relative to `NRR`
- whether that read is provider-first before any pooled total
- whether `Baseline` remains an auxiliary weaker surface on the same accepted-branch boundary

Out of scope:
- Phase 1 ambiguity-turn priority resolution
- later-horizon multi-turn followthrough beyond the decisive accepted-branch turn
- any claim wider than the frozen Phase 2 provider-first rule

## Provider Slice: Anthropic

| arm | accepted_branch_followthrough_present = 1 | reopened_choice_absent = 1 | appropriate = 1 | accepted_branch_recognition_present = 1 | alternative_branch_push_absent = 1 | mean output_tokens |
| --- | --- | --- | --- | --- | --- | --- |
| anthropic Baseline | 144 / 144 | 144 / 144 | 142 / 144 | 144 / 144 | 144 / 144 | 120.65 |
| anthropic NRR | 59 / 144 | 109 / 144 | 55 / 144 | 144 / 144 | 110 / 144 | 61.21 |
| anthropic Ablation | 38 / 144 | 50 / 144 | 38 / 144 | 144 / 144 | 66 / 144 | 111.01 |
| delta (NRR - Ablation) | 21 | 59 | 17 | 0 | 44 | -49.80 |
| delta (NRR - Baseline) | -85 | -35 | -87 | 0 | -34 | -59.44 |

Provider read:
- `appropriate` gap (`NRR - Ablation`): `17`
- `accepted_branch_followthrough_present` gap (`NRR - Ablation`): `21`
- `reopened_choice_absent` gap (`NRR - Ablation`): `59`
- `template_spread_pass`: `false`
- provider-level read: `inconclusive`

## Provider Slice: Gemini

| arm | accepted_branch_followthrough_present = 1 | reopened_choice_absent = 1 | appropriate = 1 | accepted_branch_recognition_present = 1 | alternative_branch_push_absent = 1 | mean output_tokens |
| --- | --- | --- | --- | --- | --- | --- |
| gemini Baseline | 105 / 144 | 144 / 144 | 72 / 144 | 144 / 144 | 144 / 144 | 28.40 |
| gemini NRR | 107 / 144 | 144 / 144 | 93 / 144 | 144 / 144 | 144 / 144 | 41.76 |
| gemini Ablation | 60 / 144 | 144 / 144 | 36 / 144 | 144 / 144 | 144 / 144 | 30.32 |
| delta (NRR - Ablation) | 47 | 0 | 57 | 0 | 0 | 11.44 |
| delta (NRR - Baseline) | 2 | 0 | 21 | 0 | 0 | 13.36 |

Provider read:
- `appropriate` gap (`NRR - Ablation`): `57`
- `accepted_branch_followthrough_present` gap (`NRR - Ablation`): `47`
- `reopened_choice_absent` gap (`NRR - Ablation`): `0`
- `template_spread_pass`: `true`
- provider-level read: `support`


## 4. Manipulation-Check Read
Manipulation-check artifact:
- `guarantee_phase2_priority_resolution_downstream_acceptance_manipulation_check_table_v1_2026-03-21.csv`

Current read:
- `Ablation` non-compliance:
  - `0 / 144` in both providers
- `NRR` contamination:
  - `0 / 144` in both providers
- `Baseline` contamination:
  - `0 / 144` in both providers

Operational meaning:
- the intended visible comparative-evaluation insertion remained present on the final successful `Ablation` bundles
- no visible two-direction comparative evaluation appeared in the final successful `NRR` or `Baseline` bundles

## 5. Template-Delta Read
Template-delta artifact:
- `guarantee_phase2_priority_resolution_downstream_acceptance_template_delta_table_v1_2026-03-21.csv`

Current read:
- use the provider-first rule on `appropriate`, while keeping `accepted_branch_followthrough_present` and `reopened_choice_absent` as the two component checks
- `template_spread_pass` reuses the Phase 1 threshold
- exact ties on `appropriate` remain `non-support`
- in this pass:
  - Anthropic shows a positive `NRR - Ablation` gap, but the gain does not satisfy the spread rule, so the provider-level result remains `inconclusive`
  - Gemini shows a positive `NRR - Ablation` gap that clears the spread rule, so the provider-level result reaches `support`

## 6. Per-Protocol Supplemental Read
Per-protocol artifact:
- `guarantee_phase2_priority_resolution_downstream_acceptance_per_protocol_supplemental_table_v1_2026-03-21.csv`

Current read:
- per-protocol denominators equal ITT denominators in all six final successful bundles
- reason:
  - no `Ablation` non-compliance rows
  - no `NRR` / `Baseline` contamination rows

## 7. Pooled Totals
Provider slices above remain the decisive read.
Pooled totals are shown only after the provider-first tables.

| arm | accepted_branch_followthrough_present = 1 | reopened_choice_absent = 1 | appropriate = 1 | accepted_branch_recognition_present = 1 | alternative_branch_push_absent = 1 | mean output_tokens |
| --- | --- | --- | --- | --- | --- | --- |
| pooled Baseline | 249 / 288 | 288 / 288 | 214 / 288 | 288 / 288 | 288 / 288 | 74.53 |
| pooled NRR | 166 / 288 | 253 / 288 | 148 / 288 | 288 / 288 | 254 / 288 | 51.48 |
| pooled Ablation | 98 / 288 | 194 / 288 | 74 / 288 | 288 / 288 | 210 / 288 | 70.66 |
| pooled delta (NRR - Ablation) | 68 | 59 | 74 | 0 | 44 | -19.18 |

Pooled read boundary:
- pooled totals do not override the provider-first decision rule
- they only summarize the combined direction after the provider slices are already fixed

## 8. Assistant-Side Read
- overall judgment:
  - `adopt`
- reason:
  - the readout is now reproducible from the six final successful bundles, keeps the frozen provider-first rule explicit, and leaves the execution-history-only artifact excluded from all downstream tables
- current best read:
  - `NRR` outperforms `Ablation` on `appropriate` in both providers
  - `Gemini` reaches `support` while the other provider remains `inconclusive`, so the provider-first read is mixed rather than provider-balanced `support`
  - `Anthropic Baseline` is stronger than `Anthropic NRR` on this downstream-acceptance boundary, so `Baseline` remains an important auxiliary comparator rather than a dominated floor
