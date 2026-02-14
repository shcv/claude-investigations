# Changelog for version 0.2.91


### New Features

#### 1. Conversation History Database Storage
Claude Code now stores conversation history in a local SQLite database, providing persistent storage and better performance for conversation management.

- New database schema includes tables for:
  - Base messages with parent-child relationships
  - User messages with content and tool results
  - Assistant messages with model info, cost, and duration
  - Conversation summaries for quick browsing

#### 2. Enhanced Conversation Browser
The conversation browser has been significantly improved with:

- **Automatic conversation summaries**: Claude generates concise 5-10 word titles for each conversation
- **Better organization**: Shows modification time, creation time, and message count for each conversation
- **Sidechain support**: Properly handles and displays sidechain conversations
- **Mixed storage**: Seamlessly combines file-based and database-stored conversations

Example usage:
```bash
# Browse previous conversations with enhanced UI
claude --logs
```

The browser now displays:
- Modified time (e.g., "2 hours ago")
- Created time
- Number of messages
- Auto-generated summary or first message preview
- Sidechain indicator when applicable

#### 3. Claude Max Subscription Integration
New support for Claude Max subscriptions with automatic detection and notifications.

- Checks if your account has Claude Max access
- Shows a one-time notification if Claude Max is available
- Prompts to login to activate the subscription

The notification appears as:
```
Your can now use your Claude Max subscription with Claude Code • /login to activate
```


### Improvements

#### 1. Relative Time Formatting
Added human-friendly relative time display throughout the interface:
- "2 hours ago" instead of timestamps
- "in 5 minutes" for future times
- Narrow format for recent times (e.g., "5m ago", "2h ago")

#### 2. Message Filtering
New message filtering logic that removes redundant tool use messages from conversation display, making conversations cleaner and easier to read.

#### 3. Tool Permission Flow
Improved the tool permission dialog flow:
- Better handling of tool rejection scenarios
- More consistent permission context management
- Enhanced file operation permission requests


### API and Configuration Updates

#### 1. New API Base URL Configuration
Added `BASE_API_URL` to configuration for better API endpoint management:
- Production: `https://api.anthropic.com`
- Development: `http://localhost:3000`


### Technical Changes

#### 1. Database Migration System
- Automatic database creation and migration on first use
- Support for both Bun and Node.js SQLite drivers
- Atomic transaction support for data integrity

#### 2. Performance Optimizations
- Parallel loading of conversation summaries
- Efficient database queries with recursive CTEs
- Caching of conversation summaries

#### 3. Stream Processing
Changed from using `Stream` to `PassThrough` for better stream handling compatibility.


### Bug Fixes

- Fixed duplicate conversation display issues
- Improved error handling for database operations
- Better handling of malformed conversation files
- Fixed permission dialog edge cases


### Internal Changes

- Removed several unused functions and imports
- Consolidated message storage logic
- Improved code organization for conversation management
- Enhanced type safety for database operations
