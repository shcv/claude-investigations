# Changelog for version 0.2.120


### Tool Permission Handling Improvements

#### Enhanced CLI Tool Filtering
The permission system for CLI tools has been improved with better parsing of allowed and disallowed tool arguments:

- **New comma-separated tool parsing**: The `--allowed-tools` and `--disallowed-tools` CLI arguments now support comma-separated values for specifying multiple tools in a single argument
  
  Example usage:
  ```bash
  # Allow multiple tools with comma separation
  claude-code --allowed-tools "Read,Write,Edit" 
  
  # Disallow specific tools
  claude-code --disallowed-tools "Bash,WebSearch"
  
  # Can still use multiple arguments
  claude-code --allowed-tools Read --allowed-tools Write
  ```

- **Improved tool name parsing**: Tool names are now properly trimmed of whitespace and empty values are filtered out, making the tool specification more robust


### Internal Changes

#### Async MCP Client Discovery
- Converted the MCP (Model Context Protocol) client discovery function from a wrapped promise to a native async function, improving code clarity and maintainability

#### Stream Import Optimization  
- Consolidated stream imports: Removed redundant `stream` import and instead imports `PassThrough` directly from the stream module when needed

#### Process Import Cleanup
- Simplified process imports by importing `cwd` directly from `node:process` instead of importing the entire process module


### Technical Details

The main changes revolve around the `tR5` function (previously `Sy0`) which handles tool permissions:

```javascript
// New implementation with tool name parsing
function tR5({ allowedToolsCli, disallowedToolsCli, permissionMode }) {
  let parsedAllowed = fc1(allowedToolsCli),    // Parse comma-separated values
      parsedDisallowed = fc1(disallowedToolsCli);
  return Fb0(
    {
      mode: permissionMode,
      alwaysAllowRules: { cliArg: parsedAllowed },
      alwaysDenyRules: { cliArg: parsedDisallowed },
    },
    Db0(),
  );
}
```

Where `fc1` is the new parsing function that:
1. Handles null/undefined inputs gracefully
2. Splits comma-separated values
3. Trims whitespace from each tool name
4. Filters out empty strings

This enhancement makes it easier to specify multiple tools in scripts and command-line usage without needing to repeat the flag multiple times.
