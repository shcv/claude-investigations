# Changelog for version 1.0.87

## 🎯 Highlights
Version 1.0.87 enhances the permission system with granular source tracking and new management operations, while improving session notes extraction to better filter system content. These internal improvements provide better debugging capabilities and more flexible permission control.

## 💪 Improvements

### Enhanced Permission System with Source and Behavior Tracking
**What changed:** Permission rules now include metadata about their origin and behavior type
**Previous behavior:** Rules were simple objects with just type and rules array
**New behavior:** Rules now track their source (session/localSettings/cliArg) and behavior (allow/deny)
**Impact:** Better debugging of permission issues and understanding of where rules originate from

### New Permission Management Operations
**What changed:** Added ability to remove and replace permission rules dynamically
**Previous behavior:** Could only add rules and directories to permissions
**New behavior:** Three new operations available: `removeRules`, `removeDirectories`, and `replaceRules`
**Impact:** More flexible permission management during runtime, allowing selective removal of rules from specific sources

### Improved Session Notes Extraction
**What changed:** Better filtering of system-generated content from session notes
**Previous behavior:** Basic exclusion of note-taking instructions
**New behavior:** Now excludes system prompts, claude.md entries, and past session summaries
**Impact:** Cleaner session notes that only capture actual user conversations

### Permission Update Logging
**What changed:** Added detailed logging for all permission operations
**Previous behavior:** No logging of permission changes
**New behavior:** Every permission update is logged with details about rules, sources, and behaviors
**Impact:** Easier troubleshooting of permission-related issues with clear audit trail

### Working Directory Source Tracking
**What changed:** Working directories now track their configuration source
**Previous behavior:** Directories stored without origin information
**New behavior:** Each directory records whether it came from session, localSettings, or CLI arguments
**Impact:** Better understanding of how working directories were configured for debugging
