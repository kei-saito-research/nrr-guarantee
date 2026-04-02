# Guarantee Second Claim Unit Fill v1

## Status
- Date: 2026-03-20
- Type: guarantee drafting memo
- Scope: choose and fill the second explicit bounded claim unit for the current
  `Guarantee` manuscript line
- Depends on:
  - `series_planning/policy_verification_pilot_protocol_current_v1_2026-03-18.md`
  - `review_pack/ENERGY_REVIEW_policy_verification_downstream_boundary_scope_2026-03-17_v1/CONTEXT/energy_guarantee_claim_schema_candidate_v2_2026-03-17.md`
  - `nrr-energy/results/analysis/energy_policy_verification_downstream_boundary_baseline_vs_energy_policy_comparison_memo_v1_2026-03-17.md`
  - `nrr-energy/results/analysis/energy_policy_verification_downstream_boundary_readout_external_review_decision_memo_v1_2026-03-17.md`
  - `nrr-energy/results/analysis/energy_priority_resolution_manuscript_boundary_text_v2_2026-03-18.md`
- Not a final manuscript claim freeze

## 1. Assistant-Side Decision
- judgment:
  - `adopt`
- reason:
  - the downstream-boundary / preacceptance-burden surface is the next safest
    `Guarantee` fill because the shared gain is real in both provider slices while
    the active Gemini residual remains explicit enough to keep the claim narrow

## 2. Why This Claim Unit Comes Second
After the early ambiguity-turn unit, the downstream-boundary surface is the next
best bounded candidate because:
1. both provider slices remove `preacceptance_rework_burden_absent` under matched
   conditions
2. the readout is externally cross-checked
3. the remaining limit is visible and manuscript-useful:
   downstream burden removal does not by itself guarantee clean first accepted-
   direction followthrough on all rows

## 3. Filled Claim Unit

### 3.1 provider_scope
- the tested provider pair only:
  - Anthropic `claude-sonnet-4-6`
  - Gemini `gemini-2.0-flash`

### 3.2 family_scope
- frozen downstream-boundary / preacceptance-burden family only

### 3.3 horizon_scope
- the first accepted-direction downstream boundary only

### 3.4 observability_scope
- the frozen downstream pilot annotation fields only:
  - `accepted_direction_followthrough_present`
  - `rejected_direction_intrusion_absent`
  - `preacceptance_rework_burden_absent`
  - `appropriate`

### 3.5 comparison_scope
- matched baseline vs Energy-policy comparison under the frozen downstream-
  boundary pilot conditions

### 3.6 supported_behavior
- removal of preacceptance rework burden under accepted-direction downstream
  follow-up

### 3.7 explicit_failure_boundary
- the shared support is burden removal, not full downstream followthrough closure
- Gemini retains first accepted-direction follow-up residuals on part of the
  frozen surface
- this fill does not establish explicit quarantine or later-horizon stability

### 3.8 unsupported_extension
- provider-universal downstream handoff quality
- side-topic/quarantine guarantees
- later-horizon continuation guarantees
- broad end-task quality claims

## 4. Evidence Read Supporting This Fill
Under the frozen downstream-boundary pilot:
- Anthropic baseline `preacceptance_rework_burden_absent = 1`: `0 / 24`
- Anthropic Energy-policy `preacceptance_rework_burden_absent = 1`: `24 / 24`
- Gemini baseline `preacceptance_rework_burden_absent = 1`: `0 / 24`
- Gemini Energy-policy `preacceptance_rework_burden_absent = 1`: `24 / 24`

The active residual stays visible:
- Gemini Energy-policy `accepted_direction_followthrough_present = 1`: `10 / 24`
- the weakest residual remains `C_incident_response`, where acknowledgment can
  persist without concrete workstart

The external readout gate is already closed for this pilot:
- independent Codex review: `adopt`
- Claude review: `adopt`

## 5. Manuscript-Facing Claim Sentence
Under the tested provider pair, for the frozen downstream-boundary /
preacceptance-burden family, at the first accepted-direction downstream boundary,
and on the directly scored fields `accepted_direction_followthrough_present`,
`rejected_direction_intrusion_absent`, `preacceptance_rework_burden_absent`, and
`appropriate`, the Energy-policy arm is supported relative to matched baseline
only for removal of preacceptance rework burden. This support excludes provider-
universal downstream handoff quality, explicit quarantine closure, and later-
horizon stability, and it remains bounded by the visible Gemini first-follow-up
residual on part of the tested surface.

## 6. Manuscript-Facing Evidence Paragraph
The next supportable `Guarantee` entry point is the frozen downstream-boundary
pilot. Under matched baseline vs Energy-policy conditions, both tested provider
slices moved from `0 / 24` to `24 / 24` on
`preacceptance_rework_burden_absent`, which means the policy reliably removed the
need to rework preacceptance material before following the accepted direction.
However, this gain did not collapse all downstream behavior into one clean story:
Anthropic remained clean on the frozen surface, while Gemini still showed weak
first accepted-direction followthrough on part of the surface, especially in
`C_incident_response`. The carry-forward read is therefore a bounded downstream
burden-removal claim, not a provider-universal downstream-quality or later-
horizon stability claim.
