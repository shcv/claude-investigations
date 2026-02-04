# Changelog for version 2.1.27

## Summary

This release adds the `--from-pr` flag for resuming sessions linked to pull requests, introduces PDF page rendering via poppler-utils (`pdftoppm`), and adds OSC52 clipboard support for SSH sessions. The multi-agent team UI gets significantly enhanced with structured status messages and agent lifecycle indicators. Under the hood, the Sentry error tracking SDK and localForage dependencies have been completely removed.

## New Features

### `--from-pr` Flag for PR-Linked Session Resume

**What**: Resume a previous Claude Code session that was linked to a specific pull request, by PR number or URL.

**Usage**:
```bash
claude --from-pr 123
claude --from-pr https://github.com/owner/repo/pull/123
claude --from-pr          # opens interactive picker
claude --from-pr "search" # opens picker filtered by search term
```

**Details**:
- Accepts a PR number, a full PR URL, or no value (opens an interactive picker)
- When passed a string that is not a number/URL, it filters the picker by that search term
- Works alongside existing `--resume` and `--continue` session management flags

**Evidence**: CLI option definition (search for `"--from-pr [value]"`)

### PDF Page Rendering via poppler-utils

**What**: Claude Code can now render PDF pages as JPEG images using `pdftoppm` from poppler-utils, enabling visual analysis of PDF content beyond text extraction.

**Details**:
- Uses `pdftoppm` to convert PDF pages to JPEG images at 100 DPI
- Requires poppler-utils to be installed (`brew install poppler` on macOS, `apt-get install poppler-utils` on Linux)
- Provides detailed error handling for: password-protected PDFs, corrupted/invalid files, oversized files, and missing pdftoppm
- Falls back gracefully with a clear install instruction message when poppler-utils is not available
- Separate size limits for text extraction vs page rendering
- Tracked via `tengu_pdf_page_extraction` telemetry

**Evidence**: PDF page rendering function (search for `"pdftoppm is not installed. Install poppler-utils"`)

### OSC52 Clipboard Support for SSH Sessions

**What**: Clipboard copy now works over SSH connections using the OSC52 escape sequence protocol, supported by modern terminal emulators.

**Details**:
- Automatically detects SSH sessions and attempts OSC52-based clipboard copy
- Supported terminals include: iTerm2, Kitty, Ghostty, WezTerm, Alacritty
- For tmux users, requires `set-clipboard` to be enabled and `allow-passthrough` to be on
- Provides a clear error message listing compatible terminals when OSC52 fails
- Replaces the old generic platform-specific error message with SSH-aware guidance

**Evidence**: SSH clipboard error message (search for `"clipboard access requires a terminal that supports OSC52"`)

## Improvements

### Enhanced Multi-Agent Team UI

The multi-agent/team system receives significant UI improvements with structured status messages and lifecycle indicators.

**New status indicators**:
- `Agent idle` / `Agent idle - Task X completed` status display for idle agents
- `1 agent spawned` / `N agents spawned` notifications when teammates are created
- `1 agent shut down` / `N agents shut down` notifications when teammates exit
- `Created team` display when a new team is initialized

**Structured message formatting**:
- `[Shutdown Request from X]` - when an agent requests another to shut down
- `[Shutdown Approved] X is now exiting` - when shutdown is accepted
- `[Shutdown Rejected] X: reason` - when shutdown is declined
- `[Join Request] name wants to join` - when an agent requests to join a team
- `[Join Approved] You are now name in team` - when join is accepted
- `[Join Rejected] reason` - when join is declined
- `[Task Assigned] #id - subject` - when a task is assigned to an agent
- `[Plan Approval Request from X]` - when plan review is requested
- `[Plan Approved] You can now proceed with implementation` - when plan is approved
- `[Plan Rejected] feedback` - when plan is rejected with feedback

**Evidence**: Agent idle status (search for `"Agent idle"`) and spawn notifications (search for `"1 agent spawned"`)

### Improved Authentication Error Messages

Authentication failures now provide more specific messages distinguishing between account-level and organization-level access issues.

- "Your account does not have access to Claude. Please login again or contact your administrator."
- "Your organization does not have access to Claude. Please login again or contact your administrator."

These are more informative than the previous generic "Your account does not have access to Claude Code. Please run /login." message.

**Evidence**: Account access error messages (search for `"Your account does not have access to Claude. Please login again"`)

### Improved Transcript/JSONL File Validation

Reading transcript files now provides clearer error messages when files are malformed:

- "No messages found in JSONL file" - when JSONL file parses but contains no messages
- "No valid conversation chain found in JSONL file" - when messages exist but no valid chain can be reconstructed
- "Invalid JSON in transcript file" - when JSON parsing fails
- "Transcript messages must be an array" / "Transcript must be an array of messages or an object with a messages array" - format validation

**Evidence**: JSONL validation (search for `"No messages found in JSONL file"`)

### Space Key Dismisses Notifications

The notification dismiss prompt now accepts Space in addition to Enter and Escape, changing from "Press Enter or Escape to dismiss" to "Press Space, Enter, or Escape to dismiss".

**Evidence**: Dismiss prompt text (search for `"Press Space, Enter, or Escape to dismiss"`)

### Tool Error Categorization

Tool execution failures now provide more specific error messages distinguishing between different failure types:
- `tool input error:` for input validation failures
- `tool validation error:` for custom validation failures
- `tool permission denied` for rejected tool calls
- `tool error (Nms):` for runtime errors with execution timing

**Evidence**: Tool error messages (search for `"tool input error"` and `"tool validation error"`)

### "Penguin" Theme Colors

New color variants added for UI theming:
- Light themes: `rgb(15,144,127)` / `rgb(55,184,167)` shimmer
- Dark themes: `rgb(47,176,159)` / `rgb(87,206,189)` shimmer

**Evidence**: Theme color definitions (search for `"penguin"`)

### Multi-File Patch Validation

Better error message when attempting to create patches without file headers:
- "Cannot omit file headers on a multi-file patch. (The result would be unparseable; how would a tool trying to apply the patch know which changes are to which file?)"

**Evidence**: Diff formatter validation (search for `"Cannot omit file headers on a multi-file patch"`)

### Dependency Cleanup: Sentry and localForage Removed

Two significant third-party dependencies have been removed from the bundle:

- **Sentry SDK** (v7.120.3): The entire Sentry error tracking infrastructure has been removed. The old version contained 179 references to Sentry including DSN configuration, error capture, transaction tracing, and browser/Node integrations. The new version has zero Sentry code (only a reference in an MCP setup example).
- **localForage**: The browser-compatible storage library has been completely removed (previously 7 references).

This reduces bundle size and removes third-party error telemetry from the CLI.

**Evidence**: Sentry DSN was at `"https://e531a1d9ec1de9064fae9d4affb0b0f4@o1158394.ingest.us.sentry.io/..."` in v2.1.26, absent in v2.1.27. Search for `"sentry"` or `"localforage"` in both versions to confirm removal.
