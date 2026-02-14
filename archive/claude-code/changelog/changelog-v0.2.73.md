# Changelog for version 0.2.73

# Claude Code v0.2.73 Changelog


### Theme Command Alias
The `/config` command now has a `/theme` alias, providing quick access to theme settings directly:
```bash
# Both commands now open the config panel
/config
/theme
```


### Improved Theme Descriptions
Theme options in the config panel now display clearer, more user-friendly descriptions:
- **Light mode** - Previously "Dark text"
- **Dark mode** - Previously "Light text"  
- **Light mode (colorblind-friendly)** - Previously "Dark text (colorblind-friendly)"
- **Dark mode (colorblind-friendly)** - Previously "Light text (colorblind-friendly)"
- **Light mode (ANSI colors only)** - Previously "Dark text (ANSI colors only)"
- **Dark mode (ANSI colors only)** - Previously "Light text (ANSI colors only)"


### IDE Extension Detection
Claude Code now detects if you have the Anthropic MCP extension installed in supported IDEs (VS Code, Cursor, Windsurf). When detected, a status indicator appears showing:
```
✓ Found [IDE name] extension • /config
```


### TodoRead Tool Enhancement
The `TodoRead` tool now has clearer usage instructions, explicitly stating that no parameters should be provided:
```
Usage:
- This tool takes in no parameters. So leave the input blank or empty. 
  DO NOT include a dummy object, placeholder string or a key like "input" or "empty". 
  LEAVE IT BLANK.
```


### Better Pipe Handling in Bash Commands
Improved handling of piped commands in bash shells. The system now properly redirects stdin only for the first command in a pipeline, preventing issues with commands like:
```bash
# This now works correctly
echo "test" | grep "test" | wc -l
```


### Custom Shell Support
Added support for specifying custom shells when executing bash commands, providing more flexibility for users with non-standard shell configurations.

## Technical Changes

- Refactored extension detection to use synchronous execution with proper error handling
- Improved bash command parsing for better pipe detection
- Updated import statements for better module organization
- Enhanced shell command execution with custom shell parameter support

## Bug Fixes

- Fixed potential issues with stdin redirection in piped commands
- Improved error handling for IDE extension detection
- Better handling of edge cases in shell command execution
