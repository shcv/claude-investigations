# Changelog for version 2.1.26

## Summary

This release adds a `--all` flag to the plugin disable command for bulk disabling, introduces a new `terminalTitleFromRename` setting, and adds hook interrupt support that lets hooks abort tool execution mid-flight. Internally, the bundled Statsig SDK has been almost entirely removed, and a new HybridTransport mechanism handles MCP bridge communication via HTTP POST with retry logic.

### Plugin Disable --all Flag

What: The `claude plugin disable` command now accepts an optional `--all` flag to disable all enabled plugins at once, instead of requiring a specific plugin name.

Usage:
```bash
claude plugin disable --all
claude plugin disable [plugin]
```

Details:
- The command signature changed from `disable <plugin>` (required) to `disable [plugin]` (optional)
- Use `--all` / `-a` to disable all enabled plugins in one shot
- Cannot combine `--all` with a specific plugin name (error: "Cannot use --all with a specific plugin")
- Cannot combine `--scope` with `--all`
- If no plugins are enabled, displays "No enabled plugins to disable"

Evidence: Plugin disable all handler (search for `"Disable all enabled plugins"` or `"Cannot use --all with a specific plugin"`)


### Terminal Tab Title Setting

What: New `terminalTitleFromRename` boolean setting that controls whether the terminal tab title is pinned to the value from `/rename` or auto-updated based on conversation topic.

Usage:
Set in `settings.json` or `settings.local.json`:
```json
{
  "terminalTitleFromRename": true
}
```

Details:
- When `true`, the terminal tab title is set from `/rename` and not auto-updated based on the conversation topic
- When `false` or absent, the previous auto-update behavior continues
- This is useful for users who use `/rename` to set a meaningful session name and don't want it overwritten

Evidence: Zod schema setting description (search for `"terminal tab title is set from /rename"`)


### Hook Interrupt Support

What: Hooks can now interrupt and abort tool execution. When a hook returns a response with the `interrupt` flag set, the tool's abort controller is triggered, stopping the in-progress operation.

Details:
- Applies to both pre-tool and post-tool hooks
- When a hook signals interrupt, the tool execution is aborted via `abortController.abort()`
- The interrupt is logged with tool name and hook message for debugging
- This also applies to SDK permission prompts: a deny with interrupt will abort the controller

Evidence: Hook abort on interrupt (search for `"Hook interrupt: tool="`) and SDK deny+interrupt (search for `"SDK permission prompt deny+interrupt: tool="`)

### Plan Execution UI Improvements

The plan execution prompt has been improved with clearer messaging and numbered options. The confirmation prompt now reads "Claude has written up a plan and is ready to execute. Would you like to proceed?" instead of the previous generic "Would you like to proceed?". Plan selection options (like "Chat about this" and "Skip interview and plan immediately") are now displayed with numbered prefixes for easier keyboard selection.

Evidence: Plan confirmation text (search for `"written up a plan and is ready to execute"`)


### MCP Permission Mode: follow_a_plan

A new `follow_a_plan` permission mode has been added for MCP server interactions. The available permission modes are now `ask`, `skip_all_permission_checks`, and `follow_a_plan`. When the permission mode is set, a confirmation message "Permission mode set to: [mode]" is returned. This mode appears to be used during plan execution to provide an intermediate permission level between full ask and full bypass.

Evidence: Permission mode handler (search for `"follow_a_plan"` or `"Permission mode set to:"`)


### MCP Server Disconnect Flow

New UI flow for disconnecting MCP servers via the browser. Users are shown instructions like "Find the MCP server in the browser and click 'Disconnect'" with options to open claude.ai directly. The disconnect flow includes "Press Enter to open the browser" and "Press Enter when done" confirmation steps.

Evidence: MCP disconnect instructions (search for `'Find the MCP server in the browser and click "Disconnect"'`)


### SubagentStop Hook Documentation

The SubagentStop hook's description now documents the JSON input format: "Input to command is JSON with agent_id, agent_type, and agent_transcript_path." This was previously undocumented, making it clearer for hook authors what data is available when a subagent completes.

Evidence: SubagentStop description update (search for `"agent_id, agent_type, and agent_transcript_path"`)


### Skills Deduplication Changed from Inode to File-Based

The skill deduplication mechanism has changed from inode-based comparison (which relied on filesystem-level identity via inodes, symlinks, or hard links) to file-based comparison. Debug messages now say "same file" instead of "same inode". This likely improves compatibility across different filesystem types and platforms.

Evidence: Skill dedup logging (search for `"skills (same file)"`)


### InboxPoller Validation Improvements

The InboxPoller now validates sandbox permission requests and team permission updates more strictly, logging warnings for malformed data rather than potentially crashing:
- Validates that `hostPattern.host` exists on sandbox permission requests
- Validates that `permissionUpdate.rules` and `permissionUpdate.behavior` exist on team permission updates

Evidence: Validation messages (search for `"[InboxPoller] Invalid sandbox permission request"`)


### Clear Authentication UI

A new "Clear authentication for [name]" UI element has been added, allowing users to clear authentication credentials for specific services or plugins.

Evidence: Auth clearing UI (search for `"Clear authentication for "`)

### Statsig SDK Removal

The bundled Statsig client SDK has been almost entirely removed (from approximately 87 string references down to 7). This includes removal of:
- The Statsig SDK key and all SDK-specific error messages
- DNS-based fallback mechanisms (`cloudflare-dns.com`, `application/dns-message`)
- Local storage providers, event loggers, and evaluation adapters
- The `node://localhost` browser shim used by the Statsig SDK

Feature flag evaluation likely moved to a server-side or pre-evaluated model. This should reduce bundle size and eliminate Statsig-related network requests at startup.


### HybridTransport for MCP Bridge

A new `HybridTransport` class has been added that converts WebSocket URLs to HTTP POST endpoints for sending events. It:
- Transforms `/ws/` paths to `/session/` and appends `/events`
- Includes retry logic with multiple attempts
- Handles client errors (4xx except 429) by not retrying
- Uses session tokens for authentication
- Falls back gracefully if no session token is available

This supplements the existing WebSocket transport with an HTTP POST channel, likely improving reliability of the Claude in Chrome MCP bridge connection. The bridge URL is logged at startup, showing "none (using native socket)" when no bridge is configured.

Evidence: HybridTransport implementation (search for `"HybridTransport: POST URL ="`)
