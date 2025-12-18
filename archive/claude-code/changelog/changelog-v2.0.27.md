# Changelog for version 2.0.27

## 🎯 Highlights

Version 2.0.27 brings significant performance improvements through lazy Yoga rendering library loading, an enhanced session resume interface with interactive search and filtering, and improved environment variable handling. The changes focus on faster startup times and better user experience when managing multiple coding sessions.

## 🚀 New Features

### Interactive Session Resume with Search and Filtering
**What:** When resuming previous sessions, you can now search through sessions and filter by git branch to quickly find what you're looking for.

**How to use:**
```bash
# Start claude code
claude

# Press Ctrl+R to open session resume
# Then:
# - Press 'B' to toggle filtering by current git branch
# - Press '/' to enter search mode
# - Type to search across session summaries and branch names
# - Press Escape or Enter to exit search mode
```

**Details:**
- Search is case-insensitive and matches against session summary, first prompt, and git branch
- Branch filtering shows only sessions from your current branch (when toggled on)
- Visual feedback shows active filters and search term with a cursor indicator
- Context-aware help text shows available commands based on current mode
- **Evidence**: `lEA() at line 392685` in v2.0.27 (complete rewrite from `mEA() at line 392011` in v2.0.26)

### New Bordered Box UI Component
**What:** A new reusable UI component for displaying content in bordered boxes with titles and subtitles.

**Details:**
- Provides consistent styling for permissions prompts and informational sections
- Supports rounded top border with customizable colors
- Configurable inner padding and optional title coloring
- Used throughout the CLI for better visual organization
- **Evidence**: `UC() at line 430364`

### Environment Variable Expansion Function
**What:** Refactored environment variable expansion into a standalone, reusable function.

**Details:**
- Supports `${VAR}` and `${VAR:-default}` syntax for environment variables
- Tracks missing variables for better error reporting
- Now used in multiple places for consistent variable handling
- Improved code maintainability through extraction from inline implementation
- **Evidence**: `iuA() at line 262768` (extracted from inline code in `Ps8()` at line 283329 in v2.0.26)

## ⚡ Improvements

### Lazy Loading of Yoga Rendering Library
**What:** The Yoga WASM rendering library is now loaded on-demand instead of during startup, significantly improving CLI startup time for non-rendering operations.

**How it works:**
- Yoga library loads only when rendering is actually needed
- Automatic error checking prevents usage before initialization
- Memoization ensures the library loads only once
- Most CLI commands (git operations, file reading, etc.) now start faster

**Details:**
- Previous version loaded Yoga synchronously during startup at multiple points
- New version uses lazy async loading with `await xq0()` memoization
- Error guard function `EL9() at line 53524` throws "Yoga not loaded" if accessed prematurely
- Single initialization point at `OR9() at line 71850` replaces multiple `await hp()` calls
- **Evidence**: `Wq0() at line 52532`, `EL9() at line 53524`, `NMA() at line 53603` (replaced synchronous `hp() at line 52526` in v2.0.26)

### Enhanced Session Resume UI
**What:** The session resume interface is more responsive and provides better visual feedback.

**Details:**
- Dynamic layout adjusts for active filters
- Focused input shows cursor indicator for better feedback
- Help text adapts based on current state (search mode vs normal mode)
- Cleaner presentation of session metadata
- **Evidence**: Enhanced `lEA() at line 392685` compared to v2.0.26

### Code Organization and Maintainability
**What:** Several internal refactorings improve code quality without changing user-facing behavior.

**Details:**
- Environment variable expansion logic extracted into reusable function
- Better separation of concerns in session management code
- Reduced code duplication through function extraction
- Improved error messages and validation

## 🔧 Technical Changes

- Import changes: Added `cwd as uL0` from `node:process` at line 70580
- Import changes: Added `execSync as H9Q, spawn as _v8` from `node:child_process` at line 248770
- Function `BM0() at line 71622` added for clearing terminal screen
- Multiple helper functions added for the new session filtering features
- Yoga-related functions refactored from synchronous (`hp()`, `Qq0` global) to async lazy pattern (`Wq0()`, `j61` with `EL9()` getter)
