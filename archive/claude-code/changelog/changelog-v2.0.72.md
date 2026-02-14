# Changelog for version 2.0.72


## Summary

This release adds a new `/mobile` command with QR codes to download the Claude mobile app, improves file indexing performance using `git ls-files`, introduces session indexing for faster conversation loading, and enhances multi-agent team workflows with improved teammate lifecycle management. The TodoWrite tool now shows a deprecation notice pointing to the new task management tools.


### `/mobile` Command - Mobile App QR Codes
What: A new slash command that displays QR codes for downloading the Claude mobile app.

Usage:
```
/mobile
```

Details:
- Shows a QR code that links to the iOS App Store or Google Play Store
- Use Tab or arrow keys to switch between iOS and Android
- Press Escape or 'q' to close
- Aliases: `/ios`, `/android`

Evidence: `s77()` at line 500313 (contains `"Show QR code to download the Claude mobile app"`, `mO0` object with App Store/Play Store URLs)


### Session Indexing [Gradual Rollout]
What: A new session indexing system that caches conversation metadata for faster session loading.

Details:
- Creates a `sessions-index.json` file that caches session metadata
- Enables faster loading of conversation history without parsing all JSONL files
- Tracks session ID, message count, timestamps, branch info, and tags
- Feature-flagged behind `tengu_session_index`

Evidence: `icB()` at line 274892 (contains `"sessions-index.json"`, `tengu_session_index` flag check via `Vm1()`)


### Tool Search Beta Support
What: Adds the `tool-search-tool-2025-10-19` beta header for Vertex and Bedrock providers.

Details:
- New beta feature flag added to the list of Claude betas
- Provider-specific version selection (different identifier for Vertex/Bedrock)

Evidence: `L4Q()` at line 64075 (contains `"tool-search-tool-2025-10-19"` beta string, checks `l4()` for provider)


### Marketplace Blocklist Support
What: Administrators can now block specific marketplace sources via policy settings.

Details:
- New `blockedMarketplaces` policy setting to prevent installation from specific sources
- Supports blocking by source type: `github`, `git`, `url`, `npm`, `file`, `directory`
- Matches GitHub repos, git URLs, npm packages, and local paths
- Cross-format matching (e.g., SSH and HTTPS GitHub URLs treated as equivalent)

Evidence: `njA()` at line 279108 (contains `"blockedMarketplaces"`, `tU3()` for source matching logic)


### File Indexing with `git ls-files`
What: File indexing now uses `git ls-files` for significantly faster project file discovery in git repositories.

Details:
- Uses `git ls-files --recurse-submodules` for tracked files
- Background fetches untracked files with `git ls-files --others`
- Falls back to ripgrep for non-git directories
- Respects `.ignore` and `.rgignore` files
- Caches results per working directory

Evidence: `fs5()` at line 447111 (contains `"git ls-files"`, `"getFilesUsingGit"` log messages, fallback to ripgrep)


### TodoWrite Deprecation Notice
What: The TodoWrite tool now displays a deprecation notice recommending the new task management tools.

Details:
- Notice appears when using TodoWrite in team/multi-agent contexts
- Recommends: TaskCreate, TaskGet, TaskUpdate, TaskList
- The new tools support team collaboration, task dependencies, and persistent storage

Evidence: `Uj8` at line 190520 (contains `"DEPRECATED"`, lists `TaskCreate`, `TaskGet`, `TaskUpdate`, `TaskList`)


### Stable Channel Downgrade Dialog
What: When switching from beta/preview to stable channel, users now see a dialog if the stable version is older.

Details:
- Prompts when stable version is lower than current version
- Options: "Allow downgrade to stable version" or "Stay on current version until stable catches up"
- Prevents accidental version downgrades

Evidence: `L59()` at line 489041 (contains `"Switch to Stable Channel"`, `"Allow downgrade to stable version"`)


### Settings Error Dialog
What: A new interactive dialog when settings files contain parse errors.

Details:
- Shows which settings files have errors
- Warns that files with errors are skipped entirely
- Options: "Exit and fix manually" or "Continue without these settings"

Evidence: `ZK7()` at line 530828 (contains `"Settings Error"`, `"Files with errors are skipped entirely"`)


### Teammate Lifecycle Improvements
What: Better handling of teammate termination and task reassignment in multi-agent workflows.

Details:
- When a teammate is terminated, open tasks assigned to them are automatically unassigned
- Leader receives notification with list of unassigned tasks
- Team-wide permission paths now propagate to teammates on initialization
- Teammates send idle notifications to leader when their Stop hook fires

Evidence: `De2()` at line 465299 (contains `"teammate_terminated"`, task unassignment logic), `ZJ1()` at line 389847 (contains `"TeammateInit"`, `"teamAllowedPaths"`)


### Invoked Skills Context
What: Skills invoked during a session are now tracked and can be included in system context.

Details:
- Tracks skill name, path, content, and invocation time
- New `invoked_skills` message type for system context
- Skills sorted by most recent invocation

Evidence: `N65()` at line 377668 (contains `"invoked_skills"`, `BS0()` for skill tracking), `QS0()` at line 2443 (skill registration)


### Enhanced DOM Event System
What: Internal Ink rendering now uses a proper DOM event system with capturing and bubbling phases.

Details:
- New `Dg` base event class with full event phase support
- Keyboard events (`PsA`), focus events (`pZA`), paste events (`qc1`), resize events (`Rc1`)
- Proper event propagation with `stopPropagation()` and `stopImmediatePropagation()`
- `eventTargetId` attribute tracking for event dispatch

Evidence: `Dg` class at line 169824, `Hg()` at line 169805 (event dispatch), `K$8()` at line 169776 (path building with capturing/bubbling)


### Tool Reference Filtering
What: Tool references in conversation history are now filtered when the referenced tool is no longer available.

Details:
- Prevents errors when resuming sessions after tools have been removed
- Logs warning when filtering out unavailable tool references
- Replaces empty results with placeholder text

Evidence: `p97()` at line 483382 (contains `"Filtering out tool_reference for unavailable tool"`)


### Shell CWD Reset Warning Parsing
What: Shell output now properly parses and extracts CWD reset warnings.

Details:
- Extracts "Shell cwd was reset to ..." messages from stderr
- Separates warning from actual error output for cleaner display

Evidence: `f17()` at line 460046 (contains `cwdResetWarning`, regex `Ks2` for `"Shell cwd was reset to"`)


### Bash Command Prefix Stripping
What: Bash tool now strips common command prefixes when analyzing commands.

Details:
- Strips: `timeout`, `time`, `nice -n`, `nohup` prefixes
- Helps with command pattern matching and analysis

Evidence: `oO2()` at line 397353 (regex patterns for `timeout`, `time`, `nice`, `nohup`)


### Minimum Version Enforcement
What: Updates can now be blocked if they would install a version below the configured minimum.

Details:
- Checks `minimumVersion` from version info before updating
- Logs skip message when update would go below minimum
- Helps prevent accidental downgrades in managed environments

Evidence: `SHA()` at line 523149 (contains `"minimumVersion"`, `"Skipping update to"`, `"below minimumVersion"`)


### BTW Side Questions [In Development]
What: Quick side questions that fork a conversation without using the main context.

Status: Stubbed - regex exists but parser always returns `{ isBtw: !1 }`

Details:
- Intended syntax: Start message with "btw" to ask a quick question
- Would create a forked conversation for the side question
- Side questions cannot use tools
- UI component exists with "btw" label and "Answering..." spinner
- Full infrastructure exists but `vK1()` returns false

Orphaned Tip: ⚠️ Users may see: "Start with 'btw' to ask a quick side question without interrupting Claude's current work" - but the feature doesn't work yet.

Evidence: `vK1()` at line 451168 (returns `{ isBtw: !1, question: "" }`), `Ze5` regex at line 451196 (`/^btw\b/gi`), tip definition at line 472886 (`id: "btw-side-question"`, `isRelevant: !0` - always shows)


## Bug Fixes

- Fixed escaping of parentheses in tool rule content (`mJ7()`, `dJ7()`, `cM()` at line 519380 - proper handling of `\(` and `\)`)


## Notes

The new task management tools (TaskCreate, TaskGet, TaskUpdate, TaskList) are designed for multi-agent team workflows. If you're using TodoWrite in a team context, consider migrating to the new tools for better collaboration support.
