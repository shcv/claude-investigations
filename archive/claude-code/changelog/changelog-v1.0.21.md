# Changelog for version 1.0.21

Based on my analysis of the diff file, here is the changelog for Claude Code version 1.0.21:

### New Features

#### MCP Prompts Support
- Added support for MCP (Model Context Protocol) prompts functionality
- New methods available for MCP servers:
  - `prompts/get` - Retrieve a specific prompt by name with optional arguments
  - `prompts/list` - List all available prompts from an MCP server
- Added prompt list change notifications support via `notifications/prompts/list_changed`

### Improvements

#### Enhanced OAuth/Authentication Flow
- Improved OAuth client information handling during authorization flows
- Better support for dynamic OAuth client registration
- Enhanced client metadata persistence when exchanging authorization codes
- More robust handling of OAuth redirect URLs with proper client ID parameters

#### Error Handling Enhancements
- Added validation for server capability requirements:
  - Prompts support verification for MCP servers
  - Proper error messages when servers don't support required features
  - Better error reporting for incompatible authentication servers
- Improved validation for OAuth response types and code challenge methods

### Technical Improvements

- Enhanced session ID handling in connection establishment
- Better support for client information persistence across OAuth flows
- Improved error state tracking with optional `isError` flag

### MCP Integration Examples

When connecting to an MCP server that supports prompts, you can now:

```bash
# List all available prompts from a connected MCP server
claude code mcp list-prompts

# Get a specific prompt with arguments
claude code mcp get-prompt "code-review" --args '{"language": "javascript"}'
```

This version focuses on expanding MCP capabilities and improving the robustness of OAuth authentication flows, making it easier to integrate with various MCP servers and maintain secure connections.
