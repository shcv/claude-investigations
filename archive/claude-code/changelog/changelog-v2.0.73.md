# Changelog for version 2.0.73


## Summary

This release introduces a new `/skills` command for viewing available skills, adds the `/theme` command as a standalone slash command, expands LSP tool support with call hierarchy features, and includes a "year-end 2025" promotional message about 2x rate limits. The SlashCommand tool has been removed, and prompt suggestion filtering has been significantly improved.

### /skills Command
**What**: New command to view all available skills and their sources.

**Usage**:
```bash
/skills
```

**Details**:
- Displays skills grouped by source (policy settings, user settings, project settings, plugins)
- Shows skill names, estimated token counts, and source locations
- Skill locations displayed: `~/.claude/skills/`, `.claude/skills/`, or plugin sources
- Skills with `user-invocable: false` in their frontmatter are now hidden from user invocation

**Evidence**: `YX9()` at line 503132 (skills dialog, contains `"Skills"`, `"skill"`)


### /theme Command (Standalone)
**What**: The theme picker is now available as a standalone `/theme` command.

**Usage**:
```bash
/theme
```

**Details**:
- Previously only accessible via `/settings`, now directly invocable
- Allows quick theme changes without navigating through settings

**Evidence**: `FY7()` at line 503626 (theme command, contains `"theme"`, `"Theme picker"`)


### LSP Call Hierarchy Support
**What**: New LSP operations for exploring function call relationships.

**Usage**:
The LSP tool now supports three new operations:
- `prepareCallHierarchy`: Get call hierarchy item at a position
- `incomingCalls`: Find all functions/methods that call the function at a position
- `outgoingCalls`: Find all functions/methods called by the function at a position

**Details**:
- Results are grouped by file for easier navigation
- Shows call sites with line numbers
- Useful for understanding code flow and dependencies

**Evidence**: `WL0` at line 481308 (LSP tool prompt, contains `"prepareCallHierarchy"`, `"incomingCalls"`, `"outgoingCalls"`)


### Year-End 2025 Rate Limit Promotion
**What**: A promotional message announcing 2x higher rate limits through December 31, 2025.

**Details**:
- Displayed via the `tengu_year_end_2025_campaign_promo` feature flag
- Message: "A gift for you - Your rate limits are 2x higher through 12/31"

**Evidence**: `_q0()` at line 464135 (promo message, contains `"2x higher"`, `"12/31"`)


### Kill Ring Yank Cycling (Meta-y)
**What**: Added Emacs-style yank cycling with Meta-y to rotate through killed text history.

**Usage**:
After yanking with Ctrl-y, press Meta-y (Alt-y on most terminals) to cycle through previously killed text.

**Details**:
- Stores up to 10 killed text entries
- Cycles through the kill ring each time Meta-y is pressed
- Follows standard Emacs keybinding conventions

**Evidence**: `BA()` function at line 521106 (yank cycling handler, key mapping `["y", BA]` in Meta handlers)


### SlashCommand Tool Removed
The `SlashCommand` tool has been removed. Slash commands are now invoked directly by the user or through the `Skill` tool. This simplifies the tool surface and removes redundant functionality.

**Evidence**: Removed `$S = "SlashCommand"` at line 424048, removed `ir = { name: $S, ...}` tool definition


### Prompt Suggestion Filtering Enhanced
Significantly improved filtering of unsuitable prompt suggestions with new rejection criteria:
- **Word count limits**: Suggestions must be 2-8 words
- **No evaluative phrases**: Filters out "thanks", "looks good", "sounds good", etc.
- **No Claude voice**: Rejects suggestions starting with "let me", "I'll", "here's", etc.
- **No multiple sentences**: Suggestions with sentence boundaries are rejected
- Added early exit conditions for pending permissions, active elicitations, and plan mode

**Evidence**: `km5()` at line 404234 (prompt suggestion filter, contains `"claude_voice"`, `"evaluative"`, `"too_few_words"`)


### Claude 3.5 Haiku Deprecation Notice
Added deprecation warning for Claude 3.5 Haiku with retirement date of February 19, 2026 (first-party API only).

**Evidence**: `d97` at line 476533 (deprecation config, contains `"claude-3-5-haiku"`, `"February 19, 2026"`)


### Image Cache with Session Cleanup
Images pasted during a session are now cached to disk for potential later reference, with automatic cleanup of old session image caches.

**Evidence**: `ys2()` at line 454701 (image cache cleanup), `Rs2 = "image-cache"` at line 454721


### MCP Tool Search Feature Flag
Tool search for MCP can now be enabled via the `tengu_mcp_tool_search` feature flag, expanding the tool search functionality to MCP servers.

**Evidence**: `zIA()` at line 259974 (tool mode selector, contains `'if (aU("tengu_mcp_tool_search", !1)) return "tst"'`)


### Skills Frontmatter: user-invocable
Skills now support a `user-invocable` frontmatter field. When set to `false`, the skill is hidden from user-facing command lists but can still be invoked by the model.

**Evidence**: `BX9()` at line 502839 (skill builder, contains `"userInvocable"`, `"user-invocable"`)


### Improved Team Task Handling on Teammate Termination
When a teammate is terminated or shuts down, their open tasks are now properly unassigned and a notification is sent listing the affected tasks for reassignment.

**Evidence**: `a11()` at line 207479 (task unassignment handler, contains `"was terminated"`, `"unassigned"`)


### Deep Search Removed from Resume Dialog
The "deep search" (`:` prefix) feature for searching within message content has been removed from the session resume dialog, simplifying the search interface.

**Evidence**: Removed `tengu_session_deep_search_toggled` telemetry event at line 8130


## Bug Fixes

- Fixed hooks from plugins being incorrectly loaded when hooks are restricted by policy (`aI7()` at line 523289, checks `pluginName` before including hooks)
- Fixed update command to support installing specific versions via `--version` flag (`LDA()` at line 524409, `rZA()` at line 146572)


## Notes

The removal of the SlashCommand tool means that models can no longer programmatically invoke slash commands on behalf of users. Skills and custom commands should be invoked directly by users or through the Skill tool for model-initiated invocation.
