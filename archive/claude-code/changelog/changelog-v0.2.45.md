# Changelog for version 0.2.45

# Claude Code v0.2.45 Changelog

## New Features

### Environment Variable Support for API Customization
Claude Code now supports a new environment variable `CLAUDE_CODE_EXTRA_BODY` that allows users to inject additional parameters into API requests.

**Usage:**
```bash
# Set custom API parameters as a JSON object
export CLAUDE_CODE_EXTRA_BODY='{"temperature": 0.8, "max_tokens": 4000}'
claude "Your prompt here"
```

This feature enables:
- Customization of API request parameters without modifying code
- Fine-tuning of Claude's response behavior (temperature, max tokens, etc.)
- Advanced users to experiment with API options

**Error Handling:**
- The value must be a valid JSON object (not an array or primitive)
- Invalid JSON will be logged to stderr and ignored
- Parsing errors are gracefully handled with descriptive error messages

## Internal Changes

### Import Optimizations
- Switched from default imports to named imports for better tree-shaking:
  - `stream` module now uses `import { Readable as o$4 }`
  - `node:process` module now uses `import { cwd as zw0 }`
- These changes may result in slightly smaller bundle sizes and improved load times

## Technical Details

The new `O41()` function handles the environment variable parsing:
```javascript
function O41() {
  let I = process.env.CLAUDE_CODE_EXTRA_BODY;
  if (!I) return {};
  try {
    let G = wO(I); // JSON parse wrapper
    if (G && typeof G === "object" && !Array.isArray(G)) return G;
    return (console.error("CLAUDE_CODE_EXTRA_BODY must be a JSON object"), {});
  } catch (G) {
    return (
      console.error(
        `Error parsing CLAUDE_CODE_EXTRA_BODY: ${G instanceof Error ? G.message : String(G)}`,
      ),
      {}
    );
  }
}
```

This function is likely called during API request construction to merge custom parameters with default request bodies.
