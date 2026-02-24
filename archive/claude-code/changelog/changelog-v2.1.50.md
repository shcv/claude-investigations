# Changelog for version 2.1.50


## Summary

This release introduces the new `/diff` command for viewing uncommitted changes and per-turn diffs, adds VCS-agnostic worktree isolation through configurable hooks (`WorktreeCreate`/`WorktreeRemove`), and includes improved handling for MCP servers that are still connecting. Several internal improvements enhance system sleep detection for WebSocket connections and add better logging for sandbox symlink handling on Linux.

### `/diff` Command
What: A new slash command to view uncommitted changes and per-turn file diffs directly in the CLI.

Usage:
```
/diff
```

Details:
- Opens a dialog showing uncommitted changes in your repository
- Displays per-turn diffs showing what changed during each interaction
- Provides a clear visual summary of file modifications

Evidence: Diff dialog slash command (search for `"View uncommitted changes and per-turn diffs"`)


### VCS-Agnostic Worktree Isolation via Hooks
What: Custom hooks for creating and removing worktrees, enabling worktree isolation to work with any version control system—not just Git.

Usage:
Configure hooks in your `settings.json`:
```json
{
  "hooks": {
    "WorktreeCreate": [{
      "command": "your-worktree-create-script"
    }],
    "WorktreeRemove": [{
      "command": "your-worktree-remove-script"
    }]
  }
}
```

Details:
- `WorktreeCreate` hook receives JSON input with `name` (suggested worktree slug); stdout should contain the absolute path to the created worktree
- `WorktreeRemove` hook receives JSON input with `worktree_path` (absolute path to worktree); exit code 0 indicates successful removal
- Enables worktree isolation for non-Git VCS systems (Mercurial, SVN, etc.)
- Error messages guide users when hooks are missing or fail

Evidence: Hook types and error messages (search for `"WorktreeCreate"`, `"WorktreeRemove"`, `"Configure WorktreeCreate/WorktreeRemove hooks"`)


### `/agents` Command for Listing Configured Agents
What: A new command to list all configured agents with their sources and status.

Usage:
```
/agents
```

Details:
- Shows agents grouped by source (User, Project, Local, Managed, Plugin, CLI arg, Built-in)
- Displays which agents are shadowed/overridden by higher-priority sources
- Shows model and memory settings for each agent

Evidence: Agent listing function (search for `"List configured agents"`, `"No agents found."`, `"shadowed by"`)


### Agent Worktree Isolation Option
What: Agents can now specify an `isolation` field to run in an isolated worktree.

Usage:
Agents can be configured with `isolation: "worktree"` to run in a temporary git worktree or hook-based worktree for isolated work.

Details:
- Creates an isolated copy of the repository for the agent to work on
- Supports both Git worktrees and custom hook-based worktrees
- Useful for agents that need to make changes without affecting the main working directory

Evidence: Isolation parsing in agent frontmatter (search for `"isolation"`, `"Isolation mode"`)

### Pending MCP Server Notification in ToolSearch
What: When searching for deferred tools, if some MCP servers are still connecting, the tool now reports which servers are pending.

Details:
- Results include `pending_mcp_servers` field when servers are still initializing
- Message indicates servers are connecting and tools will become available shortly

Evidence: Pending server handling (search for `"Some MCP servers are still connecting"`, `"pending_mcp_servers"`)


### System Sleep Detection for WebSocket Connections
What: Improved reconnection handling when the system wakes from sleep.

Details:
- Detects large time gaps between reconnection attempts indicating system sleep
- Resets the reconnection budget after sleep to avoid exhausting retries
- Adds periodic keep-alive frames for more reliable connection maintenance

Evidence: Sleep detection logic (search for `"Detected system sleep"`, `"resetting reconnection budget"`)


### Improved Bash Command Prefix Suggestions
What: More intelligent command prefix extraction for permission rules, with support for suggesting editable prefixes.

Details:
- Uses @withfig/autocomplete specs for better understanding of command structure
- Supports `pyright`, `timeout`, `sleep`, `alias`, `nohup`, `time`, and `srun` commands with proper argument parsing
- Permission prompts can show "Yes, and don't ask again for" with editable command prefix

Evidence: Fig autocomplete integration (search for `"@withfig/autocomplete"`, `"command prefix (e.g., npm run:*)"`)


### Enhanced Memory Prompts
What: Clearer organization of memory guidance with separate sections for explicit user requests.

Details:
- Added "Explicit user requests" section for remember/forget instructions
- More concise guidance on when to save memories
- Removed redundant "when in doubt" guidance

Evidence: Memory prompt changes (search for `"## Explicit user requests:"`)


### Linux Sandbox Symlink Safety
What: Better handling of symlinked write paths in the Linux sandbox.

Details:
- Skips symlink write paths that point outside expected locations
- Logs warnings when write paths cannot be resolved
- Prevents potential sandbox escapes via symlink manipulation

Evidence: Sandbox symlink handling (search for `"Skipping symlink write path pointing outside expected location"`)


### macOS Sandbox Unix Socket Permissions
What: More granular Unix socket permissions in the macOS sandbox.

Details:
- Changed from broad `network*` permission to specific `network-bind` and `network-outbound` for Unix sockets
- Adds `AF_UNIX` socket domain permission explicitly
- Improves security by limiting socket access to specific paths

Evidence: Sandbox socket rules (search for `"(allow system-socket (socket-domain AF_UNIX))"`)


### Improved Session Resume Telemetry
What: Better tracking of session resume performance and success/failure.

Details:
- Tracks resume duration in milliseconds
- Reports success/failure status for session resume operations
- Helps identify performance issues with session loading

Evidence: Resume telemetry (search for `"tengu_session_resumed"`, `"resume_duration_ms"`)


### CLAUDE_CODE_SIMPLE Mode Improvements
What: Enhanced behavior for CLAUDE_CODE_SIMPLE environment variable.

Details:
- Disables attachments when CLAUDE_CODE_SIMPLE is set
- Skips memory file loading for simplified operation
- Adds CWD and Date to system prompt in simple mode

Evidence: Simple mode checks (search for `"CLAUDE_CODE_SIMPLE"`)

## Bug Fixes

- Fixed issue where GitHub issue/PR references with fewer than 3 digits (e.g., `#12`) were incorrectly linkified; now only references with 3+ digits are processed (search for `/(?<!\w)#(\d{3,})\b/`)

- Fixed duplicate MCP tools when connecting to multiple servers that provide tools with the same name (search for `"wG([...Y6.mcp.tools"` — deduplication by name)

- Fixed memory leak in ring buffer `clear()` method that wasn't resetting the buffer array (search for `"this.buffer.length = 0"`)

- Removed "Penguin mode promo" discount display that was showing in the fast mode UI (search for removal of `Bl4` component)

- Fixed cleanup of LSP diagnostics that had already been sent as attachments (search for `"if (J.attachmentSent) j96.delete(O)"`)

- Removed the code diff footer feature flag and setting (`codeDiffFooterEnabled`) that was behind `tengu_code_diff_cli` - this functionality is now handled by the new `/diff` command

## Notes

The `/diff` command replaces the previous code diff footer that was shown at the bottom of the chat. Users who relied on the footer can now use `/diff` to view the same information on demand.
