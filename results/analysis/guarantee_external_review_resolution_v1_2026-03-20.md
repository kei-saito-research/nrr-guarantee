# Guarantee External Review Resolution v1

## Purpose

Record the concrete changes applied after the first independent Codex and Claude
review pass on the `v7` Guarantee package.

## Resolved issues in `v8`

- self-contained reviewability:
  - the repository now ships a local supporting-layer source bundle under
    `supporting_layer_sources/current/`
  - future review zips must preserve the repository root layout so the shipped
    `scripts/build_current_manuscript.sh` and
    `scripts/verify_current_package.sh` entrypoints remain executable
- evidence-import traceability:
  - the manuscript's evidence-import section now states that the cited support
    files are shipped in-package
  - `reproducibility.md` now points to local bundled copies instead of external
    workspace-only paths
- second claim-unit boundary wording:
  - manuscript `v8` now states directly that the second unit is supported only
    on `preacceptance_rework_burden_absent`
  - the remaining scored fields are retained for boundary reporting rather than
    as separately supported downstream behaviors
- Energy handoff version note:
  - the bundled `energy_to_policy_handoff_memo_v1_2026-03-18.md` is retained as
    an ownership-boundary trace
  - `v8` notes that the memo was frozen against Energy manuscript `v8`, while
    the currently closed Energy package is `v9`, with no downstream boundary
    change imported into Guarantee from that revision
- later-horizon wording:
  - the boundary section now opens from the negative constraint first
  - limited next-checkpoint persistence is reported only to locate failure onset,
    not as a fourth supported claim unit
- package integrity:
  - checksum coverage now includes the current working draft, repo metadata,
    executable review scripts, analysis memos supporting the current claim fills,
    and the bundled support-layer source files
  - no `-e` checksum residue is present in the current local package surface
- discussion/conclusion wording:
  - unauthorized `comparative evaluation pressure` wording was removed
  - conclusion no longer refers to `more review-readable prose`

## Remaining gate

- rerun independent Codex and Claude review on the revised self-contained `v8`
  package
- if that re-review is clean, close the git-ready package surface
