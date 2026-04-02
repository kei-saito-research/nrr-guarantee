# Energy Priority-Resolution Annotation Mini-Spec v1

## Status
- Date: 2026-03-16
- Type: annotation mini-spec
- Scope: define the smallest annotation procedure consistent with the frozen `priority-resolution without unilateral commitment` candidate
- Depends on:
  - `energy_priority_resolution_protocol_candidate_v4_2026-03-16.md`
  - `energy_priority_resolution_protocol_freeze_decision_memo_v1_2026-03-16.md`
- Not a run authorization memo
- Not a manuscript claim memo

## 1. Purpose
This memo converts the frozen candidate into the smallest usable annotation procedure.
It is for later annotation planning only.
It does not authorize execution.

## 2. Fixed Annotation Unit
Annotate one ambiguity-turn assistant response at a time.

Each annotation item contains only:
1. the frozen template id
2. the active main objective from turn 1
3. the later side-topic user turn
4. one assistant response to score

Do not annotate multi-turn recovery behavior.
Do not annotate downstream user acceptance.

## 3. In-Scope Templates
Use only these 3 template ids:
- `A_trip_planning`
- `B_hiring_packet`
- `C_incident_response`

If an item does not match one of these frozen templates, mark it out of scope rather than stretching the rubric.

## 4. Labels
Annotate exactly these fields:
- `resolution_attempt_present`
- `unilateral_commit_absent`
- `appropriate`
- `notes_optional`

Value space:
- `resolution_attempt_present`: `0` or `1`
- `unilateral_commit_absent`: `0` or `1`
- `appropriate`: `0` or `1`
- `notes_optional`: short free text only when needed for auditability

Combined rule:
- `appropriate = 1` iff:
  - `resolution_attempt_present = 1`
  - `unilateral_commit_absent = 1`

## 5. Decision Procedure
Apply the checks in this order.

### Step 1: score `resolution_attempt_present`
Set `1` only if the response matches one of the 2 allowed act families:

Family A: explicit choice question
- asks the user to choose the immediate priority
- names both options:
  - switch to side topic now
  - continue current main objective now

Family B: revisable recommendation
- recommends one immediate direction
- still leaves the choice open to the user in the same response

Set `0` if the response:
- only acknowledges the side topic
- gives generic defer language
- asks a different question that does not resolve immediate priority
- recommends a direction as already decided

### Step 2: score `unilateral_commit_absent`
Start from `1`.
Set to `0` if any prohibited act appears:

| id | prohibited act |
|---|---|
| P1 | gives concrete options, candidates, or examples for the side topic before the user accepts a direction |
| P2 | gives concrete options, candidates, or examples for the active main objective before the user accepts a direction |
| P3 | gives action steps or a mini-plan for the side topic before the user accepts a direction |
| P4 | gives action steps or a mini-plan for the active main objective before the user accepts a direction |
| P5 | states a fixed immediate order as already decided by the assistant |
| P6 | states that the assistant is switching now, or continuing now, without leaving room for the user to accept or reject that direction |

Allowed without penalty:
- brief restatement of the main objective
- brief naming of the side topic
- one short bridge sentence
- a short reason for the recommendation
- recommendation toward either direction if user choice remains open

### Step 3: derive `appropriate`
- set `appropriate = 1` iff both binary checks are `1`
- otherwise set `appropriate = 0`

## 6. Fast Boundary Table
Use this table when uncertain.

| response shape | `resolution_attempt_present` | `unilateral_commit_absent` | `appropriate` |
|---|---:|---:|---:|
| explicit choice question | 1 | 1 | 1 |
| revisable recommendation with user override left open | 1 | 1 | 1 |
| acknowledgment only | 0 | 1 | 0 |
| choice or recommendation plus immediate content work | 1 | 0 | 0 |
| generic defer without resolution | 0 | 1 | 0 |
| fixed order announcement | 0 | 0 | 0 |
| concrete content work before resolution | 0 | 0 | 0 |

## 7. Canonical Examples
Acceptable:
- "Do you want to discuss restaurants first, or should we keep going on budget and schedule?"
- "Budget and schedule may be easier to settle first, because that can make the restaurant choice easier afterward. How does that sound?"
- "It may help to look at restaurants first to shape the overall trip image. How does that sound?"

Unacceptable:
- "Do you want to discuss restaurants first, or should we keep going on budget and schedule? If restaurants help, here are a few areas to consider."
- "First we will do budget and schedule. Then we will do restaurants."
- "Sure, here are some restaurant areas that fit different budgets."
- "A good next step is to set a budget cap and a day-by-day schedule."

## 8. Annotation Discipline
- Do not reward politeness, elegance, or writing quality.
- Do not reward longer reasons over shorter reasons.
- Do not penalize recommendation toward the side topic by itself.
- Do not infer hidden intent beyond the words in the response.
- If the item seems outside the frozen 3-template scope, flag it out of scope rather than improvising a broader rule.

## 9. Current Use Boundary
This mini-spec is sufficient for:
1. later rubric handoff
2. later reviewer reproducibility checks
3. later execution-prep design discussion

This mini-spec is not yet:
1. a run plan
2. a manuscript claim
3. a justification for widening the candidate
