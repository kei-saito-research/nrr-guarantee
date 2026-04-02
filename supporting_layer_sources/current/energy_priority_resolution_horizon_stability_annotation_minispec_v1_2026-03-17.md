# Energy Priority-Resolution Horizon Stability Annotation Mini-Spec v1

## Status
- Date: 2026-03-17
- Type: annotation mini-spec
- Scope: define the smallest usable scoring procedure for the first `priority-resolution horizon stability` protocol candidate
- Depends on:
  - `energy_priority_resolution_horizon_stability_protocol_candidate_v1_2026-03-17.md`
- Not a run authorization memo
- Not a manuscript claim memo

## 1. Purpose
This memo converts the horizon-stability candidate into the smallest reviewable scoring procedure.

It is sufficient for:
1. assistant-side checkpoint scoring
2. later reviewer reproducibility checks
3. keeping the family narrow before exact rows are frozen

It does not authorize execution.

## 2. Fixed Annotation Unit
Annotate one scored assistant checkpoint at a time.

Each item should contain only:
1. the frozen template id
2. the checkpoint id
   - `turn7`
   - `turn9`
   - `turn11`
3. the original main objective
4. the chosen side-topic line so far
5. the most recent user detail available before the scored checkpoint
6. the scored assistant reply

Do not score:
- overall conversation quality
- final travel-plan quality
- prose elegance

## 3. Labels
Annotate exactly these fields:
- `chosen_side_direction_progress_present`
- `user_detail_use_present`
- `unresolved_relation_preserved_or_narrowly_checked`
- `suspended_main_reference_absent`
- `starter_question_repeat_absent`
- `appropriate`
- `notes_optional`

Value space:
- each binary field: `0` or `1`
- `notes_optional`: short free text only when needed for auditability

Combined rule:
- `appropriate = 1` iff all five binary checks are `1`

## 4. Decision Procedure
Apply the checks in this order.

### Step 1: score `chosen_side_direction_progress_present`
Set `1` iff the reply makes useful progress on the chosen side topic.

Set `0` if the reply:
- returns to the suspended original main objective
- only acknowledges and stops
- asks a generic non-advancing question

### Step 2: score `user_detail_use_present`
Set `1` iff the reply uses the user detail already supplied for the active side-topic line.

For the restaurant example:
- visible use of `fish` or `ramen` counts
- generic restaurant talk without using the supplied detail does not

### Step 3: score `unresolved_relation_preserved_or_narrowly_checked`
Set `1` iff the reply either:
- keeps ambiguous relations unresolved while still progressing, or
- asks one narrow clarifying question exactly where the ambiguity matters

Set `0` if the reply prematurely fixes the meaning without support from the user.

### Step 4: score `suspended_main_reference_absent`
Start from `1`.
Set to `0` if the reply reactivates the suspended original main objective.

For the travel example, this includes:
- budget
- schedule

### Step 5: score `starter_question_repeat_absent`
Start from `1`.
Set to `0` if the reply repeats an earlier already-answered starter question instead of using the answer already given.

At later checkpoints, apply the same rule to earlier already-answered follow-up questions as well.

Operational reading:
- if turn 7 asked a narrowing question and turn 8 answered it,
- then turn 9 should not simply repeat that same now-answered question
- the same rule applies again from turn 9 to turn 11

## 5. Fast Boundary Table

| response shape | progress | detail use | unresolved relation | suspended-main absent | no repeated starter | appropriate |
|---|---:|---:|---:|---:|---:|---:|
| advances restaurant search using fish/ramen and asks one narrow clarification | 1 | 1 | 1 | 1 | 1 | 1 |
| only says "fish and ramen sound great" and stops | 0 | 1 | 1 | 1 | 1 | 0 |
| asks again what cuisine the user wants | 0 | 0 | 1 | 1 | 0 | 0 |
| returns to budget/schedule | 0 | depends | depends | 0 | 1 | 0 |
| assumes `fish ramen` without support and continues on that basis | 1 | 1 | 0 | 1 | 1 | 0 |

## 6. Annotation Discipline
- do not reward verbosity by itself
- do not reward strong decisiveness when that decisiveness collapses unresolved meaning
- do not penalize one narrow clarifying question if it is needed to preserve the ambiguity boundary
- do not infer hidden intent beyond the visible text
- do not redesign the family after seeing outcomes

## 7. Scope Boundary
This scoring procedure carries:
- bounded checkpoint scoring for a horizon-stability family
- a way to measure whether prompt-layer control still holds across multiple later assistant turns

This scoring procedure does not carry:
- exact row freeze
- execution approval
- manuscript-facing claims
