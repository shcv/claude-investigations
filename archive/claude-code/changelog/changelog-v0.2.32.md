# Changelog for version 0.2.32


### New Features

#### Interactive MCP Setup Wizard
- **New command: `claude mcp add`** - Launch an interactive step-by-step wizard to configure MCP (Model Context Protocol) servers
  - Step 1: Configure server name
  - Step 2: Set server scope (project-specific or global)
  - Step 3: Specify the command to run the server
  - Step 4: Add command arguments
  - Step 5: Set environment variables
  - Step 6: Review and confirm configuration
  
  Example usage:
  ```bash
  claude mcp add
  ```
  
  The wizard guides you through each configuration step with helpful prompts and allows you to navigate back to previous steps if needed.

#### Project Onboarding Tracking
- Added `hasCompletedProjectOnboarding` flag to track whether users have completed the project-specific onboarding process
- Automatically marks project onboarding as complete after first use


### Bug Fixes
- Fixed issues with PersistentShell functionality
- Improved error handling for MCP server configuration


### Internal Improvements
- Added HTTP client dependencies for improved networking capabilities:
  - Added `delayed-stream` and `combined-stream` modules for streaming support
  - Integrated `form-data` library for multipart form handling
  - Added axios HTTP client with full feature support including interceptors and request/response transformations
- Updated MIME type database with extensive application type definitions
- Enhanced configuration storage with new `allowedTools` property in project settings


### Technical Changes
- Removed unused command processing function `fY9` 
- Removed redundant process and stream imports
- Removed hardcoded git command allowlist (`R_9`)
- Added comprehensive HTTP request handling infrastructure with retry logic and error handling
