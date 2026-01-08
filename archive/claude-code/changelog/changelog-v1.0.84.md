# Changelog for version 1.0.84

## Highlights
Version 1.0.84 introduces improved search performance with native ripgrep integration, enhanced file path completion with quoted path support, and refined UI components for better interactive selections.

### Native Ripgrep Integration
**What:** Built-in support for using ripgrep as the search backend with automatic availability detection
**How to use:**
```bash
# Ripgrep is automatically detected and used when available
claude --grep "search term" 

# The CLI now tests ripgrep availability on first use
# Falls back gracefully if ripgrep is not available
```
**Details:**
- Automatic detection of system ripgrep installation
- Built-in ripgrep binary as fallback option
- Performance telemetry for ripgrep availability
- Configurable search modes (system vs built-in)

### Enhanced File Path Completion
**What:** Support for quoted file paths in prompts, especially for paths with spaces
**How to use:**
```bash
# Now supports quoted paths in prompts
@"path with spaces/file.txt"

# Mixed quoted and unquoted paths work seamlessly
@file1.txt @"folder with spaces/file2.txt" @file3.txt
```
**Details:**
- Handles both `@"quoted paths"` and `@unquoted` paths
- Improved regex patterns for path extraction
- Better support for paths containing spaces and special characters
- Works in both command line and interactive modes

### Improved UI Selection Components  
**What:** New visual components for better feedback in interactive selections
**How to use:**
```bash
# Selections now show clearer visual indicators
# - Blue pointer (►) for focused items
# - Green checkmark (✓) for selected items
# - Improved color coding for better visibility
```
**Details:**
- Consistent visual indicators across all selection interfaces
- Better color scheme using "suggestion" and "success" colors
- Enhanced padding and spacing for improved readability

### Todo List Display Enhancement
**What changed:** Condensed todo list view with configurable verbosity
**Previous behavior:** All todos always displayed in full
**New behavior:** Smart condensed view showing only changed items and summaries
**Impact:** Cleaner output that focuses on what's currently relevant, with option for full verbosity when needed

### Ripgrep Status Reporting
**What changed:** Added ripgrep configuration details to system diagnostics
**Previous behavior:** No visibility into search backend status
**New behavior:** Reports ripgrep mode, availability, and system path in diagnostics
**Impact:** Easier troubleshooting of search-related issues and performance optimization

### Session History Management
**What changed:** Removed bookmark persistence to simplify session tracking
**Previous behavior:** Bookmarks were persisted across sessions
**New behavior:** Session management focuses on messages and checkpoints only
**Impact:** Simplified data model with more reliable session recovery

### Fixed: Code Signing for macOS Ripgrep Binary
- **Issue:** Ripgrep binary on macOS could fail due to code signing requirements
- **Cause:** macOS Gatekeeper blocking unsigned binaries
- **Resolution:** Added proper code signing flow for built-in ripgrep on macOS

### Fixed: File Path Token Parsing
- **Issue:** File paths with special characters or quotes could be incorrectly parsed
- **Cause:** Regex patterns didn't account for quoted path formats
- **Resolution:** Enhanced regex patterns to handle both quoted and unquoted paths

### Fixed: UI Component Color Consistency
- **Issue:** Inconsistent color schemes across different selection components
- **Cause:** Hardcoded color values instead of theme colors
- **Resolution:** Unified color system using semantic color names
