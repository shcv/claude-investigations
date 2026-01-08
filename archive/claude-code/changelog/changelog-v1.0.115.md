# Changelog for version 1.0.115

## Highlights
This release adds rainbow color support to the color theme system and improves thinking detection toggle behavior to be more predictable and user-controlled.

### Rainbow Color Palette
**What:** Added a complete rainbow color palette to all theme variants (light, dark, and custom themes)

**Details:**
- Seven new rainbow colors: red, orange, yellow, green, blue, indigo, violet
- Each color includes both normal and shimmer variants for animated effects
- Colors added to theme objects: `gq9` at line 360299, `uq9` at line 360354, `hq9` at line 360244, `dq9` at line 360464, `mq9` at line 360409, `cq9` at line 360519
- Example color values:
  - `rainbow_red`: "rgb(235,95,87)"
  - `rainbow_orange`: "rgb(245,139,87)"
  - `rainbow_yellow`: "rgb(250,195,95)"
  - And corresponding shimmer variants for each

### Rainbow Color Arrays and Helper Functions
**What:** New infrastructure for cycling through rainbow colors

**How to use:**
The system now includes:
- `Cj9` array at line 365972: Contains the seven rainbow color names for cycling
- `Uj9` array at line 365981: Contains the seven rainbow shimmer color names
- `m61()` function at line 365993: Cycles through rainbow colors by index
- `Ew1()` function at line 365990: Checks if a string matches "ultrathink" (case-insensitive)

**Details:**
- The `m61(index, useShimmer)` function takes an index and optional shimmer flag, returning the appropriate rainbow color name
- Uses modulo arithmetic to cycle through colors: `Q[A % Q.length]`
- **Evidence**: `m61() at line 365993`, `Ew1() at line 365990`, `Cj9 at line 365972`, `Uj9 at line 365981`

### Thinking Detection Toggle Behavior
**What:** Improved how the thinking detection disabled state works when users toggle it on/off

**Details:**
- Removed automatic re-enabling of thinking when users clear thinking tokens from input (previously in `useEffect` at line 437586-437588 in v1.0.114)
- Introduced computed "effective disabled" state (`i1` at line 437849) that only treats thinking as disabled when both:
  1. User has disabled thinking, AND
  2. Thinking tokens are present in the input
- Visual feedback (border colors, shimmer effects) now shows thinking detection state more accurately
- User preference for disabled thinking now persists instead of being automatically reset
- **Evidence**: `i1 variable at line 437849 in Yp5()`, removed `useEffect` from previous version

### Code Organization
**What:** Refactored imports for better tree-shaking and bundle optimization

**Details:**
- Changed `node:process` import from default to named import for `cwd()` function
- Import structure: `import { cwd as TNA } from "node:process"` at line 361351
- Import structure: `import { PassThrough as xi5 } from "stream"` at line 442117
- No functional changes, just more efficient bundling
- **Evidence**: `import { cwd as TNA } at line 361351`, `import { PassThrough as xi5 } at line 442117`
