# Changelog for version 2.0.0

## Highlights

Version 2.0.0 introduces Claude Sonnet 4.5 as the new default model, completely redesigns the welcome screen with a new "Clawd" mascot and adaptive layout system, and adds a `/usage` command for subscription plan usage tracking. The thinking feature has been streamlined to use a simple "ultrathink" trigger, and the MultiEdit tool has been removed in favor of the existing Edit tool.


### Claude Sonnet 4.5 Model
**What:** New default model `claude-sonnet-4-5-20250929` with improved performance for daily coding tasks

**How to use:**
```bash
# Sonnet 4.5 is now the default - no changes needed
claude

# Or explicitly specify it
claude --model sonnet45
```

**Details:**
- Available across all platforms (first-party API, Bedrock, Vertex AI)
- Automatic migration from previous default models
- Described as "Smartest model for daily use"
- Supports 1M token context window variant: `claude-sonnet-4-5[1m]`
- **Evidence**: `U10` at line 367516, `GM1()` at line 368315, model detection logic at line 340617 in v2.0.0


### /usage Command
**What:** View your subscription plan usage limits and current consumption

**How to use:**
```bash
/usage
```

**Details:**
- Shows current 5-hour session usage
- Displays 7-day usage across all models
- Shows 7-day Opus-specific usage
- Visual progress bars with percentage indicators
- Reset time countdown
- Only available for subscription plans (API key users see informational message)
- **Evidence**: `OXB` command definition at line 416198, usage API endpoint at line 402408, UI components `E3B()` and `WS6()` at lines 402479-402532 in v2.0.0


### Redesigned Welcome Screen
**What:** Complete overhaul with adaptive layout, branded "Clawd" mascot, and dynamic content feeds

**Features:**
- **Clawd mascot**: Custom ASCII art character with theme-aware rendering
- **Three responsive layouts**: Adapts to terminal width (compact/horizontal/vertical)
- **Dynamic feeds**: Recent activity with timestamps, release notes, getting started tips
- **Personalized greeting**: Shows user's display name when available
- **Model & billing info**: Quick view of current settings

**Details:**
- Automatically adjusts to terminal size and capabilities
- Special rendering optimizations for Apple Terminal
- Supports both light and dark themes
- Shows recent conversation history
- Displays latest changelog entries
- Contextual tips based on project state
- **Evidence**: Main welcome screen `iOB()` at line 429317, Clawd mascot `PK5()` at line 429231, feed system `gOB()` at line 429168, splash screen `Pc1()` at line 441300 in v2.0.0


### Extended Thinking Improvements
**What:** Simplified thinking trigger system with new programmatic control

**How to use:**
```bash
# Use "ultrathink" anywhere in your prompt for maximum thinking
claude
> Please ultrathink about this architectural design

# Toggle thinking with tab key during interactive sessions
# Or use /t command
```

**Details:**
- Streamlined from multilingual pattern matching to single "ultrathink" keyword
- Binary mode: ULTRATHINK (31,999 tokens) or NONE
- New `thinkingMetadata` API for programmatic control without text triggers
- Removed complex multi-level system (HIGHEST/MIDDLE/BASIC) in favor of simpler on/off
- Thinking state notifications show "Thinking on/off (tab to toggle)"
- **Evidence**: Pattern at line 363628, functions `Y61()` at line 363667, `Y09()` at line 363644, `le1()` at line 363671, metadata handling at line 363649 in v2.0.0


### Enhanced Settings Dialog
**What:** Tabbed interface combining status, configuration, and usage in one place

**How to use:**
```bash
/status  # Opens with Status tab
/config  # Opens with Config tab  
/usage   # Opens with Usage tab
```

**Details:**
- Tab navigation to cycle between Status/Config/Usage panels
- Status tab shows system diagnostics, IDE connection, MCP servers, memory usage
- Config tab provides interactive settings management
- Usage tab displays subscription limits (new in 2.0.0)
- Unified interface reduces command clutter
- **Evidence**: Tabbed component `L01()` at line 394930, status dialog `h01()` at line 402533 in v2.0.0


### Session Persistence Improvements
**What:** Enhanced session history deduplication and conflict detection

**Details:**
- Prevents duplicate entries when fetching session history
- Tracks already-fetched UUIDs per session to avoid redundant storage
- Improved conflict resolution with UUID mismatch detection
- Better error messages for concurrent modification scenarios
- **Evidence**: Deduplication logic in `F8B()` at line 397200, UUID tracking with `Cv1` map in v2.0.0


### IDE Selection Indicator
**What:** Shows currently active file or selected text from connected IDE

**Display:**
- "⧉ In filename.ts" when a file is active
- "⧉ 15 lines selected" when text is selected

**Details:**
- Only appears when IDE is connected and has an active context
- Helps confirm Claude knows which file you're working in
- Updates automatically as you switch files
- **Evidence**: `aLB()` function at line 423498 in v2.0.0


### Notification System Enhancements
**What:** Improved notification queue management with invalidation support

**Details:**
- Notifications can now invalidate previous notifications by key
- Better handling of immediate-priority notifications
- Prevents notification spam by filtering duplicates
- Queue management ensures only relevant notifications are shown
- **Evidence**: Enhanced `xG()` notification hook at line 363012 with `invalidates` support at lines 363225-363244 in v2.0.0


### Auto-compact Token Budget Display
**What:** Context window display now shows reserved space for auto-compact and output tokens

**Details:**
- New "Reserved (autocompact + output tokens)" category in /context display
- Shows available tokens after accounting for auto-compact threshold
- Helps users understand actual usable context space
- More accurate free space calculations for subscription plans
- **Evidence**: `L3B` and `CS6` variables at lines 402598 and 403199, calculation logic in `y3B()` at line 403320 in v2.0.0


### Thinking Time Display
**What:** Visual feedback when Claude uses extended thinking

**Display:**
```
∴ Thinking…  (while active)
∴ Thought for 12s (ctrl+o to show thinking)  (after completion)
```

**Details:**
- Real-time indicator during thinking phase
- Shows total thinking duration after completion
- Reminds users how to view thinking content
- Only appears when thinking is actually used
- **Evidence**: `m3B()` function at line 404483 in v2.0.0


### Path Truncation Algorithm
**What:** Improved file path display in narrow terminals

**Details:**
- Smart truncation preserves first and last path components
- Uses middle ellipsis (…) to show structure
- Handles root paths and edge cases gracefully
- Example: `/very/long/path/to/file.ts` → `/very/…/to/file.ts`
- **Evidence**: `MI1()` function at line 405562 in v2.0.0


### Model Display Names
**What:** Clearer model naming in UI

**Changes:**
- "Sonnet 4.5" for the new default model
- "Sonnet 4.5 (with 1M token context)" for extended context variant
- Consistent capitalization and formatting
- **Evidence**: `UeA()` function at line 368322, `JM()` at line 368327, `lJA()` at line 367531 in v2.0.0


### Restore Dialog File Display
**What:** Better file information when restoring changes

**Details:**
- Shows specific filenames instead of generic "files changed"
- Lists up to 2 files by name, then "and N other files"
- More informative change summaries
- **Evidence**: `uf6()` function at line 414892 in v2.0.0


### Recent Activity Feed
**What:** Welcome screen shows recent conversations with timestamps

**Details:**
- Displays last 3 non-sidechain conversations
- Filters out apology-heavy sessions
- Shows conversation summary or first prompt
- Relative timestamps (e.g., "2h ago", "yesterday")
- Quick context for resuming work
- **Evidence**: `_GB()` function at line 405621, `iR0()` at line 429186 in v2.0.0


### Sonnet 4.5 Migration
**What:** Automatic model upgrade for existing users

**Details:**
- Users with explicit model settings are migrated to Sonnet 4.5
- Migration timestamp tracked to show "Model updated to Sonnet 4.5" notification
- One-time migration prevents repeated notifications
- Graceful handling of users who prefer other models
- **Evidence**: `v4Q()` migration function at line 443290, notification in `NRB()` at line 430680 in v2.0.0


### Subscription Plan Notifications
**What:** Prompts to activate Claude subscription if available

**Details:**
- Shows up to 3 times for eligible users
- "Use your existing Claude [plan] with Claude Code · /login to activate"
- Tracks notification count to avoid annoyance
- Only shown to users with available subscriptions
- **Evidence**: `MRB()` notification at line 430699, subscription check `sK5()` referenced in v2.0.0


### Extended Thinking Simplification
**What:** Streamlined from multilingual multi-level system to single trigger

**Previous (v1.0.128):**
- 8 languages supported (English, Japanese, Chinese, Spanish, French, German, Korean, Italian)
- 4 thinking levels: HIGHEST (31,999 tokens), MIDDLE (10,000), BASIC (4,000), NONE (0)
- Dozens of trigger phrases per language
- Complex pattern matching with negation filtering

**Now (v2.0.0):**
- English-only "ultrathink" trigger
- 2 levels: ULTRATHINK (31,999 tokens) or NONE (0)
- Simple case-insensitive regex matching
- New `thinkingMetadata` API for programmatic control

**Implications:**
- More predictable behavior
- Easier to remember single trigger word
- Programmatic control via metadata for advanced use cases
- **Evidence**: Removed `v19` patterns at line 363665 in v1.0.128, new simplified system with `NU1` at line 363628 and functions at lines 363644-363671 in v2.0.0


### Tool List Updates
**What:** Removed MultiEdit from available tools array

**Details:**
- MultiEdit tool completely removed from codebase
- Tool arrays updated from `["Edit", "MultiEdit", "Write", "NotebookEdit"]` to `["Edit", "Write", "NotebookEdit"]`
- Edit tool handles all file editing use cases
- Reduces complexity and potential confusion between Edit and MultiEdit
- **Evidence**: Tool array `HK5` at line 428943 in v1.0.128 vs `IK5` at line 428118 in v2.0.0


### State Management Improvements
**What:** Simplified state update logic removes redundant null checks

**Details:**
- Model selection updates no longer check if `oldState` is null before comparison
- Assumes initial state is always available
- Cleaner conditional logic
- Added thinking state persistence to user settings
- **Evidence**: Function `Bp()` at line 443042 in v1.0.128 vs `df()` at line 443128 in v2.0.0


### Notification Color Scheme
**What:** Reduced thinking notification color levels

**Details:**
- Removed medium and low thinking level colors
- Now only "none" (text) and "high" (claude) colors
- Matches simplified binary thinking system
- **Evidence**: Variables `cT` and `aa` at lines 363617-363618 in v1.0.128 vs `LU1` and `$WA` at lines 363586-363587 in v2.0.0


### MultiEdit Tool
**What:** The MultiEdit tool has been removed entirely

**Reason:** The Edit tool provides all necessary file editing capabilities, and having both tools caused confusion.

**Migration:** Use the Edit tool for all file modifications. For multiple edits to the same file, Claude will use Edit multiple times as needed.

**Evidence:** Variable `sH = "MultiEdit"` at line 365916, tool registration in arrays at line 428943, prompts mentioning MultiEdit at lines 440925-440941 in v1.0.128 - all removed in v2.0.0


### Multilingual Extended Thinking Triggers
**What:** Support for non-English thinking trigger phrases removed

**Affected Languages:**
- Japanese (熟考, 深思, etc.)
- Chinese (深思, 仔细思考, etc.)
- Spanish (piensa más, etc.)
- French (réfléchis, etc.)
- German (denk nach, etc.)
- Korean (심사숙고, 깊이 생각, etc.)
- Italian (pensa profondamente, etc.)

**Replacement:** Use "ultrathink" in English for maximum thinking tokens

**Evidence:** Variable `v19` with multilingual patterns at line 363665 in v1.0.128 - removed in v2.0.0, replaced with single English pattern `G09` at line 363628


### Legacy Welcome Screen Components
**What:** Old ASCII banner and static welcome screen removed

**Removed Components:**
- Large ASCII art "CLAUDE CODE" logo (`lGB()` at line 406445)
- Simple header with star icon (`DN0()` at line 406867)
- Static environment overrides display (`_A1()` at line 407407)

**Replacement:** New adaptive welcome screen with Clawd mascot and dynamic feeds

**Evidence:** Functions `lGB()`, `DN0()`, `_A1()` in v1.0.128 completely replaced by new system in v2.0.0


### Opusplan Fallback Mode
**What:** Removed "Opus Plan Mode" model fallback strategy

**Details:**
- Previously: "Use Opus 4.1 in plan mode, Sonnet 4 otherwise"
- This specific fallback configuration is no longer available
- Standard model selection and rate limit fallback still work
- **Evidence**: Variable `D31` at line 368627, function `U31()` at line 368577 in v1.0.128 - removed in v2.0.0


### Config Command Array Functions
**What:** Removed several project-level config management functions

**Removed:**
- `Ym1()` - Add items to array config (line 439101)
- `YPB()` - Remove items from array config (line 439140)
- `VPB()` - Set config value (line 439430)
- `KPB()` - Delete config key (line 439488)
- `FPB()` - Get config value (line 439413)
- `zPB()` - List config (line 439507)

**Reason:** Config management migrated to settings.json system

**Migration:** Use `.claude/settings.json` for project configuration instead of CLI commands

**Evidence:** Functions at lines 439101-439507 in v1.0.128 marked as removed in diff


### Post-Tool Hook Feedback Messages
**What:** Removed dedicated function for creating post-tool feedback system messages

**Details:**
- Function `kv1(A, B)` removed - created system messages for tool hook feedback
- Feedback mechanism still exists but implementation changed
- **Evidence**: Function `kv1()` at line 397255 in v1.0.128 vs different implementation in v2.0.0


### Session Persistence Deduplication
**What:** Fixed duplicate session log entries when fetching history

**Issue:** When resuming sessions, the same entries could be persisted multiple times

**Fix:** Added UUID tracking per session to skip already-fetched entries

**Impact:** Cleaner session history, reduced storage overhead, faster session loading

**Evidence:** New deduplication check at start of `F8B()` function at line 397200 in v2.0.0


### Terminal Width Calculation
**What:** Improved responsive layout calculations for welcome screen

**Details:**
- Better handling of very narrow terminals (< 70 columns)
- Fixed edge cases in path truncation
- More accurate column calculations for multi-panel layouts
- **Evidence**: Layout functions `SGB()` at line 405537, `yGB()` at line 405541 in v2.0.0


### Breaking Changes
1. **MultiEdit tool removed** - Extensions or scripts using MultiEdit must switch to Edit tool
2. **Non-English thinking triggers removed** - Only "ultrathink" works now
3. **Project config CLI commands removed** - Use settings.json instead
4. **Opusplan mode removed** - Adjust model selection strategy if using this


### Migration Guide
- **MultiEdit → Edit**: Simply use Edit tool; Claude will apply multiple edits as needed
- **Multilingual thinking → ultrathink**: Replace language-specific triggers with "ultrathink"
- **Config commands → settings.json**: Move `allowedTools`, `ignorePatterns` to `.claude/settings.json` permissions object
- **Model selection**: Sonnet 4.5 is now default; explicit model selections are preserved


### Version Information
- **Version:** 2.0.0
- **Previous Version:** 1.0.128
- **Release Date:** 2025 (based on model identifiers)
- **Major Version Bump Reason:** Breaking changes (removed tools, removed CLI commands, simplified thinking system)
