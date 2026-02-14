# Changelog for version 1.0.86

## Highlights
Version 1.0.86 introduces a context usage visualization command, enhances file permission handling with intelligent suggestions and git config protection, and improves the trust dialog UI for better clarity and security awareness.


### Context Usage Visualization
**What:** New `/context` command that displays current token usage as a colored grid
**How to use:**
```bash
# In your Claude Code session, type:
/context
```
**Details:**
- Shows a visual grid where each square represents a portion of your context window
- Different colors indicate different categories (system prompt, tools, messages, etc.)
- Displays detailed breakdowns including memory files, MCP tools, and custom agents
- Grid size adapts based on model capacity (20x10 for ≥1M token models, 10x10 otherwise)
- Helps identify what's consuming context and why you might hit limits


### Git Configuration File Protection
**What:** Added security protection for `.git/config` and `.gitconfig` files
**How to use:**
```bash
# Claude will now ask for explicit permission before editing:
# - .git/config files in repositories
# - .gitconfig files (global git configuration)
```
**Details:**
- Prevents potential code execution via git configuration files
- Requires explicit user permission to edit these sensitive files
- Protection covers both repository-level and global git configurations
- Provides clear explanation about why permission is needed


### Intelligent Permission Suggestions
**What:** Context-aware suggestions when Claude requests file permissions
**How to use:**
```bash
# When Claude needs file access, you'll see smart suggestions like:
# For reading: "Allow reading from /directory/** during this session"
# For writing: "Allow all edits in /directory/ during this session"
```
**Details:**
- Different suggestions for read vs write operations
- Suggests appropriate permission scope based on the operation
- Can suggest switching to "acceptEdits" mode for write operations
- Provides rules that can be applied to efficiently grant permissions


### Enhanced Trust Dialog
**What changed:** Simplified and consolidated the project trust dialog
**Previous behavior:** Multiple separate warnings with complex dynamic options
**New behavior:** Single unified warning with clear execution source listing
**Impact:** 
- Clearer messaging about security risks
- Better organization showing what allows execution (MCP servers, settings files, commands)
- Simplified to just "Yes, proceed" or "No, exit" options
- Shows configuration sources in a more digestible format


### Todo List Persistence
**What changed:** Todos are now saved to disk when modified
**Previous behavior:** Todos only existed in memory during the session
**New behavior:** Todos persist to JSON files on disk (though not automatically loaded on restart)
**Impact:**
- Todo changes are saved for potential future recovery
- TodoWrite tool now enforces keeping at least one task in_progress
- Visual feedback simplified - completed tasks always show in green


### Todo List Feature Flag System
**What changed:** TodoWrite tool now controlled by runtime feature flag instead of hardcoded visibility
**Previous behavior:** TodoWrite had hardcoded visibility conditions
**New behavior:** Todo list visibility controlled by `todoFeatureEnabled` feature flag (defaults to disabled)
**Implementation:** Tool inclusion controlled by dynamic feature flag system rather than hardcoded conditions
**Impact:**
- Todos become opt-in feature rather than always-on
- Tool functionality remains fully implemented but filtered out at runtime by default
- Users must explicitly enable todo feature to see todo list management
- Creates configurable task management system
- Todos still persist to disk and function when enabled


### Smart Todo Display (Hidden Implementation)
**What changed:** Improved todo list visualization with intelligent truncation (for internal use)
**Previous behavior:** Simple list display without truncation
**New behavior:** Shows up to 4 most relevant items with counts for hidden items
**Impact:** (Note: These improvements exist in code but users never see them due to display removal)
- Prioritizes showing in-progress tasks
- Displays "... +N done" for multiple completed tasks
- Shows "... +N more" for remaining tasks
- Would keep focus on active work while maintaining context (if visible)


### Permission Prompt Clarity
**What changed:** Operation-specific permission messages
**Previous behavior:** Generic permission messages for all operations
**New behavior:** Different messages for read vs write operations
**Impact:**
- "Allow reading from /directory/" for read operations
- "Allow all edits in /directory/" for write operations
- Clearer about what permissions are being granted
- Better session-based permission options


### Attachment Message Grouping
**What changed:** Improved handling of file attachments in conversations
**Previous behavior:** Attachments could be separated from their context
**New behavior:** Attachments are properly grouped with associated messages
**Impact:**
- File attachments stay with their relevant assistant or user messages
- Prevents context loss when processing conversations with attachments
- Better message organization for complex conversations


### Fixed: Spinner Words Configuration Structure
- **Issue:** Spinner words were stored as a plain array limiting extensibility
- **Cause:** Original implementation didn't account for future configuration needs
- **Resolution:** Restructured as an object with `words` property allowing future expansion
- **Affected versions:** All versions prior to 1.0.86
