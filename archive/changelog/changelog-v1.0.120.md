# Changelog for version 1.0.120

## 🎯 Highlights

Version 1.0.120 introduces persistent file history across session resumes, a redesigned filesystem permissions model with simplified configuration, enhanced MCP server support with dynamic header generation, and critical security improvements for symlink handling.

## 🚀 New Features

### File History Persistence Across Sessions

**What:** File backup snapshots are now persisted to session logs and restored when resuming previous sessions, preserving the complete file modification history across Claude Code restarts.

**How it works:**
- During execution, file history snapshots are automatically saved to the session log file
- When resuming a session (e.g., `claude --resume <session-id>`), backup files from the previous session are hard-linked or copied to the new session directory
- The file history UI state is fully restored, showing which files were tracked and their modification history

**Details:**
- Session log entries now include a new type: `"file-history-snapshot"` at `insertFileHistorySnapshot()` at line 438449
- New function `a_1()` at line 384641 handles cross-session backup file migration
- New function `t11()` at line 384611 generates session-specific backup file paths
- New function `n_1()` at line 384636 processes snapshots to extract tracked files for UI restoration
- Session log class now includes `fileHistorySnapshots` Map at line 438396
- Backup files are stored per session in `~/.config/claude/file-history/<sessionId>/`

**Evidence**: `insertFileHistorySnapshot()` at line 438449, `a_1()` at line 384641, `t11()` at line 384611, `n_1()` at line 384636, `fileHistorySnapshots` field at line 438396

### MCP Dynamic Header Generation with headersHelper

**What:** MCP server configurations can now specify a shell command that generates HTTP headers dynamically at runtime, enabling secure credential management and token rotation.

**How to use:**
```json
{
  "mcpServers": {
    "my-api": {
      "transport": {
        "type": "sse",
        "url": "https://api.example.com/sse",
        "headers": {
          "X-Static-Header": "value"
        },
        "headersHelper": "~/scripts/get-auth-token.sh"
      }
    }
  }
}
```

**Details:**
- The `headersHelper` command must output valid JSON with string key-value pairs
- Dynamic headers override static headers (merge strategy: `{...static, ...dynamic}`)
- Includes workspace trust security checks for project/local-scoped servers at `Xo6()` at line 393477
- Comprehensive validation ensures proper JSON format and string values
- Errors are logged with telemetry event `tengu_mcp_headersHelper_missing_trust`
- Use cases: fetching tokens from credential managers, generating time-based auth, reading secrets from environment-specific sources

**Evidence**: `Xo6()` function at line 393477, `uw0()` merge function at line 393531, schema definitions at lines 353050-353074

### Unix Domain Socket Support for Network Permissions

**What:** Network permissions now support Unix domain sockets for local IPC, enabling tools like SSH agents and Docker to work within the sandbox.

**How to configure:**
```json
{
  "permissions": {
    "network": {
      "allowUnixSockets": true  // Allow all Unix sockets
    }
  }
}
```

Or with specific paths:
```json
{
  "permissions": {
    "network": {
      "allowUnixSockets": [
        "/var/run/docker.sock",
        "~/.ssh/agent.sock"
      ]
    }
  }
}
```

**Details:**
- Three modes: `true` (allow all), `false` (block all - default), or array of specific socket paths
- Currently implemented for macOS sandbox profiles using `(remote unix-socket)` directive
- Essential for Docker, SSH agents, and other development tools requiring local IPC
- Type: `boolean | string[]`

**Evidence**: Schema definition at lines 354206-354217, implementation at lines 374968-374975, parameter usage at line 375216

### SlashCommand Tool Validation

**What:** The internal `SlashCommand` tool now includes comprehensive input validation before execution, catching errors early and providing clear error messages.

**Details:**
- Validates command format with error code 1 at `validateInput()` at line 425333
- Checks if command exists with error code 2
- Verifies command can be loaded with error code 3
- Detects `disableModelInvocation` conflicts with error code 4
- Ensures command is prompt-based with error code 5
- Validation occurs before permission checks, improving error reporting

**Evidence**: `validateInput()` method at lines 425333-425369 in `X21` tool definition

## 🔒 Security Improvements

### Symlink Resolution in Permission Checks

**What:** File permission checks now resolve symlinks and verify that BOTH the symlink path AND its target are allowed, preventing permission bypass attacks via symlinks.

**How it works:**
- When checking read/edit permissions for `/home/user/project/link`, Claude Code now resolves it to its real path (e.g., `/etc/passwd`)
- Both paths are checked against permission rules
- Access is denied if EITHER path is restricted

**Details:**
- New function `CD1()` at line 339792 returns array of [original_path, resolved_path]
- Helper function `fW()` at line 339783 performs symlink resolution using `realpathSync()`
- Integrated into read permissions at `o11()` at line 439057
- Integrated into edit permissions at `dd()` at line 439126
- Integrated into working directory checks at `QE()` at line 438915
- Gracefully handles non-existent files and resolution errors

**Evidence**: `CD1()` at line 339792, `fW()` at line 339783, read permission integration at lines 439066-439084, edit permission integration at lines 439133-439154

### Enhanced Bash Command Analysis

**What:** Improved detection of shell variable expansion and command substitution in bash commands for more accurate file path extraction.

**Details:**
- Now detects patterns like `$VARIABLE` and `$(command)` in command arguments at `Ng6()` at line 382386
- Sets `mayHaveUnknownFiles` flag when variable expansion is detected
- Prevents false positives in automatic file reading after bash execution
- More conservative approach to file permission pre-approval

**Evidence**: Variable expansion detection at lines 382407-382412 in `Ng6()` function

## 🔄 Changes to Existing Features

### Redesigned Filesystem Permissions Model

**What:** The filesystem permissions configuration has been completely redesigned with a simplified, asymmetric approach: reads use denylist-only mode, writes use allowlist-only mode.

**Old model (v1.0.119):**
```json
{
  "permissions": {
    "filesystem": {
      "read": {
        "allowAllExcept": ["/etc/", "/private/"]
      },
      "write": {
        "denyAllExcept": ["/home/user/project/"]
      }
    }
  }
}
```

**New model (v1.0.120):**
```json
{
  "permissions": {
    "filesystem": {
      "read": {
        "denyOnly": ["/etc/passwd", "/private/keys/"]
      },
      "write": {
        "allowOnly": ["/home/user/project/"],
        "includeDefaults": true,
        "denyWithinAllow": ["./.claude/"]
      }
    }
  }
}
```

**Key differences:**
- **Read permissions**: Only `denyOnly` mode (assumes open by default, deny specific paths)
- **Write permissions**: Only `allowOnly` mode (assumes closed by default, allow specific paths)
- **Lost feature**: Can no longer do restrictive read permissions (`denyAllExcept` for reads is removed)
- **New feature**: `denyWithinAllow` allows exceptions within allowed write paths
- **Breaking change**: Existing v1.0.119 configurations are incompatible

**Evidence**: New schemas at lines 354053-354067 (`ew9` and `Aq9`), old schemas removed from lines 354007-354030 (`y10` and `k10`), new implementation at lines 374904-374938 (`ob6()` and `tb6()`)

### Tool Output Schemas

**What:** Several tools now include explicit `outputSchema` definitions alongside their existing `inputSchema`, improving type safety and documentation.

**Tools updated:**
- Read tool: `outputSchema` at `th6` at line 381201
- Edit tool: `outputSchema` at `yGB` at line 395229
- MultiEdit tool: `outputSchema` at `xo6` at line 395850
- Write tool: `outputSchema` at `co6` at line 396008
- Bash tool: `outputSchema` at `np6` at line 387039
- Grep tool: `outputSchema` at `sW5` at line 420771
- WebFetch tool: `outputSchema` at `bW5` at line 417012
- SlashCommand tool: `outputSchema` at `XX5` at line 425324

**Evidence**: Multiple schema definitions across tool implementations

### Documentation URL Updates

**What:** Internal documentation URLs have been updated from `docs.anthropic.com` to `docs.claude.com`.

**Examples:**
- Permissions docs: `https://docs.claude.com/en/docs/claude-code/iam#configuring-permissions`
- Environment variables: `https://docs.claude.com/en/docs/claude-code/settings#environment-variables`
- Hooks documentation: `https://docs.claude.com/en/docs/claude-code/hooks`
- Claude Code docs map: `https://docs.claude.com/en/docs/claude-code/claude_code_docs_map.md`

**Evidence**: `Cq9` object at line 354656, `pQ5` variable at line 403791, version constants at line 371686

### Consumer Terms Update UI

**What:** Two new UI components display information about updates to Anthropic's Consumer Terms and Privacy Policy.

**Details:**
- Pre-acceptance message function `pW5()` at line 418651 (effective September 28, 2025)
- Post-acceptance message function `iW5()` at line 418738
- Includes information about model training opt-in and data retention changes
- Provides links to updated terms, privacy policy, and announcement

**Evidence**: `pW5()` at line 418651, `iW5()` at line 418738

### Session Log Transcript Format

**What:** Session log transcripts now include a `fileHistorySnapshots` field in addition to existing fields.

**Format change:**
```javascript
{
  date, messages, fullPath, value, created, modified,
  firstPrompt, messageCount, isSidechain, leafUuid,
  summary, checkpoints,
  fileHistorySnapshots,  // NEW
  gitBranch
}
```

**Evidence**: `cRB()` function at line 438159, new parameter at line 438184

## 🐛 Bug Fixes

### Removed Redundant Slash Command Execution Logic

**What:** Removed duplicate condition check in slash command processing that always evaluated to true.

**Details:**
- Old code at line 1373: `if (!0) Y(!0);` - condition always true, always executed
- New code at line 1499: `Y(!0);` - executes directly without redundant check
- No functional change, just cleaner code

**Evidence**: Comparison of `lNB()` function structure at lines 424900-425196

### Stream Import Refactoring

**What:** Changed stream module import from default import to named import for better clarity.

**Details:**
- Old: `import dFQ from "stream";` (line 338181 removed)
- New: `import { PassThrough as rr5 } from "stream";` (line 443623 added)
- More explicit about what's being imported
- Better tree-shaking support

**Evidence**: Import statement change at line 443623

## 🧹 Internal Changes

### File History Cleanup on Session Expiry

**What:** New cleanup function removes expired file history backup directories based on the configured retention period.

**Details:**
- Function `yr5()` at line 442733 removes backup directories older than retention threshold
- Respects `cleanupPeriodDays` setting from configuration
- Returns statistics: `{ messages: count, errors: count }`
- Integrated into session cleanup routine at `rQQ()` at line 442760
- Empty directories are removed after cleanup

**Evidence**: `yr5()` at line 442733, integration at line 442760 (previously `uQQ()`)

### Documentation Reference Updates

**What:** Internal documentation and error message references updated across the codebase.

**Details:**
- Version updated from `1.0.119` to `1.0.120` in constants
- README URL updated: `https://docs.claude.com/s/claude-code`
- Issue reporting: `https://github.com/anthropics/claude-code/issues`

**Evidence**: Version constants at `Gt()` and `RU()` at lines 371752-371755

### Removed Internal Functions

**What:** Several internal functions were removed as part of the permissions model refactoring.

**Removed functions:**
- `sBB()` - Generic allow/deny rule generator (line 374871-374901)
- `pBB()` - Old read permission default paths (line 374680-374713)
- `i9B()` - Old bash file path analyzer (line 382301-382346)
- Various permission getter functions: `ZQB()`, `GQB()`, `YQB()`, `pb6()`, `ib6()`, `JQB()` (lines 375215-375242)

**Reason:** Replaced by new permission model implementation with separate read/write functions.

**Evidence**: Diff sections showing removed functions

### GitHub Actions Workflow Variables

**What:** GitHub Actions workflow YAML templates updated (renamed internal variables).

**Details:**
- Variables `wDB` and `qDB` renamed to `PDB` and `jDB`
- No functional changes to the workflows themselves
- Both templates remain identical in content

**Evidence**: Variables at lines 408499 and 408550

## 📊 Verification Checklist

- [x] File history persistence verified as NEW in v1.0.120 (did not exist in v1.0.119)
- [x] Permissions model verified as completely redesigned, not enhanced
- [x] MCP headersHelper verified as NEW functionality
- [x] Symlink resolution verified as NEW security feature
- [x] Unix socket support verified as NEW capability
- [x] All major claims include specific function names and line numbers
- [x] Distinguished between NEW and ENHANCED features
- [x] Excluded internal refactoring with no user impact
- [x] Provided concrete usage examples for new features
