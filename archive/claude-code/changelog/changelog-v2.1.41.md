# Changelog for version 2.1.41


## Summary

This release introduces comprehensive memory guidance (rolling out via feature flag), MCP session recovery with automatic tool retries, and improved device file handling in the Read tool. WebSocket connections now handle permanent close codes and include Bun-specific ping support. The admin eligibility API for extra usage requests was also added.


### Enhanced Memory System Guidance [Gradual Rollout]
What: Detailed instructions for Claude on when and how to use the persistent memory directory.

Details:
The new guidance includes:
- **When to access memories**: When memories are relevant, user refers to prior work, or explicitly asks to recall
- **When to save memories**: Project context, user preferences, debugging insights, architectural decisions
- **What to save**: Patterns, conventions, user workflow preferences, recurring problem solutions
- **What NOT to save**: Ephemeral task details, duplicate information contradicting CLAUDE.md
- **Memory hygiene**: Remove outdated info, organize by topic not chronologically, use separate topic files

Status: Controlled by `tengu_mulberry_fog` feature flag (defaults to disabled)

Evidence: Memory guidance system (search for `"You MUST access memories when"`)


### MCP Session Recovery with Automatic Retry
What: When an MCP server session expires, Claude Code now automatically reconnects and retries the failed tool call.

Details:
- Detects session expiration via 404 status with error code -32001 or connection close
- Clears connection cache and triggers re-initialization
- Automatically retries the tool call that failed due to session expiration
- New `McpSessionExpiredError` error type for proper error handling

Evidence: MCP session recovery (search for `"MCP session expired during tool call"` and `"Retrying tool"`)


### Device File Read Blocking
What: The Read tool now blocks attempts to read device files that would block or produce infinite output.

Details:
Blocked device files include:
- `/dev/zero`, `/dev/random`, `/dev/urandom`, `/dev/full`
- `/dev/stdin`, `/dev/tty`, `/dev/console`
- `/dev/stdout`, `/dev/stderr`, `/dev/fd/0`, `/dev/fd/1`, `/dev/fd/2`

Error message: "Cannot read '[path]': this device file would block or produce infinite output."

Evidence: Device file blocklist (search for `"device file would block"`)


### AWS Authentication Permission Type
What: New permission category for AWS authentication operations displayed in the permission UI.

Evidence: AWS Auth permission (search for `"AWS Authentication"`)


### StopTaskError for Task Termination
What: New error type for cleanly stopping running tasks with proper error code handling.

Evidence: Task stop error (search for `"StopTaskError"`)


### FileTooLargeError for Read Tool
What: New error type thrown when attempting to read files exceeding the maximum size limit.

Evidence: File size error (search for `"FileTooLargeError"`)


### Admin Eligibility API for Extra Usage
What: New API endpoint to check eligibility for extra usage requests in team/enterprise contexts.

Evidence: Admin eligibility endpoint (search for `"admin_requests/eligibility"`)


### WebSocket Connection Handling
- **Permanent close detection**: WebSocket connections now recognize permanent close codes and avoid unnecessary reconnection attempts
- **Bun ping support**: Added specific ping handling for Bun runtime WebSocket connections
- **Sessions WebSocket**: Similar permanent close handling for session WebSocket connections

Evidence: WebSocket improvements (search for `"WebSocketTransport: Permanent close code"` and `"Sent ping (Bun)"`)


### Image Dimension Error Handling
Added specific error handling for images exceeding the 2000px dimension limit in many-image requests. The error message now provides actionable guidance:
- In interactive mode: "Run /compact to remove old images from context, or start a new session"
- In non-interactive mode: "Start a new session with fewer images"

Evidence: Image dimension handling (search for `"image dimensions exceed"`)


### Shell Snapshot Recovery
Added automatic recreation of shell snapshots when the snapshot file goes missing, improving resilience of the shell execution environment.

Evidence: Shell snapshot recovery (search for `"Failed to recreate shell snapshot"`)


### Pre-flight Check Message Generalization
The pre-flight check warning now uses a generic tool name placeholder instead of hardcoded "[BashTool]", making it applicable to multiple tool types. The emoji prefix was also removed for cleaner output.

Evidence: Pre-flight message (search for `"Pre-flight check is taking longer"`)


### Streaming Fallback Error Logging
Added explicit error logging when streaming fails and non-streaming fallback is disabled, controlled by `tengu_disable_streaming_to_non_streaming_fallback` feature flag.

Evidence: Streaming fallback (search for `"non-streaming fallback disabled"`)


### Error Message Terminology Update
- Changed "Failed to read bash history" to "Failed to read shell history" (more accurate for multi-shell support)

## Bug Fixes

- Removed obsolete `ignorePatterns` migration code and related error handling (search for `"Failed to migrate ignorePatterns"` in v2.1.40 - absent in v2.1.41)
- Removed "No editor available" error path - editor handling appears to have been restructured
- Removed task stop status error message (`"is not running, so cannot be stopped"`) - logic was revised

## Internal Changes (Not User-Facing)

- Removed "Layout engine: yoga" debug logging
- Code path changes for task stopping don't affect user behavior
- Minor text adjustments in Plan agent phase descriptions
