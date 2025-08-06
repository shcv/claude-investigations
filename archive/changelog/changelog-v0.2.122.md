# Changelog for version 0.2.122

# Claude Code v0.2.122 Changelog

## New Features

### Co-Authorship Attribution
- **Added automatic co-authorship credits** for Claude-generated commits and pull requests
  - When Claude helps create commits, it now automatically adds a "Co-Authored-By: Claude <noreply@anthropic.com>" line to the commit message
  - Pull requests created with Claude's assistance include a "🤖 Generated with Claude Code" attribution
  - This feature can be disabled by setting `includeCoAuthoredBy` to `false` in your configuration
  
  **Example**: When you ask Claude to create a commit, the commit message will now include:
  ```
  Your commit message here
  
  🤖 Generated with Claude Code
  
  Co-Authored-By: Claude <noreply@anthropic.com>
  ```

## Technical Changes

### Import Optimizations
- Replaced generic `stream` import with more specific `PassThrough` import from the stream module
- Changed from importing the entire `node:process` module to only importing the `cwd` function
- These changes improve startup performance by reducing unnecessary module loading

### Internal Updates
- Added new internal variable binding for improved module compatibility
- Minor structural improvements maintaining 99.9% similarity with previous version

## Summary
This release focuses on giving proper attribution when Claude assists with git operations, making it clear which commits and pull requests were created with AI assistance. The co-authorship feature is enabled by default but can be disabled if needed. Additionally, some import optimizations were made to improve performance.
