# Changelog for version 1.0.127

## Highlights

Version 1.0.127 focuses on internal code refactoring and improvements with 98.9% structural similarity to v1.0.126. The main user-facing changes include enhanced sandbox command filtering capabilities, improved UI text clarity for history search and file restoration, and updated color scheme implementation using ANSI color names.

### Enhanced Sandbox Command Filtering

**What:** Added support for substring-based command filtering in the sandbox configuration through the new `tengu_sandbox_disabled_commands` feature gate.

**How it works:**

The sandbox now supports two methods for disabling commands:
1. Exact command matching (existing `unsandboxedCommands` in settings)
2. Substring matching (new `tengu_sandbox_disabled_commands` feature flag)

**Details:**
- Substring matching allows blocking commands that contain specific patterns anywhere in the command string
- The new `tengu_sandbox_disabled_commands` feature flag provides `commands` and `substrings` arrays
- Both methods are combined when evaluating whether a command should bypass sandboxing
- **Evidence**: `Qg2()` function at line 379010 in v1.0.127 (replaces `qu2()` at line 383844 in v1.0.126)

### Improved Diff Stats Display Component

**What:** New unified component for displaying file change statistics during restore operations.

**Details:**
- Created `kGB()` helper component at line 413123 to consistently display file names and diff stats
- Shows either the single filename or count of multiple files
- Displays insertions (+) and deletions (-) with appropriate colors
- Simplifies the restore UI presentation
- **Evidence**: `kGB()` component at line 413123 (new in v1.0.127, did not exist in v1.0.126)

### Clearer History Search Prompts

**What:** Updated history search interface text for better clarity.

**Changes:**
- Changed "bck-i-search:" to "search prompts:"
- Changed "failing bck-i-search:" to "no matching prompt:"
- Added visible cursor in search field (previously hidden)
- **Evidence**: Modified in function at line 425036 in v1.0.127 (was at line 429928 in v1.0.126)

**Why it matters:** The new prompts use plain language instead of technical terminal jargon, making the feature more discoverable and user-friendly.

### Better File Restore Messaging

**What:** Improved clarity when viewing file restoration previews.

**Changes:**
- When no files changed: Now shows "The code has **not changed**" instead of "The code will be **restored**"
- Simplified multi-file display using the new `kGB` component
- More consistent formatting across different restore scenarios
- **Evidence**: Function `ey6()` at line 413105 in v1.0.127 (was `ek6()` at line 415828 in v1.0.126)

**Why it matters:** Users can now immediately understand whether there are actual changes to review or if the code state is unchanged.

### Color Scheme Refactoring

**What:** Internal refactoring of color definitions from hex values to ANSI color names.

**Changes:**
- Light theme colors now use `"ansi:colorName"` format (e.g., `"ansi:magenta"`, `"ansi:blueBright"`)
- Dark theme colors similarly use ANSI names
- Added new `clawd_body` color property
- **Evidence**: Color objects `QlQ` and `ZlQ` around line 356107-356221 in v1.0.127 (replaced `rlQ` and `olQ` at line 356102-356158 in v1.0.126)

**Why it matters:** While mostly internal, this improves cross-platform color rendering and maintainability. Users may notice slightly improved color consistency across different terminal emulators.

### Model and Output Style Selection Refactoring

**What:** Restructured the model and output style selection menus for better code organization.

**Details:**
- Model selection function restructured (was `bz5()` at line 438053, now `bK5()` at line 435315)
- Output style selection function restructured (was `mz5()` at line 438157, now `mK5()` at line 435411)
- Callback functions extracted for cleaner separation of concerns
- No functional changes to user experience
- **Evidence**: Functions `bK5()` and `mK5()` at lines 435315 and 435411 in v1.0.127

### Code Refactoring

- Removed unused stream import variable (import renamed internally)
- Extensive variable and function renaming (8,964 renames)
- 46 additions, 101 deletions, 19 modifications to declarations
- Improved code structure while maintaining 98.9% structural similarity
- No tree-sitter functionality was removed (still present in v1.0.127)

**Note:** The majority of changes in this release are internal refactorings that improve code maintainability without affecting user-visible behavior.
