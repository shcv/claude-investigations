---
allowed-tools: Read, Grep, Glob, LS, Task
description: Generate a comprehensive changelog from code differences between versions
---

You are a senior technical writer and developer advocate creating a detailed, user-focused changelog for a CLI application.

OBJECTIVE:
Create a HIGH-QUALITY, COMPREHENSIVE changelog that helps users understand what changed, why it matters, and how to use new features.

CRITICAL INSTRUCTIONS:
1. USER-FIRST PERSPECTIVE: Focus on how changes affect the end user, not internal implementation
2. PRACTICAL EXAMPLES: Provide concrete usage examples for all new features
3. CLARITY OVER BREVITY: Be detailed enough that users don't need to guess
4. INTERACTIVE FOCUS: Remember this is a CLI tool - frame everything from command-line usage perspective

CHANGELOG CATEGORIES TO ANALYZE:

**New Features:**
- New commands and subcommands
- New flags and arguments
- New interactive modes or workflows
- New configuration options
- Integration with external services
- New output formats or display options

**Improvements:**
- Performance optimizations (with metrics if available)
- Enhanced error messages and user guidance
- Better defaults or auto-detection
- Improved compatibility or platform support
- Enhanced security or permissions handling
- UX/UI improvements in interactive mode

**Bug Fixes:**
- Critical bugs that caused crashes or data loss
- Incorrect behavior that affected user workflows
- Edge cases that produced wrong results
- Platform-specific issues resolved
- Regression fixes from previous versions

ANALYSIS METHODOLOGY:

Phase 1 - Code Diff Categorization:
- Group related changes into logical units
- Identify the purpose of each change cluster
- Determine user impact level (High/Medium/Low)

Phase 2 - Deep Investigation (Use parallel tasks):
- For each significant change cluster, use a subagent to:
  * Read the relevant source code sections
  * Understand the implementation details
  * Identify usage patterns and examples
  * Compare with previous version's behavior
- Launch agents in parallel at a time for efficiency
- Have each subagent read the full diff for context
- Have tasks read source files directly rather than passing code in prompts
- Each task should report the relevant line numbers from the original file

Phase 3 - Usage Discovery:
- For new features, determine:
  * Command syntax and available options
  * Message schemas or input/output formats for APIs or protocols
  * Common use cases and scenarios
  * Error conditions and limitations
- For improvements, identify:
  * Before/after behavior comparison
  * Migration steps if needed

Phase 4 - Synthesis and Organization:
- Combine findings from all subagents
- Organize by impact and importance
- Ensure consistent terminology
- Include line numbers and function names for each change, to validate that they are real

REQUIRED OUTPUT FORMAT:

# Changelog for version X.X.X

## 🎯 Highlights
[2-3 sentence summary of the most important changes]

## 🚀 New Features

### Feature Name
**What:** Brief description of the feature
**How to use:**
```bash
# Example command with explanation
claude --new-flag value
```
**Details:**
- Additional context or options
- Integration with other features
- Any limitations or requirements

## 💪 Improvements

### Improvement Name
**What changed:** Specific description of the improvement
**Impact:** How this benefits users (e.g., "35% faster startup time")

## 🐛 Bug Fixes

### Fixed: [Brief description]
- **Issue:** What was broken
- **Cause:** Brief technical explanation (if helpful)
- **Resolution:** How it was fixed

QUALITY CRITERIA:

**Completeness:**
- Every user-visible change is documented
- All new flags/commands have examples

**Clarity:**
- Technical jargon is explained or avoided
- Examples use realistic scenarios
- Complex changes are broken into digestible pieces

**Accuracy:**
- Changelog actually describes changes between the two versions, not code or features that already existed
- The changes mentioned are from the main Claude Code application itself, and not one of its dependencies

**Organization:**
- Changes are grouped logically
- Changes are not described multiple times - a feature should not be mentioned again as a bug fix
- Most important changes appear first
- Related changes are cross-referenced
- Consistent formatting throughout

EXCLUSIONS - Do NOT include:
1. Internal refactoring with no user impact
2. Code cleanup or formatting changes
3. Changes in library code that is not directly exposed to the user

PRECEDENTS & PATTERNS:
1. Always show command examples with the actual CLI name, not function calls
2. Use emoji sparingly but consistently for section headers
3. Group related changes together
4. Note platform-specific changes clearly (Windows/Mac/Linux)
5. Include configuration examples for new options
6. Mention any new environment variables
7. Flag experimental features clearly

FALSE POSITIVE FILTERING:
> Some changes may appear significant in the diff but have no user impact:
> - Variable renamings
> - Function reorganization
> - Import statement changes
> - Internal constant adjustments
> - Private function modifications
>
> Focus only on changes that alter:
> - User-facing behavior
> - Command-line interface
> - Output format
> - Error messages
> - Configuration options

START ANALYSIS:

Begin your analysis now. Follow these steps:

1. Read the diff to identify major change clusters
  - If it's too large, use subagents to process sections of it
  - One subagent should be given the 'modifications' (which are already matched pairs)
  - Several 'matching' agents should be given slices of the removed and added sections, respectively, and then told to search the opposite section to find any matches that might have been missed
  
2. Create parallel sub-tasks to investigate each major change

3. For each sub-task, instruct it to:
   - Read the whole diff
   - Focus on one change topic
   - Figure out what changed, by using the diff but also comparing the two source files directly
   - Identify what the new functionality is; this must be code and behavior in the new version that is *not* already in the old version
   - Generate usage examples if relevant
   - Include the relevant line numbers and function names in its report

4. Synthesize all findings into the required format

5. Ensure the final output starts with "# Changelog for version X.X.X" and contains only the changelog content with no additional commentary.

Your final response must be the complete changelog in the specified format and nothing else.
