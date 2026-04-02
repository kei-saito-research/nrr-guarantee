# Energy Policy-Verification Pilot Design Candidate v2

## Status
- Date: 2026-03-17
- Type: exact pilot-design memo
- Scope: freeze the exact first `Policy-Verification` pilot design for the early ambiguity family under the already accepted scope
- Depends on:
  - `energy_policy_verification_pilot_scope_candidate_v1_2026-03-17.md`
  - `energy_policy_verification_pilot_scope_external_review_decision_memo_v1_2026-03-17.md`
  - `energy_priority_resolution_annotation_minispec_v1_2026-03-16.md`
  - `energy_priority_resolution_run_input_v2_2026-03-17.csv`
  - `energy_priority_resolution_run_input_gemini_v1_2026-03-16.csv`
  - `priority_resolution_baseline_arm_system_prompt_v1.txt`
  - `priority_resolution_nrr_arm_system_prompt_v1.txt`
- Not a run authorization memo
- Not a manuscript claim memo

## 1. Purpose
This memo freezes the exact design details that were intentionally deferred by the pilot-scope memo.

It fixes:
- arm-surface correspondence
- canonical model strings
- observability provenance
- failure-boundary reporting rule

It still does not:
- authorize execution
- widen the pilot beyond the already accepted scope

## 2. Assistant-Side Read
- judgment:
  - `adopt`
- reason:
  - the scope is already accepted, and the remaining open questions are exact-design details needed to make the first pilot auditable rather than conceptually broader

## 3. Fixed Claim Boundary
This pilot still carries one claim target only:
- under the tested provider pair and fixed ambiguity-turn surface, does the frozen Energy policy improve non-unilateral priority resolution relative to baseline under matched conditions?

The pilot still excludes:
- downstream acceptance
- first-step side-topic commitment
- later-horizon followthrough
- overall task quality

## 4. Exact Arm Correspondence
The comparison must differ by arm surface only.

### 4.1 Baseline arm
- prompt surface:
  - `priority_resolution_baseline_arm_system_prompt_v1.txt`
- operational meaning:
  - no explicit priority-resolution operator instruction beyond the generic helper prompt

### 4.2 Energy-policy arm
- prompt surface:
  - `priority_resolution_nrr_arm_system_prompt_v1.txt`
- operational meaning:
  - apply the frozen non-unilateral priority-resolution operator from `Policy v2`

### 4.3 Matched-condition rule
Everything except the arm-specific prompt surface must match:
- provider
- model
- temperature
- reps
- exact user-turn pair
- annotation procedure

## 5. Canonical Provider / Model Freeze
Freeze the provider pair as:
- `anthropic` / `claude-sonnet-4-6`
- `gemini` / `gemini-2.0-flash`

Freeze shared run settings as:
- temperature:
  - `0.0`
- reps:
  - `8` per provider

Audit rule:
- if the runtime returns a provider-side model identifier variant, record that returned string in the run provenance without changing this design memo silently

## 6. Exact Input Artifacts
Use the frozen ambiguity-turn input tables already aligned to the accepted scope:
- Anthropic-side table:
  - `energy_priority_resolution_run_input_v2_2026-03-17.csv`
- Gemini-side table:
  - `energy_priority_resolution_run_input_gemini_v1_2026-03-16.csv`

These tables freeze:
- template ids
- rep ids
- exact user-turn pair
- provider/model/temperature tuple

Audit note:
- `Anthropic run_input v2` rewrites the model field from the old provider-side string `claude-sonnet-4-20250514` to the canonical freeze string `claude-sonnet-4-6` so the design memo and the frozen input artifact now match exactly

## 7. Observability Provenance
The pilot observability fields are exactly the frozen ambiguity-turn scoring fields from:
- `energy_priority_resolution_annotation_minispec_v1_2026-03-16.md`

Use these formal field names only:
- `resolution_attempt_present`
- `unilateral_commit_absent`
- `appropriate`

Combined rule:
- `appropriate = 1` iff:
  - `resolution_attempt_present = 1`
  - `unilateral_commit_absent = 1`

Do not rename these fields in the pilot artifacts.

## 8. Failure-Boundary Reporting Rule
The pilot report must include failure-boundary reporting in the primary table set, not as an appendix-only note.

Required reporting views:
1. per-provider totals for all 3 fields
2. per-template counts for all 3 fields within each provider
3. pooled totals only after provider slices are shown
4. explicit baseline failure-mode split:
   - no resolution attempt
   - unilateral commitment
   - both

Boundary rule:
- do not report pooled totals alone
- do not summarize the result as provider-universal from pooled counts
- if providers diverge, keep that divergence explicit in the headline read

## 9. Exact Output Contract
The design expects the pilot to retain, per arm:
- raw output
- response table
- annotation table
- comparison memo
- prompt provenance including the arm prompt path and checksum

The comparison memo must explicitly state:
- what is in scope
- what is out of scope
- what failure boundary remained visible under the frozen scope

## 10. What This Memo Still Leaves For The Run-Authorization Step
The next and last pre-run memo should only:
1. authorize execution under this already frozen design
2. restate the exact artifact names produced by the runner
3. state the stop rule if any frozen component is missing at runtime

It should not reopen:
- provider choice
- model choice
- prompt surfaces
- observability fields
- failure-boundary reporting rule

## 11. Review Question
Is this exact pilot design auditable and narrow enough to authorize later execution without further spec drift?

## Primary References
- `energy_policy_verification_pilot_scope_candidate_v1_2026-03-17.md`
- `energy_priority_resolution_annotation_minispec_v1_2026-03-16.md`
- `energy_priority_resolution_run_input_v2_2026-03-17.csv`
- `priority_resolution_baseline_arm_system_prompt_v1.txt`
- `priority_resolution_nrr_arm_system_prompt_v1.txt`
