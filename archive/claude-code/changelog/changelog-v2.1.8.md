# Changelog for version 2.1.8


## Summary

This release adds the `/fork` command for creating conversation forks, extends browser extension support beyond Chrome to include Brave, Edge, Arc, Chromium, Vivaldi, and Opera, and introduces macOS sleep prevention during long operations. The "ultrathink" keyword is now deprecated since thinking budget is max by default.

### /fork Command
**What**: Create a fork of the current conversation at any point, branching off into a separate session while preserving the original context.

**Usage**:
```bash
/fork              # Fork with auto-generated name
/fork my-branch    # Fork with custom name
```

**Details**:
- Creates a complete copy of the conversation up to the current point
- Automatically switches you to the new forked session
- Preserves all message history, attachments, and context
- Emits telemetry event `tengu_conversation_forked`
- Use `/resume` to switch between original and forked sessions

**Evidence**: `cK7` at line 489820 (`name: "fork"`, `description: "Create a fork of the current conversation at this point"`)

### Multi-Browser Extension Support
**What**: The "Claude in Chrome" browser extension now supports multiple Chromium-based browsers beyond just Google Chrome.

**Details**:
- Newly supported browsers: **Brave**, **Microsoft Edge**, **Arc**, **Chromium**, **Vivaldi**, **Opera**
- Auto-detects installed browsers and configures native messaging hosts for each
- Registers appropriate Windows registry keys for each browser
- Cross-platform support (macOS, Linux, Windows)

**Evidence**: `txA` at line 295966 (browser config object with `"brave"`, `"arc"`, `"edge"`, `"chromium"`, `"vivaldi"`, `"opera"` entries and `NativeMessagingHosts` paths)

### macOS Sleep Prevention
**What**: Claude Code now automatically prevents macOS from sleeping during long-running operations.

**Usage**: Automatic—no user action required.

**Details**:
- Uses macOS `caffeinate -i` command to prevent idle sleep
- Active only during operations that need it (reference-counted)
- Automatically restarts caffeinate every 4 minutes to maintain prevention during very long tasks
- Properly cleans up on session exit
- Only applies to macOS; no effect on other platforms

**Evidence**: `OW9()` at line 517291 (`caffeinate`, `-i`, `-t`, `"Started caffeinate to prevent sleep"`)

### Plan Mode Interview Skip
**What**: In plan mode, you can now skip the AskUserQuestion interview and jump straight to planning.

**Details**:
- When answering plan mode questions, a new option appears: "Skip interview and plan immediately"
- Also adds "Chat about this" option for discussing questions with Claude
- Navigate between options using arrow keys
- Useful when you want Claude to proceed without answering all clarifying questions

**Evidence**: `kD9()` at line 521459 (`"Skip interview and plan immediately"`, `"Chat about this"`)

### .claude Folder Session Permissions
**What**: A new permission scope for allowing Claude to edit its own configuration files within `.claude/` directories.

**Details**:
- When Claude requests to edit files in `.claude/`, a new option appears: "Yes, and allow Claude to edit its own settings for this session"
- Grants session-scoped permission for the `/.claude/**` glob pattern
- Streamlines workflows where Claude needs to update its own configuration

**Evidence**: `GrA` at line 96077 (`"/.claude/**"`), `LN7()` at line 517637 (`scope: "claude-folder"`)

### Context Microcompaction Boundaries
**What**: New internal infrastructure for tracking context compression events in long conversations.

**Details**:
- Adds `microcompact_boundary` system message type
- Tracks metadata about compaction: trigger, tokens saved, compacted tool IDs
- Used internally for session memory management
- No direct user interaction required

**Evidence**: `Uv2()` at line 430955 (`subtype: "microcompact_boundary"`, `content: "Context microcompacted"`)

### tmux Integration Improvements
Adds platform-specific installation instructions when tmux is not found:
- macOS: `brew install tmux`
- Linux: `sudo apt install tmux` or `sudo dnf install tmux`
- Windows: Suggests WSL or Cygwin

**Evidence**: `ZI9()` at line 513876 (`"Install tmux with: brew install tmux"`)

### Settings Validation for Cleanup
When settings have validation errors but `cleanupPeriodDays` is explicitly set, cleanup is now skipped with a clear warning message rather than potentially misbehaving.

**Evidence**: `ww9()` at line 540061 (`"Skipping cleanup: settings have validation errors but cleanupPeriodDays was explicitly set"`)

### OAuth Metadata Discovery
MCP OAuth connections now attempt to auto-discover OAuth metadata from the server, improving compatibility with OAuth providers.

**Evidence**: `g92()` at line 296348 (`"Set OAuth metadata from server discovery"`)

### File Download for API Sessions
Adds file download infrastructure for SDK/API sessions with retries and parallel download support.

**Evidence**: `HR7()` at line 537150 (`files-api-2025-04-14`, `"/v1/files/${A}/content"`)

## Bug Fixes

- Fixed variable expansion detection to properly recognize both `$VAR` and `%VAR%` patterns (`Xh()` at line 501011)
- Internal telemetry function renames for consistency (multiple functions)

### Ultrathink Keyword Deprecated
**What**: The `ultrathink` keyword no longer has any effect.

**Details**:
- Previous behavior: typing "ultrathink" in a message would enable extended thinking
- New behavior: Thinking budget is now **max by default** for all messages
- Users may see a tip: "Ultrathink no longer does anything. Thinking budget is now max by default."
- The regex pattern still exists but the parsing/detection logic has been removed

**Evidence**: Tip at line 528403 (`"ultrathink-deprecated"`, `"Ultrathink no longer does anything. Thinking budget is now max by default."`)
