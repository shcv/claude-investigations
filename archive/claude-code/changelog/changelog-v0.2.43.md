# Changelog for version 0.2.43

# Claude Code v0.2.43 Changelog

## Overview
This release focuses on internal optimizations and introduces a new domain checking capability for web fetching. The terminal rendering system has been significantly refactored for better performance.

### Domain Fetch Verification
A new function `tP3` has been added that checks whether a domain can be fetched before attempting web operations:

```javascript
async function tP3(domain) {
  try {
    let response = await fetch(
      `https://claude.ai/api/web/domain_info?domain=${encodeURIComponent(domain)}`
    );
    if (response.ok) return (await response.json()).can_fetch === true;
    return false;
  } catch (error) {
    return (logError(error), true);
  }
}
```

This appears to be a pre-flight check for the WebFetch tool, allowing Claude Code to verify domain accessibility before attempting to fetch content.

### Terminal Rendering Refactoring
The terminal rendering system underwent significant optimization:

1. **Removed OSC 133 Terminal Integration**: The shell integration sequences (OSC 133) that were used for marking prompts and command boundaries have been completely removed. This includes:
   - Prompt start/end markers (`\x1B]133;A\x07`, `\x1B]133;B\x07`)
   - Command markers (`\x1B]133;C\x07`, `\x1B]133;D\x07`)
   - Bracketed paste mode sequences (`\x1B[?2026h`, `\x1B[?2026l`)

2. **Simplified Render Buffer Class**: The `yy` class (now `uy`) has been streamlined:
   - Removed `startOscPrompt` and `endOscPrompt` parameters
   - Simplified constructor to only take width and height
   - More efficient output generation using map/join instead of manual string concatenation

3. **Cleaner Output Handling**: The main renderer class (`Nn` → `gn`) now:
   - No longer tracks or strips OSC sequences from output
   - Simplified terminal clearing logic
   - More direct output writing without intermediate processing

## Import Changes

- **Stream Import Modified**: Changed from default import to named import for better tree-shaking:
  ```javascript
  // Before: import b$4 from "stream";
  // After: import { Readable as v$4 } from "stream";
  ```

- **Process Import Updated**: Changed to named import:
  ```javascript
  // Before: import Hh2 from "node:process";
  // After: import { cwd as ww0 } from "node:process";
  ```

## Performance Improvements

1. **Reduced String Operations**: The removal of regex-based OSC sequence stripping (`t59` regex) eliminates unnecessary string processing on every render.

2. **Simplified Render Pipeline**: The output generation is now more direct, reducing the number of intermediate transformations.

3. **Memory Efficiency**: Removed several string constants and helper functions that were used for OSC sequence handling.

## Technical Details

- **Structural Similarity**: 99.8% - indicating this is primarily an optimization release
- **Declaration Changes**: +3 additions, -12 deletions, 3 modifications
- **Affected Components**: Terminal rendering, web fetching, import optimization

## Impact for Users

This update should be transparent to end users with the following potential improvements:
- Slightly faster terminal rendering, especially for output-heavy operations
- More reliable web fetching with pre-flight domain checks
- Reduced memory footprint due to code removal

The removal of OSC 133 sequences suggests Claude Code is moving away from shell-specific integrations in favor of a more universal approach to terminal handling.
