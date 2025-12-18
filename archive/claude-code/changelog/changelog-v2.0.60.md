# Changelog for version 2.0.60

## 🎯 Highlights
This release adds Pro plan Opus defaults, improved teammate/agent messaging UI, smarter git state detection to prevent diff issues during rebases/merges, and enhanced prompt queue execution handling.

## 🚀 New Features

### Pro Plan Opus Default Option
**What:** New experimental feature that allows Pro plan subscribers to use Opus 4.5 as their default model.

**How it works:**
When enabled via the `tengu_opus_default_pro_plan` experiment, Pro plan users will see "Opus 4.5 · Most capable for complex work" as their default model option.

**Details:**
- Controlled by experimental flag `tengu_opus_default_pro_plan` with variant `opus_is_default`
- Added `VI6()` function at line 181554 that checks if the user's plan is "pro"
- Added `haA()` function at line 181569 that checks if the Opus default experiment is enabled
- Model description function `uaA()` at line 181634 now includes the Pro plan Opus option check

### Teammate Message Display Component
**What:** New UI component to render incoming teammate messages with proper formatting and color support.

**How to use:**
Teammate messages are automatically displayed when received via the inbox system. Messages appear with the teammate's ID and optional color styling.

**Details:**
- Added `L69()` component at line 471586 to parse and render `<teammate-message>` tags
- Added `KS7()` parser function at line 471552 that extracts teammate ID, color, and content from message tags
- Messages are rendered with teammate identification and styled borders
- **Evidence**: Message rendering added at line 17992-17993 in the message display switch statement

### Agent Notification Display Component  
**What:** New UI component to display agent completion/failure notifications in the conversation.

**How to use:**
When a background agent completes or fails, a notification is automatically shown with the agent ID, status, and summary.

**Details:**
- Added `O69()` component at line 471624 to render `<agent-notification>` tags
- Displays agent ID, status (completed/failed/stopped), and summary message
- Includes guidance to use `AgentOutputTool` to retrieve full results
- Added function `m39()` at line 479132 to format and queue agent notifications
- **Evidence**: Message rendering added at line 17994-17995 in the message display switch statement

### Prompt Queue Auto-Execution Hook
**What:** New hook that automatically processes queued commands when the session becomes idle.

**How it works:**
When commands are queued (via `/add-to-queue` or similar), they are now automatically executed when the session is no longer busy, rather than requiring manual intervention.

**Details:**
- Added `i59()` hook at line 475244 that monitors loading state and queued commands
- Calls `executeQueuedInput` callback when session is idle and queue is non-empty
- Added `p59()` function for executing the queued input with proper state management
- Tracks execution with a ref to prevent duplicate processing
- **Evidence**: Hook usage at line 19833-19839 in main component

### Teammate Message Submission Handler
**What:** New handler that allows submitting messages directly from the inbox to the conversation when idle.

**How it works:**
Messages from teammates in the inbox can now be submitted as user queries when the session is idle, enabling seamless teammate collaboration.

**Details:**
- Added `w39()` hook at line 478948 for inbox polling and message delivery
- Added `onSubmitTeammateMessage` callback that creates a user message from teammate content
- Includes sophisticated idle detection and busy-state queuing logic
- **Evidence**: Hook usage at line 19883 in main component

### Disable Slash Commands Option
**What:** New `disableSlashCommands` parameter for the main component that prevents slash command processing.

**How to use:**
Pass `disableSlashCommands: true` to the main component to disable all slash command handling.

**Details:**
- Added `disableSlashCommands` parameter at line 19137 with default value `false`
- When enabled, the commands list is replaced with an empty array
- **Evidence**: Parameter defined at line 19137, conditional at line 19191

## ⚡ Improvements

### Git Rebase/Merge State Detection
**What:** Claude now detects when git is in the middle of a rebase, merge, cherry-pick, or revert operation and skips the diff display to avoid confusing partial state.

**Details:**
- Added `rm5()` function at line 405566 that checks for git state files:
  - `MERGE_HEAD` - merge in progress
  - `REBASE_HEAD` - rebase in progress  
  - `CHERRY_PICK_HEAD` - cherry-pick in progress
  - `REVERT_HEAD` - revert in progress
- The `ky2()` function at line 405477 now calls `rm5()` and returns early if any state file exists
- **Evidence**: New function added at line 16108, integration at line 17927

### WebFetch Documentation Mode
**What:** WebFetch now has a special mode for fetching documentation that allows including code examples without the strict quote limits.

**How it works:**
When fetching from llms.txt or documentation sources, the response can include full code examples and documentation excerpts rather than being limited to 125-character quotes.

**Details:**
- Added `Zp0()` function at line 53880 with conditional prompt generation
- When the `isDocumentation` flag is true, uses prompt: "Include relevant details, code examples, and documentation excerpts as needed"
- When false, uses the standard restrictive prompt with 125-character quote limits
- Added `ZzB` variable at line 182657 pointing to `https://platform.claude.com/llms.txt`
- **Evidence**: New function at line 7427, parameter added to `md2()` at line 18044-18045

### Model Name Display Function
**What:** New helper function that formats model identifiers into user-friendly "Claude" prefixed names.

**Details:**
- Added `PCB()` function at line 181670
- Transforms model IDs like "sonnet" into "Claude Sonnet"
- Returns just "Claude" if the model name is unchanged after transformation
- **Evidence**: Function at line 7462-7468

### React Reconciler Update  
**What:** Updated internal React reconciler with scheduler improvements for better performance.

**Details:**
- Added new scheduler functions including `Hg1()`, `taA()`, `aaA()` for priority queue management
- Added `Dg1()` for work loop execution with expiration handling
- Added timing functions `Iy()`, `PzB()` for deadline checking
- These are internal React infrastructure updates that improve rendering performance

## Other Changes

### Inbox Message Handling Improvements
- Inbox polling now properly queues messages when session is busy
- Messages are delivered when session transitions from busy to idle
- Improved logging with `[InboxPoller]` prefix for debugging

### Query Return Value Handling
- The `onQuery` callback no longer returns a status object
- Simplified concurrent query handling that just returns early without status
