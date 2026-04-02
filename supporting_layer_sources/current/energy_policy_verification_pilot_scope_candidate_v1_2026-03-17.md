# Energy Policy-Verification Pilot Scope Candidate v1

## Status
- Date: 2026-03-17
- Type: pilot-scope freeze memo
- Scope: freeze the first narrow `Policy-Verification` pilot scope under the current `Policy`, `Dynamics`, and `Guarantee` constraints
- Depends on:
  - `energy_policy_minimal_spec_candidate_v2_2026-03-17.md`
  - `energy_dynamics_mechanism_skeleton_candidate_v2_2026-03-17.md`
  - `energy_guarantee_claim_schema_candidate_v2_2026-03-17.md`
  - `energy_priority_resolution_two_provider_read_memo_v1_2026-03-16.md`
  - `energy_priority_resolution_downstream_acceptance_two_provider_read_memo_v1_2026-03-17.md`
- Not a run authorization memo
- Not a manuscript claim memo

## 1. Purpose
This memo freezes the first narrow `Policy-Verification` pilot scope.

It does not yet:
- authorize execution
- finalize the exact run table
- expand to multiple family claims at once

Its role is narrower:
- choose the first claim-field values that the pilot will target
- freeze the provider / family / horizon / observability / comparison scope before any new pilot wording is written

## 2. Assistant-Side Read
- judgment:
  - `adopt`
- reason:
  - the current line already supports several bounded claim shapes, but the narrowest mainline pilot is the early-control ambiguity family because it is the strongest clean two-provider read and maps directly to the frozen policy action set

## 3. Why This Family Is First
The first pilot should target the narrowest claim that is:
1. already strongly supported by current evidence
2. directly expressed by the frozen `Policy`
3. easy to compare against a plain baseline under matched conditions
4. clean enough to support later bounded `Guarantee` language without borrowing downstream or later-horizon complexity

Current assistant-side decision:
- first pilot family:
  - `priority-resolution ambiguity resolution without unilateral commitment`

Deferred for later pilots:
- downstream acceptance
- first-step side-topic commitment
- later-horizon stability

Reason for deferral:
- those families are real and useful, but they add stronger provider sensitivity, later-horizon boundary complexity, or extra episode structure

## 4. Targeted Guarantee-Field Fill
The first pilot is designed against the following field values.

### 4.1 `provider_scope`
- tested provider pair only:
  - `anthropic` / `claude-sonnet-4-20250514`
  - `gemini` / `gemini-2.0-flash`

### 4.2 `family_scope`
- one family only:
  - `priority-resolution ambiguity resolution`

### 4.3 `horizon_scope`
- one checkpoint band only:
  - the ambiguity-turn response at the early decision boundary

### 4.4 `observability_scope`
- one frozen metric family only:
  - `resolution_attempt_present`
  - `unilateral_commit_absent`
  - `appropriate`

### 4.5 `comparison_scope`
- mainline comparison only:
  - baseline vs Energy policy under matched conditions

### 4.6 `supported_behavior`
- non-unilateral priority resolution on the ambiguity-turn surface

### 4.7 `explicit_failure_boundary`
- failure may still appear as:
  - no resolution attempt
  - unilateral commitment
  - provider-specific baseline failure structure
- the claim does not extend beyond the ambiguity-turn boundary

### 4.8 `unsupported_extension`
- downstream acceptance
- side-topic workstart quality
- later-horizon followthrough
- provider universality
- broad conversation-policy validity

## 5. Frozen Pilot Scope
### 5.1 Unit of analysis
- one ambiguity-turn assistant response only

### 5.2 Surface family
- the same frozen three-template ambiguity surface used in the current policy line:
  - `A_trip_planning`
  - `B_hiring_packet`
  - `C_incident_response`

### 5.3 Matched conditions
- provider
- model
- temperature
- reps
- exact user-turn pair per template
- same scoring procedure across both arms

### 5.4 Primary settings
- temperature:
  - `0.0`
- reps:
  - `8` per provider

## 6. Why This Scope Is Narrow Enough
1. one family only
2. one horizon only
3. one metric family only
4. one mainline comparison only
5. one tested provider pair only

This avoids:
- bundling early-control and downstream acceptance into one claim
- using later-horizon instability as if it were part of the same success claim
- drifting into long-horizon or broad conversation-policy validation

## 7. What This Pilot Would Need To Freeze Next
After this scope freeze, the next design memo should freeze:
1. the exact pilot input artifact
2. the exact baseline arm prompt surface
3. the exact Energy-policy arm prompt surface
4. the scoring / annotation procedure
5. the reporting table including gains and explicit failure counts

## 8. What This Pilot Would Answer
This pilot would answer:
- under the tested provider pair and fixed ambiguity-turn surface, does the frozen Energy policy reproduce non-unilateral priority resolution relative to baseline under matched conditions?

## 9. What This Pilot Would Not Answer
This pilot would not answer:
- downstream acceptance quality
- first-step side-topic commitment quality
- later-horizon stability
- overall task quality
- guarantee closure beyond the early boundary

## 10. Current Boundary
The current branch evidence may motivate later pilots on downstream or later-horizon families.
But those are not part of the first `Policy-Verification` pilot scope.

If a later memo wants to include them, it should open a new scope artifact rather than silently widening this one.

## 11. Review Question
Is this first `Policy-Verification` pilot scope narrow, role-consistent, and aligned with `Guarantee schema v2`?

## Primary References
- `energy_policy_minimal_spec_candidate_v2_2026-03-17.md`
- `energy_dynamics_mechanism_skeleton_candidate_v2_2026-03-17.md`
- `energy_guarantee_claim_schema_candidate_v2_2026-03-17.md`
- `energy_priority_resolution_two_provider_read_memo_v1_2026-03-16.md`
