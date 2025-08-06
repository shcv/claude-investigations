# Changelog for version 0.2.85

## Claude Code v0.2.85 Changelog

### New Features

#### Environment Variable Management
- **Enhanced environment variable handling**: Environment variables are now loaded from multiple sources in a hierarchical manner. The new system merges environment variables from:
  - Local settings (`localSettings`)
  - Project settings (`projectSettings`) 
  - Managed settings (`managedSettings`)
  
  This allows for more flexible configuration management across different scopes.

#### Model Support
- **Added support for Claude 3.5 Sonnet v2 (October 2022 release)**:
  - First-party API: `claude-3-5-sonnet-20241022`
  - AWS Bedrock: `anthropic.claude-3-5-sonnet-20241022-v2:0`
  - Google Vertex: `claude-3-5-sonnet-v2@20241022`
  
  The new model includes updated pricing:
  - Input tokens: $3 per million
  - Output tokens: $15 per million
  - Prompt cache write: $3.75 per million
  - Prompt cache read: $0.30 per million

#### Cost Tracking
- **Improved unknown model cost handling**: When using models without known pricing information, the system now properly flags this with `hasUnknownModelCost = true` to alert users that cost calculations may be incomplete.

### Improvements

#### Settings Management
- **New settings hierarchy**: Settings can now be stored at different levels with clear visual indicators:
  - Local project settings: `On this machine in [path]`
  - Project settings: `Checked in at .claude/settings.json`
  
- **Settings persistence**: New functions for reading and writing settings with proper JSON formatting and indentation.

#### Performance
- **Lazy initialization**: Added lazy loading for certain operations using a new `jx1` function that initializes components only when needed.

#### Developer Experience
- **Better cost display**: The cost summary now handles cases where cost calculation might be unavailable, providing clearer feedback to users.

### Technical Changes

- Bumped version from 0.37.0 to 0.40.0
- Refactored stream imports to use named imports (`PassThrough`) instead of default imports
- Improved process imports to use named imports (`cwd`) for better tree-shaking
- Added schema validation for package information using Zod
- Removed git checkout special case handling from permission checks

### Bug Fixes

- Fixed environment variable loading to properly merge variables from all configuration sources
- Improved error handling for model configuration fetching with proper fallback behavior
