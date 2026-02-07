--- archive/claude-code/pretty/pretty-v2.1.31.js
+++ archive/claude-code/pretty/pretty-v2.1.32.js
Structural similarity: 98.6%
Matched: 14400/14490 vs 14605
Changes: 205 added, 90 removed, 988 structural, 42 string-only (13370 unchanged)

Filtered: 47 version bumps, 620 reformatting-only changes

=== Import Style Changes ===

"child_process":
  - import By9 from "child_process";
  - import my9 from "child_process";
  + import { execFile as hqK, spawn as IqK, spawnSync as xqK } from "child_process";
  + import { spawn as Um5, spawnSync as pm5 } from "child_process";

"crypto":
  - import LN9 from "crypto";
  - import RN9 from "crypto";
  + import { createHash as O64, randomUUID as zI9 } from "crypto";
  + import { createHash as iFY, randomBytes as nFY } from "crypto";
  + import { randomBytes as QKz, randomUUID as gKz } from "crypto";
  + import { randomBytes as QJz, timingSafeEqual as gJz } from "crypto";

"https":
  - import xn7 from "https";
  + import { Agent as eY5 } from "https";

"node:child_process":
  - import ck6 from "node:child_process";
  - import we7 from "node:child_process";
  + import { execFile as R09, execFileSync as Ol2 } from "node:child_process";
  + import { execFileSync as iQY, spawn as nQY } from "node:child_process";

"node:fs":
  - import eR9 from "node:fs";
  - import Ky9 from "node:fs";
  + import {
  +   existsSync as gg1,
  +   statSync as xQY,
  +   mkdirSync as bQY,
  +   realpathSync as uQY,
  + } from "node:fs";
  + import {
  +   constants as pQY,
  +   readFileSync as dQY,
  +   existsSync as cQY,
  +   unlinkSync as lQY,
  + } from "node:fs";

"node:os":
  - import qy9 from "node:os";
  + import { homedir as kJz } from "node:os";

"node:path":
  - import ze7 from "node:path";
  + import {
  +   join as NJ,
  +   dirname as hd,
  +   resolve as Om,
  +   delimiter as wdY,
  +   basename as HdY,
  + } from "node:path";

"node:process":
  - import b2q from "node:process";
  + import { cwd as RW7 } from "node:process";

"node:util":
  - import wG9 from "node:util";
  + import { isDeepStrictEqual as v8q } from "node:util";

"path":
  - import SR9 from "path";
  + import { dirname as Q_z, join as TNq } from "path";

"stream":
  - import yz1 from "stream";
  + import { PassThrough as DJz } from "stream";

=== Removed ===

--- Removed M4 (pretty-v2.1.31.js:28104-28118)
- function M4() {
-   let A = (() => {
-       switch (z48()) {
-         case "local":
-           return f8K;
-         case "staging":
-           return Z8K ?? Y48;
-         case "prod":
-           return Y48;
-       }
-     })(),
-     q = process.env.CLAUDE_CODE_OAUTH_CLIENT_ID;
-   if (q) return { ...A, CLIENT_ID: q };
-   return A;
- }

--- Removed U8 (pretty-v2.1.31.js:147616-147627)
- function U8() {
-   if (RY(process.env.CLAUDE_CODE_AGENT_SWARMS)) return !1;
-   if (!r8("tengu_brass_pebble", !1)) return !1;
-   if (jA6()) return !0;
-   if (Dk()) return !0;
-   let A = vK(),
-     q = w3();
-   if (q?.hasExtraUsageEnabled === !0) return !0;
-   if (A === "enterprise" && q?.billingType === "usage_based") return !0;
-   if (A === null) return !0;
-   return !1;
- }

--- Removed h07 (pretty-v2.1.31.js:168811-168995)
- var h07 = E(() => {
-   C07 = `Use this tool to create and manage a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user.
- It also helps the user understand the progress of the task and overall progress of their requests.
- 
- ## When to Use This Tool
- Use this tool proactively in these scenarios:
- 
- 1. Complex multi-step tasks - When a task requires 3 or more distinct steps or actions
- 2. Non-trivial and complex tasks - Tasks that require careful planning or multiple operations
- 3. User explicitly requests todo list - When the user directly asks you to use the todo list
- 4. User provides multiple tasks - When users provide a list of things to be done (numbered or comma-separated)
- 5. After receiving new instructions - Immediately capture user requirements as todos
- 6. When you start working on a task - Mark it as in_progress BEFORE beginning work. Ideally you should only have one todo as in_progress at a time
- 7. After completing a task - Mark it as completed and add any new follow-up tasks discovered during implementation
- 
- ## When NOT to Use This Tool
- 
- Skip using this tool when:
- 1. There is only a single, straightforward task
- 2. The task is trivial and tracking it provides no organizational benefit
- 3. The task can be completed in less than 3 trivial steps
- 4. The task is purely conversational or informational
- 
- NOTE that you should not use this tool if there is only one trivial task to do. In this case you are better off just doing the task directly.
- 
- ## Examples of When to Use the Todo List
- 
- <example>
- User: I want to add a dark mode toggle to the application settings. Make sure you run the tests and build when you're done!
- Assistant: I'll help add a dark mode toggle to your application settings. Let me create a todo list to track this implementation.
- *Creates todo list with the following items:*
- 1. Creating dark mode toggle component in Settings page
- 2. Adding dark mode state management (context/store)
- 3. Implementing CSS-in-JS styles for dark theme
- 4. Updating existing components to support theme switching
- 5. Running tests and build process, addressing any failures or errors that occur
- *Begins working on the first task*
- 
- <reasoning>
- The assistant used the todo list because:
- 1. Adding dark mode is a multi-step feature requiring UI, state management, and styling changes
- 2. The user explicitly requested tests and build be run afterward
- 3. The assistant inferred that tests and build need to pass by adding "Ensure tests and build succeed" as the final task
- </reasoning>
- </example>
- 
- <example>
- User: Help me rename the function getCwd to getCurrentWorkingDirectory across my project
- Assistant: Let me first search through your codebase to find all occurrences of 'getCwd'.
- *Uses grep or search tools to locate all instances of getCwd in the codebase*
- Assistant: I've found 15 instances of 'getCwd' across 8 different files. Let me create a todo list to track these changes.
- *Creates todo list with specific items for each file that needs updating*
- 
- <reasoning>
- The assistant used the todo list because:
- 1. First, the assistant searched to understand the scope of the task
- 2. Upon finding multiple occurrences across different files, it determined this was a complex task with multiple steps
- 3. The todo list helps ensure every instance is tracked and updated systematically
- 4. This approach prevents missing any occurrences and maintains code consistency
- </reasoning>
- </example>
- 
- 
- <example>
- User: I need to implement these features for my e-commerce site: user registration, product catalog, shopping cart, and checkout flow.
- Assistant: I'll help implement these features. First, let's add all the features to the todo list.
- *Creates a todo list breaking down each feature into specific tasks based on the project architecture*
- Assistant: Let's start with user registration. This will involve creating database models, API endpoints, and frontend forms that integrate with your existing authentication system.
- 
- <reasoning>
- The assistant used the todo list because:
- 1. The user provided multiple complex features to implement in a comma separated list
- 2. The todo list helps organize these large features into manageable tasks
- 3. This approach allows for tracking progress across the entire implementation
- </reasoning>
- </example>
- 
- <example>
- User: Can you help optimize my React application? It's rendering slowly and has performance issues.</user>
- Assistant: I'll help optimize your React application. First, let me examine your codebase to identify potential performance bottlenecks.
- *Reviews component structure, render patterns, state management, and data fetching*
- Assistant: After analyzing your codebase, I've identified several performance issues. Let me create a todo list to track our optimization efforts.
- *Creates todo list with items like: 1) Implementing memoization for expensive calculations in ProductList, 2) Adding virtualization for long lists in Dashboard, 3) Optimizing image loading in Gallery component, 4) Fixing state update loops in ShoppingCart, 5) Reviewing bundle size and implementing code splitting*
- Let's start by implementing memoization for the expensive calculations in your ProductList component.</assistant>
- 
- <reasoning>
- The assistant used the todo list because:
- 1. First, the assistant examined the codebase to identify specific performance issues
- 2. Based on this analysis, it identified multiple optimization opportunities
- 3. Performance optimization is a non-trivial task requiring multiple steps
- 4. The todo list helps methodically track improvements across different components
- 5. This systematic approach ensures all performance bottlenecks are addressed
- </reasoning>
- </example>
- 
- ## Examples of When NOT to Use the Todo List
- 
- <example>
- User: How do I print 'Hello World' in Python?
- Assistant: In Python, you can print "Hello World" with this simple code:
- 
- python
- print("Hello World")
- 
- This will output the text "Hello World" to the console when executed.</assistant>
- 
- <reasoning>
- The assistant did not use the todo list because this is a single, trivial task that can be completed in one step. There's no need to track multiple tasks or steps for such a straightforward request.
- </reasoning>
- </example>
- 
- <example>
- User: What does the git status command do?
- Assistant: The git status command shows the current state of your working directory and staging area. It displays which changes have been staged, which haven't, and which files aren't being tracked by Git. This is a fundamental command for understanding the current state of your repository before making commits.
- 
- <reasoning>
- The assistant did not use the todo list because this is an informational request with no actual coding task to complete. The user is simply asking for an explanation, not for the assistant to perform multiple steps or tasks.
- </reasoning>
- </example>
- 
- <example>
- User: Can you add a comment to the calculateTotal function to explain what it does?
- Assistant: Sure, let me add a comment to the calculateTotal function to explain what it does.
- * Uses the ${pq} tool to add a comment to the calculateTotal function *
- 
- <reasoning>
- The assistant did not use the todo list because this is a single, straightforward task confined to one location in the code. Adding a comment doesn't require tracking multiple steps or systematic organization.
- </reasoning>
- </example>
- 
- <example>
- User: Run npm install for me and tell me what happens.
- Assistant: I'll run the npm install command for you.
- 
- *Executes: npm install*
- 
- The command completed successfully. Here's the output:
- [Output of npm install command]
- 
- All dependencies have been installed according to your package.json file.
- 
- <reasoning>
- The assistant did not use the todo list because this is a single command execution with immediate results. There are no multiple steps to track or organize, making the todo list unnecessary for this straightforward task.
- </reasoning>
- </example>
- 
- ## Task States and Management
- 
- 1. **Task States**: Use these states to track progress:
-    - pending: Task not yet started
-    - in_progress: Currently working on (limit to ONE task at a time)
-    - completed: Task finished successfully
- 
-    **IMPORTANT**: Task descriptions must have two forms:
-    - content: The imperative form describing what needs to be done (e.g., "Run tests", "Build the project")
-    - activeForm: The present continuous form shown during execution (e.g., "Running tests", "Building the project")
- 
- 2. **Task Management**:
-    - Update task status in real-time as you work
-    - Mark tasks complete IMMEDIATELY after finishing (don't batch completions)
-    - Exactly ONE task must be in_progress at any time (not less, not more)
-    - Complete current tasks before starting new ones
-    - Remove tasks that are no longer relevant from the list entirely
- 
- 3. **Task Completion Requirements**:
-    - ONLY mark a task as completed when you have FULLY accomplished it
-    - If you encounter errors, blockers, or cannot finish, keep the task as in_progress
-    - When blocked, create a new task describing what needs to be resolved
-    - Never mark a task as completed if:
-      - Tests are failing
-      - Implementation is partial
-      - You encountered unresolved errors
-      - You couldn't find necessary files or dependencies
- 
- 4. **Task Breakdown**:
-    - Create specific, actionable items
-    - Break complex tasks into smaller, manageable steps
-    - Use clear, descriptive task names
-    - Always provide both forms:
-      - content: "Fix authentication bug"
-      - activeForm: "Fixing authentication bug"
- 
- When in doubt, use this tool. Being proactive with task management demonstrates attentiveness and ensures you complete all requirements successfully.
- `;
- });

--- Removed DM7 (pretty-v2.1.31.js:184778-184786)
- var DM7 = E(() => {
-   d4A();
-   b4A();
-   p81();
-   n_();
-   v_1();
-   _6();
-   XM7 = new Intl.Segmenter();
- });

--- Removed hY (pretty-v2.1.31.js:189993-189996)
- function hY(A) {
-   let K = W6().featureUsage?.[A];
-   return K !== void 0 && K.usageCount > 0;
- }

--- Removed NG7 (pretty-v2.1.31.js:190003-190007)
- function NG7() {
-   let A = {};
-   for (let q of fK6) A[q.id] = { explored: 0, total: 0 };
-   return A;
- }

--- Removed NK6 (pretty-v2.1.31.js:190009-190425)
- var NK6 = E(() => {
-   uA();
-   k7();
-   C8();
-   Gw();
-   fK6 = [
-     {
-       id: "quick-wins",
-       name: "Quick Wins",
-       description: "Try these in 30 seconds",
-       order: 1,
-     },
-     {
-       id: "speed",
-       name: "10x Your Speed",
-       description: "Efficiency boosters",
-       order: 2,
-     },
-     {
-       id: "code",
-       name: "Level Up Your Code",
-       description: "Dev workflows",
-       order: 3,
-     },
-     {
-       id: "collaborate",
-       name: "Share & Collaborate",
-       description: "Work with your team",
-       order: 4,
-     },
-     {
-       id: "customize",
-       name: "Make It Yours",
-       description: "Personalize Claude",
-       order: 5,
-     },
-     {
-       id: "power-user",
-       name: "Power User",
-       description: "Advanced features",
-       order: 6,
-     },
-   ];
-   VK6 = [
-     {
-       id: "image-paste",
-       name: "Paste Images",
-       description: "Paste screenshots for Claude to analyze",
-       categoryId: "quick-wins",
-       tryItPrompt: "Press Ctrl+V to paste an image from clipboard",
-       hasBeenUsed: async () => hY("image-paste"),
-     },
-     {
-       id: "resume",
-       name: "Resume Conversations",
-       description: "Pick up where you left off",
-       categoryId: "quick-wins",
-       tryItPrompt: "Type /resume to continue a past conversation",
-       hasBeenUsed: async () => hY("resume"),
-     },
-     {
-       id: "cost",
-       name: "Track Costs",
-       description: "See your session spending",
-       categoryId: "quick-wins",
-       tryItPrompt: "Type /cost to see session cost",
-       hasBeenUsed: async () => hY("cost"),
-     },
-     {
-       id: "external-editor",
-       name: "External Editor",
-       description: "Edit prompts in VS Code or vim",
-       categoryId: "quick-wins",
-       get tryItPrompt() {
-         return `Press ${HX("chat:externalEditor", "Chat", "Ctrl+G")} to open your editor`;
-       },
-       hasBeenUsed: async () => hY("external-editor"),
-     },
-     {
-       id: "slash-commands",
-       name: "Skills",
-       description: "Quick actions with /skills",
-       categoryId: "quick-wins",
-       tryItPrompt: "Type / to see available skills",
-       hasBeenUsed: async () => hY("slash-commands"),
-     },
-     {
-       id: "at-mentions",
-       name: "@-mentions",
-       description: "Reference files with @filename",
-       categoryId: "quick-wins",
-       tryItPrompt: "Type @ followed by a filename",
-       hasBeenUsed: async () => hY("at-mentions"),
-     },
-     {
-       id: "clear",
-       name: "Fresh Start",
-       description: "Clear and start over",
-       categoryId: "quick-wins",
-       tryItPrompt: "Type /clear for a fresh conversation",
-       hasBeenUsed: async () => hY("clear"),
-     },
-     {
-       id: "rewind",
-       name: "Undo Changes",
-       description: "Go back to a previous point",
-       categoryId: "quick-wins",
-       tryItPrompt: "Type /rewind to undo",
-       hasBeenUsed: async () => hY("rewind"),
-     },
-     {
-       id: "ctrl-underscore",
-       name: "Quick Undo",
-       description: "Undo with keyboard shortcut",
-       categoryId: "quick-wins",
-       get tryItPrompt() {
-         return `Press ${HX("chat:undo", "Chat", "Ctrl+_")} to undo`;
-       },
-       hasBeenUsed: async () => hY("ctrl-underscore"),
-     },
-     {
-       id: "double-escape",
-       name: "Clear Input",
-       description: "Double-tap Escape to clear",
-       categoryId: "quick-wins",
-       tryItPrompt: "Press Escape twice to clear input",
-       hasBeenUsed: async () => hY("double-escape"),
-     },
-     {
-       id: "prompt-stash",
-       name: "Stash Prompt",
-       description: "Save prompt for later",
-       categoryId: "quick-wins",
-       get tryItPrompt() {
-         let A = HX("chat:stash", "Chat", "Ctrl+S");
-         return `Press ${A} to stash, ${A} again to restore`;
-       },
-       hasBeenUsed: async () => hY("prompt-stash"),
-     },
-     {
-       id: "vim-mode",
-       name: "Vim Mode",
-       description: "Vim keybindings in the prompt",
-       categoryId: "speed",
-       tryItPrompt: "Type /vim to toggle Vim mode",
-       hasBeenUsed: async () => hY("vim-mode"),
-     },
-     {
-       id: "history-search",
-       name: "History Search",
-       description: "Search past prompts like bash",
-       categoryId: "speed",
-       get tryItPrompt() {
-         return `Press ${HX("history:search", "Global", "Ctrl+R")} to search history`;
-       },
-       hasBeenUsed: async () => hY("history-search"),
-     },
-     {
-       id: "tab-completion",
-       name: "Tab Completion",
-       description: "Autocomplete file paths",
-       categoryId: "speed",
-       tryItPrompt: "Start typing a path and press Tab",
-       hasBeenUsed: async () => hY("tab-completion"),
-     },
-     {
-       id: "prompt-queue",
-       name: "Prompt Queue",
-       description: "Type while Claude works",
-       categoryId: "speed",
-       tryItPrompt: "Type your next prompt while Claude is responding",
-       hasBeenUsed: async () => {
-         return W6().promptQueueUseCount > 0;
-       },
-     },
-     {
-       id: "teleport",
-       name: "Teleport",
-       description: "Jump to any GitHub repo instantly",
-       categoryId: "speed",
-       tryItPrompt: "Type /teleport owner/repo to jump there",
-       hasBeenUsed: async () => hY("teleport"),
-     },
-     {
-       id: "plan-mode",
-       name: "Plan Mode",
-       description: "Think before you code",
-       categoryId: "speed",
-       tryItPrompt: "Press Shift+Tab twice for Plan Mode",
-       hasBeenUsed: async () => {
-         return W6().lastPlanModeUse !== void 0;
-       },
-     },
-     {
-       id: "bash-mode",
-       name: "Bash Mode",
-       description: "Run shell commands with ! prefix",
-       categoryId: "speed",
-       tryItPrompt: "Type !ls to list files",
-       hasBeenUsed: async () => hY("bash-mode"),
-     },
-     {
-       id: "compact",
-       name: "Compact Context",
-       description: "Summarize to free up space",
-       categoryId: "speed",
-       tryItPrompt: "Type /compact to summarize",
-       hasBeenUsed: async () => hY("compact"),
-     },
-     {
-       id: "memory-mode",
-       name: "Quick Memory",
-       description: "Save notes with # prefix",
-       categoryId: "speed",
-       tryItPrompt: "Press # to add to memory",
-       hasBeenUsed: async () => {
-         return W6().memoryUsageCount > 0;
-       },
-     },
-     {
-       id: "auto-accept-mode",
-       name: "Auto-Accept Edits",
-       description: "Skip confirmations",
-       categoryId: "speed",
-       tryItPrompt: "Press Shift+Tab once for Auto-Accept",
-       hasBeenUsed: async () => hY("auto-accept-mode"),
-     },
-     {
-       id: "context",
-       name: "Context Viewer",
-       description: "See what Claude sees",
-       categoryId: "speed",
-       tryItPrompt: "Type /context to visualize usage",
-       hasBeenUsed: async () => hY("context"),
-     },
-     {
-       id: "backslash-return",
-       name: "Multi-line Input",
-       description: "Type longer prompts",
-       categoryId: "speed",
-       tryItPrompt: "Type \\ then Enter for a new line",
-       hasBeenUsed: async () => {
-         return W6().hasUsedBackslashReturn === !0;
-       },
-     },
-     {
-       id: "review",
-       name: "Code Review",
-       description: "AI-powered code review",
-       categoryId: "code",
-       tryItPrompt: "Type /review to review a PR",
-       hasBeenUsed: async () => hY("review"),
-     },
-     {
-       id: "security-review",
-       name: "Security Review",
-       description: "Find vulnerabilities",
-       categoryId: "code",
-       tryItPrompt: "Ask Claude to do a security review",
-       hasBeenUsed: async () => hY("security-review"),
-     },
-     {
-       id: "git-commits",
-       name: "Git Commits",
-       description: "Claude-assisted commits",
-       categoryId: "code",
-       tryItPrompt: "Ask Claude to commit your changes",
-       hasBeenUsed: async () => hY("git-commits"),
-     },
-     {
-       id: "pr-creation",
-       name: "PR Creation",
-       description: "Create PRs with Claude",
-       categoryId: "code",
-       tryItPrompt: "Ask Claude to create a pull request",
-       hasBeenUsed: async () => hY("pr-creation"),
-     },
-     {
-       id: "branch-management",
-       name: "Branch Management",
-       description: "Git branch operations",
-       categoryId: "code",
-       tryItPrompt: "Ask Claude to create a branch",
-       hasBeenUsed: async () => hY("branch-management"),
-     },
-     {
-       id: "share",
-       name: "Share Conversations",
-       description: "Share a link to your session",
-       categoryId: "collaborate",
-       tryItPrompt: "Type /share to get a shareable link",
-       hasBeenUsed: async () => hY("share"),
-     },
-     {
-       id: "export",
-       name: "Export",
-       description: "Save as markdown",
-       categoryId: "collaborate",
-       tryItPrompt: "Type /export to save conversation",
-       hasBeenUsed: async () => hY("export"),
-     },
-     {
-       id: "github-app",
-       name: "GitHub Integration",
-       description: "Connect to GitHub Actions",
-       categoryId: "collaborate",
-       tryItPrompt: "Type /install-github-app to set up",
-       hasBeenUsed: async () => hY("github-app"),
-     },
-     {
-       id: "slack-app",
-       name: "Slack Notifications",
-       description: "Get notified in Slack",
-       categoryId: "collaborate",
-       tryItPrompt: "Type /install-slack-app to connect",
-       hasBeenUsed: async () => hY("slack-app"),
-     },
-     {
-       id: "custom-commands",
-       name: "Custom Skills",
-       description: "Create your own /skills",
-       categoryId: "customize",
-       tryItPrompt: "Create .claude/skills/myskill/SKILL.md",
-       hasBeenUsed: async () => {
-         let A = y6(),
-           q = ZK6(A, ".claude", "skills"),
-           K = ZK6(ZG7(), ".claude", "skills");
-         return GK6(q) || GK6(K);
-       },
-     },
-     {
-       id: "hooks",
-       name: "Hooks",
-       description: "Auto-run scripts on events",
-       categoryId: "customize",
-       tryItPrompt: "Add hooks to .claude/settings.json",
-       hasBeenUsed: async () => {
-         let A = P8();
-         return Object.keys(A.hooks ?? {}).length > 0;
-       },
-     },
-     {
-       id: "theme",
-       name: "Themes",
-       description: "Customize colors",
-       categoryId: "customize",
-       tryItPrompt: "Type /config to change theme",
-       hasBeenUsed: async () => hY("theme"),
-     },
-     {
-       id: "claude-md-project",
-       name: "Project Instructions",
-       description: "CLAUDE.md for your project",
-       categoryId: "customize",
-       tryItPrompt: "Create CLAUDE.md in your project root",
-       hasBeenUsed: async () => {
-         let A = y6(),
-           q = ZK6(A, "CLAUDE.md");
-         return GK6(q);
-       },
-     },
-     {
-       id: "claude-md-user",
-       name: "Personal Instructions",
-       description: "Your global CLAUDE.md",
-       categoryId: "customize",
-       tryItPrompt: "Create ~/.claude/CLAUDE.md",
-       hasBeenUsed: async () => {
-         let A = ZK6(ZG7(), ".claude", "CLAUDE.md");
-         return GK6(A);
-       },
-     },
-     {
-       id: "mcp-servers",
-       name: "MCP Servers",
-       description: "Connect external tools",
-       categoryId: "power-user",
-       tryItPrompt: "Type /mcp to manage servers",
-       hasBeenUsed: async () => {
-         let A = W6();
-         return Object.keys(A.mcpServers ?? {}).length > 0;
-       },
-     },
-     {
-       id: "ide-integration",
-       name: "IDE Integration",
-       description: "Connect to VS Code",
-       categoryId: "power-user",
-       tryItPrompt: "Type /ide to configure",
-       hasBeenUsed: async () => hY("ide-integration"),
-     },
-     {
-       id: "subagents",
-       name: "Subagents",
-       description: "Claude spawns helper agents",
-       categoryId: "power-user",
-       tryItPrompt: "Ask Claude to explore the codebase",
-       hasBeenUsed: async () => hY("subagents"),
-     },
-     {
-       id: "plugins",
-       name: "Plugins",
-       description: "Extend with plugins",
-       categoryId: "power-user",
-       tryItPrompt: "Type /plugin to manage plugins",
-       hasBeenUsed: async () => hY("plugins"),
-     },
-     {
-       id: "multi-directory",
-       name: "Multi-Directory",
-       description: "Work across projects",
-       categoryId: "power-user",
-       tryItPrompt: "Type /add-dir to add another directory",
-       hasBeenUsed: async () => hY("multi-directory"),
-     },
-   ];
- });

--- Removed TG7 (pretty-v2.1.31.js:190439-190451)
- async function TG7() {
-   let A = VK6.map(async (z) => ({
-       id: z.id,
-       categoryId: z.categoryId,
-       used: await z.hasBeenUsed(),
-     })),
-     q = await Promise.all(A),
-     K = NG7(),
-     Y = 0;
-   for (let z of q)
-     if ((K[z.categoryId].total++, z.used)) (K[z.categoryId].explored++, Y++);
-   return { explored: Y, total: VK6.length, byCategory: K };
- }

--- Removed UG7 (pretty-v2.1.31.js:191651-191662)
- var UG7 = E(() => {
-   B81();
-   Zb();
-   r81();
-   b_1();
-   mG7();
-   Pq6();
-   FG7 =
-     typeof Intl < "u" && "Segmenter" in Intl
-       ? new Intl.Segmenter(void 0, { granularity: "grapheme" })
-       : null;
- });

--- Removed s_1 (pretty-v2.1.31.js:194807-195042)
- function s_1(A) {
-   let q = t(51),
-     {
-       option: K,
-       isFocused: Y,
-       isSelected: z,
-       shouldShowDownArrow: w,
-       shouldShowUpArrow: H,
-       maxIndexWidth: O,
-       index: $,
-       inputValue: _,
-       onInputChange: J,
-       onSubmit: X,
-       onExit: D,
-       layout: j,
-       children: M,
-       showLabel: W,
-       onOpenEditor: P,
-       resetCursorOnUpdate: G,
-     } = A,
-     f = W === void 0 ? !1 : W,
-     V = G === void 0 ? !1 : G,
-     N = f || K.showLabelWithValue === !0,
-     [T, k] = q_.useState(_.length),
-     y;
-   if (q[0] !== _.length || q[1] !== Y || q[2] !== V)
-     ((y = () => {
-       if (V && Y) k(_.length);
-     }),
-       (q[0] = _.length),
-       (q[1] = Y),
-       (q[2] = V),
-       (q[3] = y));
-   else y = q[3];
-   let B;
-   if (q[4] !== _ || q[5] !== Y || q[6] !== V)
-     ((B = [V, Y, _]), (q[4] = _), (q[5] = Y), (q[6] = V), (q[7] = B));
-   else B = q[7];
-   q_.useEffect(y, B);
-   let C;
-   if (q[8] !== _ || q[9] !== J || q[10] !== P)
-     ((C = () => {
-       P?.(_, J);
-     }),
-       (q[8] = _),
-       (q[9] = J),
-       (q[10] = P),
-       (q[11] = C));
-   else C = q[11];
-   let m = Y && !!P,
-     u;
-   if (q[12] !== m)
-     ((u = { context: "Chat", isActive: m }), (q[12] = m), (q[13] = u));
-   else u = q[13];
-   zA("chat:externalEditor", C, u);
-   let U = j === "expanded" ? O + 3 : O + 4,
-     g = j === "compact" ? 0 : void 0,
-     x = `${$}.`,
-     d;
-   if (q[14] !== O || q[15] !== x)
-     ((d = x.padEnd(O + 2)), (q[14] = O), (q[15] = x), (q[16] = d));
-   else d = q[16];
-   let r;
-   if (q[17] !== d)
-     ((r = q_.default.createElement(Z, { dimColor: !0 }, d)),
-       (q[17] = d),
-       (q[18] = r));
-   else r = q[18];
-   let c;
-   if (
-     q[19] !== T ||
-     q[20] !== _ ||
-     q[21] !== Y ||
-     q[22] !== D ||
-     q[23] !== J ||
-     q[24] !== X ||
-     q[25] !== K ||
-     q[26] !== N
-   )
-     ((c = N
-       ? q_.default.createElement(
-           q_.default.Fragment,
-           null,
-           q_.default.createElement(
-             Z,
-             { color: Y ? "suggestion" : void 0 },
-             K.label,
-           ),
-           Y
-             ? q_.default.createElement(
-                 q_.default.Fragment,
-                 null,
-                 q_.default.createElement(
-                   Z,
-                   { color: "suggestion" },
-                   K.labelValueSeparator ?? ", ",
-                 ),
-                 q_.default.createElement(eK, {
-                   value: _,
-                   onChange: (s) => {
-                     (J(s), K.onChange(s));
-                   },
-                   onSubmit: X,
-                   onExit: D,
-                   placeholder: K.placeholder,
-                   focus: !0,
-                   showCursor: !0,
-                   cursorOffset: T,
-                   onChangeCursorOffset: k,
-                   columns: 80,
-                 }),
-               )
-             : _ &&
-                 q_.default.createElement(
-                   Z,
-                   null,
-                   K.labelValueSeparator ?? ", ",
-                   _,
-                 ),
-         )
-       : Y
-         ? q_.default.createElement(eK, {
-             value: _,
-             onChange: (s) => {
-               (J(s), K.onChange(s));
-             },
-             onSubmit: X,
-             onExit: D,
-             placeholder:
-               K.placeholder || (typeof K.label === "string" ? K.label : void 0),
-             focus: !0,
-             showCursor: !0,
-             cursorOffset: T,
-             onChangeCursorOffset: k,
-             columns: 80,
-           })
-         : q_.default.createElement(
-             Z,
-             { color: _ ? void 0 : "inactive" },
-             _ || K.placeholder || K.label,
-           )),
-       (q[19] = T),
-       (q[20] = _),
-       (q[21] = Y),
-       (q[22] = D),
-       (q[23] = J),
-       (q[24] = X),
-       (q[25] = K),
-       (q[26] = N),
-       (q[27] = c));
-   else c = q[27];
-   let q1;
-   if (q[28] !== M || q[29] !== r || q[30] !== c || q[31] !== g)
-     ((q1 = q_.default.createElement(
-       h,
-       { flexDirection: "row", flexShrink: g },
-       r,
-       M,
-       c,
-     )),
-       (q[28] = M),
-       (q[29] = r),
-       (q[30] = c),
-       (q[31] = g),
-       (q[32] = q1));
-   else q1 = q[32];
-   let H1;
-   if (q[33] !== Y || q[34] !== z || q[35] !== w || q[36] !== H || q[37] !== q1)
-     ((H1 = q_.default.createElement(
-       tn,
-       {
-         isFocused: Y,
-         isSelected: z,
-         shouldShowDownArrow: w,
-         shouldShowUpArrow: H,
-       },
-       q1,
-     )),
-       (q[33] = Y),
-       (q[34] = z),
-       (q[35] = w),
-       (q[36] = H),
-       (q[37] = q1),
-       (q[38] = H1));
-   else H1 = q[38];
-   let $1;
-   if (
-     q[39] !== U ||
-     q[40] !== Y ||
-     q[41] !== z ||
-     q[42] !== K.description ||
-     q[43] !== K.dimDescription
-   )
-     (($1 =
-       K.description &&
-       q_.default.createElement(
-         h,
-         { paddingLeft: U },
-         q_.default.createElement(
-           Z,
-           {
-             dimColor: K.dimDescription !== !1,
-             color: z ? "success" : Y ? "suggestion" : void 0,
-           },
-           K.description,
-         ),
-       )),
-       (q[39] = U),
-       (q[40] = Y),
-       (q[41] = z),
-       (q[42] = K.description),
-       (q[43] = K.dimDescription),
-       (q[44] = $1));
-   else $1 = q[44];
-   let A1;
-   if (q[45] !== j)
-     ((A1 = j === "expanded" && q_.default.createElement(Z, null, " ")),
-       (q[45] = j),
-       (q[46] = A1));
-   else A1 = q[46];
-   let O1;
-   if (q[47] !== H1 || q[48] !== $1 || q[49] !== A1)
-     ((O1 = q_.default.createElement(
-       h,
-       { flexDirection: "column", flexShrink: 0 },
-       H1,
-       $1,
-       A1,
-     )),
-       (q[47] = H1),
-       (q[48] = $1),
-       (q[49] = A1),
-       (q[50] = O1));
-   else O1 = q[50];
-   return O1;
- }

--- Removed ko (pretty-v2.1.31.js:272380-272399)
- var ko = E(() => {
-   Q4();
-   NH6();
-   g6();
-   mA();
-   ((Q14 = `Search for or select deferred tools to make them available for use.
- 
- **MANDATORY PREREQUISITE - THIS IS A HARD REQUIREMENT**
- 
- You MUST use this tool to load deferred tools BEFORE calling them directly.
- 
- This is a BLOCKING REQUIREMENT - deferred tools listed below are NOT available until you load them using this tool. Both query modes (keyword search and direct selection) load the returned tools — once a tool appears in the results, it is immediately available to call.${g14}`),
-     (CS9 = `Search for or select deferred tools to make them available for use.
- 
- **MANDATORY PREREQUISITE - THIS IS A HARD REQUIREMENT**
- 
- You MUST use this tool to load deferred tools BEFORE calling them directly.
- 
- This is a BLOCKING REQUIREMENT - deferred tools are NOT available until you load them using this tool. Look for <available-deferred-tools> messages in the conversation for the list of tools you can discover. Both query modes (keyword search and direct selection) load the returned tools — once a tool appears in the results, it is immediately available to call.${g14}`));
- });

--- Removed Fb1 (pretty-v2.1.31.js:293811-293842)
- var Fb1 = E(() => {
-   j_();
-   _6();
-   N6();
-   j_();
-   kr1();
-   Wz();
-   XDA = YA(async (A) => {
-     return `Execute a skill within the main conversation
- 
- When users ask you to perform tasks, check if any of the available skills match. Skills provide specialized capabilities and domain knowledge.
- 
- When users reference a "slash command" or "/<something>" (e.g., "/commit", "/review-pr"), they are referring to a skill. Use this tool to invoke it.
- 
- How to invoke:
- - Use this tool with the skill name and optional arguments
- - Examples:
-   - \`skill: "pdf"\` - invoke the pdf skill
-   - \`skill: "commit", args: "-m 'Fix bug'"\` - invoke with arguments
-   - \`skill: "review-pr", args: "123"\` - invoke with arguments
-   - \`skill: "ms-office-suite:pdf"\` - invoke using fully qualified name
- 
- Important:
- - Available skills are listed in system-reminder messages in the conversation
- - When a skill matches the user's request, this is a BLOCKING REQUIREMENT: invoke the relevant Skill tool BEFORE generating any other response about the task
- - NEVER mention a skill without actually calling this tool
- - Do not invoke a skill that is already running
- - Do not use this tool for built-in CLI commands (like /help, /clear, etc.)
- - If you see a <${SN}> tag in the current conversation turn, the skill has ALREADY been loaded - follow the instructions directly instead of calling this tool again
- `;
-   });
- });

--- Removed QS (pretty-v2.1.31.js:301496-301498)
- var QS = E(() => {
-   Qp9 = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
- });

--- Removed bfA (pretty-v2.1.31.js:356430-356439)
- var bfA = `
- # Teammate Communication
- 
- IMPORTANT: You are running as a teammate in a swarm. Your plain text output is NOT visible to the user or the team lead. To communicate with anyone on your team:
- - Use the Teammate tool with the \`write\` operation to send messages to specific teammates
- - Use the Teammate tool with the \`broadcast\` operation sparingly for team-wide announcements
- - Just typing a response in text is not visible to others - you must use the tool
- 
- The user interacts only with the team lead. Your work is coordinated through the task system and teammate messaging.
- `;

--- Removed rfA (pretty-v2.1.31.js:357780-357790)
- function rfA(A) {
-   return {
-     type: "join_request",
-     requestId: A.requestId,
-     sessionId: A.sessionId,
-     proposedName: A.proposedName,
-     capabilities: A.capabilities,
-     cwd: A.cwd,
-     timestamp: new Date().toISOString(),
-   };
- }

--- Removed ofA (pretty-v2.1.31.js:357791-357804)
- function ofA(A) {
-   return {
-     type: "join_approved",
-     requestId: A.requestId,
-     teamName: A.teamName,
-     teamFilePath: A.teamFilePath,
-     leadAgentId: A.leadAgentId,
-     agentId: A.agentId,
-     agentName: A.agentName,
-     color: A.color,
-     planModeRequired: A.planModeRequired,
-     timestamp: new Date().toISOString(),
-   };
- }

--- Removed N06 (pretty-v2.1.31.js:357805-357812)
- function N06(A) {
-   return {
-     type: "join_rejected",
-     requestId: A.requestId,
-     reason: A.reason,
-     timestamp: new Date().toISOString(),
-   };
- }

--- Removed T06 (pretty-v2.1.31.js:357813-357819)
- function T06(A) {
-   try {
-     let q = OA(A);
-     if (q && q.type === "join_request") return q;
-   } catch {}
-   return null;
- }

--- Removed EM1 (pretty-v2.1.31.js:357820-357826)
- function EM1(A) {
-   try {
-     let q = OA(A);
-     if (q && q.type === "join_approved") return q;
-   } catch {}
-   return null;
- }

--- Removed kM1 (pretty-v2.1.31.js:357827-357833)
- function kM1(A) {
-   try {
-     let q = OA(A);
-     if (q && q.type === "join_rejected") return q;
-   } catch {}
-   return null;
- }

--- Removed v06 (pretty-v2.1.31.js:357834-357840)
- function v06(A, q) {
-   let K = QfA(),
-     Y = Tn(A),
-     z = Tn(q),
-     w = VM1(K, Y, "inboxes");
-   return VM1(w, `pending-${z}.json`);
- }

--- Removed E06 (pretty-v2.1.31.js:357841-357859)
- function E06(A, q) {
-   let K = v06(A, q);
-   if ((I(`[TeammateMailbox] readPendingInbox: path=${K}`), !jB(K)))
-     return (I("[TeammateMailbox] readPendingInbox: file does not exist"), []);
-   try {
-     let Y = FfA(K, "utf-8"),
-       z = OA(Y);
-     return (
-       I(`[TeammateMailbox] readPendingInbox: read ${z.length} message(s)`),
-       z
-     );
-   } catch (Y) {
-     return (
-       I(`Failed to read pending inbox for ${q}: ${Y}`),
-       e(Y instanceof Error ? Y : Error(String(Y))),
-       []
-     );
-   }
- }

--- Removed $m1 (pretty-v2.1.31.js:357860-357890)
- function $m1(A, q, K) {
-   Iv4(A);
-   let Y = v06(A, q),
-     z = `${Y}.lock`;
-   if (
-     (I(
-       `[TeammateMailbox] writeToPendingInbox: sessionId=${q}, from=${K.from}, path=${Y}`,
-     ),
-     !jB(Y))
-   )
-     (Q8(Y, "[]", "utf-8"),
-       I(
-         "[TeammateMailbox] writeToPendingInbox: created new pending inbox file",
-       ));
-   let w;
-   try {
-     w = NM1.lockSync(Y, { lockfilePath: z });
-     let H = E06(A, q),
-       O = { ...K, read: !1 };
-     (H.push(O),
-       Q8(Y, F1(H, null, 2), "utf-8"),
-       I(
-         `[TeammateMailbox] Wrote message to pending inbox for ${q} from ${K.from}`,
-       ));
-   } catch (H) {
-     (I(`Failed to write to pending inbox for ${q}: ${H}`),
-       e(H instanceof Error ? H : Error(String(H))));
-   } finally {
-     if (w) w();
-   }
- }

--- Removed LM1 (pretty-v2.1.31.js:357891-357900)
- function LM1(A, q) {
-   let K = v06(A, q);
-   if (!jB(K)) return;
-   try {
-     (p$Y(K), I(`[TeammateMailbox] Cleared pending inbox for ${q}`));
-   } catch (Y) {
-     (I(`Failed to clear pending inbox for ${q}: ${Y}`),
-       e(Y instanceof Error ? Y : Error(String(Y))));
-   }
- }

--- Removed gM1 (pretty-v2.1.31.js:364785-364790)
- function gM1(A, q) {
-   if (!vp()) return;
-   let K = FM1(q);
-   if (K.length === 0) return;
-   return { command: A, cwd: y6(), descriptions: K };
- }

--- Removed wk4 (pretty-v2.1.31.js:364802-364806)
- function wk4(A) {
-   let q = e06.get(A);
-   if (q) e06.delete(A);
-   return q;
- }

--- Removed qD6 (pretty-v2.1.31.js:364807-364813)
- async function qD6(A, q, K) {
-   let { command: Y, cwd: z, descriptions: w } = A,
-     H = wk4(Y),
-     O = H ? await H : await QM1(Y, z, w, "allow", q, K);
-   t06(Y, "allow", w, O);
-   return;
- }

--- Removed Hk4 (pretty-v2.1.31.js:364814-364829)
- async function Hk4(A, q, K, Y) {
-   let { command: z, cwd: w, descriptions: H } = A,
-     O = wk4(z),
-     $;
-   try {
-     $ = O ? await O : await QM1(z, w, H, "allow", q, K);
-   } catch (_) {
-     if (_ instanceof Kz || _ instanceof Qz) {
-       Y.onComplete?.();
-       return;
-     }
-     throw (Y.onComplete?.(), _);
-   }
-   if ((t06(z, "allow", H, $), !Y.shouldContinue())) return;
-   Y.onComplete?.();
- }

--- Removed Pk4 (pretty-v2.1.31.js:366066-366072)
- function Pk4() {
-   if (cM1)
-     ((Ws = cM1), I(`[TeammateModeSnapshot] Captured from CLI override: ${Ws}`));
-   else
-     ((Ws = W6().teammateMode ?? "auto"),
-       I(`[TeammateModeSnapshot] Captured from config: ${Ws}`));
- }

--- Removed ck4 (pretty-v2.1.31.js:367435-367480)
- function ck4(A, q, K) {
-   (I(
-     `[JoinInit] Initializing as teammate ${A.agentName} in team ${A.teamName}`,
-   ),
-     n1A({
-       agentId: A.agentId,
-       agentName: A.agentName,
-       teamName: A.teamName,
-       color: A.color,
-       planModeRequired: A.planModeRequired ?? !1,
-     }),
-     q((Y) => {
-       let z = A.planModeRequired
-         ? qz(Y.toolPermissionContext, {
-             type: "setMode",
-             mode: "plan",
-             destination: "session",
-           })
-         : Y.toolPermissionContext;
-       if (A.planModeRequired)
-         I("[JoinInit] Plan mode required, setting permission mode to plan");
-       return {
-         ...Y,
-         teamContext: {
-           teamName: A.teamName,
-           teamFilePath: A.teamFilePath,
-           leadAgentId: A.leadAgentId,
-           selfAgentId: A.agentId,
-           selfAgentName: A.agentName,
-           selfAgentColor: A.color,
-           isLeader: !1,
-           teammates: {},
-         },
-         toolPermissionContext: z,
-       };
-     }),
-     Im1(q, K, {
-       teamName: A.teamName,
-       agentId: A.agentId,
-       agentName: A.agentName,
-     }),
-     LM1(A.teamName, K),
-     I(
-       `[JoinInit] Successfully initialized as teammate ${A.agentName}@${A.teamName}`,
-     ));
- }

--- Removed PXY (pretty-v2.1.31.js:367518-367520)
- function PXY(A) {
-   return "teams" in A && Array.isArray(A.teams);
- }

--- Removed GXY (pretty-v2.1.31.js:367521-367534)
- function GXY(A) {
-   return (
-     "status" in A &&
-     [
-       "approved",
-       "rejected",
-       "timeout",
-       "request_sent",
-       "already_in_team",
-       "team_not_found",
-       "error",
-     ].includes(A.status)
-   );
- }

--- Removed ZXY (pretty-v2.1.31.js:367535-367537)
- function ZXY(A) {
-   return "member_name" in A && "member_agent_id" in A;
- }

--- Removed fXY (pretty-v2.1.31.js:367538-367545)
- function fXY(A) {
-   return (
-     "requestId" in A &&
-     "success" in A &&
-     !("member_name" in A) &&
-     !("status" in A)
-   );
- }

--- Removed ak4 (pretty-v2.1.31.js:367546-367639)
- function ak4(A, q, { verbose: K }) {
-   let Y = typeof A === "string" ? OA(A) : A;
-   if (WXY(Y))
-     return nW.default.createElement(Z, { dimColor: !0 }, "  ", "Created team");
-   if (PXY(Y)) {
-     let z = Y.teams.length;
-     if (z === 0)
-       return nW.default.createElement(
-         Z,
-         { dimColor: !0 },
-         "  ",
-         "no teams available to join",
-       );
-     return nW.default.createElement(
-       Z,
-       { dimColor: !0 },
-       "  ",
-       "found ",
-       z,
-       " team",
-       z === 1 ? "" : "s",
-       ":",
-       " ",
-       Y.teams.map((w) => w.name).join(", "),
-     );
-   }
-   if (GXY(Y))
-     switch (Y.status) {
-       case "approved":
-         return nW.default.createElement(
-           Z,
-           { dimColor: !0 },
-           "  ",
-           "joined team ",
-           Y.teamName,
-           " as ",
-           Y.agentName,
-         );
-       case "rejected":
-         return nW.default.createElement(
-           Z,
-           { dimColor: !0 },
-           "  ",
-           "join request rejected",
-         );
-       case "timeout":
-         return nW.default.createElement(
-           Z,
-           { dimColor: !0 },
-           "  ",
-           "join request timed out",
-         );
-       case "already_in_team":
-         return nW.default.createElement(
-           Z,
-           { dimColor: !0 },
-           "  ",
-           "already in a team",
-         );
-       case "team_not_found":
-         return nW.default.createElement(
-           Z,
-           { dimColor: !0 },
-           "  ",
-           "team not found",
-         );
-       default:
-         return nW.default.createElement(Z, { dimColor: !0 }, "  ", Y.message);
-     }
-   if (ZXY(Y))
-     return nW.default.createElement(
-       Z,
-       { dimColor: !0 },
-       "  ",
-       "approved join request from ",
-       Y.member_name,
-     );
-   if (fXY(Y))
-     return nW.default.createElement(
-       Z,
-       { dimColor: !0 },
-       "  ",
-       "rejected join request",
-     );
-   if ("success" in Y && "team_name" in Y && "message" in Y) return null;
-   if ("message" in Y)
-     return nW.default.createElement(Z, { dimColor: !0 }, "  ", Y.message);
-   return nW.default.createElement(
-     Z,
-     { dimColor: !0 },
-     "  ",
-     "operation complete",
-   );
- }

--- Removed xXY (pretty-v2.1.31.js:368043-368141)
- async function xXY(A, q) {
-   let { setAppState: K } = q,
-     { team_name: Y, proposed_name: z, capabilities: w, timeout_ms: H } = A;
-   if (!Y) throw Error("team_name is required for requestJoin operation");
-   if (!z)
-     return {
-       data: {
-         success: !1,
-         message:
-           "proposed_name is required for requestJoin operation. Please provide a name to join the team.",
-         status: "error",
-       },
-     };
-   let O = await q.getAppState(),
-     $ = R5(O.teamContext);
-   if ($)
-     return {
-       data: {
-         success: !1,
-         message: `Already a member of team "${$}". Cannot join another team.`,
-         status: "already_in_team",
-         teamName: $,
-       },
-     };
-   let _ = sH(Y);
-   if (!_)
-     return {
-       data: {
-         success: !1,
-         message: `Team "${Y}" not found`,
-         status: "team_not_found",
-       },
-     };
-   let J = F6(),
-     X = Ks("join", J),
-     D = rfA({
-       requestId: X,
-       sessionId: J,
-       proposedName: z,
-       capabilities: w,
-       cwd: y6(),
-     }),
-     M = _.members.find((f) => f.agentId === _.leadAgentId)?.name || Tz;
-   (p5(M, { from: z, text: F1(D), timestamp: new Date().toISOString() }, Y),
-     I(`[RequestJoin] Sent join request to ${M} for team ${Y}`));
-   let W = H || 60000,
-     P = 1000,
-     G = Date.now();
-   while (Date.now() - G < W) {
-     let f = E06(Y, J);
-     for (let V of f) {
-       let N = EM1(V.text);
-       if (N && N.requestId === X)
-         return (
-           I(`[RequestJoin] Join approved by team ${Y}`),
-           ck4(N, K, J),
-           {
-             data: {
-               success: !0,
-               message: `Successfully joined team "${Y}" as ${N.agentName}`,
-               status: "approved",
-               requestId: X,
-               teamName: Y,
-               agentId: N.agentId,
-               agentName: N.agentName,
-             },
-           }
-         );
-       let T = kM1(V.text);
-       if (T && T.requestId === X)
-         return (
-           I(`[RequestJoin] Join rejected by team ${Y}: ${T.reason}`),
-           LM1(Y, J),
-           {
-             data: {
-               success: !1,
-               message: `Join request rejected: ${T.reason || "No reason provided"}`,
-               status: "rejected",
-               requestId: X,
-               teamName: Y,
-             },
-           }
-         );
-     }
-     await new Promise((V) => setTimeout(V, P));
-   }
-   return (
-     LM1(Y, J),
-     {
-       data: {
-         success: !1,
-         message: `Join request timed out after ${W / 1000} seconds. The team leader may be busy or unavailable.`,
-         status: "timeout",
-         requestId: X,
-         teamName: Y,
-       },
-     }
-   );
- }

--- Removed bXY (pretty-v2.1.31.js:368142-368244)
- async function bXY(A, q) {
-   let K = await q.getAppState(),
-     { target_agent_id: Y, request_id: z, assigned_name: w } = A;
-   if (!Y || !z)
-     throw Error(
-       "target_agent_id and request_id are required for approveJoin operation",
-     );
-   if (!qX(K.teamContext))
-     return {
-       data: {
-         success: !1,
-         message:
-           "Only the team leader can approve join requests. Use spawn to create teammates.",
-         member_name: "",
-         member_agent_id: "",
-       },
-     };
-   let H = K.teamContext?.teamName;
-   if (!H)
-     return {
-       data: {
-         success: !1,
-         message: "Not currently in a team context",
-         member_name: "",
-         member_agent_id: "",
-       },
-     };
-   let O = sH(H);
-   if (!O)
-     return {
-       data: {
-         success: !1,
-         message: `Team "${H}" config not found`,
-         member_name: "",
-         member_agent_id: "",
-       },
-     };
-   let $ = z.match(/@([^@]+)$/);
-   if (!$ || !$[1])
-     return {
-       data: {
-         success: !1,
-         message: `Invalid request_id format: ${z}`,
-         member_name: "",
-         member_agent_id: "",
-       },
-     };
-   let _ = $[1],
-     J = w || Y;
-   if (O.members.find((P) => P.name === J)) {
-     let P = N06({
-       requestId: z,
-       reason: `Name "${J}" is already in use. Please request with a different name.`,
-     });
-     return (
-       $m1(H, _, { from: Tz, text: F1(P), timestamp: new Date().toISOString() }),
-       I(`[ApproveJoin] Rejected join request - name "${J}" already in use`),
-       {
-         data: {
-           success: !1,
-           message: `Name "${J}" is already in use. Rejection sent to joiner.`,
-           member_name: "",
-           member_agent_id: "",
-         },
-       }
-     );
-   }
-   let D = bV(J, H),
-     j = fB(D);
-   (O.members.push({
-     agentId: D,
-     name: J,
-     color: j,
-     joinedAt: Date.now(),
-     tmuxPaneId: "",
-     cwd: "",
-     subscriptions: [],
-   }),
-     TB(H, O));
-   let M = NB(XNA(), bm1(H), "config.json"),
-     W = ofA({
-       requestId: z,
-       teamName: H,
-       teamFilePath: M,
-       leadAgentId: O.leadAgentId,
-       agentId: D,
-       agentName: J,
-       color: j,
-       planModeRequired: !1,
-     });
-   return (
-     $m1(H, _, { from: Tz, text: F1(W), timestamp: new Date().toISOString() }),
-     I(`[ApproveJoin] Approved join request for ${J} (${D}) to team ${H}`),
-     {
-       data: {
-         success: !0,
-         message: `Successfully approved ${J} to join the team`,
-         member_name: J,
-         member_agent_id: D,
-       },
-     }
-   );
- }

--- Removed uXY (pretty-v2.1.31.js:368245-368296)
- async function uXY(A, q) {
-   let K = await q.getAppState(),
-     { target_agent_id: Y, request_id: z, reason: w } = A;
-   if (!Y || !z)
-     throw Error(
-       "target_agent_id and request_id are required for rejectJoin operation",
-     );
-   if (!qX(K.teamContext))
-     return {
-       data: {
-         success: !1,
-         message: "Only the team leader can reject join requests",
-         requestId: z,
-       },
-     };
-   let H = K.teamContext?.teamName;
-   if (!H)
-     return {
-       data: {
-         success: !1,
-         message: "Not currently in a team context",
-         requestId: z,
-       },
-     };
-   let O = z.match(/@([^@]+)$/);
-   if (!O || !O[1])
-     return {
-       data: {
-         success: !1,
-         message: `Invalid request_id format: ${z}`,
-         requestId: z,
-       },
-     };
-   let $ = O[1],
-     _ = N06({
-       requestId: z,
-       reason: w || "Join request was rejected by the team leader",
-     });
-   return (
-     $m1(H, $, { from: Tz, text: F1(_), timestamp: new Date().toISOString() }),
-     I(
-       `[RejectJoin] Rejected join request from ${Y}: ${w || "no reason given"}`,
-     ),
-     {
-       data: {
-         success: !0,
-         message: `Successfully rejected join request from ${Y}`,
-         requestId: z,
-       },
-     }
-   );
- }

--- Removed BXY (pretty-v2.1.31.js:368297-368334)
- async function BXY(A, q) {
-   let K = XNA();
-   if (!WD6(K))
-     return {
-       data: {
-         success: !0,
-         teams: [],
-         message: "No teams directory found. No teams available to join.",
-       },
-     };
-   let z = (await q.getAppState()).teamContext?.teamName,
-     w = NXY(K, { withFileTypes: !0 })
-       .filter((O) => O.isDirectory())
-       .map((O) => O.name),
-     H = [];
-   for (let O of w) {
-     let $ = sH(O);
-     if (!$) continue;
-     if (z && bm1(z) === O) continue;
-     H.push({
-       name: $.name,
-       description: $.description,
-       leadAgentId: $.leadAgentId,
-       memberCount: $.members.length,
-       createdAt: $.createdAt,
-     });
-   }
-   return {
-     data: {
-       success: !0,
-       teams: H,
-       message:
-         H.length > 0
-           ? `Found ${H.length} team(s) available to join`
-           : "No teams available to join",
-     },
-   };
- }

--- Removed dMY (pretty-v2.1.31.js:387299-387352)
- function dMY(A) {
-   let q = t(7),
-     { request: K } = A,
-     Y;
-   if (q[0] !== K.proposedName)
-     ((Y = q9.createElement(
-       h,
-       { marginBottom: 1 },
-       q9.createElement(
-         Z,
-         { color: "cyan_FOR_SUBAGENTS_ONLY", bold: !0 },
-         "Join Request from ",
-         K.proposedName,
-       ),
-     )),
-       (q[0] = K.proposedName),
-       (q[1] = Y));
-   else Y = q[1];
-   let z;
-   if (q[2] !== K.capabilities)
-     ((z =
-       K.capabilities &&
-       q9.createElement(
-         h,
-         null,
-         q9.createElement(Z, null, "Capabilities: ", K.capabilities),
-       )),
-       (q[2] = K.capabilities),
-       (q[3] = z));
-   else z = q[3];
-   let w;
-   if (q[4] !== Y || q[5] !== z)
-     ((w = q9.createElement(
-       h,
-       { flexDirection: "column", marginY: 1 },
-       q9.createElement(
-         h,
-         {
-           borderStyle: "round",
-           borderColor: "cyan_FOR_SUBAGENTS_ONLY",
-           flexDirection: "column",
-           paddingX: 1,
-           paddingY: 1,
-         },
-         Y,
-         z,
-       ),
-     )),
-       (q[4] = Y),
-       (q[5] = z),
-       (q[6] = w));
-   else w = q[6];
-   return w;
- }

--- Removed cMY (pretty-v2.1.31.js:387353-387401)
- function cMY(A) {
-   let q = t(7),
-     { response: K } = A,
-     Y;
-   if (q[0] !== K.teamName)
-     ((Y = q9.createElement(
-       Z,
-       { color: "success", bold: !0 },
-       "Join Approved - Welcome to ",
-       K.teamName,
-       "!",
-     )),
-       (q[0] = K.teamName),
-       (q[1] = Y));
-   else Y = q[1];
-   let z;
-   if (q[2] !== K.agentName)
-     ((z = q9.createElement(
-       h,
-       { marginTop: 1 },
-       q9.createElement(Z, null, "You are now ", K.agentName, " in the team."),
-     )),
-       (q[2] = K.agentName),
-       (q[3] = z));
-   else z = q[3];
-   let w;
-   if (q[4] !== Y || q[5] !== z)
-     ((w = q9.createElement(
-       h,
-       { flexDirection: "column", marginY: 1 },
-       q9.createElement(
-         h,
-         {
-           borderStyle: "round",
-           borderColor: "success",
-           flexDirection: "column",
-           paddingX: 1,
-           paddingY: 1,
-         },
-         Y,
-         z,
-       ),
-     )),
-       (q[4] = Y),
-       (q[5] = z),
-       (q[6] = w));
-   else w = q[6];
-   return w;
- }

--- Removed lMY (pretty-v2.1.31.js:387402-387455)
- function lMY(A) {
-   let q = t(5),
-     { response: K } = A,
-     Y;
-   if (q[0] === Symbol.for("react.memo_cache_sentinel"))
-     ((Y = q9.createElement(
-       Z,
-       { color: "error", bold: !0 },
-       "Join Request Rejected",
-     )),
-       (q[0] = Y));
-   else Y = q[0];
-   let z;
-   if (q[1] !== K.reason)
-     ((z =
-       K.reason &&
-       q9.createElement(
-         h,
-         {
-           marginTop: 1,
-           borderStyle: "dashed",
-           borderColor: "subtle",
-           borderLeft: !1,
-           borderRight: !1,
-           paddingX: 1,
-         },
-         q9.createElement(Z, null, "Reason: ", K.reason),
-       )),
-       (q[1] = K.reason),
-       (q[2] = z));
-   else z = q[2];
-   let w;
-   if (q[3] !== z)
-     ((w = q9.createElement(
-       h,
-       { flexDirection: "column", marginY: 1 },
-       q9.createElement(
-         h,
-         {
-           borderStyle: "round",
-           borderColor: "error",
-           flexDirection: "column",
-           paddingX: 1,
-           paddingY: 1,
-         },
-         Y,
-         z,
-       ),
-     )),
-       (q[3] = z),
-       (q[4] = w));
-   else w = q[4];
-   return w;
- }

--- Removed OI4 (pretty-v2.1.31.js:387456-387464)
- function OI4(A) {
-   let q = T06(A);
-   if (q) return q9.createElement(dMY, { request: q });
-   let K = EM1(A);
-   if (K) return q9.createElement(cMY, { response: K });
-   let Y = kM1(A);
-   if (Y) return q9.createElement(lMY, { response: Y });
-   return null;
- }

--- Removed $I4 (pretty-v2.1.31.js:387465-387476)
- function $I4(A) {
-   let q = T06(A);
-   if (q) {
-     let z = q.capabilities ? ` - ${q.capabilities}` : "";
-     return `[Join Request] ${q.proposedName} wants to join${z}`;
-   }
-   let K = EM1(A);
-   if (K) return `[Join Approved] You are now ${K.agentName} in ${K.teamName}`;
-   let Y = kM1(A);
-   if (Y) return `[Join Rejected] ${Y.reason || "Request was rejected"}`;
-   return null;
- }

--- Removed DI4 (pretty-v2.1.31.js:387837-387883)
- function DI4(A) {
-   let q = t(14),
-     { addMargin: K, param: Y } = A,
-     { text: z } = Y,
-     w,
-     H,
-     O,
-     $,
-     _,
-     J;
-   if (q[0] !== K || q[1] !== z) {
-     J = Symbol.for("react.early_return_sentinel");
-     A: {
-       let D = sMY(z);
-       if (D.length === 0) {
-         J = null;
-         break A;
-       }
-       ((w = h),
-         (H = "column"),
-         (O = K ? 1 : 0),
-         ($ = "100%"),
-         (_ = D.map(eMY)));
-     }
-     ((q[0] = K),
-       (q[1] = z),
-       (q[2] = w),
-       (q[3] = H),
-       (q[4] = O),
-       (q[5] = $),
-       (q[6] = _),
-       (q[7] = J));
-   } else
-     ((w = q[2]), (H = q[3]), (O = q[4]), ($ = q[5]), (_ = q[6]), (J = q[7]));
-   if (J !== Symbol.for("react.early_return_sentinel")) return J;
-   let X;
-   if (q[8] !== w || q[9] !== H || q[10] !== O || q[11] !== $ || q[12] !== _)
-     ((X = p3.createElement(w, { flexDirection: H, marginTop: O, width: $ }, _)),
-       (q[8] = w),
-       (q[9] = H),
-       (q[10] = O),
-       (q[11] = $),
-       (q[12] = _),
-       (q[13] = X));
-   else X = q[13];
-   return X;
- }

--- Removed IU4 (pretty-v2.1.31.js:419376-419529)
- var IU4 = E(() => {
-   ((jEY = `Use this tool proactively when you're about to start a non-trivial implementation task. Getting user sign-off on your approach before writing code prevents wasted effort and ensures alignment. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
- 
- ## When to Use This Tool
- 
- **Prefer using EnterPlanMode** for implementation tasks unless they're simple. Use it when ANY of these conditions apply:
- 
- 1. **New Feature Implementation**: Adding meaningful new functionality
-    - Example: "Add a logout button" - where should it go? What should happen on click?
-    - Example: "Add form validation" - what rules? What error messages?
- 
- 2. **Multiple Valid Approaches**: The task can be solved in several different ways
-    - Example: "Add caching to the API" - could use Redis, in-memory, file-based, etc.
-    - Example: "Improve performance" - many optimization strategies possible
- 
- 3. **Code Modifications**: Changes that affect existing behavior or structure
-    - Example: "Update the login flow" - what exactly should change?
-    - Example: "Refactor this component" - what's the target architecture?
- 
- 4. **Architectural Decisions**: The task requires choosing between patterns or technologies
-    - Example: "Add real-time updates" - WebSockets vs SSE vs polling
-    - Example: "Implement state management" - Redux vs Context vs custom solution
- 
- 5. **Multi-File Changes**: The task will likely touch more than 2-3 files
-    - Example: "Refactor the authentication system"
-    - Example: "Add a new API endpoint with tests"
- 
- 6. **Unclear Requirements**: You need to explore before understanding the full scope
-    - Example: "Make the app faster" - need to profile and identify bottlenecks
-    - Example: "Fix the bug in checkout" - need to investigate root cause
- 
- 7. **User Preferences Matter**: The implementation could reasonably go multiple ways
-    - If you would use ${Rw} to clarify the approach, use EnterPlanMode instead
-    - Plan mode lets you explore first, then present options with context
- 
- ## When NOT to Use This Tool
- 
- Only skip EnterPlanMode for simple tasks:
- - Single-line or few-line fixes (typos, obvious bugs, small tweaks)
- - Adding a single function with clear requirements
- - Tasks where the user has given very specific, detailed instructions
- - Pure research/exploration tasks (use the Task tool with explore agent instead)
- 
- ## What Happens in Plan Mode
- 
- In plan mode, you'll:
- 1. Thoroughly explore the codebase using Glob, Grep, and Read tools
- 2. Understand existing patterns and architecture
- 3. Design an implementation approach
- 4. Present your plan to the user for approval
- 5. Use ${Rw} if you need to clarify approaches
- 6. Exit plan mode with ExitPlanMode when ready to implement
- 
- ## Examples
- 
- ### GOOD - Use EnterPlanMode:
- User: "Add user authentication to the app"
- - Requires architectural decisions (session vs JWT, where to store tokens, middleware structure)
- 
- User: "Optimize the database queries"
- - Multiple approaches possible, need to profile first, significant impact
- 
- User: "Implement dark mode"
- - Architectural decision on theme system, affects many components
- 
- User: "Add a delete button to the user profile"
- - Seems simple but involves: where to place it, confirmation dialog, API call, error handling, state updates
- 
- User: "Update the error handling in the API"
- - Affects multiple files, user should approve the approach
- 
- ### BAD - Don't use EnterPlanMode:
- User: "Fix the typo in the README"
- - Straightforward, no planning needed
- 
- User: "Add a console.log to debug this function"
- - Simple, obvious implementation
- 
- User: "What files handle routing?"
- - Research task, not implementation planning
- 
- ## Important Notes
- 
- - This tool REQUIRES user approval - they must consent to entering plan mode
- - If unsure whether to use it, err on the side of planning - it's better to get alignment upfront than to redo work
- - Users appreciate being consulted before significant changes are made to their codebase
- `),
-     (H8H = `Use this tool when a task has genuine ambiguity about the right approach and getting user input before coding would prevent significant rework. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
- 
- ## When to Use This Tool
- 
- Plan mode is valuable when the implementation approach is genuinely unclear. Use it when:
- 
- 1. **Significant Architectural Ambiguity**: Multiple reasonable approaches exist and the choice meaningfully affects the codebase
-    - Example: "Add caching to the API" - Redis vs in-memory vs file-based
-    - Example: "Add real-time updates" - WebSockets vs SSE vs polling
- 
- 2. **Unclear Requirements**: You need to explore and clarify before you can make progress
-    - Example: "Make the app faster" - need to profile and identify bottlenecks
-    - Example: "Refactor this module" - need to understand what the target architecture should be
- 
- 3. **High-Impact Restructuring**: The task will significantly restructure existing code and getting buy-in first reduces risk
-    - Example: "Redesign the authentication system"
-    - Example: "Migrate from one state management approach to another"
- 
- ## When NOT to Use This Tool
- 
- Skip plan mode when you can reasonably infer the right approach:
- - The task is straightforward even if it touches multiple files
- - The user's request is specific enough that the implementation path is clear
- - You're adding a feature with an obvious implementation pattern (e.g., adding a button, a new endpoint following existing conventions)
- - Bug fixes where the fix is clear once you understand the bug
- - Research/exploration tasks (use the Task tool with explore agent instead)
- - The user says something like "can we work on X" or "let's do X" — just get started
- 
- When in doubt, prefer starting work and using ${Rw} for specific questions over entering a full planning phase.
- 
- ## What Happens in Plan Mode
- 
- In plan mode, you'll:
- 1. Explore the codebase using Glob, Grep, and Read tools
- 2. Understand existing patterns and architecture
- 3. Design an implementation approach
- 4. Present your plan to the user for approval
- 5. Use ${Rw} if you need to clarify approaches
- 6. Exit plan mode with ExitPlanMode when ready to implement
- 
- ## Examples
- 
- ### GOOD - Use EnterPlanMode:
- User: "Add user authentication to the app"
- - Genuinely ambiguous: session vs JWT, where to store tokens, middleware structure
- 
- User: "Redesign the data pipeline"
- - Major restructuring where the wrong approach wastes significant effort
- 
- ### BAD - Don't use EnterPlanMode:
- User: "Add a delete button to the user profile"
- - Implementation path is clear; just do it
- 
- User: "Can we work on the search feature?"
- - User wants to get started, not plan
- 
- User: "Update the error handling in the API"
- - Start working; ask specific questions if needed
- 
- User: "Fix the typo in the README"
- - Straightforward, no planning needed
- 
- ## Important Notes
- 
- - This tool REQUIRES user approval - they must consent to entering plan mode
- `));
- });

--- Removed yp4 (pretty-v2.1.31.js:420835-420836)
- var yp4 =
-   "Send messages to teammates and handle protocol requests (shutdown, plan approval)";

--- Removed Ho4 (pretty-v2.1.31.js:442881-442883)
- function Ho4(A) {
-   return A.find((q) => q.name === OJ);
- }

--- Removed jo4 (pretty-v2.1.31.js:443333-443335)
- function jo4(A) {
-   return A.some((q) => q.name === HM);
- }

--- Removed gg1 (pretty-v2.1.31.js:459646-459656)
- function gg1(A) {
-   let q = A.toLowerCase();
-   return ![
-     "3-5-haiku",
-     "haiku-4-5",
-     "3-5-sonnet",
-     "3-7-sonnet",
-     "sonnet-4",
-     "opus-4-1",
-   ].some((Y) => q.includes(Y));
- }

--- Removed y1q (pretty-v2.1.31.js:463040-463120)
- function y1q(A) {
-   let q = t(13),
-     { categories: K, stats: Y, onSelect: z } = A,
-     [w, H] = R1q.useState(0),
-     O;
-   if (q[0] !== K || q[1] !== w || q[2] !== z)
-     ((O = (J, X) => {
-       let D = en(J);
-       if (X.upArrow || J === "k") H((j) => (j > 0 ? j - 1 : K.length - 1));
-       else if (X.downArrow || J === "j")
-         H((j) => (j < K.length - 1 ? j + 1 : 0));
-       else if (X.return) {
-         let j = K[w];
-         if (j) z(j.id);
-       } else if (D >= "1" && D <= "9") {
-         let j = parseInt(D, 10) - 1;
-         if (j < K.length) {
-           H(j);
-           let M = K[j];
-           if (M) z(M.id);
-         }
-       }
-     }),
-       (q[0] = K),
-       (q[1] = w),
-       (q[2] = z),
-       (q[3] = O));
-   else O = q[3];
-   eA(O);
-   let $;
-   if (q[4] !== K || q[5] !== w || q[6] !== Y) {
-     let J;
-     if (q[8] !== w || q[9] !== Y)
-       ((J = (X, D) => {
-         let j = D === w,
-           M = Y?.[X.id],
-           W = M?.explored ?? 0,
-           P = M?.total ?? 0,
-           G,
-           f;
-         if (W === 0) ((G = d1.circle), (f = "inactive"));
-         else if (W === P) ((G = d1.tick), (f = "success"));
-         else ((G = d1.circleFilled), (f = "warning"));
-         let V = j ? "suggestion" : void 0;
-         return Nt.default.createElement(
-           h,
-           { key: X.id, gap: 1 },
-           Nt.default.createElement(Z, { color: V }, j ? d1.pointer : " "),
-           Nt.default.createElement(Z, { color: f }, G),
-           Nt.default.createElement(
-             h,
-             { width: 24 },
-             Nt.default.createElement(Z, { color: V, bold: j }, X.name),
-           ),
-           Nt.default.createElement(
-             Z,
-             { dimColor: !0 },
-             "[",
-             W,
-             "/",
-             P,
-             " ",
-             W === P ? "completed" : W === 0 ? "unexplored" : "explored",
-             "]",
-           ),
-         );
-       }),
-         (q[8] = w),
-         (q[9] = Y),
-         (q[10] = J));
-     else J = q[10];
-     (($ = K.map(J)), (q[4] = K), (q[5] = w), (q[6] = Y), (q[7] = $));
-   } else $ = q[7];
-   let _;
-   if (q[11] !== $)
-     ((_ = Nt.default.createElement(h, { flexDirection: "column" }, $)),
-       (q[11] = $),
-       (q[12] = _));
-   else _ = q[12];
-   return _;
- }

--- Removed S1q (pretty-v2.1.31.js:463128-463201)
- function S1q(A) {
-   let q = t(22),
-     { feature: K, isUsed: Y, isFocused: z } = A,
-     w = Y ? d1.tick : d1.circle,
-     H = Y ? "success" : "inactive",
-     O = z ? "suggestion" : void 0,
-     $ = z ? d1.pointer : " ",
-     _;
-   if (q[0] !== O || q[1] !== $)
-     ((_ = fd.default.createElement(Z, { color: O }, $)),
-       (q[0] = O),
-       (q[1] = $),
-       (q[2] = _));
-   else _ = q[2];
-   let J;
-   if (q[3] !== H || q[4] !== w)
-     ((J = fd.default.createElement(Z, { color: H }, w)),
-       (q[3] = H),
-       (q[4] = w),
-       (q[5] = J));
-   else J = q[5];
-   let X;
-   if (q[6] !== K.name || q[7] !== O || q[8] !== z)
-     ((X = fd.default.createElement(Z, { color: O, bold: z }, K.name)),
-       (q[6] = K.name),
-       (q[7] = O),
-       (q[8] = z),
-       (q[9] = X));
-   else X = q[9];
-   let D;
-   if (q[10] !== _ || q[11] !== J || q[12] !== X)
-     ((D = fd.default.createElement(h, { gap: 1 }, _, J, X)),
-       (q[10] = _),
-       (q[11] = J),
-       (q[12] = X),
-       (q[13] = D));
-   else D = q[13];
-   let j;
-   if (
-     q[14] !== K.description ||
-     q[15] !== K.tryItPrompt ||
-     q[16] !== z ||
-     q[17] !== Y
-   )
-     ((j =
-       z &&
-       fd.default.createElement(
-         h,
-         { flexDirection: "column", marginLeft: 4 },
-         fd.default.createElement(Z, { dimColor: !0 }, K.description),
-         !Y &&
-           K.tryItPrompt &&
-           fd.default.createElement(
-             Z,
-             { color: "warning", dimColor: !0 },
-             "Try it: ",
-             K.tryItPrompt,
-           ),
-       )),
-       (q[14] = K.description),
-       (q[15] = K.tryItPrompt),
-       (q[16] = z),
-       (q[17] = Y),
-       (q[18] = j));
-   else j = q[18];
-   let M;
-   if (q[19] !== D || q[20] !== j)
-     ((M = fd.default.createElement(h, { flexDirection: "column" }, D, j)),
-       (q[19] = D),
-       (q[20] = j),
-       (q[21] = M));
-   else M = q[21];
-   return M;
- }

--- Removed I1q (pretty-v2.1.31.js:463209-463387)
- function I1q(A) {
-   let q = t(39),
-     { categoryId: K, onBack: Y, onClose: z } = A,
-     [w, H] = ig1.useState(0),
-     O;
-   if (q[0] === Symbol.for("react.memo_cache_sentinel")) ((O = {}), (q[0] = O));
-   else O = q[0];
-   let [$, _] = ig1.useState(O),
-     J = v7(),
-     X;
-   if (q[1] !== K) ((X = VG7(K)), (q[1] = K), (q[2] = X));
-   else X = q[2];
-   let D = X,
-     j;
-   if (q[3] !== K) ((j = fG7(K)), (q[3] = K), (q[4] = j));
-   else j = q[4];
-   let M = j,
-     W,
-     P;
-   if (q[5] !== M)
-     ((W = () => {
-       Promise.all(M.map(xpY)).then((U) => _(Object.fromEntries(U)));
-     }),
-       (P = [M]),
-       (q[5] = M),
-       (q[6] = W),
-       (q[7] = P));
-   else ((W = q[6]), (P = q[7]));
-   ig1.useEffect(W, P);
-   let G;
-   if (q[8] === Symbol.for("react.memo_cache_sentinel"))
-     ((G = { context: "Confirmation" }), (q[8] = G));
-   else G = q[8];
-   zA("confirm:no", z, G);
-   let f;
-   if (q[9] !== M.length || q[10] !== Y)
-     ((f = (U, g) => {
-       if (g.backspace || g.delete) Y();
-       else if (g.upArrow || U === "k") H((x) => (x > 0 ? x - 1 : M.length - 1));
-       else if (g.downArrow || U === "j")
-         H((x) => (x < M.length - 1 ? x + 1 : 0));
-     }),
-       (q[9] = M.length),
-       (q[10] = Y),
-       (q[11] = f));
-   else f = q[11];
-   if ((eA(f), !D)) {
-     let U;
-     if (q[12] === Symbol.for("react.memo_cache_sentinel"))
-       ((U = qj.default.createElement(
-         Z,
-         { color: "error" },
-         "Category not found",
-       )),
-         (q[12] = U));
-     else U = q[12];
-     return U;
-   }
-   let V;
-   if (q[13] === Symbol.for("react.memo_cache_sentinel"))
-     ((V = qj.default.createElement(Q5, {
-       dividerColor: "suggestion",
-       dividerDimColor: !0,
-     })),
-       (q[13] = V));
-   else V = q[13];
-   let N;
-   if (q[14] !== D.name)
-     ((N = qj.default.createElement(
-       Z,
-       { bold: !0, color: "suggestion" },
-       D.name,
-     )),
-       (q[14] = D.name),
-       (q[15] = N));
-   else N = q[15];
-   let T;
-   if (q[16] !== D.description)
-     ((T = qj.default.createElement(Z, { dimColor: !0 }, D.description)),
-       (q[16] = D.description),
-       (q[17] = T));
-   else T = q[17];
-   let k;
-   if (q[18] !== T || q[19] !== N)
-     ((k = qj.default.createElement(h, { flexDirection: "column" }, N, T)),
-       (q[18] = T),
-       (q[19] = N),
-       (q[20] = k));
-   else k = q[20];
-   let y;
-   if (q[21] !== M || q[22] !== w || q[23] !== $) {
-     let U;
-     if (q[25] !== w || q[26] !== $)
-       ((U = (g, x) =>
-         qj.default.createElement(S1q, {
-           key: g.id,
-           feature: g,
-           isUsed: $[g.id] ?? !1,
-           isFocused: x === w,
-         })),
-         (q[25] = w),
-         (q[26] = $),
-         (q[27] = U));
-     else U = q[27];
-     ((y = M.map(U)), (q[21] = M), (q[22] = w), (q[23] = $), (q[24] = y));
-   } else y = q[24];
-   let B;
-   if (q[28] !== y)
-     ((B = qj.default.createElement(h, { flexDirection: "column" }, y)),
-       (q[28] = y),
-       (q[29] = B));
-   else B = q[29];
-   let C;
-   if (q[30] !== k || q[31] !== B)
-     ((C = qj.default.createElement(
-       h,
-       { flexDirection: "column", paddingX: 1, gap: 1 },
-       k,
-       B,
-     )),
-       (q[30] = k),
-       (q[31] = B),
-       (q[32] = C));
-   else C = q[32];
-   let m;
-   if (q[33] !== J.keyName || q[34] !== J.pending)
-     ((m = qj.default.createElement(
-       h,
-       { paddingX: 1 },
-       qj.default.createElement(
-         Z,
-         { dimColor: !0, italic: !0 },
-         J.pending
-           ? qj.default.createElement(
-               qj.default.Fragment,
-               null,
-               "Press ",
-               J.keyName,
-               " again to exit",
-             )
-           : qj.default.createElement(
-               nA,
-               null,
-               qj.default.createElement(_A, {
-                 shortcut: "↑/↓",
-                 action: "navigate",
-               }),
-               qj.default.createElement(_A, {
-                 shortcut: "Backspace",
-                 action: "back",
-               }),
-               qj.default.createElement(kA, {
-                 action: "confirm:no",
-                 context: "Confirmation",
-                 fallback: "Esc",
-                 description: "close",
-               }),
-             ),
-       ),
-     )),
-       (q[33] = J.keyName),
-       (q[34] = J.pending),
-       (q[35] = m));
-   else m = q[35];
-   let u;
-   if (q[36] !== C || q[37] !== m)
-     ((u = qj.default.createElement(
-       h,
-       { flexDirection: "column", paddingBottom: 1 },
-       V,
-       C,
-       m,
-     )),
-       (q[36] = C),
-       (q[37] = m),
-       (q[38] = u));
-   else u = q[38];
-   return u;
- }

--- Removed xpY (pretty-v2.1.31.js:463388-463390)
- async function xpY(A) {
-   return [A.id, await A.hasBeenUsed()];
- }

--- Removed b1q (pretty-v2.1.31.js:463405-463597)
- function b1q(A) {
-   let q = t(28),
-     { onClose: K } = A,
-     [Y, z] = Uw.useState(null),
-     [w, H] = Uw.useState(null),
-     O = v7(),
-     $;
-   if (q[0] === Symbol.for("react.memo_cache_sentinel"))
-     (($ = () => {
-       TG7().then(H);
-     }),
-       (q[0] = $));
-   else $ = q[0];
-   let _;
-   if (q[1] !== Y) ((_ = [Y]), (q[1] = Y), (q[2] = _));
-   else _ = q[2];
-   Uw.useEffect($, _);
-   let J = !Y,
-     X;
-   if (q[3] !== J)
-     ((X = { context: "Confirmation", isActive: J }), (q[3] = J), (q[4] = X));
-   else X = q[4];
-   if ((zA("confirm:no", K, X), Y)) {
-     let y;
-     if (q[5] === Symbol.for("react.memo_cache_sentinel"))
-       ((y = () => z(null)), (q[5] = y));
-     else y = q[5];
-     let B;
-     if (q[6] !== K || q[7] !== Y)
-       ((B = Uw.default.createElement(I1q, {
-         categoryId: Y,
-         onBack: y,
-         onClose: K,
-       })),
-         (q[6] = K),
-         (q[7] = Y),
-         (q[8] = B));
-     else B = q[8];
-     return B;
-   }
-   let D = w ? w.explored / w.total : 0,
-     j;
-   if (q[9] !== w)
-     ((j = w ? Math.round((w.explored / w.total) * 100) : 0),
-       (q[9] = w),
-       (q[10] = j));
-   else j = q[10];
-   let M = j,
-     W;
-   if (q[11] === Symbol.for("react.memo_cache_sentinel"))
-     ((W = Uw.default.createElement(Q5, {
-       dividerColor: "suggestion",
-       dividerDimColor: !0,
-     })),
-       (q[11] = W));
-   else W = q[11];
-   let P;
-   if (q[12] === Symbol.for("react.memo_cache_sentinel"))
-     ((P = Uw.default.createElement(
-       h,
-       { flexDirection: "column" },
-       Uw.default.createElement(
-         Z,
-         { bold: !0, color: "suggestion" },
-         "Discover Claude Code",
-       ),
-       Uw.default.createElement(
-         Z,
-         { dimColor: !0 },
-         "Explore features and track your progress",
-       ),
-     )),
-       (q[12] = P));
-   else P = q[12];
-   let G;
-   if (q[13] !== M || q[14] !== D || q[15] !== w)
-     ((G =
-       w &&
-       Uw.default.createElement(
-         h,
-         { flexDirection: "column", gap: 0 },
-         Uw.default.createElement(
-           Z,
-           null,
-           "You've explored",
-           " ",
-           Uw.default.createElement(
-             Z,
-             { bold: !0, color: "success" },
-             w.explored,
-           ),
-           " ",
-           "of ",
-           w.total,
-           " features (",
-           M,
-           "%)",
-         ),
-         Uw.default.createElement(
-           h,
-           null,
-           Uw.default.createElement(H51, {
-             ratio: D,
-             width: 40,
-             fillColor: "success",
-             emptyColor: "inactive",
-           }),
-         ),
-       )),
-       (q[13] = M),
-       (q[14] = D),
-       (q[15] = w),
-       (q[16] = G));
-   else G = q[16];
-   let f = w?.byCategory ?? null,
-     V;
-   if (q[17] !== f)
-     ((V = Uw.default.createElement(y1q, {
-       categories: fK6,
-       stats: f,
-       onSelect: z,
-     })),
-       (q[17] = f),
-       (q[18] = V));
-   else V = q[18];
-   let N;
-   if (q[19] !== V || q[20] !== G)
-     ((N = Uw.default.createElement(
-       h,
-       { flexDirection: "column", paddingX: 1, gap: 1 },
-       P,
-       G,
-       V,
-     )),
-       (q[19] = V),
-       (q[20] = G),
-       (q[21] = N));
-   else N = q[21];
-   let T;
-   if (q[22] !== O.keyName || q[23] !== O.pending)
-     ((T = Uw.default.createElement(
-       h,
-       { paddingX: 1 },
-       Uw.default.createElement(
-         Z,
-         { dimColor: !0, italic: !0 },
-         O.pending
-           ? Uw.default.createElement(
-               Uw.default.Fragment,
-               null,
-               "Press ",
-               O.keyName,
-               " again to exit",
-             )
-           : Uw.default.createElement(
-               nA,
-               null,
-               Uw.default.createElement(_A, {
-                 shortcut: "↑/↓",
-                 action: "navigate",
-               }),
-               Uw.default.createElement(_A, {
-                 shortcut: "Enter",
-                 action: "explore",
-               }),
-               Uw.default.createElement(kA, {
-                 action: "confirm:no",
-                 context: "Confirmation",
-                 fallback: "Esc",
-                 description: "close",
-               }),
-             ),
-       ),
-     )),
-       (q[22] = O.keyName),
-       (q[23] = O.pending),
-       (q[24] = T));
-   else T = q[24];
-   let k;
-   if (q[25] !== N || q[26] !== T)
-     ((k = Uw.default.createElement(
-       h,
-       { flexDirection: "column", paddingBottom: 1 },
-       W,
-       N,
-       T,
-     )),
-       (q[25] = N),
-       (q[26] = T),
-       (q[27] = k));
-   else k = q[27];
-   return k;
- }

--- Removed B1q (pretty-v2.1.31.js:463616-463633)
- var B1q = E(() => {
-   u1q();
-   rz();
-   ((cSA = o(J1(), 1)),
-     (AbH = {
-       type: "local-jsx",
-       name: "discover",
-       description: "Explore Claude Code features and track your progress",
-       isEnabled: TK6,
-       isHidden: !TK6(),
-       async call(A) {
-         return cSA.createElement(b1q, { onClose: A });
-       },
-       userFacingName() {
-         return "discover";
-       },
-     }));
- });

--- Removed $Aq (pretty-v2.1.31.js:468456-468640)
- function $Aq(A) {
-   let q = t(18),
-     { onSubmit: K, defaultSelections: Y } = A,
-     z;
-   if (q[0] !== Y) ((z = new Set(Y)), (q[0] = Y), (q[1] = z));
-   else z = q[1];
-   let [w, H] = xZ6.useState(z),
-     [O, $] = xZ6.useState(0),
-     [_, J] = xZ6.useState(!1),
-     X = [
-       {
-         value: "claude",
-         label: "@Claude Code",
-         description: "Tag @claude in issues and PR comments",
-       },
-       {
-         value: "claude-review",
-         label: "Claude Code Review",
-         description: "Automated code review on new PRs",
-       },
-     ];
-   eA((x, d) => {
-     if (d.upArrow) ($((r) => (r > 0 ? r - 1 : X.length - 1)), J(!1));
-     else if (d.downArrow) ($((r) => (r < X.length - 1 ? r + 1 : 0)), J(!1));
-     else if (x === " ") {
-       let r = X[O]?.value;
-       if (r)
-         H((c) => {
-           let q1 = new Set(c);
-           if (q1.has(r)) q1.delete(r);
-           else q1.add(r);
-           return q1;
-         });
-     } else if (d.return)
-       if (w.size === 0) J(!0);
-       else K(Array.from(w));
-   });
-   let D = h,
-     j = "column",
-     M = "round",
-     W = !0,
-     P = 1,
-     G = "100%",
-     f,
-     V;
-   if (q[2] === Symbol.for("react.memo_cache_sentinel"))
-     ((f = qO.default.createElement(
-       Z,
-       { bold: !0 },
-       "Select GitHub workflows to install",
-     )),
-       (V = qO.default.createElement(
-         Z,
-         { dimColor: !0 },
-         "We'll create a workflow file in your repository for each one you select.",
-       )),
-       (q[2] = f),
-       (q[3] = V));
-   else ((f = q[2]), (V = q[3]));
-   let N;
-   if (q[4] === Symbol.for("react.memo_cache_sentinel"))
-     ((N = qO.default.createElement(
-       h,
-       { flexDirection: "column", marginBottom: 1 },
-       f,
-       V,
-       qO.default.createElement(
-         h,
-         { marginTop: 1 },
-         qO.default.createElement(
-           Z,
-           { dimColor: !0 },
-           "More workflow examples (issue triage, CI fixes, etc.) at:",
-           " ",
-           qO.default.createElement(
-             A4,
-             {
-               url: "https://github.com/anthropics/claude-code-action/blob/main/examples/",
-             },
-             "https://github.com/anthropics/claude-code-action/blob/main/examples/",
-           ),
-         ),
-       ),
-     )),
-       (q[4] = N));
-   else N = q[4];
-   let T = h,
-     k = "column",
-     y = 1,
-     B = X.map((x, d) => {
-       let r = w.has(x.value),
-         c = d === O;
-       return qO.default.createElement(
-         h,
-         {
-           key: x.value,
-           flexDirection: "row",
-           marginBottom: d < X.length - 1 ? 1 : 0,
-         },
-         qO.default.createElement(
-           h,
-           { marginRight: 1, minWidth: 2 },
-           qO.default.createElement(Z, { bold: c }, r ? "✓" : " "),
-         ),
-         qO.default.createElement(
-           h,
-           { flexDirection: "column" },
-           qO.default.createElement(Z, { bold: c }, x.label),
-           qO.default.createElement(Z, { dimColor: !0 }, x.description),
-         ),
-       );
-     }),
-     C;
-   if (q[5] !== T || q[6] !== B)
-     ((C = qO.default.createElement(T, { flexDirection: k, paddingX: y }, B)),
-       (q[5] = T),
-       (q[6] = B),
-       (q[7] = C));
-   else C = q[7];
-   let m;
-   if (q[8] !== D || q[9] !== C || q[10] !== N)
-     ((m = qO.default.createElement(
-       D,
-       {
-         flexDirection: j,
-         borderStyle: M,
-         borderDimColor: W,
-         paddingX: P,
-         width: G,
-       },
-       N,
-       C,
-     )),
-       (q[8] = D),
-       (q[9] = C),
-       (q[10] = N),
-       (q[11] = m));
-   else m = q[11];
-   let u;
-   if (q[12] === Symbol.for("react.memo_cache_sentinel"))
-     ((u = qO.default.createElement(
-       h,
-       { marginLeft: 2 },
-       qO.default.createElement(
-         Z,
-         { dimColor: !0 },
-         qO.default.createElement(
-           nA,
-           null,
-           qO.default.createElement(_A, { shortcut: "↑↓", action: "Navigate" }),
-           qO.default.createElement(_A, { shortcut: "Space", action: "toggle" }),
-           qO.default.createElement(_A, {
-             shortcut: "Enter",
-             action: "confirm",
-           }),
-         ),
-       ),
-     )),
-       (q[12] = u));
-   else u = q[12];
-   let U;
-   if (q[13] !== _)
-     ((U =
-       _ &&
-       qO.default.createElement(
-         h,
-         { marginLeft: 1 },
-         qO.default.createElement(
-           Z,
-           { color: "error" },
-           "You must select at least one workflow to continue",
-         ),
-       )),
-       (q[13] = _),
-       (q[14] = U));
-   else U = q[14];
-   let g;
-   if (q[15] !== m || q[16] !== U)
-     ((g = qO.default.createElement(qO.default.Fragment, null, m, u, U)),
-       (q[15] = m),
-       (q[16] = U),
-       (q[17] = g));
-   else g = q[17];
-   return g;
- }

--- Removed vqq (pretty-v2.1.31.js:485529-485563)
- function vqq() {
-   let A = t(4),
-     q = !!kG1(),
-     K;
-   if (A[0] === Symbol.for("react.memo_cache_sentinel"))
-     ((K = Td.createElement(Z, { color: "claude" }, "[✻]")), (A[0] = K));
-   else K = A[0];
-   let Y;
-   if (A[1] === Symbol.for("react.memo_cache_sentinel"))
-     ((Y = Td.createElement(Z, { color: "claude" }, "[✻]")), (A[1] = Y));
-   else Y = A[1];
-   let z;
-   if (A[2] === Symbol.for("react.memo_cache_sentinel"))
-     ((z = Td.createElement(Z, { color: "claude" }, "[✻]")), (A[2] = z));
-   else z = A[2];
-   let w;
-   if (A[3] === Symbol.for("react.memo_cache_sentinel"))
-     ((w = Td.createElement(
-       Z,
-       { dimColor: !0 },
-       K,
-       " ",
-       Y,
-       " ",
-       z,
-       " ·",
-       " ",
-       q
-         ? "Share Claude Code and earn extra usage · /passes"
-         : "3 guest passes at /passes",
-     )),
-       (A[3] = w));
-   else w = A[3];
-   return w;
- }

--- Removed ssY (pretty-v2.1.31.js:492314-492327)
- function ssY() {
-   U4("vim-mode");
-   let q = W6().editorMode || "normal";
-   if (q === "emacs") q = "normal";
-   let K = q === "normal" ? "vim" : "normal";
-   return (
-     XA((Y) => ({ ...Y, editorMode: K })),
-     n("tengu_editor_mode_changed", { mode: K, source: "command" }),
-     Promise.resolve({
-       type: "text",
-       value: `Editor mode set to ${K}. ${K === "vim" ? "Use Escape key to toggle between INSERT and NORMAL modes." : "Using standard (readline) keyboard bindings."}`,
-     })
-   );
- }

--- Removed iAz (pretty-v2.1.31.js:510476-511254)
- function iAz(A, q) {
-   let K = (C) => {
-       if (!C) return "";
-       return C.split(
-         `
- 
- `,
-       ).map((m) => {
-         let u = Z9(m);
-         return (
-           (u = u.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")),
-           (u = u.replace(/^- /gm, "• ")),
-           (u = u.replace(/\n/g, "<br>")),
-           `<p>${u}</p>`
-         );
-       }).join(`
- `);
-     },
-     Y = q.at_a_glance,
-     z = Y
-       ? `
-     <div class="at-a-glance">
-       <div class="glance-title">At a Glance</div>
-       <div class="glance-sections">
-         ${Y.whats_working ? `<div class="glance-section"><strong>What's working:</strong> ${WV6(Y.whats_working)} <a href="#section-wins" class="see-more">Impressive Things You Did →</a></div>` : ""}
-         ${Y.whats_hindering ? `<div class="glance-section"><strong>What's hindering you:</strong> ${WV6(Y.whats_hindering)} <a href="#section-friction" class="see-more">Where Things Go Wrong →</a></div>` : ""}
-         ${Y.quick_wins ? `<div class="glance-section"><strong>Quick wins to try:</strong> ${WV6(Y.quick_wins)} <a href="#section-features" class="see-more">Features to Try →</a></div>` : ""}
-         ${Y.ambitious_workflows ? `<div class="glance-section"><strong>Ambitious workflows:</strong> ${WV6(Y.ambitious_workflows)} <a href="#section-horizon" class="see-more">On the Horizon →</a></div>` : ""}
-       </div>
-     </div>
-     `
-       : "",
-     w = q.project_areas?.areas || [],
-     H =
-       w.length > 0
-         ? `
-     <h2 id="section-work">What You Work On</h2>
-     <div class="project-areas">
-       ${w
-         .map(
-           (C) => `
-         <div class="project-area">
-           <div class="area-header">
-             <span class="area-name">${Z9(C.name)}</span>
-             <span class="area-count">~${C.session_count} sessions</span>
-           </div>
-           <div class="area-desc">${Z9(C.description)}</div>
-         </div>
-       `,
-         )
-         .join("")}
-     </div>
-     `
-         : "",
-     O = q.interaction_style,
-     $ = O?.narrative
-       ? `
-     <h2 id="section-usage">How You Use Claude Code</h2>
-     <div class="narrative">
-       ${K(O.narrative)}
-       ${O.key_pattern ? `<div class="key-insight"><strong>Key pattern:</strong> ${Z9(O.key_pattern)}</div>` : ""}
-     </div>
-     `
-       : "",
-     _ = q.what_works,
-     J =
-       _?.impressive_workflows && _.impressive_workflows.length > 0
-         ? `
-     <h2 id="section-wins">Impressive Things You Did</h2>
-     ${_.intro ? `<p class="section-intro">${Z9(_.intro)}</p>` : ""}
-     <div class="big-wins">
-       ${_.impressive_workflows
-         .map(
-           (C) => `
-         <div class="big-win">
-           <div class="big-win-title">${Z9(C.title || "")}</div>
-           <div class="big-win-desc">${Z9(C.description || "")}</div>
-         </div>
-       `,
-         )
-         .join("")}
-     </div>
-     `
-         : "",
-     X = q.friction_analysis,
-     D =
-       X?.categories && X.categories.length > 0
-         ? `
-     <h2 id="section-friction">Where Things Go Wrong</h2>
-     ${X.intro ? `<p class="section-intro">${Z9(X.intro)}</p>` : ""}
-     <div class="friction-categories">
-       ${X.categories
-         .map(
-           (C) => `
-         <div class="friction-category">
-           <div class="friction-title">${Z9(C.category || "")}</div>
-           <div class="friction-desc">${Z9(C.description || "")}</div>
-           ${C.examples ? `<ul class="friction-examples">${C.examples.map((m) => `<li>${Z9(m)}</li>`).join("")}</ul>` : ""}
-         </div>
-       `,
-         )
-         .join("")}
-     </div>
-     `
-         : "",
-     j = q.suggestions,
-     M = j
-       ? `
-     ${
-       j.claude_md_additions && j.claude_md_additions.length > 0
-         ? `
-     <h2 id="section-features">Existing CC Features to Try</h2>
-     <div class="claude-md-section">
-       <h3>Suggested CLAUDE.md Additions</h3>
-       <p style="font-size: 12px; color: #64748b; margin-bottom: 12px;">Just copy this into Claude Code to add it to your CLAUDE.md.</p>
-       <div class="claude-md-actions">
-         <button class="copy-all-btn" onclick="copyAllCheckedClaudeMd()">Copy All Checked</button>
-       </div>
-       ${j.claude_md_additions
-         .map(
-           (C, m) => `
-         <div class="claude-md-item">
-           <input type="checkbox" id="cmd-${m}" class="cmd-checkbox" checked data-text="${Z9(C.prompt_scaffold || C.where || "Add to CLAUDE.md")}\\n\\n${Z9(C.addition)}">
-           <label for="cmd-${m}">
-             <code class="cmd-code">${Z9(C.addition)}</code>
-             <button class="copy-btn" onclick="copyCmdItem(${m})">Copy</button>
-           </label>
-           <div class="cmd-why">${Z9(C.why)}</div>
-         </div>
-       `,
-         )
-         .join("")}
-     </div>
-     `
-         : ""
-     }
-     ${
-       j.features_to_try && j.features_to_try.length > 0
-         ? `
-     <p style="font-size: 13px; color: #64748b; margin-bottom: 12px;">Just copy this into Claude Code and it'll set it up for you.</p>
-     <div class="features-section">
-       ${j.features_to_try
-         .map(
-           (C) => `
-         <div class="feature-card">
-           <div class="feature-title">${Z9(C.feature || "")}</div>
-           <div class="feature-oneliner">${Z9(C.one_liner || "")}</div>
-           <div class="feature-why"><strong>Why for you:</strong> ${Z9(C.why_for_you || "")}</div>
-           ${
-             C.example_code
-               ? `
-           <div class="feature-examples">
-             <div class="feature-example">
-               <div class="example-code-row">
-                 <code class="example-code">${Z9(C.example_code)}</code>
-                 <button class="copy-btn" onclick="copyText(this)">Copy</button>
-               </div>
-             </div>
-           </div>
-           `
-               : ""
-           }
-         </div>
-       `,
-         )
-         .join("")}
-     </div>
-     `
-         : ""
-     }
-     ${
-       j.usage_patterns && j.usage_patterns.length > 0
-         ? `
-     <h2 id="section-patterns">New Ways to Use Claude Code</h2>
-     <p style="font-size: 13px; color: #64748b; margin-bottom: 12px;">Just copy this into Claude Code and it'll walk you through it.</p>
-     <div class="patterns-section">
-       ${j.usage_patterns
-         .map(
-           (C) => `
-         <div class="pattern-card">
-           <div class="pattern-title">${Z9(C.title || "")}</div>
-           <div class="pattern-summary">${Z9(C.suggestion || "")}</div>
-           ${C.detail ? `<div class="pattern-detail">${Z9(C.detail)}</div>` : ""}
-           ${
-             C.copyable_prompt
-               ? `
-           <div class="copyable-prompt-section">
-             <div class="prompt-label">Paste into Claude Code:</div>
-             <div class="copyable-prompt-row">
-               <code class="copyable-prompt">${Z9(C.copyable_prompt)}</code>
-               <button class="copy-btn" onclick="copyText(this)">Copy</button>
-             </div>
-           </div>
-           `
-               : ""
-           }
-         </div>
-       `,
-         )
-         .join("")}
-     </div>
-     `
-         : ""
-     }
-     `
-       : "",
-     W = q.on_the_horizon,
-     P =
-       W?.opportunities && W.opportunities.length > 0
-         ? `
-     <h2 id="section-horizon">On the Horizon</h2>
-     ${W.intro ? `<p class="section-intro">${Z9(W.intro)}</p>` : ""}
-     <div class="horizon-section">
-       ${W.opportunities
-         .map(
-           (C) => `
-         <div class="horizon-card">
-           <div class="horizon-title">${Z9(C.title || "")}</div>
-           <div class="horizon-possible">${Z9(C.whats_possible || "")}</div>
-           ${C.how_to_try ? `<div class="horizon-tip"><strong>Getting started:</strong> ${Z9(C.how_to_try)}</div>` : ""}
-           ${C.copyable_prompt ? `<div class="pattern-prompt"><div class="prompt-label">Paste into Claude Code:</div><code>${Z9(C.copyable_prompt)}</code><button class="copy-btn" onclick="copyText(this)">Copy</button></div>` : ""}
-         </div>
-       `,
-         )
-         .join("")}
-     </div>
-     `
-         : "",
-     G = [],
-     f = [],
-     V =
-       G.length > 0 || f.length > 0
-         ? `
-     <h2 id="section-feedback" class="feedback-header">Closing the Loop: Feedback for Other Teams</h2>
-     <p class="feedback-intro">Suggestions for the CC product and model teams based on your usage patterns. Click to expand.</p>
-     ${
-       G.length > 0
-         ? `
-     <div class="collapsible-section">
-       <div class="collapsible-header" onclick="toggleCollapsible(this)">
-         <span class="collapsible-arrow">▶</span>
-         <h3>Product Improvements for CC Team</h3>
-       </div>
-       <div class="collapsible-content">
-         <div class="suggestions-section">
-           ${G.map(
-             (C) => `
-             <div class="feedback-card team-card">
-               <div class="feedback-title">${Z9(C.title || "")}</div>
-               <div class="feedback-detail">${Z9(C.detail || "")}</div>
-               ${C.evidence ? `<div class="feedback-evidence"><em>Evidence:</em> ${Z9(C.evidence)}</div>` : ""}
-             </div>
-           `,
-           ).join("")}
-         </div>
-       </div>
-     </div>
-     `
-         : ""
-     }
-     ${
-       f.length > 0
-         ? `
-     <div class="collapsible-section">
-       <div class="collapsible-header" onclick="toggleCollapsible(this)">
-         <span class="collapsible-arrow">▶</span>
-         <h3>Model Behavior Improvements</h3>
-       </div>
-       <div class="collapsible-content">
-         <div class="suggestions-section">
-           ${f
-             .map(
-               (C) => `
-             <div class="feedback-card model-card">
-               <div class="feedback-title">${Z9(C.title || "")}</div>
-               <div class="feedback-detail">${Z9(C.detail || "")}</div>
-               ${C.evidence ? `<div class="feedback-evidence"><em>Evidence:</em> ${Z9(C.evidence)}</div>` : ""}
-             </div>
-           `,
-             )
-             .join("")}
-         </div>
-       </div>
-     </div>
-     `
-         : ""
-     }
-     `
-         : "",
-     N = q.fun_ending,
-     T = N?.headline
-       ? `
-     <div class="fun-ending">
-       <div class="fun-headline">"${Z9(N.headline)}"</div>
-       ${N.detail ? `<div class="fun-detail">${Z9(N.detail)}</div>` : ""}
-     </div>
-     `
-       : "",
-     k = `
-     * { box-sizing: border-box; margin: 0; padding: 0; }
-     body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; background: #f8fafc; color: #334155; line-height: 1.65; padding: 48px 24px; }
-     .container { max-width: 800px; margin: 0 auto; }
-     h1 { font-size: 32px; font-weight: 700; color: #0f172a; margin-bottom: 8px; }
-     h2 { font-size: 20px; font-weight: 600; color: #0f172a; margin-top: 48px; margin-bottom: 16px; }
-     .subtitle { color: #64748b; font-size: 15px; margin-bottom: 32px; }
-     .nav-toc { display: flex; flex-wrap: wrap; gap: 8px; margin: 24px 0 32px 0; padding: 16px; background: white; border-radius: 8px; border: 1px solid #e2e8f0; }
-     .nav-toc a { font-size: 12px; color: #64748b; text-decoration: none; padding: 6px 12px; border-radius: 6px; background: #f1f5f9; transition: all 0.15s; }
-     .nav-toc a:hover { background: #e2e8f0; color: #334155; }
-     .stats-row { display: flex; gap: 24px; margin-bottom: 40px; padding: 20px 0; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0; flex-wrap: wrap; }
-     .stat { text-align: center; }
-     .stat-value { font-size: 24px; font-weight: 700; color: #0f172a; }
-     .stat-label { font-size: 11px; color: #64748b; text-transform: uppercase; }
-     .at-a-glance { background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border: 1px solid #f59e0b; border-radius: 12px; padding: 20px 24px; margin-bottom: 32px; }
-     .glance-title { font-size: 16px; font-weight: 700; color: #92400e; margin-bottom: 16px; }
-     .glance-sections { display: flex; flex-direction: column; gap: 12px; }
-     .glance-section { font-size: 14px; color: #78350f; line-height: 1.6; }
-     .glance-section strong { color: #92400e; }
-     .see-more { color: #b45309; text-decoration: none; font-size: 13px; white-space: nowrap; }
-     .see-more:hover { text-decoration: underline; }
-     .project-areas { display: flex; flex-direction: column; gap: 12px; margin-bottom: 32px; }
-     .project-area { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; }
-     .area-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
-     .area-name { font-weight: 600; font-size: 15px; color: #0f172a; }
-     .area-count { font-size: 12px; color: #64748b; background: #f1f5f9; padding: 2px 8px; border-radius: 4px; }
-     .area-desc { font-size: 14px; color: #475569; line-height: 1.5; }
-     .narrative { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin-bottom: 24px; }
-     .narrative p { margin-bottom: 12px; font-size: 14px; color: #475569; line-height: 1.7; }
-     .key-insight { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 12px 16px; margin-top: 12px; font-size: 14px; color: #166534; }
-     .section-intro { font-size: 14px; color: #64748b; margin-bottom: 16px; }
-     .big-wins { display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px; }
-     .big-win { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 16px; }
-     .big-win-title { font-weight: 600; font-size: 15px; color: #166534; margin-bottom: 8px; }
-     .big-win-desc { font-size: 14px; color: #15803d; line-height: 1.5; }
-     .friction-categories { display: flex; flex-direction: column; gap: 16px; margin-bottom: 24px; }
-     .friction-category { background: #fef2f2; border: 1px solid #fca5a5; border-radius: 8px; padding: 16px; }
-     .friction-title { font-weight: 600; font-size: 15px; color: #991b1b; margin-bottom: 6px; }
-     .friction-desc { font-size: 13px; color: #7f1d1d; margin-bottom: 10px; }
-     .friction-examples { margin: 0 0 0 20px; font-size: 13px; color: #334155; }
-     .friction-examples li { margin-bottom: 4px; }
-     .claude-md-section { background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 16px; margin-bottom: 20px; }
-     .claude-md-section h3 { font-size: 14px; font-weight: 600; color: #1e40af; margin: 0 0 12px 0; }
-     .claude-md-actions { margin-bottom: 12px; padding-bottom: 12px; border-bottom: 1px solid #dbeafe; }
-     .copy-all-btn { background: #2563eb; color: white; border: none; border-radius: 4px; padding: 6px 12px; font-size: 12px; cursor: pointer; font-weight: 500; transition: all 0.2s; }
-     .copy-all-btn:hover { background: #1d4ed8; }
-     .copy-all-btn.copied { background: #16a34a; }
-     .claude-md-item { display: flex; flex-wrap: wrap; align-items: flex-start; gap: 8px; padding: 10px 0; border-bottom: 1px solid #dbeafe; }
-     .claude-md-item:last-child { border-bottom: none; }
-     .cmd-checkbox { margin-top: 2px; }
-     .cmd-code { background: white; padding: 8px 12px; border-radius: 4px; font-size: 12px; color: #1e40af; border: 1px solid #bfdbfe; font-family: monospace; display: block; white-space: pre-wrap; word-break: break-word; flex: 1; }
-     .cmd-why { font-size: 12px; color: #64748b; width: 100%; padding-left: 24px; margin-top: 4px; }
-     .features-section, .patterns-section { display: flex; flex-direction: column; gap: 12px; margin: 16px 0; }
-     .feature-card { background: #f0fdf4; border: 1px solid #86efac; border-radius: 8px; padding: 16px; }
-     .pattern-card { background: #f0f9ff; border: 1px solid #7dd3fc; border-radius: 8px; padding: 16px; }
-     .feature-title, .pattern-title { font-weight: 600; font-size: 15px; color: #0f172a; margin-bottom: 6px; }
-     .feature-oneliner { font-size: 14px; color: #475569; margin-bottom: 8px; }
-     .pattern-summary { font-size: 14px; color: #475569; margin-bottom: 8px; }
-     .feature-why, .pattern-detail { font-size: 13px; color: #334155; line-height: 1.5; }
-     .feature-examples { margin-top: 12px; }
-     .feature-example { padding: 8px 0; border-top: 1px solid #d1fae5; }
-     .feature-example:first-child { border-top: none; }
-     .example-desc { font-size: 13px; color: #334155; margin-bottom: 6px; }
-     .example-code-row { display: flex; align-items: flex-start; gap: 8px; }
-     .example-code { flex: 1; background: #f1f5f9; padding: 8px 12px; border-radius: 4px; font-family: monospace; font-size: 12px; color: #334155; overflow-x: auto; white-space: pre-wrap; }
-     .copyable-prompt-section { margin-top: 12px; padding-top: 12px; border-top: 1px solid #e2e8f0; }
-     .copyable-prompt-row { display: flex; align-items: flex-start; gap: 8px; }
-     .copyable-prompt { flex: 1; background: #f8fafc; padding: 10px 12px; border-radius: 4px; font-family: monospace; font-size: 12px; color: #334155; border: 1px solid #e2e8f0; white-space: pre-wrap; line-height: 1.5; }
-     .feature-code { background: #f8fafc; padding: 12px; border-radius: 6px; margin-top: 12px; border: 1px solid #e2e8f0; display: flex; align-items: flex-start; gap: 8px; }
-     .feature-code code { flex: 1; font-family: monospace; font-size: 12px; color: #334155; white-space: pre-wrap; }
-     .pattern-prompt { background: #f8fafc; padding: 12px; border-radius: 6px; margin-top: 12px; border: 1px solid #e2e8f0; }
-     .pattern-prompt code { font-family: monospace; font-size: 12px; color: #334155; display: block; white-space: pre-wrap; margin-bottom: 8px; }
-     .prompt-label { font-size: 11px; font-weight: 600; text-transform: uppercase; color: #64748b; margin-bottom: 6px; }
-     .copy-btn { background: #e2e8f0; border: none; border-radius: 4px; padding: 4px 8px; font-size: 11px; cursor: pointer; color: #475569; flex-shrink: 0; }
-     .copy-btn:hover { background: #cbd5e1; }
-     .charts-row { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin: 24px 0; }
-     .chart-card { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; }
-     .chart-title { font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase; margin-bottom: 12px; }
-     .bar-row { display: flex; align-items: center; margin-bottom: 6px; }
-     .bar-label { width: 100px; font-size: 11px; color: #475569; flex-shrink: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
-     .bar-track { flex: 1; height: 6px; background: #f1f5f9; border-radius: 3px; margin: 0 8px; }
-     .bar-fill { height: 100%; border-radius: 3px; }
-     .bar-value { width: 28px; font-size: 11px; font-weight: 500; color: #64748b; text-align: right; }
-     .empty { color: #94a3b8; font-size: 13px; }
-     .horizon-section { display: flex; flex-direction: column; gap: 16px; }
-     .horizon-card { background: linear-gradient(135deg, #faf5ff 0%, #f5f3ff 100%); border: 1px solid #c4b5fd; border-radius: 8px; padding: 16px; }
-     .horizon-title { font-weight: 600; font-size: 15px; color: #5b21b6; margin-bottom: 8px; }
-     .horizon-possible { font-size: 14px; color: #334155; margin-bottom: 10px; line-height: 1.5; }
-     .horizon-tip { font-size: 13px; color: #6b21a8; background: rgba(255,255,255,0.6); padding: 8px 12px; border-radius: 4px; }
-     .feedback-header { margin-top: 48px; color: #64748b; font-size: 16px; }
-     .feedback-intro { font-size: 13px; color: #94a3b8; margin-bottom: 16px; }
-     .feedback-section { margin-top: 16px; }
-     .feedback-section h3 { font-size: 14px; font-weight: 600; color: #475569; margin-bottom: 12px; }
-     .feedback-card { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin-bottom: 12px; }
-     .feedback-card.team-card { background: #eff6ff; border-color: #bfdbfe; }
-     .feedback-card.model-card { background: #faf5ff; border-color: #e9d5ff; }
-     .feedback-title { font-weight: 600; font-size: 14px; color: #0f172a; margin-bottom: 6px; }
-     .feedback-detail { font-size: 13px; color: #475569; line-height: 1.5; }
-     .feedback-evidence { font-size: 12px; color: #64748b; margin-top: 8px; }
-     .fun-ending { background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border: 1px solid #fbbf24; border-radius: 12px; padding: 24px; margin-top: 40px; text-align: center; }
-     .fun-headline { font-size: 18px; font-weight: 600; color: #78350f; margin-bottom: 8px; }
-     .fun-detail { font-size: 14px; color: #92400e; }
-     .collapsible-section { margin-top: 16px; }
-     .collapsible-header { display: flex; align-items: center; gap: 8px; cursor: pointer; padding: 12px 0; border-bottom: 1px solid #e2e8f0; }
-     .collapsible-header h3 { margin: 0; font-size: 14px; font-weight: 600; color: #475569; }
-     .collapsible-arrow { font-size: 12px; color: #94a3b8; transition: transform 0.2s; }
-     .collapsible-content { display: none; padding-top: 16px; }
-     .collapsible-content.open { display: block; }
-     .collapsible-header.open .collapsible-arrow { transform: rotate(90deg); }
-     @media (max-width: 640px) { .charts-row { grid-template-columns: 1fr; } .stats-row { justify-content: center; } }
-   `,
-     B = `
-     function toggleCollapsible(header) {
-       header.classList.toggle('open');
-       const content = header.nextElementSibling;
-       content.classList.toggle('open');
-     }
-     function copyText(btn) {
-       const code = btn.previousElementSibling;
-       navigator.clipboard.writeText(code.textContent).then(() => {
-         btn.textContent = 'Copied!';
-         setTimeout(() => { btn.textContent = 'Copy'; }, 2000);
-       });
-     }
-     function copyCmdItem(idx) {
-       const checkbox = document.getElementById('cmd-' + idx);
-       if (checkbox) {
-         const text = checkbox.dataset.text;
-         navigator.clipboard.writeText(text).then(() => {
-           const btn = checkbox.nextElementSibling.querySelector('.copy-btn');
-           if (btn) { btn.textContent = 'Copied!'; setTimeout(() => { btn.textContent = 'Copy'; }, 2000); }
-         });
-       }
-     }
-     function copyAllCheckedClaudeMd() {
-       const checkboxes = document.querySelectorAll('.cmd-checkbox:checked');
-       const texts = [];
-       checkboxes.forEach(cb => {
-         if (cb.dataset.text) { texts.push(cb.dataset.text); }
-       });
-       const combined = texts.join('\\n');
-       const btn = document.querySelector('.copy-all-btn');
-       if (btn) {
-         navigator.clipboard.writeText(combined).then(() => {
-           btn.textContent = 'Copied ' + texts.length + ' items!';
-           btn.classList.add('copied');
-           setTimeout(() => { btn.textContent = 'Copy All Checked'; btn.classList.remove('copied'); }, 2000);
-         });
-       }
-     }
-     // Timezone selector for time of day chart (data is from our own analytics, not user input)
-     const rawHourCounts = ${lAz(A.message_hours)};
-     function updateHourHistogram(offsetFromPT) {
-       const periods = [
-         { label: "Morning (6-12)", range: [6,7,8,9,10,11] },
-         { label: "Afternoon (12-18)", range: [12,13,14,15,16,17] },
-         { label: "Evening (18-24)", range: [18,19,20,21,22,23] },
-         { label: "Night (0-6)", range: [0,1,2,3,4,5] }
-       ];
-       const adjustedCounts = {};
-       for (const [hour, count] of Object.entries(rawHourCounts)) {
-         const newHour = (parseInt(hour) + offsetFromPT + 24) % 24;
-         adjustedCounts[newHour] = (adjustedCounts[newHour] || 0) + count;
-       }
-       const periodCounts = periods.map(p => ({
-         label: p.label,
-         count: p.range.reduce((sum, h) => sum + (adjustedCounts[h] || 0), 0)
-       }));
-       const maxCount = Math.max(...periodCounts.map(p => p.count)) || 1;
-       const container = document.getElementById('hour-histogram');
-       container.textContent = '';
-       periodCounts.forEach(p => {
-         const row = document.createElement('div');
-         row.className = 'bar-row';
-         const label = document.createElement('div');
-         label.className = 'bar-label';
-         label.textContent = p.label;
-         const track = document.createElement('div');
-         track.className = 'bar-track';
-         const fill = document.createElement('div');
-         fill.className = 'bar-fill';
-         fill.style.width = (p.count / maxCount) * 100 + '%';
-         fill.style.background = '#8b5cf6';
-         track.appendChild(fill);
-         const value = document.createElement('div');
-         value.className = 'bar-value';
-         value.textContent = p.count;
-         row.appendChild(label);
-         row.appendChild(track);
-         row.appendChild(value);
-         container.appendChild(row);
-       });
-     }
-     document.getElementById('timezone-select').addEventListener('change', function() {
-       const customInput = document.getElementById('custom-offset');
-       if (this.value === 'custom') {
-         customInput.style.display = 'inline-block';
-         customInput.focus();
-       } else {
-         customInput.style.display = 'none';
-         updateHourHistogram(parseInt(this.value));
-       }
-     });
-     document.getElementById('custom-offset').addEventListener('change', function() {
-       const offset = parseInt(this.value) + 8;
-       updateHourHistogram(offset);
-     });
-   `;
-   return `<!DOCTYPE html>
- <html>
- <head>
-   <meta charset="utf-8">
-   <title>Claude Code Insights</title>
-   <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
-   <style>
-     * { box-sizing: border-box; margin: 0; padding: 0; }
-     body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; background: #f8fafc; color: #334155; line-height: 1.65; padding: 48px 24px; }
-     .container { max-width: 800px; margin: 0 auto; }
-     h1 { font-size: 32px; font-weight: 700; color: #0f172a; margin-bottom: 8px; }
-     h2 { font-size: 20px; font-weight: 600; color: #0f172a; margin-top: 48px; margin-bottom: 16px; }
-     .subtitle { color: #64748b; font-size: 15px; margin-bottom: 32px; }
-     .nav-toc { display: flex; flex-wrap: wrap; gap: 8px; margin: 24px 0 32px 0; padding: 16px; background: white; border-radius: 8px; border: 1px solid #e2e8f0; }
-     .nav-toc a { font-size: 12px; color: #64748b; text-decoration: none; padding: 6px 12px; border-radius: 6px; background: #f1f5f9; transition: all 0.15s; }
-     .nav-toc a:hover { background: #e2e8f0; color: #334155; }
-     .stats-row { display: flex; gap: 24px; margin-bottom: 40px; padding: 20px 0; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0; flex-wrap: wrap; }
-     .stat { text-align: center; }
-     .stat-value { font-size: 24px; font-weight: 700; color: #0f172a; }
-     .stat-label { font-size: 11px; color: #64748b; text-transform: uppercase; }
-     .at-a-glance { background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border: 1px solid #f59e0b; border-radius: 12px; padding: 20px 24px; margin-bottom: 32px; }
-     .glance-title { font-size: 16px; font-weight: 700; color: #92400e; margin-bottom: 16px; }
-     .glance-sections { display: flex; flex-direction: column; gap: 12px; }
-     .glance-section { font-size: 14px; color: #78350f; line-height: 1.6; }
-     .glance-section strong { color: #92400e; }
-     .see-more { color: #b45309; text-decoration: none; font-size: 13px; white-space: nowrap; }
-     .see-more:hover { text-decoration: underline; }
-     .project-areas { display: flex; flex-direction: column; gap: 12px; margin-bottom: 32px; }
-     .project-area { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; }
-     .area-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
-     .area-name { font-weight: 600; font-size: 15px; color: #0f172a; }
-     .area-count { font-size: 12px; color: #64748b; background: #f1f5f9; padding: 2px 8px; border-radius: 4px; }
-     .area-desc { font-size: 14px; color: #475569; line-height: 1.5; }
-     .narrative { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin-bottom: 24px; }
-     .narrative p { margin-bottom: 12px; font-size: 14px; color: #475569; line-height: 1.7; }
-     .key-insight { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 12px 16px; margin-top: 12px; font-size: 14px; color: #166534; }
-     .section-intro { font-size: 14px; color: #64748b; margin-bottom: 16px; }
-     .big-wins { display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px; }
-     .big-win { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 16px; }
-     .big-win-title { font-weight: 600; font-size: 15px; color: #166534; margin-bottom: 8px; }
-     .big-win-desc { font-size: 14px; color: #15803d; line-height: 1.5; }
-     .friction-categories { display: flex; flex-direction: column; gap: 16px; margin-bottom: 24px; }
-     .friction-category { background: #fef2f2; border: 1px solid #fca5a5; border-radius: 8px; padding: 16px; }
-     .friction-title { font-weight: 600; font-size: 15px; color: #991b1b; margin-bottom: 6px; }
-     .friction-desc { font-size: 13px; color: #7f1d1d; margin-bottom: 10px; }
-     .friction-examples { margin: 0 0 0 20px; font-size: 13px; color: #334155; }
-     .friction-examples li { margin-bottom: 4px; }
-     .claude-md-section { background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 16px; margin-bottom: 20px; }
-     .claude-md-section h3 { font-size: 14px; font-weight: 600; color: #1e40af; margin: 0 0 12px 0; }
-     .claude-md-actions { margin-bottom: 12px; padding-bottom: 12px; border-bottom: 1px solid #dbeafe; }
-     .copy-all-btn { background: #2563eb; color: white; border: none; border-radius: 4px; padding: 6px 12px; font-size: 12px; cursor: pointer; font-weight: 500; transition: all 0.2s; }
-     .copy-all-btn:hover { background: #1d4ed8; }
-     .copy-all-btn.copied { background: #16a34a; }
-     .claude-md-item { display: flex; flex-wrap: wrap; align-items: flex-start; gap: 8px; padding: 10px 0; border-bottom: 1px solid #dbeafe; }
-     .claude-md-item:last-child { border-bottom: none; }
-     .cmd-checkbox { margin-top: 2px; }
-     .cmd-code { background: white; padding: 8px 12px; border-radius: 4px; font-size: 12px; color: #1e40af; border: 1px solid #bfdbfe; font-family: monospace; display: block; white-space: pre-wrap; word-break: break-word; flex: 1; }
-     .cmd-why { font-size: 12px; color: #64748b; width: 100%; padding-left: 24px; margin-top: 4px; }
-     .features-section, .patterns-section { display: flex; flex-direction: column; gap: 12px; margin: 16px 0; }
-     .feature-card { background: #f0fdf4; border: 1px solid #86efac; border-radius: 8px; padding: 16px; }
-     .pattern-card { background: #f0f9ff; border: 1px solid #7dd3fc; border-radius: 8px; padding: 16px; }
-     .feature-title, .pattern-title { font-weight: 600; font-size: 15px; color: #0f172a; margin-bottom: 6px; }
-     .feature-oneliner { font-size: 14px; color: #475569; margin-bottom: 8px; }
-     .pattern-summary { font-size: 14px; color: #475569; margin-bottom: 8px; }
-     .feature-why, .pattern-detail { font-size: 13px; color: #334155; line-height: 1.5; }
-     .feature-examples { margin-top: 12px; }
-     .feature-example { padding: 8px 0; border-top: 1px solid #d1fae5; }
-     .feature-example:first-child { border-top: none; }
-     .example-desc { font-size: 13px; color: #334155; margin-bottom: 6px; }
-     .example-code-row { display: flex; align-items: flex-start; gap: 8px; }
-     .example-code { flex: 1; background: #f1f5f9; padding: 8px 12px; border-radius: 4px; font-family: monospace; font-size: 12px; color: #334155; overflow-x: auto; white-space: pre-wrap; }
-     .copyable-prompt-section { margin-top: 12px; padding-top: 12px; border-top: 1px solid #e2e8f0; }
-     .copyable-prompt-row { display: flex; align-items: flex-start; gap: 8px; }
-     .copyable-prompt { flex: 1; background: #f8fafc; padding: 10px 12px; border-radius: 4px; font-family: monospace; font-size: 12px; color: #334155; border: 1px solid #e2e8f0; white-space: pre-wrap; line-height: 1.5; }
-     .feature-code { background: #f8fafc; padding: 12px; border-radius: 6px; margin-top: 12px; border: 1px solid #e2e8f0; display: flex; align-items: flex-start; gap: 8px; }
-     .feature-code code { flex: 1; font-family: monospace; font-size: 12px; color: #334155; white-space: pre-wrap; }
-     .pattern-prompt { background: #f8fafc; padding: 12px; border-radius: 6px; margin-top: 12px; border: 1px solid #e2e8f0; }
-     .pattern-prompt code { font-family: monospace; font-size: 12px; color: #334155; display: block; white-space: pre-wrap; margin-bottom: 8px; }
-     .prompt-label { font-size: 11px; font-weight: 600; text-transform: uppercase; color: #64748b; margin-bottom: 6px; }
-     .copy-btn { background: #e2e8f0; border: none; border-radius: 4px; padding: 4px 8px; font-size: 11px; cursor: pointer; color: #475569; flex-shrink: 0; }
-     .copy-btn:hover { background: #cbd5e1; }
-     .charts-row { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin: 24px 0; }
-     .chart-card { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; }
-     .chart-title { font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase; margin-bottom: 12px; }
-     .bar-row { display: flex; align-items: center; margin-bottom: 6px; }
-     .bar-label { width: 100px; font-size: 11px; color: #475569; flex-shrink: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
-     .bar-track { flex: 1; height: 6px; background: #f1f5f9; border-radius: 3px; margin: 0 8px; }
-     .bar-fill { height: 100%; border-radius: 3px; }
-     .bar-value { width: 28px; font-size: 11px; font-weight: 500; color: #64748b; text-align: right; }
-     .empty { color: #94a3b8; font-size: 13px; }
-     .horizon-section { display: flex; flex-direction: column; gap: 16px; }
-     .horizon-card { background: linear-gradient(135deg, #faf5ff 0%, #f5f3ff 100%); border: 1px solid #c4b5fd; border-radius: 8px; padding: 16px; }
-     .horizon-title { font-weight: 600; font-size: 15px; color: #5b21b6; margin-bottom: 8px; }
-     .horizon-possible { font-size: 14px; color: #334155; margin-bottom: 10px; line-height: 1.5; }
-     .horizon-tip { font-size: 13px; color: #6b21a8; background: rgba(255,255,255,0.6); padding: 8px 12px; border-radius: 4px; }
-     .feedback-header { margin-top: 48px; color: #64748b; font-size: 16px; }
-     .feedback-intro { font-size: 13px; color: #94a3b8; margin-bottom: 16px; }
-     .feedback-section { margin-top: 16px; }
-     .feedback-section h3 { font-size: 14px; font-weight: 600; color: #475569; margin-bottom: 12px; }
-     .feedback-card { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin-bottom: 12px; }
-     .feedback-card.team-card { background: #eff6ff; border-color: #bfdbfe; }
-     .feedback-card.model-card { background: #faf5ff; border-color: #e9d5ff; }
-     .feedback-title { font-weight: 600; font-size: 14px; color: #0f172a; margin-bottom: 6px; }
-     .feedback-detail { font-size: 13px; color: #475569; line-height: 1.5; }
-     .feedback-evidence { font-size: 12px; color: #64748b; margin-top: 8px; }
-     .fun-ending { background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border: 1px solid #fbbf24; border-radius: 12px; padding: 24px; margin-top: 40px; text-align: center; }
-     .fun-headline { font-size: 18px; font-weight: 600; color: #78350f; margin-bottom: 8px; }
-     .fun-detail { font-size: 14px; color: #92400e; }
-     .collapsible-section { margin-top: 16px; }
-     .collapsible-header { display: flex; align-items: center; gap: 8px; cursor: pointer; padding: 12px 0; border-bottom: 1px solid #e2e8f0; }
-     .collapsible-header h3 { margin: 0; font-size: 14px; font-weight: 600; color: #475569; }
-     .collapsible-arrow { font-size: 12px; color: #94a3b8; transition: transform 0.2s; }
-     .collapsible-content { display: none; padding-top: 16px; }
-     .collapsible-content.open { display: block; }
-     .collapsible-header.open .collapsible-arrow { transform: rotate(90deg); }
-     @media (max-width: 640px) { .charts-row { grid-template-columns: 1fr; } .stats-row { justify-content: center; } }
-   </style>
- </head>
- <body>
-   <div class="container">
-     <h1>Claude Code Insights</h1>
-     <p class="subtitle">${A.total_messages.toLocaleString()} messages across ${A.total_sessions} sessions | ${A.date_range.start} to ${A.date_range.end}</p>
- 
-     ${z}
- 
-     <nav class="nav-toc">
-       <a href="#section-work">What You Work On</a>
-       <a href="#section-usage">How You Use CC</a>
-       <a href="#section-wins">Impressive Things</a>
-       <a href="#section-friction">Where Things Go Wrong</a>
-       <a href="#section-features">Features to Try</a>
-       <a href="#section-patterns">New Usage Patterns</a>
-       <a href="#section-horizon">On the Horizon</a>
-       <a href="#section-feedback">Team Feedback</a>
-     </nav>
- 
-     <div class="stats-row">
-       <div class="stat"><div class="stat-value">${A.total_messages.toLocaleString()}</div><div class="stat-label">Messages</div></div>
-       <div class="stat"><div class="stat-value">+${A.total_lines_added.toLocaleString()}/-${A.total_lines_removed.toLocaleString()}</div><div class="stat-label">Lines</div></div>
-       <div class="stat"><div class="stat-value">${A.total_files_modified}</div><div class="stat-label">Files</div></div>
-       <div class="stat"><div class="stat-value">${A.days_active}</div><div class="stat-label">Days</div></div>
-       <div class="stat"><div class="stat-value">${A.messages_per_day}</div><div class="stat-label">Msgs/Day</div></div>
-     </div>
- 
-     ${H}
- 
-     <div class="charts-row">
-       <div class="chart-card">
-         <div class="chart-title">What You Wanted</div>
-         ${bd(A.goal_categories, "#2563eb")}
-       </div>
-       <div class="chart-card">
-         <div class="chart-title">Top Tools Used</div>
-         ${bd(A.tool_counts, "#0891b2")}
-       </div>
-     </div>
- 
-     <div class="charts-row">
-       <div class="chart-card">
-         <div class="chart-title">Languages</div>
-         ${bd(A.languages, "#10b981")}
-       </div>
-       <div class="chart-card">
-         <div class="chart-title">Session Types</div>
-         ${bd(A.session_types || {}, "#8b5cf6")}
-       </div>
-     </div>
- 
-     ${$}
- 
-     <!-- Response Time Distribution -->
-     <div class="chart-card" style="margin: 24px 0;">
-       <div class="chart-title">User Response Time Distribution</div>
-       ${dAz(A.user_response_times)}
-       <div style="font-size: 12px; color: #64748b; margin-top: 8px;">
-         Median: ${A.median_response_time.toFixed(1)}s &bull; Average: ${A.avg_response_time.toFixed(1)}s
-       </div>
-     </div>
- 
-     <!-- Multi-clauding Section (matching Python reference) -->
-     <div class="chart-card" style="margin: 24px 0;">
-       <div class="chart-title">Multi-Clauding (Parallel Sessions)</div>
-       ${
-         A.multi_clauding.overlap_events === 0
-           ? `
-         <p style="font-size: 14px; color: #64748b; padding: 8px 0;">
-           No parallel session usage detected. You typically work with one Claude Code session at a time.
-         </p>
-       `
-           : `
-         <div style="display: flex; gap: 24px; margin: 12px 0;">
-           <div style="text-align: center;">
-             <div style="font-size: 24px; font-weight: 700; color: #7c3aed;">${A.multi_clauding.overlap_events}</div>
-             <div style="font-size: 11px; color: #64748b; text-transform: uppercase;">Overlap Events</div>
-           </div>
-           <div style="text-align: center;">
-             <div style="font-size: 24px; font-weight: 700; color: #7c3aed;">${A.multi_clauding.sessions_involved}</div>
-             <div style="font-size: 11px; color: #64748b; text-transform: uppercase;">Sessions Involved</div>
-           </div>
-           <div style="text-align: center;">
-             <div style="font-size: 24px; font-weight: 700; color: #7c3aed;">${A.total_messages > 0 ? Math.round((100 * A.multi_clauding.user_messages_during) / A.total_messages) : 0}%</div>
-             <div style="font-size: 11px; color: #64748b; text-transform: uppercase;">Of Messages</div>
-           </div>
-         </div>
-         <p style="font-size: 13px; color: #475569; margin-top: 12px;">
-           You run multiple Claude Code sessions simultaneously. Multi-clauding is detected when sessions
-           overlap in time, suggesting parallel workflows.
-         </p>
-       `
-       }
-     </div>
- 
-     <!-- Time of Day & Tool Errors -->
-     <div class="charts-row">
-       <div class="chart-card">
-         <div class="chart-title" style="display: flex; align-items: center; gap: 12px;">
-           User Messages by Time of Day
-           <select id="timezone-select" style="font-size: 12px; padding: 4px 8px; border-radius: 4px; border: 1px solid #e2e8f0;">
-             <option value="0">PT (UTC-8)</option>
-             <option value="3">ET (UTC-5)</option>
-             <option value="8">London (UTC)</option>
-             <option value="9">CET (UTC+1)</option>
-             <option value="17">Tokyo (UTC+9)</option>
-             <option value="custom">Custom offset...</option>
-           </select>
-           <input type="number" id="custom-offset" placeholder="UTC offset" style="display: none; width: 80px; font-size: 12px; padding: 4px; border-radius: 4px; border: 1px solid #e2e8f0;">
-         </div>
-         ${cAz(A.message_hours)}
-       </div>
-       <div class="chart-card">
-         <div class="chart-title">Tool Errors Encountered</div>
-         ${Object.keys(A.tool_error_categories).length > 0 ? bd(A.tool_error_categories, "#dc2626") : '<p class="empty">No tool errors</p>'}
-       </div>
-     </div>
- 
-     ${J}
- 
-     <div class="charts-row">
-       <div class="chart-card">
-         <div class="chart-title">What Helped Most (Claude's Capabilities)</div>
-         ${bd(A.success, "#16a34a")}
-       </div>
-       <div class="chart-card">
-         <div class="chart-title">Outcomes</div>
-         ${bd(A.outcomes, "#8b5cf6", 6, pAz)}
-       </div>
-     </div>
- 
-     ${D}
- 
-     <div class="charts-row">
-       <div class="chart-card">
-         <div class="chart-title">Primary Friction Types</div>
-         ${bd(A.friction, "#dc2626")}
-       </div>
-       <div class="chart-card">
-         <div class="chart-title">Inferred Satisfaction (model-estimated)</div>
-         ${bd(A.satisfaction, "#eab308", 6, UAz)}
-       </div>
-     </div>
- 
-     ${M}
- 
-     ${P}
- 
-     ${T}
- 
-     ${V}
-   </div>
-   <script>${B}</script>
- </body>
- </html>`;
- }

--- Removed Mzq (pretty-v2.1.31.js:512656-512665)
- async function Mzq() {
-   try {
-     let { stdout: A } = await RA("uname", ["-sr"], {
-       preserveOutputOnError: !1,
-     });
-     return A.trim();
-   } catch {
-     return "unknown";
-   }
- }

--- Removed z8z (pretty-v2.1.31.js:512698-512698)
-   z8z = "Claude Opus 4.5",

--- Removed w8z (pretty-v2.1.31.js:512699-512699)
-   w8z = "claude-opus-4-5-20251101",

--- Removed mV (pretty-v2.1.31.js:512703-512734)
- var mV = E(() => {
-   N5();
-   AY();
-   k7();
-   C8();
-   _D();
-   BH();
-   $_1();
-   kq();
-   SO1();
-   j_();
-   iD();
-   CB();
-   HG();
-   cx1();
-   nz();
-   yq();
-   s6();
-   mA();
-   e7();
-   Q4();
-   GbA();
-   Wz();
-   _6();
-   SDA();
-   Yzq();
-   ZbA = {
-     opus: "claude-opus-4-5-20251101",
-     sonnet: "claude-sonnet-4-5-20250929",
-     haiku: "claude-haiku-4-5-20251001",
-   };
- });

--- Removed vzq (pretty-v2.1.31.js:513898-513900)
- var vzq = E(() => {
-   u8z = /(?<!<)<<(?!<)(-)?(['"])?\\?(\w+)\2?/;
- });

--- Removed xE4 (pretty-v2.1.31.js:514083-514089)
- function xE4(A) {
-   try {
-     return yX(A).length > 1 && !c8z(A);
-   } catch {
-     return !0;
-   }
- }

--- Removed lV6 (pretty-v2.1.31.js:527213-527240)
- var lV6 = E(() => {
-   p1();
-   u1();
-   S8();
-   R7();
-   D8();
-   ok6();
-   g6();
-   n3();
-   y5();
-   F8();
-   N6();
-   zZ();
-   Aq();
-   DX();
-   Wz();
-   ((LA = o(J1(), 1)), (CJ = o(J1(), 1)));
-   ((L3z = [
-     { value: "both", label: "Restore code and conversation" },
-     { value: "conversation", label: "Restore conversation" },
-     { value: "code", label: "Restore code" },
-     { value: "nevermind", label: "Never mind" },
-   ]),
-     (R3z = [
-       { value: "conversation", label: "Restore conversation" },
-       { value: "nevermind", label: "Never mind" },
-     ]));
- });

--- Removed cOq (pretty-v2.1.31.js:534300-534611)
- function cOq(A) {
-   let q = t(68),
-     { toolUseConfirm: K, onDone: Y, onReject: z } = A,
-     w = fkA.safeParse(K.input),
-     H = w.success ? w.data.questions || [] : [],
-     O = w.success ? w.data.metadata?.source : void 0,
-     _ = T6(D9z) === "plan",
-     J;
-   if (q[0] !== _) ((J = _ ? nG() : void 0), (q[0] = _), (q[1] = J));
-   else J = q[1];
-   let X = J,
-     D = FOq(),
-     {
-       currentQuestionIndex: j,
-       answers: M,
-       questionStates: W,
-       isInTextInput: P,
-       nextQuestion: G,
-       prevQuestion: f,
-       updateQuestionState: V,
-       setAnswer: N,
-       setTextInputMode: T,
-     } = D,
-     k = j < (H?.length || 0) ? H?.[j] : null,
-     y = j === (H?.length || 0),
-     B = H?.every((s) => s?.question && !!M[s.question]) ?? !1,
-     C = H.length === 1 && !H[0]?.multiSelect,
-     m;
-   if (
-     q[2] !== _ ||
-     q[3] !== O ||
-     q[4] !== Y ||
-     q[5] !== z ||
-     q[6] !== H.length ||
-     q[7] !== K
-   )
-     ((m = () => {
-       if (O)
-         n("tengu_ask_user_question_rejected", {
-           source: O,
-           questionCount: H.length,
-           isInPlanMode: _,
-           interviewPhaseEnabled: _ && h0(),
-         });
-       (Y(), z(), K.onReject());
-     }),
-       (q[2] = _),
-       (q[3] = O),
-       (q[4] = Y),
-       (q[5] = z),
-       (q[6] = H.length),
-       (q[7] = K),
-       (q[8] = m));
-   else m = q[8];
-   let u = m,
-     U;
-   if (
-     q[9] !== M ||
-     q[10] !== _ ||
-     q[11] !== O ||
-     q[12] !== Y ||
-     q[13] !== H ||
-     q[14] !== K
-   )
-     ((U = () => {
-       let w1 = `The user wants to clarify these questions.
-     This means they may have additional information, context or questions for you.
-     Take their response into account and then reformulate the questions if appropriate.
-     Start by asking them what they would like to clarify.
- 
-     Questions asked:
- ${H.map((Z1) => {
-   let j1 = M[Z1.question];
-   if (j1)
-     return `- "${Z1.question}"
-   Answer: ${j1}`;
-   return `- "${Z1.question}"
-   (No answer provided)`;
- }).join(`
- `)}`;
-       if (O)
-         n("tengu_ask_user_question_respond_to_claude", {
-           source: O,
-           questionCount: H.length,
-           isInPlanMode: _,
-           interviewPhaseEnabled: _ && h0(),
-         });
-       (Y(), K.onReject(w1));
-     }),
-       (q[9] = M),
-       (q[10] = _),
-       (q[11] = O),
-       (q[12] = Y),
-       (q[13] = H),
-       (q[14] = K),
-       (q[15] = U));
-   else U = q[15];
-   let g = U,
-     x;
-   if (
-     q[16] !== M ||
-     q[17] !== _ ||
-     q[18] !== O ||
-     q[19] !== Y ||
-     q[20] !== H ||
-     q[21] !== K
-   )
-     ((x = () => {
-       let w1 = `The user has indicated they have provided enough answers for the plan interview.
- Stop asking clarifying questions and proceed to finish the plan with the information you have.
- 
- Questions asked and answers provided:
- ${H.map((Z1) => {
-   let j1 = M[Z1.question];
-   if (j1)
-     return `- "${Z1.question}"
-   Answer: ${j1}`;
-   return `- "${Z1.question}"
-   (No answer provided)`;
- }).join(`
- `)}`;
-       if (O)
-         n("tengu_ask_user_question_finish_plan_interview", {
-           source: O,
-           questionCount: H.length,
-           isInPlanMode: _,
-           interviewPhaseEnabled: _ && h0(),
-         });
-       (Y(), K.onReject(w1));
-     }),
-       (q[16] = M),
-       (q[17] = _),
-       (q[18] = O),
-       (q[19] = Y),
-       (q[20] = H),
-       (q[21] = K),
-       (q[22] = x));
-   else x = q[22];
-   let d = x,
-     r;
-   if (
-     q[23] !== _ ||
-     q[24] !== O ||
-     q[25] !== Y ||
-     q[26] !== H.length ||
-     q[27] !== K
-   )
-     ((r = (s) => {
-       if (O)
-         n("tengu_ask_user_question_accepted", {
-           source: O,
-           questionCount: H.length,
-           answerCount: Object.keys(s).length,
-           isInPlanMode: _,
-           interviewPhaseEnabled: _ && h0(),
-         });
-       let w1 = { ...K.input, answers: s };
-       (Y(), K.onAllow(w1, []));
-     }),
-       (q[23] = _),
-       (q[24] = O),
-       (q[25] = Y),
-       (q[26] = H.length),
-       (q[27] = K),
-       (q[28] = r));
-   else r = q[28];
-   let c = r,
-     q1;
-   if (q[29] !== M || q[30] !== H.length || q[31] !== N || q[32] !== c)
-     ((q1 = (s, w1, Z1, j1) => {
-       let L1 = j1 === void 0 ? !0 : j1,
-         v1,
-         Y1 = Array.isArray(w1);
-       if (Y1) v1 = w1.join(", ");
-       else v1 = Z1 || w1;
-       let K1 = H.length === 1;
-       if (!Y1 && K1 && L1) {
-         let X1 = { ...M, [s]: v1 };
-         c(X1);
-         return;
-       }
-       N(s, v1, L1);
-     }),
-       (q[29] = M),
-       (q[30] = H.length),
-       (q[31] = N),
-       (q[32] = c),
-       (q[33] = q1));
-   else q1 = q[33];
-   let H1 = q1,
-     $1;
-   if (q[34] !== M || q[35] !== u || q[36] !== c)
-     (($1 = function (w1) {
-       if (w1 === "cancel") {
-         u();
-         return;
-       }
-       if (w1 === "submit") c(M);
-     }),
-       (q[34] = M),
-       (q[35] = u),
-       (q[36] = c),
-       (q[37] = $1));
-   else $1 = q[37];
-   let A1 = $1,
-     O1;
-   if (
-     q[38] !== j ||
-     q[39] !== C ||
-     q[40] !== y ||
-     q[41] !== P ||
-     q[42] !== G ||
-     q[43] !== f ||
-     q[44] !== H.length
-   )
-     ((O1 = (s, w1) => {
-       if (P && !y) return;
-       if ((w1.leftArrow || (w1.shift && w1.tab)) && j > 0) f();
-       let Z1 = C ? (H?.length || 1) - 1 : H?.length || 0;
-       if ((w1.rightArrow || (w1.tab && !w1.shift)) && j < Z1) G();
-     }),
-       (q[38] = j),
-       (q[39] = C),
-       (q[40] = y),
-       (q[41] = P),
-       (q[42] = G),
-       (q[43] = f),
-       (q[44] = H.length),
-       (q[45] = O1));
-   else O1 = q[45];
-   if ((eA(O1), k)) {
-     let s;
-     if (
-       q[46] !== M ||
-       q[47] !== k ||
-       q[48] !== j ||
-       q[49] !== u ||
-       q[50] !== d ||
-       q[51] !== H1 ||
-       q[52] !== g ||
-       q[53] !== C ||
-       q[54] !== G ||
-       q[55] !== X ||
-       q[56] !== W ||
-       q[57] !== H ||
-       q[58] !== T ||
-       q[59] !== V
-     )
-       ((s = YBA.default.createElement(gOq, {
-         question: k,
-         questions: H,
-         currentQuestionIndex: j,
-         answers: M,
-         questionStates: W,
-         hideSubmitTab: C,
-         planFilePath: X,
-         onUpdateQuestionState: V,
-         onAnswer: H1,
-         onTextInputFocus: T,
-         onCancel: u,
-         onSubmit: G,
-         onRespondToClaude: g,
-         onFinishPlanInterview: d,
-       })),
-         (q[46] = M),
-         (q[47] = k),
-         (q[48] = j),
-         (q[49] = u),
-         (q[50] = d),
-         (q[51] = H1),
-         (q[52] = g),
-         (q[53] = C),
-         (q[54] = G),
-         (q[55] = X),
-         (q[56] = W),
-         (q[57] = H),
-         (q[58] = T),
-         (q[59] = V),
-         (q[60] = s));
-     else s = q[60];
-     return s;
-   }
-   if (y) {
-     let s;
-     if (
-       q[61] !== B ||
-       q[62] !== M ||
-       q[63] !== j ||
-       q[64] !== A1 ||
-       q[65] !== H ||
-       q[66] !== K.permissionResult
-     )
-       ((s = YBA.default.createElement(pOq, {
-         questions: H,
-         currentQuestionIndex: j,
-         answers: M,
-         allQuestionsAnswered: B,
-         permissionResult: K.permissionResult,
-         onFinalResponse: A1,
-       })),
-         (q[61] = B),
-         (q[62] = M),
-         (q[63] = j),
-         (q[64] = A1),
-         (q[65] = H),
-         (q[66] = K.permissionResult),
-         (q[67] = s));
-     else s = q[67];
-     return s;
-   }
-   return null;
- }

--- Removed eYz (pretty-v2.1.31.js:540466-540528)
- function eYz(A) {
-   let q = t(15),
-     { task: K, isSelected: Y } = A,
-     w = !_Z1(K.status)
-       ? Date.now() - K.startTime
-       : (K.endTime ?? K.startTime) - K.startTime,
-     H;
-   if (q[0] !== w) ((H = E2(w)), (q[0] = w), (q[1] = H));
-   else H = q[1];
-   let O = H,
-     $ = K.progress?.tokenCount,
-     _ = K.progress?.lastActivity,
-     J = _ ? d1.arrowDown : d1.arrowUp,
-     X;
-   if (q[2] !== J || q[3] !== $)
-     ((X = $ !== void 0 && $ > 0 ? ` · ${J} ${pK($)} tokens` : ""),
-       (q[2] = J),
-       (q[3] = $),
-       (q[4] = X));
-   else X = q[4];
-   let D = X,
-     j;
-   if (q[5] !== _?.activityDescription || q[6] !== K.progress)
-     ((j =
-       (K.progress?.recentActivities && mu(K.progress.recentActivities)) ??
-       _?.activityDescription),
-       (q[5] = _?.activityDescription),
-       (q[6] = K.progress),
-       (q[7] = j));
-   else j = q[7];
-   let M = j,
-     W = M ? ` · ${M}` : "",
-     P = Y ? d1.pointer + " " : "  ",
-     G = !Y,
-     f;
-   if (
-     q[8] !== W ||
-     q[9] !== O ||
-     q[10] !== P ||
-     q[11] !== G ||
-     q[12] !== K.description ||
-     q[13] !== D
-   )
-     ((f = SZ.createElement(
-       Z,
-       { dimColor: G },
-       P,
-       K.description,
-       " · ",
-       O,
-       D,
-       W,
-     )),
-       (q[8] = W),
-       (q[9] = O),
-       (q[10] = P),
-       (q[11] = G),
-       (q[12] = K.description),
-       (q[13] = D),
-       (q[14] = f));
-   else f = q[14];
-   return f;
- }

--- Removed vzz (pretty-v2.1.31.js:542703-542705)
- function vzz(A) {
-   return _2.default.createElement(Z, { key: `sep-${A}` }, " · ");
- }

--- Removed $Xq (pretty-v2.1.31.js:545535-545650)
- function $Xq({ config: A, setMessages: q, setIsLoading: K, onInit: Y }) {
-   let z = !!A,
-     w = A?.hasInitialPrompt ?? !1,
-     [H, O] = xR.useState({
-       isConnected: !1,
-       isLoading: w,
-       responseTimedOut: !1,
-     }),
-     $ = xR.useRef(null),
-     [_, J] = xR.useState(null),
-     X = xR.useRef(null);
-   xR.useEffect(() => {
-     if (!A) return;
-     I(`[useRemoteSession] Initializing for session ${A.sessionId}`);
-     let W = new dBA(A, {
-       onMessage: (P) => {
-         if (
-           (I(`[useRemoteSession] Received message type: ${P.type}`), $.current)
-         )
-           (clearTimeout($.current), ($.current = null));
-         if (
-           (O((f) => (f.responseTimedOut ? { ...f, responseTimedOut: !1 } : f)),
-           P.type === "system" && P.subtype === "init" && Y)
-         )
-           (I(
-             `[useRemoteSession] Init received with ${P.slash_commands.length} slash commands`,
-           ),
-             Y(P.slash_commands));
-         if (yN6(P))
-           (O((f) => ({ ...f, isLoading: !1, responseTimedOut: !1 })), K(!1));
-         let G = RN6(P);
-         if (G.type === "message") q((f) => [...f, G.message]);
-         else if (G.type === "stream_event")
-           I("[useRemoteSession] Skipping stream event (not yet implemented)");
-       },
-       onPermissionRequest: (P, G) => {
-         (I(`[useRemoteSession] Permission request for tool: ${P.tool_name}`),
-           J({ request: P, requestId: G }),
-           K(!1));
-       },
-       onConnected: () => {
-         (I("[useRemoteSession] Connected"),
-           O((P) => ({ ...P, isConnected: !0 })));
-       },
-       onDisconnected: () => {
-         (I("[useRemoteSession] Disconnected"),
-           O((P) => ({ ...P, isConnected: !1 })),
-           K(!1));
-       },
-       onError: (P) => {
-         I(`[useRemoteSession] Error: ${P.message}`);
-       },
-     });
-     return (
-       (X.current = W),
-       W.connect(),
-       () => {
-         if ((I("[useRemoteSession] Cleanup - disconnecting"), $.current))
-           (clearTimeout($.current), ($.current = null));
-         (W.disconnect(), (X.current = null));
-       }
-     );
-   }, [A, q, K, Y]);
-   let D = xR.useCallback(
-       async (W) => {
-         let P = X.current;
-         if (!P) return (I("[useRemoteSession] Cannot send - no manager"), !1);
-         if ($.current) clearTimeout($.current);
-         (O((f) => ({ ...f, isLoading: !0, responseTimedOut: !1 })), K(!0));
-         let G = await P.sendMessage(W);
-         if (!G) return (O((f) => ({ ...f, isLoading: !1 })), K(!1), !1);
-         return (
-           ($.current = setTimeout(() => {
-             (I("[useRemoteSession] Response timeout - attempting reconnect"),
-               O((V) => ({ ...V, responseTimedOut: !0 })));
-             let f = tD(
-               "Remote session may be unresponsive. Attempting to reconnect…",
-               "warning",
-             );
-             (q((V) => [...V, f]), P.reconnect());
-           }, H2z)),
-           G
-         );
-       },
-       [K, q],
-     ),
-     j = xR.useCallback(
-       (W) => {
-         let P = X.current,
-           G = _;
-         if (!P || !G) {
-           I("[useRemoteSession] Cannot respond - no pending request");
-           return;
-         }
-         let f = W
-           ? { behavior: "allow", updatedInput: G.request.input }
-           : { behavior: "deny", message: "User denied permission" };
-         if ((P.respondToPermissionRequest(G.requestId, f), J(null), W)) K(!0);
-       },
-       [_, K],
-     ),
-     M = xR.useCallback(() => {
-       if ($.current) (clearTimeout($.current), ($.current = null));
-       (X.current?.disconnect(),
-         (X.current = null),
-         O({ isConnected: !1, isLoading: !1, responseTimedOut: !1 }));
-     }, []);
-   return {
-     isRemoteMode: z,
-     state: H,
-     sendMessage: D,
-     pendingPermissionRequest: _,
-     respondToPermission: j,
-     disconnect: M,
-   };
- }

--- Removed XXq (pretty-v2.1.31.js:545760-545854)
- function XXq({ config: A, setMessages: q, setIsLoading: K }) {
-   let Y = !!A,
-     [z, w] = bR.useState({
-       isConnected: !1,
-       isLoading: !1,
-       responseTimedOut: !1,
-     }),
-     [H, O] = bR.useState(null),
-     $ = bR.useRef(null),
-     _ = bR.useRef(!1);
-   bR.useEffect(() => {
-     if (!A) return;
-     ((_.current = !1), I(`[useDirectConnect] Connecting to ${A.wsUrl}`));
-     let j = new iBA(A, {
-       onMessage: (M) => {
-         if (yN6(M)) (w((P) => ({ ...P, isLoading: !1 })), K(!1));
-         if (M.type === "system" && M.subtype === "init") {
-           if (_.current) return;
-           _.current = !0;
-         }
-         let W = RN6(M, { convertToolResults: !0 });
-         if (W.type === "message") q((P) => [...P, W.message]);
-       },
-       onPermissionRequest: (M, W) => {
-         (I(`[useDirectConnect] Permission request for tool: ${M.tool_name}`),
-           O({ request: M, requestId: W }),
-           K(!1));
-       },
-       onConnected: () => {
-         (I("[useDirectConnect] Connected"),
-           w((M) => ({ ...M, isConnected: !0 })));
-       },
-       onDisconnected: () => {
-         (I("[useDirectConnect] Disconnected"),
-           w((M) => {
-             if (!M.isConnected)
-               process.stderr.write(`
- Failed to connect to server at ${A.wsUrl}
- `);
-             else
-               process.stderr.write(`
- Server disconnected.
- `);
-             return (ZK(1), { ...M, isConnected: !1 });
-           }),
-           K(!1));
-       },
-       onError: (M) => {
-         I(`[useDirectConnect] Error: ${M.message}`);
-       },
-     });
-     return (
-       ($.current = j),
-       j.connect(),
-       () => {
-         (I("[useDirectConnect] Cleanup - disconnecting"),
-           j.disconnect(),
-           ($.current = null));
-       }
-     );
-   }, [A, q, K]);
-   let J = bR.useCallback(
-       async (j) => {
-         let M = $.current;
-         if (!M) return !1;
-         return (w((W) => ({ ...W, isLoading: !0 })), K(!0), M.sendMessage(j));
-       },
-       [K],
-     ),
-     X = bR.useCallback(
-       (j) => {
-         let M = $.current,
-           W = H;
-         if (!M || !W) return;
-         let P = j
-           ? { behavior: "allow", updatedInput: W.request.input }
-           : { behavior: "deny", message: "User denied permission" };
-         if ((M.respondToPermissionRequest(W.requestId, P), O(null), j)) K(!0);
-       },
-       [H, K],
-     ),
-     D = bR.useCallback(() => {
-       ($.current?.disconnect(),
-         ($.current = null),
-         w({ isConnected: !1, isLoading: !1, responseTimedOut: !1 }));
-     }, []);
-   return {
-     isRemoteMode: Y,
-     state: z,
-     sendMessage: J,
-     pendingPermissionRequest: H,
-     respondToPermission: X,
-     disconnect: D,
-   };
- }

--- Removed CHz (pretty-v2.1.31.js:555782-555782)
-   CHz = () => {},

--- Removed import@568489 (pretty-v2.1.31.js:568490-568490)
- import { platform as wuA } from "os";

--- Removed import@568491 (pretty-v2.1.31.js:568492-568501)
- import {
-   existsSync as x4z,
-   unlinkSync as HuA,
-   chmodSync as m2q,
-   statSync as b4z,
-   mkdirSync as u4z,
-   readdirSync as F2q,
-   rmdirSync as B4z,
-   appendFileSync as m4z,
- } from "fs";

=== Added ===

+++ Added jE6 (pretty-v2.1.32.js:1801-1801)
+   jE6 = "adaptive-thinking-2026-01-28",

+++ Added TCq (pretty-v2.1.32.js:1819-1822)
+ function TCq(A) {
+   let q = A.toLowerCase();
+   return q.includes("claude-sonnet-4") || q.includes("opus-4-6");
+ }

+++ Added Pk6 (pretty-v2.1.32.js:2620-2622)
+ function Pk6(A, q) {
+   i6.systemPromptSectionCache.set(A, q);
+ }

+++ Added D4 (pretty-v2.1.32.js:28121-28154)
+ function D4() {
+   let A = (() => {
+       switch (u48()) {
+         case "local":
+           return Y4K;
+         case "staging":
+           return K4K ?? b48;
+         case "prod":
+           return b48;
+       }
+     })(),
+     q = process.env.CLAUDE_CODE_CUSTOM_OAUTH_URL;
+   if (q) {
+     let Y = q.replace(/\/$/, "");
+     if (!z4K.includes(Y))
+       throw Error("CLAUDE_CODE_CUSTOM_OAUTH_URL is not an approved endpoint.");
+     A = {
+       ...A,
+       BASE_API_URL: Y,
+       CONSOLE_AUTHORIZE_URL: `${Y}/oauth/authorize`,
+       CLAUDE_AI_AUTHORIZE_URL: `${Y}/oauth/authorize`,
+       TOKEN_URL: `${Y}/v1/oauth/token`,
+       API_KEY_URL: `${Y}/api/oauth/claude_cli/create_api_key`,
+       ROLES_URL: `${Y}/api/oauth/claude_cli/roles`,
+       CONSOLE_SUCCESS_URL: `${Y}/oauth/code/success?app=claude-code`,
+       CLAUDEAI_SUCCESS_URL: `${Y}/oauth/code/success?app=claude-code`,
+       MANUAL_REDIRECT_URL: `${Y}/oauth/code/callback`,
+       OAUTH_FILE_SUFFIX: "-custom-oauth",
+     };
+   }
+   let K = process.env.CLAUDE_CODE_OAUTH_CLIENT_ID;
+   if (K) A = { ...A, CLIENT_ID: K };
+   return A;
+ }

+++ Added gA6 (pretty-v2.1.32.js:138699-138701)
+ function gA6() {
+   FA1.cache.clear();
+ }

+++ Added MC (pretty-v2.1.32.js:146499-146502)
+ function MC() {
+   if (!w6A) w6A = new Intl.Segmenter(void 0, { granularity: "grapheme" });
+   return w6A;
+ }

+++ Added k27 (pretty-v2.1.32.js:146503-146506)
+ function k27() {
+   if (!H6A) H6A = new Intl.Segmenter(void 0, { granularity: "word" });
+   return H6A;
+ }

+++ Added $6A (pretty-v2.1.32.js:146507-146514)
+ function $6A(A, q) {
+   let K = `${A}:${q}`,
+     Y = E27.get(K);
+   if (!Y)
+     ((Y = new Intl.RelativeTimeFormat("en", { style: A, numeric: q })),
+       E27.set(K, Y));
+   return Y;
+ }

+++ Added _6A (pretty-v2.1.32.js:146515-146518)
+ function _6A() {
+   if (!O6A) O6A = Intl.DateTimeFormat().resolvedOptions().timeZone;
+   return O6A;
+ }

+++ Added T86 (pretty-v2.1.32.js:146873-146875)
+ function T86(A, q) {
+   return A ? dN5 : H$1;
+ }

+++ Added k86 (pretty-v2.1.32.js:147107-147112)
+ function k86() {
+   if (x8("tengu_marble_lantern_disabled", !1)) return { hasAccess: !1 };
+   if (s7() !== "firstParty")
+     return { hasAccess: !x8("tengu_marble_lantern_3p_disabled", !1) };
+   return { hasAccess: !U8() };
+ }

+++ Added d27 (pretty-v2.1.32.js:147335-147344)
+ function d27(A = !1) {
+   let q = s7() !== "firstParty";
+   return {
+     value: q ? "claude-opus-4-6[1m]" : "opus[1m]",
+     label: "Opus (1M context)",
+     description: `Opus 4.6 for long sessions${q ? "" : ` · ${Nb(T86(!0, A))}`}`,
+     descriptionForModel:
+       "Opus 4.6 with 1M context window - for long sessions with large codebases",
+   };
+ }

+++ Added F8 (pretty-v2.1.32.js:147595-147599)
+ function F8() {
+   if (!$6(process.env.CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS)) return !1;
+   if (!x8("tengu_amber_flint", !1)) return !1;
+   return !0;
+ }

+++ Added XT5 (pretty-v2.1.32.js:147611-147613)
+ function XT5(A) {
+   return A?.agentType === "subagent";
+ }

+++ Added n27 (pretty-v2.1.32.js:147614-147618)
+ function n27() {
+   let A = v6A();
+   if (!XT5(A) || !A.subagentName) return;
+   return A.isBuiltIn ? A.subagentName : "user-defined";
+ }

+++ Added BT5 (pretty-v2.1.32.js:148275-148282)
+ function BT5() {
+   return {
+     slack_team_id: "",
+     is_enterprise_install: !1,
+     trigger: "",
+     creation_method: "",
+   };
+ }

+++ Added Ly1 (pretty-v2.1.32.js:168436-168438)
+ function Ly1() {
+   return f7("policySettings")?.sandbox?.network?.allowManagedDomainsOnly === !0;
+ }

+++ Added GD7 (pretty-v2.1.32.js:168920-169104)
+ var GD7 = v(() => {
+   MD7 = `Use this tool to create and manage a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user.
+ It also helps the user understand the progress of the task and overall progress of their requests.
+ 
+ ## When to Use This Tool
+ Use this tool proactively in these scenarios:
+ 
+ 1. Complex multi-step tasks - When a task requires 3 or more distinct steps or actions
+ 2. Non-trivial and complex tasks - Tasks that require careful planning or multiple operations
+ 3. User explicitly requests todo list - When the user directly asks you to use the todo list
+ 4. User provides multiple tasks - When users provide a list of things to be done (numbered or comma-separated)
+ 5. After receiving new instructions - Immediately capture user requirements as todos
+ 6. When you start working on a task - Mark it as in_progress BEFORE beginning work. Ideally you should only have one todo as in_progress at a time
+ 7. After completing a task - Mark it as completed and add any new follow-up tasks discovered during implementation
+ 
+ ## When NOT to Use This Tool
+ 
+ Skip using this tool when:
+ 1. There is only a single, straightforward task
+ 2. The task is trivial and tracking it provides no organizational benefit
+ 3. The task can be completed in less than 3 trivial steps
+ 4. The task is purely conversational or informational
+ 
+ NOTE that you should not use this tool if there is only one trivial task to do. In this case you are better off just doing the task directly.
+ 
+ ## Examples of When to Use the Todo List
+ 
+ <example>
+ User: I want to add a dark mode toggle to the application settings. Make sure you run the tests and build when you're done!
+ Assistant: I'll help add a dark mode toggle to your application settings. Let me create a todo list to track this implementation.
+ *Creates todo list with the following items:*
+ 1. Creating dark mode toggle component in Settings page
+ 2. Adding dark mode state management (context/store)
+ 3. Implementing CSS-in-JS styles for dark theme
+ 4. Updating existing components to support theme switching
+ 5. Running tests and build process, addressing any failures or errors that occur
+ *Begins working on the first task*
+ 
+ <reasoning>
+ The assistant used the todo list because:
+ 1. Adding dark mode is a multi-step feature requiring UI, state management, and styling changes
+ 2. The user explicitly requested tests and build be run afterward
+ 3. The assistant inferred that tests and build need to pass by adding "Ensure tests and build succeed" as the final task
+ </reasoning>
+ </example>
+ 
+ <example>
+ User: Help me rename the function getCwd to getCurrentWorkingDirectory across my project
+ Assistant: Let me first search through your codebase to find all occurrences of 'getCwd'.
+ *Uses grep or search tools to locate all instances of getCwd in the codebase*
+ Assistant: I've found 15 instances of 'getCwd' across 8 different files. Let me create a todo list to track these changes.
+ *Creates todo list with specific items for each file that needs updating*
+ 
+ <reasoning>
+ The assistant used the todo list because:
+ 1. First, the assistant searched to understand the scope of the task
+ 2. Upon finding multiple occurrences across different files, it determined this was a complex task with multiple steps
+ 3. The todo list helps ensure every instance is tracked and updated systematically
+ 4. This approach prevents missing any occurrences and maintains code consistency
+ </reasoning>
+ </example>
+ 
+ 
+ <example>
+ User: I need to implement these features for my e-commerce site: user registration, product catalog, shopping cart, and checkout flow.
+ Assistant: I'll help implement these features. First, let's add all the features to the todo list.
+ *Creates a todo list breaking down each feature into specific tasks based on the project architecture*
+ Assistant: Let's start with user registration. This will involve creating database models, API endpoints, and frontend forms that integrate with your existing authentication system.
+ 
+ <reasoning>
+ The assistant used the todo list because:
+ 1. The user provided multiple complex features to implement in a comma separated list
+ 2. The todo list helps organize these large features into manageable tasks
+ 3. This approach allows for tracking progress across the entire implementation
+ </reasoning>
+ </example>
+ 
+ <example>
+ User: Can you help optimize my React application? It's rendering slowly and has performance issues.</user>
+ Assistant: I'll help optimize your React application. First, let me examine your codebase to identify potential performance bottlenecks.
+ *Reviews component structure, render patterns, state management, and data fetching*
+ Assistant: After analyzing your codebase, I've identified several performance issues. Let me create a todo list to track our optimization efforts.
+ *Creates todo list with items like: 1) Implementing memoization for expensive calculations in ProductList, 2) Adding virtualization for long lists in Dashboard, 3) Optimizing image loading in Gallery component, 4) Fixing state update loops in ShoppingCart, 5) Reviewing bundle size and implementing code splitting*
+ Let's start by implementing memoization for the expensive calculations in your ProductList component.</assistant>
+ 
+ <reasoning>
+ The assistant used the todo list because:
+ 1. First, the assistant examined the codebase to identify specific performance issues
+ 2. Based on this analysis, it identified multiple optimization opportunities
+ 3. Performance optimization is a non-trivial task requiring multiple steps
+ 4. The todo list helps methodically track improvements across different components
+ 5. This systematic approach ensures all performance bottlenecks are addressed
+ </reasoning>
+ </example>
+ 
+ ## Examples of When NOT to Use the Todo List
+ 
+ <example>
+ User: How do I print 'Hello World' in Python?
+ Assistant: In Python, you can print "Hello World" with this simple code:
+ 
+ python
+ print("Hello World")
+ 
+ This will output the text "Hello World" to the console when executed.</assistant>
+ 
+ <reasoning>
+ The assistant did not use the todo list because this is a single, trivial task that can be completed in one step. There's no need to track multiple tasks or steps for such a straightforward request.
+ </reasoning>
+ </example>
+ 
+ <example>
+ User: What does the git status command do?
+ Assistant: The git status command shows the current state of your working directory and staging area. It displays which changes have been staged, which haven't, and which files aren't being tracked by Git. This is a fundamental command for understanding the current state of your repository before making commits.
+ 
+ <reasoning>
+ The assistant did not use the todo list because this is an informational request with no actual coding task to complete. The user is simply asking for an explanation, not for the assistant to perform multiple steps or tasks.
+ </reasoning>
+ </example>
+ 
+ <example>
+ User: Can you add a comment to the calculateTotal function to explain what it does?
+ Assistant: Sure, let me add a comment to the calculateTotal function to explain what it does.
+ * Uses the ${aq} tool to add a comment to the calculateTotal function *
+ 
+ <reasoning>
+ The assistant did not use the todo list because this is a single, straightforward task confined to one location in the code. Adding a comment doesn't require tracking multiple steps or systematic organization.
+ </reasoning>
+ </example>
+ 
+ <example>
+ User: Run npm install for me and tell me what happens.
+ Assistant: I'll run the npm install command for you.
+ 
+ *Executes: npm install*
+ 
+ The command completed successfully. Here's the output:
+ [Output of npm install command]
+ 
+ All dependencies have been installed according to your package.json file.
+ 
+ <reasoning>
+ The assistant did not use the todo list because this is a single command execution with immediate results. There are no multiple steps to track or organize, making the todo list unnecessary for this straightforward task.
+ </reasoning>
+ </example>
+ 
+ ## Task States and Management
+ 
+ 1. **Task States**: Use these states to track progress:
+    - pending: Task not yet started
+    - in_progress: Currently working on (limit to ONE task at a time)
+    - completed: Task finished successfully
+ 
+    **IMPORTANT**: Task descriptions must have two forms:
+    - content: The imperative form describing what needs to be done (e.g., "Run tests", "Build the project")
+    - activeForm: The present continuous form shown during execution (e.g., "Running tests", "Building the project")
+ 
+ 2. **Task Management**:
+    - Update task status in real-time as you work
+    - Mark tasks complete IMMEDIATELY after finishing (don't batch completions)
+    - Exactly ONE task must be in_progress at any time (not less, not more)
+    - Complete current tasks before starting new ones
+    - Remove tasks that are no longer relevant from the list entirely
+ 
+ 3. **Task Completion Requirements**:
+    - ONLY mark a task as completed when you have FULLY accomplished it
+    - If you encounter errors, blockers, or cannot finish, keep the task as in_progress
+    - When blocked, create a new task describing what needs to be resolved
+    - Never mark a task as completed if:
+      - Tests are failing
+      - Implementation is partial
+      - You encountered unresolved errors
+      - You couldn't find necessary files or dependencies
+ 
+ 4. **Task Breakdown**:
+    - Create specific, actionable items
+    - Break complex tasks into smaller, manageable steps
+    - Use clear, descriptive task names
+    - Always provide both forms:
+      - content: "Fix authentication bug"
+      - activeForm: "Fixing authentication bug"
+ 
+ When in doubt, use this tool. Being proactive with task management demonstrates attentiveness and ensures you complete all requirements successfully.
+ `;
+ });

+++ Added pW7 (pretty-v2.1.32.js:186820-186838)
+ function pW7() {
+   if (!process.stdin.isTTY || zC1) return;
+   ((zC1 = !0), (sn = ""));
+   try {
+     (process.stdin.setEncoding("utf8"),
+       process.stdin.setRawMode(!0),
+       process.stdin.ref(),
+       (wC1 = () => {
+         let A = process.stdin.read();
+         while (A !== null) {
+           if (typeof A === "string") Zp5(A);
+           A = process.stdin.read();
+         }
+       }),
+       process.stdin.on("readable", wC1));
+   } catch {
+     zC1 = !1;
+   }
+ }

+++ Added Zp5 (pretty-v2.1.32.js:186839-186876)
+ function Zp5(A) {
+   let q = 0;
+   while (q < A.length) {
+     let K = A[q],
+       Y = K.charCodeAt(0);
+     if (Y === 3) {
+       (Y71(), process.exit(130));
+       return;
+     }
+     if (Y === 4) {
+       Y71();
+       return;
+     }
+     if (Y === 127 || Y === 8) {
+       if (sn.length > 0) sn = sn.slice(0, -1);
+       q++;
+       continue;
+     }
+     if (Y === 27) {
+       q++;
+       while (q < A.length && !(A.charCodeAt(q) >= 64 && A.charCodeAt(q) <= 126))
+         q++;
+       if (q < A.length) q++;
+       continue;
+     }
+     if (Y < 32 && Y !== 9 && Y !== 10 && Y !== 13) {
+       q++;
+       continue;
+     }
+     if (Y === 13) {
+       ((sn += `
+ `),
+         q++);
+       continue;
+     }
+     ((sn += K), q++);
+   }
+ }

+++ Added Y71 (pretty-v2.1.32.js:186877-186881)
+ function Y71() {
+   if (!zC1) return;
+   if (((zC1 = !1), wC1))
+     (process.stdin.removeListener("readable", wC1), (wC1 = null));
+ }

+++ Added dW7 (pretty-v2.1.32.js:186882-186886)
+ function dW7() {
+   Y71();
+   let A = sn.trim();
+   return ((sn = ""), A);
+ }

+++ Added eG9 (pretty-v2.1.32.js:246383-246390)
+ async function eG9(A) {
+   let q = `${D4().BASE_API_URL}/api/claude_code_penguin_mode`,
+     K =
+       "accessToken" in A
+         ? { Authorization: `Bearer ${A.accessToken}`, "anthropic-beta": Wf }
+         : { "x-api-key": A.apiKey };
+   return (await rA.get(q, { headers: K })).data.enabled;
+ }

+++ Added X01 (pretty-v2.1.32.js:251710-252162)
+ function X01(A) {
+   let q = A1(100),
+     {
+       option: K,
+       isFocused: Y,
+       isSelected: z,
+       shouldShowDownArrow: w,
+       shouldShowUpArrow: H,
+       maxIndexWidth: O,
+       index: $,
+       inputValue: _,
+       onInputChange: J,
+       onSubmit: X,
+       onExit: D,
+       layout: j,
+       children: M,
+       showLabel: W,
+       onOpenEditor: G,
+       resetCursorOnUpdate: P,
+       onImagePaste: V,
+       pastedContents: Z,
+       onRemoveImage: N,
+       imagesSelected: T,
+       selectedImageIndex: k,
+       onImagesSelectedChange: y,
+       onSelectedImageIndexChange: u,
+     } = A,
+     S = W === void 0 ? !1 : W,
+     m = P === void 0 ? !1 : P,
+     b = k === void 0 ? 0 : k,
+     U;
+   if (q[0] !== Z)
+     ((U = Z ? Object.values(Z).filter(Gf9) : []), (q[0] = Z), (q[1] = U));
+   else U = q[1];
+   let g = U,
+     x = S || K.showLabelWithValue === !0,
+     [p, n] = ZY.useState(_.length),
+     r;
+   if (q[2] !== _.length || q[3] !== Y || q[4] !== m)
+     ((r = () => {
+       if (m && Y) n(_.length);
+     }),
+       (q[2] = _.length),
+       (q[3] = Y),
+       (q[4] = m),
+       (q[5] = r));
+   else r = q[5];
+   let z1;
+   if (q[6] !== _ || q[7] !== Y || q[8] !== m)
+     ((z1 = [m, Y, _]), (q[6] = _), (q[7] = Y), (q[8] = m), (q[9] = z1));
+   else z1 = q[9];
+   ZY.useEffect(r, z1);
+   let f1;
+   if (q[10] !== _ || q[11] !== J || q[12] !== G)
+     ((f1 = () => {
+       G?.(_, J);
+     }),
+       (q[10] = _),
+       (q[11] = J),
+       (q[12] = G),
+       (q[13] = f1));
+   else f1 = q[13];
+   let Z1 = Y && !!G,
+     H1;
+   if (q[14] !== Z1)
+     ((H1 = { context: "Chat", isActive: Z1 }), (q[14] = Z1), (q[15] = H1));
+   else H1 = q[15];
+   DA("chat:externalEditor", f1, H1);
+   let D1;
+   if (q[16] !== V)
+     ((D1 = () => {
+       if (!V) return;
+       _01().then((G6) => {
+         if (G6) V(G6.base64, G6.mediaType, void 0, G6.dimensions);
+       });
+     }),
+       (q[16] = V),
+       (q[17] = D1));
+   else D1 = q[17];
+   let t = Y && !!V,
+     e;
+   if (q[18] !== t)
+     ((e = { context: "Chat", isActive: t }), (q[18] = t), (q[19] = e));
+   else e = q[19];
+   DA("chat:imagePaste", D1, e);
+   let G1;
+   if (q[20] !== g || q[21] !== N)
+     ((G1 = () => {
+       if (g.length > 0 && N) N(g[g.length - 1].id);
+     }),
+       (q[20] = g),
+       (q[21] = N),
+       (q[22] = G1));
+   else G1 = q[22];
+   let w1 = Y && !T && _ === "" && g.length > 0 && !!N,
+     V1;
+   if (q[23] !== w1)
+     ((V1 = { context: "Attachments", isActive: w1 }),
+       (q[23] = w1),
+       (q[24] = V1));
+   else V1 = q[24];
+   DA("attachments:remove", G1, V1);
+   let E1, q1;
+   if (q[25] !== g.length || q[26] !== u || q[27] !== b)
+     ((E1 = () => {
+       if (g.length > 1) u?.((b + 1) % g.length);
+     }),
+       (q1 = () => {
+         if (g.length > 1) u?.((b - 1 + g.length) % g.length);
+       }),
+       (q[25] = g.length),
+       (q[26] = u),
+       (q[27] = b),
+       (q[28] = E1),
+       (q[29] = q1));
+   else ((E1 = q[28]), (q1 = q[29]));
+   let s;
+   if (q[30] !== g || q[31] !== y || q[32] !== N || q[33] !== u || q[34] !== b)
+     ((s = () => {
+       let G6 = g[b];
+       if (G6 && N)
+         if ((N(G6.id), g.length <= 1)) y?.(!1);
+         else u?.(Math.min(b, g.length - 2));
+     }),
+       (q[30] = g),
+       (q[31] = y),
+       (q[32] = N),
+       (q[33] = u),
+       (q[34] = b),
+       (q[35] = s));
+   else s = q[35];
+   let j1;
+   if (q[36] !== y)
+     ((j1 = () => {
+       y?.(!1);
+     }),
+       (q[36] = y),
+       (q[37] = j1));
+   else j1 = q[37];
+   let J1;
+   if (q[38] !== E1 || q[39] !== q1 || q[40] !== s || q[41] !== j1)
+     ((J1 = {
+       "attachments:next": E1,
+       "attachments:previous": q1,
+       "attachments:remove": s,
+       "attachments:exit": j1,
+     }),
+       (q[38] = E1),
+       (q[39] = q1),
+       (q[40] = s),
+       (q[41] = j1),
+       (q[42] = J1));
+   else J1 = q[42];
+   let o = Y && !!T,
+     _1;
+   if (q[43] !== o)
+     ((_1 = { context: "Attachments", isActive: o }), (q[43] = o), (q[44] = _1));
+   else _1 = q[44];
+   l7(J1, _1);
+   let O1;
+   if (q[45] !== y)
+     ((O1 = (G6, P6) => {
+       if (P6.upArrow) y?.(!1);
+     }),
+       (q[45] = y),
+       (q[46] = O1));
+   else O1 = q[46];
+   let N1 = Y && !!T,
+     L1;
+   if (q[47] !== N1) ((L1 = { isActive: N1 }), (q[47] = N1), (q[48] = L1));
+   else L1 = q[48];
+   Y8(O1, L1);
+   let I1, X1;
+   if (q[49] !== T || q[50] !== Y || q[51] !== y)
+     ((I1 = () => {
+       if (!Y && T) y?.(!1);
+     }),
+       (X1 = [Y, T, y]),
+       (q[49] = T),
+       (q[50] = Y),
+       (q[51] = y),
+       (q[52] = I1),
+       (q[53] = X1));
+   else ((I1 = q[52]), (X1 = q[53]));
+   ZY.useEffect(I1, X1);
+   let S1 = j === "expanded" ? O + 3 : O + 4,
+     v1 = j === "compact" ? 0 : void 0,
+     U1 = `${$}.`,
+     e1;
+   if (q[54] !== O || q[55] !== U1)
+     ((e1 = U1.padEnd(O + 2)), (q[54] = O), (q[55] = U1), (q[56] = e1));
+   else e1 = q[56];
+   let Z6;
+   if (q[57] !== e1)
+     ((Z6 = ZY.default.createElement(f, { dimColor: !0 }, e1)),
+       (q[57] = e1),
+       (q[58] = Z6));
+   else Z6 = q[58];
+   let V6;
+   if (
+     q[59] !== p ||
+     q[60] !== T ||
+     q[61] !== _ ||
+     q[62] !== Y ||
+     q[63] !== D ||
+     q[64] !== V ||
+     q[65] !== J ||
+     q[66] !== X ||
+     q[67] !== K ||
+     q[68] !== x
+   )
+     ((V6 = x
+       ? ZY.default.createElement(
+           ZY.default.Fragment,
+           null,
+           ZY.default.createElement(
+             f,
+             { color: Y ? "suggestion" : void 0 },
+             K.label,
+           ),
+           Y
+             ? ZY.default.createElement(
+                 ZY.default.Fragment,
+                 null,
+                 ZY.default.createElement(
+                   f,
+                   { color: "suggestion" },
+                   K.labelValueSeparator ?? ", ",
+                 ),
+                 ZY.default.createElement(sK, {
+                   value: _,
+                   onChange: (G6) => {
+                     (J(G6), K.onChange(G6));
+                   },
+                   onSubmit: X,
+                   onExit: D,
+                   placeholder: K.placeholder,
+                   focus: !T,
+                   showCursor: !0,
+                   cursorOffset: p,
+                   onChangeCursorOffset: n,
+                   columns: 80,
+                   onImagePaste: V,
+                   onPaste: (G6) => {
+                     let P6 = _.slice(0, p),
+                       U6 = _.slice(p),
+                       W1 = P6 + G6 + U6;
+                     (J(W1), K.onChange(W1), n(P6.length + G6.length));
+                   },
+                 }),
+               )
+             : _ &&
+                 ZY.default.createElement(
+                   f,
+                   null,
+                   K.labelValueSeparator ?? ", ",
+                   _,
+                 ),
+         )
+       : Y
+         ? ZY.default.createElement(sK, {
+             value: _,
+             onChange: (G6) => {
+               (J(G6), K.onChange(G6));
+             },
+             onSubmit: X,
+             onExit: D,
+             placeholder:
+               K.placeholder || (typeof K.label === "string" ? K.label : void 0),
+             focus: !T,
+             showCursor: !0,
+             cursorOffset: p,
+             onChangeCursorOffset: n,
+             columns: 80,
+             onImagePaste: V,
+             onPaste: (G6) => {
+               let P6 = _.slice(0, p),
+                 U6 = _.slice(p),
+                 W1 = P6 + G6 + U6;
+               (J(W1), K.onChange(W1), n(P6.length + G6.length));
+             },
+           })
+         : ZY.default.createElement(
+             f,
+             { color: _ ? void 0 : "inactive" },
+             _ || K.placeholder || K.label,
+           )),
+       (q[59] = p),
+       (q[60] = T),
+       (q[61] = _),
+       (q[62] = Y),
+       (q[63] = D),
+       (q[64] = V),
+       (q[65] = J),
+       (q[66] = X),
+       (q[67] = K),
+       (q[68] = x),
+       (q[69] = V6));
+   else V6 = q[69];
+   let K6;
+   if (q[70] !== M || q[71] !== v1 || q[72] !== Z6 || q[73] !== V6)
+     ((K6 = ZY.default.createElement(
+       I,
+       { flexDirection: "row", flexShrink: v1 },
+       Z6,
+       M,
+       V6,
+     )),
+       (q[70] = M),
+       (q[71] = v1),
+       (q[72] = Z6),
+       (q[73] = V6),
+       (q[74] = K6));
+   else K6 = q[74];
+   let d6;
+   if (q[75] !== Y || q[76] !== z || q[77] !== w || q[78] !== H || q[79] !== K6)
+     ((d6 = ZY.default.createElement(
+       Wo,
+       {
+         isFocused: Y,
+         isSelected: z,
+         shouldShowDownArrow: w,
+         shouldShowUpArrow: H,
+       },
+       K6,
+     )),
+       (q[75] = Y),
+       (q[76] = z),
+       (q[77] = w),
+       (q[78] = H),
+       (q[79] = K6),
+       (q[80] = d6));
+   else d6 = q[80];
+   let AA;
+   if (
+     q[81] !== S1 ||
+     q[82] !== Y ||
+     q[83] !== z ||
+     q[84] !== K.description ||
+     q[85] !== K.dimDescription
+   )
+     ((AA =
+       K.description &&
+       ZY.default.createElement(
+         I,
+         { paddingLeft: S1 },
+         ZY.default.createElement(
+           f,
+           {
+             dimColor: K.dimDescription !== !1,
+             color: z ? "success" : Y ? "suggestion" : void 0,
+           },
+           K.description,
+         ),
+       )),
+       (q[81] = S1),
+       (q[82] = Y),
+       (q[83] = z),
+       (q[84] = K.description),
+       (q[85] = K.dimDescription),
+       (q[86] = AA));
+   else AA = q[86];
+   let r1;
+   if (q[87] !== S1 || q[88] !== g || q[89] !== T || q[90] !== Y || q[91] !== b)
+     ((r1 =
+       g.length > 0 &&
+       ZY.default.createElement(
+         I,
+         { flexDirection: "row", gap: 1, paddingLeft: S1 },
+         g.map((G6, P6) =>
+           ZY.default.createElement(S26, {
+             key: G6.id,
+             imageId: G6.id,
+             isSelected: !!T && P6 === b,
+           }),
+         ),
+         ZY.default.createElement(
+           I,
+           { flexGrow: 1, justifyContent: "flex-start", flexDirection: "row" },
+           ZY.default.createElement(
+             f,
+             { dimColor: !0 },
+             T
+               ? ZY.default.createElement(
+                   pA,
+                   null,
+                   g.length > 1 &&
+                     ZY.default.createElement(
+                       ZY.default.Fragment,
+                       null,
+                       ZY.default.createElement(NA, {
+                         action: "attachments:next",
+                         context: "Attachments",
+                         fallback: "→",
+                         description: "next",
+                       }),
+                       ZY.default.createElement(NA, {
+                         action: "attachments:previous",
+                         context: "Attachments",
+                         fallback: "←",
+                         description: "prev",
+                       }),
+                     ),
+                   ZY.default.createElement(NA, {
+                     action: "attachments:remove",
+                     context: "Attachments",
+                     fallback: "backspace",
+                     description: "remove",
+                   }),
+                   ZY.default.createElement(NA, {
+                     action: "attachments:exit",
+                     context: "Attachments",
+                     fallback: "esc",
+                     description: "cancel",
+                   }),
+                 )
+               : Y
+                 ? "(↓ to select)"
+                 : null,
+           ),
+         ),
+       )),
+       (q[87] = S1),
+       (q[88] = g),
+       (q[89] = T),
+       (q[90] = Y),
+       (q[91] = b),
+       (q[92] = r1));
+   else r1 = q[92];
+   let H6;
+   if (q[93] !== j)
+     ((H6 = j === "expanded" && ZY.default.createElement(f, null, " ")),
+       (q[93] = j),
+       (q[94] = H6));
+   else H6 = q[94];
+   let j6;
+   if (q[95] !== d6 || q[96] !== AA || q[97] !== r1 || q[98] !== H6)
+     ((j6 = ZY.default.createElement(
+       I,
+       { flexDirection: "column", flexShrink: 0 },
+       d6,
+       AA,
+       r1,
+       H6,
+     )),
+       (q[95] = d6),
+       (q[96] = AA),
+       (q[97] = r1),
+       (q[98] = H6),
+       (q[99] = j6));
+   else j6 = q[99];
+   return j6;
+ }

+++ Added Ef9 (pretty-v2.1.32.js:252953-252955)
+ function Ef9(A) {
+   return A.type === "image";
+ }

+++ Added kf9 (pretty-v2.1.32.js:252956-252958)
+ function kf9(A) {
+   return A.type === "image";
+ }

+++ Added Qo (pretty-v2.1.32.js:274213-274232)
+ var Qo = v(() => {
+   g4();
+   _O6();
+   F6();
+   BA();
+   ((zA4 = `Search for or select deferred tools to make them available for use.
+ 
+ **MANDATORY PREREQUISITE - THIS IS A HARD REQUIREMENT**
+ 
+ You MUST use this tool to load deferred tools BEFORE calling them directly.
+ 
+ This is a BLOCKING REQUIREMENT - deferred tools listed below are NOT available until you load them using this tool. Both query modes (keyword search and direct selection) load the returned tools — once a tool appears in the results, it is immediately available to call.${wA4}`),
+     (Ix9 = `Search for or select deferred tools to make them available for use.
+ 
+ **MANDATORY PREREQUISITE - THIS IS A HARD REQUIREMENT**
+ 
+ You MUST use this tool to load deferred tools BEFORE calling them directly.
+ 
+ This is a BLOCKING REQUIREMENT - deferred tools are NOT available until you load them using this tool. Look for <available-deferred-tools> messages in the conversation for the list of tools you can discover. Both query modes (keyword search and direct selection) load the returned tools — once a tool appears in the results, it is immediately available to call.${wA4}`));
+ });

+++ Added Rd9 (pretty-v2.1.32.js:295600-295605)
+ function Rd9(A) {
+   if (Number(process.env.SLASH_COMMAND_TOOL_CHAR_BUDGET))
+     return Number(process.env.SLASH_COMMAND_TOOL_CHAR_BUDGET);
+   if (A) return Math.floor(A * kd9 * Ed9);
+   return Ld9;
+ }

+++ Added Ed9 (pretty-v2.1.32.js:295650-295650)
+ var Ed9 = 0.02,

+++ Added wu1 (pretty-v2.1.32.js:295655-295686)
+ var wu1 = v(() => {
+   W_();
+   _6();
+   k6();
+   W_();
+   er1();
+   Wz();
+   DjA = qA(async (A) => {
+     return `Execute a skill within the main conversation
+ 
+ When users ask you to perform tasks, check if any of the available skills match. Skills provide specialized capabilities and domain knowledge.
+ 
+ When users reference a "slash command" or "/<something>" (e.g., "/commit", "/review-pr"), they are referring to a skill. Use this tool to invoke it.
+ 
+ How to invoke:
+ - Use this tool with the skill name and optional arguments
+ - Examples:
+   - \`skill: "pdf"\` - invoke the pdf skill
+   - \`skill: "commit", args: "-m 'Fix bug'"\` - invoke with arguments
+   - \`skill: "review-pr", args: "123"\` - invoke with arguments
+   - \`skill: "ms-office-suite:pdf"\` - invoke using fully qualified name
+ 
+ Important:
+ - Available skills are listed in system-reminder messages in the conversation
+ - When a skill matches the user's request, this is a BLOCKING REQUIREMENT: invoke the relevant Skill tool BEFORE generating any other response about the task
+ - NEVER mention a skill without actually calling this tool
+ - Do not invoke a skill that is already running
+ - Do not use this tool for built-in CLI commands (like /help, /clear, etc.)
+ - If you see a <${Hf}> tag in the current conversation turn, the skill has ALREADY been loaded - follow the instructions directly instead of calling this tool again
+ `;
+   });
+ });

+++ Added K94 (pretty-v2.1.32.js:297043-297045)
+ function K94() {
+   ((Kj1.length = 0), b$6());
+ }

+++ Added Z94 (pretty-v2.1.32.js:298004-298007)
+ function Z94(A, q) {
+   for (let [K, Y] of Object.entries(A))
+     if (Y.type === "local_agent" && Y.status === "running") va(K, q);
+ }

+++ Added f94 (pretty-v2.1.32.js:298015-298028)
+ function f94(A, q, K) {
+   BY(A, K, (Y) => {
+     if (Y.status !== "running") return Y;
+     return {
+       ...Y,
+       progress: {
+         ...Y.progress,
+         toolUseCount: Y.progress?.toolUseCount ?? 0,
+         tokenCount: Y.progress?.tokenCount ?? 0,
+         summary: q,
+       },
+     };
+   });
+ }

+++ Added sY4 (pretty-v2.1.32.js:301205-301290)
+ function sY4(A) {
+   let q = `Your task is to create a detailed summary of the RECENT portion of the conversation — the messages that follow earlier retained context. The earlier messages are being kept intact and do NOT need to be summarized. Focus your summary on what was discussed, learned, and accomplished in the recent messages only.
+ 
+ Before providing your final summary, wrap your analysis in <analysis> tags to organize your thoughts and ensure you've covered all necessary points. In your analysis process:
+ 
+ 1. Analyze the recent messages chronologically. For each section thoroughly identify:
+    - The user's explicit requests and intents
+    - Your approach to addressing the user's requests
+    - Key decisions, technical concepts and code patterns
+    - Specific details like:
+      - file names
+      - full code snippets
+      - function signatures
+      - file edits
+   - Errors that you ran into and how you fixed them
+   - Pay special attention to specific user feedback that you received, especially if the user told you to do something differently.
+ 2. Double-check for technical accuracy and completeness, addressing each required element thoroughly.
+ 
+ Your summary should include the following sections:
+ 
+ 1. Primary Request and Intent: Capture the user's explicit requests and intents from the recent messages
+ 2. Key Technical Concepts: List important technical concepts, technologies, and frameworks discussed recently.
+ 3. Files and Code Sections: Enumerate specific files and code sections examined, modified, or created. Include full code snippets where applicable and include a summary of why this file read or edit is important.
+ 4. Errors and fixes: List errors encountered and how they were fixed.
+ 5. Problem Solving: Document problems solved and any ongoing troubleshooting efforts.
+ 6. All user messages: List ALL user messages from the recent portion that are not tool results.
+ 7. Pending Tasks: Outline any pending tasks from the recent messages.
+ 8. Current Work: Describe precisely what was being worked on immediately before this summary request.
+ 9. Optional Next Step: List the next step related to the most recent work. Include direct quotes from the most recent conversation.
+ 
+ Here's an example of how your output should be structured:
+ 
+ <example>
+ <analysis>
+ [Your thought process, ensuring all points are covered thoroughly and accurately]
+ </analysis>
+ 
+ <summary>
+ 1. Primary Request and Intent:
+    [Detailed description]
+ 
+ 2. Key Technical Concepts:
+    - [Concept 1]
+    - [Concept 2]
+ 
+ 3. Files and Code Sections:
+    - [File Name 1]
+       - [Summary of why this file is important]
+       - [Important Code Snippet]
+ 
+ 4. Errors and fixes:
+     - [Error description]:
+       - [How you fixed it]
+ 
+ 5. Problem Solving:
+    [Description]
+ 
+ 6. All user messages:
+     - [Detailed non tool use user message]
+ 
+ 7. Pending Tasks:
+    - [Task 1]
+ 
+ 8. Current Work:
+    [Precise description of current work]
+ 
+ 9. Optional Next Step:
+    [Optional Next step to take]
+ 
+ </summary>
+ </example>
+ 
+ Please provide your summary based on the RECENT messages only (after the retained earlier context), following this structure and ensuring precision and thoroughness in your response.
+ `;
+   if (A && A.trim() !== "")
+     q += `
+ 
+ Additional Instructions:
+ ${A}`;
+   return (
+     (q += `
+ 
+ IMPORTANT: Do NOT use any tools. You MUST respond with ONLY the <summary>...</summary> block as your text output.`),
+     q
+   );
+ }

+++ Added VMA (pretty-v2.1.32.js:302250-302254)
+ function VMA(A) {
+   if (typeof A !== "string") return null;
+   if (Pz4.test(A) || Gl9.test(A)) return A;
+   return null;
+ }

+++ Added sS (pretty-v2.1.32.js:302260-302263)
+ var sS = v(() => {
+   ((Pz4 = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i),
+     (Gl9 = /^[a-z][a-z0-9]*(_[a-z][a-z0-9]*)*_[0-9A-Za-z]+$/));
+ });

+++ Added xM1 (pretty-v2.1.32.js:356484-356486)
+ var xM1 = v(() => {
+   PE4 = new Map();
+ });

+++ Added PVA (pretty-v2.1.32.js:356929-356939)
+ var PVA = `
+ # Agent Teammate Communication
+ 
+ IMPORTANT: You are running as an agent in a team. To communicate with anyone on your team:
+ - Use the SendMessage tool with type \`message\` to send messages to specific teammates
+ - Use the SendMessage tool with type \`broadcast\` sparingly for team-wide announcements
+ 
+ Just writing a response in text is not visible to others on your team - you MUST use the SendMessage tool.
+ 
+ The user interacts primarily with the team lead. Your work is coordinated through the task system and teammate messaging.
+ `;

+++ Added Rm1 (pretty-v2.1.32.js:358236-358264)
+ function Rm1(A) {
+   for (let q = A.length - 1; q >= 0; q--) {
+     let K = A[q];
+     if (K?.type !== "assistant") continue;
+     for (let Y of K.message.content)
+       if (
+         Y.type === "tool_use" &&
+         Y.name === wB &&
+         typeof Y.input === "object" &&
+         Y.input !== null &&
+         "type" in Y.input &&
+         Y.input.type === "message" &&
+         "recipient" in Y.input &&
+         typeof Y.input.recipient === "string" &&
+         Y.input.recipient.toLowerCase() !== h2.toLowerCase()
+       ) {
+         let z = Y.input.recipient,
+           w =
+             "summary" in Y.input && typeof Y.input.summary === "string"
+               ? Y.input.summary
+               : "content" in Y.input && typeof Y.input.content === "string"
+                 ? Y.input.content.slice(0, 80)
+                 : void 0;
+         if (w) return `[to ${z}] ${w}`;
+       }
+     break;
+   }
+   return;
+ }

+++ Added ML4 (pretty-v2.1.32.js:366426-366432)
+ function ML4() {
+   if (AW1)
+     ((Rs = AW1), h(`[TeammateModeSnapshot] Captured from CLI override: ${Rs}`));
+   else
+     ((Rs = M6().teammateMode ?? "auto"),
+       h(`[TeammateModeSnapshot] Captured from config: ${Rs}`));
+ }

+++ Added iL4 (pretty-v2.1.32.js:367679-367692)
+ function iL4(A, q, { verbose: K }) {
+   let Y = typeof A === "string" ? JA(A) : A;
+   if (SDY(Y))
+     return zW1.default.createElement(f, { dimColor: !0 }, "  ", "Created team");
+   if ("success" in Y && "team_name" in Y && "message" in Y) return null;
+   if ("message" in Y)
+     return zW1.default.createElement(f, { dimColor: !0 }, "  ", Y.message);
+   return zW1.default.createElement(
+     f,
+     { dimColor: !0 },
+     "  ",
+     "operation complete",
+   );
+ }

+++ Added Cx4 (pretty-v2.1.32.js:389338-389488)
+ function Cx4(A) {
+   let q = A1(24),
+     { message: K, screen: Y } = A,
+     z = Y === "transcript",
+     w;
+   if (q[0] !== K) ((w = xF1(K) || ""), (q[0] = K), (q[1] = w));
+   else w = q[1];
+   let H = w,
+     O = K.summarizeMetadata;
+   if (O) {
+     let j;
+     if (q[2] === Symbol.for("react.memo_cache_sentinel"))
+       ((j = cK.createElement(
+         I,
+         { minWidth: 2 },
+         cK.createElement(f, { color: "text" }, KY),
+       )),
+         (q[2] = j));
+     else j = q[2];
+     let M;
+     if (q[3] === Symbol.for("react.memo_cache_sentinel"))
+       ((M = cK.createElement(f, { bold: !0 }, "Summarized conversation")),
+         (q[3] = M));
+     else M = q[3];
+     let W;
+     if (q[4] !== z || q[5] !== O)
+       ((W =
+         !z &&
+         cK.createElement(
+           HA,
+           null,
+           cK.createElement(
+             I,
+             { flexDirection: "column" },
+             cK.createElement(
+               f,
+               { dimColor: !0 },
+               "Summarized ",
+               O.messagesSummarized,
+               " messages from this point",
+             ),
+             O.userContext &&
+               cK.createElement(
+                 f,
+                 { dimColor: !0 },
+                 "Context: ",
+                 "“",
+                 O.userContext,
+                 "”",
+               ),
+             cK.createElement(
+               f,
+               { dimColor: !0 },
+               cK.createElement(NA, {
+                 action: "app:toggleTranscript",
+                 context: "Global",
+                 fallback: "ctrl+o",
+                 description: "expand history",
+                 parens: !0,
+               }),
+             ),
+           ),
+         )),
+         (q[4] = z),
+         (q[5] = O),
+         (q[6] = W));
+     else W = q[6];
+     let G;
+     if (q[7] !== z || q[8] !== H)
+       ((G = z && cK.createElement(HA, null, cK.createElement(f, null, H))),
+         (q[7] = z),
+         (q[8] = H),
+         (q[9] = G));
+     else G = q[9];
+     let P;
+     if (q[10] !== W || q[11] !== G)
+       ((P = cK.createElement(
+         I,
+         { flexDirection: "column", marginTop: 1 },
+         cK.createElement(
+           I,
+           { flexDirection: "row" },
+           j,
+           cK.createElement(I, { flexDirection: "column" }, M, W, G),
+         ),
+       )),
+         (q[10] = W),
+         (q[11] = G),
+         (q[12] = P));
+     else P = q[12];
+     return P;
+   }
+   let $;
+   if (q[13] === Symbol.for("react.memo_cache_sentinel"))
+     (($ = cK.createElement(
+       I,
+       { minWidth: 2 },
+       cK.createElement(f, { color: "text" }, KY),
+     )),
+       (q[13] = $));
+   else $ = q[13];
+   let _;
+   if (q[14] !== z)
+     ((_ =
+       !z &&
+       cK.createElement(
+         f,
+         { dimColor: !0 },
+         " ",
+         cK.createElement(NA, {
+           action: "app:toggleTranscript",
+           context: "Global",
+           fallback: "ctrl+o",
+           description: "expand",
+           parens: !0,
+         }),
+       )),
+       (q[14] = z),
+       (q[15] = _));
+   else _ = q[15];
+   let J;
+   if (q[16] !== _)
+     ((J = cK.createElement(
+       I,
+       { flexDirection: "row" },
+       $,
+       cK.createElement(
+         I,
+         { flexDirection: "column" },
+         cK.createElement(f, { bold: !0 }, "Compact summary", _),
+       ),
+     )),
+       (q[16] = _),
+       (q[17] = J));
+   else J = q[17];
+   let X;
+   if (q[18] !== z || q[19] !== H)
+     ((X = z && cK.createElement(HA, null, cK.createElement(f, null, H))),
+       (q[18] = z),
+       (q[19] = H),
+       (q[20] = X));
+   else X = q[20];
+   let D;
+   if (q[21] !== J || q[22] !== X)
+     ((D = cK.createElement(I, { flexDirection: "column", marginTop: 1 }, J, X)),
+       (q[21] = J),
+       (q[22] = X),
+       (q[23] = D));
+   else D = q[23];
+   return D;
+ }

+++ Added SPY (pretty-v2.1.32.js:390565-390583)
+ function SPY(A) {
+   return `Describe your most recent action in 3-5 words using present tense (-ing). Name the file or function, not the branch. Do not use tools.
+ ${
+   A
+     ? `
+ Previous: "${A}" — say something NEW.
+ `
+     : ""
+ }
+ Good: "Reading runAgent.ts"
+ Good: "Fixing null check in validate.ts"
+ Good: "Running auth module tests"
+ Good: "Adding retry logic to fetchUser"
+ 
+ Bad (past tense): "Analyzed the branch diff"
+ Bad (too vague): "Investigating the issue"
+ Bad (too long): "Reviewing full branch diff and AgentTool.tsx integration"
+ Bad (branch name): "Analyzed adam/background-summary branch diff"`;
+ }

+++ Added cx4 (pretty-v2.1.32.js:390584-390650)
+ function cx4(A, q, K, Y) {
+   let z = null,
+     w = null,
+     H = !1,
+     O = null;
+   async function $() {
+     if (H) return;
+     h(`[AgentSummary] Timer fired for agent ${q}`);
+     try {
+       let X = await VW1(q);
+       if (!X || X.length < 3) {
+         h(
+           `[AgentSummary] Skipping summary for ${A}: not enough messages (${X?.length ?? 0})`,
+         );
+         return;
+       }
+       let D = uF1(X),
+         j = { ...K, forkContextMessages: D };
+       (h(`[AgentSummary] Forking for summary, ${D.length} messages in context`),
+         (z = new AbortController()));
+       let M = async () => ({
+           behavior: "deny",
+           message: "No tools needed for summary",
+           decisionReason: { type: "other", reason: "summary only" },
+         }),
+         W = await Lv({
+           promptMessages: [p6({ content: SPY(O) })],
+           cacheSafeParams: j,
+           canUseTool: M,
+           querySource: "agent_summary",
+           forkLabel: "agent_summary",
+           overrides: { abortController: z },
+           skipTranscript: !0,
+         });
+       if (H) return;
+       for (let G of W.messages) {
+         if (G.type !== "assistant") continue;
+         if (G.isApiErrorMessage) {
+           h(`[AgentSummary] Skipping API error message for ${A}`);
+           continue;
+         }
+         let P = G.message.content.find((V) => V.type === "text");
+         if (P?.type === "text" && P.text.trim()) {
+           let V = P.text.trim();
+           (h(`[AgentSummary] Summary result for ${A}: ${V}`),
+             (O = V),
+             f94(A, V, Y));
+           break;
+         }
+       }
+     } catch (X) {
+       if (!H && X instanceof Error) K1(X);
+     } finally {
+       if (((z = null), !H)) _();
+     }
+   }
+   function _() {
+     if (H) return;
+     w = setTimeout(() => void $(), CPY);
+   }
+   function J() {
+     if ((h(`[AgentSummary] Stopping summarization for ${A}`), (H = !0), w))
+       (clearTimeout(w), (w = null));
+     if (z) (z.abort(), (z = null));
+   }
+   return (_(), { stop: J });
+ }

+++ Added Ep4 (pretty-v2.1.32.js:418947-419100)
+ var Ep4 = v(() => {
+   ((GLY = `Use this tool proactively when you're about to start a non-trivial implementation task. Getting user sign-off on your approach before writing code prevents wasted effort and ensures alignment. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
+ 
+ ## When to Use This Tool
+ 
+ **Prefer using EnterPlanMode** for implementation tasks unless they're simple. Use it when ANY of these conditions apply:
+ 
+ 1. **New Feature Implementation**: Adding meaningful new functionality
+    - Example: "Add a logout button" - where should it go? What should happen on click?
+    - Example: "Add form validation" - what rules? What error messages?
+ 
+ 2. **Multiple Valid Approaches**: The task can be solved in several different ways
+    - Example: "Add caching to the API" - could use Redis, in-memory, file-based, etc.
+    - Example: "Improve performance" - many optimization strategies possible
+ 
+ 3. **Code Modifications**: Changes that affect existing behavior or structure
+    - Example: "Update the login flow" - what exactly should change?
+    - Example: "Refactor this component" - what's the target architecture?
+ 
+ 4. **Architectural Decisions**: The task requires choosing between patterns or technologies
+    - Example: "Add real-time updates" - WebSockets vs SSE vs polling
+    - Example: "Implement state management" - Redux vs Context vs custom solution
+ 
+ 5. **Multi-File Changes**: The task will likely touch more than 2-3 files
+    - Example: "Refactor the authentication system"
+    - Example: "Add a new API endpoint with tests"
+ 
+ 6. **Unclear Requirements**: You need to explore before understanding the full scope
+    - Example: "Make the app faster" - need to profile and identify bottlenecks
+    - Example: "Fix the bug in checkout" - need to investigate root cause
+ 
+ 7. **User Preferences Matter**: The implementation could reasonably go multiple ways
+    - If you would use ${kw} to clarify the approach, use EnterPlanMode instead
+    - Plan mode lets you explore first, then present options with context
+ 
+ ## When NOT to Use This Tool
+ 
+ Only skip EnterPlanMode for simple tasks:
+ - Single-line or few-line fixes (typos, obvious bugs, small tweaks)
+ - Adding a single function with clear requirements
+ - Tasks where the user has given very specific, detailed instructions
+ - Pure research/exploration tasks (use the Task tool with explore agent instead)
+ 
+ ## What Happens in Plan Mode
+ 
+ In plan mode, you'll:
+ 1. Thoroughly explore the codebase using Glob, Grep, and Read tools
+ 2. Understand existing patterns and architecture
+ 3. Design an implementation approach
+ 4. Present your plan to the user for approval
+ 5. Use ${kw} if you need to clarify approaches
+ 6. Exit plan mode with ExitPlanMode when ready to implement
+ 
+ ## Examples
+ 
+ ### GOOD - Use EnterPlanMode:
+ User: "Add user authentication to the app"
+ - Requires architectural decisions (session vs JWT, where to store tokens, middleware structure)
+ 
+ User: "Optimize the database queries"
+ - Multiple approaches possible, need to profile first, significant impact
+ 
+ User: "Implement dark mode"
+ - Architectural decision on theme system, affects many components
+ 
+ User: "Add a delete button to the user profile"
+ - Seems simple but involves: where to place it, confirmation dialog, API call, error handling, state updates
+ 
+ User: "Update the error handling in the API"
+ - Affects multiple files, user should approve the approach
+ 
+ ### BAD - Don't use EnterPlanMode:
+ User: "Fix the typo in the README"
+ - Straightforward, no planning needed
+ 
+ User: "Add a console.log to debug this function"
+ - Simple, obvious implementation
+ 
+ User: "What files handle routing?"
+ - Research task, not implementation planning
+ 
+ ## Important Notes
+ 
+ - This tool REQUIRES user approval - they must consent to entering plan mode
+ - If unsure whether to use it, err on the side of planning - it's better to get alignment upfront than to redo work
+ - Users appreciate being consulted before significant changes are made to their codebase
+ `),
+     (MqH = `Use this tool when a task has genuine ambiguity about the right approach and getting user input before coding would prevent significant rework. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
+ 
+ ## When to Use This Tool
+ 
+ Plan mode is valuable when the implementation approach is genuinely unclear. Use it when:
+ 
+ 1. **Significant Architectural Ambiguity**: Multiple reasonable approaches exist and the choice meaningfully affects the codebase
+    - Example: "Add caching to the API" - Redis vs in-memory vs file-based
+    - Example: "Add real-time updates" - WebSockets vs SSE vs polling
+ 
+ 2. **Unclear Requirements**: You need to explore and clarify before you can make progress
+    - Example: "Make the app faster" - need to profile and identify bottlenecks
+    - Example: "Refactor this module" - need to understand what the target architecture should be
+ 
+ 3. **High-Impact Restructuring**: The task will significantly restructure existing code and getting buy-in first reduces risk
+    - Example: "Redesign the authentication system"
+    - Example: "Migrate from one state management approach to another"
+ 
+ ## When NOT to Use This Tool
+ 
+ Skip plan mode when you can reasonably infer the right approach:
+ - The task is straightforward even if it touches multiple files
+ - The user's request is specific enough that the implementation path is clear
+ - You're adding a feature with an obvious implementation pattern (e.g., adding a button, a new endpoint following existing conventions)
+ - Bug fixes where the fix is clear once you understand the bug
+ - Research/exploration tasks (use the Task tool with explore agent instead)
+ - The user says something like "can we work on X" or "let's do X" — just get started
+ 
+ When in doubt, prefer starting work and using ${kw} for specific questions over entering a full planning phase.
+ 
+ ## What Happens in Plan Mode
+ 
+ In plan mode, you'll:
+ 1. Explore the codebase using Glob, Grep, and Read tools
+ 2. Understand existing patterns and architecture
+ 3. Design an implementation approach
+ 4. Present your plan to the user for approval
+ 5. Use ${kw} if you need to clarify approaches
+ 6. Exit plan mode with ExitPlanMode when ready to implement
+ 
+ ## Examples
+ 
+ ### GOOD - Use EnterPlanMode:
+ User: "Add user authentication to the app"
+ - Genuinely ambiguous: session vs JWT, where to store tokens, middleware structure
+ 
+ User: "Redesign the data pipeline"
+ - Major restructuring where the wrong approach wastes significant effort
+ 
+ ### BAD - Don't use EnterPlanMode:
+ User: "Add a delete button to the user profile"
+ - Implementation path is clear; just do it
+ 
+ User: "Can we work on the search feature?"
+ - User wants to get started, not plan
+ 
+ User: "Update the error handling in the API"
+ - Start working; ask specific questions if needed
+ 
+ User: "Fix the typo in the README"
+ - Straightforward, no planning needed
+ 
+ ## Important Notes
+ 
+ - This tool REQUIRES user approval - they must consent to entering plan mode
+ `));
+ });

+++ Added Vd4 (pretty-v2.1.32.js:420396-420397)
+ var Vd4 =
+   "Send messages to agent teammates and handle protocol requests (shutdown, plan approval)";

+++ Added od4 (pretty-v2.1.32.js:422365-422367)
+ async function od4(A, q, K) {
+   return (A.load ? (await A.load()).call : A.call)(q, K);
+ }

+++ Added HG1 (pretty-v2.1.32.js:422368-422370)
+ async function HG1(A, q, K, Y) {
+   return (A.load ? (await A.load()).call : A.call)(q, K, Y);
+ }

+++ Added Nc4 (pretty-v2.1.32.js:424802-424924)
+ async function Nc4(A, q, K, Y, z) {
+   try {
+     let w = A.slice(q),
+       H = A.slice(0, q);
+     if (w.length === 0)
+       throw Error("Nothing to summarize after the selected message.");
+     let O = mL(A);
+     (K.onCompactProgress?.({ type: "hooks_start", hookType: "pre_compact" }),
+       K.setSDKStatus?.("compacting"));
+     let $ = await IW6(
+         { trigger: "manual", customInstructions: null },
+         K.abortController.signal,
+       ),
+       _;
+     if ($.newCustomInstructions && z)
+       _ = `${$.newCustomInstructions}
+ 
+ User context: ${z}`;
+     else if ($.newCustomInstructions) _ = $.newCustomInstructions;
+     else if (z) _ = `User context: ${z}`;
+     (K.setStreamMode?.("requesting"),
+       K.setResponseLength?.(() => 0),
+       K.onCompactProgress?.({ type: "compact_start" }));
+     let J = sY4(_),
+       X = p6({ content: J }),
+       D = await vc4({
+         messages: A,
+         summaryRequest: X,
+         appState: await K.getAppState(),
+         context: K,
+         preCompactTokenCount: O,
+         cacheSafeParams: Y,
+       }),
+       j = Xd(D);
+     if (!j)
+       throw (
+         c("tengu_partial_compact_failed", {
+           reason: "no_summary",
+           preCompactTokenCount: O,
+         }),
+         Error(
+           "Failed to generate conversation summary - response did not contain valid text content",
+         )
+       );
+     else if (j.startsWith(J_))
+       throw (
+         c("tengu_partial_compact_failed", {
+           reason: "api_error",
+           preCompactTokenCount: O,
+         }),
+         Error(j)
+       );
+     else if (j.startsWith(wU))
+       throw (
+         c("tengu_partial_compact_failed", {
+           reason: "prompt_too_long",
+           preCompactTokenCount: O,
+         }),
+         Error(Vc4)
+       );
+     let M = yXA(K.readFileState);
+     (K.readFileState.clear(), Jd());
+     let [W, G] = await Promise.all([Ec4(M, K, fc4), Rc4(K)]),
+       P = [...W, ...G],
+       V = kc4(K.agentId ?? u6());
+     if (V) P.push(V);
+     let Z = hW6(K.agentId);
+     if (Z) P.push(Z);
+     let N = Lc4();
+     if (N) P.push(N);
+     K.onCompactProgress?.({ type: "hooks_start", hookType: "session_start" });
+     let T = await UM("compact", { model: K.options.mainLoopModel }),
+       k = RV([D]),
+       y = uU(D);
+     c("tengu_partial_compact", {
+       preCompactTokenCount: O,
+       postCompactTokenCount: k,
+       messagesKept: H.length,
+       messagesSummarized: w.length,
+       trigger: "message_selector",
+       compactionInputTokens: y?.input_tokens,
+       compactionOutputTokens: y?.output_tokens,
+       compactionCacheReadTokens: y?.cache_read_input_tokens ?? 0,
+       compactionCacheCreationTokens: y?.cache_creation_input_tokens ?? 0,
+     });
+     let u = pQ1("manual", O ?? 0, H[H.length - 1]?.uuid, z, w.length),
+       S = oO(u6()),
+       m = [
+         p6({
+           content: ku1(j, !1, S),
+           isCompactSummary: !0,
+           ...(H.length > 0
+             ? {
+                 summarizeMetadata: {
+                   messagesSummarized: w.length,
+                   userContext: z,
+                 },
+               }
+             : { isVisibleInTranscriptOnly: !0 }),
+         }),
+       ];
+     return (
+       JMA(K.options.querySource ?? "compact", K.agentId),
+       {
+         boundaryMarker: u,
+         summaryMessages: m,
+         messagesToKeep: H,
+         attachments: P,
+         hookResults: T,
+         preCompactTokenCount: O,
+         postCompactTokenCount: k,
+         compactionUsage: y,
+       }
+     );
+   } catch (w) {
+     throw (Tc4(w, K), w);
+   } finally {
+     (K.setStreamMode?.("requesting"),
+       K.setResponseLength?.(() => 0),
+       K.onCompactProgress?.({ type: "compact_end" }),
+       K.setSDKStatus?.(null));
+   }
+ }

+++ Added xc4 (pretty-v2.1.32.js:425223-425225)
+ function xc4() {
+   xW6 = void 0;
+ }

+++ Added mc4 (pretty-v2.1.32.js:425247-425249)
+ function mc4(A) {
+   Cc4 = A;
+ }

+++ Added Nr4 (pretty-v2.1.32.js:431004-431011)
+ function Nr4(A) {
+   let q = 0;
+   for (let K of A)
+     if (K.type === "user" && K.imagePasteIds) {
+       for (let Y of K.imagePasteIds) if (Y > q) q = Y;
+     }
+   return q + 1;
+ }

+++ Added xbY (pretty-v2.1.32.js:435077-435099)
+   xbY = `[SUGGESTION MODE: You are suggesting for a coordinator orchestrating workers.]
+ 
+ The user manages workers via the Task tool. Worker results arrive as <task-notification> messages that look like user messages but aren't.
+ 
+ FIRST: Check the conversation state.
+ - Did a worker just report results? -> Suggest the coordinator's next action
+ - Are workers still running? -> Silence (let them finish)
+ - Did the user just give an instruction? -> Silence (coordinator is executing)
+ 
+ COORDINATOR ACTIONS (suggest these):
+ - After worker research: "let me synthesize and implement the fix"
+ - After worker implementation: "verify the changes" or "run the tests"
+ - After all workers done: "commit the changes" or "create the PR"
+ - After worker failure: a specific corrective instruction
+ 
+ NEVER SUGGEST:
+ - Generic coding actions ("fix the bug", "add a test") — the coordinator delegates, not does
+ - Questions or evaluative phrases
+ - Claude-voice ("Let me...", "I'll...")
+ - Actions the coordinator already started
+ 
+ Format: 2-12 words, match the user's style. Or nothing.
+ Reply with ONLY the suggestion, no quotes or explanation.`,

+++ Added va4 (pretty-v2.1.32.js:443646-443648)
+ function va4(A) {
+   return A.type === "image";
+ }

+++ Added ya4 (pretty-v2.1.32.js:443925-443925)
+   ya4 = "";

+++ Added ps4 (pretty-v2.1.32.js:448015-448015)
+ var ps4 = 16000,

+++ Added AZ6 (pretty-v2.1.32.js:451854-451865)
+ function AZ6(A, q) {
+   J$();
+   let K = jq();
+   h(`Settings changed from ${A}, updating app state`);
+   let Y = B76();
+   (T51(),
+     q((z) => {
+       let w = Qt4(z.toolPermissionContext, Y);
+       if (w.isBypassPermissionsModeAvailable && sG1()) w = tG1(w);
+       return { ...z, settings: K, toolPermissionContext: w };
+     }));
+ }

+++ Added yd (pretty-v2.1.32.js:456776-456778)
+ function yd(A, q) {
+   return { name: A, compute: q, cacheBreak: !1 };
+ }

+++ Added Cd (pretty-v2.1.32.js:456779-456781)
+ function Cd(A, q, K) {
+   return { name: A, compute: q, cacheBreak: !0 };
+ }

+++ Added cSA (pretty-v2.1.32.js:456782-456791)
+ async function cSA(A) {
+   let q = Gk6();
+   return Promise.all(
+     A.map(async (K) => {
+       if (!K.cacheBreak && q.has(K.name)) return q.get(K.name) ?? null;
+       let Y = await K.compute();
+       return (Pk6(K.name, Y), Y);
+     }),
+   );
+ }

+++ Added bpY (pretty-v2.1.32.js:456856-456858)
+ var bpY = async (A, q) => {
+   return (B4("clear"), await nSA(q), { type: "text", value: "" });
+ };

+++ Added W1q (pretty-v2.1.32.js:456924-456940)
+ var W1q = v(() => {
+   N9();
+   ((mpY = {
+     type: "local",
+     name: "color",
+     description: "Set the prompt bar color for this session",
+     isEnabled: () => F8(),
+     isHidden: !1,
+     supportsNonInteractive: !1,
+     argumentHint: "<color>",
+     load: () => Promise.resolve().then(() => (j1q(), D1q)),
+     userFacingName() {
+       return "color";
+     },
+   }),
+     (M1q = mpY));
+ });

+++ Added P1q (pretty-v2.1.32.js:456945-456945)
+ var P1q = {};

+++ Added V1q (pretty-v2.1.32.js:456977-456991)
+ var V1q = v(() => {
+   ((gpY = {
+     type: "local",
+     name: "copy",
+     description: "Copy Claude's last response to clipboard as markdown",
+     isEnabled: () => !0,
+     isHidden: !1,
+     supportsNonInteractive: !1,
+     load: () => Promise.resolve().then(() => (Z1q(), P1q)),
+     userFacingName() {
+       return "copy";
+     },
+   }),
+     (f1q = gpY));
+ });

+++ Added k1q (pretty-v2.1.32.js:457019-457019)
+ var k1q = {};

+++ Added y1q (pretty-v2.1.32.js:457119-457136)
+ var y1q = v(() => {
+   BA();
+   ((cpY = {
+     type: "local",
+     name: "compact",
+     description:
+       "Clear conversation history but keep a summary in context. Optional: /compact [instructions for summarization]",
+     isEnabled: () => !$6(process.env.DISABLE_COMPACT),
+     isHidden: !1,
+     supportsNonInteractive: !0,
+     argumentHint: "<optional custom summarization instructions>",
+     load: () => Promise.resolve().then(() => (L1q(), k1q)),
+     userFacingName() {
+       return "compact";
+     },
+   }),
+     (R1q = cpY));
+ });

+++ Added $U1 (pretty-v2.1.32.js:459519-459521)
+ function $U1(A) {
+   return A.toLowerCase().includes("opus-4-6");
+ }

+++ Added DU1 (pretty-v2.1.32.js:461490-461504)
+ function DU1() {
+   if (!x8("tengu_copper_lantern", !1)) return !1;
+   if (!JC()) return !1;
+   let A = TK();
+   if (A !== "pro" && A !== "max") return !1;
+   if (M6().hasVisitedExtraUsage) return !1;
+   let K = z3();
+   if (K?.subscriptionCreatedAt) {
+     let Y = dQ("tengu_copper_lantern_config", {
+       meridian: "2026-02-05T07:59:00Z",
+     });
+     if (new Date(K.subscriptionCreatedAt) >= new Date(Y.meridian)) return !1;
+   }
+   return !0;
+ }

+++ Added rdY (pretty-v2.1.32.js:461505-461508)
+ function rdY() {
+   if ((M6().opus46FeedSeenCount ?? 0) >= ndY) return !1;
+   return !0;
+ }

+++ Added odY (pretty-v2.1.32.js:461509-461514)
+ function odY() {
+   if (!x8("tengu_silver_lantern", !1)) return null;
+   if (DU1()) return "promo";
+   if (rdY()) return "launch-only";
+   return null;
+ }

+++ Added QZ6 (pretty-v2.1.32.js:461522-461526)
+ function QZ6() {
+   let q = (M6().opus46FeedSeenCount ?? 0) + 1;
+   (OA((K) => ({ ...K, opus46FeedSeenCount: q })),
+     c("tengu_opus46_feed_shown", { seen_count: q }));
+ }

+++ Added V6q (pretty-v2.1.32.js:461527-461583)
+ function V6q(A) {
+   let q = A1(3),
+     { variant: K } = A;
+   switch (K) {
+     case "promo-copper": {
+       let Y;
+       if (q[0] === Symbol.for("react.memo_cache_sentinel"))
+         ((Y = EG.createElement(
+           f,
+           { dimColor: !0 },
+           EG.createElement(
+             EG.Fragment,
+             null,
+             EG.createElement(
+               f,
+               { color: "claude" },
+               "Opus 4.6 is here · $50 free extra usage",
+             ),
+             " ",
+             "· /extra-usage to enable",
+           ),
+         )),
+           (q[0] = Y));
+       else Y = q[0];
+       return Y;
+     }
+     case "promo": {
+       let Y;
+       if (q[1] === Symbol.for("react.memo_cache_sentinel"))
+         ((Y = EG.createElement(
+           f,
+           { dimColor: !0 },
+           EG.createElement(
+             f,
+             { color: "claude" },
+             "Opus 4.6 is here · $50 free extra usage",
+           ),
+           " · /extra-usage to enable",
+         )),
+           (q[1] = Y));
+       else Y = q[1];
+       return Y;
+     }
+     case "launch-only": {
+       let Y;
+       if (q[2] === Symbol.for("react.memo_cache_sentinel"))
+         ((Y = EG.createElement(
+           f,
+           { dimColor: !0 },
+           "Opus 4.6 is here · Most capable for ambitious work",
+         )),
+           (q[2] = Y));
+       else Y = q[2];
+       return Y;
+     }
+   }
+ }

+++ Added E6q (pretty-v2.1.32.js:462070-462070)
+ var E6q = {};

+++ Added tdY (pretty-v2.1.32.js:462073-462079)
+   tdY = async (A, q) => {
+     return fhA.createElement(WP1, {
+       onClose: A,
+       context: q,
+       defaultTab: "Config",
+     });
+   };

+++ Added B6q (pretty-v2.1.32.js:463003-463003)
+ var B6q = {};

+++ Added Q6q (pretty-v2.1.32.js:463025-463042)
+ var Q6q = v(() => {
+   D7();
+   ((bcY = {
+     type: "local",
+     name: "cost",
+     description: "Show the total cost and duration of the current session",
+     isEnabled: () => !0,
+     get isHidden() {
+       return U8();
+     },
+     supportsNonInteractive: !0,
+     load: () => Promise.resolve().then(() => (m6q(), B6q)),
+     userFacingName() {
+       return "cost";
+     },
+   }),
+     (F6q = bcY));
+ });

+++ Added AAq (pretty-v2.1.32.js:464607-464607)
+ var AAq = {};

+++ Added NlY (pretty-v2.1.32.js:464610-464612)
+   NlY = (A, q, K) => {
+     return Promise.resolve(e6q.default.createElement(rZ6, { onDone: A }));
+   };

+++ Added ZAq (pretty-v2.1.32.js:464878-464878)
+ var ZAq = {};

+++ Added mlY (pretty-v2.1.32.js:464957-464959)
+   mlY = async (A) => {
+     return rv.createElement(BlY, { onDone: A });
+   };

+++ Added yAq (pretty-v2.1.32.js:465648-465648)
+ var yAq = {};

+++ Added UlY (pretty-v2.1.32.js:465651-465653)
+   UlY = async (A, { options: { commands: q } }) => {
+     return mhA.createElement(LAq, { commands: q, onClose: A });
+   };

+++ Added XiY (pretty-v2.1.32.js:468197-468219)
+ function XiY(A) {
+   if (A.pending)
+     return XN.default.createElement(
+       f,
+       null,
+       "Press ",
+       A.keyName,
+       " again to exit",
+     );
+   return XN.default.createElement(
+     pA,
+     null,
+     XN.default.createElement(YA, { shortcut: "↑↓", action: "navigate" }),
+     XN.default.createElement(YA, { shortcut: "Space", action: "toggle" }),
+     XN.default.createElement(YA, { shortcut: "Enter", action: "confirm" }),
+     XN.default.createElement(NA, {
+       action: "confirm:no",
+       context: "Confirmation",
+       fallback: "Esc",
+       description: "cancel",
+     }),
+   );
+ }

+++ Added S8q (pretty-v2.1.32.js:468220-468326)
+ function S8q(A) {
+   let q = A1(14),
+     { onSubmit: K, defaultSelections: Y } = A,
+     [z, w] = C8q.useState(!1),
+     H;
+   if (q[0] !== K)
+     ((H = (P) => {
+       if (P.length === 0) {
+         w(!0);
+         return;
+       }
+       (w(!1), K(P));
+     }),
+       (q[0] = K),
+       (q[1] = H));
+   else H = q[1];
+   let O = H,
+     $;
+   if (q[2] === Symbol.for("react.memo_cache_sentinel"))
+     (($ = () => {
+       w(!1);
+     }),
+       (q[2] = $));
+   else $ = q[2];
+   let _ = $,
+     J;
+   if (q[3] === Symbol.for("react.memo_cache_sentinel"))
+     ((J = () => {
+       w(!0);
+     }),
+       (q[3] = J));
+   else J = q[3];
+   let X = J,
+     D;
+   if (q[4] === Symbol.for("react.memo_cache_sentinel"))
+     ((D = XN.default.createElement(
+       I,
+       null,
+       XN.default.createElement(
+         f,
+         { dimColor: !0 },
+         "More workflow examples (issue triage, CI fixes, etc.) at:",
+         " ",
+         XN.default.createElement(
+           q4,
+           {
+             url: "https://github.com/anthropics/claude-code-action/blob/main/examples/",
+           },
+           "https://github.com/anthropics/claude-code-action/blob/main/examples/",
+         ),
+       ),
+     )),
+       (q[4] = D));
+   else D = q[4];
+   let j;
+   if (q[5] === Symbol.for("react.memo_cache_sentinel"))
+     ((j = JiY.map(DiY)), (q[5] = j));
+   else j = q[5];
+   let M;
+   if (q[6] !== Y || q[7] !== O)
+     ((M = XN.default.createElement(TP1, {
+       options: j,
+       defaultValue: Y,
+       onSubmit: O,
+       onChange: _,
+     })),
+       (q[6] = Y),
+       (q[7] = O),
+       (q[8] = M));
+   else M = q[8];
+   let W;
+   if (q[9] !== z)
+     ((W =
+       z &&
+       XN.default.createElement(
+         I,
+         null,
+         XN.default.createElement(
+           f,
+           { color: "error" },
+           "You must select at least one workflow to continue",
+         ),
+       )),
+       (q[9] = z),
+       (q[10] = W));
+   else W = q[10];
+   let G;
+   if (q[11] !== M || q[12] !== W)
+     ((G = XN.default.createElement(
+       w8,
+       {
+         title: "Select GitHub workflows to install",
+         subtitle:
+           "We'll create a workflow file in your repository for each one you select.",
+         onCancel: X,
+         inputGuide: XiY,
+       },
+       D,
+       M,
+       W,
+     )),
+       (q[11] = M),
+       (q[12] = W),
+       (q[13] = G));
+   else G = q[13];
+   return G;
+ }

+++ Added h8q (pretty-v2.1.32.js:468331-468351)
+ var h8q = v(() => {
+   d1();
+   u1();
+   hq();
+   tZ6();
+   Tq();
+   LK();
+   Cq();
+   ((XN = a($1(), 1)),
+     (C8q = a($1(), 1)),
+     (JiY = [
+       {
+         value: "claude",
+         label: "@Claude Code - Tag @claude in issues and PR comments",
+       },
+       {
+         value: "claude-review",
+         label: "Claude Code Review - Automated code review on new PRs",
+       },
+     ]));
+ });

+++ Added LtY (pretty-v2.1.32.js:484569-484571)
+ function LtY(A) {
+   return A.id === "opus-4.6-available";
+ }

+++ Added dKq (pretty-v2.1.32.js:485212-485265)
+ function dKq(A) {
+   switch (A) {
+     case "promo-copper":
+       return {
+         title: "Opus 4.6 is here",
+         lines: [],
+         customContent: {
+           content: sO.createElement(
+             I,
+             { marginY: 1 },
+             sO.createElement(
+               f,
+               { bold: !0, color: "claude" },
+               "$50 free extra usage",
+             ),
+           ),
+           width: 48,
+         },
+         footer: "/extra-usage to enable",
+       };
+     case "promo":
+       return {
+         title: "Opus 4.6 is here",
+         lines: [],
+         customContent: {
+           content: sO.createElement(
+             I,
+             { marginY: 1 },
+             sO.createElement(
+               f,
+               { bold: !0, color: "claude" },
+               "$50 free extra usage",
+             ),
+           ),
+           width: 48,
+         },
+         footer: "/extra-usage to enable",
+       };
+     case "launch-only":
+       return {
+         title: "Opus 4.6 is here",
+         lines: [],
+         customContent: {
+           content: sO.createElement(
+             I,
+             { marginY: 1 },
+             sO.createElement(f, null, "Most capable for ambitious work"),
+           ),
+           width: 48,
+         },
+         footer: "/model to switch",
+       };
+   }
+ }

+++ Added df6 (pretty-v2.1.32.js:485297-485300)
+ function df6() {
+   let [A] = lKq.useState(mtY);
+   return A;
+ }

+++ Added iKq (pretty-v2.1.32.js:485309-485331)
+ function iKq() {
+   let A = A1(1),
+     q;
+   if (A[0] === Symbol.for("react.memo_cache_sentinel")) {
+     let K = nt();
+     ((q = Bd.createElement(
+       f,
+       { dimColor: !0 },
+       Bd.createElement(f, { color: "claude" }, "[✻]"),
+       " ",
+       Bd.createElement(f, { color: "claude" }, "[✻]"),
+       " ",
+       Bd.createElement(f, { color: "claude" }, "[✻]"),
+       " ·",
+       " ",
+       K
+         ? `Share Claude Code and earn ${it(K)} of extra usage · /passes`
+         : "3 guest passes at /passes",
+     )),
+       (A[0] = q));
+   } else q = A[0];
+   return q;
+ }

+++ Added $eY (pretty-v2.1.32.js:488500-488500)
+   $eY = 4,

+++ Added k3q (pretty-v2.1.32.js:488726-488726)
+ var k3q = {};

+++ Added y3q (pretty-v2.1.32.js:488943-488958)
+ var y3q = v(() => {
+   ((ReY = {
+     type: "local-jsx",
+     name: "resume",
+     description: "Resume a previous conversation",
+     aliases: ["continue"],
+     isEnabled: () => !0,
+     isHidden: !1,
+     argumentHint: "[conversation id or search term]",
+     load: () => Promise.resolve().then(() => (L3q(), k3q)),
+     userFacingName() {
+       return "resume";
+     },
+   }),
+     (R3q = ReY));
+ });

+++ Added C3q (pretty-v2.1.32.js:489004-489004)
+ var C3q = {};

+++ Added xeY (pretty-v2.1.32.js:489140-489142)
+   xeY = async (A) => {
+     return m2.createElement(yeY, { onDone: A });
+   };

+++ Added _5q (pretty-v2.1.32.js:491903-491903)
+ var _5q = {};

+++ Added H1z (pretty-v2.1.32.js:491906-491912)
+   H1z = async (A, q) => {
+     return CxA.createElement(WP1, {
+       onClose: A,
+       context: q,
+       defaultTab: "Usage",
+     });
+   };

+++ Added j5q (pretty-v2.1.32.js:491931-491931)
+ var j5q = {};

+++ Added $1z (pretty-v2.1.32.js:491983-491985)
+   $1z = async (A, q) => {
+     return Qd.createElement(O1z, { onDone: A });
+   };

+++ Added P5q (pretty-v2.1.32.js:492008-492008)
+ var P5q = {};

+++ Added J1z (pretty-v2.1.32.js:492010-492023)
+ var J1z = async () => {
+   B4("vim-mode");
+   let q = M6().editorMode || "normal";
+   if (q === "emacs") q = "normal";
+   let K = q === "normal" ? "vim" : "normal";
+   return (
+     OA((Y) => ({ ...Y, editorMode: K })),
+     c("tengu_editor_mode_changed", { mode: K, source: "command" }),
+     {
+       type: "text",
+       value: `Editor mode set to ${K}. ${K === "vim" ? "Use Escape key to toggle between INSERT and NORMAL modes." : "Using standard (readline) keyboard bindings."}`,
+     }
+   );
+ };

+++ Added C1z (pretty-v2.1.32.js:492787-492789)
+ function C1z(A) {
+   return { label: A.path, value: A.path };
+ }

+++ Added B5q (pretty-v2.1.32.js:493851-493851)
+ var B5q = {};

+++ Added F1z (pretty-v2.1.32.js:493854-493856)
+   F1z = async (A) => {
+     return bxA.createElement(x5q, { onExit: A });
+   };

+++ Added n1z (pretty-v2.1.32.js:494657-494666)
+ function n1z(A) {
+   return A.pending
+     ? n7.default.createElement(f, null, "Press ", A.keyName, " again to exit")
+     : n7.default.createElement(
+         pA,
+         null,
+         n7.default.createElement(YA, { shortcut: "Enter", action: "confirm" }),
+         n7.default.createElement(YA, { shortcut: "Esc", action: "cancel" }),
+       );
+ }

+++ Added T9q (pretty-v2.1.32.js:496971-496971)
+ var T9q = {};

+++ Added k9q (pretty-v2.1.32.js:496987-497000)
+ var k9q = v(() => {
+   (($6z = {
+     type: "local-jsx",
+     name: "hooks",
+     description: "Manage hook configurations for tool events",
+     isEnabled: () => !0,
+     isHidden: !1,
+     load: () => Promise.resolve().then(() => (v9q(), T9q)),
+     userFacingName() {
+       return "hooks";
+     },
+   }),
+     (E9q = $6z));
+ });

+++ Added Szq (pretty-v2.1.32.js:505125-505125)
+ var Szq = {};

+++ Added Y8z (pretty-v2.1.32.js:505130-505132)
+ async function Y8z(A) {
+   return (A(K8z()), await $K(0, "prompt_input_exit"), null);
+ }

+++ Added hzq (pretty-v2.1.32.js:505134-505141)
+ var hzq = v(() => {
+   $61();
+   $w();
+   VP1();
+   Czq();
+   ((A8z = a($1(), 1)),
+     (q8z = ["Goodbye!", "See ya!", "Bye!", "Catch you later!"]));
+ });

+++ Added Fzq (pretty-v2.1.32.js:505457-505457)
+ var Fzq = {};

+++ Added Uzq (pretty-v2.1.32.js:505587-505601)
+ var Uzq = v(() => {
+   gzq = {
+     immediate: !0,
+     type: "local-jsx",
+     name: "model",
+     userFacingName() {
+       return "model";
+     },
+     description: "Set the AI model for Claude Code",
+     isEnabled: () => !0,
+     isHidden: !1,
+     argumentHint: "[model]",
+     load: () => Promise.resolve().then(() => (Qzq(), Fzq)),
+   };
+ });

+++ Added u2q (pretty-v2.1.32.js:509266-509266)
+ var u2q = {};

+++ Added F7z (pretty-v2.1.32.js:509269-509271)
+   F7z = async (A) => {
+     return dbA.createElement(S2q, { onClose: A });
+   };

+++ Added p7z (pretty-v2.1.32.js:509295-509297)
+ function p7z() {
+   return WC();
+ }

+++ Added _4z (pretty-v2.1.32.js:510102-510878)
+ function _4z(A, q) {
+   let K = (S) => {
+       if (!S) return "";
+       return S.split(
+         `
+ 
+ `,
+       ).map((m) => {
+         let b = D9(m);
+         return (
+           (b = b.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")),
+           (b = b.replace(/^- /gm, "• ")),
+           (b = b.replace(/\n/g, "<br>")),
+           `<p>${b}</p>`
+         );
+       }).join(`
+ `);
+     },
+     Y = q.at_a_glance,
+     z = Y
+       ? `
+     <div class="at-a-glance">
+       <div class="glance-title">At a Glance</div>
+       <div class="glance-sections">
+         ${Y.whats_working ? `<div class="glance-section"><strong>What's working:</strong> ${IV6(Y.whats_working)} <a href="#section-wins" class="see-more">Impressive Things You Did →</a></div>` : ""}
+         ${Y.whats_hindering ? `<div class="glance-section"><strong>What's hindering you:</strong> ${IV6(Y.whats_hindering)} <a href="#section-friction" class="see-more">Where Things Go Wrong →</a></div>` : ""}
+         ${Y.quick_wins ? `<div class="glance-section"><strong>Quick wins to try:</strong> ${IV6(Y.quick_wins)} <a href="#section-features" class="see-more">Features to Try →</a></div>` : ""}
+         ${Y.ambitious_workflows ? `<div class="glance-section"><strong>Ambitious workflows:</strong> ${IV6(Y.ambitious_workflows)} <a href="#section-horizon" class="see-more">On the Horizon →</a></div>` : ""}
+       </div>
+     </div>
+     `
+       : "",
+     w = q.project_areas?.areas || [],
+     H =
+       w.length > 0
+         ? `
+     <h2 id="section-work">What You Work On</h2>
+     <div class="project-areas">
+       ${w
+         .map(
+           (S) => `
+         <div class="project-area">
+           <div class="area-header">
+             <span class="area-name">${D9(S.name)}</span>
+             <span class="area-count">~${S.session_count} sessions</span>
+           </div>
+           <div class="area-desc">${D9(S.description)}</div>
+         </div>
+       `,
+         )
+         .join("")}
+     </div>
+     `
+         : "",
+     O = q.interaction_style,
+     $ = O?.narrative
+       ? `
+     <h2 id="section-usage">How You Use Claude Code</h2>
+     <div class="narrative">
+       ${K(O.narrative)}
+       ${O.key_pattern ? `<div class="key-insight"><strong>Key pattern:</strong> ${D9(O.key_pattern)}</div>` : ""}
+     </div>
+     `
+       : "",
+     _ = q.what_works,
+     J =
+       _?.impressive_workflows && _.impressive_workflows.length > 0
+         ? `
+     <h2 id="section-wins">Impressive Things You Did</h2>
+     ${_.intro ? `<p class="section-intro">${D9(_.intro)}</p>` : ""}
+     <div class="big-wins">
+       ${_.impressive_workflows
+         .map(
+           (S) => `
+         <div class="big-win">
+           <div class="big-win-title">${D9(S.title || "")}</div>
+           <div class="big-win-desc">${D9(S.description || "")}</div>
+         </div>
+       `,
+         )
+         .join("")}
+     </div>
+     `
+         : "",
+     X = q.friction_analysis,
+     D =
+       X?.categories && X.categories.length > 0
+         ? `
+     <h2 id="section-friction">Where Things Go Wrong</h2>
+     ${X.intro ? `<p class="section-intro">${D9(X.intro)}</p>` : ""}
+     <div class="friction-categories">
+       ${X.categories
+         .map(
+           (S) => `
+         <div class="friction-category">
+           <div class="friction-title">${D9(S.category || "")}</div>
+           <div class="friction-desc">${D9(S.description || "")}</div>
+           ${S.examples ? `<ul class="friction-examples">${S.examples.map((m) => `<li>${D9(m)}</li>`).join("")}</ul>` : ""}
+         </div>
+       `,
+         )
+         .join("")}
+     </div>
+     `
+         : "",
+     j = q.suggestions,
+     M = j
+       ? `
+     ${
+       j.claude_md_additions && j.claude_md_additions.length > 0
+         ? `
+     <h2 id="section-features">Existing CC Features to Try</h2>
+     <div class="claude-md-section">
+       <h3>Suggested CLAUDE.md Additions</h3>
+       <p style="font-size: 12px; color: #64748b; margin-bottom: 12px;">Just copy this into Claude Code to add it to your CLAUDE.md.</p>
+       <div class="claude-md-actions">
+         <button class="copy-all-btn" onclick="copyAllCheckedClaudeMd()">Copy All Checked</button>
+       </div>
+       ${j.claude_md_additions
+         .map(
+           (S, m) => `
+         <div class="claude-md-item">
+           <input type="checkbox" id="cmd-${m}" class="cmd-checkbox" checked data-text="${D9(S.prompt_scaffold || S.where || "Add to CLAUDE.md")}\\n\\n${D9(S.addition)}">
+           <label for="cmd-${m}">
+             <code class="cmd-code">${D9(S.addition)}</code>
+             <button class="copy-btn" onclick="copyCmdItem(${m})">Copy</button>
+           </label>
+           <div class="cmd-why">${D9(S.why)}</div>
+         </div>
+       `,
+         )
+         .join("")}
+     </div>
+     `
+         : ""
+     }
+     ${
+       j.features_to_try && j.features_to_try.length > 0
+         ? `
+     <p style="font-size: 13px; color: #64748b; margin-bottom: 12px;">Just copy this into Claude Code and it'll set it up for you.</p>
+     <div class="features-section">
+       ${j.features_to_try
+         .map(
+           (S) => `
+         <div class="feature-card">
+           <div class="feature-title">${D9(S.feature || "")}</div>
+           <div class="feature-oneliner">${D9(S.one_liner || "")}</div>
+           <div class="feature-why"><strong>Why for you:</strong> ${D9(S.why_for_you || "")}</div>
+           ${
+             S.example_code
+               ? `
+           <div class="feature-examples">
+             <div class="feature-example">
+               <div class="example-code-row">
+                 <code class="example-code">${D9(S.example_code)}</code>
+                 <button class="copy-btn" onclick="copyText(this)">Copy</button>
+               </div>
+             </div>
+           </div>
+           `
+               : ""
+           }
+         </div>
+       `,
+         )
+         .join("")}
+     </div>
+     `
+         : ""
+     }
+     ${
+       j.usage_patterns && j.usage_patterns.length > 0
+         ? `
+     <h2 id="section-patterns">New Ways to Use Claude Code</h2>
+     <p style="font-size: 13px; color: #64748b; margin-bottom: 12px;">Just copy this into Claude Code and it'll walk you through it.</p>
+     <div class="patterns-section">
+       ${j.usage_patterns
+         .map(
+           (S) => `
+         <div class="pattern-card">
+           <div class="pattern-title">${D9(S.title || "")}</div>
+           <div class="pattern-summary">${D9(S.suggestion || "")}</div>
+           ${S.detail ? `<div class="pattern-detail">${D9(S.detail)}</div>` : ""}
+           ${
+             S.copyable_prompt
+               ? `
+           <div class="copyable-prompt-section">
+             <div class="prompt-label">Paste into Claude Code:</div>
+             <div class="copyable-prompt-row">
+               <code class="copyable-prompt">${D9(S.copyable_prompt)}</code>
+               <button class="copy-btn" onclick="copyText(this)">Copy</button>
+             </div>
+           </div>
+           `
+               : ""
+           }
+         </div>
+       `,
+         )
+         .join("")}
+     </div>
+     `
+         : ""
+     }
+     `
+       : "",
+     W = q.on_the_horizon,
+     G =
+       W?.opportunities && W.opportunities.length > 0
+         ? `
+     <h2 id="section-horizon">On the Horizon</h2>
+     ${W.intro ? `<p class="section-intro">${D9(W.intro)}</p>` : ""}
+     <div class="horizon-section">
+       ${W.opportunities
+         .map(
+           (S) => `
+         <div class="horizon-card">
+           <div class="horizon-title">${D9(S.title || "")}</div>
+           <div class="horizon-possible">${D9(S.whats_possible || "")}</div>
+           ${S.how_to_try ? `<div class="horizon-tip"><strong>Getting started:</strong> ${D9(S.how_to_try)}</div>` : ""}
+           ${S.copyable_prompt ? `<div class="pattern-prompt"><div class="prompt-label">Paste into Claude Code:</div><code>${D9(S.copyable_prompt)}</code><button class="copy-btn" onclick="copyText(this)">Copy</button></div>` : ""}
+         </div>
+       `,
+         )
+         .join("")}
+     </div>
+     `
+         : "",
+     P = [],
+     V = [],
+     Z =
+       P.length > 0 || V.length > 0
+         ? `
+     <h2 id="section-feedback" class="feedback-header">Closing the Loop: Feedback for Other Teams</h2>
+     <p class="feedback-intro">Suggestions for the CC product and model teams based on your usage patterns. Click to expand.</p>
+     ${
+       P.length > 0
+         ? `
+     <div class="collapsible-section">
+       <div class="collapsible-header" onclick="toggleCollapsible(this)">
+         <span class="collapsible-arrow">▶</span>
+         <h3>Product Improvements for CC Team</h3>
+       </div>
+       <div class="collapsible-content">
+         <div class="suggestions-section">
+           ${P.map(
+             (S) => `
+             <div class="feedback-card team-card">
+               <div class="feedback-title">${D9(S.title || "")}</div>
+               <div class="feedback-detail">${D9(S.detail || "")}</div>
+               ${S.evidence ? `<div class="feedback-evidence"><em>Evidence:</em> ${D9(S.evidence)}</div>` : ""}
+             </div>
+           `,
+           ).join("")}
+         </div>
+       </div>
+     </div>
+     `
+         : ""
+     }
+     ${
+       V.length > 0
+         ? `
+     <div class="collapsible-section">
+       <div class="collapsible-header" onclick="toggleCollapsible(this)">
+         <span class="collapsible-arrow">▶</span>
+         <h3>Model Behavior Improvements</h3>
+       </div>
+       <div class="collapsible-content">
+         <div class="suggestions-section">
+           ${V.map(
+             (S) => `
+             <div class="feedback-card model-card">
+               <div class="feedback-title">${D9(S.title || "")}</div>
+               <div class="feedback-detail">${D9(S.detail || "")}</div>
+               ${S.evidence ? `<div class="feedback-evidence"><em>Evidence:</em> ${D9(S.evidence)}</div>` : ""}
+             </div>
+           `,
+           ).join("")}
+         </div>
+       </div>
+     </div>
+     `
+         : ""
+     }
+     `
+         : "",
+     N = q.fun_ending,
+     T = N?.headline
+       ? `
+     <div class="fun-ending">
+       <div class="fun-headline">"${D9(N.headline)}"</div>
+       ${N.detail ? `<div class="fun-detail">${D9(N.detail)}</div>` : ""}
+     </div>
+     `
+       : "",
+     k = `
+     * { box-sizing: border-box; margin: 0; padding: 0; }
+     body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; background: #f8fafc; color: #334155; line-height: 1.65; padding: 48px 24px; }
+     .container { max-width: 800px; margin: 0 auto; }
+     h1 { font-size: 32px; font-weight: 700; color: #0f172a; margin-bottom: 8px; }
+     h2 { font-size: 20px; font-weight: 600; color: #0f172a; margin-top: 48px; margin-bottom: 16px; }
+     .subtitle { color: #64748b; font-size: 15px; margin-bottom: 32px; }
+     .nav-toc { display: flex; flex-wrap: wrap; gap: 8px; margin: 24px 0 32px 0; padding: 16px; background: white; border-radius: 8px; border: 1px solid #e2e8f0; }
+     .nav-toc a { font-size: 12px; color: #64748b; text-decoration: none; padding: 6px 12px; border-radius: 6px; background: #f1f5f9; transition: all 0.15s; }
+     .nav-toc a:hover { background: #e2e8f0; color: #334155; }
+     .stats-row { display: flex; gap: 24px; margin-bottom: 40px; padding: 20px 0; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0; flex-wrap: wrap; }
+     .stat { text-align: center; }
+     .stat-value { font-size: 24px; font-weight: 700; color: #0f172a; }
+     .stat-label { font-size: 11px; color: #64748b; text-transform: uppercase; }
+     .at-a-glance { background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border: 1px solid #f59e0b; border-radius: 12px; padding: 20px 24px; margin-bottom: 32px; }
+     .glance-title { font-size: 16px; font-weight: 700; color: #92400e; margin-bottom: 16px; }
+     .glance-sections { display: flex; flex-direction: column; gap: 12px; }
+     .glance-section { font-size: 14px; color: #78350f; line-height: 1.6; }
+     .glance-section strong { color: #92400e; }
+     .see-more { color: #b45309; text-decoration: none; font-size: 13px; white-space: nowrap; }
+     .see-more:hover { text-decoration: underline; }
+     .project-areas { display: flex; flex-direction: column; gap: 12px; margin-bottom: 32px; }
+     .project-area { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; }
+     .area-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
+     .area-name { font-weight: 600; font-size: 15px; color: #0f172a; }
+     .area-count { font-size: 12px; color: #64748b; background: #f1f5f9; padding: 2px 8px; border-radius: 4px; }
+     .area-desc { font-size: 14px; color: #475569; line-height: 1.5; }
+     .narrative { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin-bottom: 24px; }
+     .narrative p { margin-bottom: 12px; font-size: 14px; color: #475569; line-height: 1.7; }
+     .key-insight { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 12px 16px; margin-top: 12px; font-size: 14px; color: #166534; }
+     .section-intro { font-size: 14px; color: #64748b; margin-bottom: 16px; }
+     .big-wins { display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px; }
+     .big-win { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 16px; }
+     .big-win-title { font-weight: 600; font-size: 15px; color: #166534; margin-bottom: 8px; }
+     .big-win-desc { font-size: 14px; color: #15803d; line-height: 1.5; }
+     .friction-categories { display: flex; flex-direction: column; gap: 16px; margin-bottom: 24px; }
+     .friction-category { background: #fef2f2; border: 1px solid #fca5a5; border-radius: 8px; padding: 16px; }
+     .friction-title { font-weight: 600; font-size: 15px; color: #991b1b; margin-bottom: 6px; }
+     .friction-desc { font-size: 13px; color: #7f1d1d; margin-bottom: 10px; }
+     .friction-examples { margin: 0 0 0 20px; font-size: 13px; color: #334155; }
+     .friction-examples li { margin-bottom: 4px; }
+     .claude-md-section { background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 16px; margin-bottom: 20px; }
+     .claude-md-section h3 { font-size: 14px; font-weight: 600; color: #1e40af; margin: 0 0 12px 0; }
+     .claude-md-actions { margin-bottom: 12px; padding-bottom: 12px; border-bottom: 1px solid #dbeafe; }
+     .copy-all-btn { background: #2563eb; color: white; border: none; border-radius: 4px; padding: 6px 12px; font-size: 12px; cursor: pointer; font-weight: 500; transition: all 0.2s; }
+     .copy-all-btn:hover { background: #1d4ed8; }
+     .copy-all-btn.copied { background: #16a34a; }
+     .claude-md-item { display: flex; flex-wrap: wrap; align-items: flex-start; gap: 8px; padding: 10px 0; border-bottom: 1px solid #dbeafe; }
+     .claude-md-item:last-child { border-bottom: none; }
+     .cmd-checkbox { margin-top: 2px; }
+     .cmd-code { background: white; padding: 8px 12px; border-radius: 4px; font-size: 12px; color: #1e40af; border: 1px solid #bfdbfe; font-family: monospace; display: block; white-space: pre-wrap; word-break: break-word; flex: 1; }
+     .cmd-why { font-size: 12px; color: #64748b; width: 100%; padding-left: 24px; margin-top: 4px; }
+     .features-section, .patterns-section { display: flex; flex-direction: column; gap: 12px; margin: 16px 0; }
+     .feature-card { background: #f0fdf4; border: 1px solid #86efac; border-radius: 8px; padding: 16px; }
+     .pattern-card { background: #f0f9ff; border: 1px solid #7dd3fc; border-radius: 8px; padding: 16px; }
+     .feature-title, .pattern-title { font-weight: 600; font-size: 15px; color: #0f172a; margin-bottom: 6px; }
+     .feature-oneliner { font-size: 14px; color: #475569; margin-bottom: 8px; }
+     .pattern-summary { font-size: 14px; color: #475569; margin-bottom: 8px; }
+     .feature-why, .pattern-detail { font-size: 13px; color: #334155; line-height: 1.5; }
+     .feature-examples { margin-top: 12px; }
+     .feature-example { padding: 8px 0; border-top: 1px solid #d1fae5; }
+     .feature-example:first-child { border-top: none; }
+     .example-desc { font-size: 13px; color: #334155; margin-bottom: 6px; }
+     .example-code-row { display: flex; align-items: flex-start; gap: 8px; }
+     .example-code { flex: 1; background: #f1f5f9; padding: 8px 12px; border-radius: 4px; font-family: monospace; font-size: 12px; color: #334155; overflow-x: auto; white-space: pre-wrap; }
+     .copyable-prompt-section { margin-top: 12px; padding-top: 12px; border-top: 1px solid #e2e8f0; }
+     .copyable-prompt-row { display: flex; align-items: flex-start; gap: 8px; }
+     .copyable-prompt { flex: 1; background: #f8fafc; padding: 10px 12px; border-radius: 4px; font-family: monospace; font-size: 12px; color: #334155; border: 1px solid #e2e8f0; white-space: pre-wrap; line-height: 1.5; }
+     .feature-code { background: #f8fafc; padding: 12px; border-radius: 6px; margin-top: 12px; border: 1px solid #e2e8f0; display: flex; align-items: flex-start; gap: 8px; }
+     .feature-code code { flex: 1; font-family: monospace; font-size: 12px; color: #334155; white-space: pre-wrap; }
+     .pattern-prompt { background: #f8fafc; padding: 12px; border-radius: 6px; margin-top: 12px; border: 1px solid #e2e8f0; }
+     .pattern-prompt code { font-family: monospace; font-size: 12px; color: #334155; display: block; white-space: pre-wrap; margin-bottom: 8px; }
+     .prompt-label { font-size: 11px; font-weight: 600; text-transform: uppercase; color: #64748b; margin-bottom: 6px; }
+     .copy-btn { background: #e2e8f0; border: none; border-radius: 4px; padding: 4px 8px; font-size: 11px; cursor: pointer; color: #475569; flex-shrink: 0; }
+     .copy-btn:hover { background: #cbd5e1; }
+     .charts-row { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin: 24px 0; }
+     .chart-card { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; }
+     .chart-title { font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase; margin-bottom: 12px; }
+     .bar-row { display: flex; align-items: center; margin-bottom: 6px; }
+     .bar-label { width: 100px; font-size: 11px; color: #475569; flex-shrink: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
+     .bar-track { flex: 1; height: 6px; background: #f1f5f9; border-radius: 3px; margin: 0 8px; }
+     .bar-fill { height: 100%; border-radius: 3px; }
+     .bar-value { width: 28px; font-size: 11px; font-weight: 500; color: #64748b; text-align: right; }
+     .empty { color: #94a3b8; font-size: 13px; }
+     .horizon-section { display: flex; flex-direction: column; gap: 16px; }
+     .horizon-card { background: linear-gradient(135deg, #faf5ff 0%, #f5f3ff 100%); border: 1px solid #c4b5fd; border-radius: 8px; padding: 16px; }
+     .horizon-title { font-weight: 600; font-size: 15px; color: #5b21b6; margin-bottom: 8px; }
+     .horizon-possible { font-size: 14px; color: #334155; margin-bottom: 10px; line-height: 1.5; }
+     .horizon-tip { font-size: 13px; color: #6b21a8; background: rgba(255,255,255,0.6); padding: 8px 12px; border-radius: 4px; }
+     .feedback-header { margin-top: 48px; color: #64748b; font-size: 16px; }
+     .feedback-intro { font-size: 13px; color: #94a3b8; margin-bottom: 16px; }
+     .feedback-section { margin-top: 16px; }
+     .feedback-section h3 { font-size: 14px; font-weight: 600; color: #475569; margin-bottom: 12px; }
+     .feedback-card { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin-bottom: 12px; }
+     .feedback-card.team-card { background: #eff6ff; border-color: #bfdbfe; }
+     .feedback-card.model-card { background: #faf5ff; border-color: #e9d5ff; }
+     .feedback-title { font-weight: 600; font-size: 14px; color: #0f172a; margin-bottom: 6px; }
+     .feedback-detail { font-size: 13px; color: #475569; line-height: 1.5; }
+     .feedback-evidence { font-size: 12px; color: #64748b; margin-top: 8px; }
+     .fun-ending { background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border: 1px solid #fbbf24; border-radius: 12px; padding: 24px; margin-top: 40px; text-align: center; }
+     .fun-headline { font-size: 18px; font-weight: 600; color: #78350f; margin-bottom: 8px; }
+     .fun-detail { font-size: 14px; color: #92400e; }
+     .collapsible-section { margin-top: 16px; }
+     .collapsible-header { display: flex; align-items: center; gap: 8px; cursor: pointer; padding: 12px 0; border-bottom: 1px solid #e2e8f0; }
+     .collapsible-header h3 { margin: 0; font-size: 14px; font-weight: 600; color: #475569; }
+     .collapsible-arrow { font-size: 12px; color: #94a3b8; transition: transform 0.2s; }
+     .collapsible-content { display: none; padding-top: 16px; }
+     .collapsible-content.open { display: block; }
+     .collapsible-header.open .collapsible-arrow { transform: rotate(90deg); }
+     @media (max-width: 640px) { .charts-row { grid-template-columns: 1fr; } .stats-row { justify-content: center; } }
+   `,
+     u = `
+     function toggleCollapsible(header) {
+       header.classList.toggle('open');
+       const content = header.nextElementSibling;
+       content.classList.toggle('open');
+     }
+     function copyText(btn) {
+       const code = btn.previousElementSibling;
+       navigator.clipboard.writeText(code.textContent).then(() => {
+         btn.textContent = 'Copied!';
+         setTimeout(() => { btn.textContent = 'Copy'; }, 2000);
+       });
+     }
+     function copyCmdItem(idx) {
+       const checkbox = document.getElementById('cmd-' + idx);
+       if (checkbox) {
+         const text = checkbox.dataset.text;
+         navigator.clipboard.writeText(text).then(() => {
+           const btn = checkbox.nextElementSibling.querySelector('.copy-btn');
+           if (btn) { btn.textContent = 'Copied!'; setTimeout(() => { btn.textContent = 'Copy'; }, 2000); }
+         });
+       }
+     }
+     function copyAllCheckedClaudeMd() {
+       const checkboxes = document.querySelectorAll('.cmd-checkbox:checked');
+       const texts = [];
+       checkboxes.forEach(cb => {
+         if (cb.dataset.text) { texts.push(cb.dataset.text); }
+       });
+       const combined = texts.join('\\n');
+       const btn = document.querySelector('.copy-all-btn');
+       if (btn) {
+         navigator.clipboard.writeText(combined).then(() => {
+           btn.textContent = 'Copied ' + texts.length + ' items!';
+           btn.classList.add('copied');
+           setTimeout(() => { btn.textContent = 'Copy All Checked'; btn.classList.remove('copied'); }, 2000);
+         });
+       }
+     }
+     // Timezone selector for time of day chart (data is from our own analytics, not user input)
+     const rawHourCounts = ${$4z(A.message_hours)};
+     function updateHourHistogram(offsetFromPT) {
+       const periods = [
+         { label: "Morning (6-12)", range: [6,7,8,9,10,11] },
+         { label: "Afternoon (12-18)", range: [12,13,14,15,16,17] },
+         { label: "Evening (18-24)", range: [18,19,20,21,22,23] },
+         { label: "Night (0-6)", range: [0,1,2,3,4,5] }
+       ];
+       const adjustedCounts = {};
+       for (const [hour, count] of Object.entries(rawHourCounts)) {
+         const newHour = (parseInt(hour) + offsetFromPT + 24) % 24;
+         adjustedCounts[newHour] = (adjustedCounts[newHour] || 0) + count;
+       }
+       const periodCounts = periods.map(p => ({
+         label: p.label,
+         count: p.range.reduce((sum, h) => sum + (adjustedCounts[h] || 0), 0)
+       }));
+       const maxCount = Math.max(...periodCounts.map(p => p.count)) || 1;
+       const container = document.getElementById('hour-histogram');
+       container.textContent = '';
+       periodCounts.forEach(p => {
+         const row = document.createElement('div');
+         row.className = 'bar-row';
+         const label = document.createElement('div');
+         label.className = 'bar-label';
+         label.textContent = p.label;
+         const track = document.createElement('div');
+         track.className = 'bar-track';
+         const fill = document.createElement('div');
+         fill.className = 'bar-fill';
+         fill.style.width = (p.count / maxCount) * 100 + '%';
+         fill.style.background = '#8b5cf6';
+         track.appendChild(fill);
+         const value = document.createElement('div');
+         value.className = 'bar-value';
+         value.textContent = p.count;
+         row.appendChild(label);
+         row.appendChild(track);
+         row.appendChild(value);
+         container.appendChild(row);
+       });
+     }
+     document.getElementById('timezone-select').addEventListener('change', function() {
+       const customInput = document.getElementById('custom-offset');
+       if (this.value === 'custom') {
+         customInput.style.display = 'inline-block';
+         customInput.focus();
+       } else {
+         customInput.style.display = 'none';
+         updateHourHistogram(parseInt(this.value));
+       }
+     });
+     document.getElementById('custom-offset').addEventListener('change', function() {
+       const offset = parseInt(this.value) + 8;
+       updateHourHistogram(offset);
+     });
+   `;
+   return `<!DOCTYPE html>
+ <html>
+ <head>
+   <meta charset="utf-8">
+   <title>Claude Code Insights</title>
+   <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
+   <style>
+     * { box-sizing: border-box; margin: 0; padding: 0; }
+     body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; background: #f8fafc; color: #334155; line-height: 1.65; padding: 48px 24px; }
+     .container { max-width: 800px; margin: 0 auto; }
+     h1 { font-size: 32px; font-weight: 700; color: #0f172a; margin-bottom: 8px; }
+     h2 { font-size: 20px; font-weight: 600; color: #0f172a; margin-top: 48px; margin-bottom: 16px; }
+     .subtitle { color: #64748b; font-size: 15px; margin-bottom: 32px; }
+     .nav-toc { display: flex; flex-wrap: wrap; gap: 8px; margin: 24px 0 32px 0; padding: 16px; background: white; border-radius: 8px; border: 1px solid #e2e8f0; }
+     .nav-toc a { font-size: 12px; color: #64748b; text-decoration: none; padding: 6px 12px; border-radius: 6px; background: #f1f5f9; transition: all 0.15s; }
+     .nav-toc a:hover { background: #e2e8f0; color: #334155; }
+     .stats-row { display: flex; gap: 24px; margin-bottom: 40px; padding: 20px 0; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0; flex-wrap: wrap; }
+     .stat { text-align: center; }
+     .stat-value { font-size: 24px; font-weight: 700; color: #0f172a; }
+     .stat-label { font-size: 11px; color: #64748b; text-transform: uppercase; }
+     .at-a-glance { background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border: 1px solid #f59e0b; border-radius: 12px; padding: 20px 24px; margin-bottom: 32px; }
+     .glance-title { font-size: 16px; font-weight: 700; color: #92400e; margin-bottom: 16px; }
+     .glance-sections { display: flex; flex-direction: column; gap: 12px; }
+     .glance-section { font-size: 14px; color: #78350f; line-height: 1.6; }
+     .glance-section strong { color: #92400e; }
+     .see-more { color: #b45309; text-decoration: none; font-size: 13px; white-space: nowrap; }
+     .see-more:hover { text-decoration: underline; }
+     .project-areas { display: flex; flex-direction: column; gap: 12px; margin-bottom: 32px; }
+     .project-area { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; }
+     .area-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
+     .area-name { font-weight: 600; font-size: 15px; color: #0f172a; }
+     .area-count { font-size: 12px; color: #64748b; background: #f1f5f9; padding: 2px 8px; border-radius: 4px; }
+     .area-desc { font-size: 14px; color: #475569; line-height: 1.5; }
+     .narrative { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin-bottom: 24px; }
+     .narrative p { margin-bottom: 12px; font-size: 14px; color: #475569; line-height: 1.7; }
+     .key-insight { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 12px 16px; margin-top: 12px; font-size: 14px; color: #166534; }
+     .section-intro { font-size: 14px; color: #64748b; margin-bottom: 16px; }
+     .big-wins { display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px; }
+     .big-win { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 16px; }
+     .big-win-title { font-weight: 600; font-size: 15px; color: #166534; margin-bottom: 8px; }
+     .big-win-desc { font-size: 14px; color: #15803d; line-height: 1.5; }
+     .friction-categories { display: flex; flex-direction: column; gap: 16px; margin-bottom: 24px; }
+     .friction-category { background: #fef2f2; border: 1px solid #fca5a5; border-radius: 8px; padding: 16px; }
+     .friction-title { font-weight: 600; font-size: 15px; color: #991b1b; margin-bottom: 6px; }
+     .friction-desc { font-size: 13px; color: #7f1d1d; margin-bottom: 10px; }
+     .friction-examples { margin: 0 0 0 20px; font-size: 13px; color: #334155; }
+     .friction-examples li { margin-bottom: 4px; }
+     .claude-md-section { background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 16px; margin-bottom: 20px; }
+     .claude-md-section h3 { font-size: 14px; font-weight: 600; color: #1e40af; margin: 0 0 12px 0; }
+     .claude-md-actions { margin-bottom: 12px; padding-bottom: 12px; border-bottom: 1px solid #dbeafe; }
+     .copy-all-btn { background: #2563eb; color: white; border: none; border-radius: 4px; padding: 6px 12px; font-size: 12px; cursor: pointer; font-weight: 500; transition: all 0.2s; }
+     .copy-all-btn:hover { background: #1d4ed8; }
+     .copy-all-btn.copied { background: #16a34a; }
+     .claude-md-item { display: flex; flex-wrap: wrap; align-items: flex-start; gap: 8px; padding: 10px 0; border-bottom: 1px solid #dbeafe; }
+     .claude-md-item:last-child { border-bottom: none; }
+     .cmd-checkbox { margin-top: 2px; }
+     .cmd-code { background: white; padding: 8px 12px; border-radius: 4px; font-size: 12px; color: #1e40af; border: 1px solid #bfdbfe; font-family: monospace; display: block; white-space: pre-wrap; word-break: break-word; flex: 1; }
+     .cmd-why { font-size: 12px; color: #64748b; width: 100%; padding-left: 24px; margin-top: 4px; }
+     .features-section, .patterns-section { display: flex; flex-direction: column; gap: 12px; margin: 16px 0; }
+     .feature-card { background: #f0fdf4; border: 1px solid #86efac; border-radius: 8px; padding: 16px; }
+     .pattern-card { background: #f0f9ff; border: 1px solid #7dd3fc; border-radius: 8px; padding: 16px; }
+     .feature-title, .pattern-title { font-weight: 600; font-size: 15px; color: #0f172a; margin-bottom: 6px; }
+     .feature-oneliner { font-size: 14px; color: #475569; margin-bottom: 8px; }
+     .pattern-summary { font-size: 14px; color: #475569; margin-bottom: 8px; }
+     .feature-why, .pattern-detail { font-size: 13px; color: #334155; line-height: 1.5; }
+     .feature-examples { margin-top: 12px; }
+     .feature-example { padding: 8px 0; border-top: 1px solid #d1fae5; }
+     .feature-example:first-child { border-top: none; }
+     .example-desc { font-size: 13px; color: #334155; margin-bottom: 6px; }
+     .example-code-row { display: flex; align-items: flex-start; gap: 8px; }
+     .example-code { flex: 1; background: #f1f5f9; padding: 8px 12px; border-radius: 4px; font-family: monospace; font-size: 12px; color: #334155; overflow-x: auto; white-space: pre-wrap; }
+     .copyable-prompt-section { margin-top: 12px; padding-top: 12px; border-top: 1px solid #e2e8f0; }
+     .copyable-prompt-row { display: flex; align-items: flex-start; gap: 8px; }
+     .copyable-prompt { flex: 1; background: #f8fafc; padding: 10px 12px; border-radius: 4px; font-family: monospace; font-size: 12px; color: #334155; border: 1px solid #e2e8f0; white-space: pre-wrap; line-height: 1.5; }
+     .feature-code { background: #f8fafc; padding: 12px; border-radius: 6px; margin-top: 12px; border: 1px solid #e2e8f0; display: flex; align-items: flex-start; gap: 8px; }
+     .feature-code code { flex: 1; font-family: monospace; font-size: 12px; color: #334155; white-space: pre-wrap; }
+     .pattern-prompt { background: #f8fafc; padding: 12px; border-radius: 6px; margin-top: 12px; border: 1px solid #e2e8f0; }
+     .pattern-prompt code { font-family: monospace; font-size: 12px; color: #334155; display: block; white-space: pre-wrap; margin-bottom: 8px; }
+     .prompt-label { font-size: 11px; font-weight: 600; text-transform: uppercase; color: #64748b; margin-bottom: 6px; }
+     .copy-btn { background: #e2e8f0; border: none; border-radius: 4px; padding: 4px 8px; font-size: 11px; cursor: pointer; color: #475569; flex-shrink: 0; }
+     .copy-btn:hover { background: #cbd5e1; }
+     .charts-row { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin: 24px 0; }
+     .chart-card { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; }
+     .chart-title { font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase; margin-bottom: 12px; }
+     .bar-row { display: flex; align-items: center; margin-bottom: 6px; }
+     .bar-label { width: 100px; font-size: 11px; color: #475569; flex-shrink: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
+     .bar-track { flex: 1; height: 6px; background: #f1f5f9; border-radius: 3px; margin: 0 8px; }
+     .bar-fill { height: 100%; border-radius: 3px; }
+     .bar-value { width: 28px; font-size: 11px; font-weight: 500; color: #64748b; text-align: right; }
+     .empty { color: #94a3b8; font-size: 13px; }
+     .horizon-section { display: flex; flex-direction: column; gap: 16px; }
+     .horizon-card { background: linear-gradient(135deg, #faf5ff 0%, #f5f3ff 100%); border: 1px solid #c4b5fd; border-radius: 8px; padding: 16px; }
+     .horizon-title { font-weight: 600; font-size: 15px; color: #5b21b6; margin-bottom: 8px; }
+     .horizon-possible { font-size: 14px; color: #334155; margin-bottom: 10px; line-height: 1.5; }
+     .horizon-tip { font-size: 13px; color: #6b21a8; background: rgba(255,255,255,0.6); padding: 8px 12px; border-radius: 4px; }
+     .feedback-header { margin-top: 48px; color: #64748b; font-size: 16px; }
+     .feedback-intro { font-size: 13px; color: #94a3b8; margin-bottom: 16px; }
+     .feedback-section { margin-top: 16px; }
+     .feedback-section h3 { font-size: 14px; font-weight: 600; color: #475569; margin-bottom: 12px; }
+     .feedback-card { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin-bottom: 12px; }
+     .feedback-card.team-card { background: #eff6ff; border-color: #bfdbfe; }
+     .feedback-card.model-card { background: #faf5ff; border-color: #e9d5ff; }
+     .feedback-title { font-weight: 600; font-size: 14px; color: #0f172a; margin-bottom: 6px; }
+     .feedback-detail { font-size: 13px; color: #475569; line-height: 1.5; }
+     .feedback-evidence { font-size: 12px; color: #64748b; margin-top: 8px; }
+     .fun-ending { background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border: 1px solid #fbbf24; border-radius: 12px; padding: 24px; margin-top: 40px; text-align: center; }
+     .fun-headline { font-size: 18px; font-weight: 600; color: #78350f; margin-bottom: 8px; }
+     .fun-detail { font-size: 14px; color: #92400e; }
+     .collapsible-section { margin-top: 16px; }
+     .collapsible-header { display: flex; align-items: center; gap: 8px; cursor: pointer; padding: 12px 0; border-bottom: 1px solid #e2e8f0; }
+     .collapsible-header h3 { margin: 0; font-size: 14px; font-weight: 600; color: #475569; }
+     .collapsible-arrow { font-size: 12px; color: #94a3b8; transition: transform 0.2s; }
+     .collapsible-content { display: none; padding-top: 16px; }
+     .collapsible-content.open { display: block; }
+     .collapsible-header.open .collapsible-arrow { transform: rotate(90deg); }
+     @media (max-width: 640px) { .charts-row { grid-template-columns: 1fr; } .stats-row { justify-content: center; } }
+   </style>
+ </head>
+ <body>
+   <div class="container">
+     <h1>Claude Code Insights</h1>
+     <p class="subtitle">${A.total_messages.toLocaleString()} messages across ${A.total_sessions} sessions | ${A.date_range.start} to ${A.date_range.end}</p>
+ 
+     ${z}
+ 
+     <nav class="nav-toc">
+       <a href="#section-work">What You Work On</a>
+       <a href="#section-usage">How You Use CC</a>
+       <a href="#section-wins">Impressive Things</a>
+       <a href="#section-friction">Where Things Go Wrong</a>
+       <a href="#section-features">Features to Try</a>
+       <a href="#section-patterns">New Usage Patterns</a>
+       <a href="#section-horizon">On the Horizon</a>
+       <a href="#section-feedback">Team Feedback</a>
+     </nav>
+ 
+     <div class="stats-row">
+       <div class="stat"><div class="stat-value">${A.total_messages.toLocaleString()}</div><div class="stat-label">Messages</div></div>
+       <div class="stat"><div class="stat-value">+${A.total_lines_added.toLocaleString()}/-${A.total_lines_removed.toLocaleString()}</div><div class="stat-label">Lines</div></div>
+       <div class="stat"><div class="stat-value">${A.total_files_modified}</div><div class="stat-label">Files</div></div>
+       <div class="stat"><div class="stat-value">${A.days_active}</div><div class="stat-label">Days</div></div>
+       <div class="stat"><div class="stat-value">${A.messages_per_day}</div><div class="stat-label">Msgs/Day</div></div>
+     </div>
+ 
+     ${H}
+ 
+     <div class="charts-row">
+       <div class="chart-card">
+         <div class="chart-title">What You Wanted</div>
+         ${od(A.goal_categories, "#2563eb")}
+       </div>
+       <div class="chart-card">
+         <div class="chart-title">Top Tools Used</div>
+         ${od(A.tool_counts, "#0891b2")}
+       </div>
+     </div>
+ 
+     <div class="charts-row">
+       <div class="chart-card">
+         <div class="chart-title">Languages</div>
+         ${od(A.languages, "#10b981")}
+       </div>
+       <div class="chart-card">
+         <div class="chart-title">Session Types</div>
+         ${od(A.session_types || {}, "#8b5cf6")}
+       </div>
+     </div>
+ 
+     ${$}
+ 
+     <!-- Response Time Distribution -->
+     <div class="chart-card" style="margin: 24px 0;">
+       <div class="chart-title">User Response Time Distribution</div>
+       ${H4z(A.user_response_times)}
+       <div style="font-size: 12px; color: #64748b; margin-top: 8px;">
+         Median: ${A.median_response_time.toFixed(1)}s &bull; Average: ${A.avg_response_time.toFixed(1)}s
+       </div>
+     </div>
+ 
+     <!-- Multi-clauding Section (matching Python reference) -->
+     <div class="chart-card" style="margin: 24px 0;">
+       <div class="chart-title">Multi-Clauding (Parallel Sessions)</div>
+       ${
+         A.multi_clauding.overlap_events === 0
+           ? `
+         <p style="font-size: 14px; color: #64748b; padding: 8px 0;">
+           No parallel session usage detected. You typically work with one Claude Code session at a time.
+         </p>
+       `
+           : `
+         <div style="display: flex; gap: 24px; margin: 12px 0;">
+           <div style="text-align: center;">
+             <div style="font-size: 24px; font-weight: 700; color: #7c3aed;">${A.multi_clauding.overlap_events}</div>
+             <div style="font-size: 11px; color: #64748b; text-transform: uppercase;">Overlap Events</div>
+           </div>
+           <div style="text-align: center;">
+             <div style="font-size: 24px; font-weight: 700; color: #7c3aed;">${A.multi_clauding.sessions_involved}</div>
+             <div style="font-size: 11px; color: #64748b; text-transform: uppercase;">Sessions Involved</div>
+           </div>
+           <div style="text-align: center;">
+             <div style="font-size: 24px; font-weight: 700; color: #7c3aed;">${A.total_messages > 0 ? Math.round((100 * A.multi_clauding.user_messages_during) / A.total_messages) : 0}%</div>
+             <div style="font-size: 11px; color: #64748b; text-transform: uppercase;">Of Messages</div>
+           </div>
+         </div>
+         <p style="font-size: 13px; color: #475569; margin-top: 12px;">
+           You run multiple Claude Code sessions simultaneously. Multi-clauding is detected when sessions
+           overlap in time, suggesting parallel workflows.
+         </p>
+       `
+       }
+     </div>
+ 
+     <!-- Time of Day & Tool Errors -->
+     <div class="charts-row">
+       <div class="chart-card">
+         <div class="chart-title" style="display: flex; align-items: center; gap: 12px;">
+           User Messages by Time of Day
+           <select id="timezone-select" style="font-size: 12px; padding: 4px 8px; border-radius: 4px; border: 1px solid #e2e8f0;">
+             <option value="0">PT (UTC-8)</option>
+             <option value="3">ET (UTC-5)</option>
+             <option value="8">London (UTC)</option>
+             <option value="9">CET (UTC+1)</option>
+             <option value="17">Tokyo (UTC+9)</option>
+             <option value="custom">Custom offset...</option>
+           </select>
+           <input type="number" id="custom-offset" placeholder="UTC offset" style="display: none; width: 80px; font-size: 12px; padding: 4px; border-radius: 4px; border: 1px solid #e2e8f0;">
+         </div>
+         ${O4z(A.message_hours)}
+       </div>
+       <div class="chart-card">
+         <div class="chart-title">Tool Errors Encountered</div>
+         ${Object.keys(A.tool_error_categories).length > 0 ? od(A.tool_error_categories, "#dc2626") : '<p class="empty">No tool errors</p>'}
+       </div>
+     </div>
+ 
+     ${J}
+ 
+     <div class="charts-row">
+       <div class="chart-card">
+         <div class="chart-title">What Helped Most (Claude's Capabilities)</div>
+         ${od(A.success, "#16a34a")}
+       </div>
+       <div class="chart-card">
+         <div class="chart-title">Outcomes</div>
+         ${od(A.outcomes, "#8b5cf6", 6, w4z)}
+       </div>
+     </div>
+ 
+     ${D}
+ 
+     <div class="charts-row">
+       <div class="chart-card">
+         <div class="chart-title">Primary Friction Types</div>
+         ${od(A.friction, "#dc2626")}
+       </div>
+       <div class="chart-card">
+         <div class="chart-title">Inferred Satisfaction (model-estimated)</div>
+         ${od(A.satisfaction, "#eab308", 6, z4z)}
+       </div>
+     </div>
+ 
+     ${M}
+ 
+     ${G}
+ 
+     ${T}
+ 
+     ${Z}
+   </div>
+   <script>${u}</script>
+ </body>
+ </html>`;
+ }

+++ Added N4z (pretty-v2.1.32.js:512354-512354)
+   N4z = "Claude Opus 4.6",

+++ Added T4z (pretty-v2.1.32.js:512355-512355)
+   T4z = "claude-opus-4-6",

+++ Added aV (pretty-v2.1.32.js:512360-512403)
+ var aV = v(() => {
+   Z5();
+   a9();
+   Z7();
+   R8();
+   OD();
+   oH();
+   k_1();
+   Rq();
+   pO1();
+   W_();
+   iD();
+   lB();
+   MP();
+   Xb1();
+   az();
+   Eq();
+   a6();
+   BA();
+   a4();
+   Q7();
+   g4();
+   fZ6();
+   obA();
+   Wz();
+   _6();
+   SjA();
+   i2q();
+   abA = {
+     opus: "claude-opus-4-6",
+     sonnet: "claude-sonnet-4-5-20250929",
+     haiku: "claude-haiku-4-5-20251001",
+   };
+   Ywq = qA(async function () {
+     try {
+       let { stdout: A } = await CA("uname", ["-sr"], {
+         preserveOutputOnError: !1,
+       });
+       return A.trim();
+     } catch {
+       return "unknown";
+     }
+   });
+ });

+++ Added Xwq (pretty-v2.1.32.js:513575-513577)
+ var Xwq = v(() => {
+   s4z = /(?<!<)<<(?!<)(-)?[ \t]*(['"])?\\?(\w+)\2?/;
+ });

+++ Added xk4 (pretty-v2.1.32.js:513760-513764)
+ function xk4(A) {
+   let { processedCommand: q } = mV6(A);
+   if (!Qz(q, (Y) => `$${Y}`).success) return !0;
+   return vX(A).length > 1 && !Hqz(A);
+ }

+++ Added Uqz (pretty-v2.1.32.js:517021-517028)
+ function Uqz(A) {
+   if (A.length === 0) return !1;
+   for (let q of A) {
+     if (q.type !== "text") return !1;
+     if (q.text !== void 0 && q.text.trim() !== "") return !1;
+   }
+   return !0;
+ }

+++ Added CQ1 (pretty-v2.1.32.js:517029-517053)
+ function CQ1(A) {
+   let q = !1,
+     K = A.filter((z) => {
+       if (z.type !== "assistant") return !0;
+       let w = z.message.content;
+       if (!Array.isArray(w) || w.length === 0) return !0;
+       if (Uqz(w))
+         return (
+           (q = !0),
+           c("tengu_filtered_whitespace_only_assistant", {
+             messageUUID: z.uuid,
+           }),
+           !1
+         );
+       return !0;
+     });
+   if (!q) return A;
+   let Y = [];
+   for (let z of K) {
+     let w = Y[Y.length - 1];
+     if (z.type === "user" && w?.type === "user") Y[Y.length - 1] = Fwq(w, z);
+     else Y.push(z);
+   }
+   return Y;
+ }

+++ Added Ct4 (pretty-v2.1.32.js:517282-517282)
+ var Ct4 = {};

+++ Added NuA (pretty-v2.1.32.js:518030-518033)
+ function NuA(A, q) {
+   let K = oO(A);
+   je(K, { type: "agent-setting", agentSetting: q, sessionId: A });
+ }

+++ Added hSA (pretty-v2.1.32.js:518396-518407)
+ function hSA(A) {
+   let q = {};
+   for (let K of Object.values(A))
+     if (
+       K.type === "in_process_teammate" &&
+       K.identity?.agentId &&
+       K.messages &&
+       K.messages.length > 0
+     )
+       q[K.identity.agentId] = K.messages;
+   return q;
+ }

+++ Added kKz (pretty-v2.1.32.js:518980-518982)
+ function kKz(A) {
+   return zZ1(A).startsWith(XV6());
+ }

+++ Added zOq (pretty-v2.1.32.js:522382-522382)
+ var zOq = {};

+++ Added HOq (pretty-v2.1.32.js:522906-522906)
+ var HOq = {};

+++ Added u9z (pretty-v2.1.32.js:525850-525859)
+ function u9z(A) {
+   return A.filter((q) => q.type === "user")
+     .map((q) => {
+       let K = q.message.content;
+       if (typeof K === "string") return K;
+       return K.filter((Y) => Y.type === "text").map((Y) => Y.text).join(`
+ `);
+     })
+     .filter((q) => q.trim().length > 0);
+ }

+++ Added B9z (pretty-v2.1.32.js:525863-525994)
+ var B9z = `# Skillify {{userDescriptionBlock}}
+ 
+ You are capturing this session's repeatable process as a reusable skill.
+ 
+ ## Your Session Context
+ 
+ Here is the session memory summary:
+ <session_memory>
+ {{sessionMemory}}
+ </session_memory>
+ 
+ Here are the user's messages during this session. Pay attention to how they steered the process, to help capture their detailed preferences in the skill:
+ <user_messages>
+ {{userMessages}}
+ </user_messages>
+ 
+ ## Your Task
+ 
+ ### Step 1: Analyze the Session
+ 
+ Before asking any questions, analyze the session to identify:
+ - What repeatable process was performed
+ - What the inputs/parameters were
+ - The distinct steps (in order)
+ - The success artifacts/criteria (e.g. not just "writing code," but "an open PR with CI fully passing") for each step
+ - Where the user corrected or steered you
+ - What tools and permissions were needed
+ - What agents were used
+ - What the goals and success artifacts were
+ 
+ ### Step 2: Interview the User
+ 
+ You will use the AskUserQuestion to understand what the user wants to automate. Important notes:
+ - Use AskUserQuestion for ALL questions! Never ask questions via plain text.
+ - For each round, iterate as much as needed until the user is happy.
+ - The user always has a freeform "Other" option to type edits or feedback -- do NOT add your own "Needs tweaking" or "I'll provide edits" option. Just offer the substantive choices.
+ 
+ **Round 1: High level confirmation**
+ - Suggest a name and description for the skill based on your analysis. Ask the user to confirm or rename.
+ - Suggest high-level goal(s) and specific success criteria for the skill.
+ 
+ **Round 2: More details**
+ - Present the high-level steps you identified as a numbered list. Tell the user you will dig into the detail in the next round.
+ - If you think the skill will require arguments, suggest arguments based on what you observed. Make sure you understand what someone would need to provide.
+ - If it's not clear, ask if this skill should run inline (in the current conversation) or forked (as a sub-agent with its own context). Forked is better for self-contained tasks that don't need mid-process user input; inline is better when the user wants to steer mid-process.
+ 
+ **Round 3: Breaking down each step**
+ For each major step, if it's not glaringly obvious, ask:
+ - What does this step produce that later steps need? (data, artifacts, IDs)
+ - What proves that this step succeeded, and that we can move on?
+ - Should the user be asked to confirm before proceeding? (especially for irreversible actions like merging, sending messages, or destructive operations)
+ - Are any steps independent and could run in parallel? (e.g., posting to Slack and monitoring CI at the same time)
+ - How should the skill be executed? (e.g. always use a Task agent to conduct code review, or invoke an agent team for a set of concurrent steps)
+ - What are the hard constraints or hard preferences? Things that must or must not happen?
+ 
+ You may do multiple rounds of AskUserQuestion here, one round per step, especially if there are more than 3 steps or many clarification questions. Iterate as much as needed.
+ 
+ IMPORTANT: Pay special attention to places where the user corrected you during the session, to help inform your design.
+ 
+ **Round 4: Final questions**
+ - Confirm when this skill should be invoked, and suggest/confirm trigger phrases too. (e.g. For a cherrypick workflow you could say: Use when the user wants to cherry-pick a PR to a release branch. Examples: 'cherry-pick to release', 'CP this PR', 'hotfix.')
+ - You can also ask for any other gotchas or things to watch out for, if it's still unclear.
+ 
+ Stop interviewing once you have enough information. IMPORTANT: Don't over-ask for simple processes!
+ 
+ ### Step 3: Write the SKILL.md
+ 
+ Create the skill directory and file at \`.claude/skills/{{skillName}}/SKILL.md\`.
+ 
+ Use this format:
+ 
+ \`\`\`markdown
+ ---
+ name: {{skill-name}}
+ description: {{one-line description}}
+ allowed-tools:
+   {{list of tool permission patterns observed during session}}
+ when_to_use: {{detailed description of when Claude should automatically invoke this skill, including trigger phrases and example user messages}}
+ argument-hint: "{{hint showing argument placeholders}}"
+ arguments:
+   {{list of argument names}}
+ context: {{inline or fork -- omit for inline}}
+ ---
+ 
+ # {{Skill Title}}
+ Description of skill
+ 
+ ## Inputs
+ - \`$arg_name\`: Description of this input
+ 
+ ## Goal
+ Clearly stated goal for this workflow. Best if you have clearly defined artifacts or criteria for completion.
+ 
+ ## Steps
+ 
+ ### 1. Step Name
+ What to do in this step. Be specific and actionable. Include commands when appropriate.
+ 
+ **Success criteria**: ALWAYS include this! This shows that the step is done and we can move on. Can be a list.
+ 
+ IMPORTANT: see the next section below for the per-step annotations you can optionally include for each step.
+ 
+ ...
+ \`\`\`
+ 
+ **Per-step annotations**:
+ - **Success criteria** is REQUIRED on every step. This helps the model understand what the user expects from their workflow, and when it should have the confidence to move on.
+ - **Execution**: \`Direct\` (default), \`Task agent\` (straightforward subagents), \`Teammate\` (agent with true parallelism and inter-agent communication), or \`[human]\` (user does it). Only needs specifying if not Direct.
+ - **Artifacts**: Data this step produces that later steps need (e.g., PR number, commit SHA). Only include if later steps depend on it.
+ - **Human checkpoint**: When to pause and ask the user before proceeding. Include for irreversible actions (merging, sending messages), error judgment (merge conflicts), or output review.
+ - **Rules**: Hard rules for the workflow. User corrections during the reference session can be especially useful here.
+ 
+ **Step structure tips:**
+ - Steps that can run concurrently use sub-numbers: 3a, 3b
+ - Steps requiring the user to act get \`[human]\` in the title
+ - Keep simple skills simple -- a 2-step skill doesn't need annotations on every step
+ 
+ **Frontmatter rules:**
+ - \`allowed-tools\`: Minimum permissions needed (use patterns like \`Bash(gh:*)\` not \`Bash\`)
+ - \`context\`: Only set \`context: fork\` for self-contained skills that don't need mid-process user input.
+ - \`when_to_use\` is CRITICAL -- tells the model when to auto-invoke. Start with "Use when..." and include trigger phrases. Example: "Use when the user wants to cherry-pick a PR to a release branch. Examples: 'cherry-pick to release', 'CP this PR', 'hotfix'."
+ - \`arguments\` and \`argument-hint\`: Only include if the skill takes parameters. Use \`$name\` in the body for substitution.
+ 
+ ### Step 4: Confirm and Save
+ 
+ Before writing the file, show the user the complete SKILL.md content and ask for final confirmation using AskUserQuestion.
+ 
+ After writing, tell the user:
+ - Where the skill was saved
+ - How to invoke it: \`/{{skill-name}} [arguments]\`
+ - That they can edit the SKILL.md directly to refine it
+ `;

+++ Added $$q (pretty-v2.1.32.js:525999-526001)
+ function $$q() {
+   if ((gOq(), cOq(), rOq(), aOq(), tOq(), A$q(), z$q(), H$q(), rP1())) pOq();
+ }

+++ Added _$q (pretty-v2.1.32.js:526002-526013)
+ var _$q = v(() => {
+   UOq();
+   dOq();
+   lOq();
+   oOq();
+   sOq();
+   eOq();
+   q$q();
+   w$q();
+   O$q();
+   $91();
+ });

+++ Added DZ1 (pretty-v2.1.32.js:526235-526235)
+   DZ1 = null,

+++ Added M$q (pretty-v2.1.32.js:526237-526237)
+   M$q = !1;

+++ Added b_q (pretty-v2.1.32.js:534374-534782)
+ function b_q(A) {
+   let q = A1(89),
+     { toolUseConfirm: K, onDone: Y, onReject: z } = A,
+     w = ikA.safeParse(K.input),
+     H = w.success ? w.data.questions || [] : [],
+     O = w.success ? w.data.metadata?.source : void 0,
+     $;
+   if (q[0] === Symbol.for("react.memo_cache_sentinel")) (($ = {}), (q[0] = $));
+   else $ = q[0];
+   let [_, J] = VN6.useState($),
+     X = VN6.useRef(0),
+     D;
+   if (q[1] === Symbol.for("react.memo_cache_sentinel"))
+     ((D = function (_1, O1, N1, L1, I1, X1) {
+       X.current = X.current + 1;
+       let S1 = X.current,
+         v1 = {
+           id: S1,
+           type: "image",
+           content: O1,
+           mediaType: N1 || "image/png",
+           filename: L1 || "Pasted image",
+           dimensions: I1,
+         };
+       (J01(v1),
+         setTimeout(() => i41(v1), 0),
+         J((U1) => ({ ...U1, [_1]: { ...(U1[_1] ?? {}), [S1]: v1 } })));
+     }),
+       (q[1] = D));
+   else D = q[1];
+   let j = D,
+     M;
+   if (q[2] === Symbol.for("react.memo_cache_sentinel"))
+     ((M = (o, _1) => {
+       J((O1) => {
+         let N1 = { ...(O1[o] ?? {}) };
+         return (delete N1[_1], { ...O1, [o]: N1 });
+       });
+     }),
+       (q[2] = M));
+   else M = q[2];
+   let W = M,
+     G;
+   if (q[3] !== _)
+     ((G = Object.values(_).flatMap(xzz).filter(Izz)), (q[3] = _), (q[4] = G));
+   else G = q[4];
+   let P = G,
+     Z = T6(hzz) === "plan",
+     N;
+   if (q[5] !== Z) ((N = Z ? qZ() : void 0), (q[5] = Z), (q[6] = N));
+   else N = q[6];
+   let T = N,
+     k = y_q(),
+     {
+       currentQuestionIndex: y,
+       answers: u,
+       questionStates: S,
+       isInTextInput: m,
+       nextQuestion: b,
+       prevQuestion: U,
+       updateQuestionState: g,
+       setAnswer: x,
+       setTextInputMode: p,
+     } = k,
+     n = y < (H?.length || 0) ? H?.[y] : null,
+     r = y === (H?.length || 0),
+     z1 = H?.every((o) => o?.question && !!u[o.question]) ?? !1,
+     f1 = H.length === 1 && !H[0]?.multiSelect,
+     Z1;
+   if (
+     q[7] !== Z ||
+     q[8] !== O ||
+     q[9] !== Y ||
+     q[10] !== z ||
+     q[11] !== H.length ||
+     q[12] !== K
+   )
+     ((Z1 = () => {
+       if (O)
+         c("tengu_ask_user_question_rejected", {
+           source: O,
+           questionCount: H.length,
+           isInPlanMode: Z,
+           interviewPhaseEnabled: Z && b0(),
+         });
+       (Y(), z(), K.onReject());
+     }),
+       (q[7] = Z),
+       (q[8] = O),
+       (q[9] = Y),
+       (q[10] = z),
+       (q[11] = H.length),
+       (q[12] = K),
+       (q[13] = Z1));
+   else Z1 = q[13];
+   let H1 = Z1,
+     D1;
+   if (
+     q[14] !== P ||
+     q[15] !== u ||
+     q[16] !== Z ||
+     q[17] !== O ||
+     q[18] !== Y ||
+     q[19] !== H ||
+     q[20] !== K
+   )
+     ((D1 = async () => {
+       let _1 = `The user wants to clarify these questions.
+     This means they may have additional information, context or questions for you.
+     Take their response into account and then reformulate the questions if appropriate.
+     Start by asking them what they would like to clarify.
+ 
+     Questions asked:
+ ${H.map((N1) => {
+   let L1 = u[N1.question];
+   if (L1)
+     return `- "${N1.question}"
+   Answer: ${L1}`;
+   return `- "${N1.question}"
+   (No answer provided)`;
+ }).join(`
+ `)}`;
+       if (O)
+         c("tengu_ask_user_question_respond_to_claude", {
+           source: O,
+           questionCount: H.length,
+           isInPlanMode: Z,
+           interviewPhaseEnabled: Z && b0(),
+         });
+       let O1 = await uBA(P);
+       (Y(), K.onReject(_1, O1 && O1.length > 0 ? O1 : void 0));
+     }),
+       (q[14] = P),
+       (q[15] = u),
+       (q[16] = Z),
+       (q[17] = O),
+       (q[18] = Y),
+       (q[19] = H),
+       (q[20] = K),
+       (q[21] = D1));
+   else D1 = q[21];
+   let t = D1,
+     e;
+   if (
+     q[22] !== P ||
+     q[23] !== u ||
+     q[24] !== Z ||
+     q[25] !== O ||
+     q[26] !== Y ||
+     q[27] !== H ||
+     q[28] !== K
+   )
+     ((e = async () => {
+       let _1 = `The user has indicated they have provided enough answers for the plan interview.
+ Stop asking clarifying questions and proceed to finish the plan with the information you have.
+ 
+ Questions asked and answers provided:
+ ${H.map((N1) => {
+   let L1 = u[N1.question];
+   if (L1)
+     return `- "${N1.question}"
+   Answer: ${L1}`;
+   return `- "${N1.question}"
+   (No answer provided)`;
+ }).join(`
+ `)}`;
+       if (O)
+         c("tengu_ask_user_question_finish_plan_interview", {
+           source: O,
+           questionCount: H.length,
+           isInPlanMode: Z,
+           interviewPhaseEnabled: Z && b0(),
+         });
+       let O1 = await uBA(P);
+       (Y(), K.onReject(_1, O1 && O1.length > 0 ? O1 : void 0));
+     }),
+       (q[22] = P),
+       (q[23] = u),
+       (q[24] = Z),
+       (q[25] = O),
+       (q[26] = Y),
+       (q[27] = H),
+       (q[28] = K),
+       (q[29] = e));
+   else e = q[29];
+   let G1 = e,
+     w1;
+   if (
+     q[30] !== P ||
+     q[31] !== Z ||
+     q[32] !== O ||
+     q[33] !== Y ||
+     q[34] !== H.length ||
+     q[35] !== K
+   )
+     ((w1 = async (o) => {
+       if (O)
+         c("tengu_ask_user_question_accepted", {
+           source: O,
+           questionCount: H.length,
+           answerCount: Object.keys(o).length,
+           isInPlanMode: Z,
+           interviewPhaseEnabled: Z && b0(),
+         });
+       let _1 = { ...K.input, answers: o },
+         O1 = await uBA(P);
+       (Y(), K.onAllow(_1, [], void 0, O1 && O1.length > 0 ? O1 : void 0));
+     }),
+       (q[30] = P),
+       (q[31] = Z),
+       (q[32] = O),
+       (q[33] = Y),
+       (q[34] = H.length),
+       (q[35] = K),
+       (q[36] = w1));
+   else w1 = q[36];
+   let V1 = w1,
+     E1;
+   if (
+     q[37] !== u ||
+     q[38] !== _ ||
+     q[39] !== H.length ||
+     q[40] !== x ||
+     q[41] !== V1
+   )
+     ((E1 = (o, _1, O1, N1) => {
+       let L1 = N1 === void 0 ? !0 : N1,
+         I1,
+         X1 = Array.isArray(_1);
+       if (X1) I1 = _1.join(", ");
+       else if (O1)
+         I1 =
+           Object.values(_[o] ?? {}).filter(Szz).length > 0
+             ? `${O1} (Image attached)`
+             : O1;
+       else if (_1 === "__other__")
+         I1 =
+           Object.values(_[o] ?? {}).filter(Czz).length > 0
+             ? "(Image attached)"
+             : _1;
+       else I1 = _1;
+       let S1 = H.length === 1;
+       if (!X1 && S1 && L1) {
+         let v1 = { ...u, [o]: I1 };
+         V1(v1).catch(K1);
+         return;
+       }
+       x(o, I1, L1);
+     }),
+       (q[37] = u),
+       (q[38] = _),
+       (q[39] = H.length),
+       (q[40] = x),
+       (q[41] = V1),
+       (q[42] = E1));
+   else E1 = q[42];
+   let q1 = E1,
+     s;
+   if (q[43] !== u || q[44] !== H1 || q[45] !== V1)
+     ((s = function (_1) {
+       if (_1 === "cancel") {
+         H1();
+         return;
+       }
+       if (_1 === "submit") V1(u).catch(K1);
+     }),
+       (q[43] = u),
+       (q[44] = H1),
+       (q[45] = V1),
+       (q[46] = s));
+   else s = q[46];
+   let j1 = s,
+     J1;
+   if (
+     q[47] !== y ||
+     q[48] !== f1 ||
+     q[49] !== r ||
+     q[50] !== m ||
+     q[51] !== b ||
+     q[52] !== U ||
+     q[53] !== H.length
+   )
+     ((J1 = (o, _1) => {
+       if (m && !r) return;
+       if ((_1.leftArrow || (_1.shift && _1.tab)) && y > 0) U();
+       let O1 = f1 ? (H?.length || 1) - 1 : H?.length || 0;
+       if ((_1.rightArrow || (_1.tab && !_1.shift)) && y < O1) b();
+     }),
+       (q[47] = y),
+       (q[48] = f1),
+       (q[49] = r),
+       (q[50] = m),
+       (q[51] = b),
+       (q[52] = U),
+       (q[53] = H.length),
+       (q[54] = J1));
+   else J1 = q[54];
+   if ((Y8(J1), n)) {
+     let o;
+     if (q[55] !== n.question || q[56] !== j)
+       ((o = (L1, I1, X1, S1, v1) => j(n.question, L1, I1, X1, S1, v1)),
+         (q[55] = n.question),
+         (q[56] = j),
+         (q[57] = o));
+     else o = q[57];
+     let _1;
+     if (q[58] !== n.question || q[59] !== _)
+       ((_1 = _[n.question] ?? {}),
+         (q[58] = n.question),
+         (q[59] = _),
+         (q[60] = _1));
+     else _1 = q[60];
+     let O1;
+     if (q[61] !== n.question || q[62] !== W)
+       ((O1 = (L1) => W(n.question, L1)),
+         (q[61] = n.question),
+         (q[62] = W),
+         (q[63] = O1));
+     else O1 = q[63];
+     let N1;
+     if (
+       q[64] !== u ||
+       q[65] !== n ||
+       q[66] !== y ||
+       q[67] !== H1 ||
+       q[68] !== G1 ||
+       q[69] !== q1 ||
+       q[70] !== t ||
+       q[71] !== f1 ||
+       q[72] !== b ||
+       q[73] !== T ||
+       q[74] !== S ||
+       q[75] !== H ||
+       q[76] !== p ||
+       q[77] !== o ||
+       q[78] !== _1 ||
+       q[79] !== O1 ||
+       q[80] !== g
+     )
+       ((N1 = BBA.default.createElement(S_q, {
+         question: n,
+         questions: H,
+         currentQuestionIndex: y,
+         answers: u,
+         questionStates: S,
+         hideSubmitTab: f1,
+         planFilePath: T,
+         onUpdateQuestionState: g,
+         onAnswer: q1,
+         onTextInputFocus: p,
+         onCancel: H1,
+         onSubmit: b,
+         onRespondToClaude: t,
+         onFinishPlanInterview: G1,
+         onImagePaste: o,
+         pastedContents: _1,
+         onRemoveImage: O1,
+       })),
+         (q[64] = u),
+         (q[65] = n),
+         (q[66] = y),
+         (q[67] = H1),
+         (q[68] = G1),
+         (q[69] = q1),
+         (q[70] = t),
+         (q[71] = f1),
+         (q[72] = b),
+         (q[73] = T),
+         (q[74] = S),
+         (q[75] = H),
+         (q[76] = p),
+         (q[77] = o),
+         (q[78] = _1),
+         (q[79] = O1),
+         (q[80] = g),
+         (q[81] = N1));
+     else N1 = q[81];
+     return N1;
+   }
+   if (r) {
+     let o;
+     if (
+       q[82] !== z1 ||
+       q[83] !== u ||
+       q[84] !== y ||
+       q[85] !== j1 ||
+       q[86] !== H ||
+       q[87] !== K.permissionResult
+     )
+       ((o = BBA.default.createElement(I_q, {
+         questions: H,
+         currentQuestionIndex: y,
+         answers: u,
+         allQuestionsAnswered: z1,
+         permissionResult: K.permissionResult,
+         onFinalResponse: j1,
+       })),
+         (q[82] = z1),
+         (q[83] = u),
+         (q[84] = y),
+         (q[85] = j1),
+         (q[86] = H),
+         (q[87] = K.permissionResult),
+         (q[88] = o));
+     else o = q[88];
+     return o;
+   }
+   return null;
+ }

+++ Added Czz (pretty-v2.1.32.js:534783-534785)
+ function Czz(A) {
+   return A.type === "image";
+ }

+++ Added Szz (pretty-v2.1.32.js:534786-534788)
+ function Szz(A) {
+   return A.type === "image";
+ }

+++ Added Izz (pretty-v2.1.32.js:534792-534794)
+ function Izz(A) {
+   return A.type === "image";
+ }

+++ Added uBA (pretty-v2.1.32.js:534798-534813)
+ async function uBA(A) {
+   if (A.length === 0) return;
+   return Promise.all(
+     A.map(async (q) => {
+       let K = {
+         type: "image",
+         source: {
+           type: "base64",
+           media_type: q.mediaType || "image/png",
+           data: q.content,
+         },
+       };
+       return (await B41(K)).block;
+     }),
+   );
+ }

+++ Added E91 (pretty-v2.1.32.js:536935-536935)
+   E91 = null,

+++ Added aBA (pretty-v2.1.32.js:537283-537283)
+ var aBA = null,

+++ Added xN6 (pretty-v2.1.32.js:538142-538142)
+   xN6 = null;

+++ Added XXq (pretty-v2.1.32.js:539185-539187)
+ function XXq(A, q) {
+   return { nextMode: EZ1(A, q), context: A };
+ }

+++ Added LZ1 (pretty-v2.1.32.js:539252-539260)
+ function LZ1(A, q) {
+   if (!q) return !1;
+   let K = !1;
+   for (let Y of Object.values(A)) {
+     if (!Bh(Y) || (h9() && Y.type === "local_agent")) continue;
+     if (((K = !0), Y.type !== "in_process_teammate")) return !1;
+   }
+   return K;
+ }

+++ Added LXq (pretty-v2.1.32.js:540445-540445)
+   LXq = null,

+++ Added fwz (pretty-v2.1.32.js:540680-540682)
+ function fwz(A) {
+   return A.type === "local_agent";
+ }

+++ Added Nwz (pretty-v2.1.32.js:540686-540791)
+ function Nwz(A) {
+   let q = A1(30),
+     { task: K, isSelected: Y } = A,
+     { columns: z } = z8(),
+     w = !kZ1(K.status),
+     H = w ? Date.now() - K.startTime : (K.endTime ?? K.startTime) - K.startTime,
+     O;
+   if (q[0] !== H) ((O = nz(H)), (q[0] = H), (q[1] = O));
+   else O = q[1];
+   let $ = O,
+     _ = K.progress?.tokenCount,
+     J = K.progress?.lastActivity,
+     X = J ? n1.arrowDown : n1.arrowUp,
+     D;
+   if (q[2] !== X || q[3] !== _)
+     ((D = _ !== void 0 && _ > 0 ? ` · ${X} ${gK(_)} tokens` : ""),
+       (q[2] = X),
+       (q[3] = _),
+       (q[4] = D));
+   else D = q[4];
+   let j = D,
+     M = K.progress?.summary,
+     W = M || K.description,
+     G,
+     P;
+   if (q[5] !== M || q[6] !== K.id)
+     ((G = () => {
+       h(
+         `[CoordinatorAgentStatus] Summary updated for task ${K.id}: ${M ?? "(none)"}`,
+       );
+     }),
+       (P = [M, K.id]),
+       (q[5] = M),
+       (q[6] = K.id),
+       (q[7] = G),
+       (q[8] = P));
+   else ((G = q[7]), (P = q[8]));
+   xX.useEffect(G, P);
+   let V;
+   if (q[9] !== J?.activityDescription || q[10] !== M || q[11] !== K.progress)
+     ((V = M
+       ? void 0
+       : ((K.progress?.recentActivities && OB(K.progress.recentActivities)) ??
+         J?.activityDescription)),
+       (q[9] = J?.activityDescription),
+       (q[10] = M),
+       (q[11] = K.progress),
+       (q[12] = V));
+   else V = q[12];
+   let Z = V,
+     N = Z ? ` · ${Z}` : "",
+     T = Y ? n1.pointer + " " : "  ",
+     k = ` · ${$}${j}${N}`,
+     y = z - O7(T) - O7(k),
+     u = Math.max(0, y),
+     S;
+   if (q[13] !== W || q[14] !== u)
+     ((S = uT(W, u, "truncate-end")), (q[13] = W), (q[14] = u), (q[15] = S));
+   else S = q[15];
+   let m = S;
+   if (!w) {
+     let g = !Y,
+       x;
+     if (q[16] === Symbol.for("react.memo_cache_sentinel"))
+       ((x = xX.createElement(
+         f,
+         { color: "warning" },
+         " · ",
+         n1.cross,
+         " Stopped",
+       )),
+         (q[16] = x));
+     else x = q[16];
+     let p;
+     if (q[17] !== $ || q[18] !== T || q[19] !== g || q[20] !== j || q[21] !== m)
+       ((p = xX.createElement(f, { dimColor: g }, T, m, " · ", $, j, x)),
+         (q[17] = $),
+         (q[18] = T),
+         (q[19] = g),
+         (q[20] = j),
+         (q[21] = m),
+         (q[22] = p));
+     else p = q[22];
+     return p;
+   }
+   let b = !Y,
+     U;
+   if (
+     q[23] !== N ||
+     q[24] !== $ ||
+     q[25] !== T ||
+     q[26] !== b ||
+     q[27] !== j ||
+     q[28] !== m
+   )
+     ((U = xX.createElement(f, { dimColor: b }, T, m, " · ", $, j, N)),
+       (q[23] = N),
+       (q[24] = $),
+       (q[25] = T),
+       (q[26] = b),
+       (q[27] = j),
+       (q[28] = m),
+       (q[29] = U));
+   else U = q[29];
+   return U;
+ }

+++ Added twz (pretty-v2.1.32.js:543102-543102)
+   twz = null,

+++ Added XHz (pretty-v2.1.32.js:543508-543510)
+ function XHz(A) {
+   return A.type === "image";
+ }

+++ Added aN6 (pretty-v2.1.32.js:545685-545716)
+ function aN6(A, q) {
+   return {
+     type: "assistant",
+     uuid: yHz(),
+     message: {
+       id: `remote-${q}`,
+       type: "message",
+       role: "assistant",
+       content: [
+         {
+           type: "tool_use",
+           id: A.tool_use_id,
+           name: A.tool_name,
+           input: A.input,
+         },
+       ],
+       model: "",
+       stop_reason: null,
+       stop_sequence: null,
+       container: null,
+       context_management: null,
+       usage: {
+         input_tokens: 0,
+         output_tokens: 0,
+         cache_creation_input_tokens: 0,
+         cache_read_input_tokens: 0,
+       },
+     },
+     requestId: void 0,
+     timestamp: new Date().toISOString(),
+   };
+ }

+++ Added sN6 (pretty-v2.1.32.js:545717-545740)
+ function sN6(A) {
+   return {
+     name: A,
+     inputSchema: {},
+     isEnabled: () => !0,
+     userFacingName: () => A,
+     renderToolUseMessage: (q) => {
+       let K = Object.entries(q);
+       if (K.length === 0) return "";
+       return K.slice(0, 3)
+         .map(([Y, z]) => {
+           let w = typeof z === "string" ? z : g1(z);
+           return `${Y}: ${w}`;
+         })
+         .join(", ");
+     },
+     call: async () => ({ data: "" }),
+     description: async () => "",
+     prompt: () => "",
+     isReadOnly: () => !1,
+     isMcp: !1,
+     needsPermissions: () => !0,
+   };
+ }

+++ Added t0q (pretty-v2.1.32.js:545744-545904)
+ function t0q({
+   config: A,
+   setMessages: q,
+   setIsLoading: K,
+   onInit: Y,
+   setToolUseConfirmQueue: z,
+   tools: w,
+   setStreamingToolUses: H,
+   setStreamMode: O,
+   setInProgressToolUseIDs: $,
+ }) {
+   let _ = !!A,
+     J = LI.useRef(null),
+     X = LI.useRef(null),
+     D = LI.useRef(w);
+   (LI.useEffect(() => {
+     D.current = w;
+   }, [w]),
+     LI.useEffect(() => {
+       if (!A) return;
+       h(`[useRemoteSession] Initializing for session ${A.sessionId}`);
+       let G = new NmA(A, {
+         onMessage: (P) => {
+           if (
+             (h(`[useRemoteSession] Received message type: ${P.type}`),
+             J.current)
+           )
+             (clearTimeout(J.current), (J.current = null));
+           if (P.type === "system" && P.subtype === "init" && Y)
+             (h(
+               `[useRemoteSession] Init received with ${P.slash_commands.length} slash commands`,
+             ),
+               Y(P.slash_commands));
+           if (oN6(P)) K(!1);
+           let V = rN6(P);
+           if (V.type === "message") {
+             if (
+               (H?.((Z) => (Z.length > 0 ? [] : Z)),
+               $ && V.message.type === "assistant")
+             ) {
+               let Z = V.message.message.content
+                 .filter((N) => N.type === "tool_use")
+                 .map((N) => N.id);
+               if (Z.length > 0)
+                 $((N) => {
+                   let T = new Set(N);
+                   for (let k of Z) T.add(k);
+                   return T;
+                 });
+             }
+             q((Z) => [...Z, V.message]);
+           } else if (V.type === "stream_event")
+             if (H && O)
+               xG1(
+                 V.event,
+                 (Z) => q((N) => [...N, Z]),
+                 () => {},
+                 O,
+                 H,
+               );
+             else
+               h(
+                 "[useRemoteSession] Stream event received but streaming callbacks not provided",
+               );
+         },
+         onPermissionRequest: (P, V) => {
+           h(`[useRemoteSession] Permission request for tool: ${P.tool_name}`);
+           let Z = oT(D.current, P.tool_name) ?? sN6(P.tool_name),
+             N = aN6(P, V),
+             T = {
+               behavior: "ask",
+               message: P.description ?? `${P.tool_name} requires permission`,
+               suggestions: P.permission_suggestions,
+               blockedPath: P.blocked_path,
+             },
+             k = {
+               assistantMessage: N,
+               tool: Z,
+               description:
+                 P.description ?? `${P.tool_name} requires permission`,
+               input: P.input,
+               toolUseContext: {},
+               toolUseID: P.tool_use_id,
+               permissionResult: T,
+               permissionPromptStartTimeMs: Date.now(),
+               onUserInteraction() {},
+               onAbort() {
+                 let y = { behavior: "deny", message: "User aborted" };
+                 (G.respondToPermissionRequest(V, y),
+                   z((u) => u.filter((S) => S.toolUseID !== P.tool_use_id)));
+               },
+               onAllow(y, u, S) {
+                 let m = { behavior: "allow", updatedInput: y };
+                 (G.respondToPermissionRequest(V, m),
+                   z((b) => b.filter((U) => U.toolUseID !== P.tool_use_id)),
+                   K(!0));
+               },
+               onReject(y) {
+                 let u = {
+                   behavior: "deny",
+                   message: y ?? "User denied permission",
+                 };
+                 (G.respondToPermissionRequest(V, u),
+                   z((S) => S.filter((m) => m.toolUseID !== P.tool_use_id)));
+               },
+               async recheckPermission() {},
+             };
+           (z((y) => [...y, k]), K(!1));
+         },
+         onConnected: () => {
+           h("[useRemoteSession] Connected");
+         },
+         onDisconnected: () => {
+           (h("[useRemoteSession] Disconnected"), K(!1));
+         },
+         onError: (P) => {
+           h(`[useRemoteSession] Error: ${P.message}`);
+         },
+       });
+       return (
+         (X.current = G),
+         G.connect(),
+         () => {
+           if ((h("[useRemoteSession] Cleanup - disconnecting"), J.current))
+             (clearTimeout(J.current), (J.current = null));
+           (G.disconnect(), (X.current = null));
+         }
+       );
+     }, [A, q, K, Y, z, H, O, $]));
+   let j = LI.useCallback(
+       async (G) => {
+         let P = X.current;
+         if (!P) return (h("[useRemoteSession] Cannot send - no manager"), !1);
+         if (J.current) clearTimeout(J.current);
+         K(!0);
+         let V = await P.sendMessage(G);
+         if (!V) return (K(!1), !1);
+         return (
+           (J.current = setTimeout(() => {
+             h("[useRemoteSession] Response timeout - attempting reconnect");
+             let Z = eD(
+               "Remote session may be unresponsive. Attempting to reconnect…",
+               "warning",
+             );
+             (q((N) => [...N, Z]), P.reconnect());
+           }, CHz)),
+           V
+         );
+       },
+       [K, q],
+     ),
+     M = LI.useCallback(() => {
+       if (J.current) (clearTimeout(J.current), (J.current = null));
+       (X.current?.cancelSession(), K(!1));
+     }, [K]),
+     W = LI.useCallback(() => {
+       if (J.current) (clearTimeout(J.current), (J.current = null));
+       (X.current?.disconnect(), (X.current = null));
+     }, []);
+   return { isRemoteMode: _, sendMessage: j, cancelRequest: M, disconnect: W };
+ }

+++ Added qDq (pretty-v2.1.32.js:546024-546139)
+ function qDq({
+   config: A,
+   setMessages: q,
+   setIsLoading: K,
+   setToolUseConfirmQueue: Y,
+   tools: z,
+ }) {
+   let w = !!A,
+     H = nR.useRef(null),
+     O = nR.useRef(!1),
+     $ = nR.useRef(!1),
+     _ = nR.useRef(z);
+   (nR.useEffect(() => {
+     _.current = z;
+   }, [z]),
+     nR.useEffect(() => {
+       if (!A) return;
+       ((O.current = !1), h(`[useDirectConnect] Connecting to ${A.wsUrl}`));
+       let j = new kmA(A, {
+         onMessage: (M) => {
+           if (oN6(M)) K(!1);
+           if (M.type === "system" && M.subtype === "init") {
+             if (O.current) return;
+             O.current = !0;
+           }
+           let W = rN6(M, { convertToolResults: !0 });
+           if (W.type === "message") q((G) => [...G, W.message]);
+         },
+         onPermissionRequest: (M, W) => {
+           h(`[useDirectConnect] Permission request for tool: ${M.tool_name}`);
+           let G = oT(_.current, M.tool_name) ?? sN6(M.tool_name),
+             P = aN6(M, W),
+             V = {
+               behavior: "ask",
+               message: M.description ?? `${M.tool_name} requires permission`,
+               suggestions: M.permission_suggestions,
+               blockedPath: M.blocked_path,
+             },
+             Z = {
+               assistantMessage: P,
+               tool: G,
+               description:
+                 M.description ?? `${M.tool_name} requires permission`,
+               input: M.input,
+               toolUseContext: {},
+               toolUseID: M.tool_use_id,
+               permissionResult: V,
+               permissionPromptStartTimeMs: Date.now(),
+               onUserInteraction() {},
+               onAbort() {
+                 let N = { behavior: "deny", message: "User aborted" };
+                 (j.respondToPermissionRequest(W, N),
+                   Y((T) => T.filter((k) => k.toolUseID !== M.tool_use_id)));
+               },
+               onAllow(N, T, k) {
+                 let y = { behavior: "allow", updatedInput: N };
+                 (j.respondToPermissionRequest(W, y),
+                   Y((u) => u.filter((S) => S.toolUseID !== M.tool_use_id)),
+                   K(!0));
+               },
+               onReject(N) {
+                 let T = {
+                   behavior: "deny",
+                   message: N ?? "User denied permission",
+                 };
+                 (j.respondToPermissionRequest(W, T),
+                   Y((k) => k.filter((y) => y.toolUseID !== M.tool_use_id)));
+               },
+               async recheckPermission() {},
+             };
+           (Y((N) => [...N, Z]), K(!1));
+         },
+         onConnected: () => {
+           (h("[useDirectConnect] Connected"), ($.current = !0));
+         },
+         onDisconnected: () => {
+           if ((h("[useDirectConnect] Disconnected"), !$.current))
+             process.stderr.write(`
+ Failed to connect to server at ${A.wsUrl}
+ `);
+           else
+             process.stderr.write(`
+ Server disconnected.
+ `);
+           (($.current = !1), $K(1), K(!1));
+         },
+         onError: (M) => {
+           h(`[useDirectConnect] Error: ${M.message}`);
+         },
+       });
+       return (
+         (H.current = j),
+         j.connect(),
+         () => {
+           (h("[useDirectConnect] Cleanup - disconnecting"),
+             j.disconnect(),
+             (H.current = null));
+         }
+       );
+     }, [A, q, K, Y]));
+   let J = nR.useCallback(
+       async (j) => {
+         let M = H.current;
+         if (!M) return !1;
+         return (K(!0), M.sendMessage(j));
+       },
+       [K],
+     ),
+     X = nR.useCallback(() => {
+       (H.current?.sendInterrupt(), K(!1));
+     }, [K]),
+     D = nR.useCallback(() => {
+       (H.current?.disconnect(), (H.current = null), ($.current = !1));
+     }, []);
+   return { isRemoteMode: w, sendMessage: J, cancelRequest: X, disconnect: D };
+ }

+++ Added ZDq (pretty-v2.1.32.js:546765-546773)
+ var ZDq = v(() => {
+   tU();
+   JO();
+   _6();
+   oz();
+   Zv();
+   V$();
+   I6();
+ });

+++ Added CDq (pretty-v2.1.32.js:547177-547189)
+ function CDq(A) {
+   return {
+     push(q) {
+       A((K) => [...K, q]);
+     },
+     remove(q) {
+       A((K) => K.filter((Y) => Y.toolUseID !== q));
+     },
+     update(q, K) {
+       A((Y) => Y.map((z) => (z.toolUseID === q ? { ...z, ...K } : z)));
+     },
+   };
+ }

+++ Added BDq (pretty-v2.1.32.js:547380-547388)
+ var BDq = v(() => {
+   F6();
+   IO();
+   MK1();
+   HJ();
+   Cp();
+   e81();
+   KT6();
+ });

+++ Added qFA (pretty-v2.1.32.js:551258-551261)
+ var qFA = v(() => {
+   AFA();
+   XE();
+ });

+++ Added cWq (pretty-v2.1.32.js:551746-551748)
+ var cWq = v(() => {
+   dWq();
+ });

+++ Added OVq (pretty-v2.1.32.js:554344-554351)
+ var OVq = v(() => {
+   d1();
+   K2();
+   pW();
+   Q8();
+   j3();
+   a$z = a($1(), 1);
+ });

+++ Added IT6 (pretty-v2.1.32.js:556250-556250)
+   IT6 = null;

+++ Added XFA (pretty-v2.1.32.js:556251-556403)
+ var XFA = v(() => {
+   d1();
+   u1();
+   j$q();
+   K2();
+   ZF1();
+   f$q();
+   O71();
+   _M();
+   a6();
+   _6();
+   Q7();
+   I6();
+   Zv();
+   gM1();
+   JO();
+   Lh();
+   Sm1();
+   oz();
+   T$q();
+   Lh();
+   Sa();
+   k$q();
+   XN6();
+   I$q();
+   m_q();
+   d_q();
+   i0q();
+   r0q();
+   e0q();
+   KDq();
+   YDq();
+   Ez();
+   rNA();
+   aV();
+   $P6();
+   qv();
+   vD();
+   jBA();
+   Ik();
+   LmA();
+   $Dq();
+   ZS();
+   JDq();
+   DDq();
+   jDq();
+   xB();
+   Lw();
+   WDq();
+   PDq();
+   EDq();
+   RDq();
+   gDq();
+   V$();
+   xBA();
+   obA();
+   FA();
+   F6();
+   J8();
+   W01();
+   Wz();
+   Kp();
+   $w();
+   aDq();
+   Ajq();
+   Kjq();
+   CG1();
+   o31();
+   wjq();
+   JvA();
+   YbA();
+   Ojq();
+   _jq();
+   mmA();
+   UP1();
+   Mm1();
+   XVA();
+   Xjq();
+   DVA();
+   CI1();
+   Ot();
+   jjq();
+   E0();
+   wK1();
+   VF1();
+   Q8();
+   zB();
+   xD();
+   Eq();
+   bG1();
+   EG6();
+   e31();
+   hp();
+   WZ();
+   n41();
+   Eq();
+   Vd1();
+   Pjq();
+   N9();
+   Zjq();
+   zO();
+   Njq();
+   fbA();
+   uV();
+   Ea();
+   fM();
+   Ejq();
+   r$6();
+   Ljq();
+   R31();
+   fg1();
+   wXA();
+   JVA();
+   P2();
+   ut();
+   hjq();
+   xjq();
+   Bjq();
+   Qjq();
+   Ujq();
+   cjq();
+   ijq();
+   sjq();
+   AMq();
+   jH();
+   KMq();
+   YMq();
+   zfq();
+   vhA();
+   Ofq();
+   _fq();
+   Vfq();
+   vfq();
+   Lfq();
+   yfq();
+   Sfq();
+   Rj6();
+   Ifq();
+   ufq();
+   mfq();
+   Qfq();
+   Ufq();
+   cfq();
+   nfq();
+   afq();
+   efq();
+   qVq();
+   HVq();
+   OVq();
+   XVq();
+   jVq();
+   ((N7 = a($1(), 1)), (lA = a($1(), 1)));
+ });

+++ Added GFA (pretty-v2.1.32.js:556996-557003)
+ var GFA = v(() => {
+   d1();
+   u1();
+   FA();
+   a5();
+   hq();
+   Dc = a($1(), 1);
+ });

+++ Added PFA (pretty-v2.1.32.js:557991-557996)
+ var PFA = v(() => {
+   d1();
+   u1();
+   Z5();
+   UA = a($1(), 1);
+ });

+++ Added sVq (pretty-v2.1.32.js:558977-559002)
+ var sVq = v(() => {
+   d1();
+   u1();
+   r8();
+   Ez();
+   XFA();
+   lf6();
+   k6();
+   J8();
+   Eq();
+   rf6();
+   b31();
+   bG1();
+   Wq();
+   _p();
+   ZxA();
+   a6();
+   Eq();
+   Ik();
+   pp1();
+   iD();
+   Q7();
+   Q8();
+   Vd1();
+   cY = a($1(), 1);
+ });

+++ Added fFA (pretty-v2.1.32.js:559293-559298)
+ var fFA = v(() => {
+   d1();
+   u1();
+   u1();
+   ZFA = a($1(), 1);
+ });

+++ Added _Nq (pretty-v2.1.32.js:559420-559433)
+ var _Nq = v(() => {
+   d1();
+   u1();
+   tZ6();
+   R8();
+   QO8();
+   fFA();
+   F6();
+   Tq();
+   LK();
+   Cq();
+   hq();
+   sR = a($1(), 1);
+ });

+++ Added XNq (pretty-v2.1.32.js:559511-559519)
+ var XNq = v(() => {
+   d1();
+   a5();
+   R8();
+   fFA();
+   F6();
+   hq();
+   gT6 = a($1(), 1);
+ });

+++ Added yNq (pretty-v2.1.32.js:559733-559736)
+ var yNq = v(() => {
+   F6();
+   W_();
+ });

+++ Added CNq (pretty-v2.1.32.js:559738-559741)
+ var CNq = v(() => {
+   I6();
+   l_z = a(l_6(), 1);
+ });

+++ Added xNq (pretty-v2.1.32.js:559971-559980)
+ var xNq = v(() => {
+   d1();
+   u1();
+   u1();
+   FA();
+   F6();
+   $91();
+   hq();
+   jj = a($1(), 1);
+ });

+++ Added pNq (pretty-v2.1.32.js:560203-560207)
+ var pNq = v(() => {
+   FA();
+   R8();
+   r2();
+ });

+++ Added cNq (pretty-v2.1.32.js:560219-560224)
+ var cNq = v(() => {
+   FA();
+   R8();
+   r2();
+   Q7();
+ });

+++ Added iNq (pretty-v2.1.32.js:560240-560245)
+ var iNq = v(() => {
+   FA();
+   R8();
+   r2();
+   Q7();
+ });

+++ Added rNq (pretty-v2.1.32.js:560255-560259)
+ var rNq = v(() => {
+   FA();
+   R8();
+   R8();
+ });

+++ Added oNq (pretty-v2.1.32.js:560260-560262)
+ var oNq = v(() => {
+   R8();
+ });

+++ Added aNq (pretty-v2.1.32.js:560826-560826)
+   aNq = 3,

+++ Added eNq (pretty-v2.1.32.js:560918-560922)
+ var eNq = v(() => {
+   yFA();
+   sNq();
+   BA();
+ });

+++ Added qTq (pretty-v2.1.32.js:560976-560981)
+ var qTq = v(() => {
+   MP();
+   bn();
+   oH();
+   OD();
+ });

+++ Added zTq (pretty-v2.1.32.js:561568-561602)
+ var zTq = v(() => {
+   w61();
+   pW();
+   W_();
+   Z7();
+   aV();
+   qv();
+   Ik();
+   o31();
+   _M();
+   kd();
+   Eq();
+   BA();
+   J8();
+   HB();
+   umA();
+   a6();
+   Q7();
+   N_6();
+   ak();
+   Wz();
+   D7();
+   $g1();
+   Lu1();
+   NH();
+   FA();
+   P2();
+   lB();
+   R8();
+   wJ();
+   k6();
+   WZ();
+   XN6();
+   EG6();
+ });

+++ Added wTq (pretty-v2.1.32.js:561603-561605)
+ var wTq = v(() => {
+   _6();
+ });

+++ Added $Tq (pretty-v2.1.32.js:561635-561638)
+ var $Tq = v(() => {
+   _6();
+   $w();
+ });

+++ Added XTq (pretty-v2.1.32.js:561670-561672)
+ var XTq = v(() => {
+   sS();
+ });

+++ Added TTq (pretty-v2.1.32.js:563694-563703)
+ var TTq = v(() => {
+   F6();
+   yp();
+   hR();
+   Nh();
+   _6();
+   $w();
+   Zs();
+   R8();
+ });

+++ Added ITq (pretty-v2.1.32.js:564176-564185)
+ var ITq = v(() => {
+   d1();
+   u1();
+   hq();
+   a5();
+   Ez();
+   i4();
+   IFA();
+   ((sM = a($1(), 1)), (cT6 = a($1(), 1)));
+ });

+++ Added UTq (pretty-v2.1.32.js:564671-564678)
+ var UTq = v(() => {
+   d1();
+   Zd();
+   wH();
+   F6();
+   a6();
+   lT6 = a($1(), 1);
+ });

+++ Added cTq (pretty-v2.1.32.js:564850-564862)
+ var cTq = v(() => {
+   d1();
+   u1();
+   QTq();
+   Ez();
+   UTq();
+   F6();
+   Q8();
+   xB();
+   _6();
+   IB();
+   ((IG = a($1(), 1)), (pTq = a($1(), 1)));
+ });

+++ Added iTq (pretty-v2.1.32.js:565010-565017)
+ var iTq = v(() => {
+   PZ();
+   RX();
+   BA();
+   I6();
+   F6();
+   V51();
+ });

+++ Added Avq (pretty-v2.1.32.js:565335-565335)
+ var Avq = {};

=== Structural Changes ===

@@@ function 'XmA' (was 'IBA') — structural (98.7%)
--- pretty-v2.1.31.js:539062
+++ pretty-v2.1.32.js:539268
@@ -149,7 +149,7 @@
     else X1 = q[40];
     return X1;
   }
-  if (P && W.every(HYz)) return null;
+  if (LZ1(D ?? {}, G)) return null;
   let m;
   if (q[41] !== Y || q[42] !== K)
     ((m =

@@@ variable '$H' (was 'qH') — structural (97.5%)
--- pretty-v2.1.31.js:90449
+++ pretty-v2.1.32.js:90328
@@ -230,7 +230,8 @@
       if (A.signer) O = Ql.normalizeProvider(A.signer);
       else if (A.regionInfoProvider)
         O = () =>
-          Ql.normalizeProvider(A.region)()
+          qi
+            .normalizeProvider(A.region)()
             .then(async (_) => [
               (await A.regionInfoProvider(_, {
                 useFipsEndpoint: await A.useFipsEndpoint(),

@@@ function 'j_' (was '$_') — structural (96.9%)
--- pretty-v2.1.31.js:516085
+++ pretty-v2.1.32.js:515759
@@ -82,6 +82,6 @@
     }
   }),
     h94(H));
-  let O = k7z(H);
+  let O = gqz(CQ1(H));
   return L7z(O);
 }

@@@ variable 'b2q' (was 'nYq') — structural (96.5%)
--- pretty-v2.1.31.js:509591
+++ pretty-v2.1.32.js:509207
@@ -14,6 +14,7 @@
   Vb();
   hn();
   Aq();
+  Wq();
   (($8 = o(J1(), 1)), (kZ = o(J1(), 1)), (pYq = o(ZYq(), 1)));
   ((QYq = { "7d": "Last 7 days", "30d": "Last 30 days", all: "All time" }),
     (MV6 = ["all", "7d", "30d"]));

@@@ function 'qXz' (was 'b$z') — structural (96.3%)
--- pretty-v2.1.31.js:565654
+++ pretty-v2.1.32.js:565803
@@ -14,6 +14,7 @@
     K = A.includes("--init-only"),
     Y = A.some((O) => O.startsWith("--sdk-url")),
     z = q || K || Y || !process.stdout.isTTY;
+  if (z) Y71();
   (fE6(!z), x$z(z));
   let H = (() => {
     if (process.env.GITHUB_ACTIONS === "true") return "github-action";

@@@ variable 'W_' (was 'j_') — structural (96.3%)
--- pretty-v2.1.31.js:511780
+++ pretty-v2.1.32.js:511404
@@ -94,6 +94,7 @@
   eYq();
   Azq();
   MO();
+  EO();
   ((MbA = YA(() => [
     Vt4,
     l5q,

@@@ function 'r3q' (was 'NKq') — structural (95.7%)
--- pretty-v2.1.31.js:490758
+++ pretty-v2.1.32.js:490421
@@ -91,12 +91,19 @@
       K.status !== "running" &&
       gY.default.createElement(
         Z,
-        { color: K.status === "completed" ? "success" : "error" },
+        {
+          color:
+            K.status === "completed"
+              ? "success"
+              : K.status === "killed"
+                ? "warning"
+                : "error",
+        },
         K.status === "completed"
           ? "Completed"
           : K.status === "failed"
             ? "Failed"
-            : "Killed",
+            : "Stopped",
         " · ",
       )),
       (q[25] = K.status),

@@@ class 'aK' (was 'tK') — structural (95.4%)
--- pretty-v2.1.31.js:192451
+++ pretty-v2.1.32.js:248948
@@ -20,7 +20,7 @@
       }
       if (z !== O) return _.trimEnd();
       let J = this.measuredText.displayWidthToStringIndex(_, w),
-        X = Array.from(aqA.segment(_)).map(({ segment: G, index: f }) => ({
+        X = Array.from(MC().segment(_)).map(({ segment: P, index: V }) => ({
           segment: G,
           index: f,
         })),

@@@ class 'iwq' (was 'z2q') — structural (95.0%)
--- pretty-v2.1.31.js:517695
+++ pretty-v2.1.32.js:517418
@@ -200,6 +200,7 @@
     else if (A.type === "tag") this.enqueueWrite(w, A);
     else if (A.type === "agent-name") this.enqueueWrite(w, A);
     else if (A.type === "agent-color") this.enqueueWrite(w, A);
+    else if (A.type === "agent-setting") this.enqueueWrite(w, A);
     else if (A.type === "pr-link") this.enqueueWrite(w, A);
     else if (A.type === "file-history-snapshot") this.enqueueWrite(w, A);
     else if (A.type === "attribution-snapshot") this.enqueueWrite(w, A);

@@@ variable 'Xc6' (was 'gd6') — structural (94.6%)
--- pretty-v2.1.31.js:105334
+++ pretty-v2.1.32.js:105214
@@ -14,7 +14,10 @@
             K?.debug(
               "@aws-sdk/credential-provider-ini - credential_source is EcsContainer",
             ),
-            async () => Qv1.chain(w(z ?? {}), H(z))().then(Fd6)
+            async () =>
+              ev1
+                .chain(w(z ?? {}), H(z))()
+                .then(_c6)
           );
         },
         Ec2InstanceMetadata: async (z) => {

@@@ variable 'VoA' (was 'drA') — structural (94.4%)
--- pretty-v2.1.31.js:15479
+++ pretty-v2.1.32.js:15495
@@ -47,9 +47,7 @@
             O = (q1, H1, $1) => {
               c(q1, H1, (A1, O1, s) => {
                 if (A1) return $1(A1);
-                let w1 = U6.isArray(O1)
-                  ? O1.map((Z1) => FrA(Z1))
-                  : [FrA(O1, s)];
+                let e = c6.isArray(D1) ? D1.map((G1) => WoA(G1)) : [WoA(D1, t)];
                 H1.all ? $1(A1, w1) : $1(A1, w1[0].address, w1[0].family);
               });
             };

@@@ variable 'u6q' (was 'v1q') — structural (94.3%)
--- pretty-v2.1.31.js:462922
+++ pretty-v2.1.32.js:462919
@@ -7,6 +7,7 @@
   rz();
   s6();
   MO();
+  j3();
   ((dSA = o(J1(), 1)),
     (N1q = {
       name: "context",

@@@ function 'pm1' (was 'vm1') — structural (94.0%)
--- pretty-v2.1.31.js:513927
+++ pretty-v2.1.32.js:513604
@@ -22,7 +22,7 @@
         .replaceAll("\\)", K.ESCAPED_CLOSE_PAREN),
       ($) => `$${$}`,
     );
-  if (!H.success) throw Error(`Failed to parse command: ${H.error}`);
+  if (!H.success) return YuA([A], z);
   let O = H.tokens;
   if (O.length === 0) return [];
   try {

@@@ variable 'AG1' (was 'dW1') — structural (93.3%)
--- pretty-v2.1.31.js:416079
+++ pretty-v2.1.32.js:415718
@@ -13,12 +13,12 @@
       bytes: b.number().describe("Size of the fetched content in bytes"),
       code: b.number().describe("HTTP response code"),
       codeText: b.string().describe("HTTP response code text"),
-      result: b
-        .string()
-        .describe("Processed result from applying the prompt to the content"),
-      durationMs: b
-        .number()
-        .describe("Time taken to fetch and process the content"),
+      result: B.string().describe(
+        "Processed result from applying the prompt to the content",
+      ),
+      durationMs: B.number().describe(
+        "Time taken to fetch and process the content",
+      ),
       url: b.string().describe("The URL that was fetched"),
     })));
   sD = {

@@@ function 'nz' (was 'E2') — structural (93.2%)
--- pretty-v2.1.31.js:146631
+++ pretty-v2.1.32.js:146552
@@ -12,6 +12,12 @@
   if (z === 60) ((z = 0), Y++);
   if (Y === 24) ((Y = 0), K++);
   let H = q?.hideTrailingZeros;
+  if (q?.mostSignificantOnly) {
+    if (K > 0) return `${K}d`;
+    if (Y > 0) return `${Y}h`;
+    if (z > 0) return `${z}m`;
+    return `${w}s`;
+  }
   if (K > 0) {
     if (H && Y === 0 && z === 0) return `${K}d`;
     if (H && z === 0) return `${K}d ${Y}h`;

@@@ variable 'lW7' (was 'YW7') — structural (93.2%)
--- pretty-v2.1.31.js:186728
+++ pretty-v2.1.32.js:186921
@@ -131,7 +131,8 @@
       if ((q.setEncoding("utf8"), A)) {
         if (this.rawModeEnabledCount === 0) {
           if (
-            (q.ref(),
+            (Y71(),
+            q.ref(),
             q.setRawMode(!0),
             q.addListener("readable", this.handleReadable),
             this.props.stdout.write(qW7),

@@@ class 'kmA' (was 'iBA') — structural (93.2%)
--- pretty-v2.1.31.js:545668
+++ pretty-v2.1.32.js:545923
@@ -80,6 +80,15 @@
     });
     this.ws.send(K);
   }
+  sendInterrupt() {
+    if (!this.ws || this.ws.readyState !== WebSocket.OPEN) return;
+    let A = g1({
+      type: "control_request",
+      request_id: crypto.randomUUID(),
+      request: { subtype: "interrupt" },
+    });
+    this.ws.send(A);
+  }
   disconnect() {
     if (this.ws) (this.ws.close(), (this.ws = null));
   }

@@@ class 'NmA' (was 'dBA') — structural (93.1%)
--- pretty-v2.1.31.js:545282
+++ pretty-v2.1.32.js:545427
@@ -91,6 +91,10 @@
   isConnected() {
     return this.websocket?.isConnected() ?? !1;
   }
+  cancelSession() {
+    (h("[RemoteSessionManager] Sending interrupt signal"),
+      this.websocket?.sendControlRequest({ subtype: "interrupt" }));
+  }
   getSessionId() {
     return this.config.sessionId;
   }

@@@ variable 'jH' (was 'mH') — structural (92.8%)
--- pretty-v2.1.31.js:168573
+++ pretty-v2.1.32.js:168681
@@ -10,6 +10,7 @@
   BH();
   aI();
   nz();
+  az();
   ((V7A = YA(() => {
     let { rgPath: A, rgArgs: q } = E21();
     return W$.checkDependencies({ command: A, args: q });

@@@ class 'bl7' (was 'WZ7') — structural (92.8%)
--- pretty-v2.1.31.js:192872
+++ pretty-v2.1.32.js:249369
@@ -15,7 +15,7 @@
   getGraphemeBoundaries() {
     if (!this.graphemeBoundaries) {
       this.graphemeBoundaries = [];
-      for (let { index: A } of aqA.segment(this.text))
+      for (let { index: A } of MC().segment(this.text))
         this.graphemeBoundaries.push(A);
       this.graphemeBoundaries.push(this.text.length);
     }
@@ -25,7 +25,7 @@
   getWordBoundaries() {
     if (!this.wordBoundariesCache) {
       this.wordBoundariesCache = [];
-      for (let A of Kl5.segment(this.text))
+      for (let A of k27().segment(this.text))
         this.wordBoundariesCache.push({
           start: A.index,
           end: A.index + A.segment.length,
@@ -61,7 +61,7 @@
     if (A === this.text) return this.offsetAtDisplayWidth(q);
     let K = 0,
       Y = 0;
-    for (let { segment: z, index: w } of aqA.segment(A)) {
+    for (let { segment: z, index: w } of MC().segment(A)) {
       let H = j7(z);
       if (K + H > q) break;
       ((K += H), (Y = w + z.length));

@@@ function 'Aj7' (was 'jD7') — structural (92.7%)
--- pretty-v2.1.31.js:178294
+++ pretty-v2.1.32.js:178414
@@ -25,7 +25,7 @@
     return Y;
   }
   let K = 0;
-  for (let { segment: Y } of NF5.segment(A)) {
+  for (let { segment: Y } of MC().segment(A)) {
     if (((DD7.lastIndex = 0), DD7.test(Y))) {
       K += vF5(Y);
       continue;

@@@ function 'VJq' (was 'S$q') — structural (92.5%)
--- pretty-v2.1.31.js:536339
+++ pretty-v2.1.32.js:536524
@@ -161,9 +161,7 @@
   else s = q[25];
   let w1;
   if (q[26] !== W)
-    ((w1 = z5.createElement(W$q, { tokenUsage: W })),
-      (q[26] = W),
-      (q[27] = w1));
+    ((e = A5.createElement(wJq, { tokenUsage: W })), (q[26] = W), (q[27] = e));
   else w1 = q[27];
   let Z1;
   if (

@@@ variable 'WSA' (was 'cCA') — structural (92.0%)
--- pretty-v2.1.31.js:453653
+++ pretty-v2.1.32.js:453447
@@ -3,6 +3,7 @@
   u1();
   Aq();
   n_();
+  z_();
   ((Lv = o(J1(), 1)), (dCA = o(J1(), 1)));
   RQY = dCA.memo(function (q) {
     let K = t(25),

@@@ function 'PTq' (was 'xVq') — structural (91.8%)
--- pretty-v2.1.31.js:561585
+++ pretty-v2.1.32.js:561735
@@ -1,7 +1,7 @@
 async function xVq(A, q, K, Y, z, w, H, O) {
   if (
-    (lJ.subscribe(() => {
-      K$();
+    (dJ.subscribe((T) => {
+      AZ6(T, K);
     }),
     GRA(),
     await Gj1())
@@ -36,8 +36,6 @@
       $3(1));
     return;
   }
-  if (O.thinking === "disabled") O.maxThinkingTokens = 0;
-  else if (O.thinking === "adaptive") O.maxThinkingTokens = void 0;
   let $ = A$z(A, O);
   if (O.outputFormat === "stream-json" && O.verbose)
     $94((T) => {

@@@ class 'Dg1' (was 'pQ1') — structural (91.5%)
--- pretty-v2.1.31.js:431942
+++ pretty-v2.1.32.js:431696
@@ -42,7 +42,15 @@
       return;
     }
     let Y = K.inputSchema.safeParse(A.input),
-      z = Y?.success ? K.isConcurrencySafe(Y.data) : !1;
+      z = Y?.success
+        ? (() => {
+            try {
+              return Boolean(K.isConcurrencySafe(Y.data));
+            } catch {
+              return !1;
+            }
+          })()
+        : !1;
     (this.tools.push({
       id: A.id,
       block: A,
@@ -103,8 +111,11 @@
   getAbortReason() {
     if (this.discarded) return "streaming_fallback";
     if (this.hasErrored) return "sibling_error";
-    if (this.toolUseContext.abortController.signal.aborted)
+    if (this.toolUseContext.abortController.signal.aborted) {
+      if (this.toolUseContext.abortController.signal.reason === "interrupt")
+        return null;
       return "user_interrupted";
+    }
     return null;
   }
   async executeTool(A) {

@@@ variable 'lkA' (was 'ZkA') — structural (91.4%)
--- pretty-v2.1.31.js:417101
+++ pretty-v2.1.32.js:416738
@@ -11,12 +11,10 @@
   h6();
   ((CvY = b.strictObject({
     query: b.string().min(2).describe("The search query to use"),
-    allowed_domains: b
-      .array(b.string())
+    allowed_domains: B.array(B.string())
       .optional()
       .describe("Only include search results from these domains"),
-    blocked_domains: b
-      .array(b.string())
+    blocked_domains: B.array(B.string())
       .optional()
       .describe("Never include search results from these domains"),
   })),
@@ -30,12 +28,12 @@
     })),
     (IvY = b.object({
       query: b.string().describe("The search query that was executed"),
-      results: b
-        .array(b.union([hvY, b.string()]))
-        .describe("Search results and/or text commentary from the model"),
-      durationSeconds: b
-        .number()
-        .describe("Time taken to complete the search operation"),
+      results: B.array(B.union([bkY, B.string()])).describe(
+        "Search results and/or text commentary from the model",
+      ),
+      durationSeconds: B.number().describe(
+        "Time taken to complete the search operation",
+      ),
     })));
   lM6 = {
     name: vT,

@@@ function 'Hx4' (was 'XI4') — structural (91.3%)
--- pretty-v2.1.31.js:387788
+++ pretty-v2.1.32.js:387271
@@ -4,8 +4,6 @@
   let K = HI4(A);
   if (K) return K;
   let Y = $I4(A);
-  if (Y) return Y;
-  let z = gfA(A);
   if (z) return aMY(z);
   let w = JI4(A);
   if (w) return w;

@@@ function 'T6q' (was 'D1q') — structural (91.2%)
--- pretty-v2.1.31.js:461738
+++ pretty-v2.1.32.js:461717
@@ -93,6 +93,14 @@
     ),
     A.extra_usage &&
       u7.createElement(sUY, { extraUsage: A.extra_usage, maxWidth: $ }),
+    DU1()
+      ? E7.createElement(
+          f,
+          { dimColor: !0 },
+          E7.createElement(f, { color: "claude" }, "$50 free extra usage"),
+          " · /extra-usage to enable",
+        )
+      : null,
     u7.createElement(
       Z,
       { dimColor: !0 },

@@@ function 'a7A' (was 'Z7A') — structural (90.7%)
--- pretty-v2.1.31.js:168341
+++ pretty-v2.1.32.js:168439
@@ -2,11 +2,21 @@
   let q = A.permissions || {},
     K = [],
     Y = [];
-  for (let D of A.sandbox?.network?.allowedDomains || []) K.push(D);
-  for (let D of q.allow || []) {
-    let j = Xy1(D);
-    if (j.toolName === G$ && j.ruleContent?.startsWith("domain:"))
-      K.push(j.ruleContent.substring(7));
+  if (Ly1()) {
+    let D = f7("policySettings");
+    for (let j of D?.sandbox?.network?.allowedDomains || []) K.push(j);
+    for (let j of D?.permissions?.allow || []) {
+      let M = Z_1(j);
+      if (M.toolName === bO && M.ruleContent?.startsWith("domain:"))
+        K.push(M.ruleContent.substring(7));
+    }
+  } else {
+    for (let D of A.sandbox?.network?.allowedDomains || []) K.push(D);
+    for (let D of q.allow || []) {
+      let j = Z_1(D);
+      if (j.toolName === bO && j.ruleContent?.startsWith("domain:"))
+        K.push(j.ruleContent.substring(7));
+    }
   }
   for (let D of q.deny || []) {
     let j = Xy1(D);

@@@ function 'aUA' (was 'fUA') — structural (90.7%)
--- pretty-v2.1.31.js:2010
+++ pretty-v2.1.32.js:2016
@@ -77,6 +77,7 @@
     mainThreadAgentType: void 0,
     isRemoteMode: !1,
     directConnectServerUrl: void 0,
+    systemPromptSectionCache: new Map(),
     additionalDirectoriesForClaudeMd: [],
     resumedTranscriptPath: null,
   };

@@@ variable 'vG6' (was 'YP6') — structural (90.5%)
--- pretty-v2.1.31.js:432808
+++ pretty-v2.1.32.js:432573
@@ -1086,9 +1086,76 @@
       },
       date: {
         safeFlags: {
+          "-a": "none",
+          "-d": "none",
+          "-l": "none",
+          "-f": "none",
+          "-x": "none",
+          "-L": "number",
+          "-R": "none",
+          "-P": "string",
           "-d": "string",
+          "--gitignore": "none",
+          "--gitfile": "string",
+          "--ignore-case": "none",
+          "--matchdirs": "none",
+          "--metafirst": "none",
+          "--prune": "none",
+          "--info": "none",
+          "--infofile": "string",
+          "--noreport": "none",
+          "--charset": "string",
+          "--filelimit": "number",
+          "-q": "none",
+          "-N": "none",
+          "-Q": "none",
+          "-p": "none",
+          "-u": "none",
+          "-g": "none",
+          "-s": "none",
+          "-h": "none",
+          "--si": "none",
+          "--du": "none",
+          "-D": "none",
+          "--timefmt": "string",
+          "-F": "none",
+          "--inodes": "none",
+          "--device": "none",
+          "-v": "none",
+          "-t": "none",
+          "-c": "none",
+          "-U": "none",
+          "-r": "none",
+          "--dirsfirst": "none",
+          "--filesfirst": "none",
           "--date": "string",
+          "-i": "none",
+          "-A": "none",
+          "-S": "none",
+          "-n": "none",
+          "-C": "none",
+          "-X": "none",
+          "-J": "none",
           "-r": "string",
+          "--nolinks": "none",
+          "--hintro": "string",
+          "--houtro": "string",
+          "-T": "string",
+          "--hyperlink": "none",
+          "--scheme": "string",
+          "--authority": "string",
+          "--fromfile": "none",
+          "--fromtabfile": "none",
+          "--fflinks": "none",
+          "--help": "none",
+          "--version": "none",
+        },
+      },
+      date: {
+        safeFlags: {
+          "-d": "string",
+          "--date": "string",
+          "-r": "string",
           "--reference": "string",
           "-u": "none",
           "--utc": "none",
@@ -1212,6 +1279,65 @@
             .some((Y) => Y === "--watch" || Y === "-w");
         },
       },
+      "docker compose ps": {
+        safeFlags: {
+          "--format": "string",
+          "--filter": "string",
+          "--quiet": "none",
+          "-q": "none",
+          "--services": "none",
+          "--status": "string",
+          "--all": "none",
+          "-a": "none",
+          "--no-trunc": "none",
+          "--orphans": "none",
+        },
+      },
+      "docker compose logs": {
+        safeFlags: {
+          "--follow": "none",
+          "-f": "none",
+          "--tail": "string",
+          "-n": "string",
+          "--timestamps": "none",
+          "-t": "none",
+          "--no-color": "none",
+          "--no-log-prefix": "none",
+          "--since": "string",
+          "--until": "string",
+        },
+      },
+      "docker compose top": { safeFlags: {} },
+      "docker compose config": {
+        safeFlags: {
+          "--format": "string",
+          "--services": "none",
+          "--volumes": "none",
+          "--profiles": "none",
+        },
+      },
+      "docker logs": {
+        safeFlags: {
+          "--follow": "none",
+          "-f": "none",
+          "--tail": "string",
+          "-n": "string",
+          "--timestamps": "none",
+          "-t": "none",
+          "--since": "string",
+          "--until": "string",
+          "--details": "none",
+        },
+      },
+      "docker inspect": {
+        safeFlags: {
+          "--format": "string",
+          "-f": "string",
+          "--type": "string",
+          "--size": "none",
+          "-s": "none",
+        },
+      },
     }));
   YIY = ["echo", "printf", "wc", "grep", "head", "tail"];
   ((HIY = [
@@ -1268,7 +1394,6 @@
       /^npm -v$/,
       /^python --version$/,
       /^python3 --version$/,
-      /^tree$/,
       /^history(?:\s+\d+)?\s*$/,
       /^alias$/,
       /^arch(?:\s+(?:--help|-h))?\s*$/,

@@@ function 'dDY' (was 'IXY') — structural (90.2%)
--- pretty-v2.1.31.js:367981
+++ pretty-v2.1.32.js:368033
@@ -38,6 +38,7 @@
   return (
     n46(P),
     Wy1(P),
+    ED7(mD6(_)),
     K((G) => ({
       ...G,
       teamContext: {

@@@ class 'Dm1' (was 'rB1') — structural (90.0%)
--- pretty-v2.1.31.js:355101
+++ pretty-v2.1.32.js:355598
@@ -37,6 +37,8 @@
           organizationUuid: _.organization?.uuid,
           displayName: J.displayName,
           hasExtraUsageEnabled: J.hasExtraUsageEnabled ?? void 0,
+          billingType: J.billingType ?? void 0,
+          subscriptionCreatedAt: J.subscriptionCreatedAt,
         });
       if ($) {
         let X = Wa1(_.scope);

@@@ function 'Nm6' (was 'aB6') — structural (89.6%)
--- pretty-v2.1.31.js:78103
+++ pretty-v2.1.32.js:77954
@@ -21,6 +21,11 @@
       if (_.displayName !== void 0) X.displayName = _.displayName;
       if (typeof _.hasExtraUsageEnabled === "boolean")
         X.hasExtraUsageEnabled = _.hasExtraUsageEnabled;
+      if (_.billingType !== null) X.billingType = _.billingType;
+      if (_.accountCreatedAt !== void 0)
+        X.accountCreatedAt = _.accountCreatedAt;
+      if (_.subscriptionCreatedAt !== void 0)
+        X.subscriptionCreatedAt = _.subscriptionCreatedAt;
       if (Object.keys(X).length > 0)
         XA((D) => ({
           ...D,

@@@ function 'ft' (was 'Jt') — structural (89.6%)
--- pretty-v2.1.31.js:437688
+++ pretty-v2.1.32.js:437619
@@ -33,6 +33,7 @@
         sessionId: z,
         agentName: K?.agentName,
         agentColor: K?.agentColor,
+        agentSetting: K?.agentSetting,
         customTitle: K?.customTitle,
         tag: K?.tag,
         mode: K?.mode,

@@@ function 'yL1' (was 'jL1') — structural (89.4%)
--- pretty-v2.1.31.js:146704
+++ pretty-v2.1.32.js:146625
@@ -7,6 +7,7 @@
       q,
     ];
   if (A.tag) K.push(`#${A.tag}`);
+  if (A.agentSetting) K.push(`agent:${A.agentSetting}`);
   if (A.prNumber) {
     let Y = A.prRepository
       ? `${A.prRepository.split("/")[1]}#${A.prNumber}`

@@@ variable 'Vi7' (was 'qf7') — structural (89.4%)
--- pretty-v2.1.31.js:194683
+++ pretty-v2.1.32.js:251178
@@ -8,6 +8,8 @@
     onDownFromLastItem: H,
     onInputModeToggle: O,
     inputValues: $,
+    imagesSelected: _ = !1,
+    onEnterImageSelection: J,
   }) => {
     nk("select", !!K.onCancel);
     let _ = PKA.useMemo(() => {
@@ -60,6 +62,11 @@
             return;
           }
           if (P) {
+            if (_) return;
+            if (M.downArrow && J?.()) {
+              W.stopImmediatePropagation();
+              return;
+            }
             if (D.downArrow || (D.ctrl && X === "n")) {
               if (H) {
                 let G = Y[Y.length - 1];

@@@ function 'A4z' (was 'mAz') — structural (89.1%)
--- pretty-v2.1.31.js:509994
+++ pretty-v2.1.32.js:509617
@@ -40,6 +40,9 @@
     let O = OA(H[0]);
     return ((O.session_id = q), O);
   } catch (K) {
-    return (e(K instanceof Error ? K : Error("Facet extraction failed")), null);
+    return (
+      K1(K instanceof Error ? K : Error("Facet extraction failed")),
+      null
+    );
   }
 }

@@@ function 'i1z' (was 'btY') — structural (89.1%)
--- pretty-v2.1.31.js:494684
+++ pretty-v2.1.32.js:494362
@@ -4,17 +4,8 @@
   if (A[0] === Symbol.for("react.memo_cache_sentinel"))
     ((q = A7.default.createElement(
       h,
-      { flexDirection: "column" },
-      A7.default.createElement(
-        Z,
-        { bold: !0, color: "professionalBlue" },
-        "Updates to Consumer Terms and Policies",
-      ),
-      A7.default.createElement(
-        Z,
-        null,
-        "We've updated our Consumer Terms and Privacy Policy.",
-      ),
+      null,
+      "We've updated our Consumer Terms and Privacy Policy.",
     )),
       (A[0] = q));
   else q = A[0];

@@@ variable 'pj6' (was 'Tj6') — structural (89.1%)
--- pretty-v2.1.31.js:392349
+++ pretty-v2.1.32.js:391987
@@ -19,16 +19,15 @@
   D8();
   Nj6();
   ((pWY = b.object({
-    skill: b
-      .string()
-      .describe('The skill name. E.g., "commit", "review-pr", or "pdf"'),
+    skill: B.string().describe(
+      'The skill name. E.g., "commit", "review-pr", or "pdf"',
+    ),
     args: b.string().optional().describe("Optional arguments for the skill"),
   })),
     (dWY = b.object({
       success: b.boolean().describe("Whether the skill is valid"),
       commandName: b.string().describe("The name of the skill"),
-      allowedTools: b
-        .array(b.string())
+      allowedTools: B.array(B.string())
         .optional()
         .describe("Tools allowed by this skill"),
       model: b.string().optional().describe("Model override if specified"),
@@ -38,9 +37,9 @@
       success: b.boolean().describe("Whether the skill completed successfully"),
       commandName: b.string().describe("The name of the skill"),
       status: b.literal("forked").describe("Execution status"),
-      agentId: b
-        .string()
-        .describe("The ID of the sub-agent that executed the skill"),
+      agentId: B.string().describe(
+        "The ID of the sub-agent that executed the skill",
+      ),
       result: b.string().describe("The result from the forked skill execution"),
     })),
     (lWY = b.union([dWY, cWY])),
@@ -195,12 +194,12 @@
               I(`  newMessage ${k + 1}: ${y.substring(0, 150)}...`);
             }
           }));
-        let V = f
-            .filter((T) => T.type === "user" && "message" in T)
-            .map((T) => {
+        let Z = V.filter((T) => T.type === "user" && "message" in T).map(
+            (T) => {
               let k = T.message.content;
               return typeof k === "string" ? k : F1(k);
-            }).join(`
+            },
+          ).join(`
 
 `),
           N = _?.type === "prompt" && _.source ? `${_.source}:${O}` : O;

@@@ function 'WKq' (was 'n4q') — structural (89.0%)
--- pretty-v2.1.31.js:484795
+++ pretty-v2.1.32.js:484499
@@ -7,11 +7,11 @@
     O = (w ? z.s1mAccessCache?.[w] : void 0)?.hasAccessNotAsDefault,
     $ = w && z.hasShownS1MWelcomeV2?.[w],
     _ = q7() && O && !$,
-    X = !(w && z.hasShownOpus45Notice?.[w]),
+    X = !(w && z.hasShownOpus46Notice?.[w]),
     D = {
       config: z,
       showSonnet1MNotice: _,
-      showOpus45Notice: X,
+      showOpus46Notice: X,
       agentDefinitions: K,
     },
     j = l4q(D);
@@ -20,7 +20,7 @@
     let N = j.some(faY),
       T = j.some(ZaY);
     if (N) n("tengu_sonnet_1m_notice_shown", {});
-    if (T) n("tengu_opus_45_notice_shown", {});
+    if (T) c("tengu_opus_46_notice_shown", {});
     if (N || T)
       XA((k) => ({
         ...k,
@@ -28,7 +28,7 @@
           hasShownS1MWelcomeV2: { ...k.hasShownS1MWelcomeV2, [w]: !0 },
         }),
         ...(T && {
-          hasShownOpus45Notice: { ...k.hasShownOpus45Notice, [w]: !0 },
+          hasShownOpus46Notice: { ...k.hasShownOpus46Notice, [w]: !0 },
         }),
       }));
   }, [j, z, w]);

@@@ function 'nYz' (was 'S5z') — structural (88.9%)
--- pretty-v2.1.31.js:530547
+++ pretty-v2.1.32.js:530566
@@ -39,9 +39,8 @@
     [m, u] = y_.useState("yes"),
     [U, g] = y_.useState(!1),
     [x, d] = y_.useState(!1),
-    r = y_.useRef(!1);
-  if (A.classifierCheckInProgress) r.current = !0;
-  let q1 = gK1("requesting", "Attempting to auto-approve…", !0, !1),
+    n = C_.useRef(!1),
+    z1 = tK1("requesting", "Attempting to auto-approve…", !0, !1),
     H1 = p8.isSandboxingEnabled(),
     $1 = H1 && UM1(A.input),
     A1 = y_.useMemo(
@@ -76,10 +75,7 @@
   let Z1 = y_.useCallback(() => {
     A.onDismissCheckmark?.();
   }, [A]);
-  zA("confirm:no", Z1, {
-    context: "Confirmation",
-    isActive: !!A.classifierAutoApproved,
-  });
+  DA("confirm:no", G1, { context: "Confirmation", isActive: !1 });
   function j1(K1) {
     A.onUserInteraction();
     let X1 = { toolName: Uq(A.tool.name), isMcp: A.tool.isMcp ?? !1 };
@@ -202,14 +198,12 @@
             }),
             S$.default.createElement(
               Z,
-              { dimColor: A.classifierAutoApproved },
+              { dimColor: !1 },
               "Do you want to proceed?",
             ),
             S$.default.createElement(ZA, {
-              options: A.classifierAutoApproved
-                ? s.map((K1) => ({ ...K1, disabled: !0 }))
-                : s,
-              isDisabled: A.classifierAutoApproved,
+              options: t,
+              isDisabled: !1,
               inlineDescriptions: !0,
               onChange: v1,
               onCancel: () => L1(),

@@@ function '_Kz' (was 'r7z') — structural (88.8%)
--- pretty-v2.1.31.js:518829
+++ pretty-v2.1.32.js:518578
@@ -10,6 +10,7 @@
           H.includes('"isSidechain":true') || H.includes('"isSidechain": true'),
         $ = BbA(H, "cwd"),
         _ = BbA(H, "teamName"),
+        J = UV6(H, "agentSetting"),
         J = o7z(H),
         X = Math.max(0, q - TV6),
         D =
@@ -43,6 +44,7 @@
         teamName: _,
         customTitle: j,
         tag: M,
+        agentSetting: J,
         prNumber: f,
         prUrl: P,
         prRepository: G,

@@@ function 'Tm6' (was 'sB6') — structural (88.8%)
--- pretty-v2.1.31.js:78196
+++ pretty-v2.1.32.js:78052
@@ -23,7 +23,11 @@
     subscriptionType: Y,
     rateLimitTier: q?.organization?.rate_limit_tier ?? null,
     hasExtraUsageEnabled: q?.organization?.has_extra_usage_enabled ?? null,
+    billingType: q?.organization?.billing_type ?? null,
   };
   if (q?.account?.display_name) z.displayName = q.account.display_name;
+  if (q?.account?.created_at) z.accountCreatedAt = q.account.created_at;
+  if (q?.organization?.subscription_created_at)
+    z.subscriptionCreatedAt = q.organization.subscription_created_at;
   return (n("tengu_oauth_profile_fetch_success", {}), z);
 }

@@@ function 'pDY' (was 'hXY') — structural (88.7%)
--- pretty-v2.1.31.js:367948
+++ pretty-v2.1.32.js:368000
@@ -16,7 +16,7 @@
         };
       }
     }
-    (await qL4(w), Fk4());
+    (await tL4(w), BL4(), kD7());
   }
   return (
     K((H) => ({ ...H, teamContext: void 0, inbox: { messages: [] } })),

@@@ function 'za4' (was 'Ko4') — structural (88.5%)
--- pretty-v2.1.31.js:442318
+++ pretty-v2.1.32.js:442261
@@ -3,7 +3,7 @@
   if (hI(w, A, z)) return null;
   try {
     let H = w.readFileSync(A, { encoding: "utf-8" }),
-      { frontmatter: O, content: $ } = z0(H),
+      { frontmatter: O, content: $ } = H0(H, A),
       _ = O.name || nbY(A).replace(/\.md$/, ""),
       X = [q, ...K, _].join(":"),
       D = O.description || O["when-to-use"] || `Agent from ${q} plugin`,

@@@ function 'jHz' (was 'izz') — structural (88.5%)
--- pretty-v2.1.31.js:543822
+++ pretty-v2.1.32.js:543954
@@ -61,6 +61,7 @@
     R6 = T6((j6) => j6.speculationSessionTimeSavedMs),
     K6 = T6((j6) => j6.viewingAgentTaskId),
     a6 = T6((j6) => j6.viewSelectionMode),
+    AA = T6((m6) => m6.showSpinnerTree),
     VA = T6((j6) => j6.mainLoopModel),
     t1 = T6((j6) => j6.mainLoopModelForSession),
     O6 = T6((j6) => j6.thinkingEnabled),
@@ -332,7 +333,8 @@
     if (d) {
       if (G5.length > 0) (e6(!0), K8("none"));
       else if (
-        Object.values(f1).filter((m4) => m4.status === "running").length > 0
+        Object.values(X1).filter((Q4) => Q4.status === "running").length > 0 &&
+        !LZ1(X1, AA)
       )
         K8("tasks");
       else K8("none");
@@ -340,7 +342,7 @@
     }
     if (L6) {
       let Z7 = Object.values(f1).filter((m4) => m4.status === "running").length;
-      if ((e6(!1), Z7 > 0)) K8("tasks");
+      if ((LA(!1), G7 > 0 && !LZ1(X1, AA))) m8("tasks");
       else K8("none");
       return;
     }
@@ -383,7 +385,7 @@
     let Z7 = iA(),
       m4 = G5.length > 0;
     if (Z7) {
-      if (j6 > 0) {
+      if (m6 > 0 && !LZ1(X1, AA)) {
         if ((K8("tasks"), e6(!1), !W6().hasSeenTasksHint))
           XA((D3) => {
             if (D3.hasSeenTasksHint === !0) return D3;
@@ -659,7 +661,7 @@
           L1(!1);
         return;
       }
-      let j6 = $Z1(K, S1);
+      let { nextMode: m6, context: sA } = XXq(K, S1);
       if (
         (n("tengu_mode_cycle", { to: j6 }), K.mode === "plan" && j6 !== "plan")
       )
@@ -669,10 +671,7 @@
       if (j6 === "plan") XA((dA) => ({ ...dA, lastPlanModeUse: Date.now() }));
       if (j6 === "acceptEdits") U4("auto-accept-mode");
       if (
-        (h1((dA) => ({
-          ...dA,
-          toolPermissionContext: { ...dA.toolPermissionContext, mode: j6 },
-        })),
+        (I1((G7) => ({ ...G7, toolPermissionContext: { ...sA, mode: m6 } })),
         Y({ ...K, mode: j6 }),
         WNA(j6, S1?.teamName),
         j1)
@@ -884,6 +883,8 @@
     }));
   let u$ = UJq(),
     B$ = !1,
+    DY = !1,
+    yJ = !1,
     { columns: m$, rows: $Y } = A8(),
     xJ = m$ - 3,
     rO = hJ && b3 ? b3 : P6,
@@ -1121,7 +1122,7 @@
             width: "100%",
             borderText: B$
               ? {
-                  content: ` ${YxA()} `,
+                  content: ` ${uxA(!0, mX)} `,
                   position: "top",
                   align: "end",
                   offset: 0,

@@@ variable 'DW6' (was 'nM6') — structural (88.4%)
--- pretty-v2.1.31.js:417807
+++ pretty-v2.1.32.js:417421
@@ -7,89 +7,71 @@
   kj();
   ((k$ = o(J1(), 1)),
     (mvY = b.object({
-      label: b
-        .string()
-        .describe(
-          "The display text for this option that the user will see and select. Should be concise (1-5 words) and clearly describe the choice.",
-        ),
-      description: b
-        .string()
-        .describe(
-          "Explanation of what this option means or what will happen if chosen. Useful for providing context about trade-offs or implications.",
-        ),
+      label: B.string().describe(
+        "The display text for this option that the user will see and select. Should be concise (1-5 words) and clearly describe the choice.",
+      ),
+      description: B.string().describe(
+        "Explanation of what this option means or what will happen if chosen. Useful for providing context about trade-offs or implications.",
+      ),
     })),
     (Ug4 = b.object({
-      question: b
-        .string()
-        .describe(
-          'The complete question to ask the user. Should be clear, specific, and end with a question mark. Example: "Which library should we use for date formatting?" If multiSelect is true, phrase it accordingly, e.g. "Which features do you want to enable?"',
-        ),
-      header: b
-        .string()
-        .describe(
-          `Very short label displayed as a chip/tag (max ${Q34} chars). Examples: "Auth method", "Library", "Approach".`,
-        ),
-      options: b
-        .array(mvY)
+      question: B.string().describe(
+        'The complete question to ask the user. Should be clear, specific, and end with a question mark. Example: "Which library should we use for date formatting?" If multiSelect is true, phrase it accordingly, e.g. "Which features do you want to enable?"',
+      ),
+      header: B.string().describe(
+        `Very short label displayed as a chip/tag (max ${S$7} chars). Examples: "Auth method", "Library", "Approach".`,
+      ),
+      options: B.array(gkY)
         .min(2)
         .max(4)
         .describe(
           "The available choices for this question. Must have 2-4 options. Each option should be a distinct, mutually exclusive choice (unless multiSelect is enabled). There should be no 'Other' option, that will be provided automatically.",
         ),
-      multiSelect: b
-        .boolean()
+      multiSelect: B.boolean()
         .default(!1)
         .describe(
           "Set to true to allow the user to select multiple options instead of just one. Use when choices are not mutually exclusive.",
         ),
     })),
-    (fkA = b
-      .strictObject({
-        questions: b
-          .array(Ug4)
-          .min(1)
-          .max(4)
-          .describe("Questions to ask the user (1-4 questions)"),
-        answers: b
-          .record(b.string(), b.string())
-          .optional()
-          .describe("User answers collected by the permission component"),
-        metadata: b
-          .object({
-            source: b
-              .string()
-              .optional()
-              .describe(
-                'Optional identifier for the source of this question (e.g., "remember" for /remember command). Used for analytics tracking.',
-              ),
-          })
+    (ikA = B.strictObject({
+      questions: B.array(xU4)
+        .min(1)
+        .max(4)
+        .describe("Questions to ask the user (1-4 questions)"),
+      answers: B.record(B.string(), B.string())
+        .optional()
+        .describe("User answers collected by the permission component"),
+      metadata: B.object({
+        source: B.string()
           .optional()
           .describe(
-            "Optional metadata for tracking and analytics purposes. Not displayed to user.",
+            'Optional identifier for the source of this question (e.g., "remember" for /remember command). Used for analytics tracking.',
           ),
       })
-      .refine(
-        (A) => {
-          let q = A.questions.map((K) => K.question);
+        .optional()
+        .describe(
+          "Optional metadata for tracking and analytics purposes. Not displayed to user.",
+        ),
+    }).refine(
+      (A) => {
+        let q = A.questions.map((K) => K.question);
+        if (q.length !== new Set(q).size) return !1;
+        for (let K of A.questions) {
+          let Y = K.options.map((z) => z.label);
           if (q.length !== new Set(q).size) return !1;
-          for (let K of A.questions) {
-            let Y = K.options.map((z) => z.label);
-            if (Y.length !== new Set(Y).size) return !1;
-          }
-          return !0;
-        },
-        {
-          message:
-            "Question texts must be unique, option labels must be unique within each question",
-        },
-      )),
+        }
+        return !0;
+      },
+      {
+        message:
+          "Question texts must be unique, option labels must be unique within each question",
+      },
+    )),
     (l6H = b.object({
       questions: b.array(Ug4).describe("The questions that were asked"),
-      answers: b
-        .record(b.string(), b.string())
-        .describe(
-          "The answers provided by the user (question text -> answer string; multi-select answers are comma-separated)",
-        ),
+      answers: B.record(B.string(), B.string()).describe(
+        "The answers provided by the user (question text -> answer string; multi-select answers are comma-separated)",
+      ),
     })));
   iM6 = {
     name: Rw,

@@@ function 'NuY' (was 'kxY') — structural (88.3%)
--- pretty-v2.1.31.js:439291
+++ pretty-v2.1.32.js:439231
@@ -29,7 +29,9 @@
       Fw("todo_reminders", () => (wH() ? zbY(z, q) : KbY(z, q))),
       ...(U8()
         ? [
-            Fw("teammate_mailbox", async () => $bY(q)),
+            ...(w === "session_memory"
+              ? []
+              : [lw("teammate_mailbox", async () => zBY(q))]),
             Fw("team_context", async () => _bY(z ?? [])),
           ]
         : []),

@@@ function 'JWA' (was 'TMA') — structural (88.1%)
--- pretty-v2.1.31.js:311551
+++ pretty-v2.1.32.js:312324
@@ -28,7 +28,8 @@
     let O = H,
       _ = {
         ddsource: "nodejs",
-        ddtags: Mr9.filter((J) => O[J] !== void 0 && O[J] !== null)
+        ddtags: la9
+          .filter((J) => O[J] !== void 0 && O[J] !== null)
           .map((J) => `${Jw4(J)}:${O[J]}`)
           .join(","),
         message: A,

@@@ function 'gLY' (was 'mEY') — structural (88.1%)
--- pretty-v2.1.31.js:420951
+++ pretty-v2.1.32.js:420511
@@ -48,6 +48,7 @@
         senderColor: H,
         target: "@team",
         summary: A.summary,
+        content: A.content,
       },
     },
   };

@@@ function 'X94' (was 'n34') — structural (88.0%)
--- pretty-v2.1.31.js:295688
+++ pretty-v2.1.32.js:297528
@@ -1,5 +1,6 @@
 function n34(A) {
-  let q = A.split(xDA.sep).join(IDA.sep);
+  let q = Oc9(A),
+    K = q.split(xjA.sep).join(IjA.sep);
   if (
     hO() &&
     (q.includes("/agent-memory/") || q.includes("/agent-memory-local/"))

@@@ function 'm0q' (was 'rJq') — structural (87.9%)
--- pretty-v2.1.31.js:543533
+++ pretty-v2.1.32.js:543659
@@ -56,6 +56,7 @@
         (n("tengu_prompt_suggestion", {
           outcome: N ? "accepted" : "ignored",
           prompt_id: w,
+          coordinator_mode: h9(),
           ...($ && { generationRequestId: $ }),
           ...(N && { acceptMethod: V ? "tab" : "enter" }),
           ...(N && { timeToAcceptMs: T - H }),

@@@ class 'VmA' (was 'pBA') — structural (87.6%)
--- pretty-v2.1.31.js:545124
+++ pretty-v2.1.32.js:545260
@@ -107,6 +107,15 @@
     }
     (I("[SessionsWebSocket] Sending control response"), this.ws.send(F1(A)));
   }
+  sendControlRequest(A) {
+    if (!this.ws || this.state !== "connected") {
+      K1(Error("[SessionsWebSocket] Cannot send: not connected"));
+      return;
+    }
+    let q = { type: "control_request", request_id: WHz(), request: A };
+    (h(`[SessionsWebSocket] Sending control request: ${A.subtype}`),
+      this.ws.send(g1(q)));
+  }
   isConnected() {
     return this.state === "connected";
   }

@@@ function 'P6q' (was '_1q') — structural (87.5%)
--- pretty-v2.1.31.js:460347
+++ pretty-v2.1.32.js:460213
@@ -120,16 +120,22 @@
         },
       },
       ...[],
-      {
-        id: "promptSuggestionEnabled",
-        label: "Prompt suggestions",
-        value: c,
-        type: "boolean",
-        onChange(f1) {
-          (q1((S1) => ({ ...S1, promptSuggestionEnabled: f1 })),
-            D7("userSettings", { promptSuggestionEnabled: f1 ? void 0 : !1 }));
-        },
-      },
+      ...(x8("tengu_chomp_inflection", !0)
+        ? [
+            {
+              id: "promptSuggestionEnabled",
+              label: "Prompt suggestions",
+              value: r,
+              type: "boolean",
+              onChange(X1) {
+                (z1((S1) => ({ ...S1, promptSuggestionEnabled: X1 })),
+                  _7("userSettings", {
+                    promptSuggestionEnabled: X1 ? void 0 : !1,
+                  }));
+              },
+            },
+          ]
+        : []),
       ...[],
       ...(K1
         ? [
@@ -924,10 +930,10 @@
                           PACKAGE_URL: "@anthropic-ai/claude-code",
                           README_URL:
                             "https://code.claude.com/docs/en/overview",
-                          VERSION: "2.1.31",
+                          VERSION: "2.1.32",
                           FEEDBACK_CHANNEL:
                             "https://github.com/anthropics/claude-code/issues",
-                          BUILD_TIME: "2026-02-04T00:00:54Z",
+                          BUILD_TIME: "2026-02-05T17:02:01Z",
                         }.VERSION,
                         onChoice: (f1) => {
                           if ((Z1(null), K(!1), f1 === "cancel")) return;
@@ -939,10 +945,10 @@
                               PACKAGE_URL: "@anthropic-ai/claude-code",
                               README_URL:
                                 "https://code.claude.com/docs/en/overview",
-                              VERSION: "2.1.31",
+                              VERSION: "2.1.32",
                               FEEDBACK_CHANNEL:
                                 "https://github.com/anthropics/claude-code/issues",
-                              BUILD_TIME: "2026-02-04T00:00:54Z",
+                              BUILD_TIME: "2026-02-05T17:02:01Z",
                             }.VERSION;
                           (D7("userSettings", S1),
                             M((E1) => ({ ...E1, ...S1 })),

@@@ function 'K0' (was 'HD') — structural (87.5%)
--- pretty-v2.1.31.js:147265
+++ pretty-v2.1.32.js:147212
@@ -1,4 +1,5 @@
 function HD(A) {
+  if (A.includes("claude-opus-4-6")) return "claude-opus-4-6";
   if (A.includes("claude-opus-4-5")) return "claude-opus-4-5";
   if (A.includes("claude-opus-4-1")) return "claude-opus-4-1";
   if (A.includes("claude-opus-4")) return "claude-opus-4";

@@@ function 'zNA' (was 'LVA') — structural (87.3%)
--- pretty-v2.1.31.js:519697
+++ pretty-v2.1.32.js:519453
@@ -1,4 +1,5 @@
 function LVA(A, q) {
+  let K = zZ1(A);
   if (J4z(A))
     return {
       behavior: "allow",

@@@ function 'RCA' (was 'KCA') — structural (87.2%)
--- pretty-v2.1.31.js:446494
+++ pretty-v2.1.32.js:446443
@@ -14,5 +14,5 @@
     }
   }
   let Y = `MCP server "${K}" tool "${q}": unexpected response format`;
-  throw (Pz(K, Y), new VF(Y));
+  throw (Gz(K, Y), new FE(Y, "MCP tool unexpected response format"));
 }

@@@ function 'BlY' (was 'udY') — structural (87.1%)
--- pretty-v2.1.31.js:465457
+++ pretty-v2.1.32.js:464880
@@ -4,6 +4,7 @@
   });
   let { columns: q } = A8(),
     K = async ($) => {
+      B4("memory-mode");
       try {
         if ($.includes(w8())) {
           let j = w8();

@@@ function 'ZJz' (was 'sOz') — structural (87.1%)
--- pretty-v2.1.31.js:562535
+++ pretty-v2.1.32.js:562684
@@ -1,4 +1,4 @@
-async function sOz(A, q, K, Y, z, w, H, O, $, _) {
+async function ZJz(A, q, K, Y, z, w, H, O, $, _, J) {
   if (K) {
     Y.enqueue({
       type: "control_response",
@@ -46,30 +46,27 @@
     M11(M);
   }
   if (A.jsonSchema) UE6(A.jsonSchema);
+  let W = {
+    commands: z.map((G) => ({
+      name: G.userFacingName(),
+      description: fP1(G),
+      argumentHint: G.argumentHint || "",
+    })),
+    output_style: D,
+    available_output_styles: Object.keys(j),
+    models: w,
+    account: {
+      email: M?.email,
+      organization: M?.organization,
+      subscriptionType: M?.subscription,
+      tokenSource: M?.tokenSource,
+      apiKeySource: M?.apiKeySource,
+    },
+  };
   if (
     (Y.enqueue({
       type: "control_response",
-      response: {
-        subtype: "success",
-        request_id: q,
-        response: {
-          commands: z.map((M) => ({
-            name: M.userFacingName(),
-            description: wG1(M),
-            argumentHint: M.argumentHint || "",
-          })),
-          output_style: X,
-          available_output_styles: Object.keys(D),
-          models: w,
-          account: {
-            email: j?.email,
-            organization: j?.organization,
-            subscriptionType: j?.subscription,
-            tokenSource: j?.tokenSource,
-            apiKeySource: j?.apiKeySource,
-          },
-        },
-      },
+      response: { subtype: "success", request_id: q, response: W },
     }),
     O)
   ) {

@@@ variable 'wp4' (was 'jU4') — structural (87.1%)
--- pretty-v2.1.31.js:418854
+++ pretty-v2.1.32.js:418432
@@ -11,8 +11,29 @@
   _6();
   JU4();
   ((qEY = b.strictObject({
-    operation: b
-      .enum([
+    operation: B.enum([
+      "goToDefinition",
+      "findReferences",
+      "hover",
+      "documentSymbol",
+      "workspaceSymbol",
+      "goToImplementation",
+      "prepareCallHierarchy",
+      "incomingCalls",
+      "outgoingCalls",
+    ]).describe("The LSP operation to perform"),
+    filePath: B.string().describe("The absolute or relative path to the file"),
+    line: B.number()
+      .int()
+      .positive()
+      .describe("The line number (1-based, as shown in editors)"),
+    character: B.number()
+      .int()
+      .positive()
+      .describe("The character offset (1-based, as shown in editors)"),
+  })),
+    (wLY = B.object({
+      operation: B.enum([
         "goToDefinition",
         "findReferences",
         "hover",
@@ -22,46 +43,17 @@
         "prepareCallHierarchy",
         "incomingCalls",
         "outgoingCalls",
-      ])
-      .describe("The LSP operation to perform"),
-    filePath: b.string().describe("The absolute or relative path to the file"),
-    line: b
-      .number()
-      .int()
-      .positive()
-      .describe("The line number (1-based, as shown in editors)"),
-    character: b
-      .number()
-      .int()
-      .positive()
-      .describe("The character offset (1-based, as shown in editors)"),
-  })),
-    (KEY = b.object({
-      operation: b
-        .enum([
-          "goToDefinition",
-          "findReferences",
-          "hover",
-          "documentSymbol",
-          "workspaceSymbol",
-          "goToImplementation",
-          "prepareCallHierarchy",
-          "incomingCalls",
-          "outgoingCalls",
-        ])
-        .describe("The LSP operation that was performed"),
+      ]).describe("The LSP operation that was performed"),
       result: b.string().describe("The formatted result of the LSP operation"),
-      filePath: b
-        .string()
-        .describe("The file path the operation was performed on"),
-      resultCount: b
-        .number()
+      filePath: B.string().describe(
+        "The file path the operation was performed on",
+      ),
+      resultCount: B.number()
         .int()
         .nonnegative()
         .optional()
         .describe("Number of results (definitions, references, symbols)"),
-      fileCount: b
-        .number()
+      fileCount: B.number()
         .int()
         .nonnegative()
         .optional()
@@ -153,7 +145,9 @@
         let w = gp();
         if (!w)
           return (
-            e(Error("LSP server manager not initialized when tool was called")),
+            K1(
+              Error("LSP server manager not initialized when tool was called"),
+            ),
             {
               data: {
                 operation: A.operation,

@@@ function 'le4' (was 'ot4') — structural (86.8%)
--- pretty-v2.1.31.js:455892
+++ pretty-v2.1.32.js:455687
@@ -30,6 +30,8 @@
         m = wSA(z),
         u = [...new Set([...C, ...m])],
         [U, g] = await Promise.all([HSA(u), TgY()]),
+        x = hSA(z),
+        p = { ...U, ...x },
         x = {
           latestAssistantMessageId: B,
           message_count: q.length,
@@ -43,10 +45,10 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.31",
+            VERSION: "2.1.32",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-02-04T00:00:54Z",
+            BUILD_TIME: "2026-02-05T17:02:01Z",
           }.VERSION,
           transcript: $_(q),
           errors: k,
@@ -203,10 +205,10 @@
                     "report the issue at https://github.com/anthropics/claude-code/issues",
                   PACKAGE_URL: "@anthropic-ai/claude-code",
                   README_URL: "https://code.claude.com/docs/en/overview",
-                  VERSION: "2.1.31",
+                  VERSION: "2.1.32",
                   FEEDBACK_CHANNEL:
                     "https://github.com/anthropics/claude-code/issues",
-                  BUILD_TIME: "2026-02-04T00:00:54Z",
+                  BUILD_TIME: "2026-02-05T17:02:01Z",
                 }.VERSION,
               ),
             ),

@@@ function 'eM1' (was 'dM1') — structural (86.7%)
--- pretty-v2.1.31.js:368516
+++ pretty-v2.1.32.js:368197
@@ -39,7 +39,7 @@
         status: "in_progress",
         blocks: [],
         blockedBy: [],
-        metadata: {},
+        metadata: { _internal: !0 },
       }),
       G = {
         ...oG(J, "in_process_teammate", W),

@@@ function 'qj7' (was 'MD7') — structural (86.6%)
--- pretty-v2.1.31.js:178363
+++ pretty-v2.1.32.js:178483
@@ -21,9 +21,11 @@
     if (q >= 98 && q <= 99) return !0;
   }
   if (
-    (A >= 3633 && A <= 3642) ||
+    A === 3633 ||
+    (A >= 3636 && A <= 3642) ||
     (A >= 3655 && A <= 3662) ||
-    (A >= 3761 && A <= 3772) ||
+    A === 3761 ||
+    (A >= 3764 && A <= 3772) ||
     (A >= 3784 && A <= 3789)
   )
     return !0;

@@@ function 'A7q' (was 'IAq') — structural (86.5%)
--- pretty-v2.1.31.js:472949
+++ pretty-v2.1.32.js:472651
@@ -200,9 +200,7 @@
       try {
         (await dr4(A1.name, O1),
           _((s) =>
-            s.map((w1) =>
-              w1.name === A1.name ? { ...w1, autoUpdate: O1 } : w1,
-            ),
+            t.map((e) => (e.name === H1.name ? { ...e, autoUpdate: D1 } : e)),
           ),
           C((s) => (s ? { ...s, autoUpdate: O1 } : s)));
       } catch (s) {

@@@ function 'gPY' (was 'mWY') — structural (86.4%)
--- pretty-v2.1.31.js:391932
+++ pretty-v2.1.32.js:391569
@@ -50,6 +50,7 @@
       },
       taskId: G.taskId,
       prompt: w,
+      description: A.description,
       agentDefinition: W,
       teammateContext: G.teammateContext,
       toolUseContext: q,

@@@ function 'jP1' (was 'tP1') — structural (86.3%)
--- pretty-v2.1.31.js:459684
+++ pretty-v2.1.32.js:459549
@@ -10,12 +10,13 @@
     O = A === null ? ZZ6 : A,
     $ = 10,
     _ = v7(),
+    J = T6((x) => !1),
     J = T6((g) => g.effortValue),
     X = sV.useRef(J !== void 0 ? A1q(J) : "high"),
     [D, j] = sV.useState(X.current),
     [M, W] = sV.useState(!1),
     [P, G] = sV.useState(O),
-    f = sV.useMemo(() => q81(), []),
+    Z = _N.useMemo(() => J81(J ?? !1), [J]),
     V = sV.useMemo(() => {
       if (A !== null && !f.some((g) => g.value === A))
         return [...f, { value: A, label: qC(A), description: "Current model" }];

@@@ function 'Yz5' (was 'Z95') — structural (86.3%)
--- pretty-v2.1.31.js:138436
+++ pretty-v2.1.32.js:138327
@@ -14,7 +14,8 @@
     H = tx(A, "claude-sonnet-4-5-20250929"),
     O = tx(A, "claude-opus-4-20250514"),
     $ = tx(A, "claude-opus-4-1-20250805"),
-    _ = tx(A, "claude-opus-4-5-20251101");
+    _ = _C(A, "claude-opus-4-5-20251101"),
+    J = _C(A, "claude-opus-4-6");
   return {
     haiku35: q || Uk1.bedrock,
     haiku45: K || pk1.bedrock,
@@ -25,5 +26,6 @@
     opus40: O || ck1.bedrock,
     opus41: $ || lk1.bedrock,
     opus45: _ || IA1.bedrock,
+    opus46: J || gA1.bedrock,
   };
 }

@@@ function 'k54' (was 'H34') — structural (86.1%)
--- pretty-v2.1.31.js:293676
+++ pretty-v2.1.32.js:295514
@@ -3,7 +3,7 @@
   if (hI(Y, A, K)) return null;
   try {
     let z = Y.readFileSync(A, { encoding: "utf-8" }),
-      { frontmatter: w, content: H } = z0(z),
+      { frontmatter: w, content: H } = H0(z, A),
       O = Vg9(A, ".md"),
       $ = w.name || O,
       _ = `${q}:${$}`,

@@@ variable 'kD' — structural (86.0%)
--- pretty-v2.1.31.js:450925
+++ pretty-v2.1.32.js:450870
@@ -39,6 +39,7 @@
   zZ();
   fW1();
   W2();
+  gz();
   ((NCA = o(J1(), 1)),
     (IFY = new Set([
       "find",
@@ -69,8 +70,7 @@
     (hG6 = M6(process.env.CLAUDE_CODE_DISABLE_BACKGROUND_TASKS)),
     (Es4 = b.strictObject({
       command: b.string().describe("The command to execute"),
-      timeout: b
-        .number()
+      timeout: B.number()
         .optional()
         .describe(`Optional timeout in milliseconds (max ${NG6()})`),
       description: b.string().optional()
@@ -85,20 +85,20 @@
 - find . -name "*.tmp" -exec rm {} \\; → "Find and delete all .tmp files recursively"
 - git reset --hard origin/main → "Discard all local changes and match remote main"
 - curl -s url | jq '.data[]' → "Fetch JSON from URL and extract data array elements"`),
-      run_in_background: b
-        .boolean()
+      run_in_background: B.boolean()
         .optional()
         .describe(
           "Set to true to run this command in the background. Use TaskOutput to read the output later.",
         ),
-      dangerouslyDisableSandbox: b
-        .boolean()
+      dangerouslyDisableSandbox: B.boolean()
         .optional()
         .describe(
           "Set this to true to dangerously override sandbox mode and run commands without sandboxing.",
         ),
-      _simulatedSedEdit: b
-        .object({ filePath: b.string(), newContent: b.string() })
+      _simulatedSedEdit: B.object({
+        filePath: B.string(),
+        newContent: B.string(),
+      })
         .optional()
         .describe("Internal: pre-computed sed edit result from preview"),
     })),
@@ -130,39 +130,32 @@
   FFY = b.object({
     stdout: b.string().describe("The standard output of the command"),
     stderr: b.string().describe("The standard error output of the command"),
-    rawOutputPath: b
-      .string()
+    rawOutputPath: B.string()
       .optional()
       .describe("Path to raw output file for large MCP tool outputs"),
     interrupted: b.boolean().describe("Whether the command was interrupted"),
-    isImage: b
-      .boolean()
+    isImage: B.boolean()
       .optional()
       .describe("Flag to indicate if stdout contains image data"),
-    backgroundTaskId: b
-      .string()
+    backgroundTaskId: B.string()
       .optional()
       .describe(
         "ID of the background task if command is running in background",
       ),
-    backgroundedByUser: b
-      .boolean()
+    backgroundedByUser: B.boolean()
       .optional()
       .describe(
         "True if the user manually backgrounded the command with Ctrl+B",
       ),
-    dangerouslyDisableSandbox: b
-      .boolean()
+    dangerouslyDisableSandbox: B.boolean()
       .optional()
       .describe("Flag to indicate if sandbox mode was overridden"),
-    returnCodeInterpretation: b
-      .string()
+    returnCodeInterpretation: B.string()
       .optional()
       .describe(
         "Semantic interpretation for non-error exit codes with special meaning",
       ),
-    structuredContent: b
-      .array(b.any())
+    structuredContent: B.array(B.any())
       .optional()
       .describe("Structured content blocks from mcp-cli commands"),
   });
@@ -315,15 +308,15 @@
             });
           }
         while (!c.done);
+        ((W = r.value), BgY(A.command, W.code, W.stdout));
+        let z1 = W.interrupted && w.signal.reason === "interrupt";
         if (
-          ((W = c.value),
-          gFY(A.command, W.code, W.stdout),
-          J.append((W.stdout || "").trimEnd() + Gg1),
+          (J.append((W.stdout || "").trimEnd() + pg1),
           (D = Ns4(A.command, W.code, W.stdout || "", W.stderr || "")),
           W.stderr && W.stderr.includes(".git/index.lock': File exists"))
         )
           n("tengu_git_index_lock_error", {});
-        if (D.isError) {
+        if (D.isError && !z1) {
           if ((X.append(W.stderr.trimEnd() + Gg1), W.code !== 0))
             X.append(`Exit code ${W.code}`);
         } else if (oK1(A.command) !== null) X.append(W.stderr.trimEnd() + Gg1);
@@ -339,8 +332,8 @@
           A.command,
           W.stderr || "",
         );
-        if (D.isError) throw new Vy(W.stdout, q1, W.code, W.interrupted);
-        M = W.interrupted;
+        if (D.isError && !z1) throw new Iy(W.stdout, f1, W.code, W.interrupted);
+        M = z1 ? !1 : W.interrupted;
       } finally {
         if (_) _(null);
       }

@@@ function 'HT6' (was 'mN6') — structural (86.0%)
--- pretty-v2.1.31.js:547830
+++ pretty-v2.1.32.js:548142
@@ -47,18 +47,22 @@
     if (q1 && q1.type === "local-jsx") {
       (H(""), y(0), B());
       let H1 = J(X, [], n4(), [], void 0, D),
-        $1 = (O1, s) => {
-          if (
-            (_({ jsx: null, shouldHidePromptInput: !1, clearLocalJSX: !0 }),
-            O1 && s?.display !== "skip" && A.addNotification)
-          )
-            A.addNotification({
-              key: `immediate-${q1.name}`,
-              text: O1,
-              priority: "low",
-            });
-        },
-        A1 = await q1.call($1, H1, c);
+        H1 = await HG1(
+          z1,
+          (D1, t) => {
+            if (
+              (_({ jsx: null, shouldHidePromptInput: !1, clearLocalJSX: !0 }),
+              D1 && t?.display !== "skip" && A.addNotification)
+            )
+              A.addNotification({
+                key: `immediate-${z1.name}`,
+                text: D1,
+                priority: "low",
+              });
+          },
+          f1,
+          r,
+        );
       if (A1) _({ jsx: A1, shouldHidePromptInput: !1, isLocalJSXCommand: !0 });
       return;
     }

@@@ variable 'xv' (was 'fv') — structural (85.9%)
--- pretty-v2.1.31.js:449971
+++ pretty-v2.1.32.js:449924
@@ -117,20 +117,17 @@
     ])));
   ((PG6 = b.strictObject({
     file_path: b.string().describe("The absolute path to the file to read"),
-    offset: b
-      .number()
+    offset: B.number()
       .optional()
       .describe(
         "The line number to start reading from. Only provide if the file is too large to read at once",
       ),
-    limit: b
-      .number()
+    limit: B.number()
       .optional()
       .describe(
         "The number of lines to read. Only provide if the file is too large to read at once.",
       ),
-    pages: b
-      .string()
+    pages: B.string()
       .optional()
       .describe(
         `Page range for PDF files (e.g., "1-5", "3", "10-20"). Only applicable to PDF files. Maximum ${XJ1} pages per request.`,
@@ -143,9 +140,9 @@
         file: b.object({
           filePath: b.string().describe("The path to the file that was read"),
           content: b.string().describe("The content of the file"),
-          numLines: b
-            .number()
-            .describe("Number of lines in the returned content"),
+          numLines: B.number().describe(
+            "Number of lines in the returned content",
+          ),
           startLine: b.number().describe("The starting line number"),
           totalLines: b.number().describe("Total number of lines in the file"),
         }),
@@ -156,25 +153,20 @@
           base64: b.string().describe("Base64-encoded image data"),
           type: ZFY.describe("The MIME type of the image"),
           originalSize: b.number().describe("Original file size in bytes"),
-          dimensions: b
-            .object({
-              originalWidth: b
-                .number()
-                .optional()
-                .describe("Original image width in pixels"),
-              originalHeight: b
-                .number()
-                .optional()
-                .describe("Original image height in pixels"),
-              displayWidth: b
-                .number()
-                .optional()
-                .describe("Displayed image width in pixels (after resizing)"),
-              displayHeight: b
-                .number()
-                .optional()
-                .describe("Displayed image height in pixels (after resizing)"),
-            })
+          dimensions: B.object({
+            originalWidth: B.number()
+              .optional()
+              .describe("Original image width in pixels"),
+            originalHeight: B.number()
+              .optional()
+              .describe("Original image height in pixels"),
+            displayWidth: B.number()
+              .optional()
+              .describe("Displayed image width in pixels (after resizing)"),
+            displayHeight: B.number()
+              .optional()
+              .describe("Displayed image height in pixels (after resizing)"),
+          })
             .optional()
             .describe("Image dimension info for coordinate mapping"),
         }),
@@ -200,9 +192,9 @@
           filePath: b.string().describe("The path to the PDF file"),
           originalSize: b.number().describe("Original file size in bytes"),
           count: b.number().describe("Number of pages extracted"),
-          outputDir: b
-            .string()
-            .describe("Directory containing extracted page images"),
+          outputDir: B.string().describe(
+            "Directory containing extracted page images",
+          ),
         }),
       }),
     ])),

@@@ function 's9' (was 'c2') — structural (85.7%)
--- pretty-v2.1.31.js:147446
+++ pretty-v2.1.32.js:147408
@@ -12,7 +12,7 @@
       case "haiku":
         return p1A() + (Y ? "[1m]" : "");
       case "opus":
-        return AC();
+        return WC() + (Y ? "[1m]" : "");
       case "best":
         return MV5();
       default:

@@@ function 'SmA' (was 'Im1') — structural (85.6%)
--- pretty-v2.1.31.js:367365
+++ pretty-v2.1.32.js:546704
@@ -43,7 +43,7 @@
       "",
       (J, X) => {
         xm1(Y, w, !1);
-        let D = wm1(w);
+        let D = vm1(w, { idleReason: "available", summary: Rm1(J) });
         return (
           p5(_, {
             from: w,

@@@ function 'dP1' (was 'yG1') — structural (85.6%)
--- pretty-v2.1.31.js:491095
+++ pretty-v2.1.32.js:490768
@@ -5,9 +5,11 @@
     H =
       K === "completed"
         ? "success"
-        : K === "failed" || K === "killed"
+        : K === "failed"
           ? "error"
-          : void 0,
+          : K === "killed"
+            ? "warning"
+            : void 0,
     O;
   if (q[0] !== H || q[1] !== w || q[2] !== z)
     ((O = RG1.default.createElement(

@@@ function '_R4' (was 'DL4') — structural (85.5%)
--- pretty-v2.1.31.js:369195
+++ pretty-v2.1.32.js:368861
@@ -228,7 +228,6 @@
           allIdle: h1,
           leaderVerb: q1,
           leaderTokenCount: V6,
-          frame: w1,
         }),
     );
   }
@@ -270,7 +269,6 @@
           allIdle: h1,
           leaderVerb: q1,
           leaderTokenCount: V6,
-          frame: w1,
         })
       : N && u && u.length > 0
         ? e8.createElement(

@@@ variable 'Q8' (was 'F8') — structural (85.5%)
--- pretty-v2.1.31.js:452191
+++ pretty-v2.1.32.js:452138
@@ -10,8 +10,6 @@
   CCA();
   nU();
   fP1();
-  C8();
-  _6();
   ((T0 = o(J1(), 1)), (s31 = { status: "idle" }));
   ((SCA = T0.default.createContext(null)),
     (gs4 = T0.default.createContext(!1)));

@@@ function 'xXq' (was 'p_q') — structural (85.4%)
--- pretty-v2.1.31.js:540406
+++ pretty-v2.1.32.js:540616
@@ -25,11 +25,15 @@
       });
   if (H.length > 0) K.current = [...K.current, ...H];
   if (!M_()) return null;
-  let O = [];
+  let O = 3000,
+    $ = [];
   for (let $ of K.current) {
     let _ = z.get($);
     if (!_) continue;
     if (!_Z1(_.status)) O.push(_);
+    else if (J.status === "killed" && J.endTime) {
+      if (Date.now() - J.endTime < O) $.push(J);
+    }
   }
   if (O.length === 0) return null;
   return SZ.createElement(

@@@ class 'Bd1' (was '_d1') — structural (85.3%)
--- pretty-v2.1.31.js:560443
+++ pretty-v2.1.32.js:560579
@@ -11,7 +11,6 @@
   reconnectTimer = null;
   pingInterval = null;
   pongReceived = !0;
-  keepaliveInterval = null;
   messageBuffer;
   constructor(A, q = {}, K) {
     ((this.url = A),
@@ -54,7 +53,6 @@
         ((this.reconnectAttempts = 0),
           (this.state = "connected"),
           this.startPingInterval(),
-          this.startKeepaliveInterval(),
           zS7(() => {
             if (this.state === "connected" && this.ws)
               try {
@@ -110,7 +108,7 @@
     }
   }
   doDisconnect() {
-    if ((this.stopPingInterval(), this.stopKeepaliveInterval(), HYA(), this.ws))
+    if ((this.stopPingInterval(), jXA(), this.ws))
       (this.ws.close(), (this.ws = null));
   }
   handleConnectionError() {
@@ -152,7 +150,6 @@
     if (this.reconnectTimer)
       (clearTimeout(this.reconnectTimer), (this.reconnectTimer = null));
     (this.stopPingInterval(),
-      this.stopKeepaliveInterval(),
       HYA(),
       (this.state = "closing"),
       this.doDisconnect());
@@ -245,23 +242,5 @@
   stopPingInterval() {
     if (this.pingInterval)
       (clearInterval(this.pingInterval), (this.pingInterval = null));
-  }
-  startKeepaliveInterval() {
-    (this.stopKeepaliveInterval(),
-      (this.keepaliveInterval = setInterval(() => {
-        if (this.state === "connected" && this.ws)
-          try {
-            (this.ws.send(
-              F1({ type: "keep_alive" }) +
-                `
-`,
-            ),
-              I("WebSocketTransport: Sent keep_alive (interval)"));
-          } catch {}
-      }, gOz)));
-  }
-  stopKeepaliveInterval() {
-    if (this.keepaliveInterval)
-      (clearInterval(this.keepaliveInterval), (this.keepaliveInterval = null));
   }
 }

@@@ function 'SG6' (was 'JP6') — structural (85.2%)
--- pretty-v2.1.31.js:434910
+++ pretty-v2.1.32.js:434809
@@ -10,6 +10,11 @@
       n("tengu_prompt_suggestion_init", { enabled: !0, source: "env" }),
       !0
     );
+  if (!x8("tengu_chomp_inflection", !0))
+    return (
+      c("tengu_prompt_suggestion_init", { enabled: !1, source: "growthbook" }),
+      !1
+    );
   if (_4())
     return (
       n("tengu_prompt_suggestion_init", {

@@@ function 'ER' (was '$R') — structural (85.2%)
--- pretty-v2.1.31.js:518332
+++ pretty-v2.1.32.js:518059
@@ -10,6 +10,7 @@
       tags: w,
       agentNames: H,
       agentColors: O,
+      agentSettings: $,
       prNumbers: $,
       prUrls: _,
       prRepositories: J,
@@ -40,6 +41,7 @@
       tag: f ? w.get(f) : A.tag,
       agentName: f ? H.get(f) : A.agentName,
       agentColor: f ? O.get(f) : A.agentColor,
+      agentSetting: Z ? $.get(Z) : A.agentSetting,
       mode: f ? X.get(f) : A.mode,
       prNumber: f ? $.get(f) : A.prNumber,
       prUrl: f ? _.get(f) : A.prUrl,

@@@ function 'rF1' (was 'sj6') — structural (85.1%)
--- pretty-v2.1.31.js:399095
+++ pretty-v2.1.32.js:398734
@@ -10,7 +10,7 @@
             O = E31(H, "SKILL.md");
           try {
             let $ = K.readFileSync(O, { encoding: "utf-8" }),
-              { frontmatter: _, content: J } = z0($),
+              { frontmatter: _, content: J } = H0($, O),
               X = w.name,
               D = _.description ?? IU(J, "Skill"),
               j = RS(_["allowed-tools"]),

@@@ function 'DAz' (was 'teY') — structural (84.9%)
--- pretty-v2.1.31.js:501754
+++ pretty-v2.1.32.js:501361
@@ -11,5 +11,8 @@
     w = "",
     H = z.data;
   if (H.type === "text") w = H.file.content;
-  return { memoryPath: Y, currentMemory: w };
+  return (
+    c("tengu_session_memory_file_read", { content_length: w.length }),
+    { memoryPath: Y, currentMemory: w }
+  );
 }

@@@ function 'hx4' (was 'UI4') — structural (84.9%)
--- pretty-v2.1.31.js:390333
+++ pretty-v2.1.32.js:389870
@@ -28,7 +28,11 @@
           null,
           w ?? "Running in the background",
           " ",
-          D5.createElement(_A, { shortcut: "↓", action: "manage", parens: !0 }),
+          _5.createElement(YA, {
+            shortcut: "shift+↑",
+            action: "manage",
+            parens: !0,
+          }),
         );
       return "Done";
     }),
@@ -56,14 +60,13 @@
             D5.createElement(
               D5.Fragment,
               null,
-              " ",
+              " (",
               D5.createElement(
                 Z,
                 { backgroundColor: z, color: z ? "inverseText" : void 0 },
-                "(",
                 Y,
-                ")",
               ),
+              ")",
             ),
         )),
       (q[5] = K),

@@@ variable 'pO1' (was 'SO1') — structural (84.7%)
--- pretty-v2.1.31.js:138342
+++ pretty-v2.1.32.js:138226
@@ -53,5 +53,11 @@
       bedrock: "us.anthropic.claude-opus-4-5-20251101-v1:0",
       vertex: "claude-opus-4-5@20251101",
       foundry: "claude-opus-4-5",
+    }),
+    (gA1 = {
+      firstParty: "claude-opus-4-6",
+      bedrock: "us.anthropic.claude-opus-4-6-v1",
+      vertex: "claude-opus-4-6",
+      foundry: "claude-opus-4-6",
     }));
 });

@@@ variable 'MKq' (was 'i4q') — structural (84.5%)
--- pretty-v2.1.31.js:484466
+++ pretty-v2.1.32.js:484169
@@ -12,6 +12,7 @@
   Q4();
   RIA();
   uA();
+  FA();
   ((P7 = o(J1(), 1)),
     (YaY = {
       id: "large-memory-files",
@@ -211,27 +212,27 @@
       },
     }),
     (_aY = {
-      id: "opus-4.5-available",
+      id: "opus-4.6-available",
       type: "info",
-      isActive: (A) => A.showOpus45Notice === !0,
+      isActive: (A) => A.showOpus46Notice === !0,
       render: () => {
         let q = H4() !== "firstParty",
           K = vK(),
           Y = K === "max",
           z = K === "team",
           w = K === "pro",
-          H = _5().toLowerCase().includes("opus-4-5"),
+          H = H5().toLowerCase().includes("opus-4-6"),
           O;
         if (Y || z || w || H)
-          O = P7.createElement(Z, { dimColor: !0 }, "Welcome to Opus 4.5");
+          O = V7.createElement(f, { dimColor: !0 }, "Welcome to Opus 4.6");
         else if (q)
           O = P7.createElement(
             Z,
             { dimColor: !0 },
-            "/model to try Opus 4.5. Note: you may need to request access from your cloud provider",
+            "/model to try Opus 4.6. Note: you may need to request access from your cloud provider",
           );
         else
-          O = P7.createElement(Z, { dimColor: !0 }, "/model to try Opus 4.5");
+          O = V7.createElement(f, { dimColor: !0 }, "/model to try Opus 4.6");
         return P7.createElement(h, { marginLeft: 1 }, O);
       },
     }),

@@@ variable 'lmA' (was 'XmA') — structural (84.3%)
--- pretty-v2.1.31.js:550174
+++ pretty-v2.1.32.js:550502
@@ -19,6 +19,8 @@
   hn();
   zM();
   Bt();
+  jU1();
+  pW();
   ((Owz = [
     {
       id: "new-user-warmup",
@@ -366,7 +368,11 @@
     {
       id: "guest-passes",
       content: async (A) => {
-        return `You have free guest passes to share · ${E8("claude", A.theme)("/passes")}`;
+        let q = v8("claude", A.theme),
+          K = nt();
+        return K
+          ? `Share Claude Code and earn ${q(it(K))} of extra usage · ${q("/passes")}`
+          : `You have free guest passes to share · ${q("/passes")}`;
       },
       cooldownSessions: 3,
       isRelevant: async () => {
@@ -375,6 +381,14 @@
         return q;
       },
     },
+    {
+      id: "overage-promo",
+      content: async (A) => {
+        return `${v8("claude", A.theme)("$50 free extra usage")} · /extra-usage to enable`;
+      },
+      cooldownSessions: 3,
+      isRelevant: async () => DU1(),
+    },
   ]),
     ($wz = []));
 });

@@@ function 'Tg1' (was 'tQ1') — structural (84.1%)
--- pretty-v2.1.31.js:437669
+++ pretty-v2.1.32.js:437599
@@ -2,6 +2,7 @@
   try {
     let q = A.map(oIY),
       K = KW6(q),
+      Y = TW6(K),
       Y = YW6(K);
     if (Y[Y.length - 1]?.type === "user") Y.push(vL({ content: lq1 }));
     return Y;

@@@ function 'h5z' (was 'PKz') — structural (83.8%)
--- pretty-v2.1.31.js:523772
+++ pretty-v2.1.32.js:523529
@@ -23,5 +23,11 @@
       let H = Tp1.resolve(w);
       (await A.stat(H), q.push(H));
     } catch {}
+  for (let H of v11()) {
+    let O = G91.join(H, ".claude", "skills");
+    try {
+      (await A.stat(O), q.push(O));
+    } catch {}
+  }
   return q;
 }

@@@ variable 'fg1' (was 'oQ1') — structural (83.7%)
--- pretty-v2.1.31.js:434878
+++ pretty-v2.1.32.js:434774
@@ -16,6 +16,8 @@
   zP6();
   zM();
   fP1();
+  hG1();
+  fM();
   ((EIY = new Set(["Edit", "Write", "NotebookEdit"])),
     (kIY = new Set([
       "Read",

@@@ function 'uP6' (was 'GG6') — structural (83.7%)
--- pretty-v2.1.31.js:448461
+++ pretty-v2.1.32.js:448414
@@ -12,7 +12,7 @@
   }
   let A = _5(),
     q = K86(A) !== null,
-    K = QN7() || q ? w27(A) : "Claude Opus 4.5",
+    K = Bi7() || q ? g27(A) : "Claude Opus 4.6",
     Y = `\uD83E\uDD16 Generated with [Claude Code](${mN7})`,
     z = `Co-Authored-By: ${K} <noreply@anthropic.com>`,
     w = Lq();

@@@ function 'Wx4' (was 'RI4') — structural (83.6%)
--- pretty-v2.1.31.js:388624
+++ pretty-v2.1.32.js:387985
@@ -1,9 +1,13 @@
-function RI4({ attachment: A, addMargin: q, verbose: K }) {
+function Wx4({ attachment: A, addMargin: q, verbose: K, isTranscriptMode: Y }) {
   let Y = T6((z) => z.tasks);
   if (U8() && A.type === "teammate_mailbox") {
     let z = A.messages.filter((w) => {
+      if (XZ(H.text)) return !1;
       try {
-        return OA(w.text)?.type !== "idle_notification";
+        let O = JA(H.text);
+        return (
+          O?.type !== "idle_notification" && O?.type !== "teammate_terminated"
+        );
       } catch {
         return !0;
       }
@@ -36,20 +40,6 @@
         let $ = Yj6(w.text, w.from);
         if ($)
           return $4.default.createElement($4.default.Fragment, { key: H }, $);
-        let _ = qZ(w.text);
-        if (_) {
-          let D = WJ(w.color);
-          return $4.default.createElement(
-            h,
-            { key: H, marginTop: 1 },
-            $4.default.createElement(
-              Z,
-              { color: D },
-              `@${w.from}${d1.pointer}`,
-            ),
-            $4.default.createElement(Z, null, ` ${_.from} is now exiting.`),
-          );
-        }
         let J = WJ(w.color),
           X = XI4(w.text) ?? w.text;
         return $4.default.createElement(JWY, {
@@ -58,6 +48,7 @@
           inkColor: J,
           content: X,
           summary: w.summary,
+          isTranscriptMode: Y,
         });
       }),
     );
@@ -283,6 +274,7 @@
       );
     }
     case "task_status": {
+      if (h9() && A.status === "killed") return null;
       if (U8()) {
         let w = Y[A.taskId];
         if (
@@ -312,7 +304,12 @@
           );
         }
       }
-      let z = A.status === "completed" ? "completed in background" : A.status;
+      let w =
+        A.status === "completed"
+          ? "completed in background"
+          : A.status === "killed"
+            ? "stopped"
+            : A.status;
       return $4.default.createElement(
         h,
         { flexDirection: "row", width: "100%", marginTop: 1 },

@@@ variable 'MX' (was 'fX') — structural (83.5%)
--- pretty-v2.1.31.js:514821
+++ pretty-v2.1.32.js:514496
@@ -12,10 +12,7 @@
           decisionReason: { type: "mode", mode: "dontAsk" },
           message: bzq(A.name),
         };
-      if (
-        (H.toolPermissionContext.mode,
-        H.toolPermissionContext.shouldAvoidPermissionPrompts)
-      )
+      if (H.toolPermissionContext.shouldAvoidPermissionPrompts)
         return {
           behavior: "deny",
           decisionReason: {

@@@ function 'J6q' (was 'K1q') — structural (83.5%)
--- pretty-v2.1.31.js:459854
+++ pretty-v2.1.32.js:459720
@@ -3,7 +3,7 @@
     { effort: K } = A,
     Y;
   if (q[0] === Symbol.for("react.memo_cache_sentinel"))
-    ((Y = ["low", "medium", "high", "max"]), (q[0] = Y));
+    ((Y = ["low", "medium", "high"]), (q[0] = Y));
   else Y = q[0];
   let z = Y,
     w = K ? z.indexOf(K) + 1 : 0,

@@@ variable 'LeY' (was 'YKq') — structural (83.5%)
--- pretty-v2.1.31.js:489082
+++ pretty-v2.1.32.js:488869
@@ -1,95 +1,53 @@
-var YKq = E(() => {
-  p1();
-  R7();
-  B3();
-  u1();
-  q2();
-  yf6();
-  zK();
-  yq();
-  QS();
-  Aq();
-  Ap();
-  gIA();
-  rz();
-  vG1();
-  s6();
-  hf6();
-  N6();
-  q5 = o(J1(), 1);
-  ((GsY = {
-    type: "local-jsx",
-    name: "resume",
-    description: "Resume a conversation",
-    get argumentHint() {
-      return Km() ? "[session-id or title]" : "[session-id]";
-    },
-    isEnabled: () => !0,
-    isHidden: !1,
-    async call(A, q, K) {
-      U4("resume");
-      let Y = async (_, J, X) => {
-          try {
-            (await q.resume?.(_, J, X), A(void 0, { display: "skip" }));
-          } catch (D) {
-            (e(D), A(`Failed to resume: ${D.message}`));
-          }
-        },
-        z = K?.trim();
-      if (!z)
+  LeY = async (A, q, K) => {
+    B4("resume");
+    let Y = async (_, J, X) => {
+        try {
+          (await q.resume?.(_, J, X), A(void 0, { display: "skip" }));
+        } catch (D) {
+          (K1(D), A(`Failed to resume: ${D.message}`));
+        }
+      },
+      z = K?.trim();
+    if (!z)
+      return s3.createElement(keY, { key: Date.now(), onDone: A, onResume: Y });
+    let w = await Gm(N8()),
+      H = await Hp1(w);
+    if (H.length === 0)
+      return s3.createElement(NxA, {
+        message: "No conversations found to resume.",
+        args: z,
+        onDone: () => A("No conversations found to resume."),
+      });
+    let O = aS(z);
+    if (O) {
+      let _ = H.filter((J) => Xw(J) === O).sort(
+        (J, X) => X.modified.getTime() - J.modified.getTime(),
+      );
+      if (_.length > 0) {
+        let J = _[0],
+          X = Bv(J) ? await ER(J) : J;
+        return (Y(O, X, "slash_command_session_id"), null);
+      }
+    }
+    if (md()) {
+      let _ = await Pm(z, { exact: !0 });
+      if (_.length === 1) {
+        let J = _[0],
+          X = Xw(J);
+        if (X) {
+          let D = Bv(J) ? await ER(J) : J;
+          return (Y(X, D, "slash_command_title"), null);
+        }
+      }
+      if (_.length > 1) {
+        let J = E3q({ resultType: "multipleMatches", arg: z, count: _.length });
         return q5.createElement(PsY, {
-          key: Date.now(),
-          onDone: A,
-          onResume: Y,
-        });
-      let w = await qm(M8()),
-        H = await uU1(w);
-      if (H.length === 0)
-        return q5.createElement(dIA, {
-          message: "No conversations found to resume.",
+          message: J,
           args: z,
-          onDone: () => A("No conversations found to resume."),
+          onDone: () => A(J),
         });
-      let O = oT(z);
-      if (O) {
-        let _ = H.filter((J) => Yw(J) === O).sort(
-          (J, X) => X.modified.getTime() - J.modified.getTime(),
-        );
-        if (_.length > 0) {
-          let J = _[0],
-            X = Tv(J) ? await $R(J) : J;
-          return (Y(O, X, "slash_command_session_id"), null);
-        }
       }
-      if (Km()) {
-        let _ = await Ym(z, { exact: !0 });
-        if (_.length === 1) {
-          let J = _[0],
-            X = Yw(J);
-          if (X) {
-            let D = Tv(J) ? await $R(J) : J;
-            return (Y(X, D, "slash_command_title"), null);
-          }
-        }
-        if (_.length > 1) {
-          let J = qKq({
-            resultType: "multipleMatches",
-            arg: z,
-            count: _.length,
-          });
-          return q5.createElement(dIA, {
-            message: J,
-            args: z,
-            onDone: () => A(J),
-          });
-        }
-      }
-      let $ = qKq({ resultType: "sessionNotFound", arg: z });
-      return q5.createElement(dIA, { message: $, args: z, onDone: () => A($) });
-    },
-    userFacingName() {
-      return "resume";
-    },
-  }),
-    (KKq = GsY));
-});
+    }
+    let $ = E3q({ resultType: "sessionNotFound", arg: z });
+    return s3.createElement(NxA, { message: $, args: z, onDone: () => A($) });
+  };

@@@ variable 'LF1' (was 'HF1') — structural (83.3%)
--- pretty-v2.1.31.js:380717
+++ pretty-v2.1.32.js:380382
@@ -19,6 +19,8 @@
       },
       isHidden: !1,
       async call(A, q) {
+        if (!M6().hasVisitedExtraUsage)
+          OA(($) => ({ ...$, hasVisitedExtraUsage: !0 }));
         let K = vK(),
           Y = K === "team" || K === "enterprise",
           z = gu(),

@@@ variable 'qG' (was 'gW') — structural (83.3%)
--- pretty-v2.1.31.js:440190
+++ pretty-v2.1.32.js:440131
@@ -44,6 +44,8 @@
   Nz();
   wv();
   EO();
+  Zv();
+  uO();
   ((CP6 = { TURNS_SINCE_WRITE: 10, TURNS_BETWEEN_REMINDERS: 10 }),
     (Sr4 = {
       TURNS_BETWEEN_ATTACHMENTS: 5,

@@@ function 'Kwq' (was 'jzq') — structural (83.3%)
--- pretty-v2.1.31.js:512645
+++ pretty-v2.1.32.js:512310
@@ -1,5 +1,6 @@
 function jzq(A) {
-  if (A.includes("claude-opus-4-5")) return "May 2025";
+  if (A.includes("claude-opus-4-6")) return "May 2025";
+  else if (A.includes("claude-opus-4-5")) return "May 2025";
   else if (A.includes("claude-haiku-4")) return "February 2025";
   else if (
     A.includes("claude-opus-4") ||

@@@ function 'XKz' (was 'a7z') — structural (83.3%)
--- pretty-v2.1.31.js:518990
+++ pretty-v2.1.32.js:518741
@@ -10,6 +10,7 @@
       teamName: K.teamName,
       customTitle: K.customTitle,
       tag: K.tag,
+      agentSetting: K.agentSetting,
       prNumber: K.prNumber,
       prUrl: K.prUrl,
       prRepository: K.prRepository,

@@@ function 'pYq' (was 'w9q') — structural (83.2%)
--- pretty-v2.1.31.js:501892
+++ pretty-v2.1.32.js:501502
@@ -100,7 +100,9 @@
           yK.createElement(
             Z,
             { bold: !0, color: "permission" },
-            "Network Restrictions:",
+            "Network Restrictions",
+            Ly1() ? " (Managed)" : "",
+            ":",
           ),
           O.allowedHosts &&
             O.allowedHosts.length > 0 &&

@@@ variable 'Pz' (was 'Fz') — structural (83.1%)
--- pretty-v2.1.31.js:28128
+++ pretty-v2.1.32.js:28165
@@ -43,5 +43,10 @@
       OAUTH_FILE_SUFFIX: "-local-oauth",
       MCP_PROXY_URL: "http://localhost:8205",
       MCP_PROXY_PATH: "/v1/toolbox/shttp/mcp/{server_id}",
-    }));
+    }),
+    (z4K = [
+      "https://beacon.claude-ai.staging.ant.dev",
+      "https://claude.fedstart.com",
+      "https://claude-staging.fedstart.com",
+    ]));
 });

@@@ function 'YNA' (was 'kVA') — structural (83.1%)
--- pretty-v2.1.31.js:519638
+++ pretty-v2.1.32.js:519393
@@ -1,4 +1,5 @@
 function kVA(A, q) {
+  let K = zZ1(A);
   if (W2q(A))
     return {
       behavior: "allow",

@@@ class 'KTq' (was 'ZVq') — structural (82.9%)
--- pretty-v2.1.31.js:560869
+++ pretty-v2.1.32.js:560983
@@ -196,9 +196,9 @@
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.31",
+          VERSION: "2.1.32",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-02-04T00:00:54Z",
+          BUILD_TIME: "2026-02-05T17:02:01Z",
         }.VERSION,
         output_style: a,
         agents: N.map((K6) => K6.agentType),
@@ -239,7 +239,14 @@
               },
             });
       }
-      if (y) await ph(j1);
+      if (y) {
+        if (
+          (await KI(w1),
+          $6(process.env.CLAUDE_CODE_EAGER_FLUSH) ||
+            $6(process.env.CLAUDE_CODE_IS_COWORK))
+        )
+          await Rt();
+      }
       yield {
         type: "result",
         subtype: "success",
@@ -336,6 +343,13 @@
           )
             S1 = K6.attachment.data;
           else if (K6.attachment.type === "max_turns_reached") {
+            if (y) {
+              if (
+                $6(process.env.CLAUDE_CODE_EAGER_FLUSH) ||
+                $6(process.env.CLAUDE_CODE_IS_COWORK)
+              )
+                await Rt();
+            }
             yield {
               type: "result",
               subtype: "error_max_turns",
@@ -392,6 +406,13 @@
           break;
       }
       if (_ !== void 0 && d0() >= _) {
+        if (y) {
+          if (
+            $6(process.env.CLAUDE_CODE_EAGER_FLUSH) ||
+            $6(process.env.CLAUDE_CODE_IS_COWORK)
+          )
+            await Rt();
+        }
         yield {
           type: "result",
           subtype: "error_max_budget_usd",
@@ -414,6 +435,13 @@
         let VA = ubA(this.mutableMessages, M0) - U1,
           t1 = parseInt(process.env.MAX_STRUCTURED_OUTPUT_RETRIES || "5", 10);
         if (VA >= t1) {
+          if (y) {
+            if (
+              $6(process.env.CLAUDE_CODE_EAGER_FLUSH) ||
+              $6(process.env.CLAUDE_CODE_IS_COWORK)
+            )
+              await Rt();
+          }
           yield {
             type: "result",
             subtype: "error_max_structured_output_retries",
@@ -437,6 +465,13 @@
       }
     }
     let Y6 = tM(j1);
+    if (y) {
+      if (
+        $6(process.env.CLAUDE_CODE_EAGER_FLUSH) ||
+        $6(process.env.CLAUDE_CODE_IS_COWORK)
+      )
+        await Rt();
+    }
     if (!xn4(Y6)) {
       yield {
         type: "result",

@@@ function 'jyA' (was 'dRA') — structural (82.8%)
--- pretty-v2.1.31.js:434473
+++ pretty-v2.1.32.js:434370
@@ -132,15 +132,14 @@
               },
             };
         }
-        if (
-          M.name === "Bash" &&
-          "command" in W &&
-          typeof W.command === "string"
-        ) {
-          let V = W.command;
-          if (KP6({ command: V }, _P6(V)).behavior !== "allow")
+        if (M.name === "Bash") {
+          let Z =
+            "command" in W && typeof W.command === "string" ? W.command : "";
+          if (!Z || TG6({ command: Z }, CG6(Z)).behavior !== "allow")
             return (
-              I(`[Speculation] Stopping at bash: ${V.slice(0, 50)}...`),
+              h(
+                `[Speculation] Stopping at bash: ${Z.slice(0, 50) || "missing command"}`,
+              ),
               ZP1(K, () => ({
                 boundary: { type: "bash", command: V, completedAt: Date.now() },
               })),

@@@ variable 'fd4' (was 'Rp4') — structural (82.3%)
--- pretty-v2.1.31.js:420603
+++ pretty-v2.1.32.js:420164
@@ -47,7 +47,7 @@
       renderToolResultMessage: kp4,
       async call() {
         let A = OG(),
-          q = JD(A),
+          q = $D(A).filter((z) => !z.metadata?._internal),
           K = new Set(
             q.filter((z) => z.status === "completed").map((z) => z.id),
           );

@@@ function 'OKz' (was 'i7z') — structural (82.3%)
--- pretty-v2.1.31.js:518752
+++ pretty-v2.1.32.js:518499
@@ -6,6 +6,7 @@
     tags: w,
     agentNames: H,
     agentColors: O,
+    agentSettings: $,
     prNumbers: $,
     prUrls: _,
     prRepositories: J,
@@ -46,6 +47,7 @@
       tag: w.get(T),
       agentName: H.get(T),
       agentColor: O.get(T),
+      agentSetting: $.get(k),
       mode: X.get(T),
       prNumber: $.get(T),
       prUrl: _.get(T),

@@@ function 'Ju1' (was 'cb1') — structural (82.2%)
--- pretty-v2.1.31.js:295594
+++ pretty-v2.1.32.js:297433
@@ -1,5 +1,6 @@
 function cb1(A) {
-  let q = Oa(l34(), ".claude", "agent-memory") + pD1,
+  let q = Yc9(A),
+    K = Va(_94(), ".claude", "agent-memory") + Jj1,
     K = Oa(y6(), ".claude", "agent-memory") + pD1,
     Y = Oa(y6(), ".claude", "agent-memory-local") + pD1;
   return A.startsWith(q) || A.startsWith(K) || A.startsWith(Y);

@@@ variable 'qvq' (was 'GNq') — structural (82.2%)
--- pretty-v2.1.31.js:568212
+++ pretty-v2.1.32.js:568410
@@ -185,7 +185,6 @@
   _Nq();
   iD();
   Gp1();
-  QP();
   XK = o(J1(), 1);
   Wq("main_tsx_entry");
   Wq("main_tsx_imports_loaded");

@@@ variable 'Lh' (was 'Mh') — structural (81.9%)
--- pretty-v2.1.31.js:368701
+++ pretty-v2.1.32.js:368382
@@ -51,9 +51,9 @@
                 : q === "failed"
                   ? "error"
                   : q === "killed"
-                    ? "error"
+                    ? "warning"
                     : "inactive",
-          O = q;
+          O = q === "killed" ? "stopped" : q;
         if (q === "running" && w) O = "idle";
         else if (q === "running" && z) O = "awaiting approval";
         let $ = Y ? ` (${Y.toolUseCount} tools, ${Y.tokenCount} tokens)` : "";

@@@ variable 'Ez' (was 'q2') — structural (81.8%)
--- pretty-v2.1.31.js:369595
+++ pretty-v2.1.32.js:369259
@@ -25,6 +25,7 @@
   ZNA();
   n_();
   u1();
+  u1();
   ((e8 = o(J1(), 1)),
     (Hv = o(J1(), 1)),
     (JL4 = tB1()),

@@@ function 'X91' (was 'K91') — structural (81.4%)
--- pretty-v2.1.31.js:518413
+++ pretty-v2.1.32.js:518142
@@ -10,6 +10,7 @@
     _ = new Map(),
     J = new Map(),
     X = new Map(),
+    D = new Map(),
     D = new Map();
   try {
     let f = await q2q(A),
@@ -35,6 +36,8 @@
         w.set(N.sessionId, N.agentName);
       else if (N.type === "agent-color" && N.sessionId)
         H.set(N.sessionId, N.agentColor);
+      else if (T.type === "agent-setting" && T.sessionId)
+        O.set(T.sessionId, T.agentSetting);
       else if (N.type === "mode" && N.sessionId) J.set(N.sessionId, N.mode);
       else if (N.type === "pr-link" && N.sessionId)
         (O.set(N.sessionId, N.prNumber),
@@ -71,6 +74,7 @@
     tags: z,
     agentNames: w,
     agentColors: H,
+    agentSettings: O,
     prNumbers: O,
     prUrls: $,
     prRepositories: _,

@@@ function 'GDq' (was 'LXq') — structural (81.4%)
--- pretty-v2.1.31.js:546267
+++ pretty-v2.1.32.js:546563
@@ -13,8 +13,11 @@
     (($.current = O),
       z((X) => {
         let j = CN6(X.tasks).length;
-        if (j === 0 && J > 0 && X.selectedIPAgentIndex !== -1)
+        if (j === 0 && J > 0 && X.selectedIPAgentIndex !== -1) {
+          if (X.viewSelectionMode === "viewing-agent")
+            return { ...X, selectedIPAgentIndex: -1 };
           return { ...X, selectedIPAgentIndex: -1, viewSelectionMode: "none" };
+        }
         let M = X.showSpinnerTree ? j : j - 1;
         if (j > 0 && X.selectedIPAgentIndex > M)
           return { ...X, selectedIPAgentIndex: M };
@@ -32,9 +35,12 @@
       let D = K;
       if (D) {
         let j = A[D];
-        if (HJ(j) && j.status === "running")
+        if (h$(j) && j.status === "running") {
           j.currentWorkAbortController?.abort();
+          return;
+        }
       }
+      jI(z);
       return;
     }
     if (X.escape && q === "selecting-agent") {

@@@ function 'wR4' (was '$L4') — structural (81.4%)
--- pretty-v2.1.31.js:368917
+++ pretty-v2.1.32.js:368599
@@ -1,7 +1,6 @@
 function $L4({
   teammate: A,
   isLast: q,
-  frame: K,
   isSelected: Y,
   isForegrounded: z,
   allIdle: w,
@@ -69,15 +68,9 @@
       }
       if (_) return null;
       return g3.createElement(
-        g3.Fragment,
         null,
-        K !== void 0 &&
-          g3.createElement(Zp, { frame: K, messageColor: "claude" }),
-        g3.createElement(
-          Z,
-          { color: "claude" },
-          O1?.endsWith("…") ? O1 : `${O1}…`,
-        ),
+        { dimColor: !0 },
+        H1?.endsWith("…") ? H1 : `${H1}…`,
       );
     },
     w1 = H ? pXY(A.messages) : [],
@@ -97,7 +90,7 @@
       x &&
         g3.createElement(
           Z,
-          { bold: !0, color: Y ? "suggestion" : X },
+          { color: K ? "suggestion" : J },
           "@",
           A.identity.agentName,
         ),
@@ -117,7 +110,7 @@
           pK(T),
           " tokens",
         ),
-      q1 && g3.createElement(Z, null, " · ", Fm1),
+      r && x9.createElement(f, { dimColor: !0 }, " · ", zF1),
       c && g3.createElement(Z, { dimColor: !0 }, " · enter to view"),
     ),
     w1.map((j1, L1) =>

@@@ function 'X6q' (was 'Y1q') — structural (81.4%)
--- pretty-v2.1.31.js:459881
+++ pretty-v2.1.32.js:459747
@@ -1,5 +1,5 @@
 function Y1q(A, q) {
-  let K = ["low", "medium", "high", "max"],
+  let K = ["low", "medium", "high"],
     Y = K.indexOf(A);
   if (q === "right") return K[(Y + 1) % K.length];
   else return K[(Y - 1 + K.length) % K.length];

@@@ function 'aVq' (was 'Dfq') — structural (81.1%)
--- pretty-v2.1.31.js:558556
+++ pretty-v2.1.32.js:558713
@@ -6,6 +6,7 @@
   dynamicMcpConfig: z,
   mcpCliEndpoint: w,
   debug: H,
+  mainThreadAgentDefinition: O,
   strictMcpConfig: O = !1,
   systemPrompt: $,
   appendSystemPrompt: _,
@@ -16,6 +17,7 @@
   filterByPr: M,
 }) {
   let { rows: W } = A8(),
+    P = T6((t) => t.agentDefinitions),
     P = h7(),
     [G, f] = cY.default.useState([]),
     [V, N] = cY.default.useState(!0),
@@ -28,8 +30,7 @@
       let A1 = G.filter((O1) => !O1.isSidechain);
       if (M !== void 0) {
         if (M === !0) A1 = A1.filter((O1) => O1.prNumber !== void 0);
-        else if (typeof M === "number")
-          A1 = A1.filter((O1) => O1.prNumber === M);
+        else if (typeof W === "number") t = t.filter((e) => e.prNumber === W);
         else if (typeof M === "string") {
           let O1 = $Oz(M);
           if (O1 !== null) A1 = A1.filter((s) => s.prNumber === O1);
@@ -98,6 +99,19 @@
         if (Xs()) lG1();
         (await Cv(), ML1(s.sessionId));
       }
+      let w1 = O;
+      if (!O && G1.agentSetting) {
+        let E1 = P?.activeAgents.find((q1) => q1.agentType === G1.agentSetting);
+        if (E1) {
+          if (
+            ((w1 = E1),
+            fy(E1.agentType),
+            V((q1) => ({ ...q1, agent: E1.agentType })),
+            !zf() && E1.model && E1.model !== "inherit")
+          )
+            rG(s9(E1.model));
+        }
+      }
       let w1 = ip1(s.agentName, s.agentColor);
       if (w1) P((Z1) => ({ ...Z1, standaloneAgentContext: w1 }));
       (f([]),
@@ -106,6 +120,7 @@
           fileHistorySnapshots: s.fileHistorySnapshots,
           agentName: s.agentName,
           agentColor: s.agentColor,
+          mainThreadAgentDefinition: w1,
         }));
     } catch (s) {
       throw (e(s), s);
@@ -127,6 +142,7 @@
       strictMcpConfig: O,
       systemPrompt: $,
       appendSystemPrompt: _,
+      mainThreadAgentDefinition: b.mainThreadAgentDefinition,
       disableSlashCommands: X,
       taskListId: j,
     });

@@@ function 'S86' (was 'K86') — structural (81.1%)
--- pretty-v2.1.31.js:147314
+++ pretty-v2.1.32.js:147262
@@ -1,5 +1,9 @@
 function K86(A) {
   switch (A) {
+    case XH().opus46:
+      return "Opus 4.6";
+    case XH().opus46 + "[1m]":
+      return "Opus 4.6 (1M context)";
     case j$().opus45:
       return "Opus 4.5";
     case j$().opus41:

@@@ function 'vwq' (was 'uzq') — structural (80.6%)
--- pretty-v2.1.31.js:514881
+++ pretty-v2.1.32.js:514553
@@ -1,8 +1,4 @@
-function uzq({
-  permissionModeCli: A,
-  dangerouslySkipPermissions: q,
-  dangerouslySkipPermissionsWithClassifiers: K,
-}) {
+function vwq({ permissionModeCli: A, dangerouslySkipPermissions: q, ...K }) {
   let Y = P8() || {},
     z = aY("tengu_disable_bypass_permissions_mode"),
     w = Y.permissions?.disableBypassPermissionsMode === "disable",
@@ -12,6 +8,7 @@
   if (q) O.push("bypassPermissions");
   if (A) O.push(Ny(A));
   if (Y.permissions?.defaultMode) O.push(Y.permissions.defaultMode);
+  let _;
   for (let _ of O) {
     if (_ === "bypassPermissions" && H) {
       if (z)
@@ -31,7 +28,9 @@
       });
       continue;
     }
-    return { mode: _, notification: $ };
+    _ = { mode: J, notification: $ };
+    break;
   }
-  return { mode: "default", notification: $ };
+  if (!_) _ = { mode: "default", notification: $ };
+  return _;
 }

@@@ function 'hXY' (was 'G_Y') — structural (80.6%)
--- pretty-v2.1.31.js:358692
+++ pretty-v2.1.32.js:359056
@@ -2,7 +2,7 @@
   let { fullyUnquotedContent: q } = A;
   if (!/[\n\r]/.test(q))
     return { behavior: "passthrough", message: "No newlines" };
-  if (/[\n\r]\s*[a-zA-Z/.~]/.test(q))
+  if (/[\n\r]\s*[a-zA-Z/.~({$![>|]/.test(q))
     return (
       n("tengu_bash_security_check_triggered", {
         checkId: GH.NEWLINES,

@@@ function 'gxY' (was 'lhY') — structural (80.5%)
--- pretty-v2.1.31.js:431438
+++ pretty-v2.1.32.js:431171
@@ -208,12 +208,22 @@
       }));
     let B = V.message;
     if (W && !B) B = `Execution stopped by PreToolUse hook${P ? `: ${P}` : ""}`;
+    let S = [{ type: "tool_result", content: u, is_error: !0, tool_use_id: q }],
+      m = Z.behavior === "ask" ? Z.contentBlocks : void 0;
+    if (m?.length) S.push(...m);
+    let b;
+    if (m?.length) {
+      let U = m.filter((g) => g.type === "image").length;
+      if (U > 0) {
+        let g = Nr4(Y.messages);
+        b = Array.from({ length: U }, (x, p) => g + p);
+      }
+    }
     return (
       j.push({
         message: p6({
-          content: [
-            { type: "tool_result", content: B, is_error: !0, tool_use_id: q },
-          ],
+          content: S,
+          imagePasteIds: b,
           toolUseResult: `Error: ${B}`,
           sourceToolAssistantUUID: w.uuid,
         }),
@@ -362,9 +372,20 @@
       let $1 = [await yH6(A, q1, q)];
       if ("acceptFeedback" in V && V.acceptFeedback)
         $1.push({ type: "text", text: V.acceptFeedback });
+      let H1 = "contentBlocks" in Z ? Z.contentBlocks : void 0;
+      if (H1?.length) Z1.push(...H1);
+      let D1;
+      if (H1?.length) {
+        let t = H1.filter((e) => e.type === "image").length;
+        if (t > 0) {
+          let e = Nr4(Y.messages);
+          D1 = Array.from({ length: t }, (G1, w1) => e + w1);
+        }
+      }
       j.push({
         message: p6({
           content: $1,
+          imagePasteIds: D1,
           toolUseResult: Y.agentId && !Y.preserveToolUseResults ? void 0 : q1,
           mcpMeta: Y.agentId ? void 0 : r,
           sourceToolAssistantUUID: w.uuid,

@@@ function 'phA' (was 'JhA') — structural (80.1%)
--- pretty-v2.1.31.js:472012
+++ pretty-v2.1.32.js:471714
@@ -1,6 +1,5 @@
 function JhA({ agentServer: A, onCancel: q, onComplete: K }) {
   let [Y] = M7(),
-    z = v7(),
     [w, H] = Lt.useState(!1),
     [O, $] = Lt.useState(null),
     [_, J] = Lt.useState(null),
@@ -88,136 +87,135 @@
   return (
     P.push({ label: "Back", value: "back" }),
     rK.default.createElement(
-      rK.default.Fragment,
       null,
+      {
+        title: `${M} MCP Server`,
+        subtitle: "agent-only",
+        onCancel: q,
+        inputGuide: (G) =>
+          G.pending
+            ? Q3.default.createElement(
+                f,
+                null,
+                "Press ",
+                G.keyName,
+                " again to exit",
+              )
+            : Q3.default.createElement(
+                pA,
+                null,
+                Q3.default.createElement(YA, {
+                  shortcut: "↑↓",
+                  action: "navigate",
+                }),
+                Q3.default.createElement(YA, {
+                  shortcut: "Enter",
+                  action: "confirm",
+                }),
+                Q3.default.createElement(NA, {
+                  action: "confirm:no",
+                  context: "Confirmation",
+                  fallback: "Esc",
+                  description: "go back",
+                }),
+              ),
+      },
       rK.default.createElement(
         h,
-        { flexDirection: "column", paddingX: 1, borderStyle: "round" },
+        { flexDirection: "column", gap: 0 },
         rK.default.createElement(
           h,
-          { marginBottom: 1 },
-          rK.default.createElement(Z, { bold: !0 }, W, " MCP Server"),
-          rK.default.createElement(Z, { dimColor: !0 }, " (agent-only)"),
-        ),
-        rK.default.createElement(
           h,
-          { flexDirection: "column", gap: 0 },
+          Q3.default.createElement(f, { bold: !0 }, "Type: "),
+          Q3.default.createElement(f, { dimColor: !0 }, A.transport),
+        ),
+        A.url &&
           rK.default.createElement(
             h,
             null,
             rK.default.createElement(Z, { bold: !0 }, "Type: "),
-            rK.default.createElement(Z, { dimColor: !0 }, A.transport),
+            Q3.default.createElement(f, { dimColor: !0 }, A.url),
           ),
-          A.url &&
-            rK.default.createElement(
-              h,
-              null,
-              rK.default.createElement(Z, { bold: !0 }, "URL: "),
-              rK.default.createElement(Z, { dimColor: !0 }, A.url),
-            ),
-          A.command &&
-            rK.default.createElement(
-              h,
-              null,
-              rK.default.createElement(Z, { bold: !0 }, "Command: "),
-              rK.default.createElement(Z, { dimColor: !0 }, A.command),
-            ),
+        A.command &&
           rK.default.createElement(
             h,
             null,
-            rK.default.createElement(Z, { bold: !0 }, "Used by: "),
-            rK.default.createElement(
-              Z,
-              { dimColor: !0 },
-              A.sourceAgents.join(", "),
-            ),
+            Q3.default.createElement(f, { bold: !0 }, "Command: "),
+            Q3.default.createElement(f, { dimColor: !0 }, A.command),
           ),
+        Q3.default.createElement(
+          I,
+          null,
+          Q3.default.createElement(f, { bold: !0 }, "Used by: "),
           rK.default.createElement(
             h,
-            { marginTop: 1 },
-            rK.default.createElement(Z, { bold: !0 }, "Status: "),
-            rK.default.createElement(
-              Z,
-              null,
-              E8("inactive", Y)(d1.radioOff),
-              " not connected (agent-only)",
-            ),
+            { dimColor: !0 },
+            A.sourceAgents.join(", "),
           ),
-          A.needsAuth &&
-            rK.default.createElement(
-              h,
-              null,
-              rK.default.createElement(Z, { bold: !0 }, "Auth: "),
-              A.isAuthenticated
-                ? rK.default.createElement(
-                    Z,
-                    null,
-                    E8("success", Y)(d1.tick),
-                    " authenticated",
-                  )
-                : rK.default.createElement(
-                    Z,
-                    null,
-                    E8("warning", Y)(d1.triangleUpOutline),
-                    " may need authentication",
-                  ),
-            ),
         ),
         rK.default.createElement(
           h,
           { marginTop: 1 },
+          Q3.default.createElement(f, { bold: !0 }, "Status: "),
           rK.default.createElement(
             Z,
-            { dimColor: !0 },
-            "This server connects only when running the agent.",
+            null,
+            v8("inactive", Y)(n1.radioOff),
+            " not connected (agent-only)",
           ),
         ),
-        O &&
+        A.needsAuth &&
           rK.default.createElement(
             h,
-            { marginTop: 1 },
-            rK.default.createElement(Z, { color: "error" }, "Error: ", O),
+            null,
+            Q3.default.createElement(f, { bold: !0 }, "Auth: "),
+            A.isAuthenticated
+              ? Q3.default.createElement(
+                  f,
+                  null,
+                  v8("success", Y)(n1.tick),
+                  " authenticated",
+                )
+              : Q3.default.createElement(
+                  f,
+                  null,
+                  v8("warning", Y)(n1.triangleUpOutline),
+                  " may need authentication",
+                ),
           ),
+      ),
+      Q3.default.createElement(
+        I,
+        null,
         rK.default.createElement(
           h,
-          { marginTop: 1 },
-          rK.default.createElement(ZA, {
-            options: P,
-            onChange: async (G) => {
-              switch (G) {
-                case "auth":
-                  await M();
-                  break;
-                case "back":
-                  q();
-                  break;
-              }
-            },
-            onCancel: q,
-          }),
+          { dimColor: !0 },
+          "This server connects only when running the agent.",
         ),
       ),
-      rK.default.createElement(
-        h,
-        { marginLeft: 3 },
+      H &&
         rK.default.createElement(
           Z,
-          { dimColor: !0 },
-          z.pending
-            ? rK.default.createElement(
-                rK.default.Fragment,
-                null,
-                "Press ",
-                z.keyName,
-                " again to exit",
-              )
-            : rK.default.createElement(kA, {
-                action: "confirm:no",
-                context: "Confirmation",
-                fallback: "Esc",
-                description: "go back",
-              }),
+          null,
+          Q3.default.createElement(f, { color: "error" }, "Error: ", H),
         ),
+      Q3.default.createElement(
+        I,
+        null,
+        Q3.default.createElement(ZA, {
+          options: W,
+          onChange: async (G) => {
+            switch (G) {
+              case "auth":
+                await j();
+                break;
+              case "back":
+                q();
+                break;
+            }
+          },
+          onCancel: q,
+        }),
       ),
     )
   );

@@@ function 'XOA' (was 'TjA') — structural (80.1%)
--- pretty-v2.1.31.js:299789
+++ pretty-v2.1.32.js:246101
@@ -135,6 +135,13 @@
       content: `${$J} (${q}): ${A.message}`,
       error: "invalid_request",
     });
+  if (A instanceof p4 && A.status === 404)
+    return zz({
+      content: X4()
+        ? `There's an issue with the selected model (${q}). It may not exist or you may not have access to it. Use --model to pick a different model.`
+        : `There's an issue with the selected model (${q}). It may not exist or you may not have access to it. Run /model to pick a different model.`,
+      error: "invalid_request",
+    });
   if (A instanceof Error)
     return vz({ content: `${$J}: ${A.message}`, error: "unknown" });
   return vz({ content: $J, error: "unknown" });

@@@ variable 'MG1' (was 'fQ1') — structural (80.0%)
--- pretty-v2.1.31.js:425553
+++ pretty-v2.1.32.js:425273
@@ -1,6 +1,7 @@
 var fQ1 = E(() => {
   tA();
   nz();
+  F6();
   ((ZQ1 = {
     minimumMessageTokensToInit: 1e4,
     minimumTokensBetweenUpdate: 5000,

@@@ variable 'zt' (was 'is') — structural (79.9%)
--- pretty-v2.1.31.js:448066
+++ pretty-v2.1.32.js:448021
@@ -22,38 +22,31 @@
   kF1();
   Qs();
   ((zCA = b.strictObject({
-    file_path: b
-      .string()
-      .describe(
-        "The absolute path to the file to write (must be absolute, not relative)",
-      ),
+    file_path: B.string().describe(
+      "The absolute path to the file to write (must be absolute, not relative)",
+    ),
     content: b.string().describe("The content to write to the file"),
   })),
     (EmY = b.object({
-      type: b
-        .enum(["create", "update"])
-        .describe(
-          "Whether a new file was created or an existing file was updated",
-        ),
+      type: B.enum(["create", "update"]).describe(
+        "Whether a new file was created or an existing file was updated",
+      ),
       filePath: b.string().describe("The path to the file that was written"),
       content: b.string().describe("The content that was written to the file"),
       structuredPatch: b.array(O3A).describe("Diff patch showing the changes"),
-      originalFile: b
-        .string()
+      originalFile: B.string()
         .nullable()
         .describe(
           "The original file content before the write (null for new files)",
         ),
-      gitDiff: b
-        .object({
-          filename: b.string(),
-          status: b.enum(["modified", "added"]),
-          additions: b.number(),
-          deletions: b.number(),
-          changes: b.number(),
-          patch: b.string(),
-        })
-        .optional(),
+      gitDiff: B.object({
+        filename: B.string(),
+        status: B.enum(["modified", "added"]),
+        additions: B.number(),
+        deletions: B.number(),
+        changes: B.number(),
+        patch: B.string(),
+      }).optional(),
     })),
     (wP = {
       name: m5,

@@@ variable 'TQ1' (was 'eF1') — structural (79.9%)
--- pretty-v2.1.31.js:417491
+++ pretty-v2.1.32.js:417126
@@ -9,80 +9,62 @@
   Fg4();
   lW1();
   bH();
-  s6();
   ((uvY = b.object({
     tool: b.enum(["Bash"]).describe("The tool this prompt applies to"),
-    prompt: b
-      .string()
-      .describe(
-        'Semantic description of the action, e.g. "run tests", "install dependencies"',
-      ),
+    prompt: B.string().describe(
+      'Semantic description of the action, e.g. "run tests", "install dependencies"',
+    ),
   })),
-    (Qg4 = b
-      .strictObject({
-        allowedPrompts: b
-          .array(uvY)
-          .optional()
-          .describe(
-            "Prompt-based permissions needed to implement the plan. These describe categories of actions rather than specific commands.",
-          ),
-        pushToRemote: b
-          .boolean()
-          .optional()
-          .describe("Whether to push the plan to a remote Claude.ai session"),
-        remoteSessionId: b
-          .string()
-          .optional()
-          .describe("The remote session ID if pushed to remote"),
-        remoteSessionUrl: b
-          .string()
-          .optional()
-          .describe("The remote session URL if pushed to remote"),
-        remoteSessionTitle: b
-          .string()
-          .optional()
-          .describe("The remote session title if pushed to remote"),
-      })
-      .passthrough()),
+    (hU4 = B.strictObject({
+      allowedPrompts: B.array(FkY)
+        .optional()
+        .describe(
+          "Prompt-based permissions needed to implement the plan. These describe categories of actions rather than specific commands.",
+        ),
+      pushToRemote: B.boolean()
+        .optional()
+        .describe("Whether to push the plan to a remote Claude.ai session"),
+      remoteSessionId: B.string()
+        .optional()
+        .describe("The remote session ID if pushed to remote"),
+      remoteSessionUrl: B.string()
+        .optional()
+        .describe("The remote session URL if pushed to remote"),
+      remoteSessionTitle: B.string()
+        .optional()
+        .describe("The remote session title if pushed to remote"),
+    }).passthrough()),
     (I6H = Qg4.extend({
-      plan: b
-        .string()
+      plan: B.string()
         .optional()
         .describe(
           "The plan content (injected by normalizeToolInput from disk)",
         ),
     })),
     (BvY = b.object({
-      plan: b
-        .string()
+      plan: B.string()
         .nullable()
         .describe("The plan that was presented to the user"),
       isAgent: b.boolean(),
-      filePath: b
-        .string()
+      filePath: B.string()
         .optional()
         .describe("The file path where the plan was saved"),
-      pushToRemote: b
-        .boolean()
+      pushToRemote: B.boolean()
         .optional()
         .describe("Whether the plan was pushed to a remote session"),
       remoteSessionId: b.string().optional().describe("The remote session ID"),
-      remoteSessionUrl: b
-        .string()
+      remoteSessionUrl: B.string()
         .optional()
         .describe("The remote session URL"),
-      hasTaskTool: b
-        .boolean()
+      hasTaskTool: B.boolean()
         .optional()
         .describe("Whether the Task tool is available in the current context"),
-      awaitingLeaderApproval: b
-        .boolean()
+      awaitingLeaderApproval: B.boolean()
         .optional()
         .describe(
           "When true, the teammate has sent a plan approval request to the team leader",
         ),
-      requestId: b
-        .string()
+      requestId: B.string()
         .optional()
         .describe("Unique identifier for the plan approval request"),
     })),
@@ -171,18 +153,16 @@
           });
         q.setAppState((H) => {
           if (H.toolPermissionContext.mode !== "plan") return H;
-          return (
-            CN(!0),
-            SI(!0),
-            {
-              ...H,
-              toolPermissionContext: qz(H.toolPermissionContext, {
-                type: "setMode",
-                mode: "default",
-                destination: "session",
-              }),
-            }
-          );
+          (gN(!0), sI(!0));
+          let O = H.toolPermissionContext.prePlanMode ?? "default";
+          return {
+            ...H,
+            toolPermissionContext: {
+              ...H.toolPermissionContext,
+              mode: O,
+              prePlanMode: void 0,
+            },
+          };
         });
         let w = U8() && q.options.tools.some((H) => H.name === YK);
         return {
@@ -250,18 +230,17 @@
               "User has approved exiting plan mode. You can now proceed.",
             tool_use_id: _,
           };
+        let J = H
+          ? `
+
+If this plan can be broken down into multiple independent tasks, consider using the ${BV} tool to create a team and parallelize the work.`
+          : "";
         return {
           type: "tool_result",
           content: `User has approved your plan. You can now start coding. Start with updating your todo list if applicable
 
 Your plan has been saved to: ${K}
-You can refer back to it if needed during implementation.${
-            H
-              ? `
-
-If this plan can be broken down into multiple independent tasks, consider using a team of teammates (via the Task tool with team_name) to parallelize the work.`
-              : ""
-          }
+You can refer back to it if needed during implementation.${J}
 
 ## Approved Plan:
 ${q}`,

@@@ function 'QLY' (was 'BEY') — structural (79.7%)
--- pretty-v2.1.31.js:420919
+++ pretty-v2.1.32.js:420478
@@ -26,6 +26,7 @@
         target: `@${w}`,
         targetColor: O,
         summary: A.summary,
+        content: A.content,
       },
     },
   };

@@@ function 'Ywz' (was 'mYz') — structural (79.6%)
--- pretty-v2.1.31.js:539892
+++ pretty-v2.1.32.js:540088
@@ -1,5 +1,5 @@
 function mYz(A) {
-  let q = t(19),
+  let q = A1(20),
     {
       mode: K,
       toolPermissionContext: Y,
@@ -19,6 +19,7 @@
     P = T6(dYz),
     G = T6(pYz),
     f = T6(UYz),
+    Z = T6(Owz),
     N =
       vN6.useSyncExternalStore(
         u_q?.subscribeToProactiveChanges ?? BYz,
@@ -79,6 +80,8 @@
   let c = Y?.mode,
     q1 = !NJ8(c),
     H1 = W === "viewing-agent",
+    H1 = G ? D[G] : void 0,
+    D1 = Z1 && H1 != null && H1.status !== "running",
     $1 = B > 0 || H1,
     A1 = (k || q1 ? 1 : 0) + ($1 ? 1 : 0) + (r ? 1 : 0),
     w1 =
@@ -97,7 +100,6 @@
     j1 = A1 < 2 && !k,
     v1 = (!G && $1 && Object.values(D).some(QYz)) || (!G && H1),
     Y1 = [
-      ...[],
       ...(M
         ? [
             a7.createElement(
@@ -202,12 +204,20 @@
         : []),
     ],
     K1 = z ? rYz(w, m, u, C, P) : [];
-  if (!v1 && z) Y1.push(...K1);
+  if (D1)
+    J1.push(
+      m7.createElement(
+        f,
+        { dimColor: !0, key: "esc-return" },
+        m7.createElement(YA, { shortcut: b, action: "return to team lead" }),
+      ),
+    );
+  else if (!j1 && z) J1.push(...o);
   if (v1) {
-    let _1 = [...Y1, ...K1],
+    let O1 = D1 ? J1 : [...J1, ...o],
       a = !w,
       D1;
-    if (q[9] !== H1 || q[10] !== a || q[11] !== H || q[12] !== _)
+    if (q[10] !== Z1 || q[11] !== N1 || q[12] !== H || q[13] !== _)
       ((D1 = a7.createElement(
         h,
         null,
@@ -219,47 +229,47 @@
           isLeaderIdle: a,
         }),
       )),
-        (q[9] = H1),
         (q[10] = a),
         (q[11] = H),
         (q[12] = _),
-        (q[13] = D1));
-    else D1 = q[13];
+        (q[13] = _),
+        (q[14] = L1));
+    else L1 = q[14];
     let G1 =
         _1.length > 0 &&
         a7.createElement(h, null, a7.createElement(nA, null, _1)),
       N1;
-    if (q[14] !== D1 || q[15] !== G1)
+    if (q[15] !== L1 || q[16] !== I1)
       ((N1 = a7.createElement(h, { flexDirection: "column" }, D1, G1)),
-        (q[14] = D1),
         (q[15] = G1),
-        (q[16] = N1));
-    else N1 = q[16];
+        (q[16] = I1),
+        (q[17] = X1));
+    else X1 = q[17];
     return N1;
   }
   let X1 = k && Object.values(D).some(FYz);
   if (Y1.length === 0 && z) {
     let _1;
-    if (q[17] === Symbol.for("react.memo_cache_sentinel"))
+    if (q[18] === Symbol.for("react.memo_cache_sentinel"))
       ((_1 = a7.createElement(
         Z,
         { dimColor: !0, key: "shortcuts-hint" },
         "? for shortcuts",
       )),
-        (q[17] = _1));
-    else _1 = q[17];
+        (q[18] = O1));
+    else O1 = q[18];
     Y1.push(_1);
   }
   if (X1 && z) {
     let _1;
-    if (q[18] === Symbol.for("react.memo_cache_sentinel"))
+    if (q[19] === Symbol.for("react.memo_cache_sentinel"))
       ((_1 = a7.createElement(
         Z,
         { dimColor: !0, key: "manage-tasks" },
         a7.createElement(_A, { shortcut: "↓", action: "manage tasks" }),
       )),
-        (q[18] = _1));
-    else _1 = q[18];
+        (q[19] = O1));
+    else O1 = q[19];
     Y1.push(_1);
   }
   if (Y1.length === 0) return null;

@@@ function 't3q' (was 'kKq') — structural (79.5%)
--- pretty-v2.1.31.js:491122
+++ pretty-v2.1.32.js:490797
@@ -27,7 +27,10 @@
     case "killed": {
       let Y;
       if (q[2] === Symbol.for("react.memo_cache_sentinel"))
-        ((Y = RG1.default.createElement(yG1, { status: "killed" })),
+        ((Y = pP1.default.createElement(dP1, {
+          status: "killed",
+          label: "stopped",
+        })),
           (q[2] = Y));
       else Y = q[2];
       return Y;

@@@ function 'b91' (was 'E91') — structural (79.5%)
--- pretty-v2.1.31.js:554140
+++ pretty-v2.1.32.js:554494
@@ -29,7 +29,8 @@
       () => I("[REPL:unmount] REPL unmounting")
     );
   }, [P]);
-  let k = T6((I6) => I6.toolPermissionContext),
+  let [k, y] = lA.useState(P),
+    u = T6((E6) => E6.toolPermissionContext),
     y = T6((I6) => I6.verbose),
     B = T6((I6) => I6.mcp),
     C = T6((I6) => I6.plugins),
@@ -198,10 +199,19 @@
       return (av4(P4), () => sv4());
     }, [P4]));
   let [B4, h8] = oA.useState(Y ?? []),
+    B1 = lA.useRef(Y4),
+    m1 = lA.useCallback((E6) => {
+      if (typeof E6 === "function")
+        hz((M8) => {
+          let k8 = E6(M8);
+          return ((B1.current = k8), k8);
+        });
+      else ((B1.current = E6), hz(E6));
+    }, []),
     [Yq, N3] = oA.useState(null);
   HZq();
   let [g1, l1] = oA.useState([]),
-    [J6, P6] = oA.useState(""),
+    [yA, hA] = lA.useState(() => dW7()),
     Q6 = oA.useRef(J6);
   ((Q6.current = J6),
     oA.useEffect(() => {
@@ -229,8 +239,25 @@
       },
       [a],
     ),
-    fq = $Xq({ config: N, setMessages: h8, setIsLoading: b3, onInit: s7 }),
-    l3 = XXq({ config: T, setMessages: h8, setIsLoading: b3 }),
+    [XY, X2] = lA.useState(new Set()),
+    Iz = t0q({
+      config: N,
+      setMessages: m1,
+      setIsLoading: I3,
+      onInit: i9,
+      setToolUseConfirmQueue: uq,
+      tools: W6,
+      setStreamingToolUses: bq,
+      setStreamMode: u7,
+      setInProgressToolUseIDs: X2,
+    }),
+    jw = qDq({
+      config: T,
+      setMessages: m1,
+      setIsLoading: I3,
+      setToolUseConfirmQueue: uq,
+      tools: W6,
+    }),
     SK = l3.isRemoteMode ? l3 : fq,
     [$9, w5] = oA.useState({}),
     [hz, OY] = oA.useState(0),
@@ -246,7 +273,6 @@
     [x0, Mj] = oA.useState(!1),
     [IJ, oK] = oA.useState(hmA()),
     [QK, h_] = oA.useState(W6().hasAcknowledgedCostThreshold),
-    [nO, b$] = oA.useState(new Set()),
     [I_, b0] = oA.useState("INSERT"),
     [u$, B$] = oA.useState(!1),
     [m$, $Y] = oA.useState(!1),
@@ -355,6 +381,18 @@
           _8.fileHistorySnapshots)
         )
           ij6(_8);
+        if (!P) {
+          let J4 = M8.agentSetting
+            ? U?.activeAgents.find((G9) => G9.agentType === M8.agentSetting)
+            : void 0;
+          if (
+            (y(J4),
+            fy(J4?.agentType),
+            s((G9) => ({ ...G9, agent: J4?.agentType })),
+            J4 && !zf() && J4.model && J4.model !== "inherit")
+          )
+            rG(s9(J4.model));
+        }
         if (U8())
           v1((wq) => ({
             ...wq,
@@ -427,7 +465,15 @@
     if (_Y === "elicitation") return;
     if (((aK.current = !1), j6(), _Y === "tool-permission"))
       (Z4[0]?.onAbort(), P4([]));
+    else if (BH.isRemoteMode) BH.cancelRequest();
     else lq?.abort();
+    if (h9())
+      (Z94(w1, s),
+        K94(),
+        s((E6) => {
+          if (E6.queuedCommands.length === 0) return E6;
+          return { ...E6, queuedCommands: [] };
+        }));
   }
   let b_ = oA.useCallback(async () => {
       let I6 = await rO6(
@@ -633,9 +679,9 @@
     ),
     Ve = oA.useCallback(
       async (I6, _8, x8, MK, h4, R4, wq) => {
-        let Hq = _8
-          .filter(($O) => $O.type === "user" || $O.type === "assistant")
-          .pop();
+        let G9 = M8.filter(
+          (B_) => B_.type === "user" || B_.type === "assistant",
+        ).pop();
         if (MK) {
           pp.handleQueryStart(a6);
           let $O = af(a6);
@@ -693,19 +739,22 @@
             ((LH = !0), (dR = !0));
             let aO = sN7() || "Background session",
               { taskId: F$, abortSignal: XI } = w54(aO, v1, G, x8);
-            ($54(KE, F$, v1, (jN) => void ph(jN), B4, XI),
-              await zZ6({
-                setMessages: h8,
-                readFileState: LY.current,
-                getAppState: async () =>
-                  new Promise((jN) => {
-                    v1((Q$) => {
-                      return (jN(Q$), Q$);
-                    });
-                  }),
-                setAppState: v1,
-                setConversationId: oK,
-              }));
+            y94(uG, BG, s, (kN) => void KI(kN), Y4, GE);
+            let { clearConversation: gm } = await Promise.resolve().then(
+              () => (NZ6(), rSA),
+            );
+            await gm({
+              setMessages: m1,
+              readFileState: D6.current,
+              getAppState: async () =>
+                new Promise((kN) => {
+                  s((II) => {
+                    return (kN(II), II);
+                  });
+                }),
+              setAppState: s,
+              setConversationId: AH,
+            });
           } else if ($O.result.done) dR = !0;
           else
             XP6(
@@ -752,22 +801,20 @@
         }
         ((aK.current = !0), (gq.current = I6));
         try {
-          if (
-            (b3(!0),
+          (I3(!0),
             h8((NK) => [...NK, ...I6]),
             tq(void 0),
             (ow.current = 0),
-            I7([]),
-            wq && Hq)
-          ) {
-            let NK = [...B4, ...I6];
-            if (!(await wq(Hq, NK))) return;
-          }
+            bq([]));
           let g9 = await new Promise((NK) => {
             h8((Dz) => {
               return (NK(Dz), Dz);
             });
           });
+          if (J4 && G9) {
+            let K5 = [...q5, ...E6];
+            if (!(await J4(G9, K5))) return;
+          }
           await Ve(g9, I6, _8, x8, MK, h4, R4);
         } finally {
           ((aK.current = !1), SJ(Date.now()), j6());
@@ -778,7 +825,7 @@
             } else h8((Dz) => [...Dz, bbA(g9)]);
         }
       },
-      [B4, Ve, b3, v1, j6],
+      [Gc, I3, s, sA],
     ),
     DN = oA.useRef(!1);
   oA.useEffect(() => {
@@ -787,7 +834,10 @@
     DN.current = !0;
     async function _8(x8) {
       if (x8.clearContext) {
-        let R4 = x8.message.planContent ? Qb1() : void 0;
+        let p7 = k8.message.planContent ? Hu1() : void 0,
+          { clearConversation: J4 } = await Promise.resolve().then(
+            () => (NZ6(), rSA),
+          );
         if (
           (await zZ6({
             setMessages: h8,
@@ -887,7 +937,7 @@
                   }
                 },
                 qc = EP(B4, [], n4(), [], void 0, X1),
-                Kc = await g9.call(Sm, qc, Hq);
+                KH = await HG1(q5, F9, EN, G9);
               if (Kc)
                 m7({
                   jsx: Kc,
@@ -948,6 +998,7 @@
           ideSelection: VA,
           setUserInputOnProcessing: tq,
           setAbortController: g8,
+          abortController: V4,
           onQuery: kP,
           resetLoadingState: j6,
           thinkingEnabled: g,
@@ -1021,7 +1072,7 @@
     }, [bJ]),
     UR = oA.useCallback(async () => {
       T3(!0);
-      let I6 = await AV6.call(() => {});
+      let M8 = await (await PV6.load()).call(() => {});
       V7(I6);
     }, []),
     y91 = oA.useCallback(() => {
@@ -1389,9 +1440,9 @@
               }
               O9((R4) => {
                 return (
-                  R4.filter((wq) => wq.hostPattern.host === h4).forEach((wq) =>
-                    wq.resolvePromise(_8),
-                  ),
+                  p7
+                    .filter((J4) => J4.hostPattern.host === P4)
+                    .forEach((J4) => J4.resolvePromise(M8)),
                   R4.filter((wq) => wq.hostPattern.host !== h4)
                 );
               });
@@ -1577,6 +1628,67 @@
               v1((x8) => ({ ...x8, fileHistory: _8(x8.fileHistory) }));
             }, I6.uuid);
           },
+          onSummarize: async (E6, M8) => {
+            let k8 = Y4.indexOf(E6);
+            if (k8 === -1) return;
+            let h7 = s4(),
+              P4 = d$(Y4, [], h7, [], void 0, o),
+              p7 = await P4.getAppState(),
+              J4 = await jZ(
+                P4.options.tools,
+                P4.options.mainLoopModel,
+                Array.from(
+                  p7.toolPermissionContext.additionalWorkingDirectories.keys(),
+                ),
+                P4.options.mcpClients,
+              ),
+              G9 = Z51({
+                mainThreadAgentDefinition: void 0,
+                toolUseContext: P4,
+                customSystemPrompt: P4.options.customSystemPrompt,
+                defaultSystemPrompt: J4,
+                appendSystemPrompt: P4.options.appendSystemPrompt,
+              }),
+              [q5, K5] = await Promise.all([C$(), y$()]),
+              q9 = await Nc4(
+                Y4,
+                k8,
+                P4,
+                {
+                  systemPrompt: G9,
+                  userContext: q5,
+                  systemContext: K5,
+                  toolUseContext: P4,
+                  forkContextMessages: Y4,
+                },
+                M8,
+              );
+            (m1([
+              q9.boundaryMarker,
+              ...(q9.messagesToKeep ?? []),
+              ...q9.summaryMessages,
+              ...q9.attachments,
+              ...q9.hookResults,
+            ]),
+              AH(hT6()));
+            let F9 = xF1(E6);
+            if (F9 !== null) {
+              let KH = F4(F9, "bash-input"),
+                AW = F4(F9, Hf);
+              if (KH) (hA(KH), T8("bash"));
+              else if (AW) {
+                let b_ = F4(F9, "command-args") || "";
+                (hA(`${AW} ${b_}`), T8("prompt"));
+              } else (hA(F9), T8("prompt"));
+            }
+            let EN = JD("app:toggleTranscript", "Global", "ctrl+o");
+            AA({
+              key: "summarize-ctrl-o-hint",
+              text: `Conversation summarized (${EN} for history)`,
+              priority: "medium",
+              timeoutMs: 8000,
+            });
+          },
           onRestoreMessage: async (I6) => {
             let _8 = B4.indexOf(I6),
               x8 = B4.slice(0, _8);

@@@ variable 'ppY' (was 'Ve4') — structural (79.3%)
--- pretty-v2.1.31.js:457178
+++ pretty-v2.1.32.js:457045
@@ -1,63 +1,17 @@
-var Ve4 = E(() => {
-  gT();
-  vD();
-  js();
-  mV();
-  dP6();
-  p31();
-  GW6();
-  vW6();
-  fQ1();
-  N6();
-  B3();
-  L_6();
-  mA();
-  rz();
-  Gw();
-  ((ogY = {
-    type: "local",
-    name: "compact",
-    description:
-      "Clear conversation history but keep a summary in context. Optional: /compact [instructions for summarization]",
-    isEnabled: () => !M6(process.env.DISABLE_COMPACT),
-    isHidden: !1,
-    supportsNonInteractive: !0,
-    argumentHint: "<optional custom summarization instructions>",
-    async call(A, q) {
-      U4("compact");
-      let { abortController: K, messages: Y } = q;
-      if (Y.length === 0) throw Error("No messages to compact");
-      let z = A.trim();
-      try {
-        if (!z) {
-          let X = await TW6(Y, q.agentId);
-          if (X) {
-            (J_.cache.clear?.(), YJ.cache.clear?.(), KP1());
-            let D = wK1("tip"),
-              j = HX("app:toggleTranscript", "Global", "ctrl+o"),
-              M = [
-                ...(q.options.verbose ? [] : [`(${j} to see full summary)`]),
-                ...(D ? [D] : []),
-              ];
-            return {
-              type: "compact",
-              compactionResult: X,
-              displayText: q6.dim(
-                "Compacted " +
-                  M.join(`
-`),
-              ),
-            };
-          }
-        }
-        let H = (await ep(Y, void 0, q)).messages,
-          O = await pM1(H, q, await agY(q, H), !1, z, !1);
-        (g31(void 0), KP1(), J_.cache.clear?.(), YJ.cache.clear?.());
+var ppY = async (A, q) => {
+  B4("compact");
+  let { abortController: K, messages: Y } = q;
+  if (Y.length === 0) throw Error("No messages to compact");
+  let z = A.trim();
+  try {
+    if (!z) {
+      let X = await pW6(Y, q.agentId);
+      if (X) {
+        (C$.cache.clear?.(), zJ.cache.clear?.(), WG1());
         let $ = wK1("tip"),
           _ = HX("app:toggleTranscript", "Global", "ctrl+o"),
           J = [
             ...(q.options.verbose ? [] : [`(${_} to see full summary)`]),
-            ...(O.userDisplayMessage ? [O.userDisplayMessage] : []),
             ...($ ? [$] : []),
           ];
         return {
@@ -69,19 +23,34 @@
 `),
           ),
         };
-      } catch (w) {
-        if (K.signal.aborted) throw Error("Compaction canceled.");
-        else if (w instanceof Error && w.message === PQ1) throw Error(PQ1);
-        else
-          throw (
-            e(w instanceof Error ? w : Error(String(w))),
-            Error(`Error during compaction: ${w}`)
-          );
       }
-    },
-    userFacingName() {
-      return "compact";
-    },
-  }),
-    (fe4 = ogY));
-});
+    }
+    let H = (await Dd(Y, void 0, q)).messages,
+      O = await tM1(H, q, await dpY(q, H), !1, z, !1);
+    (s31(void 0), WG1(), C$.cache.clear?.(), zJ.cache.clear?.(), ZZ6());
+    let $ = PK1("tip"),
+      _ = JD("app:toggleTranscript", "Global", "ctrl+o"),
+      J = [
+        ...(q.options.verbose ? [] : [`(${_} to see full summary)`]),
+        ...(O.userDisplayMessage ? [O.userDisplayMessage] : []),
+        ...($ ? [$] : []),
+      ];
+    return {
+      type: "compact",
+      compactionResult: O,
+      displayText: Y6.dim(
+        "Compacted " +
+          J.join(`
+`),
+      ),
+    };
+  } catch (w) {
+    if (K.signal.aborted) throw Error("Compaction canceled.");
+    else if (w instanceof Error && w.message === gQ1) throw Error(gQ1);
+    else
+      throw (
+        K1(w instanceof Error ? w : Error(String(w))),
+        Error(`Error during compaction: ${w}`)
+      );
+  }
+};

@@@ function 'WJz' (was 'rOz') — structural (79.0%)
--- pretty-v2.1.31.js:561810
+++ pretty-v2.1.32.js:561958
@@ -415,6 +415,7 @@
               !!J.enableAuthStatus,
               J,
               _,
+              O,
             ),
               ($1 = !0));
           } else if (A1.request.subtype === "set_permission_mode") {

@@@ variable 'S6q' (was 'Z1q') — structural (78.9%)
--- pretty-v2.1.31.js:462714
+++ pretty-v2.1.32.js:462710
@@ -3,6 +3,7 @@
   u1();
   MO();
   F4();
+  j3();
   GA = o(J1(), 1);
   ApY = ["Project", "User", "Managed", "Plugin", "Built-in"];
 });

@@@ function 'r2q' (was 'T8z') — structural (78.9%)
--- pretty-v2.1.31.js:512614
+++ pretty-v2.1.32.js:512279
@@ -20,7 +20,7 @@
       `The current date is: ${z_1()}`,
       w,
       O,
-      `The most recent Claude model family is Claude 4.5. Model IDs — Opus 4.5: '${ZbA.opus}', Sonnet 4.5: '${ZbA.sonnet}', Haiku 4.5: '${ZbA.haiku}'. When building AI applications, default to the latest and most capable Claude models.`,
+      `The most recent Claude model family is Claude 4.5/4.6. Model IDs — Opus 4.6: '${abA.opus}', Sonnet 4.5: '${abA.sonnet}', Haiku 4.5: '${abA.haiku}'. When building AI applications, default to the latest and most capable Claude models.`,
     ].filter((_) => _ !== null);
   return [
     "# Environment",

@@@ function 'YHq' (was 'W2q') — structural (78.9%)
--- pretty-v2.1.31.js:519217
+++ pretty-v2.1.32.js:518969
@@ -1,4 +1,5 @@
 function W2q(A) {
-  let q = Uv(jM(), Qb1());
+  let q = KE(ZM(), Hu1()),
+    K = zZ1(A);
   return A.startsWith(q) && A.endsWith(".md");
 }

@@@ function 'gU5' (was 'tQ5') — structural (78.9%)
--- pretty-v2.1.31.js:184753
+++ pretty-v2.1.32.js:184877
@@ -9,7 +9,7 @@
       O = H.styles;
     if (Y.length > 0 && !sQ5(O, z)) {
       let $ = Y.join("");
-      for (let { segment: _ } of XM7.segment($))
+      for (let { segment: _ } of MC().segment($))
         K.push({ type: "char", value: _, fullWidth: j7(_) === 2, styles: z });
       Y.length = 0;
     }
@@ -17,7 +17,7 @@
   }
   if (Y.length > 0) {
     let w = Y.join("");
-    for (let { segment: H } of XM7.segment(w))
+    for (let { segment: H } of MC().segment(w))
       K.push({ type: "char", value: H, fullWidth: j7(H) === 2, styles: z });
   }
   return K;

@@@ function 'oBY' (was 'ebY') — structural (78.8%)
--- pretty-v2.1.31.js:442523
+++ pretty-v2.1.32.js:442466
@@ -58,16 +58,18 @@
       B = K.mcpServers,
       C;
     if (Array.isArray(B))
-      C = B.map((g) => {
-        let x = Yo4.safeParse(g);
-        if (x.success) return x.data;
-        return (
-          I(
-            `Agent file ${A} has invalid mcpServers item: ${F1(g)}. Error: ${x.error.message}`,
-          ),
-          null
-        );
-      }).filter((g) => g !== null);
+      S = u
+        .map((g) => {
+          let x = wa4.safeParse(g);
+          if (x.success) return x.data;
+          return (
+            h(
+              `Agent file ${A} has invalid mcpServers item: ${g1(g)}. Error: ${x.error.message}`,
+            ),
+            null
+          );
+        })
+        .filter((g) => g !== null);
     let m = sbY(K, w),
       u = Y.trim();
     return {

@@@ function 'MuA' (was 'mbA') — structural (78.7%)
--- pretty-v2.1.31.js:518195
+++ pretty-v2.1.32.js:517919
@@ -1,4 +1,4 @@
-function mbA(A, q = 0, K, Y, z, w, H, O) {
+function MuA(A, q = 0, K, Y, z, w, H, O, $) {
   let $ = A[A.length - 1],
     _ = A[0],
     J = UbA(A),
@@ -16,6 +16,7 @@
     isSidechain: _.isSidechain,
     teamName: _.teamName,
     agentName: _.agentName,
+    agentSetting: $,
     leafUuid: $.uuid,
     summary: K,
     customTitle: Y,

@@@ function 'YY' (was 'wY') — structural (78.7%)
--- pretty-v2.1.31.js:452073
+++ pretty-v2.1.32.js:452031
@@ -28,19 +28,8 @@
   else _ = q[5];
   T0.useEffect($, _);
   let J;
-  if (q[6] !== O)
-    ((J = (M, W) => {
-      I(`Settings changed from ${M}, updating AppState`);
-      let P = O76();
-      (J51(),
-        O.setState((G) => {
-          let f = Us4(G.toolPermissionContext, P);
-          if (f.isBypassPermissionsModeAvailable && fg1()) f = Vg1(f);
-          return { ...G, settings: W, toolPermissionContext: f };
-        }));
-    }),
-      (q[6] = O),
-      (q[7] = J));
+  if (q[6] !== O.setState)
+    ((J = (M) => AZ6(M, O.setState)), (q[6] = O.setState), (q[7] = J));
   else J = q[7];
   let X = T0.useEffectEvent(J);
   r_1(X);

@@@ function 'p_q' (was 'tOq') — structural (78.4%)
--- pretty-v2.1.31.js:534873
+++ pretty-v2.1.32.js:535075
@@ -51,7 +51,7 @@
     { columns: T } = A8(),
     k = j !== void 0 ? D[j] : void 0,
     y = k && sOq(k.schema);
-  (v7(), aV6("Claude Code needs your input", "elicitation_dialog"));
+  GN6("Claude Code needs your input", "elicitation_dialog");
   function B($1) {
     let A1 = D.length + 2,
       O1 =
@@ -103,22 +103,16 @@
     if (!k) return;
     (P(void 0), f(""), N(0));
   }
-  let x = k !== void 0 && W === k.name;
+  let x = k !== void 0 && W === k.name,
+    p = x && y && !ZZ1(k?.schema);
   (zA(
     "confirm:no",
     () => {
-      K("cancel");
+      g();
     },
-    { context: "Settings", isActive: !x },
+    { context: "Settings", isActive: p && P === "" },
   ),
     zA(
-      "confirm:no",
-      () => {
-        g();
-      },
-      { context: "Settings", isActive: x && y && !KZ1(k?.schema) && G === "" },
-    ),
-    eA(
       ($1, A1) => {
         if (x && KZ1(k?.schema)) return;
         if (x && y) return;
@@ -292,9 +286,9 @@
               ),
             );
           else if (y) {
-            let Y1 = J[O1],
-              K1 = oOq(s);
-            if (Z1 && W === O1)
+            let s = J[t];
+            if (w1 && W === t) {
+              let j1 = Q_q(e);
               return v1(
                 FK.default.createElement(
                   h,
@@ -327,6 +321,7 @@
                   ),
                 ),
               );
+            }
             return v1(
               FK.default.createElement(
                 Z,
@@ -368,30 +363,18 @@
   return FK.default.createElement(
     h,
     {
-      flexDirection: "column",
-      gap: 1,
-      padding: 1,
-      borderStyle: "round",
-      borderColor: "permission",
+      title: `MCP Server "${A}" requests your input`,
+      subtitle: z,
+      color: "permission",
+      onCancel: () => K("cancel"),
+      isCancelActive: !p,
+      hideInputGuide: !0,
     },
-    FK.default.createElement(
-      Z,
-      { bold: !0 },
-      d1.info,
-      " MCP Server “",
-      A,
-      "” requests your input",
-    ),
-    FK.default.createElement(
-      h,
-      { padding: 1 },
-      FK.default.createElement(Z, null, z),
-    ),
     r(),
     D.length > 0 &&
       FK.default.createElement(
-        FK.default.Fragment,
         null,
+        { flexDirection: "column", gap: 1 },
         H1.length > 0 &&
           FK.default.createElement(
             Z,

@@@ variable 'KD6' (was 'h06') — structural (78.3%)
--- pretty-v2.1.31.js:358963
+++ pretty-v2.1.32.js:359327
@@ -7,6 +7,7 @@
       { pattern: />\(/, message: "process substitution >()" },
       { pattern: /\$\(/, message: "$() command substitution" },
       { pattern: /\$\{/, message: "${} parameter substitution" },
+      { pattern: /\$\[/, message: "$[] legacy arithmetic expansion" },
       { pattern: /~\[/, message: "Zsh-style parameter expansion" },
       { pattern: /\(e:/, message: "Zsh-style glob qualifiers" },
       { pattern: /<#/, message: "PowerShell comment syntax" },

@@@ function 'DNA' (was 'bVA') — structural (78.2%)
--- pretty-v2.1.31.js:364830
+++ pretty-v2.1.32.js:365161
@@ -75,7 +75,7 @@
             reason: `Required by Bash prompt rule: "${m.matchedDescription}"`,
           },
           suggestions: U,
-          pendingClassifierCheck: gM1(A.command, Y.toolPermissionContext),
+          ...{},
         };
       }
     }
@@ -99,7 +99,7 @@
               reason:
                 T.message ?? "Command contains patterns that require approval",
             },
-            pendingClassifierCheck: gM1(A.command, Y.toolPermissionContext),
+            ...{},
           }
         );
       Y = await q.getAppState();
@@ -107,13 +107,7 @@
       if (k.behavior !== "passthrough") return k;
     }
     if (O.behavior === "ask")
-      return (
-        (Y = await q.getAppState()),
-        {
-          ...O,
-          pendingClassifierCheck: gM1(A.command, Y.toolPermissionContext),
-        }
-      );
+      return ((Y = await q.getAppState()), { ...O, ...{} });
     return O;
   }
   if (!M6(process.env.CLAUDE_CODE_DISABLE_COMMAND_INJECTION_CHECK)) {
@@ -126,7 +120,7 @@
         message: G_(c4.name, k),
         decisionReason: k,
         suggestions: [],
-        pendingClassifierCheck: gM1(A.command, Y.toolPermissionContext),
+        ...{},
       };
     }
   }
@@ -185,10 +179,7 @@
   if (((Y = await q.getAppState()), $.length === 1)) {
     let T = Ak4({ command: $[0] }, Y.toolPermissionContext, P, J);
     if (T.behavior === "ask" || T.behavior === "passthrough")
-      return {
-        ...T,
-        pendingClassifierCheck: gM1(A.command, Y.toolPermissionContext),
-      };
+      return { ...T, ...{} };
     return T;
   }
   let G = new Map();
@@ -239,6 +230,6 @@
     message: G_(c4.name, V),
     decisionReason: V,
     suggestions: N,
-    pendingClassifierCheck: gM1(A.command, Y.toolPermissionContext),
+    ...{},
   };
 }

@@@ function 'ld4' (was 'ep4') — structural (78.1%)
--- pretty-v2.1.31.js:422570
+++ pretty-v2.1.32.js:422145
@@ -16,6 +16,7 @@
           N,
           T,
           k,
+          y,
           y;
         if (V && f.success && f.data.name) {
           N = `@${f.data.name}`;
@@ -44,6 +45,7 @@
           isError: j,
           isAsync: m,
           color: k,
+          descriptionColor: y,
           lastToolInfo: G,
           taskDescription: y,
         };
@@ -97,6 +99,7 @@
         key: X.id,
         agentType: X.agentType,
         description: X.description,
+        descriptionColor: X.descriptionColor,
         taskDescription: X.taskDescription,
         toolUseCount: X.toolUseCount,
         tokens: X.tokens,

@@@ function 'Em6' (was 'eB6') — structural (77.8%)
--- pretty-v2.1.31.js:78368
+++ pretty-v2.1.32.js:78246
@@ -5,6 +5,7 @@
     A.includes("claude-sonnet-4-5") ||
     A.includes("claude-opus-4-1") ||
     A.includes("claude-opus-4-5") ||
+    A.includes("claude-opus-4-6") ||
     A.includes("claude-haiku-4-5")
   );
 }

@@@ variable 'i0q' (was 'KXq') — structural (77.8%)
--- pretty-v2.1.31.js:545013
+++ pretty-v2.1.32.js:545146
@@ -72,6 +72,8 @@
   OW1();
   FS();
   zxA();
+  BxA();
+  d0q();
   ((B7 = o(J1(), 1)), (hq = o(J1(), 1)));
   qXq = B7.memo(izz);
 });

@@@ function 'gd4' (was 'rp4') — structural (77.4%)
--- pretty-v2.1.31.js:422243
+++ pretty-v2.1.32.js:421818
@@ -19,7 +19,7 @@
               hA.createElement(
                 nA,
                 null,
-                hA.createElement(_A, { shortcut: "↓", action: "manage" }),
+                bA.createElement(YA, { shortcut: "shift+↑", action: "manage" }),
                 W &&
                   hA.createElement(kA, {
                     action: "app:toggleTranscript",

@@@ function 'EbY' (was 'CIY') — structural (77.4%)
--- pretty-v2.1.31.js:434398
+++ pretty-v2.1.32.js:434289
@@ -23,6 +23,12 @@
     let H = w.message.content.filter(z);
     if (H.length === w.message.content.length) return w;
     if (H.length === 0) return null;
+    if (
+      !H.some(
+        ($) => $.type !== "text" || ($.text !== void 0 && $.text.trim() !== ""),
+      )
+    )
+      return null;
     return { ...w, message: { ...w.message, content: H } };
   }).filter((w) => w !== null);
 }

@@@ function 'wHq' (was 'G2q') — structural (77.3%)
--- pretty-v2.1.31.js:519263
+++ pretty-v2.1.32.js:519017
@@ -1,5 +1,6 @@
 function G2q(A) {
   if (!BG1()) return !1;
-  let q = fV6();
+  let q = BV6(),
+    K = zZ1(A);
   return A === q || A.startsWith(q + ZP);
 }

@@@ function 'uT5' (was 'rV5') — structural (77.1%)
--- pretty-v2.1.31.js:148262
+++ pretty-v2.1.32.js:148243
@@ -27,5 +27,6 @@
     deployment_environment: "",
     is_conductor: !1,
     version_base: "",
+    coworker_type: "",
   };
 }

@@@ function 'v_q' (was 'xOq') — structural (76.9%)
--- pretty-v2.1.31.js:532351
+++ pretty-v2.1.32.js:532357
@@ -3,6 +3,28 @@
     w = h7(),
     { addNotification: H } = Sq(),
     [O, $] = hR.useState(""),
+    [_, J] = nM.useState({}),
+    X = nM.useRef(0);
+  function D(w1, V1, E1, q1, s) {
+    let j1 = X.current++,
+      J1 = {
+        id: j1,
+        type: "image",
+        content: w1,
+        mediaType: V1 || "image/png",
+        filename: E1 || "Pasted image",
+        dimensions: q1,
+      };
+    (J01(J1), setTimeout(() => i41(J1), 0), J((o) => ({ ...o, [j1]: J1 })));
+  }
+  let j = nM.useCallback((w1) => {
+      J((V1) => {
+        let E1 = { ...V1 };
+        return (delete E1[w1], E1);
+      });
+    }, []),
+    M = Object.values(_).filter((w1) => w1.type === "image"),
+    W = M.length > 0,
     _ = A.tool.name === XV,
     J = _ ? void 0 : A.input.plan,
     X = _ ? nG() : void 0,
@@ -166,7 +188,12 @@
       let L1 = "",
         Y1 = `
 
-If you need specific details from before exiting plan mode (like exact code snippets, error messages, or content you generated), read the full transcript at: ${v_(F6())}`;
+If you need specific details from before exiting plan mode (like exact code snippets, error messages, or content you generated), read the full transcript at: ${oO(u6())}`,
+        L1 = F8()
+          ? `
+
+If this plan can be broken down into multiple independent tasks, consider using the ${BV} tool to create a team and parallelize the work.`
+          : "";
       (w((K1) => ({
         ...K1,
         initialMessage: {
@@ -174,7 +201,7 @@
             ...p6({
               content: `Implement the following plan:
 
-${W}${L1}${Y1}`,
+${k}${_1}${N1}${L1}`,
             }),
             planContent: W,
           },
@@ -226,15 +253,33 @@
     }
     if (H1 === "no") {
       let j1 = O.trim();
-      if (!j1) return;
-      (n("tengu_plan_exit", {
+      if (!o && !W) return;
+      c("tengu_plan_exit", {
         planLengthChars: W.length,
         outcome: "no",
         interviewPhaseEnabled: h0(),
-      }),
-        q(),
+      });
+      let _1;
+      if (W)
+        _1 = await Promise.all(
+          M.map(async (O1) => {
+            let N1 = {
+              type: "image",
+              source: {
+                type: "base64",
+                media_type: O1.mediaType || "image/png",
+                data: O1.content,
+              },
+            };
+            return (await B41(N1)).block;
+          }),
+        );
+      (q(),
         K(),
-        A.onReject(j1));
+        A.onReject(
+          o || (W ? "(See attached image)" : void 0),
+          _1 && _1.length > 0 ? _1 : void 0,
+        ));
     }
   }
   let c = oh(),
@@ -285,10 +330,12 @@
             },
             onCancel: () => N("default"),
           }),
-        ),
-        H1.filter(($1) => $1.url).map(($1, A1) =>
-          Y5.default.createElement(Z, { key: A1, dimColor: !0 }, $1.url),
         ),
+        w1
+          .filter((V1) => V1.url)
+          .map((V1, E1) =>
+            e3.default.createElement(f, { key: E1, dimColor: !0 }, V1.url),
+          ),
         Y5.default.createElement(Z, { dimColor: !0 }, "← to go back"),
       ),
     );
@@ -492,6 +539,9 @@
                   K(),
                   A.onReject());
               },
+              onImagePaste: D,
+              pastedContents: _,
+              onRemoveImage: j,
             }),
           ),
         ),

@@@ function 'S_q' (was 'gOq') — structural (76.5%)
--- pretty-v2.1.31.js:533654
+++ pretty-v2.1.32.js:533713
@@ -1,5 +1,5 @@
 function gOq(A) {
-  let q = t(92),
+  let q = A1(95),
     {
       question: K,
       questions: Y,
@@ -15,6 +15,9 @@
       onSubmit: j,
       onRespondToClaude: M,
       onFinishPlanInterview: W,
+      onImagePaste: G,
+      pastedContents: P,
+      onRemoveImage: V,
     } = A,
     P = O === void 0 ? !1 : O,
     G = T6(X9z) === "plan",
@@ -207,11 +210,14 @@
     q[49] !== j ||
     q[50] !== _ ||
     q[51] !== A1 ||
-    q[52] !== K.multiSelect ||
-    q[53] !== K.question ||
+    q[52] !== _ ||
+    q[53] !== e ||
     q[54] !== H ||
-    q[55] !== H1 ||
-    q[56] !== Y.length
+    q[55] !== K.multiSelect ||
+    q[56] !== K.question ||
+    q[57] !== H ||
+    q[58] !== D1 ||
+    q[59] !== Y.length
   )
     ((j1 = dY.default.createElement(
       h,
@@ -236,6 +242,9 @@
             onDownFromLastItem: g,
             isDisabled: f,
             onOpenEditor: q1,
+            onImagePaste: G,
+            pastedContents: P,
+            onRemoveImage: V,
           })
         : dY.default.createElement(ZA, {
             key: K.question,
@@ -252,6 +261,9 @@
             isDisabled: f,
             layout: "compact-vertical",
             onOpenEditor: q1,
+            onImagePaste: G,
+            pastedContents: P,
+            onRemoveImage: V,
           }),
     )),
       (q[43] = z),
@@ -263,51 +275,54 @@
       (q[49] = j),
       (q[50] = _),
       (q[51] = A1),
-      (q[52] = K.multiSelect),
-      (q[53] = K.question),
+      (q[52] = _),
+      (q[53] = e),
       (q[54] = H),
-      (q[55] = H1),
-      (q[56] = Y.length),
-      (q[57] = j1));
-  else j1 = q[57];
+      (q[55] = K.multiSelect),
+      (q[56] = K.question),
+      (q[57] = H),
+      (q[58] = D1),
+      (q[59] = Y.length),
+      (q[60] = q1));
+  else q1 = q[60];
   let L1;
-  if (q[58] === Symbol.for("react.memo_cache_sentinel"))
+  if (q[61] === Symbol.for("react.memo_cache_sentinel"))
     ((L1 = dY.default.createElement(Q5, { dividerColor: "inactive" })),
-      (q[58] = L1));
-  else L1 = q[58];
+      (q[61] = s));
+  else s = q[61];
   let v1;
-  if (q[59] !== N || q[60] !== f)
+  if (q[62] !== y || q[63] !== T)
     ((v1 =
       f && N === 0
         ? dY.default.createElement(Z, { color: "suggestion" }, d1.pointer)
         : dY.default.createElement(Z, null, " ")),
-      (q[59] = N),
-      (q[60] = f),
-      (q[61] = v1));
-  else v1 = q[61];
-  let Y1 = f && N === 0 ? "suggestion" : void 0,
-    K1 = A1.length + 1,
-    X1;
-  if (q[62] !== Y1 || q[63] !== K1)
-    ((X1 = dY.default.createElement(Z, { color: Y1 }, K1, ". Chat about this")),
       (q[62] = Y1),
       (q[63] = K1),
       (q[64] = X1));
   else X1 = q[64];
-  let _1;
+  let J1 = T && y === 0 ? "suggestion" : void 0,
+    o = e.length + 1,
+    _1;
   if (q[65] !== v1 || q[66] !== X1)
+    ((_1 = dY.default.createElement(f, { color: J1 }, o, ". Chat about this")),
+      (q[65] = J1),
+      (q[66] = o),
+      (q[67] = _1));
+  else _1 = q[67];
+  let O1;
+  if (q[68] !== j1 || q[69] !== _1)
     ((_1 = dY.default.createElement(
       h,
       { flexDirection: "row", gap: 1 },
       v1,
       X1,
     )),
-      (q[65] = v1),
-      (q[66] = X1),
-      (q[67] = _1));
-  else _1 = q[67];
+      (q[68] = j1),
+      (q[69] = _1),
+      (q[70] = O1));
+  else O1 = q[70];
   let a;
-  if (q[68] !== N || q[69] !== f || q[70] !== G || q[71] !== A1.length)
+  if (q[71] !== y || q[72] !== T || q[73] !== N || q[74] !== e.length)
     ((a =
       G &&
       dY.default.createElement(
@@ -323,21 +338,21 @@
           ". Skip interview and plan immediately",
         ),
       )),
-      (q[68] = N),
-      (q[69] = f),
-      (q[70] = G),
-      (q[71] = A1.length),
-      (q[72] = a));
-  else a = q[72];
-  let D1;
-  if (q[73] !== _1 || q[74] !== a)
-    ((D1 = dY.default.createElement(h, { flexDirection: "column" }, L1, _1, a)),
+      (q[71] = y),
+      (q[72] = T),
       (q[73] = _1),
-      (q[74] = a),
+      (q[74] = e.length),
       (q[75] = D1));
   else D1 = q[75];
   let G1;
-  if (q[76] !== Y.length)
+  if (q[76] !== O1 || q[77] !== N1)
+    ((L1 = dY.default.createElement(I, { flexDirection: "column" }, s, O1, N1)),
+      (q[76] = O1),
+      (q[77] = N1),
+      (q[78] = L1));
+  else L1 = q[78];
+  let I1;
+  if (q[79] !== Y.length)
     ((G1 =
       Y.length === 1
         ? dY.default.createElement(
@@ -349,11 +364,11 @@
             " to navigate",
           )
         : "Tab/Arrow keys to navigate"),
-      (q[76] = Y.length),
-      (q[77] = G1));
-  else G1 = q[77];
+      (q[79] = Y.length),
+      (q[80] = I1));
+  else I1 = q[80];
   let N1;
-  if (q[78] !== k)
+  if (q[81] !== S)
     ((N1 =
       k &&
       C &&
@@ -363,11 +378,11 @@
         " · ctrl+g to edit in ",
         C,
       )),
-      (q[78] = k),
-      (q[79] = N1));
-  else N1 = q[79];
+      (q[81] = S),
+      (q[82] = X1));
+  else X1 = q[82];
   let R1;
-  if (q[80] !== G1 || q[81] !== N1)
+  if (q[83] !== I1 || q[84] !== X1)
     ((R1 = dY.default.createElement(
       h,
       { marginTop: 1 },
@@ -382,17 +397,17 @@
         "· Esc to cancel",
       ),
     )),
-      (q[80] = G1),
-      (q[81] = N1),
-      (q[82] = R1));
-  else R1 = q[82];
+      (q[83] = I1),
+      (q[84] = X1),
+      (q[85] = S1));
+  else S1 = q[85];
   let h1;
   if (
-    q[83] !== w1 ||
-    q[84] !== Z1 ||
-    q[85] !== j1 ||
     q[86] !== D1 ||
-    q[87] !== R1
+    q[87] !== E1 ||
+    q[88] !== q1 ||
+    q[89] !== L1 ||
+    q[90] !== S1
   )
     ((h1 = dY.default.createElement(
       h,
@@ -403,15 +418,15 @@
       D1,
       R1,
     )),
-      (q[83] = w1),
-      (q[84] = Z1),
-      (q[85] = j1),
       (q[86] = D1),
       (q[87] = R1),
-      (q[88] = h1));
-  else h1 = q[88];
+      (q[88] = q1),
+      (q[89] = L1),
+      (q[90] = S1),
+      (q[91] = v1));
+  else v1 = q[91];
   let f1;
-  if (q[89] !== h1 || q[90] !== O1)
+  if (q[92] !== v1 || q[93] !== G1)
     ((f1 = dY.default.createElement(
       h,
       { flexDirection: "column", marginTop: 0 },
@@ -419,9 +434,9 @@
       s,
       h1,
     )),
-      (q[89] = h1),
-      (q[90] = O1),
-      (q[91] = f1));
-  else f1 = q[91];
+      (q[92] = v1),
+      (q[93] = G1),
+      (q[94] = U1));
+  else U1 = q[94];
   return f1;
 }

@@@ variable 'PZ6' (was 'KZ6') — structural (76.5%)
--- pretty-v2.1.31.js:456962
+++ pretty-v2.1.32.js:456757
@@ -14,7 +14,6 @@
   tG();
   C8();
   kq();
-  g6();
   Oe4 = o(Ix1(), 1);
   ((oP1 = []), (iP1 = []));
 });

@@@ variable 'n3q' (was 'VKq') — structural (76.5%)
--- pretty-v2.1.31.js:490727
+++ pretty-v2.1.32.js:490389
@@ -12,5 +12,6 @@
   wK();
   hTA();
   D8();
+  hq();
   ((F9 = o(J1(), 1)), (msY = []));
 });

@@@ function 'zG1' (was 'nW1') — structural (76.4%)
--- pretty-v2.1.31.js:446303
+++ pretty-v2.1.32.js:446249
@@ -2,6 +2,9 @@
   if (A.config.type === "sdk") return A;
   let q = await HR(A.name, A.config);
   if (q.type !== "connected")
-    throw new VF(`MCP server "${A.name}" is not connected`);
+    throw new FE(
+      `MCP server "${A.name}" is not connected`,
+      "MCP server not connected",
+    );
   return q;
 }

@@@ variable 'pW' (was 'FS') — structural (76.3%)
--- pretty-v2.1.31.js:300067
+++ pretty-v2.1.32.js:246399
@@ -6,5 +6,10 @@
   f7();
   Xw();
   Q4();
+  Q7();
+  g4();
+  Pz();
+  FA();
   ((zp9 = { status: "active" }), (Hp9 = new Set()));
+  tG9 = new Set();
 });

@@@ function 'Fqz' (was 'v7z') — structural (76.0%)
--- pretty-v2.1.31.js:516630
+++ pretty-v2.1.32.js:516303
@@ -374,10 +374,20 @@
         }),
       ]);
     case "task_status": {
+      let K = A.status === "killed" ? "stopped" : A.status;
+      if (A.status === "killed")
+        return [
+          p6({
+            content: NI(
+              `Task "${A.description}" (${A.taskId}) was stopped by the user.`,
+            ),
+            isMeta: !0,
+          }),
+        ];
       let K = [
         `Task ${A.taskId}`,
         `(type: ${A.taskType})`,
-        `(status: ${A.status})`,
+        `(status: ${K})`,
         `(description: ${A.description})`,
       ];
       if (A.deltaSummary) K.push(`Delta: ${A.deltaSummary}`);

@@@ function 'lf' (was 'hf') — structural (76.0%)
--- pretty-v2.1.31.js:138566
+++ pretty-v2.1.32.js:138459
@@ -13,6 +13,7 @@
     A ||
     Y ||
     ((z === "ANTHROPIC_API_KEY" || z === "apiKeyHelper") &&
-      !M6(process.env.CLAUDE_CODE_REMOTE))
+      !$6(process.env.CLAUDE_CODE_REMOTE) &&
+      process.env.CLAUDE_CODE_ENVIRONMENT_KIND !== "bridge")
   );
 }

@@@ function 'c$z' (was 'NHz') — structural (75.9%)
--- pretty-v2.1.31.js:553808
+++ pretty-v2.1.32.js:554160
@@ -1,6 +1,7 @@
 function NHz(A) {
   let q = A.toLowerCase();
-  if (q.includes("opus-4-5")) return null;
+  if (q.includes("opus-4-6")) return null;
+  if (q.includes("opus-4-5")) return "Opus 4.5";
   if (q.includes("opus-4-1")) return "Opus 4.1";
   if (q.includes("opus-4")) return "Opus 4";
   return null;

@@@ function 'k31' (was 'j31') — structural (75.8%)
--- pretty-v2.1.31.js:388097
+++ pretty-v2.1.32.js:387537
@@ -1,11 +1,12 @@
 function j31(A) {
-  let q = t(33),
+  let q = A1(34),
     {
       addMargin: K,
       param: Y,
       verbose: z,
       thinkingMetadata: w,
       planContent: H,
+      isTranscriptMode: O,
     } = A;
   if (Y.text.trim() === _v) return null;
   if (H) {
@@ -100,35 +101,40 @@
   }
   if (U8() && Y.text.includes(`<${Q_}`)) {
     let $;
-    if (q[23] !== K || q[24] !== Y)
-      (($ = Bw.createElement(DI4, { addMargin: K, param: Y })),
+    if (q[23] !== K || q[24] !== O || q[25] !== Y)
+      ((_ = dw.createElement(Ox4, {
+        addMargin: K,
+        param: Y,
+        isTranscriptMode: O,
+      })),
         (q[23] = K),
         (q[24] = Y),
-        (q[25] = $));
-    else $ = q[25];
+        (q[25] = Y),
+        (q[26] = _));
+    else _ = q[26];
     return $;
   }
   if (Y.text.includes(`<${F_}`)) {
     let $;
-    if (q[26] !== K || q[27] !== Y)
+    if (q[27] !== K || q[28] !== Y)
       (($ = Bw.createElement(MI4, { addMargin: K, param: Y })),
-        (q[26] = K),
         (q[27] = Y),
-        (q[28] = $));
-    else $ = q[28];
+        (q[28] = Y),
+        (q[29] = _));
+    else _ = q[29];
     return $;
   }
   let O;
-  if (q[29] !== K || q[30] !== Y || q[31] !== w)
+  if (q[30] !== K || q[31] !== Y || q[32] !== w)
     ((O = Bw.createElement(lh4, {
       addMargin: K,
       param: Y,
       thinkingMetadata: w,
     })),
-      (q[29] = K),
       (q[30] = Y),
       (q[31] = w),
-      (q[32] = O));
-  else O = q[32];
+      (q[32] = w),
+      (q[33] = $));
+  else $ = q[33];
   return O;
 }

@@@ variable 'SHA' (was 'MjA') — structural (75.8%)
--- pretty-v2.1.31.js:299282
+++ pretty-v2.1.32.js:239503
@@ -1,6 +1,7 @@
 var MjA = E(() => {
   f7();
   uA();
+  FA();
   gU9 = [
     "You've hit your",
     "You've used",

@@@ variable 'C31' (was 'G31') — structural (75.8%)
--- pretty-v2.1.31.js:390310
+++ pretty-v2.1.32.js:389846
@@ -18,6 +18,7 @@
   FI4();
   gI4();
   aKA();
+  Sx4();
   K9 = o(J1(), 1);
   Dv = K9.memo(NWY, EWY);
 });

@@@ function 'nKq' (was 'Eqq') — structural (75.7%)
--- pretty-v2.1.31.js:485646
+++ pretty-v2.1.32.js:485414
@@ -13,10 +13,14 @@
       agentName: J,
     } = w.current,
     X = q ?? J,
+    D = df6(),
     D = kf6();
-  Rf6.useEffect(() => {
+  (sU1.useEffect(() => {
     if (D) Lf6();
-  }, [D]);
+  }, [D]),
+    sU1.useEffect(() => {
+      if (j && !D) QZ6();
+    }, [j, D]));
   let j = Math.max(A - 15, 20),
     W = CY(H, Math.max(j - "Claude Code v".length, 6)),
     { shouldSplit: P, truncatedModel: G, truncatedBilling: f } = wqq($, _, j),
@@ -47,6 +51,7 @@
         : s4.createElement(Z, { dimColor: !0 }, G, " · ", f),
       s4.createElement(Z, { dimColor: !0 }, X ? `@${X} · ${k}` : k),
       D && s4.createElement(vqq, null),
+      !D && j && r4.createElement(V6q, { variant: j }),
     ),
   );
 }

@@@ function 't_q' (was '$$q') — structural (75.6%)
--- pretty-v2.1.31.js:535699
+++ pretty-v2.1.32.js:535884
@@ -21,10 +21,10 @@
                 "report the issue at https://github.com/anthropics/claude-code/issues",
               PACKAGE_URL: "@anthropic-ai/claude-code",
               README_URL: "https://code.claude.com/docs/en/overview",
-              VERSION: "2.1.31",
+              VERSION: "2.1.32",
               FEEDBACK_CHANNEL:
                 "https://github.com/anthropics/claude-code/issues",
-              BUILD_TIME: "2026-02-04T00:00:54Z",
+              BUILD_TIME: "2026-02-05T17:02:01Z",
             }.VERSION,
             G,
             { loose: !0 },
@@ -32,7 +32,7 @@
           !IM1(G);
       if ((z(!!f), f))
         I(
-          `PackageManagerAutoUpdater: Update available ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.31", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-04T00:00:54Z" }.VERSION} -> ${G}`,
+          `PackageManagerAutoUpdater: Update available ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION} -> ${P}`,
         );
     }),
       (q[0] = O));
@@ -70,9 +70,9 @@
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.31",
+          VERSION: "2.1.32",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-02-04T00:00:54Z",
+          BUILD_TIME: "2026-02-05T17:02:01Z",
         }.VERSION,
       )),
       (q[3] = K),

@@@ variable 'hj6' (was 'Xj6') — structural (75.4%)
--- pretty-v2.1.31.js:421552
+++ pretty-v2.1.32.js:421109
@@ -31,36 +31,33 @@
   lTA();
   Tk();
   N0();
+  E0();
   ((mkA = o(J1(), 1)),
     (AW6 = M6(process.env.CLAUDE_CODE_DISABLE_BACKGROUND_TASKS)),
     (oEY = b.object({
-      description: b
-        .string()
-        .describe("A short (3-5 word) description of the task"),
+      description: B.string().describe(
+        "A short (3-5 word) description of the task",
+      ),
       prompt: b.string().describe("The task for the agent to perform"),
-      subagent_type: b
-        .string()
-        .describe("The type of specialized agent to use for this task"),
-      model: b
-        .enum(["sonnet", "opus", "haiku"])
+      subagent_type: B.string().describe(
+        "The type of specialized agent to use for this task",
+      ),
+      model: B.enum(["sonnet", "opus", "haiku"])
         .optional()
         .describe(
           "Optional model to use for this agent. If not specified, inherits from parent. Prefer haiku for quick, straightforward tasks to minimize cost and latency.",
         ),
-      resume: b
-        .string()
+      resume: B.string()
         .optional()
         .describe(
           "Optional agent ID to resume from. If provided, the agent will continue from the previous execution transcript.",
         ),
-      run_in_background: b
-        .boolean()
+      run_in_background: B.boolean()
         .optional()
         .describe(
           `Set to true to run this agent in the background. The tool result will include an output_file path - use ${Pq} tool or ${Q7} tail to check on output.`,
         ),
-      max_turns: b
-        .number()
+      max_turns: B.number()
         .int()
         .positive()
         .optional()
@@ -70,8 +67,7 @@
     })),
     (aEY = b.object({
       name: b.string().optional().describe("Name for the spawned agent"),
-      team_name: b
-        .string()
+      team_name: B.string()
         .optional()
         .describe(
           "Team name for spawning. Uses current team context if omitted.",
@@ -95,19 +91,15 @@
         output_tokens: b.number(),
         cache_creation_input_tokens: b.number().nullable(),
         cache_read_input_tokens: b.number().nullable(),
-        server_tool_use: b
-          .object({
-            web_search_requests: b.number(),
-            web_fetch_requests: b.number(),
-          })
-          .nullable(),
+        server_tool_use: B.object({
+          web_search_requests: B.number(),
+          web_fetch_requests: B.number(),
+        }).nullable(),
         service_tier: b.enum(["standard", "priority", "batch"]).nullable(),
-        cache_creation: b
-          .object({
-            ephemeral_1h_input_tokens: b.number(),
-            ephemeral_5m_input_tokens: b.number(),
-          })
-          .nullable(),
+        cache_creation: B.object({
+          ephemeral_1h_input_tokens: B.number(),
+          ephemeral_5m_input_tokens: B.number(),
+        }).nullable(),
       }),
     })),
     (tEY = sEY.extend({ status: b.literal("completed"), prompt: b.string() })),
@@ -116,9 +108,9 @@
       agentId: b.string().describe("The ID of the async agent"),
       description: b.string().describe("The description of the task"),
       prompt: b.string().describe("The prompt for the agent"),
-      outputFile: b
-        .string()
-        .describe("Path to the output file for checking agent progress"),
+      outputFile: B.string().describe(
+        "Path to the output file for checking agent progress",
+      ),
     })),
     (AkY = b.union([tEY, eEY, MY4])));
   $W1 = {
@@ -186,6 +178,7 @@
           {
             name: O,
             prompt: A,
+            description: K,
             team_name: G,
             use_splitpane: !0,
             plan_mode_required: _ === "plan",
@@ -245,7 +238,7 @@
           );
         let c = await zW6(VV(z));
         if (!c) throw Error(`No transcript found for agent ID: ${z}`);
-        k = YW6(KW6(c));
+        k = CQ1(TW6(NW6(r)));
       }
       let y = N?.forkContext ? J.messages : void 0,
         B;
@@ -305,9 +298,16 @@
             setAppState: J.setAppState,
             parentAbortController: J.abortController,
           }),
-          q1 = { agentId: r, parentSessionId: di(), agentType: "subagent" };
+          z1 = {
+            agentId: n,
+            parentSessionId: Yn(),
+            agentType: "subagent",
+            subagentName: N.agentType,
+            isBuiltIn: tD(N),
+          };
         return (
           sO1(q1, async () => {
+            let f1;
             try {
               let H1 = [],
                 $1 = ob1(),
@@ -319,10 +319,22 @@
                   agentId: VV(c.agentId),
                   abortController: c.abortController,
                 },
+                onCacheSafeParams: b
+                  ? (w1) => {
+                      let { stop: V1 } = cx4(
+                        r.agentId,
+                        zZ(r.agentId),
+                        w1,
+                        J.setAppState,
+                      );
+                      f1 = V1;
+                    }
+                  : void 0,
               }))
                 (H1.push(w1),
                   lD1($1, w1, A1, J.options.tools),
                   FDA(c.agentId, ab1($1), J.setAppState));
+              f1?.();
               let O1 = ukA(H1, c.agentId, m),
                 s = O1.content
                   .filter((w1) => w1.type === "text")
@@ -335,9 +347,9 @@
                   durationMs: O1.totalDurationMs,
                 }));
             } catch (H1) {
-              if (H1 instanceof Qz) {
-                (Qq1(c.agentId, J.setAppState),
-                  gq1(c.agentId, K, "killed", void 0, J.setAppState));
+              if ((f1?.(), Z1 instanceof Z2)) {
+                if (va(r.agentId, J.setAppState))
+                  qK1(r.agentId, K, "killed", void 0, J.setAppState);
                 return;
               }
               let $1 = H1 instanceof Error ? H1.message : String(H1);
@@ -358,7 +370,13 @@
         );
       } else {
         let r = z ? VV(z) : mL(),
-          c = { agentId: r, parentSessionId: di(), agentType: "subagent" };
+          r = {
+            agentId: n,
+            parentSessionId: Yn(),
+            agentType: "subagent",
+            subagentName: N.agentType,
+            isBuiltIn: tD(N),
+          };
         return sO1(c, async () => {
           let q1 = [],
             H1 = [],
@@ -461,8 +479,8 @@
                           }));
                       } catch (N1) {
                         if (N1 instanceof Qz) {
-                          (Qq1(G1, J.setAppState),
-                            gq1(G1, K, "killed", void 0, J.setAppState));
+                          if (va(O1, J.setAppState))
+                            qK1(O1, K, "killed", void 0, J.setAppState);
                           return;
                         }
                         let R1 = N1 instanceof Error ? N1.message : String(N1);

@@@ function 'Rs4' (was 'ka4') — structural (75.1%)
--- pretty-v2.1.31.js:446532
+++ pretty-v2.1.32.js:446481
@@ -29,6 +29,7 @@
           V(
             new VF(
               `MCP server "${q}" tool "${K}" timed out after ${Math.floor(J / 1000)}s`,
+              "MCP tool timeout",
             ),
           );
         }, J);
@@ -61,10 +62,7 @@
         let V = j.content[0];
         if (V && typeof V === "object" && "text" in V) f = V.text;
       } else if ("error" in j) f = String(j.error);
-      throw (
-        Pz(q, f),
-        new VF(f, `MCP server "${q}" tool "${K}": returned error`)
-      );
+      throw (Gz(q, V), new FE(V, "MCP tool returned error"));
     }
     let M = Date.now() - O,
       W =

@@@ function 'P86' (was 'cA6') — structural (75.1%)
--- pretty-v2.1.31.js:146665
+++ pretty-v2.1.32.js:146592
@@ -16,14 +16,8 @@
       let D = Math.trunc(H / J);
       if (K === "narrow")
         return H < 0 ? `${Math.abs(D)}${X} ago` : `in ${D}${X}`;
-      return new Intl.RelativeTimeFormat("en", {
-        style: "long",
-        numeric: Y,
-      }).format(D, _);
+      return $6A("long", Y).format(X, $);
     }
   if (K === "narrow") return H <= 0 ? "0s ago" : "in 0s";
-  return new Intl.RelativeTimeFormat("en", { style: K, numeric: Y }).format(
-    0,
-    "second",
-  );
+  return $6A(K, Y).format(0, "second");
 }

@@@ function 'WP' (was 'OG') — structural (75.0%)
--- pretty-v2.1.31.js:169091
+++ pretty-v2.1.32.js:169206
@@ -2,6 +2,6 @@
   if (process.env.CLAUDE_CODE_TASK_LIST_ID)
     return process.env.CLAUDE_CODE_TASK_LIST_ID;
   let A = Nk();
-  if (A) return A.parentSessionId;
-  return R5() || F6();
+  if (A) return A.teamName;
+  return u5() || $4A || u6();
 }

@@@ function 'o06' (was 'V06') — structural (75.0%)
--- pretty-v2.1.31.js:357736
+++ pretty-v2.1.32.js:358195
@@ -12,9 +12,6 @@
       K === "shutdown_approved" ||
       K === "team_permission_update" ||
       K === "mode_set_request" ||
-      K === "join_request" ||
-      K === "join_approved" ||
-      K === "join_rejected" ||
       K === "plan_approval_request" ||
       K === "plan_approval_response"
     );

@@@ function 'pQ1' (was 'jW6') — structural (75.0%)
--- pretty-v2.1.31.js:517187
+++ pretty-v2.1.32.js:516870
@@ -1,4 +1,4 @@
-function jW6(A, q, K) {
+function pQ1(A, q, K, Y, z) {
   return {
     type: "system",
     subtype: "compact_boundary",
@@ -7,7 +7,12 @@
     timestamp: new Date().toISOString(),
     uuid: LZ(),
     level: "info",
-    compactMetadata: { trigger: A, preTokens: q },
+    compactMetadata: {
+      trigger: A,
+      preTokens: q,
+      userContext: Y,
+      messagesSummarized: z,
+    },
     ...(K ? { logicalParentUuid: K } : {}),
   };
 }

@@@ function 'Q06' (was 'X06') — structural (74.8%)
--- pretty-v2.1.31.js:355891
+++ pretty-v2.1.32.js:356390
@@ -11,7 +11,7 @@
         w = null;
       function H() {
         let X = OG(),
-          D = JD(X);
+          D = $D(X).filter((M) => !M.metadata?._internal);
         sB1 = D;
         let j = D.some((M) => M.status !== "completed");
         if (j || D.length === 0) {
@@ -40,7 +40,7 @@
           w = ROY(J, O);
         } catch {}
       return () => {
-        if (($(), w)) w.close();
+        if (((IM1 = void 0), (aK1 = null), $(), w)) w.close();
         if (z) clearTimeout(z);
         if (Y) clearTimeout(Y);
         if (K) clearTimeout(K);

@@@ function 'CmA' (was 'aBA') — structural (74.7%)
--- pretty-v2.1.31.js:546197
+++ pretty-v2.1.32.js:546483
@@ -18,11 +18,20 @@
     W = T6((U) => U.queuedCommands.length),
     P = void 0,
     G = T6((U) => U.viewSelectionMode),
+    V = T6((g) =>
+      Object.values(g.tasks).some(
+        (x) => x.type === "local_agent" && x.status === "running",
+      ),
+    ),
     f = EXq.useCallback(() => {
       if (w !== void 0 && !w.aborted) {
         (n("tengu_cancel", {}), q(() => []), K());
         return;
       }
+      if (h9() && V) {
+        (c("tengu_cancel", {}), q(() => []), K());
+        return;
+      }
       if (j.getState().queuedCommands.length > 0) {
         if (H) {
           H();
@@ -30,7 +39,7 @@
         }
       }
       (n("tengu_cancel", {}), q(() => []), K());
-    }, [j, M, w, H, q, K]),
+    }, [j, M, w, H, q, K, V]),
     V = tZ7(),
     N = w !== void 0 && !w.aborted,
     T = W > 0,
@@ -45,7 +54,7 @@
       !V &&
       G !== "viewing-agent" &&
       !(Tt() && O === "INSERT") &&
-      (N || T || y),
+      (T || k || u || V),
     m = C && !k,
     u = y || C;
   return (

@@@ variable 'd41' (was 'Y71') — structural (74.7%)
--- pretty-v2.1.31.js:193738
+++ pretty-v2.1.32.js:250233
@@ -32,7 +32,7 @@
         : "Install Shift+Enter key binding for newlines",
     isEnabled: () => !0,
     isHidden: Gl5(),
-    async call(A, q) {
+    async call(A, q, K) {
       if (xA.terminal && xA.terminal in WC1) {
         let Y = `Shift+Enter is natively supported in ${WC1[xA.terminal]}.

@@@ variable 'QpY' (was 'Ge4') — structural (74.6%)
--- pretty-v2.1.31.js:457112
+++ pretty-v2.1.32.js:456952
@@ -1,36 +1,19 @@
-var Ge4 = E(() => {
-  Ap();
-  D8();
-  rz();
-  ((rgY = {
-    type: "local",
-    name: "copy",
-    description: "Copy Claude's last response to clipboard as markdown",
-    isEnabled: () => !0,
-    isHidden: !1,
-    supportsNonInteractive: !1,
-    async call(A, q) {
-      U4("copy");
-      let K = rV(q.messages);
-      if (!K) return { type: "text", value: "No assistant message to copy" };
-      let Y = K.message.content;
-      if (!Array.isArray(Y) || Y.length === 0)
-        return { type: "text", value: "No content to copy" };
-      let z = ngY(Y);
-      if (!z) return { type: "text", value: "No text content to copy" };
-      if (await dW(z)) {
-        let H = z.split(`
+var QpY = async (A, q) => {
+  B4("copy");
+  let K = HN(q.messages);
+  if (!K) return { type: "text", value: "No assistant message to copy" };
+  let Y = K.message.content;
+  if (!Array.isArray(Y) || Y.length === 0)
+    return { type: "text", value: "No content to copy" };
+  let z = FpY(Y);
+  if (!z) return { type: "text", value: "No text content to copy" };
+  if (await zG(z)) {
+    let H = z.split(`
 `).length;
-        return {
-          type: "text",
-          value: `Copied to clipboard (${z.length} characters, ${H} lines)`,
-        };
-      }
-      return { type: "text", value: Mj1() };
-    },
-    userFacingName() {
-      return "copy";
-    },
-  }),
-    (Pe4 = rgY));
-});
+    return {
+      type: "text",
+      value: `Copied to clipboard (${z.length} characters, ${H} lines)`,
+    };
+  }
+  return { type: "text", value: hj1() };
+};

@@@ variable 'O$1' (was 'GL1') — structural (74.6%)
--- pretty-v2.1.31.js:146987
+++ pretty-v2.1.32.js:146916
@@ -25,6 +25,13 @@
       webSearchRequests: 0.01,
     }),
     (Q1A = {
+      inputTokens: 10,
+      outputTokens: 37.5,
+      promptCacheWriteTokens: 12.5,
+      promptCacheReadTokens: 1,
+      webSearchRequests: 0.01,
+    }),
+    (W6A = {
       inputTokens: 6,
       outputTokens: 22.5,
       promptCacheWriteTokens: 7.5,
@@ -44,16 +51,17 @@
       promptCacheWriteTokens: 1.25,
       promptCacheReadTokens: 0.1,
       webSearchRequests: 0.01,
-    }),
-    (rA6 = {
-      [HD(Uk1.firstParty)]: g1A,
-      [HD(pk1.firstParty)]: U1A,
-      [HD(gk1.firstParty)]: tA1,
-      [HD(Qk1.firstParty)]: tA1,
-      [HD(hA1.firstParty)]: tA1,
-      [HD(dk1.firstParty)]: PL1,
-      [HD(ck1.firstParty)]: nA6,
-      [HD(lk1.firstParty)]: nA6,
-      [HD(IA1.firstParty)]: PL1,
     }));
+  N86 = {
+    [K0(qL1.firstParty)]: G6A,
+    [K0(KL1.firstParty)]: P6A,
+    [K0(AL1.firstParty)]: H81,
+    [K0(ek1.firstParty)]: H81,
+    [K0(QA1.firstParty)]: H81,
+    [K0(YL1.firstParty)]: H$1,
+    [K0(zL1.firstParty)]: V86,
+    [K0(wL1.firstParty)]: V86,
+    [K0(HL1.firstParty)]: H$1,
+    [K0(gA1.firstParty)]: H$1,
+  };
 });

@@@ function 'J81' (was 'q81') — structural (74.4%)
--- pretty-v2.1.31.js:147425
+++ pretty-v2.1.32.js:147386
@@ -1,5 +1,5 @@
-function q81() {
-  let A = EV5(),
+function J81(A = !1) {
+  let q = _T5(A),
     q = null,
     K = A86(),
     Y = Qf1();
@@ -10,7 +10,8 @@
   if (!q7() && l1A(q))
     if (q === "sonnet") A.push(c1A());
     else if (q === "sonnet[1m]") A.push(H27());
-    else if (q === "opus") A.push(O27());
+    else if (K === "opus[1m]") q.push(d27(A));
+    else if (K === "opus") q.push(U27(A));
     else if (q === "haiku") A.push(NV5());
     else A.push({ value: q, label: q, description: "Custom model" });
   else A.push({ value: q, label: q, description: "Custom model" });

@@@ function 'V54' (was 'q34') — structural (74.4%)
--- pretty-v2.1.31.js:293307
+++ pretty-v2.1.32.js:295142
@@ -8,7 +8,7 @@
       if (hI(H, $, w)) return O;
       try {
         let J = H.readFileSync($, { encoding: "utf-8" }),
-          { frontmatter: X, content: D } = z0(J),
+          { frontmatter: X, content: D } = H0(J, $),
           j = `${q}:${yD1(A)}`,
           M = { filePath: $, baseDir: Ya($), frontmatter: X, content: D },
           W = ub1(j, M, K, Y, z, !0, { isSkillMode: !0 });
@@ -27,7 +27,7 @@
         if (hI(H, D, w)) continue;
         try {
           let j = H.readFileSync(D, { encoding: "utf-8" }),
-            { frontmatter: M, content: W } = z0(j),
+            { frontmatter: M, content: W } = H0(j, D),
             P = `${q}:${J.name}`,
             G = { filePath: D, baseDir: Ya(D), frontmatter: M, content: W },
             f = ub1(P, G, K, Y, z, !0, { isSkillMode: !0 });

@@@ function 'ZRY' (was 'WkY') — structural (74.2%)
--- pretty-v2.1.31.js:423003
+++ pretty-v2.1.32.js:422588
@@ -16,7 +16,8 @@
     switch ($.type) {
       case "local-jsx":
         return new Promise((_) => {
-          $.call(
+          HG1(
+            $,
             (J, X) => {
               if (X?.display === "skip") {
                 _({ messages: [], shouldQuery: !1, command: $ });
@@ -76,7 +77,7 @@
         });
         try {
           let J = bM(),
-            X = await $.call(q, Y);
+            X = await od4($, q, Y);
           if (X.type === "skip")
             return { messages: [], shouldQuery: !1, command: $ };
           if (X.type === "compact") {

@@@ function 'mT5' (was 'oV5') — structural (74.2%)
--- pretty-v2.1.31.js:148293
+++ pretty-v2.1.32.js:148283
@@ -24,5 +24,7 @@
     agent_id: "",
     parent_session_id: "",
     agent_type: "",
+    slack: void 0,
+    team_name: "",
   };
 }

@@@ variable 'Pn7' (was 'fT7') — structural (74.2%)
--- pretty-v2.1.31.js:203077
+++ pretty-v2.1.32.js:254143
@@ -6,6 +6,7 @@
   D8();
   F4();
   VJ1();
+  j3();
   bC1 = o(J1(), 1);
   ZT7 = fg.renderToolResultMessage;
 });

@@@ variable 'Qf6' (was 'Vf6') — structural (74.2%)
--- pretty-v2.1.31.js:485070
+++ pretty-v2.1.32.js:484774
@@ -7,6 +7,7 @@
   f7();
   e7();
   C8();
+  R8();
   t4q = o(CC(), 1);
   vU1 = [];
 });

@@@ variable 'HN6' (was 'gV6') — structural (74.2%)
--- pretty-v2.1.31.js:523820
+++ pretty-v2.1.32.js:523583
@@ -7,6 +7,7 @@
   gW();
   tA();
   g6();
+  F6();
   nG1 = new Set();
   rG1 = { initialize: MKz, dispose: mwq, subscribe: WKz, resetForTesting: GKz };
 });

@@@ function 'TyY' (was 'RLY') — structural (74.1%)
--- pretty-v2.1.31.js:426252
+++ pretty-v2.1.32.js:425973
@@ -2,6 +2,9 @@
   if (q === "session_memory" || q === "compact") return !1;
   if (!qd()) return !1;
   let K = GS(A),
-    { isAboveAutoCompactThreshold: Y } = Ad(K);
+    Y = rm1(),
+    z = A51();
+  h(`autocompact: tokens=${K} threshold=${Y} effectiveWindow=${z}`);
+  let { isAboveAutoCompactThreshold: w } = jd(K);
   return Y;
 }

@@@ function 'Ns' (was 'Js') — structural (73.9%)
--- pretty-v2.1.31.js:362965
+++ pretty-v2.1.32.js:363333
@@ -5,18 +5,18 @@
         "report the issue at https://github.com/anthropics/claude-code/issues",
       PACKAGE_URL: "@anthropic-ai/claude-code",
       README_URL: "https://code.claude.com/docs/en/overview",
-      VERSION: "2.1.31",
+      VERSION: "2.1.32",
       FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-      BUILD_TIME: "2026-02-04T00:00:54Z",
+      BUILD_TIME: "2026-02-05T17:02:01Z",
     }.VERSION
       ? {
           ISSUES_EXPLAINER:
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.31",
+          VERSION: "2.1.32",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-02-04T00:00:54Z",
+          BUILD_TIME: "2026-02-05T17:02:01Z",
         }.VERSION
       : "unknown",
     K = await n_Y(),
@@ -40,23 +40,23 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.31",
+            VERSION: "2.1.32",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-02-04T00:00:54Z",
+            BUILD_TIME: "2026-02-05T17:02:01Z",
           }.PACKAGE_URL &&
           {
             ISSUES_EXPLAINER:
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.31",
+            VERSION: "2.1.32",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-02-04T00:00:54Z",
+            BUILD_TIME: "2026-02-05T17:02:01Z",
           }.PACKAGE_URL !== "@anthropic-ai/claude-code"
         )
-          P += ` && npm -g uninstall ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.31", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-04T00:00:54Z" }.PACKAGE_URL}`;
+          G += ` && npm -g uninstall ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.PACKAGE_URL}`;
         w.push({
           issue: `Leftover npm global installation at ${W.path}`,
           fix: `Run: ${P}`,

@@@ function 'p6' — structural (73.9%)
--- pretty-v2.1.31.js:515596
+++ pretty-v2.1.32.js:515268
@@ -3,6 +3,7 @@
   isMeta: q,
   isVisibleInTranscriptOnly: K,
   isCompactSummary: Y,
+  summarizeMetadata: z,
   toolUseResult: z,
   mcpMeta: w,
   uuid: H,
@@ -19,6 +20,7 @@
     isMeta: q,
     isVisibleInTranscriptOnly: K,
     isCompactSummary: Y,
+    summarizeMetadata: z,
     uuid: H ?? LZ(),
     timestamp: $ ?? new Date().toISOString(),
     toolUseResult: z,

@@@ function '_Xz' (was 'U$z') — structural (73.9%)
--- pretty-v2.1.31.js:568767
+++ pretty-v2.1.32.js:568964
@@ -6,7 +6,7 @@
   ) {
     (Wq("cli_version_fast_path"),
       console.log(
-        `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.31", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-04T00:00:54Z" }.VERSION} (Claude Code)`,
+        `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION} (Claude Code)`,
       ));
     return;
   }
@@ -30,7 +30,9 @@
     return;
   }
   let q = A.includes("--tmux") || A.includes("--tmux=classic");
-  Wq("cli_before_main_import");
+  if (A.length === 1 && (A[0] === "--update" || A[0] === "--upgrade"))
+    process.argv = [process.argv[0], process.argv[1], "update"];
+  (pW7(), Vq("cli_before_main_import"));
   let { main: K } = await Promise.resolve().then(() => (GNq(), PNq));
   (Wq("cli_after_main_import"), await K(), Wq("cli_after_main_complete"));
 }

@@@ function 'LKz' (was 'X4z') — structural (73.7%)
--- pretty-v2.1.31.js:519230
+++ pretty-v2.1.32.js:518983
@@ -1,4 +1,5 @@
 function X4z(A) {
-  let q = nH(y6());
+  let q = wO(y6()),
+    K = zZ1(A);
   return A === q || A.startsWith(q + ZP);
 }

@@@ function 'nNA' (was 'GNA') — structural (73.3%)
--- pretty-v2.1.31.js:369065
+++ pretty-v2.1.32.js:368741
@@ -1,5 +1,4 @@
 function GNA({
-  frame: A,
   selectedIndex: q,
   isInSelectionMode: K,
   allIdle: Y,
@@ -38,20 +37,12 @@
           { bold: M, color: j ? "suggestion" : W },
           "team-lead",
         ),
-        !D &&
-          z &&
-          U3.createElement(
-            U3.Fragment,
-            null,
-            U3.createElement(Z, { dimColor: !0 }, ": "),
-            U3.createElement(Zp, { frame: A, messageColor: "claude" }),
-            U3.createElement(Z, { color: "claude" }, z, "…"),
-          ),
+        !X && Y && zY.createElement(f, { dimColor: !0 }, ": ", Y, "…"),
         !D && !z && H && U3.createElement(Z, { dimColor: !0 }, ": ", H),
         w !== void 0 &&
           w > 0 &&
           U3.createElement(Z, { dimColor: !M }, " ", "· ", pK(w), " tokens"),
-        M && U3.createElement(Z, null, " · ", Fm1),
+        j && zY.createElement(f, { dimColor: !0 }, " · ", zF1),
         j && !D && U3.createElement(Z, { dimColor: !0 }, " · enter to view"),
       ),
     X.map((f, V) =>
@@ -63,7 +54,6 @@
         isForegrounded: $ === f.id,
         allIdle: Y,
         showPreview: _,
-        frame: A,
       }),
     ),
     K && U3.createElement(dXY, { isSelected: P }),

@@@ function 'NP9' (was 'tHY') — structural (73.0%)
--- pretty-v2.1.31.js:354514
+++ pretty-v2.1.32.js:246718
@@ -5,7 +5,7 @@
     if (q.skipRetry) return q;
     if (K > jfA) return q;
     let Y = cU(K);
-    (I(`Remote settings: Retry ${K}/${jfA} after ${Y}ms`), await mS(Y));
+    (h(`Policy limits: Retry ${K}/${jOA} after ${Y}ms`), await WS(Y));
   }
   return q;
 }

@@@ function 'C_Y' (was 'MOY') — structural (73.0%)
--- pretty-v2.1.31.js:354813
+++ pretty-v2.1.32.js:355305
@@ -5,7 +5,7 @@
     if (q.skipRetry) return q;
     if (K > ffA) return q;
     let Y = cU(K);
-    (I(`Policy limits: Retry ${K}/${ffA} after ${Y}ms`), await mS(Y));
+    (h(`Remote settings: Retry ${K}/${qVA} after ${Y}ms`), await WS(Y));
   }
   return q;
 }

@@@ variable 'Yu1' (was 'Bb1') — structural (72.9%)
--- pretty-v2.1.31.js:293355
+++ pretty-v2.1.32.js:295190
@@ -72,7 +72,7 @@
             } else if (O.isFile() && w.endsWith(".md")) {
               if (hI(H, w, z)) continue;
               let $ = H.readFileSync(w, { encoding: "utf-8" }),
-                { frontmatter: _, content: J } = z0($),
+                { frontmatter: _, content: J } = H0($, w),
                 X,
                 D;
               if (Y.commandsMetadata) {
@@ -118,7 +118,10 @@
         for (let [w, H] of Object.entries(Y.commandsMetadata))
           if (H.content && !H.source)
             try {
-              let { frontmatter: O, content: $ } = z0(H.content),
+              let { frontmatter: O, content: $ } = H0(
+                  H.content,
+                  `<inline:${Y.name}:${w}>`,
+                ),
                 _ = {
                   ...O,
                   ...(H.description && { description: H.description }),

@@@ function 'Td4' (was 'Sp4') — structural (72.7%)
--- pretty-v2.1.31.js:420837
+++ pretty-v2.1.32.js:420398
@@ -1,8 +1,9 @@
 function Sp4(A) {
   switch (A.type) {
     case "message":
+      return `to @${A.recipient}`;
     case "broadcast":
-      return "";
+      return "to @team";
     case "shutdown_request":
       return `request shutdown: ${A.recipient}`;
     case "shutdown_response":

@@@ function 'JDY' (was 'oJY') — structural (72.4%)
--- pretty-v2.1.31.js:365531
+++ pretty-v2.1.32.js:365871
@@ -3,6 +3,7 @@
       identity: q,
       taskId: K,
       prompt: Y,
+      description: z,
       agentDefinition: z,
       teammateContext: w,
       toolUseContext: H,
@@ -52,12 +53,14 @@
       agentType: q.agentName,
       whenToUse: `In-process teammate: ${q.agentName}`,
       getSystemPrompt: () => W,
-      tools: z?.tools ?? ["*"],
+      tools: w?.tools
+        ? [...new Set([...w.tools, wB, BV, dS, eq1, AK1, aL])]
+        : ["*"],
       source: "projectSettings",
       permissionMode: "default",
     },
     G = [],
-    f = FVA("team-lead", Y),
+    Z = GNA("team-lead", Y, void 0, z),
     V = f,
     N = !1;
   _k4(q.parentSessionId, q.agentName);
@@ -160,7 +163,8 @@
                           "type" in Z1 &&
                           Z1.type === "tool_result"
                         ) {
-                          if (s) ((s = new Set(s)), s.delete(Z1.tool_use_id));
+                          if (V1)
+                            ((V1 = new Set(V1)), V1.delete(q1.tool_use_id));
                         }
                     }
                   }
@@ -188,18 +192,30 @@
         let $1 = vz({ content: tK1 });
         Ep(K, (A1) => ({ ...A1, messages: [...(A1.messages ?? []), $1] }), j);
       }
-      (Ep(
-        K,
-        ($1) => {
-          return (
-            $1.onIdleCallbacks?.forEach((A1) => A1()),
-            { ...$1, isIdle: !0, onIdleCallbacks: [] }
-          );
-        },
-        j,
-      ),
-        $k4(q.agentName, q.color, q.teamName),
-        I(`[inProcessRunner] ${q.agentId} finished prompt, waiting for next`));
+      let H1 = (await O.getAppState()).tasks[K],
+        D1 = H1?.type === "in_process_teammate" && H1.isIdle;
+      if (
+        (Sp(
+          K,
+          (e) => {
+            return (
+              e.onIdleCallbacks?.forEach((G1) => G1()),
+              { ...e, isIdle: !0, onIdleCallbacks: [] }
+            );
+          },
+          M,
+        ),
+        !D1)
+      )
+        HL4(q.agentName, q.color, q.teamName, {
+          idleReason: f1 ? "interrupted" : "available",
+          summary: Rm1(V),
+        });
+      else
+        h(
+          `[inProcessRunner] Skipping duplicate idle notification for ${q.agentName}`,
+        );
+      h(`[inProcessRunner] ${q.agentId} finished prompt, waiting for next`);
       let H1 = await rJY(q, O, K, H.getAppState, j, q.parentSessionId);
       switch (H1.type) {
         case "shutdown_request":
@@ -218,7 +234,7 @@
           )
             V = H1.message;
           else
-            ((V = FVA(H1.from, H1.message, H1.color)),
+            ((N = GNA(t.from, t.message, t.color, t.summary)),
               QVA(K, p6({ content: V }), j));
           break;
         case "aborted":
@@ -251,7 +267,11 @@
         },
         j,
       ),
-      $k4(q.agentName, q.color, q.teamName, void 0, "failed", k),
+      HL4(q.agentName, q.color, q.teamName, {
+        idleReason: "failed",
+        completedStatus: "failed",
+        failureReason: y,
+      }),
       { success: !1, error: k, messages: G }
     );
   }

@@@ variable 'HR4' (was 'oIA') — structural (72.4%)
--- pretty-v2.1.31.js:491861
+++ pretty-v2.1.32.js:368726
@@ -11,16 +11,5 @@
   EKq();
   F8();
   Uq1();
-  iD1();
-  Mh();
-  yKq();
-  N0();
-  Aq();
-  Bq();
-  wK();
-  Z3();
-  _6();
-  QU1();
-  Bu();
   ((_K = o(J1(), 1)), (i51 = o(J1(), 1)));
 });

@@@ variable 'sKq' (was 'qBA') — structural (72.4%)
--- pretty-v2.1.31.js:532890
+++ pretty-v2.1.32.js:485883
@@ -24,7 +24,5 @@
   AY();
   q2();
   pW();
-  ABA();
-  wp1();
   ((Y5 = o(J1(), 1)), (hR = o(J1(), 1)));
 });

@@@ variable 'XN6' (was 'A_q') — structural (72.4%)
--- pretty-v2.1.31.js:537960
+++ pretty-v2.1.32.js:527163
@@ -16,8 +16,5 @@
   Gw();
   A2();
   yb();
-  u1();
-  c9();
-  bb1();
   ((cw = o(J1(), 1)), (TBA = o(J1(), 1)));
 });

@@@ variable 'xBA' (was 'Q_q') — structural (72.4%)
--- pretty-v2.1.31.js:540239
+++ pretty-v2.1.32.js:532946
@@ -19,5 +19,15 @@
   Aq();
   Q4();
   uA();
+  PV();
+  KG1();
+  Zd();
+  a9();
+  Ez();
+  YG();
+  IBA();
+  Sp1();
+  vL();
+  Go();
   ((a7 = o(J1(), 1)), (vN6 = o(J1(), 1)));
 });

@@@ variable 'd_q' (was 'jGq') — structural (72.4%)
--- pretty-v2.1.31.js:552667
+++ pretty-v2.1.32.js:535513
@@ -2,5 +2,15 @@
   p1();
   u1();
   A2();
+  x7();
+  CBA();
+  k5();
+  Cq();
+  hq();
+  Tq();
+  LK();
+  g_q();
+  KO();
+  Wq();
   ((Xj = o(J1(), 1)), (XGq = o(J1(), 1)));
 });

@@@ variable 'SXq' (was 'fZq') — structural (72.4%)
--- pretty-v2.1.31.js:554092
+++ pretty-v2.1.32.js:540448
@@ -2,5 +2,23 @@
   p1();
   u1();
   s6();
+  ZP1();
+  Lw();
+  yj();
+  MXq();
+  Jd1();
+  N9();
+  GXq();
+  Ch();
+  Q8();
+  ZXq();
+  VXq();
+  EXq();
+  Tq();
+  Cq();
+  Wq();
+  j3();
+  g4();
+  FA();
   ((ZZq = o(J1(), 1)), (yHz = o(J1(), 1)));
 });

@@@ variable 'IXq' (was 'ImA') — structural (72.4%)
--- pretty-v2.1.31.js:555785
+++ pretty-v2.1.32.js:540597
@@ -15,136 +15,5 @@
   Kw();
   Mh();
   Xm1();
-  Nz();
-  IHq();
-  Mh();
-  Wa();
-  uHq();
-  lV6();
-  pHq();
-  nOq();
-  eOq();
-  KXq();
-  zXq();
-  _Xq();
-  DXq();
-  jXq();
-  q2();
-  ZNA();
-  mV();
-  dP6();
-  gT();
-  vD();
-  uuA();
-  Zk();
-  nBA();
-  ZXq();
-  hC();
-  VXq();
-  TXq();
-  vXq();
-  XB();
-  Gw();
-  kXq();
-  RXq();
-  xXq();
-  BXq();
-  iXq();
-  bH();
-  qBA();
-  GbA();
-  uA();
-  g6();
-  D8();
-  Hr();
-  Wz();
-  nU();
-  Sw();
-  K0q();
-  H0q();
-  $0q();
-  GP1();
-  F31();
-  X0q();
-  mTA();
-  kxA();
-  j0q();
-  W0q();
-  YmA();
-  LG1();
-  aB1();
-  CfA();
-  G0q();
-  SfA();
-  DC1();
-  as();
-  f0q();
-  N0();
-  nq1();
-  AF1();
-  F8();
-  bu();
-  xD();
-  yq();
-  NP1();
-  zP6();
-  p31();
-  zZ();
-  D71();
-  yq();
-  np1();
-  v0q();
-  c9();
-  E0q();
-  pH();
-  R0q();
-  UxA();
-  wZ6();
-  ZV();
-  S0q();
-  O$6();
-  I0q();
-  W31();
-  oQ1();
-  t9A();
-  yfA();
-  j2();
-  kt();
-  m0q();
-  Q0q();
-  p0q();
-  l0q();
-  n0q();
-  a0q();
-  t0q();
-  YDq();
-  HDq();
-  mH();
-  $Dq();
-  _Dq();
-  JGq();
-  lSA();
-  jGq();
-  WGq();
-  LGq();
-  CGq();
-  IGq();
-  bGq();
-  BGq();
-  wj6();
-  FGq();
-  UGq();
-  dGq();
-  lGq();
-  nGq();
-  aGq();
-  eGq();
-  KZq();
-  wZq();
-  OZq();
-  DZq();
-  jZq();
-  GZq();
-  fZq();
   ((G7 = o(J1(), 1)), (oA = o(J1(), 1)));
 });

@@@ variable 'oXq' (was 'dZq') — structural (72.4%)
--- pretty-v2.1.31.js:557004
+++ pretty-v2.1.32.js:541714
@@ -7,5 +7,18 @@
   UZq();
   g6();
   B5();
+  _6();
+  JM();
+  i_1();
+  uO();
+  hq();
+  Zv();
+  Ch();
+  JO();
+  JmA();
+  yj();
+  Q8();
+  I6();
+  ku();
   ((mR = o(J1(), 1)), (fZ1 = o(J1(), 1)));
 });

@@@ variable 'Ejq' (was 'Xfq') — structural (72.4%)
--- pretty-v2.1.31.js:558535
+++ pretty-v2.1.32.js:549386
@@ -9,6 +9,5 @@
   vG1();
   s6();
   hf6();
-  h6();
   ((HOz = o(J1(), 1)), (Jfq = o(J1(), 1)));
 });

@@@ function 'c3q' (was 'GKq') — structural (72.3%)
--- pretty-v2.1.31.js:490121
+++ pretty-v2.1.32.js:489857
@@ -2,14 +2,12 @@
   let [z, w] = FU1.useState(!1),
     [H, O] = FU1.useState(null),
     $ = () => K("Remote session details dismissed", { display: "system" });
-  (c7({ "confirm:no": $, "confirm:yes": $ }, { context: "Confirmation" }),
-    eA((W, P) => {
-      if (W === " ")
-        K("Remote session details dismissed", { display: "system" });
-      else if (P.leftArrow && Y) Y();
-      else if (W === "t" && !z) J();
-    }));
-  let _ = v7();
+  Y8((M, W) => {
+    if (M === " ") K("Remote session details dismissed", { display: "system" });
+    else if (W.leftArrow && Y) Y();
+    else if (M === "t" && !z) _();
+    else if (W.return) $();
+  });
   async function J() {
     (w(!0), O(null));
     try {
@@ -28,169 +26,25 @@
     D = FU1.useMemo(() => {
       return eH(WKq(A.log.slice(-3))).filter((W) => W.type !== "progress");
     }, [A]),
-    j = A.title.length > 50 ? A.title.substring(0, 47) + "..." : A.title,
+    D = A.title.length > 50 ? A.title.substring(0, 47) + "…" : A.title,
     M = A.status === "pending" ? "starting" : A.status;
   return x5.default.createElement(
     h,
-    { width: "100%", flexDirection: "column" },
-    x5.default.createElement(
-      h,
-      { width: "100%" },
-      x5.default.createElement(
-        h,
-        {
-          borderStyle: "round",
-          borderColor: "background",
-          flexDirection: "column",
-          marginTop: 1,
-          paddingLeft: 1,
-          paddingRight: 1,
-          width: "100%",
-        },
-        x5.default.createElement(
-          h,
-          null,
-          x5.default.createElement(
-            Z,
-            { color: "background", bold: !0 },
-            "Remote session details",
-          ),
-        ),
-        x5.default.createElement(
-          h,
-          { flexDirection: "column", marginTop: 1 },
-          x5.default.createElement(
-            Z,
-            null,
-            x5.default.createElement(Z, { bold: !0 }, "Status"),
-            ":",
-            " ",
-            M === "running" || M === "starting"
-              ? x5.default.createElement(Z, { color: "background" }, M)
-              : M === "completed"
-                ? x5.default.createElement(Z, { color: "success" }, M)
-                : x5.default.createElement(Z, { color: "error" }, M),
-          ),
-          x5.default.createElement(
-            Z,
-            null,
-            x5.default.createElement(Z, { bold: !0 }, "Runtime"),
-            ": ",
-            X(A.startTime),
-          ),
-          x5.default.createElement(
-            Z,
-            { wrap: "truncate-end" },
-            x5.default.createElement(Z, { bold: !0 }, "Title"),
-            ": ",
-            j,
-          ),
-          x5.default.createElement(
-            Z,
-            null,
-            x5.default.createElement(Z, { bold: !0 }, "Progress"),
-            ":",
-            " ",
-            x5.default.createElement(bf6, { session: A }),
-          ),
-          x5.default.createElement(
-            Z,
-            null,
-            x5.default.createElement(Z, { bold: !0 }, "Session URL"),
-            ":",
-            " ",
-            x5.default.createElement(
+    {
+      title: "Remote session details",
+      onCancel: $,
+      color: "background",
+      borderDimColor: !0,
+      inputGuide: (M) =>
+        M.pending
+          ? kY.default.createElement(
               A4,
-              { url: K51(A.sessionId) },
-              x5.default.createElement(Z, { dimColor: !0 }, K51(A.sessionId)),
-            ),
-          ),
-        ),
-        A.log.length > 0 &&
-          x5.default.createElement(
-            h,
-            { flexDirection: "column", marginTop: 1 },
-            x5.default.createElement(
               Z,
-              null,
-              x5.default.createElement(Z, { bold: !0 }, "Recent messages"),
-              ":",
-            ),
-            x5.default.createElement(
-              h,
-              { flexDirection: "column", height: 10, overflowY: "hidden" },
-              D.map((W, P) =>
-                x5.default.createElement(Dv, {
-                  key: P,
-                  message: W,
-                  lookups: kh,
-                  addMargin: P > 0,
-                  tools: q.options.tools,
-                  commands: q.options.commands,
-                  verbose: q.options.verbose,
-                  inProgressToolUseIDs: new Set(),
-                  progressMessagesForMessage: [],
-                  shouldAnimate: !1,
-                  shouldShowDot: !1,
-                  style: "condensed",
-                  isTranscriptMode: !1,
-                  isStatic: !0,
-                }),
-              ),
-            ),
-            x5.default.createElement(
-              h,
-              { marginTop: 1 },
-              x5.default.createElement(
-                Z,
-                { dimColor: !0, italic: !0 },
-                "Showing last ",
-                Math.min(3, A.log.length),
-                " of",
-                " ",
-                A.log.length,
-                " messages",
-              ),
-            ),
-          ),
-        H &&
-          x5.default.createElement(
-            h,
-            { marginTop: 1 },
-            x5.default.createElement(
-              Z,
-              { color: "error" },
-              "Teleport failed: ",
-              H,
-            ),
-          ),
-        z &&
-          x5.default.createElement(
-            h,
-            { marginTop: 1 },
-            x5.default.createElement(
-              Z,
-              { color: "background" },
-              "Teleporting to session...",
-            ),
-          ),
-      ),
-    ),
-    x5.default.createElement(
-      h,
-      { marginLeft: 2 },
-      _.pending
-        ? x5.default.createElement(
-            Z,
-            { dimColor: !0 },
-            "Press ",
-            _.keyName,
-            " again to exit",
-          )
-        : x5.default.createElement(
-            Z,
-            { dimColor: !0 },
-            x5.default.createElement(
+              "Press ",
+              M.keyName,
+              " again to exit",
+            )
+          : kY.default.createElement(
               nA,
               null,
               Y &&
@@ -208,7 +62,115 @@
                   action: "teleport",
                 }),
             ),
+    },
+    kY.default.createElement(
+      I,
+      { flexDirection: "column" },
+      kY.default.createElement(
+        f,
+        null,
+        kY.default.createElement(f, { bold: !0 }, "Status"),
+        ":",
+        " ",
+        j === "running" || j === "starting"
+          ? kY.default.createElement(f, { color: "background" }, j)
+          : j === "completed"
+            ? kY.default.createElement(f, { color: "success" }, j)
+            : kY.default.createElement(f, { color: "error" }, j),
+      ),
+      kY.default.createElement(
+        f,
+        null,
+        kY.default.createElement(f, { bold: !0 }, "Runtime"),
+        ": ",
+        J(A.startTime),
+      ),
+      kY.default.createElement(
+        f,
+        { wrap: "truncate-end" },
+        kY.default.createElement(f, { bold: !0 }, "Title"),
+        ": ",
+        D,
+      ),
+      kY.default.createElement(
+        f,
+        null,
+        kY.default.createElement(f, { bold: !0 }, "Progress"),
+        ":",
+        " ",
+        kY.default.createElement(sf6, { session: A }),
+      ),
+      kY.default.createElement(
+        f,
+        null,
+        kY.default.createElement(f, { bold: !0 }, "Session URL"),
+        ":",
+        " ",
+        kY.default.createElement(
+          q4,
+          { url: M51(A.sessionId) },
+          kY.default.createElement(f, { dimColor: !0 }, M51(A.sessionId)),
+        ),
+      ),
+    ),
+    A.log.length > 0 &&
+      kY.default.createElement(
+        I,
+        { flexDirection: "column", marginTop: 1 },
+        kY.default.createElement(
+          f,
+          null,
+          kY.default.createElement(f, { bold: !0 }, "Recent messages"),
+          ":",
+        ),
+        kY.default.createElement(
+          I,
+          { flexDirection: "column", height: 10, overflowY: "hidden" },
+          X.map((M, W) =>
+            kY.default.createElement(kv, {
+              key: W,
+              message: M,
+              lookups: Qh,
+              addMargin: W > 0,
+              tools: q.options.tools,
+              commands: q.options.commands,
+              verbose: q.options.verbose,
+              inProgressToolUseIDs: new Set(),
+              progressMessagesForMessage: [],
+              shouldAnimate: !1,
+              shouldShowDot: !1,
+              style: "condensed",
+              isTranscriptMode: !1,
+              isStatic: !0,
+            }),
           ),
-    ),
+        ),
+        kY.default.createElement(
+          I,
+          { marginTop: 1 },
+          kY.default.createElement(
+            f,
+            { dimColor: !0, italic: !0 },
+            "Showing last ",
+            Math.min(3, A.log.length),
+            " of",
+            " ",
+            A.log.length,
+            " messages",
+          ),
+        ),
+      ),
+    H &&
+      kY.default.createElement(
+        I,
+        { marginTop: 1 },
+        kY.default.createElement(f, { color: "error" }, "Teleport failed: ", H),
+      ),
+    z &&
+      kY.default.createElement(
+        f,
+        { color: "background" },
+        "Teleporting to session…",
+      ),
   );
 }

@@@ function 'j51' (was 'q51') — structural (72.1%)
--- pretty-v2.1.31.js:438624
+++ pretty-v2.1.32.js:438556
@@ -13,7 +13,9 @@
     let w = await Ox();
     if (!w)
       return (
-        e(Error("Unable to get organization UUID for remote session creation")),
+        K1(
+          Error("Unable to get organization UUID for remote session creation"),
+        ),
         null
       );
     let H = await Vh(),
@@ -36,11 +38,17 @@
     }
     let X = await TP1();
     if (!X || X.length === 0)
-      return (e(Error("No environments available for session creation")), null);
+      return (
+        K1(Error("No environments available for session creation")),
+        null
+      );
     let j = P8()?.remote?.defaultEnvironmentId,
       M = (j && X.find((B) => B.environment_id === j)) || X[0];
     if (!M)
-      return (e(Error("No environments available for session creation")), null);
+      return (
+        K1(Error("No environments available for session creation")),
+        null
+      );
     if (j) {
       let B = M.environment_id === j;
       I(

@@@ function 'WN6' (was 'oV6') — structural (71.9%)
--- pretty-v2.1.31.js:530817
+++ pretty-v2.1.32.js:530830
@@ -1,12 +1,6 @@
 function oV6(A) {
-  let q = t(59),
-    {
-      toolUseConfirm: K,
-      onDone: Y,
-      onReject: z,
-      verbose: w,
-      workerBadge: H,
-    } = A,
+  let q = A1(58),
+    { toolUseConfirm: K, onDone: Y, onReject: z, workerBadge: w } = A,
     [O] = M7(),
     $,
     _;
@@ -168,94 +162,93 @@
   else m = q[26];
   let u = m,
     U;
-  if (q[27] !== O || q[28] !== K.input || q[29] !== K.tool || q[30] !== w)
-    ((U = K.tool.renderToolUseMessage(K.input, { theme: O, verbose: w })),
+  if (q[27] !== H || q[28] !== K.input || q[29] !== K.tool)
+    ((b = K.tool.renderToolUseMessage(K.input, { theme: H, verbose: !0 })),
       (q[27] = O),
       (q[28] = K.input),
       (q[29] = K.tool),
-      (q[30] = w),
-      (q[31] = U));
-  else U = q[31];
+      (q[30] = b));
+  else b = q[30];
   let g;
-  if (q[32] !== $)
+  if (q[31] !== O)
     ((g = $.endsWith(" (MCP)")
       ? SR.default.createElement(Z, { dimColor: !0 }, " (MCP)")
       : ""),
-      (q[32] = $),
-      (q[33] = g));
-  else g = q[33];
+      (q[31] = O),
+      (q[32] = U));
+  else U = q[32];
   let x;
-  if (q[34] !== U || q[35] !== g || q[36] !== J)
+  if (q[33] !== b || q[34] !== U || q[35] !== _)
     ((x = SR.default.createElement(Z, null, J, "(", U, ")", g)),
+      (q[33] = b),
       (q[34] = U),
       (q[35] = g),
-      (q[36] = J),
-      (q[37] = x));
-  else x = q[37];
+      (q[36] = g));
+  else g = q[36];
   let d;
-  if (q[38] !== K.description)
-    ((d = Af7(K.description, 3)), (q[38] = K.description), (q[39] = d));
-  else d = q[39];
+  if (q[37] !== K.description)
+    ((x = fi7(K.description, 3)), (q[37] = K.description), (q[38] = x));
+  else x = q[38];
   let r;
-  if (q[40] !== d)
+  if (q[39] !== x)
     ((r = SR.default.createElement(Z, { dimColor: !0 }, d)),
-      (q[40] = d),
-      (q[41] = r));
-  else r = q[41];
+      (q[39] = x),
+      (q[40] = p));
+  else p = q[40];
   let c;
-  if (q[42] !== x || q[43] !== r)
+  if (q[41] !== g || q[42] !== p)
     ((c = SR.default.createElement(
       h,
       { flexDirection: "column", paddingX: 2, paddingY: 1 },
       x,
       r,
     )),
+      (q[41] = g),
       (q[42] = x),
-      (q[43] = r),
-      (q[44] = c));
-  else c = q[44];
+      (q[43] = n));
+  else n = q[43];
   let q1;
-  if (q[45] !== K.permissionResult)
+  if (q[44] !== K.permissionResult)
     ((q1 = SR.default.createElement(YN, {
       permissionResult: K.permissionResult,
       toolType: "tool",
     })),
-      (q[45] = K.permissionResult),
-      (q[46] = q1));
-  else q1 = q[46];
+      (q[44] = K.permissionResult),
+      (q[45] = r));
+  else r = q[45];
   let H1;
-  if (q[47] !== P || q[48] !== M || q[49] !== y || q[50] !== u)
+  if (q[46] !== W || q[47] !== j || q[48] !== k || q[49] !== m)
     ((H1 = SR.default.createElement(eG1, {
       options: y,
       onSelect: M,
       onCancel: P,
       toolAnalyticsContext: u,
     })),
+      (q[46] = W),
       (q[47] = P),
       (q[48] = M),
       (q[49] = y),
-      (q[50] = u),
-      (q[51] = H1));
-  else H1 = q[51];
+      (q[50] = z1));
+  else z1 = q[50];
   let $1;
-  if (q[52] !== q1 || q[53] !== H1)
+  if (q[51] !== r || q[52] !== z1)
     (($1 = SR.default.createElement(h, { flexDirection: "column" }, q1, H1)),
+      (q[51] = r),
       (q[52] = q1),
-      (q[53] = H1),
-      (q[54] = $1));
-  else $1 = q[54];
+      (q[53] = f1));
+  else f1 = q[53];
   let A1;
-  if (q[55] !== c || q[56] !== $1 || q[57] !== H)
+  if (q[54] !== n || q[55] !== f1 || q[56] !== w)
     ((A1 = SR.default.createElement(
       xw,
       { title: "Tool use", workerBadge: H },
       c,
       $1,
     )),
+      (q[54] = n),
       (q[55] = c),
       (q[56] = $1),
-      (q[57] = H),
-      (q[58] = A1));
-  else A1 = q[58];
+      (q[57] = Z1));
+  else Z1 = q[57];
   return A1;
 }

@@@ function '_uA' (was 'hbA') — structural (71.8%)
--- pretty-v2.1.31.js:515165
+++ pretty-v2.1.32.js:514837
@@ -15,7 +15,7 @@
         z.map(async (H) => {
           try {
             let O = await A7z(H, { encoding: "utf-8" }),
-              { frontmatter: $, content: _ } = z0(O);
+              { frontmatter: $, content: _ } = H0(O, H);
             return { filePath: H, frontmatter: $, content: _ };
           } catch (O) {
             let $ = O instanceof Error ? O.message : String(O);

@@@ function 'Je6' (was 'Qt6') — structural (71.4%)
--- pretty-v2.1.31.js:138323
+++ pretty-v2.1.32.js:138206
@@ -1,15 +1,16 @@
 function Qt6(A) {
   if (H4() === "foundry") return;
   let q = A.toLowerCase();
-  if (q.includes("claude-sonnet-4-5") && q.includes("[1m]"))
-    return "Sonnet 4.5 (with 1M context)";
-  if (q.includes("claude-sonnet-4-5")) return "Sonnet 4.5";
-  if (q.includes("claude-sonnet-4") && q.includes("[1m]"))
-    return "Sonnet 4 (with 1M context)";
-  if (q.includes("claude-sonnet-4")) return "Sonnet 4";
+  if (q.includes("claude-opus-4-6[1m]")) return "Opus 4.6 (with 1M context)";
+  if (q.includes("claude-opus-4-6")) return "Opus 4.6";
   if (q.includes("claude-opus-4-5")) return "Opus 4.5";
   if (q.includes("claude-opus-4-1")) return "Opus 4.1";
   if (q.includes("claude-opus-4")) return "Opus 4";
+  if (q.includes("claude-sonnet-4-5[1m]"))
+    return "Sonnet 4.5 (with 1M context)";
+  if (q.includes("claude-sonnet-4-5")) return "Sonnet 4.5";
+  if (q.includes("claude-sonnet-4[1m]")) return "Sonnet 4 (with 1M context)";
+  if (q.includes("claude-sonnet-4")) return "Sonnet 4";
   if (q.includes("claude-3-7-sonnet")) return "Claude 3.7 Sonnet";
   if (q.includes("claude-3-5-sonnet")) return "Claude 3.5 Sonnet";
   if (q.includes("claude-haiku-4-5")) return "Haiku 4.5";

@@@ function 'QT5' (was 'sV5') — structural (71.4%)
--- pretty-v2.1.31.js:148654
+++ pretty-v2.1.32.js:148698
@@ -10,6 +10,7 @@
     device_id: "",
     auth: void 0,
     session_id: "",
+    anonymous_id: "",
     event_metadata_vars: "",
   };
 }

@@@ function 'xG6' (was 'MP6') — structural (71.4%)
--- pretty-v2.1.31.js:518502
+++ pretty-v2.1.32.js:518235
@@ -6,13 +6,15 @@
         summaries: Y,
         customTitles: z,
         tags: w,
+        agentSettings: H,
         fileHistorySnapshots: H,
         attributionSnapshots: O,
       } = await cbA(A),
       $ = K ? Y.get(K.uuid) : void 0,
       _ = K ? z.get(K.sessionId) : void 0,
-      J = K ? w.get(K.sessionId) : void 0;
-    return mbA(q, 0, $, _, vV6(H, q), J, v_(A), EV6(O, q));
+      X = K ? w.get(K.sessionId) : void 0,
+      D = H.get(A);
+    return MuA(q, 0, _, J, dV6(O, q), X, oO(A), cV6($, q), D);
   }
   return null;
 }

@@@ variable 'ALA' (was 'RkA') — structural (71.2%)
--- pretty-v2.1.31.js:419576
+++ pretty-v2.1.32.js:419147
@@ -47,11 +47,14 @@
           Oy(K.toolPermissionContext.mode, "plan"),
           q.setAppState((Y) => ({
             ...Y,
-            toolPermissionContext: qz(Y.toolPermissionContext, {
-              type: "setMode",
-              mode: "plan",
-              destination: "session",
-            }),
+            toolPermissionContext: {
+              ...t2(Y.toolPermissionContext, {
+                type: "setMode",
+                mode: "plan",
+                destination: "session",
+              }),
+              prePlanMode: Y.toolPermissionContext.mode,
+            },
           })),
           {
             data: {

@@@ function 'f0q' (was 'yJq') — structural (71.2%)
--- pretty-v2.1.31.js:542919
+++ pretty-v2.1.32.js:543089
@@ -7,6 +7,6 @@
       return `Message @${K.length > LJq ? K.slice(0, LJq - 3) + "..." : K}…`;
     if (Y.length > 0 && (W6().queuedCommandUpHintCount || 0) < hzz)
       return "Press up to edit queued messages";
-    if (q < 1 && z) return EJq();
+    if (q < 1 && z && !twz?.isProactiveActive()) return W0q();
   }, [A, Y, q, z, K]);
 }

@@@ function 'w$1' (was 'iO1') — structural (70.8%)
--- pretty-v2.1.31.js:146721
+++ pretty-v2.1.32.js:146643
@@ -15,16 +15,15 @@
     return (
       Y.toLocaleString("en-US", _).replace(/ ([AP]M)/i, (X, D) =>
         D.toLowerCase(),
-      ) + (q ? ` (${Intl.DateTimeFormat().resolvedOptions().timeZone})` : "")
+      ) + (q ? ` (${_6A()})` : "")
     );
   }
-  let O = Y.toLocaleTimeString("en-US", {
+  return (
+    Y.toLocaleTimeString("en-US", {
       hour: "numeric",
       minute: w === 0 ? void 0 : "2-digit",
       hour12: !0,
-    }),
-    $ = Intl.DateTimeFormat().resolvedOptions().timeZone;
-  return (
-    O.replace(/ ([AP]M)/i, (_, J) => J.toLowerCase()) + (q ? ` (${$})` : "")
+    }).replace(/ ([AP]M)/i, ($, _) => _.toLowerCase()) +
+    (q ? ` (${_6A()})` : "")
   );
 }

@@@ function 'RG6' (was 'OP6') — structural (70.8%)
--- pretty-v2.1.31.js:434348
+++ pretty-v2.1.32.js:434238
@@ -6,6 +6,7 @@
     suggestion_length: Y,
     tools_executed: gRA(z),
     completed: w !== null,
+    coordinator_mode: h9(),
     boundary_type: w?.type,
     boundary_tool: RIY(w),
     boundary_detail: yIY(w),

@@@ function 'fd9' (was 'Pg9') — structural (70.8%)
--- pretty-v2.1.31.js:293152
+++ pretty-v2.1.32.js:294987
@@ -10,7 +10,7 @@
             let J = RD1(H, _.name);
             if (hI(z, J, K)) continue;
             let X = z.readFileSync(J, { encoding: "utf-8" }),
-              { frontmatter: D, content: j } = z0(X);
+              { frontmatter: D, content: j } = H0(X, J);
             Y.push({ filePath: J, baseDir: q, frontmatter: D, content: j });
           }
         return;
@@ -21,7 +21,7 @@
         else if (_.isFile() && _.name.toLowerCase().endsWith(".md")) {
           if (hI(z, J, K)) continue;
           let X = z.readFileSync(J, { encoding: "utf-8" }),
-            { frontmatter: D, content: j } = z0(X);
+            { frontmatter: D, content: j } = H0(X, J);
           Y.push({ filePath: J, baseDir: q, frontmatter: D, content: j });
         }
       }

@@@ function 'bW6' (was 'xd4') — structural (70.6%)
--- pretty-v2.1.31.js:425515
+++ pretty-v2.1.32.js:425234
@@ -2,5 +2,6 @@
   let A = x1(),
     q = U31();
   if (!A.existsSync(q)) return null;
-  return A.readFileSync(q, { encoding: "utf-8" });
+  let K = A.readFileSync(q, { encoding: "utf-8" });
+  return (c("tengu_session_memory_loaded", { content_length: K.length }), K);
 }

@@@ function 'B48' (was 'w48') — structural (70.5%)
--- pretty-v2.1.31.js:28094
+++ pretty-v2.1.32.js:28110
@@ -1,4 +1,5 @@
 function w48() {
+  if (process.env.CLAUDE_CODE_CUSTOM_OAUTH_URL) return "-custom-oauth";
   switch (z48()) {
     case "local":
       return "-local-oauth";

@@@ function 'J$1' (was 'oO1') — structural (70.4%)
--- pretty-v2.1.31.js:147176
+++ pretty-v2.1.32.js:147124
@@ -1,3 +1,8 @@
 function oO1(A) {
-  return A === j$().opus40 || A === j$().opus41 || A === j$().opus45;
+  return (
+    A === XH().opus40 ||
+    A === XH().opus41 ||
+    A === XH().opus45 ||
+    A === XH().opus46
+  );
 }

@@@ function 'VTq' (was 'BVq') — structural (70.3%)
--- pretty-v2.1.31.js:563045
+++ pretty-v2.1.32.js:563193
@@ -1,6 +1,6 @@
 async function BVq() {
   (n("tengu_update_check", {}),
-    f4(`Current version: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.31", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-04T00:00:54Z" }.VERSION}
+    k4(`Current version: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION}
 `));
   let A = Lq()?.autoUpdatesChannel ?? "latest";
   (f4(`Checking for updates to ${A} version...
@@ -92,16 +92,16 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.31",
+            VERSION: "2.1.32",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-02-04T00:00:54Z",
+            BUILD_TIME: "2026-02-05T17:02:01Z",
           }.VERSION,
           J,
           { loose: !0 },
         )
       )
-        (f4(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.31", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-04T00:00:54Z" }.VERSION} → ${J}
+        (k4(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION} → ${J}
 `),
           f4(`
 `),
@@ -127,16 +127,16 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.31",
+            VERSION: "2.1.32",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-02-04T00:00:54Z",
+            BUILD_TIME: "2026-02-05T17:02:01Z",
           }.VERSION,
           J,
           { loose: !0 },
         )
       )
-        (f4(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.31", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-04T00:00:54Z" }.VERSION} → ${J}
+        (k4(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION} → ${J}
 `),
           f4(`
 `),
@@ -162,16 +162,16 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.31",
+            VERSION: "2.1.32",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-02-04T00:00:54Z",
+            BUILD_TIME: "2026-02-05T17:02:01Z",
           }.VERSION,
           J,
           { loose: !0 },
         )
       )
-        (f4(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.31", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-04T00:00:54Z" }.VERSION} → ${J}
+        (k4(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION} → ${J}
 `),
           f4(`
 `),
@@ -253,14 +253,14 @@
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.31",
+          VERSION: "2.1.32",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-02-04T00:00:54Z",
+          BUILD_TIME: "2026-02-05T17:02:01Z",
         }.VERSION
       )
         f4(
           q6.green(
-            `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.31", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-04T00:00:54Z" }.VERSION})`,
+            `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION})`,
           ) +
             `
 `,
@@ -268,7 +268,7 @@
       else
         (f4(
           q6.green(
-            `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.31", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-04T00:00:54Z" }.VERSION} to version ${_.latestVersion}`,
+            `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION} to version ${_.latestVersion}`,
           ) +
             `
 `,
@@ -291,10 +291,10 @@
   if (K.installMethod !== "native") await Bg1();
   (I("update: Checking npm registry for latest version"),
     I(
-      `update: Package URL: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.31", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-04T00:00:54Z" }.PACKAGE_URL}`,
+      `update: Package URL: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.PACKAGE_URL}`,
     ));
   let Y = A === "stable" ? "stable" : "latest",
-    z = `npm view ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.31", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-04T00:00:54Z" }.PACKAGE_URL}@${Y} version`;
+    z = `npm view ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.PACKAGE_URL}@${Y} version`;
   I(`update: Running: ${z}`);
   let w = await iK1(A);
   if ((I(`update: Latest version from npm: ${w || "FAILED"}`), !w)) {
@@ -322,18 +322,18 @@
           "report the issue at https://github.com/anthropics/claude-code/issues",
         PACKAGE_URL: "@anthropic-ai/claude-code",
         README_URL: "https://code.claude.com/docs/en/overview",
-        VERSION: "2.1.31",
+        VERSION: "2.1.32",
         FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-        BUILD_TIME: "2026-02-04T00:00:54Z",
+        BUILD_TIME: "2026-02-05T17:02:01Z",
       }.PACKAGE_URL &&
         !{
           ISSUES_EXPLAINER:
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.31",
+          VERSION: "2.1.32",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-02-04T00:00:54Z",
+          BUILD_TIME: "2026-02-05T17:02:01Z",
         }.PACKAGE_URL.startsWith("@anthropic"))
     )
       process.stderr.write(`  • Internal/development build not published to npm
@@ -352,9 +352,9 @@
           "report the issue at https://github.com/anthropics/claude-code/issues",
         PACKAGE_URL: "@anthropic-ai/claude-code",
         README_URL: "https://code.claude.com/docs/en/overview",
-        VERSION: "2.1.31",
+        VERSION: "2.1.32",
         FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-        BUILD_TIME: "2026-02-04T00:00:54Z",
+        BUILD_TIME: "2026-02-05T17:02:01Z",
       }.PACKAGE_URL || "@anthropic-ai/claude-code";
     (process.stderr.write(`  • Manually check: npm view ${_} version
 `),
@@ -369,20 +369,20 @@
         "report the issue at https://github.com/anthropics/claude-code/issues",
       PACKAGE_URL: "@anthropic-ai/claude-code",
       README_URL: "https://code.claude.com/docs/en/overview",
-      VERSION: "2.1.31",
+      VERSION: "2.1.32",
       FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-      BUILD_TIME: "2026-02-04T00:00:54Z",
+      BUILD_TIME: "2026-02-05T17:02:01Z",
     }.VERSION
   )
     (f4(
       q6.green(
-        `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.31", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-04T00:00:54Z" }.VERSION})`,
+        `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION})`,
       ) +
         `
 `,
     ),
       await ZK(0));
-  (f4(`New version available: ${w} (current: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.31", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-04T00:00:54Z" }.VERSION})
+  (k4(`New version available: ${w} (current: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION})
 `),
     f4(`Installing update...
 `));
@@ -429,7 +429,7 @@
     case "success":
       (f4(
         q6.green(
-          `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.31", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-04T00:00:54Z" }.VERSION} to version ${w}`,
+          `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION} to version ${w}`,
         ) +
           `
 `,
@@ -445,7 +445,7 @@
         (process.stderr.write(`Try manually updating with:
 `),
           process.stderr
-            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.31", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-04T00:00:54Z" }.PACKAGE_URL}
+            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.PACKAGE_URL}
 `));
       else
         (process.stderr.write(`Try running with sudo or fix npm permissions
@@ -464,7 +464,7 @@
         (process.stderr.write(`Try manually updating with:
 `),
           process.stderr
-            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.31", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-04T00:00:54Z" }.PACKAGE_URL}
+            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.PACKAGE_URL}
 `));
       else
         process.stderr

@@@ function 'UuY' (was 'lxY') — structural (70.2%)
--- pretty-v2.1.31.js:439742
+++ pretty-v2.1.32.js:439684
@@ -4,17 +4,16 @@
   if (Y.length === 0) return [];
   let z = eQ1.size === 0;
   for (let H of Y) eQ1.add(H.name);
-  return (
-    I(
-      `Sending ${Y.length} skills via attachment (${z ? "initial" : "dynamic"}, ${eQ1.size} total sent)`,
-    ),
-    [
-      {
-        type: "skill_listing",
-        content: $34(Y),
-        skillCount: Y.length,
-        isInitial: z,
-      },
-    ]
+  h(
+    `Sending ${Y.length} skills via attachment (${z ? "initial" : "dynamic"}, ${vg1.size} total sent)`,
   );
+  let w = _W(A.options.mainLoopModel, Zj());
+  return [
+    {
+      type: "skill_listing",
+      content: R54(Y, w),
+      skillCount: Y.length,
+      isInitial: z,
+    },
+  ];
 }

@@@ function 'mp4' (was 'lU4') — structural (70.0%)
--- pretty-v2.1.31.js:419962
+++ pretty-v2.1.32.js:419533
@@ -1,8 +1,7 @@
 function lU4() {
   let A = U8() ? " and potentially assigned to teammates" : "",
     q = U8()
-      ? `- New tasks are created with status 'open' and no owner - use TeammateTool's assignTask to assign them
-`
+      ? "- New tasks are created with status 'open' and no owner - use TaskUpdate with the `owner` parameter to assign them\n"
       : "";
   return `Use this tool to create a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user.
 It also helps the user understand the progress of the task and overall progress of their requests.

@@@ variable '$w7' (was 'L27') — structural (69.2%)
--- pretty-v2.1.31.js:148682
+++ pretty-v2.1.32.js:148727
@@ -22,6 +22,9 @@
         device_id: YC(A.device_id) ? globalThis.String(A.device_id) : "",
         auth: YC(A.auth) ? BQ.fromJSON(A.auth) : void 0,
         session_id: YC(A.session_id) ? globalThis.String(A.session_id) : "",
+        anonymous_id: Bk(A.anonymous_id)
+          ? globalThis.String(A.anonymous_id)
+          : "",
         event_metadata_vars: YC(A.event_metadata_vars)
           ? globalThis.String(A.event_metadata_vars)
           : "",
@@ -41,6 +44,7 @@
       if (A.device_id !== void 0) q.device_id = A.device_id;
       if (A.auth !== void 0) q.auth = BQ.toJSON(A.auth);
       if (A.session_id !== void 0) q.session_id = A.session_id;
+      if (A.anonymous_id !== void 0) q.anonymous_id = A.anonymous_id;
       if (A.event_metadata_vars !== void 0)
         q.event_metadata_vars = A.event_metadata_vars;
       return q;
@@ -64,6 +68,7 @@
             ? BQ.fromPartial(A.auth)
             : void 0),
         (q.session_id = A.session_id ?? ""),
+        (q.anonymous_id = A.anonymous_id ?? ""),
         (q.event_metadata_vars = A.event_metadata_vars ?? ""),
         q
       );

@@@ function 'ZP9' (was 'oHY') — structural (69.2%)
--- pretty-v2.1.31.js:354476
+++ pretty-v2.1.32.js:246669
@@ -1,3 +1,3 @@
 function oHY() {
-  return `${M4().BASE_API_URL}/api/claude_code/settings`;
+  return `${D4().BASE_API_URL}/api/claude_code/policy_limits`;
 }

@@@ function 'L_Y' (was 'XOY') — structural (69.2%)
--- pretty-v2.1.31.js:354764
+++ pretty-v2.1.32.js:355267
@@ -1,3 +1,3 @@
 function XOY() {
-  return `${M4().BASE_API_URL}/api/claude_code/policy_limits`;
+  return `${D4().BASE_API_URL}/api/claude_code/settings`;
 }

@@@ variable 'lf6' (was 'yI4') — structural (69.2%)
--- pretty-v2.1.31.js:389066
+++ pretty-v2.1.32.js:488506
@@ -18,5 +18,14 @@
   Kw();
   Hr();
   Aq();
+  F6();
+  J3q();
+  k6();
+  Cq();
+  Tq();
+  LK();
+  P3q();
+  k51();
+  L51();
   $4 = o(J1(), 1);
 });

@@@ variable 'L3q' (was 'cM6') — structural (69.2%)
--- pretty-v2.1.31.js:422746
+++ pretty-v2.1.32.js:488922
@@ -16,13 +16,5 @@
   wr();
   Bq();
   uK();
-  wK();
-  k_6();
-  pI4();
-  Xj6();
-  Yj1();
-  F4();
-  CS();
-  e7();
   hA = o(J1(), 1);
 });

@@@ variable 'MZ1' (was 'ae4') — structural (69.2%)
--- pretty-v2.1.31.js:459090
+++ pretty-v2.1.32.js:528378
@@ -10,13 +10,5 @@
   B3();
   _h();
   mA();
-  yQ();
-  yO1();
-  C8();
-  Qg1();
-  mH();
-  R7();
-  f7();
-  MO();
   T51 = o(J1(), 1);
 });

@@@ variable 'RBA' (was 'yf6') — structural (69.2%)
--- pretty-v2.1.31.js:488722
+++ pretty-v2.1.32.js:531085
@@ -10,21 +10,5 @@
   yq();
   y5();
   B4q();
-  n3();
-  AY();
-  vG1();
-  s6();
-  QH();
-  yq();
-  s6();
-  g6();
-  Uqq();
-  N6();
-  wK();
-  Bq();
-  uK();
-  rqq();
-  j51();
-  M51();
   w7 = o(J1(), 1);
 });

@@@ variable 'rt' (was 'J3q') — structural (69.2%)
--- pretty-v2.1.31.js:494474
+++ pretty-v2.1.32.js:485126
@@ -6,7 +6,6 @@
   g6();
   Ap();
   n3();
-  ((l7 = o(J1(), 1)), (wm = o(J1(), 1)));
   StY = {
     USD: "$",
     EUR: "€",

@@@ variable 'm_q' (was 'oJq') — structural (69.2%)
--- pretty-v2.1.31.js:543613
+++ pretty-v2.1.32.js:534929
@@ -3,5 +3,27 @@
   g6();
   oQ1();
   l81();
+  kD();
+  i$q();
+  __q();
+  RBA();
+  CBA();
+  M_q();
+  G_q();
+  sF1();
+  dI1();
+  P01();
+  xv();
+  AG1();
+  Z_q();
+  T_q();
+  TQ1();
+  xBA();
+  ALA();
+  k_q();
+  pj6();
+  R_q();
+  DW6();
+  u_q();
   rd = o(J1(), 1);
 });

@@@ variable 'jmA' (was '_Xq') — structural (69.2%)
--- pretty-v2.1.31.js:545653
+++ pretty-v2.1.32.js:540793
@@ -3,5 +3,12 @@
   lBA();
   _6();
   D8();
+  x7();
+  j3();
+  Jd1();
+  cS();
+  z_();
+  Wq();
+  _6();
   xR = o(J1(), 1);
 });

@@@ variable 'EDq' (was 'DXq') — structural (69.2%)
--- pretty-v2.1.31.js:545856
+++ pretty-v2.1.32.js:546882
@@ -3,5 +3,7 @@
   lBA();
   _6();
   Sw();
+  Zv();
+  oz();
   bR = o(J1(), 1);
 });

@@@ variable 'pDq' (was 'jXq') — structural (69.2%)
--- pretty-v2.1.31.js:545864
+++ pretty-v2.1.32.js:547691
@@ -3,5 +3,19 @@
   u1();
   S8();
   eZ6();
+  sq();
+  Zd();
+  xh();
+  KG1();
+  QG6();
+  _6();
+  Eq();
+  Pw();
+  NH();
+  xv();
+  Q7();
+  Kf();
+  a9();
+  IBA();
   $2z = o(J1(), 1);
 });

@@@ variable 'lDq' (was 'R0q') — structural (69.2%)
--- pretty-v2.1.31.js:549002
+++ pretty-v2.1.32.js:547865
@@ -3,5 +3,10 @@
   uA();
   pH();
   mA();
+  kD();
+  iG1();
+  iG1();
+  wH();
+  vz();
   k0q = o(J1(), 1);
 });

@@@ variable 'Kjq' (was 'Q0q') — structural (69.2%)
--- pretty-v2.1.31.js:549486
+++ pretty-v2.1.32.js:548463
@@ -1,11 +1,4 @@
 var Q0q = E(() => {
   p1();
-  Q4();
-  g6();
-  ui();
-  mA();
-  D8();
-  HmA();
-  vW6();
   We = o(J1(), 1);
 });

@@@ variable 'wjq' (was '_Dq') — structural (69.2%)
--- pretty-v2.1.31.js:550732
+++ pretty-v2.1.32.js:548474
@@ -1,7 +1,4 @@
 var _Dq = E(() => {
   p1();
-  u1();
-  y5();
-  qv();
   lw = o(J1(), 1);
 });

@@@ variable 'Ojq' (was 'dGq') — structural (69.2%)
--- pretty-v2.1.31.js:553598
+++ pretty-v2.1.32.js:548485
@@ -1,7 +1,4 @@
 var dGq = E(() => {
   p1();
-  A2();
-  _h();
-  mA();
   zT6 = o(J1(), 1);
 });

@@@ variable 'Xjq' (was 'DZq') — structural (69.2%)
--- pretty-v2.1.31.js:553985
+++ pretty-v2.1.32.js:548697
@@ -1,5 +1,9 @@
 var DZq = E(() => {
   F8();
   A2();
+  Q8();
+  nq1();
+  mp();
+  Tq();
   wd1 = o(J1(), 1);
 });

@@@ variable 'Pjq' (was 'jZq') — structural (69.2%)
--- pretty-v2.1.31.js:553991
+++ pretty-v2.1.32.js:549244
@@ -3,5 +3,21 @@
   A2();
   FS();
   F8();
+  Wz();
+  V$();
+  yj();
+  Zv();
+  _6();
+  Q8();
+  ZF1();
+  O71();
+  gM1();
+  I6();
+  Sm1();
+  E0();
+  J8();
+  Ch();
+  FB();
+  uO();
   RHz = o(J1(), 1);
 });

@@@ variable 'yjq' (was 'TZq') — structural (69.2%)
--- pretty-v2.1.31.js:555949
+++ pretty-v2.1.32.js:549512
@@ -1,5 +1,4 @@
 var TZq = E(() => {
   p1();
-  DKA();
   VZq = o(J1(), 1);
 });

@@@ variable 'gmA' (was '_fq') — structural (69.2%)
--- pretty-v2.1.31.js:558521
+++ pretty-v2.1.32.js:549569
@@ -1,13 +1,4 @@
 var _fq = E(() => {
   p1();
-  u1();
-  A9();
-  u1();
-  F8();
-  XB();
-  Sw();
-  iSA();
-  Z3();
-  JB();
   Ze = o(J1(), 1);
 });

@@@ variable 'cjq' (was 'jfq') — structural (69.2%)
--- pretty-v2.1.31.js:558804
+++ pretty-v2.1.32.js:550398
@@ -5,21 +5,5 @@
   q2();
   ImA();
   yf6();
-  N6();
-  D8();
-  yq();
-  hf6();
-  T31();
-  NP1();
-  Aq();
-  Ap();
-  gIA();
-  s6();
-  yq();
-  Zk();
-  Gp1();
-  iD();
-  F8();
-  np1();
   cY = o(J1(), 1);
 });

@@@ variable 'KMq' (was 'Cfq') — structural (69.2%)
--- pretty-v2.1.31.js:559396
+++ pretty-v2.1.32.js:550952
@@ -1,11 +1,4 @@
 var Cfq = E(() => {
   u1();
-  kfq();
-  Rfq();
-  F8();
-  HZ();
-  IX();
-  JB();
-  XB();
   L91 = o(J1(), 1);
 });

@@@ variable '_fq' (was 'nfq') — structural (69.2%)
--- pretty-v2.1.31.js:559651
+++ pretty-v2.1.32.js:553114
@@ -6,6 +6,5 @@
   g6();
   u1();
   Sw();
-  Z3();
   td = o(J1(), 1);
 });

@@@ variable 'Ufq' (was 'qNq') — structural (69.2%)
--- pretty-v2.1.31.js:564446
+++ pretty-v2.1.32.js:554086
@@ -4,13 +4,5 @@
   A9();
   q2();
   Aq();
-  _6();
-  $yA();
-  $31();
-  Nh();
-  Bq();
-  uK();
-  Gw();
-  wK();
   JK = o(J1(), 1);
 });

@@@ function 'aeY' (was 'QsY') — structural (68.9%)
--- pretty-v2.1.31.js:490364
+++ pretty-v2.1.32.js:490061
@@ -6,8 +6,9 @@
     case "completed":
       return "success";
     case "failed":
+      return "error";
     case "killed":
-      return "error";
+      return "warning";
     default:
       return "background";
   }

@@@ function 'R54' (was '$34') — structural (68.8%)
--- pretty-v2.1.31.js:293779
+++ pretty-v2.1.32.js:295620
@@ -1,6 +1,6 @@
-function $34(A) {
+function R54(A, q) {
   if (A.length === 0) return "";
-  let q = Ng9(),
+  let K = Rd9(q),
     K = A.map((O) => ({ cmd: O, full: Tg9(O) }));
   if (K.reduce((O, $) => O + $.full.length, 0) + (K.length - 1) <= q)
     return K.map((O) => O.full).join(`

@@@ function '$81' (was 'Ui') — structural (68.6%)
--- pretty-v2.1.31.js:147352
+++ pretty-v2.1.32.js:147304
@@ -2,7 +2,6 @@
   if (q7()) {
     if (!Xk())
       return { value: null, label: "Sonnet", description: c1A().description };
-    if (aO1()) return { value: null, label: "Opus", description: ZL1() };
     return { value: null, label: "Default (recommended)", description: ZL1() };
   }
   let A = H4() !== "firstParty";

@@@ variable 'iQ' (was 'QQ') — structural (68.0%)
--- pretty-v2.1.31.js:156694
+++ pretty-v2.1.32.js:156752
@@ -1,4 +1,5 @@
 var QQ = E(() => {
   eH7();
+  _6();
   GS5 = /[{}[\]*&#!|>%@`]/;
 });

@@@ function 'aKq' (was 'Rqq') — structural (68.0%)
--- pretty-v2.1.31.js:485754
+++ pretty-v2.1.32.js:485529
@@ -8,6 +8,7 @@
     O = NZ7(),
     $ = p8.isSandboxingEnabled(),
     _ = kf6(),
+    J = FZ6(),
     J = T6((Z1) => Z1.agent),
     X = W6(),
     D;
@@ -33,9 +34,9 @@
           "report the issue at https://github.com/anthropics/claude-code/issues",
         PACKAGE_URL: "@anthropic-ai/claude-code",
         README_URL: "https://code.claude.com/docs/en/overview",
-        VERSION: "2.1.31",
+        VERSION: "2.1.32",
         FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-        BUILD_TIME: "2026-02-04T00:00:54Z",
+        BUILD_TIME: "2026-02-05T17:02:01Z",
       }.VERSION
     )
       return;
@@ -48,10 +49,10 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.31",
+            VERSION: "2.1.32",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-02-04T00:00:54Z",
+            BUILD_TIME: "2026-02-05T17:02:01Z",
           }.VERSION
         )
           return j1;
@@ -62,10 +63,10 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.31",
+            VERSION: "2.1.32",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-02-04T00:00:54Z",
+            BUILD_TIME: "2026-02-05T17:02:01Z",
           }.VERSION,
         };
       }),
@@ -75,7 +76,10 @@
   }, [X, O]),
     c51.useEffect(() => {
       if (_ && !O) Lf6();
-    }, [_, O]));
+    }, [_, O]),
+    ot.useEffect(() => {
+      if (J && !O && !_) QZ6();
+    }, [J, O, _]));
   let [P, { isVisible: G }] = Xg(),
     f = ff6(),
     V = c51.useRef(f);
@@ -278,7 +282,9 @@
               ? [fqq(eqA()), Ef6(z)]
               : _
                 ? [Ef6(z), Vqq()]
-                : [Ef6(z), Zqq(D)],
+                : J
+                  ? [aU1(z), dKq(J)]
+                  : [aU1(z), gKq(j)],
             maxWidth: w1,
           }),
       ),

@@@ variable '_j1' (was 'UD1') — structural (67.8%)
--- pretty-v2.1.31.js:295467
+++ pretty-v2.1.32.js:297297
@@ -25,5 +25,6 @@
       ...[],
       QD1,
     ])),
+    (O94 = new Set([dS, eq1, AK1, aL])),
     (A$6 = new Set([Ha, QD1, wa, aO6, sO6, uU, YK])));
 });

@@@ variable 'BpY' (was 'Me4') — structural (67.4%)
--- pretty-v2.1.31.js:457047
+++ pretty-v2.1.32.js:456882
@@ -1,55 +1,35 @@
-var Me4 = E(() => {
-  yq();
-  s6();
-  wM();
-  c9();
-  Nz();
-  ((igY = {
-    type: "local",
-    name: "color",
-    description: "Set the prompt bar color for this session",
-    isEnabled: () => U8(),
-    isHidden: !1,
-    supportsNonInteractive: !1,
-    argumentHint: "<color>",
-    async call(A, q) {
-      if (iz())
-        return {
-          type: "text",
-          value:
-            "Cannot set color: This session is a swarm teammate. Teammate colors are assigned by the team leader.",
-        };
-      if (!A || A.trim() === "")
-        return {
-          type: "text",
-          value: `Please provide a color. Available colors: ${X_.join(", ")}`,
-        };
-      let K = A.trim().toLowerCase();
-      if (!X_.includes(K)) {
-        let w = X_.join(", ");
-        return {
-          type: "text",
-          value: `Invalid color "${K}". Available colors: ${w}`,
-        };
-      }
-      let Y = F6(),
-        z = T$();
-      return (
-        await ZSA(Y, K, z),
-        q.setAppState((w) => ({
-          ...w,
-          standaloneAgentContext: {
-            ...w.standaloneAgentContext,
-            name: w.standaloneAgentContext?.name ?? "",
-            color: K,
-          },
-        })),
-        { type: "text", value: `Session color set to: ${K}` }
-      );
-    },
-    userFacingName() {
-      return "color";
-    },
-  }),
-    (je4 = igY));
-});
+var BpY = async (A, q) => {
+  if (rz())
+    return {
+      type: "text",
+      value:
+        "Cannot set color: This session is a swarm teammate. Teammate colors are assigned by the team leader.",
+    };
+  if (!A || A.trim() === "")
+    return {
+      type: "text",
+      value: `Please provide a color. Available colors: ${S$.join(", ")}`,
+    };
+  let K = A.trim().toLowerCase();
+  if (!S$.includes(K)) {
+    let w = S$.join(", ");
+    return {
+      type: "text",
+      value: `Invalid color "${K}". Available colors: ${w}`,
+    };
+  }
+  let Y = u6(),
+    z = I$();
+  return (
+    await oSA(Y, K, z),
+    q.setAppState((w) => ({
+      ...w,
+      standaloneAgentContext: {
+        ...w.standaloneAgentContext,
+        name: w.standaloneAgentContext?.name ?? "",
+        color: K,
+      },
+    })),
+    { type: "text", value: `Session color set to: ${K}` }
+  );
+};

@@@ variable 'fX8' (was 'pJ8') — structural (67.3%)
--- pretty-v2.1.31.js:74068
+++ pretty-v2.1.32.js:73990
@@ -1,43 +1,43 @@
 var pJ8 = E(() => {
   t7();
-  ((c$K = b
-    .object({
-      allowedDomains: b.array(b.string()).optional(),
-      allowUnixSockets: b
-        .array(b.string())
+  ((CJK = B.object({
+    allowedDomains: B.array(B.string()).optional(),
+    allowManagedDomainsOnly: B.boolean()
+      .optional()
+      .describe(
+        "When true (and set in managed settings), only allowedDomains and WebFetch(domain:...) allow rules from managed settings are respected. User, project, local, and flag settings domains are ignored. Denied domains are still respected from all sources.",
+      ),
+    allowUnixSockets: B.array(B.string())
+      .optional()
+      .describe(
+        "macOS only: Unix socket paths to allow. Ignored on Linux (seccomp cannot filter by path).",
+      ),
+    allowAllUnixSockets: B.boolean()
+      .optional()
+      .describe(
+        "If true, allow all Unix sockets (disables blocking on both platforms).",
+      ),
+    allowLocalBinding: B.boolean().optional(),
+    httpProxyPort: B.number().optional(),
+    socksProxyPort: B.number().optional(),
+  }).optional()),
+    (ZX8 = B.object({
+      enabled: B.boolean().optional(),
+      autoAllowBashIfSandboxed: B.boolean().optional(),
+      allowUnsandboxedCommands: B.boolean()
         .optional()
         .describe(
-          "macOS only: Unix socket paths to allow. Ignored on Linux (seccomp cannot filter by path).",
+          "Allow commands to run outside the sandbox via the dangerouslyDisableSandbox parameter. When false, the dangerouslyDisableSandbox parameter is completely ignored and all commands must run sandboxed. Default: true.",
         ),
-      allowAllUnixSockets: b
-        .boolean()
+      network: CJK,
+      ignoreViolations: B.record(B.string(), B.array(B.string())).optional(),
+      enableWeakerNestedSandbox: B.boolean().optional(),
+      excludedCommands: B.array(B.string()).optional(),
+      ripgrep: B.object({
+        command: B.string(),
+        args: B.array(B.string()).optional(),
+      })
         .optional()
-        .describe(
-          "If true, allow all Unix sockets (disables blocking on both platforms).",
-        ),
-      allowLocalBinding: b.boolean().optional(),
-      httpProxyPort: b.number().optional(),
-      socksProxyPort: b.number().optional(),
-    })
-    .optional()),
-    (UJ8 = b
-      .object({
-        enabled: b.boolean().optional(),
-        autoAllowBashIfSandboxed: b.boolean().optional(),
-        allowUnsandboxedCommands: b
-          .boolean()
-          .optional()
-          .describe(
-            "Allow commands to run outside the sandbox via the dangerouslyDisableSandbox parameter. When false, the dangerouslyDisableSandbox parameter is completely ignored and all commands must run sandboxed. Default: true.",
-          ),
-        network: c$K,
-        ignoreViolations: b.record(b.string(), b.array(b.string())).optional(),
-        enableWeakerNestedSandbox: b.boolean().optional(),
-        excludedCommands: b.array(b.string()).optional(),
-        ripgrep: b
-          .object({ command: b.string(), args: b.array(b.string()).optional() })
-          .optional()
-          .describe("Custom ripgrep configuration for bundled ripgrep support"),
-      })
-      .passthrough()));
+        .describe("Custom ripgrep configuration for bundled ripgrep support"),
+    }).passthrough()));
 });

@@@ function 'OL1' (was 'ik1') — structural (66.7%)
--- pretty-v2.1.31.js:138423
+++ pretty-v2.1.32.js:138313
@@ -9,5 +9,6 @@
     opus40: ck1[A],
     opus41: lk1[A],
     opus45: IA1[A],
+    opus46: gA1[A],
   };
 }

@@@ function 'H0' (was 'z0') — structural (66.7%)
--- pretty-v2.1.31.js:156635
+++ pretty-v2.1.32.js:156687
@@ -1,4 +1,4 @@
-function z0(A) {
+function H0(A, q) {
   let q = /^---\s*\n([\s\S]*?)---\s*\n?/,
     K = A.match(q);
   if (!K) return { frontmatter: {}, content: A };
@@ -13,7 +13,13 @@
       let H = ZS5(Y),
         O = H76(H);
       if (O && typeof O === "object" && !Array.isArray(O)) w = O;
-    } catch {}
+    } catch (O) {
+      let $ = q ? ` in ${q}` : "";
+      h(
+        `Failed to parse YAML frontmatter${$}: ${O instanceof Error ? O.message : O}`,
+        { level: "warn" },
+      );
+    }
   }
   return { frontmatter: w, content: z };
 }

@@@ function 'NMA' (was 'xjA') — structural (66.7%)
--- pretty-v2.1.31.js:301552
+++ pretty-v2.1.32.js:302320
@@ -5,7 +5,10 @@
     if (gD1.has(z.name)) return !1;
     if (!q && LDA.has(z.name)) return !1;
     if (K && !eO6.has(z.name)) {
-      if (U8() && z.name === YK && KG()) return !0;
+      if (F8() && dj()) {
+        if (z.name === OK) return !0;
+        if (O94.has(z.name)) return !0;
+      }
       return !1;
     }
     return !0;

@@@ function 'lSA' (was 'YZ6') — structural (66.7%)
--- pretty-v2.1.31.js:456983
+++ pretty-v2.1.32.js:456800
@@ -8,5 +8,6 @@
     ss(),
     n94(),
     lE6(),
-    mJA(null));
+    FXA(null),
+    ZZ6());
 }

@@@ variable 'fTq' (was 'uVq') — structural (66.7%)
--- pretty-v2.1.31.js:562971
+++ pretty-v2.1.32.js:563117
@@ -70,5 +70,7 @@
   Kw();
   wv();
   EO();
+  Zv();
+  uO();
   IVq = new Set();
 });

@@@ function 'uqz' (was 'V7z') — structural (66.1%)
--- pretty-v2.1.31.js:516559
+++ pretty-v2.1.32.js:516233
@@ -12,9 +12,8 @@
 
 0. Write your plan in the plan file specified above. This is the ONLY file you are allowed to edit.
 
-1. **Explore the codebase**: Use ${f7z()} tools to understand the codebase. Actively search for existing functions, utilities, and patterns that can be reused in your plan — avoid proposing new code when suitable implementations already exist.${`
-You have access to the ${dT.agentType} agent type if you want to delegate search.
-Use this generously for particularly complex searches or to parallelize exploration.`}
+1. **Explore the codebase**: Use ${bqz()} tools to understand the codebase. Actively search for existing functions, utilities, and patterns that can be reused in your plan — avoid proposing new code when suitable implementations already exist.
+You can use the ${Yv.agentType} agent type to parallelize complex searches without filling your context, though for straightforward queries direct tools are simpler.
 
 2. **Interview the user**: Use ${Rw} to interview the user and ask questions that:
    - Clarify ambiguous requirements

@@@ function 'y$q' (was 'FHq') — structural (66.1%)
--- pretty-v2.1.31.js:526513
+++ pretty-v2.1.32.js:526409
@@ -3,6 +3,7 @@
   onPreRestore: q,
   onRestoreMessage: K,
   onRestoreCode: Y,
+  onSummarize: z,
   onClose: z,
 }) {
   let w = T6((H1) => H1.fileHistory),
@@ -19,7 +20,33 @@
     [W, P] = CJ.useState(void 0),
     [G, f] = CJ.useState(void 0),
     [V, N] = CJ.useState(!1),
-    [T, k] = CJ.useState("both");
+    [k, y] = g$.useState(null),
+    [u, S] = g$.useState("both"),
+    [m, b] = g$.useState("");
+  function U(G1) {
+    let w1 = G1
+      ? [
+          { value: "both", label: "Restore code and conversation" },
+          { value: "conversation", label: "Restore conversation" },
+          { value: "code", label: "Restore code" },
+        ]
+      : [{ value: "conversation", label: "Restore conversation" }];
+    return (
+      w1.push({
+        value: "summarize",
+        label: "Summarize from here",
+        type: "input",
+        placeholder: "add context (optional)",
+        initialValue: "",
+        onChange: b,
+        allowEmptySubmitToCancel: !0,
+        showLabelWithValue: !0,
+        labelValueSeparator: ": ",
+      }),
+      w1.push({ value: "nevermind", label: "Never mind" }),
+      w1
+    );
+  }
   CJ.useEffect(() => {
     n("tengu_message_selector_opened", {});
   }, []);
@@ -64,6 +91,20 @@
       P(void 0);
       return;
     }
+    if (G1 === "summarize") {
+      (q(), T(!0), y("summarize"), $(void 0));
+      try {
+        let E1 = m.trim() || void 0;
+        (await z(G, E1), T(!1), y(null), P(void 0), w());
+      } catch (E1) {
+        (K1(E1),
+          T(!1),
+          y(null),
+          $(`Failed to summarize:
+${E1}`));
+      }
+      return;
+    }
     (q(), N(!0), O(void 0));
     let $1 = null,
       A1 = null;
@@ -110,7 +151,7 @@
       let H1 = J[X];
       if (H1) y(H1);
     }, [J, X, y]);
-  (zA("confirm:no", m, { context: "Confirmation" }),
+  (DA("confirm:no", n, { context: "Confirmation", isActive: !G }),
     c7(
       {
         "messageSelector:up": u,
@@ -204,33 +245,47 @@
           LA.createElement(
             h,
             { flexDirection: "column" },
-            T === "both" || T === "conversation"
+            u === "summarize"
               ? LA.createElement(
                   Z,
                   { dimColor: !0 },
-                  "The conversation will be forked.",
+                  "Messages after this point will be summarized.",
                 )
-              : LA.createElement(
-                  Z,
-                  { dimColor: !0 },
-                  "The conversation will be unchanged.",
-                ),
-            q1 && (T === "both" || T === "code")
-              ? LA.createElement(y3z, { diffStatsForRestore: G })
-              : LA.createElement(
-                  Z,
-                  { dimColor: !0 },
-                  "The code will be unchanged.",
-                ),
+              : u === "both" || u === "conversation"
+                ? TA.createElement(
+                    f,
+                    { dimColor: !0 },
+                    "The conversation will be forked.",
+                  )
+                : TA.createElement(
+                    f,
+                    { dimColor: !0 },
+                    "The conversation will be unchanged.",
+                  ),
+            u !== "summarize" &&
+              (e && (u === "both" || u === "code")
+                ? TA.createElement(d9z, { diffStatsForRestore: V })
+                : TA.createElement(
+                    f,
+                    { dimColor: !0 },
+                    "The code will be unchanged.",
+                  )),
           ),
-          LA.createElement(ZA, {
-            isDisabled: V,
-            options: q1 ? L3z : R3z,
-            defaultFocusValue: q1 ? "both" : "conversation",
-            onFocus: (H1) => k(H1),
-            onChange: (H1) => B(H1),
-            onCancel: () => P(void 0),
-          }),
+          N && k === "summarize"
+            ? TA.createElement(
+                I,
+                { flexDirection: "row", gap: 1 },
+                TA.createElement(x4, null),
+                TA.createElement(f, null, "Summarizing…"),
+              )
+            : TA.createElement(ZA, {
+                isDisabled: N,
+                options: U(!!e),
+                defaultFocusValue: e ? "both" : "conversation",
+                onFocus: (G1) => S(G1),
+                onChange: (G1) => x(G1),
+                onCancel: () => P(void 0),
+              }),
           q1 &&
             LA.createElement(
               h,
@@ -344,24 +399,25 @@
             }),
           ),
         ),
-      LA.createElement(
-        Z,
-        { dimColor: !0, italic: !0 },
-        C.pending
-          ? LA.createElement(
-              LA.Fragment,
-              null,
-              "Press ",
-              C.keyName,
-              " again to exit",
-            )
-          : LA.createElement(
-              LA.Fragment,
-              null,
-              !H && M && "Enter to continue · ",
-              "Esc to exit",
-            ),
-      ),
+      !G &&
+        TA.createElement(
+          f,
+          { dimColor: !0, italic: !0 },
+          p.pending
+            ? TA.createElement(
+                TA.Fragment,
+                null,
+                "Press ",
+                p.keyName,
+                " again to exit",
+              )
+            : TA.createElement(
+                TA.Fragment,
+                null,
+                !O && W && "Enter to continue · ",
+                "Esc to exit",
+              ),
+        ),
     ),
   );
 }

@@@ function 'ofq' (was 'qZq') — structural (65.8%)
--- pretty-v2.1.31.js:553815
+++ pretty-v2.1.32.js:554168
@@ -9,15 +9,15 @@
       let w = _5(),
         H = NHz(w);
       if (!H) return;
-      (n("tengu_opus45_upgrade_nudge_shown", { currentModel: w }),
+      (c("tengu_opus46_upgrade_nudge_shown", { currentModel: w }),
         q({
-          key: "opus-45-upgrade-nudge",
+          key: "opus-46-upgrade-nudge",
           jsx: Yd1.createElement(
             Z,
             { color: "suggestion" },
             "Currently using ",
             H,
-            ". Opus 4.5 is our best model for coding",
+            ". Opus 4.6 is our best model for coding",
             Yd1.createElement(
               Z,
               { color: "text", dimColor: !0 },

@@@ function 'zXz' (was 'm$z') — structural (65.7%)
--- pretty-v2.1.31.js:565739
+++ pretty-v2.1.32.js:565889
@@ -116,7 +116,7 @@
       .addOption(
         new W5(
           "--max-thinking-tokens <tokens>",
-          "Maximum number of thinking tokens. (only works with --print)",
+          "Maximum number of thinking tokens (only works with --print)",
         )
           .argParser(Number)
           .hideHelp(),
@@ -286,7 +286,7 @@
       )
       .option(
         "--session-id <uuid>",
-        "Use a specific session ID for the conversation (must be a valid UUID)",
+        "Use a specific session ID for the conversation (UUID or tagged ID)",
       )
       .option(
         "--agents <json>",
@@ -396,7 +396,8 @@
           if (d6.teammateMode)
             jNq().setCliTeammateModeOverride?.(d6.teammateMode);
         }
-        let L1 = $.sdkUrl ?? void 0;
+        let V1 = $.sdkUrl ?? void 0,
+          E1 = y || $6(process.env.CLAUDE_CODE_INCLUDE_PARTIAL_MESSAGES);
         if (L1) {
           if (!g) g = "stream-json";
           if (!U) U = "stream-json";
@@ -416,7 +417,7 @@
           let d6 = oT(k);
           if (!d6)
             (process.stderr.write(
-              q6.red(`Error: Invalid session ID. Must be a valid UUID.
+              Y6.red(`Error: Invalid session ID. Must be a valid UUID or tagged ID.
 `),
             ),
               process.exit(1));
@@ -516,7 +517,7 @@
           { mode: N1, notification: R1 } = uzq({
             permissionModeCli: G,
             dangerouslySkipPermissions: X,
-            dangerouslySkipPermissionsWithClassifiers: G1,
+            ...{},
           });
         hE6(N1 === "bypassPermissions");
         let h1 = {};
@@ -715,7 +716,8 @@
               `Warning: agent "${L6}" not found. Available agents: ${D6.activeAgents.map((d6) => d6.agentType).join(", ")}. Using default behavior.`,
             );
         }
-        if ((sf1(e6?.agentType), _1 && e6 && !a && !HP(e6))) {
+        if ((fy(LA?.agentType), LA?.agentType)) NuA(u6(), LA.agentType);
+        if (o && LA && !_1 && !tD(LA)) {
           let d6 = e6.getSystemPrompt();
           if (d6) a = d6;
         }
@@ -776,7 +778,7 @@
             m7 = d6.filter((Z4) => !Z4.mcpErrorMetadata);
           if (m7.length > 0) await $fq(m7);
         }
-        (y94().catch((d6) => e(d6)), tz7(), Gqq(), kJq());
+        (pU7().catch((RA) => K1(RA)), I27(), QKq(), Cc7(), G0q());
         let { servers: j8 } = await VA;
         I(`[STARTUP] MCP configs loaded in ${Date.now() - a6}ms`);
         let k8 = { ...j8, ...h1 },
@@ -927,7 +929,6 @@
                 agent: u,
                 setupTrigger: EY ?? void 0,
                 mcpDeferredPromise: n8,
-                ...{},
               },
             ));
           return;
@@ -1044,7 +1045,11 @@
         let ww = vY;
         if ((k$z(), $.continue))
           try {
-            (n("tengu_continue", {}), YZ6());
+            c("tengu_continue", {});
+            let { clearSessionCaches: RA } = await Promise.resolve().then(
+              () => (VZ6(), iSA),
+            );
+            RA();
             let d6 = await Jt(void 0, void 0);
             if (!d6)
               (console.error("No conversation found to continue"),
@@ -1054,10 +1059,29 @@
               if (d6.sessionId)
                 (iZ(FW(d6.sessionId)), await Cv(), ML1(d6.sessionId));
             }
+            let $4;
+            if (!LA && e8.agentSetting) {
+              let Y4 = h6.activeAgents.find(
+                (hz) => hz.agentType === e8.agentSetting,
+              );
+              if (Y4) {
+                if (
+                  ((LA = Y4),
+                  fy(Y4.agentType),
+                  ($4 = Y4.agentType),
+                  !zf() && Y4.model && Y4.model !== "inherit")
+                )
+                  rG(s9(Y4.model));
+              } else
+                h(
+                  `Resumed session had agent "${e8.agentSetting}" but it is no longer available. Using default behavior.`,
+                );
+            }
             let Z4 = V0q(d6),
               P4 = ip1(d6.agentName, d6.agentColor),
               O9 = {
                 ...jK,
+                ...($4 && { agent: $4 }),
                 ...(Z4 && { attribution: Z4 }),
                 ...(P4 && { standaloneAgentContext: P4 }),
                 agentDefinitions: D6,
@@ -1098,12 +1122,16 @@
             (e(d6 instanceof Error ? d6 : Error(String(d6))), process.exit(1));
           }
         else if ($.resume || $.fromPr || v1 || K1 !== null) {
+          let { clearSessionCaches: RA } = await Promise.resolve().then(
+            () => (VZ6(), iSA),
+          );
           YZ6();
           let d6 = null,
             m7 = void 0,
             Z4 = void 0,
             P4 = void 0,
             Dq = void 0,
+            x5 = void 0,
             O9 = oT($.resume),
             x7 = void 0,
             b5 = null,
@@ -1309,6 +1337,7 @@
                 (m7 = Yq.fileHistorySnapshots),
                 (Z4 = Yq.agentName),
                 (P4 = Yq.agentColor),
+                (F7 = m1.agentSetting),
                 n("tengu_session_resumed", { entrypoint: "cli_flag" }),
                 !$.forkSession)
               ) {
@@ -1341,9 +1370,26 @@
             }
           if (Array.isArray(d6)) {
             if (yvA(d6)) us();
+            let B1;
+            if (!LA && F7) {
+              let VA = h6.activeAgents.find((yA) => yA.agentType === F7);
+              if (VA) {
+                if (
+                  ((LA = VA),
+                  fy(VA.agentType),
+                  (B1 = VA.agentType),
+                  !zf() && VA.model && VA.model !== "inherit")
+                )
+                  rG(s9(VA.model));
+              } else
+                h(
+                  `Resumed session had agent "${F7}" but it is no longer available. Using default behavior.`,
+                );
+            }
             let h8 = ip1(Z4, P4),
               N3 = {
                 ...jK,
+                ...(B1 && { agent: B1 }),
                 ...(h8 && { standaloneAgentContext: h8 }),
                 agentDefinitions: D6,
               },
@@ -1393,6 +1439,7 @@
                     XK.default.createElement(Dfq, {
                       commands: [...H6, ...Q9],
                       debug: _ || J,
+                      mainThreadAgentDefinition: LA,
                       worktreePaths: h8,
                       initialTools: ww,
                       mcpClients: tq,
@@ -1448,7 +1495,7 @@
         }
       })
       .version(
-        `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.31", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-04T00:00:54Z" }.VERSION} (Claude Code)`,
+        `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION} (Claude Code)`,
         "-v, --version",
         "Output the version number",
       ),
@@ -2355,6 +2402,7 @@
       }),
     q
       .command("update")
+      .alias("upgrade")
       .description("Check for updates and install if available")
       .helpOption("-h, --help", "Display help for command")
       .action(BVq),

@@@ function 'uxA' (was 'YxA') — structural (65.5%)
--- pretty-v2.1.31.js:494271
+++ pretty-v2.1.32.js:493975
@@ -1,5 +1,6 @@
-function YxA(A = !0) {
+function uxA(A = !0, q = !1) {
   if (!A) return "↯";
   let K = W6().theme;
+  if (q) return Y6.dim(v8("promptBorder", Y)("↯"));
   return E8("penguin", K)("↯");
 }

@@@ variable 'N8z' (was 'AYq') — structural (65.4%)
--- pretty-v2.1.31.js:505942
+++ pretty-v2.1.32.js:505554
@@ -1,44 +1,20 @@
-var AYq = E(() => {
-  fZ6();
-  F8();
-  e7();
-  hkA();
-  g6();
-  B3();
-  f7();
-  Wz();
-  FS();
-  zI = o(J1(), 1);
-  e9q = {
-    immediate: !0,
-    type: "local-jsx",
-    name: "model",
-    userFacingName() {
-      return "model";
-    },
-    description: "Set the AI model for Claude Code",
-    isEnabled: () => !0,
-    isHidden: !1,
-    argumentHint: "[model]",
-    async call(A, q, K) {
-      if (((K = K?.trim() || ""), $z1.includes(K)))
-        return (
-          n("tengu_model_command_inline_help", { args: K }),
-          zI.createElement(K6z, { onDone: A })
-        );
-      if (Oz1.includes(K)) {
-        A(
-          "Run /model to open the model selection menu, or /model [modelName] to set the model.",
-          { display: "system" },
-        );
-        return;
-      }
-      if (K)
-        return (
-          n("tengu_model_command_inline", { args: K }),
-          zI.createElement(e1z, { args: K, onDone: A })
-        );
-      return zI.createElement(t1z, { onDone: A });
-    },
-  };
-});
+  N8z = async (A, q, K) => {
+    if (((K = K?.trim() || ""), Vz1.includes(K)))
+      return (
+        c("tengu_model_command_inline_help", { args: K }),
+        VI.createElement(P8z, { onDone: A })
+      );
+    if (fz1.includes(K)) {
+      A(
+        "Run /model to open the model selection menu, or /model [modelName] to set the model.",
+        { display: "system" },
+      );
+      return;
+    }
+    if (K)
+      return (
+        c("tengu_model_command_inline", { args: K }),
+        VI.createElement(M8z, { args: K, onDone: A })
+      );
+    return VI.createElement(j8z, { onDone: A });
+  };

@@@ variable 'qVq' (was 'UZq') — structural (65.4%)
--- pretty-v2.1.31.js:556861
+++ pretty-v2.1.32.js:554289
@@ -1,3 +1,4 @@
 var UZq = E(() => {
+  wxA();
   MT6 = o(J1(), 1);
 });

@@@ function 'zDY' (was 'dJY') — structural (65.3%)
--- pretty-v2.1.31.js:365219
+++ pretty-v2.1.32.js:365541
@@ -2,14 +2,6 @@
   return async (K, Y, z, w, H) => {
     let O = await fX(K, Y, z, w, H);
     if (O.behavior !== "ask") return O;
-    if (K.name === Q7 && O.pendingClassifierCheck) {
-      let X = await qD6(
-        O.pendingClassifierCheck,
-        q.signal,
-        z.options.isNonInteractiveSession,
-      );
-      if (X) return { behavior: "allow", updatedInput: Y, decisionReason: X };
-    }
     if (q.signal.aborted) return { behavior: "ask", message: jh };
     let $ = await z.getAppState(),
       _ = await K.description(Y, {
@@ -50,7 +42,7 @@
                   q.signal.removeEventListener("abort", j),
                   X({ behavior: "ask", message: jh }));
               },
-              async onAllow(W, P, G) {
+              async onAllow(W, G, P, V) {
                 if (D) return;
                 if (
                   ((D = !0),
@@ -71,13 +63,14 @@
                   updatedInput: W,
                   userModified: !1,
                   acceptFeedback: f || void 0,
+                  ...(V && V.length > 0 && { contentBlocks: V }),
                 });
               },
-              onReject(W) {
+              onReject(W, G) {
                 if (D) return;
                 ((D = !0), q.signal.removeEventListener("abort", j));
                 let P = W ? `${Lm1}${W}` : jh;
-                X({ behavior: "ask", message: P });
+                X({ behavior: "ask", message: P, contentBlocks: G });
               },
               async recheckPermission() {
                 if (D) return;
@@ -106,15 +99,20 @@
       (C06({
         requestId: D.id,
         toolUseId: H,
-        onAllow(P, G) {
+        onAllow(G, P, V, Z) {
           (W(), gQ(G));
           let f = P && Object.keys(P).length > 0 ? P : Y;
-          X({ behavior: "allow", updatedInput: f, userModified: !1 });
+          X({
+            behavior: "allow",
+            updatedInput: N,
+            userModified: !1,
+            ...(Z && Z.length > 0 && { contentBlocks: Z }),
+          });
         },
-        onReject(P) {
+        onReject(G, P) {
           W();
           let G = P ? `${Lm1}${P}` : jh;
-          X({ behavior: "ask", message: G });
+          X({ behavior: "ask", message: V, contentBlocks: P });
         },
       }),
         L06(D));

@@@ variable 'ss' (was 'Qs') — structural (64.8%)
--- pretty-v2.1.31.js:399325
+++ pretty-v2.1.32.js:398964
@@ -29,8 +29,14 @@
           ? Promise.all(Y.map((D) => sj6(D, "projectSettings")))
           : Promise.resolve([]),
       ]),
+      O = v11(),
+      $ = UJ("projectSettings")
+        ? await Promise.all(
+            O.map((M) => rF1(os(M, ".claude", "skills"), "projectSettings")),
+          )
+        : [],
       O = await KfY(A),
-      $ = [...z, ...w, ...H.flat(), ...O],
+      J = [...z, ...w, ...H.flat(), ...$.flat(), ..._],
       _ = new Map(),
       J = [];
     for (let { skill: D, filePath: j } of $) {
@@ -53,7 +59,7 @@
     if (X > 0) I(`Deduplicated ${X} skills (same file)`);
     return (
       I(
-        `Loaded ${J.length} unique skills (managed: ${z.length}, user: ${w.length}, project: ${H.flat().length}, legacy commands: ${O.length})`,
+        `Loaded ${D.length} unique skills (managed: ${z.length}, user: ${w.length}, project: ${H.flat().length}, additional: ${$.flat().length}, legacy commands: ${_.length})`,
       ),
       J
     );

@@@ function 'L06' (was 'aX6') — structural (64.7%)
--- pretty-v2.1.31.js:353506
+++ pretty-v2.1.32.js:354281
@@ -1,5 +1,5 @@
 function aX6(A) {
-  let q = t(40),
+  let q = A1(43),
     {
       isDisabled: K,
       visibleOptionCount: Y,
@@ -16,6 +16,9 @@
       initialFocusLast: M,
       onOpenEditor: W,
       hideIndexes: P,
+      onImagePaste: P,
+      pastedContents: V,
+      onRemoveImage: Z,
     } = A,
     G = K === void 0 ? !1 : K,
     f = Y === void 0 ? 5 : Y,
@@ -81,8 +84,11 @@
     q[17] !== G ||
     q[18] !== H ||
     q[19] !== W ||
-    q[20] !== z.length ||
-    q[21] !== y
+    q[20] !== W ||
+    q[21] !== Z ||
+    q[22] !== z.length ||
+    q[23] !== V ||
+    q[24] !== m
   ) {
     let r = z.length.toString().length;
     ((C = h),
@@ -122,6 +128,9 @@
                 },
                 layout: "compact",
                 onOpenEditor: W,
+                onImagePaste: P,
+                pastedContents: V,
+                onRemoveImage: Z,
               },
               iW.default.createElement(
                 Z,
@@ -147,7 +156,11 @@
               description: c.description,
             },
             !T &&
-              iW.default.createElement(Z, { dimColor: !0 }, `${Z1}.`.padEnd(r)),
+              OG.default.createElement(
+                f,
+                { dimColor: !0 },
+                `${E1}.`.padEnd(f1),
+              ),
             iW.default.createElement(
               Z,
               { color: !T && $1 ? "success" : void 0 },
@@ -167,24 +180,27 @@
       (q[17] = G),
       (q[18] = H),
       (q[19] = W),
-      (q[20] = z.length),
+      (q[20] = W),
       (q[21] = y),
-      (q[22] = B),
+      (q[22] = z.length),
       (q[23] = C),
       (q[24] = m),
       (q[25] = u),
-      (q[26] = U));
-  } else ((B = q[22]), (C = q[23]), (m = q[24]), (u = q[25]), (U = q[26]));
+      (q[26] = U),
+      (q[27] = g),
+      (q[28] = x),
+      (q[29] = p));
+  } else ((b = q[25]), (U = q[26]), (g = q[27]), (x = q[28]), (p = q[29]));
   let g;
-  if (q[27] !== B || q[28] !== m || q[29] !== u)
+  if (q[30] !== b || q[31] !== g || q[32] !== x)
     ((g = iW.default.createElement(B, { flexDirection: m }, u)),
-      (q[27] = B),
-      (q[28] = m),
-      (q[29] = u),
-      (q[30] = g));
-  else g = q[30];
+      (q[30] = b),
+      (q[31] = g),
+      (q[32] = x),
+      (q[33] = n));
+  else n = q[33];
   let x;
-  if (q[31] !== X || q[32] !== y.isSubmitFocused || q[33] !== J)
+  if (q[34] !== X || q[35] !== m.isSubmitFocused || q[36] !== J)
     ((x =
       J &&
       X &&
@@ -204,19 +220,19 @@
           ),
         ),
       )),
-      (q[31] = X),
-      (q[32] = y.isSubmitFocused),
-      (q[33] = J),
-      (q[34] = x));
-  else x = q[34];
+      (q[34] = X),
+      (q[35] = m.isSubmitFocused),
+      (q[36] = J),
+      (q[37] = r));
+  else r = q[37];
   let d;
-  if (q[35] !== C || q[36] !== g || q[37] !== x || q[38] !== U)
+  if (q[38] !== U || q[39] !== n || q[40] !== r || q[41] !== p)
     ((d = iW.default.createElement(C, { flexDirection: U }, g, x)),
-      (q[35] = C),
-      (q[36] = g),
-      (q[37] = x),
       (q[38] = U),
-      (q[39] = d));
-  else d = q[39];
+      (q[39] = n),
+      (q[40] = r),
+      (q[41] = p),
+      (q[42] = z1));
+  else z1 = q[42];
   return d;
 }

@@@ function 'Gjq' (was 'T0q') — structural (64.5%)
--- pretty-v2.1.31.js:548472
+++ pretty-v2.1.32.js:548793
@@ -331,9 +331,18 @@
               (w((r) => {
                 if (!r.teamContext?.teammates) return r;
                 if (!(g in r.teamContext.teammates)) return r;
-                let { [g]: c, ...q1 } = r.teamContext.teammates;
+                let { [g]: r, ...z1 } = n.teamContext.teammates,
+                  f1 = { ...n.tasks };
+                for (let [Z1, H1] of Object.entries(f1))
+                  if (h$(H1) && H1.identity.agentId === g)
+                    f1[Z1] = {
+                      ...H1,
+                      status: "completed",
+                      endTime: Date.now(),
+                    };
                 return {
                   ...r,
+                  tasks: f1,
                   teamContext: { ...r.teamContext, teammates: q1 },
                   inbox: {
                     messages: [

@@@ function '_DY' (was 'rJY') — structural (64.1%)
--- pretty-v2.1.31.js:365443
+++ pretty-v2.1.32.js:365764
@@ -43,25 +43,44 @@
     I(`[inProcessRunner] ${A.agentName} poll #${O}: checking mailbox`);
     try {
       let X = fp(A.agentName, A.teamName),
-        D = X.findIndex((j) => !j.read);
-      if (D !== -1) {
+        D = -1,
+        j = null;
+      for (let W = 0; W < X.length; W++) {
         let j = X[D];
-        if (j) {
-          I(
-            `[inProcessRunner] ${A.agentName} found unread message at index ${D}`,
-          );
+        if (G && !G.read) {
           let M = zs(j.text);
-          if (M)
-            return (
-              I(
-                `[inProcessRunner] ${A.agentName} received shutdown request from ${M.from}`,
-              ),
-              Ym1(A.agentName, A.teamName, D),
-              { type: "shutdown_request", request: M, originalMessage: j.text }
-            );
+          if (P) {
+            ((D = W), (j = P));
+            break;
+          }
+        }
+      }
+      if (D !== -1) {
+        let W = X[D],
+          G = X.slice(0, D).filter((P) => !P.read).length;
+        return (
+          h(
+            `[inProcessRunner] ${A.agentName} received shutdown request from ${j?.from} (prioritized over ${G} unread messages)`,
+          ),
+          Nm1(A.agentName, A.teamName, D),
+          { type: "shutdown_request", request: j, originalMessage: W.text }
+        );
+      }
+      let M = -1;
+      for (let W = 0; W < X.length; W++) {
+        let G = X[W];
+        if (G && !G.read && G.from === h2) {
+          M = W;
+          break;
+        }
+      }
+      if (M === -1) M = X.findIndex((W) => !W.read);
+      if (M !== -1) {
+        let W = X[M];
+        if (W)
           return (
             I(
-              `[inProcessRunner] ${A.agentName} received new message from ${j.from}`,
+              `[inProcessRunner] ${A.agentName} received new message from ${W.from} (index ${M})`,
             ),
             Ym1(A.agentName, A.teamName, D),
             {
@@ -69,9 +88,9 @@
               message: j.text,
               from: j.from,
               color: j.color,
+              summary: W.summary,
             }
           );
-        }
       }
     } catch (X) {
       I(`[inProcessRunner] ${A.agentName} poll error: ${X}`);

@@@ function 'w8' (was 'l8') — structural (63.9%)
--- pretty-v2.1.31.js:217949
+++ pretty-v2.1.32.js:268936
@@ -1,5 +1,5 @@
 function l8(A) {
-  let q = t(10),
+  let q = A1(11),
     {
       title: K,
       subtitle: Y,
@@ -10,6 +10,7 @@
       hideInputGuide: $,
       hideBorder: _,
       inputGuide: J,
+      isCancelActive: X,
     } = A,
     X;
   if (
@@ -21,7 +22,8 @@
     q[5] !== J ||
     q[6] !== w ||
     q[7] !== Y ||
-    q[8] !== K
+    q[8] !== Y ||
+    q[9] !== K
   )
     ((X = LW.default.createElement(
       N39,
@@ -34,6 +36,7 @@
         hideInputGuide: $,
         hideBorder: _,
         inputGuide: J,
+        isCancelActive: X,
       },
       z,
     )),
@@ -46,7 +49,8 @@
       (q[6] = w),
       (q[7] = Y),
       (q[8] = K),
-      (q[9] = X));
-  else X = q[9];
+      (q[9] = K),
+      (q[10] = D));
+  else D = q[10];
   return X;
 }

@@@ function 'vm1' (was 'wm1') — structural (63.9%)
--- pretty-v2.1.31.js:357519
+++ pretty-v2.1.32.js:357976
@@ -1,10 +1,12 @@
-function wm1(A, q, K, Y) {
+function vm1(A, q) {
   return {
     type: "idle_notification",
     from: A,
     timestamp: new Date().toISOString(),
-    completedTaskId: q,
-    completedStatus: K,
-    failureReason: Y,
+    idleReason: q?.idleReason,
+    summary: q?.summary,
+    completedTaskId: q?.completedTaskId,
+    completedStatus: q?.completedStatus,
+    failureReason: q?.failureReason,
   };
 }

@@@ function 'I0q' (was 'UJq') — structural (63.7%)
--- pretty-v2.1.31.js:543174
+++ pretty-v2.1.32.js:543345
@@ -1,6 +1,7 @@
 function UJq() {
   let A = T6((w) => w.teamContext),
     q = T6((w) => w.standaloneAgentContext),
+    K = T6((H) => H.agent),
     K = Z_(),
     [Y, z] = LN6.useState(null);
   if (
@@ -48,5 +49,12 @@
       return { text: w ?? "", bgColor: O };
     }
   }
+  if (K) {
+    let O = Y.getState().agentDefinitions.activeAgents.find(
+        (_) => _.agentType === K,
+      )?.color,
+      $ = O && S$.includes(O) ? HO[O] : "promptBorder";
+    return { text: K, bgColor: $ };
+  }
   return null;
 }

@@@ function 'AV6' (was 'mf6') — structural (63.7%)
--- pretty-v2.1.31.js:494788
+++ pretty-v2.1.32.js:494457
@@ -1,9 +1,8 @@
 function mf6(A) {
-  let q = t(39),
+  let q = A1(34),
     { showIfAlreadyViewed: K, location: Y, onDone: z } = A,
     [w, H] = A7.useState(null),
     [O, $] = A7.useState(null),
-    _ = v7(),
     J,
     X;
   if (q[0] !== Y || q[1] !== z || q[2] !== K)
@@ -92,7 +91,21 @@
   else M = q[9];
   let W = M,
     P;
-  if (q[10] !== O?.notice_is_grace_period)
+  if (q[10] !== O?.notice_is_grace_period || q[11] !== D)
+    ((W = function () {
+      if (O?.notice_is_grace_period) {
+        D("defer");
+        return;
+      }
+      D("escape");
+    }),
+      (q[10] = O?.notice_is_grace_period),
+      (q[11] = D),
+      (q[12] = W));
+  else W = q[12];
+  let G = W,
+    P;
+  if (q[13] !== O?.notice_is_grace_period)
     ((P = A7.default.createElement(
       h,
       { flexDirection: "column", gap: 1, flexGrow: 1 },
@@ -100,26 +113,26 @@
         ? A7.default.createElement(xtY, null)
         : A7.default.createElement(btY, null),
     )),
-      (q[10] = O?.notice_is_grace_period),
-      (q[11] = P));
-  else P = q[11];
+      (q[13] = O?.notice_is_grace_period),
+      (q[14] = P));
+  else P = q[14];
   let G;
-  if (q[12] === Symbol.for("react.memo_cache_sentinel"))
+  if (q[15] === Symbol.for("react.memo_cache_sentinel"))
     ((G = A7.default.createElement(
       h,
       { flexShrink: 0 },
       A7.default.createElement(Z, { color: "professionalBlue" }, ItY),
     )),
-      (q[12] = G));
-  else G = q[12];
+      (q[15] = V));
+  else V = q[15];
   let f;
-  if (q[13] !== P)
+  if (q[16] !== P)
     ((f = A7.default.createElement(h, { flexDirection: "row" }, P, G)),
-      (q[13] = P),
-      (q[14] = f));
-  else f = q[14];
+      (q[16] = P),
+      (q[17] = Z));
+  else Z = q[17];
   let V;
-  if (q[15] === Symbol.for("react.memo_cache_sentinel"))
+  if (q[18] === Symbol.for("react.memo_cache_sentinel"))
     ((V = A7.default.createElement(
       h,
       { flexDirection: "column" },
@@ -134,47 +147,28 @@
         "Your choice takes effect immediately upon confirmation.",
       ),
     )),
-      (q[15] = V));
-  else V = q[15];
+      (q[18] = N));
+  else N = q[18];
   let N;
-  if (q[16] !== O?.notice_is_grace_period)
+  if (q[19] !== O?.notice_is_grace_period)
     ((N = O?.notice_is_grace_period
       ? [{ label: "Not now", value: "defer" }]
       : []),
-      (q[16] = O?.notice_is_grace_period),
-      (q[17] = N));
-  else N = q[17];
-  let T;
-  if (q[18] !== W || q[19] !== N)
-    ((T = [...W, ...N]), (q[18] = W), (q[19] = N), (q[20] = T));
+      (q[19] = O?.notice_is_grace_period),
+      (q[20] = T));
   else T = q[20];
   let k;
-  if (q[21] !== j) ((k = (U) => j(U)), (q[21] = j), (q[22] = k));
-  else k = q[22];
+  if (q[21] !== M || q[22] !== T)
+    ((k = [...M, ...T]), (q[21] = M), (q[22] = T), (q[23] = k));
+  else k = q[23];
   let y;
-  if (q[23] !== O?.notice_is_grace_period || q[24] !== j)
-    ((y = () => {
-      if (O?.notice_is_grace_period) {
-        j("defer");
-        return;
-      }
-      j("escape");
-    }),
-      (q[23] = O?.notice_is_grace_period),
-      (q[24] = j),
-      (q[25] = y));
+  if (q[24] !== D) ((y = (m) => D(m)), (q[24] = D), (q[25] = y));
   else y = q[25];
   let B;
   if (q[26] !== T || q[27] !== k || q[28] !== y)
     ((B = A7.default.createElement(
       h,
-      {
-        flexDirection: "column",
-        gap: 1,
-        padding: 1,
-        borderStyle: "round",
-        borderColor: "professionalBlue",
-      },
+      { flexDirection: "column", gap: 1 },
       V,
       A7.default.createElement(ZA, { options: T, onChange: k, onCancel: y }),
     )),
@@ -184,59 +178,23 @@
       (q[29] = B));
   else B = q[29];
   let C;
-  if (q[30] !== B || q[31] !== f)
+  if (q[30] !== G || q[31] !== u || q[32] !== Z)
     ((C = A7.default.createElement(
       h,
       {
-        flexDirection: "column",
-        width: 100,
-        gap: 1,
-        paddingTop: 1,
-        paddingLeft: 1,
-        paddingRight: 1,
-        borderStyle: "round",
-        borderColor: "professionalBlue",
+        title: "Updates to Consumer Terms and Policies",
+        color: "professionalBlue",
+        borderDimColor: !1,
+        onCancel: G,
+        inputGuide: n1z,
       },
       f,
       B,
     )),
       (q[30] = B),
       (q[31] = f),
-      (q[32] = C));
-  else C = q[32];
-  let m;
-  if (q[33] !== _.keyName || q[34] !== _.pending)
-    ((m = A7.default.createElement(
-      h,
-      { marginLeft: 1 },
-      A7.default.createElement(
-        Z,
-        { dimColor: !0 },
-        _.pending
-          ? A7.default.createElement(
-              A7.default.Fragment,
-              null,
-              "Press ",
-              _.keyName,
-              " again to exit",
-            )
-          : A7.default.createElement(
-              A7.default.Fragment,
-              null,
-              "Enter to confirm · Esc to cancel",
-            ),
-      ),
-    )),
-      (q[33] = _.keyName),
-      (q[34] = _.pending),
-      (q[35] = m));
-  else m = q[35];
-  let u;
-  if (q[36] !== C || q[37] !== m)
-    ((u = A7.default.createElement(A7.default.Fragment, null, C, m)),
-      (q[36] = C),
-      (q[37] = m),
-      (q[38] = u));
-  else u = q[38];
+      (q[32] = Z),
+      (q[33] = S));
+  else S = q[33];
   return u;
 }

@@@ function 'pKq' (was 'Vqq') — structural (63.4%)
--- pretty-v2.1.31.js:485465
+++ pretty-v2.1.32.js:485188
@@ -1,7 +1,8 @@
 function Vqq() {
-  let q = kG1()
-    ? "Share Claude Code and earn extra usage"
-    : "Share Claude Code with friends";
+  let A = nt(),
+    q = A
+      ? `Share Claude Code and earn ${it(A)} of extra usage`
+      : "Share Claude Code with friends";
   return {
     title: "3 guest passes",
     lines: [],
@@ -16,7 +17,7 @@
         ),
         NR.createElement(Z, { dimColor: !0 }, q),
       ),
-      width: 38,
+      width: 48,
     },
     footer: "/passes",
   };

@@@ variable 'dP' (was 'VG') — structural (62.7%)
--- pretty-v2.1.31.js:446719
+++ pretty-v2.1.32.js:446666
@@ -254,10 +254,10 @@
                 "report the issue at https://github.com/anthropics/claude-code/issues",
               PACKAGE_URL: "@anthropic-ai/claude-code",
               README_URL: "https://code.claude.com/docs/en/overview",
-              VERSION: "2.1.31",
+              VERSION: "2.1.32",
               FEEDBACK_CHANNEL:
                 "https://github.com/anthropics/claude-code/issues",
-              BUILD_TIME: "2026-02-04T00:00:54Z",
+              BUILD_TIME: "2026-02-05T17:02:01Z",
             }.VERSION ?? "unknown",
         },
         { capabilities: { roots: {}, ...{} } },
@@ -301,6 +301,7 @@
               m(
                 new VF(
                   `MCP server "${A}" connection timed out after ${DG6()}ms`,
+                  "MCP connection timeout",
                 ),
               ));
           }, DG6());
@@ -735,6 +736,13 @@
                   elapsedTimeMs: Date.now() - D,
                 },
               });
+            if (j instanceof Error && !(j instanceof FE)) {
+              let M = j.constructor.name;
+              if (M === "Error")
+                throw new FE(j.message, j.message.slice(0, 200));
+              if (M === "McpError" && "code" in j && typeof j.code === "number")
+                throw new FE(j.message, `McpError ${j.code}`);
+            }
             throw j;
           }
         },

@@@ function 'n2q' (was 'zzq') — structural (62.3%)
--- pretty-v2.1.31.js:512377
+++ pretty-v2.1.32.js:512002
@@ -4,7 +4,34 @@
   let z = y6(),
     [w, H, O] = await Promise.all([rT(z), fbA(), T8z(q, K)]),
     $ = Lq(),
-    _ = new Set(A.map((J) => J.name));
+    _ = new Set(A.map((D) => D.name)),
+    J = [
+      yd("session_memory", () => a2q()),
+      Cd(
+        "auto_memory",
+        () => CjA(),
+        "MEMORY.md is read from disk each turn and can be edited by the model",
+      ),
+      Cd(
+        "ant_model_override",
+        () => s2q(),
+        "GrowthBook feature value can change via periodic refresh or auth change",
+      ),
+      yd("env_info_simple", () => r2q(q, K)),
+      yd("language", () => t2q($.language)),
+      Cd(
+        "output_style",
+        () => e2q(H),
+        "User can change output style mid-session via /output-style command",
+      ),
+      Cd(
+        "mcp_instructions",
+        () => Awq(Y),
+        "MCP servers connect/disconnect between turns",
+      ),
+      yd("scratchpad", () => zwq()),
+    ],
+    X = await cSA(J);
   return [
     W8z(H),
     P8z(_),
@@ -16,13 +43,6 @@
     r8("tengu_system_prompt_global_cache", !1)
       ? [MP1]
       : []),
-    Hzq(),
-    CDA(),
-    Ozq(),
-    O,
-    $zq($.language),
-    _zq(H),
-    Jzq(Y),
-    Wzq(),
+    ...X,
   ].filter((J) => J !== null);
 }

@@@ variable 'Q7' (was 'e7') — structural (61.9%)
--- pretty-v2.1.31.js:147570
+++ pretty-v2.1.32.js:147535
@@ -16,7 +16,16 @@
   Xw();
   Fk1();
   Q4();
-  ((nO1 = ["sonnet", "opus", "haiku", "best", "sonnet[1m]", "opusplan"]),
+  g4();
+  (($$1 = [
+    "sonnet",
+    "opus",
+    "haiku",
+    "best",
+    "sonnet[1m]",
+    "opus[1m]",
+    "opusplan",
+  ]),
     (jV5 = hA1),
     (sz7 = jV5.firstParty),
     (rO1 = [...nO1, "inherit"]));
@@ -26,7 +35,7 @@
   ((TV5 = {
     value: "opus",
     label: "Opus",
-    description: "Opus 4.5 · Most capable for complex work",
+    description: "Opus 4.6 · Most capable for complex work",
   }),
     (ez7 = {
       value: "sonnet[1m]",
@@ -34,6 +43,11 @@
       description: "Sonnet 4.5 with 1M context · Uses rate limits faster",
     }),
     (A27 = {
+      value: "opus[1m]",
+      label: "Opus (1M context)",
+      description: "Opus 4.6 with 1M context · Uses rate limits faster",
+    }),
+    (OT5 = {
       value: "sonnet",
       label: "Sonnet",
       description: "Sonnet 4.5 · Best for everyday tasks",

@@@ function 'l1z' (was 'xtY') — structural (61.7%)
--- pretty-v2.1.31.js:494550
+++ pretty-v2.1.32.js:494242
@@ -1,48 +1,34 @@
 function xtY() {
-  let A = t(10),
+  let A = A1(9),
     q;
   if (A[0] === Symbol.for("react.memo_cache_sentinel"))
     ((q = A7.default.createElement(
       Z,
-      { bold: !0, color: "professionalBlue" },
-      "Updates to Consumer Terms and Policies",
+      null,
+      "An update to our Consumer Terms and Privacy Policy will take effect on",
+      " ",
+      n7.default.createElement(f, { bold: !0 }, "October 8, 2025"),
+      ". You can accept the updated terms today.",
     )),
       (A[0] = q));
   else q = A[0];
   let K;
   if (A[1] === Symbol.for("react.memo_cache_sentinel"))
-    ((K = A7.default.createElement(
-      h,
-      { flexDirection: "column" },
-      q,
-      A7.default.createElement(
-        Z,
-        null,
-        "An update to our Consumer Terms and Privacy Policy will take effect on",
-        " ",
-        A7.default.createElement(Z, { bold: !0 }, "October 8, 2025"),
-        ". You can accept the updated terms today.",
-      ),
-    )),
-      (A[1] = K));
+    ((K = n7.default.createElement(f, null, "What's changing?")), (A[1] = K));
   else K = A[1];
-  let Y;
+  let Y, z;
   if (A[2] === Symbol.for("react.memo_cache_sentinel"))
-    ((Y = A7.default.createElement(Z, null, "What's changing?")), (A[2] = Y));
-  else Y = A[2];
-  let z, w;
-  if (A[3] === Symbol.for("react.memo_cache_sentinel"))
     ((z = A7.default.createElement(Z, null, "• ")),
       (w = A7.default.createElement(
         Z,
         { bold: !0 },
         "You can help improve Claude ",
       )),
-      (A[3] = z),
-      (A[4] = w));
-  else ((z = A[3]), (w = A[4]));
+      (A[2] = Y),
+      (A[3] = z));
+  else ((Y = A[2]), (z = A[3]));
   let H;
-  if (A[5] === Symbol.for("react.memo_cache_sentinel"))
+  if (A[4] === Symbol.for("react.memo_cache_sentinel"))
     ((H = A7.default.createElement(
       h,
       { paddingLeft: 1 },
@@ -62,10 +48,10 @@
         ),
       ),
     )),
-      (A[5] = H));
-  else H = A[5];
+      (A[4] = w));
+  else w = A[4];
   let O;
-  if (A[6] === Symbol.for("react.memo_cache_sentinel"))
+  if (A[5] === Symbol.for("react.memo_cache_sentinel"))
     ((O = A7.default.createElement(
       h,
       { flexDirection: "column" },
@@ -91,24 +77,24 @@
         ),
       ),
     )),
+      (A[5] = H));
+  else H = A[5];
+  let O;
+  if (A[6] === Symbol.for("react.memo_cache_sentinel"))
+    ((O = n7.default.createElement(q4, {
+      url: "https://www.anthropic.com/news/updates-to-our-consumer-terms",
+    })),
       (A[6] = O));
   else O = A[6];
   let $;
   if (A[7] === Symbol.for("react.memo_cache_sentinel"))
     (($ = A7.default.createElement(A4, {
-      url: "https://www.anthropic.com/news/updates-to-our-consumer-terms",
+      url: "https://anthropic.com/legal/terms",
     })),
       (A[7] = $));
   else $ = A[7];
   let _;
   if (A[8] === Symbol.for("react.memo_cache_sentinel"))
-    ((_ = A7.default.createElement(A4, {
-      url: "https://anthropic.com/legal/terms",
-    })),
-      (A[8] = _));
-  else _ = A[8];
-  let J;
-  if (A[9] === Symbol.for("react.memo_cache_sentinel"))
     ((J = A7.default.createElement(
       A7.default.Fragment,
       null,
@@ -128,7 +114,7 @@
         ")",
       ),
     )),
-      (A[9] = J));
-  else J = A[9];
+      (A[8] = _));
+  else _ = A[8];
   return J;
 }

@@@ function 'LpY' (was 'mgY') — structural (61.6%)
--- pretty-v2.1.31.js:456631
+++ pretty-v2.1.32.js:456428
@@ -35,7 +35,6 @@
 `,
         )
         .filter(Boolean),
-      $ = M8(),
       _ = we4(O, Y, $),
       J = He4(Y, z);
     if (J) {
@@ -68,7 +67,6 @@
 `,
                 )
                 .filter(Boolean),
-              W = M8(),
               P = we4(M, Y, W),
               G = He4(Y, z);
             if (G && P.length > 0) {

@@@ function 'yDq' (was 'mXq') — structural (61.4%)
--- pretty-v2.1.31.js:546666
+++ pretty-v2.1.32.js:547038
@@ -1,138 +1,139 @@
 function mXq(A, q, K, Y, z, w, H) {
-  let O = Y.message.id;
-  return Object.freeze({
-    tool: A,
-    input: q,
-    toolUseContext: K,
-    assistantMessage: Y,
-    messageId: O,
-    toolUseID: z,
-    logDecision(_, J) {
-      hN6(
-        {
-          tool: A,
-          input: J?.input ?? q,
-          toolUseContext: K,
-          messageId: O,
-          toolUseID: z,
-        },
-        _,
-        J?.permissionPromptStartTimeMs,
-      );
-    },
-    logCancelled() {
-      n("tengu_tool_use_cancelled", { messageID: O, toolName: Uq(A.name) });
-    },
-    async persistPermissions(_) {
-      if (_.length === 0) return !1;
-      gQ(_);
-      let J = await K.getAppState();
-      return (
-        w(MT(J.toolPermissionContext, _)),
-        _.some((X) => vAA(X.destination))
-      );
-    },
-    resolveIfAborted(_) {
-      if (!K.abortController.signal.aborted) return !1;
-      return (this.logCancelled(), _(this.cancelAndAbort(void 0, !0)), !0);
-    },
-    cancelAndAbort(_, J) {
-      let X = !!K.agentId,
-        D = _ ? `${X ? Lm1 : vu1}${_}` : X ? jh : YK1;
-      if (J || (!_ && !X))
-        (I(
-          `Aborting: tool=${A.name} isAbort=${J} hasFeedback=${!!_} isSubagent=${X}`,
-        ),
-          K.abortController.abort());
-      return { behavior: "ask", message: D };
-    },
-    async tryClassifier(_, J) {
-      if (A.name !== Q7 || !_) return null;
-      let X = await qD6(
-        _,
-        K.abortController.signal,
-        K.options.isNonInteractiveSession,
-      );
-      if (!X) return null;
-      return (
-        this.logDecision({
-          decision: "accept",
-          source: { type: "classifier" },
-        }),
-        this.buildAllow(J ?? q, { decisionReason: X })
-      );
-    },
-    async runHooks(_, J, X, D) {
-      for await (let j of sQ1(A.name, z, q, K, _, J, K.abortController.signal))
-        if (j.permissionRequestResult) {
-          let M = j.permissionRequestResult;
-          if (M.behavior === "allow") {
-            let W = M.updatedInput ?? X ?? q;
-            return await this.handleHookAllow(W, M.updatedPermissions ?? [], D);
-          } else if (M.behavior === "deny") {
-            if (
-              (this.logDecision(
-                { decision: "reject", source: { type: "hook" } },
-                { permissionPromptStartTimeMs: D },
-              ),
-              M.interrupt)
-            )
-              (I(`Hook interrupt: tool=${A.name} hookMessage=${M.message}`),
-                K.abortController.abort());
-            return this.buildDeny(M.message || "Permission denied by hook", {
-              type: "hook",
-              hookName: "PermissionRequest",
-              reason: M.message,
-            });
+  let O = Y.message.id,
+    $ = {
+      tool: A,
+      input: q,
+      toolUseContext: K,
+      assistantMessage: Y,
+      messageId: O,
+      toolUseID: z,
+      logDecision(_, J) {
+        AT6(
+          {
+            tool: A,
+            input: J?.input ?? q,
+            toolUseContext: K,
+            messageId: O,
+            toolUseID: z,
+          },
+          _,
+          J?.permissionPromptStartTimeMs,
+        );
+      },
+      logCancelled() {
+        c("tengu_tool_use_cancelled", { messageID: O, toolName: oq(A.name) });
+      },
+      async persistPermissions(_) {
+        if (_.length === 0) return !1;
+        nQ(_);
+        let J = await K.getAppState();
+        return (
+          w(kT(J.toolPermissionContext, _)),
+          _.some((X) => q8A(X.destination))
+        );
+      },
+      resolveIfAborted(_) {
+        if (!K.abortController.signal.aborted) return !1;
+        return (this.logCancelled(), _(this.cancelAndAbort(void 0, !0)), !0);
+      },
+      cancelAndAbort(_, J, X) {
+        let D = !!K.agentId,
+          j = _ ? `${D ? nm1 : pu1}${_}` : D ? kh : WK1;
+        if (J || (!_ && !X?.length && !D))
+          (h(
+            `Aborting: tool=${A.name} isAbort=${J} hasFeedback=${!!_} isSubagent=${D}`,
+          ),
+            K.abortController.abort());
+        return { behavior: "ask", message: j, contentBlocks: X };
+      },
+      ...{},
+      async runHooks(_, J, X, D) {
+        for await (let j of Ng1(
+          A.name,
+          z,
+          q,
+          K,
+          _,
+          J,
+          K.abortController.signal,
+        ))
+          if (j.permissionRequestResult) {
+            let M = j.permissionRequestResult;
+            if (M.behavior === "allow") {
+              let W = M.updatedInput ?? X ?? q;
+              return await this.handleHookAllow(
+                W,
+                M.updatedPermissions ?? [],
+                D,
+              );
+            } else if (M.behavior === "deny") {
+              if (
+                (this.logDecision(
+                  { decision: "reject", source: { type: "hook" } },
+                  { permissionPromptStartTimeMs: D },
+                ),
+                M.interrupt)
+              )
+                (h(`Hook interrupt: tool=${A.name} hookMessage=${M.message}`),
+                  K.abortController.abort());
+              return this.buildDeny(M.message || "Permission denied by hook", {
+                type: "hook",
+                hookName: "PermissionRequest",
+                reason: M.message,
+              });
+            }
           }
-        }
-      return null;
-    },
-    buildAllow(_, J) {
-      return {
-        behavior: "allow",
-        updatedInput: _,
-        userModified: J?.userModified ?? !1,
-        ...(J?.decisionReason && { decisionReason: J.decisionReason }),
-        ...(J?.acceptFeedback && { acceptFeedback: J.acceptFeedback }),
-      };
-    },
-    buildDeny(_, J) {
-      return { behavior: "deny", message: _, decisionReason: J };
-    },
-    async handleUserAllow(_, J, X, D) {
-      let j = await this.persistPermissions(J);
-      this.logDecision(
-        { decision: "accept", source: { type: "user", permanent: j } },
-        { input: _, permissionPromptStartTimeMs: D },
-      );
-      let M = A.inputsEquivalent ? !A.inputsEquivalent(q, _) : !1,
-        W = X?.trim();
-      return this.buildAllow(_, {
-        userModified: M,
-        acceptFeedback: W || void 0,
-      });
-    },
-    async handleHookAllow(_, J, X) {
-      let D = await this.persistPermissions(J);
-      return (
+        return null;
+      },
+      buildAllow(_, J) {
+        return {
+          behavior: "allow",
+          updatedInput: _,
+          userModified: J?.userModified ?? !1,
+          ...(J?.decisionReason && { decisionReason: J.decisionReason }),
+          ...(J?.acceptFeedback && { acceptFeedback: J.acceptFeedback }),
+          ...(J?.contentBlocks &&
+            J.contentBlocks.length > 0 && { contentBlocks: J.contentBlocks }),
+        };
+      },
+      buildDeny(_, J) {
+        return { behavior: "deny", message: _, decisionReason: J };
+      },
+      async handleUserAllow(_, J, X, D, j) {
+        let M = await this.persistPermissions(J);
         this.logDecision(
           { decision: "accept", source: { type: "hook", permanent: D } },
           { input: _, permissionPromptStartTimeMs: X },
-        ),
-        this.buildAllow(_, {
-          decisionReason: { type: "hook", hookName: "PermissionRequest" },
-        })
-      );
-    },
-    pushToQueue(_) {
-      H?.((J) => [...J, _]);
-    },
-    removeFromQueue() {
-      H?.((_) => _.filter((J) => J.toolUseID !== z));
-    },
-    updateQueueItem(_) {
-      H?.((J) => J.map((X) => (X.toolUseID === z ? { ...X, ..._ } : X)));
-    },
-  });
+        );
+        let W = A.inputsEquivalent ? !A.inputsEquivalent(q, _) : !1,
+          G = X?.trim();
+        return this.buildAllow(_, {
+          userModified: W,
+          acceptFeedback: G || void 0,
+          contentBlocks: j,
+        });
+      },
+      async handleHookAllow(_, J, X) {
+        let D = await this.persistPermissions(J);
+        return (
+          this.logDecision(
+            { decision: "accept", source: { type: "hook", permanent: D } },
+            { input: _, permissionPromptStartTimeMs: X },
+          ),
+          this.buildAllow(_, {
+            decisionReason: { type: "hook", hookName: "PermissionRequest" },
+          })
+        );
+      },
+      pushToQueue(_) {
+        H?.push(_);
+      },
+      removeFromQueue() {
+        H?.remove(z);
+      },
+      updateQueueItem(_) {
+        H?.update(z, _);
+      },
+    };
+  return Object.freeze($);
 }

@@@ variable 'Ow7' (was 'k27') — structural (61.0%)
--- pretty-v2.1.31.js:148334
+++ pretty-v2.1.32.js:148326
@@ -104,6 +104,9 @@
         version_base: KK(A.version_base)
           ? globalThis.String(A.version_base)
           : "",
+        coworker_type: Mq(A.coworker_type)
+          ? globalThis.String(A.coworker_type)
+          : "",
       };
     },
     toJSON(A) {
@@ -151,6 +154,7 @@
         q.deployment_environment = A.deployment_environment;
       if (A.is_conductor !== void 0) q.is_conductor = A.is_conductor;
       if (A.version_base !== void 0) q.version_base = A.version_base;
+      if (A.coworker_type !== void 0) q.coworker_type = A.coworker_type;
       return q;
     },
     create(A) {
@@ -192,6 +196,45 @@
         (q.deployment_environment = A.deployment_environment ?? ""),
         (q.is_conductor = A.is_conductor ?? !1),
         (q.version_base = A.version_base ?? ""),
+        (q.coworker_type = A.coworker_type ?? ""),
+        q
+      );
+    },
+  };
+  g86 = {
+    fromJSON(A) {
+      return {
+        slack_team_id: Mq(A.slack_team_id)
+          ? globalThis.String(A.slack_team_id)
+          : "",
+        is_enterprise_install: Mq(A.is_enterprise_install)
+          ? globalThis.Boolean(A.is_enterprise_install)
+          : !1,
+        trigger: Mq(A.trigger) ? globalThis.String(A.trigger) : "",
+        creation_method: Mq(A.creation_method)
+          ? globalThis.String(A.creation_method)
+          : "",
+      };
+    },
+    toJSON(A) {
+      let q = {};
+      if (A.slack_team_id !== void 0) q.slack_team_id = A.slack_team_id;
+      if (A.is_enterprise_install !== void 0)
+        q.is_enterprise_install = A.is_enterprise_install;
+      if (A.trigger !== void 0) q.trigger = A.trigger;
+      if (A.creation_method !== void 0) q.creation_method = A.creation_method;
+      return q;
+    },
+    create(A) {
+      return g86.fromPartial(A ?? {});
+    },
+    fromPartial(A) {
+      let q = BT5();
+      return (
+        (q.slack_team_id = A.slack_team_id ?? ""),
+        (q.is_enterprise_install = A.is_enterprise_install ?? !1),
+        (q.trigger = A.trigger ?? ""),
+        (q.creation_method = A.creation_method ?? ""),
         q
       );
     },
@@ -241,6 +284,8 @@
           ? globalThis.String(A.parent_session_id)
           : "",
         agent_type: KK(A.agent_type) ? globalThis.String(A.agent_type) : "",
+        slack: Mq(A.slack) ? g86.fromJSON(A.slack) : void 0,
+        team_name: Mq(A.team_name) ? globalThis.String(A.team_name) : "",
       };
     },
     toJSON(A) {
@@ -277,6 +322,8 @@
       if (A.parent_session_id !== void 0)
         q.parent_session_id = A.parent_session_id;
       if (A.agent_type !== void 0) q.agent_type = A.agent_type;
+      if (A.slack !== void 0) q.slack = g86.toJSON(A.slack);
+      if (A.team_name !== void 0) q.team_name = A.team_name;
       return q;
     },
     create(A) {
@@ -313,6 +360,11 @@
         (q.agent_id = A.agent_id ?? ""),
         (q.parent_session_id = A.parent_session_id ?? ""),
         (q.agent_type = A.agent_type ?? ""),
+        (q.slack =
+          A.slack !== void 0 && A.slack !== null
+            ? g86.fromPartial(A.slack)
+            : void 0),
+        (q.team_name = A.team_name ?? ""),
         q
       );
     },

@@@ variable 'xcY' (was 'k1q') — structural (60.7%)
--- pretty-v2.1.31.js:463006
+++ pretty-v2.1.32.js:463005
@@ -1,33 +1,13 @@
-var k1q = E(() => {
-  Zk();
-  f7();
-  BS();
-  rz();
-  ((IpY = {
-    type: "local",
-    name: "cost",
-    description: "Show the total cost and duration of the current session",
-    isEnabled: () => !0,
-    get isHidden() {
-      return q7();
-    },
-    supportsNonInteractive: !0,
-    async call() {
-      if ((U4("cost"), q7())) {
-        let A;
-        if (NV.isUsingOverage)
-          A =
-            "You are currently using your overages to power your Claude Code usage. We will automatically switch you back to your subscription rate limits when they reset";
-        else
-          A =
-            "You are currently using your subscription to power your Claude Code usage";
-        return { type: "text", value: A };
-      }
-      return { type: "text", value: F1A() };
-    },
-    userFacingName() {
-      return "cost";
-    },
-  }),
-    (E1q = IpY));
-});
+var xcY = async () => {
+  if ((B4("cost"), U8())) {
+    let A;
+    if (WV.isUsingOverage)
+      A =
+        "You are currently using your overages to power your Claude Code usage. We will automatically switch you back to your subscription rate limits when they reset";
+    else
+      A =
+        "You are currently using your subscription to power your Claude Code usage";
+    return { type: "text", value: A };
+  }
+  return { type: "text", value: M6A() };
+};

@@@ function 'yjA' (was 'yDA') — structural (60.5%)
--- pretty-v2.1.31.js:295524
+++ pretty-v2.1.32.js:297355
@@ -17,10 +17,11 @@
     `As you work, consult your memory files to build on previous experience. When you encounter a mistake that seems like it could be common, check your ${q} for relevant notes — and if nothing is written yet, record what you learned.`,
     "",
     "Guidelines:",
+    `- \`${fa}\` is always loaded into your system prompt — lines after ${_u1} will be truncated, so keep it concise`,
+    "- Create separate topic files (e.g., `debugging.md`, `patterns.md`) for detailed notes and link to them from MEMORY.md",
     "- Record insights about problem constraints, strategies that worked or failed, and lessons learned",
     "- Update or remove memories that turn out to be wrong or outdated",
     "- Organize memory semantically by topic, not chronologically",
-    `- \`${Fq1}\` is always loaded into your system prompt — lines after ${db1} will be truncated, so keep it concise and link to other files in your ${q} directory for details`,
     "- Use the Write and Edit tools to update your memory files",
     ...(Y ?? []),
     "",
@@ -28,14 +29,20 @@
   if (H.trim()) {
     let $ = H.trim().split(`
 `),
-      _ = H.trim();
-    if ($.length > db1)
+      _ = $.length > _u1;
+    c("tengu_memdir_loaded", {
+      content_length: H.length,
+      line_count: $.length,
+      was_truncated: _,
+    });
+    let J = H.trim();
+    if (_)
       _ =
         $.slice(0, db1).join(`
 `) +
         `
 
-> ⚠️ ${Fq1} is ${$.length} lines (limit: ${db1}). Only the first ${db1} lines were loaded. Please compact or reorganize it.`;
+> WARNING: ${fa} is ${$.length} lines (limit: ${_u1}). Only the first ${_u1} lines were loaded. Move detailed content into separate topic files and keep ${fa} as a concise index.`;
     O.push(`## ${Fq1}`, "", _);
   } else
     O.push(

@@@ function 'TPY' (was 'NWY') — structural (60.3%)
--- pretty-v2.1.31.js:389974
+++ pretty-v2.1.32.js:389499
@@ -24,6 +24,7 @@
         addMargin: K,
         attachment: A.attachment,
         verbose: w,
+        isTranscriptMode: D,
       });
     case "assistant":
       return K9.createElement(
@@ -52,6 +53,11 @@
         ),
       );
     case "user": {
+      if (A.isCompactSummary)
+        return S5.createElement(Cx4, {
+          message: A,
+          screen: D ? "transcript" : "prompt",
+        });
       let f = 0,
         V = G === A.uuid,
         N = K9.createElement(
@@ -72,6 +78,7 @@
               imageIndex: y ?? f,
               isUserContinuation: W,
               lookups: q,
+              isTranscriptMode: D,
             });
           }),
         );

@@@ function 'Vf9' (was 'ZaY') — structural (60.0%)
--- pretty-v2.1.31.js:484865
+++ pretty-v2.1.32.js:252941
@@ -1,3 +1,3 @@
 function ZaY(A) {
-  return A.id === "opus-4.5-available";
+  return A.type === "image";
 }

@@@ function 'GNA' (was 'FVA') — structural (59.5%)
--- pretty-v2.1.31.js:365378
+++ pretty-v2.1.32.js:365698
@@ -1,6 +1,7 @@
-function FVA(A, q, K) {
-  let Y = K ? ` color="${K}"` : "";
-  return `<${Q_} teammate_id="${A}"${Y}>
+function GNA(A, q, K, Y) {
+  let z = K ? ` color="${K}"` : "",
+    w = Y ? ` summary="${Y}"` : "";
+  return `<${U_} teammate_id="${A}"${z}${w}>
 ${q}
 </${Q_}>`;
 }

@@@ function 'yG6' (was '$P6') — structural (59.3%)
--- pretty-v2.1.31.js:434907
+++ pretty-v2.1.32.js:434805
@@ -1,3 +1,4 @@
 function $P6() {
+  if (h9()) return "coordinator";
   return r8(xIY, "user_intent");
 }

@@@ function 'YI' (was 'dh') — structural (59.1%)
--- pretty-v2.1.31.js:435116
+++ pretty-v2.1.32.js:435020
@@ -1,8 +1,10 @@
 function dh(A, q, K) {
+  let Y = K ?? yG6();
   n("tengu_prompt_suggestion", {
     outcome: "suppressed",
     reason: A,
-    prompt_id: K ?? $P6(),
+    prompt_id: Y,
+    coordinator_mode: h9(),
     ...!1,
   });
 }

@@@ function 'i3q' (was 'fKq') — structural (59.0%)
--- pretty-v2.1.31.js:490393
+++ pretty-v2.1.32.js:490091
@@ -1,5 +1,5 @@
 function fKq(A) {
-  let q = t(63),
+  let q = A1(61),
     { agent: K, onDone: Y, onKillAgent: z, onBack: w, onForeground: H } = A,
     O;
   if (q[0] !== K.agentId)
@@ -18,8 +18,7 @@
   let M = j,
     W = K31(K.startTime, K.status === "running"),
     P;
-  if (q[5] !== Y)
-    ((P = { "confirm:no": Y, "confirm:yes": Y }), (q[5] = Y), (q[6] = P));
+  if (q[5] !== Y) ((G = { "confirm:yes": Y }), (q[5] = Y), (q[6] = G));
   else P = q[6];
   let G;
   if (q[7] === Symbol.for("react.memo_cache_sentinel"))
@@ -48,8 +47,7 @@
       (q[13] = f));
   else f = q[13];
   eA(f);
-  let V = v7(),
-    N;
+  let Z;
   if (q[14] !== K.prompt)
     ((N = p4(K.prompt, "plan")), (q[14] = K.prompt), (q[15] = N));
   else N = q[15];
@@ -57,19 +55,18 @@
     k = K.prompt.length > 300 ? K.prompt.substring(0, 297) + "…" : K.prompt,
     y = K.result?.totalTokens ?? K.progress?.tokenCount,
     B = K.result?.totalToolUseCount ?? K.progress?.toolUseCount,
+    u = K.selectedAgent?.agentType ?? "agent",
     C = K.description || "Async agent",
     m;
-  if (q[16] !== C)
-    ((m = F9.default.createElement(
-      h,
-      null,
-      F9.default.createElement(Z, { color: "background", bold: !0 }, C),
-    )),
+  if (q[16] !== u || q[17] !== S)
+    ((m = $z.default.createElement(f, null, u, " ›", " ", S)),
       (q[16] = C),
-      (q[17] = m));
-  else m = q[17];
-  let u;
-  if (q[18] !== K.status)
+      (q[17] = S),
+      (q[18] = m));
+  else m = q[18];
+  let b = m,
+    U;
+  if (q[19] !== K.status)
     ((u =
       K.status !== "running" &&
       F9.default.createElement(
@@ -84,11 +81,11 @@
             : "Killed",
         " · ",
       )),
-      (q[18] = K.status),
-      (q[19] = u));
-  else u = q[19];
+      (q[19] = K.status),
+      (q[20] = U));
+  else U = q[20];
   let U;
-  if (q[20] !== y)
+  if (q[21] !== k)
     ((U =
       y !== void 0 &&
       y > 0 &&
@@ -99,11 +96,11 @@
         pK(y),
         " tokens",
       )),
-      (q[20] = y),
-      (q[21] = U));
-  else U = q[21];
+      (q[21] = k),
+      (q[22] = g));
+  else g = q[22];
   let g;
-  if (q[22] !== B)
+  if (q[23] !== y)
     ((g =
       B !== void 0 &&
       B > 0 &&
@@ -116,33 +113,73 @@
         " ",
         B === 1 ? "tool" : "tools",
       )),
-      (q[22] = B),
-      (q[23] = g));
-  else g = q[23];
+      (q[23] = y),
+      (q[24] = x));
+  else x = q[24];
   let x;
-  if (q[24] !== W || q[25] !== U || q[26] !== g)
+  if (q[25] !== W || q[26] !== g || q[27] !== x)
     ((x = F9.default.createElement(Z, { dimColor: !0 }, W, U, g)),
-      (q[24] = W),
       (q[25] = U),
       (q[26] = g),
-      (q[27] = x));
-  else x = q[27];
+      (q[27] = x),
+      (q[28] = p));
+  else p = q[28];
   let d;
-  if (q[28] !== u || q[29] !== x)
+  if (q[29] !== U || q[30] !== p)
     ((d = F9.default.createElement(h, null, u, x)),
-      (q[28] = u),
       (q[29] = x),
-      (q[30] = d));
-  else d = q[30];
+      (q[30] = p),
+      (q[31] = n));
+  else n = q[31];
+  let r = n,
+    z1;
+  if (q[32] !== K.status || q[33] !== w || q[34] !== H || q[35] !== z)
+    ((z1 = (G1) =>
+      G1.pending
+        ? $z.default.createElement(
+            f,
+            null,
+            "Press ",
+            G1.keyName,
+            " again to exit",
+          )
+        : $z.default.createElement(
+            pA,
+            null,
+            w &&
+              $z.default.createElement(YA, {
+                shortcut: "←",
+                action: "go back",
+              }),
+            $z.default.createElement(YA, {
+              shortcut: "Esc/Enter/Space",
+              action: "close",
+            }),
+            K.status === "running" &&
+              z &&
+              $z.default.createElement(YA, { shortcut: "k", action: "kill" }),
+            K.status === "running" &&
+              H &&
+              $z.default.createElement(YA, {
+                shortcut: "f",
+                action: "foreground",
+              }),
+          )),
+      (q[32] = K.status),
+      (q[33] = w),
+      (q[34] = H),
+      (q[35] = z),
+      (q[36] = z1));
+  else z1 = q[36];
   let r;
-  if (q[31] !== K.progress || q[32] !== K.status || q[33] !== D)
+  if (q[37] !== K.progress || q[38] !== K.status || q[39] !== D)
     ((r =
       K.status === "running" &&
       K.progress?.recentActivities &&
       K.progress.recentActivities.length > 0 &&
       F9.default.createElement(
         h,
-        { flexDirection: "column", marginTop: 1 },
+        { flexDirection: "column" },
         F9.default.createElement(Z, { bold: !0, dimColor: !0 }, "Progress"),
         K.progress.recentActivities.map((w1, Z1) =>
           F9.default.createElement(
@@ -157,13 +194,13 @@
           ),
         ),
       )),
-      (q[31] = K.progress),
-      (q[32] = K.status),
-      (q[33] = D),
-      (q[34] = r));
-  else r = q[34];
+      (q[37] = K.progress),
+      (q[38] = K.status),
+      (q[39] = D),
+      (q[40] = f1));
+  else f1 = q[40];
   let c;
-  if (q[35] !== X || q[36] !== _)
+  if (q[41] !== X || q[42] !== _)
     ((c =
       _.length > 0 &&
       F9.default.createElement(
@@ -180,12 +217,12 @@
         ),
         F9.default.createElement(As, { todos: _ }),
       )),
-      (q[35] = X),
-      (q[36] = _),
-      (q[37] = c));
-  else c = q[37];
+      (q[41] = X),
+      (q[42] = _),
+      (q[43] = Z1));
+  else Z1 = q[43];
   let q1;
-  if (q[38] !== k || q[39] !== T)
+  if (q[44] !== T || q[45] !== N)
     ((q1 = T
       ? F9.default.createElement(
           h,
@@ -198,12 +235,12 @@
           F9.default.createElement(Z, { bold: !0, dimColor: !0 }, "Prompt"),
           F9.default.createElement(Z, { wrap: "wrap" }, k),
         )),
-      (q[38] = k),
-      (q[39] = T),
-      (q[40] = q1));
-  else q1 = q[40];
+      (q[44] = T),
+      (q[45] = N),
+      (q[46] = H1));
+  else H1 = q[46];
   let H1;
-  if (q[41] !== K.error || q[42] !== K.status)
+  if (q[47] !== K.error || q[48] !== K.status)
     ((H1 =
       K.status === "failed" &&
       K.error &&
@@ -213,12 +250,12 @@
         F9.default.createElement(Z, { bold: !0, color: "error" }, "Error"),
         F9.default.createElement(Z, { color: "error", wrap: "wrap" }, K.error),
       )),
-      (q[41] = K.error),
-      (q[42] = K.status),
-      (q[43] = H1));
-  else H1 = q[43];
+      (q[47] = K.error),
+      (q[48] = K.status),
+      (q[49] = D1));
+  else D1 = q[49];
   let $1;
-  if (q[44] !== r || q[45] !== c || q[46] !== q1 || q[47] !== H1)
+  if (q[50] !== f1 || q[51] !== Z1 || q[52] !== H1 || q[53] !== D1)
     (($1 = F9.default.createElement(
       h,
       { flexDirection: "column" },
@@ -227,104 +264,31 @@
       q1,
       H1,
     )),
-      (q[44] = r),
-      (q[45] = c),
-      (q[46] = q1),
-      (q[47] = H1),
-      (q[48] = $1));
-  else $1 = q[48];
-  let A1;
-  if (q[49] !== d || q[50] !== $1 || q[51] !== m)
-    ((A1 = F9.default.createElement(
-      h,
-      { width: "100%" },
-      F9.default.createElement(
-        h,
-        {
-          borderStyle: "round",
-          borderColor: "background",
-          flexDirection: "column",
-          marginTop: 1,
-          paddingLeft: 1,
-          paddingRight: 1,
-          width: "100%",
-        },
-        m,
-        d,
-        $1,
-      ),
-    )),
-      (q[49] = d),
       (q[50] = $1),
       (q[51] = m),
-      (q[52] = A1));
-  else A1 = q[52];
+      (q[52] = H1),
+      (q[53] = D1),
+      (q[54] = t));
+  else t = q[54];
   let O1;
-  if (
-    q[53] !== K.status ||
-    q[54] !== V.keyName ||
-    q[55] !== V.pending ||
-    q[56] !== w ||
-    q[57] !== H ||
-    q[58] !== z
-  )
+  if (q[55] !== Y || q[56] !== r || q[57] !== z1 || q[58] !== t || q[59] !== b)
     ((O1 = F9.default.createElement(
       h,
-      { marginLeft: 2 },
-      V.pending
-        ? F9.default.createElement(
-            Z,
-            { dimColor: !0 },
-            "Press ",
-            V.keyName,
-            " again to exit",
-          )
-        : F9.default.createElement(
-            Z,
-            { dimColor: !0 },
-            F9.default.createElement(
-              nA,
-              null,
-              w &&
-                F9.default.createElement(_A, {
-                  shortcut: "←",
-                  action: "go back",
-                }),
-              F9.default.createElement(_A, {
-                shortcut: "Esc/Enter/Space",
-                action: "close",
-              }),
-              K.status === "running" &&
-                z &&
-                F9.default.createElement(_A, { shortcut: "k", action: "kill" }),
-              K.status === "running" &&
-                H &&
-                F9.default.createElement(_A, {
-                  shortcut: "f",
-                  action: "foreground",
-                }),
-            ),
-          ),
+      {
+        title: b,
+        subtitle: r,
+        onCancel: Y,
+        color: "background",
+        inputGuide: z1,
+      },
+      t,
     )),
-      (q[53] = K.status),
-      (q[54] = V.keyName),
-      (q[55] = V.pending),
+      (q[55] = Y),
       (q[56] = w),
       (q[57] = H),
       (q[58] = z),
-      (q[59] = O1));
-  else O1 = q[59];
-  let s;
-  if (q[60] !== A1 || q[61] !== O1)
-    ((s = F9.default.createElement(
-      h,
-      { width: "100%", flexDirection: "column" },
-      A1,
-      O1,
-    )),
-      (q[60] = A1),
-      (q[61] = O1),
-      (q[62] = s));
-  else s = q[62];
+      (q[59] = b),
+      (q[60] = e));
+  else e = q[60];
   return s;
 }

@@@ function 'T08' (was 'lX8') — structural (58.6%)
--- pretty-v2.1.31.js:78234
+++ pretty-v2.1.32.js:78094
@@ -1,6 +1,14 @@
 async function lX8() {
-  if (W6().oauthAccount || !q7()) return !1;
   let q = o4();
+  if (
+    (A.oauthAccount &&
+      A.oauthAccount.billingType !== void 0 &&
+      A.oauthAccount.accountCreatedAt !== void 0 &&
+      A.oauthAccount.subscriptionCreatedAt !== void 0) ||
+    !U8()
+  )
+    return !1;
+  let q = n4();
   if (q?.accessToken) {
     let K = await Zw1(q.accessToken);
     if (K)
@@ -12,6 +20,9 @@
           displayName: K.account.display_name || void 0,
           hasExtraUsageEnabled: K.organization.has_extra_usage_enabled ?? !1,
           billingType: K.organization.billing_type ?? void 0,
+          accountCreatedAt: K.account.created_at,
+          subscriptionCreatedAt:
+            K.organization.subscription_created_at ?? void 0,
         }),
         !0
       );

@@@ function 'bXq' (was 'd_q') — structural (58.4%)
--- pretty-v2.1.31.js:540448
+++ pretty-v2.1.32.js:540662
@@ -6,9 +6,12 @@
       q = 0;
       break A;
     }
-    let K = 0;
-    for (let Y of Object.values(A))
-      if (Y.type === "local_agent" && !_Z1(Y.status)) K++;
+    let K = Date.now(),
+      Y = Object.values(A).filter(fwz),
+      z = 0;
+    for (let w of Y)
+      if (!kZ1(w.status)) z++;
+      else if (w.status === "killed" && w.endTime && K - w.endTime < 3000) z++;
     q = K;
   }
   return q;

@@@ function 'd$q' (was 'eHq') — structural (58.4%)
--- pretty-v2.1.31.js:527909
+++ pretty-v2.1.32.js:527851
@@ -1,11 +1,12 @@
 function eHq(A) {
-  let q = t(34),
+  let q = A1(37),
     {
       onChange: K,
       options: Y,
       input: z,
       filePath: w,
       ideName: H,
+      symlinkTarget: O,
       rejectFeedback: O,
       acceptFeedback: $,
       setFocusedOption: _,
@@ -32,17 +33,31 @@
       (q[2] = W));
   else W = q[2];
   let P;
-  if (q[3] === Symbol.for("react.memo_cache_sentinel"))
+  if (q[3] !== O)
     ((P =
+      O &&
+      HE.default.createElement(
+        f,
+        { color: "warning" },
+        $Yz(y6(), O).startsWith("..")
+          ? `This will modify ${O} (outside working directory) via a symlink`
+          : `Symlink target: ${O}`,
+      )),
+      (q[3] = O),
+      (q[4] = P));
+  else P = q[4];
+  let V;
+  if (q[5] === Symbol.for("react.memo_cache_sentinel"))
+    ((V =
       gS1() &&
       yR.default.createElement(Z, { dimColor: !0 }, "Save file to continue…")),
-      (q[3] = P));
-  else P = q[3];
+      (q[5] = V));
+  else V = q[5];
   let G;
-  if (q[4] !== w) ((G = i3z(w)), (q[4] = w), (q[5] = G));
-  else G = q[5];
+  if (q[6] !== w) ((Z = OYz(w)), (q[6] = w), (q[7] = Z));
+  else Z = q[7];
   let f;
-  if (q[6] !== G)
+  if (q[8] !== Z)
     ((f = yR.default.createElement(
       Z,
       null,
@@ -51,11 +66,11 @@
       yR.default.createElement(Z, { bold: !0 }, G),
       "?",
     )),
-      (q[6] = G),
-      (q[7] = f));
-  else f = q[7];
+      (q[8] = Z),
+      (q[9] = N));
+  else N = q[9];
   let V;
-  if (q[8] !== $ || q[9] !== z || q[10] !== K || q[11] !== Y || q[12] !== O)
+  if (q[10] !== _ || q[11] !== z || q[12] !== K || q[13] !== Y || q[14] !== $)
     ((V = (u) => {
       let U = Y.find((g) => g.value === u);
       if (U) {
@@ -72,25 +87,25 @@
         K(U.option, z);
       }
     }),
-      (q[8] = $),
-      (q[9] = z),
       (q[10] = K),
       (q[11] = Y),
       (q[12] = O),
-      (q[13] = V));
-  else V = q[13];
-  let N;
-  if (q[14] !== z || q[15] !== K)
-    ((N = () => K({ type: "reject" }, z)),
+      (q[13] = Y),
       (q[14] = z),
-      (q[15] = K),
-      (q[16] = N));
-  else N = q[16];
+      (q[15] = T));
+  else T = q[15];
   let T;
-  if (q[17] !== _) ((T = (u) => _(u)), (q[17] = _), (q[18] = T));
+  if (q[16] !== z || q[17] !== K)
+    ((k = () => K({ type: "reject" }, z)),
+      (q[16] = z),
+      (q[17] = K),
+      (q[18] = k));
   else T = q[18];
   let k;
-  if (q[19] !== J || q[20] !== Y || q[21] !== V || q[22] !== N || q[23] !== T)
+  if (q[19] !== J) ((y = (g) => J(g)), (q[19] = J), (q[20] = y));
+  else y = q[20];
+  let u;
+  if (q[21] !== X || q[22] !== Y || q[23] !== T || q[24] !== k || q[25] !== y)
     ((k = yR.default.createElement(ZA, {
       options: Y,
       inlineDescriptions: !0,
@@ -99,33 +114,33 @@
       onFocus: T,
       onInputModeToggle: J,
     })),
-      (q[19] = J),
-      (q[20] = Y),
       (q[21] = V),
       (q[22] = N),
       (q[23] = T),
-      (q[24] = k));
-  else k = q[24];
+      (q[24] = k),
+      (q[25] = y),
+      (q[26] = u));
+  else u = q[26];
   let y;
-  if (q[25] !== f || q[26] !== k)
+  if (q[27] !== u || q[28] !== N)
     ((y = yR.default.createElement(h, { flexDirection: "column" }, f, k)),
-      (q[25] = f),
-      (q[26] = k),
-      (q[27] = y));
-  else y = q[27];
+      (q[27] = u),
+      (q[28] = N),
+      (q[29] = S));
+  else S = q[29];
   let B = ((X === "yes" && !D) || (X === "no" && !j)) && " · Tab to amend",
     C;
-  if (q[28] !== B)
+  if (q[30] !== m)
     ((C = yR.default.createElement(
       h,
       { marginTop: 1 },
       yR.default.createElement(Z, { dimColor: !0 }, "Esc to cancel", B),
     )),
-      (q[28] = B),
-      (q[29] = C));
-  else C = q[29];
+      (q[30] = m),
+      (q[31] = b));
+  else b = q[31];
   let m;
-  if (q[30] !== y || q[31] !== C || q[32] !== W)
+  if (q[32] !== S || q[33] !== b || q[34] !== G || q[35] !== P)
     ((m = yR.default.createElement(
       h,
       { flexDirection: "column" },
@@ -137,12 +152,14 @@
         P,
         y,
         C,
+        b,
       ),
     )),
-      (q[30] = y),
-      (q[31] = C),
       (q[32] = W),
-      (q[33] = m));
-  else m = q[33];
+      (q[33] = b),
+      (q[34] = G),
+      (q[35] = P),
+      (q[36] = U));
+  else U = q[36];
   return m;
 }

@@@ variable 'dj6' (was 'tG') — structural (57.9%)
--- pretty-v2.1.31.js:437521
+++ pretty-v2.1.32.js:422874
@@ -27,4 +27,5 @@
   tn4();
   UU();
   h6();
+  hp();
 });

@@@ variable 'qt4' (was 'xN6') — structural (57.9%)
--- pretty-v2.1.31.js:546804
+++ pretty-v2.1.32.js:449145
@@ -8,4 +8,8 @@
   tBA();
   tG();
   _6();
+  Px();
+  Z7();
+  C21();
+  iD();
 });

@@@ variable 'L1q' (was 'qmA') — structural (57.9%)
--- pretty-v2.1.31.js:547811
+++ pretty-v2.1.32.js:457101
@@ -13,4 +13,5 @@
   GP1();
   s6();
   OW1();
+  Lw();
 });

@@@ variable '$zq' (was 'afq') — structural (57.9%)
--- pretty-v2.1.31.js:559914
+++ pretty-v2.1.32.js:504333
@@ -6,8 +6,4 @@
   bu();
   pG1();
   iD();
-  Gp1();
-  f7();
-  N6();
-  Np1();
 });

@@@ variable 'k2q' (was 'VVq') — structural (57.9%)
--- pretty-v2.1.31.js:561419
+++ pretty-v2.1.32.js:508191
@@ -6,29 +6,4 @@
   mV();
   gT();
   Zk();
-  F31();
-  zM();
-  Dd();
-  yq();
-  D8();
-  uu();
-  qmA();
-  s6();
-  e7();
-  b$6();
-  Bk();
-  Wz();
-  f7();
-  FQ1();
-  Ou1();
-  OH();
-  uA();
-  j2();
-  CB();
-  C8();
-  zJ();
-  N6();
-  zZ();
-  lV6();
-  zP6();
 });

@@@ variable '$d' (was 'AFA') — structural (57.9%)
--- pretty-v2.1.31.js:563893
+++ pretty-v2.1.32.js:514699
@@ -4,4 +4,14 @@
   s6();
   _6();
   v11();
+  EO();
+  BA();
+  OZ6();
+  V$();
+  eA();
+  g4();
+  _6();
+  $w();
+  E0();
+  N9();
 });

@@@ function 'g3q' (was 'jKq') — structural (57.3%)
--- pretty-v2.1.31.js:489632
+++ pretty-v2.1.32.js:489421
@@ -1,5 +1,5 @@
 function jKq(A) {
-  let q = t(51),
+  let q = A1(47),
     { shell: K, onDone: Y, onKillShell: z, onBack: w } = A,
     { columns: H } = A8(),
     [O, $] = BU1.useState(0),
@@ -16,8 +16,7 @@
   else D = q[2];
   let j = D,
     M;
-  if (q[3] !== j)
-    ((M = { "confirm:no": j, "confirm:yes": j }), (q[3] = j), (q[4] = M));
+  if (q[3] !== j) ((M = { "confirm:yes": j }), (q[3] = j), (q[4] = M));
   else M = q[4];
   let W;
   if (q[5] === Symbol.for("react.memo_cache_sentinel"))
@@ -38,8 +37,7 @@
       (q[10] = P));
   else P = q[10];
   eA(P);
-  let G = v7(),
-    f = xsY,
+  let P = ceY,
     V;
   if (q[11] !== K.id || q[12] !== K.status)
     ((V = () => {
@@ -68,24 +66,43 @@
   let T =
       K.command.length > 280 ? K.command.substring(0, 277) + "…" : K.command,
     k;
-  if (q[18] === Symbol.for("react.memo_cache_sentinel"))
-    ((k = Cz.default.createElement(
-      h,
-      null,
-      Cz.default.createElement(
-        Z,
-        { color: "background", bold: !0 },
-        "Shell details",
-      ),
-    )),
-      (q[18] = k));
-  else k = q[18];
+  if (q[18] !== w || q[19] !== z || q[20] !== K.status)
+    ((T = (r) =>
+      r.pending
+        ? WO.default.createElement(
+            f,
+            null,
+            "Press ",
+            r.keyName,
+            " again to exit",
+          )
+        : WO.default.createElement(
+            pA,
+            null,
+            w &&
+              WO.default.createElement(YA, {
+                shortcut: "←",
+                action: "go back",
+              }),
+            WO.default.createElement(YA, {
+              shortcut: "Esc/Enter/Space",
+              action: "close",
+            }),
+            K.status === "running" &&
+              z &&
+              WO.default.createElement(YA, { shortcut: "k", action: "kill" }),
+          )),
+      (q[18] = w),
+      (q[19] = z),
+      (q[20] = K.status),
+      (q[21] = T));
+  else T = q[21];
   let y;
-  if (q[19] === Symbol.for("react.memo_cache_sentinel"))
-    ((y = Cz.default.createElement(Z, { bold: !0 }, "Status:")), (q[19] = y));
-  else y = q[19];
+  if (q[22] === Symbol.for("react.memo_cache_sentinel"))
+    ((k = WO.default.createElement(f, { bold: !0 }, "Status:")), (q[22] = k));
+  else k = q[22];
   let B;
-  if (q[20] !== K.result || q[21] !== K.status)
+  if (q[23] !== K.result || q[24] !== K.status)
     ((B = Cz.default.createElement(
       Z,
       null,
@@ -112,59 +129,53 @@
               K.result?.code !== void 0 && ` (exit code: ${K.result.code})`,
             ),
     )),
-      (q[20] = K.result),
-      (q[21] = K.status),
-      (q[22] = B));
-  else B = q[22];
-  let C;
-  if (q[23] === Symbol.for("react.memo_cache_sentinel"))
-    ((C = Cz.default.createElement(Z, { bold: !0 }, "Runtime:")), (q[23] = C));
-  else C = q[23];
-  let m = f(K.startTime),
-    u;
-  if (q[24] !== m)
-    ((u = Cz.default.createElement(Z, null, C, " ", m)),
-      (q[24] = m),
+      (q[23] = K.result),
+      (q[24] = K.status),
       (q[25] = u));
   else u = q[25];
   let U;
   if (q[26] === Symbol.for("react.memo_cache_sentinel"))
-    ((U = Cz.default.createElement(Z, { bold: !0 }, "Command:")), (q[26] = U));
+    ((u = WO.default.createElement(f, { bold: !0 }, "Runtime:")), (q[26] = u));
   else U = q[26];
-  let g;
+  let S = P(K.startTime),
+    m;
   if (q[27] !== T)
-    ((g = Cz.default.createElement(Z, { wrap: "wrap" }, U, " ", T)),
+    ((m = WO.default.createElement(f, null, u, " ", S)),
       (q[27] = T),
       (q[28] = g));
   else g = q[28];
   let x;
-  if (q[29] !== B || q[30] !== u || q[31] !== g)
-    ((x = Cz.default.createElement(
-      h,
-      { flexDirection: "column", marginTop: 1 },
-      B,
-      u,
-      g,
-    )),
-      (q[29] = B),
+  if (q[29] === Symbol.for("react.memo_cache_sentinel"))
+    ((b = WO.default.createElement(f, { bold: !0 }, "Command:")), (q[29] = b));
+  else b = q[29];
+  let U;
+  if (q[30] !== N)
+    ((U = WO.default.createElement(f, { wrap: "wrap" }, b, " ", N)),
       (q[30] = u),
-      (q[31] = g),
-      (q[32] = x));
-  else x = q[32];
+      (q[31] = U));
+  else U = q[31];
   let d;
-  if (q[33] === Symbol.for("react.memo_cache_sentinel"))
-    ((d = Cz.default.createElement(Z, { bold: !0 }, "Output:")), (q[33] = d));
-  else d = q[33];
+  if (q[32] !== y || q[33] !== m || q[34] !== U)
+    ((g = WO.default.createElement(I, { flexDirection: "column" }, y, m, U)),
+      (q[32] = y),
+      (q[33] = m),
+      (q[34] = U),
+      (q[35] = g));
+  else g = q[35];
   let r;
+  if (q[36] === Symbol.for("react.memo_cache_sentinel"))
+    ((x = WO.default.createElement(f, { bold: !0 }, "Output:")), (q[36] = x));
+  else x = q[36];
+  let p;
   if (
-    q[34] !== H ||
-    q[35] !== J.stdout ||
-    q[36] !== J.stdoutLines ||
-    q[37] !== K.id
+    q[37] !== H ||
+    q[38] !== J.stdout ||
+    q[39] !== J.stdoutLines ||
+    q[40] !== K.id
   )
     ((r = Cz.default.createElement(
       h,
-      { flexDirection: "column", marginTop: 1 },
+      { flexDirection: "column" },
       d,
       J.stdout
         ? Cz.default.createElement(
@@ -178,7 +189,7 @@
                 paddingX: 1,
                 flexDirection: "column",
                 height: 12,
-                maxWidth: H - 8,
+                maxWidth: H - 6,
               },
               J.stdout
                 .split(
@@ -198,95 +209,31 @@
           )
         : Cz.default.createElement(Z, { dimColor: !0 }, "No output available"),
     )),
-      (q[34] = H),
-      (q[35] = J.stdout),
-      (q[36] = J.stdoutLines),
-      (q[37] = K.id),
-      (q[38] = r));
-  else r = q[38];
-  let c;
-  if (q[39] !== x || q[40] !== r)
-    ((c = Cz.default.createElement(
-      h,
-      { width: "100%" },
-      Cz.default.createElement(
-        h,
-        {
-          borderStyle: "round",
-          borderColor: "background",
-          flexDirection: "column",
-          marginTop: 1,
-          paddingLeft: 1,
-          paddingRight: 1,
-          width: "100%",
-        },
-        k,
-        x,
-        r,
-      ),
-    )),
-      (q[39] = x),
-      (q[40] = r),
+      (q[37] = H),
+      (q[38] = J.stdout),
+      (q[39] = J.stdoutLines),
+      (q[40] = K.id),
       (q[41] = c));
   else c = q[41];
   let q1;
-  if (
-    q[42] !== G.keyName ||
-    q[43] !== G.pending ||
-    q[44] !== w ||
-    q[45] !== z ||
-    q[46] !== K.status
-  )
-    ((q1 = Cz.default.createElement(
-      h,
-      { marginLeft: 2 },
-      G.pending
-        ? Cz.default.createElement(
-            Z,
-            { dimColor: !0 },
-            "Press ",
-            G.keyName,
-            " again to exit",
-          )
-        : Cz.default.createElement(
-            Z,
-            { dimColor: !0 },
-            Cz.default.createElement(
-              nA,
-              null,
-              w &&
-                Cz.default.createElement(_A, {
-                  shortcut: "←",
-                  action: "go back",
-                }),
-              Cz.default.createElement(_A, {
-                shortcut: "Esc/Enter/Space",
-                action: "close",
-              }),
-              K.status === "running" &&
-                z &&
-                Cz.default.createElement(_A, { shortcut: "k", action: "kill" }),
-            ),
-          ),
-    )),
-      (q[42] = G.keyName),
-      (q[43] = G.pending),
-      (q[44] = w),
-      (q[45] = z),
-      (q[46] = K.status),
-      (q[47] = q1));
-  else q1 = q[47];
-  let H1;
-  if (q[48] !== c || q[49] !== q1)
+  if (q[42] !== j || q[43] !== g || q[44] !== p || q[45] !== T)
     ((H1 = Cz.default.createElement(
       h,
-      { width: "100%", flexDirection: "column" },
+      {
+        title: "Shell details",
+        onCancel: j,
+        color: "background",
+        borderDimColor: !1,
+        inputGuide: T,
+      },
       c,
       q1,
     )),
-      (q[48] = c),
-      (q[49] = q1),
-      (q[50] = H1));
-  else H1 = q[50];
+      (q[42] = j),
+      (q[43] = g),
+      (q[44] = p),
+      (q[45] = T),
+      (q[46] = n));
+  else n = q[46];
   return H1;
 }

@@@ variable 'z_' (was 'n_') — structural (57.1%)
--- pretty-v2.1.31.js:178426
+++ pretty-v2.1.32.js:178551
@@ -1,5 +1,6 @@
 var n_ = E(() => {
   Bk();
   vy1();
-  ((WD7 = o(XD7(), 1)), (NF5 = new Intl.Segmenter()), (DD7 = WD7.default()));
+  z$1();
+  ((Kj7 = a(tD7(), 1)), (eD7 = Kj7.default()));
 });

@@@ function 'Jjq' (was 'P0q') — structural (57.0%)
--- pretty-v2.1.31.js:548312
+++ pretty-v2.1.32.js:548628
@@ -1,5 +1,5 @@
 function P0q() {
-  let A = t(14),
+  let A = A1(16),
     q = T6(x2z);
   if (!q) return null;
   let K;
@@ -7,6 +7,7 @@
     ((K = WJ(q.identity.color)), (A[0] = q.identity.color), (A[1] = K));
   else K = A[1];
   let Y = K,
+    z = q.status === "running",
     z;
   if (A[2] === Symbol.for("react.memo_cache_sentinel"))
     ((z = hZ.createElement(Z, null, "Viewing ")), (A[2] = z));
@@ -23,37 +24,42 @@
       (A[4] = q.identity.agentName),
       (A[5] = w));
   else w = A[5];
-  let H;
-  if (A[6] === Symbol.for("react.memo_cache_sentinel"))
+  let O = z ? "shift+up" : "esc",
+    $;
+  if (A[6] !== O)
     ((H = hZ.createElement(
       Z,
       { dimColor: !0 },
       " · ",
-      hZ.createElement(_A, { shortcut: "shift+up", action: "return" }),
+      UZ.createElement(YA, { shortcut: O, action: "return" }),
     )),
-      (A[6] = H));
-  else H = A[6];
+      (A[6] = O),
+      (A[7] = $));
+  else $ = A[7];
   let O;
-  if (A[7] !== w)
-    ((O = hZ.createElement(h, null, z, w, H)), (A[7] = w), (A[8] = O));
-  else O = A[8];
+  if (A[8] !== H || A[9] !== $)
+    ((_ = UZ.createElement(I, null, w, H, $)),
+      (A[8] = H),
+      (A[9] = $),
+      (A[10] = _));
+  else _ = A[10];
   let $;
-  if (A[9] !== q.prompt)
+  if (A[11] !== q.prompt)
     (($ = hZ.createElement(Z, { dimColor: !0 }, q.prompt)),
-      (A[9] = q.prompt),
-      (A[10] = $));
-  else $ = A[10];
+      (A[11] = q.prompt),
+      (A[12] = J));
+  else J = A[12];
   let _;
-  if (A[11] !== O || A[12] !== $)
+  if (A[13] !== _ || A[14] !== J)
     ((_ = hZ.createElement(
       h,
       { flexDirection: "column", marginBottom: 1 },
       O,
       $,
     )),
-      (A[11] = O),
-      (A[12] = $),
-      (A[13] = _));
-  else _ = A[13];
+      (A[13] = _),
+      (A[14] = J),
+      (A[15] = X));
+  else X = A[15];
   return _;
 }

@@@ function 'tL4' (was 'qL4') — structural (56.8%)
--- pretty-v2.1.31.js:367919
+++ pretty-v2.1.32.js:367971
@@ -17,13 +17,13 @@
       );
     }
   let w = bk(q);
-  if (WD6(w))
-    try {
-      (JNA(w, { recursive: !0, force: !0 }),
-        I(`[TeammateTool] Cleaned up tasks directory: ${w}`));
-    } catch (H) {
-      I(
-        `[TeammateTool] Failed to clean up tasks directory ${w}: ${H instanceof Error ? H.message : String(H)}`,
-      );
-    }
+  try {
+    (UNA(H, { recursive: !0, force: !0 }),
+      h(`[TeammateTool] Cleaned up tasks directory: ${H}`),
+      T_1());
+  } catch (O) {
+    h(
+      `[TeammateTool] Failed to clean up tasks directory ${H}: ${O instanceof Error ? O.message : String(O)}`,
+    );
+  }
 }

@@@ function 'cKz' (was 'klY') — structural (56.2%)
--- pretty-v2.1.31.js:479445
+++ pretty-v2.1.32.js:568618
@@ -1,3 +1,3 @@
 function klY() {
-  return null;
+  return;
 }

@@@ function 'jZ' (was 'BV') — structural (56.2%)
--- pretty-v2.1.31.js:512405
+++ pretty-v2.1.32.js:512050
@@ -21,7 +21,34 @@
     D =
       H.map((j) => `/${j.userFacingName()}`).length > 0 && J.has(OJ)
         ? `- /<skill-name> (e.g., /commit) is shorthand for users to invoke a user-invocable skill. When executed, the skill gets expanded to a full prompt. Use the ${OJ} tool to execute them. IMPORTANT: Only use ${OJ} for skills listed in its user-invocable skills section - do not guess or use built-in CLI commands.`
-        : "";
+        : "",
+    j = [
+      yd("session_memory", () => a2q()),
+      Cd(
+        "auto_memory",
+        () => CjA(),
+        "MEMORY.md is read from disk each turn and can be edited by the model",
+      ),
+      Cd(
+        "ant_model_override",
+        () => s2q(),
+        "GrowthBook feature value can change via periodic refresh or auth change",
+      ),
+      yd("env_info", () => sbA(q, K)),
+      yd("language", () => t2q(_.language)),
+      Cd(
+        "output_style",
+        () => e2q(O),
+        "User can change output style mid-session via /output-style command",
+      ),
+      Cd(
+        "mcp_instructions",
+        () => Awq(Y),
+        "MCP servers connect/disconnect between turns",
+      ),
+      yd("scratchpad", () => zwq()),
+    ],
+    M = await cSA(j);
   return [
     H8z(O),
     O8z(O),
@@ -35,13 +62,6 @@
     j8z(J),
     M8z(),
     ...(r8("tengu_system_prompt_global_cache", !1) ? [MP1] : []),
-    Hzq(),
-    CDA(),
-    Ozq(),
-    $,
-    $zq(_.language),
-    _zq(O),
-    Jzq(Y),
-    Wzq(),
+    ...M,
   ].filter((j) => j !== null);
 }

@@@ function 'nmA' (was 'jmA') — structural (56.2%)
--- pretty-v2.1.31.js:550614
+++ pretty-v2.1.32.js:550956
@@ -1,5 +1,5 @@
 function jmA(A) {
-  let q = t(21),
+  let q = A1(22),
     { hostPattern: K, onUserResponse: Y } = A,
     { host: z } = K,
     w;
@@ -24,24 +24,33 @@
   let H = w,
     O;
   if (q[2] === Symbol.for("react.memo_cache_sentinel"))
-    ((O = { label: "Yes", value: "yes" }), (q[2] = O));
+    ((O = Ly1()), (q[2] = O));
   else O = q[2];
+  let $ = O,
+    _;
+  if (q[3] === Symbol.for("react.memo_cache_sentinel"))
+    ((_ = { label: "Yes", value: "yes" }), (q[3] = _));
+  else _ = q[3];
   let $;
-  if (q[3] !== z)
-    (($ = {
-      label: lw.createElement(
-        Z,
-        null,
-        "Yes, and don't ask again for ",
-        lw.createElement(Z, { bold: !0 }, z),
-      ),
-      value: "yes-dont-ask-again",
-    }),
-      (q[3] = z),
-      (q[4] = $));
-  else $ = q[4];
+  if (q[4] !== z)
+    ((J = !$
+      ? [
+          {
+            label: sw.createElement(
+              f,
+              null,
+              "Yes, and don't ask again for ",
+              sw.createElement(f, { bold: !0 }, z),
+            ),
+            value: "yes-dont-ask-again",
+          },
+        ]
+      : []),
+      (q[4] = z),
+      (q[5] = J));
+  else J = q[5];
   let _;
-  if (q[5] === Symbol.for("react.memo_cache_sentinel"))
+  if (q[6] === Symbol.for("react.memo_cache_sentinel"))
     ((_ = {
       label: lw.createElement(
         Z,
@@ -51,53 +60,53 @@
       ),
       value: "no",
     }),
-      (q[5] = _));
-  else _ = q[5];
+      (q[6] = X));
+  else X = q[6];
   let J;
-  if (q[6] !== $) ((J = [O, $, _]), (q[6] = $), (q[7] = J));
-  else J = q[7];
+  if (q[7] !== J) ((D = [_, ...J, X]), (q[7] = J), (q[8] = D));
+  else D = q[8];
   let X = J,
     D;
-  if (q[8] === Symbol.for("react.memo_cache_sentinel"))
-    ((D = lw.createElement(Z, { dimColor: !0 }, "Host:")), (q[8] = D));
-  else D = q[8];
+  if (q[9] === Symbol.for("react.memo_cache_sentinel"))
+    ((M = sw.createElement(f, { dimColor: !0 }, "Host:")), (q[9] = M));
+  else M = q[9];
   let j;
-  if (q[9] !== z)
+  if (q[10] !== z)
     ((j = lw.createElement(h, null, D, lw.createElement(Z, null, " ", z))),
-      (q[9] = z),
-      (q[10] = j));
-  else j = q[10];
+      (q[10] = z),
+      (q[11] = W));
+  else W = q[11];
   let M;
-  if (q[11] === Symbol.for("react.memo_cache_sentinel"))
+  if (q[12] === Symbol.for("react.memo_cache_sentinel"))
     ((M = lw.createElement(
       h,
       { marginTop: 1 },
       lw.createElement(Z, null, "Do you want to allow this connection?"),
     )),
-      (q[11] = M));
-  else M = q[11];
+      (q[12] = G));
+  else G = q[12];
   let W;
-  if (q[12] !== Y)
+  if (q[13] !== Y)
     ((W = () => {
       Y({ allow: !1, persistToSettings: !1 });
     }),
-      (q[12] = Y),
-      (q[13] = W));
-  else W = q[13];
+      (q[13] = Y),
+      (q[14] = P));
+  else P = q[14];
   let P;
-  if (q[14] !== H || q[15] !== X || q[16] !== W)
+  if (q[15] !== H || q[16] !== j || q[17] !== P)
     ((P = lw.createElement(
       h,
       null,
       lw.createElement(ZA, { options: X, onChange: H, onCancel: W }),
     )),
-      (q[14] = H),
       (q[15] = X),
       (q[16] = W),
-      (q[17] = P));
-  else P = q[17];
+      (q[17] = P),
+      (q[18] = V));
+  else V = q[18];
   let G;
-  if (q[18] !== P || q[19] !== j)
+  if (q[19] !== V || q[20] !== W)
     ((G = lw.createElement(
       xw,
       { title: "Network request outside of sandbox" },
@@ -109,9 +118,9 @@
         P,
       ),
     )),
-      (q[18] = P),
       (q[19] = j),
-      (q[20] = G));
-  else G = q[20];
+      (q[20] = W),
+      (q[21] = Z));
+  else Z = q[21];
   return G;
 }

@@@ function 'pL4' (was 'ik4') — structural (56.1%)
--- pretty-v2.1.31.js:367488
+++ pretty-v2.1.32.js:367657
@@ -4,14 +4,6 @@
       return `create team: ${A.team_name}`;
     case "cleanup":
       return `cleanup team: ${A.team_name || "current"}`;
-    case "discoverTeams":
-      return "discover available teams";
-    case "requestJoin":
-      return `request to join team: ${A.team_name}${A.proposed_name ? ` as '${A.proposed_name}'` : ""}`;
-    case "approveJoin":
-      return `approve join request: ${A.request_id}`;
-    case "rejectJoin":
-      return `reject join request: ${A.request_id}`;
     default:
       return "teammate operation";
   }

@@@ variable 'YT5' (was 'fV5') — structural (55.9%)
--- pretty-v2.1.31.js:147550
+++ pretty-v2.1.32.js:147514
@@ -1,9 +1,9 @@
   fV5 = () => {
     let A = H4() !== "firstParty";
     return {
-      value: j$().opus45,
-      label: "Opus 4.5",
-      description: `Opus 4.5 · Most capable for complex work${A ? "" : ` · ${Fi(PL1)}`}`,
-      descriptionForModel: "Opus 4.5 - most capable for complex work",
+      value: XH().opus46,
+      label: "Opus 4.6",
+      description: `Opus 4.6 · Most capable for complex work${A ? "" : ` · ${Nb(H$1)}`}`,
+      descriptionForModel: "Opus 4.6 - most capable for complex work",
     };
   },

@@@ function 'Ox4' (was 'eMY') — structural (55.7%)
--- pretty-v2.1.31.js:387884
+++ pretty-v2.1.32.js:387317
@@ -1,48 +1,59 @@
-function eMY(A, q) {
-  let K = WJ(A.color),
-    Y = tMY(A.teammateId),
-    z = Yj6(A.content, Y);
-  if (z) return p3.createElement(p3.Fragment, { key: q }, z);
-  if (qZ(A.content)) return null;
-  let w = wI4(A.content);
-  if (w) return p3.createElement(p3.Fragment, { key: q }, w);
-  let H = OI4(A.content);
-  if (H) return p3.createElement(p3.Fragment, { key: q }, H);
-  let O = _I4(A.content);
-  if (O) return p3.createElement(p3.Fragment, { key: q }, O);
-  let $ = null;
-  try {
-    $ = OA(A.content);
-  } catch {}
-  if ($?.type === "idle_notification") return null;
-  if ($?.type === "task_completed") {
-    let _ = $;
-    return p3.createElement(
-      h,
-      { key: q, flexDirection: "column", marginTop: 1 },
-      p3.createElement(Z, { color: K }, `@${Y}${d1.pointer}`),
-      p3.createElement(
-        jA,
-        null,
-        p3.createElement(Z, { color: "success" }, "✓"),
-        p3.createElement(
-          Z,
-          null,
-          " ",
-          "Completed task #",
-          _.taskId,
-          _.taskSubject &&
-            p3.createElement(Z, { dimColor: !0 }, " (", _.taskSubject, ")"),
-        ),
-      ),
-    );
-  }
-  if ($?.type === "teammate_terminated") return null;
-  return p3.createElement(AWY, {
-    key: q,
-    displayName: Y,
-    inkColor: K,
-    content: A.content,
-    summary: A.summary,
+function Ox4({ addMargin: A, param: { text: q }, isTranscriptMode: K }) {
+  let Y = qPY(q).filter((z) => {
+    if (XZ(z.content)) return !1;
+    try {
+      if (JA(z.content)?.type === "teammate_terminated") return !1;
+    } catch {}
+    return !0;
   });
+  if (Y.length === 0) return null;
+  return C5.createElement(
+    I,
+    { flexDirection: "column", marginTop: A ? 1 : 0, width: "100%" },
+    Y.map((z, w) => {
+      let H = CM(z.color),
+        O = KPY(z.teammateId),
+        $ = kj6(z.content, O);
+      if ($) return C5.createElement(C5.Fragment, { key: w }, $);
+      let _ = Kx4(z.content);
+      if (_) return C5.createElement(C5.Fragment, { key: w }, _);
+      let J = zx4(z.content);
+      if (J) return C5.createElement(C5.Fragment, { key: w }, J);
+      let X = null;
+      try {
+        X = JA(z.content);
+      } catch {}
+      if (X?.type === "idle_notification") return null;
+      if (X?.type === "task_completed") {
+        let D = X;
+        return C5.createElement(
+          I,
+          { key: w, flexDirection: "column", marginTop: 1 },
+          C5.createElement(f, { color: H }, `@${O}${n1.pointer}`),
+          C5.createElement(
+            HA,
+            null,
+            C5.createElement(f, { color: "success" }, "✓"),
+            C5.createElement(
+              f,
+              null,
+              " ",
+              "Completed task #",
+              D.taskId,
+              D.taskSubject &&
+                C5.createElement(f, { dimColor: !0 }, " (", D.taskSubject, ")"),
+            ),
+          ),
+        );
+      }
+      return C5.createElement(YPY, {
+        key: w,
+        displayName: O,
+        inkColor: H,
+        content: z.content,
+        summary: z.summary,
+        isTranscriptMode: K,
+      });
+    }),
+  );
 }

@@@ function 'UL4' (was 'dk4') — structural (55.6%)
--- pretty-v2.1.31.js:367165
+++ pretty-v2.1.32.js:367525
@@ -2,101 +2,46 @@
   return `
 # TeammateTool
 
-Manage teams and coordinate teammates in a swarm. Use this tool for team operations, communication, and task assignment. Note: To spawn new teammates, use the Task tool with \`team_name\` and \`name\` parameters.
+Manage teams and coordinate agents on your team. Use this tool to create and clean up teams. To spawn new teammates, use the Task tool with \`team_name\` and \`name\` parameters.
 
 ## Operations
 
 ### spawnTeam - Create a Team
 
-Create a new team to coordinate multiple agents working on a project. Teams have a 1:1 correspondence with task lists (Team = Project = TaskList).
-
-\`\`\`
-{
-  "operation": "spawnTeam",
-  "team_name": "my-project",
-  "description": "Working on feature X"
-}
-\`\`\`
-
-This creates:
-- A team file at \`~/.claude/teams/{team-name}.json\`
-- A corresponding task list directory at \`~/.claude/tasks/{team-name}/\`
-
-### discoverTeams - Discover Available Teams
+## When to Use
 
-List teams that are available to join. Returns teams from \`~/.claude/teams/\` that you are not already a member of.
+Use this tool proactively whenever:
+- The user explicitly asks to use a team, swarm, or group of agents
+- The user mentions wanting agents to work together, coordinate, or collaborate
+- A task is complex enough that it would benefit from parallel work by multiple agents (e.g., building a full-stack feature with frontend and backend work, refactoring a codebase while keeping tests passing, implementing a multi-step project with research, planning, and coding phases)
 
-\`\`\`
-{
-  "operation": "discoverTeams"
-}
-\`\`\`
+When in doubt about whether a task warrants a team, prefer spawning a team.
 
-Returns a list of teams with:
-- **name**: Team name
-- **description**: Team description (if set)
-- **leadAgentId**: ID of the team leader
-- **memberCount**: Current number of team members
+## Choosing Agent Types for Teammates
 
-Use this to find teams you can request to join with \`requestJoin\`.
+When spawning teammates via the Task tool, choose the \`subagent_type\` based on what tools the agent needs for its task. Each agent type has a different set of available tools — match the agent to the work:
 
-### requestJoin - Request to Join a Team
+- **Read-only agents** (e.g., Explore, Plan) cannot edit or write files. Only assign them research, search, or planning tasks. Never assign them implementation work.
+- **Full-capability agents** (e.g., general-purpose) have access to all tools including file editing, writing, and bash. Use these for tasks that require making changes.
+- **Custom agents** defined in \`.claude/agents/\` may have their own tool restrictions. Check their descriptions to understand what they can and cannot do.
 
-Send a join request to a team's leader. The leader will receive a \`join_request\` message and can approve or reject it.
+Always review the agent type descriptions and their available tools listed in the Task tool prompt before selecting a \`subagent_type\` for a teammate.
 
-- **team_name**: Name of the team to join (REQUIRED)
-- **proposed_name**: (Optional) Your proposed name for the team (defaults to generated slug)
-- **capabilities**: (Optional) Description of what you can help with
+Create a new team to coordinate multiple agents working on a project. Teams have a 1:1 correspondence with task lists (Team = TaskList).
 
 \`\`\`
 {
-  "operation": "requestJoin",
+  "operation": "spawnTeam",
   "team_name": "my-project",
-  "proposed_name": "helper",
-  "capabilities": "I can help with code review and testing"
+  "description": "Working on feature X"
 }
 \`\`\`
 
-After sending the request, you will receive either a \`join_approved\` or \`join_rejected\` message in response.
-
-### approveJoin - Approve a Join Request (Leader Only)
-
-When an agent requests to join your team, they send a join request as a JSON message with \`type: "join_request"\`. Use \`approveJoin\` to accept them:
-- **target_agent_id**: Use the \`proposedName\` field from the join_request message (REQUIRED)
-- **request_id**: Use the \`requestId\` field from the join_request message (REQUIRED)
-
-Example: If you receive a message like \`{"type":"join_request","proposedName":"helper","requestId":"join-123",...}\`, use:
-\`\`\`
-{
-  "operation": "approveJoin",
-  "target_agent_id": "helper",
-  "request_id": "join-123"
-}
-\`\`\`
+This creates a team file and a corresponding task list directory.
 
-The agent will be added to your team and notified of approval. They will receive their assigned agent ID, name, and color.
-
-### rejectJoin - Reject a Join Request (Leader Only)
-
-Use \`rejectJoin\` to decline a join request:
-- **target_agent_id**: Use the \`proposedName\` field from the join_request message (REQUIRED)
-- **request_id**: Use the \`requestId\` field from the join_request message (REQUIRED)
-- **reason**: (Optional) Explanation of why the request was rejected
-
-\`\`\`
-{
-  "operation": "rejectJoin",
-  "target_agent_id": "helper",
-  "request_id": "join-123",
-  "reason": "Team is at capacity"
-}
-\`\`\`
-
-The agent will be notified of the rejection with your reason.
-
 ### cleanup - Clean Up Team Resources
 
-Remove team and task directories when the swarm work is complete:
+Remove team and task directories when work is complete:
 
 \`\`\`
 {
@@ -105,14 +50,11 @@
 \`\`\`
 
 This operation:
-- Removes the team directory (\`~/.claude/teams/{team-name}/\`)
-- Removes the task directory (\`~/.claude/tasks/{team-name}/\`)
+- Removes the team and task directories
 - Clears team context from the current session
 
 **IMPORTANT**: \`cleanup\` will fail if the team still has active members. Gracefully terminate teammates first, then call \`cleanup\` after all teammates have shut down.
 
-Use this when all teammates have finished their work and you want to clean up the team resources. The team name is automatically determined from the \`CLAUDE_CODE_TEAM_NAME\` environment variable.
-
 ## Team Workflow
 
 1. **Create a team** with \`spawnTeam\` - this creates both the team and its task list
@@ -120,7 +62,8 @@
 3. **Spawn teammates** using the Task tool with \`team_name\` and \`name\` parameters to create teammates that join the team
 4. **Assign tasks** using TaskUpdate with \`owner\` to give tasks to idle teammates
 5. **Teammates work on assigned tasks** and mark them completed via TaskUpdate
-6. **Teammates go idle between turns** - after each turn, teammates automatically go idle and send a notification. This is normal—idle teammates can still receive messages and will wake up to process them
+6. **Teammates go idle between turns** - after each turn, teammates automatically go idle and send a notification. IMPORTANT: Be patient with idle teammates! Don't comment on their idleness until it actually impacts your work.
+7. **Shutdown your team** - when the task is completed, gracefully shut down your teammates via SendMessage with type: "shutdown_request".
 
 ## Task Ownership
 
@@ -135,8 +78,6 @@
 - These messages appear automatically as new conversation turns (like user messages)
 - If you're busy (mid-turn), messages are queued and delivered when your turn ends
 - The UI shows a brief notification with the sender's name when messages are waiting
-
-Messages will be delivered automatically.
 
 When reporting on teammate messages, you do NOT need to quote the original message—it's already rendered to the user.
 
@@ -147,18 +88,8 @@
 - **Idle teammates can receive messages.** Sending a message to an idle teammate wakes them up and they will process it normally.
 - **Idle notifications are automatic.** The system sends an idle notification whenever a teammate's turn ends. You do not need to react to idle notifications unless you want to assign new work or send a follow-up message.
 - **Do not treat idle as an error.** A teammate sending a message and then going idle is the normal flow—they sent their message and are now waiting for a response.
-
-## Environment Variables
-
-Spawned teammates have these environment variables set:
-- \`CLAUDE_CODE_AGENT_ID\`: Unique identifier for this agent
-- \`CLAUDE_CODE_AGENT_TYPE\`: Role/type of the agent (if specified)
-- \`CLAUDE_CODE_TEAM_NAME\`: Name of the team this agent belongs to
-- \`CLAUDE_CODE_PLAN_MODE_REQUIRED\`: Set to "true" if the teammate must enter plan mode before implementing changes
+- **Peer DM visibility.** When a teammate sends a DM to another teammate, a brief summary is included in their idle notification. This gives you visibility into peer collaboration without the full message content. You do not need to respond to these summaries — they are informational.
 
-**IMPORTANT for teammates:** Use your \`CLAUDE_CODE_AGENT_ID\` environment variable when:
-- Adding comments to tasks (as the \`author\` field)
-- Sending messages to other teammates
 ## Discovering Team Members
 
 Teammates can read the team config file to discover other team members:
@@ -169,7 +100,7 @@
 - \`agentId\`: Unique identifier (for reference only - do not use for communication)
 - \`agentType\`: Role/type of the agent
 
-**IMPORTANT**: Always refer to teammates by their NAME (e.g., "team-lead", "researcher", "tester"), never by UUID. Names are used for:
+**IMPORTANT**: Always refer to teammates by their NAME (e.g., "team-lead", "researcher", "tester"). Names are used for:
 - \`target_agent_id\` when sending messages
 - Identifying task owners
 
@@ -180,12 +111,7 @@
 
 ## Task List Coordination
 
-Teams share a task list that all teammates can access:
-- **Task list location**: \`~/.claude/tasks/{team-name}/\`
-
-**IMPORTANT notes for communication with your team**:
-- Do not use terminal tools to view your team's activity, always send a message to your teammates (and remember, refer to them by name).
-- Your team cannot hear you if you do not use the teammate send message tool. Always send a message to your teammates if you are responding to them.
+Teams share a task list that all teammates can access at \`~/.claude/tasks/{team-name}/\`.
 
 Teammates should:
 1. Check TaskList periodically, **especially after completing each task**, to find available work or see newly unblocked tasks
@@ -195,6 +121,12 @@
 5. Coordinate with other teammates by reading the task list status
 6. If all available tasks are blocked, notify the team lead or help resolve blocking tasks
 
-**IMPORTANT**: Do NOT send structured JSON status messages like \`{"type":"idle",...}\` or \`{"type":"task_completed",...}\`. Use TaskUpdate to mark tasks completed and the system will automatically send idle notifications when you stop. Just communicate in plain text when you need to message teammates.
+**IMPORTANT notes for communication with your team**:
+- Do not use terminal tools to view your team's activity; always send a message to your teammates (and remember, refer to them by name).
+- Your team cannot hear you if you do not use the SendMessage tool. Always send a message to your teammates if you are responding to them.
+- Do NOT send structured JSON status messages like \`{"type":"idle",...}\` or \`{"type":"task_completed",...}\`. Just communicate in plain text when you need to message teammates.
+- Use TaskUpdate to mark tasks completed.
+- If you are an agent in the team, the system will automatically send idle notifications to the team lead when you stop. 
+
 `.trim();
 }

@@@ function 'Nd4' (was 'Cp4') — structural (55.6%)
--- pretty-v2.1.31.js:420693
+++ pretty-v2.1.32.js:420254
@@ -2,7 +2,7 @@
   return `
 # SendMessageTool
 
-Send messages to teammates and handle protocol requests/responses in a swarm.
+Send messages to agent teammates and handle protocol requests/responses in a team.
 
 ## Message Types

@@@ function 'St' (was 'ft') — structural (55.6%)
--- pretty-v2.1.31.js:459643
+++ pretty-v2.1.32.js:459516
@@ -1,3 +1,3 @@
 function ft() {
-  return r8("tengu_workout", !1);
+  return x8("tengu_workout2", !1);
 }

@@@ function 'IDq' (was 'gXq') — structural (55.2%)
--- pretty-v2.1.31.js:546840
+++ pretty-v2.1.32.js:547220
@@ -1,13 +1,7 @@
 async function gXq(A) {
   if (!U8() || !_m1()) return null;
-  let {
-      ctx: q,
-      description: K,
-      pendingClassifierCheck: Y,
-      updatedInput: z,
-      suggestions: w,
-    } = A,
-    H = await q.tryClassifier(Y, z);
+  let { ctx: q, description: K, updatedInput: Y, suggestions: z } = A,
+    w = null;
   if (H) return H;
   try {
     let O = () =>
@@ -27,20 +21,20 @@
       (C06({
         requestId: D.id,
         toolUseId: q.toolUseID,
-        async onAllow(j, M, W) {
+        async onAllow(D, j, M, W) {
           if (!X()) return;
           O();
           let P = j && Object.keys(j).length > 0 ? j : q.input;
-          J(await q.handleUserAllow(P, M, W));
+          _(await q.handleUserAllow(G, j, M, void 0, W));
         },
-        onReject(j) {
+        onReject(D, j) {
           if (!X()) return;
           (O(),
             q.logDecision({
               decision: "reject",
               source: { type: "user_reject", hasFeedback: !!j },
             }),
-            J(q.cancelAndAbort(j)));
+            _(q.cancelAndAbort(D, void 0, j)));
         },
       }),
         L06(D),

@@@ function 'vm6' (was 'tB6') — structural (55.1%)
--- pretty-v2.1.31.js:78254
+++ pretty-v2.1.32.js:78125
@@ -5,6 +5,8 @@
   displayName: Y,
   hasExtraUsageEnabled: z,
   billingType: w,
+  accountCreatedAt: H,
+  subscriptionCreatedAt: O,
 }) {
   let H = {
     accountUuid: A,
@@ -12,6 +14,8 @@
     organizationUuid: K,
     hasExtraUsageEnabled: z,
     billingType: w,
+    accountCreatedAt: H,
+    subscriptionCreatedAt: O,
   };
   if (Y) H.displayName = Y;
   XA((O) => {
@@ -20,7 +24,10 @@
       O.oauthAccount?.emailAddress === H.emailAddress &&
       O.oauthAccount?.organizationUuid === H.organizationUuid &&
       O.oauthAccount?.displayName === H.displayName &&
-      O.oauthAccount?.hasExtraUsageEnabled === H.hasExtraUsageEnabled
+      _.oauthAccount?.hasExtraUsageEnabled === $.hasExtraUsageEnabled &&
+      _.oauthAccount?.billingType === $.billingType &&
+      _.oauthAccount?.accountCreatedAt === $.accountCreatedAt &&
+      _.oauthAccount?.subscriptionCreatedAt === $.subscriptionCreatedAt
     )
       return O;
     return { ...O, oauthAccount: H };

@@@ function 'Dg5' (was 'EF5') — structural (55.0%)
--- pretty-v2.1.31.js:178398
+++ pretty-v2.1.32.js:178520
@@ -1,8 +1,9 @@
 function EF5(A) {
-  if (!A.includes("‍")) return !1;
-  for (let q = 1; q < A.length; q++)
-    if (A.charCodeAt(q) === 8205) {
-      let K = A.charCodeAt(q - 1);
+  let q = 0;
+  for (let K = 0; K < A.length; K++) {
+    let Y = A.charCodeAt(K);
+    if (Y === 3634 || Y === 3635 || Y === 3762 || Y === 3763) return !0;
+    if (Y === 8205) {
       if (
         K === 2381 ||
         K === 2509 ||
@@ -16,5 +17,7 @@
       )
         return !0;
     }
+    q = Y;
+  }
   return !1;
 }

@@@ variable 'O6z' (was 'p3q') — structural (54.8%)
--- pretty-v2.1.31.js:497371
+++ pretty-v2.1.32.js:496974
@@ -1,23 +1,6 @@
-var p3q = E(() => {
-  g3q();
-  N0();
-  g6();
-  ((OxA = o(J1(), 1)),
-    (rtY = {
-      type: "local-jsx",
-      name: "hooks",
-      description: "Manage hook configurations for tool events",
-      isEnabled: () => !0,
-      isHidden: !1,
-      async call(A, q) {
-        n("tengu_hooks_command", {});
-        let Y = (await q.getAppState()).toolPermissionContext,
-          z = hX(Y).map((w) => w.name);
-        return OxA.createElement(Q3q, { toolNames: z, onExit: A });
-      },
-      userFacingName() {
-        return "hooks";
-      },
-    }),
-    (U3q = rtY));
-});
+  O6z = async (A, q) => {
+    c("tengu_hooks_command", {});
+    let Y = (await q.getAppState()).toolPermissionContext,
+      z = LX(Y).map((w) => w.name);
+    return QxA.createElement(V9q, { toolNames: z, onExit: A });
+  };

@@@ function 'ZA' — structural (54.8%)
--- pretty-v2.1.31.js:195060
+++ pretty-v2.1.32.js:252187
@@ -1,5 +1,5 @@
 function ZA(A) {
-  let q = t(63),
+  let q = A1(72),
     {
       isDisabled: K,
       hideIndexes: Y,
@@ -18,6 +18,9 @@
       onDownFromLastItem: P,
       onInputModeToggle: G,
       onOpenEditor: f,
+      onImagePaste: Z,
+      pastedContents: N,
+      onRemoveImage: T,
     } = A,
     V = K === void 0 ? !1 : K,
     N = Y === void 0 ? !1 : Y,
@@ -25,6 +28,8 @@
     k = D === void 0 ? "compact" : D,
     y = j === void 0 ? !1 : j,
     B = M === void 0 ? !1 : M,
+    [U, g] = m4.useState(!1),
+    [x, p] = m4.useState(0),
     C;
   if (q[0] !== H)
     ((C = () => {
@@ -101,15 +106,29 @@
   let c = rZ7(r),
     q1 = y || (N ? "numeric" : !1),
     H1;
+  if (q[15] !== N)
+    ((w1 = () => {
+      if (N && Object.values(N).some(kf9)) {
+        let o = Object.values(N).filter(Ef9).length;
+        return (g(!0), p(o - 1), !0);
+      }
+      return !1;
+    }),
+      (q[15] = N),
+      (q[16] = w1));
+  else w1 = q[16];
+  let V1;
   if (
-    q[15] !== m ||
-    q[16] !== V ||
     q[17] !== P ||
     q[18] !== G ||
     q[19] !== W ||
     q[20] !== H ||
     q[21] !== c ||
-    q[22] !== q1
+    q[22] !== W ||
+    q[23] !== H ||
+    q[24] !== e ||
+    q[25] !== G1 ||
+    q[26] !== w1
   )
     ((H1 = {
       isDisabled: V,
@@ -121,47 +140,56 @@
       onDownFromLastItem: P,
       onInputModeToggle: G,
       inputValues: m,
+      imagesSelected: U,
+      onEnterImageSelection: w1,
     }),
-      (q[15] = m),
-      (q[16] = V),
       (q[17] = P),
       (q[18] = G),
       (q[19] = W),
       (q[20] = H),
       (q[21] = c),
       (q[22] = q1),
-      (q[23] = H1));
-  else H1 = q[23];
+      (q[23] = H),
+      (q[24] = e),
+      (q[25] = G1),
+      (q[26] = w1),
+      (q[27] = V1));
+  else V1 = q[27];
   qf7(H1);
   let $1, A1, O1, s;
   if (
-    q[24] !== N ||
-    q[25] !== w ||
-    q[26] !== B ||
-    q[27] !== m ||
     q[28] !== V ||
     q[29] !== k ||
     q[30] !== $ ||
     q[31] !== _ ||
     q[32] !== f ||
-    q[33] !== H.length ||
-    q[34] !== c.focusedValue ||
-    q[35] !== c.options ||
-    q[36] !== c.value ||
-    q[37] !== c.visibleFromIndex ||
-    q[38] !== c.visibleOptions ||
-    q[39] !== c.visibleToIndex
+    q[33] !== k ||
+    q[34] !== S ||
+    q[35] !== $ ||
+    q[36] !== _ ||
+    q[37] !== Z ||
+    q[38] !== V ||
+    q[39] !== T ||
+    q[40] !== H.length ||
+    q[41] !== N ||
+    q[42] !== x ||
+    q[43] !== e.focusedValue ||
+    q[44] !== e.options ||
+    q[45] !== e.value ||
+    q[46] !== e.visibleFromIndex ||
+    q[47] !== e.visibleOptions ||
+    q[48] !== e.visibleToIndex
   ) {
     s = Symbol.for("react.early_return_sentinel");
     A: {
       let Z1 = { container: ll5, highlightedText: cl5 };
       if (k === "expanded") {
         let X1;
-        if (q[44] !== c.options.length)
+        if (q[53] !== e.options.length)
           ((X1 = c.options.length.toString()),
-            (q[44] = c.options.length),
-            (q[45] = X1));
-        else X1 = q[45];
+            (q[53] = e.options.length),
+            (q[54] = X1));
+        else X1 = q[54];
         let _1 = X1.length;
         s = I4.default.createElement(
           h,
@@ -175,7 +203,9 @@
               S1 = !V && c.focusedValue === a.value,
               E1 = c.value === a.value;
             if (a.type === "input") {
-              let R6 = m.has(a.value) ? m.get(a.value) : a.initialValue || "";
+              let P6 = r.has(v1.value)
+                ? r.get(v1.value)
+                : v1.initialValue || "";
               return I4.default.createElement(s_1, {
                 key: String(a.value),
                 option: a,
@@ -193,7 +223,9 @@
                   });
                 },
                 onSubmit: (K6) => {
-                  if (K6.trim() || a.allowEmptySubmitToCancel) _?.(a.value);
+                  let W1 = N && Object.values(N).some(Nf9);
+                  if (U6.trim() || W1 || v1.allowEmptySubmitToCancel)
+                    _?.(v1.value);
                   else $?.();
                 },
                 onExit: $,
@@ -201,6 +233,13 @@
                 showLabel: B,
                 onOpenEditor: f,
                 resetCursorOnUpdate: a.resetCursorOnUpdate,
+                onImagePaste: Z,
+                pastedContents: N,
+                onRemoveImage: T,
+                imagesSelected: U,
+                selectedImageIndex: x,
+                onImagesSelectedChange: g,
+                onSelectedImageIndexChange: p,
               });
             }
             let U1 = a.label;
@@ -248,12 +287,12 @@
       }
       if (k === "compact-vertical") {
         let X1;
-        if (q[46] !== N || q[47] !== c.options)
+        if (q[55] !== y || q[56] !== e.options)
           ((X1 = N ? 0 : c.options.length.toString().length),
-            (q[46] = N),
-            (q[47] = c.options),
-            (q[48] = X1));
-        else X1 = q[48];
+            (q[55] = y),
+            (q[56] = e.options),
+            (q[57] = X1));
+        else X1 = q[57];
         let _1 = X1;
         s = I4.default.createElement(
           h,
@@ -267,7 +306,9 @@
               S1 = !V && c.focusedValue === a.value,
               E1 = c.value === a.value;
             if (a.type === "input") {
-              let E6 = m.has(a.value) ? m.get(a.value) : a.initialValue || "";
+              let G6 = r.has(v1.value)
+                ? r.get(v1.value)
+                : v1.initialValue || "";
               return I4.default.createElement(s_1, {
                 key: String(a.value),
                 option: a,
@@ -285,7 +326,9 @@
                   });
                 },
                 onSubmit: (R6) => {
-                  if (R6.trim() || a.allowEmptySubmitToCancel) _?.(a.value);
+                  let U6 = N && Object.values(N).some(Vf9);
+                  if (P6.trim() || U6 || v1.allowEmptySubmitToCancel)
+                    _?.(v1.value);
                   else $?.();
                 },
                 onExit: $,
@@ -293,6 +336,13 @@
                 showLabel: B,
                 onOpenEditor: f,
                 resetCursorOnUpdate: a.resetCursorOnUpdate,
+                onImagePaste: Z,
+                pastedContents: N,
+                onRemoveImage: T,
+                imagesSelected: U,
+                selectedImageIndex: x,
+                onImagesSelectedChange: g,
+                onSelectedImageIndexChange: p,
               });
             }
             let U1 = a.label;
@@ -369,12 +419,12 @@
         break A;
       }
       let j1;
-      if (q[49] !== N || q[50] !== c.options)
+      if (q[58] !== y || q[59] !== e.options)
         ((j1 = N ? 0 : c.options.length.toString().length),
-          (q[49] = N),
-          (q[50] = c.options),
-          (q[51] = j1));
-      else j1 = q[51];
+          (q[58] = y),
+          (q[59] = e.options),
+          (q[60] = _1));
+      else _1 = q[60];
       let L1 = j1,
         v1 = c.visibleOptions.some(dl5),
         Y1 = !B && !v1 && c.visibleOptions.some(pl5),
@@ -412,7 +462,7 @@
         });
       if (Y1) {
         let X1;
-        if (q[52] !== N || q[53] !== L1)
+        if (q[61] !== y || q[62] !== O1)
           ((X1 = (D1) => {
             if (D1.option.type === "input") return 0;
             let G1 = eK6(D1.option.label),
@@ -420,13 +470,13 @@
               R1 = D1.isSelected ? 2 : 0;
             return 2 + N1 + j7(G1) + R1;
           }),
-            (q[52] = N),
-            (q[53] = L1),
-            (q[54] = X1));
-        else X1 = q[54];
+            (q[61] = y),
+            (q[62] = O1),
+            (q[63] = X1));
+        else X1 = q[63];
         let _1 = Math.max(...K1.map(X1)),
           a;
-        if (q[55] !== N || q[56] !== L1 || q[57] !== _1)
+        if (q[64] !== y || q[65] !== O1 || q[66] !== S1)
           ((a = (D1) => {
             if (D1.option.type === "input") return null;
             let G1 = eK6(D1.option.label),
@@ -515,11 +565,11 @@
               ),
             );
           }),
-            (q[55] = N),
-            (q[56] = L1),
-            (q[57] = _1),
-            (q[58] = a));
-        else a = q[58];
+            (q[64] = y),
+            (q[65] = O1),
+            (q[66] = S1),
+            (q[67] = v1));
+        else v1 = q[67];
         s = I4.default.createElement(h, { ...Z1.container() }, K1.map(a));
         break A;
       }
@@ -552,7 +602,9 @@
                 });
               },
               onSubmit: (O6) => {
-                if (O6.trim() || X1.allowEmptySubmitToCancel) _?.(X1.value);
+                let q6 = N && Object.values(N).some(Pf9);
+                if (O6.trim() || q6 || X1.allowEmptySubmitToCancel)
+                  _?.(X1.value);
                 else $?.();
               },
               onExit: $,
@@ -560,6 +612,13 @@
               showLabel: B,
               onOpenEditor: f,
               resetCursorOnUpdate: X1.resetCursorOnUpdate,
+              onImagePaste: Z,
+              pastedContents: N,
+              onRemoveImage: T,
+              imagesSelected: U,
+              selectedImageIndex: x,
+              onImagesSelectedChange: g,
+              onSelectedImageIndexChange: p,
             });
           }
           let a = X1.label;
@@ -647,35 +706,40 @@
           );
         })));
     }
-    ((q[24] = N),
-      (q[25] = w),
-      (q[26] = B),
-      (q[27] = m),
-      (q[28] = V),
+    ((q[28] = y),
       (q[29] = k),
       (q[30] = $),
       (q[31] = _),
       (q[32] = f),
-      (q[33] = H.length),
-      (q[34] = c.focusedValue),
-      (q[35] = c.options),
-      (q[36] = c.value),
-      (q[37] = c.visibleFromIndex),
-      (q[38] = c.visibleOptions),
-      (q[39] = c.visibleToIndex),
-      (q[40] = $1),
+      (q[33] = k),
+      (q[34] = S),
+      (q[35] = $),
+      (q[36] = _),
+      (q[37] = Z),
+      (q[38] = V),
+      (q[39] = T),
+      (q[40] = H.length),
       (q[41] = A1),
       (q[42] = O1),
-      (q[43] = s));
-  } else (($1 = q[40]), (A1 = q[41]), (O1 = q[42]), (s = q[43]));
+      (q[43] = e.focusedValue),
+      (q[44] = e.options),
+      (q[45] = e.value),
+      (q[46] = e.visibleFromIndex),
+      (q[47] = e.visibleOptions),
+      (q[48] = e.visibleToIndex),
+      (q[49] = E1),
+      (q[50] = q1),
+      (q[51] = s),
+      (q[52] = j1));
+  } else ((E1 = q[49]), (q1 = q[50]), (s = q[51]), (j1 = q[52]));
   if (s !== Symbol.for("react.early_return_sentinel")) return s;
   let w1;
-  if (q[59] !== $1 || q[60] !== A1 || q[61] !== O1)
+  if (q[68] !== E1 || q[69] !== q1 || q[70] !== s)
     ((w1 = I4.default.createElement($1, { ...A1 }, O1)),
-      (q[59] = $1),
-      (q[60] = A1),
-      (q[61] = O1),
-      (q[62] = w1));
-  else w1 = q[62];
+      (q[68] = E1),
+      (q[69] = q1),
+      (q[70] = s),
+      (q[71] = J1));
+  else J1 = q[71];
   return w1;
 }

@@@ function 'DOz' (was 'gx1') — structural (54.5%)
--- pretty-v2.1.31.js:271082
+++ pretty-v2.1.32.js:549789
@@ -1,3 +1,3 @@
 function gx1(A) {
-  return A.startsWith(yJA());
+  return A.uuid;
 }

@@@ function 'XPY' (was 'JWY') — structural (54.3%)
--- pretty-v2.1.31.js:388992
+++ pretty-v2.1.32.js:388350
@@ -1,55 +1,61 @@
 function JWY(A) {
-  let q = t(16),
-    { displayName: K, inkColor: Y, content: z, summary: w } = A,
-    { columns: H } = A8(),
-    O = H - 2,
+  let q = A1(14),
+    {
+      displayName: K,
+      inkColor: Y,
+      content: z,
+      summary: w,
+      isTranscriptMode: H,
+    } = A,
+    O = `@${K}${n1.pointer}`,
     $;
   if (q[0] !== z || q[1] !== O)
-    (($ = ZJ1(z, O)), (q[0] = z), (q[1] = O), (q[2] = $));
+    (($ = v4.default.createElement(f, { color: Y }, O)),
+      (q[0] = Y),
+      (q[1] = O),
+      (q[2] = $));
   else $ = q[2];
-  let _ = $,
-    J = `@${K}${d1.pointer}`,
-    X;
-  if (q[3] !== Y || q[4] !== J)
-    ((X = $4.default.createElement(Z, { color: Y }, J)),
+  let _;
+  if (q[3] !== w)
+    ((_ = w && v4.default.createElement(f, null, " ", w)),
       (q[3] = Y),
-      (q[4] = J),
-      (q[5] = X));
-  else X = q[5];
+      (q[4] = _));
+  else _ = q[4];
   let D;
-  if (q[6] !== w)
-    ((D = w && $4.default.createElement(Z, null, " ", w)),
+  if (q[5] !== $ || q[6] !== _)
+    ((J = v4.default.createElement(I, null, $, _)),
+      (q[5] = $),
       (q[6] = w),
       (q[7] = D));
   else D = q[7];
   let j;
   if (q[8] !== X || q[9] !== D)
-    ((j = $4.default.createElement(h, null, X, D)),
+    ((X =
+      H &&
+      v4.default.createElement(
+        I,
+        { paddingLeft: 2 },
+        v4.default.createElement(
+          f,
+          null,
+          v4.default.createElement(R3, null, z),
+        ),
+      )),
       (q[8] = X),
       (q[9] = D),
       (q[10] = j));
   else j = q[10];
   let M;
-  if (q[11] !== _)
-    ((M = $4.default.createElement(
-      h,
-      { paddingLeft: 2 },
-      $4.default.createElement(Z, null, $4.default.createElement(L3, null, _)),
-    )),
-      (q[11] = _),
-      (q[12] = M));
-  else M = q[12];
-  let W;
-  if (q[13] !== j || q[14] !== M)
+  if (q[11] !== J || q[12] !== X)
     ((W = $4.default.createElement(
       h,
       { flexDirection: "column", marginTop: 1 },
       j,
       M,
     )),
-      (q[13] = j),
-      (q[14] = M),
-      (q[15] = W));
-  else W = q[15];
+      (q[11] = J),
+      (q[12] = X),
+      (q[13] = D));
+  else D = q[13];
   return W;
 }

@@@ function 'YPY' (was 'AWY') — structural (54.2%)
--- pretty-v2.1.31.js:387932
+++ pretty-v2.1.32.js:387376
@@ -1,48 +1,47 @@
 function AWY(A) {
-  let q = t(16),
-    { displayName: K, inkColor: Y, content: z, summary: w } = A,
-    { columns: H } = A8(),
-    O = H - 2,
+  let q = A1(14),
+    {
+      displayName: K,
+      inkColor: Y,
+      content: z,
+      summary: w,
+      isTranscriptMode: H,
+    } = A,
+    O = `@${K}${n1.pointer}`,
     $;
   if (q[0] !== z || q[1] !== O)
-    (($ = ZJ1(z, O)), (q[0] = z), (q[1] = O), (q[2] = $));
+    (($ = C5.createElement(f, { color: Y }, O)),
+      (q[0] = Y),
+      (q[1] = O),
+      (q[2] = $));
   else $ = q[2];
-  let _ = $,
-    J = `@${K}${d1.pointer}`,
-    X;
-  if (q[3] !== Y || q[4] !== J)
-    ((X = p3.createElement(Z, { color: Y }, J)),
-      (q[3] = Y),
-      (q[4] = J),
-      (q[5] = X));
-  else X = q[5];
   let D;
-  if (q[6] !== w)
-    ((D = w && p3.createElement(Z, null, " ", w)), (q[6] = w), (q[7] = D));
+  if (q[3] !== w)
+    ((_ = w && C5.createElement(f, null, " ", w)), (q[3] = w), (q[4] = _));
+  else _ = q[4];
+  let J;
+  if (q[5] !== $ || q[6] !== _)
+    ((J = C5.createElement(I, null, $, _)), (q[5] = $), (q[6] = _), (q[7] = J));
   else D = q[7];
   let j;
   if (q[8] !== X || q[9] !== D)
-    ((j = p3.createElement(h, null, X, D)),
+    ((X =
+      H &&
+      C5.createElement(
+        I,
+        { paddingLeft: 2 },
+        C5.createElement(f, null, C5.createElement(R3, null, z)),
+      )),
       (q[8] = X),
       (q[9] = D),
       (q[10] = j));
   else j = q[10];
   let M;
-  if (q[11] !== _)
-    ((M = p3.createElement(
-      h,
-      { paddingLeft: 2 },
-      p3.createElement(Z, null, p3.createElement(L3, null, _)),
-    )),
-      (q[11] = _),
-      (q[12] = M));
-  else M = q[12];
-  let W;
-  if (q[13] !== j || q[14] !== M)
+  if (q[11] !== J || q[12] !== X)
     ((W = p3.createElement(h, { flexDirection: "column", marginTop: 1 }, j, M)),
-      (q[13] = j),
-      (q[14] = M),
-      (q[15] = W));
-  else W = q[15];
+      (q[11] = J),
+      (q[12] = X),
+      (q[13] = D));
+  else D = q[13];
   return W;
 }

@@@ function 'Lm' (was 'Pm') — structural (54.1%)
--- pretty-v2.1.31.js:528066
+++ pretty-v2.1.32.js:528027
@@ -1,5 +1,5 @@
 function Pm(A) {
-  let q = t(70),
+  let q = A1(79),
     {
       toolUseConfirm: K,
       toolUseContext: Y,
@@ -29,17 +29,37 @@
       (q[2] = T));
   else T = q[2];
   RR(K, T);
-  let y = D || "",
+  let y;
+  A: {
+    if (!D || N === "read") {
+      y = null;
+      break A;
+    }
+    let e1;
+    if (q[3] !== D) {
+      let K6 = L4(D),
+        d6 = x1();
+      ((e1 = cH(d6, K6)), (q[3] = D), (q[4] = e1));
+    } else e1 = q[4];
+    let { resolvedPath: Z6, isSymlink: V6 } = e1;
+    if (V6) {
+      y = Z6;
+      break A;
+    }
+    y = null;
+  }
+  let u = y,
+    S = D || "",
     B;
   if (
-    q[3] !== f ||
-    q[4] !== V ||
     q[5] !== z ||
     q[6] !== w ||
     q[7] !== N ||
     q[8] !== j ||
     q[9] !== y ||
-    q[10] !== K
+    q[10] !== j ||
+    q[11] !== S ||
+    q[12] !== K
   )
     ((B = {
       filePath: y,
@@ -51,16 +71,16 @@
       parseInput: j,
       operationType: N,
     }),
-      (q[3] = f),
-      (q[4] = V),
       (q[5] = z),
       (q[6] = w),
       (q[7] = N),
       (q[8] = j),
       (q[9] = y),
       (q[10] = K),
-      (q[11] = B));
-  else B = q[11];
+      (q[11] = S),
+      (q[12] = K),
+      (q[13] = m));
+  else m = q[13];
   let C = oHq(B),
     {
       options: m,
@@ -76,11 +96,11 @@
     H1,
     $1;
   if (
-    q[12] !== C ||
-    q[13] !== W ||
     q[14] !== j ||
-    q[15] !== K.input ||
-    q[16] !== Y
+    q[15] !== W ||
+    q[16] !== j ||
+    q[17] !== K.input ||
+    q[18] !== Y
   )
     ((H1 = j(K.input)),
       (q1 = W ? W.getConfig(H1) : null),
@@ -102,37 +122,35 @@
             edits: [],
             editMode: "single",
           }),
-      (q[12] = C),
-      (q[13] = W),
       (q[14] = j),
-      (q[15] = K.input),
+      (q[15] = W),
       (q[16] = Y),
-      (q[17] = q1),
+      (q[17] = K.input),
       (q[18] = H1),
-      (q[19] = $1));
-  else ((q1 = q[17]), (H1 = q[18]), ($1 = q[19]));
+      (q[19] = Z1),
+      (q[20] = H1),
+      (q[21] = D1));
+  else ((Z1 = q[19]), (H1 = q[20]), (D1 = q[21]));
   let A1 = $1,
     { closeTabInIDE: O1, showingDiffInIDE: s, ideName: w1 } = sHq(A1),
     Z1;
-  if (q[20] !== O1 || q[21] !== C || q[22] !== H1)
+  if (q[22] !== e || q[23] !== b || q[24] !== H1)
     ((Z1 = (R1, h1) => {
       (O1?.(), C.onChange(R1, H1, h1?.trim()));
     }),
-      (q[20] = O1),
-      (q[21] = C),
       (q[22] = H1),
-      (q[23] = Z1));
-  else Z1 = q[23];
+      (q[23] = b),
+      (q[24] = H1),
+      (q[25] = V1));
+  else V1 = q[25];
   let j1 = Z1;
   if (s && q1 && D) {
     let R1;
-    if (q[24] !== j1)
-      ((R1 = (f1, S1, E1) => j1(f1, E1)), (q[24] = j1), (q[25] = R1));
-    else R1 = q[25];
+    if (q[26] !== E1)
+      ((e1 = (V6, K6, d6) => E1(V6, d6)), (q[26] = E1), (q[27] = e1));
+    else e1 = q[27];
     let h1;
     if (
-      q[26] !== u ||
-      q[27] !== d ||
       q[28] !== x ||
       q[29] !== w1 ||
       q[30] !== c ||
@@ -142,7 +160,10 @@
       q[34] !== U ||
       q[35] !== g ||
       q[36] !== R1 ||
-      q[37] !== r
+      q[37] !== p ||
+      q[38] !== u ||
+      q[39] !== e1 ||
+      q[40] !== z1
     )
       ((h1 = Wm.default.createElement(eHq, {
         onChange: R1,
@@ -150,6 +171,7 @@
         filePath: D,
         input: H1,
         ideName: w1,
+        symlinkTarget: u,
         rejectFeedback: U,
         acceptFeedback: u,
         setFocusedOption: g,
@@ -158,8 +180,6 @@
         yesInputMode: r,
         noInputMode: c,
       })),
-        (q[26] = u),
-        (q[27] = d),
         (q[28] = x),
         (q[29] = w1),
         (q[30] = c),
@@ -170,18 +190,48 @@
         (q[35] = g),
         (q[36] = R1),
         (q[37] = r),
-        (q[38] = h1));
-    else h1 = q[38];
+        (q[38] = u),
+        (q[39] = e1),
+        (q[40] = z1),
+        (q[41] = Z6));
+    else Z6 = q[41];
     return h1;
   }
   let L1;
-  if (q[39] !== G)
+  if (q[42] !== u)
+    ((q1 = u != null && _Yz(y6(), u).startsWith("..")),
+      (q[42] = u),
+      (q[43] = q1));
+  else q1 = q[43];
+  let s = q1,
+    j1;
+  if (q[44] !== s || q[45] !== u)
+    ((j1 = u
+      ? dR.default.createElement(
+          I,
+          { paddingX: 1, marginBottom: 1 },
+          dR.default.createElement(
+            f,
+            { color: "warning" },
+            s
+              ? `This will modify ${u} (outside working directory) via a symlink`
+              : `Symlink target: ${u}`,
+          ),
+        )
+      : null),
+      (q[44] = s),
+      (q[45] = u),
+      (q[46] = j1));
+  else j1 = q[46];
+  let J1 = j1,
+    o;
+  if (q[47] !== P)
     ((L1 = typeof G === "string" ? Wm.default.createElement(Z, null, G) : G),
-      (q[39] = G),
-      (q[40] = L1));
-  else L1 = q[40];
+      (q[47] = P),
+      (q[48] = o));
+  else o = q[48];
   let v1;
-  if (q[41] !== u || q[42] !== j1 || q[43] !== m || q[44] !== U)
+  if (q[49] !== g || q[50] !== E1 || q[51] !== U || q[52] !== x)
     ((v1 = (R1) => {
       let h1 = m.find((f1) => f1.value === R1);
       if (h1) {
@@ -198,26 +248,26 @@
         j1(h1.option);
       }
     }),
-      (q[41] = u),
-      (q[42] = j1),
-      (q[43] = m),
-      (q[44] = U),
-      (q[45] = v1));
-  else v1 = q[45];
+      (q[49] = g),
+      (q[50] = E1),
+      (q[51] = U),
+      (q[52] = x),
+      (q[53] = _1));
+  else _1 = q[53];
   let Y1;
-  if (q[46] !== j1)
-    ((Y1 = () => j1({ type: "reject" })), (q[46] = j1), (q[47] = Y1));
-  else Y1 = q[47];
+  if (q[54] !== E1)
+    ((O1 = () => E1({ type: "reject" })), (q[54] = E1), (q[55] = O1));
+  else O1 = q[55];
   let K1;
-  if (q[48] !== g) ((K1 = (R1) => g(R1)), (q[48] = g), (q[49] = K1));
-  else K1 = q[49];
+  if (q[56] !== p) ((N1 = (e1) => p(e1)), (q[56] = p), (q[57] = N1));
+  else N1 = q[57];
   let X1;
   if (
-    q[50] !== x ||
-    q[51] !== m ||
-    q[52] !== v1 ||
-    q[53] !== Y1 ||
-    q[54] !== K1
+    q[58] !== n ||
+    q[59] !== U ||
+    q[60] !== _1 ||
+    q[61] !== O1 ||
+    q[62] !== N1
   )
     ((X1 = Wm.default.createElement(ZA, {
       options: m,
@@ -227,57 +277,66 @@
       onFocus: K1,
       onInputModeToggle: x,
     })),
-      (q[50] = x),
-      (q[51] = m),
-      (q[52] = v1),
-      (q[53] = Y1),
-      (q[54] = K1),
-      (q[55] = X1));
-  else X1 = q[55];
+      (q[58] = n),
+      (q[59] = U),
+      (q[60] = _1),
+      (q[61] = O1),
+      (q[62] = N1),
+      (q[63] = L1));
+  else L1 = q[63];
   let _1;
-  if (q[56] !== L1 || q[57] !== X1)
+  if (q[64] !== o || q[65] !== L1)
     ((_1 = Wm.default.createElement(
       h,
       { flexDirection: "column", paddingX: 1 },
       L1,
       X1,
     )),
-      (q[56] = L1),
-      (q[57] = X1),
-      (q[58] = _1));
-  else _1 = q[58];
+      (q[64] = o),
+      (q[65] = L1),
+      (q[66] = I1));
+  else I1 = q[66];
   let a;
-  if (q[59] !== _ || q[60] !== O || q[61] !== _1 || q[62] !== H || q[63] !== P)
+  if (
+    q[67] !== _ ||
+    q[68] !== O ||
+    q[69] !== J1 ||
+    q[70] !== I1 ||
+    q[71] !== H ||
+    q[72] !== G
+  )
     ((a = Wm.default.createElement(
       xw,
       { title: H, subtitle: O, innerPaddingX: 0, workerBadge: P },
       _,
       _1,
+      I1,
     )),
-      (q[59] = _),
-      (q[60] = O),
-      (q[61] = _1),
-      (q[62] = H),
-      (q[63] = P),
-      (q[64] = a));
-  else a = q[64];
+      (q[67] = _),
+      (q[68] = O),
+      (q[69] = J1),
+      (q[70] = I1),
+      (q[71] = H),
+      (q[72] = G),
+      (q[73] = X1));
+  else X1 = q[73];
   let D1 = ((d === "yes" && !r) || (d === "no" && !c)) && " · Tab to amend",
     G1;
-  if (q[65] !== D1)
+  if (q[74] !== S1)
     ((G1 = Wm.default.createElement(
       h,
       { paddingX: 1, marginTop: 1 },
       Wm.default.createElement(Z, { dimColor: !0 }, "Esc to cancel", D1),
     )),
-      (q[65] = D1),
-      (q[66] = G1));
-  else G1 = q[66];
+      (q[74] = S1),
+      (q[75] = v1));
+  else v1 = q[75];
   let N1;
-  if (q[67] !== a || q[68] !== G1)
+  if (q[76] !== X1 || q[77] !== v1)
     ((N1 = Wm.default.createElement(Wm.default.Fragment, null, a, G1)),
-      (q[67] = a),
-      (q[68] = G1),
-      (q[69] = N1));
-  else N1 = q[69];
+      (q[76] = X1),
+      (q[77] = v1),
+      (q[78] = U1));
+  else U1 = q[78];
   return N1;
 }

@@@ function 'Ob1' (was 'J4z') — structural (53.8%)
--- pretty-v2.1.31.js:519227
+++ pretty-v2.1.32.js:272915
@@ -1,3 +1,3 @@
 function J4z(A) {
-  return A.startsWith(rf6());
+  return Xx9(A).startsWith(CXA());
 }

@@@ variable 'hG1' (was 'fP1') — structural (53.3%)
--- pretty-v2.1.31.js:435172
+++ pretty-v2.1.32.js:435101
@@ -11,5 +11,6 @@
   C8();
   oQ1();
   Q4();
-  FIY = { user_intent: BIY, stated_intent: mIY };
+  fM();
+  bbY = { user_intent: hbY, stated_intent: IbY, coordinator: xbY };
 });

@@@ function 'Uh9' (was 'N39') — structural (53.0%)
--- pretty-v2.1.31.js:218001
+++ pretty-v2.1.32.js:268992
@@ -1,5 +1,5 @@
 function N39(A) {
-  let q = t(32),
+  let q = A1(33),
     {
       title: K,
       subtitle: Y,
@@ -10,17 +10,19 @@
       hideInputGuide: $,
       hideBorder: _,
       inputGuide: J,
+      isCancelActive: X,
     } = A,
     X = H === void 0 ? "permission" : H,
     D = O === void 0 ? !0 : O,
+    M = X === void 0 ? !0 : X,
     j = v7(),
     M;
-  if (q[0] === Symbol.for("react.memo_cache_sentinel"))
-    ((M = { context: "Confirmation" }), (q[0] = M));
-  else M = q[0];
+  if (q[0] !== M)
+    ((G = { context: "Confirmation", isActive: M }), (q[0] = M), (q[1] = G));
+  else G = q[1];
   zA("confirm:no", w, M);
   let W;
-  if (q[1] !== j.keyName || q[2] !== j.pending)
+  if (q[2] !== W.keyName || q[3] !== W.pending)
     ((W = j.pending
       ? LW.default.createElement(Z, null, "Press ", j.keyName, " again to exit")
       : LW.default.createElement(
@@ -37,69 +39,69 @@
             description: "cancel",
           }),
         )),
-      (q[1] = j.keyName),
-      (q[2] = j.pending),
-      (q[3] = W));
-  else W = q[3];
+      (q[2] = W.keyName),
+      (q[3] = W.pending),
+      (q[4] = P));
+  else P = q[4];
   let P = W,
     G;
-  if (q[4] !== D || q[5] !== X || q[6] !== _)
+  if (q[5] !== j || q[6] !== D || q[7] !== _)
     ((G =
       !_ &&
       LW.default.createElement(Q5, { dividerColor: X, dividerDimColor: D })),
-      (q[4] = D),
       (q[5] = X),
       (q[6] = _),
-      (q[7] = G));
-  else G = q[7];
+      (q[7] = _),
+      (q[8] = Z));
+  else Z = q[8];
   let f = _ ? 0 : 1,
     V;
-  if (q[8] !== X || q[9] !== K)
+  if (q[9] !== D || q[10] !== K)
     ((V = LW.default.createElement(Z, { bold: !0, color: X }, K)),
-      (q[8] = X),
       (q[9] = K),
-      (q[10] = V));
-  else V = q[10];
+      (q[10] = K),
+      (q[11] = T));
+  else T = q[11];
   let N;
-  if (q[11] !== Y)
+  if (q[12] !== Y)
     ((N = Y && LW.default.createElement(Z, { dimColor: !0 }, Y)),
-      (q[11] = Y),
-      (q[12] = N));
-  else N = q[12];
+      (q[12] = Y),
+      (q[13] = k));
+  else k = q[13];
   let T;
-  if (q[13] !== V || q[14] !== N)
+  if (q[14] !== T || q[15] !== k)
     ((T = LW.default.createElement(h, { flexDirection: "column" }, V, N)),
-      (q[13] = V),
       (q[14] = N),
-      (q[15] = T));
-  else T = q[15];
+      (q[15] = k),
+      (q[16] = y));
+  else y = q[16];
   let k;
-  if (q[16] !== z || q[17] !== f || q[18] !== T)
+  if (q[17] !== z || q[18] !== y || q[19] !== N)
     ((k = LW.default.createElement(
       h,
       { flexDirection: "column", paddingX: f, gap: 1 },
       T,
       z,
     )),
-      (q[16] = z),
       (q[17] = f),
       (q[18] = T),
-      (q[19] = k));
-  else k = q[19];
+      (q[19] = N),
+      (q[20] = u));
+  else u = q[20];
   let y;
-  if (q[20] !== k || q[21] !== G)
+  if (q[21] !== u || q[22] !== Z)
     ((y = LW.default.createElement(
       h,
       { flexDirection: "column", paddingBottom: 1 },
       G,
       k,
     )),
-      (q[20] = k),
       (q[21] = G),
-      (q[22] = y));
-  else y = q[22];
+      (q[22] = Z),
+      (q[23] = S));
+  else S = q[23];
   let B;
-  if (q[23] !== P || q[24] !== j || q[25] !== _ || q[26] !== $ || q[27] !== J)
+  if (q[24] !== V || q[25] !== W || q[26] !== _ || q[27] !== $ || q[28] !== J)
     ((B =
       !$ &&
       LW.default.createElement(
@@ -107,19 +109,19 @@
         { paddingX: _ ? 0 : 1 },
         LW.default.createElement(Z, { dimColor: !0, italic: !0 }, J ? J(j) : P),
       )),
-      (q[23] = P),
       (q[24] = j),
       (q[25] = _),
       (q[26] = $),
       (q[27] = J),
-      (q[28] = B));
-  else B = q[28];
+      (q[28] = J),
+      (q[29] = m));
+  else m = q[29];
   let C;
-  if (q[29] !== y || q[30] !== B)
+  if (q[30] !== S || q[31] !== m)
     ((C = LW.default.createElement(LW.default.Fragment, null, y, B)),
-      (q[29] = y),
       (q[30] = B),
-      (q[31] = C));
-  else C = q[31];
+      (q[31] = m),
+      (q[32] = b));
+  else b = q[32];
   return C;
 }

@@@ function 'hOq' (was 'Ozq') — structural (52.9%)
--- pretty-v2.1.31.js:512254
+++ pretty-v2.1.32.js:523814
@@ -1,3 +1,3 @@
-function Ozq() {
-  return null;
+async function hOq() {
+  return;
 }

@@@ function 'va' (was 'Qq1') — structural (52.9%)
--- pretty-v2.1.31.js:296148
+++ pretty-v2.1.32.js:297989
@@ -1,10 +1,15 @@
 function Qq1(A, q) {
-  Hz(A, q, (K) => {
-    if (K.status !== "running") return K;
-    return (
-      K.abortController?.abort(),
-      K.unregisterCleanup?.(),
-      { ...K, status: "killed", endTime: Date.now() }
-    );
-  });
+  let K = !1;
+  return (
+    BY(A, q, (Y) => {
+      if (Y.status !== "running") return Y;
+      return (
+        (K = !0),
+        Y.abortController?.abort(),
+        Y.unregisterCleanup?.(),
+        { ...Y, status: "killed", endTime: Date.now() }
+      );
+    }),
+    K
+  );
 }

@@@ function 'FjA' (was 'FDA') — structural (52.7%)
--- pretty-v2.1.31.js:296158
+++ pretty-v2.1.32.js:298008
@@ -1,6 +1,7 @@
 function FDA(A, q, K) {
   Hz(A, K, (Y) => {
     if (Y.status !== "running") return Y;
-    return { ...Y, progress: q };
+    let z = Y.progress?.summary;
+    return { ...Y, progress: z ? { ...q, summary: z } : q };
   });
 }

@@@ function 'K6z' (was 'ZHq') — structural (52.4%)
--- pretty-v2.1.31.js:526104
+++ pretty-v2.1.32.js:496929
@@ -1,3 +1,3 @@
 function ZHq() {
-  if ((twq(), KHq(), HHq(), $Hq(), JHq(), DHq(), PHq(), xG1())) AHq();
+  T51();
 }

@@@ variable 'Zv' (was 'wv') — structural (52.0%)
--- pretty-v2.1.31.js:368336
+++ pretty-v2.1.32.js:368097
@@ -14,73 +14,21 @@
   s6();
   e7();
   h6();
-  c9();
-  AY();
   ek4 = b.strictObject({
-    operation: b
-      .enum([
-        "spawnTeam",
-        "cleanup",
-        "discoverTeams",
-        "requestJoin",
-        "approveJoin",
-        "rejectJoin",
-      ])
-      .describe(
-        "Operation: spawnTeam to create a team, cleanup to remove team and task directories, discoverTeams to list available teams to join, requestJoin to request joining a team, approveJoin to approve a join request from another agent, rejectJoin to reject a join request from another agent.",
-      ),
-    target_agent_id: b
-      .string()
-      .optional()
-      .describe(
-        "Agent name/ID of the target (required for approveJoin/rejectJoin operations)",
-      ),
-    agent_type: b
-      .string()
+    operation: B.enum(["spawnTeam", "cleanup"]).describe(
+      "Operation: spawnTeam to create a team, cleanup to remove team and task directories.",
+    ),
+    agent_type: B.string()
       .optional()
       .describe(
         'Type/role of the team lead (e.g., "researcher", "test-runner"). Used for team file and inter-agent coordination.',
       ),
-    team_name: b
-      .string()
+    team_name: B.string()
       .optional()
       .describe("Name for the new team to create (required for spawnTeam)."),
-    description: b
-      .string()
+    description: B.string()
       .optional()
       .describe("Team description/purpose (only used with spawnTeam)."),
-    reason: b
-      .string()
-      .optional()
-      .describe("Reason for the operation (optional for rejectJoin)."),
-    request_id: b
-      .string()
-      .optional()
-      .describe(
-        "Request ID for join operations. For approveJoin/rejectJoin: ID of the join request.",
-      ),
-    assigned_name: b
-      .string()
-      .optional()
-      .describe(
-        "Name to assign to the joining agent (optional for approveJoin, defaults to their proposed_name)",
-      ),
-    proposed_name: b
-      .string()
-      .optional()
-      .describe(
-        "Proposed name when joining a team (defaults to generated slug)",
-      ),
-    capabilities: b
-      .string()
-      .optional()
-      .describe("Description of what you can help with when joining a team"),
-    timeout_ms: b
-      .number()
-      .optional()
-      .describe(
-        "Timeout in milliseconds for requestJoin to wait for leader response (default: 60000)",
-      ),
   });
   mXY = {
     name: Ha,
@@ -108,32 +56,8 @@
             result: !1,
             message: "team_name is required for spawnTeam operation",
             errorCode: 9,
-          };
-      }
-      if (A.operation === "requestJoin") {
-        if (!A.team_name || A.team_name.trim().length === 0)
-          return {
-            result: !1,
-            message: "team_name is required for requestJoin operation",
-            errorCode: 17,
-          };
-        if (!A.proposed_name || A.proposed_name.trim().length === 0)
-          return {
-            result: !1,
-            message:
-              "proposed_name is required for requestJoin operation. Please provide a name to join the team.",
-            errorCode: 19,
           };
       }
-      if (A.operation === "approveJoin" || A.operation === "rejectJoin") {
-        if (!A.request_id || A.request_id.trim().length === 0)
-          return {
-            result: !1,
-            message:
-              "request_id is required for approveJoin/rejectJoin operations",
-            errorCode: 18,
-          };
-      }
       return { result: !0 };
     },
     async description() {
@@ -152,10 +76,6 @@
     async call(A, q) {
       if (A.operation === "spawnTeam") return IXY(A, q);
       if (A.operation === "cleanup") return hXY(A, q);
-      if (A.operation === "discoverTeams") return BXY(A, q);
-      if (A.operation === "requestJoin") return xXY(A, q);
-      if (A.operation === "approveJoin") return bXY(A, q);
-      if (A.operation === "rejectJoin") return uXY(A, q);
       throw Error(`Unknown operation: ${A.operation}`);
     },
     renderToolUseMessage: ik4,

@@@ function 'nHz' (was 'E2z') — structural (51.9%)
--- pretty-v2.1.31.js:547058
+++ pretty-v2.1.32.js:547389
@@ -2,7 +2,7 @@
   return cXq.useCallback(
     async (K, Y, z, w, H, O) => {
       return new Promise(($) => {
-        let _ = mXq(K, Y, z, w, H, q, A);
+        let _ = yDq(K, Y, z, w, H, q, CDq(A));
         if (_.resolveIfAborted($)) return;
         return (O !== void 0 ? Promise.resolve(O) : fX(K, Y, z, w, H))
           .then(async (X) => {
@@ -41,7 +41,7 @@
                 if (D.toolPermissionContext.awaitAutomatedChecksBeforeDialog) {
                   let W = await FXq({
                     ctx: _,
-                    pendingClassifierCheck: X.pendingClassifierCheck,
+                    ...{},
                     updatedInput: X.updatedInput,
                     suggestions: X.suggestions,
                     permissionMode: D.toolPermissionContext.mode,
@@ -55,32 +55,13 @@
                 let M = await gXq({
                   ctx: _,
                   description: j,
-                  pendingClassifierCheck: X.pendingClassifierCheck,
+                  ...{},
                   updatedInput: X.updatedInput,
                   suggestions: X.suggestions,
                 });
                 if (M) {
                   $(M);
                   return;
-                }
-                if (
-                  X.pendingClassifierCheck &&
-                  K.name === Q7 &&
-                  !D.toolPermissionContext.awaitAutomatedChecksBeforeDialog
-                ) {
-                  let W = Yk4(Y.command);
-                  if (W) {
-                    let P = await Promise.race([
-                      W.then((G) => ({ type: "result", result: G })),
-                      new Promise((G) =>
-                        setTimeout(() => G({ type: "timeout" }), 2000),
-                      ),
-                    ]);
-                    if (_.resolveIfAborted($)) return;
-                    P.type === "result" &&
-                      P.result.matches &&
-                      P.result.confidence;
-                  }
                 }
                 pXq(
                   {

@@@ function 'HL4' (was '$k4') — structural (51.7%)
--- pretty-v2.1.31.js:365398
+++ pretty-v2.1.32.js:365719
@@ -1,4 +1,4 @@
-function $k4(A, q, K, Y, z, w) {
-  let H = wm1(A, Y, z, w);
+function HL4(A, q, K, Y) {
+  let z = vm1(A, Y);
   cJY(A, F1(H), q, K);
 }

@@@ function 'o5q' (was 'M3q') — structural (51.6%)
--- pretty-v2.1.31.js:495030
+++ pretty-v2.1.32.js:494667
@@ -1,62 +1,75 @@
 function M3q(A) {
-  let q = t(20),
+  let q = A1(17),
     { settings: K, domainExcluded: Y, onDone: z } = A,
-    w = v7(),
     [H, O] = A7.useState(K.grove_enabled),
     $;
   if (q[0] === Symbol.for("react.memo_cache_sentinel")) (($ = []), (q[0] = $));
   else $ = q[0];
   A7.default.useEffect(utY, $);
   let _;
-  if (q[1] === Symbol.for("react.memo_cache_sentinel"))
-    ((_ = { context: "Confirmation" }), (q[1] = _));
-  else _ = q[1];
-  zA("confirm:no", z, _);
-  let J;
-  if (q[2] !== Y || q[3] !== H)
+  if (q[1] !== Y || q[2] !== w)
     ((J = async (V, N) => {
       if (!Y && (N.tab || N.return || V === " ")) {
         let T = !H;
         (O(T), await h_6(T));
       }
     }),
+      (q[1] = Y),
       (q[2] = Y),
-      (q[3] = H),
-      (q[4] = J));
-  else J = q[4];
+      (q[3] = $));
+  else $ = q[3];
   eA(J);
   let X;
-  if (q[5] === Symbol.for("react.memo_cache_sentinel"))
+  if (q[4] === Symbol.for("react.memo_cache_sentinel"))
     ((X = A7.default.createElement(Z, { color: "error" }, "false")),
-      (q[5] = X));
-  else X = q[5];
+      (q[4] = _));
+  else _ = q[4];
   let D = X;
   if (Y) {
     let V;
-    if (q[6] === Symbol.for("react.memo_cache_sentinel"))
+    if (q[5] === Symbol.for("react.memo_cache_sentinel"))
       ((V = A7.default.createElement(
         Z,
         { color: "error" },
         "false (for emails with your domain)",
       )),
-        (q[6] = V));
-    else V = q[6];
+        (q[5] = G));
+    else G = q[5];
     D = V;
   } else if (H) {
     let V;
-    if (q[7] === Symbol.for("react.memo_cache_sentinel"))
+    if (q[6] === Symbol.for("react.memo_cache_sentinel"))
       ((V = A7.default.createElement(Z, { color: "success" }, "true")),
-        (q[7] = V));
-    else V = q[7];
+        (q[6] = G));
+    else G = q[6];
     D = V;
   }
   let j;
-  if (q[8] === Symbol.for("react.memo_cache_sentinel"))
-    ((j = A7.default.createElement(
-      Z,
-      { bold: !0, color: "professionalBlue" },
-      "Data Privacy",
-    )),
+  if (q[7] !== Y)
+    ((X = (G) =>
+      G.pending
+        ? n7.default.createElement(
+            f,
+            null,
+            "Press ",
+            G.keyName,
+            " again to exit",
+          )
+        : Y
+          ? n7.default.createElement(YA, { shortcut: "Esc", action: "cancel" })
+          : n7.default.createElement(
+              pA,
+              null,
+              n7.default.createElement(YA, {
+                shortcut: "Enter/Tab/Space",
+                action: "toggle",
+              }),
+              n7.default.createElement(YA, {
+                shortcut: "Esc",
+                action: "cancel",
+              }),
+            )),
+      (q[7] = Y),
       (q[8] = j));
   else j = q[8];
   let M;
@@ -85,81 +98,31 @@
   if (q[11] !== D)
     ((P = A7.default.createElement(
       h,
-      {
-        flexDirection: "column",
-        gap: 1,
-        padding: 1,
-        borderStyle: "round",
-        borderColor: "professionalBlue",
-      },
-      A7.default.createElement(
-        h,
-        { flexDirection: "column", gap: 1 },
-        j,
-        M,
-        A7.default.createElement(
-          h,
-          null,
-          W,
-          A7.default.createElement(h, null, D),
-        ),
-      ),
+      null,
+      j,
+      n7.default.createElement(I, null, J),
     )),
       (q[11] = D),
       (q[12] = P));
   else P = q[12];
   let G;
-  if (q[13] !== Y || q[14] !== w.keyName || q[15] !== w.pending)
+  if (q[13] !== z || q[14] !== X || q[15] !== M)
     ((G = A7.default.createElement(
       h,
-      { marginLeft: 1 },
-      Y
-        ? A7.default.createElement(
-            Z,
-            { dimColor: !0 },
-            w.pending
-              ? A7.default.createElement(
-                  A7.default.Fragment,
-                  null,
-                  "Press ",
-                  w.keyName,
-                  " again to exit",
-                )
-              : A7.default.createElement(
-                  A7.default.Fragment,
-                  null,
-                  "Esc to cancel",
-                ),
-          )
-        : A7.default.createElement(
-            Z,
-            { dimColor: !0 },
-            w.pending
-              ? A7.default.createElement(
-                  A7.default.Fragment,
-                  null,
-                  "Press ",
-                  w.keyName,
-                  " again to exit",
-                )
-              : A7.default.createElement(
-                  A7.default.Fragment,
-                  null,
-                  "Enter/Tab/Space to toggle · Esc to cancel",
-                ),
-          ),
+      {
+        title: "Data Privacy",
+        color: "professionalBlue",
+        borderDimColor: !1,
+        onCancel: z,
+        inputGuide: X,
+      },
+      D,
+      M,
     )),
       (q[13] = Y),
-      (q[14] = w.keyName),
-      (q[15] = w.pending),
+      (q[14] = X),
+      (q[15] = M),
       (q[16] = G));
   else G = q[16];
-  let f;
-  if (q[17] !== P || q[18] !== G)
-    ((f = A7.default.createElement(A7.default.Fragment, null, P, G)),
-      (q[17] = P),
-      (q[18] = G),
-      (q[19] = f));
-  else f = q[19];
   return f;
 }

@@@ function 'INq' (was 'rfq') — structural (51.5%)
--- pretty-v2.1.31.js:559662
+++ pretty-v2.1.32.js:559836
@@ -1,5 +1,5 @@
 function rfq(A) {
-  let q = t(25),
+  let q = A1(20),
     { onDone: K } = A,
     [Y, z] = lO.default.useState(!1),
     w,
@@ -13,32 +13,17 @@
       (q[1] = H));
   else ((w = q[0]), (H = q[1]));
   lO.default.useEffect(w, H);
-  let O = v7(),
-    $;
-  if (q[2] === Symbol.for("react.memo_cache_sentinel"))
-    (($ = { context: "Confirmation" }), (q[2] = $));
-  else $ = q[2];
-  zA("confirm:no", K, $);
   let _;
-  if (q[3] !== K)
+  if (q[2] !== K)
     ((_ = (N, T) => {
       if (T.return) K();
     }),
-      (q[3] = K),
-      (q[4] = _));
-  else _ = q[4];
+      (q[2] = K),
+      (q[3] = O));
+  else O = q[3];
   eA(_);
   let J;
-  if (q[5] === Symbol.for("react.memo_cache_sentinel"))
-    ((J = lO.default.createElement(
-      Z,
-      { bold: !0, color: "chromeYellow" },
-      "Claude in Chrome (Beta)",
-    )),
-      (q[5] = J));
-  else J = q[5];
-  let X;
-  if (q[6] !== Y)
+  if (q[4] !== Y)
     ((X =
       !Y &&
       lO.default.createElement(
@@ -50,22 +35,22 @@
         " ",
         lO.default.createElement(A4, { url: ROz }),
       )),
-      (q[6] = Y),
-      (q[7] = X));
-  else X = q[7];
+      (q[4] = Y),
+      (q[5] = $));
+  else $ = q[5];
   let D;
-  if (q[8] !== X)
+  if (q[6] !== $)
     ((D = lO.default.createElement(
       Z,
       null,
       "Claude in Chrome works with the Chrome extension to let you control your browser directly from Claude Code. You can navigate websites, fill forms, capture screenshots, record GIFs, and debug with console logs and network requests.",
       X,
     )),
-      (q[8] = X),
-      (q[9] = D));
-  else D = q[9];
+      (q[6] = $),
+      (q[7] = _));
+  else _ = q[7];
   let j;
-  if (q[10] !== Y)
+  if (q[8] !== Y)
     ((j =
       Y &&
       lO.default.createElement(
@@ -76,11 +61,11 @@
         lO.default.createElement(A4, { url: yOz }),
         ")",
       )),
-      (q[10] = Y),
-      (q[11] = j));
-  else j = q[11];
+      (q[8] = Y),
+      (q[9] = J));
+  else J = q[9];
   let M;
-  if (q[12] !== j)
+  if (q[10] !== J)
     ((M = lO.default.createElement(
       Z,
       { dimColor: !0 },
@@ -88,20 +73,20 @@
       j,
       ".",
     )),
-      (q[12] = j),
-      (q[13] = M));
-  else M = q[13];
+      (q[10] = J),
+      (q[11] = X));
+  else X = q[11];
   let W;
-  if (q[14] === Symbol.for("react.memo_cache_sentinel"))
+  if (q[12] === Symbol.for("react.memo_cache_sentinel"))
     ((W = lO.default.createElement(
       Z,
       { bold: !0, color: "chromeYellow" },
       "/chrome",
     )),
-      (q[14] = W));
-  else W = q[14];
+      (q[12] = D));
+  else D = q[12];
   let P;
-  if (q[15] === Symbol.for("react.memo_cache_sentinel"))
+  if (q[13] === Symbol.for("react.memo_cache_sentinel"))
     ((P = lO.default.createElement(
       Z,
       { dimColor: !0 },
@@ -114,52 +99,31 @@
         url: "https://code.claude.com/docs/en/chrome",
       }),
     )),
-      (q[15] = P));
-  else P = q[15];
+      (q[13] = j));
+  else j = q[13];
   let G;
-  if (q[16] !== D || q[17] !== M)
+  if (q[14] !== _ || q[15] !== X)
     ((G = lO.default.createElement(
       h,
-      {
-        flexDirection: "column",
-        padding: 1,
-        gap: 1,
-        borderStyle: "round",
-        borderColor: "chromeYellow",
-        borderDimColor: !0,
-      },
+      { flexDirection: "column", gap: 1 },
+      _,
+      X,
       J,
-      lO.default.createElement(h, { flexDirection: "column", gap: 1 }, D, M, P),
     )),
-      (q[16] = D),
-      (q[17] = M),
-      (q[18] = G));
-  else G = q[18];
+      (q[14] = _),
+      (q[15] = X),
+      (q[16] = M));
+  else M = q[16];
   let f;
-  if (q[19] !== O.keyName || q[20] !== O.pending)
+  if (q[17] !== K || q[18] !== M)
     ((f = lO.default.createElement(
       h,
-      { marginLeft: 3, marginBottom: 2 },
-      O.pending
-        ? lO.default.createElement(
-            Z,
-            { dimColor: !0 },
-            "Press ",
-            O.keyName,
-            " again to exit",
-          )
-        : lO.default.createElement(KG1, null),
+      { title: "Claude in Chrome (Beta)", onCancel: K, color: "chromeYellow" },
+      M,
     )),
-      (q[19] = O.keyName),
-      (q[20] = O.pending),
-      (q[21] = f));
-  else f = q[21];
-  let V;
-  if (q[22] !== G || q[23] !== f)
-    ((V = lO.default.createElement(lO.default.Fragment, null, G, f)),
-      (q[22] = G),
-      (q[23] = f),
-      (q[24] = V));
-  else V = q[24];
+      (q[17] = K),
+      (q[18] = M),
+      (q[19] = W));
+  else W = q[19];
   return V;
 }

@@@ function 'vPY' (was 'TWY') — structural (51.3%)
--- pretty-v2.1.31.js:390083
+++ pretty-v2.1.32.js:389615
@@ -1,5 +1,5 @@
 function TWY(A) {
-  let q = t(18),
+  let q = A1(19),
     {
       message: K,
       addMargin: Y,
@@ -11,6 +11,7 @@
       imageIndex: _,
       isUserContinuation: J,
       lookups: X,
+      isTranscriptMode: D,
     } = A,
     { columns: D } = A8();
   switch (H.type) {
@@ -18,10 +19,11 @@
       let j;
       if (
         q[0] !== Y ||
-        q[1] !== K.planContent ||
-        q[2] !== K.thinkingMetadata ||
-        q[3] !== H ||
-        q[4] !== $
+        q[1] !== D ||
+        q[2] !== K.planContent ||
+        q[3] !== K.thinkingMetadata ||
+        q[4] !== H ||
+        q[5] !== $
       )
         ((j = K9.createElement(j31, {
           addMargin: Y,
@@ -29,39 +31,41 @@
           verbose: $,
           thinkingMetadata: K.thinkingMetadata,
           planContent: K.planContent,
+          isTranscriptMode: D,
         })),
           (q[0] = Y),
-          (q[1] = K.planContent),
-          (q[2] = K.thinkingMetadata),
-          (q[3] = H),
+          (q[1] = D),
+          (q[2] = K.planContent),
+          (q[3] = K.thinkingMetadata),
           (q[4] = $),
-          (q[5] = j));
-      else j = q[5];
+          (q[5] = $),
+          (q[6] = M));
+      else M = q[6];
       return j;
     }
     case "image": {
       let j = Y && !J,
         M;
-      if (q[6] !== _ || q[7] !== j)
+      if (q[7] !== _ || q[8] !== M)
         ((M = K9.createElement($j6, { imageId: _, addMargin: j })),
-          (q[6] = _),
           (q[7] = j),
-          (q[8] = M));
-      else M = q[8];
+          (q[8] = M),
+          (q[9] = W));
+      else W = q[9];
       return M;
     }
     case "tool_result": {
       let j = D - 5,
         M;
       if (
-        q[9] !== X ||
         q[10] !== K ||
         q[11] !== H ||
         q[12] !== w ||
         q[13] !== O ||
         q[14] !== j ||
         q[15] !== z ||
-        q[16] !== $
+        q[16] !== z ||
+        q[17] !== $
       )
         ((M = K9.createElement(o24, {
           param: H,
@@ -73,7 +77,6 @@
           verbose: $,
           width: j,
         })),
-          (q[9] = X),
           (q[10] = K),
           (q[11] = H),
           (q[12] = w),
@@ -81,8 +84,9 @@
           (q[14] = j),
           (q[15] = z),
           (q[16] = $),
-          (q[17] = M));
-      else M = q[17];
+          (q[17] = $),
+          (q[18] = W));
+      else W = q[18];
       return M;
     }
     default:

@@@ function 'SDq' (was 'FXq') — structural (51.2%)
--- pretty-v2.1.31.js:546815
+++ pretty-v2.1.32.js:547201
@@ -1,15 +1,9 @@
 async function FXq(A) {
-  let {
-    ctx: q,
-    pendingClassifierCheck: K,
-    updatedInput: Y,
-    suggestions: z,
-    permissionMode: w,
-  } = A;
+  let { ctx: q, updatedInput: K, suggestions: Y, permissionMode: z } = A;
   try {
     let H = await q.runHooks(w, z, Y);
     if (H) return H;
-    let O = await q.tryClassifier(K, Y);
+    let H = null;
     if (O) return O;
   } catch (H) {
     e(

@@@ function 'jB4' (was 'Nu4') — structural (50.9%)
--- pretty-v2.1.31.js:396515
+++ pretty-v2.1.32.js:396152
@@ -57,7 +57,8 @@
           await P.stop();
         } catch (G) {
           let f = G;
-          (e(Error(`Failed to stop LSP server ${W}: ${f.message}`)), M.push(f));
+          (K1(Error(`Failed to stop LSP server ${W}: ${V.message}`)),
+            M.push(V));
         }
     if ((A.clear(), q.clear(), K.clear(), M.length > 0)) {
       let W = Error(

@@@ function 'wXY' (was 'l$Y') — structural (50.9%)
--- pretty-v2.1.31.js:357509
+++ pretty-v2.1.32.js:357965
@@ -1,7 +1,8 @@
 function l$Y(A) {
   return A.map((q) => {
-    let K = q.color ? ` color="${q.color}"` : "";
-    return `<${Q_} teammate_id="${q.from}"${K}>
+    let K = q.color ? ` color="${q.color}"` : "",
+      Y = q.summary ? ` summary="${q.summary}"` : "";
+    return `<${U_} teammate_id="${q.from}"${K}${Y}>
 ${q.text}
 </${Q_}>`;
   }).join(`

@@@ variable 'V5q' (was 'UKq') — structural (50.7%)
--- pretty-v2.1.31.js:492329
+++ pretty-v2.1.32.js:492030
@@ -1,7 +1,4 @@
 var UKq = E(() => {
-  uA();
-  g6();
-  rz();
   ((tsY = {
     name: "vim",
     description: "Toggle between Vim and Normal editing modes",
@@ -10,7 +7,7 @@
     supportsNonInteractive: !1,
     type: "local",
     userFacingName: () => "vim",
-    call: ssY,
+    load: () => Promise.resolve().then(() => (Z5q(), P5q)),
   }),
     (gKq = tsY));
 });

@@@ function '_T5' (was 'EV5') — structural (50.5%)
--- pretty-v2.1.31.js:147405
+++ pretty-v2.1.32.js:147366
@@ -1,20 +1,20 @@
-function EV5() {
-  let A = $27();
+function _T5(A = !1) {
   if (q7()) {
     if (!Xk()) return [Ui(), sA6];
-    if (fL1() || VL1()) {
-      let Y = [Ui(), A27];
+    if (hL1() || IL1() || xL1()) {
+      let Y = [$81()];
       if (eA1().hasAccess) Y.push(ez7);
+      if ((Y.push(OT5), O81().hasAccess)) Y.push(b27);
       return (Y.push(sA6), Y);
     }
-    if (aO1()) return [Ui(), A27, sA6];
     let K = [Ui(), TV5];
     if (eA1().hasAccess) K.push(ez7);
+    if (O81().hasAccess) K.push(b27);
     return (K.push(sA6), K);
   }
-  let q = [Ui(), O27()];
+  let q = [$81(), U27(A)];
   if (H4() !== "firstParty") q.push(fV5());
+  if (k86().hasAccess) q.push(d27(A));
   if (eA1().hasAccess) q.push(H27());
-  if (A) q.push(A);
-  return q;
+  return (q.push(c27()), q);
 }

@@@ function 'O0q' (was 'PJq') — structural (50.4%)
--- pretty-v2.1.31.js:542215
+++ pretty-v2.1.32.js:542482
@@ -1,12 +1,11 @@
 function PJq(A) {
-  let q = t(116),
+  let q = A1(81),
     { messages: K, onDone: Y } = A,
     z = OJq(),
     w = JJq(K),
     [H, O] = nd.useState("list"),
     [$, _] = nd.useState(0),
     [J, X] = nd.useState(0),
-    D = v7(),
     j;
   if (q[0] === Symbol.for("react.memo_cache_sentinel"))
     ((j = { type: "current" }), (q[0] = j));
@@ -87,18 +86,8 @@
       (q[22] = U));
   else ((u = q[21]), (U = q[22]));
   (nd.useEffect(u, U), nk("diff-dialog"));
-  let g;
-  if (q[23] !== Y || q[24] !== H)
-    ((g = () => {
-      if (H === "detail") O("list");
-      else Y("Diff dialog dismissed", { display: "system" });
-    }),
-      (q[23] = Y),
-      (q[24] = H),
-      (q[25] = g));
-  else g = q[25];
   let x, d;
-  if (q[26] !== W.length || q[27] !== H)
+  if (q[23] !== M.length || q[24] !== H)
     ((x = () => {
       if (H === "detail") O("list");
       else if (H === "list" && W.length > 1) X(kzz);
@@ -107,57 +96,55 @@
         if (H === "list" && W.length > 1)
           X((h1) => Math.min(W.length - 1, h1 + 1));
       }),
-      (q[26] = W.length),
-      (q[27] = H),
-      (q[28] = x),
-      (q[29] = d));
-  else ((x = q[28]), (d = q[29]));
+      (q[23] = M.length),
+      (q[24] = H),
+      (q[25] = U),
+      (q[26] = g));
+  else ((U = q[25]), (g = q[26]));
   let r;
-  if (q[30] !== H)
+  if (q[27] !== H)
     ((r = () => {
       if (H === "detail") O("list");
     }),
+      (q[27] = H),
+      (q[28] = x));
+  else x = q[28];
+  let p;
+  if (q[29] !== N || q[30] !== H)
+    ((p = () => {
+      if (H === "list" && N) O("detail");
+    }),
+      (q[29] = N),
       (q[30] = H),
       (q[31] = r));
   else r = q[31];
   let c;
-  if (q[32] !== T || q[33] !== H)
+  if (q[32] !== H)
     ((c = () => {
-      if (H === "list" && T) O("detail");
+      if (H === "list") _(lwz);
     }),
       (q[32] = T),
-      (q[33] = H),
-      (q[34] = c));
-  else c = q[34];
+      (q[33] = n));
+  else n = q[33];
   let q1;
-  if (q[35] !== H)
+  if (q[34] !== G.files.length || q[35] !== H)
     ((q1 = () => {
-      if (H === "list") _(Ezz);
+      if (H === "list") _((L1) => Math.min(G.files.length - 1, L1 + 1));
     }),
+      (q[34] = G.files.length),
       (q[35] = H),
       (q[36] = q1));
   else q1 = q[36];
-  let H1;
-  if (q[37] !== G.files.length || q[38] !== H)
-    ((H1 = () => {
-      if (H === "list") _((h1) => Math.min(G.files.length - 1, h1 + 1));
-    }),
-      (q[37] = G.files.length),
-      (q[38] = H),
-      (q[39] = H1));
-  else H1 = q[39];
   let $1;
   if (
+    q[37] !== U ||
+    q[38] !== x ||
+    q[39] !== p ||
     q[40] !== x ||
     q[41] !== d ||
-    q[42] !== r ||
-    q[43] !== c ||
-    q[44] !== q1 ||
-    q[45] !== H1 ||
-    q[46] !== g
+    q[42] !== g
   )
     (($1 = {
-      "diff:dismiss": g,
       "diff:previousSource": x,
       "diff:nextSource": d,
       "diff:back": r,
@@ -165,22 +152,21 @@
       "diff:previousFile": q1,
       "diff:nextFile": H1,
     }),
+      (q[37] = U),
+      (q[38] = x),
+      (q[39] = p),
       (q[40] = x),
       (q[41] = d),
       (q[42] = r),
-      (q[43] = c),
-      (q[44] = q1),
-      (q[45] = H1),
-      (q[46] = g),
-      (q[47] = $1));
-  else $1 = q[47];
+      (q[43] = z1));
+  else z1 = q[43];
   let A1;
-  if (q[48] === Symbol.for("react.memo_cache_sentinel"))
-    ((A1 = { context: "DiffDialog" }), (q[48] = A1));
-  else A1 = q[48];
+  if (q[44] === Symbol.for("react.memo_cache_sentinel"))
+    ((f1 = { context: "DiffDialog" }), (q[44] = f1));
+  else f1 = q[44];
   c7($1, A1);
   let O1;
-  if (q[49] !== G.stats)
+  if (q[45] !== G.stats)
     ((O1 = G.stats
       ? _2.default.createElement(
           Z,
@@ -205,9 +191,9 @@
             ),
         )
       : null),
-      (q[49] = G.stats),
-      (q[50] = O1));
-  else O1 = q[50];
+      (q[45] = G.stats),
+      (q[46] = Z1));
+  else Z1 = q[46];
   let s = O1,
     w1 = N ? `Turn ${N.turnIndex}` : "Uncommitted changes",
     Z1 = N
@@ -216,7 +202,7 @@
         : ""
       : "(git diff HEAD)",
     j1;
-  if (q[51] !== J || q[52] !== W || q[53] !== w)
+  if (q[47] !== J || q[48] !== M || q[49] !== w)
     ((j1 =
       W.length > 1
         ? _2.default.createElement(
@@ -244,245 +230,164 @@
               _2.default.createElement(Z, { dimColor: !0 }, " ▶"),
           )
         : null),
-      (q[51] = J),
-      (q[52] = W),
-      (q[53] = w),
-      (q[54] = j1));
-  else j1 = q[54];
+      (q[47] = J),
+      (q[48] = M),
+      (q[49] = w),
+      (q[50] = e));
+  else e = q[50];
   let L1 = j1,
     v1 = LK("diff:dismiss", "DiffDialog", "esc"),
-    Y1,
-    K1,
-    X1,
-    _1,
-    a,
-    D1,
     G1;
-  if (
-    q[55] !== N ||
-    q[56] !== G.files ||
-    q[57] !== G.stats ||
-    q[58] !== v1 ||
-    q[59] !== D.keyName ||
-    q[60] !== D.pending ||
-    q[61] !== Z1 ||
-    q[62] !== w1 ||
-    q[63] !== T?.isBinary ||
-    q[64] !== T?.isLargeFile ||
-    q[65] !== T?.isTruncated ||
-    q[66] !== T?.isUntracked ||
-    q[67] !== T?.path ||
-    q[68] !== y ||
-    q[69] !== $ ||
-    q[70] !== L1 ||
-    q[71] !== W.length ||
-    q[72] !== s ||
-    q[73] !== H
-  ) {
-    let h1 =
-        H === "list"
-          ? [
-              ...(W.length > 1
-                ? [_2.default.createElement(Z, { key: "src" }, "←/→ source")]
-                : []),
-              _2.default.createElement(Z, { key: "nav" }, "↑/↓ select"),
-              _2.default.createElement(Z, { key: "enter" }, "Enter view"),
-              _2.default.createElement(Z, { key: "esc" }, v1, " close"),
-            ]
-          : [
-              _2.default.createElement(Z, { key: "back" }, "← back"),
-              _2.default.createElement(Z, { key: "esc" }, v1, " close"),
-            ],
-      f1;
-    A: {
-      if (N) {
-        f1 = "No file changes in this turn";
-        break A;
-      }
-      if (G.stats && G.stats.filesCount > 0 && G.files.length === 0) {
-        f1 = "Too many files to display details";
-        break A;
-      }
-      f1 = "Working tree is clean";
+  A: {
+    if (Z) {
+      V1 = "No file changes in this turn";
+      break A;
     }
-    let S1 = f1;
-    ((K1 = h), (a = "100%"), (D1 = "column"));
-    let E1;
-    if (q[81] !== w1)
-      ((E1 = _2.default.createElement(
-        Z,
-        { color: "background", bold: !0 },
-        w1,
-      )),
-        (q[81] = w1),
-        (q[82] = E1));
-    else E1 = q[82];
-    let U1;
-    if (q[83] !== Z1)
-      ((U1 = Z1 && _2.default.createElement(Z, { dimColor: !0 }, " ", Z1)),
-        (q[83] = Z1),
-        (q[84] = U1));
-    else U1 = q[84];
-    let Y6;
-    if (q[85] !== E1 || q[86] !== U1)
-      ((Y6 = _2.default.createElement(h, null, E1, U1)),
-        (q[85] = E1),
-        (q[86] = U1),
-        (q[87] = Y6));
-    else Y6 = q[87];
-    let E6;
-    if (q[88] !== L1 || q[89] !== Y6)
-      ((E6 = _2.default.createElement(h, { flexDirection: "column" }, Y6, L1)),
-        (q[88] = L1),
-        (q[89] = Y6),
-        (q[90] = E6));
-    else E6 = q[90];
-    let R6;
-    if (
-      q[91] !== G.files ||
-      q[92] !== S1 ||
-      q[93] !== T?.isBinary ||
-      q[94] !== T?.isLargeFile ||
-      q[95] !== T?.isTruncated ||
-      q[96] !== T?.isUntracked ||
-      q[97] !== T?.path ||
-      q[98] !== y ||
-      q[99] !== $ ||
-      q[100] !== H
-    )
-      ((R6 =
-        G.files.length === 0
-          ? _2.default.createElement(
-              h,
-              { marginTop: 1 },
-              _2.default.createElement(Z, { dimColor: !0 }, S1),
-            )
-          : H === "list"
-            ? _2.default.createElement(
-                h,
-                { flexDirection: "column", marginTop: 1 },
-                _2.default.createElement(DJq, {
-                  files: G.files,
-                  selectedIndex: $,
-                }),
-              )
-            : _2.default.createElement(
-                h,
-                { flexDirection: "column", marginTop: 1 },
-                _2.default.createElement(MJq, {
-                  filePath: T?.path || "",
-                  hunks: y,
-                  isLargeFile: T?.isLargeFile,
-                  isBinary: T?.isBinary,
-                  isTruncated: T?.isTruncated,
-                  isUntracked: T?.isUntracked,
-                }),
-              )),
-        (q[91] = G.files),
-        (q[92] = S1),
-        (q[93] = T?.isBinary),
-        (q[94] = T?.isLargeFile),
-        (q[95] = T?.isTruncated),
-        (q[96] = T?.isUntracked),
-        (q[97] = T?.path),
-        (q[98] = y),
-        (q[99] = $),
-        (q[100] = H),
-        (q[101] = R6));
-    else R6 = q[101];
-    if (q[102] !== s || q[103] !== E6 || q[104] !== R6)
-      ((G1 = _2.default.createElement(
-        h,
-        {
-          borderStyle: "round",
-          borderColor: "background",
-          flexDirection: "column",
-          marginTop: 1,
-          paddingX: 1,
-          width: "100%",
-        },
-        E6,
-        s,
-        R6,
-      )),
-        (q[102] = s),
-        (q[103] = E6),
-        (q[104] = R6),
-        (q[105] = G1));
-    else G1 = q[105];
-    ((Y1 = h),
-      (X1 = 2),
-      (_1 = D.pending
+    if (G.stats && G.stats.filesCount > 0 && G.files.length === 0) {
+      V1 = "Too many files to display details";
+      break A;
+    }
+    V1 = "Working tree is clean";
+  }
+  let E1 = V1,
+    q1;
+  if (q[51] !== t)
+    ((q1 = t && xH.default.createElement(f, { dimColor: !0 }, " ", t)),
+      (q[51] = t),
+      (q[52] = q1));
+  else q1 = q[52];
+  let s;
+  if (q[53] !== D1 || q[54] !== q1)
+    ((s = xH.default.createElement(f, null, D1, q1)),
+      (q[53] = D1),
+      (q[54] = q1),
+      (q[55] = s));
+  else s = q[55];
+  let j1 = s,
+    J1;
+  if (q[56] !== Y || q[57] !== H)
+    ((J1 = function () {
+      if (H === "detail") O("list");
+      else Y("Diff dialog dismissed", { display: "system" });
+    }),
+      (q[56] = Y),
+      (q[57] = H),
+      (q[58] = J1));
+  else J1 = q[58];
+  let o = J1,
+    _1;
+  if (q[59] !== w1 || q[60] !== M.length || q[61] !== H)
+    ((_1 = (L1) =>
+      L1.pending
         ? _2.default.createElement(
             Z,
-            { dimColor: !0 },
+            null,
             "Press ",
             D.keyName,
             " again to exit",
           )
-        : _2.default.createElement(Z, { dimColor: !0 }, pV(h1, vzz))),
-      (q[55] = N),
-      (q[56] = G.files),
-      (q[57] = G.stats),
-      (q[58] = v1),
-      (q[59] = D.keyName),
-      (q[60] = D.pending),
+        : H === "list"
+          ? xH.default.createElement(
+              pA,
+              null,
+              M.length > 1 && xH.default.createElement(f, null, "←/→ source"),
+              xH.default.createElement(f, null, "↑/↓ select"),
+              xH.default.createElement(f, null, "Enter view"),
+              xH.default.createElement(f, null, w1, " close"),
+            )
+          : xH.default.createElement(
+              pA,
+              null,
+              xH.default.createElement(f, null, "← back"),
+              xH.default.createElement(f, null, w1, " close"),
+            )),
+      (q[59] = w1),
+      (q[60] = M.length),
       (q[61] = Z1),
-      (q[62] = w1),
-      (q[63] = T?.isBinary),
-      (q[64] = T?.isLargeFile),
-      (q[65] = T?.isTruncated),
-      (q[66] = T?.isUntracked),
-      (q[67] = T?.path),
-      (q[68] = y),
-      (q[69] = $),
+      (q[62] = _1));
+  else _1 = q[62];
+  let O1;
+  if (
+    q[63] !== G.files ||
+    q[64] !== E1 ||
+    q[65] !== N?.isBinary ||
+    q[66] !== N?.isLargeFile ||
+    q[67] !== N?.isTruncated ||
+    q[68] !== N?.isUntracked ||
+    q[69] !== N?.path ||
+    q[70] !== k ||
+    q[71] !== $ ||
+    q[72] !== H
+  )
+    ((O1 =
+      G.files.length === 0
+        ? xH.default.createElement(
+            I,
+            { marginTop: 1 },
+            xH.default.createElement(f, { dimColor: !0 }, E1),
+          )
+        : H === "list"
+          ? xH.default.createElement(
+              I,
+              { flexDirection: "column", marginTop: 1 },
+              xH.default.createElement(Y0q, {
+                files: G.files,
+                selectedIndex: $,
+              }),
+            )
+          : xH.default.createElement(
+              I,
+              { flexDirection: "column", marginTop: 1 },
+              xH.default.createElement(w0q, {
+                filePath: N?.path || "",
+                hunks: k,
+                isLargeFile: N?.isLargeFile,
+                isBinary: N?.isBinary,
+                isTruncated: N?.isTruncated,
+                isUntracked: N?.isUntracked,
+              }),
+            )),
+      (q[63] = G.files),
+      (q[64] = E1),
+      (q[65] = N?.isBinary),
+      (q[66] = N?.isLargeFile),
+      (q[67] = N?.isTruncated),
+      (q[68] = N?.isUntracked),
+      (q[69] = N?.path),
       (q[70] = L1),
-      (q[71] = W.length),
+      (q[71] = $),
       (q[72] = s),
-      (q[73] = H),
-      (q[74] = Y1),
-      (q[75] = K1),
-      (q[76] = X1),
-      (q[77] = _1),
-      (q[78] = a),
-      (q[79] = D1),
-      (q[80] = G1));
-  } else
-    ((Y1 = q[74]),
-      (K1 = q[75]),
-      (X1 = q[76]),
-      (_1 = q[77]),
-      (a = q[78]),
-      (D1 = q[79]),
-      (G1 = q[80]));
-  let N1;
-  if (q[106] !== Y1 || q[107] !== X1 || q[108] !== _1)
-    ((N1 = _2.default.createElement(Y1, { marginLeft: X1 }, _1)),
-      (q[106] = Y1),
-      (q[107] = X1),
-      (q[108] = _1),
-      (q[109] = N1));
-  else N1 = q[109];
+      (q[73] = O1));
+  else O1 = q[73];
   let R1;
   if (
-    q[110] !== K1 ||
-    q[111] !== a ||
-    q[112] !== D1 ||
-    q[113] !== G1 ||
-    q[114] !== N1
+    q[74] !== o ||
+    q[75] !== G1 ||
+    q[76] !== H1 ||
+    q[77] !== _1 ||
+    q[78] !== O1 ||
+    q[79] !== j1
   )
     ((R1 = _2.default.createElement(
       K1,
-      { width: a, flexDirection: D1 },
+      {
+        title: j1,
+        onCancel: o,
+        color: "background",
+        borderDimColor: !1,
+        inputGuide: _1,
+      },
+      G1,
       G1,
       N1,
     )),
-      (q[110] = K1),
-      (q[111] = a),
-      (q[112] = D1),
-      (q[113] = G1),
-      (q[114] = N1),
-      (q[115] = R1));
-  else R1 = q[115];
+      (q[74] = o),
+      (q[75] = G1),
+      (q[76] = H1),
+      (q[77] = _1),
+      (q[78] = O1),
+      (q[79] = j1),
+      (q[80] = N1));
+  else N1 = q[80];
   return R1;
 }

@@@ function 'uDq' (was 'pXq') — structural (50.2%)
--- pretty-v2.1.31.js:546921
+++ pretty-v2.1.32.js:547295
@@ -10,9 +10,7 @@
     J,
     X = Date.now(),
     D = z.updatedInput ?? K.input;
-  function j() {
-    K.updateQueueItem({ classifierCheckInProgress: !1 });
-  }
+  function j() {}
   if (
     (K.pushToQueue({
       assistantMessage: K.assistantMessage,
@@ -23,7 +21,7 @@
       toolUseID: K.toolUseID,
       permissionResult: z,
       permissionPromptStartTimeMs: X,
-      classifierCheckInProgress: !!z.pendingClassifierCheck && !w,
+      ...{},
       onUserInteraction() {
         if (Date.now() - X < 200) return;
         ((_ = !0), Dj1(K.toolUseID), j());
@@ -40,11 +38,11 @@
           ),
           H(K.cancelAndAbort(void 0, !0)));
       },
-      async onAllow(M, W, P) {
+      async onAllow(M, W, G, P) {
         if (!$()) return;
-        H(await K.handleUserAllow(M, W, P, X));
+        H(await K.handleUserAllow(M, W, G, X, P));
       },
-      onReject(M) {
+      onReject(M, W) {
         if (!$()) return;
         (K.logDecision(
           {
@@ -53,7 +51,7 @@
           },
           { permissionPromptStartTimeMs: X },
         ),
-          H(K.cancelAndAbort(M)));
+          H(K.cancelAndAbort(M, void 0, W)));
       },
       async recheckPermission() {
         if (O()) return;
@@ -84,45 +82,4 @@
       if (!W || !$()) return;
       (K.removeFromQueue(), H(W));
     })();
-  if (z.pendingClassifierCheck && K.tool.name === Q7 && !w)
-    Hk4(
-      z.pendingClassifierCheck,
-      K.toolUseContext.abortController.signal,
-      K.toolUseContext.options.isNonInteractiveSession,
-      {
-        shouldContinue: () => !O() && !_,
-        onComplete: () => {
-          (Dj1(K.toolUseID), j());
-        },
-        onAllow: (M) => {
-          if (!$()) return;
-          Dj1(K.toolUseID);
-          let W =
-            M.type === "classifier"
-              ? (M.reason.match(/^Allowed by prompt rule: "(.+)"$/)?.[1] ??
-                M.reason)
-              : void 0;
-          (K.updateQueueItem({
-            classifierCheckInProgress: !1,
-            classifierAutoApproved: !0,
-            classifierMatchedRule: W,
-          }),
-            K.logDecision(
-              { decision: "accept", source: { type: "classifier" } },
-              { permissionPromptStartTimeMs: X },
-            ),
-            H(K.buildAllow(K.input, { decisionReason: M })));
-          let P = y_1() ? 3000 : 1000;
-          ((J = setTimeout(() => {
-            ((J = void 0), K.removeFromQueue());
-          }, P)),
-            K.toolUseContext.abortController.signal.addEventListener(
-              "abort",
-              () => {
-                if (J) (clearTimeout(J), (J = void 0));
-              },
-            ));
-        },
-      },
-    );
 }

@@@ function 'pc4' (was 'Ng9') — structural (50.0%)
--- pretty-v2.1.31.js:293762
+++ pretty-v2.1.32.js:425262
@@ -1,3 +1,3 @@
 function Ng9() {
-  return Number(process.env.SLASH_COMMAND_TOOL_CHAR_BUDGET) || 15000;
+  return jG1.toolCallsBetweenUpdates;
 }

@@@ variable 'Q5q' (was 'z3q') — structural (50.0%)
--- pretty-v2.1.31.js:494154
+++ pretty-v2.1.32.js:493862
@@ -1,19 +1,15 @@
 var z3q = E(() => {
-  q3q();
-  ((KxA = o(J1(), 1)),
-    (ktY = {
-      type: "local-jsx",
-      name: "permissions",
-      aliases: ["allowed-tools"],
-      description: "Manage allow & deny tool permission rules",
-      isEnabled: () => !0,
-      isHidden: !1,
-      async call(A) {
-        return KxA.createElement(A3q, { onExit: A });
-      },
-      userFacingName() {
-        return "permissions";
-      },
-    }),
+  ((Q1z = {
+    type: "local-jsx",
+    name: "permissions",
+    aliases: ["allowed-tools"],
+    description: "Manage allow & deny tool permission rules",
+    isEnabled: () => !0,
+    isHidden: !1,
+    load: () => Promise.resolve().then(() => (m5q(), B5q)),
+    userFacingName() {
+      return "permissions";
+    },
+  }),
     (Y3q = ktY));
 });

@@@ variable 'I3q' (was 'wKq') — structural (48.9%)
--- pretty-v2.1.31.js:489355
+++ pretty-v2.1.32.js:489153
@@ -1,12 +1,5 @@
 var wKq = E(() => {
   p1();
-  u1();
-  fIA();
-  F8();
-  s6();
-  _6();
-  S8();
-  ((b2 = o(J1(), 1)), (xf6 = o(J1(), 1)));
   ((vsY = {
     type: "local-jsx",
     name: "session",
@@ -16,9 +9,7 @@
     get isHidden() {
       return !Rl1();
     },
-    async call(A) {
-      return b2.createElement(ZsY, { onDone: A });
-    },
+    load: () => Promise.resolve().then(() => (S3q(), C3q)),
     userFacingName() {
       return "session";
     },

@@@ variable 'R6q' (was 'W1q') — structural (48.9%)
--- pretty-v2.1.31.js:462081
+++ pretty-v2.1.32.js:462085
@@ -1,23 +1,15 @@
 var W1q = E(() => {
-  TZ6();
-  ((USA = o(J1(), 1)),
-    (tUY = {
-      aliases: ["settings"],
-      type: "local-jsx",
-      name: "config",
-      description: "Open config panel",
-      isEnabled: () => !0,
-      isHidden: !1,
-      async call(A, q) {
-        return USA.createElement(AG1, {
-          onClose: A,
-          context: q,
-          defaultTab: "Config",
-        });
-      },
-      userFacingName() {
-        return "config";
-      },
-    }),
+  ((edY = {
+    aliases: ["settings"],
+    type: "local-jsx",
+    name: "config",
+    description: "Open config panel",
+    isEnabled: () => !0,
+    isHidden: !1,
+    load: () => Promise.resolve().then(() => (k6q(), E6q)),
+    userFacingName() {
+      return "config";
+    },
+  }),
     (M1q = tUY));
 });

@@@ variable 'F2q' (was 'oYq') — structural (46.9%)
--- pretty-v2.1.31.js:509650
+++ pretty-v2.1.32.js:509277
@@ -1,18 +1,14 @@
 var oYq = E(() => {
-  nYq();
-  ((XbA = o(J1(), 1)),
-    (TAz = {
-      type: "local-jsx",
-      name: "stats",
-      description: "Show your Claude Code usage statistics and activity",
-      isEnabled: () => !0,
-      isHidden: !1,
-      async call(A, q, K) {
-        return XbA.createElement(dYq, { onClose: A });
-      },
-      userFacingName() {
-        return "stats";
-      },
-    }),
+  ((Q7z = {
+    type: "local-jsx",
+    name: "stats",
+    description: "Show your Claude Code usage statistics and activity",
+    isEnabled: () => !0,
+    isHidden: !1,
+    load: () => Promise.resolve().then(() => (B2q(), u2q)),
+    userFacingName() {
+      return "stats";
+    },
+  }),
     (rYq = TAz));
 });

@@@ variable 'NAq' (was 'D6q') — structural (46.4%)
--- pretty-v2.1.31.js:465532
+++ pretty-v2.1.32.js:464977
@@ -1,30 +1,14 @@
 var D6q = E(() => {
-  mA();
-  N6();
-  sB();
-  tA();
-  h6();
-  $6q();
-  J6q();
-  u1();
-  S8();
-  u1();
-  vD();
-  Aq();
-  ((bv = o(J1(), 1)),
-    (KhA = o(J1(), 1)),
-    (bdY = {
-      type: "local-jsx",
-      name: "memory",
-      description: "Edit Claude memory files",
-      isEnabled: () => !0,
-      isHidden: !1,
-      async call(A) {
-        return bv.createElement(udY, { onDone: A });
-      },
-      userFacingName() {
-        return this.name;
-      },
-    }));
-  X6q = bdY;
+  ((FlY = {
+    type: "local-jsx",
+    name: "memory",
+    description: "Edit Claude memory files",
+    isEnabled: () => !0,
+    isHidden: !1,
+    load: () => Promise.resolve().then(() => (fAq(), ZAq)),
+    userFacingName() {
+      return this.name;
+    },
+  }),
+    (VAq = FlY));
 });

@@@ variable 'D5q' (was 'mKq') — structural (46.2%)
--- pretty-v2.1.31.js:492222
+++ pretty-v2.1.32.js:491918
@@ -1,21 +1,13 @@
 var mKq = E(() => {
-  TZ6();
-  ((sIA = o(J1(), 1)),
-    (BKq = {
-      type: "local-jsx",
-      name: "usage",
-      description: "Show plan usage limits",
-      isEnabled: () => !0,
-      isHidden: !1,
-      async call(A, q) {
-        return sIA.createElement(AG1, {
-          onClose: A,
-          context: q,
-          defaultTab: "Usage",
-        });
-      },
-      userFacingName() {
-        return "usage";
-      },
-    }));
+  X5q = {
+    type: "local-jsx",
+    name: "usage",
+    description: "Show plan usage limits",
+    isEnabled: () => !0,
+    isHidden: !1,
+    load: () => Promise.resolve().then(() => (J5q(), _5q)),
+    userFacingName() {
+      return "usage";
+    },
+  };
 });

@@@ variable 'X1q' (was 'wZ6') — structural (45.7%)
--- pretty-v2.1.31.js:457015
+++ pretty-v2.1.32.js:456864
@@ -1,17 +1,4 @@
 var wZ6 = E(() => {
-  j_();
-  gT();
-  vD();
-  s6();
-  Dd();
-  yq();
-  as();
-  tG();
-  rz();
-  KZ6();
-  xD();
-  gW();
-  Hu1();
   ((lgY = {
     type: "local",
     name: "clear",
@@ -20,9 +7,7 @@
     isEnabled: () => !0,
     isHidden: !1,
     supportsNonInteractive: !1,
-    async call(A, q) {
-      return (U4("clear"), await zZ6(q), { type: "text", value: "" });
-    },
+    load: () => Promise.resolve().then(() => (_1q(), $1q)),
     userFacingName() {
       return "clear";
     },

@@@ variable 'G5q' (was 'QKq') — structural (45.1%)
--- pretty-v2.1.31.js:492293
+++ pretty-v2.1.32.js:491994
@@ -1,21 +1,14 @@
 var QKq = E(() => {
-  p1();
-  u1();
-  GZ6();
-  DX();
-  ((Ed = o(J1(), 1)),
-    (osY = {
-      type: "local-jsx",
-      name: "theme",
-      description: "Change the theme",
-      isEnabled: () => !0,
-      isHidden: !1,
-      async call(A, q) {
-        return Ed.createElement(asY, { onDone: A });
-      },
-      userFacingName() {
-        return "theme";
-      },
-    }));
-  FKq = osY;
+  ((_1z = {
+    type: "local-jsx",
+    name: "theme",
+    description: "Change the theme",
+    isEnabled: () => !0,
+    isHidden: !1,
+    load: () => Promise.resolve().then(() => (M5q(), j5q)),
+    userFacingName() {
+      return "theme";
+    },
+  }),
+    (W5q = _1z));
 });

@@@ variable 'hAq' (was 'V6q') — structural (44.7%)
--- pretty-v2.1.31.js:466226
+++ pretty-v2.1.32.js:465659
@@ -1,18 +1,14 @@
 var V6q = E(() => {
-  Z6q();
-  ((whA = o(J1(), 1)),
-    (FdY = {
-      type: "local-jsx",
-      name: "help",
-      description: "Show help and available commands",
-      isEnabled: () => !0,
-      isHidden: !1,
-      async call(A, { options: { commands: q } }) {
-        return whA.createElement(G6q, { commands: q, onClose: A });
-      },
-      userFacingName() {
-        return "help";
-      },
-    }),
+  ((plY = {
+    type: "local-jsx",
+    name: "help",
+    description: "Show help and available commands",
+    isEnabled: () => !0,
+    isHidden: !1,
+    load: () => Promise.resolve().then(() => (CAq(), yAq)),
+    userFacingName() {
+      return "help";
+    },
+  }),
     (f6q = FdY));
 });

@@@ variable 'YAq' (was 'a1q') — structural (43.7%)
--- pretty-v2.1.31.js:465195
+++ pretty-v2.1.32.js:464618
@@ -1,21 +1,15 @@
 var a1q = E(() => {
-  aSA();
-  ((r1q = o(J1(), 1)),
-    (VdY = {
-      name: "doctor",
-      description:
-        "Diagnose and verify your Claude Code installation and settings",
-      isEnabled: () => !process.env.DISABLE_DOCTOR_COMMAND,
-      isHidden: !1,
-      userFacingName() {
-        return "doctor";
-      },
-      type: "local-jsx",
-      call(A, q, K) {
-        return new Promise((Y) =>
-          Y(r1q.default.createElement(SZ6, { onDone: A })),
-        );
-      },
-    }),
+  ((TlY = {
+    name: "doctor",
+    description:
+      "Diagnose and verify your Claude Code installation and settings",
+    isEnabled: () => !process.env.DISABLE_DOCTOR_COMMAND,
+    isHidden: !1,
+    userFacingName() {
+      return "doctor";
+    },
+    type: "local-jsx",
+    load: () => Promise.resolve().then(() => (qAq(), AAq)),
+  }),
     (o1q = VdY));
 });

@@@ function 'Z86' (was 'lA6') — structural (43.0%)
--- pretty-v2.1.31.js:146924
+++ pretty-v2.1.32.js:146848
@@ -1,11 +1,12 @@
 function lA6(A, q, K) {
-  (YE6(A, q, K),
-    WE6()?.add(A, { model: K }),
-    aY1()?.add(q.input_tokens, { type: "input", model: K }),
-    aY1()?.add(q.output_tokens, { type: "output", model: K }),
-    aY1()?.add(q.cache_read_input_tokens ?? 0, { type: "cacheRead", model: K }),
+  LE6(A, q, K);
+  let Y = { model: K };
+  (FE6()?.add(A, Y),
+    $z1()?.add(q.input_tokens, { ...Y, type: "input" }),
+    $z1()?.add(q.output_tokens, { ...Y, type: "output" }),
+    $z1()?.add(q.cache_read_input_tokens ?? 0, { ...Y, type: "cacheRead" }),
     aY1()?.add(q.cache_creation_input_tokens ?? 0, {
+      ...Y,
       type: "cacheCreation",
-      model: K,
     }));
 }

@@@ variable 'U27' (was 'O27') — structural (42.5%)
--- pretty-v2.1.31.js:147539
+++ pretty-v2.1.32.js:147501
@@ -1,11 +1,13 @@
-  O27 = () => {
-    let A = H4() !== "firstParty";
+  U27 = (A = !1) => {
+    let q = s7() !== "firstParty",
+      K = q ? "4.1" : "4.6",
+      Y = q ? V86 : T86(!1, A);
     return {
       value: "opus",
       label: A ? "Opus 4.1" : "Opus",
-      description: `Opus ${A ? "4.1" : "4.5"} · ${A ? "Legacy" : "Most capable for complex work"}${A ? "" : ` · ${Fi(A ? nA6 : PL1)}`}`,
+      description: `Opus ${K} · ${q ? "Legacy" : "Most capable for complex work"}${q ? "" : ` · ${Nb(Y)}`}`,
       descriptionForModel: A
         ? "Opus 4.1 - legacy version"
-        : "Opus 4.5 - most capable for complex work",
+        : "Opus 4.6 - most capable for complex work",
     };
   },

@@@ function 'vQY' (was 'RmY') — structural (42.0%)
--- pretty-v2.1.31.js:448416
+++ pretty-v2.1.32.js:448364
@@ -1,19 +1,23 @@
 async function RmY(A, q, K) {
   if (A.hook_event_name !== "PostToolUse") return {};
-  let Y = LmY(A.tool_name, A.tool_input);
-  if (Y === "session_memory") n("tengu_session_memory_accessed", {});
-  else if (Y === "session_transcript") n("tengu_transcript_accessed", {});
+  let Y = TQY(A.tool_name, A.tool_input),
+    z = n27(),
+    w = z ? { subagent_name: z } : {};
+  if (Y === "session_memory") c("tengu_session_memory_accessed", { ...w });
+  else if (Y === "session_transcript") c("tengu_transcript_accessed", { ...w });
   let z = kmY(A.tool_name, A.tool_input);
   if (z && bDA(z))
-    switch ((n("tengu_memdir_accessed", { tool: A.tool_name }), A.tool_name)) {
+    switch (
+      (c("tengu_memdir_accessed", { tool: A.tool_name, ...w }), A.tool_name)
+    ) {
       case Pq:
-        n("tengu_memdir_file_read", {});
+        c("tengu_memdir_file_read", { ...w });
         break;
       case pq:
-        n("tengu_memdir_file_edit", {});
+        c("tengu_memdir_file_edit", { ...w });
         break;
       case m5:
-        n("tengu_memdir_file_write", {});
+        c("tengu_memdir_file_write", { ...w });
         break;
     }
   return {};

@@@ function 'Ld4' (was 'bp4') — structural (41.6%)
--- pretty-v2.1.31.js:420865
+++ pretty-v2.1.32.js:420427
@@ -1,28 +1,25 @@
 function bp4(A, q, { verbose: K }) {
   let Y = typeof A === "string" ? OA(A) : A;
   if ("routing" in Y && Y.routing) {
-    let {
-      sender: z,
-      senderColor: w,
-      target: H,
-      targetColor: O,
-      summary: $,
-    } = Y.routing;
+    let { summary: z, content: w } = Y.routing;
+    if (K && w)
+      return oh.default.createElement(
+        HA,
+        null,
+        oh.default.createElement(f, null, w),
+      );
     return qR.default.createElement(
       h,
-      { marginTop: 1 },
-      qR.default.createElement(Z, { color: WJ(w) }, `@${z}`),
-      qR.default.createElement(Z, null, ` ${d1.pointerSmall} `),
-      qR.default.createElement(Z, { color: WJ(O) }, `${H}${d1.pointer}`),
-      qR.default.createElement(Z, null, " ", $),
+      null,
+      oh.default.createElement(f, null, z),
+      oh.default.createElement(f, null, " "),
+      oh.default.createElement(sT, null),
     );
   }
-  if ("request_id" in Y && "target" in Y)
-    return qR.default.createElement(
-      h,
-      { marginTop: 1 },
-      qR.default.createElement(Z, null, `@${Y.target}${d1.pointer}`),
-      qR.default.createElement(Z, null, " shutdown request sent"),
-    );
-  return qR.default.createElement(Z, { dimColor: !0 }, "  ", Y.message);
+  if ("request_id" in Y && "target" in Y) return null;
+  return oh.default.createElement(
+    HA,
+    null,
+    oh.default.createElement(f, { dimColor: !0 }, Y.message),
+  );
 }

@@@ variable 'A01' (was 'd_1') — structural (41.5%)
--- pretty-v2.1.31.js:193098
+++ pretty-v2.1.32.js:249593
@@ -1,9 +1,7 @@
 var d_1 = E(() => {
   _q6();
   n_();
+  z$1();
   ck = [];
-  ((aqA = new Intl.Segmenter(void 0, { granularity: "grapheme" })),
-    (Kl5 = new Intl.Segmenter(void 0, { granularity: "word" })),
-    (Yl5 = /^[\p{L}\p{N}\p{M}_]$/u),
-    ($C1 = /\s/));
+  ((VZ9 = /^[\p{L}\p{N}\p{M}_]$/u), (kI1 = /\s/));
 });

@@@ variable 'fbA' (was 'UxA') — structural (40.2%)
--- pretty-v2.1.31.js:505525
+++ pretty-v2.1.32.js:505143
@@ -1,10 +1,4 @@
 var UxA = E(() => {
-  A61();
-  Sw();
-  HG1();
-  i9q();
-  ((g1z = o(J1(), 1)),
-    (U1z = ["Goodbye!", "See ya!", "Bye!", "Catch you later!"]));
   ((d1z = {
     type: "local-jsx",
     name: "exit",
@@ -12,9 +6,7 @@
     description: "Exit the REPL",
     isEnabled: () => !0,
     isHidden: !1,
-    async call(A) {
-      return (A(p1z()), await ZK(0, "prompt_input_exit"), null);
-    },
+    load: () => Promise.resolve().then(() => (hzq(), Szq)),
     userFacingName() {
       return "exit";
     },

=== String Changes ===

@@@ class 'LNA' (was 'rVA') — string-only
--- pretty-v2.1.31.js:366434
+++ pretty-v2.1.32.js:366794
@@ -226,7 +226,7 @@
         K,
         "-h",
         "-p",
-        "70",
+        "70%",
         "-P",
         "-F",
         "#{pane_id}",

@@@ function 'Zu1' (was 'tb1') — string-only
--- pretty-v2.1.31.js:296565
+++ pretty-v2.1.32.js:298430
@@ -13,7 +13,7 @@
         ? `completed${Y !== void 0 ? ` (exit code ${Y})` : ""}`
         : K === "failed"
           ? `failed${Y !== void 0 ? ` with exit code ${Y}` : ""}`
-          : "was killed",
+          : "was stopped",
     O = Lw(A),
     $ = `<${F_}>
 <${rZ}>${A}</${rZ}>

@@@ function 'OuY' (was 'XxY') — string-only
--- pretty-v2.1.31.js:438816
+++ pretty-v2.1.32.js:438756
@@ -4,7 +4,7 @@
         ? "completed successfully"
         : K === "failed"
           ? "failed"
-          : "was killed",
+          : "was stopped",
     w = Lw(A),
     H = `<${F_}>
 <${rZ}>${A}</${rZ}>

@@@ function 'KT5' (was 'ZV5') — string-only
--- pretty-v2.1.31.js:147305
+++ pretty-v2.1.32.js:147253
@@ -1,4 +1,4 @@
 function ZV5(A) {
-  if (A === "opusplan") return "Opus 4.5 in plan mode, else Sonnet 4.5";
+  if (A === "opusplan") return "Opus 4.6 in plan mode, else Sonnet 4.5";
   return qG(c2(A));
 }

@@@ function 'C86' (was 'ZL1') — string-only
--- pretty-v2.1.31.js:147300
+++ pretty-v2.1.32.js:147248
@@ -1,5 +1,5 @@
 function ZL1() {
   if (fL1() || VL1() || aO1())
-    return "Opus 4.5 · Most capable for complex work";
+    return "Opus 4.6 · Most capable for complex work";
   return "Sonnet 4.5 · Best for everyday tasks";
 }

@@@ function 'Nf9' (was 'QYz') — string-only
--- pretty-v2.1.31.js:540162
+++ pretty-v2.1.32.js:252944
@@ -1,3 +1,3 @@
 function QYz(A) {
-  return A.type === "in_process_teammate";
+  return A.type === "image";
 }

@@@ function 'fz4' (was 'FRq') — string-only
--- pretty-v2.1.31.js:1817
+++ pretty-v2.1.32.js:302301
@@ -1,3 +1,3 @@
 function FRq(A) {
-  return A.toLowerCase().includes("claude-sonnet-4");
+  return A.toLowerCase().includes("opus-4-6");
 }

@@@ variable '$T5' (was 'vV5') — string-only
--- pretty-v2.1.31.js:147563
+++ pretty-v2.1.32.js:147528
@@ -2,6 +2,6 @@
     return {
       value: "opusplan",
       label: "Opus Plan Mode",
-      description: "Use Opus 4.5 in plan mode, Sonnet 4.5 otherwise",
+      description: "Use Opus 4.6 in plan mode, Sonnet 4.5 otherwise",
     };
   };

@@@ function 'u4z' (was 'Z8z') — string-only
--- pretty-v2.1.31.js:512322
+++ pretty-v2.1.32.js:511947
@@ -8,5 +8,5 @@
 - Hard-to-reverse operations: force-pushing (can also overwrite upstream), git reset --hard, amending published commits, removing or downgrading packages/dependencies, modifying CI/CD pipelines
 - Actions visible to others or that affect shared state: pushing code, creating/closing/commenting on PRs or issues, sending messages (Slack, email, GitHub), posting to external services, modifying shared infrastructure or permissions
 
-When you encounter an obstacle, do not use destructive actions as a shortcut to simply make it go away. For instance, try to identify root causes and fix underlying issues rather than bypassing safety checks (e.g. --no-verify). If you discover unexpected state like unfamiliar files, branches, or configuration, investigate before deleting or overwriting, as it may represent the user's in-progress work. For example, typically resolve merge conflicts rather than discarding changes. In short: only take risky actions carefully, and when in doubt, ask before acting. Follow both the spirit and letter of these instructions - measure twice, cut once.`;
+When you encounter an obstacle, do not use destructive actions as a shortcut to simply make it go away. For instance, try to identify root causes and fix underlying issues rather than bypassing safety checks (e.g. --no-verify). If you discover unexpected state like unfamiliar files, branches, or configuration, investigate before deleting or overwriting, as it may represent the user's in-progress work. For example, typically resolve merge conflicts rather than discarding changes; similarly, if a lock file exists, investigate what process holds it rather than deleting it. In short: only take risky actions carefully, and when in doubt, ask before acting. Follow both the spirit and letter of these instructions - measure twice, cut once.`;
 }
