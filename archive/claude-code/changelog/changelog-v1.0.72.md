# Changelog for version 1.0.72

## Highlights
Claude Code 1.0.72 introduces a new `/statusline` command for customizing your terminal status line, enhances security with improved path validation, and provides clearer visual indicators for different operational modes.

### Status Line Configuration Command
**What:** New `/statusline` command for customizing Claude Code's status line UI
**Why:** Allows users to personalize their terminal experience and display custom information in the status line
**How to use:**
```bash
# Configure status line from your shell PS1
/statusline

# Configure with custom command
/statusline "Configure my custom status display"
```
**Details:**
- Creates a specialized "statusline-setup" agent to handle configuration
- Can read and convert existing shell PS1 configurations
- Saves custom scripts to `~/.claude/statusline-command.sh` if needed
- Updates settings in `~/.claude/settings.json`

### Enhanced Mode Display System
**What:** Improved visual indicators for different Claude Code operational modes
**Why:** Makes it clearer which mode Claude Code is operating in, improving user awareness and control
**How to use:**
The mode display is automatic and shows in the interface with distinct icons and colors:
- **Default mode**: "Default" - standard operation
- **Plan mode**: "Plan" with ⏸ icon - planning before execution
- **Accept Edits mode**: "Accept" with ⏵⏵ icon - auto-accepting file edits
- **Bypass Permissions mode**: "Bypass" with warning styling - security restrictions bypassed
**Details:**
- Color-coded indicators (text, planMode, autoAccept, error)
- Clear visual distinction between modes
- Better integration with status line

### Improved Path Security Validation
**What:** Enhanced validation for file system commands with clearer security messages
**Why:** Provides better security boundaries and more helpful error messages when paths are restricted
**How to use:**
Path validation is automatic for commands like `cd`, `ls`, and `find`. When blocked, you'll see specific messages like:
```
cd in '/restricted/path' was blocked. For security, Claude Code may only 
change directories to the allowed working directories for this session: [list]
```
**Details:**
- Better handling of glob patterns (`*`, `?`, `[`, `]`, `{`, `}`)
- Proper tilde expansion (`~` and `~/` paths)
- Improved handling of relative paths with `..`
- More specific error messages for each command type

### Agent File Validation
**What changed:** Better error reporting for invalid agent configuration files
**Impact:** Clearer error messages when agent files are missing required fields or have invalid configurations, making it easier to debug custom agents

### Token Usage Tracking
**What changed:** More accurate calculation of token usage including cache tokens
**Impact:** Better cost tracking with separate accounting for cached vs uncached tokens, providing more accurate usage reports

### Background Shell Display
**What changed:** New component for displaying running background shells in the UI
**Impact:** Better visibility of background processes with indicators showing shell count and status

### Fixed: Path validation edge cases
- **Issue:** Certain path patterns with glob characters or parent directory references were not properly validated
- **Resolution:** Improved regex patterns and path resolution logic to handle all edge cases correctly

### Fixed: Module import cleanup
- **Issue:** Unused imports from crypto and stream modules were left in the codebase
- **Resolution:** Removed unused imports and reorganized module dependencies for cleaner code

### Fixed: Agent frontmatter parsing
- **Issue:** Missing or invalid frontmatter fields in agent files produced unclear error messages
- **Resolution:** Added specific validation and error reporting for required fields (name, description, model)
