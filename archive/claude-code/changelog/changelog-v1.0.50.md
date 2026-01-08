# Changelog for version 1.0.50

# Claude Code v1.0.50 Changelog

### Plan Rejection UI Enhancement
- **Improved visual feedback when users reject proposed plans**: When a user rejects Claude's proposed plan and chooses to stay in plan mode, the interface now displays a dedicated UI component with:
  - A clear error message: "User rejected Claude's plan:"
  - The rejected plan displayed in a bordered box with proper styling
  - Better visual distinction using the plan mode theme colors

### Example Usage:
When Claude proposes a plan and the user rejects it, they'll now see a more informative display instead of a generic message. This helps users understand what was rejected and provides better context for continuing in plan mode.

### Import Optimizations
- Streamlined Node.js module imports:
  - Consolidated process imports to use named imports (`import { cwd as OMA } from "node:process"`)
  - Optimized stream imports to use specific components (`import { PassThrough } from "node:stream"`)
  - Removed redundant duplicate imports for `stream` and `node:process` modules

### Code Organization
- Added new UI component `yz1` for rendering rejected plan messages
- Introduced new constant `Nk` with a descriptive rejection message template
- Added response filtering logic with `tA1` ("No response requested.") to the response set

### Message Handling Improvements
- Enhanced the message error rendering function to differentiate between:
  - Standard tool execution errors
  - Plan rejection scenarios (now with dedicated UI)
- Added theme-aware rendering for plan rejection messages using the current theme context

### Performance
- Reduced bundle size by removing 4 redundant imports
- Better code organization with more specific imports


**Note**: This update focuses on improving the user experience when working with Claude's plan mode, particularly when users choose to reject proposed plans and continue iterating. The visual improvements make it clearer what was rejected and why the user is still in plan mode.
