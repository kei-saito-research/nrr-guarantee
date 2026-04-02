# Guarantee Upstream Spine Import Note v2

## Status
- Date: 2026-04-02
- Type: repo-local manuscript-facing import note
- Scope: fix the current upstream authority line for the `Guarantee`
  manuscript-facing spine without rewriting the frozen support-layer handoff
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
- `supporting_layer_sources/current/nrr-energy_manuscript_v26.tex`
- `supporting_layer_sources/current/nrr-energy_manuscript_v26.pdf`

## 3. Historical Files That Remain Bundled

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

## 4. Manuscript-Facing Consequence

For the current `Guarantee` manuscript:
- use this note to anchor the Introduction and Program Position spine wording
- use the support bundle for imported policy / dynamics / policy-verification
  layer texts and historical handoff provenance only
