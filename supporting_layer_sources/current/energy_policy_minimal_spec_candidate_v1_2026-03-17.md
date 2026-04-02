# Energy Policy Minimal Spec Candidate v1

## Status
- Date: 2026-03-17
- Type: policy candidate memo
- Scope: define the first minimal `Policy` specification that follows the current `Energy` package read without widening into `Policy-Verification` or `Guarantee`
- Depends on:
  - `energy_priority_resolution_protocol_freeze_decision_memo_v1_2026-03-16.md`
  - `energy_priority_resolution_branch_synthesis_memo_v2_2026-03-17.md`
  - `energy_priority_resolution_horizon_stability_family_synthesis_memo_v1_2026-03-17.md`
  - `energy_forward_validation_protocol_v11_2026-03-14.md`
- Not a run authorization memo
- Not a manuscript claim memo

## 1. Purpose
`Energy` is now closed enough to support a narrow policy-design step.

This memo does only one thing:
- convert the current measured `priority-resolution` read into the smallest frozen action specification that can later be checked by `Dynamics` and `Policy-Verification`

This memo does not:
- claim that the policy already works prospectively at program scale
- define `Guarantee`
- widen the surface beyond the currently supported family

## 2. Assistant-Side Read
- judgment:
  - `adopt`
- reason:
  - the current branch already fixes a reproducible early control region, a narrow downstream boundary, and a measured later-horizon failure mode, which is enough to freeze a minimal policy vocabulary without pretending that later-horizon stability is solved

## 3. Minimal Policy Role
The role of `Policy` here is:
- take the current `Energy` judgment and convert it into a narrow action rule
- freeze the smallest state vocabulary needed for later `Dynamics`
- freeze the smallest comparison target needed for later `Policy-Verification`

Operationally, this policy is about:
- when to commit
- when to defer
- when to issue one narrow downstream check
- what must remain unresolved rather than prematurely collapsed

## 4. Frozen State Vocabulary
Use the following state terms only.

1. `active_objective`
- the currently chosen working direction for the next useful assistant move

2. `suspended_objective`
- a previously active direction that is intentionally not advanced for now

3. `unresolved_relation`
- a relation whose exact ordering, interpretation, or binding still matters for the next step and has not yet been fixed by the user

4. `accepted_direction`
- the direction explicitly selected by the user or accepted by the user after a revisable recommendation

5. `quarantine`
- the rule that the `suspended_objective` must not re-enter content planning unless release conditions are met

6. `narrow_downstream_check`
- one local clarification that is allowed only when the next useful move depends on an `unresolved_relation`

## 5. Frozen Action Set
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
  - the accepted direction is explicitly parked/completed and the user asks to return
- required boundary:
  - release must be user-triggered or task-state-triggered, not assistant-assumed

## 6. Condition Rules
### 6.1 Pre-acceptance rule
If priority is unresolved and no direction has been accepted:
- default to `defer_with_resolution`
- do not commit to content on either side
- do not fix ordering on the user's behalf

### 6.2 Post-acceptance rule
If one direction is accepted:
- default to `commit_to_accepted_direction`
- mark the previous main line as `suspended_objective` when applicable
- enforce `quarantine`

### 6.3 Unresolved-relation rule
If the accepted direction contains an `unresolved_relation`:
- prefer `commit_with_relation_preservation`
- escalate to `narrow_downstream_check` only when the next useful step truly depends on that relation
- never convert the unresolved relation into a silent assistant-side commitment

### 6.4 Later-horizon rule
Across later checkpoints:
- preserving `quarantine` is necessary but not sufficient
- the first shared watch point is premature commitment on `unresolved_relation`
- therefore later-horizon stability should be read first through relation handling, not only through suspended-main reactivation

## 7. Failure Boundary
Treat the following as policy failures.

### 7.1 Over-commit failures
- unilateral direction choice before user acceptance
- content work before direction acceptance
- premature commitment on unresolved ordering or interpretation
- reactivating the suspended objective without a release condition

### 7.2 Over-defer failures
- repeated starter-style questioning after the direction is already accepted
- generic acknowledgment without useful progress on the accepted direction
- using clarification as a delay tactic when no local relation actually blocks the next step

## 8. What Current Evidence Supports
Current branch evidence supports freezing this policy shape because:
- non-unilateral priority resolution is reproducible on the tested provider pair
- preacceptance burden removal is a real shared downstream gain
- first-step side-topic commitment after explicit side-first acceptance is reproducible
- later-horizon degradation is measured and is more honestly explained by unresolved-relation collapse than by simple suspended-main reactivation

## 9. What This Candidate Does Not Yet Freeze
This memo does not yet freeze:
- provider / family / metric selection for `Policy-Verification`
- mechanism language beyond what `Dynamics` needs for its first skeleton
- any `Guarantee` thresholds or bounded claims
- any claim that this policy is already validated prospectively against baseline

## 10. Immediate Next Attachments
This candidate is intended to feed three next artifacts:

1. `Dynamics` mechanism skeleton
- describe how `active_objective`, `suspended_objective`, `quarantine`, and `unresolved_relation` hold or collapse over later turns

2. `Guarantee` claim schema
- specify which provider / family / horizon / observability conditions could support a bounded claim later

3. `Policy-Verification` pilot design
- define a fixed paired comparison for `baseline vs Energy policy` under selected conditions

## 11. Review Question
Is this minimal policy spec narrow and executable enough that:
- `Dynamics` can describe it without redesigning it
- `Policy-Verification` can test it without silently widening it
- later `Guarantee` language can stay bounded to explicit conditions

## Primary References
- `energy_priority_resolution_protocol_freeze_decision_memo_v1_2026-03-16.md`
- `energy_priority_resolution_branch_synthesis_memo_v2_2026-03-17.md`
- `energy_priority_resolution_horizon_stability_family_synthesis_memo_v1_2026-03-17.md`
- `energy_forward_validation_protocol_v11_2026-03-14.md`
