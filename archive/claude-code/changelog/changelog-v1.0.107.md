# Changelog for version 1.0.107

## Highlights
Version 1.0.107 removes the conversation compacting feature that allowed users to condense chat history while maintaining navigation markers. This change streamlines the codebase by eliminating the compact boundary system and its associated UI components.


### Enhanced File System Support
**What:** Added current working directory access functionality
**How to use:**
The CLI now has improved file path resolution capabilities for better cross-platform compatibility and file operations.
**Details:**
- Internal enhancement for file system operations
- Improved path handling across different operating systems
- **Evidence**: `{ cwd as vP2 } from "node:process"` at line 361243


### Conversation Compacting
**What:** The conversation compacting feature has been completely removed
**Previously:** Users could compact conversation history while maintaining a boundary marker with "ctrl+r for history" functionality
**Impact:** 
- No longer possible to compact conversations to manage context length
- The "Conversation compacted · ctrl+r for history" UI is no longer available
- Compact boundary system messages are no longer generated
**Details:**
- **Evidence**: Functions `Z9B()` at line 391737, `EG1()` at line 391749, `Lf6()` at line 391752, `c_1()` at line 391759, and `ibB()` at line 411623 removed from v1.0.106
- All references to "compact_boundary" and "Conversation compacted" text eliminated
- Related metadata tracking for compacting triggers and token counts removed


### Internal Code Refactoring
Systematic renaming of internal functions and variables for code organization, including main component functions and React hook references. These changes do not affect user-facing functionality.
