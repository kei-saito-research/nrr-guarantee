# Guarantee Policy/Dynamics Manuscript Integration v2

## Status
- Date: 2026-03-20
- Type: historical guarantee drafting memo
- Scope: preserved for chronology only after the current manuscript-facing
  policy/dynamics guidance moved to
  `guarantee_policy_dynamics_manuscript_integration_v3_2026-03-30.md`
- Depends on:
  - `supporting_layer_sources/current/policy_minimal_spec_current_v1_2026-03-18.md`
  - `supporting_layer_sources/current/energy_dynamics_mechanism_skeleton_candidate_v2_2026-03-17.md`
  - `supporting_layer_sources/current/non_evaluative_principle_dynamics_closure_note_v1_2026-03-19.md`
  - `manuscript/current/nrr-guarantee_manuscript_v20.tex`

## 1. Assistant-Side Decision
- judgment:
  - `adopt`
- reason:
  - the manuscript already has bounded claims and boundary text, but it is still
    too easy to read those claims as free-floating results unless the fixed
    `Policy` and `Dynamics` vocabulary is connected directly to the supported
    surfaces in the main text

## 2. Policy Vocabulary To Surface Mapping
The manuscript should make the following links explicit:

1. early ambiguity-turn surface
- main policy action:
  - `defer_with_resolution`
- protected boundary:
  - no unilateral direction choice before `accepted_direction`

2. downstream acceptance surface
- main policy action:
  - `commit_to_accepted_direction`
- protected boundary:
  - do not collapse a provider-sensitive mixed read into pair-wide downstream
    guarantee language

3. repaired first-step side-topic surface
- main policy state read:
  - accepted side direction becomes `active_objective`
  - prior main line becomes `suspended_objective`
  - `quarantine` must remain intact
- protected boundary:
  - keep the suspended main line from re-entering first-step workstart

4. later-horizon failure boundary
- main policy stress point:
  - `unresolved_relation`
  - `local_relation_block`
- protected boundary:
  - later turns should not silently collapse unresolved meaning

## 3. Dynamics Vocabulary To Surface Mapping
The manuscript should also tie each supported surface to the current mechanism
motifs:

1. early ambiguity-turn surface
- `Stable Resolution`

2. first-step side-topic surface
- `Clean Quarantine Hold`

3. downstream acceptance surface
- transition from accepted direction into useful continuation, but now as a
  mixed provider-sensitive read (`Gemini = support`, `Anthropic = inconclusive`)

4. later-horizon boundary
- `Relation-Preservation Hold`
- `Premature Relation Collapse`
- secondarily, where relevant:
  - `Generic Stall`
  - `Repeated-Starter Attractor`

## 4. Manuscript Integration Rule
Add manuscript-facing prose that does two things:
- names the state/action vocabulary that the result surface instantiates
- names the hold/break motif that the result surface supports or bounds

Do not:
- invent new policy states
- invent new dynamics motifs
- let vocabulary integration widen the underlying evidence claim
