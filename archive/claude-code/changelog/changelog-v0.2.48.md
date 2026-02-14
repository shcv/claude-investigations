# Changelog for version 0.2.48

# Claude Code v0.2.48 Changelog

## Import Changes

This release contains minor internal refactoring of module imports with no user-facing changes:


### Refactored Imports
- **Stream module**: Changed from default import to named import
  - Before: `import PE4 from "stream"`
  - After: `import { Readable as $E4 } from "stream"`
  
- **Process module**: Changed from default import to named import
  - Before: `import Vc2 from "node:process"`
  - After: `import { cwd as yw0 } from "node:process"`


### Technical Details
- Structural similarity: 100%
- Total changes: 2 additions, 2 deletions
- 122 internal renames (no functional impact)

## Summary

Version 0.2.48 is a maintenance release focused on internal code organization. The changes involve switching from default imports to named imports for Node.js built-in modules, which is a best practice for better tree-shaking and clearer code intentions. These changes do not affect any user-facing functionality, CLI arguments, or interactive features.
