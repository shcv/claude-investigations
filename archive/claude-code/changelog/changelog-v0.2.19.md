# Changelog for version 0.2.19

### New Features

#### Vim Mode Support
- **New command**: `vim` - Toggle between vim and emacs editing modes
  - Usage: Simply type `vim` in the command prompt to switch modes
  - In vim mode: Use `Escape` key to toggle between INSERT and NORMAL modes
  - In emacs mode: Standard emacs-style keybindings are active
  - The editor mode preference is persisted in settings

#### ️ Enhanced Text Editing
- **Vim mode implementation** with full modal editing support:
  
  **Normal Mode Commands**:
  - Movement: `h` (left), `l` (right), `j` (down), `k` (up)
  - Line navigation: `0` (start of line), `$` (end of line)
  - Word navigation: `w` (next word), `e` (end of word), `b` (previous word)
  - Document navigation: `gg` (first line), `G` (last line)
  
  **Editing Commands**:
  - `i` - Insert mode at cursor
  - `I` - Insert mode at beginning of line
  - `a` - Insert mode after cursor
  - `A` - Insert mode at end of line
  - `x` - Delete character under cursor
  - `d` + motion - Delete with motion (e.g., `dd` for delete line, `d$` for delete to end of line)
  - `D` - Delete to end of line
  - `c` + motion - Change (delete and enter insert mode)
  - `C` - Change to end of line
  - `.` - Repeat last change

### Improvements

#### Input Handling Refactoring
- Improved paste handling with better chunking for large text inputs
- Enhanced placeholder rendering with cursor display
- Better separation of concerns between input state management and rendering

#### Import Optimizations
- Streamlined Node.js imports:
  - Combined imports from `node:process` (env, cwd)
  - Combined imports from `node:stream` (PassThrough)
  - Reduced redundant import statements

### Technical Changes

#### New Classes/Functions
- `q6` class (renamed from `Gd`) - Enhanced text cursor with new methods:
  - `endOfWord()` - Navigate to end of current/next word
  - `startOfFirstLine()` - Navigate to document start
  - `startOfLastLine()` - Navigate to last line start

- `Uf2()` - Core vim mode state machine handling modal editing
- `jN1()` - Vim-enabled text input component
- `sx()` - Refactored input rendering component
- `y90()` - Paste handling wrapper function

#### Settings
- New `editorMode` setting added to persistent configuration
- Default mode is "emacs" for backward compatibility

### Usage Examples

**Switching to vim mode:**
```bash
$ claude
> vim
Editor mode set to vim. Use Escape key to toggle between INSERT and NORMAL modes.
```

**Using vim navigation:**
```
# In NORMAL mode:
- Press 'i' to enter INSERT mode and start typing
- Press 'Escape' to return to NORMAL mode
- Use 'hjkl' for navigation
- Use 'dd' to delete a line
- Use '.' to repeat the last edit
```

**Switching back to emacs mode:**
```bash
> vim
Editor mode set to emacs. Using standard emacs-style keybindings.
```

The vim mode implementation provides a familiar editing experience for vim users while maintaining full compatibility with the existing emacs-style keybindings. The mode preference persists across sessions, so users only need to switch once.
