# Changelog for version 0.2.61

# Claude Code v0.2.61 Changelog

### Enhanced Keyboard Navigation
The interactive selection system now supports more keyboard shortcuts for improved navigation:

- **Vim-style navigation**: Use `j` to move down and `k` to move up through options (when not holding Ctrl or Shift)
- **Emacs-style navigation**: Use `Ctrl+n` to move down and `Ctrl+p` to move up through options
- **Traditional arrow keys**: Continue to work as before (↑/↓)

These new shortcuts work in any interactive selection menu throughout the CLI, making navigation faster for users familiar with vim or emacs keybindings.

### Stream Handling Update
- Replaced direct stream import with `PassThrough` from the stream module, improving stream handling compatibility

### Process Module Update  
- Updated process module import to use the more specific `cwd` function from `node:process` instead of importing the entire process module

### Deprecated UI Components
- Removed several internal UI selection components that were replaced by a more unified keyboard navigation system
- Removed the "April Fools" easter egg word list that included pirate-themed terms

## Technical Improvements

- Consolidated keyboard event handling into a single, more efficient function (`fJ0`)
- Reduced code duplication by removing multiple similar navigation implementations
- Improved module imports for better tree-shaking and smaller bundle size

The overall structural similarity between v0.2.60 and v0.2.61 is 99.8%, indicating this is a focused update primarily improving keyboard navigation while cleaning up deprecated code.
