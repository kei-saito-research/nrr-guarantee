# Reproducibility (NRR-Guarantee)

## Scope

This repository bundles the current `Guarantee` manuscript package under the fixed `Guarantee-centered` architecture. The current package is intentionally narrow: a manuscript, supporting evidence notes, bundled supporting-layer source files, and stable build and verification commands.

## Stable package commands

- Build the current manuscript to temp output:
  - `bash scripts/build_current_manuscript.sh`
  - default output: the highest-numbered tracked manuscript in `manuscript/current/`; at present this is `/tmp/nrr-guarantee_current_build/nrr-guarantee_manuscript_v60.pdf`
- Verify the current manuscript surface:
  - `bash scripts/verify_active_review_surface.sh`
  - this checks `manuscript/checksums_active_review_surface_sha256.txt`
- Create the current package bundle:
  - `bash scripts/create_active_review_bundle.sh`
- Regenerate the shipped figure assets:
  - `python3 scripts/generate_manuscript_figures.py`

## Current package surface

- Current manuscript TeX: `manuscript/current/nrr-guarantee_manuscript_v60.tex`
- Current manuscript PDF: `manuscript/current/nrr-guarantee_manuscript_v60.pdf`
- Current figure assets:
  - `manuscript/figures/fig1_supported_claim_progression_v1.png`
  - `manuscript/figures/fig2_guarantee_centered_architecture_v1.png`
- Figure-generation script:
  - `scripts/generate_manuscript_figures.py`
- Supporting evidence notes:
  - `results/analysis/guarantee_supporting_layer_evidence_map_v19_2026-04-02.md`
  - `results/analysis/guarantee_upstream_spine_import_note_v3_2026-04-02.md`
  - `results/analysis/guarantee_first_claim_unit_fill_v3_2026-03-30.md`
  - `results/analysis/guarantee_phase2_downstream_acceptance_closure_import_note_v5_2026-03-30.md`
  - `results/analysis/guarantee_downstream_acceptance_boundary_surface_v2_2026-03-31.md`
  - `results/analysis/guarantee_side_topic_supporting_surface_v1_2026-03-30.md`
  - `results/analysis/guarantee_later_horizon_failure_boundary_v3_2026-03-30.md`
  - `results/analysis/guarantee_policy_dynamics_manuscript_integration_v10_2026-04-02.md`
- Bundled downstream-acceptance readout directory:
  - `results/reviewed_phase2_downstream_acceptance_readout_v8/`
- Bundled supporting-layer source surface:
  - `supporting_layer_sources/current/`
- Current package checksum manifest:
  - `manuscript/checksums_active_review_surface_sha256.txt`

## Checksum policy

- `manuscript/checksums_active_review_surface_sha256.txt` defines the current package surface for this repository.
- `bash scripts/verify_active_review_surface.sh` verifies that manuscript surface, and `bash scripts/create_active_review_bundle.sh` packages the same surface into a zip that preserves the repository layout.
- Coverage includes the current manuscript line, current figure assets, repo metadata (`README.md`, `reproducibility.md`, `LICENSE`), shipped build and verification entrypoints, the figure-generation helper, the shipped claim-evidence notes used by the current line, the downstream-acceptance readout directory, and the supporting-layer source files needed to inspect the current package.

## Supporting-layer source surface

Current drafting is constrained by the following fixed support layers:
- program design brief:
  - `supporting_layer_sources/current/energy_to_guarantee_program_design_brief_v1_2026-03-17.md`
- current policy source:
  - `supporting_layer_sources/current/policy_minimal_spec_current_v1_2026-03-18.md`
- current policy-verification protocol:
  - `supporting_layer_sources/current/policy_verification_pilot_protocol_current_v1_2026-03-18.md`
- current dynamics closure note:
  - `supporting_layer_sources/current/non_evaluative_principle_dynamics_closure_note_v1_2026-03-19.md`
- current guarantee claim schema candidate:
  - `supporting_layer_sources/current/energy_guarantee_claim_schema_candidate_v2_2026-03-17.md`
- current dynamics mechanism vocabulary:
  - `supporting_layer_sources/current/energy_dynamics_mechanism_skeleton_candidate_v2_2026-03-17.md`
- current support-layer transition note in `supporting_layer_sources/current/`
- direct downstream comparison materials and run-annotation CSVs:
  - `supporting_layer_sources/current/energy_policy_verification_downstream_boundary_baseline_vs_energy_policy_comparison_memo_v1_2026-03-17.md`
  - `supporting_layer_sources/current/energy_policy_verification_priority_resolution_baseline_vs_energy_policy_comparison_memo_v1_2026-03-17.md`

## Artifact map

| Artifact | Command | Output |
|---|---|---|
| Current manuscript build | `bash scripts/build_current_manuscript.sh` | highest-numbered tracked manuscript PDF in `/tmp/nrr-guarantee_current_build/` (currently `nrr-guarantee_manuscript_v60.pdf`) |
| Current figure regeneration | `python3 scripts/generate_manuscript_figures.py` | `manuscript/figures/fig1_supported_claim_progression_v1.png`, `manuscript/figures/fig2_guarantee_centered_architecture_v1.png` |
| Current manuscript source snapshot | N/A (tracked artifact) | `manuscript/current/nrr-guarantee_manuscript_v60.tex` |
| Current supporting-layer source bundle | N/A (tracked artifact) | `supporting_layer_sources/current/` |
| Bundled downstream-acceptance readout directory | N/A (tracked artifact) | `results/reviewed_phase2_downstream_acceptance_readout_v8/` |

## Notes

- The build wrapper first attempts an offline cached TeX compile. If the local TeX cache is incomplete, it falls back to a source-rendered PDF via `cupsfilter` so the current package remains buildable in this environment.
- Shipped bundles should preserve the repository root layout rather than flattening selected files, otherwise the build and verification entrypoints stop being executable from the delivered package itself.
- Full typeset reproduction still depends on the local TeX cache state in the execution environment.
