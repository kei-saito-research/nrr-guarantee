# Policy Minimal Spec Current v1

## Status
- Date: 2026-03-18
- Type: current canonical policy memo
- Scope: establish the current canonical minimal `Policy` specification after the closed `Energy -> Policy` handoff, without reopening `Energy` or widening into `Policy-Verification` or `Guarantee`
- Depends on:
  - `energy_to_policy_handoff_memo_v1_2026-03-18.md`
  - `energy_to_guarantee_program_design_brief_v1_2026-03-17.md`
  - `energy_priority_resolution_package_map_v1_2026-03-18.md`
  - `energy_policy_minimal_spec_candidate_v2_2026-03-17.md`
- Supersedes as the current Policy entry point:
  - `energy_policy_minimal_spec_candidate_v2_2026-03-17.md`
- Not a manuscript claim memo
- Not a run-authorization memo

## 1. Assistant-Side Decision
- judgment:
  - `adopt`
- reason:
  - the closed `Energy` handoff now fixes enough bounded evidence and boundary language to promote the earlier candidate into a current downstream `Policy` source without widening the claim surface

## 2. Role Of Policy In The Current Program
`Policy` takes the fixed `Energy` measurement read and turns it into the smallest explicit action specification needed for downstream work.

This current spec does three things only:
- freeze the minimal state vocabulary
- freeze the minimal action vocabulary
- define the minimal commit / defer / check / quarantine rules that `Dynamics`, `Policy-Verification`, and `Guarantee` can inherit without redesigning `Policy`

This spec does not:
- reopen `Energy`
- claim prospective program-scale validity
- define `Guarantee`
- absorb `baseline vs Energy policy` into `Policy`

## 3. Fixed Upstream Inputs From Energy
Treat the following `Energy` read as fixed upstream input:
- ambiguity-turn gain
- downstream preacceptance-burden gain
- repaired first-step side-topic / quarantine gain on the tested provider pair
- conditional later-horizon boundary

Keep the current boundary language fixed:
- side-topic gain is not uniform across templates
- baseline is already fairly strong on `A_trip_planning` and `B_hiring_packet`
- the main incremental first-step lift is concentrated in `C_incident_response`
- later-horizon behavior remains conditional rather than uniformly stable

## 4. Ownership Boundary
- `Policy`:
  - owns the minimal action specification only
- `Dynamics`:
  - owns the time-extended hold / degrade description of the frozen policy vocabulary
- `Policy-Verification`:
  - owns prospective `baseline vs Energy policy` validation under selected conditions
- `Guarantee`:
  - owns bounded claims under explicit provider / family / horizon / observability conditions

Therefore:
- broader forward validation is not unfinished `Energy`
- wider universality chasing is not unfinished `Policy`
- `Energy` stays closed unless a genuinely new `Energy`-owned contradiction appears

## 5. Frozen State Vocabulary
Use the following state terms only.

1. `active_objective`
- the currently chosen working direction for the next useful assistant move
- if an `accepted_direction` exists, it becomes the current `active_objective` unless a later explicit release or replacement occurs

2. `suspended_objective`
- a previously active direction that is intentionally not advanced for now

3. `unresolved_relation`
- a relation whose exact ordering, interpretation, or binding still matters for the next step and has not yet been fixed by the user

4. `accepted_direction`
- the direction explicitly selected by the user, or explicitly accepted by the user after a revisable recommendation
- `revisable recommendation` means a recommendation whose direction is still left open for user acceptance or correction rather than treated as already fixed

5. `quarantine`
- the rule that the `suspended_objective` must not re-enter content planning unless release conditions are met

6. `local_relation_block`
- a local state in which the next useful move depends on resolving one `unresolved_relation`

## 6. Frozen Action Set
Use only these action classes.

1. `defer_with_resolution`
- allowed forms:
  - explicit choice question
  - revisable recommendation
- use when:
  - direction choice is not yet accepted
- required boundary:
  - do not begin substantive content work before direction acceptance

2. `commit_to_accepted_direction`
- use when:
  - one direction is already accepted
  - the next useful step does not depend on collapsing an unresolved relation
- required boundary:
  - progress the accepted direction directly
  - keep the suspended objective quarantined

3. `commit_with_relation_preservation`
- use when:
  - one direction is accepted
  - the next useful step can proceed while keeping an unresolved relation open
- required boundary:
  - preserve the unresolved relation explicitly rather than forcing one interpretation

4. `narrow_downstream_check`
- use when:
  - one direction is accepted
  - the next useful step is blocked by one local unresolved relation
- required boundary:
  - ask only the smallest clarification needed for the next step
  - do not reopen the suspended objective
  - do not reset the conversation back to the initial starter question

5. `release_quarantine`
- use when:
  - the user explicitly reactivates the suspended objective, or
  - the accepted direction has been explicitly completed or explicitly parked, and the user requests return
- minimal completion / park rule:
  - `completed` means the immediate accepted-direction deliverable has been provided or closed
  - `parked` means the user explicitly pauses or sets aside the accepted direction for now
- required boundary:
  - release must be user-triggered or explicitly task-state-triggered, not assistant-assumed

## 7. Condition Rules
### 7.1 Pre-acceptance rule
If priority is unresolved and no direction has been accepted:
- default to `defer_with_resolution`
- do not commit to content on either side
- do not fix ordering on the user's behalf

### 7.2 Post-acceptance rule
If one direction is accepted:
- default to `commit_to_accepted_direction`
- mark the previous main line as `suspended_objective` when applicable
- enforce `quarantine`

### 7.3 Unresolved-relation rule
If the accepted direction contains an `unresolved_relation`:
- prefer `commit_with_relation_preservation`
- escalate to `narrow_downstream_check` only when the immediate next useful move cannot be produced without deciding that relation
- never convert the unresolved relation into a silent assistant-side commitment

### 7.4 Later-horizon rule
Across later checkpoints:
- preserving `quarantine` is necessary but not sufficient
- the first shared watch point is premature commitment on `unresolved_relation`
- later-horizon stability should therefore be read first through relation handling, not only through suspended-main reactivation

## 8. Failure Boundary
Treat the following as policy failures.

### 8.1 Over-commit failures
- unilateral direction choice before user acceptance
- content work before direction acceptance
- premature commitment on unresolved ordering or interpretation
- reactivating the suspended objective without a release condition

### 8.2 Over-defer failures
- repeated starter-style questioning after the direction is already accepted
- generic acknowledgment without useful progress on the accepted direction
- using clarification as a delay tactic when no local relation actually blocks the next step

## 9. Downstream Interface Rules
### 9.1 Dynamics
- use this frozen vocabulary as-is
- describe how `active_objective`, `suspended_objective`, `quarantine`, and `unresolved_relation` hold or degrade over turns
- do not redesign the policy object while writing the mechanism skeleton

### 9.2 Policy-Verification
- treat `baseline vs Energy policy` as downstream-owned prospective validation
- freeze provider / family / metric in a separate verification artifact
- keep the claim narrow and selected-condition-bounded
- do not silently widen beyond the currently supported family

### 9.3 Guarantee
- build claims only from explicit provider / family / horizon / observability conditions
- do not treat this policy spec by itself as a guarantee

## 10. Current Canonical Use Rule
If someone asks where to restart the `Policy` layer, start here.

Operational rule:
- read this file after the handoff memo and program design brief
- use this file as the current canonical `Policy` source
- do not reopen `Energy` unless a genuinely new `Energy`-owned contradiction is identified explicitly
