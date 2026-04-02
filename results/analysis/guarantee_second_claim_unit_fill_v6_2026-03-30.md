# Guarantee Second Claim Unit Fill v6

## Status
- Date: 2026-03-30
- Type: guarantee drafting memo
- Scope: restate the second bounded `Guarantee` surface with an explicit
  manuscript-facing comparison contract
- Depends on:
  - `guarantee_phase2_downstream_acceptance_closure_import_note_v3_2026-03-30.md`
  - `../reviewed_phase2_downstream_acceptance_readout_v8/guarantee_phase2_priority_resolution_downstream_acceptance_provider_read_table_v1_2026-03-21.csv`
  - `../reviewed_phase2_downstream_acceptance_readout_v8/guarantee_phase2_priority_resolution_downstream_acceptance_nrr_vs_ablation_comparison_memo_v1_2026-03-21.md`
  - `../../supporting_layer_sources/current/policy_verification_pilot_protocol_current_v1_2026-03-18.md`
  - `../../supporting_layer_sources/current/energy_guarantee_claim_schema_candidate_v2_2026-03-17.md`
- Not a final manuscript claim freeze

## 1. Current bounded read

The current second claim unit remains the repaired downstream-acceptance
surface. Its truthful current read is:
- primary comparison: `NRR vs Ablation`
- auxiliary comparator: `Baseline`
- Anthropic: `inconclusive`
- Gemini: `support`
- overall: `mixed`

The same reviewed comparison memo also records that Anthropic `Baseline`
remains stronger than Anthropic `NRR` on `appropriate`. That fact belongs in
the manuscript-facing boundary read, not outside it.

## 2. Filled claim unit

### 2.1 provider_scope
- the tested provider pair only:
  - Anthropic `claude-sonnet-4-6`
  - Gemini `gemini-2.0-flash`

### 2.2 family_scope
- the repaired downstream-acceptance family only

### 2.3 horizon_scope
- the first accepted-direction downstream boundary only

### 2.4 observability_scope
- the repaired downstream-acceptance readout fields only:
  - `accepted_direction_followthrough_present`
  - `rejected_direction_intrusion_absent`
  - `preacceptance_rework_burden_absent`
  - `appropriate`

### 2.5 comparison_scope
- reviewed provider-first downstream-acceptance readout surface imported under
  `results/reviewed_phase2_downstream_acceptance_readout_v8/`
- decisive primary comparison:
  - `NRR vs Ablation`
- auxiliary comparator:
  - `Baseline`

### 2.6 supported_behavior
- bounded mixed downstream-acceptance read:
  - Gemini reaches `support`
  - Anthropic remains `inconclusive`
  - Anthropic `Baseline` remains stronger than Anthropic `NRR` on
    `appropriate`

### 2.7 explicit_failure_boundary
- this surface does not close as pair-wide support
- it does not authorize provider-universal downstream handoff quality
- it does not support a monotone `baseline -> Energy -> NRR` carry-forward read
- it does not support any claim that `NRR` generally dominates `Baseline`
- it does not establish explicit quarantine closure or later-horizon stability

### 2.8 unsupported_extension
- pair-wide downstream-acceptance guarantee language
- provider-universal downstream-quality claims
- side-topic/quarantine guarantees
- later-horizon continuation guarantees

## 3. Manuscript-facing claim sentence

Under the tested provider pair, for the repaired downstream-acceptance family,
at the first accepted-direction downstream boundary, and on the directly scored
fields `accepted_direction_followthrough_present`,
`rejected_direction_intrusion_absent`, `preacceptance_rework_burden_absent`,
and `appropriate`, the truthful current read is a bounded mixed result on a
primary `NRR vs Ablation` comparison rather than a pair-wide uniform outcome:
Gemini reaches support, while Anthropic remains inconclusive, and the
Anthropic-side auxiliary comparison keeps `Baseline` stronger than `NRR` on
`appropriate`. This surface therefore supports only bounded mixed
downstream-acceptance reporting, not pair-wide downstream-guarantee language,
not a monotone mainline-comparison success story, and not broader quarantine or
later-horizon closure claims.
