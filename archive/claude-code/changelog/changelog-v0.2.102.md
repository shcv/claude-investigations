# Changelog for version 0.2.102

# Claude Code v0.2.102 Changelog


### Enhanced Paste Reference System
The paste functionality has been significantly improved with a new reference system that allows users to reference multiple pasted items (both text and images) within a single conversation.

**New paste reference format:**
- Text pastes: `[Pasted text #1 +100 lines]` - Shows paste ID and line count
- Images: `[Image #1]` - Shows image ID

**How it works:**
When you paste multiple items during a conversation, Claude Code now assigns unique IDs to each paste. This allows you to reference specific pastes later in the conversation by their ID number.


### Improved Directory Handling
The `isDirEmptySync` function now includes an existence check before checking if a directory is empty. This prevents errors when working with non-existent directories.

```javascript
// Old behavior: Would error if directory doesn't exist
function isDirEmptySync(path) {
  return fs.isDirEmptySync(path);
}

// New behavior: Returns true for non-existent directories
function isDirEmptySync(path) {
  if (!fs.existsSync(path)) return true;
  return fs.isDirEmptySync(path);
}
```


### Command Execution Enhancement
The slash command system now properly propagates the `shouldQuery` flag from command handlers. This allows custom commands to control whether their output should trigger a follow-up query to Claude.

**Example usage:**
```bash
# Custom commands can now return both messages and control query behavior
/my-command some arguments
# The command can decide whether Claude should process the result further
```


### Better Thinking Mode Detection
The "thinking" feature detection has been improved to use proper word boundary regex patterns instead of simple string includes. This prevents false positives when these keywords appear as part of other words.

**Thinking triggers (with proper word boundaries):**
- "think" → 4,000 tokens
- "think hard", "think deeply", "megathink" → 10,000 tokens  
- "think harder", "ultrathink" → 31,999 tokens


### History Navigation Updates
The command history system now properly tracks pasted content alongside commands, maintaining the association between prompts and their pasted attachments when navigating through history with arrow keys.


### Import Optimizations
- Removed unused `stream` import
- Removed duplicate `node:process` import
- Added targeted import for `cwd` from `node:process`
- Added `PassThrough` stream import where needed


### New Internal Functions
- `El5`: Filters user messages for processing
- `wo1`: Formats pasted text references
- `FQ6`: Formats image references
- `IQ6`: Extracts paste references from text
- `dI1`: Processes conversation history with paste content
- `ke5`: Compares paste content objects for equality

These changes improve the overall robustness of paste handling, command execution, and user interaction within Claude Code.
