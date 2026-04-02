# Energy Policy-Verification Downstream Boundary Design Candidate v2

## Status
- Date: 2026-03-17
- Type: exact pilot-design memo
- Scope: freeze the exact next `Policy-Verification` pilot design for the downstream-boundary / preacceptance-burden line under the already accepted scope
- Depends on:
  - `energy_policy_verification_downstream_boundary_scope_candidate_v1_2026-03-17.md`
  - `energy_policy_verification_downstream_boundary_scope_external_review_decision_memo_v1_2026-03-17.md`
  - `energy_priority_resolution_downstream_acceptance_two_provider_read_memo_v1_2026-03-17.md`
  - `energy_priority_resolution_downstream_acceptance_annotation_minispec_v2_2026-03-17.md`
  - `energy_priority_resolution_downstream_acceptance_run_input_v2_2026-03-17.csv`
  - `energy_priority_resolution_downstream_acceptance_run_input_gemini_v1_2026-03-17.csv`
  - `priority_resolution_baseline_arm_system_prompt_v1.txt`
  - `priority_resolution_nrr_arm_system_prompt_v1.txt`
- Not a run authorization memo
- Not a manuscript claim memo

## 1. Purpose
This memo freezes the exact design details that were intentionally left open by the downstream-boundary scope memo.

It fixes:
- exact downstream episode artifacts
- exact baseline / Energy-policy prompt correspondence
- exact provider/model tuple
- exact observability and reporting rule
- the annotation row-freeze source so design scope and annotation scope point to the same active row set

It does not:
- authorize execution
- widen the next pilot beyond the accepted downstream-boundary scope

## 2. Assistant-Side Read
- judgment:
  - `adopt`
- reason:
  - the next scope is already accepted, and the remaining work is to make the downstream-boundary pilot auditable without silently widening it into a stronger downstream or quarantine claim

## 3. Fixed Claim Boundary
This next pilot carries one claim target only:
- under the tested provider pair and fixed downstream-acceptance surface, does the frozen Energy policy reduce `preacceptance_rework_burden_absent` relative to baseline under matched conditions?

This pilot still excludes:
- a claim that downstream handoff quality is provider-balanced in the strong sense
- explicit suspended-objective quarantine
- later-horizon followthrough
- overall task quality

## 4. Exact Episode And Arm Correspondence
The comparison must stay on one surface family only:
- `priority_resolution_acceptance_handoff`

Freeze the episode unit exactly as:
1. user states the active main objective
2. user introduces one plausible side topic
3. assistant responds under baseline or Energy-policy condition
4. user explicitly accepts one immediate direction
5. assistant gives the first follow-up response after that acceptance

### 4.1 Baseline arm
- prompt surface:
  - `priority_resolution_baseline_arm_system_prompt_v1.txt`
- operational meaning:
  - generic helper baseline with no explicit priority-resolution operator beyond the frozen baseline prompt artifact

### 4.2 Energy-policy arm
- prompt surface:
  - `priority_resolution_nrr_arm_system_prompt_v1.txt`
- operational meaning:
  - apply the frozen Energy priority-resolution operator already used on the mainline `baseline vs Energy policy` surface

### 4.3 Matched-condition rule
Everything except the arm-specific prompt surface must match:
- provider
- model
- temperature
- exact episode row
- annotation procedure

## 5. Canonical Provider / Model Freeze
Freeze the provider pair as:
- `anthropic` / `claude-sonnet-4-6`
- `gemini` / `gemini-2.0-flash`

Freeze shared run settings as:
- temperature:
  - `0.0`
- reps:
  - `4` per acceptance variant
- total rows:
  - `24` per provider

Audit rule:
- if the runtime returns a provider-side identifier variant, record that returned string in run provenance without silently changing this design memo

## 6. Exact Input Artifacts
Use only these frozen downstream-acceptance tables:
- Anthropic-side table:
  - `energy_priority_resolution_downstream_acceptance_run_input_v2_2026-03-17.csv`
- Gemini-side table:
  - `energy_priority_resolution_downstream_acceptance_run_input_gemini_v1_2026-03-17.csv`

These tables freeze:
- template ids
- acceptance variant ids
- rep ids
- exact turn texts
- provider/model/temperature tuple

Audit note:
- `Anthropic downstream_acceptance run_input v2` rewrites the old provider-side model string `claude-sonnet-4-20250514` to the canonical freeze string `claude-sonnet-4-6` so this design memo and the active input artifact now match exactly

## 7. Observability Provenance
Use the frozen downstream-acceptance scoring fields from:
- `energy_priority_resolution_downstream_acceptance_annotation_minispec_v2_2026-03-17.md`

Annotate exactly these fields:
- `accepted_direction_followthrough_present`
- `rejected_direction_intrusion_absent`
- `preacceptance_rework_burden_absent`
- `appropriate`
- `notes_optional`

Combined rule:
- `appropriate = 1` iff:
  - `accepted_direction_followthrough_present = 1`
  - `rejected_direction_intrusion_absent = 1`
  - `preacceptance_rework_burden_absent = 1`

Carry rule:
- the supported carry-forward metric for this next pilot is `preacceptance_rework_burden_absent`
- the other fields remain mandatory because they define the explicit downstream failure boundary rather than a silently widened success claim

## 8. Failure-Boundary Reporting Rule
The pilot report must expose provider-sensitive downstream residuals in the primary table set.

Required reporting views:
1. per-provider totals for all 4 scored fields before any pooled totals
2. per-template counts for all 4 scored fields within each provider
3. pooled totals only after provider slices are shown
4. explicit residual-failure note if `preacceptance_rework_burden_absent` improves while `accepted_direction_followthrough_present` or `appropriate` remain provider-sensitive

Boundary rule:
- do not headline pooled totals alone
- do not summarize the result as provider-universal downstream handoff quality
- keep the currently visible Gemini residual explicit if it remains present:
  - acceptance boundary is preserved
  - preacceptance burden is removed
  - but first accepted-direction work can remain too generic

## 9. Exact Output And Prompt-Provenance Contract
The design expects the pilot to retain, per arm:
- raw output
- response table
- annotation table
- comparison memo
- prompt provenance including arm prompt path and checksum

Prompt-provenance source rule for the later run-authorization memo:
- freeze prompt provenance against the project config artifacts under:
  - `nrr-energy/configs/priority_resolution/priority_resolution_baseline_arm_system_prompt_v1.txt`
  - `nrr-energy/configs/priority_resolution/priority_resolution_nrr_arm_system_prompt_v1.txt`
- do not treat shared-pack copies as the canonical checksum source
- freeze the runtime prompt source and checksum from the runtime-resolved prompt text, not from an unrelated copied file snapshot

The comparison memo must explicitly state:
- what is in scope:
  - preacceptance-burden reduction under the frozen downstream family
- what is out of scope:
  - explicit quarantine
  - later-horizon followthrough
  - provider-universal downstream quality
- what visible boundary remained under the frozen scope

## 10. What This Memo Leaves For Run Authorization
The next pre-run memo should only:
1. authorize execution under this already frozen downstream design
2. restate the exact artifact names produced by the runner
3. state the stop rule if any frozen component is missing or mismatched at runtime
4. freeze the exact prompt source path and runtime checksum for each arm

It should not reopen:
- provider choice
- model choice
- prompt surfaces
- input tables
- observability fields
- boundary reporting rule

## 11. Review Question
Is this downstream-boundary exact design auditable and narrow enough to authorize later execution without silently promoting a stronger downstream or quarantine claim?

## Primary References
- `energy_policy_verification_downstream_boundary_scope_candidate_v1_2026-03-17.md`
- `energy_priority_resolution_downstream_acceptance_annotation_minispec_v2_2026-03-17.md`
- `energy_priority_resolution_downstream_acceptance_run_input_v2_2026-03-17.csv`
- `energy_priority_resolution_downstream_acceptance_run_input_gemini_v1_2026-03-17.csv`
- `priority_resolution_baseline_arm_system_prompt_v1.txt`
- `priority_resolution_nrr_arm_system_prompt_v1.txt`
