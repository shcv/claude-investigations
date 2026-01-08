# Changelog for version 1.0.78

## Highlights
Claude Code 1.0.78 introduces enhanced security for authentication tokens, a completely refactored permission system with three-tier control, and renames "output modes" to "output styles" for clarity. The update also adds support for a new Sonnet model with 1M context and implements infrastructure for A/B testing and dynamic configuration.

### File Descriptor Authentication for Enhanced Security
**What:** Authentication tokens can now be passed via file descriptors instead of environment variables
**How to use:**
```bash
# Pass token through file descriptor (more secure)
export CLAUDE_CODE_WEBSOCKET_AUTH_FILE_DESCRIPTOR=3
exec 3< <(echo "your-token-here")
claude

# Traditional method still supported
export CLAUDE_CODE_SESSION_ACCESS_TOKEN="your-token-here"
claude
```
**Details:**
- Prevents tokens from appearing in process listings or environment dumps
- Reads token from `/proc/self/fd/<number>` on Linux systems
- Falls back to environment variable for backward compatibility
- Provides clear error messages for invalid file descriptors

### Three-Tier Permission System
**What:** New granular permission options for file operations
**How to use:**
When Claude requests file permissions, you now have three options:
- **Accept once** - Permission for this operation only
- **Accept for session** (Shift+S) - Permission for all operations this session
- **Accept for project** (Shift+A) - Persistent permission for this project
**Details:**
- Different options appear based on whether files are inside or outside your project
- Project-level permissions are saved to your local settings
- Read operations don't offer project-level write permissions
- Clearer distinction between temporary and persistent permissions

### Sonnet Model with 1M Context
**What:** New high-context variant of Claude 3.5 Sonnet with 1 million token context window
**Details:**
- Available as "Sonnet (1M context)" option
- Uses rate limits faster than standard models
- Access may be gated based on account type or feature flags
- Provides extended context for working with very large codebases

### Simplified Onboarding Experience
**What:** New streamlined onboarding for first-time users
**Details:**
- Shows "new-user-warmup" flow for users with fewer than 10 app startups
- Controlled via `cc_simple_onboarding` experiment flag
- More focused introduction compared to standard onboarding
- Automatically selected based on usage patterns

### Output Modes Renamed to Output Styles
**What changed:** The entire "output modes" feature is now called "output styles"
**Impact:** 
- Directory structure changed from `~/.claude/output-modes/` to `~/.claude/output-styles/`
- Built-in options renamed: "Insights" → "Explanatory", "Learn By Doing" → "Learning"
- Clearer terminology that better reflects the feature's purpose
- Agent type renamed from `output-mode-setup` to `output-style-setup`

### Dynamic Model Configuration
**What changed:** Models can now be configured remotely via Statsig
**Impact:**
- Claude Code can receive model updates without requiring new releases
- Supports time-based feature gating for gradual rollouts
- Enables A/B testing of different model configurations
- External overrides respect user's first usage date to prevent unexpected changes

### Enhanced Agent Configuration
**What changed:** Agent definitions now include source tracking
**Impact:**
- Agents now specify their source: `built-in`, `localSettings`, or `projectSettings`
- Better management and display of agent origins
- Statusline setup agent now recommends skipping optional git locks for better performance

### Improved Permission Storage
**What changed:** Simplified and more reliable permission persistence
**Impact:**
- Clear tracking of permission sources (session vs persistent)
- New helper functions for managing directory permissions
- Automatic addition of allowed directories to settings
- Better handling of permissions for files outside project directory

### Fixed: Stdin Terminal Mode Cleanup
- **Issue:** Terminal raw mode wasn't properly cleaned up on exit
- **Resolution:** Added `Ao4()` function to properly reset stdin terminal mode and unref the stream

### Fixed: Enterprise Account Detection
- **Issue:** Enterprise and team accounts weren't properly detected for feature gating
- **Cause:** Missing logic to check account type in conjunction with environment flags
- **Resolution:** New `BL6()` function correctly identifies enterprise/team accounts

### Fixed: Model Selection Logic
- **Issue:** Model selection didn't properly handle all user access scenarios
- **Cause:** Complex conditional logic without proper fallback chain
- **Resolution:** Refactored into cleaner function chain with proper override points
