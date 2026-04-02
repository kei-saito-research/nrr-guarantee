# Guarantee Phase 2 Downstream-Acceptance Closure Import Note v5

## Status
- Date: 2026-03-30
- Type: repo-local import note
- Scope: restate the current downstream-acceptance read so the manuscript-facing
  comparison contract, auxiliary repaired readout, and field-trace boundary are
  explicit
- Basis artifact:
  - reviewed shared-box artifact `GUARANTEE_REVIEW_phase2_downstream_acceptance_readout_2026-03-21_v8.zip`
- Not a new experiment run

## 1. Why v5 exists

`v4` repaired the comparison contract and the in-bundle audit path, but it
still let the manuscript talk half as if downstream acceptance were a filled
supported claim unit. `v5` keeps the same mainline `baseline vs Energy policy`
comparison, but fixes the role read as a downstream boundary surface rather
than a third supported guarantee claim.

## 2. Mainline carried boundary read

The current downstream-acceptance boundary is carried by the mainline
downstream-boundary read that stays on the matched `baseline vs Energy policy`
comparison surface.

Current honest mainline read:
- decisive mainline comparison:
  - `baseline vs Energy policy`
- supported behavior:
  - bounded support for `preacceptance_rework_burden_absent`
- shipped direct mainline audit artifact:
  - `supporting_layer_sources/current/energy_policy_verification_downstream_boundary_baseline_vs_energy_policy_comparison_memo_v1_2026-03-17.md`
- shipped direct run-annotation basis for that memo:
  - `supporting_layer_sources/current/energy_policy_verification_downstream_boundary_run_annotation_anthropic_baseline_v1_2026-03-17.csv`
  - `supporting_layer_sources/current/energy_policy_verification_downstream_boundary_run_annotation_anthropic_energy_policy_v1_2026-03-17.csv`
  - `supporting_layer_sources/current/energy_policy_verification_downstream_boundary_run_annotation_gemini_baseline_v1_2026-03-17.csv`
  - `supporting_layer_sources/current/energy_policy_verification_downstream_boundary_run_annotation_gemini_energy_policy_v1_2026-03-17.csv`
- direct mainline evidence carried forward:
  - Anthropic baseline `0 / 24` -> Energy policy `24 / 24` on
    `preacceptance_rework_burden_absent`
  - Gemini baseline `0 / 24` -> Energy policy `24 / 24` on
    `preacceptance_rework_burden_absent`
- visible residual kept explicit:
  - Gemini Energy-policy `accepted_direction_followthrough_present = 10 / 24`
  - the line does not close as pair-wide downstream-quality support

## 3. Imported auxiliary repaired surface

The reviewed `v8` readout surface remains imported under:
- `results/reviewed_phase2_downstream_acceptance_readout_v8/`

Read the following files there as the current auxiliary repaired readout:
- `guarantee_phase2_priority_resolution_downstream_acceptance_provider_read_table_v1_2026-03-21.csv`
- `guarantee_phase2_priority_resolution_downstream_acceptance_nrr_vs_ablation_comparison_memo_v1_2026-03-21.md`
- `guarantee_phase2_priority_resolution_downstream_acceptance_per_protocol_supplemental_table_v1_2026-03-21.csv`
- `non_evaluative_principle_guarantee_phase2_downstream_acceptance_readout_completion_memo_v8_2026-03-21.md`

Auxiliary repaired read kept visible:
- auxiliary repaired comparison:
  - `NRR vs Ablation`
- provider-first auxiliary repaired read:
  - Anthropic: `inconclusive`
  - Gemini: `support`
  - overall: `mixed`
- additional auxiliary-comparator fact that should not be hidden:
  - on the Anthropic slice, `Baseline` remains stronger than `NRR` on
    `appropriate`

## 4. Field-trace boundary

The second claim keeps the protocol-era direct observability fields in the
manuscript. The repaired imported readout is narrower and should be mapped
explicitly rather than treated as a one-to-one replacement.

- manuscript primary field:
  - `accepted_direction_followthrough_present`
  - repaired auxiliary trace:
    `accepted_branch_followthrough_present`
- manuscript primary field:
  - `rejected_direction_intrusion_absent`
  - repaired auxiliary trace:
    `reopened_choice_absent` plus `alternative_branch_push_absent`
- manuscript primary field:
  - `preacceptance_rework_burden_absent`
  - repaired auxiliary trace:
    no direct `v8` column; this field remains anchored by the mainline
    `baseline vs Energy policy` downstream-boundary memos
- manuscript primary field:
  - `appropriate`
  - repaired auxiliary trace:
    `appropriate`
- repaired auxiliary extra row-level field:
  - `accepted_branch_recognition_present`
  - role:
    useful audit trace, but not a manuscript primary observability field

## 5. Manuscript use / non-use

- manuscript use:
  - the downstream-acceptance boundary closes on the mainline
    `baseline vs Energy policy` comparison
  - supported behavior is bounded `preacceptance_rework_burden_absent`
    improvement only
  - the decisive mainline figures are now directly auditable from the shipped
    comparison memo plus its shipped run-annotation CSVs
  - the repaired `NRR vs Ablation` readout stays visible as an auxiliary
    boundary comparator
  - explicit statement that Anthropic `Baseline` remains stronger than
    Anthropic `NRR` on auxiliary repaired `appropriate`
- manuscript non-use:
  - no treatment of this surface as a third supported guarantee claim unit
  - no pair-wide downstream guarantee
  - no provider-universal downstream-quality claim
  - no claim that the auxiliary repaired read replaces the paper-level
    comparison contract
  - no claim that `NRR` generally dominates `Baseline` on this boundary
  - no explicit quarantine closure
  - no later-horizon stability claim
