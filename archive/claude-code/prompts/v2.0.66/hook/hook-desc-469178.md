---
id: hook-desc-469178
name: Hook Description
category: hook
subcategory: description
source_line: 469178
---

Input to command is JSON with original user prompt text.
Exit code 0 - stdout shown to Claude
Exit code 2 - block processing, erase original prompt, and show stderr to user only
Other exit codes - show stderr to user only
