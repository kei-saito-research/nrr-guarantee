# Policy-Verification Pilot Protocol Current v1

## Status
- Date: 2026-03-18
- Type: current canonical protocol memo
- Scope: define the current canonical `Policy-Verification` pilot protocol that follows the closed `Energy -> Policy` handoff, without reopening completed `Energy` pilots or widening into `Guarantee`
- Depends on:
  - `policy_minimal_spec_current_v1_2026-03-18.md`
  - `energy_dynamics_mechanism_skeleton_candidate_v2_2026-03-17.md`
  - `energy_guarantee_claim_schema_candidate_v2_2026-03-17.md`
  - `energy_to_policy_handoff_memo_v1_2026-03-18.md`
  - `energy_priority_resolution_package_map_v1_2026-03-18.md`
  - `energy_policy_verification_pilot_design_candidate_v2_2026-03-17.md`
  - `energy_policy_verification_downstream_boundary_design_candidate_v2_2026-03-17.md`
  - `energy_policy_verification_side_topic_quarantine_design_candidate_v1_2026-03-17.md`
- Not a run-authorization memo
- Not a manuscript claim memo

## 1. Assistant-Side Decision
- judgment:
  - `adopt`
- reason:
  - the closed `Energy` handoff, current `Policy` spec, `Dynamics v2`, and `Guarantee schema v2` together are now sufficient to fix a reusable downstream pilot protocol without silently reusing `Energy` as the owner of forward validation

## 2. Role Of Policy-Verification
`Policy-Verification` owns prospective `baseline vs Energy policy` validation under selected conditions.

This protocol exists to do four things only:
- freeze the order in which a pilot is specified
- keep each pilot aligned to the current `Policy`, `Dynamics`, and `Guarantee` constraints
- force matched-condition comparison and explicit boundary reporting
- prevent scope drift from one narrow pilot into a broad conversation-policy claim

This protocol does not:
- reopen completed `Energy` pilots
- redesign `Policy`
- write `Guarantee` language directly
- authorize execution by itself

## 3. Fixed Upstream Constraints
Every downstream pilot must inherit the following fixed upstream constraints.

### 3.1 Policy constraint
Use the current `Policy` object as fixed:
- `active_objective`
- `suspended_objective`
- `accepted_direction`
- `unresolved_relation`
- `quarantine`
- `local_relation_block`

Use only the frozen action vocabulary:
- `defer_with_resolution`
- `commit_to_accepted_direction`
- `commit_with_relation_preservation`
- `narrow_downstream_check`
- `release_quarantine`

### 3.2 Dynamics constraint
Use `Dynamics v2` as the mechanism vocabulary only.

When relevant, pilot observability should be able to speak to:
- `Stable Resolution`
- `Clean Quarantine Hold`
- `Useful Continuation Hold`
- `Relation-Preservation Hold`
- `Premature Relation Collapse`
- `Repeated-Starter Attractor`
- `Generic Stall`
- `Quarantine Leak`

The pilot may measure a subset only.
It may not silently redefine these motifs.

### 3.3 Guarantee constraint
Before any pilot design is frozen, the targeted later claim unit must already be narrowed to one explicit fill for:
1. `provider_scope`
2. `family_scope`
3. `horizon_scope`
4. `observability_scope`
5. `comparison_scope`
6. `supported_behavior`
7. `explicit_failure_boundary`
8. `unsupported_extension`

No pilot may design its claim surface after outcome inspection.

## 4. Canonical Freeze Order
Every new `Policy-Verification` pilot should follow this order.

1. scope freeze
- choose one family only
- choose one horizon band only
- choose one comparison surface only
- fill the target guarantee fields before writing exact design details

2. exact design freeze
- freeze provider / model / temperature / reps
- freeze exact input artifact names
- freeze arm-specific prompt surfaces
- freeze annotation / scoring fields
- freeze reporting tables and failure-boundary reporting rule

3. run authorization
- authorize execution only after the scope and design are already frozen
- limit the run-authorization memo to runtime stop rules, artifact contract, and provenance checks

4. readout
- report gains, regressions, and explicit non-effective regions together
- keep provider slices explicit before any pooled summary

## 5. Canonical Narrowness Rules
Each pilot must remain narrow in the following sense.

### 5.1 One family at a time
Allowed:
- one named branch family or one named subfamily

Not allowed:
- bundling ambiguity-turn, downstream acceptance, first-step side-topic, and later-horizon into one pilot claim

### 5.2 One horizon band at a time
Allowed:
- early decision boundary
- downstream acceptance boundary
- first-step side-topic workstart
- one later checkpoint band

Not allowed:
- “later followthrough in general”
- “long-horizon stability in general”

### 5.3 One comparison surface at a time
Mainline default:
- baseline vs Energy policy

Boundary:
- local operator comparisons may remain supporting lines only
- they must not silently replace the mainline comparison surface

### 5.4 Pilot-scale is sufficient
The protocol does not require large-scale execution.
Pilot-scale is acceptable if:
- the selected conditions are fixed in advance
- the run table is matched across arms
- the claim stays bounded to those selected conditions

## 6. Matched-Condition Rules
Within one paired comparison, everything except the intended arm surface must match.

Freeze as applicable:
- provider
- model
- temperature
- reps
- exact input rows
- annotation procedure
- reporting rule

Do not change these after inspecting outcomes for that paired comparison.

## 7. Observability Rules
Use only directly scored or directly logged fields.

Allowed observability families include:
- direction resolution without unilateral commitment
- preacceptance burden present / absent
- chosen-side progress
- user-detail use
- unresolved-relation preservation or narrow check
- suspended-main reference absent
- repeated-starter absence

Not allowed:
- hidden intention
- unlogged reasoning quality
- broad user satisfaction
- end-task success outside the frozen observability surface

## 8. Reporting Rules
Every pilot readout must:
- show provider slices before pooled totals
- report gains and regressions together
- make explicit what remained ineffective or conditional
- keep failure-boundary reporting in the main result set, not appendix-only

When template-level structure matters, show:
- per-template counts within provider
- pooled totals only after those slices are visible

## 9. Drift-Prohibition Rules
Do not:
- reopen closed `Energy` work because a downstream pilot remains to be run
- widen from one family to multiple families inside the same pilot artifact
- change claim-field values after reading outcomes
- swap model strings, prompt paths, or input artifacts silently
- collapse provider divergence into a pooled-only headline
- write `Guarantee`-style language from a pilot that has not fixed its claim unit in advance

## 10. Immediate Next Artifacts Under This Protocol
Each new pilot line should produce, in order:
1. one scope-freeze memo
2. one exact-design memo
3. one run-authorization memo
4. one readout memo with explicit failure-boundary reporting

## 11. Current Canonical Use Rule
If someone asks how to start the next downstream `Policy-Verification` pilot, start from this protocol.

Operational rule:
- read this file after the current `Policy` minimal spec
- choose one narrow family / horizon / observability target
- freeze the claim unit before freezing the exact design
- keep `Energy` closed unless a genuinely new `Energy`-owned contradiction appears
