# Guarantee Phase 2 Downstream-Acceptance Closure Import Note v2

## Status
- Date: 2026-03-30
- Type: repo-local import note
- Scope: make the current repaired downstream-acceptance read auditable from
  the repo and the review bundle without reopening workspace-only paths
- Basis artifact:
  - reviewed shared-box artifact `GUARANTEE_REVIEW_phase2_downstream_acceptance_readout_2026-03-21_v8.zip`
- Not a new experiment run

## 1. Why v2 Exists

`v1` recorded the repaired read but still pointed reviewers outward to the
historical shared-box artifact. The current manuscript needs the repaired read
to be auditable from the shipped repo/review surface itself.

## 2. Imported Reviewed Surface

The reviewed `v8` readout surface is now imported under:
- `results/reviewed_phase2_downstream_acceptance_readout_v8/`

Read the following files there as the decisive current repaired readout:
- `guarantee_phase2_priority_resolution_downstream_acceptance_provider_read_table_v1_2026-03-21.csv`
- `guarantee_phase2_priority_resolution_downstream_acceptance_nrr_vs_ablation_comparison_memo_v1_2026-03-21.md`
- `guarantee_phase2_priority_resolution_downstream_acceptance_per_protocol_supplemental_table_v1_2026-03-21.csv`
- `non_evaluative_principle_guarantee_phase2_downstream_acceptance_readout_completion_memo_v8_2026-03-21.md`

Supporting bundled evidence remains available there as well:
- template-delta and manipulation-check tables
- six annotation CSVs
- bundled source-bundle summaries/responses for the final successful runs

## 3. Reviewed Artifact Identity

- artifact:
  - `GUARANTEE_REVIEW_phase2_downstream_acceptance_readout_2026-03-21_v8.zip`
- reviewed checksum:
  - `9faea986a226f181a7e234b249c4a1967a7858b3e8909e38d6471ac11470e0cb`
- external review closure:
  - one independent Codex review: `adopt`
  - one Claude review: `adopt`

## 4. Adopted Current Read

- provider-first read:
  - Anthropic: `inconclusive`
  - Gemini: `support`
  - overall: `mixed`
- manuscript use:
  - bounded downstream-acceptance reporting only
- manuscript non-use:
  - no pair-wide downstream guarantee
  - no provider-universal downstream-quality claim
  - no explicit quarantine closure
  - no later-horizon stability claim

## 5. Repo-Local Import Rule

For the current manuscript line:
- use this note, `guarantee_second_claim_unit_fill_v5_2026-03-30.md`, and
  `results/reviewed_phase2_downstream_acceptance_readout_v8/` together as the
  current repo-local source surface for the repaired second claim unit
- keep the older pre-repair downstream-acceptance memo in
  `supporting_layer_sources/current/` as historical provenance only
- do not describe the support bundle by itself as the full proof surface for
  the repaired downstream-acceptance read
