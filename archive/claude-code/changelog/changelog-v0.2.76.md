# Changelog for version 0.2.76

# Claude Code v0.2.76 Changelog

### Enhanced Configuration Management
The `claude config` command has been significantly improved with a full suite of subcommands for managing both project-level and global configurations:

- **`claude config get <key>`** - Retrieve a specific configuration value
  ```bash
  # Get a project-level config value
  claude config get apiKey
  
  # Get a global config value
  claude config get -g theme
  ```

- **`claude config set <key> <value>`** - Set a configuration value
  ```bash
  # Set project-level configuration
  claude config set apiKey "sk-ant-..."
  
  # Set global theme configuration
  claude config set -g theme dark
  ```

- **`claude config list`** (alias: `ls`) - Display all configuration values
  ```bash
  # List project configurations
  claude config list
  
  # List global configurations
  claude config list -g
  ```

- **`claude config add <key> <values...>`** - Add items to array-type configurations
  ```bash
  # Add multiple values to an array config
  claude config add allowedDomains example.com api.example.com
  
  # Add to global array config
  claude config add -g trustedSources github.com gitlab.com
  ```

- **`claude config remove <key> [values...]`** (alias: `rm`) - Remove configuration values or specific items from arrays
  ```bash
  # Remove an entire config key
  claude config remove apiKey
  
  # Remove specific values from an array
  claude config remove allowedDomains example.com
  
  # Remove from global config
  claude config remove -g theme
  ```

All configuration commands support the `-g, --global` flag to operate on global settings instead of project-specific ones.

### MCP Server Integration
New Model Context Protocol (MCP) support has been added:

- **`claude mcp serve`** - Start the Claude Code MCP server for enhanced integrations
  ```bash
  claude mcp serve
  ```

### Theme Configuration Support
The configuration system now explicitly supports theme customization, with dark theme available as a configuration option.

### Array Configuration Management
Configuration values can now be arrays, with dedicated `add` and `remove` commands for managing list-based settings. This enables more flexible configuration of features like allowed domains, trusted sources, or custom command lists.

### Code Structure Updates
- Removed 86 functions and added 477 new functions, indicating significant internal refactoring
- Overall structural similarity of 92.9% maintained with the previous version
- Enhanced modularization with 6,705 total declarations (up from 6,314)

### Removed Dependencies
Several file system and process-related imports have been consolidated or removed, suggesting improved code organization and reduced redundancy.

## Notes

- The configuration system maintains separate project-level and global settings
- Project configurations take precedence over global configurations when both exist
- The new array configuration support enables more complex configuration scenarios
- MCP server integration opens possibilities for extended tool capabilities and integrations
