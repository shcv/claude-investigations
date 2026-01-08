# Changelog for version 1.0.124

## Highlights

Version 1.0.124 introduces sandboxed bash mode for enhanced security, protects `.git/hooks` directories from unauthorized modifications, and adds experimental server-controlled extended thinking capabilities. The API retry mechanism was refactored to provide real-time error feedback through the UI instead of console logging.

### Sandboxed Bash Mode (`-sb/--sandboxed-bash`)
**What:** A new permission mode that combines sandbox restrictions with automatic command approval for commands that comply with configured filesystem and network policies.

**How to use:**
```bash
# Enable sandboxed bash mode
claude -sb

# Or with long form
claude --sandboxed-bash
```

**Details:**
- Requires a sandbox configuration to be active in your `settings.json` files
- Only available when `sandbox.filesystem` or `sandbox.network` restrictions are configured
- Auto-accepts commands that comply with sandbox policies while rejecting violating commands
- Accessible via keyboard shortcut (cycles through permission modes: default → sandboxBashMode → acceptEdits → plan → bypassPermissions)
- **Evidence**: Permission mode added to enum at `X41` line 352214, mode cycling logic in `bFB()` at line 427311, validation in `Ku2()` at line 383783

### Git Hooks Protection
**What:** Claude Code now protects `.git/hooks` directories in all git repositories within your workspace, requiring explicit permission before modifying hook scripts.

**Details:**
- Scans workspace for all git repositories using `.git/HEAD` detection
- Automatically adds `.git/hooks` and `.git/config` to protected paths list
- Prevents unauthorized modification of pre-commit, post-checkout, and other git hooks
- Complements existing `.git/config` protection (present since v1.0.86)
- **Evidence**: New protection logic in `YIA()` at lines 363503-363531, filtering `.git` from recursive scans at line 363462

### Server-Controlled Extended Thinking (Experimental)
**What:** Server-side feature flag system that enables automatic extended thinking token allocation for specific users without requiring manual triggers.

**Details:**
- New API endpoint `/api/oauth/claude_cli/client_data` fetches user-specific configuration
- When `alwaysThinking` is enabled server-side, maximum thinking tokens are automatically allocated
- Thinking blocks are intelligently hidden when auto-enabled unless user explicitly requested thinking
- Does not affect manual thinking triggers or `MAX_THINKING_TOKENS` environment variable
- **Evidence**: Client data API in `TWA()` at line 361888, token allocation in `pT()` at line 362093, hiding logic at line 415872

### Enhanced API Error Display
**What:** API retry errors now appear as structured messages in the UI instead of console output, providing real-time feedback during retry attempts.

**Details:**
- Retry mechanism refactored from async function to async generator that yields error states
- New `api_error` system message type shows retry countdown, attempt number, and timeout settings
- Error messages include improved timeout descriptions: "Request timed out. Check your internet connection and proxy settings"
- Console logging of retries removed in favor of UI components
- **Evidence**: Generator function `JY1()` at line 394593, error message creator `wQB()` at line 396886, UI component `YYB()` at line 415692

### Improved Bash Tool Documentation
**What:** The Bash tool now dynamically generates documentation based on active sandbox configuration.

**Details:**
- Documentation automatically includes active filesystem and network restrictions
- Shows allowed/denied paths and hosts when sandbox is configured
- Emphasizes `/tmp/claude/` as the proper temporary directory in sandbox mode
- Provides clear guidance on sandbox violation handling
- **Evidence**: Documentation generator `ql4()` at line 371292, integrated into Bash tool description at line 371437

### Permission Prompt Infrastructure
**What:** Permission prompts now support optional subtitles for displaying additional context.

**Details:**
- New `subtitle` parameter available in permission prompt components
- Subtitle displays next to title in a row layout with truncation support
- Currently unused but provides foundation for future enhancements (e.g., showing file paths)
- **Evidence**: Component `rz()` with subtitle at line 422454, wrapper function `fO()` with subtitle parameter at line 422836

### Extended Thinking Display Enhancements
**What:** Improved visual presentation of thinking blocks with collapsible display option.

**Details:**
- New "∴" (therefore) symbol for extended thinking display
- Collapsed view shows "∴ Thinking (ctrl+o to expand)" hint
- Expanded view shows "∴ Thinking…" with full content
- Smart filtering excludes tool result messages from thinking analysis
- **Evidence**: Display logic in `BYB()` at line 414832, message filter `FYB()` at line 415832

### API Token Counting Simplification
**What:** Removed unnecessary `isNonInteractiveSession` parameter from token counting functions.

**Details:**
- Functions `KP2()` (now `NP2()`) and `zP2()` (now `LP2()`) simplified
- Token counting no longer varies based on interactive vs non-interactive mode
- **Evidence**: Function `NP2()` at line 377221, function `LP2()` at line 377245

### Retry Logic Refactoring
**What:** Extracted inline retry logic into dedicated helper functions for better maintainability.

**Details:**
- `CQB()`: New sleep function with AbortSignal support (line 394549)
- `OE6()`: Extracts retry-after header from API responses (line 394669)
- `SE6()`: Calculates max retries from options or environment variable (line 394738)
- Improves code organization without changing retry behavior
- **Evidence**: Sleep function `CQB()` at line 394549, header extraction `OE6()` at line 394669

### Web Fetch Improvements
**What:** Removed `isNonInteractiveSession` parameter from web fetch operations.

**Details:**
- Function `jJB()` (now `rJB()`) simplified to remove session type parameter
- Web fetching behavior now consistent across all session types
- **Evidence**: Function `rJB()` at line 417265

### Slash Command Logging
**What:** Added debug logging for slash commands included in the SlashCommand tool.

**Details:**
- Logs list of available slash commands when generating tool description
- Helps diagnose issues with command availability
- **Evidence**: Logging in `w4B()` at line 413120

### Prompt History Deduplication
**What:** Prompt history now deduplicates pasted content to reduce storage usage.

**Details:**
- Only stores pasted content <= 1024 characters in history
- Larger pastes are excluded from the history record
- **Evidence**: Content filtering in `CoQ()` at line 361367, size limit `KoQ` at line 361273

### Session Resume Enhancement
**What:** Session resume now supports loading messages from session history database.

**Details:**
- New function `sb()` can resume from session ID with database lookup
- Converts database message records to internal message format
- Supports resuming with checkpoints and file history snapshots
- **Evidence**: Resume function `sb()` at line 413024, message converter `Fk6()` at line 413062

### Error Categorization Improvement
**What:** Better distinction between system messages and tool result messages in error categorization.

**Details:**
- New `cQB()` function identifies `post_tool_hook_feedback` messages
- Function `AN6()` (formerly `TE6()`) now correctly categorizes these messages
- **Evidence**: Message type checker `cQB()` at line 396567, categorizer `AN6()` at line 396395

### Boolean Environment Variable Parsing
**What:** Improved parsing of environment variables to handle boolean types natively.

**Details:**
- Function `aA()` (formerly `_B()`) now accepts boolean values directly
- Previously only handled string values
- **Evidence**: Enhanced parser `aA()` at line 340564

### API Key Retrieval Simplification
**What:** Removed unnecessary `isNonInteractiveSession` parameter from API key functions.

**Details:**
- Function `RX()` (now `PX()`) no longer requires session type parameter
- Function `QZB()` (now `CZB()`) simplified similarly
- **Evidence**: Function `PX()` at line 440221, function `CZB()` at line 440217

### Client Metadata Collection Update
**What:** OAuth account metadata collection function no longer requires API key parameter.

**Details:**
- Function `AM1()` (now `CM1()`) simplified to remove unused parameter
- **Evidence**: Function `CM1()` at line 368533

### Command Chaining Simplification
**What:** Removed context parameter from multi-command permission checking.

**Details:**
- Function `Ki4()` (now `vi4()`) and `mP2()` (now `oP2()`) no longer require context parameter
- **Evidence**: Function `vi4()` at line 378258, function `oP2()` at line 371695

### IDE Integration Cleanup
**What:** Removed `isNonInteractiveSession` parameter from IDE tab management.

**Details:**
- Function `IVB()` (now `OVB()`) simplified to only require tab name and IDE client
- **Evidence**: Function `OVB()` at line 422924

### Frequently Modified Files Analysis
**What:** Removed session type parameter from git history analysis.

**Details:**
- Function `cV5()` (now `$F5()`) no longer varies behavior by session type
- **Evidence**: Function `$F5()` at line 429518

### Command Path Extraction
**What:** Simplified bash command path extraction to remove session type dependency.

**Details:**
- Function `wT2()` (now `jT2()`) no longer requires `isNonInteractiveSession` parameter
- **Evidence**: Function `jT2()` at line 372008

### Notification System Simplification
**What:** Removed notification parameter from status bar component.

**Details:**
- Function `LFB()` (now `mFB()`) simplified status bar rendering
- Notification display logic integrated differently
- **Evidence**: Function `mFB()` at line 427595

### Rate Limit Pre-Check
**What:** Removed the unified rate limit status check function `QQB()` that was called before each API request.

**Details:**
- Previously checked rate limit headers before making requests
- Rate limiting now handled entirely through retry mechanism
- **Evidence**: Function `QQB()` removed from line 394273 in v1.0.123

### GitHub Actions Workflow Template Update
**What:** Minor update to the Claude Code Review GitHub Actions workflow template.

**Details:**
- Variable renamed from `FZB` to `OZB`
- Content remains identical
- **Evidence**: Variable `OZB` at line 407460

### Stream Import Removal
**What:** Removed unused `stream` module import.

**Details:**
- Import statement for OFQ from "stream" removed
- Replaced with more specific `PassThrough` import from "stream" at line 445118
- **Evidence**: Removed import at line 338191 in v1.0.123, new import `Lt5` at line 445118


**Note:** Many function and variable names changed in this release due to JavaScript minification/bundling. The functionality described above focuses on user-visible changes and meaningful internal improvements rather than cosmetic identifier changes.
