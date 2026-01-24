# Changelog for version 2.1.10


## Summary

This release introduces a new "Push to Remote" option in Plan Mode, allowing users to send their implementation plans directly to a Claude.ai remote session for autonomous execution. It also adds support for `hostPattern` matching in enterprise marketplace configurations, replaces the command path detection mechanism with a more efficient `which`-based approach, and lays groundwork for Perfetto performance tracing (currently disabled).

### Push to Remote from Plan Mode
**What**: Send an implementation plan directly to a cloud-based Claude.ai session that will execute it autonomously.

**Usage**: When Claude presents a plan for approval, there's now an option to push the plan to a remote session instead of executing locally. This creates a new remote agent session on Claude.ai that will implement the plan in the cloud.

**Details**:
- Requires being logged in to Claude.ai (not Console)
- Requires the Claude GitHub app to be installed on the repository
- Validates prerequisites before attempting to create the remote session
- Automatically handles uncommitted or unpushed changes via a git dialog
- Creates a remote agent that appears in your session list with an `r` prefix (e.g., `r123456`)

**Evidence**: `YA()` at line 510466 (plan-to-remote handler, creates session with `e2A()` and tracks with `tengu_plan_exit` outcome `"yes-push-to-remote"`)

### Host Pattern Matching for Enterprise Marketplace Sources
**What**: Enterprises can now use regex patterns to allow plugin marketplaces from specific domains without listing each one individually.

**Usage**: In `policySettings.strictKnownMarketplaces`, add an entry with `source: "hostPattern"`:
```json
{
  "source": "hostPattern",
  "hostPattern": "^github\\.mycompany\\.com$"
}
```

**Details**:
- Matches the hostname extracted from any marketplace source type
- For GitHub sources, matches against `"github.com"`
- For Git sources (SSH or HTTPS), extracts the hostname from the URL
- Allows enterprise IT to permit all marketplaces from internal GitHub Enterprise instances

**Evidence**: `Yn4()` at line 91027 (host pattern regex matcher, uses `new RegExp(Q.hostPattern).test(B)`)

### ExitPlanMode Tool Parameters for Remote Sessions
**What**: The ExitPlanMode tool now accepts parameters to indicate the plan was pushed to a remote session.

**Details**: New optional parameters:
- `pushToRemote`: Boolean indicating the plan was pushed to remote
- `remoteSessionId`: The ID of the created remote session
- `remoteSessionUrl`: URL to access the remote session

**Evidence**: Schema at line 416146 (contains `pushToRemote`, `remoteSessionId`, `remoteSessionUrl` parameters)

### Improved Command Path Detection
**What**: Claude Code now uses native `which` (Unix) or `where.exe` (Windows) commands instead of the previous `findActualExecutable` approach for detecting executable paths.

**Details**:
- More efficient and reliable command detection
- Uses `Bun.which()` when running under Bun runtime
- Falls back to shell-based `which`/`where.exe` on other runtimes
- Includes both async (`GC()`) and sync (`d1Q()`) variants

**Evidence**: `W94()` at line 27476 (new which-based implementation, calls `where.exe` on Windows, `which` on Unix)

### Reduced React DevTools Bundle
**What**: React DevTools code has been significantly reduced in the bundle.

**Details**: References to React DevTools dropped from 45 to 2 occurrences, removing unused debugging infrastructure.

**Evidence**: Removed variable `b6B` at line 173391 in v2.1.9 (contained `__REACT_DEVTOOLS_COMPONENT_FILTERS__` setup)

### Session Naming for Autonomous Tasks
**What**: Sessions initiated via autonomous tick-based inputs now display "Autonomous session" as the default title.

**Details**: When the first prompt starts with `<tick>`, the session is labeled "Autonomous session" rather than showing the prompt content.

**Evidence**: `ad()` at line 5350 (session title generator, contains `B ? "Autonomous session" : ""` when `firstPrompt?.startsWith("<tick>")`)

## Bug Fixes

- Fixed plugin hooks skipping when `allowManagedHooksOnly` is enabled in policy settings (`Nh()` at line 194862, `WW2()` at line 314806)

### Perfetto Performance Tracing [In Development]

**What**: Infrastructure for generating Perfetto-compatible trace files to analyze Claude Code performance.

**Status**: Feature-flagged, returns `false`. The `PERFETTO_TRACING` feature gate is disabled.

**Details**:
- Set `CLAUDE_CODE_PERFETTO_TRACE=1` or provide a file path to enable (once feature flag is enabled)
- Traces include API call timing, time-to-first-token (TTFT), token throughput metrics
- Output in Chrome Trace Event format (`trace-{sessionId}.json`)
- Tracks per-agent timing with parent-child relationships for nested agent calls
- Includes metadata like input/output token counts, cache hit rates, and errors

**Usage** (when enabled):
```bash
CLAUDE_CODE_PERFETTO_TRACE=1 claude
# or
CLAUDE_CODE_PERFETTO_TRACE=/path/to/trace.json claude
```

**Evidence**: `r_2()` at line 356811 (initialization, checks `process.env.CLAUDE_CODE_PERFETTO_TRACE` but guarded by `ix.PERFETTO_TRACING` which returns `!1`)
