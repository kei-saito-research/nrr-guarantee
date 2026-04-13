# NRR-Guarantee: Bounded Commit/Defer Guarantee Surfaces and Explicit Downstream Boundaries

NRR-Guarantee hosts the manuscript snapshot and supporting reproducibility surface for the Guarantee line. The package focuses on bounded commit/defer guarantee surfaces with explicit downstream boundaries under provider, family, horizon, and observability limits.

NRR is not an anti-LLM framework.
NRR does not replace standard LLM use.
NRR optimizes when to commit and when to defer, under explicit conditions.

Part of the Non-Resolution Reasoning (NRR) research program.

## NRR Series Hub (Start here)

For the cross-paper map and current series links, start here:
- [NRR Series Hub](https://github.com/kei-saito-research/nrr-series-hub)

## Current manuscript snapshot

- Current manuscript source: `manuscript/current/nrr-guarantee_manuscript_v60.tex`
- Current manuscript PDF: `manuscript/current/nrr-guarantee_manuscript_v60.pdf`
- Current checksum manifest:
  `manuscript/checksums_active_review_surface_sha256.txt`

## Reproducibility entry points

- Reproducibility guide: `reproducibility.md`
- Build current manuscript package: `bash scripts/build_current_manuscript.sh`
- Verify the active manuscript surface:
  `bash scripts/verify_active_review_surface.sh`
- Create the active package bundle:
  `bash scripts/create_active_review_bundle.sh`
- Regenerate current figure assets: `python3 scripts/generate_manuscript_figures.py`

Current local build rule:
- try cached TeX compile first
- if required TeX resources are unavailable locally, emit a source-rendered PDF
  fallback so the current manuscript surface remains buildable
- preserve the repo-root layout when preparing a bundle so the
  shipped `scripts/` entrypoints remain executable from the artifact itself

## Current Guarantee package scope

The current package surface is defined by
`manuscript/checksums_active_review_surface_sha256.txt`.

- Current manuscript snapshot:
  - `manuscript/current/nrr-guarantee_manuscript_v60.tex`
- Current manuscript PDF:
  - `manuscript/current/nrr-guarantee_manuscript_v60.pdf`
- Current figure assets:
  - `manuscript/figures/fig1_supported_claim_progression_v1.png`
  - `manuscript/figures/fig2_guarantee_centered_architecture_v1.png`
- Figure-generation script:
  - `scripts/generate_manuscript_figures.py`
- Current supporting-layer evidence import map:
  - `results/analysis/guarantee_supporting_layer_evidence_map_v19_2026-04-02.md`
- Upstream spine import note:
  - `results/analysis/guarantee_upstream_spine_import_note_v3_2026-04-02.md`
- First explicit bounded-claim fill:
  - `results/analysis/guarantee_first_claim_unit_fill_v3_2026-03-30.md`
- Downstream-acceptance closure import note:
  - `results/analysis/guarantee_phase2_downstream_acceptance_closure_import_note_v5_2026-03-30.md`
- Downstream-acceptance boundary surface:
  - `results/analysis/guarantee_downstream_acceptance_boundary_surface_v2_2026-03-31.md`
- Imported auxiliary downstream-acceptance readout surface:
  - `results/reviewed_phase2_downstream_acceptance_readout_v8/`
- Side-topic supporting surface note:
  - `results/analysis/guarantee_side_topic_supporting_surface_v1_2026-03-30.md`
- Later-horizon failure boundary:
  - `results/analysis/guarantee_later_horizon_failure_boundary_v3_2026-03-30.md`
- Policy/dynamics manuscript integration:
  - `results/analysis/guarantee_policy_dynamics_manuscript_integration_v10_2026-04-02.md`
- Historical closure provenance:
  - `results/analysis/guarantee_git_ready_closure_v2_2026-03-20.md`
- Bundled supporting-layer sources:
  - `supporting_layer_sources/current/`
  - this directory carries the fixed support-layer texts and historical
    provenance that the manuscript imports without reopening
  - it now also ships the direct downstream-boundary comparison memo
    plus run-annotation CSVs for the downstream boundary, and review copies of
    the current upstream `NRR-Patterns v0_29` / `Energy v26` reference artifacts
  - it now also ships the repaired side-topic direct comparison memo plus its
  run-annotation CSVs, and the later-horizon provider-scored memos plus the
  active run-annotation CSVs used to support the failure boundary one layer
    below the manuscript-facing memos
  - it now also ships a row-scored behavior-first read table plus a compact
    summary-count CSV so the current secondary paragraph no longer depends on
    prose-only count reconstruction
  - the downstream boundary is not carried by this directory alone; the current
    manuscript-facing read lives in the repo-local analysis notes,
    while the imported reviewed readout surface listed above remains auxiliary
    repaired boundary evidence

The broader tracked package remains repo-local only. It may retain chronology
and helper materials that are not part of the current package
surface, and it is not shipped as part of the active bundle described
here.

## Scope boundary

This repository exposes a bounded `Guarantee`
manuscript/package surface.

It supports:
- one current manuscript line
- a fixed section structure that absorbs `Policy`, `Dynamics`, and
  `Policy-Verification` as supporting layers
- an explicit split between fixed support-layer texts and repo-local
  claim-evidence notes
- current manuscript ontology and routing being fixed by
  the active manuscript plus the current `results/analysis/` guidance surface,
  rather than by older local family labels that may remain visible inside
  imported fixed support-layer artifacts
- a repo-local upstream-spine note that separates current manuscript framing
  from frozen historical transition texts
- one filled bounded claim unit plus one downstream-acceptance boundary
  section, one side-topic supporting-surface section, and one later-horizon
  failure-boundary section
- a local bundled copy of the cited supporting-layer source artifacts
- a repo-local downstream-acceptance closure import note plus an imported
  reviewed readout surface for the current downstream boundary
- stable active-bundle build and verification entrypoints
- a self-contained current package

It does not yet establish by itself:
- provider-universal or pair-wide downstream closure
- public push timing

## Repository structure

The tree below is the navigation map for the package shipped by
`checksums_active_review_surface_sha256.txt`.

```text
nrr-guarantee/
|-- README.md
|-- LICENSE
|-- reproducibility.md
|-- manuscript/
|   |-- current/
|   |   |-- nrr-guarantee_manuscript_v60.tex
|   |   `-- nrr-guarantee_manuscript_v60.pdf
|   |-- figures/
|   |   |-- fig1_supported_claim_progression_v1.png
|   |   `-- fig2_guarantee_centered_architecture_v1.png
|   `-- checksums_active_review_surface_sha256.txt
|-- results/
|   `-- analysis/
|       |-- guarantee_supporting_layer_evidence_map_v19_2026-04-02.md
|       |-- guarantee_upstream_spine_import_note_v3_2026-04-02.md
|       `-- guarantee_first_claim_unit_fill_v3_2026-03-30.md
|       `-- guarantee_phase2_downstream_acceptance_closure_import_note_v5_2026-03-30.md
|       `-- guarantee_downstream_acceptance_boundary_surface_v2_2026-03-31.md
|       `-- guarantee_side_topic_supporting_surface_v1_2026-03-30.md
|       `-- guarantee_later_horizon_failure_boundary_v3_2026-03-30.md
|       `-- guarantee_policy_dynamics_manuscript_integration_v10_2026-04-02.md
|       `-- guarantee_git_ready_closure_v2_2026-03-20.md
|   `-- reviewed_phase2_downstream_acceptance_readout_v8/
|       `-- reviewed current readout surface
|-- supporting_layer_sources/
|   `-- current/
|       |-- README.md
|       |-- primary imported support files
|       `-- transitive local trace files needed for in-bundle review closure
`-- scripts/
    |-- build_current_manuscript.sh
    |-- create_active_review_bundle.sh
    |-- generate_manuscript_figures.py
    `-- verify_active_review_surface.sh
```

## Stable package entrypoints

- `bash scripts/build_current_manuscript.sh`
- `bash scripts/verify_active_review_surface.sh`
- `bash scripts/create_active_review_bundle.sh`
- these commands are guaranteed only when the shipped artifact preserves the
  repository root layout shown above

## License

CC BY 4.0. See `LICENSE`.

## Contact

Kei Saito
Independent Researcher, Japan
ORCID: https://orcid.org/0009-0006-4715-9176
Email: kei.saito.research@gmail.com
