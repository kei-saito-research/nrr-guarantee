# Guarantee Completion Gap Assessment v6

Date: 2026-03-20
Status: updated completion-gap read after manuscript `v18`

## Purpose

Record the current manuscript/package state of `Guarantee` without collapsing
`reviewable scaffold` into `completed paper`.

This memo replaces the shorthand read that the current line is already closed at
the normal manuscript level.

## Current state

The current `Guarantee` repository is more than a blank stub, but it is not yet
a normal completed manuscript package.

What currently exists:

- a bounded manuscript draft at
  `manuscript/current/nrr-guarantee_manuscript_v18.tex`
- a committed PDF snapshot at
  `manuscript/current/nrr-guarantee_manuscript_v18.pdf`
- three explicit bounded claim-unit fills in manuscript prose
- one later-horizon failure-boundary section
- one manuscript-native summary table for the current bounded claim surface
- one tested-scope table for the imported evidence surfaces
- one provider-sensitive residual/boundary table
- one manuscript-native source/claim trace table
- section- and table-level traceability for supporting-layer dependencies without treating local memos as bibliography entries
- an initial external prior-work citation pass covering mixed-initiative dialogue, clarification, and grounding
- manuscript wording that no longer relies on the removed series-goal figure
- a minimal formal bibliography tying the line back to the series context
- bundled supporting-layer source files for self-contained review tracing
- executable checksum verification and a review-oriented build wrapper
- external review clearance on the narrow self-contained review package

What this means operationally:

- the current line is a `reviewable scaffold`
- the current line is not yet a `normal completed paper`

## What is not yet complete

The current manuscript still lacks several elements that would normally be
expected before calling the line complete as a paper/package:

1. Normal manuscript apparatus is still only partial.
   - the manuscript now stands without the removed series-goal figure
   - the current tables are enough to make the bounded surface legible
   - the citation layer is improved by an initial external prior-work pass
   - it may still need a more selective final curation pass for reviewer-facing completeness

2. The current manuscript still contains scaffold-era internal completion text.
   - the largest paper-body checklist text is now removed
   - but the package/review sections still retain some scaffold-era framing and
     should be normalized further

3. The repo/package surface is not yet normalized to the claimed current state.
   - `manuscript/current/` is now latest-only at `v14`
   - `papers_fix/guarantee` now exists as the sync target for the current manuscript line
   - repo-facing wording is improved, but some historical memos still reflect
     the earlier overstated closure read

4. Build closure is still review-oriented rather than normal typeset closure.
   - checksum verification passes
   - the documented build path executes
   - but the current environment still falls back to `cupsfilter` after cached
     TeX compile failure, so the line is not yet in a normal "standard TeX build
     passes" state

5. Paper-native evidence presentation is still thinner than the final desired paper form.
   - the repo carries analysis memos and imported support files
   - the manuscript now exposes the three claim units and later-horizon
     boundary through paper-native tables
   - the remaining gap is now mainly whether further provenance detail belongs in
     the paper body or in an appendix/supplement

## Completion judgment

Current judgment:

- `reviewable scaffold`: complete
- `manuscript-complete paper`: not complete
- `git-ready narrow package`: conditionally complete only in the scaffold sense
- `normal release-ready manuscript package`: not complete

Safe one-line read:

- `Guarantee` is currently a review-cleared bounded scaffold, not yet a normal
  completed manuscript.

## Required work

### Required

1. Recast the manuscript from scaffold text into normal paper form.
   - remove internal completion-checklist prose from the paper body
   - rewrite the package section so it reports reproducibility facts rather than
     project-management state
   - sharpen contributions / results / claim-boundary sections into normal paper
     prose

2. Curate the formal reference apparatus for final reviewer-facing economy.
   - keep local supporting-layer dependencies visible through section structure, source/claim trace, and appendix-level provenance rather than bibliography inflation
   - keep only the outside prior work that sharpens positioning and reviewer readability

3. Keep the package surface normalized and finish the remaining mirror/wording cleanup.
   - preserve latest-only `manuscript/current/`
   - maintain the `papers_fix/guarantee` mirror
   - finish replacing any repo-facing wording that still conflates scaffold
     closure with manuscript completion

4. Correct status and repo-facing wording.
   - stop calling the line fully closed at the normal manuscript level
   - explicitly distinguish `scaffold closed` from `manuscript complete`

5. Raise build closure above fallback-only reviewability.
   - either restore a normal TeX build path in the local environment
   - or document a stable non-fallback build environment that is part of the
     intended package definition

6. Decide how much trace detail stays in the paper body versus an appendix/supplement.
   - keep imported-support transparency
   - move memo-like provenance detail out of the main text where that improves readability

### Strongly recommended

1. Add an appendix or supplementary trace note.
   - keep the imported-support transparency
   - move memo-like provenance detail out of the main paper body where possible

### Optional

1. Add one short paragraph clarifying why `Guarantee` is the downstream
   claim-owning line while `Policy`, `Dynamics`, and `Policy-Verification`
   remain supporting layers.

## Experiment judgment

New experiments are not the first missing ingredient.

Current read:

- the biggest gap is manuscript/package completion, not immediate evidence
  absence
- the current line can be made substantially more complete using already-fixed
  evidence

If new experimentation is later chosen, the strongest next candidate is:

- a single `Guarantee`-owned consolidation validation surface that presents the
  three currently supported claim units under one manuscript-native reporting
  scheme

This is stronger than immediately jumping to:

- direct causal ablation of `evaluation during retention`

Reason:

- consolidation validation strengthens the current paper identity
- direct causal ablation risks turning the line into a different paper

## Recommended work order

1. correct the repo/status wording so completion is not overstated
2. rewrite the manuscript from scaffold form into normal paper form
3. decide whether to externalize more trace detail into an appendix while trimming the prior-work set to its strongest final core
4. keep the package surface normalized and maintain `papers_fix/guarantee`
5. reassess whether one consolidation validation experiment is still needed
6. only then reopen the post-`Guarantee` upstream final integration order

## Current next-step read

The immediate task is not post-`Guarantee` upstream integration yet.

The immediate task is:

- complete `Guarantee` as a normal manuscript/package, using the existing
  bounded evidence surface first
