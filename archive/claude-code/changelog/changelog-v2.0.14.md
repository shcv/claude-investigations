# Changelog for version 2.0.14

## Highlights

This release focuses on improving the plugin installation experience with a streamlined UI, better executable file validation, and enhanced directory path handling across different platforms.

### Platform-Aware User Directory Detection
**What:** Added cross-platform support for detecting standard user directories (Desktop, Documents, Downloads) with platform-specific environment variable handling.

**How it works:**
- Windows: Uses `USERPROFILE` environment variable
- Linux/WSL: Respects XDG directory specifications (`XDG_DESKTOP_DIR`, `XDG_DOCUMENTS_DIR`, `XDG_DOWNLOAD_DIR`)
- macOS: Uses standard home directory paths
- Unknown platforms: Falls back to default paths with a warning

**Details:**
- Automatically detects the operating system and applies appropriate path resolution
- Provides directory categorization to identify if a path is "home", "desktop", "documents", "downloads", or "other"
- **Evidence**: `Im1() at line 301093` and `Yi0() at line 455838` in v2.0.14

### Improved Executable File Validation
**What:** Enhanced executable file checking to exclude zero-byte files

**How it works:**
The executable validation now explicitly rejects empty files that previously might have been incorrectly considered valid executables.

**Details:**
- Checks `file.size === 0` before attempting to verify execute permissions
- Prevents false positives when scanning for executable files
- More robust validation for system compatibility checks
- **Evidence**: `MB1() at line 280658` - added `Q.size === 0` check

### Simplified Plugin Installation UI
**What:** Streamlined the plugin installation workflow by removing the "Mark for installation" option from the plugin details screen

**Changes:**
- Removed "Mark for installation" / "Unmark for installation" toggle from plugin details view
- Simplified to direct "Install now" action
- Selection/deselection still available in the plugin list view using spacebar
- Cleaner, more focused plugin details interface

**Evidence**: 
- v2.0.13: Had "Mark for installation" option at line 438131 and dynamic "Unmark for installation" at line 438286
- v2.0.14: Option removed from `rUQ()` function - not found in new version

### Enhanced Plugin List Visual Polish
**What:** Multiple UI refinements to improve the plugin installation experience

**Changes:**
- Title capitalization: Changed "Select Marketplace" to "Select marketplace" for consistency
- Title capitalization: Changed "Install Plugins" to "Install plugins" for consistency  
- Icon change: Replaced "arrowRight" (→) with "pointerSmall" (›) for better visual hierarchy
- Selection indicator: Changed from "play" (▶) to "radioOn" (◉) for selected plugins
- Improved spacing and alignment in plugin lists

**Evidence**:
- Title changes at lines 438189/438215 (v2.0.13) vs 438265/438291 (v2.0.14)
- Icon changes visible in diff at lines showing `M0.pointerSmall` vs `q0.arrowRight` and `M0.radioOn` vs `q0.play`

### Optimized Terminal Rendering
**What:** Internal refactoring of cursor visibility tracking for more efficient terminal rendering

**Details:**
- Replaced manual `hasHiddenCursor` state tracking with dynamic `cursorVisible` checks
- More precise cursor state management based on actual frame visibility
- Changed from `resetLineCount()` to more comprehensive `reset()` method
- Internal optimization with no user-visible behavior changes

**Evidence**: `n90` class at line 69693, `renderEfficiently()` method shows cursor visibility logic

## Internal Changes

The following changes are internal refactorings with no direct user impact:

- Updated import statements for better module organization
- Variable renaming throughout the codebase (standard minification pattern changes)
- Added `bH1 = "AgentOutputTool"` string constant at line 433177 (no functional change)
- Added helper functions `QF8()` and `ZF8()` for plugin UI rendering logic


**Migration Notes:** No breaking changes. All existing workflows continue to work as before.

**Installation:** Update using your package manager: `npm install -g @anthropic-ai/claude-code@2.0.14`
