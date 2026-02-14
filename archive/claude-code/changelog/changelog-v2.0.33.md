# Changelog for version 2.0.33

## Highlights
Version 2.0.33 introduces Segment analytics telemetry alongside existing Statsig tracking, enhances LSP file synchronization with four new lifecycle management methods, adds native support for Homebrew installations, and strengthens security with three new protections against path resolution bypass attacks.


### Segment Analytics Telemetry
**What:** Dual telemetry system that sends all events to both Statsig and Segment analytics platforms
**How to use:**
```bash
# Telemetry is enabled by default and respects existing opt-out mechanisms
export DISABLE_TELEMETRY=1  # Disables both Statsig and Segment
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1  # Also disables both
```
**Details:**
- All existing telemetry events (tool usage, file operations, security checks, etc.) now tracked to Segment in addition to Statsig
- Uses anonymous IDs by default (`claudecode.v1.{uuid}`), adds user IDs when authenticated with Claude.ai
- Feature-gated behind `tengu_log_segment_events` Statsig flag for controlled rollout
- Events batched (15 per flush) and auto-flushed every 10 seconds
- Graceful shutdown ensures no data loss on exit
- **Evidence**: Analytics SDK integration at `pF0` (line 19111), tracking function `Os2()` at line 475587, dual-tracking wrapper `j1()` at line 475648, initialization `Ms2` at line 475622


### Homebrew Installation Support
**What:** Native detection and handling of Homebrew-managed installations
**How to use:**
```bash
# When installed via Homebrew, update with:
brew upgrade claude-code

# Claude Code will detect this and show appropriate instructions
claude update
# Output: "Claude is managed by Homebrew."
# "To update, run: brew upgrade claude-code"
```
**Details:**
- Detects Homebrew installations by checking for `/Caskroom/` in executable path
- Prevents self-update attempts that could conflict with Homebrew management
- Shows in-session update notifications with correct "brew upgrade" command
- Polls npm registry every 30 minutes to check for updates
- Configuration tracking automatically skipped for package-manager installations
- **Evidence**: Homebrew detection `bnA()` at line 318415, installation type classifier `HN()` at line 318435, update handler at line 488357-488400, UI component `P22` at line 377347


### LSP File Lifecycle Management
**What:** Four new methods for synchronizing file state with Language Server Protocol servers
**How to use:**
```javascript
// These methods are called automatically by Claude Code's LSP integration
// Manual use in custom integrations:
const lspManager = createLSPManager();
await lspManager.initialize();

// Notify server when opening a file
await lspManager.openFile('/path/to/file.js', fileContent);

// Sync content changes
await lspManager.changeFile('/path/to/file.js', newContent);

// Notify server when closing
await lspManager.closeFile('/path/to/file.js');

// Inspect available servers
const servers = lspManager.getAllServers();
```
**Details:**
- `getAllServers()` returns Map of all initialized LSP servers for monitoring
- `openFile(path, content)` sends `textDocument/didOpen` with proper languageId mapping
- `changeFile(path, content)` sends `textDocument/didChange`, falls back to openFile if server not running
- `closeFile(path)` sends `textDocument/didClose` for cleanup
- Configuration changed from `fileExtensions` array to `extensionToLanguage` object mapping for proper language ID support
- Better error messages in shutdown that include actual error details instead of generic "check logs"
- **Evidence**: New methods added to return object at line 446455-446465, `openFile()` implementation at line 446408, `changeFile()` at line 446428, `closeFile()` at line 446442, `getAllServers()` at line 446405


### Enhanced Security: Path Resolution Bypass Protection
**What:** Three new security checks to prevent attacks using shell expansion and directory changes
**How to use:**
These protections are automatic. Commands that trigger them will prompt for approval:
```bash
# These patterns now require manual approval:
echo "data" > /tmp/$VAR/file.txt        # Variable expansion in redirect
cd /tmp && rm -rf important/            # Directory change with write operation
cat file > /etc/$(whoami)/config        # Command substitution in path
```
**Details:**
- **Shell expansion detection**: Regex `/(?:>>?)\s*\S*\$/` catches variable expansion with redirections
- **Dollar sign in paths**: Any file path containing `$` character now requires approval to prevent variable expansion bypass
- **CD with write operations**: Compound commands using `cd` followed by write operations (rm, mv, cp, etc.) require approval since final working directory cannot be statically verified
- All three checks use `"ask"` behavior (require approval) rather than `"deny"` to allow legitimate use cases
- **Evidence**: Shell expansion check in `tP1()` at line 254131, dollar sign check in `TYQ()` at line 253932, cd detection in `Fe8()` at line 253997


### Better Update Experience
- Update notifications now appear during active sessions (previously only when running `claude update`)
- Installation type detection improved with specific handling for development, native, npm-local, npm-global, and package-manager installations
- Configuration mismatch warnings help users understand when running from unexpected installation location
- **Evidence**: AutoUpdater wrapper integration at line 377584-377985


### LSP Configuration Structure
- Server configurations now use `extensionToLanguage` mapping instead of simple `fileExtensions` array
- Enables proper LSP `languageId` specification in didOpen notifications (e.g., `.js` → `"javascript"`)
- More structured format supports language servers that handle multiple languages
- **Evidence**: Configuration validation at line 5140-5147 in diff, usage in openFile at line 446412


### Error Reporting
- LSP shutdown errors now include all failure messages directly in exception text
- Previously directed users to "check logs" without immediate visibility
- **Evidence**: Improved error at line 5173-5177 in diff


### Code Organization
- Removed unused imports: `stream`, `node:child_process`, `node:os` 
- Removed internal UI class `dR0` for cursor management
- Removed React Box component wrapper `PRA`
- Cleaned up questionnaire navigation component `A11`
- **Evidence**: Removals listed in diff lines 10-461


### System Prompts
- Function `Lo` renamed to `bo` with signature change (removed one parameter)
- Internal prompt assembly logic reorganized but user-facing behavior unchanged
- **Evidence**: Function comparison at diff lines 7090-7417

# Changelog for version 2.0.33

## Highlights
Version 2.0.33 introduces Segment analytics telemetry alongside existing Statsig tracking, enhances LSP file synchronization with four new lifecycle management methods, adds native support for Homebrew installations, and strengthens security with three new protections against path resolution bypass attacks.


### Segment Analytics Telemetry
**What:** Dual telemetry system that sends all events to both Statsig and Segment analytics platforms

**How to use:**
```bash
# Telemetry is enabled by default and respects existing opt-out mechanisms
export DISABLE_TELEMETRY=1  # Disables both Statsig and Segment
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1  # Also disables both
```

**Details:**
- All existing telemetry events (tool usage, file operations, security checks, etc.) now tracked to Segment in addition to Statsig
- Uses anonymous IDs by default (`claudecode.v1.{uuid}`), adds user IDs when authenticated with Claude.ai
- Feature-gated behind `tengu_log_segment_events` Statsig flag for controlled rollout
- Events batched (15 per flush) and auto-flushed every 10 seconds
- Graceful shutdown ensures no data loss on exit
- **Evidence**: `j1()` at line 475648, `Os2()` at line 475587, `Ms2` at line 475622


### Homebrew Installation Support
**What:** Native detection and handling of Homebrew-managed installations

**How to use:**
```bash
# When installed via Homebrew, update with:
brew upgrade claude-code

# Claude Code will detect this and show appropriate instructions
claude update
# Output: "Claude is managed by Homebrew."
# "To update, run: brew upgrade claude-code"
```

**Details:**
- Detects Homebrew installations by checking for `/Caskroom/` in executable path
- Prevents self-update attempts that could conflict with Homebrew management
- Shows in-session update notifications with correct "brew upgrade" command
- Polls npm registry every 30 minutes to check for updates
- Configuration tracking automatically skipped for package-manager installations
- **Evidence**: `bnA()` at line 318415, `HN()` at line 318435, `Pe2` at line 488357, `P22` at line 377347


### LSP File Lifecycle Management
**What:** Four new methods for synchronizing file state with Language Server Protocol servers

**Details:**
- `getAllServers()` - Returns Map of all initialized LSP servers for monitoring
- `openFile(path, content)` - Sends `textDocument/didOpen` with proper languageId mapping
- `changeFile(path, content)` - Sends `textDocument/didChange`, falls back to openFile if server not running
- `closeFile(path)` - Sends `textDocument/didClose` for cleanup
- Configuration changed from `fileExtensions` array to `extensionToLanguage` object for proper language ID support
- **Evidence**: `ym2()` at line 446307, methods at lines 446405-446454


### Enhanced Security: Path Resolution Bypass Protection
**What:** Three new security checks to prevent attacks using shell expansion and directory changes

**Examples that now require approval:**
```bash
echo "data" > /tmp/$VAR/file.txt        # Variable expansion in redirect
cd /tmp && rm -rf important/            # Directory change with write operation  
cat file > /etc/$(whoami)/config        # Command substitution in path
```

**Details:**
- Shell expansion detection: Regex `/(?:>>?)\s*\S*\$/` catches variable expansion with redirections
- Dollar sign in paths: Any file path containing `$` character requires approval
- CD with write operations: Compound commands using `cd` + write operations require approval
- All checks use `"ask"` behavior (require approval) rather than `"deny"`
- **Evidence**: `tP1()` at line 254131, `TYQ()` at line 253932, `Fe8()` at line 253997


### Better Update Experience
- Update notifications now appear during active sessions
- Installation type detection improved with specific handling for development, native, npm-local, npm-global, and package-manager types
- Configuration mismatch warnings help identify unexpected installation locations
- **Evidence**: `_22` at line 377584


### LSP Configuration Structure  
- Server configurations now use `extensionToLanguage` mapping instead of `fileExtensions` array
- Enables proper LSP `languageId` specification (e.g., `.js` → `"javascript"`)
- **Evidence**: Configuration validation at line 5140 in diff


### Error Reporting
- LSP shutdown errors now include all failure messages in exception text instead of generic "check logs" message
- **Evidence**: Error handling at line 5173 in diff
