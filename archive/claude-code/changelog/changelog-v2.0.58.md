# Changelog for version 2.0.58

## Highlights

This release introduces improved concurrent tool error handling that gracefully aborts sibling tools when one fails, adds inline feedback input when rejecting file edits, and includes a redesigned guest passes UI with visual pass cards. Session management gets significant enhancements including direct resume by session ID, a preview mode, and infrastructure for hierarchical session grouping.


### Direct Session Resume via `/resume [session-id]`
**What:** Resume sessions directly by providing a session ID or title as an argument to the `/resume` command, bypassing the interactive picker.

**How to use:**
```bash
# Resume by session ID
/resume abc123def

# Resume by exact title (when enabled)
/resume "My Project Session"
```

**Details:**
- Returns helpful error messages for "session not found" or "multiple matches" scenarios
- Falls back to interactive picker when no argument provided
- **Evidence**: `u_3` at line 497346, `YV9()` at line 497237, `BV0()` at line 497245 in v2.0.58


### Inline Feedback for File Edit Rejections
**What:** When rejecting a file edit permission, you can now type feedback directly in the permission dialog instead of having to provide it separately.

**How to use:**
- When prompted for file edit permission, select "No"
- Type your feedback in the inline input field with placeholder "Type here to tell Claude what to do differently"
- Submit to reject with your feedback attached

**Details:**
- Only appears when the rejection feedback callback is provided
- Validates that feedback is not empty before allowing rejection
- **Evidence**: `Jf2()` at line 415495 with `onRejectFeedbackChange` parameter, `Cf2()` at line 415835 in v2.0.58


### Custom API Beta Headers (`--betas`)
**What:** API key users can now specify custom beta headers to include in API requests via a new CLI option.

**How to use:**
```bash
claude --betas context-1m-2025-08-07
```

**Details:**
- Only available for API key authentication (not web/OAuth)
- Currently only `context-1m-2025-08-07` is in the allowlist
- Invalid betas trigger warnings but don't fail execution
- **Evidence**: `wn0()` at line 67682, `$n0` allowlist at line 67714, CLI option at line 526721 in v2.0.58


### Critical System Reminder (Experimental)
**What:** New experimental configuration option `criticalSystemReminder_EXPERIMENTAL` for including critical system reminders in the context.

**Details:**
- Returns content blocks of type `critical_system_reminder`
- Available through SDK configuration
- **Evidence**: `WK5()` at line 343450, case handler at line 470677 in v2.0.58


### Session Preview Mode
**What:** Preview a session's full conversation history before resuming it from the session picker.

**How to use:**
- In the session picker, press `P` to preview the selected session
- View the full message history
- Press Enter to resume or Esc to return to list

**Details:**
- Shows complete transcript with all messages
- Displays session metadata (date, message count, branch)
- **Evidence**: `GV9()` at line 496704, preview state at line 496957 in v2.0.58


### Tree-Select Session Grouping (Feature-Flagged)
**What:** Infrastructure for grouping related sessions (forks/branches with same session ID) in a collapsible tree structure.

**Details:**
- Currently disabled via feature flag (`xg()` returns false)
- Groups sessions by session ID with expand/collapse support
- Uses "▼" and "▶" indicators for group state
- **Evidence**: `QV9()` at line 496553, `h_3()` grouping at line 497146, `xg()` flag at line 513608 in v2.0.58


### Concurrent Tool Error Propagation
**What:** When one tool in a concurrent execution fails, sibling tools are now gracefully aborted with a clear "Sibling tool call errored" message instead of continuing independently.

**Details:**
- New `hasErrored` flag tracks error state across concurrent tools
- `getAbortReason()` distinguishes between user interruption and sibling errors
- Synthetic error messages clearly indicate why tools were aborted
- **Evidence**: Class `y30` at line 411600, `createSyntheticErrorMessage()` at line 411636, `getAbortReason()` at line 411653 in v2.0.58


### Redesigned Guest Passes UI
**What:** Guest passes now display as visual ASCII art cards instead of a simple list, with a cleaner layout showing remaining pass count.

**Details:**
- Available passes shown as full cards: `┌─────────┐ ) CC ✻ ┊( └─────────┘`
- Redeemed passes shown dimmed with torn corner effect
- Header shows "Guest passes · N left" with count
- Simplified interaction: Enter copies link directly
- **Evidence**: `TV9()` at line 497932, card renderer at line 498017 in v2.0.58


### Enhanced Session Memory Template
**What:** The session memory template now includes a "Current State" section and improved error tracking.

**Details:**
- New "# Current State" section for tracking active work, pending tasks, and next steps
- "User Corrections / Mistakes" renamed to "# Errors & Corrections" with expanded scope
- Now captures both errors encountered and user corrections
- **Evidence**: Template at line 518364 in v2.0.58 vs line 517543 in v2.0.57


### Session Picker Enhancements
**What:** The resume session picker now supports renaming sessions and includes additional keyboard shortcuts.

**Details:**
- Press `R` to rename the selected session inline
- Press `P` to preview session (when enabled)
- Shows expand/collapse hints for grouped sessions
- **Evidence**: `BSA()` at line 496790, rename state at line 496939 in v2.0.58


### Background Model Reference Updated
**What:** Claude's background information now references Opus 4.5 as the most recent frontier model instead of Sonnet 4.5.

**Details:**
- Affects Claude's self-awareness when discussing model capabilities
- **Evidence**: `Jy3 = "Claude Opus 4.5"` at line 509270 in v2.0.58


### Windows Managed Settings Path
**What:** On Windows, the managed settings path now checks `C:\Program Files\ClaudeCode` first before falling back to `C:\ProgramData\ClaudeCode`.

**Details:**
- Provides flexibility for enterprise deployments
- **Evidence**: `gw` function at line 511827 in v2.0.58


### Time Display "60s" Rollover Fix
**What:** Fixed an edge case where time durations could display as "60s" or "60m" instead of properly rolling over to the next unit.

**Details:**
- `Math.round()` on 59.5+ seconds would produce 60, now properly rolls over
- Adds checks: `if (G === 60) ((G = 0), B++)` for seconds→minutes
- Adds checks: `if (B === 60) ((B = 0), Q++)` for minutes→hours
- **Evidence**: `VE()` at line 230586, rollover logic at lines 230595-230596 in v2.0.58
