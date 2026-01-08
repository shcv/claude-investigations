# Changelog for version 1.0.27

# Claude Code v1.0.27 Changelog

### Working Directory Management Improvements
- **Enhanced directory addition feedback**: The `/add-dir` command now provides more detailed and specific error messages when adding working directories
  - Clear message when no path is provided: "Please provide a directory path."
  - Specific error when path doesn't exist: "Path **[path]** was not found."
  - Helpful suggestion for non-directory paths: "**[path]** is not a directory. Did you mean to add the parent directory **[parent]**?"
  - Informative message for already accessible directories: "**[path]** is already accessible within the existing working directory **[existing]**."
  - Success confirmation: "Added **[path]** as a working directory."

### Configuration Support
- **Additional directories from configuration**: Claude Code now reads additional working directories from the configuration file
  - Directories specified in `permissions.additionalDirectories` are automatically added at startup
  - These are processed alongside command-line `--add-dir` arguments

### Terminal Title Generation
- **Fixed unnecessary API calls**: Terminal title generation now skips processing for local command output (messages starting with `<local-command-stdout>`)
- **Disabled prompt caching**: Changed `enablePromptCaching` from `true` to `false` for terminal title requests to improve performance

### Import Reorganization
- Replaced direct `stream` import with `PassThrough` from `stream`
- Changed from `node:process` import to specific `cwd` import from `node:process`
- Removed unused `path.resolve` import

### Code Refactoring
- Refactored directory addition logic to use a result-based pattern instead of direct success/message returns
- Improved error handling and message formatting for directory operations
- Better separation of concerns between directory validation and permission context updates

### Adding Working Directories
```bash
# Add a directory to the working set
claude --add-dir /path/to/project

# Multiple directories can be added
claude --add-dir /project1 --add-dir /project2

# Directories from config are automatically included
# In your config file:
# permissions:
# additionalDirectories:
# - /home/user/projects
# - /opt/shared/code
```

### Error Handling Examples
```bash
# Missing path
claude --add-dir
# Output: Please provide a directory path.

# Non-existent path
claude --add-dir /fake/path
# Output: Path /fake/path was not found.

# File instead of directory
claude --add-dir /etc/passwd
# Output: /etc/passwd is not a directory. Did you mean to add the parent directory /etc?

# Already accessible directory
claude --add-dir /home/user/project/src  # (when /home/user/project is already added)
# Output: /home/user/project/src is already accessible within the existing working directory /home/user/project.
```
