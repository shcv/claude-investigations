# Changelog for version 2.0.26

## Highlights

Version 2.0.26 introduces a persistent plugin registry system to track plugin installation metadata, improves external editor integration by eliminating UI flicker, and enhances the `/sandbox` command with clearer error messages. Additionally, this release removes the experimental "always thinking" feature and simplifies internal architecture by removing redundant parameter passing across multiple functions.


### Plugin Registry System
**What:** A persistent metadata tracking system for installed plugins using `installed_plugins.json`

**How it works:**
The system automatically creates and maintains a registry file that tracks each installed plugin's version, installation date, file path, and git commit SHA. On first run after upgrading to v2.0.26, your enabled plugins are automatically migrated from settings to this new registry.

**Details:**
- Registry file location: `~/.claude/installed_plugins.json`
- Tracks installation timestamp, last update time, version, install path, and git commit SHA
- Schema versioning (currently version 1) allows future format migrations
- Automatically syncs on startup if registry is missing or outdated
- Distinguishes between local marketplace plugins and external plugins
- **Evidence**: New functions `ck2()` at line 445175, `W5A()` at line 445178, `is1()` at line 445223, `pk2()` at line 445255, `ns1()` at line 445260, and 10 additional registry management functions in pretty-v2.0.26.js


### Flicker-Free External Editor Integration
**What:** External text editors (vim, nano, code, etc.) no longer cause terminal UI flickering

**How it works:**
When you use an external editor to write messages or edit text, Claude Code now pauses all terminal rendering before launching the editor and resumes it cleanly afterward. The Zed editor receives special treatment—it doesn't clear the screen, preserving your terminal context.

**Details:**
- Ink rendering instance pauses during editor sessions via new `pause()` and `resume()` methods
- Alternate screen buffer management moved to `finally` block for reliable cleanup
- Conditional screen clearing: all editors except Zed use alternate screen buffer
- **Evidence**: Modified function `ftA()` at line 431400 (was `et1()` at line 431181 in v2.0.25), added `pause()` and `resume()` methods to Ink class `BOA` at line 71631


### Better Sandbox Error Messages
**What:** The `/sandbox` command now provides clearer, more helpful error messages

**How it works:**
Before attempting to enable sandboxing, Claude Code validates that your platform is supported (macOS or Linux). If you're on an unsupported platform like Windows, you'll receive an immediate, clear error message instead of cryptic dependency failures.

**Details:**
- Platform validation happens before dependency checks
- Error message clarifies "bubblewrap" instead of abbreviated "bwrap"
- Explicit "only supported on macOS and Linux" message for unsupported platforms
- **Evidence**: Modified function `zv6()` at line 455556 (was `lv8()` at line 455028 in v2.0.25)


### Removal of "Always Thinking" Experiment
**What:** The experimental "always thinking" feature has been completely removed

**Details:**
- Removed automatic ultra-thinking token allocation based on experiment flag
- Simplified message rendering by removing experiment-specific UI logic
- Removed from both backend logic and frontend rendering components
- **Evidence**: Removed logic from function `L_()` at line 296620 (was `Uk()` at line 296382 in v2.0.25), simplified rendering in function `n_()` at line 323185 (was `mk()` at line 324226 in v2.0.25, 45.5% similarity)


### Simplified Internal Architecture
**What:** Removed redundant parameter passing across multiple core functions

**Details:**
- Removed unused "thread context" parameter from 8+ functions including slash command processing, user input handling, and thinking token calculation
- Removed redundant "MCP tools" parameter from message loading and preparation functions
- Cleaner function signatures reduce coupling and improve maintainability
- **Evidence**: Modified functions `kO2()` at line 439904, `MN2()` at line 431613, `ON2()` at line 431920, `bS6()` at line 431736, `am()` at line 392896, `iEA()` at line 392870, and others


### Enhanced Ink Rendering Control
**What:** The Ink UI rendering system now supports programmatic pause/resume

**Details:**
- New `isPaused` state property on Ink instances
- `pause()` method stops rendering updates
- `resume()` method re-enables rendering and triggers immediate render
- Render loop checks `isPaused` flag before executing
- **Evidence**: Modified Ink class `BOA` at line 71631 (was `DO1()` at line 71390 in v2.0.25, 93.4% similarity)


### Editor Detection
Added automatic detection of editor commands (code, subl, atom, gedit, notepad++, notepad) to apply appropriate flags like `--wait` when invoking external editors.
Evidence: New function `_S6()` at line 431396


### Version Formatting Utilities
Added helper functions for formatting and displaying version changelogs in the terminal UI.
Evidence: New functions `$G2()` at line 391967 and `NC6()` at line 392007
