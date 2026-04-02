# Energy Dynamics Mechanism Skeleton Candidate v2

## Status
- Date: 2026-03-17
- Type: dynamics skeleton memo
- Scope: define the first `Dynamics` mechanism skeleton that follows the current `Policy` minimal spec without redesigning it
- Depends on:
  - `energy_dynamics_mechanism_skeleton_candidate_v1_2026-03-17.md`
  - `energy_policy_minimal_spec_candidate_v2_2026-03-17.md`
  - `energy_priority_resolution_branch_synthesis_memo_v2_2026-03-17.md`
  - `energy_priority_resolution_side_topic_followthrough_family_synthesis_memo_v1_2026-03-17.md`
  - `energy_priority_resolution_horizon_stability_two_provider_read_memo_v1_2026-03-17.md`
  - `energy_priority_resolution_horizon_stability_annotation_minispec_v1_2026-03-17.md`
- Not a run authorization memo
- Not a manuscript claim memo

## 1. Purpose
This memo gives `Dynamics` only the smallest mechanism skeleton needed for the current post-`Energy` line.

It is meant to do three things:
1. describe how the policy-frozen state vocabulary evolves over later turns
2. identify where the currently measured branch tends to hold or break
3. give `Policy-Verification` a mechanism vocabulary to check against when later metrics are frozen

It is not allowed to:
- redesign `Policy`
- choose `Policy-Verification` provider / family / metric settings
- state bounded claims for `Guarantee`

## 2. Assistant-Side Read
- judgment:
  - `adopt`
- reason:
  - the current `priority-resolution` branch now has enough early-control, second-step, and later-horizon evidence to support a narrow hold/break vocabulary without pretending that one universal dynamic law has been established

## 3. Fixed Boundary
`Dynamics` here means:
- time-ordered description of the policy-frozen state terms
- not policy invention
- not intervention design
- not guarantee language

Operational rule:
- if a later dynamics note changes the meaning of `active_objective`, `suspended_objective`, `unresolved_relation`, `quarantine`, or `local_relation_block`, that note is out of scope and must return to `Policy`

## 4. Frozen Input Vocabulary From Policy
Carry forward these terms exactly as frozen in `Policy v2`:
- `active_objective`
- `suspended_objective`
- `accepted_direction`
- `unresolved_relation`
- `quarantine`
- `local_relation_block`

Carry forward these action labels only as observed transitions:
- `defer_with_resolution`
- `commit_to_accepted_direction`
- `commit_with_relation_preservation`
- `narrow_downstream_check`
- `release_quarantine`

## 5. Time Axis For The Current Skeleton
Use the following qualitative stages only.

1. `resolution_boundary`
- before a direction is accepted

2. `first_commit_step`
- the first assistant move after `accepted_direction`

3. `second_step_followthrough`
- the next assistant continuation after a clean first commit

4. `later_horizon_checkpoint`
- later measured checkpoints such as `turn7`, `turn9`, `turn11`

This skeleton does not define a continuous-time model.
It defines a staged transition read for the current measured branch.

## 6. Core Mechanism Motifs
Use the following motifs only.

### 6.1 Stable Resolution
- shape:
  - `defer_with_resolution -> accepted_direction -> active_objective`
- read:
  - ambiguity is resolved without unilateral commitment
- current evidence:
  - supported as a reproducible two-provider early-control result

### 6.2 Clean Quarantine Hold
- shape:
  - `accepted_direction` becomes `active_objective`
  - prior line becomes `suspended_objective`
  - `quarantine` remains intact across the next useful move
- read:
  - the earlier main line stays inactive while side-topic work begins
- current evidence:
  - supported at first side-topic workstart
  - remains strong across later checkpoints in the current horizon family

### 6.3 Useful Continuation Hold
- shape:
  - accepted side direction continues
  - user detail is used
  - no repeated starter question appears
- read:
  - the branch continues to make useful progress without reopening the earlier boundary
- current evidence:
  - mixed beyond the first side-topic workstart
  - weaker at one-turn-later followthrough than at first-step commitment

### 6.4 Relation-Preservation Hold
- shape:
  - side-topic progress continues
  - an `unresolved_relation` remains open, or one narrow local check is used exactly where needed
- read:
  - the branch keeps moving without silently collapsing unresolved meaning
  - `local_relation_block` is the state in which an `unresolved_relation` is still active and the immediate next useful move cannot be produced without deciding it
- current evidence:
  - this is the key later-horizon stress point
  - it weakens before `quarantine` itself breaks

### 6.5 Premature Relation Collapse
- shape:
  - the assistant commits an ordering / interpretation / binding before user support
- read:
  - later-horizon break through unresolved-relation collapse
- current evidence:
  - shared failure mode across providers
  - cleanest shared surface appears in `C_incident_response` at `turn9`

### 6.6 Repeated-Starter Attractor
- shape:
  - the assistant re-asks an already-answered starter-style question instead of using the available answer
- read:
  - over-defer failure that blocks useful continuation without necessarily breaking quarantine
  - this is a side-topic-family local motif, not a core shared later-horizon motif
- current evidence:
  - visible in side-topic followthrough lines
  - especially concrete on Anthropic in the narrow `A_trip_planning` answer-use residual

### 6.7 Generic Stall
- shape:
  - acknowledgment or generic continuation without useful progress
- read:
  - over-defer failure after a clean direction choice
- current evidence:
  - present in second-step followthrough boundaries
  - not the dominant explanation for every later failure

### 6.8 Quarantine Leak
- shape:
  - the suspended main line re-enters planning or content before release conditions
- read:
  - direct break of the active-vs-suspended boundary
- current evidence:
  - measured, but weaker than relation-collapse as the current shared later-horizon explanation

## 7. Transition Read By Stage
### 7.1 Resolution Boundary -> First Commit Step
Dominant successful transition:
- `defer_with_resolution -> accepted_direction -> commit_to_accepted_direction`

Current read:
- this stage is the strongest supported control region in the branch

### 7.2 First Commit Step -> Second-Step Followthrough
Dominant uncertainty:
- whether useful continuation remains specific and answer-using rather than generic or repeated-question driven

Current read:
- this stage is mixed and provider-sensitive
- it should not be collapsed into one universal rescue story

### 7.3 Second-Step Followthrough -> Later Horizon
Dominant risk order in the current branch aggregate read:
1. useful continuation weakens
2. unresolved relation collapses
3. quarantine may still remain intact

Current read:
- later-horizon degradation is better modeled as relation-handling failure under preserved quarantine than as immediate return to the suspended main line

## 8. Template / Provider Notes For The Current Skeleton
### 8.1 Shared read
- `quarantine` is strong across providers in the measured horizon family
- `unresolved_relation` collapse is shared enough to count as a real mechanism motif

### 8.2 Template dependence
- `C_incident_response` is the cleanest shared later-horizon failure surface
- `A_trip_planning` and `B_hiring_packet` differ in how long useful continuation holds before break

### 8.3 Provider dependence
- Anthropic and Gemini do not share one universal break depth
- Anthropic exposes a concrete repeated-starter attractor on the narrow `A` followthrough surface
- Gemini shows mixed second-step continuation and later-horizon degradation without making one single attractor sufficient for all misses

## 9. What This Skeleton Supports
This skeleton supports:
- a narrow description of where the current branch tends to hold
- a narrow description of where it tends to break
- a mechanism vocabulary for later `Policy-Verification` metric sanity checks

## 10. What This Skeleton Does Not Support
This skeleton does not support:
- one universal dynamic law across templates
- one provider-balanced degradation depth
- one guarantee-style condition statement
- redesign of the policy action set
- any claim that later-horizon stability is solved

## 11. Immediate Next Attachments
This skeleton should feed:

1. `Guarantee` claim schema
- use this hold/break vocabulary to state what later bounded claims may or may not say

2. `Policy-Verification` metric freeze
- check that the pilot metrics actually observe:
  - quarantine hold
  - useful continuation
  - unresolved-relation preservation or collapse
  - repeated-starter attractor where relevant

## 12. Review Question
Is this mechanism skeleton narrow and faithful enough that:
- it describes the current `Policy` without redesigning it
- it captures the measured hold/break motifs honestly
- it gives `Policy-Verification` a usable mechanism vocabulary without pre-choosing the pilot

## Primary References
- `energy_dynamics_mechanism_skeleton_candidate_v1_2026-03-17.md`
- `energy_policy_minimal_spec_candidate_v2_2026-03-17.md`
- `energy_priority_resolution_branch_synthesis_memo_v2_2026-03-17.md`
- `energy_priority_resolution_side_topic_followthrough_family_synthesis_memo_v1_2026-03-17.md`
- `energy_priority_resolution_horizon_stability_two_provider_read_memo_v1_2026-03-17.md`
- `energy_priority_resolution_horizon_stability_annotation_minispec_v1_2026-03-17.md`
