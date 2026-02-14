# Changelog for version 0.2.92

# Claude Code v0.2.92 Changelog


### OAuth Token Revocation Handling
- Added proper error handling for revoked OAuth tokens
- When an OAuth token is revoked, users will now see the message: "OAuth token revoked · Please run /login"
- This provides clearer guidance on how to resolve authentication issues


### Git Repository Detection
- Added two new helper functions for Git repository detection:
  - **Repository check**: Determines if the current directory is inside a Git repository
  - **Repository root**: Finds the root directory of the current Git repository
- These functions improve Git-related operations by providing better context awareness


### Local Claude Configuration Support
- Added support for `CLAUDE.local.md` files
- This allows for project-specific Claude configuration that overrides global settings
- The system can now generate and write local configuration files when needed


### Command Execution Enhancement
- Modified the command execution function to accept an optional working directory parameter
- Previously, the working directory was always set to the current directory
- Now supports executing commands in specific directories, improving flexibility for Git operations and other directory-specific commands


### Import Reorganization
- Streamlined imports by consolidating Node.js process and stream imports
- Added proper path utilities import for file path operations
- This improves code organization and reduces redundancy


### Error Handling
- Enhanced error handling to specifically catch OAuth token revocation (403 status)
- Previously, OAuth errors might have been handled generically
- Now provides specific, actionable error messages for authentication issues


### Handling OAuth Token Revocation
When your OAuth token is revoked, you'll see:
```
OAuth token revoked · Please run /login
```
Simply run the login command to re-authenticate:
```bash
claude login
```


### Working with Git Repositories
The new Git detection features work automatically in the background, but they enable Claude to:
- Better understand when you're working in a Git repository
- Find the repository root for operations that need it
- Provide more context-aware Git-related suggestions


### Local Configuration
If you need project-specific Claude settings, a `CLAUDE.local.md` file can now be created in your project directory. This file will override global Claude settings for that specific project.
