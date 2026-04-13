# Prospective Killer Pilot Manuscript-Facing Claim Memo v1

## Purpose
- fix what the current repaired full prospective-killer pilot can now support as manuscript-facing wording
- separate cleared behavioral claims from supporting mechanistic context
- keep future-architecture wording bounded until a later explicit judgment promotes it

## Current Evidence Base
- repaired full behavioral read:
  - `/Users/saitokei/Documents/New project/series_planning/prospective_killer_pilot_en_bridge_a2_mode_repair_full_readout_v1_2026-04-05.md`
- repaired full summary:
  - `/Users/saitokei/Documents/New project/series_planning/prospective_killer_pilot_en_bridge_a2_mode_repair_full_summary_v1_2026-04-05.json`
- repaired full rebuild judgment:
  - `/Users/saitokei/Documents/New project/series_planning/prospective_killer_pilot_repaired_full_rebuild_judgment_memo_v1_2026-04-05.md`
- sidecar carry-forward read:
  - `/Users/saitokei/Documents/New project/series_planning/prospective_killer_pilot_carry_forward_read_memo_v1_2026-04-05.md`

## Assistant-Side Evaluation
- decision:
  - `partial adopt`
- reason:
  - the paper can now be framed as a bridge from prompt-implemented `NRR` control toward architectural motivation, but the repaired full run does not support writing the current mainline as if prompt-level `NRR` simply works on one turn and then universally collapses on all multi-turn use

## Paper Role
- safe role read:
  - this paper is not merely a prompt-tip note
  - it is a condition-bounded behavioral paper about what current softmax-based LLMs can and cannot sustain when `NRR-style` control is implemented at the prompt level across multiple turns
- safe bridge read:
  - the repaired full run shows that prompt-level `NRR` can materially improve multi-turn behavior under tested conditions
  - but it also leaves a persistent family-level residual in later followthrough
  - together, those two facts support a bounded architectural motivation:
    - prompt-level control can move outcomes substantially
    - yet current turn-wise reconvergence still appears to limit how stably that control is maintained across families and turns
- safe future-facing implication:
  - this makes the line usable as a bridge toward research on more native ambiguity-maintaining or deferred-commitment generation designs
  - it does not yet justify writing that a non-softmax `NRR-native` design is already proved necessary or superior

## Cleared Behavioral Read
- the repaired English bridge `A2` surface is the active behavioral mainline for this pilot
- under the tested English scenario protocol, the repaired full run materially improves the overall `NRR` behavioral outcome relative to the unrepaired full run
- the main repaired gain is in `downstream_acceptance`, where the old `A2` question-only reopening collapse is no longer family-wide
- `early_ambiguity_turn` remains strong after repair and does not show a material transfer-loss penalty
- `later_followthrough` improves only partially and remains the main residual family

## Key Numbers Safe To Cite
- overall `final_success_rate`:
  - unrepaired full run:
    - `0.8024691358024691`
  - repaired full run:
    - `0.904320987654321`
- `NRR final_success_rate`:
  - unrepaired:
    - `0.4722222222222222`
  - repaired:
    - `0.7685185185185185`
- `DA / nrr final_success_rate`:
  - unrepaired:
    - `0.08333333333333333`
  - repaired:
    - `0.8611111111111112`
- `EA / nrr final_success_rate`:
  - unrepaired:
    - `0.8611111111111112`
  - repaired:
    - `0.8888888888888888`
- `LF / nrr final_success_rate`:
  - unrepaired:
    - `0.4722222222222222`
  - repaired:
    - `0.5555555555555556`

## Residuals That Must Stay Attached
- explicit behavioral residual:
  - `LF_002 / gemini / nrr`
- required read:
  - this remains a carried-over `A1` miss on the stay-vs-switch axis
  - it stays inside the scored aggregate
  - it should be flagged explicitly rather than excluded
- family-level residual read:
  - `LF` remains the main remaining repaired-surface bottleneck
  - do not write as if the repaired line is uniformly clean across all families

## Sidecar Placement
- the `Gemini-only logprobs` artifacts are mechanistic sidecar evidence only
- they may support a statement that the repaired `A2` surface changes early decoding tendencies in a way that aligns with the observed behavioral repair
- they do not replace the behavioral pilot
- they should not be written as provider-balanced proof

## Cleared Claim Shape
- safe direct-result shape:
  - under tested conditions, `NRR-style` control changes behavioral output quality on the repaired English bridge line
- safe mechanistic shape:
  - the behavioral change is consistent with a change in where turn-wise generation tends to re-converge, rather than with a claim that `NRR` stops re-convergence itself
- safe architecture-bridge shape:
  - the current results are consistent with reading prompt-level `NRR` as partially effective but structurally limited on present turn-wise generation mechanisms
  - this supports a bounded research motivation for more native generation designs that handle ambiguity maintenance and deferred commitment more directly
- safe limitation shape:
  - the repaired pilot supports a bounded behavioral claim with explicit residuals, not a universal replacement claim

## Safe Short Form
- repaired full run materially improves the `NRR` line, mainly by closing the old `DA / nrr / A2` collapse
- `EA` remains strong
- `LF` remains the main residual family, with `LF_002 / gemini / nrr` attached as the explicit carried-over miss
- `Gemini-only logprobs` remains supporting mechanistic context, not replacement evidence
- the paper can therefore point toward architectural motivation, but only in bounded `suggests / motivates` language

## Prose Candidates
- English:
  - `Under the tested English scenario protocol, the repaired NRR bridge line materially improves behavioral outcomes relative to the unrepaired full run, primarily by removing the earlier downstream-acceptance A2 collapse while preserving strong early-ambiguity-turn performance.`
- English:
  - `The remaining limitation is later followthrough rather than downstream acceptance: the repaired line improves that family only partially, and the explicit LF_002 / gemini / nrr A1 residual remains inside the scored set.`
- English:
  - `Taken together, these results support reading prompt-level NRR as materially effective but still structurally limited on current turn-wise reconverging generation, which in turn motivates investigation of more native ambiguity-maintaining and deferred-commitment generation designs.`
- Japanese:
  - `英語版のrepaired full runでは、未修正full runに対して behavioral outcome が有意に改善し、主改善点は downstream acceptance における旧来の A2 崩れの解消である。`
- Japanese:
  - `一方で later followthrough は部分改善に留まり、LF_002 / gemini / nrr の明示的 residual を含め、なお主残差として保持する必要がある。`
- Japanese:
  - `したがって本結果は、prompt-level の NRR 実装が現行の各ターン再収束型生成の上でも有意な改善を与えうる一方、その安定維持にはなお構造的限界が残ることを示す条件付きの橋渡し結果として読める。`

## Not Yet Cleared
- do not write as if the current repaired mainline simply `works on one turn and collapses on multiple turns`
- do not write as if the repaired full run proves that every remaining failure is directly caused by `softmax` alone
- do not yet write as if the current evidence proves a future non-softmax `NRR-native` architecture
- do not yet write as if sidecar evidence by itself establishes semantic ambiguity retention
- do not yet write as if the repaired line removes all meaningful `LF` failure risk

## Future-Architecture Hold
- preserve this as a hold item rather than cleared manuscript text:
  - the current result may support a bounded design implication that ambiguity maintenance and deferred commitment deserve more native architectural treatment than ordinary turn-wise reconvergence provides
- preserve this stronger-but-still-bounded role sentence as draft-hold material:
  - present softmax-based LLMs can be pushed toward `NRR-style` behavior at the prompt level, but the remaining multi-turn fragility suggests that a more native generation mechanism may ultimately be needed for stable ambiguity maintenance across turns
- if used later, keep it as:
  - a plausible research direction
  - not established proof
  - not guaranteed superiority claim
