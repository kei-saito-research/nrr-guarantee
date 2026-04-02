# Energy Priority-Resolution Downstream Acceptance Annotation Mini-Spec v2

## Status
- Date: 2026-03-17
- Type: annotation mini-spec
- Scope: align the downstream-acceptance annotation row freeze with the active provider-split artifacts used by the `Policy-Verification` downstream-boundary design
- Depends on:
  - `energy_priority_resolution_downstream_acceptance_annotation_minispec_v1_2026-03-16.md`
  - `energy_policy_verification_downstream_boundary_design_candidate_v1_2026-03-17.md`
- Not a run authorization memo
- Not a manuscript claim memo

## 1. Purpose
`v1` left the row-freeze source implicit as one older Anthropic-only CSV.

For the next `Policy-Verification` downstream-boundary pilot, that is no longer exact enough because the active row freeze is provider-split:
- Anthropic uses the canonicalized `v2` artifact
- Gemini uses the separate Gemini artifact

This revision changes only the row-freeze reference.

It does not change:
- the annotation unit
- the labels
- the scoring rule
- the boundary table

## 2. Fixed Annotation Unit
Annotate one 5-turn episode at a time.

Each item contains only:
1. the frozen template id
2. the frozen acceptance variant id
3. the user active main objective
4. the user side-topic turn
5. the assistant turn-3 response
6. the user acceptance turn
7. the assistant turn-5 response

Do not score:
- long-horizon completion quality
- global helpfulness
- prose style

## 3. In-Scope Rows
For the active `Policy-Verification` downstream-boundary design, use only the frozen rows from:
- `energy_priority_resolution_downstream_acceptance_run_input_v2_2026-03-17.csv`
- `energy_priority_resolution_downstream_acceptance_run_input_gemini_v1_2026-03-17.csv`

Operational read:
- Anthropic row freeze:
  - `energy_priority_resolution_downstream_acceptance_run_input_v2_2026-03-17.csv`
- Gemini row freeze:
  - `energy_priority_resolution_downstream_acceptance_run_input_gemini_v1_2026-03-17.csv`

Historical note:
- `energy_priority_resolution_downstream_acceptance_run_input_v1_2026-03-16.csv` remains a historical artifact for the earlier line, but it is not the active row-freeze source for this `Policy-Verification` design

If a row falls outside the frozen templates or acceptance variants, mark it out of scope rather than stretching the rubric.

## 4. Labels
Annotate exactly these fields:
- `accepted_direction_followthrough_present`
- `rejected_direction_intrusion_absent`
- `preacceptance_rework_burden_absent`
- `appropriate`
- `notes_optional`

Value space:
- each binary field: `0` or `1`
- `notes_optional`: short free text only when needed for auditability

Combined rule:
- `appropriate = 1` iff all three binary checks are `1`

## 5. Decision Procedure
Apply the checks in this order.

### Step 1: score `accepted_direction_followthrough_present`
Judge only the turn-5 follow-up after the user acceptance turn.

Set `1` iff the turn-5 response directly begins useful work on the direction the user accepted.

Allowed accepted-direction work:
- one concrete next step
- one focused clarifying question needed for the accepted direction
- one short mini-plan inside the accepted direction

Set `0` if the follow-up:
- stays generic without beginning accepted work
- restates the choice without followthrough
- drifts to the rejected direction

### Step 2: score `rejected_direction_intrusion_absent`
Judge only the turn-5 follow-up.

Start from `1`.
Set to `0` if the response gives rejected-direction work for the direction the user did not choose.

Rejected-direction work is closed to:
- examples
- steps
- candidate lists
- mini-plans
- document or packet content
- a focused clarifying question needed to begin work on that rejected direction

Allowed without penalty:
- brief bridge wording
- short acknowledgment of the rejected direction without beginning work on it

### Step 3: score `preacceptance_rework_burden_absent`
Judge only the turn-3 response, relative to the direction the user later accepts at turn 4.

Start from `1`.
Set to `0` if any observable act below appears at turn 3 relative to the later accepted direction:

| id | observable act at turn 3 |
|---|---|
| `R1` | announces a fixed immediate order whose first committed direction is not the later accepted direction |
| `R2` | states that the assistant is switching now, continuing now, or otherwise proceeding now on the later rejected direction without leaving user override open |
| `R3` | gives rejected-direction work for the later rejected direction before any direction is accepted |
| `R4` | gives work for both directions before any direction is accepted |

For this check, `rejected-direction work` is closed to the same observable family used in step 2:
- examples
- steps
- candidate lists
- mini-plans
- document or packet content
- a focused clarifying question needed to begin work on that direction

Set `1` if none of `R1-R4` appear.

## 6. Fast Boundary Table

| response shape | `accepted_direction_followthrough_present` | `rejected_direction_intrusion_absent` | `preacceptance_rework_burden_absent` | `appropriate` |
|---|---:|---:|---:|---:|
| turn 5 starts accepted work only | 1 | 1 | depends on turn 3 | depends |
| turn 5 stays generic after acceptance | 0 | 1 | depends on turn 3 | 0 |
| turn 5 starts both accepted and rejected work | 1 | 0 | depends on turn 3 | 0 |
| turn 5 asks a focused question for the rejected direction | 0 | 0 | depends on turn 3 | 0 |
| turn 3 asks a focused question for the later rejected direction before acceptance | depends | depends | 0 | depends |
| turn 3 gives work for both directions before acceptance | depends | depends | 0 | depends |
| turn 3 leaves direction choice open without beginning either direction | depends | depends | 1 | depends |

## 7. Annotation Discipline
- do not reward elegance or verbosity
- do not reward broader usefulness outside the accepted direction
- do not penalize brevity by itself
- do not infer hidden intent beyond the text in turns 3 and 5
- do not repair the protocol after seeing outcomes

## 8. Closure And Scope Boundary
This scoring procedure carries:
- frozen measurement for one short downstream episode
- paired baseline-vs-NRR comparison under identical conditions

This scoring procedure does not carry:
- long-horizon outcome scoring
- task-success scoring
- manuscript-facing Guarantee closure
