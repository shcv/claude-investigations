# Changelog for version 0.2.14


### New Features

#### Dynamic Terminal Detection
Claude Code now automatically detects your terminal environment using the new `BA4()` function. This provides better shell integration by recognizing:
- Popular terminals (iTerm, Alacritty, Kitty, GNOME Terminal, Windows Terminal, etc.)
- Terminal multiplexers (tmux, screen)
- SSH sessions
- WSL environments
- Non-interactive contexts

#### Enhanced Shell Support
- **Expanded shell compatibility**: Now supports multiple shell paths:
  - `/bin/bash` and `/usr/bin/bash`
  - `/bin/zsh` and `/usr/bin/zsh`
  - `/bin/sh`
- **Automatic shell discovery**: If your `SHELL` environment variable isn't set or points to an invalid shell, Claude Code will automatically find a suitable shell from the supported list
- **Better error messages**: Clear error when no suitable Unix shell environment is found

#### User Preferences Support
- **Global user configuration**: Claude Code now reads from `~/.claude/CLAUDE.md` for user-specific preferences that aren't checked into the codebase
- **Hierarchical configuration**: Combines project-specific `CLAUDE.md` files with global user preferences

#### Message of the Day (MOTD)
- New `Tp1()` component displays customizable messages from the server
- Supports color theming to match your terminal color scheme


### Improvements

#### Shell Process Management
- **Better error tracking**: The persistent shell now captures recent stdout/stderr (up to 10KB) for debugging when the shell exits unexpectedly
- **Enhanced diagnostics**: Shell exit events now include more context:
  - Working directory at time of exit
  - Queue length and execution state
  - Recent output for troubleshooting
- **Safer cleanup**: Improved error handling when cleaning up temporary files during shell exit

#### Error Reporting
- **Stack trace enhancement**: Sentry error reports now include original stack traces in a more readable format
- **Better error context**: Shell write errors now include recent stdout/stderr for debugging

#### Theme System
- **New "remember" color**: Added to all color themes for better visual distinction of remembered/saved items


### Technical Improvements

#### Code Quality
- **Type safety**: Better path resolution with new `xA9()` and `cA9()` functions for tool path validation
- **Resource management**: Improved cleanup of file descriptors and temporary files
- **Error boundaries**: More robust error handling throughout the shell execution pipeline


### Bug Fixes

- Fixed potential race conditions in shell process management
- Improved handling of shell crashes during command execution
- Better validation of file paths before operations
- More reliable shell availability checks before writing commands


### Breaking Changes

None - this release maintains backward compatibility with v0.2.9.
