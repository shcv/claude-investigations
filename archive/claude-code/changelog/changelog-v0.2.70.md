# Changelog for version 0.2.70


### New Features

#### Enhanced Conversation Management
- **Conversation ID Tracking**: A new conversation ID system has been introduced that automatically generates and tracks unique identifiers for each conversation branch. This enables better organization of chat history and conversation forks.
  - Example: When you start a new conversation or fork an existing one, Claude Code now assigns it a unique ID like `a3b2c1d4e5f6` that persists throughout the session.

#### Improved Command Permission System
- **Deny Rules for Commands**: The Bash tool now supports explicit deny rules in addition to allow rules. This provides more granular control over which commands Claude can execute.
  - You can now specify both allowed and denied command patterns
  - Deny rules take precedence over allow rules for enhanced security
  - Example: You could allow all `git` commands except `git push` by setting appropriate rules


### User Interface Improvements

#### Settings Display Enhancement
- The settings display function has been renamed and improved for better clarity. Settings descriptions now show more contextual information about their scope and effect.


### Performance Optimizations

#### Reduced Notification Timeout
- The timeout for "Claude is waiting for your input" notifications has been reduced from 5 minutes to 60 seconds (1 minute), providing more timely feedback when Claude is idle and waiting for user input.


### Architecture Changes

#### Message History Management
- New `setMessageHistory` functionality has been added alongside the existing `setMessages`, allowing for better separation between current conversation state and historical message tracking.

#### Streamlined Dependencies
- Removed several unused functions and imports related to message file naming and fork number management
- Consolidated stream handling by switching to a single PassThrough stream import
- Removed the hardcoded list of restricted commands from the Bash tool description


### Bug Fixes

- Fixed parameter ordering issues in the escape key handler
- Improved command matching logic to handle both exact matches and prefix-based patterns more reliably
- Enhanced error handling for conversation branching scenarios with better validation of message order


### Internal Improvements

- Simplified the permission checking flow for the Bash tool
- Reduced code duplication in permission rule handling
- Better separation of concerns between allow and deny rule processing
