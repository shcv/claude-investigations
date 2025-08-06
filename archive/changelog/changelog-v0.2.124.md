# Changelog for version 0.2.124

# Claude Code v0.2.124 Changelog

## Summary
This release includes minor improvements to AWS Bedrock model discovery, better error handling, and updates to the CLI launcher script.

## Changes

### Improved AWS Bedrock Model Discovery
The model discovery function has been enhanced with better error handling and a more efficient implementation:

- **Better error handling**: The function now catches and logs errors when attempting to discover available models, falling back gracefully to default Bedrock models
- **Refactored helper function**: The model search helper `U81` is now a pure function that accepts the model list as a parameter, making it more testable and reusable
- **Explicit null checking**: Added explicit checks for empty or null model lists before attempting to search

**Usage impact**: Users working with AWS Bedrock will experience more reliable model discovery, with clearer fallback behavior when model listing fails.

### CLI Launcher Script Update (v0.0.1 → v0.0.2)
The bash launcher script has been updated with a subtle but important change in cleanup behavior:

```diff
- # 1. If latest link exists, remove the link and exec it
+ # 1. If latest link exists, exec it (the app will handle cleanup)
```

**What this means for users**: The launcher no longer removes the "latest" symlink before executing Claude Code. Instead, the application itself now manages this cleanup, providing more reliable update handling and preventing potential race conditions during launches.

### Code Organization Improvements
- Consolidated stream imports to use named imports from the `stream` module
- Reorganized process-related imports to use named imports from `node:process`
- Minor code cleanup and consistency improvements

## Technical Details
- Structural similarity with previous version: 99.9%
- Total changes: 5 additions, 5 deletions, 1 modification
- The core functionality remains unchanged, with improvements focused on reliability and error handling
