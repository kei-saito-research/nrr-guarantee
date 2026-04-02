# Energy to Guarantee Program Design Brief v1

## Purpose
This brief fixes the current program-level read for the path from `Energy` to `Guarantee`.
It is meant to be the shortest handoff artifact that another Codex can read without reconstructing the recent thread.

## Program Goal
Core から Guarantee までで成立させるのは、
「位置依存同一性を一次原理にした枠組みを、条件付き有効性の工学プログラムとして
実装・品質計測・運用制御・検証まで閉じること」である。

## Layer Roles
- `Energy` = quality measurement
- `Policy` = minimal action specification that turns Energy judgments into explicit behavior rules
- `Dynamics` = description of how the policy holds or degrades across multiple turns
- `Policy-Verification` = pilot-scale forward validation of `baseline vs Energy policy`
- `Guarantee` = bounded claim under explicit provider / family / horizon / observability conditions

## Main Sequence
`Energy -> Policy -> Dynamics + Policy-Verification -> Guarantee`

## Ownership Clarification
- `baseline vs Energy policy` is not an `Energy` calibration experiment.
- Its primary ownership is `Policy-Verification`.
- In the series, it still functions as the first forward step that follows the completed `Energy` package.

## Design Constraint
`Policy-Verification` does not need to be large-scale.
It can remain pilot-scale if:
- provider / family / metric are frozen in advance
- the selected conditions are explicit
- the claim is kept narrow
- the later `Guarantee` text is bounded to exactly those conditions

## What Comes Next
1. `Energy -> Policy` handoff memo
2. `Policy` minimal spec
3. `Policy-Verification` pilot protocol
4. `Guarantee` claim schema

## Reading Rule
The five layer labels alone are not enough.
Any review or next-thread handoff should carry, at minimum:
- the main sequence
- the ownership clarification for `baseline vs Energy policy`
- the four concrete next artifacts
