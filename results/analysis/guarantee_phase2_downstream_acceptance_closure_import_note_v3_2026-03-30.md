# Guarantee Phase 2 Downstream-Acceptance Closure Import Note v3

## Status
- Date: 2026-03-30
- Type: repo-local import note
- Scope: restate the current repaired downstream-acceptance read so the
  manuscript-facing comparison contract is explicit
- Basis artifact:
  - reviewed shared-box artifact `GUARANTEE_REVIEW_phase2_downstream_acceptance_readout_2026-03-21_v8.zip`
- Not a new experiment run

## 1. Why v3 exists

`v2` made the repaired second-claim surface auditable from the shipped repo,
but the manuscript still needed a clearer statement of which comparison is
decisive for the repaired read. The current second claim does not close under
the paper's mainline `baseline vs Energy policy` comparison. It closes only as
a bounded downstream-acceptance read on a reviewed primary `NRR vs Ablation`
comparison, with `Baseline` retained as an auxiliary comparator.

## 2. Imported reviewed surface

The reviewed `v8` readout surface remains imported under:
- `results/reviewed_phase2_downstream_acceptance_readout_v8/`

Read the following files there as the decisive current repaired readout:
- `guarantee_phase2_priority_resolution_downstream_acceptance_provider_read_table_v1_2026-03-21.csv`
- `guarantee_phase2_priority_resolution_downstream_acceptance_nrr_vs_ablation_comparison_memo_v1_2026-03-21.md`
- `guarantee_phase2_priority_resolution_downstream_acceptance_per_protocol_supplemental_table_v1_2026-03-21.csv`
- `non_evaluative_principle_guarantee_phase2_downstream_acceptance_readout_completion_memo_v8_2026-03-21.md`

## 3. Adopted current read

- decisive primary comparison:
  - `NRR vs Ablation`
- auxiliary comparator retained in manuscript-facing read:
  - `Baseline`
- provider-first read:
  - Anthropic: `inconclusive`
  - Gemini: `support`
  - overall: `mixed`
- additional auxiliary-comparator fact that should not be hidden:
  - on the Anthropic slice, `Baseline` remains stronger than `NRR` on
    `appropriate`

## 4. Manuscript use / non-use

- manuscript use:
  - bounded downstream-acceptance reporting only
  - explicit statement that the decisive current comparison is `NRR vs Ablation`
  - explicit statement that `Baseline` remains an auxiliary comparator
- manuscript non-use:
  - no pair-wide downstream guarantee
  - no provider-universal downstream-quality claim
  - no monotone `baseline -> Energy -> NRR` carry-forward story
  - no claim that `NRR` generally dominates `Baseline` on this boundary
  - no explicit quarantine closure
  - no later-horizon stability claim
