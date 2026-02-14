# Changelog for version 2.0.52

## Highlights

Version 2.0.52 introduces persistent storage for large tool outputs (saving them to disk instead of truncating), adds a new `CLAUDE_ENV_FILE` environment variable for custom session configuration, and includes extra usage visibility in the `/usage` display for Pro/Max users. Internal improvements include buffered logging for better performance and enhanced telemetry for GitHub Actions workflows.


### Tool Result Persistence
**What:** Large tool outputs (>400KB) are now saved to disk instead of being truncated, allowing Claude to access the full data later.

**How it works:**
When a tool produces output exceeding 400KB with `ENABLE_TOOL_RESULT_SIZE_LIMIT` enabled, the output is:
1. Saved to `~/.claude/projects/<project>/tool-results/<tool>-<timestamp>/result.{txt|json}`
2. A 2KB preview is shown inline
3. Claude receives instructions on how to explore the full file

**Example output:**
```xml
<persisted-output>
Output too large (1.5 MB). Full output saved to: ~/.claude/projects/.../tool-results/Bash-1701234567890/result.txt

Preview (first 2.0 KB):
[preview content...]
...

You can explore this file using:
- Read tool to view portions of the file
- Grep tool to search for patterns
- Bash with jq to query JSON data
- Bash with head/tail for beginning/end
</persisted-output>
```

**Details:**
- Automatically detects JSON output and creates `.json` files with `jq` usage examples
- Tool result files are automatically granted read permission (no prompts needed)
- Falls back to truncation if file writing fails
- **Evidence:** `$_2()` at line 403698, `if5()` at line 403760, `nf5()` at line 403783


### Custom Session Environment File
**What:** New `CLAUDE_ENV_FILE` environment variable allows loading custom session environment scripts.

**How to use:**
```bash
export CLAUDE_ENV_FILE=/path/to/my-env-setup.sh
claude
```

**Details:**
- Scripts from `CLAUDE_ENV_FILE` are loaded before hook files from session-env directory
- Multiple sources can be combined (env file + hooks)
- Independent error handling - failures in one source don't prevent loading others
- Useful for personal environment configuration that doesn't belong in hooks
- **Evidence:** `kqB()` at line 232402, environment read at line 232407


### Extra Usage Display in /usage
**What:** Pro and Max plan users can now see their extra usage balance directly in the `/usage` command output.

**How to use:**
```bash
/usage  # Now shows extra usage section for eligible users
```

**Details:**
- Shows three states:
  - Not enabled: "Extra usage not enabled • /extra-usage to enable"
  - Unlimited: Shows "Unlimited" with no progress bar
  - Metered: Shows utilization bar with spending (e.g., "$5.23 / $30.00 spent")
- Displays monthly reset date
- Controlled by feature flag `claude_code_usage_show_extra_usage`
- Only visible to Pro and Max subscribers
- **Evidence:** `PM3()` at line 481986, `RJ0` title at line 482045


### Bubblewrap Sandbox Detection
**What:** New detection capability for when Claude Code is running inside a Bubblewrap sandbox on Linux.

**How it works:**
- Checks `process.platform === "linux"` AND `process.env.CLAUDE_CODE_BUBBLEWRAP === "1"`
- Infrastructure for future sandbox-aware behavior

**Details:**
- Currently unused in application code (preparation for future features)
- Part of environment detection module
- **Evidence:** `OV6()` at line 228083


### Buffered Debug Logging
**What:** Debug logging now uses intelligent buffering instead of direct filesystem writes.

**Details:**
- Accumulates log entries in memory (up to 100 entries)
- Flushes every 1000ms or when buffer is full
- Reduces filesystem I/O by 10-100x when debug logging is enabled
- Automatic immediate mode when using `--debug` flags (for real-time debugging)
- Graceful disposal ensures logs are flushed on exit
- **Evidence:** `QC0()` at line 2348, `nw9()` at line 2404


### Startup Profiling Reports Saved to Files
**What:** When startup profiling is enabled, reports are now saved to persistent files for later analysis.

**How to use:**
```bash
export CLAUDE_CODE_PROFILE_STARTUP=1
claude <command>
# Report saved to: ~/.claude/startup-perf/<timestamp>.txt
```

**Details:**
- Previously only logged to console (ephemeral)
- Now saves to `~/.claude/startup-perf/<timestamp>.txt`
- Directory created automatically if missing
- Still logs to console in addition to file
- **Evidence:** `WV9()` at line 507095, `cP3()` at line 507106


### Consolidated Permission Checks for Special Files
**What:** Permission checks for session files (bash outputs, session memory, plan files, tool results) are now centralized.

**Details:**
- New `FP3()` helper function consolidates all special file permission logic
- Tool result files automatically granted read permission (new)
- Cleaner codebase with less duplication
- **Evidence:** `FP3()` at line 506192


### Wildcard Tool Permission Rules
**What:** Added support for parsing wildcard tool permission rules like `ToolName:*`.

**Details:**
- New `Wt8()` function parses wildcard patterns in permission rules
- New `Mq()` function parses tool names with optional rule content in format `toolName(ruleContent)`
- Enhanced permission system flexibility
- **Evidence:** `Wt8()` at line 190167, `Mq()` at line 502273


### Progress Indicator Architecture Refactored
**What:** The ConEmu/Ghostty progress reporting system was refactored from an independent side-channel to an integrated render pipeline.

**Details:**
- Removed: `O81` class (ConEmu progress reporter), `T1A` class (progress manager), `LOA` global instance
- Added: `ink-progress` DOM elements, `sGB()` progress extraction from DOM
- Progress now updates synchronously with UI renders
- Same ANSI escape sequences generated, but through render pipeline
- **Evidence:** Removed classes at lines 403283-403407 (v2.0.51), new functions at lines 218873, 220775


### Growthbook Experiment Tracking
**What:** Added telemetry for A/B test experiment exposure tracking.

**Details:**
- Tracks which users are exposed to which experiment variations
- Events include: experiment ID, variation ID, device ID, user attributes
- Batched transmission via OpenTelemetry log pipeline
- Internal analytics only - no user-visible impact
- **Evidence:** `rNB()` at line 231011, `tNB()` at line 231925, `aNB()` at line 230979


### Enhanced GitHub Actions Telemetry
**What:** When running in GitHub Actions, Claude Code now collects additional metadata.

**Details:**
- New fields collected: actor, actor ID, repository, repository ID, owner, owner ID
- Sent via `github_actions_metadata` telemetry field
- Only when `GITHUB_ACTIONS=true` environment variable is set
- **Evidence:** Metadata collection at lines 228565-228573, telemetry at line 231700


### Remote Session ID Tracking
**What:** New `CLAUDE_CODE_REMOTE_SESSION_ID` environment variable for tracking remote sessions.

**Details:**
- Read from environment and included in telemetry
- Sent as HTTP header `x-claude-remote-session-id` in API requests
- Enables correlation of events across remote Claude Code sessions
- **Evidence:** Environment read at line 231577, telemetry at line 231676, header at line 301327


### Optimized Hook Count Tracking
**What:** Refactored how hook progress and resolution counts are tracked during tool execution.

**Details:**
- New `J29()` function pre-computes hook tracking maps
- `W29()` and `F29()` provide efficient lookup of sibling tool IDs and pending hooks
- Improves performance during parallel tool execution
- **Evidence:** `J29()` at line 503835, `W29()` at line 503879, `F29()` at line 503889
