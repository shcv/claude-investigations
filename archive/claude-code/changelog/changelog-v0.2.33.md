# Changelog for version 0.2.33


### New Features

#### Improved `/compact` Command
- **Enhanced message preservation**: The `/compact` command now intelligently preserves recent messages while summarizing older conversation history
- **Better handling of tool use**: Fixed issues where tool use messages could become "dangling" during compaction
- **Configurable preservation**: The command now preserves the last 10 messages by default (`fS2 = 10`) while summarizing older content
- **Improved telemetry**: Added tracking for compacted vs preserved message counts


### Bug Fixes

#### Error Reporting Improvements
- **Enhanced error details**: Bug reports now include structured error information in JSON format
- **Stack trace collection**: Added error stack trace collection to help diagnose issues more effectively
- **Better error context**: Bug reports now include complete error objects with stack traces


### Removed Features

#### Removed A/B Testing UI
The following experimental features have been removed:
- Binary feedback comparison UI (`prefer-left`, `prefer-right` options)
- Side-by-side message comparison interface
- A/B testing telemetry functions (`JE2`, `zE2`)
- Visual comparison components (`wf1`, `IQ9`, `zm2`, `gm2`)

#### Removed Internal Components
- Removed `BatchTool` variable
- Removed `onboarding` command (was ANT-ONLY and disabled)
- Removed various stream imports that were unused


### Technical Changes

#### DOM Implementation Additions
- Added extensive DOM API implementations including:
  - Event system (`Event`, `UIEvent`, `MouseEvent`, `CustomEvent`)
  - Node iteration (`NodeIterator`)
  - URL handling utilities
  - CSS style manipulation
  - Complete HTML element implementations
  - SVG element support
  - Document type handling

#### Code Organization
- Significant refactoring of internal modules
- Better separation of DOM-related functionality
- Improved module structure with clearer boundaries


### Performance Improvements

- Optimized message compaction to avoid unnecessary processing
- Better memory management during conversation compaction
- More efficient handling of large conversation histories


### User Experience Improvements

- Cleaner conversation management with improved `/compact` functionality
- More reliable preservation of recent context when compacting conversations
- Better error messages and feedback during operations
