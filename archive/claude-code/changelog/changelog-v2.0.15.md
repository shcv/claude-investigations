# Changelog for version 2.0.15

## Highlights

Version 2.0.15 introduces a new **AskUserQuestion** tool that allows Claude to ask multiple-choice questions during execution, enhances async hook support with stderr capture, and improves marketplace plugin error handling with structured error tracking.


### AskUserQuestion Tool
**What:** A new tool that enables Claude to ask users multiple-choice questions during task execution to gather preferences, clarify ambiguity, or make implementation decisions.

**How to use:**
```javascript
// Claude can now use this tool to ask questions like:
{
  "questions": [
    {
      "question": "Which library should we use for date formatting?",
      "header": "Library",
      "options": [
        {"label": "date-fns", "description": "Modern, modular"},
        {"label": "moment", "description": "Widely used, large"}
      ]
    }
  ]
}
```

**Details:**
- Supports 1-4 questions per tool use with 2-4 options each
- Users can always select "Other" to provide custom text input
- Set `multiSelect: true` to allow multiple answers per question
- Includes navigation UI with question progress indicators
- Questions have a header (max 12 characters) for display in the progress bar
- **Evidence:** New tool definition at `T6Q = "AskUserQuestion"` at line 404665, tool implementation at line 405857 in function `Tn1()`


### Async Hook Stderr Capture
**What:** Async hooks now capture and track stderr output separately from stdout, providing better visibility into hook errors and warnings.

**Details:**
- Hook state now includes dedicated `stderr` field initialized as empty string
- New function `$wA()` at line 72330 adds stderr to async hook process tracking
- Hook registration function `CwA()` at line 72298 initializes stderr field at line 72318
- Stderr stream is now monitored alongside stdout for background hook processes
- **Evidence:** Previously hooks only tracked `stdout`, now both `stdout` and `stderr` fields exist in hook state (line 72318)


### Marketplace Plugin Error Tracking
**What:** Plugin loading now uses structured error tracking with specific error types and detailed context, making it easier to diagnose marketplace installation issues.

**Details:**
- New error types: `path-not-found` (for missing component files) and `generic-error` (for other failures)
- Error objects include plugin name, source, path, and component type (commands/agents/skills)
- Function `AD6()` at line 223462 now accepts error array parameter and accumulates errors
- Each missing file is tracked with metadata: `{ type: "path-not-found", source, plugin, path, component }`
- Provides actionable error messages like "Check that the marketplace entry has the correct path"
- **Evidence:** v2.0.14 function `zV6()` at line 222943 only logged warnings; v2.0.15 function `AD6()` pushes structured error objects (lines 223537-543, 223567-573, 223593-599)


### Original Working Directory Protection
**What:** File scanning now automatically excludes the original working directory when the process has changed directories, preventing unintended file access.

**Details:**
- Function `H7B()` at line 275861 checks if current directory differs from startup directory
- If different, adds `originalCwd` to ignore paths list (lines 275873-276)
- Prevents Claude Code from scanning the launch directory when operating in a different location
- **Evidence:** v2.0.14 function `s3B()` at line 275176 had static ignore list; v2.0.15 adds dynamic `originalCwd` logic


### Write Tool File Caching
**What:** The conversation context file cache now tracks Write tool results in addition to Read tool results, improving context awareness.

**Details:**
- Function `HMQ()` at line 460001 now accepts file paths from both Read and Write tools
- Caches file content from Write operations with timestamps
- Helps maintain accurate file state tracking across tool uses
- Path normalization now works for both read and write operations
- **Evidence:** v2.0.14 function `yLQ()` at line 458431 only tracked Read tool (check at line 458451); v2.0.15 tracks both Read and Write tools (Write check added at lines 460014-460020)


### Improved Marketplace Status Messages
**What:** Git operations during marketplace installation/update now show clearer progress messages.

**Details:**
- "Updating existing marketplace cache…" instead of "Running: git pull"
- "Update failed, cleaning up and re-cloning…" for clearer failure messaging  
- "Cloning repository: [url]" instead of "Running: git clone [url]"
- "Clone complete, validating marketplace…" confirms successful completion
- **Evidence:** Function `Df1()` at line 222621 uses `QT()` helper with improved messages (lines 222636, 222650, 222651)


### Select Component Enhancements
**What:** The interactive select component now supports inline text input fields as options, enabling mixed multiple-choice and text input in a single selection UI.

**Details:**
- New "input" option type alongside existing "text" options
- Options can have `type: "input"` with `placeholder` and `initialValue` properties
- New `compact-vertical` layout mode for better description display
- Component `F01` at line 145146 renders input fields with focus state management
- Multi-select component `_GB` at line 282823 supports input options with checkboxes
- **Evidence:** Function `TA()` at line 145236 now handles `type: "input"` options (checks at lines 145558, 145643, 145723)


### Command Flag Obfuscation Detection
**What:** Fixed quote handling in command security checks to properly detect obfuscated flags with escaped characters.

**Details:**
- Function `Ck6()` at line 274379 now tracks quote state and escape sequences
- Added escape sequence tracking with `Y` flag (lines 274396-274402)
- Properly handles single quotes (`'`) and double quotes (`"`) separately (lines 274403-274410)
- Checks `fullyUnquotedContent` instead of `originalCommand` for better accuracy (line 274433)
- Prevents false positives from legitimate quoted strings in command arguments
- **Evidence:** v2.0.14 function `y_6()` at line 273725 had simpler quote detection; v2.0.15 adds stateful quote and escape tracking (lines 274389-274411)


### Hook Function Signature Improvements  
**What:** Hook execution functions now use clearer parameter naming with object destructuring for better code maintainability.

**Details:**
- Function `tX9()` at line 73192 uses named parameters: `{ toolUseID, hook, hookInput, signal }`
- Function `r40()` at line 72973 uses named parameters: `{ hookInput, matchQuery, signal, timeoutMs }`
- Replaces positional parameters with descriptive object properties
- **Evidence:** v2.0.14 used positional parameters `HX9(A, B, Q, Z)` at line 73080 and `S40(A, B, Q, Z)` at line 72895


### Permission UI Component Refactoring
**What:** Tool permission confirmation component optimized with React hooks for better performance.

**Details:**
- Function `Uu()` at line 387386 now uses `useMemo` for telemetry data (line 387407)
- Uses custom hook `JE()` for permission tracking
- Replaces direct function call `Aq()` with memoized approach
- **Evidence:** v2.0.14 function `Yu()` at line 386492 called `Aq()` directly; v2.0.15 memoizes with `useMemo`
