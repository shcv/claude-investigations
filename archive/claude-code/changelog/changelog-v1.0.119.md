# Changelog for version 1.0.119

## Highlights

Version 1.0.119 is a maintenance release focused on code quality improvements and internal refactoring. This release includes dependency updates (AWS Bedrock SDK reorganization) and error handling consistency improvements, with no user-facing feature changes or behavioral modifications.


### Code Quality Enhancements

**Error Constructor Consistency** - Standardized error handling throughout the codebase by converting legacy `Error()` calls to modern `new Error()` constructor syntax at multiple locations, improving consistency with JavaScript best practices.

Evidence: Changes in error handling patterns across multiple tool implementations, including BashOutput tool at line ~392500, SlashCommand tool at line ~395000, and KillShell tool at line ~398000 in v1.0.119.


### Dependency Updates

**AWS Bedrock SDK Module Reorganization** - Updated the bundled AWS Bedrock SDK client code, restructuring internal module exports and removing obsolete helper functions (`Nl1` at line 5314, `Wh0` at line 5387, `HoA` module at line 119576 in v1.0.118). The Bedrock SDK module was reorganized with updated command mappings and filter configurations, maintaining the same functionality while improving internal structure.

Evidence: Large module `HoA` removed from v1.0.118 and replaced with reorganized exports in v1.0.119. Commands like `CreateCustomModelCommand`, `ListFoundationModelsCommand`, and related Bedrock operations were restructured but retain identical functionality.


### Code Refactoring

**Function Extraction** - Refactored several large functions by extracting inline rendering logic into dedicated helper functions. For example:
- Read tool's rendering methods (formerly inline at line 383796 in v1.0.118) were extracted to separate functions (`w9B`, `q9B`, `E9B`, `N9B`, `L9B` at lines 381255+ in v1.0.119)
- ListMcpResources tool's rendering methods (formerly at line 393109 in v1.0.118) were similarly extracted (lines 392611+ in v1.0.119)

This improves code maintainability and readability without changing any user-visible behavior.

Evidence: Function `UA5` renamed to `OB5` and signature changed from `UA5()` to `OB5(A)` at line 401172 in v1.0.119, though both return empty arrays. Multiple rendering functions extracted from inline implementations in tool definitions.

## Notes

- **No Breaking Changes**: This release contains no breaking changes
- **No New Features**: No new commands, flags, or user-facing functionality added
- **No Bug Fixes**: No user-reported bugs were fixed in this release
- **Structural Similarity**: 98.5% code similarity with v1.0.118, confirming this is primarily a refactoring release
