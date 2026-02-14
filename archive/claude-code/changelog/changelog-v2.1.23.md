# Changelog for version 2.1.23


## Summary

This release adds a ripgrep search timeout with graceful error handling, introduces an in-app auto-update configuration dialog, adds customizable spinner verbs for personalized UI, and implements significant infrastructure improvements including WebSocket-based direct connect mode, pipelined speculation for faster responses, and a prompt cache break debugging system. The security policy for code analysis has been updated to better support authorized security testing scenarios.


### Ripgrep Search Timeout Handling
What: Ripgrep searches now have a timeout (20 seconds, or 60 seconds on WSL) with graceful error handling that returns partial results.

Details:
- Searches that take too long will now fail gracefully with a `RipgrepTimeoutError`
- Partial results found before timeout are preserved and returned
- Clear error message: "The search may have matched files but did not complete in time. Try searching a more specific path or pattern."

Evidence: `fz8` class at line 31473 (contains `"RipgrepTimeoutError"` and `"Ripgrep search timed out after"`)


### In-App Auto-Update Configuration
What: New dialog to enable or disable auto-updates directly from within Claude Code, with channel selection.

Usage: Access through the settings interface to configure auto-updates.

Details:
- Choose between "Enable with latest channel" or "Enable with stable channel"
- When auto-updates are controlled by environment variables (`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` or `DISABLE_AUTOUPDATER`), the dialog shows a message explaining this and how to re-enable

Evidence: UI component at line 488151 (contains `"Enable Auto-Updates"`, `"Enable with latest channel"`, `"Enable with stable channel"`)


### Customizable Spinner Verbs
What: New configuration option to customize the spinner verbs shown during Claude's thinking phase.

Usage: Add to your settings:
```json
{
  "spinnerVerbs": {
    "mode": "append",
    "verbs": ["Pondering", "Contemplating", "Musing"]
  }
}
```

Details:
- `mode: "append"` - adds your verbs to the default list
- `mode: "replace"` - uses only your custom verbs
- Empty verbs array with replace mode falls back to defaults

Evidence: Schema definition at line 552840 (contains `"spinnerVerbs"`, `'Customize spinner verbs. mode: "append" adds verbs to defaults, "replace" uses only your verbs.'`)


### Toggle Terminal Keybinding
What: New `app:toggleTerminal` keyboard action added to the available keybindings.

Details:
- Adds a new action for toggling terminal view
- Can be bound to a custom key combination in keybindings configuration

Evidence: Action registered at line 560172 (contains `"app:toggleTerminal"`)


### WebSocket Direct Connect Mode
What: Infrastructure for connecting directly to a remote Claude Code server via WebSocket.

Details:
- New `useDirectConnect` hook manages WebSocket connections
- Handles connection lifecycle: connecting, connected, disconnected, errors
- Supports permission request forwarding from remote sessions
- Provides clear error messaging for connection failures

Evidence: `useDirectConnect` hook at line 586518 (contains `"[useDirectConnect] Connecting to"`, `"WebSocket connection error"`, `"Server disconnected."`)


### Updated Security Policy for Code Analysis
The system prompt for security-related tasks has been expanded to better support legitimate security work:

**Previous policy**: "Assist with defensive security tasks only"

**New policy**: "Assist with authorized security testing, defensive security, CTF challenges, and educational contexts"

Details:
- Now explicitly allows: pentesting engagements, CTF competitions, security research, defensive use cases
- Still refuses: destructive techniques, DoS attacks, mass targeting, supply chain compromise, detection evasion for malicious purposes
- Dual-use security tools (C2 frameworks, credential testing, exploit development) require clear authorization context

Evidence: Policy string at line 550045 (contains `"authorized security testing"`, `"CTF challenges"`)


### Prompt Cache Break Debugging
What: New detailed logging when prompt caching breaks, helping identify why cache misses occur.

Details:
- Logs when cache breaks due to: model changes, system prompt changes (with character delta), tool schema changes
- Format: `[PROMPT CACHE BREAK] system prompt changed (+123 chars) [source=X, call #Y, cache read: A → B, creation: C]`
- Useful for debugging unexpected cache misses in long sessions

Evidence: Logging at line 266957 (contains `"[PROMPT CACHE BREAK]"`, `"system prompt changed"`, `"tools changed"`, `"model changed"`)


### Pipelined Speculation System
What: New speculative execution system that pre-generates suggestions before they're needed.

Details:
- Generates pipelined suggestions asynchronously during interaction
- Promotes cached suggestions when user input matches predictions
- Stops speculation at denied tools to avoid wasted work
- Debug logging: `[Speculation] Pipelined suggestion: "..."`, `[Speculation] Promoting pipelined suggestion: "..."`

Evidence: Speculation logic at line 457819 (contains `"[Speculation] Pipelined suggestion:"`, `"[Speculation] Promoting pipelined suggestion:"`, `"[Speculation] Stopping at denied tool:"`)


### Enhanced Fork Agent Logging
What: Forked agents now log detailed progress information for debugging.

Details:
- Logs transcript recording events
- Tracks message counts and types received
- Reports final usage statistics including cache read/create tokens
- Format: `Forked agent [name] finished: N messages, types=[...], totalUsage: input=X output=Y cacheRead=Z cacheCreate=W`

Evidence: Logging at line 421675 (contains `"Forked agent ["`, `"cacheCreate="`, `"total sent)"`)


### Dynamic Skills Loading via Attachments
What: Skills can now be loaded dynamically and sent to the model via attachments rather than in the initial prompt.

Details:
- Reduces initial prompt size by loading skills on-demand
- Logs: `Sending N skills via attachment (initial/dynamic, X total sent)`
- Skills are formatted with a header: "The following skills are available for use with the Skill tool"

Evidence: Skills handling at line 463656 (contains `"skills via attachment"`, `"The following skills are available for use with the Skill tool"`)


### GitHub PR State Field
What: PR view commands now include the `state` field in addition to existing fields.

Details:
- `gh pr view --json` now fetches: `number,url,reviewDecision,isDraft,headRefName,state`
- Previously only fetched: `number,url,reviewDecision,isDraft,headRefName`
- Enables better PR status detection (open, closed, merged)

Evidence: GH command at line 578119 (contains `"number,url,reviewDecision,isDraft,headRefName,state"`)


### Improved Windows Process Ancestor Detection
What: PowerShell-based process ancestor detection now retrieves the full ancestor chain in a single call.

Details:
- Uses a more efficient PowerShell script that walks the process tree in one execution
- Retrieves both process IDs and command lines for ancestors
- Timeout increased from 1 second to 3 seconds for reliability

Evidence: PowerShell script at line 198756 (contains `"$currentPid ="`, batched ancestor retrieval logic)


### Improved API Error Logging
What: API errors now include attempt numbers and more detailed error information.

Details:
- Format: `API error (attempt N/M): status message`
- Includes full status code and message for Anthropic API errors
- Helps diagnose retry behavior and transient failures

Evidence: Error logging at line 325950 (contains `"API error (attempt"`)


### Effort Level UI Improvements
What: The effort level selector now shows when effort is not supported for the current model.

Details:
- Displays "Effort not supported" when the model doesn't support effort configuration
- Shows arrow key hint: "← → to adjust" when effort is supported
- Optional model name shown: "Effort not supported for {model}"

Evidence: UI at line 486241 (contains `"Effort not supported"`, `"← → to adjust"`)


### Better useAppState Error Messages
What: Improved error messages for incorrect usage of the `useAppState` hook.

Details:
- Combined error for both `useAppState` and `useSetAppState`: "useAppState/useSetAppState cannot be called outside of an <AppStateProvider />"
- New error when selector returns the whole state: "Your selector in `useAppState(...)` returned the original state, which is not allowed. You must instead return a property for optimised rendering."

Evidence: Error handling at line 476661 (contains `"useAppState/useSetAppState cannot be called outside"`, `"Your selector in \`useAppState("`)


### Teammate Message UI Improvements
What: Simplified teammate message notifications in the UI.

Details:
- Changed from verbose "Queued teammate X:" to brief notification with sender's name
- Changed from text-based "Agent idle · Task N completed" status to rendered components
- Cleaner presentation of teammate messages in the conversation

Evidence: UI changes at line 416889, 423206 (removes `"Agent idle · Task"`, `"Queued teammate"`)

## Bug Fixes

- Fixed escaped backslash display in terminal setup hints: now correctly shows `\\` instead of `\` in messages about multi-line input (`p89()` at line 188045, `"Use backslash (\\\\) + Enter"`)
- Fixed prompt caching scope constant to use 2026 date: `"prompt-caching-scope-2026-01-05"` (constant at line 2882)


### Removed Swarm Launch from Plan Approval
The "Yes, and launch swarm" option has been removed from the plan approval dialog. Users can still spawn teams manually using the Task tool with `team_name` parameter after plan approval. A hint about parallelization is now shown when appropriate: "If this plan can be broken down into multiple independent tasks, consider using a team of teammates (via the Task tool with team_name) to parallelize the work."

Evidence: Removed strings `"Yes, and launch swarm"`, `"Whether to launch a swarm to implement the plan"`, `"Number of teammates to spawn in the swarm"` and added `"hasTaskTool"` schema field


### System Prompt Dynamic Boundary
New `__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__` marker added for separating static and dynamic portions of system prompts, likely for improved prompt caching behavior.

Evidence: Constant at line 550046 (contains `"__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__"`)
