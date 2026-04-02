# Energy Policy-Verification Pilot Scope External Review Decision Memo v1

## Status
- Date: 2026-03-17
- Type: external review decision memo
- Scope: record the assistant-side evaluation after one independent Codex review and one Claude review on the first `Policy-Verification` pilot scope
- Review target:
  - `energy_policy_verification_pilot_scope_candidate_v1_2026-03-17.md`
- Not a run authorization memo
- Not a manuscript claim memo

## External Review Results
- independent Codex review:
  - `adopt`
  - scope is narrow and role-consistent
  - non-blocking clarification points only:
    - keep `appropriate` tied to the formal frozen rubric field names in the next memo
    - make the `failure-boundary reporting rule` explicit in the next memo
    - decide in advance how provider slices will be shown to avoid provider-universal readings

- Claude review:
  - `adopt`
  - field freeze is structurally complete
  - non-blocking clarification points only:
    - use the current canonical Anthropic model string in the next memo
    - state explicitly that the three observability metrics come directly from the frozen ambiguity-turn scoring
    - freeze exact baseline / Energy-policy prompt-surface correspondence in the next memo

## Assistant-Side Evaluation
- decision:
  - `adopt`
- reason:
  - both reviews accept the scope itself and ask for implementation-level design clarifications that belong in the next exact pilot-design memo rather than in the scope freeze

## Next Practical Read
1. keep the scope freeze unchanged
2. cut one exact pilot-design memo that fixes:
   - baseline arm prompt surface
   - Energy-policy arm prompt surface
   - canonical model strings
   - observability provenance
   - failure-boundary reporting rule
3. send that exact design memo for narrow review before any run authorization

## Primary References
- `energy_policy_verification_pilot_scope_candidate_v1_2026-03-17.md`
- `energy_policy_verification_pilot_scope_review_brief_v1_2026-03-17.md`
