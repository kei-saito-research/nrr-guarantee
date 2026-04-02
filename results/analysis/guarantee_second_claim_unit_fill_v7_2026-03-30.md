# Guarantee Second Claim Unit Fill v7

## Status
- Date: 2026-03-30
- Type: guarantee drafting memo
- Scope: restate the second bounded `Guarantee` surface under the restored
  manuscript-facing single-contract rule
- Status note:
  - superseded historical drafting note
  - for the current `v38` line, use
    `guarantee_downstream_acceptance_boundary_surface_v1_2026-03-30.md`
  - do not read this memo as the current manuscript-facing authority surface
- Depends on:
  - `guarantee_phase2_downstream_acceptance_closure_import_note_v4_2026-03-30.md`
  - `../../supporting_layer_sources/current/energy_policy_verification_downstream_boundary_baseline_vs_energy_policy_comparison_memo_v1_2026-03-17.md`
  - `../../supporting_layer_sources/current/energy_policy_verification_downstream_boundary_run_annotation_anthropic_baseline_v1_2026-03-17.csv`
  - `../../supporting_layer_sources/current/energy_policy_verification_downstream_boundary_run_annotation_anthropic_energy_policy_v1_2026-03-17.csv`
  - `../../supporting_layer_sources/current/energy_policy_verification_downstream_boundary_run_annotation_gemini_baseline_v1_2026-03-17.csv`
  - `../../supporting_layer_sources/current/energy_policy_verification_downstream_boundary_run_annotation_gemini_energy_policy_v1_2026-03-17.csv`
  - `../../supporting_layer_sources/current/energy_priority_resolution_downstream_acceptance_two_provider_read_memo_v1_2026-03-17.md`
  - `../../supporting_layer_sources/current/energy_policy_verification_downstream_boundary_scope_candidate_v1_2026-03-17.md`
  - `../reviewed_phase2_downstream_acceptance_readout_v8/guarantee_phase2_priority_resolution_downstream_acceptance_provider_read_table_v1_2026-03-21.csv`
  - `../reviewed_phase2_downstream_acceptance_readout_v8/guarantee_phase2_priority_resolution_downstream_acceptance_nrr_vs_ablation_comparison_memo_v1_2026-03-21.md`
  - `../../supporting_layer_sources/current/policy_verification_pilot_protocol_current_v1_2026-03-18.md`
  - `../../supporting_layer_sources/current/energy_guarantee_claim_schema_candidate_v2_2026-03-17.md`
- Not a final manuscript claim freeze

## 1. Historical bounded read

This memo captured a pre-`v38` staging read in which the downstream-acceptance
surface still occupied the second carried slot. For the current `v38` line,
the authoritative downstream read is instead carried by
`guarantee_downstream_acceptance_boundary_surface_v1_2026-03-30.md`.
The historical read recorded here was:
- mainline comparison:
  - `baseline vs Energy policy`
- supported behavior:
  - bounded support for `preacceptance_rework_burden_absent`
- shared mainline gain:
  - both tested provider slices move from `0 / 24` to `24 / 24` on
    `preacceptance_rework_burden_absent`
- direct shipped mainline audit path:
  - the bundle now includes the baseline-vs-Energy comparison memo itself
  - that memo's four run-annotation CSV dependencies are also shipped locally
- visible residual:
  - Gemini still shows partial first accepted-direction followthrough
- auxiliary repaired comparator kept visible:
  - reviewed `NRR vs Ablation`
  - Anthropic: `inconclusive`
  - Gemini: `support`
  - Anthropic `Baseline` remains stronger than Anthropic `NRR` on
    `appropriate`

## 2. Historical filled claim unit

### 2.1 provider_scope
- the tested provider pair only:
  - Anthropic `claude-sonnet-4-6`
  - Gemini `gemini-2.0-flash`

### 2.2 family_scope
- the repaired downstream-acceptance family only

### 2.3 horizon_scope
- the first accepted-direction downstream boundary only

### 2.4 observability_scope
- the protocol-era downstream-boundary fields only:
  - `accepted_direction_followthrough_present`
  - `rejected_direction_intrusion_absent`
  - `preacceptance_rework_burden_absent`
  - `appropriate`
- for auxiliary repaired-readout audit only:
  - `accepted_branch_followthrough_present`
  - `reopened_choice_absent`
  - `alternative_branch_push_absent`
  - `appropriate`
- additional repaired row-level audit field only:
  - `accepted_branch_recognition_present`

### 2.5 comparison_scope
- matched baseline vs Energy-policy comparison under the frozen downstream-
  boundary pilot conditions
- auxiliary repaired comparison retained for boundary reporting only:
  - reviewed `NRR vs Ablation`
- auxiliary comparator that remains visible in that repaired read:
  - `Baseline`

### 2.6 supported_behavior
- bounded support for removal of preacceptance rework burden under the first
  accepted-direction downstream boundary
- both provider slices reach `24 / 24` on `preacceptance_rework_burden_absent`
  under the mainline comparison
- the downstream line still remains provider-sensitive beyond that shared gain

### 2.7 explicit_failure_boundary
- this surface does not close as pair-wide downstream-quality support
- Gemini still retains first accepted-direction followthrough residuals on part
  of the tested surface
- the auxiliary repaired `NRR vs Ablation` read remains mixed
- Anthropic `Baseline` remains stronger than Anthropic `NRR` on auxiliary
  repaired `appropriate`
- this surface does not establish explicit quarantine closure or later-horizon
  stability

### 2.8 unsupported_extension
- pair-wide downstream-acceptance guarantee language
- provider-universal downstream-quality claims
- any claim that the repaired auxiliary read replaces the mainline comparison
  contract
- side-topic/quarantine guarantees
- later-horizon continuation guarantees

## 3. Historical manuscript-facing claim sentence

Under the tested provider pair, for the downstream-acceptance family, at the
first accepted-direction downstream boundary, and on the directly scored fields
`accepted_direction_followthrough_present`,
`rejected_direction_intrusion_absent`, `preacceptance_rework_burden_absent`,
and `appropriate`, the matched `baseline vs Energy policy` surface supports
only bounded removal of preacceptance rework burden rather than pair-wide
downstream-quality closure: both provider slices reach `24 / 24` on
`preacceptance_rework_burden_absent`, but Gemini still retains partial
first-followthrough residuals on part of the tested surface. The imported
repaired `NRR vs Ablation` read remains auxiliary boundary evidence only:
Gemini reaches support there, Anthropic remains inconclusive, and the
Anthropic-side auxiliary comparison keeps `Baseline` stronger than `NRR` on
`appropriate`. This surface therefore does not authorize pair-wide downstream-
guarantee language, quarantine closure, or later-horizon stability claims.
