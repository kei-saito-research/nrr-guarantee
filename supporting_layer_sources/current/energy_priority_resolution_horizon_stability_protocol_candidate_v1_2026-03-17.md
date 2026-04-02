# Energy Priority-Resolution Horizon Stability Protocol Candidate v1

## Status
- Date: 2026-03-17
- Type: protocol candidate memo
- Scope: define the first candidate protocol for the `priority-resolution horizon stability` family after user-side clarification of what counts as sustained good behavior
- Depends on:
  - `energy_priority_resolution_horizon_stability_hypothesis_memo_v1_2026-03-17.md`
  - `energy_priority_resolution_side_topic_commitment_operator_two_provider_read_memo_v1_2026-03-17.md`
  - `energy_priority_resolution_side_topic_followthrough_family_synthesis_memo_v1_2026-03-17.md`
- Not a run authorization memo
- Not a manuscript claim memo

## 1. Purpose
This candidate turns the new `horizon stability` family into a reviewable experimental shape.

The goal is not to invent another rescue prompt.

The goal is to measure how many later assistant steps remain stable once the already-supported first side-topic switch has been achieved.

## 2. What Part Of Closure This Family Could Carry
This family would carry only a narrow closure segment:
1. quality measurement
   - bounded multi-step stability of the chosen side-topic line after a successful first switch
2. operational control
   - same initial side-first acceptance surface, same fixed first-step operator start, same later user-reply scaffolds, same provider/model/temp within each paired run
3. verification
   - preserve raw output, response CSV, summary JSON, annotation CSV, and comparison memos per provider and per checkpoint

This family would not carry:
- new first-step operator claims
- broad provider universality
- final task-outcome closure
- manuscript-facing Guarantee closure

## 3. Fixed Family Boundary
Keep the family measurement-first.

Do not vary initially:
- the already-supported first-step side-topic commitment operator
- the high-level side-first surface family
- the structural scoring style

Do not begin with:
- a new rescue arm
- an external-state-memory condition
- a new confusion-decomposition intervention

## 4. Plain-Language User Judgment To Preserve
The user-side desired behavior is:
- continue the chosen side topic rather than returning to the original main objective
- use the newly supplied user detail
- do not silently collapse unresolved meaning into one overcommitted interpretation

Concrete example under the trip-planning template:
- original main objective:
  - travel budget and schedule
- chosen side topic:
  - restaurant search
- user detail:
  - "fish and ramen"

Good continuation means:
- restaurant search continues
- the reply uses `fish` and `ramen`
- but the assistant does not prematurely decide between:
  - fish-ramen as one dish
  - fish and ramen on different meals
  - fish first and ramen later
- if that relation matters, the assistant may ask one narrow clarifying question rather than collapsing the ambiguity

## 5. Candidate Episode Family
Use one horizon family only:
- `priority_resolution_side_topic_horizon_stability`

Base episode prefix stays fixed:
1. user states original main objective
2. user introduces the plausible side topic
3. assistant gives clean two-way handoff
4. user explicitly selects the side topic first
5. assistant gives the already-supported explicit side-topic workstart
6. user gives one concrete side-topic answer

New horizon extension:
7. assistant continuation checkpoint 1
8. user follow-up reply
9. assistant continuation checkpoint 2
10. user follow-up reply
11. assistant continuation checkpoint 3

Initial checkpoint set:
- turn 7
- turn 9
- turn 11

## 6. Initial Observation Horizon
The first candidate family should not stop at one later assistant reply only.

Why:
- one reply can look locally fine and still collapse immediately after
- the user-side judgment is that stability should mean more than one isolated good-looking turn

Therefore the initial candidate horizon is:
- three later assistant replies after the first side-topic workstart
- operationally: score turns `7`, `9`, and `11`

## 7. Candidate Metric Family
Use one metric family only:
- `side_topic_horizon_stability_step_v1`

At each scored assistant checkpoint, annotate:
1. `chosen_side_direction_progress_present`
2. `user_detail_use_present`
3. `unresolved_relation_preserved_or_narrowly_checked`
4. `suspended_main_reference_absent`
5. `starter_question_repeat_absent`
6. `appropriate`

Combined rule:
- `appropriate = 1` iff all five binary checks are `1`

## 8. Intended Meaning Of The Checks
### 8.1 `chosen_side_direction_progress_present`
Set `1` iff the reply makes useful progress on the chosen side topic rather than merely acknowledging it.

Allowed progress forms:
- one concrete next step
- one short mini-plan
- one narrowing question that advances the active side-topic task

Set `0` if the reply:
- returns to the original main objective
- stalls at acknowledgment only
- asks a generic non-advancing question

### 8.2 `user_detail_use_present`
Set `1` iff the reply uses the user detail already given in the current active side-topic exchange.

For the restaurant example:
- using `fish` and `ramen` counts
- ignoring them and speaking only generically does not

### 8.3 `unresolved_relation_preserved_or_narrowly_checked`
Set `1` iff the reply either:
- keeps unresolved relations unresolved while still advancing, or
- asks one narrow clarifying question exactly where the unresolved relation matters

Set `0` if the reply prematurely collapses the meaning without support.

Examples of premature collapse:
- treating `fish and ramen` as `fish ramen`
- treating it as `fish dinner plus ramen later`
- treating it as one fixed itinerary order

without the user having said so

### 8.4 `suspended_main_reference_absent`
Start from `1`.
Set to `0` if the reply reactivates the suspended original main objective inside the active side-topic continuation.

For the trip example, this includes:
- budget
- schedule

### 8.5 `starter_question_repeat_absent`
Start from `1`.
Set to `0` if the reply repeats an earlier already-answered starter question instead of using the answer already on the table.

For the restaurant example:
- repeating "what kind of cuisine do you want?" after the user already answered counts as failure

## 9. Candidate Comparison Shape
The first candidate family is not yet a new intervention comparison.

Instead, compare stability across:
1. provider
   - `gemini`
   - `anthropic`
2. checkpoint depth
   - turn 7
   - turn 9
   - turn 11

Within a given provider run, keep fixed:
- provider/model/temp
- same fixed initial side-first switch surface
- same first-step side-topic commitment operator at turn 5
- same checkpoint scaffolds and later user replies

## 10. Why This Candidate Is Narrow Enough
1. it does not reopen the closed turn-7 rescue ladder
2. it keeps the already-supported first-step operator fixed rather than redesigning it
3. it changes the question from `which wording rescues turn 7?` to `how far does the achieved control actually hold?`
4. it yields bounded outputs even if the answer is negative

## 11. What This Candidate Would Answer
This candidate would answer:
- whether the side-topic line holds for one, two, or three later assistant turns
- where the first repeatable degradation appears
- whether the observed degradation is similar or different across the tested provider pair

## 12. What This Candidate Would Not Answer
This candidate would not answer:
- final task success
- unrestricted long-horizon success
- whether an external-state architecture would fix the issue
- whether a new prompt rescue should be preferred before measuring the horizon itself

## 13. Current Boundary
- this candidate does not authorize a run
- this candidate does not yet freeze exact turn-8 and turn-10 user follow-up rows
- this candidate records only the first reviewable protocol shape for the new family

## 14. Next Practical Step
If `Energy` returns from package work to experiments:
1. freeze one small set of turn-8 and turn-10 user follow-up replies per template
2. convert this metric family into an annotation mini-spec
3. send the candidate for narrow external review before any run
