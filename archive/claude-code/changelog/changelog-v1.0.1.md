# Changelog for version 1.0.1

# Claude Code v1.0.1 Changelog


### Enhanced Model Support Detection
- Added new function `vd9` for intelligent model availability checking based on deployment environment
- The function determines which Claude models are available based on the current environment:
  - **Bedrock deployments**: No models available through this check
  - **First-party deployments**: Access to Claude 3.7, Claude Opus 4, and Claude Sonnet 4
  - **Other deployments**: Access to Claude Opus 4 and Claude Sonnet 4 only

This feature allows the CLI to dynamically adjust available model options based on the deployment context, ensuring users only see models they can actually access.


### Import Reorganization
- Streamlined Node.js imports for better module organization:
  - Consolidated process import: Now uses `import { cwd as hB0 } from "node:process"` instead of a default import
  - Consolidated stream import: Now uses `import { PassThrough as N35 } from "stream"` with named import pattern
- Removed redundant import statements while maintaining all functionality

## Internal Improvements

- **Code structure**: 5,645 function renames for improved code organization
- **Bundle size**: Minor optimization with net addition of 1 declaration (6,263 total, up from 6,262)
- **Structural compatibility**: Maintains 100% structural similarity with previous version

## Notes

This is a minor release focusing on model availability detection and import optimization. The changes are backward compatible and require no user action.
