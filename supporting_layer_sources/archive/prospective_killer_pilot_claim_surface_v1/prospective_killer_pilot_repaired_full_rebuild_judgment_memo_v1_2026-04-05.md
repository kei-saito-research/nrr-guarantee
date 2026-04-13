# Prospective Killer Pilot Repaired Full Rebuild Judgment Memo v1

## Scope
- decide whether the repaired full behavioral read is already strong enough to keep the rebuild candidate closed as comparison-only
- or whether the remaining repaired-surface residual still justifies opening the rebuild candidate as an active comparison line

## Inputs
- repaired full readout:
  - `/Users/saitokei/Documents/New project/series_planning/prospective_killer_pilot_en_bridge_a2_mode_repair_full_readout_v1_2026-04-05.md`
- repaired full summary:
  - `/Users/saitokei/Documents/New project/series_planning/prospective_killer_pilot_en_bridge_a2_mode_repair_full_summary_v1_2026-04-05.json`
- prior bug-exposure full readout:
  - `/Users/saitokei/Documents/New project/series_planning/prospective_killer_pilot_en_bridge_current_full_readout_v1_2026-04-05.md`
- user-pasted Claude review on `2026-04-05`

## External Review Input
- Claude judgment:
  - `Option 1`
  - keep the repaired line as mainline
- Claude one-line read:
  - the original rebuild trigger was the `DA / nrr` collapse, that collapse is now resolved, and the remaining `LF` residual is not yet strong evidence that a rebuild candidate would change the current runtime decision

## Assistant-Side Evaluation
- decision:
  - `adopt`
- reason:
  - the repaired full run fixes the original rebuild-trigger bottleneck in `DA / nrr` strongly enough that the remaining `LF / nrr` residual reads as a carried residual family, not as current evidence that the rebuild candidate should replace or even automatically reopen the mainline runtime path

## Key Numbers
- overall `final_success_rate`:
  - unrepaired:
    - `0.8024691358024691`
  - repaired:
    - `0.904320987654321`
- `nrr final_success_rate`:
  - unrepaired:
    - `0.4722222222222222`
  - repaired:
    - `0.7685185185185185`
- `DA / nrr final_success_rate`:
  - unrepaired:
    - `0.08333333333333333`
  - repaired:
    - `0.8611111111111112`
- `LF / nrr final_success_rate`:
  - unrepaired:
    - `0.4722222222222222`
  - repaired:
    - `0.5555555555555556`

## Working Read
- the rebuild trigger originally hit because the full unrepaired line showed a family-level `DA / nrr / A2` collapse
- the repaired full run no longer supports reading `DA` as the main blocker
- `LF` remains the main residual family, but its current shape is:
  - partial improvement rather than unchanged collapse
  - still attached to the explicit `LF_002 / gemini / nrr` carry-over residual
  - not yet strong evidence that the rebuild candidate is required as the next runtime action

## Operational Consequence
- keep the repaired `A2` surface as the active English behavioral mainline
- keep the rebuild candidate as:
  - comparison-only
  - closed by default
- do not open a rebuild comparison automatically from assistant momentum

## What This Does Not Yet Decide
- manuscript-facing wording about future `NRR-native` / non-softmax design implication
- whether later manuscript freeze or release-facing routing should seek additional external double-checking on this branch judgment
