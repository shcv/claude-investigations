# Changelog for version 0.2.18

Based on my analysis of the diff file, here's the changelog for Claude Code v0.2.18:

# Claude Code v0.2.18 Changelog

### Config Management Enhancements
- **New config array operations**: Added `config add` and `config rm` subcommands to manage configuration arrays
  - `claude config add <key> <value>` - Add an item to a config array
  - `claude config rm <key> <value>` - Remove an item from a config array
- **Alias support**: Added `ls` as an alias for `config list`

### Fish Shell Support
- Added full support for Fish shell in the persistent shell environment
- Fish shell configuration files (`.config/fish/config.fish`) are now recognized

### Image Support in Command Output
- Command output can now display images when detected (data URLs with base64 encoding)
- When image data is detected in command output, it's sent to Claude and marked as "[Image data detected and sent to Claude]"

### Project Configuration
- Added `ignorePatterns` configuration option to specify patterns for files/directories to ignore
- Improved ignore pattern handling with custom pattern support via `v_()` function

### Release Notes Display
- Simplified release notes display - now shows "What's new:" instead of version-specific headers
- Improved release notes caching and display logic using `useMemo` for better performance

### Error Handling
- Enhanced error reporting with additional context in the `Ib` function
- Better error tracking with optional extra parameters

### Shell Environment
- Fixed Fish shell syntax checking with proper flags (`--no-execute -c`)
- Improved shell command validation for Fish shell compatibility

## Technical Changes

- Updated version to 0.2.18
- Added 42 new functions/variables
- Removed 12 deprecated functions/variables
- Modified 12 existing functions with improvements
- Structural similarity with v0.2.14: 99.2%

### Managing Config Arrays
```bash
# Add a pattern to ignore list
claude config add ignorePatterns "*.tmp"

# Remove a pattern from ignore list  
claude config rm ignorePatterns "*.tmp"

# List all config values (using new alias)
claude config ls
```

### Fish Shell Integration
Fish shell users can now use Claude Code seamlessly with proper shell integration and syntax validation.
