# Changelog for version 2.0.3

## 🎯 Highlights

Version 2.0.3 contains internal code optimizations and refactoring improvements. There are no user-facing changes, new features, or bug fixes in this release.

## Internal improvements

### Rendering function optimization
The internal rendering function `BiQ()` at line 356972 was refactored to `AiQ()` at line 356971, removing unnecessary `rows` and `columns` parameters that were being passed through but not actively used by the core rendering logic. The function signature changed from accepting 4 parameters `(A, B, Q, Z)` to just 2 parameters `(A, B)`, and the return value no longer includes `rows` and `columns` fields.

**Evidence**: 
- Old: `var BiQ = (A, B, Q, Z) =>` at line 356972 in v2.0.2
- New: `var AiQ = (A, B) =>` at line 356971 in v2.0.3

### Removed unused terminal size check function
The function `p3A()` at line 358129, which compared terminal dimensions and output heights between render frames, was removed as part of simplifying the rendering pipeline.

**Evidence**: `function p3A(A, B)` at line 358129 in v2.0.2 (removed in v2.0.3)

### Import statement consolidation
Import statements were refactored to use more specific destructured imports:
- Changed from `import vKQ from "stream"` to `import { PassThrough as Xe5 } from "stream"` at line 357259
- Changed from `import _4Q from "node:process"` to `import { cwd as g3A } from "node:process"` at line 443967

**Evidence**:
- Stream import: line 338165 in v2.0.2 vs line 357259 in v2.0.3
- Process import: line 442779 in v2.0.2 vs line 443967 in v2.0.3

These changes represent internal code quality improvements with no impact on CLI functionality, performance, or user experience.
