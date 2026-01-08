# Changelog for version 0.2.51

### New Features

#### Local Installation Migration Tool
A new command `migrate-installer` has been added to help users migrate from global npm installation to a local installation in their home directory. This provides better isolation and avoids global dependency conflicts.

**Usage:**
```bash
claude migrate-installer
```

This interactive command will:
1. Install Claude CLI locally to `~/.claude/local/`
2. Set up shell aliases for the `claude` command
3. Uninstall the global npm package

The migration process includes progress tracking and error handling, with telemetry to monitor success rates.

#### Enhanced Memory Management UI
The memory management interface has been completely redesigned with a more user-friendly selection system:

- **Visual improvements**: Better layout with clear descriptions and examples for each memory type
- **Three memory locations**:
  - **Project memory** - Stored in `./CLAUDE.md` (checked into version control)
  - **Project memory (local)** - Stored in `./CLAUDE.local.md` (gitignored)  
  - **User memory** - Stored in `~/.claude/CLAUDE.md` (global across all projects)
- **Interactive selection**: Use arrow keys to navigate between options with visual feedback
- **Helpful examples**: Each memory type now shows concrete usage examples

#### MCP Server Approval System
New security features for MCP (Model Context Protocol) servers detected in project `.mcp.json` files:

- **Batch approval**: When multiple MCP servers are detected, users can select which ones to enable using a checkbox interface
- **Single server approval**: For projects with one MCP server, a simple yes/no prompt
- **Security warnings**: Clear explanations about MCP server capabilities and risks
- **Persistent choices**: Approved/rejected servers are saved and remembered
- **Management command**: Users can reset their choices with `claude mcp reset-project-choices`

**Interactive prompts:**
- Space to select/deselect servers
- Enter to confirm selections
- Escape to reject all servers

### Improvements

#### Enhanced URL Detection and Handling
- **Improved URL extraction**: Now detects both full URLs and domain names (e.g., `example.com` will be converted to `https://example.com`)
- **HTTP to HTTPS upgrade**: HTTP URLs are automatically upgraded to HTTPS for security
- **Better redirect handling**: Only allows redirects that add "www." to the hostname for security
- **Placeholder system**: URLs in content are replaced with placeholders during processing to avoid false matches

#### WebFetch Tool Updates
- Added guidance to prefer MCP-provided web fetch tools when available
- Updated security notes about URL validation
- Improved error messages for domain restrictions

### Technical Changes

#### ️ Infrastructure Updates
- Added proper handling for Node.js inspector/debugger detection
- Improved telemetry for tracking migration success
- Better error handling in the initialization process
- Enhanced process exit handling with proper cleanup

#### Security Enhancements
- Stricter URL validation removing protocol restrictions (now accepts both HTTP and HTTPS)
- Better domain validation for web fetching
- Enhanced MCP server security with explicit user approval required

### Bug Fixes

- Fixed memory type selection UI to use proper dropdown components instead of manual navigation
- Improved error handling during local installation migration
- Better cleanup of interrupted processes

### Internal Changes

- Added new utility functions for stream handling (`sU4`, `IR4`, `ZR4`, `WR4`)
- Improved partition utility with `JR4` for array splitting
- Enhanced token counting with `eO2` function
- Better component organization with dedicated UI components for MCP approval
