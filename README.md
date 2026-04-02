# NRR-Guarantee: Bounded Commit/Defer Guarantee Surfaces and Explicit Downstream Boundaries

NRR-Guarantee is the downstream paper/repository surface that closes the current
`Guarantee-centered` architecture under explicit provider, family, horizon, and
observability bounds.

NRR is not an anti-LLM framework.
NRR does not replace standard LLM use.
NRR optimizes when to commit and when to defer, under explicit conditions.
Series numbering policy: `paper3` is permanently skipped and never reused.

Part of the Non-Resolution Reasoning (NRR) research program.

## NRR Series Hub (Start here)

For the cross-paper map and current series links, start here:
- [NRR Series Hub](https://github.com/kei-saito-research/nrr-series-hub)

## Current manuscript snapshot

- Protected baseline source: `manuscript/current/nrr-guarantee_manuscript_v27.tex`
- Protected baseline PDF: `manuscript/current/nrr-guarantee_manuscript_v27.pdf`
- Active derived review source: `manuscript/current/nrr-guarantee_manuscript_v54.tex`
- Active derived review PDF: `manuscript/current/nrr-guarantee_manuscript_v54.pdf`
- Active review checksum manifest:
  `manuscript/current/checksums_active_review_surface_sha256.txt`

## Derived review variant

- Protected baseline remains:
  - `manuscript/current/nrr-guarantee_manuscript_v27.tex`
  - `manuscript/current/nrr-guarantee_manuscript_v27.pdf`
- Current rewritten derived variant for review:
  - `manuscript/current/nrr-guarantee_manuscript_v54.tex`
  - `manuscript/current/nrr-guarantee_manuscript_v54.pdf`
- Read `v54` as a review-pending derived variant, not as the promoted baseline

## Reproducibility entry points

- Review-package guide: `reproducibility.md`
- Build current manuscript package: `bash scripts/build_current_manuscript.sh`
- Verify the reviewer-facing active review surface:
  `bash scripts/verify_active_review_surface.sh`
- Create the reviewer-facing active review bundle:
  `bash scripts/create_active_review_bundle.sh`
- Regenerate current figure assets: `python3 scripts/generate_manuscript_figures.py`

Current local build rule:
- try cached TeX compile first
- if required TeX resources are unavailable locally, emit a source-rendered PDF
  fallback so the current reviewer-facing manuscript surface remains buildable
- preserve the repo-root layout when preparing an external review zip so the
  shipped `scripts/` entrypoints remain executable from the artifact itself

## Current Guarantee package scope

The reviewer-facing active review surface is defined by
`manuscript/current/checksums_active_review_surface_sha256.txt` and is the
surface that the active review bundle ships and verifies.

- Protected baseline snapshot:
  - `manuscript/current/nrr-guarantee_manuscript_v27.tex`
- Active derived review snapshot:
  - `manuscript/current/nrr-guarantee_manuscript_v54.tex`
- Protected baseline PDF:
  - `manuscript/current/nrr-guarantee_manuscript_v27.pdf`
- Active derived review PDF:
  - `manuscript/current/nrr-guarantee_manuscript_v54.pdf`
- Current figure assets:
  - `manuscript/current/fig1_supported_claim_progression_v1.png`
  - `manuscript/current/fig2_guarantee_centered_architecture_v1.png`
- Figure-generation script:
  - `scripts/generate_manuscript_figures.py`
- Current supporting-layer evidence import map:
  - `results/analysis/guarantee_supporting_layer_evidence_map_v19_2026-04-02.md`
- Manuscript-facing upstream spine import note:
  - `results/analysis/guarantee_upstream_spine_import_note_v3_2026-04-02.md`
- First explicit bounded-claim fill:
  - `results/analysis/guarantee_first_claim_unit_fill_v3_2026-03-30.md`
- Downstream-acceptance closure import note:
  - `results/analysis/guarantee_phase2_downstream_acceptance_closure_import_note_v5_2026-03-30.md`
- Downstream-acceptance boundary surface:
  - `results/analysis/guarantee_downstream_acceptance_boundary_surface_v2_2026-03-31.md`
- Imported reviewed auxiliary downstream-acceptance readout surface:
  - `results/reviewed_phase2_downstream_acceptance_readout_v8/`
- Side-topic supporting surface note:
  - `results/analysis/guarantee_side_topic_supporting_surface_v1_2026-03-30.md`
- Behavior-first manipulation-check import note:
  - `results/analysis/guarantee_behavior_first_manipulation_check_import_note_v10_2026-04-02.md`
- Behavior-first shipped scored audit tables:
  - `supporting_layer_sources/current/guarantee_behavior_first_provider_pair_rerun_v1/guarantee_behavior_first_provider_pair_row_scored_read_table_v1_2026-03-31.csv`
  - `supporting_layer_sources/current/guarantee_behavior_first_provider_pair_rerun_v1/guarantee_behavior_first_provider_pair_summary_counts_v1_2026-03-31.csv`
- Later-horizon failure boundary:
  - `results/analysis/guarantee_later_horizon_failure_boundary_v3_2026-03-30.md`
- Policy/dynamics manuscript integration:
  - `results/analysis/guarantee_policy_dynamics_manuscript_integration_v10_2026-04-02.md`
- Historical external-review closure provenance:
  - `results/analysis/guarantee_git_ready_closure_v2_2026-03-20.md`
- Bundled supporting-layer sources for repo-local review tracing:
  - `supporting_layer_sources/current/`
  - this directory carries the fixed support-layer texts and historical
    provenance that the manuscript imports without reopening
  - it now also ships the direct mainline downstream-boundary comparison memo
    plus run-annotation CSVs for the downstream boundary, and review copies of
    the current integrated `paper7 v0_29` / `Energy v26` authority artifacts
  - it now also ships the repaired side-topic direct comparison memo plus its
  run-annotation CSVs, and the later-horizon provider-scored memos plus the
  active run-annotation CSVs used to support the failure boundary one layer
    below the manuscript-facing memos
  - it now also ships a row-scored behavior-first read table plus a compact
    summary-count CSV so the current secondary paragraph no longer depends on
    prose-only count reconstruction
  - the downstream boundary is not carried by this directory alone; the current
  manuscript-facing mainline read lives in the repo-local analysis notes,
  while the imported reviewed readout surface listed above remains auxiliary
    repaired boundary evidence

The broader tracked package remains repo-local only. It may retain chronology
and helper materials that are not part of the reviewer-facing active review
surface, and it is not shipped as part of the active review bundle described
here.

Current review-status read:
- last externally review-cleared artifact:
  - the historical `v8` shared-box package recorded in
    `results/analysis/guarantee_git_ready_closure_v2_2026-03-20.md`
- protected baseline status:
  - `v27` is the preserved protected baseline and should not be read as already
    externally re-cleared at `v27`
- active manuscript/package line:
  - `v54` is the current active derived review line for confirm review
  - `v46` is the upstream-sync derived review variant under the fixed
    `paper7 -> Energy -> Guarantee` spine; it preserves the side-topic result as
    supporting evidence, keeps later-horizon as a boundary-only surface under a
    separate `priority-resolution horizon-stability` family, makes the Gemini
    downstream followthrough regression explicit on the mainline boundary
    surface, and carries the current behavior-first provenance notes on the
    derived line
  - `v47` is the current package-integrity derived review variant; it preserves
    the `v46` claim surface while making the review target, evidence-routing
    map, and active-bundle file inventory internally consistent
  - `v48` closes the remaining package-integrity gap by aligning the current
    authority notes to the active review line and shipping the cited historical
    review-clear provenance inside the bundle itself
  - `v49` preserves the `v46` claim surface and the `v48` package boundary
    while repairing manuscript-date provenance, aligning the Transfer/Coupled
    bibliography to the bundled upstream authority copies, and lifting the
    behavior-first direct audit note onto the current review line
  - `v50` preserves the `v46` claim surface and the `v49` package boundary
    while canonicalizing the shipped Transfer repo identity to the protected
    hidden-state-interface-reuse tree, treating the bundled paper7
    `nrr-transfer` label as historical provenance only, and correcting the
    current evidence map's behavior-first audit-note inventory
  - `v51` preserves the `v46` claim surface and the `v50` package boundary
    while aligning the carried `paper7` bibliography title to the bundled
    upstream authority copy and making the README status read unambiguous about
    `v27` as protected baseline versus `v51` as the active derived review line
  - `v52` preserves the `v46` claim surface and the `v51` package boundary
    while narrowing the manuscript's repository-surface description to the
    actual shipped active review surface by removing the unbundled working
    drafting-outline item
  - `v53` preserves the `v46` claim surface and the `v52` package boundary
    while syncing the current authority/provenance notes to the active line and
    making the downstream-acceptance boundary ontology explicit as a
    priority-resolution-family accepted-direction boundary
  - `v54` preserves the `v46` claim surface and the `v53` package boundary
    while unifying the downstream-acceptance ontology across the manuscript and
    the carried downstream-boundary authority memo as one later boundary inside
    the carried priority-resolution family, and while advancing the current
    guidance notes to the same active line

## Scope boundary

This repository currently exposes a bounded reviewer-facing `Guarantee`
manuscript/package surface.

It supports:
- a protected baseline plus one active derived review line
- a fixed section structure that absorbs `Policy`, `Dynamics`, and
  `Policy-Verification` as supporting layers
- an explicit split between fixed support-layer texts and repo-local
  claim-evidence notes
- current manuscript ontology and current reviewer-facing routing being fixed by
  the active manuscript plus the current `results/analysis/` guidance surface,
  rather than by older local family labels that may remain visible inside
  imported fixed support-layer artifacts
- a repo-local upstream-spine note that separates current manuscript authority
  from frozen historical handoff texts
- one filled bounded claim unit plus one downstream-acceptance boundary
  section, one side-topic supporting-surface section, and one later-horizon
  failure-boundary section
- a local bundled copy of the cited supporting-layer source artifacts
- a repo-local downstream-acceptance closure import note plus an imported
  reviewed readout surface for the current downstream boundary
- a secondary behavior-first manipulation-check note with explicit limitations
- stable active-bundle build and verification entrypoints
- an externally reviewable current package

It does not yet establish by itself:
- provider-universal or pair-wide downstream closure
- public push timing

## Repository structure

The tree below is the navigation map for the reviewer-facing active review
bundle shipped by `checksums_active_review_surface_sha256.txt`.

```text
nrr-guarantee/
|-- README.md
|-- LICENSE
|-- reproducibility.md
|-- manuscript/
|   `-- current/
|       |-- nrr-guarantee_manuscript_v27.tex
|       |-- nrr-guarantee_manuscript_v27.pdf
|       |-- nrr-guarantee_manuscript_v54.tex
|       |-- nrr-guarantee_manuscript_v54.pdf
|       |-- fig1_supported_claim_progression_v1.png
|       |-- fig2_guarantee_centered_architecture_v1.png
|       `-- checksums_active_review_surface_sha256.txt
|-- results/
|   `-- analysis/
|       |-- guarantee_supporting_layer_evidence_map_v19_2026-04-02.md
|       |-- guarantee_upstream_spine_import_note_v3_2026-04-02.md
|       `-- guarantee_first_claim_unit_fill_v3_2026-03-30.md
|       `-- guarantee_phase2_downstream_acceptance_closure_import_note_v5_2026-03-30.md
|       `-- guarantee_downstream_acceptance_boundary_surface_v2_2026-03-31.md
|       `-- guarantee_side_topic_supporting_surface_v1_2026-03-30.md
|       `-- guarantee_behavior_first_manipulation_check_import_note_v10_2026-04-02.md
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

## Stable review-package entrypoints

- `bash scripts/build_current_manuscript.sh`
- `bash scripts/verify_active_review_surface.sh`
- `bash scripts/create_active_review_bundle.sh`
- these commands are guaranteed only when the review artifact preserves the
  repository root layout shown above

## License

CC BY 4.0. See `LICENSE`.

## Contact

Kei Saito
Independent Researcher, Japan
ORCID: https://orcid.org/0009-0006-4715-9176
Email: kei.saito.research@gmail.com
