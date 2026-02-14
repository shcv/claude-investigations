# Changelog for version 0.2.47

# Claude Code v0.2.47 Changelog


### Tab Completion for Files and Folders
- **Press Tab** to auto-complete file and folder names while typing paths
- Works in interactive mode when entering file paths
- Speeds up navigation and reduces typing errors


### Auto-Accept Mode for File Edits
- **Press Shift+Tab** to toggle auto-accept mode for file edits
- When enabled, file edits are automatically accepted without confirmation prompts
- Visual indicator shows when auto-accept is active: `⏵⏵ auto-accept edits on`
- Particularly useful for workflows with many trusted file modifications


### ️ Automatic Conversation Compaction
- Conversations can now continue indefinitely without hitting token limits
- Claude automatically compacts older messages when approaching token thresholds
- Toggle this feature on/off using the `/config` command
- Preserves conversation context while managing token usage efficiently


### Improved Thinking Mode Control
- New environment variable `MAX_THINKING_TOKENS` allows precise control over thinking token allocation
- Set a specific number of thinking tokens instead of relying on keyword detection
- Example: `export MAX_THINKING_TOKENS=8000`


### Better Error Privacy
- Enhanced redaction of sensitive information in error messages and stack traces
- Automatically redacts:
  - Anthropic API keys (`sk-ant-*`)
  - AWS keys (`AKIA*` patterns)
  - GCP keys (`AIza*` patterns)
  - GCP service accounts (`*@*.iam.gserviceaccount.com`)
  - Generic API keys in various formats


### Improved Bug Report Titles
- Bug report title generation now creates more technical, descriptive titles
- Better extraction of key error messages for clearer issue tracking
- Fallback to simple title extraction if AI generation fails


### Enhanced Permission Prompts
- Permission prompts now show numbered options (1, 2, 3) for easier selection
- Type the number to quickly select an option
- Escape key consistently selects "No" across all prompts
- More consistent formatting and better visual hierarchy

## Technical Improvements

- Stream imports updated from default imports to named imports for better compatibility
- Process imports now use `node:process` prefix for clarity
- Removed unused imports and variables for cleaner codebase
- Added fallback behavior for bug report title generation


### Using Tab Completion
```bash
# Start typing a path and press Tab
$ claude read /home/user/proj[TAB]
# Completes to: /home/user/projects/

$ claude edit ./src/comp[TAB]
# Shows available completions or completes if unique
```


### Toggling Auto-Accept Mode
```bash
# During a conversation, press Shift+Tab
# You'll see: ⏵⏵ auto-accept edits on (shift+tab to toggle)

# All subsequent file edits will be automatically accepted
# Press Shift+Tab again to disable
```


### Setting Maximum Thinking Tokens
```bash
# Set a specific thinking token limit
$ export MAX_THINKING_TOKENS=15000
$ claude

# Now all thinking operations will use exactly 15000 tokens
```
