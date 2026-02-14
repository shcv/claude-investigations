# Changelog for version 1.0.43

# Claude Code v1.0.43 Changelog


### New Theme Preview Feature
Version 1.0.43 introduces a major enhancement to the theme management system with the ability to preview themes before applying them permanently.

#### Key Changes:

**Enhanced Theme Context**
- The theme context has been completely redesigned with a richer API
- New context structure includes:
  ```javascript
  {
    theme: null,           // Current saved theme
    setTheme: (A) => A,    // Set and save theme
    setPreviewTheme: (A) => A,  // Preview theme without saving
    savePreview: () => {},      // Save the previewed theme
    currentTheme: null,    // Active theme (preview or saved)
  }
  ```

**New Theme Provider Component**
- Added `jT1` component that provides theme state management
- Tracks both saved themes and preview themes separately
- Allows users to test themes before committing to them

**Updated Theme Hook**
- The `hB` hook now returns `currentTheme` instead of just the saved theme
- This means components will automatically use preview themes when active


### User-Facing Benefits:

1. **Try Before You Apply**: You can now preview how a theme looks before permanently switching to it
2. **Easy Rollback**: If you don't like a preview theme, simply don't save it
3. **Seamless Testing**: The UI updates immediately when previewing themes, giving instant feedback


### Usage Example:
When using Claude Code, you might interact with themes like this:
- Preview a theme temporarily to see how it looks
- If you like it, save the preview to make it permanent
- If not, the preview is discarded and your original theme remains


### Stream Handling Updates
- Migrated from generic stream imports to more specific `PassThrough` imports
- Added `PassThrough` imports from both `node:stream` and `stream` modules
- This likely improves performance and reduces bundle size


### Process Module Import
- Added specific import for `cwd` (current working directory) from `node:process`
- Removed generic process import, using only what's needed

These changes represent a focus on improving the user experience around theme customization while also making technical optimizations to the codebase.
