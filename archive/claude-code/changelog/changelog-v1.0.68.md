# Changelog for version 1.0.68

Based on my analysis of the diff file for version 1.0.68, here is the detailed changelog:

# Claude Code v1.0.68 Changelog

## New Features

### 🚀 Teleport - Resume Sessions Across Machines
A powerful new `--teleport` feature allows you to resume Claude Code sessions from other machines or continue someone else's shared session.

**Usage:**
```bash
# Resume by session ID
claude --teleport abc123def456

# Resume from a URL
claude --teleport https://claude.ai/chat/abc123def456
```

**Features:**
- Automatically fetches conversation history from remote sessions
- Switches to the appropriate git branch if needed
- Offers to stash uncommitted changes before switching branches
- Supports custom headers via `TELEPORT_HEADERS` environment variable
- Validates authentication status before proceeding

**Environment Variables:**
- `TELEPORT_RESUME_URL`: Override the default URL for session resumption
- `TELEPORT_HEADERS`: Pass custom headers as JSON (e.g., `export TELEPORT_HEADERS='{"Authorization": "Bearer token"}'`)

### 🎨 Customizable Output Modes
Configure how Claude Code communicates with you by selecting from different output modes.

**Features:**
- Support for custom output modes stored in `.claude/output-modes/` directories
- Both user-level and project-level output mode configurations
- Interactive selection UI with up to 10 visible options (increased from 3)
- Dynamic loading with "Loading output modes..." indicator
- Each mode includes a description to help you choose

### 🔧 Enhanced Hooks Management
New global control over Claude Code's hook system for better troubleshooting and control.

**New Capability:**
- Disable all hooks globally without deleting your configuration
- Clear UI indicator when hooks are disabled showing:
  - Warning banner explaining hooks are disabled
  - Count of configured hooks that aren't running
  - Option to re-enable all hooks with one click

## Improvements

### 📝 Expanded Shell Command Support
10 new commands added to the safe command whitelist, allowing execution without approval prompts:

- `nl` - Number lines in files
- `hostname` - Display system hostname
- `arch` - Show system architecture
- `groups` - List user groups
- `nproc` - Display number of processors
- `basename` - Extract filename from path
- `dirname` - Extract directory from path  
- `realpath` - Resolve to absolute path
- `base64` - Encode/decode base64 data
- `file` - Determine file type

### 🛡️ Better Error Handling
- Improved shell execution with `shell: true` option for better compatibility
- Enhanced error messages with clearer explanations
- Try-catch blocks added to critical command execution paths
- Better timeout and cancellation handling for long-running commands

### 🎯 UI/UX Enhancements
- Loading states with descriptive messages throughout the interface
- Interactive prompts for git stash decisions during teleport
- Clearer permission descriptions for tool access levels
- Improved session selection UI when multiple sessions are available

## Technical Changes

### Removed Features
- Removed `NotebookRead` tool and related Jupyter notebook reading functionality
- Cleaned up unused imports for `node:stream`

### Command Execution Improvements
- New command tracking infrastructure with unique command IDs
- Enhanced verbose logging with timestamped output
- Escaped command strings for improved security
- Better handling of piped commands and multi-line output

## Breaking Changes
None - This release maintains backward compatibility with existing workflows.

## Notes
- The teleport feature requires a clean git working directory or will prompt to stash changes
- Custom output modes can be placed in `.claude/output-modes/` in your home or project directory
- The expanded shell command whitelist improves productivity for common system tasks while maintaining security
