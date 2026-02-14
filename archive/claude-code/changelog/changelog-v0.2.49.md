# Changelog for version 0.2.49

# Claude Code v0.2.49 Changelog

## MCP Server Scope Terminology Update

The primary change in this version is a renaming of MCP (Model Context Protocol) server scopes to improve clarity:


### Scope Renaming
- **"project" → "local"**: MCP servers that are specific to the current project are now called "local" servers
- **"global" → "user"**: MCP servers available across all projects are now called "user" servers


### What This Means for Users

When managing MCP servers, you'll now see updated terminology:
- **Local servers** (formerly "project"): Private to you in the current project
- **User servers** (formerly "global"): Available in all your projects
- **Project servers**: Shared via .mcp.json (terminology unchanged)


### Examples

When using MCP-related commands, the scope names have changed:

```bash
# Adding an MCP server with the new scope names
claude mcp add --scope local    # Adds to current project only
claude mcp add --scope user     # Adds to all your projects

# The allowed scopes list now shows:
# ["local", "user"] instead of ["user", "global"]
```


### Technical Details

The update includes:
- Updated display strings in the `vj` function that formats scope names for user display
- The `DO5` variable (allowed scopes list) now contains `["local", "user"]` instead of `["user", "global"]`
- Import optimizations for stream handling modules

This is a terminology-only change that makes the scope names more intuitive - no functionality has been altered.
