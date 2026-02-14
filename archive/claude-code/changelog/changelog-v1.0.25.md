# Changelog for version 1.0.25

# Claude Code v1.0.25 Changelog


### Enhanced Terminal Support
- **Improved Ghostty terminal compatibility**: Added specific spinner character set for Ghostty terminal (`TERM=xterm-ghostty`), providing better visual feedback during operations


### Workspace Permissions Tab
- **New "Workspace" permissions tab**: Added alongside the existing "Allow" and "Deny" tabs in the permissions interface
  - Allows users to manage which directories Claude can access
  - Provides granular control over file system access permissions
  - Navigate between tabs using Tab or arrow keys


### ️ Directory Management in Permissions
- **Add directories to workspace**: New interactive flow to add directories that Claude can read and edit
  - Access via the Workspace tab in permissions
  - Enter directory paths interactively
  - Clear feedback when directories are added or removed
  
- **Remove directories from workspace**: Easily remove previously added directories
  - Visual confirmation dialog before removal
  - Shows which directory will be removed from Claude's access


### ️ Improved PATH Configuration
- **Better PATH setup for ~/.local/bin**: Enhanced the installation process to properly configure PATH
  - Detects if ~/.local/bin is already in PATH
  - Handles cases where PATH is configured but not loaded in current shell
  - Removes old `alias claude` entries automatically
  - Provides clearer instructions for shell configuration
  - Example output: "Added ~/.local/bin to PATH in ~/.zshrc. You may need to restart your shell or run: source ~/.zshrc"


### Custom Command Enhancements
- **Frontmatter parsing**: Custom commands now support YAML-style frontmatter in markdown files
  ```markdown
  title: My Command
  description: Does something useful
  
  Command content here...
  ```

- **Inline bash execution**: Execute bash commands directly within custom command markdown
  - Block syntax: ` ```!echo "Hello from command"``` `
  - Inline syntax: `` !`date` ``
  - Commands are validated and executed with proper permissions
  - Output is inserted directly into the rendered content


### Better Output Formatting
- **Improved line wrapping**: Long lines in output are now properly wrapped at terminal width boundaries
- **Enhanced truncation display**: When output is truncated, shows more accurate line counts


### Terminal Reset
- Fixed incomplete terminal reset sequence by adding proper termination (`\x1B[0m\x1B(B`)


### Version Parsing
- Added robust version string parsing to handle edge cases in version comparisons


### ️ Code Organization
- Modularized color inversion logic for better theme support
- Improved git repository root detection with fallback mechanisms
- Enhanced custom command discovery to check both global and project-local directories


### Analytics
- Added "command" to tracked context types for better usage insights


### Managing Workspace Directories
```bash
# In Claude Code, navigate to permissions
# Select the "Workspace" tab
# Choose "Add directory..."
# Enter: /home/user/my-project
# Claude can now read and edit files in that directory
```


### Using Custom Commands with Bash Execution
Create a custom command file with inline bash:
```markdown
title: System Info
description: Shows current system information

Current user: !`whoami`
Current directory: !`pwd`

System details:
```!
uname -a
df -h
```
```

The bash commands will execute when the custom command is invoked, with output inserted into the response.
