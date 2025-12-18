# Changelog for version 2.0.44

## 🎯 Highlights

Version 2.0.44 introduces an experimental reasoning effort control feature that allows Claude to adjust its reasoning depth based on experiment configuration. This is gated behind a Statsig experiment flag and enables testing different trade-offs between response speed and thoroughness.

## 🚀 New Features

### Experimental Reasoning Effort Control

**What:** A new system that allows Claude to dynamically adjust how much reasoning it applies to tasks based on an experiment-controlled effort level.

**How it works:**
This feature is controlled by the Statsig experiment flag `tengu_effort_exp` with parameter `tengu_effort_level`. When enabled, it accepts three levels:
- `low` (maps to effort value 45)
- `medium` (maps to effort value 75) 
- `high` (maps to effort value 99)

**Details:**
- The feature automatically injects reasoning effort instructions into Claude's system prompt when the experiment is active
- Lower effort values prioritize faster, more efficient responses
- Higher effort values enable maximum reasoning and thoroughness
- The effort scale ranges from 0-100, with Claude instructed to vary reasoning depth accordingly
- This is an A/B test feature - only users enrolled in the Statsig experiment will have access
- **Evidence**: `function sQI() at line 470523`, `aQI mapping at line 470940`, `system prompt integration at line 470717`

**Technical implementation:**
- New function `sQI()` reads experiment configuration and generates reasoning effort instructions
- Mapping object `aQI = { low: 45, medium: 75, high: 99 }` converts string levels to numeric values
- The generated `<reasoning_effort>` XML tag is appended to the system prompt array
- Experiment values are retrieved via the Statsig client using the `d3()` helper function

## 🔧 Internal Changes

### Module System Refactoring

**What:** Significant restructuring of module initialization and dependencies

**Details:**
- The module initialization variable was renamed from `LQ` to `Pr`
- Initialization dependencies were completely reorganized with different function calls
- Usage of the initialization function was reduced from 69 call sites to 6, suggesting more efficient lazy loading or granular initialization
- Import statements were reorganized by the bundler, but no functional changes to imports were made
- **Evidence**: `variable Pr at line 470923` (previously `LQ at line 480763` in v2.0.43)
