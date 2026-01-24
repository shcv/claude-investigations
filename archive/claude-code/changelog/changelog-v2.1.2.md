# Changelog for version 2.1.2


## Summary

This release adds a new permission explainer feature that shows risk assessments for tool actions, improves git commit attribution handling for `--amend` operations, and removes the experimental bash output summarization system. It also adds winget installation detection on Windows, better image validation, and fixes for transient git states during commit attribution.

### Permission Explainer [Gradual Rollout]

**What**: A new feature that analyzes tool use requests and displays risk assessments (LOW/MEDIUM/HIGH) with explanations when Claude requests permissions.

**Details**:
- Evaluates commands before execution and categorizes risk levels
- LOW risk: Standard dev workflows (git operations, tests, installs, builds)
- MEDIUM risk: Bulk deletions, complex shell pipelines, config modifications
- HIGH risk: Dangerous or irreversible operations, system-level changes
- Only displays warnings for MEDIUM and HIGH risk actions
- Controlled by `tengu_permission_explainer` feature flag
- Can be enabled via `PERMISSION_EXPLAINER_ENABLED=true` environment variable

**Evidence**: `Hu2()` at line 417436 (permission explainer generator, contains `"tengu_permission_explainer"`)

### Windows Winget Installation Detection

**What**: Claude Code now detects when it was installed via Windows Package Manager (winget) for better installation source tracking.

**Details**:
- Detects winget installations by checking execution path patterns
- Recognizes `Microsoft\WinGet\Packages` and `Microsoft\WinGet\Links` paths
- Installation source now reports "winget" instead of "unknown" on Windows

**Evidence**: `KF0()` at line 370058 (winget detection, contains `/Microsoft[/\\]WinGet[/\\]Packages/i`)

### Improved Git Commit Attribution for Amends

**What**: Git commit attribution now properly handles `git commit --amend` operations by recalculating and replacing existing Claude trailers.

**Details**:
- Detects when a commit command includes `--amend`
- Strips existing Claude attribution trailers before recalculating
- Properly replaces `Claude-Generated-By`, `Claude-Steers`, `Claude-Permission-Prompts`, `Claude-Escapes`, and `Claude-Plan` fields
- Prevents duplicate or stale attribution data in amended commits

**Evidence**: `v$7()` at line 531681 (amend attribution handler, contains `"--amend"` detection and trailer replacement)

### Transient Git State Detection

**What**: Commit attribution now skips processing during transient git states to prevent interference with ongoing operations.

**Details**:
- Detects rebase, merge, cherry-pick, and bisect operations
- Checks for `.git/rebase-merge`, `.git/rebase-apply`, `.git/MERGE_HEAD`, `.git/CHERRY_PICK_HEAD`, `.git/BISECT_LOG`
- Prevents attribution from running during these incomplete states

**Evidence**: `_RB()` at line 226382 (transient state checker, contains `".git/rebase-merge"`)

### Image Size Validation

**What**: Validates image sizes before sending to the API and provides clear error messages when images exceed limits.

**Details**:
- Checks base64-encoded image sizes against API limits
- Provides human-readable size information (KB/MB) in error messages
- Reports which specific images are too large when multiple exceed limits
- Suggests resizing images before sending

**Evidence**: `urB()` at line 278763 (image validator, contains `"exceeds API limit"`)

### Bash Security Check for Malformed Token Injection

Commands with ambiguous syntax containing command separators (`;`, `&&`, `||`) combined with unbalanced brackets, parentheses, or quotes now trigger permission prompts to prevent potential injection attacks.

**Evidence**: `_j5()` at line 366196 (security checker, contains `"MALFORMED_TOKEN_INJECTION"`)

### Windows Managed Settings Migration Warning

Users on Windows with managed settings in the deprecated `C:\ProgramData\ClaudeCode\` location now see a warning notification to contact their administrator about migrating to `C:\Program Files\ClaudeCode\`.

**Evidence**: `K89()` at line 475350 (deprecation warning, contains `"ProgramData\\ClaudeCode\\managed-settings.json"`)

### Enhanced Plugin Management UI

The plugin management interface has been refactored with improved state handling, better MCP server grouping under parent plugins, and clearer status indicators for pending operations.

**Evidence**: `gK9()` at line 512088 (plugin manager, contains `"pendingToggle"`)

## Bug Fixes

- Removed experimental bash output summarization feature that could cause inconsistent output handling (`j22()` at line 299915, contained `"bash_output_summarization"`)
- Removed `tengu_tool_result_persistence` feature flag and associated tool result truncation logic that was gated behind it (`V71()` at line 294547)
- Removed background plan verification agent (`VerifyPlanExecution`) that ran automatically after plan completion (`i39()` at line 474724)
- Fixed plan mode tracking to properly count user prompts since plan exit (`Zp5()` at line 403780)

### Custom Environment Variables Warning

**What**: Infrastructure added to detect and warn about custom environment variables in project/local settings.

**Status**: Code exists but appears to be internal validation only.

**Details**:
- Maintains an allowlist (`i9A`) of known/safe environment variable names
- Can detect when project settings contain non-allowlisted env vars
- Function `iC9()` returns list of settings files with custom env vars

**Evidence**: `uC9()` at line 530822 (env validator, checks against `i9A` allowlist)

## Notes

The bash output summarization feature has been completely removed. If you relied on the automatic summarization of verbose command output, you may see more raw output in tool results. The feature was experimental and gated behind feature flags.
