# Changelog for version 2.1.6


## Summary

This release introduces git token injection for private repository cloning, a new `/keybindings` command for keyboard shortcut customization, enhanced `/stats` with date range filtering, and improved "add directory to workspace" with tab completion. The internal command explanation system has been refactored to use tool-based structured output, and the cache warming feature has been removed.


### Git Token Injection for Private Repository Cloning
What: Claude Code now automatically injects authentication tokens when cloning HTTPS repositories, supporting GitHub, GitLab, and Bitbucket.

Usage: Set the appropriate environment variable and clone private repositories seamlessly:
```bash
export GITHUB_TOKEN=your_token
# Or: GH_TOKEN, GITLAB_TOKEN, GL_TOKEN, BITBUCKET_TOKEN
```

Details:
- Automatically detects authentication failures and retries with token injection
- Supports `GITHUB_TOKEN`/`GH_TOKEN` for github.com
- Supports `GITLAB_TOKEN`/`GL_TOKEN` for gitlab.com and GitLab self-hosted instances
- Supports `BITBUCKET_TOKEN` for bitbucket.org
- Tokens in error messages are automatically redacted for security
- Preserves `SSH_AUTH_SOCK` for SSH key agent forwarding

Evidence: `K55()` at line 299739 (token injection logic, contains `"Injecting GitHub token into clone URL"`)


### Keybindings Command
What: New `/keybindings` command to open or create a keybindings configuration file for customizing keyboard shortcuts.

Usage:
```
/keybindings
```

Details:
- Opens or creates `~/.config/claude-code/keybindings.json`
- Template includes syntax documentation for modifiers (ctrl, alt, shift, meta)
- Supports chord shortcuts like `"ctrl+k ctrl+s"`
- File is automatically reloaded when saved
- Documents reserved keys (ctrl+c, ctrl+d) and terminal conflicts (ctrl+b, ctrl+a, ctrl+z)
- Feature is currently in preview and may need to be enabled

Evidence: `iD7()` at line 497353 (command implementation, contains `"keybindings"`)


### Stats Date Range Filtering
What: The `/stats` command now supports filtering by date range with a keyboard shortcut to cycle through options.

Usage: Press `r` while viewing stats to cycle through:
- All time (default)
- Last 7 days
- Last 30 days

Details:
- Displays loading indicator when fetching filtered stats
- Shows "r to cycle dates" in the help text
- Caches fetched date ranges for faster switching

Evidence: `MC7()` at line 521418 (stats dialog, contains `"r to cycle dates"`)


### Numpad Key Support
What: Added support for numeric keypad keys in the input handling system.

Details:
- Supports numpad digits 0-9 (codes 57399-57408)
- Supports numpad operators: `.` `/` `*` `-` `+` `=`
- Supports numpad Enter key

Evidence: `KW8()` at line 212920 (key code handler, contains cases 57399-57415)


### Add Directory Dialog with Tab Completion
The "add directory to workspace" dialog now includes path autocomplete functionality with tab completion.

Details:
- Press Tab to autocomplete the current directory suggestion
- Shows directory suggestions as you type
- Navigate suggestions with up/down arrows or ctrl+p/ctrl+n
- Help text updated to: "Tab to complete · Enter to add · Esc to cancel"

Evidence: `mz1()` at line 489858 (add directory component, contains `"Tab to complete"`)


### Version Information Display
The `/version` command now shows both stable and latest versions from npm dist-tags and GCS.

Details:
- Fetches version info from npm with `--prefer-online` flag
- Falls back to GCS storage for version information
- Displays "Stable version" and "Latest version" separately

Evidence: `zD7()` at line 495798 (version display, contains `"Stable version"`, `"Latest version"`)


### MCP Logging Infrastructure
Added structured logging for MCP (Model Context Protocol) server errors and debug messages.

Details:
- New `logMCPError()` and `logMCPDebug()` functions for server-specific logging
- MCP logs stored separately per server in `mcp-logs-{serverName}` directories
- Error log sink initialization with buffering for early errors before sink is ready

Evidence: `Lq9()` at line 536969 (error log sink initialization, contains `logMCPError`, `logMCPDebug`)


### Command Explanation Tool Refactoring
The shell command explanation system has been refactored from structured outputs to a tool-based approach.

Details:
- Now uses `explain_command` tool with explicit JSON schema
- Cleaner separation between explanation, reasoning, and risk assessment
- Simplified system prompt: "Analyze shell commands and explain what they do, why you're running them, and potential risks."

Evidence: `zE5` at line 2256 (tool definition, contains `"explain_command"`)


### ExitPlanMode Permission Requests
When exiting plan mode, Claude can now request prompt-based bash permissions that will be pre-approved for the session.

Details:
- New `allowedPrompts` parameter accepts semantic descriptions of actions
- Example: `{"tool": "Bash", "prompt": "run tests"}` matches npm test, pytest, etc.
- Permissions are session-scoped and cleared when the session ends
- Guidelines encourage narrow, security-conscious permission scoping

Evidence: `jE2` at line 2362 (ExitPlanMode description, contains `"allowedPrompts"`)


### Extended Book Comparison List for Stats
The `/stats` comparison feature now includes more books for token usage comparison.

Details: Added 10 new books including "The Little Prince", "A Christmas Carol", "Fahrenheit 451", "Slaughterhouse-Five", "The Catcher in the Rye", "Dune", "Moby-Dick", "Crime and Punishment", "A Game of Thrones", "The Count of Monte Cristo", and "Les Misérables".

Evidence: `_C7` at line 4141 (book list array)


### Extended Time Comparison List for Stats
Added more time-based comparisons for session duration statistics.

Details: Added comparisons including "listening to Abbey Road", "a yoga class", "a World Cup soccer match", "watching Titanic", and "a full night of sleep".

Evidence: `jC7` at line 4167 (time comparison array)

## Bug Fixes

- Fixed path truncation for long file paths in autocomplete suggestions with smart ellipsis placement (`ItQ()` at line 139331, preserves filename visibility)


### Cache Warming
The cache warming feature has been completely removed.

Details:
- Removed `Dr5()` cache warming configuration function
- Removed `In2()` cache warming hook
- Removed `tengu_cache_warming_request` telemetry
- Removed agent warmup functionality (`iU9`, `yS0` functions)

Evidence: Removal of functions at lines 437535-437845 in v2.1.5


### Terminal Progress Bar
The terminal progress bar component has been removed from the UI.

Details:
- Removed `kbA()` progress bar rendering function
- Removed `G21()` ink-progress component
- Removed progress state tracking (`rUB`, `Z00`, `$K8` functions)

Evidence: Removal of `ink-progress` element handling


### BTW Side Questions [In Development]
What: A quick side question feature allowing users to ask tangential questions without interrupting the main conversation flow.

Status: Stubbed - command infrastructure exists but `isEnabled` returns `false`.

Details:
- Registered as `/btw` command
- Description: "Ask a quick side question without interrupting the main conversation"
- Side question infrastructure (API calls, response handling) already exists from previous versions
- Parser function returns `{ isBtw: !1 }` (always false)

Evidence: `bW7` at line 3694 (btw command definition, `isEnabled: () => !1`)
