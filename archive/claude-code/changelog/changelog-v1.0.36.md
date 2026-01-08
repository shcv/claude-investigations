# Changelog for version 1.0.36

# Claude Code v1.0.36 Changelog

### Web Search Enhancement
- **Improved date awareness**: Web search now accounts for "Today's date" in the environment context, ensuring searches use current year information rather than outdated dates

### mTLS (Mutual TLS) Support
- **Enterprise-grade security**: Added comprehensive support for mutual TLS authentication
- **Environment variables** for certificate configuration:
  - `NODE_EXTRA_CA_CERTS`: Load custom CA certificates
  - `CLAUDE_CODE_CLIENT_CERT`: Specify client certificate
  - `CLAUDE_CODE_CLIENT_KEY`: Specify client private key
  - `CLAUDE_CODE_CLIENT_KEY_PASSPHRASE`: Optional passphrase for encrypted keys
- **Automatic integration**: mTLS certificates are automatically configured for both HTTP clients and proxy connections
- **Diagnostic support**: mTLS configuration is now visible in API configuration diagnostics

### Enhanced Update Command
- **Improved diagnostics**: The `claude update` command now provides detailed installation health information
- **Multiple installation detection**: Warns when multiple Claude Code installations are found
- **Configuration validation**: Automatically detects and fixes mismatches between actual installation type and configuration
- **Better error messages**: More informative warnings with specific fix instructions
- **Visual improvements**: Color-coded output (yellow for warnings, green for success, red for errors)

### Installation Health Monitoring
- **New health check system**: Detects and reports installation issues including:
  - Multiple installations
  - Permission problems for auto-updates
  - Configuration mismatches
  - Global installation update limitations

### Token Usage Tracking
- **Web search metrics**: Added `webSearchRequests` tracking to model usage statistics
- **New helper function**: `w8A()` for retrieving web search request counts

### OAuth Discovery Enhancement
- **Improved well-known endpoint discovery**: Now supports OAuth authorization server metadata at both standard and path-specific locations
- **Better error handling**: Gracefully handles 404 responses when searching for OAuth metadata

### Security Improvements
- **Enhanced directory traversal protection**: Updated `cd` command validation with clearer security messages
- **Better path validation**: Improved checking for allowed working directories

### Code Editor Integration
- **Text truncation**: Selected text from IDE is now truncated to 2000 characters to prevent overwhelming the context

## Bug Fixes

- Fixed configuration storage issue where fallback storage wasn't properly cleaned up after successful primary storage writes
- Improved resource URL validation logic to handle undefined resources correctly
- Fixed image handling in user prompts to process images before other content

## Internal Changes

- Replaced several utility functions with more efficient implementations using lodash
- Updated proxy agent initialization to support mTLS configurations
- Improved error handling in fetch operations for OAuth discovery
- Added proper TypeScript imports for Node.js stream and process modules

## Developer Notes

These changes focus on enterprise security features (mTLS support), improved installation management, and better diagnostic capabilities. The update command now provides a much more informative and user-friendly experience when checking for and installing updates.
