# Guarantee External Review Resolution v2

## Purpose

Record the follow-up package fix after confirmatory re-review on the revised
`v8` self-contained package.

## Trigger

- confirmatory Codex re-review accepted the `v8` manuscript-level fixes but still
  found a package issue:
  - the bundled `supporting_layer_sources/current/` surface still contained
    workspace-only or missing-target links inside copied upstream source files

## Applied fix

- expanded `supporting_layer_sources/current/` beyond the first imported layer so
  the current review path can resolve its local transitive references
- copied the Energy `v8` manuscript artifacts referenced by the handoff memo into
  the same bundle
- normalized shipped upstream copies so workspace-specific absolute paths are
  removed
- kept locally shipped targets as local markdown links
- converted any remaining non-shipped transitive targets into provenance-only
  filename text rather than leaving broken markdown links behind

## Result

- the shipped support bundle now contains no workspace-only paths
- local markdown links inside the shipped bundle no longer point to missing files
- direct manuscript review, evidence import tracing, and source-bundle inspection
  can all proceed from the delivered artifact without following broken in-bundle
  links

## Remaining gate

- rerun the package verify/build checks on the updated shipped surface
- refresh the external review pack and shared-box zip with the normalized source
  bundle
