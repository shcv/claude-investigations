# Changelog for version 0.2.74

# Claude Code v0.2.74 Changelog

### Enhanced Caching System
- Added a new caching mechanism with automatic refresh capabilities (`P$2` function)
  - Supports configurable TTL (default: 5 minutes)
  - Automatically refreshes stale cache entries in the background
  - Prevents duplicate requests while refreshing
  - Accessible cache clearing via `.cache.clear()` method

### Improved Diff Viewer Layout
- Enhanced the diff viewer component with dynamic width calculation
  - Now automatically adjusts to container width when not explicitly specified
  - Default width set to 80 characters
  - Better responsive behavior for patch display

### Node Dimension Utilities
- Added `OV9` helper for extracting computed dimensions from Yoga layout nodes
  - Returns width and height from Yoga node computations
  - Provides safe fallback to 0 when node is unavailable

### API Client Refactoring
- Simplified API client initialization logic
  - Removed caching of API client instances (removed `Dp` global variable)
  - Each request now creates a fresh client instance
  - Better separation between different authentication modes (Bearer token vs API key)

### Import Optimizations
- Reorganized stream imports to use named imports (`PassThrough`)
- Consolidated process imports to use named imports (`cwd`)
- Improved module loading efficiency

### Code Quality Improvements
- Removed unused functions and variables
- Better error handling in the caching system
- Cleaner separation of concerns in API authentication flow

## Bug Fixes

- Fixed potential memory leaks from cached API client instances
- Improved error handling for cache refresh failures
- Better handling of edge cases in diff viewer width calculations

## Breaking Changes

None - This release maintains full backward compatibility with v0.2.73.
