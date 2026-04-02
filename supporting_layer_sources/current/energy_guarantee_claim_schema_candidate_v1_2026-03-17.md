# Energy Guarantee Claim Schema Candidate v1

## Status
- Date: 2026-03-17
- Type: guarantee schema memo
- Scope: define the first bounded-claim schema that later `Policy-Verification` must satisfy before any `Guarantee` language is written
- Depends on:
  - `energy_policy_minimal_spec_candidate_v2_2026-03-17.md`
  - `energy_dynamics_mechanism_skeleton_candidate_v1_2026-03-17.md`
  - `energy_priority_resolution_branch_synthesis_memo_v2_2026-03-17.md`
  - `energy_priority_resolution_manuscript_boundary_text_v1_2026-03-17.md`
- Not a run authorization memo
- Not a manuscript claim memo

## 1. Purpose
This memo fixes the schema of the later `Guarantee` claim before `Policy-Verification` pilot design is frozen.

The goal is not to write the guarantee now.
The goal is to constrain what later counts as a valid guarantee-shaped statement.

This schema exists to prevent drift such as:
- upgrading a measured boundary read into a broad efficacy claim
- collapsing template-dependent later-horizon limits into one universal story
- writing guarantee text after results inspection without a pre-fixed claim form

## 2. Assistant-Side Read
- judgment:
  - `adopt`
- reason:
  - the branch already supports a narrow early-control region and a measured later-horizon boundary, so a claim schema can now be fixed even though no guarantee claim is yet authorized

## 3. Claim Unit
Any later guarantee statement must be expressed as one bounded claim unit with all fields filled.

Required fields:
1. `provider_scope`
2. `family_scope`
3. `horizon_scope`
4. `observability_scope`
5. `comparison_scope`
6. `supported_behavior`
7. `explicit_failure_boundary`
8. `unsupported_extension`

No guarantee statement is valid if any field is omitted.

## 4. Current Allowed Value Shapes
### 4.1 `provider_scope`
Allowed shape:
- exact tested provider set only

Current schema read:
- claims may later name the tested provider pair
- claims may later name one provider-specific slice
- claims may not say or imply provider universality

### 4.2 `family_scope`
Allowed shape:
- one named branch family only

Current schema read:
- `priority-resolution` may support family-bounded claims
- subfamilies may be named separately:
  - ambiguity resolution
  - downstream acceptance
  - first-step side-topic commitment
  - later-horizon stability
- no guarantee may silently merge unrelated branch families

### 4.3 `horizon_scope`
Allowed shape:
- one explicit checkpoint band only

Current schema read:
- early decision boundary
- downstream acceptance boundary
- first-step side-topic workstart
- later measured checkpoints such as `turn7`, `turn9`, `turn11`

No guarantee may say:
- long-horizon in general
- later followthrough in general
- stable continuation in general

### 4.4 `observability_scope`
Allowed shape:
- only behaviors directly scored or directly logged in the frozen protocol

Current schema read:
- direction resolution without unilateral commitment
- preacceptance burden present / absent
- chosen-side progress
- user-detail use
- unresolved-relation preservation or narrow check
- suspended-main reference absent
- repeated-starter absence

No guarantee may rely on:
- hidden intention
- unlogged reasoning quality
- broader conversation satisfaction
- final task success beyond the scored boundary

### 4.5 `comparison_scope`
Allowed shape:
- one frozen paired comparison under fixed conditions

Current schema read:
- baseline vs Energy policy
- or baseline vs one explicitly named operator arm inside a narrow local line

No guarantee may aggregate across incompatible comparison surfaces without a separately frozen rule.

## 5. Current Supported Claim Shapes
The schema currently permits only the following claim shapes later, if `Policy-Verification` actually supports them.

### 5.1 Early-control claim shape
Under the tested provider scope and frozen ambiguity-resolution family, the Energy policy supports non-unilateral priority resolution at the early decision boundary relative to baseline under fixed conditions.

### 5.2 Downstream-boundary claim shape
Under the tested provider scope and frozen downstream-acceptance family, the Energy policy reduces preacceptance burden relative to baseline under fixed conditions.

### 5.3 First-step commitment claim shape
Under the tested provider scope and frozen first-step side-topic family, the Energy policy supports clean first-step side-topic commitment while keeping the prior objective quarantined under fixed conditions.

### 5.4 Later-horizon boundary claim shape
Under the tested provider scope and frozen later-horizon family, the Energy policy more reliably preserves quarantine than unresolved-relation handling at later checkpoints; later-horizon followthrough therefore remains conditional rather than uniformly stable.

## 6. Explicitly Disallowed Claim Shapes
The schema forbids later claims of the following forms.

1. provider-universal claims
- example:
  - the policy is stable across providers

2. family-universal claims
- example:
  - the policy solves followthrough generally

3. long-horizon closure claims
- example:
  - the policy remains stable across later turns

4. mechanism-overreach claims
- example:
  - later failure is always caused by one single attractor

5. outcome-overreach claims
- example:
  - the policy improves end-task quality overall

6. replacement rhetoric
- example:
  - the policy should replace standard assistant behavior

## 7. Canonical Statement Template
Later guarantee text must fill this template only:

`Under [provider_scope], for [family_scope], at [horizon_scope], and on [observability_scope], the frozen Energy policy is supported relative to [comparison_scope] only for [supported_behavior]. This support excludes [explicit_failure_boundary] and does not extend to [unsupported_extension].`

## 8. Current Placeholder Fill For The Priority-Resolution Line
This is a schema example only, not an authorized guarantee:

- `provider_scope`
  - the tested provider pair, or one named tested provider slice
- `family_scope`
  - frozen `priority-resolution` branch, with one named subfamily
- `horizon_scope`
  - early boundary, downstream acceptance, first-step side-topic, or later checkpoints `turn7/9/11`
- `observability_scope`
  - only the frozen scored fields for that family
- `comparison_scope`
  - baseline vs Energy policy under fixed conditions
- `supported_behavior`
  - one narrow bounded behavior only
- `explicit_failure_boundary`
  - template dependence, provider dependence, unresolved-relation collapse, repeated-starter attractor, or lack of long-horizon closure
- `unsupported_extension`
  - provider universality, long-horizon closure, broad outcome improvement, guarantee beyond scored observables

## 9. What Policy-Verification Must Freeze Before Claim Use
Before any guarantee-shaped statement is permitted, `Policy-Verification` must freeze:
1. provider scope
2. family scope
3. metric / observability scope
4. comparison scope
5. failure-boundary reporting rule

If any of these are chosen after inspecting pilot outcomes, the resulting claim is invalid for guarantee use.

## 10. What This Schema Supports
This schema supports:
- reverse-design of the pilot from the later claim shape
- bounded manuscript language
- failure-boundary reporting as part of the claim, not as an appendix-only afterthought

## 11. What This Schema Does Not Support
This schema does not support:
- any immediate guarantee claim
- threshold selection by itself
- proof language
- skipping `Policy-Verification`

## 12. Next Practical Use
Use this schema as the constraint for the next `Policy-Verification` design memo.

The next pilot-design artifact should show explicitly:
- which claim field values are being targeted
- which values remain intentionally out of scope

## Primary References
- `energy_policy_minimal_spec_candidate_v2_2026-03-17.md`
- `energy_dynamics_mechanism_skeleton_candidate_v1_2026-03-17.md`
- `energy_priority_resolution_branch_synthesis_memo_v2_2026-03-17.md`
- `energy_priority_resolution_manuscript_boundary_text_v1_2026-03-17.md`
