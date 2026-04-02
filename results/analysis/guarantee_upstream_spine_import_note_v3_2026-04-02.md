# Guarantee Upstream Spine Import Note v3

## Status
- Date: 2026-04-02
- Type: repo-local manuscript-facing import note
- Scope: fix the current upstream authority line for the `Guarantee`
  manuscript-facing spine and canonical upstream bibliography identity on the
  current `v54` review line without rewriting the frozen support-layer handoff
  artifacts

## 1. Why This Note Exists

The frozen support-layer bundle still preserves older handoff surfaces created
before the manuscript-facing series spine was reset. Those files remain useful
as provenance for ownership transfer and support-layer vocabulary, but they are
not the current manuscript-facing authority for the upstream sequence used by
the rewritten `Guarantee` line.

## 2. Current Manuscript-Facing Upstream Authority

For the current rewritten `Guarantee` line, read the upstream authority as:
- integrated `paper7`:
  - `paper7_integrated_manuscript_v0_29_2026-04-01.tex`
- current closed `Energy` line:
  - `nrr-energy_manuscript_v26.tex`
- current manuscript-facing spine:
  - `paper7 -> Energy -> Guarantee`

The shipped support bundle now also includes review copies of those current
authority files:
- `supporting_layer_sources/current/paper7_integrated_manuscript_v0_29_2026-04-01.tex`
- `supporting_layer_sources/current/paper7_integrated_manuscript_v0_29_2026-04-01.pdf`
- `supporting_layer_sources/current/paper7_integrated_manuscript_v0_29_transfer_repo_identity_note_v1_2026-04-02.md`
- `supporting_layer_sources/current/nrr-energy_manuscript_v26.tex`
- `supporting_layer_sources/current/nrr-energy_manuscript_v26.pdf`

## 3. Canonical Transfer Repository Identity

For the active `Guarantee v54` review surface, treat the bundled
`paper5-nrr-transfer-v123.tex` snapshot as having one canonical repository
identity:
- canonical repo/tree:
  - `https://github.com/kei-saito-research/hidden-state-interface-reuse/tree/24bd24ea183f282cf535205ca4447e8169bac3b0`

Why this is the package-level authority:
- the protected Transfer authority file for this workspace lives under the
  hidden-state-interface-reuse tree
- the bundled current `Energy v26` authority copy already cites the same
  `paper5-nrr-transfer-v123.tex` snapshot under that tree

Historical-label rule:
- the bundled `paper7 v0_29` review copy still preserves the older
  `nrr-transfer/tree/24bd24ea183f282cf535205ca4447e8169bac3b0` label as
  historical provenance only
- do not read that preserved older label as defining a second upstream
  Transfer identity inside the current `Guarantee` package
- for direct reads of the bundled `paper7` copy, use the shipped sidecar note
  `supporting_layer_sources/current/paper7_integrated_manuscript_v0_29_transfer_repo_identity_note_v1_2026-04-02.md`
  so the package-level canonical identity stays visible next to that review
  copy

## 4. Historical Files That Remain Bundled

The following bundled files remain historical support/handoff provenance only:
- `supporting_layer_sources/current/energy_to_guarantee_program_design_brief_v1_2026-03-17.md`
- `supporting_layer_sources/current/energy_to_policy_handoff_memo_v1_2026-03-18.md`
- `supporting_layer_sources/current/nrr-energy_manuscript_v8.tex`
- `supporting_layer_sources/current/nrr-energy_manuscript_v8.pdf`

Use rule:
- keep those files as frozen provenance
- do not read their older local sequence wording as the current
  manuscript-facing spine
- do not read their `v8` handoff snapshot as replacing the current closed
  `Energy v26` authority line

## 5. Manuscript-Facing Consequence

For the current `Guarantee` manuscript:
- use this note to anchor the Introduction and Program Position spine wording
- use the hidden-state-interface-reuse tree as the current package's canonical
  Transfer repository identity for the shipped `paper5-nrr-transfer-v123.tex`
  snapshot
- use the support bundle for imported policy / dynamics / policy-verification
  layer texts and historical handoff provenance only
