# Changelog for version 2.1.11


## Summary

Version 2.1.11 is a maintenance release with no user-facing changes. The release consists entirely of internal code refactoring and a version bump from 2.1.10.

## New Features

*None*

## Improvements

*None*

## Bug Fixes

*None*

## Internal Changes

This release contains only internal changes that do not affect user-facing functionality:

- **Version bump**: 2.1.10 → 2.1.11
- **Build timestamp**: Updated from `2026-01-17T00:11:03Z` to `2026-01-17T01:19:11Z` (approximately 1 hour later)
- **Code refactoring**: One OAuth metadata discovery helper function (`R42`) was refactored/inlined
- **Re-minification**: 6,293 variable renames from fresh minification pass (internal identifier changes like `FT8` → `KT8`)

Evidence: Diff header shows 99.9% structural similarity with only 17 additions, 18 deletions, and 55 modifications across ~13,000 declarations.

## Notes

This appears to be a quick follow-up release to v2.1.10 released approximately one hour earlier, likely containing minor internal fixes or build adjustments not visible in the minified output.
