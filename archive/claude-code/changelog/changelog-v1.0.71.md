# Changelog for version 1.0.71

## Highlights
Version 1.0.71 introduces a customizable statusLine feature for terminal display, simplifies memory management for better reliability, and adds protection against concurrent operations while improving overall performance through optimized imports and bug fixes.

### StatusLine Display
**What:** Customizable status line at the bottom of your terminal showing contextual information
**Why:** Provides at-a-glance information about your current session, model, and working directory
**How to use:**
```bash
# Configure in ~/.claude/settings.json
{
  "statusLine": {
    "type": "command",
    "command": "cat | jq -r '\"\\(.model.display_name) in \\(.workspace.current_dir)\"'",
    "padding": 1
  }
}
```
**Details:**
- Receives JSON input with session_id, model info, workspace paths, and more
- Updates every 300ms (debounced) to show current context
- Can display any command output, limited to first line
- Supports ANSI color codes for custom styling

### StatusLine Setup Agent
**What:** New specialized agent that converts your shell PS1 prompt to Claude Code statusLine
**Why:** Makes it easy to replicate your familiar shell prompt in Claude Code without manual configuration
**How to use:**
```bash
# Ask Claude to set up your statusLine
"Use the statusline-setup agent to convert my PS1 to a statusLine"

# Or use it directly
/task statusline-setup "Convert my shell prompt"
```
**Details:**
- Automatically reads ~/.zshrc, ~/.bashrc, ~/.bash_profile, or ~/.profile
- Converts PS1 escape sequences (\\u → $(whoami), \\w → $(pwd), etc.)
- Preserves your ANSI color codes
- Updates settings.json automatically
- Removes trailing $ or > characters from output

### Global Hooks Control
**What:** New setting to disable all hooks globally
**Why:** Provides an escape hatch when hooks are causing issues or impacting performance
**How to use:**
```json
// In ~/.claude/settings.json
{
  "disableAllHooks": true
}
```
**Details:**
- Disables all hook executions including statusLine updates
- Useful for debugging or performance optimization
- Logs a message when hooks are skipped

### Concurrent Query Protection
**What:** Detection and tracking of simultaneous query executions
**Why:** Prevents race conditions and undefined behavior from rapid command execution
**Details:**
- Automatically detects when multiple queries run simultaneously
- Logs telemetry event `tengu_concurrent_onquery_detected`
- Helps identify problematic usage patterns

### Simplified Memory Management
**What changed:** Complete rewrite of memory saving from AI-based merging to direct file append
**Impact:** Memory operations are now 10-100x faster and much more reliable

### Optimized Imports
**What changed:** Switched from full module imports to specific function imports
**Impact:** Reduced bundle size and improved startup performance

### Performance Threshold Updates
**What changed:** New memory and context management thresholds
**Impact:** Better handling of large contexts and improved memory efficiency
**Details:**
- Updated context size limits to 13000/20000 tokens
- Improved memory management for long-running sessions

### Fixed: StatusLine Feature Was Non-Functional
- **Issue:** StatusLine feature always returned false, making it completely unusable
- **Cause:** Logic error in feature detection function that ignored configuration
- **Resolution:** Properly checks for statusLine configuration and enables feature
- **Affected users:** Anyone trying to use statusLine in v1.0.70

### Fixed: Memory Saving Could Fail Unpredictably
- **Issue:** Memory additions would sometimes fail with "No tool use found" errors
- **Cause:** Complex AI-based approach that required perfect tool responses
- **Resolution:** Simplified to direct file append operations
- **Affected users:** Users frequently saving memories

### Fixed: Potential Race Conditions in Concurrent Queries
- **Issue:** Multiple simultaneous queries could cause undefined behavior
- **Cause:** No protection against concurrent execution
- **Resolution:** Added detection and tracking of concurrent queries
- **Affected users:** Users triggering rapid commands or using automation

### Fixed: Unused Dependencies and Code Cleanup
- **Issue:** Importing entire modules when only specific functions were needed
- **Resolution:** Changed to named imports for crypto, stream, and process modules
- **Affected users:** All users benefit from smaller bundle size

### Code Organization
- Removed deprecated memory management functions (`AuB`, `lhB`, `l$8`)
- Cleaned up unused variables (`uw2`, `ZG8`, `GG8`, `FG8`)
- Reorganized GitHub Actions workflow variables for consistency

### Performance Optimizations
- Switched to named imports for better tree-shaking
- Updated memory thresholds for improved performance
- Added context management feature flag for future API support
