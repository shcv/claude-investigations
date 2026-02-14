# Changelog for version 2.0.64

## Highlights
This release contains two minor changes: the official plugins repository URL was updated to match its marketplace name, and screenshot copying now provides a clearer error message when running in builds without embedded font assets.

## New Features

*No new features in this release.*


### Official Plugins Repository Renamed
**What:** The GitHub repository URL for the official plugins marketplace was updated from `anthropics/claude-code-plugins` to `anthropics/claude-plugins-official`.

**Details:**
- This aligns the repository name with the existing marketplace identifier `claude-plugins-official`
- Existing plugin references using the old repository name in documentation may need updating
- **Evidence**: Variable `r70` at line 496527 in v2.0.63 → Variable `e70` at line 496571 in v2.0.64


### Screenshot Copying Build Check
**What:** Screenshot copying now verifies build capabilities before attempting to generate screenshots, providing a clearer error message when the feature is unavailable.

**Details:**
- In builds without embedded font files (non-Bun builds or Bun builds without embedded assets), users will now see: "Screenshot copying is not available in this build"
- Previously, the feature would attempt to run and potentially fail with a less helpful error message
- The core screenshot functionality remains unchanged for supported builds
- **Evidence**: New guard clause in `Ib2()` at lines 483446-483450 in v2.0.64, calling `e5()` build check function at lines 17067-17074

## Internal Changes

This release includes 9,263 internal variable renames due to bundler regeneration. These do not affect functionality and are not user-visible.
