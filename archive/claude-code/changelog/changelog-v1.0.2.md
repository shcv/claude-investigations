# Changelog for version 1.0.2

# Claude Code v1.0.2 Changelog

## Breaking Changes
None

### Model Token Limit Updates
- **Removed Opus model-specific token limit**: The function that determines token limits for different Claude models no longer includes a special case for Opus models. Previously, Opus models had a 4096 token limit, but now they will use the default 20,000 token limit.
  
  This means when using Claude Code with Opus models, you can now include much longer contexts in your requests - up to 20,000 tokens instead of the previous 4,096 token limit.

### Internal Improvements
- **Optimized imports**: Refactored Node.js imports to be more specific:
  - Changed from importing the entire `node:process` module to importing only the `cwd` (current working directory) function
  - Changed from importing the entire `stream` module to importing only the `PassThrough` class
  
  These changes improve code efficiency by reducing unnecessary imports and making the codebase more modular.

## Summary
This is a minor update focused on internal optimizations and expanding token limits for Opus models. Users working with Opus models will benefit from the ability to process significantly larger contexts (5x increase in token limit). The import optimizations are internal improvements that won't affect the user experience but contribute to better code organization and potentially faster startup times.
