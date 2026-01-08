# Changelog for version 1.0.114

## Highlights
Version 1.0.114 introduces macOS filesystem sandboxing, an interactive thinking mode with visual highlighting, and enhanced Windows terminal support. This release focuses on security hardening, improved user experience, and better cross-platform compatibility.

### Filesystem Sandboxing for macOS
**What:** Fine-grained filesystem access controls using macOS sandbox-exec, allowing you to restrict which files and directories bash commands can read or write.

**How to use:**
Configure in `.claude/settings.json`:
```json
{
  "sandbox": {
    "filesystem": {
      "read": {
        "allow": ["~/projects/*", "~/data"],
        "deny": ["/etc/passwd"]
      },
      "write": {
        "allow": ["~/projects/output/*"],
        "deny": ["~/projects/output/protected"]
      }
    }
  }
}
```

**Details:**
- Complements existing network sandboxing (v1.0.113 only had network restrictions)
- Read allow-list mode denies all reads except specified paths
- Write deny-list blocks specific paths while allowing essential system paths
- Automatically allows stdout/stderr, temp directories, and Claude config paths
- Supports path expansion (`~`, `./`, `../`) and wildcards (`/*` suffix only)
- Path validation prevents shell metacharacters (`&&`, `||`, `;`, backticks, `$`)
- **Evidence**: `QBB() at line 374281`, `y41() at line 353864`

### Interactive Thinking Mode with Visual Highlighting
**What:** Real-time detection and visual highlighting of thinking trigger words in 7 languages (English, Japanese, Chinese, Spanish, French, German, Korean) with three intensity levels.

**How to use:**
Type trigger words in your prompt to activate extended thinking:
```bash
# Basic (4,000 tokens): "think", "考えて", "想"
claude "think about the best algorithm for this"

# Medium (10,000 tokens): "think deeply", "megathink", "もっと考えて"
claude "think deeply about the edge cases"

# High (31,999 tokens): "think harder", "ultrathink", "熟考"
claude "think harder about the security implications"
```

**Details:**
- Trigger words are highlighted with shimmer effects as you type
- Status bar shows: "Thinking on • [level] • /t to disable"
- Use `/t` command to toggle thinking mode on/off
- Intelligently ignores conversational phrases like "I think" and "we think"
- Color-coded by intensity: basic (low), medium (medium), high (max)
- **Evidence**: `TTA() at line 366061`, `PTA() at line 366112`, `fA0() at line 366083`, `o1Q() at line 436378`

### Windows Terminal Enhanced Support
**What:** Improved clear screen handling for Windows Terminal and VSCode integrated terminal on Windows.

**Details:**
- Detects Windows Terminal via `WT_SESSION` environment variable
- Detects VSCode terminal via `TERM_PROGRAM` environment variable
- Modern Windows terminals now use full clear sequence (`\x1B[2J\x1B[3J\x1B[H`) that clears scrollback buffer
- Legacy Windows consoles continue using compatible sequence (`\x1B[2J\x1B[0f`)
- Provides cleaner screen clearing experience in modern Windows environments
- **Evidence**: `JN9() at line 362129`, `XN9() at line 362132`, `FN9() at line 362142`

### Output Truncation Protection
**What:** Automatic truncation of bash command output exceeding 64MB to prevent memory issues.

**Details:**
- Default limit: 64MB (67,108,736 bytes)
- Truncated output shows: `... [output truncated - ${KB}KB removed]`
- Tracks total bytes received even when truncated
- Prevents crashes from commands generating massive output
- **Evidence**: `class ga at line 362733`

### Bulk File History Restore
**What:** Restore multiple files from file history backups in a single operation.

**Details:**
- Restores files to their pre-session state from backups
- Handles three scenarios: restore from backup, delete new files, skip missing files
- Supports dry-run mode to preview changes
- Returns count of files affected
- Continues on errors with detailed logging
- **Evidence**: `_3B() at line 393833`, `k3B() at line 393866`

### Smart Editor Detection
**What:** Intelligent editor selection that verifies editors are actually installed before attempting to use them.

**How it works:**
```bash
# Priority order: $VISUAL → $EDITOR → code → vi → nano
# Only selects editors that exist on the system
claude /memory
```

**Details:**
- Uses `which` (Unix) or `where` (Windows) to check editor availability
- Tries VS Code (`code`), then `vi`, then `nano` in order
- Trims whitespace from environment variables to prevent issues
- Throws clear error if no editor is available
- Improves reliability when opening memory files
- **Evidence**: `If1() at line 404558`, `V95() at line 404550`

### Enhanced PostToolUse Hook Messages
**What:** Specialized system message types for hook execution outcomes instead of generic informational messages.

**Details:**
- New message type: `post_tool_hook_success` for successful hook completion
- New message type: `post_tool_hook_cancelled` for user-cancelled hooks
- Clearer semantic representation in message history
- Better structured for UI rendering and debugging
- Note: PostToolUse hooks existed in v1.0.113, only the message types are new
- **Evidence**: `PIB() at line 398052`, `jq0() at line 398064`

### Improved Interrupt Messaging
**What:** More informative interrupt messages that guide users on what to do next.

**Details:**
- Changed from "Interrupted by user" to "Interrupted · What should Claude do instead?"
- Clearer call-to-action for users after interrupting
- Better UX for mid-task cancellations
- **Evidence**: `lM() at line 373333`, `t8() at line 373341`

### Environment Variable Support for Default Haiku Model
**What:** Configure default Haiku model via `ANTHROPIC_DEFAULT_HAIKU_MODEL` environment variable.

**Details:**
- Allows overriding the default Haiku model for specific use cases
- Falls back to standard Haiku 3.5 if not set
- Useful for testing or using alternative Haiku versions
- **Evidence**: `FX2() at line 371423`

### Empty Directory Cleanup
**What:** Automatically removes empty directories after file operations.

**Details:**
- Cleans up empty directories left after file deletions
- Prevents directory clutter in file history operations
- Silently handles cases where directory removal fails
- **Evidence**: `U65() at line 411458`

### Metrics Reset Function
**What:** Proper reset of session cost and usage metrics.

**Details:**
- Resets total cost, API duration, tool duration, line counts
- Ensures clean state for new sessions
- Prevents metric accumulation across sessions
- **Evidence**: `Fo1() at line 340029`

### Image Optimization
- Added `hOA() at line 364421` for processing and optimizing base64-encoded images

### String Truncation Utility
- Added `u00() at line 362718` for joining and truncating string arrays with size limits

### Path Processing Helpers
- Added `EG1() at line 374270` for expanding filesystem paths (`~`, `./`, relative to absolute)
- Added `NG1() at line 374278` for escaping paths in sandbox profiles

### Thinking Detection Utilities
- Added `$j9() at line 366080` for checking if text contains thinking triggers
- Added `Nw1() at line 366092` for extracting trigger word positions
- Added `Ew1() at line 365889` for splitting text into highlighted/normal segments
