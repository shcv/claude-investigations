# Changelog for version 0.2.77

# Claude Code v0.2.77 Changelog


### Enhanced IDE Selection Integration
The IDE integration now supports a new **"Add to Prompt"** capability. When working with code selections from your IDE:

- **Automatic prompt insertion**: IDE selections can now be automatically added to your prompt input with the new `addToPrompt` parameter
- **Improved selection handling**: The system now distinguishes between viewing selections and actively including them in prompts

**Example usage**: When you select code in your IDE and trigger the "Add to Prompt" action, the selected code will be automatically inserted at your cursor position in the Claude Code prompt, formatted with file context.


### SSE IDE Connection Type
Added support for Server-Sent Events (SSE) based IDE connections:

```javascript
{
  type: "sse-ide",
  url: "https://your-ide-endpoint.com/sse"
}
```

This enables real-time communication with IDEs that support SSE protocols.


### File Watching and Change Detection
Claude Code now actively monitors files you've previously read and notifies you of changes:

- **Automatic change detection**: Files you've read are tracked with timestamps
- **Smart diff display**: When a watched file changes, Claude shows only the modified portions with context
- **Performance optimization**: File change checks are batched and run asynchronously

**Example**: If you read a file and later it's modified externally, Claude will show:
```
File edited: /path/to/file.js
[Shows relevant changes with line numbers]
```


### Enhanced File Context Handling
Improved how file mentions and contexts are processed:

- Files mentioned in prompts now include a `mode` field to distinguish between new file references (`mode: "new"`) and edited files (`mode: "edited"`)
- Better tracking of file states for more accurate context management


### Refined Selection Text Formatting
When IDE selections are auto-included in prompts, the formatting has been improved:

- Selections with file context: `"The current selection is in [filename]:\n[selected code]"`
- Selections without file context: `"The current selection is:\n[selected code]"`
- File-only context: `"Currently viewing [filename]"`


### Import Optimizations
- Replaced full module imports with targeted imports for better performance:
  - `import { PassThrough as nu9 } from "stream"` instead of `import rz9 from "stream"`
  - `import { cwd as _e0 } from "node:process"` instead of `import xT2 from "node:process"`


### Code Architecture
- New function `iR2` coordinates both new file extractions and file change detection
- New function `v63` specifically handles watched file change detection
- Improved separation of concerns between different file handling modes

## Bug Fixes

- Fixed potential issues with file state management by using more specific property names (`readFileState` instead of `readFileTimestamps`)
- Improved error handling for file stat operations when checking for changes

## Breaking Changes

None - This version maintains backward compatibility with existing workflows.
