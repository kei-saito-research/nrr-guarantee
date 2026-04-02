# Energy Priority-Resolution Downstream Acceptance Two-Provider Read Memo v1

## Status
- Date: 2026-03-17
- Type: two-provider read memo
- Scope: summarize the current two-provider read after paired downstream-acceptance comparisons on Anthropic and Gemini
- Depends on:
  - `energy_priority_resolution_downstream_acceptance_baseline_vs_nrr_comparison_memo_v1_2026-03-17.md`
  - `energy_priority_resolution_downstream_acceptance_gemini_baseline_vs_nrr_comparison_memo_v1_2026-03-17.md`
- Not a manuscript claim memo

## 1. What This Line Carries
Under the current scope, this line now carries a real two-provider downstream episode read at the level of:
1. measurement
   - one frozen accepted-direction handoff metric family
2. control
   - same templates, same acceptance variants, same episode unit, same arm split
3. verification
   - retained arm-specific raw, response, summary, annotation, and comparison artifacts

This line still does not carry:
- broader conversation-policy validity
- longer-horizon outcome closure
- manuscript-facing Guarantee closure

## 2. Aggregate Two-Provider Read

| provider | baseline `appropriate = 1` | NRR `appropriate = 1` | delta |
|---|---:|---:|---:|
| Anthropic | 0 / 24 | 24 / 24 | +24 |
| Gemini | 0 / 24 | 10 / 24 | +10 |

Supplementary metric split:

| provider | baseline `accepted_direction_followthrough_present = 1` | NRR `accepted_direction_followthrough_present = 1` | baseline `preacceptance_rework_burden_absent = 1` | NRR `preacceptance_rework_burden_absent = 1` |
|---|---:|---:|---:|---:|
| Anthropic | 24 / 24 | 24 / 24 | 0 / 24 | 24 / 24 |
| Gemini | 14 / 24 | 10 / 24 | 0 / 24 | 24 / 24 |

## 3. Current Best Read
Shared gain across both providers:
- baseline leaves preacceptance burden on all tested rows
- NRR removes that burden on all tested rows

Provider-specific split:
- Anthropic:
  - downstream followthrough also stays clean after acceptance
  - result: `24 / 24`
- Gemini:
  - preacceptance burden is removed
  - but downstream followthrough after acceptance is often too generic
  - result: `10 / 24`

Operational interpretation:
- the line does reproduce a real cross-provider gain on the measurement that motivated the downstream episode cut
- but the full downstream handoff effect is provider-sensitive

## 4. Failure Modes To Keep Explicit
1. baseline failure mode:
   - starts work before the user accepts a direction
2. Gemini NRR residual failure mode:
   - preserves the acceptance boundary, then stops at a generic acknowledgment instead of beginning useful accepted-direction work
3. strongest provider-specific weak region:
   - `C_incident_response` on Gemini NRR:
     - `appropriate = 0 / 8`

## 5. Boundary
This two-provider read does not justify:
- manuscript-facing Guarantee closure
- a claim that the current downstream handoff operator is provider-balanced in the strong sense
- rerunning this line after outcome inspection

## 6. Assistant-Side Read
- overall judgment:
  - `adopt`
- reason:
  - the line now has a real two-provider read that reports both gains and concrete provider-specific failure modes under a frozen protocol
- next honest read:
  - the downstream acceptance line is no longer Anthropic-only, but it ends as a mixed two-provider result rather than a clean provider-balanced closure
