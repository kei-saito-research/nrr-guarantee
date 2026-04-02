# Guarantee Supporting Layer Evidence Map v5

## Purpose

This memo restates the current manuscript-facing source map after the `v33`
comparison-contract repair.

## Source split

### A. Fixed support-layer texts

These live under `supporting_layer_sources/current/` and are imported without
reopening their ownership:
- `energy_to_guarantee_program_design_brief_v1_2026-03-17.md`
- `policy_minimal_spec_current_v1_2026-03-18.md`
- `energy_dynamics_mechanism_skeleton_candidate_v2_2026-03-17.md`
- `non_evaluative_principle_dynamics_closure_note_v1_2026-03-19.md`
- `policy_verification_pilot_protocol_current_v1_2026-03-18.md`
- `energy_guarantee_claim_schema_candidate_v2_2026-03-17.md`
- `energy_to_policy_handoff_memo_v1_2026-03-18.md`
- `energy_policy_verification_priority_resolution_baseline_vs_energy_policy_comparison_memo_v1_2026-03-17.md`

### B. Manuscript-facing repo-local notes

These live under `results/analysis/` and should be read as the current
manuscript-facing guidance surface:
- `guarantee_upstream_spine_import_note_v1_2026-03-30.md`
- `guarantee_first_claim_unit_fill_v3_2026-03-30.md`
- `guarantee_phase2_downstream_acceptance_closure_import_note_v3_2026-03-30.md`
- `guarantee_second_claim_unit_fill_v6_2026-03-30.md`
- `guarantee_third_claim_unit_fill_v2_2026-03-20.md`
- `guarantee_later_horizon_failure_boundary_v2_2026-03-20.md`
- `guarantee_policy_dynamics_manuscript_integration_v2_2026-03-20.md`

### C. Imported reviewed readout surface

This lives under `results/reviewed_phase2_downstream_acceptance_readout_v8/`
and carries the audited current repaired readout for the second claim unit:
- `guarantee_phase2_priority_resolution_downstream_acceptance_provider_read_table_v1_2026-03-21.csv`
- `guarantee_phase2_priority_resolution_downstream_acceptance_nrr_vs_ablation_comparison_memo_v1_2026-03-21.md`
- `guarantee_phase2_priority_resolution_downstream_acceptance_per_protocol_supplemental_table_v1_2026-03-21.csv`
- `non_evaluative_principle_guarantee_phase2_downstream_acceptance_readout_completion_memo_v8_2026-03-21.md`

## Section-to-source map

| Guarantee manuscript section | Current source artifact | Current use |
|---|---|---|
| Introduction | `results/analysis/guarantee_upstream_spine_import_note_v1_2026-03-30.md` | Fix the manuscript-facing upstream spine |
| Program position and scope | `results/analysis/guarantee_upstream_spine_import_note_v1_2026-03-30.md` | Fix `Guarantee` as the downstream claim-owning line under `paper7 -> Energy -> Guarantee` |
| Supporting-layer inputs: Policy | `supporting_layer_sources/current/policy_minimal_spec_current_v1_2026-03-18.md` | Import frozen state/action vocabulary |
| Supporting-layer inputs: Dynamics | `supporting_layer_sources/current/energy_dynamics_mechanism_skeleton_candidate_v2_2026-03-17.md` | Import hold/degrade/break motif vocabulary |
| Supporting-layer inputs: Dynamics closure | `supporting_layer_sources/current/non_evaluative_principle_dynamics_closure_note_v1_2026-03-19.md` | Keep Dynamics as mechanism vocabulary only |
| Supporting-layer inputs: Policy-Verification | `supporting_layer_sources/current/policy_verification_pilot_protocol_current_v1_2026-03-18.md` | Import matched-condition protocol constraints |
| First explicit claim-unit fill | `results/analysis/guarantee_first_claim_unit_fill_v3_2026-03-30.md` | Promote the first manuscript-facing bounded claim with its direct comparison memo present in the shipped surface |
| Second downstream-acceptance fill | `results/analysis/guarantee_second_claim_unit_fill_v6_2026-03-30.md` | Promote the repaired mixed downstream-acceptance claim with explicit comparison contract |
| Second downstream-acceptance closure note | `results/analysis/guarantee_phase2_downstream_acceptance_closure_import_note_v3_2026-03-30.md` | State that the decisive current comparison is `NRR vs Ablation` and keep `Baseline` visible as an auxiliary comparator |
| Second downstream-acceptance reviewed basis | `results/reviewed_phase2_downstream_acceptance_readout_v8/guarantee_phase2_priority_resolution_downstream_acceptance_provider_read_table_v1_2026-03-21.csv` | Anchor the provider-first mixed result inside the shipped repo surface |
| Third explicit claim-unit fill | `results/analysis/guarantee_third_claim_unit_fill_v2_2026-03-20.md` | Promote the repaired first-step side-topic/quarantine claim |
| Later-horizon failure boundary | `results/analysis/guarantee_later_horizon_failure_boundary_v2_2026-03-20.md` | Import later-horizon material as boundary reporting only |
| Policy/dynamics manuscript integration | `results/analysis/guarantee_policy_dynamics_manuscript_integration_v2_2026-03-20.md` | Tie supported surfaces to policy vocabulary and dynamics motifs |
