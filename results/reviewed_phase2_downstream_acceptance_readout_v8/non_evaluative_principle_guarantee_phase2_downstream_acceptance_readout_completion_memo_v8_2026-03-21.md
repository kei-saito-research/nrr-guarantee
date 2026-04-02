# 非評価原理 Guarantee Phase 2 downstream acceptance readout completion memo v8

日付: 2026-03-21
状態: assistant-side repaired / external review pending
依存:
- `non_evaluative_principle_guarantee_phase2_downstream_acceptance_readout_review_decision_memo_v3_2026-03-21.md`
- `nrr-energy/scripts/build_guarantee_phase2_downstream_acceptance_readout_v1.py`

## 1. Purpose

This memo records the repaired Phase 2 downstream-acceptance readout after the
shared-box `v7` artifact was held on the narrow blocker that the review-pack
instructions still mixed the older provider-balanced `inconclusive` headline
with the repaired truthful provider-first mixed read.

## 2. Repair Applied

Pack repair:
- keep the already-repaired scoring-layer separation intact
- keep the already-repaired artifact-local packed provenance
- preserve the bundled-source rebuild path and
  `canned_step2_assistant_turn`-only manipulation checks
- align `00_START_HERE.md`, `01_REVIEW_REQUEST.md`, and `02_PACKAGE_SCOPE.md`
  to the same truthful current provider-first read:
  - `Anthropic = inconclusive`
  - `Gemini = support`
  - overall `mixed`

Verification:
- repo-side execution still succeeds
- pack-local execution succeeds from bundled `CURRENT/source_bundles/`
- previously cited false negatives still score `appropriate = 1`
- shipped annotation outputs still preserve row-level separation between
  `appropriate` and `accepted_branch_followthrough_present`
- packed annotation CSV `source_outdir` values still remain artifact-local
- packed comparison memo still lists bundled source paths as artifact-local
  `CURRENT/source_bundles/...`
- the manipulation-check table still reports:
  - ablation non-compliance `0 / 144` in both providers
  - baseline / NRR contamination `0 / 144` in both providers
- those zeros still come from the frozen canned turn itself rather than an
  arm-label shortcut
- the packaged comparison memo is regenerated inside the bundled `CURRENT/`
  surface
- the excluded raw-only history artifact is bundled for provenance only and
  remains excluded from all decisive downstream tables
- the review-pack instructions now ask reviewers to judge only the repaired
  truthful current read, not the older provider-balanced `inconclusive`
  headline

## 3. Current Read

The repaired read remains:
- Anthropic provider read:
  - `inconclusive`
- Gemini provider read:
  - `support`
- provider-first overall read:
  - `mixed`

This repaired review surface preserves the prior `v7` scoring fixes while
making the review target internally consistent. The provider-first read is:
- Anthropic remains `inconclusive`
- Gemini reaches `support`

## 4. Assistant-Side Decision

- judgment:
  - `adopt`
- reason:
  - the repaired readout now closes the `appropriate` scoring-contract blocker
    while keeping the bundled surface internally consistent and truthful to the
    repaired scoring rule and repaired current read

## 5. Next Action

Next action:
 - send repaired readout artifact `v8` to shared-box review
 - do not close external review until the repaired `v8` artifact is reviewed as
  the new latest-only target
