# Reproducibility (NRR-Guarantee)

## Scope

This repository surface bundles the current bounded `Guarantee`
manuscript/package under the fixed `Guarantee-centered` architecture.

At this stage the package is intentionally narrow:
- a current manuscript
- a supporting-layer evidence map
- a bundled supporting-layer source surface
- stable active-bundle build and verification commands

## Stable package commands

- Build the current manuscript to temp output:
  - `bash scripts/build_current_manuscript.sh`
  - default output: the highest-numbered tracked manuscript in
    `manuscript/current/`; at present this is
    `/tmp/nrr-guarantee_current_build/nrr-guarantee_manuscript_v56.pdf`
- Verify the reviewer-facing active review surface:
  - `bash scripts/verify_active_review_surface.sh`
  - this checks
    `manuscript/current/checksums_active_review_surface_sha256.txt`
  - command assumes the delivered artifact preserves the repository root layout
    so `scripts/`, `manuscript/current/`, `results/analysis/`,
    `results/reviewed_phase2_downstream_acceptance_readout_v8/`, and
    `supporting_layer_sources/current/` remain in the same relative positions
- Create the reviewer-facing active review bundle:
  - `bash scripts/create_active_review_bundle.sh`
- Regenerate the shipped figure assets:
  - `python3 scripts/generate_manuscript_figures.py`

## Reviewer-facing active review surface

- Current manuscript TeX: `manuscript/current/nrr-guarantee_manuscript_v56.tex`
- Current manuscript PDF: `manuscript/current/nrr-guarantee_manuscript_v56.pdf`
- Current figure assets:
  - `manuscript/current/fig1_supported_claim_progression_v1.png`
  - `manuscript/current/fig2_guarantee_centered_architecture_v1.png`
- Figure-generation script:
  - `scripts/generate_manuscript_figures.py`
- Supporting-layer evidence map:
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
- Later-horizon failure boundary:
  - `results/analysis/guarantee_later_horizon_failure_boundary_v3_2026-03-30.md`
- Policy/dynamics manuscript integration:
  - `results/analysis/guarantee_policy_dynamics_manuscript_integration_v10_2026-04-02.md`
- Behavior-first manipulation-check import note:
  - `results/analysis/guarantee_behavior_first_manipulation_check_import_note_v10_2026-04-02.md`
- Historical external-review closure provenance:
  - `results/analysis/guarantee_git_ready_closure_v2_2026-03-20.md`
- Behavior-first row-scored read table:
  - `supporting_layer_sources/current/guarantee_behavior_first_provider_pair_rerun_v1/guarantee_behavior_first_provider_pair_row_scored_read_table_v1_2026-03-31.csv`
- Behavior-first summary counts table:
  - `supporting_layer_sources/current/guarantee_behavior_first_provider_pair_rerun_v1/guarantee_behavior_first_provider_pair_summary_counts_v1_2026-03-31.csv`
- Bundled supporting-layer source surface:
  - `supporting_layer_sources/current/`
  - this directory now includes the primary imported support files plus the local
    transitive trace files needed to eliminate broken in-bundle links for the
    current bounded package surface
  - where imported fixed support files retain older local family labels, those
    labels remain part of the bundled source history only; the current
    manuscript ontology is fixed by the active manuscript and the current
    manuscript-facing `results/analysis/` notes
  - it now also includes the direct mainline downstream-boundary comparison
    memo, its four run-annotation CSV dependencies, and review copies of the
    current integrated `paper7 v0_29` / `Energy v26` authority artifacts
  - it now also includes the repaired side-topic comparison memo, its input-
    repair memo, its repaired `v2` input CSVs, and its four run-annotation
    CSVs
  - it now also includes the bounded behavior-first provider-pair rerun audit
    note, its frozen source rows, copied provider-pair rerun outputs, and
    shipped scored read tables so the current secondary paragraph can be
    checked locally without prose-only count reconstruction
  - it also includes the later-horizon two-provider memo, provider-scored
    memos, artifact-repair memo, and active run-annotation CSVs
- Active review checksum manifest:
  - `manuscript/current/checksums_active_review_surface_sha256.txt`

## Broader tracked package

The repo-local tracked package remains wider than the reviewer-facing active
review surface. It retains chronology and helper materials for local integrity
checks, but those files are not part of the active review bundle documented
here.

## Checksum policy

- `manuscript/current/checksums_active_review_surface_sha256.txt` defines the
  reviewer-facing active review surface for this repository.
- `bash scripts/verify_active_review_surface.sh` verifies that active review
  surface, and `bash scripts/create_active_review_bundle.sh` packages the same
  surface into a reviewer-facing zip.
- Active review coverage includes the current manuscript line, current
  committed figure assets, repo metadata
  (`README.md`, `reproducibility.md`, `LICENSE`), the reviewer-facing verify
  and bundle entrypoints, the figure-generation helper in `scripts/`, the
  repo-local claim-evidence notes used by the active derived variant, the
  imported reviewed downstream-acceptance readout surface, and the bundled
  supporting-layer source files needed to inspect the current line.
- The broader tracked package is repo-local and is not the shipped active
  review bundle documented in this file.

## Supporting-layer source surface

Current drafting is constrained by the following already-fixed support layers:
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
- ownership-boundary trace:
  - `supporting_layer_sources/current/energy_to_policy_handoff_memo_v1_2026-03-18.md`
  - this memo references the Energy package at manuscript `v8` because it was
    frozen at handoff time; the now-closed Energy manuscript is `v26`, and that
    later revision does not change the downstream support-layer boundaries used
    by the current `Guarantee` package
- upstream spine authority note:
  - `results/analysis/guarantee_upstream_spine_import_note_v3_2026-04-02.md`
  - use this note for the current manuscript-facing spine
    `paper7 -> Energy -> Guarantee`
  - use the same note to read
    `hidden-state-interface-reuse/tree/24bd24ea183f282cf535205ca4447e8169bac3b0`
    as the package's canonical Transfer repo identity for
    `paper5-nrr-transfer-v123.tex`, with the bundled paper7
    `nrr-transfer/tree/...` label preserved as historical provenance only
- downstream-acceptance provenance note:
  - the older
    `supporting_layer_sources/current/energy_priority_resolution_downstream_acceptance_two_provider_read_memo_v1_2026-03-17.md`
    remains historical pre-repair provenance only
  - the direct mainline downstream comparison is now also shipped under
    `supporting_layer_sources/current/energy_policy_verification_downstream_boundary_baseline_vs_energy_policy_comparison_memo_v1_2026-03-17.md`
    together with its four run-annotation CSVs
  - the current repaired downstream-boundary read is carried by the repo-local files
    `results/analysis/guarantee_phase2_downstream_acceptance_closure_import_note_v5_2026-03-30.md`
    and
    `results/analysis/guarantee_downstream_acceptance_boundary_surface_v2_2026-03-31.md`
  - the current first-claim direct comparison memo is now shipped under
    `supporting_layer_sources/current/energy_policy_verification_priority_resolution_baseline_vs_energy_policy_comparison_memo_v1_2026-03-17.md`
  - the audited repaired auxiliary readout itself is imported under
    `results/reviewed_phase2_downstream_acceptance_readout_v8/`
- bundle portability note:
  - workspace-specific absolute links have been normalized inside the shipped
  support bundle
  - where a transitive historical target is not shipped as a local file, the
    bundle preserves the target name as provenance text rather than as a broken
    markdown link
  - the repaired side-topic rerun input files now ship locally as the active
    `v2` inputs named by the repair memo
  - the behavior-first paragraph now has a shipped local audit path under
    `supporting_layer_sources/current/guarantee_behavior_first_provider_pair_rerun_v1/`
    rather than relying on note-only restatement

## Artifact map

| Artifact | Command | Output |
|---|---|---|
| Current manuscript build | `bash scripts/build_current_manuscript.sh` | highest-numbered tracked manuscript PDF in `/tmp/nrr-guarantee_current_build/` (currently `nrr-guarantee_manuscript_v56.pdf`) |
| Current figure regeneration | `python3 scripts/generate_manuscript_figures.py` | `manuscript/current/fig1_supported_claim_progression_v1.png`, `manuscript/current/fig2_guarantee_centered_architecture_v1.png` |
| Current manuscript source snapshot | N/A (tracked artifact) | `manuscript/current/nrr-guarantee_manuscript_v56.tex` |
| Current supporting-layer source bundle | N/A (tracked artifact) | `supporting_layer_sources/current/` |
| Imported reviewed downstream-acceptance surface | N/A (tracked artifact) | `results/reviewed_phase2_downstream_acceptance_readout_v8/` |

## Scope caveat

- This package is the current bounded reviewer-facing `Guarantee` manuscript
  surface.
- The build wrapper first attempts an offline cached TeX compile. If the local TeX
  cache is incomplete, it falls back to a source-rendered PDF via `cupsfilter` so
  the current package remains buildable in this environment.
- External review artifacts should preserve the repository root layout rather than
  flattening selected files, otherwise the shipped build/verify entrypoints stop
  being executable from the delivered package itself.
- The supporting-layer source bundle is normalized for portability: workspace-only
  paths are removed, shipped transitive references resolve locally, and
  non-shipped transitive references are rendered as provenance-only filenames.
- The support bundle is not by itself the full proof surface for the current
  downstream boundary; that mainline read is carried by the repo-local claim-evidence
  notes, while the imported reviewed readout surface listed above remains
  auxiliary repaired boundary evidence. The shipped support bundle now supplies
  the direct mainline comparison memo and run-annotation artifacts needed to
  audit the decisive baseline-vs-Energy figures locally.
- The behavior-first paragraph is still a secondary bounded note rather than a
  formal carried surface, but the shipped package now includes the local audit
  note, source rows, copied provider-pair rerun outputs, and row-scored tables
  needed to inspect that paragraph from inside the bundle itself.
- Full typeset reproduction still depends on the local TeX cache state in the
  execution environment.
- The last externally review-cleared narrow package is the historical `v8`
  shared-box artifact recorded in
  `results/analysis/guarantee_git_ready_closure_v2_2026-03-20.md`.
- The rewritten `v46` derived variant reflects the fixed
  `paper7 -> Energy -> Guarantee` spine while keeping the side-topic result as
  supporting evidence and the later-horizon material as a boundary-only
  diagnostic surface under a separate `priority-resolution horizon-stability`
  family; this line also keeps the downstream Discussion on the mainline
  authorization path while making the Gemini mainline followthrough regression
  explicit and aligning the current behavior-first audit surface to the
  reviewed `v46` package, before any baseline promotion or package
  renumbering.
- The package-integrity `v47` derived variant keeps that same claim surface
  while aligning the active review target, current source map, and reviewer-
  facing file inventory to the shipped `v47` bundle.
- The package-integrity `v48` derived variant closes the remaining reviewer-
  facing gap by aligning the current authority notes to the active review line
  and by shipping the cited historical review-clear provenance note inside the
  active bundle itself.
- The provenance-normalization `v50` derived variant preserves that same claim
  surface while canonicalizing the Transfer repo identity to the protected
  hidden-state-interface-reuse tree used by the current package, preserving the
  bundled paper7 `nrr-transfer` label as historical provenance only, and
  correcting the current evidence map so its behavior-first direct audit basis
  matches the shipped `v8` audit note.
- The provenance-clarity `v51` derived variant preserves that same claim
  surface while aligning the carried `paper7` bibliography title to the bundled
  `paper7 v0_29` authority copy and clarifying the active confirm-review line.
- The repo-surface-closure `v52` derived variant preserves that same claim
  surface while removing the unshipped working-drafting-outline item from the
  manuscript's repository-surface description so the prose matches the actual
  active review bundle exactly.
- The ontology-and-guidance-sync `v53` derived variant preserves that same
  claim surface while syncing the current authority/provenance note layer to
  the active line and making the downstream-acceptance boundary's place inside
  the priority-resolution family explicit across the manuscript ontology.
- The ontology-closure `v54` derived variant preserves that same claim surface
  while removing the remaining split between manuscript ontology and the carried
  downstream-boundary authority memo, so both now read the downstream-
  acceptance surface as the first accepted-direction boundary inside the
  carried priority-resolution family.
- The formatting-normalization `v56` derived variant preserves that same claim
  surface and package boundary while restoring the series-standard front matter,
  adding the shared AI acknowledgments block, making the manuscript-facing
  limitations explicit, and normalizing the active derived bibliography away
  from internal manuscript-version filenames.
