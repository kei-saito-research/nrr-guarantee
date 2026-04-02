# Guarantee behavior-first provider-pair rerun bundle audit note v6

## Status
- Date: 2026-03-31
- Type: supporting-layer audit note
- Scope: provide a shipped local audit path for the bounded behavior-first
  paragraph carried by `nrr-guarantee_manuscript_v45.tex`
- Not a supported-claim memo
- Supersedes:
  - `guarantee_behavior_first_provider_pair_rerun_bundle_audit_note_v5_2026-03-31.md`

## 1. Shipped Direct Audit Basis

The current bundle now carries the exact local surfaces needed to inspect the
bounded behavior-first paragraph without relying on prose-only restatement:

- exact frozen source rows:
  - `guarantee_behavior_first_provider_pair_rerun_v1/non_evaluative_principle_guarantee_behavior_first_provider_local_exact_design_source_rows_anthropic_v1_2026-03-24.csv`
  - `guarantee_behavior_first_provider_pair_rerun_v1/non_evaluative_principle_guarantee_behavior_first_provider_local_exact_design_source_rows_gemini_v1_2026-03-24.csv`
- copied provider-pair rerun outputs:
  - `guarantee_behavior_first_provider_pair_rerun_v1/guarantee_behavior_first_provider_local_20260323T211444Z_anthropic_implementation/`
  - `guarantee_behavior_first_provider_pair_rerun_v1/guarantee_behavior_first_provider_local_20260323T211444Z_anthropic_ablation/`
  - `guarantee_behavior_first_provider_pair_rerun_v1/guarantee_behavior_first_provider_local_20260323T211444Z_gemini_implementation/`
  - `guarantee_behavior_first_provider_pair_rerun_v1/guarantee_behavior_first_provider_local_20260323T211444Z_gemini_ablation/`
- shipped scored read tables:
  - `guarantee_behavior_first_provider_pair_rerun_v1/guarantee_behavior_first_provider_pair_row_scored_read_table_v1_2026-03-31.csv`
  - `guarantee_behavior_first_provider_pair_rerun_v1/guarantee_behavior_first_provider_pair_summary_counts_v1_2026-03-31.csv`

Inside each copied output root, the bundle ships:
- `guarantee_rewritten_nrr_small_test_summary_v1.json`
- `guarantee_rewritten_nrr_small_test_responses_v1.csv`
- `guarantee_rewritten_nrr_small_test_raw_v1.jsonl`

For current package review, the scored row table, summary counts, and response
CSVs are the primary local audit surface; the raw JSONL files remain execution
provenance.

## 2. Bounded Auditable Read

The current manuscript uses this shipped surface only for the following narrow
behavior-first read:

- implementation remains in direct relation work on `8 / 10` provider-pair rows
- the two softer implementation rows are `Gemini D1` and `Gemini D5`
- ablation opens with comparison framing on all `10 / 10` provider-pair rows
- the ablation realization is still compressed:
  - `8 / 10` rows read as `opening comparison -> follow-up question`
  - `2 / 10` rows read as `opening comparison -> direct step`
- the clearest single-row collapse remains Anthropic `D2`, which is retained as
  the manuscript's visible `1 / 10` limitation row

These are the only current package conclusions authorized from this shipped
behavior-first surface.

## 3. Current Manuscript Use / Non-Use

Current manuscript use:
- bounded behavioral-separation evidence only
- visible support that repaired opening-comparison insertion changes the first
  move on the tested provider pair
- visible limitation that the manipulated form remains compressed and includes a
  single clear collapse row

Current manuscript non-use:
- no supported `Guarantee` claim unit
- no downstream-boundary surface
- no pair-level continuation-quality superiority claim
- no clean two-stage realization claim

## 4. Practical Consequence

The current `Guarantee` package is auditable on this behavior-first paragraph
only if review stays on the shipped source rows, copied provider-pair rerun
outputs, and the scored read tables listed above, and only if the paragraph
remains in this bounded secondary role.
