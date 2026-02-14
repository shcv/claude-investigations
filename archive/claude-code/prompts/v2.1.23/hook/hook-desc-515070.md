---
id: hook-desc-515070
name: Hook Description
category: hook
subcategory: description
source_line: 515070
---

Input to command is JSON of tool call arguments.
Exit code 0 - stdout/stderr not shown
Exit code 2 - show stderr to model and block tool call
Other exit codes - show stderr to user only but continue with tool call
