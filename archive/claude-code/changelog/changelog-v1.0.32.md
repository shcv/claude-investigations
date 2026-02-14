# Changelog for version 1.0.32


### New Features

#### Plan Mode
- **New interactive planning feature**: Claude can now present implementation plans before writing code
- When tackling complex coding tasks, Claude will:
  - Analyze requirements and create a structured plan
  - Present the plan in markdown format for your review
  - Wait for your approval before proceeding with implementation
- **Usage**: Automatically activated for implementation tasks requiring code changes
- **Example**: When you ask "Help me implement dark mode for my app", Claude will first present a plan outlining the steps before making any code changes

#### Exit Plan Mode Tool
- New `exit_plan_mode` tool allows Claude to transition from planning to implementation
- Supports markdown-formatted plans for better readability
- Distinguishes between research tasks (no plan needed) and implementation tasks (plan recommended)


### Improvements

#### Performance Enhancements
- **HTTP Agent Caching**: Improved performance for operations involving multiple HTTP requests through agent caching
- Reduced overhead when making repeated network calls

#### Configuration Directory Handling
- **Simplified config directory resolution**: The configuration directory logic has been streamlined
- Now uses the nullish coalescing operator (`??`) for cleaner fallback handling
- Priority remains: `CLAUDE_CONFIG_DIR` environment variable → default `~/.claude` directory
- **Note**: Support for `XDG_CONFIG_HOME` has been removed in favor of the simpler approach

#### Error Handling
- **Enhanced BigInt handling**: Better error messages when encountering BigInt values that cannot be converted to numbers
- **Improved type conversion**: More robust handling of numeric type conversions with clearer error reporting
- **Better JSON parsing errors**: More informative error messages for JSON parsing failures


### Technical Improvements
- Removed several unused modules related to:
  - WebIDL type conversions (`KD2`, `wD2`)
  - Unicode/Punycode processing (`ED2`, `LD2`, `iw`)
- Code cleanup and optimization resulting in a slightly smaller bundle size
- Structural similarity with v1.0.31: 99.6%


### Bug Fixes
- Various stability improvements in error handling paths
- Better handling of edge cases in type conversions


### Summary
Version 1.0.32 introduces Plan Mode as the major user-facing feature, allowing for better collaboration between users and Claude on complex coding tasks. The update also includes performance improvements, simplified configuration handling, and enhanced error reporting, making Claude Code more efficient and user-friendly.
