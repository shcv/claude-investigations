# Changelog for version 2.0.54

## Highlights

This release introduces enterprise hook control via `allowManagedHooksOnly`, adds telemetry event sampling to reduce observability costs, and begins testing a new CDN infrastructure with "dark read" parallel downloads. Terminal progress indicators are now more compatible across different terminal emulators.


### Enterprise Hook Control: `allowManagedHooksOnly` Policy Setting
**What:** New policy setting that restricts hook execution to only those defined in managed enterprise settings, blocking user, project, local, and plugin hooks.

**How to use:** Configure in your managed policy settings:
```json
{
  "policySettings": {
    "allowManagedHooksOnly": true,
    "hooks": {
      "PreToolUse": [...]
    }
  }
}
```

**Details:**
- When enabled, only hooks from `policySettings.hooks` will execute
- Plugin hooks are explicitly skipped with log message "Skipping plugin hooks - allowManagedHooksOnly is enabled"
- Complements existing `disableAllHooks` setting by providing a middle ground
- **Evidence**: `eQ1()` at line 337237, `VA0()` at line 337232, policy schema at line 503153


### Telemetry Event Sampling
**What:** Probabilistic sampling mechanism that reduces telemetry overhead by logging only a configurable fraction of events.

**Details:**
- Sampling rates configured via Statsig dynamic config `tengu_event_sampling_config`
- Per-event sample rates between 0 and 1 (0% to 100%)
- When sampled, events include `sample_rate` metadata for statistical reconstruction
- Events with `sample_rate: 0` are completely dropped
- **Evidence**: `lg1()` at line 231903, `ZD6()` at line 231900, modified `ZA()` at line 507257


### CDN Dark Read Testing
**What:** Parallel download attempts from new CDN infrastructure (`downloads.claude.ai`) alongside the primary Google Cloud Storage source, for performance testing without user impact.

**Details:**
- Runs silently in background during binary downloads
- Collects latency, success/failure, and error type metrics
- Reports via `tengu_native_cdn_dark_read_failure` telemetry event
- Creates temporary `claude-cdn-dark-read-*` directories, automatically cleaned up
- **Evidence**: `kp5()` at line 428907, `Ah2` CDN URL at line 428959


### MCP Endpoint Warning System
**What:** New warning when MCP endpoint files cannot be found, with automatic fallback to state files.

**How it appears:**
```
Warning: MCP endpoint file not found at <path> (session: <id>). Falling back to state file.
```

**Details:**
- Warning displays once per session (uses `lV9` flag to prevent spam)
- Error messages now include session IDs and file paths for easier debugging
- **Evidence**: `DH()` at line 519760, warning message at line 519769


### Smarter Terminal Progress Indicators
**What:** OSC 9;4 taskbar progress sequences now only emit for terminals that properly support them.

**Details:**
- **Enabled for**: ConEmu (via ConEmuANSI/ConEmuPID/ConEmuTask env vars) and Ghostty (TERM=xterm-ghostty)
- **Disabled for**: Windows Terminal (WT_SESSION) and non-TTY environments
- Prevents garbled output in unsupported terminals
- **Evidence**: New `GQ6()` function at line 220728, conditional rendering at line 220776


### Session Memory Path Refactoring
**What:** Session memory now uses project-based paths instead of global paths, with centralized helper functions.

**Details:**
- New path: `<project-dir>/<session-id>/session-memory/` instead of `<global-config>/session-memory/`
- Three new helpers: `zI1()` (base path), `_B1()` (summary.md path), `zP3()` (path check)
- New `summary.md` file with structured template (Task specification, Files and Functions, Workflow, etc.)
- Better isolation between projects and sessions
- **Evidence**: `zI1()` at line 506034, `_B1()` at line 506037, `jG2()` summary reader at line 340819


### Plan Mode Data Handling Refactored
**What:** Plan injection/stripping moved from inline code to dedicated helper functions for cleaner architecture.

**Details:**
- `O_2()` at line 403698: Adds plan content to ExitPlanMode tool input
- `R_2()` at line 403754: Strips plan field from tool outputs in conversation history
- Improves code maintainability and separation of concerns
- **Evidence**: See lines referenced above, formerly inline at v2.0.53:404788-404791


### Binary Download Telemetry
**What:** Successful binary downloads now report latency metrics.

**Details:**
- New `tengu_binary_download_success` event with `latency_ms` and `is_cdn` fields
- Helps track download performance across different sources
- **Evidence**: `Bh2()` at line 428934, telemetry call at line 428563


### OverflowTest Tool Removed
**What:** Internal testing tool for generating large outputs has been removed from the codebase.

**Details:**
- Tool was only available when `ENABLE_OVERFLOW_TEST_TOOL` environment variable was set
- Used for testing tool result persistence with configurable output sizes (1-10000 KB)
- Some orphaned schema definitions remain as dead code (`BdZ`, `GdZ` at line 475943)
- **Evidence**: Full removal from v2.0.53 lines 475722-475818


### Import Reorganization
- Various import statements reorganized and consolidated
- No functional impact on users
- **Evidence**: Multiple import changes in diff (stream, child_process, crypto, fs, path modules)


### Hook Loading Functions Renamed
- `ZA0` → `DA0`, `YLA` → `XLA` for hook initialization
- Now use centralized `VA0()` to get hooks respecting `allowManagedHooksOnly`
- **Evidence**: Lines 337259-337268 in v2.0.54
