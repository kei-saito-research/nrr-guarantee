# Supporting-Layer Source Bundle

This directory contains frozen local copies of the supporting-layer source
artifacts cited by the current `NRR-Guarantee` manuscript and
`reproducibility.md`.

## Purpose

- keep the current Guarantee package inspectable without requiring the
  reader to resolve workspace-only paths outside this repository
- preserve the exact source-layer texts that the current manuscript imports into
  its bounded claim surface
- include the direct early-claim comparison memo and run-annotation CSVs needed
  to inspect the first claim one level below the external-review memo
- include the direct downstream-boundary baseline-vs-Energy comparison memo and
  run-annotation CSVs needed to inspect the downstream boundary's decisive
  figures inside the bundle itself
- include the repaired side-topic baseline-vs-revised comparison memo and
  repaired input artifacts and run-annotation CSVs needed to inspect the
  side-topic supporting surface one level below the manuscript-facing memo
- include the bounded behavior-first provider-pair rerun audit note together
  with shipped source rows, copied provider-pair rerun outputs, and scored read
  tables needed to inspect the secondary behavior-first paragraph locally
- include the later-horizon two-provider read memo together with provider-scored
  memos and run-annotation CSVs needed to inspect the failure boundary one
  layer below the summary memo
- include copies of the current manuscript-facing upstream reference
  artifacts for `NRR-Patterns v0_29` and `Energy v26`

## Provenance

- files copied from `series_planning/`, `nrr-energy/results/analysis/`, and the
  referenced Energy review-pack context surface on 2026-03-20 JST
- these are review copies for the current Guarantee package; they do not reopen
  ownership of the upstream lines
- early ambiguity-turn comparison artifacts were additionally copied from
  `nrr-energy/results/analysis/` on 2026-03-30 JST so the shipped surface
  contains the direct baseline-vs-Energy comparison memo used by the first
  claim unit
- downstream-boundary baseline-vs-Energy comparison artifacts were additionally
  copied from `nrr-energy/results/analysis/` and the related Energy review-pack
  surface on 2026-03-30 JST so the shipped surface contains the direct
  downstream-boundary comparison memo and its run-annotation CSVs
- repaired side-topic comparison artifacts were additionally copied from
  `nrr-energy/results/analysis/` on 2026-03-30 JST so the shipped surface
  contains the direct side-topic comparison memo, its input-repair memo, its
  repaired `v2` input CSVs, and its four run-annotation CSVs
- bounded behavior-first audit artifacts were additionally copied from
  `series_planning/` and `nrr-energy/results/` on 2026-03-30 JST, then scored
  locally on 2026-03-31 JST so the shipped surface contains the local audit
  note, the exact source-row CSVs, the copied provider-pair rerun outputs, and
  the scored behavior-first read tables for the current secondary paragraph
- later-horizon scored artifacts were additionally copied from
  `nrr-energy/results/analysis/` on 2026-03-30 JST so the shipped surface
  contains the two-provider memo, the provider-scored memos, the artifact-
  repair memo, and the active run-annotation CSVs
- current upstream reference copies for `NRR-Patterns v0_29` and
  `Energy v26` were additionally copied on 2026-04-02 JST so the shipped
  surface can audit the live spine directly rather than by note-only assertion
- for the bundled `paper5-nrr-transfer-v123.tex` reference snapshot, this
  package now treats the hidden-state-interface-reuse tree at commit
  `24bd24ea183f282cf535205ca4447e8169bac3b0` as the canonical repo identity;
  the older `nrr-transfer` tree label preserved inside the bundled upstream
  review copy remains historical provenance only
- a sidecar reviewer note now sits next to the bundled upstream review copy:
  - `paper7_integrated_manuscript_v0_29_transfer_repo_identity_note_v1_2026-04-02.md`
  - use it when reading the bundled upstream copy directly so the preserved old
    label is not mistaken for the current package-level canonical identity

## Portability Normalization

- workspace-specific absolute links have been removed from the shipped copies
- if a referenced transitive artifact is present in this directory, the local
  markdown link resolves inside the bundle
- if a referenced transitive artifact is not part of the current shipped bundle,
  its target is preserved as provenance-only filename text rather than as a
  broken markdown link

## Energy note

- the frozen Energy-to-policy transition note in this bundle was copied when the
  Energy manuscript package was at `v8`
- the current closed Energy manuscript is now `v26`
- copies of the current `NRR-Patterns v0_29` and current Energy
  `v26` reference artifacts are now also shipped locally
- the bundled `v8` transition snapshot remains historical provenance only
- older upstream review copies corresponding to the earlier integrated release
  and `Energy v11` remain historical
  provenance only if present locally
- the current manuscript-facing spine is not the older local sequence preserved
  in the frozen transition texts; it is `NRR-Patterns -> Energy -> Guarantee`
- those later manuscript-facing upstream changes do not alter the downstream
  support-layer boundaries imported into the current Guarantee manuscript
