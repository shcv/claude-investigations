# Changelog for version 0.2.35

# Claude Code v0.2.35 Changelog

## Import Optimizations

This version includes minor optimizations to module imports, focusing on more specific imports from Node.js built-in modules:

### Stream Module Changes
- **Optimized `stream` imports**: Instead of importing entire modules, the code now imports only the specific classes needed:
  - Changed from `import vR4 from "stream"` to `import { Readable as qR4 } from "stream"`
  - Changed from `import e20 from "node:stream"` to `import { PassThrough as so1 } from "node:stream"`

### Process Module Changes
- **Optimized `process` imports**: Similar optimization for the process module:
  - Changed from `import gb2 from "node:process"` to `import { cwd as q00 } from "node:process"`

## Technical Details

These changes represent a move towards more efficient imports by using destructured imports rather than default imports. This can lead to:
- Smaller bundle sizes through better tree-shaking
- Clearer code intent by explicitly naming the imported functionality
- Potential performance improvements by avoiding unnecessary module loading

## Impact on Users

These are internal implementation changes with no impact on CLI functionality or user-facing features. All commands and interactions remain unchanged.
