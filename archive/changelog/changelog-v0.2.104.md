# Changelog for version 0.2.104

# Claude Code v0.2.104 Changelog

## New Features

### 🔍 Web Search Integration
- **New `/websearch` command**: Search the web directly from Claude Code
  - Domain filtering supported with `--allowed-domains` and `--blocked-domains` flags
  - Returns formatted search results with titles and URLs
  - Limited to 8 searches per conversation
  - Currently available in the US only
  
  Example usage:
  ```bash
  /websearch "latest React 19 features"
  /websearch "Python async best practices" --allowed-domains=python.org,realpython.com
  ```

### 🖥️ Enhanced IDE Integration
- **New `/ide` command**: Manage IDE connections and integrations
  - Connect to VS Code, Cursor, or other supported IDEs with Claude Code extensions
  - View connection status and available IDEs
  - Disconnect from current IDE
  
  Example usage:
  ```bash
  /ide  # Opens IDE selection interface
  ```

### 💾 Database Status Monitoring
- Added database health checks to system diagnostics
- Database availability now shown in status displays
- Warning when database is unavailable (affects continue/resume features)

## Improvements

### 📊 Token Usage Tracking
- Enhanced token counting with cache-aware metrics
  - Track cache read tokens separately
  - Track cache creation tokens
  - Better cost estimation with unknown model handling
  - Last interaction time tracking

### 🔐 Authentication Improvements
- Improved token refresh mechanism with file locking
  - Prevents race conditions during concurrent refresh attempts
  - Automatic retry with exponential backoff
  - Better error handling for locked resources

### 📝 Memory Management
- New memory size warnings:
  - Warning threshold at 92% of limit (previously 95%)
  - Large file detection for memory items exceeding threshold
  - ULTRACLAUDE.md file size monitoring (warns if > 1000 chars)
  
### 🛠️ System Status Display
- Enhanced startup diagnostics showing:
  - Working directory information
  - Memory usage with specific file warnings
  - IDE connection status
  - Database availability

## Technical Changes

### Dependencies
- Added `graceful-fs` for improved file system operations
- Added `proper-lockfile` for concurrent access control
- Added `retry` for robust operation retries
- Added `signal-exit` for better process cleanup

### Internal Improvements
- Better error handling for file system operations
- Improved retry logic for transient failures
- Enhanced process signal handling
- More robust file locking mechanisms

## Bug Fixes
- Fixed duplicate comment issue in generated code
- Improved handling of file system errors (EMFILE, ENFILE)
- Better cleanup on process exit
- Fixed race conditions in token refresh

## Beta Features
- Support for custom betas via `ANTHROPIC_BETAS` environment variable
  - Comma-separated list of beta feature flags
  - Example: `ANTHROPIC_BETAS=feature1,feature2`
