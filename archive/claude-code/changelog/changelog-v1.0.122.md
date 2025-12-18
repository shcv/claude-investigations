# Changelog for version 1.0.122

## 🎯 Highlights

Version 1.0.122 significantly enhances security and configurability with hardened macOS sandbox policies based on Chrome's security model, a new `--setting-sources` flag for controlling which configuration files are loaded, and improved slash command management to optimize context window usage.

## 🚀 New Features

### Setting Sources Control

**What:** Control which configuration sources Claude Code loads via a new `--setting-sources` command-line flag

**How to use:**
```bash
# Only load user settings (ignore project/local configs)
claude --setting-sources=user

# Load user and project settings (ignore local)
claude --setting-sources=user,project

# Managed environment mode (only enterprise policies and CLI flags)
claude --setting-sources=
```

**Details:**
- Valid source values: `user`, `project`, `local` (comma-separated)
- Policy settings and CLI flags are always loaded (cannot be disabled)
- Enables controlled environments where project settings should be ignored
- Affects CLAUDE.md loading, MCP server configuration, and agent definitions
- **Evidence**: `St5() at line 447294`, `N4A() at line 348834`, `pn0() at line 340374`, `Rg() at line 348856`

### Sandbox Violation Filtering

**What:** Configure which sandbox violations to ignore for specific commands or globally

**How to use:**
```javascript
// In settings file
{
  "sandbox": {
    "ignoreViolations": {
      "*": ["/tmp", "/dev/null"],           // Ignore these paths for all commands
      "npm install": ["/private/var/folders"], // Ignore for specific command
      "python": ["/Library/Python"]
    }
  }
}
```

**Details:**
- Reduces noise from expected/harmless sandbox violations
- Violations are now correlated with the specific command that triggered them
- Commands are base64-encoded in sandbox logs for precise tracking
- Each violation now includes the command, not just the filesystem path
- **Evidence**: `Ec4 schema at line 370115`, `eR2() at line 370611`, `jc4() at line 370372`

### WebSocket Transport for MCP Servers

**What:** Configure MCP servers to use WebSocket connections directly

**How to use:**
```json
{
  "mcpServers": {
    "my-server": {
      "type": "ws",
      "url": "ws://localhost:8080",
      "headers": {
        "Authorization": "Bearer token123"
      }
    }
  }
}
```

**Details:**
- Previously WebSocket was only available for internal IDE communication
- Now supports custom headers and authentication
- Complements existing stdio, SSE, and HTTP transports
- **Evidence**: `F56 schema at line 388759`, transport enum updated at line 388727

### JSON Agent Definitions

**What:** Define custom agents using JSON format in addition to Markdown files

**How to use:**
```json
{
  "agents": {
    "my-agent": {
      "description": "Handles custom tasks",
      "prompt": "You are a specialized agent for...",
      "tools": ["Read", "Write", "Bash"],
      "model": "claude-3-5-sonnet-20241022"
    }
  }
}
```

**Details:**
- Enables programmatic agent configuration without creating .md files
- Supports runtime agent configuration via settings files
- Agents can now come from "flagSettings" source (CLI configuration)
- Includes validation with clear error messages for invalid definitions
- **Evidence**: `QRB schema at line 434547`, `GRB() at line 434642`, `$K5() at line 434622`

## ✨ Improvements

### Enhanced Sandbox Security (macOS)

**What changed:** macOS sandbox policies rewritten based on Chrome's security model, replacing broad wildcards with explicit whitelists

**How it works now:**
- **Process permissions:** Only allows `process-exec`, `process-fork`, and same-sandbox operations (previously allowed all process operations)
- **Mach IPC:** Restricts to 9 specific Apple system services instead of allowing all Mach operations
- **IOKit access:** Limited to specific device classes (IOSurfaceRootUserClient, RootDomainUserClient) instead of all IOKit operations
- **Sysctls:** Whitelists ~45 specific hardware/kernel information sysctls instead of allowing all reads
- **File I/O:** Specific device files only (/dev/null, /dev/random, etc.)

**Details:**
- Follows principle of least privilege
- Based on Chromium's battle-tested sandbox implementation
- Breaking change: Commands relying on unrestricted system access may fail
- Unix socket configuration changed: `allowUnixSockets` now only accepts array of paths (boolean values removed)
- **Evidence**: `kc4() at line 370411` (new profile generator replacing `eb6() at line 374940` in v1.0.120)

### Dynamic Auto-Protection for Claude Directories

**What changed:** Protected directories are now discovered dynamically instead of using a static list

**How it works now:**
- Automatically finds and protects all `.claude/commands` and `.claude/agents` directories in your project
- Uses ripgrep to locate Claude-specific directories at runtime
- Prevents accidental deletion or modification of Claude configuration
- Also protects user config files: `.gitconfig`, `.bashrc`, `.zshrc`, `.profile`, `.ripgreprc`, `.mcp.json`

**Details:**
- Adapts to your project structure automatically
- No manual configuration needed
- More reliable protection across different project layouts
- **Evidence**: `iR2() at line 370172` (replaces static `ZQB() at line 374759` in v1.0.120)

### Slash Command Budget Management

**What changed:** Slash command descriptions are now limited to prevent excessive context window usage

**How it works now:**
- Default character budget: 15,000 characters
- Configurable via `SLASH_COMMAND_TOOL_CHAR_BUDGET` environment variable
- Shows notification when commands are truncated: "(Showing 25 of 50 commands due to token limits)"
- Only includes commands with user-specified descriptions (excludes built-in commands without descriptions)

**Details:**
- Prevents unlimited context consumption with many custom commands
- Prioritizes commands by order (shows first N that fit in budget)
- Separate token tracking for slash command overhead
- **Evidence**: `GM6() at line 402246`, `G4B() at line 402255`, `Y4B() at line 402266`

### Expanded Ultrathink Triggers

**What changed:** Ultrathink mode now recognizes natural language variations

**Trigger phrases:**
- `"ultrathink"` (original)
- `"think ultra hard"` (new)
- `"think ultrahard"` (new)

**Details:**
- More discoverable and intuitive for users
- Backward compatible with original trigger
- **Evidence**: `DU1() at line 361856` (replaces `dw1() at line 366346` in v1.0.120)

### Account Display Names

**What changed:** OAuth account display names are now captured and synchronized

**How it works now:**
- Display names are fetched from `/api/oauth/profile` endpoint
- Stored alongside email, organization, and UUID
- Automatically updated during token refresh
- Available for showing richer user identification

**Details:**
- Improves user identification beyond email addresses
- Kept in sync with server changes
- **Evidence**: `Dq0() at line 405124` returns `{ subscriptionType, displayName }` (previously `JB0() at line 371316` returned only subscription string)

### Improved Git Ignore for Checkpoints

**What changed:** Checkpoint gitignore now prevents duplicate entries and has better error logging

**How it works now:**
- Reads existing `.gitignore` before appending to avoid duplicates
- Uses structured error logging with explicit error levels
- Better path handling with trailing slashes
- Creates parent directories if needed

**Details:**
- More robust against repeated invocations
- Cleaner `.gitignore` files
- Better error reporting and telemetry
- **Evidence**: `yy6() at line 412545`, `aY1() at line 404121` (enhanced from `u35()` and `Z61()` in v1.0.120)

### Status Line Reorganization

**What changed:** `/status` command output reordered and enhanced

**New section order:**
1. Working directory (moved to top)
2. **Setting sources** (new section showing which configs are active)
3. Installation status
4. System diagnostics
5. MCP servers
6. Account information
7. API provider
8. Memory usage

**Details:**
- Most frequently needed information appears first
- New "Setting Sources" section shows enabled config sources
- Account information extraction refactored for reusability
- **Evidence**: `Ey6() at line 411883` (new section), `My6() at line 411961` (refactored account display)

## 🔧 Internal Improvements

### Session Quality Classification

**What:** Internal analytics to detect user frustration and PR creation requests

**Details:**
- Analyzes conversation patterns to identify frustrated users
- Detects explicit pull request creation requests
- Sends telemetry event `tengu_session_quality_classification` for matching sessions
- Uses a lightweight model to analyze user message patterns
- No user-visible changes
- **Evidence**: `jr5() at line 442431`, `Pr5() at line 442426`

### OAuth Environment Mode Removed

**What:** Removed `USE_LOCAL_OAUTH` environment variable support

**Details:**
- Previously allowed switching between "local" and "prod" OAuth modes
- Now hardcoded to "prod" mode only
- Simplifies OAuth configuration
- **Evidence**: `M9A() at line 346962` always returns "prod" (replaced `ao1() at line 339979` in v1.0.120)

### Agent System Refactoring

**What:** Agent loading architecture improved for better maintainability

**Details:**
- Extracted deduplication logic into reusable `YR() at line 434554`
- Task tool description generation moved to `PXB() at line 419667` (same output as before)
- Support for "flagSettings" agent source added
- More modular code structure
- No user-visible behavioral changes

### Thinking-Only Response Detection

**What:** New helper to detect assistant responses containing only thinking blocks

**Details:**
- `xQB() at line 396683` checks if response is all `<thinking>` content
- Enables better handling of extended thinking responses
- Internal optimization, no user-facing changes

## 📊 Configuration Changes

### Breaking Changes

1. **Sandbox `allowUnixSockets` configuration:**
   - v1.0.120: Accepted `true`, `false`, or array of paths
   - v1.0.122: Only accepts array of specific paths
   - Migration: Change `allowUnixSockets: true` to `allowUnixSockets: ["/path/to/socket"]`

2. **Stricter macOS sandbox policies:**
   - Commands requiring unrestricted Mach IPC, IOKit, or sysctl access may fail
   - Review sandbox violations and add to `ignoreViolations` if needed

### New Configuration Options

```javascript
{
  "sandbox": {
    "ignoreViolations": {
      "*": ["path1", "path2"],  // Global ignore patterns
      "command-pattern": ["path3"]  // Command-specific ignore patterns
    }
  }
}
```

## 🐛 Bug Fixes

### Duplicate `.gitignore` Entries

Fixed checkpoint gitignore logic to check for existing patterns before appending, preventing duplicate `**/.claude/checkpoints` entries in `.gitignore` files.
- **Evidence**: `aY1() at line 404121` now reads file content before appending

---

**Note:** All line numbers reference `/home/shcv/projects/claude-investigations/archive/pretty/pretty-v1.0.122.js` unless otherwise specified.
