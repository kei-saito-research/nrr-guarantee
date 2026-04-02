# Energy Policy-Verification Side-Topic Quarantine Design Candidate v1

## Status
- Date: 2026-03-17
- Type: exact pilot-design memo
- Scope: freeze the exact next `Policy-Verification` pilot design for the first-step side-topic / quarantine line under the already accepted scope
- Depends on:
  - `energy_policy_verification_side_topic_quarantine_scope_candidate_v1_2026-03-17.md`
  - `energy_policy_verification_side_topic_quarantine_scope_external_review_decision_memo_v1_2026-03-17.md`
  - `energy_policy_verification_side_topic_quarantine_annotation_minispec_v1_2026-03-17.md`
  - `energy_policy_verification_side_topic_quarantine_run_input_v1_2026-03-17.csv`
  - `energy_policy_verification_side_topic_quarantine_run_input_gemini_v1_2026-03-17.csv`
  - `priority_resolution_baseline_arm_system_prompt_v1.txt`
  - `priority_resolution_nrr_resolution_plus_first_commit_candidate_v2.txt`
- Not a run authorization memo
- Not a manuscript claim memo

## 1. Purpose
This memo freezes the exact design details intentionally left open by the side-topic / quarantine scope memo.

It fixes:
- exact first-step side-topic episode artifacts
- exact baseline / revised Energy-policy prompt correspondence
- exact provider/model tuple
- exact first-step annotation and reporting rule
- the provider-split row-freeze source so design scope and annotation scope point to the same active row set

It does not:
- authorize execution
- widen the pilot beyond the accepted first-step side-topic / quarantine scope

## 2. Assistant-Side Read
- judgment:
  - `adopt`
- reason:
  - the scope is already accepted, and the remaining work is to make the first-step side-topic / quarantine pilot auditable without silently widening it into later followthrough or template-local rescue claims

## 3. Fixed Claim Boundary
This next pilot carries one claim target only:
- under the tested provider pair and fixed first-step side-topic surface, does the revised Energy policy improve `appropriate` relative to baseline under matched conditions?

This pilot still excludes:
1. one-turn-later side-topic continuation quality
2. later-horizon stability
3. answer-use completeness
4. template-local quarantine repair
5. overall downstream task quality

## 4. Exact Episode And Arm Correspondence
The comparison must stay on one surface family only:
- `priority_resolution_side_first_handoff`

Freeze the episode unit exactly as:
1. user states the active main objective
2. user introduces one plausible side topic
3. assistant produces one fixed clean priority-resolution handoff turn
4. user explicitly accepts the side direction
5. assistant gives the first follow-up response after that acceptance

For this pilot, turn 3 is fixed context rather than a scored variable.
This keeps the first-step family isolated and does not reopen the already-closed early-resolution line.

### 4.1 Baseline arm
- prompt surface:
  - `priority_resolution_baseline_arm_system_prompt_v1.txt`
- operational meaning:
  - generic helper baseline with no explicit priority-resolution operator beyond the frozen baseline prompt artifact

### 4.2 Revised Energy-policy arm
- prompt surface:
  - `priority_resolution_nrr_resolution_plus_first_commit_candidate_v2.txt`
- operational meaning:
  - apply the adopted revised Energy policy on the first post-acceptance step while holding the handoff context fixed

### 4.3 Matched-condition rule
Everything except the arm-specific prompt surface must match:
1. provider
2. model
3. temperature
4. exact episode row
5. annotation procedure

## 5. Canonical Provider / Model Freeze
Freeze the provider pair as:
- `anthropic` / `claude-sonnet-4-6`
- `gemini` / `gemini-2.0-flash`

Freeze shared run settings as:
- temperature:
  - `0.0`
- reps:
  - `4` per provider
- total rows:
  - `12` per provider

Audit rule:
- if the runtime returns a provider-side identifier variant, record that returned string in run provenance without silently changing this design memo

## 6. Exact Input Artifacts
Use only these frozen first-step side-topic tables:
- Anthropic-side table:
  - `energy_policy_verification_side_topic_quarantine_run_input_v1_2026-03-17.csv`
- Gemini-side table:
  - `energy_policy_verification_side_topic_quarantine_run_input_gemini_v1_2026-03-17.csv`

These tables freeze:
1. template ids
2. acceptance variant ids
3. rep ids
4. exact turn texts
5. provider/model/temperature tuple

Audit note:
- the Anthropic-side table rewrites the older supporting-line model string `claude-sonnet-4-20250514` to the canonical freeze string `claude-sonnet-4-6` so this design memo and the active row artifact now match exactly

## 7. Observability Provenance
Use the frozen first-step side-topic scoring fields from:
- `energy_policy_verification_side_topic_quarantine_annotation_minispec_v1_2026-03-17.md`

Annotate exactly these fields:
- `chosen_side_direction_workstart_present`
- `suspended_main_reference_absent`
- `main_direction_intrusion_absent`
- `appropriate`
- `notes_optional`

Combined rule:
- `appropriate = 1` iff:
  - `chosen_side_direction_workstart_present = 1`
  - `suspended_main_reference_absent = 1`
  - `main_direction_intrusion_absent = 1`

Carry rule:
- the supported carry-forward metric for this next pilot is `appropriate`
- the other fields remain mandatory because they define the explicit first-step failure boundary rather than a silently widened success claim

## 8. Failure-Boundary Reporting Rule
The pilot report must expose provider-sensitive first-step residuals in the primary table set.

Required reporting views:
1. per-provider totals for all 4 scored fields before any pooled totals
2. per-template counts for all 4 scored fields within each provider
3. pooled totals only after provider slices are shown
4. explicit residual note if any provider still:
  - acknowledges without beginning accepted side-topic work
  - keeps the suspended main objective verbally live
  - gives any work for the suspended main objective

Boundary rule:
- do not headline pooled totals alone
- do not summarize the result as provider-universal side-topic / quarantine closure
- keep any provider difference explicit if it remains present

## 9. Exact Output And Prompt-Provenance Contract
The design expects the pilot to retain, per arm:
1. raw output
2. response table
3. annotation table
4. comparison memo
5. prompt provenance including arm prompt path and checksum

Prompt-provenance source rule for the later run-authorization memo:
- freeze prompt provenance against the project config artifacts under:
  - `nrr-energy/configs/priority_resolution/priority_resolution_baseline_arm_system_prompt_v1.txt`
  - `nrr-energy/configs/priority_resolution/priority_resolution_nrr_resolution_plus_first_commit_candidate_v2.txt`
- do not treat shared-pack copies as the canonical checksum source
- freeze the runtime prompt source and checksum from the runtime-resolved prompt text, not from an unrelated copied file snapshot

The comparison memo must explicitly state:
- what is in scope:
  - first-step side-topic commitment / quarantine under the frozen first-step family
- what is out of scope:
  - later followthrough
  - answer-use completeness
  - provider universality
  - overall downstream quality
- what visible boundary remained under the frozen scope

## 10. What This Memo Leaves For Run Authorization
The next pre-run memo should only:
1. authorize execution under this already frozen first-step design
2. restate the exact artifact names produced by the runner
3. state the stop rule if any frozen component is missing or mismatched at runtime
4. freeze the exact prompt source path and runtime checksum for each arm

It should not reopen:
1. provider choice
2. model choice
3. prompt surfaces
4. input tables
5. observability fields
6. failure-boundary reporting rule

## 11. Review Question
Is this side-topic / quarantine exact design auditable and narrow enough to authorize later execution without silently promoting a later-followthrough or local-rescue claim?

## Primary References
- `energy_policy_verification_side_topic_quarantine_scope_candidate_v1_2026-03-17.md`
- `energy_policy_verification_side_topic_quarantine_annotation_minispec_v1_2026-03-17.md`
- `energy_policy_verification_side_topic_quarantine_run_input_v1_2026-03-17.csv`
- `energy_policy_verification_side_topic_quarantine_run_input_gemini_v1_2026-03-17.csv`
- `priority_resolution_baseline_arm_system_prompt_v1.txt`
- `priority_resolution_nrr_resolution_plus_first_commit_candidate_v2.txt`
