# Changelog for version 1.0.126

## 🎯 Highlights
Internal code optimizations to improve module loading efficiency. No user-facing changes or new features in this release.

## Internal Improvements

### Module Import Optimization
Refined Node.js module imports to be more specific, importing only the required functions rather than entire modules. This change reduces memory footprint and improves load times.

**Technical details:**
- Changed from `import AKQ from "stream"` to `import { PassThrough as ht5 } from "stream"` at line 445281
- Changed from `import i9Q from "node:process"` to `import { cwd as y7A } from "node:process"` at line 357186

These optimizations have no impact on CLI behavior or available features—they simply make the code more efficient internally.
