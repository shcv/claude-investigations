# Changelog for version 2.1.21


## Summary

This release adds enterprise organization policy controls, improves the hook system for better SDK integration, and enhances shell completion support with automatic cache generation. The update also refines user-facing messages and adds experimental tool search optimization.


### Organization Policy Limits (Enterprise)

What: Enterprise organizations can now enforce access policies that restrict certain Claude Code features like remote sessions.

Details:
- New API endpoint `/api/claude_code/policy_limits` fetches organization-defined restrictions
- Policies are cached locally at `~/.config/claude-code/policy-limits.json`
- Automatic refresh on authentication changes and periodic background polling
- Currently enforces `allow_remote_sessions` policy for teleport and remote session creation
- Only available for enterprise subscription users with proper API scopes
- When blocked, users see: "Remote sessions are disabled by your organization's policy."

Evidence: `BB()` at line 388033 (enterprise check, uses `subscriptionType !== "enterprise"`), `YP()` at line 380468 (policy checker, uses `"allow_remote_sessions"`), `IX2()` at line 380287 (API endpoint builder, contains `"/api/claude_code/policy_limits"`)


### Shell Completion Cache Management

What: Shell completion files are now automatically generated and cached, with auto-regeneration on updates.

Usage:
Completion files are stored at:
- `~/.claude/completion.bash` for bash
- `~/.claude/completion.zsh` for zsh  
- `~/.claude/completion.fish` for fish (stored in `$XDG_CONFIG_HOME/fish/config.fish`)

Details:
- Completion caches are automatically regenerated after Claude Code updates
- Uses `claude completion <shell-flag> --output <cache-file>` under the hood
- Logs show `update: Regenerating <shell> completion cache` and `update: Regenerated <shell> completion cache at <path>`
- Improves shell startup performance by avoiding regenerating completions on every shell launch

Evidence: `k69()` at line 184272-184299 (shell detection, contains `"completion.bash"`, `"completion.fish"`, `"completion.zsh"`), `wq6()` at line 184307 (cache regeneration, contains `"update: Regenerating"` and `"completion cache"`)


### Enhanced Hook System for SDK Integration

What: The compacting system now uses structured progress callbacks instead of text spinner messages, enabling better programmatic integration.

Details:
- New `onCompactProgress` callback with `{ type, hookType }` events
- Hook types include `"pre_compact"` and `"session_start"`
- Event types: `"hooks_start"` when hooks begin execution
- Replaces legacy `setSpinnerMessage` calls with structured events
- UI still displays "Running PreCompact hooks…" and "Running SessionStart hooks…" but via event-driven rendering

Evidence: Line 449199 (hook start event, `K.onCompactProgress?.({ type: "hooks_start", hookType: "pre_compact" })`), line 449280 (session start event, `hookType: "session_start"`), line 571772 (UI rendering, contains `"Running PreCompact hooks…"`)


### Task List ID Ordering

What: Task list documentation now recommends working on tasks in ID order (lowest first) when multiple tasks are available.

Details:
- New `.highwatermark` file for tracking task ID generation
- Documentation updated to say "Prefer working on tasks in ID order (lowest ID first)"
- Helps teams coordinate work more predictably
- Part of the teammate workflow system

Evidence: `Co3 = ".highwatermark"` at line 155744 (highwatermark constant), string literal `"Prefer working on tasks in ID order"` in TaskList tool description


### Personalized Welcome Message

What: The startup welcome message now shows which IDE or terminal you're using.

Details:
- Format changed from "Welcome to Claude Code" to "Welcome to Claude Code for <IDE name>"
- Shows editor name like "VS Code", "Cursor", "Zed", or terminal name
- Detected from IDE integration context or `$TERM` environment variable
- Makes multi-IDE workflows clearer

Evidence: Line 306414 (welcome message rendering, `"Welcome to Claude Code for ", $` where `$` is IDE name from `J0()`)


### Clearer Thinking Mode Warning

The warning when changing thinking mode mid-conversation is now more explicit about performance impacts.

**Old message**: "Changing mid-conversation may reduce quality. For best results, set this at the start of a session."

**New message**: "Changing thinking mode mid-conversation will increase latency and may reduce quality. For best results, set this at the start of a session."

The message now mentions latency impact explicitly, helping users make informed decisions.

Evidence: Line 472714 (settings UI), line 559581 (toggle confirmation dialog), contains `"Changing thinking mode mid-conversation will increase latency and may reduce quality"`


### Simplified Auto Tool Search Logging

Debug log messages for automatic tool search are now clearer and more concise.

**Changes**:
- When enabled: "Auto tool search enabled: <token count>" (no more enabled/disabled toggle noise)
- When disabled: "Auto tool search disabled: <token count>" 
- Removed redundant "threshold" and "percentage" details from enable/disable messages
- Threshold context still present but only for character fallback edge cases

Evidence: Line 451497 (enabled message, `"Auto tool search enabled: ${X}"`), line 451529 (disabled message, `"Auto tool search disabled: ${X}"`)


### Improved Marketplace Installation for Headless Mode

Plugin installation in headless/SDK mode now supports extra marketplaces and has better error reporting.

Details:
- Now installs plugins from all configured marketplaces, not just default
- Skips plugins from unknown marketplaces with clear logging
- Individual marketplace installation failures don't block other installations
- Logs: `installPluginsForHeadless: installed extra marketplace <name>` on success
- Logs: `installPluginsForHeadless: failed to install extra marketplace <name>` on failure
- Logs: `installPluginsForHeadless: skipping N plugins from unknown marketplaces: <list>`

Evidence: Lines 580240-580263 (marketplace installation loop, contains `"installPluginsForHeadless: installed extra marketplace"` and `"skipping ${J.length} plugins from unknown marketplaces"`)


### Enhanced PermissionRequest Hook Error Messages

When a PermissionRequest hook denies an action, the error message now defaults to a clearer system message if the hook doesn't provide one.

Details:
- Default message: "Permission denied by PermissionRequest hook"
- Helps debug which hook is blocking an operation
- Part of the plugin hook system for security controls

Evidence: Line 579288 (hook denial, `X.message || "Permission denied by PermissionRequest hook"`)


### CLI Init Only Flag Description Update

The `--init-only` flag description now accurately reflects that it runs both Setup and SessionStart:startup hooks, not just Setup.

**Old**: "Run Setup hooks with init trigger, then exit"
**New**: "Run Setup and SessionStart:startup hooks, then exit"

Evidence: Line 585008 (CLI option description, contains `"Run Setup and SessionStart:startup hooks, then exit"`)


### Deferred Tool Search Experiment (tengu_tst_kx7)

An A/B test is running to evaluate enabling automatic tool search even when below the token threshold, if deferred tools are present in the context.

Details:
- Feature flag: `tengu_tst_kx7` (controlled by GrowthBook)
- Activates when: below normal tool search threshold BUT deferred tools exist
- Hypothesis: Deferred tools signal potential tool use even at low token counts
- Logs: `"Tool search enabled via experiment (tengu_tst_kx7)"` or `"disabled via experiment"`
- Falls back silently if GrowthBook not ready: `"tengu_tst_kx7: GrowthBook not ready, skipping"`

Evidence: Line 451507 (experiment check, contains `V4("tengu_tst_kx7", !1)` and `"via experiment (tengu_tst_kx7): below threshold, deferred tools present"`)

## Bug Fixes

- Fixed stream completion fallback trigger when message_start received but no content blocks completed (`"Stream completed with message_start but no content blocks completed - triggering non-streaming fallback"`)
- Fixed agent logging to properly identify agent in compact messages (`"[inProcessRunner] ${K.agentId} compacting history"` now includes agent ID)

## Notes

**For SDK users**: The `onCompactProgress` callback replaces `setSpinnerMessage` for hook events. Update your integration to handle the new structured events:
```typescript
{
  type: "hooks_start",
  hookType: "pre_compact" | "session_start"
}
```

**For enterprise users**: If remote sessions stop working, check with your organization admin about the new `allow_remote_sessions` policy. This is controlled at the organization level via the policy limits API.
