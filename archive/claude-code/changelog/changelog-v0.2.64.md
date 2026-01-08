# Changelog for version 0.2.64

### New Features

#### Tool Call Counter
A new visual indicator that displays the number of tool calls being made during interactions. This can be enabled through the `showToolCallCount` configuration option, helping users track Claude's tool usage in real-time.

#### ULTRACLAUDE.md Support (Experimental)
Introduced experimental support for a new user preferences file called `ULTRACLAUDE.md`. This file:
- Lives in the `.claude` directory alongside other configuration files
- Provides critical user preferences that override default behavior
- Includes a warning when the file exceeds 1000 characters
- Can be edited using the `/memory` command

Example warning display:
```
⚠️ ULTRACLAUDE.md exceeds 1000 chars (1234 chars) • /memory to edit
```

#### Enhanced Permission Debug Info
New permission debugging display that shows detailed information about permission decisions:
- Rule-based decisions with their sources (CLI argument, local settings, or project settings)
- Mode information (Default, Accept Edits, or Bypass Permissions)
- Subcommand results with visual checkmarks (✓) or crosses (✗)
- Hierarchical display of permission decision reasons

Example output:
```
Permission debug info:
✓ read-file
  ⎿ allow rule from CLI argument
✗ write-file
  ⎿ Default mode
```

### Improvements

#### Enhanced Instruction System
- Updated the instruction preamble from "Codebase-specific instructions" to more authoritative language
- New critical user preferences reminder system that seamlessly injects user preferences into conversations
- Preferences are automatically appended to user messages without disrupting the conversation flow

#### ️ Stream Processing Enhancement
The stream event handler now includes an optional callback for tool use detection, allowing the UI to respond immediately when Claude begins using tools.

### Technical Changes

#### New Utility Functions
- Added array utility functions for improved performance:
  - `includes()` implementation with optimized search
  - `uniqBy()` for removing duplicates with custom comparator
  - Enhanced array searching with NaN handling

#### Import Reorganization
- Migrated from direct `stream` imports to named imports (`PassThrough`)
- Updated process and OS imports to use modern Node.js module syntax
- Better organization of platform-specific imports (`EOL`, `platform`, `homedir`)

### Bug Fixes
- Fixed potential issues with instruction content injection by properly handling edge cases in message arrays
- Improved error handling for EACCES permission errors with better telemetry

### Configuration
New configuration option added to the animation settings:
```javascript
{
  useHaiku: false,
  haikuInterval: 5,
  thinking: "default",
  responding: "default", 
  toolUse: "default",
  normal: "default",
  charAnimation: "none",
  showToolCallCount: false  // New option
}
```
