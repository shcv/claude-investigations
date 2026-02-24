# Changelog for version 2.1.48


## Summary

This release introduces a major new worktree workflow for isolated development, adds HTTP hooks and a new ConfigChange hook event, and removes the experimental MCP-CLI feature. Users can now work in git worktrees with optional tmux integration, and exclude specific CLAUDE.md files using glob patterns.


### Git Worktree Mode

What: Create and work in isolated git worktrees directly from Claude Code, with full session management and cleanup prompts.

Usage:
```bash
# Start Claude Code with a new worktree
claude --worktree
claude -w

# Start with a named worktree
claude --worktree=my-feature

# Combine with tmux for parallel sessions
claude --worktree --tmux
```

Details:
- Creates a new git worktree in `.claude/worktrees/` with a dedicated branch based on HEAD
- Automatically switches the session's working directory to the worktree
- On session exit, prompts to keep or remove the worktree and associated tmux session
- Symlinks configured directories (like `node_modules`) from main repo to avoid disk bloat
- Copies `settings.local.json` and configures git hooks from the main repository
- The worktree branch is automatically deleted when removing the worktree

Evidence: New `-w, --worktree [name]` flag and CreateWorktree tool (search for `"Create a new git worktree for this session"`)


### CreateWorktree Tool

What: A new built-in tool that allows Claude to create worktrees mid-session when users request isolated work.

Usage:
```
User: "Start a worktree for this feature"
User: "Work in isolation on a separate branch"
```

Details:
- Tool activates when user asks to "work in isolation" or "start a worktree"
- Must be in a git repository and not already in a worktree
- Creates worktree with optional custom name
- Session automatically switches to the new worktree directory

Evidence: Tool description (search for `"Use this tool when the user asks to work in isolation"`)


### HTTP Hooks

What: A new hook type that sends HTTP POST requests instead of executing shell commands, enabling webhook-style integrations.

Usage (in settings.json or CLAUDE.md):
```json
{
  "hooks": {
    "PreToolUse": [{
      "type": "http",
      "url": "https://your-server.com/hook",
      "headers": {
        "Authorization": "Bearer $MY_TOKEN"
      },
      "timeout": 30
    }]
  }
}
```

Details:
- Supports environment variable expansion in headers (`$VAR_NAME` or `${VAR_NAME}` syntax)
- Configurable timeout per request
- JSON response parsing with optional logging
- Works with all hook events including the new ConfigChange event

Evidence: New http hook type definition (search for `"HTTP hook type"`)


### ConfigChange Hook Event

What: A new hook event that fires when configuration files change during a session, allowing validation and blocking of config changes.

Details:
- Fires when skills, settings, or CLAUDE.md files are modified
- Can block changes by returning exit code 2
- Input includes source (user_settings, project_settings, etc.) and file_path
- Useful for enforcing configuration policies

Evidence: New ConfigChange hook event (search for `"ConfigChange"`)


### CLAUDE.md Exclude Patterns

What: Exclude specific CLAUDE.md files from loading using glob patterns or absolute paths.

Usage (in settings.json):
```json
{
  "memory": {
    "excludePatterns": [
      "/home/user/monorepo/CLAUDE.md",
      "**/node_modules/**/CLAUDE.md",
      "**/some-dir/.claude/rules/**"
    ]
  }
}
```

Details:
- Uses picomatch for glob pattern matching
- Patterns match against absolute file paths
- Only applies to User, Project, and Local memory types (Managed/policy files cannot be excluded)

Evidence: New excludePatterns setting (search for `"Glob patterns or absolute paths of CLAUDE.md files to exclude from loading"`)


### Tmux Integration for Worktrees

What: Automatically create tmux sessions when starting worktrees, with iTerm2 native pane support.

Usage:
```bash
claude --worktree --tmux
claude -w --tmux=classic  # Use traditional tmux instead of iTerm2 integration
```

Details:
- Creates a tmux session for parallel worktree work
- Uses iTerm2 native panes when available for better integration
- Use `--tmux=classic` for traditional tmux behavior
- Session management options on exit: keep both, keep worktree only, or remove all

Evidence: New --tmux flag (search for `"Create a tmux session for the worktree"`)


### Model Capability Descriptions

What: Added explicit descriptions for model thinking capabilities in the schema.

Details:
- New `effortLevels` field describes available effort levels for models
- New `supportsAdaptiveThinking` field indicates whether a model supports adaptive thinking (Claude decides when and how much to think)

Evidence: New schema descriptions (search for `"Whether this model supports adaptive thinking"`)


### Git Diff for Issue Creation

What: Improved git diff generation when creating issues, with better handling of edge cases.

Details:
- Handles shallow clones gracefully with HEAD-only mode
- Falls back to HEAD-only mode when no remote or merge-base is found
- Captures untracked files with size limits (500MB per file, 5GB total)
- Excludes binary files from untracked file capture
- Filters out excessively large files automatically

Evidence: New shallow clone detection (search for `"Shallow clone detected, using HEAD-only mode for issue"`)


### MCP Server Authentication Caching

What: Caches MCP servers that need authentication to reduce redundant connection attempts.

Details:
- Stores needs-auth status in `mcp-needs-auth-cache.json`
- Skips connection attempts for cached servers
- Logged as "Skipping connection (cached needs-auth)"

Evidence: New cache file (search for `"mcp-needs-auth-cache.json"`)


### Background Agent UX Improvements

What: Better messaging for background agent management.

Details:
- New "Press again to kill all background agents" message for confirmation
- Clearer output file instructions

Evidence: New UI text (search for `"Press again to kill all background agents"`)


### IDE Opening Feedback

What: Better feedback when opening worktrees or projects in IDEs.

Details:
- Clearer messages for manual IDE opening
- Specific messaging for worktree vs project contexts

Evidence: New message handling (search for `"Please open the"`)


## Bug Fixes

- Fixed path traversal detection (search for `"path traversal detected"`)
- Added validation for non-empty strings and patterns (search for `"Expected a non-empty string"`)


### MCP-CLI Removed

What: The experimental `mcp-cli` command-line interface for MCP servers has been removed.

Details:
- The `ENABLE_EXPERIMENTAL_MCP_CLI` environment variable is no longer recognized
- The `mcp-cli` command (info, call, servers, tools, grep, resources, read) is removed
- MCP tools continue to work through the normal tool interface

Impact: If you relied on `mcp-cli` commands in bash scripts or hooks, migrate to using MCP tools through Claude's standard tool interface.

Evidence: Removal of mcp-cli infrastructure (removed strings: `"mcp-cli info"`, `"mcp-cli call"`, `"ENABLE_EXPERIMENTAL_MCP_CLI"`)


## Notes

The worktree feature requires being in a git repository and having git installed. Tmux integration requires tmux to be installed (`sudo apt install tmux` on Linux). iTerm2 users will get native pane integration when using `--tmux` without the `=classic` suffix.
