# Guarantee First Claim Unit Fill v2

## Status
- Date: 2026-03-20
- Type: guarantee drafting memo
- Scope: choose and fill the first explicit bounded claim unit for the current
  `Guarantee` manuscript line
- Depends on:
  - `supporting_layer_sources/current/policy_verification_pilot_protocol_current_v1_2026-03-18.md`
  - `supporting_layer_sources/current/energy_guarantee_claim_schema_candidate_v2_2026-03-17.md`
  - `supporting_layer_sources/current/energy_priority_resolution_annotation_minispec_v1_2026-03-16.md`
  - `supporting_layer_sources/current/energy_policy_verification_pilot_readout_external_review_decision_memo_v1_2026-03-17.md`
  - `supporting_layer_sources/current/energy_priority_resolution_manuscript_boundary_text_v2_2026-03-18.md`
- Not a final manuscript claim freeze

## 1. Assistant-Side Decision
- judgment:
  - `adopt`
- reason:
  - the early ambiguity-turn surface is the cleanest first `Guarantee` entry point
    because the tested provider pair moves in the same direction, the matched
    conditions are explicit, the readout is externally cross-checked, and the
    remaining boundary is easy to keep narrow

## 2. Why This Claim Unit Comes First
The current branch has several bounded downstream gains:
- early ambiguity-turn non-unilateral priority resolution
- downstream preacceptance-burden removal
- repaired first-step side-topic / quarantine improvement

For the first explicit claim unit, the early ambiguity-turn surface is the safest
starting point because:
1. both provider slices show the same full-direction improvement under matched
   conditions
2. no residual failure rows appear on the frozen mini-spec surface
3. the out-of-scope boundary remains easy to state:
   no downstream, side-topic, later-horizon, or provider-universal extension

## 3. Filled Claim Unit

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
- matched baseline vs Energy-policy comparison under the frozen early
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

## 4. Evidence Read Supporting This Fill
Under the frozen early ambiguity-turn pilot:
- Anthropic baseline `appropriate = 1`: `0 / 24`
- Anthropic Energy-policy `appropriate = 1`: `24 / 24`
- Gemini baseline `appropriate = 1`: `0 / 24`
- Gemini Energy-policy `appropriate = 1`: `24 / 24`

Provider slices are the primary read. The shared direction of change supports a
tested-provider-pair bounded claim, not a provider-universal claim.

The external readout gate is already closed for this pilot:
- independent Codex review: `adopt`
- Claude review: `adopt`

## 5. Manuscript-Facing Claim Sentence
Under the tested provider pair, for the frozen `priority-resolution`
ambiguity-turn family, at the early decision boundary, and on the directly scored
fields `resolution_attempt_present`, `unilateral_commit_absent`, and
`appropriate`, the Energy-policy arm is supported relative to matched baseline
only for non-unilateral priority resolution. This support excludes downstream
acceptance, side-topic/quarantine, and later-horizon behavior, and it does not
extend to provider-universal or broad downstream-quality claims.

## 6. Manuscript-Facing Evidence Paragraph
The strongest current entry point for the `Guarantee` line is the frozen early
ambiguity-turn pilot. Under matched baseline vs Energy-policy conditions, both
tested provider slices moved from `0 / 24` to `24 / 24` on the pilot's
`appropriate` field, while baseline failure modes remained visible as either
ambiguity-preserving but unresolved responses or unilateral/content-before-
resolution behavior. The externally cross-checked carry-forward read is therefore
that the Energy-policy surface supports non-unilateral priority resolution at the
early decision boundary on the tested provider pair. This is a bounded early
control claim only; it does not by itself establish downstream followthrough,
quarantine behavior, later-horizon stability, or provider-universal validity.
