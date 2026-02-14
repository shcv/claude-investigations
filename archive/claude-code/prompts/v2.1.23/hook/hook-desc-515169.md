---
id: hook-desc-515169
name: Hook Description
category: hook
subcategory: description
source_line: 515169
---

Input to command is JSON with tool_name, tool_input, and tool_use_id.
Output JSON with hookSpecificOutput containing decision to allow or deny.
Exit code 0 - use hook decision if provided
Other exit codes - show stderr to user only
