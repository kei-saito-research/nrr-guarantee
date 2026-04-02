# Energy Forward Validation Protocol v11

## Status
- Type: operational protocol memo
- Date: 2026-03-14
- Scope: define the active forward-validation surface after Gemini combo widening clears under chunked all-8 execution
- Supersedes: `energy_forward_validation_protocol_v10_2026-03-14.md`
- Not a manuscript claim by itself

## 1. Purpose
This memo fixes the first forward validation shape for `baseline` versus `Energy policy`.
The goal is not to re-prove the calibration paper on the same rows.
The goal is to test whether the frozen Energy decision instrument improves or degrades outcomes on new paired runs under fixed conditions.

## 2. Fixed Claim Boundary
- This protocol tests prospective behavior of one frozen Energy policy candidate.
- It does not authorize universal policy claims.
- Results must report gains, regressions, and explicit non-effective regions together.
- If the forward test fails, the calibration paper remains a calibration paper; it does not become invalid retrospectively.
- The current routed Stage A package is frozen at the implementation-gated-trial level only; it is operationally usable for forward validation, but it is not itself a manuscript-facing proof that the routed prefix signal directly measures grounded state quality.

## 3. Frozen Policy Candidate for First Test
Use one primary policy candidate only for the first forward run:
- cost definition: `C_net(output)`
- profile: `q50_c50`
- threshold rule: `tau` grouped by `dataset_family x profile`
- online rule:
  - compute frozen standardized `DeltaU_online`
  - if `DeltaU_online > tau_group_value`, choose `prefer_pattern`
  - if `DeltaU_online < -tau_group_value`, choose `prefer_baseline`
  - if `|DeltaU_online| <= tau_group_value`, emit `tie`

Operational decision mapping for the first test:
- `prefer_pattern`: commit the pattern-side update path
- `prefer_baseline`: commit the baseline-side update path
- `tie`: fall back to baseline

Rationale for this first freeze:
- `q50_c50` with `C_net(output)` is the manuscript's primary reporting slice
- the current calibration already exposes its strongest and weakest regions
- the first prospective test should validate one fixed candidate before adding profile variants

## 4. Observable Extractor Gate
The online Energy arm may not use realized outcome variables directly.
It must consume frozen proxy observables estimated before route choice.

Define the online inputs as:
- `q_hat_online`: pre-decision proxy for the quality-side term
- `c_hat_online`: pre-decision proxy for the cost-side term under the `C_net(output)` family

### 4.1 Required extractor package
Stage A must produce and freeze one `observable_extractor_v2` package with:
- extractor identifier and version
- code or deterministic rule implementation reference
- checksum
- allowed input fields
- exact formula or deterministic transform producing `q_hat_online`
- exact formula or deterministic transform producing `c_hat_online`
- any auxiliary constants or lookup tables

### 4.2 Required replay artifact
Stage A must also freeze the canonical pre-branch replay artifact:
- `decision_context_v2`

`decision_context_v2` is the route-invariant decision record used for extractor replay.
If the run framework cannot emit `decision_context_v2` before route choice, the Energy arm is shadow-only and not live-valid.

### 4.3 Allowed inputs for the extractor
The extractor may use only information available before the route choice:
- current task state
- current turn input
- current partial trace up to the decision point
- provider
- model
- temperature
- prompt template family
- deterministic parser outputs derived from the current partial trace

### 4.4 Forbidden inputs for the extractor
The extractor may not use:
- realized misinterpretation outcomes
- realized rework-cost outcomes
- paired baseline-versus-pattern result labels from the same forward run
- any information from later turns not available at the decision point
- manual post-hoc annotations added after the run

### 4.5 Gate rule
- Current status:
  - `observable_extractor_v2_compact_grounding_2026-03-12` is frozen for Stage A use
  - `decision_context_v2` is frozen for Stage A use
  - implementation-gated live trials froze successfully on Anthropic and Gemini for both `stable` and `context-drift`
- Therefore the Stage A instrumentation gate is currently satisfied for the first forward validation.
- If either frozen artifact changes after this point, the forward validation must not silently reuse this protocol; create a new protocol version instead.

## 5. Calibration Parameter Bundle
Stage A must also produce and freeze one calibration parameter bundle for the policy candidate.
This bundle must be versioned and checksummed before Stage B begins.

### 5.1 Bundle structure
The bundle may contain one row per online lookup key, but `tau` is not independently fit per condition in the current canonical calibration artifacts.
For the current protocol version:
- z-score parameters are bundle-lookup-key-addressable
- `tau` is inherited from the grouped calibration summary at `dataset_family x profile`

Required fields:
- `condition_key`
- `dataset_family`
- `provider`
- `pattern_or_combo_direction`
- `temperature`
- `profile=q50_c50`
- `cost_variant=c_net_output`
- `wq`
- `wc`
- `q_mu_cal`
- `q_sd_cal`
- `c_mu_cal`
- `c_sd_cal`
- `tau_group_key`
- `tau_group_value`

### 5.1a Forward coverage lookup rule
For exact Stage A route-probe rows, the row address may equal the original route-probe `condition_key`.

For the first covered forward slice, online lookup must instead use the frozen forward coverage rule:
- `forward_bundle_coverage_v1_provider_model_temp_pattern_2026-03-12`

Canonical lookup key:
- `forward_coverage_v1|dataset_family|provider|model|temperature|pattern_or_combo_direction`

Operational meaning:
- preserve `dataset_family`
- preserve `provider`
- preserve `model`
- preserve `temperature`
- preserve `pattern_or_combo_direction`
- do not preserve `scenario_id`
- do not preserve `template_id`

This rule is required because the forward-only pool emits new `S_FORWARD_*` scenario/template identities that are not exact matches to the Stage A route-probe rows.

### 5.1b Gemini combo split freeze and chunked all-8 execution surface
For Gemini combo, do not keep using the old mixed combo bundle as the active package surface.

Keep the split-family bundle family as the active package base.

For the originally opened two-direction surface, use:
- opened-surface split bundle:
  - `forward_combo_split_bundle_stagea_gemini_t00_candidate_v1_2026-03-13.json`
- split coverage rule:
  - `forward_combo_split_bundle_v1_family_provider_model_temp_direction_2026-03-13`

For widened all-8 execution, use:
- unified split bundle:
  - `forward_combo_split_bundle_stagea_gemini_t00_all8_rep8_candidate_v1_2026-03-14.json`

Operational meaning:
- `S_FORWARD_STABLE_01` maps to `combo_stable`
- `S_FORWARD_CONTEXT_DRIFT_01` maps to `combo_nonstable`
- `S_FORWARD_DRIFT_RETURN_RECOVERY_01` maps to `combo_nonstable`

Boundary:
- this is the active Gemini combo execution freeze for the currently opened surface
- evidence supporting the opened two-direction freeze:
  - online rerun `energy_forward_online_gemini_combo_t00_20260314T055254Z` passed with `exact_match_count = 6/6`
  - main rerun `energy_forward_main_gemini_combo_t00_20260314T062243Z` passed with `exact_match_count = 48/48`
  - stable route counts improved from the old mixed-bundle all-baseline behavior to:
    - `branch_conditional = 5/8` pattern-side, `3/8` baseline
    - `conditional_branch = 6/8` pattern-side, `2/8` baseline
  - nonstable rows remained baseline-side:
    - `context-drift = 16/16` baseline
    - `drift-return-recovery = 16/16` baseline
- evidence supporting widened all-8 execution:
  - remaining-6 widening rescue and smoke:
    - online rerun `energy_forward_online_gemini_combo_t00_20260314T090650Z` passed with `exact_match_count = 18/18`
    - main rerun `energy_forward_main_gemini_combo_t00_20260314T091301Z` passed with `exact_match_count = 54/54`
  - unified all-8 scenario-chunked online runs:
    - `energy_forward_online_gemini_combo_t00_20260314T095220Z` passed with `exact_match_count = 16/16`
    - `energy_forward_online_gemini_combo_t00_20260314T094901Z` passed with `exact_match_count = 8/8`
  - unified all-8 scenario-chunked main runs:
    - `energy_forward_main_gemini_combo_t00_20260314T095813Z` passed with `exact_match_count = 48/48`
    - `energy_forward_main_gemini_combo_t00_20260314T101209Z` passed with `exact_match_count = 24/24`
  - unified all-8 monolithic online rerun after launcher/runtime fix:
    - `energy_forward_online_gemini_combo_t00_20260314T150144Z` passed with `exact_match_count = 24/24`
- authorization:
  - this freeze authorizes continued E-next execution on the originally opened Gemini combo two-direction surface
  - this freeze also authorizes widened all-8 Gemini combo execution when runs are chunked by scenario
  - this freeze also authorizes monolithic all-8 Gemini combo online execution on the same bundle after the launcher/runtime fix that cleared raw campaign write
- required chunking rule for unified all-8 execution:
  - chunk A:
    - `S_FORWARD_STABLE_01,S_FORWARD_CONTEXT_DRIFT_01`
  - chunk B:
    - `S_FORWARD_DRIFT_RETURN_RECOVERY_01`
- if Gemini combo calibration/read is redesigned again after this point, create `v12`

### 5.2 Canonical tau source
For this protocol version, `tau_group_value` must come from the current grouped calibration artifact:
- `stats/evidence/energy_e1_tau_summary_v1_1.csv`

Canonical grouping rule:
- single-operator rows inherit the `stageb + q50_c50` net tau
- ordered-combo rows inherit the `combo + q50_c50` net tau

No forward-test row may recompute `tau`.
If a future Energy line adopts condition-specific threshold fitting, that change requires a new protocol version.

### 5.3 Bundle generator dependency
Stage A must also freeze one calibration-bundle generator compatible with `observable_extractor_v2`.

Minimum bundle-generator requirements:
- deterministic script or implementation reference
- fixed input corpus
- fixed output schema
- checksum

Canonical Stage A input corpus:
- shadow runs logged with `decision_context_v2`

If the bundle generator is not frozen, Stage A is incomplete even if the extractor package and bundle schema are frozen.

Current forward-coverage generator candidate:
- `scripts/build_forward_coverage_bundle_v1.py`

### 5.4 Canonical bundle checksum scope
For the current Python reference implementation, `bundle_checksum` is defined as the SHA-256 of the UTF-8 JSON serialization of the canonical bundle identity.

Canonical identity rule:
- exclude `generated_at_utc`
- exclude the self-referential `bundle_checksum` value itself when hashing
- project each row to the required bundle fields listed in `5.1`
- sort rows lexicographically by those projected fields before hashing
- serialize object keys with `sort_keys=True`
- require all numeric identity fields to be finite

Scope note:
- this checksum definition is frozen for the current CPython reference implementation
- cross-language or cross-runtime checksum equivalence is not yet required and remains deferred beyond Stage A

## 6. Baseline and Energy Arms
### 6.1 Baseline arm
- Standard non-Energy execution under the same task, provider, model, and temperature
- No Energy gating or post-hoc route switching

### 6.2 Energy arm
- Same upstream task and fixed prompts
- Same provider/model/temperature cell as the paired baseline arm
- Use only `observable_extractor_v2`, `decision_context_v2`, and the frozen calibration parameter bundle
- Use the frozen Energy decision rule above to choose commit/defer routing online
- If the run is a forward-only row, derive the bundle lookup key using `5.1a` before fetching frozen moments
- For Gemini combo runs on the opened split-frozen surface, derive the effective dataset family using `5.1b` before fetching the bundle row

### 6.3 Pairing unit
Each comparison unit must match on:
- scenario
- provider
- model
- temperature
- repetition index
- prompt template family

## 7. Data Split Rule
- Calibration artifacts from the current paper remain frozen and are not expanded with the new forward runs.
- Forward validation must use new runs only.
- No row from the current calibration artifacts may be reused as forward-test evidence.

## 8. First Validation Scope
Run two stages in order.

### Stage A: instrumentation and freeze gate
- purpose: confirm logging, routing, token accounting, pre-decision extractor behavior, and replayability
- size: one small pilot batch only
- no claim use
- required outputs:
  - frozen `observable_extractor_v2`
  - frozen `decision_context_v2` schema and emitted pilot artifacts
  - frozen calibration-bundle generator
  - frozen calibration parameter bundle
  - successful shadow replay showing that logged decisions can be recomputed exactly

Current status:
- completed at the implementation-gated-trial level
- no additional Stage A extractor-rescue work is required before the first forward validation pass
- Anthropic forward shadow pilot on the new `S_FORWARD_*` pool passed for `t=0.3` and `pattern=branch`
- remaining Stage A caveat to carry into reporting:
  - under current routed-live conditions, the grounding component saturates and the effective live `q` range collapses to `[0.75, 1.00]`
  - Gemini context-drift replay retains the highest current within-condition token correlation (`|corr| = 0.547057823888`), which remains inside gate but should be watched first in later expansion

Current forward bundle coverage status:
- covered now:
  - `stageb + anthropic + claude-sonnet-4-20250514 + t=0.3 + branch`
- current Gemini combo split surfaces:
  - opened two-direction split freeze remains valid
  - remaining-6 widening is execution-supported
  - unified all-8 is execution-supported under scenario chunking
- not yet authorized as default:
  - monolithic all-8 single-run launcher path

### Stage B: main forward paired validation
Stage B may begin only after Stage A gate success.

- providers/models:
  - `claude-sonnet-4-20250514`
  - `gemini-2.0-flash`
  - `gpt-4o-mini-2024-07-18`
- condition families:
  - single-operator cells aligned with Stage B structure
  - ordered-combo cells aligned with current combo structure
- temperatures:
  - single-operator cells: `t=0.0` and `t=0.3`
  - ordered-combo cells: `t=0.0`
- scenarios:
  - new scenarios only
  - scenario pool must be frozen before result inspection
- repetitions:
  - freeze before the first main run
  - no outcome-based expansion after inspection

Current execution rule:
- keep existing non-combo and Anthropic combo lanes moving without reopening prompt design
- keep Gemini combo on the split successor path
- for widened all-8 Gemini combo execution, use scenario chunking with the unified all-8 bundle
- carry explicit Gemini limitation language because stable effectiveness remains direction-dependent
- do not promote monolithic all-8 single-run execution to the default path until the raw-write stall is resolved

## 9. Hypotheses for the First Forward Test
### Primary hypothesis
Under fixed conditions, the frozen Energy policy increases usable commit/defer decisions without unacceptable quality regression relative to baseline.

### Required failure-sensitive reading
The test must also be allowed to show:
- no practical gain
- provider-specific regressions
- temperature-specific regressions
- over-commit and over-defer failure concentration

## 10. Primary Metrics
Report at minimum:
- misinterpretation outcome
- rework cost tokens
- output tokens
- realized net utility under the frozen `C_net(output)` definition
- decision coverage rate
- over-commit rate
- over-defer rate
- tie fallback rate

Recommended paired summaries:
- Energy minus baseline mean delta per metric
- provider-separated summaries
- temperature-separated summaries
- ordered-combo direction summaries

## 11. Frozen Outcome Labeling Rule
To prevent post-hoc reinterpretation, define failure labels from the paired realized outcomes with the same frozen utility family and the same deadband width.

For each paired comparison unit, compute:
- `DeltaU_realized` using the forward-run realized `Q` and `C_net(output)` values, standardized with the frozen calibration parameters from Section 5
- `tau_group_value` from the same row's `tau_group_key`

Then define the realized preference label:
- if `DeltaU_realized > tau_group_value`, realized label = `prefer_pattern`
- if `DeltaU_realized < -tau_group_value`, realized label = `prefer_baseline`
- if `|DeltaU_realized| <= tau_group_value`, realized label = `tie`

Failure flags are then fixed as:
- `over_commit_flag = 1` if the executed route is pattern-side and realized label = `prefer_baseline`
- `over_defer_flag = 1` if the executed route is baseline-side and realized label = `prefer_pattern`
- `tie_fallback_flag = 1` if online decision = `tie` and executed route = baseline-side

Interpretation rule:
- tie-to-baseline is not automatically an over-defer
- it becomes an over-defer only when the realized label is `prefer_pattern`

## 12. Fixed Guard Rules
- paired baseline vs Energy comparison under identical conditions
- `max_quality_retries=0`
- no outcome-based rerun
- communication-failure retries only
- prompts, scenarios, routing logic, extractor package, replay artifact, bundle generator, and labeling rules frozen before inspecting results
- logging schema fixed before the first main run

## 13. Required Logging
### 13.1 Per run
- scenario_id
- provider
- model
- temperature
- repetition
- policy_arm (`baseline` or `energy`)
- pattern or route identifier
- condition_key
- observable_extractor_id
- observable_extractor_checksum
- calibration_bundle_id
- calibration_bundle_checksum
- calibration_bundle_generator_id
- calibration_bundle_generator_checksum
- tau_group_key

### 13.2 Pre-decision replay artifact
- `decision_context_v2` identifier
- `decision_context_v2` checksum
- `decision_context_valid`
- `decision_context_failure_code`
- decision_turn_index
- serialized `prefix_turns`

### 13.3 Per decision point
- turn_id
- condition_key
- extractor_valid
- extractor_failure_code
- q_hat_online
- c_hat_online
- q_z_frozen
- c_z_frozen
- delta_u_online
- tau_group_value_applied
- policy_decision (`prefer_pattern`, `prefer_baseline`, `tie`)
- selected_route
- parse / execution status

### 13.4 Per run summary
- final task outcome metrics
- total_tokens
- total_output_tokens
- total_rework_cost
- realized_utility_q
- realized_utility_c_net_output
- realized_delta_u
- realized_preference_label
- over_commit_flag
- over_defer_flag
- tie_fallback_flag

Audit rule:
- the logged `decision_context_v2`, `decision_context_valid`, `decision_context_failure_code`, `extractor_valid`, `extractor_failure_code`, `q_hat_online`, `c_hat_online`, `delta_u_online`, `tau_group_value_applied`, `condition_key`, extractor identifiers, and bundle-generator identifiers must be sufficient to replay and verify the online route choice after the run

## 14. Failure Reporting Rules
The main report must explicitly enumerate:
- cells where baseline outperforms Energy
- cells where Energy increases decisions but worsens quality
- cells where `tie -> baseline` fallback dominates
- cells with concentrated `over_commit_flag = 1`
- cells with concentrated `over_defer_flag = 1`
- provider-specific instability, especially if Gemini-centered risk persists
- higher-temperature risk if the Stage B-like ordering persists

## 15. Release Rule for This Protocol
- Treat this memo as the fixed protocol candidate for the first forward validation pass.
- If a protocol item changes after this point, create `v8` instead of silently editing this file in place.
