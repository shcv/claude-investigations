# Changelog for version 0.2.81

# Claude Code v0.2.81 Changelog

## Model Pricing System Overhaul

### New Dynamic Pricing Calculation
- **Added pricing configuration system** that maps model names to token costs
- **New `Fi1` function** calculates total costs based on input/output tokens and prompt cache usage
- Pricing structure includes:
  - Input tokens
  - Output tokens
  - Prompt cache write tokens
  - Prompt cache read tokens

### Model Name Extraction
- **New `Kg` function** extracts model identifiers from strings using pattern matching
- Recognizes Claude model naming format: `claude-X-Y-name`

## Extension Management Updates

### VSCode Extension Renamed
- Extension filename changed from `mcp.vsix` to `claude-code.vsix`
- Added new extension identifier: `anthropic.claude-code`

### Installation Function Enhancement
- **Replaced `wo6` with `Fo6`** for extension installation
- Added `tm1` callback function (currently a no-op placeholder)
- Installation now calls `tm1` after successful extension install for each terminal type

### Example Usage
When installing the Claude Code extension in VSCode:
```bash
# Previously would install:
code --install-extension /path/to/vendor/mcp.vsix

# Now installs:
code --install-extension /path/to/vendor/claude-code.vsix
```

## Code Cleanup

### Removed Constants
- Removed hardcoded pricing values (`fR2`, `e53`, `G63`, `I63`, `W63`, `vR2`, `R63`)
- Removed unused model identifier `MN9` (claude-3-7-sonnet-20250219)
- Removed safety supervisor message constant `Zi1`
- Removed unused numeric constant `yi1`

### Import Optimizations
- Consolidated stream imports to use named imports from "stream" module
- Replaced direct process import with named import from "node:process"

## Technical Improvements

### New Variables
- `LS2`: Added to track array length (appears to be `pn1.length`)
- `sm1`: Extension identifier string "anthropic.claude-code"

### Stream Handling
- Changed from default import to named import `PassThrough as xm9`
- Better aligned with Node.js module best practices

This update focuses on making the pricing system more flexible and maintainable while updating the extension management system to use the new Claude Code branding.
