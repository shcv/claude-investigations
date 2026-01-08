# Changelog for version 0.2.31

### New Features

#### Custom Slash Commands
Users can now create custom slash commands by placing Markdown files in `.claude/commands/` directories. These files will automatically appear as slash commands that insert prompts into your conversation.

**Usage Example:**
```bash
# Create a custom command file
mkdir -p .claude/commands/
echo "# My Custom Prompt\nThis is my custom prompt content" > .claude/commands/my-command.md

# In Claude Code, use the command
/my-command
# This will insert the contents of my-command.md into your conversation
```

This feature allows you to create reusable prompts and workflows specific to your project or personal preferences.

#### MCP Debug Mode
A new `--mcp-debug` flag provides detailed error information when MCP (Model Context Protocol) servers encounter issues.

**Usage Example:**
```bash
# Run Claude Code with MCP debugging enabled
claude --mcp-debug

# When MCP server errors occur, you'll see detailed error messages like:
# MCP server "server-name" Error details here
```

This helps troubleshoot MCP server configuration and connectivity issues.

### Internal Improvements

- **Enhanced Error Logging**: MCP server errors are now logged with better formatting and optionally displayed to console when debug mode is enabled
- **Version Update**: Updated to version 0.2.31
- **Sentry Environment**: Error tracking now includes environment tag set to "external"

### Technical Changes

- Improved error handling in the MCP tool execution flow with better error reporting
- Reorganized import statements for Node.js process and stream modules
- Added user/project scope variables for command organization
