# Changelog for version 0.2.27

# Claude Code v0.2.27 Changelog

## New Features

### Tool Permissions Management
- **New `/approved-tools` command** - Manage which tools Claude can use during your session
  - View currently approved tools
  - Add or remove tool permissions
  - Control what operations Claude can perform

### Enhanced Code Diff Display
- **Word-level diff highlighting** - See exactly what changed within modified lines
  - Intelligently matches changed lines between additions and removals
  - Highlights individual word changes within lines for better readability
  - Automatically falls back to line-level display for extensive changes (>40% of line content)
  - Color-coded word changes: additions and removals are highlighted within their respective lines

### Improved Command Experience
- **Fuzzy matching for slash commands** - Type commands more naturally
  - No need to remember exact command names
  - Partial matches and typos are handled gracefully
  - Faster command entry with intelligent suggestions

## Technical Improvements

### Better Process and Stream Handling
- Switched to named imports for Node.js built-ins (`env`, `cwd`, `PassThrough`)
- More explicit handling of process environment and streams
- Improved modularity in system interaction code

### New Diff Rendering Engine
The diff display system has been completely overhauled with several new components:

- `Sq2` - Core diff generation using the underlying diff library
- `uq2` - Main diff component that renders patches with word-level highlighting
- `zV9` - Preprocesses diff lines and identifies line types (add/remove/unchanged)
- `QV9` - Matches removed lines with their corresponding additions for word-diff analysis
- `qV9` - Performs word-level diff comparison between matched lines
- `RV9` - Renders individual lines with word-level highlighting
- `UV9` - Orchestrates the complete diff rendering process
- `ff` - Renders line numbers with proper formatting
- `fV9` - Assigns line numbers to diff entries
- `od` - Feature flag wrapper that enables word-level diff when available

### User Information Handling
- Added `homedir` and `userInfo` imports from the `os` module
- Better support for user-specific configurations and paths

## Version History Updates
The changelog now includes a new entry for v0.2.26, consolidating recent features and improvements into the version history display.
