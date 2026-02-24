# Changelog for version 2.1.45


## Summary

This release updates the default model from Sonnet 4.5 to Sonnet 4.6 across the application, adds preview/markdown support for AskUserQuestion options to help users compare visual options, and introduces improved output truncation handling for long-running bash commands. The release also includes enhanced sandbox documentation, URL elicitation support for MCP tools, and new settings for customizing sandbox paths.


### AskUserQuestion Preview/Markdown Support

What: When asking users questions with multiple options, Claude Code can now display a markdown preview pane to show code snippets, ASCII mockups, or diagrams alongside each option.

Usage: When an option in AskUserQuestion includes a `markdown` field, the UI switches to a side-by-side layout with options on the left and a preview panel on the right.

Details:
- Previews are displayed in a monospace box when an option is focused
- Supports multi-line text with newlines for ASCII art, code, or diagrams
- Only supported for single-select questions (not multiSelect)
- Users can also add free-text notes on their selection via the `n` key

Evidence: AskUserQuestion option schema now includes `markdown` field (search for `"Optional preview content shown in a monospace box"`)


### User Notes on Question Selections

What: Users can now add free-text notes to their selections when answering AskUserQuestion prompts.

Details:
- Press `n` to add notes on a selected option
- Notes are captured in the response via `annotations` field
- Useful for providing context about why a particular option was chosen

Evidence: New annotations schema (search for `"Free-text notes the user added to their selection"`)


### URL Elicitation for MCP Tools

What: MCP tools can now request that users open a URL (e.g., for OAuth flows) and wait for completion before continuing.

Details:
- Supports error code -32042 for URL elicitation requests
- Shows the URL to the user with options to "Reopen URL", "Continue without waiting", or "Skip confirmation"
- Handles completion notifications from MCP servers when the user finishes the URL flow
- If the user cancels, the tool receives a message explaining the cancellation

Evidence: URL elicitation handler (search for `"requires URL elicitation (error -32042"`)


### Custom Spinner Tips

What: A new setting allows overriding the default spinner tips with custom messages.

Usage: Configure in settings with `tips` (array of strings) and optional `excludeDefault` (boolean) to hide default tips.

Evidence: New setting description (search for `"Override spinner tips. tips: array of tip strings"`)


### Enhanced Sandbox Path Settings

What: New settings allow configuring additional paths for sandbox read/write permissions.

Details:
- `sandboxExtraAllowWritePaths`: Additional paths to allow writing within the sandbox
- `sandboxExtraDenyReadPaths`: Additional paths to deny reading within the sandbox
- `sandboxExtraDenyWritePaths`: Additional paths to deny writing within the sandbox
- These merge with paths from permission rules (Read/Edit allow/deny)

Evidence: New settings descriptions (search for `"Additional paths to allow writing within the sandbox"`)


### Agent Teams Flag

What: A new experimental `--agent-teams` CLI flag enables agent team functionality.

Usage:
```bash
claude --agent-teams
```

Details:
- Sets `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` environment variable
- Enables coordinated multi-agent workflows

Evidence: CLI flag handler (search for `"--agent-teams"`)


### Default Model Updated to Sonnet 4.6

The default model throughout Claude Code has been updated from Sonnet 4.5 to Sonnet 4.6, including:
- Model selection descriptions now reference Sonnet 4.6
- 1M context window options updated to Sonnet 4.6
- Haiku description now compares to Sonnet 4.6 instead of 4.5
- Plan mode hybrid option now uses "Opus 4.6 in plan mode, Sonnet 4.6 otherwise"

Evidence: Model descriptions updated (search for `"Sonnet 4.6 - best for everyday tasks"`)


### Improved Sandbox Temporary Directory Documentation

What: The Bash tool system prompt now provides clearer guidance on using temporary directories in sandbox mode.

Details:
- Now recommends using `$TMPDIR` environment variable instead of hardcoded `/tmp/claude`
- Notes that TMPDIR is automatically set to the correct sandbox-writable directory
- Advises that most programs respecting TMPDIR will automatically use the correct directory

Evidence: Updated bash system prompt (search for `"TMPDIR is automatically set to the correct sandbox-writable directory"`)


### Output Truncation for Large Bash Command Output

What: Long-running bash commands that produce large output now handle truncation more gracefully.

Details:
- Output is automatically spilled to disk when it exceeds the inline limit (8MB default)
- Shows truncation message with total size: "Output truncated (XXX KB total)"
- Earlier output is omitted with a message indicating how much was skipped
- Full output is saved to a file for later retrieval

Evidence: Output truncation handler (search for `"Output truncated ("`, `"KB of earlier output omitted"`)


### Enhanced Memory Recall Display

What: Improved display text for memory recall operations.

Details:
- Changed from "Recalled" to "Potentially relevant memory" for proactive memory suggestions
- Clearer distinction between recalled memories and potentially relevant memories

Evidence: New memory display strings (search for `"Potentially relevant memory:"`)


### Improved Mobile Integration Messaging

What: Updated messaging for mobile integration feature.

Details:
- Changed from "Use /mobile to get Claude on your phone" to clearer phrasing
- New messages: "Code everywhere with the Claude app" and "Continue coding in the Claude app"
- QR code instructions now include keyboard shortcut: "space for QR code"

Evidence: Mobile integration strings (search for `"/mobile to use Claude Code from the Claude app on your phone"`)


### Extra Usage Billing Labels

What: Added clearer labels for when usage is billed as extra usage or at premium rates.

Details:
- Shows "Billed as extra usage" indicator for 1M context models when applicable
- Shows "Billed at premium rate" for premium tier usage

Evidence: Billing label strings (search for `"Billed as extra usage"`)


### Effort Setting Description Updated

What: The Opus 4.6 effort setting description has been expanded to better explain the trade-offs.

Before: "Effort lets you control thinking intensity in Opus 4.6."
After: "Effort lets you control the trade off between response thoroughness and token efficiency for Opus 4.6. Higher effort levels offer higher capability, and lower levels tend to use fewer tokens to optimize..."

Evidence: Updated effort description (search for `"Effort lets you control the trade off between response thoroughness"`)


### Plugin Path Variable Handling on Windows

What: Fixed handling of `${CLAUDE_PLUGIN_ROOT}` variable replacement on Windows to correctly handle backslash path separators.

Evidence: Path replacement function now converts backslashes to forward slashes on Windows (search for `"win32" ? q.replace(/\\\\/g, "/")"`)


## Bug Fixes

- Fixed potential issue with semver comparison functions to use Bun's native implementation when available (search for `"Bun.semver"`)
- Removed dependency on js-yaml library (many YAML-related error strings removed from the codebase)
- Fixed JSON schema validation code paths (removed $ref pointer error handling that was causing issues)
- Improved rate limit event handling in SDK message adapter (search for `"Ignoring rate_limit_event message"`)


## Notes

This release removes several internal dependencies including the full js-yaml library and json-schema-ref-parser, replaced with more streamlined implementations. Users upgrading from versions using Sonnet 4.5 will automatically use Sonnet 4.6 as the default model.
