# Guarantee First Claim Unit Fill v3

## Status
- Date: 2026-03-30
- Type: guarantee drafting memo
- Scope: restate the first bounded `Guarantee` claim unit so the shipped review
  surface contains the direct comparison memo used by the claim
- Depends on:
  - `../../supporting_layer_sources/current/policy_verification_pilot_protocol_current_v1_2026-03-18.md`
  - `../../supporting_layer_sources/current/energy_guarantee_claim_schema_candidate_v2_2026-03-17.md`
  - `../../supporting_layer_sources/current/energy_priority_resolution_annotation_minispec_v1_2026-03-16.md`
  - `../../supporting_layer_sources/current/energy_policy_verification_pilot_readout_external_review_decision_memo_v1_2026-03-17.md`
  - `../../supporting_layer_sources/current/energy_policy_verification_priority_resolution_baseline_vs_energy_policy_comparison_memo_v1_2026-03-17.md`
  - `../../supporting_layer_sources/current/energy_priority_resolution_manuscript_boundary_text_v2_2026-03-18.md`
- Not a final manuscript claim freeze

## 1. Current bounded read

The first `Guarantee` claim unit remains the frozen early ambiguity-turn pilot.
Its truthful read is unchanged:
- tested provider pair only
- matched `baseline vs Energy-policy` comparison only
- supported only for non-unilateral priority resolution at the early decision
  boundary

## 2. Why v3 exists

`v2` already carried the correct bounded claim, but the shipped review surface
did not include the direct baseline-vs-Energy comparison memo named by the
policy-verification external-review note. `v3` keeps the claim unchanged while
making that direct comparison dependency explicit inside the repo-local review
surface.

## 3. Filled claim unit

### 3.1 provider_scope
- the tested provider pair only:
  - Anthropic `claude-sonnet-4-6`
  - Gemini `gemini-2.0-flash`

### 3.2 family_scope
- frozen `priority-resolution` early ambiguity-turn family only

### 3.3 horizon_scope
- the early decision boundary only

### 3.4 observability_scope
- the frozen pilot annotation fields only:
  - `resolution_attempt_present`
  - `unilateral_commit_absent`
  - `appropriate`

### 3.5 comparison_scope
- matched `baseline vs Energy-policy` comparison under the frozen early
  ambiguity-turn pilot conditions

### 3.6 supported_behavior
- non-unilateral priority resolution at the ambiguity turn

### 3.7 explicit_failure_boundary
- this fill does not establish downstream acceptance quality
- this fill does not establish side-topic or quarantine behavior
- this fill does not establish later-horizon stability

### 3.8 unsupported_extension
- provider-universal commit/defer guarantees
- long-horizon followthrough claims
- broad downstream-quality or end-task-quality claims

## 4. Direct comparison evidence

The shipped repo surface now includes the direct comparison memo:
- `../../supporting_layer_sources/current/energy_policy_verification_priority_resolution_baseline_vs_energy_policy_comparison_memo_v1_2026-03-17.md`

That memo records the matched early ambiguity-turn comparison:
- Anthropic baseline `appropriate = 1`: `0 / 24`
- Anthropic Energy-policy `appropriate = 1`: `24 / 24`
- Gemini baseline `appropriate = 1`: `0 / 24`
- Gemini Energy-policy `appropriate = 1`: `24 / 24`

Historical assistant-side review records exist in the planning layer, but the
current shipped claim read does not require an `externally cross-checked`
manuscript guarantee. The current package basis for this fill is the direct
comparison evidence above plus the explicit boundary sentence below.

## 5. Manuscript-facing claim sentence

Under the tested provider pair, for the frozen `priority-resolution`
ambiguity-turn family, at the early decision boundary, and on the directly
scored fields `resolution_attempt_present`, `unilateral_commit_absent`, and
`appropriate`, the Energy-policy arm is supported relative to matched baseline
only for non-unilateral priority resolution. This support excludes downstream
acceptance, side-topic/quarantine, and later-horizon behavior, and it does not
extend to provider-universal or broad downstream-quality claims.
