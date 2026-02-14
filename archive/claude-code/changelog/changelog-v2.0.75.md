# Changelog for version 2.0.75


## Summary

This is a maintenance release with a minor prompt optimization. The primary change removes a redundant instruction from subagent prompts that was already present in the main system prompt, reducing prompt token usage without affecting behavior.


### Reduced Subagent Prompt Token Usage

What: Removed a duplicate instruction from subagent prompts about not using colons before tool calls.

Details:
- The instruction "Do not use a colon before tool calls. Text like 'Let me read the file:' followed by a read tool call should just be 'Let me read the file.' with a period." was removed from the subagent system prompt builder
- This instruction remains in the main system prompt (`zb` function), so the guidance is still provided to the main conversation thread
- Subagents inherit context from the parent, making this instruction redundant for them
- This reduces token usage in subagent conversations without changing behavior

Evidence: `XbA()` at line 516791 (subagent prompt builder, removed duplicate colon instruction)

## Notes

This release contains no user-facing behavior changes. The 15 import additions and 15 import removals visible in the diff are internal code reorganization (changing from default imports to named imports for various Node.js modules) with no functional impact.
