# Changelog for version 0.2.118

# Claude Code v0.2.118 Changelog

## Summary
Version 0.2.118 introduces minor refactoring changes focused on code organization and visual presentation. The main changes involve extracting attachment processing logic into a dedicated function and simplifying the thinking indicator UI.


### Code Organization Improvements

#### New Attachment Processing Function
A new function `uo2` has been introduced to handle all attachment types in a more modular way:

```javascript
function uo2(attachment) {
  switch (attachment.type) {
    case "directory":
      // Returns directory listing tool calls
    case "file":
      // Handles both edited and new files
    case "selected_lines_in_ide":
      // Handles IDE selection events
    case "opened_file_in_ide":
      // Handles IDE file open events
    case "todo":
      // Handles todo list updates
    case "nested_memory":
      // Handles nested memory content
    case "queued_command":
      // Handles queued commands
    case "ultramemory":
      // Handles ultramemory content
  }
}
```

This refactoring improves code maintainability by:
- Centralizing all attachment processing logic in one place
- Making the main message processing function (`Jw`) cleaner and more focused
- Returning arrays of messages, allowing for more flexible message composition


### UI Improvements

#### Simplified Thinking Indicator
The thinking indicator display has been simplified:

**Before:**
- Used a bordered box with single-line border on the left
- Complex padding and margin configuration
- Multiple style properties for the border

**After:**
- Simple indentation using `paddingLeft: 2`
- Cleaner, more minimal appearance
- Removed the border styling entirely

This change makes the thinking indicator less visually intrusive while maintaining clarity.


### Bug Fixes

#### System Reminder Formatting
Added proper closing tags for system reminders in edited file notifications:
```javascript
// Now properly closed with:
$6({ content: "</system-reminder>", isMeta: !0 })
```


### GitHub Action Update
The GitHub Action reference has been updated from:
- `anthropics/claude-code-pr-action@beta`

To:
- `anthropics/claude-code-action@beta`

This suggests a rename or consolidation of the GitHub Action.


### Technical Updates

#### Import Changes
- Replaced generic process import with specific `cwd` import from `node:process`
- Added `PassThrough` stream import for potential streaming improvements
- Added `randomUUID` import from `node:crypto` for unique identifier generation

These changes suggest preparation for improved streaming capabilities and better unique ID generation.

## User Impact

For CLI users, these changes are mostly internal improvements that won't affect the command-line interface or interactive experience. However, you may notice:

1. **Cleaner thinking indicator**: The "✻ Thinking..." indicator now appears with simple indentation rather than a bordered box
2. **Improved reliability**: The refactored attachment handling should provide more consistent behavior when working with files, directories, and other attachments
3. **Better GitHub integration**: If using Claude Code with GitHub Actions, you'll need to update to the new action name

No changes to command-line arguments, flags, or interactive commands were introduced in this version.
