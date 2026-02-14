# Changelog for version 1.0.110

## Highlights
Version 1.0.110 introduces enterprise MCP server management, WezTerm terminal configuration support, and OAuth token refresh capabilities. The release also includes significant improvements to command queue management, WebSocket reliability, and pipe command handling.


### Enterprise MCP Server Management
**What:** Centralized MCP server configuration for enterprise deployments
**How to use:**
```bash
# Enterprise administrators can now provide managed-mcp.json
# This file takes precedence over user/project configurations
# Located at ~/.config/claude-code/managed-mcp.json
```
**Details:**
- Enterprise MCP servers have highest priority in resolution order
- Supports centralized configuration management for organizations  
- Enterprise scope integrated into existing MCP server loading system
- **Evidence**: `zC1() at line 352611`, `Ie1() at line 352953`, enterprise scope handling at `line 352598`


### WezTerm Terminal Configuration
**What:** Automatic setup of WezTerm terminal with Shift+Enter key binding
**How to use:**
```bash
# Run setup when WezTerm is detected as your terminal
claude setup
```
**Details:**
- Automatically configures `.wezterm.lua` with Shift+Enter → newline binding
- Creates backup of existing configuration before modifying
- Handles both new configs and existing configs with proper merging
- Validates existing bindings to prevent conflicts
- **Evidence**: `WN9() at line 364690`, WezTerm case added at `line 364656`


### OAuth Token Refresh Support
**What:** Proactive and on-demand refresh of OAuth tokens for MCP servers
**How to use:**
```bash
# Tokens are automatically refreshed when they expire soon
# Manual refresh available through MCP server reconnection
```
**Details:**
- Proactive refresh when tokens expire within 5 minutes (300 seconds)
- Automatic retry mechanism with proper error handling
- Maintains existing tokens if refresh fails
- Supports both refresh_token and authorization_code flows
- **Evidence**: `refreshAuthorization() at line 391499`, proactive refresh logic at `line 391410`


### Command Queue Management System
**What:** Dedicated queue manager for better command handling and editing integration
**How to use:**
```bash
# Queue multiple commands and edit them as a batch
# Commands can be queued while others are running
# Seamless transition from queue to editing mode
```
**Details:**
- New centralized queue manager with structured operations
- `popAllForEditing` method combines queued commands with current input
- Reactive updates with callback system for UI synchronization
- Atomic operations ensure consistent queue state
- **Evidence**: `yD() at line 421598`, `nrB() at line 436658`, `popAllForEditing() at line 421622`


### Enhanced WebSocket Reliability
- Added ping/keepalive functionality with 10-second intervals
- New close callback support for better connection lifecycle management
- Improved reconnection behavior with faster failure detection (3 attempts vs 5)
- **Evidence**: `startPingInterval() at line 440256`, `setOnClose() at line 440243`


### Improved Pipe Command Handling
- Complete rewrite of pipe parsing algorithm for multiple pipe support
- New safety check for multiple directory changes in piped commands
- Better command segment reconstruction with proper tokenization
- Enhanced error messages for complex command sequences
- **Evidence**: `uv6() at line 382406`, multiple cd detection at `line 382407`


### Text Styling Architecture Improvements
- Refactored from callback-based to property-based styling system
- New dedicated style application function for consistent rendering
- Better separation of style definition from application
- Improved text processing pipeline with integrated style support
- **Evidence**: `UU1() at line 360092`, `internal_styles` property usage at `line 361236`


### Box Component Color Support
Enhanced box component with theme-aware border colors using the new styling system


### Goodbye Messages
Added variety to exit messages with randomized farewell phrases


### Date Formatting Utility
New date formatting function for consistent timestamp display across the application
