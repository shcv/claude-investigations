# Changelog for version 2.0.36

## 🎯 Highlights
Version 2.0.36 introduces session-scoped hooks for temporary automation, adds telemetry infrastructure for monitoring, and improves plugin reliability with duplicate hook detection. Pro and Max users gain quick access to usage settings via a new command.

## 🚀 New Features

### Extra Usage Command
**What:** New command for Pro and Max subscribers to quickly access Claude AI usage settings
**How to use:**
```bash
claude extra-usage
```
**Details:**
- Opens https://claude.ai/settings/usage in your browser
- Only available for "pro" or "max" subscription tiers
- Can be disabled by setting `DISABLE_EXTRA_USAGE_COMMAND` environment variable
- **Evidence**: `RAI command definition at line 467420` in new function, `ha2 = RAI at line 467528`

### Session Hooks Infrastructure
**What:** New architecture for temporary, session-scoped hooks that automatically clean up when sessions end
**How it works:**
- Session hooks are stored separately from user settings (`sessionHooks` field in app state at line 141240)
- Automatically cleared on session end to prevent accumulation
- Support callback functions (`onMatch`) for programmatic responses
- Cannot be removed through settings UI (protected at diff lines 2057-2059)

**Details:**
- Three new management functions:
  - `wB1() at line 457341` - Retrieves session hooks for a specific session
  - `ll2() at line 457356` - Finds and returns matching hook callbacks
  - `il2() at line 457367` - Clears all hooks for a session
- Session hooks are merged with permanent hooks at execution time (merge logic in `nl2() at line 457391`)
- Hooks are marked with `source: "sessionHook"` to distinguish from settings-based hooks
- Designed for plugins, agents, and temporary automation without polluting user settings
- **Evidence**: State initialization at `line 141240`, management functions at `lines 457341-457367`, integration in `nl2() at lines 457391-457413`

### Datadog Telemetry Integration
**What:** New telemetry backend for event logging and monitoring
**Details:**
- Sends logs to Datadog HTTP intake endpoint: `https://http-intake.logs.datadoghq.com/api/v2/logs`
- Controlled by feature gate `tengu_log_datadog_events` (gate name at line 477899)
- Batches events for efficiency (batch size threshold `KBI`, flush interval `VBI = 15000ms` at line 477634)
- Includes context tags: user type, version, model, session ID, platform details
- Automatic flush on process exit
- **Evidence**: `FBI constant at line 477632`, gate check `er2 at line 477899`, batching logic in `QB0() at line 477567` and `BB0() at line 477543`

### OpenTelemetry 1P Events
**What:** First-party event logging using OpenTelemetry protocol
**Details:**
- Exports events to Anthropic's event logging endpoint: `{ANTHROPIC_BASE_URL}/api/event_logging/batch`
- New exporter class `IB0 at line 477676` handles batching and export
- Transforms logs into ClaudeCodeInternalEvent format with environment context
- Logger initialization in `or2() at line 477773` with automatic shutdown handling
- Controlled by feature gate `tengu_log_1p_events` (gate check in `rr2() at line 477755`)
- Events include session context, environment details, and custom metadata
- **Evidence**: `IB0 class at lines 477676-477751`, initialization `or2() at line 477773`, event emission `ZB0() at line 477761`

## 💡 Improvements

### Enhanced Plugin Hook Loading
**What:** Plugin loading now detects and prevents duplicate hook file loading
**How it works:**
- Uses `realpathSync()` to resolve canonical file paths (at line 275643 in `BwQ()`)
- Tracks loaded hook files in a Set to detect duplicates
- In strict mode (default), duplicate hooks trigger errors with helpful messages
- Automatically loads `hooks/hooks.json` if it exists, so manifest shouldn't reference it

**Details:**
- New 5th parameter added to plugin loading function `BwQ(A, B, Q, I, G = !0)` where `G` controls strict mode (function signature at line 275505)
- Strict mode enabled by default but can be disabled via marketplace entry's `strict: false` property (call site at line 275831)
- Enhanced logging: "Loaded hooks from standard location for plugin..." (at line 275647)
- Error message explains the issue: "The standard hooks/hooks.json is loaded automatically, so manifest.hooks should only reference additional hook files" (at lines 275696-275697)
- Prevents common plugin authoring mistakes and duplicate hook registrations
- **Evidence**: Function `BwQ() at line 275505`, duplicate detection at `lines 275689-275707`, Set tracking at `line 275637`

### Enhanced Session End Handling
**What:** Session end processing now includes session hook cleanup and accepts additional configuration
**Details:**
- Function renamed from `Hf1()` to `Tf1()` with enhanced parameters (signature at line 483476)
- Now accepts options object with `getAppState`, `setAppState`, `signal`, `timeoutMs` 
- Automatically clears session hooks after executing SessionEnd hooks (cleanup call `il2(I, J)` at line 483506)
- Prevents session hook accumulation across multiple sessions
- **Evidence**: Old function `Hf1 at line 482867` (removed), new function `Tf1 at line 483476` (added), session hook clearing at `line 483506`

### Improved Continue Command Detection
**What:** More robust detection of user "continue" commands
**Details:**
- Updated pattern matching in `prQ() at line 347927`
- Now trims input and checks for exact "continue" match: `if (B === "continue") return !0;`
- Also matches phrase patterns "keep going" and "go on"
- **Evidence**: Function `prQ() at line 347927`, exact match check at line 347929

### Enhanced GitHub Actions Workflow Template
**What:** PR review workflow now triggers on more PR events
**Details:**
- Previous triggers: `[opened, synchronize]`
- New triggers: `[opened, synchronize, ready_for_review, reopened]`
- Ensures reviews run when draft PRs become ready for review and when closed PRs reopen
- **Evidence**: Workflow template `yp2 at line 452368`, trigger definition at line 452314

## 🔧 Internal Changes

### Query Handler Refactoring
- Function identifier `iS2` repurposed: old agent definitions renderer moved to `Fy2() at line 437284`
- New `iS2() at line 436183` is async query handler managing user input processing, checkpointing, message preparation, and queue processing
- Not user-facing but improves code organization

### Hook Retrieval Function Update
- Function renamed from `sl2()` to `Hi2()` with additional state parameter
- Now merges session hooks with settings-based hooks
- Updated to call `nl2(A)` which includes session hook integration
- **Evidence**: Old function signature `sl2(A)` at diff line 1940, new signature `Hi2(A, B)` at diff line 1984

### Process Metrics Helper
- New helper function `Hp2() at line 451872` formats telemetry metadata
- Structures environment context, process metrics, and core session data
- Used by telemetry exporters for consistent event formatting
- **Evidence**: Function `Hp2(A, B = {})` at line 451872

---

*This changelog reflects changes from v2.0.35 to v2.0.36 based on structural diff analysis and source code verification.*
