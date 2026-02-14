# Changelog for version 0.2.123

Based on my analysis of the diff file for version 0.2.123, here is the detailed changelog:


### 🆕 New Features

#### Claude 3.7 Sonnet Model Support
- **New Model Available**: Added support for Claude 3.7 Sonnet, the latest and most capable model
- **Default Model Update**: Claude 3.7 Sonnet is now the default recommended model
- **Model Selection UI**: Updated model selector now shows:
  - "Sonnet (recommended)" - Claude 3.7 Sonnet for daily use · $3/$15 per Mtok
  - For MAX users: "Default (recommended)" - Use the best available model for MAX usage limits
- **New Model String Functions**: Added `sonnet37` model references alongside existing `haiku35` and `sonnet35`

#### AWS Bedrock Integration Improvements
- **Dynamic Model Discovery**: Added automatic detection of available Anthropic models in AWS Bedrock
- **Model Inference Profiles**: New support for AWS Bedrock inference profiles to discover and use available Claude models
- **Auto-configuration**: The CLI now automatically finds and configures available Claude models when using Bedrock as the provider:
  ```javascript
  // Example of discovered models:
  {
    haiku35: "claude-3-5-haiku-20241022",
    sonnet35: "claude-3-5-sonnet-20241022", 
    sonnet37: "claude-3-7-sonnet-20250219"
  }
  ```

#### Native Binary Auto-Updater (Experimental)
- **Local Installation Support**: New native binary installation and update system that doesn't require npm
- **Auto-Update Mechanism**: Automatic background updates without requiring restarts
- **Shell Integration**: Automatically sets up `claude` alias in your shell configuration (.bashrc, .zshrc, or .config/fish/config.fish)
- **Version Management**: Tracks "latest" and "known-good" versions with automatic fallback
- **Update Status Display**: Shows update progress and success/failure status in the UI
- **Installation Command**: Run migration with the new installation system when feature is enabled

#### IDE Integration Enhancements  
- **Real-time Diagnostics**: New diagnostics integration that tracks code issues in real-time
- **Diagnostic Tracking**: Monitors and reports new diagnostic issues (errors, warnings, lints) that appear after file edits
- **Smart Diagnostic Filtering**: Only shows diagnostics that appeared after Claude made changes, filtering out pre-existing issues
- **Multi-source Support**: Handles diagnostics from both regular files (`file://`) and Claude's virtual file system (`_claude_fs_right:`)
- **Linter Recognition**: Identifies diagnostics from popular linters including ESLint, Prettier, Pylint, RuboCop, and many others

#### Enhanced Rate Limit Handling
- **MAX Tier Detection**: New ability to detect Claude MAX subscription tiers (5x and 20x rate limits)
- **Intelligent Fallback**: Automatic model fallback when hitting rate limits for MAX users
- **Unified Rate Limit System**: New `unifiedRateLimitFallbackAvailable` flag for better rate limit management
- **Quota Checking**: New `D65()` function to check API quota status


### Improvements

#### Permission System Enhancements
- **Detailed Decision Reasons**: Permission prompts now show exactly why a permission was allowed or denied
- **Rule Suggestions**: When permissions are denied, the system suggests appropriate rules to allow the action
- **Multi-level Reasoning**: Shows permission decisions for subcommands with hierarchical reasoning display
- **Visual Indicators**: Uses colored checkmarks (✓) and crosses (✗) to indicate allowed/denied permissions

#### Configuration Management
- **Migration System**: New automatic migration for moving API keys and environment variables to user settings
- **Environment Variable Migration**: Migrates global config environment variables to user settings
- **Forced Local Installation**: Can automatically migrate users from npm global installation to local installation

#### UI/UX Improvements
- **Message Idle Notifications**: New `messageIdleNotifThresholdMs` setting (default: 60000ms) for idle notifications
- **Auto-compact Messages**: Better handling of message compaction for cleaner conversation display
- **Improved Error Messages**: New `RetryError` class provides better context for retry failures
- **Enhanced Tooltips**: More descriptive tooltips for model selection and feature explanations


### Bug Fixes

- Fixed duplicate imports and variable declarations
- Removed unused model configuration functions
- Improved handling of MCP (Model Context Protocol) tool filtering
- Better error handling for AWS Bedrock model discovery
- Fixed issues with diagnostic file path matching


### Internal Changes

- **New Utility Functions**:
  - `EU4()`: Combines and deduplicates arrays
  - `yZ2()`: Checks for set intersections
  - `a25()`: Merges message contents
  - `vS2()`: Finds related tool uses in conversation
  
- **Improved Tool Filtering**: Enhanced logic for filtering available tools based on permissions and MCP capabilities
- **Code Organization**: Better separation of concerns for model management, diagnostics, and permissions


### Notes for Developers

- The native auto-updater is controlled by the `ENABLE_IDE_INTEGRATION` environment variable
- AWS Bedrock integration requires proper AWS credentials configured
- The diagnostics feature integrates with IDEs through MCP protocol
- Model strings are now dynamically determined based on the provider (claude.ai vs Bedrock)

This update focuses heavily on improving the model selection experience, adding support for the latest Claude 3.7 Sonnet model, and providing better integration with AWS Bedrock and development environments through enhanced diagnostics support.
