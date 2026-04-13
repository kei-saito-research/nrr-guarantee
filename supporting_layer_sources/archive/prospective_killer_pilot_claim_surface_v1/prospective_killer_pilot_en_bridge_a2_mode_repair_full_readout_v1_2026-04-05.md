# Prospective Killer Pilot English Bridge A2 Mode Repair Full Readout v1

## Surface
- prompt bundle:
  - `/Users/saitokei/Documents/New project/series_planning/prospective_killer_pilot_prompt_bundle_en_bridge_a2_mode_repair_v1_2026-04-05.json`
- manifest:
  - `/Users/saitokei/Documents/New project/series_planning/prospective_killer_pilot_run_manifest_en_bridge_current_v1_2026-04-05.csv`
- runtime outputs:
  - `/Users/saitokei/Documents/New project/tmp/prospective_killer_pilot_en_bridge_a2_mode_repair_full_run_001/prospective_killer_smoke_responses_v1.csv`
  - `/Users/saitokei/Documents/New project/tmp/prospective_killer_pilot_en_bridge_a2_mode_repair_full_run_001/prospective_killer_smoke_raw_v1.jsonl`
  - `/Users/saitokei/Documents/New project/tmp/prospective_killer_pilot_en_bridge_a2_mode_repair_full_run_001/prospective_killer_smoke_summary_v1.json`
- scoring and summary:
  - `/Users/saitokei/Documents/New project/series_planning/prospective_killer_pilot_en_bridge_a2_mode_repair_full_scoring_v1_2026-04-05.csv`
  - `/Users/saitokei/Documents/New project/series_planning/prospective_killer_pilot_en_bridge_a2_mode_repair_full_summary_v1_2026-04-05.json`

## Findings First
- the repaired full run closes the old `DA / nrr / A2` collapse as a family-wide failure:
  - `DA / nrr final_success_rate=0.861`
  - prior promoted current-line read:
    - `0.083`
  - `DA` family problematic runs drop:
    - `35/108 -> 7/108`
- `EA` remains strong after the repair rather than paying a transfer-loss tax:
  - `EA final_success_rate=0.954`
  - prior:
    - `0.944`
  - `EA / nrr final_success_rate=0.889`
  - prior:
    - `0.861`
- `LF` improves, but only partially:
  - `LF final_success_rate=0.824`
  - prior:
    - `0.787`
  - `LF / nrr final_success_rate=0.556`
  - prior:
    - `0.472`
  - `LF` remains the largest repaired-surface residual family with:
    - `problematic_runs=19/108`

## Full-Run Quantitative Read
- overall:
  - `n_runs=324`
  - `final_success_rate=0.904`
  - prior:
    - `0.802`
  - `a2_in_envelope_rate=0.910`
  - prior:
    - `0.809`
  - `a1_appropriateness_pass_rate=0.630`
  - prior:
    - `0.627`
  - `premature_commit_rate=0.352`
  - prior:
    - `0.352`
  - `problematic_runs=31`
  - prior:
    - `64`
- by arm:
  - `baseline`: `final_success_rate=1.000`, `problematic_runs=0`
  - `always_defer`: `final_success_rate=0.944`, `problematic_runs=6`
  - `nrr`: `final_success_rate=0.769`, `problematic_runs=25`
  - prior `nrr`:
    - `final_success_rate=0.472`, `problematic_runs=57`
- by provider:
  - `anthropic`: `final_success_rate=0.938`, `problematic_runs=10`
  - prior:
    - `0.827`, `28`
  - `gemini`: `final_success_rate=0.870`, `problematic_runs=21`
  - prior:
    - `0.778`, `36`

## Comparison To Prior Full Current-Line Read
- the main repaired gain is exactly where the bug-exposure read said it should be:
  - `DA / nrr` no longer fails mainly by question-only `A2` reopening after accepted direction
- `EA` does not regress materially under the repaired runtime surface:
  - the bridge transfer remains strong
- `LF / nrr` is better, but it is not yet promoted from `residual` to `fully clean`:
  - the family still carries mixed later-followthrough friction after repair

## Known Residual Handling
- the explicit carried-over residual remains:
  - `LF_002 / gemini / nrr`
- in the repaired full run, both rows still show the same `A1` miss:
  - `LF_002__gemini__nrr__rep1`
  - `LF_002__gemini__nrr__rep2`
- working read:
  - `A1` still asks `budget vs schedule`
  - instead of asking the actual stay-vs-switch branch axis
- these rows stay inside the main scored aggregate and should be flagged in later summaries rather than excluded

## Scoring Note
- this read uses `assistant_side_row_level_envelope_read_v1` on the repaired full bridge-current run
- the scorer is the same assistant-side rubric judge used on the prior full current-line read
- therefore repaired-vs-unrepaired comparisons are directionally meaningful for the two runtime surfaces

## Working Judgment
- the repaired full run strongly supports keeping the repaired `A2` surface as the active behavioral mainline
- the old `DA` bottleneck is no longer the dominant blocker
- the remaining main bottleneck is now:
  - `LF`, especially `LF / nrr`
- this is enough to move the line out of `runtime execution pending`
- but the next move is no longer mechanical:
  - whether this repaired full read is already sufficient to hold the rebuild candidate at comparison-only
  - or whether a rebuild comparison should still be opened
- treat that next move as a user-visible judgment gate rather than as an automatic continuation
