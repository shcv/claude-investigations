# Changelog for version 2.0.68

## Highlights

This release adds security hardening for shell commands that access sensitive environment variables, improves the plan mode UX with cleaner empty plan handling, and introduces support for sandbox permission requests in swarm/teammate workflows. The release also includes various quality-of-life improvements to text input word navigation and the session resume UI.


### Security Check for /proc/*/environ Access
**What:** Commands attempting to access `/proc/*/environ` paths now trigger an explicit permission prompt, protecting against potential exposure of sensitive environment variables.
**Evidence:** `NC8()` function at line 371017 in v2.0.68
**Details:**
- Commands matching `/proc/*/environ` patterns are detected and flagged
- Users are prompted with a warning: "Command accesses /proc/*/environ which could expose sensitive environment variables"
- Adds telemetry event `tengu_bash_security_check_triggered` for security auditing


### Sandbox Permission Requests for Swarm Workers
**What:** Workers in swarm/teammate mode can now request sandbox network permissions (e.g., host access) from the team lead through the mailbox system.
**Evidence:** `sandbox_permission_request` and `sandbox_permission_response` message types at lines 355577-355652
**Details:**
- New message types: `sandbox_permission_request` and `sandbox_permission_response`
- Workers can request network access to specific hosts
- Team leads see prompts like "{workerName} needs network access to {host}"
- Responses are routed back through the mailbox polling system


### 2M Token Context Window Support
**What:** Added support for models with 2 million token context windows.
**Evidence:** `sN()` function at line 1996 in v2.0.68
**Details:**
- Models tagged with `[2m]` now return a 2,000,000 token context limit
- Previous support existed for `[1m]` (1 million) and default (200,000)


### Tool Deny Rules in Settings
**What:** New capability to completely disable specific tools via settings rules.
**Evidence:** `S_A()` function at line 451689
**Details:**
- Tools can be filtered out when a deny rule exists with no `ruleContent`
- Allows administrators to disable tools entirely for security or compliance


### Plan Mode Empty Plan Handling
**What:** When exiting plan mode without having written a plan, users now see a simplified confirmation dialog instead of the full plan approval UI.
**Evidence:** `Z32()` function at line 394174
**Details:**
- New "Exit plan mode?" dialog appears when plan content is empty or whitespace-only
- Cleaner UX with just "Yes/No" options instead of the full workflow
- Message displayed shows "Exited plan mode" for clarity


### Word Navigation Using ICU Word Boundaries
**What:** Text input word navigation (w, b, e in vim mode) now uses proper Unicode word boundary detection.
**Evidence:** Class `O3` at line 171232 - `getWordBoundaries()` method
**Details:**
- Replaced character-by-character word detection with `Intl.Segmenter`-based word boundaries
- Provides more accurate word movement for international text and code
- Affects `nextWord()`, `prevWord()`, and `endOfWord()` cursor movements


### Session Resume Tab UI Improvements
**What:** The session resume interface now shows a responsive tab bar that dynamically adjusts based on available width.
**Evidence:** `Jk2()` function at line 465910
**Details:**
- Tabs truncate intelligently when there are many session tags
- Shows "← N" and "→ N (tab to cycle)" indicators for overflow
- Displays "Resume (All Projects)" when viewing all projects
- Cleaner layout calculation prevents UI overflow


### BOM (Byte Order Mark) Stripping
**What:** Added utility function to strip UTF-8 BOM from file contents.
**Evidence:** `C9A()` function at line 60214
**Details:**
- Strips leading `\uFEFF` character from strings
- Helps handle files with BOM markers more gracefully


### Thinkback Plugin Source Change
**What:** The thinkback plugin source has been updated from `claude-code-marketplace` to `claude-plugins-official`.
**Evidence:** Variable `HI5` at line 467595
**Details:**
- Repository reference changed from `anthropics/claude-code-marketplace` to `anthropics/claude-plugins-official`
- Thinkback skill path construction updated accordingly


### Session Memory Configuration
**What:** Session memory feature now supports configurable thresholds via feature flags.
**Evidence:** `cm2()` function at line 493353
**Details:**
- New `tengu_sm_config` feature flag for configuration
- Configurable parameters: `minimumMessageTokensToInit`, `minimumTokensBetweenUpdate`, `toolCallsBetweenUpdates`
- Default values: 10K tokens to init, 5K between updates, 3 tool calls between updates


### API Base URL Validation
**What:** Added validation to check if the configured API base URL points to Anthropic's official API.
**Evidence:** `Ym0()` function at line 63996
**Details:**
- Validates `ANTHROPIC_BASE_URL` environment variable
- Used to determine if certain enterprise features should be enabled
- Returns true for `api.anthropic.com` or when no custom URL is set


### WebSocket Transport Session ID Logging
**What:** WebSocket transport now includes session ID in log messages for better debugging.
**Evidence:** Class `II0` at line 497588
**Details:**
- Constructor now accepts optional session ID parameter
- Log messages include session context when available
- Helps with debugging connection issues in multi-session scenarios


### Internal Refactoring
- Permission sync system refactored to use mailbox-based communication instead of file-based polling
- Removed several deprecated permission sync functions (`MH8`, `j02`, `OH8`, `SB1`, `P02`, `S02`, `_H8`)
- Inbox polling now handles multiple message types (regular messages, permission requests/responses, sandbox permissions)
- Read/Search message collapsing infrastructure added but not yet enabled (`collapsed_read_search` type)


### Removed
- `SwarmPermissionPoller` component removed in favor of unified inbox polling
- `PermissionLeaderPoller` removed in favor of mailbox-based permission handling
- Old file-based permission sync directories and lock files no longer used
