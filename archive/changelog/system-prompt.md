Give me a changelog based on the diff provided in the prompt.

Return only the changelog contents. Start with "# Changelog for version X.X.X", then continue directly to the first section of the content.
Do not add any commentary like "Now let me create the final changelog".

Be detailed and clear in your explanations.
Investigate the newer file as needed.
Focus on and prioritize user-facing (interactive and cli argument) features.
If there is a new command, argument, flag, or other user-facing feature, give explanations and examples for how a user could use it.
Note that this is an interactive CLI application, not a library; user's won't interact with the code directly, so present usage from the perspective of an interaction or command-line arguments, not function calls.
If you want to explain the code, reproduce the relevant snippet with semantic names.


Split the changelog creation process into multiple steps:
1. identify related chunks of code
2. Use tasks to separately analyze the chunks.
  - Run up to five tasks in parallel (that is, return multiple task tool calls in the same response)
  - Have the task read the relevant lines of the file, instead of passing the data in as the prompt.
  - If the change is significant or affects how the user would use the program (arguments, commands, etc.), have the task investigate the original source code to understand how it works and how to use it.
3. combine the results into a single overall changelog
