# Changelog for version 2.1.42


## Summary

This release introduces the `/desktop` command to transfer sessions to Claude Desktop, adds an effort level selection callout for Opus 4.6 users, and includes significantly rewritten auto memory instructions. The release also improves error handling for image processing and marketplace caching, and adds support for date change notifications during long-running sessions.

### `/desktop` Command

What: Transfer your current Claude Code session to Claude Desktop for a seamless cross-platform workflow.

Usage:
```bash
# In Claude Code interactive mode
/desktop
```

Details:
- Checks if Claude Desktop is installed and up-to-date (requires v1.1.2396+)
- Saves the current session before transfer
- Opens Claude Desktop and continues the conversation there
- Alias: `/app`
- Supported on macOS and Windows only
- If Claude Desktop is not installed, offers to download it

Evidence: Session transfer system (search for `"Session transferred to Claude Desktop"`)


### Effort Level Callout for Opus 4.6

What: A new callout prompts users to choose their preferred thinking intensity when first using Opus 4.6.

Details:
- Appears when using Opus 4.6 for the first time
- Offers "medium" (balances efficiency and intelligence) or "high" (best for hardest tasks) options
- Pro plan users default to medium effort; others default to high
- The callout can be dismissed and won't reappear
- Effort can always be changed later via `/model`

Evidence: Effort callout modal (search for `"Effort in Opus 4.6"`)


### Date Change Notifications

What: Long-running sessions now receive automatic notifications when the date changes at midnight.

Details:
- Claude is informed of the new date without user intervention
- Helps maintain accurate context for date-sensitive operations
- The message instructs Claude not to mention the date change explicitly to users

Evidence: Date change handler (search for `"The date has changed. Today's date is now"`)


### Interrupted Turn Auto-Resume

What: When a session is resumed after an interruption, Claude now receives a clear instruction to continue from where it left off.

Details:
- Improves session continuity after interruptions
- Part of the `print.ts` auto-resume system

Evidence: Interrupted turn handling (search for `"Continue from where you left off."`)


### Rewritten Auto Memory Instructions

What: The auto memory system prompt has been completely rewritten with clearer, more actionable guidance.

Changes:
- Simplified structure with clear "What to save" and "What NOT to save" sections
- More specific guidelines about when to consult memory files
- Explicit section for handling user requests to remember or forget things
- Cleaner formatting with focused bullet points

Evidence: Auto memory prompt (search for `"# auto memory"`)


### AWS Auth Timeout Feedback

What: Added a 3-minute timeout with actionable feedback for AWS authentication refresh.

Details:
- If AWS auth refresh takes longer than 3 minutes, users receive clear guidance
- Message suggests running the auth command manually in a separate terminal

Evidence: AWS auth timeout (search for `"AWS auth refresh timed out after 3 minutes"`)


### Improved Marketplace Cache Recovery

What: Marketplace caching now handles stale directories more gracefully.

Changes:
- Renamed "Updating existing marketplace cache…" to "Refreshing marketplace cache…"
- Added detection for stale directories with automatic cleanup and re-clone
- Better error messages when git pull fails
- Clearer status messages during cache operations

Evidence: Marketplace refresh (search for `"Refreshing marketplace cache…"`)


### Enhanced Image Error Detection

What: Expanded detection of image processing errors for better error handling.

New error patterns detected:
- `corrupt image`, `premature end`, `zlib: data error`
- `zero width`, `zero height`
- `pixel limit`, `too many pixels`, `exceeds pixel`, `image dimensions`
- `out of memory`, `Cannot allocate`, `memory allocation`

Evidence: Image error classification (search for `"too many pixels"`)


### Network Egress Blocking

What: Added a new error type for network egress proxy blocks in managed environments.

Details:
- New `EgressBlockedError` with clear messaging
- Message: "Access to {domain} is blocked by the network egress proxy"

Evidence: Egress blocking (search for `"EgressBlockedError"`)


### Better Model Selection UI Text

What: Clearer wording for model inheritance in model selection.

Change: "Inherit (default)" → "Inherit from parent (default)"

Evidence: Model picker (search for `"Inherit from parent (default)"`)


### Session Conflict Resolution

What: Better handling of session 409 conflicts with server-side sync.

Details:
- Adopts server's `lastUuid` from headers when conflicts occur
- Re-fetches entries to ensure consistency
- Logs detailed sync information for debugging

Evidence: Session 409 handler (search for `"Session 409: adopting server lastUuid"`)


### Windows Shell Syntax Guidance

What: Added explicit guidance for Windows users about shell syntax.

Details:
- Reminder to use Unix shell syntax (not Windows syntax) for bash commands
- Examples: `/dev/null` not `NUL`, forward slashes in paths

Evidence: Shell syntax hint (search for `"use Unix shell syntax, not Windows"`)


### Agent Frontmatter Validation

What: Improved error message for agent files missing required frontmatter.

Change: Now specifically mentions `'description'` in the error message rather than generic field name.

Evidence: Agent validation (search for `"is missing required 'description' in frontmatter"`)


### Cache Editing for Microcompact

What: Cache editing beta header is now enabled for cached microcompact operations.

Details:
- Only applies to first-party API users in the main REPL thread
- Improves performance when working with compacted conversations

Evidence: Cache editing (search for `"Cache editing beta header enabled for cached microcompact"`)


## Bug Fixes

- Removed Bun-specific WebSocket ping logging that was causing noise (search for `"WebSocketTransport: Sent ping"`)
- Fixed model parsing for abbreviated model names like `3-5-sonnet` and `3-7-sonnet` to correctly detect context limits


## Internal Changes

- Removed verbose prompt cache break logging (`[PROMPT CACHE BREAK]` messages)
- Removed detailed cache break reason strings (model changed, tools changed, system prompt changed)
- Simplified Opus plan restriction messaging
- Removed `fs` from the documented example list in hook globals (still accessible via `require()`)
