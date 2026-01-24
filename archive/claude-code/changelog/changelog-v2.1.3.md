# Changelog for version 2.1.3


## Summary

This release introduces a customizable keybindings system, allowing users to remap keyboard shortcuts via `~/.claude/keybindings.json`. The notification system was refactored with better terminal-specific handlers. The permission explainer UI was enhanced with a `Ctrl+E` shortcut to toggle explanations, and the `/doctor` command now reports unreachable permission rules. The Task* tools (TaskCreate, TaskGet, TaskUpdate, TaskList) were removed in favor of the simpler TodoWrite system.

### Custom Keybindings Support

**What**: Configure custom keyboard shortcuts via a JSON file in your Claude config directory.

**Usage**:
Create `~/.claude/keybindings.json` with your custom mappings:
```json
[
  {
    "context": "Chat",
    "bindings": {
      "ctrl+k": "chat:submit",
      "ctrl+l": null
    }
  }
]
```

**Details**:
- Supports contexts: `Global`, `Chat`, `Autocomplete`, `Confirmation`, `Transcript`, `HistorySearch`, `Task`, `ThemePicker`, `Help`
- Set a binding to `null` to disable it
- File is hot-reloaded on changes—no restart required
- Invalid keybindings show warnings via notifications, with details available in `/doctor`
- Reserved keys (`ctrl+c`, `ctrl+d`) cannot be remapped
- Validation warns about OS-specific conflicts (e.g., `cmd+c` on macOS)

**Evidence**: `TJ()` at line 358886 (`KeybindingSetup` component, initializes with `"[keybindings] KeybindingSetup initialized"`), `Q_A()` at line 213102 (returns `keybindings.json` path), `g_5()` at line 358862 (displays `"keybinding-config-warning"` notifications)

### Permission Explainer Keyboard Shortcut

**What**: Press `Ctrl+E` during permission prompts to toggle an AI-generated explanation of what the command does and its risk level.

**Usage**:
When Claude asks for permission to run a command, press `Ctrl+E` to see:
- What the command does (explanation)
- Why Claude is running it (reasoning)
- Potential risks with severity level (LOW/MEDIUM/HIGH)

**Details**:
- Explanations are generated on-demand using a fast model
- Toggle the explanation panel on/off with `Ctrl+E`
- Risk levels: LOW (safe dev workflows), MEDIUM (recoverable changes), HIGH (dangerous/irreversible)
- Only appears when the permission explainer feature flag is enabled

**Evidence**: `hg2()` at line 417649 (checks `X.ctrl && J === "e"`, calls `tengu_permission_explainer_shortcut_used`), `gg2()` at line 417666 (renders `"ctrl+e to "` + `"hide"` or `"explain"`), `wc5()` at line 417675 (displays explanation with `riskLevel`)

### Unreachable Permission Rules Detection

**What**: The `/doctor` command now detects and displays permission rules that will never be applied due to being shadowed by broader rules.

**Usage**:
```
/doctor
```
Look for the "Unreachable Rules" section showing:
- Which rules are shadowed
- Which broader rule is shadowing them
- How to fix the configuration

**Details**:
- Detects allow rules shadowed by ask rules
- Detects allow rules shadowed by deny rules
- Shows the source of conflicting rules (project settings, policy, etc.)
- Provides specific fix suggestions

**Evidence**: `xKA()` at line 302515 (checks for `shadowedBy` and builds unreachable rules list), `jg2()` at line 416765 (renders `"Unreachable Rules"` UI component with `shadowType` of `"ask"` or `"deny"`)

### Refactored Notification System

The terminal notification system was refactored with cleaner abstractions. Notifications now use dedicated handler functions (`sendITerm2`, `sendKitty`, `sendGhostty`, `sendBell`) instead of inline escape sequences, making the code more maintainable and easier to extend.

**Evidence**: `gd()` at line 367233 (new notification dispatcher using `FT5`), `FT5()` at line 367243 (notification router with `B.sendITerm2(Q)`, `B.sendKitty(...)`, etc.), `HT5()` at line 367266 (auto-detection handler)

### Enhanced Remember Skill

The `/remember` skill now has clearer instructions about evidence thresholds—patterns must appear in 2+ sessions before being added to memory. This prevents one-off items from polluting project memory.

**Evidence**: `Iq7` variable at line 530741 (contains `"Evidence Threshold (2+ Sessions Required)"` and `"Only extract themes and patterns that appear in 2 or more sessions"`)

### Todo System Migration

Automatic migration from the old todo system (v1) to the new task system (v2) when upgrading. Existing todos are preserved and converted to the new format.

**Evidence**: `fG0()` at line 284033 (contains `"[Todo Migration] Migrating"` and `"Successfully migrated"`)

### Dynamic Keybinding Display

Keyboard shortcut hints throughout the UI now reflect custom keybindings. If you remap `ctrl+o`, hints will show your custom binding instead of the default.

**Evidence**: `g4()` at line 213290 (resolves display text for action/context, logs `"tengu_keybinding_fallback_used"` when falling back), `gq()` at line 213305 (similar resolution function), `iP()` at line 282054 (uses `g4("app:toggleTranscript", "Global", "ctrl+o")`)

### Task* Tools Removed

The `TaskCreate`, `TaskGet`, `TaskUpdate`, and `TaskList` tools have been removed. These were a more complex team collaboration-oriented task system that has been superseded by the simpler `TodoWrite` tool.

**Details**:
- `TodoWrite` continues to work for tracking todos during sessions
- Old todos are automatically migrated to the new system
- Team collaboration features are no longer available through these tools

**Evidence**: Diff shows 23 occurrences of TaskCreate/TaskGet/TaskUpdate/TaskList in v2.1.2, reduced to 2 in v2.1.3 (legacy references only)

### Incremental TUI (tengu_sumi)

**What**: An experimental incremental terminal UI rendering system.

**Status**: Feature-flagged via `tengu_sumi`

**Details**:
- Controlled by `ENABLE_INCREMENTAL_TUI` environment variable or `tengu_sumi` feature flag
- Infrastructure is in place but gated

**Evidence**: `Sz()` at line (contains `dX(process.env.ENABLE_INCREMENTAL_TUI)` and `y8("tengu_sumi")`)

### Scratch Feature (tengu_scratch)

**What**: Purpose unclear from code, but infrastructure exists for a "scratch" feature.

**Status**: Feature-flagged via `tengu_scratch`

**Evidence**: `gzA()` at line 526466 (returns `y8("tengu_scratch")`)
