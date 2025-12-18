# Changelog for version 2.0.59

## 🎯 Highlights

This release introduces a new **Task management system** with tools for creating and tracking work items, adds **teammate mailbox messaging** for inter-agent communication, and includes a **post-compaction feedback survey**. The `/migrate-installer` command has been removed, and thinking mode support has been extended to claude-opus-4-5.

## 🚀 New Features

### Task Management System
**What:** A complete task tracking system with four new tools for managing work items during coding sessions.

**Tools added:**
- `TaskCreate` - Create a new task with subject and description
- `TaskGet` - Retrieve a task by ID with full details
- `TaskUpdate` - Update task properties (subject, description, status, owner, comments, references, blockers)
- `TaskList` - List all tasks with their current status

**How to use:**
Tasks are automatically created and managed by Claude during complex multi-step work. Each task has:
- Subject and description
- Status: `open` or `resolved`
- Optional owner assignment
- Comments with author attribution
- Reference links between tasks
- Blocking/blocked-by relationships

**Details:**
- Tasks are stored in `.claude/tasks/` directory at `tI2()` function, line 344419
- Tasks persist across sessions within the same project
- Supports bidirectional task linking via `$Y1()` function at line 485071
- **Evidence**: `TaskCreate` tool at line 484977, `TaskList` at line 485460

### Teammate Mailbox Messaging
**What:** A new messaging system allowing Claude agents to send and receive messages between teammates in multi-agent scenarios.

**How it works:**
- Mailbox stored at `.claude/mailbox` (`BH5` variable at line 344469)
- Messages formatted as `<teammate-message teammate_id="...">` (line 344461)
- Supports read/unread tracking with `AY2()` function at line 344440
- Messages delivered as attachments of type `teammate_mailbox` (line 345180)

**Details:**
- `vH5()` function at line 345163 checks for unread messages
- `QY2()` function at line 344459 formats messages for delivery
- `eI2()` function at line 344437 filters for unread messages only
- **Evidence**: New in v2.0.59 - no matches found in v2.0.58

### Post-Compaction Feedback Survey  
**What:** After memory compaction events, users can optionally provide feedback on the compaction quality.

**Details:**
- Survey message: "How did that compaction go? (optional)" at line 481872
- Analytics event: `tengu_post_compact_survey_event` at line 477154
- Survey appears after compaction operations complete
- Auto-hides after 3 seconds (`oj3 = 3000` at line 477153)
- Implemented via `V39()` hook at line 477101
- **Evidence**: Feature completely absent in v2.0.58

### Main Thread Agent Definition Support
**What:** New architecture allowing main thread agents to provide custom system prompts.

**Details:**
- New `mainThreadAgentDefinition` parameter added to main UI component at line 480951
- `HJ9()` helper function at line 480920 handles system prompt resolution
- Conditionally calls agent's `getSystemPrompt()` method with tool context
- Enables more flexible agent customization
- **Evidence**: 7 occurrences in v2.0.59, zero in v2.0.58

## ⚡ Improvements

### Extended Thinking Mode for claude-opus-4-5
**What:** Thinking mode now supports claude-opus-4-5 model via feature flag.

**How it changed:**
- Previous: Only claude-sonnet-4-5 had thinking enabled by default
- Now: claude-opus-4-5 can enable thinking via `tengu_deep_ocean_current` feature flag

**Details:**
- `VrA()` function at line 221003-221012 updated with new model check
- Feature flag check: `BZ("tengu_deep_ocean_current", "on_by_default", !1)` at line 221011
- **Evidence**: No `deep_ocean_current` in v2.0.58, added in v2.0.59

### Marketplace Download with Custom Headers
**What:** Plugin marketplace downloads now support custom HTTP headers for authentication.

**Details:**
- `c22()` function at line 306362 now accepts headers parameter
- Headers are logged (redacted) for debugging: `O85()` function at line 306357
- Enables private/authenticated marketplace support
- **Evidence**: Modified function structure shows headers parameter added

### Analytics Sink Architecture
**What:** New analytics event buffering and sink attachment system.

**Details:**
- `Hz0()` function at line 2490 attaches analytics sink
- `GA()` function at line 2505 for synchronous events  
- `eu()` function at line 2512 for async events
- Events buffered in `NFA` array until sink attached
- Prevents event loss during initialization

### Feedback Survey Type Tracking
**What:** Feedback surveys now track the survey type (session vs post-compact).

**Details:**
- `W39()` function at line 476966 adds `survey_type` parameter to analytics
- Distinguishes between regular session feedback and post-compaction feedback
- Enables better analytics segmentation

## 🗑️ Removed Features

### `/migrate-installer` Command Removed
**What:** The command to migrate from global npm installation to local installation has been removed.

**Previous behavior:**
- `claude migrate-installer` would move installation to `~/.claude/local`
- Set up shell aliases automatically
- Removed global npm package

**Details:**
- Command definition removed (was at line 495151 in v2.0.58)
- All 10+ references to `migrate-installer` removed
- Forced migration flow (`PU9()` function) also removed
- **Evidence**: Present in v2.0.58 at multiple locations, zero matches in v2.0.59

### GrowthBook Feature Flag Check Removed  
**What:** The `sm1()` function for checking `CLAUDE_CODE_ENABLE_GROWTHBOOK` environment variable was removed.

**Details:**
- Function was at line 233408 in v2.0.58
- Simplified feature flag initialization flow

## 🔧 Internal Changes

### Slash Command UI Components Refactored
**What:** `/todos` and `/plan` commands converted to use new `local-jsx` rendering pattern.

**Details:**
- `AD9()` component at line 499901 for todos display
- `wx3()` component at line 500269 for plan display  
- `$VA()` wrapper component at line 493331 for async rendering
- `UVA()` function at line 493327 for synchronous JSX-to-string conversion

### Ctrl+O Expand Hint Extracted
**What:** The "(ctrl+o to expand)" hint is now generated by a dedicated function.

**Details:**
- `keB()` function at line 282066 returns the formatted hint
- Previously was an inline string constant `rB2` at line 303505 in v2.0.58
