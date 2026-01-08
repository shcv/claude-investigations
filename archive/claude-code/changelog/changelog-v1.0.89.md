# Changelog for version 1.0.89

## Highlights
Version 1.0.89 introduces powerful debug filtering, a new wizard-based UI framework for multi-step workflows, and significantly improves reliability with enhanced error handling, permission persistence, and extended timeout support for long-running operations.

### Debug Output Filtering
**What:** Filter debug messages by category using `--debug=pattern` syntax
**How to use:**
```bash
# Show only MCP-related debug messages
claude --debug=mcp <command>

# Show all debug messages except verbose ones
claude --debug=!verbose <command>

# Show multiple specific categories
claude --debug=mcp,server1,api <command>
```
**Details:**
- Supports both include patterns (show only these) and exclude patterns with `!` prefix (hide these)
- Automatically categorizes messages based on prefixes, MCP server names, and other patterns
- Cannot mix include and exclude patterns in the same filter
- Helps reduce noise when debugging specific components

### Wizard Framework for Multi-Step Workflows
**What:** A new React-based wizard system that provides consistent navigation for multi-step processes
**How to use:**
The wizard framework is currently used internally for the agent creation flow, providing a more intuitive step-by-step experience with:
- Forward/backward navigation with clear visual indicators
- Jump to specific steps when needed
- Step history tracking for complex navigation patterns
- Persistent data across all wizard steps
**Details:**
- Replaces the previous state machine approach for agent creation
- Provides consistent UI with step counters and navigation instructions
- Supports cancellation at any point with Escape key
- Designed to be reusable for future multi-step features

### Permission Persistence
**What:** Permanent permissions granted during tool use are now automatically saved to settings files
**How to use:**
When you grant permanent permissions to a tool during execution, they are now automatically saved to the appropriate settings file (`.claude/settings.json` for project, `~/.claude/settings.json` for user). No manual configuration needed.
**Details:**
- Supports all permission types: file paths, tool rules, and directories
- Respects settings hierarchy (project vs user settings)
- Eliminates the need to re-grant permissions in future sessions
- Includes comprehensive debug logging for troubleshooting

### Enhanced Error and API Request Tracking
**What:** Internal diagnostics system that tracks the last API request and maintains an error log
**How to use:**
This feature works automatically in the background, maintaining a rolling log of the last 100 errors and tracking the most recent API request for debugging purposes.
**Details:**
- Helps diagnose issues when errors occur
- Maintains structured clones of API requests for analysis
- Error log has a 100-item limit with automatic rotation
- Primarily for internal debugging and support

### Expanded Bash Command Permission Tracking
**What:** 18 additional bash commands now require appropriate file permissions
**How to use:**
Commands like `cat`, `head`, `tail`, `diff`, `awk`, and others now trigger permission checks:
```bash
# These commands now check read permissions for the specified paths
cat /etc/passwd
head -n 10 /var/log/system.log
diff file1.txt file2.txt
```
**Details:**
- New commands include: `cat`, `head`, `tail`, `sort`, `uniq`, `wc`, `cut`, `paste`, `column`, `tr`, `file`, `stat`, `diff`, `awk`, `strings`, `hexdump`, `base64`, `nl`
- All new commands require read permissions only
- Provides clear descriptions when permission prompts appear
- Enhances security by ensuring all file access is properly authorized

### Ripgrep Error Recovery
**What changed:** Ripgrep now recovers partial results when interrupted or hitting limits
**Previous behavior:** Lost all results if ripgrep was terminated or hit buffer limits
**New behavior:** Preserves and returns valid partial results, trimming potentially incomplete last lines
**Impact:** More reliable search results in large codebases where ripgrep might hit resource limits

### API Timeout Extension
**What changed:** Default API timeout increased from 60 seconds to 600 seconds (10 minutes)
**Previous behavior:** API calls would timeout after 1 minute
**New behavior:** API calls have 10 minutes before timing out
**Impact:** Prevents timeouts for complex Claude interactions, especially with slower models or lengthy operations

### Improved Timeout Error Messages
**What changed:** Timeout errors now provide actionable guidance
**Previous behavior:** Generic timeout error messages
**New behavior:** Displays "Request timed out (check API_TIMEOUT_MS)" with clear next steps
**Impact:** Users can easily identify and resolve timeout issues by adjusting the API_TIMEOUT_MS environment variable

### TodoWrite Tool Schema Enhancement
**What changed:** TodoWrite tool now requires dual-form descriptions for all todo items
**Previous behavior:** Todo items only had `content` and `status` fields:
```json
{"content": "Fix authentication bug", "status": "pending"}
```
**New behavior:** Todo items require three fields including a new `activeForm`:
```json
{
  "content": "Fix authentication bug",
  "activeForm": "Fixing authentication bug",
  "status": "pending"
}
```
**Impact:**
- Forces clearer articulation of both task goals and current actions
- Improves communication between AI and user about task progress  
- Enables status spinner to show contextual progress messages (though todo lists remain hidden since v1.0.86)
- All three fields (`content`, `activeForm`, `status`) are now required for TodoWrite tool usage
- Note: While activeForm enhances the schema, users still cannot see todo lists due to display removal in v1.0.86

### Platform Compatibility - Musl Libc Detection
**What changed:** Added detection for musl-based Linux distributions like Alpine Linux
**Previous behavior:** Assumed all Linux systems used glibc
**New behavior:** Detects musl libc by checking for library files and ldd output
**Impact:** Improves compatibility with Alpine Linux and other musl-based distributions

### Configurable Ripgrep Timeout
**What changed:** Ripgrep timeout is now configurable via environment variable
**Previous behavior:** Fixed 10-second timeout for ripgrep operations
**New behavior:** Uses BASH_DEFAULT_TIMEOUT_MS environment variable, defaulting to 120 seconds
**Impact:** Allows adjustment for different system capabilities and codebase sizes

### Fixed: Permanent permissions not persisting between sessions
- **Issue:** When users granted "permanent" permissions through the UI, they weren't saved to disk
- **Cause:** Missing persistence layer between permission granting and settings files
- **Resolution:** Added comprehensive persistence system that writes permissions to appropriate settings files
- **Affected versions:** All versions prior to 1.0.89
