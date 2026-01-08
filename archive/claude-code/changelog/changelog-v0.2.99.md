# Changelog for version 0.2.99


### New Exit Confirmation in Transcript View
When viewing the detailed transcript (accessed via Ctrl+R), users now see a two-step exit confirmation when pressing Ctrl+C:
- First press: Shows "Press ^C again to exit" 
- Second press: Exits the application

This prevents accidental exits when reviewing conversation history.

### Updated Settings Panel
The "Todo List" setting has been renamed to "Todo list tool enabled" for better clarity about what this option controls.

### New Tip of the Day
Added a new tip that shows users the IDE integration hotkey:
- **macOS**: `Cmd+Escape` to launch Claude in your IDE
- **Other systems**: `Ctrl+Escape` to launch Claude in your IDE

This tip appears periodically (every 15 sessions) when IDE integration is available.

### Improved Todo Tool Management
The todo tool list generation now respects the user's todo feature preference more consistently. The `TodoRead` and `TodoWrite` tools are only included when the todo feature is explicitly enabled in settings.

### Code Structure Changes
- Removed unused imports and variables related to stream processing
- Simplified the todo tools initialization logic by moving it to a computed value based on user preferences
- Minor refactoring of the main application component for better performance

## Summary
This release focuses on improving the user experience with better exit handling in transcript view, clearer settings descriptions, and helpful tips for IDE integration. The changes are primarily quality-of-life improvements that make the CLI more intuitive and user-friendly.
