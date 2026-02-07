# Changelog for version 2.1.33


## Summary

This release introduces new dedicated Agent Teams tools (`TeamCreate` and `TeamDelete`), new hooks for team-based workflows (`TeammateIdle` and `TaskCompleted`), enables agent teams by default for users with the experimental flag set, and adds streaming fallback to non-streaming mode when the streaming endpoint returns a 404 error. The plan mode workflow has been significantly rewritten for a more collaborative "pair-planning" experience.

### TeamCreate and TeamDelete Tools

**What**: New dedicated tools for managing agent teams, replacing the previous operation-based approach.

**Details**:
- `TeamCreate`: Creates a new team for coordinating multiple agents. Requires `team_name` and optional `description` parameters.
- `TeamDelete`: Removes team and task directories when swarm work is complete. Fails if the team still has active members - teammates must be terminated first.
- Error messages now reference `TeamDelete` instead of the generic "cleanup operation" for ending teams.

**Evidence**: Tool definitions (search for `"TeamCreate"`, `"TeamDelete"`)

### TeammateIdle and TaskCompleted Hooks

**What**: New hook types for agent team workflows that allow custom scripts to run at key points.

**Details**:
- `TeammateIdle`: Fires when a teammate is about to go idle. Input is JSON with `teammate_name` and `team_name`. Exit code 2 prevents idle (teammate continues working).
- `TaskCompleted`: Fires when a task is being marked as completed. Input is JSON with `task_id`, `task_subject`, `task_description`, `teammate_name`, and `team_name`. Exit code 2 prevents task completion.

**Evidence**: Hook definitions (search for `"When a teammate is about to go idle"`, `"When a task is being marked as completed"`)

### Streaming Fallback to Non-Streaming Mode

**What**: Automatic fallback when the streaming API endpoint returns a 404 error.

**Details**:
- When the streaming endpoint returns HTTP 404, Claude Code now automatically falls back to non-streaming mode
- Logs a warning: "Streaming endpoint returned 404, falling back to non-streaming mode"
- Telemetry tracks these events with `error: "404_stream_creation"`

**Evidence**: Fallback logic (search for `"Streaming endpoint returned 404"`, `"404_stream_creation"`)

### Agent Teams Enabled by Default (with env var)

**What**: The `tengu_amber_flint` feature flag now defaults to `true`, enabling agent teams for users who set `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.

**Details**:
- Previously, the feature flag defaulted to `false`, requiring both the env var AND server-side enablement
- Now users only need to set `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` to use agent teams
- The system prompt note about agent teams "not available on this plan" is now conditionally hidden when teams are enabled

**Evidence**: Feature flag change from `!1` (false) to `!0` (true) (search for `"tengu_amber_flint"`)

### Revamped Plan Mode Workflow

**What**: Plan mode instructions have been completely rewritten for a more collaborative "pair-planning" experience.

**Details**:
- New framing: "You are pair-planning with the user"
- Introduces "The Loop" pattern: Explore → Update plan file → Ask user → repeat
- New "First Turn" guidance: Start with a quick scan, write a skeleton plan, ask initial questions
- "Asking Good Questions" section: Never ask what you could find by reading code; batch related questions; focus on things only the user can answer
- Simplified tool references: "to read code" instead of verbose tool lists

**Evidence**: New workflow text (search for `"pair-planning with the user"`, `"First Turn"`)

### Cleaner Login Error Messages

**What**: Login-related error messages are now unified to "Not logged in · Run /login".

**Details**:
- Previously showed "Invalid API key · Run /login" or "Missing API key · Run /login"
- Now shows a single consistent message: "Not logged in · Run /login"

**Evidence**: Error message strings (search for `"Not logged in · Run /login"`)

### Extra Usage Promo Now Includes Command

**What**: The Opus 4.6 promotional message now includes the command to enable extra usage.

**Details**:
- Previous: "Opus 4.6 is here · $50 free extra usage"
- New: "Opus 4.6 is here · $50 free extra usage · /extra-usage to enable"

**Evidence**: Promo message (search for `"/extra-usage to enable"`)

### Improved Session ID Validation

**What**: The `--session-id` flag now strictly requires a valid UUID format.

**Details**:
- Previous: Accepted "UUID or tagged ID" (`--session-id <id>`)
- New: Only accepts valid UUIDs (`--session-id <uuid>`)
- Error message updated: "Must be a valid UUID" (removed "or tagged ID")

**Evidence**: CLI option description (search for `"--session-id <uuid>"`)

### Task Panel Toggle Text

**What**: The Ctrl+T shortcut text now says "toggle tasks" instead of "show todos".

**Evidence**: UI text (search for `"to toggle tasks"`)

### Teammate Status Messages

**What**: New descriptive status messages for teammate state changes.

**Details**:
- Completed: `Teammate "name" completed their task.`
- Stopped: `Teammate "name" was stopped.`
- Idle: `Teammate "name" is idle and ready for new work.`

**Evidence**: Status message templates (search for `"completed their task"`, `"is idle and ready for new work"`)

### Plugin Validation Messages

**What**: New warning messages when enabled plugins have issues.

**Details**:
- `Plugin "X" is enabled but not found in any known marketplace`
- `Plugin "X" is enabled but you chose not to install it`

**Evidence**: Plugin validation (search for `"is enabled but not found in any known marketplace"`)

### Enhanced Debug Logging

**What**: New debug logging for WebSocket errors and cancel operations.

**Details**:
- `[SessionsWebSocket] WebSocket error` - WebSocket connection errors
- `[onCancel] focusedInputDialog=X streamMode=Y` - Cancel operation context
- `[teleportToRemote] Git source:` / `No repository detected` - Remote session setup
- `[useDeferredValue] Messages deferred by N` - UI performance tracking

**Evidence**: Debug log strings (search for `"[SessionsWebSocket]"`, `"[onCancel]"`)

### CLAUDE_CONFIG_DIR Support in Team Spawning

**What**: Team-spawned agents now inherit `CLAUDE_CONFIG_DIR` environment variable.

**Evidence**: Environment setup code (search for `"CLAUDE_CONFIG_DIR="`)

## Bug Fixes

- Fixed typo in Edit tool description: "occurences" → "occurrences" (search for `"Replace all occurrences"`)
- Improved error handling for API requests with new "Error in API request:" log format
