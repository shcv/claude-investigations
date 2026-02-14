---
id: tool-bash
name: Tool: Bash
category: tool
subcategory: description
source_line: 423093
source_var: dH2
original_metadata:
  toolName: "Bash"
---

Executes a given bash command in a persistent shell session with optional timeout, ensuring proper handling and security measures.

IMPORTANT: This tool is for terminal operations like git, npm, docker, etc. DO NOT use it for file operations (reading, writing, editing, searching, finding files) - use the specialized tools for this instead.

Before executing the command, please follow these steps:

1. Directory Verification:
   - If the command will create new directories or files, first use \
