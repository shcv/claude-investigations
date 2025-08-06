# Changelog for version 0.2.29

# Claude Code v0.2.29 Changelog

## New Features

### Enhanced `.gitignore` Support for LS Command
The `ls` command now respects `.gitignore` patterns when listing files and directories. This provides a cleaner view of your project by automatically filtering out ignored files.

**New parameter**: The `ls` command now accepts an optional `ignore` parameter where you can provide an array of glob patterns to exclude from the listing.

**Example usage**:
```bash
# List files while respecting .gitignore
claude ls /path/to/directory

# List files with custom ignore patterns
claude ls /path/to/directory --ignore "*.tmp" "*.log"
```

### Improved Command Suggestions UI
The command suggestion interface has been redesigned to be more responsive and informative:

- **Responsive layout**: Command suggestions now adapt to terminal width (switches to vertical layout when terminal width < 80 columns)
- **Command aliases**: Now displays command aliases alongside the main command name
- **Enhanced descriptions**: Shows argument names for prompt-type commands
- **Better visual hierarchy**: Improved spacing and text wrapping for better readability

### Vim Mode Indicator
For users with Vim as their `$EDITOR`, Claude Code now displays a `-- INSERT --` indicator when in insert mode, providing a familiar experience for Vim users.

## Improvements

### Tool Comparison Enhancement
The tool comparison logic now supports custom `inputsEqual` methods for tools, allowing for more sophisticated comparison of tool inputs. This improves the accuracy of determining when tools need to be re-executed.

### File Edit Refactoring
The file editing logic has been refactored for better maintainability:
- Separated file reading logic into its own function (`AY9`)
- Improved empty string replacement handling in `XY9` function
- Cleaner separation of concerns in the `Cu` (formerly `mN1`) function

### Token Usage Display
The token usage display component has been extracted into a reusable component (`xR2`), making the UI more modular and maintainable.

## Version History Update
Added changelog entry for v0.2.27 (currently empty, awaiting content).

## Technical Changes

- Refactored import statements to use named imports from Node.js built-in modules
- Added new utility functions for better code organization
- Improved error handling in `.gitignore` parsing
- Enhanced modularity of UI components
