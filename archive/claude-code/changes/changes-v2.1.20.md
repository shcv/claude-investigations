--- archive/claude-code/pretty/pretty-v2.1.19.js
+++ archive/claude-code/pretty/pretty-v2.1.20.js
Structural similarity: 96.4%
Matched: 13749/13895 vs 14262
Changes: 513 added, 146 removed, 941 structural, 38 string-only (12770 unchanged)

Filtered: 48 version bumps, 557 reformatting-only changes

=== Import Style Changes ===

"child_process":
  - import W6Y from "child_process";
  - import D6Y from "child_process";
  + import { execFile as wGq, spawn as HGq, spawnSync as JGq } from "child_process";
  + import { spawn as T25, spawnSync as v25 } from "child_process";
  + import { spawn as Is2 } from "child_process";

"https":
  - import Ds4 from "https";
  + import { Agent as hi3 } from "https";

"node:child_process":
  - import TC1 from "node:child_process";
  - import U67 from "node:child_process";
  + import { spawn as SS8, spawnSync as Hd1 } from "node:child_process";
  + import { execFile as i3Y, execFileSync as Umw } from "node:child_process";
  + import { execFileSync as sv2, spawn as tv2 } from "node:child_process";

"node:fs":
  - import T67 from "node:fs";
  - import S1Y from "node:fs";
  - import x1Y from "node:fs";
  + import {
  +   readFileSync as DD7,
  +   existsSync as MD7,
  +   mkdirSync as gCY,
  +   readdirSync as FCY,
  + } from "node:fs";
  + import {
  +   existsSync as $UA,
  +   statSync as gv2,
  +   mkdirSync as Fv2,
  +   realpathSync as Qv2,
  + } from "node:fs";
  + import {
  +   constants as nv2,
  +   readFileSync as rv2,
  +   existsSync as ov2,
  +   unlinkSync as av2,
  + } from "node:fs";

"node:os":
  - import b1Y from "node:os";
  + import { homedir as bXK } from "node:os";
  + import { homedir as M7z } from "node:os";

"node:path":
  - import Q67 from "node:path";
  + import {
  +   join as DX,
  +   dirname as xd,
  +   resolve as qm,
  +   delimiter as iS2,
  +   basename as nS2,
  + } from "node:path";

"node:process":
  - import QjK from "node:process";
  + import { cwd as m04 } from "node:process";

"node:util":
  - import mc9 from "node:util";
  + import { isDeepStrictEqual as GmK } from "node:util";

"stream":
  - import h2A from "stream";
  + import { PassThrough as w7z } from "stream";

=== Removed ===

--- Removed I1 (pretty-v2.1.19.js:5496-5504)
- var I1 = C(() => {
-   e1();
-   KfA();
-   e6();
-   r6();
-   F1();
-   RiA = [];
-   W2A = [];
- });

--- Removed hAA (pretty-v2.1.19.js:28980-29003)
- async function hAA(A) {
-   try {
-     let K = await IH5(A, "utf8");
-     if (!K.trim()) return [];
-     return (
-       (K = PzA(K)),
-       K.split(
-         `
- `,
-       )
-         .filter((q) => q.trim())
-         .map((q) => {
-           try {
-             return JSON.parse(q);
-           } catch (Y) {
-             return (qA(Error(`Error parsing line in ${A}: ${Y}`)), null);
-           }
-         })
-         .filter((q) => q !== null)
-     );
-   } catch (K) {
-     return (qA(Error(`Error opening file ${A}: ${K}`)), []);
-   }
- }

--- Removed B0 (pretty-v2.1.19.js:29027-29041)
- var B0 = C(() => {
-   I1();
-   _q8();
-   Q7();
-   F1();
-   S9 = w6((A, K = !0) => {
-     if (!A) return null;
-     try {
-       return JSON.parse(PzA(A));
-     } catch (q) {
-       if (K) qA(q);
-       return null;
-     }
-   });
- });

--- Removed Ik8 (pretty-v2.1.19.js:94090-94098)
- function Ik8() {
-   try {
-     return (
-       f1q("which", ["rg"], { stdio: "ignore", timeout: 1000 }).status === 0
-     );
-   } catch {
-     return !1;
-   }
- }

--- Removed xQ1 (pretty-v2.1.19.js:94312-94345)
- function xQ1(A) {
-   if (A) {
-     if (nvA.existsSync(A))
-       return (
-         C8(`[SeccompFilter] Using BPF filter from expected path: ${A}`),
-         A
-       );
-     C8(`[SeccompFilter] Expected path provided but file not found: ${A}`);
-   }
-   let K = uk8();
-   if (!K)
-     return (
-       C8(
-         `[SeccompFilter] Cannot find pre-generated BPF filter: unsupported architecture ${process.arch}`,
-       ),
-       null
-     );
-   C8(`[SeccompFilter] Detected architecture: ${K}`);
-   let q = xk8(Bk8(import.meta.url)),
-     Y = Ul("vendor", "seccomp", K, "unix-block.bpf"),
-     z = [Ul(q, Y), Ul(q, "..", "..", Y), Ul(q, "..", Y)];
-   for (let w of z)
-     if (nvA.existsSync(w))
-       return (
-         C8(`[SeccompFilter] Found pre-generated BPF filter: ${w} (${K})`),
-         w
-       );
-   return (
-     C8(
-       `[SeccompFilter] Pre-generated BPF filter not found in any expected location (${K})`,
-     ),
-     null
-   );
- }

--- Removed ttA (pretty-v2.1.19.js:94346-94378)
- function ttA(A) {
-   if (A) {
-     if (nvA.existsSync(A))
-       return (
-         C8(
-           `[SeccompFilter] Using apply-seccomp binary from expected path: ${A}`,
-         ),
-         A
-       );
-     C8(`[SeccompFilter] Expected path provided but file not found: ${A}`);
-   }
-   let K = uk8();
-   if (!K)
-     return (
-       C8(
-         `[SeccompFilter] Cannot find apply-seccomp binary: unsupported architecture ${process.arch}`,
-       ),
-       null
-     );
-   C8(`[SeccompFilter] Looking for apply-seccomp binary for architecture: ${K}`);
-   let q = xk8(Bk8(import.meta.url)),
-     Y = Ul("vendor", "seccomp", K, "apply-seccomp"),
-     z = [Ul(q, Y), Ul(q, "..", "..", Y), Ul(q, "..", Y)];
-   for (let w of z)
-     if (nvA.existsSync(w))
-       return (C8(`[SeccompFilter] Found apply-seccomp binary: ${w} (${K})`), w);
-   return (
-     C8(
-       `[SeccompFilter] apply-seccomp binary not found in any expected location (${K})`,
-     ),
-     null
-   );
- }

--- Removed wC8 (pretty-v2.1.19.js:95464-95475)
- function wC8(A) {
-   if (!zC8()) return !1;
-   if ((A ?? Lq?.ripgrep)?.command === void 0) {
-     if (!Ik8()) return !1;
-   }
-   if (QN() === "linux") {
-     let z = Lq?.network?.allowAllUnixSockets ?? !1,
-       w = Lq?.seccomp;
-     return dk8(z, w);
-   }
-   return !0;
- }

--- Removed Bq4 (pretty-v2.1.19.js:158762-158946)
- var Bq4 = C(() => {
-   bq4 = `Use this tool to create and manage a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user.
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
- * Uses the ${c5} tool to add a comment to the calculateTotal function *
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

--- Removed tj (pretty-v2.1.19.js:159150-159152)
- function tj() {
-   return process.env.CLAUDE_CODE_TASK_LIST_ID || j9() || n1();
- }

--- Removed n16 (pretty-v2.1.19.js:159159-159161)
- function n16(A, K) {
-   return Z71(lb(A), `${Kn(K)}.json`);
- }

--- Removed Cg3 (pretty-v2.1.19.js:171629-171632)
-   Cg3 = () => {
-     if (x66 === void 0) throw Error("Yoga not loaded");
-     return x66;
-   },

--- Removed m71 (pretty-v2.1.19.js:171734-171745)
- var m71 = C(() => {
-   O8A();
-   S34();
-   I71();
-   L66();
-   Q7();
-   G94();
-   b66();
-   W94 = w6(async () => {
-     x66 = await f34();
-   });
- });

--- Removed gg3 (pretty-v2.1.19.js:171869-171878)
-   gg3 = (A, K = {}) => {
-     (Ig3(A, K),
-       Sg3(A, K),
-       hg3(A, K),
-       bg3(A, K),
-       xg3(A, K),
-       Bg3(A, K),
-       ug3(A, K),
-       mg3(A, K));
-   },

--- Removed Bz9 (pretty-v2.1.19.js:197086-197104)
- function Bz9(A) {
-   if (A.option.type === "input") return null;
-   return a7.default.createElement(
-     f,
-     {
-       key: String(A.option.value),
-       wrap: "wrap-trim",
-       dimColor: A.isOptionDisabled || A.option.dimDescription !== !1,
-       color: A.isOptionDisabled
-         ? void 0
-         : A.isSelected
-           ? "success"
-           : A.isFocused
-             ? "suggestion"
-             : void 0,
-     },
-     a7.default.createElement(t3, null, A.option.description || ""),
-   );
- }

--- Removed AH1 (pretty-v2.1.19.js:268980-268989)
- function AH1(A) {
-   let K = A.filter(eV);
-   if (K.length === 0) return V47;
-   let q = K.map((Y) => Y.name).join(`
- `);
-   return `${V47}
- 
- Available deferred tools (must be loaded before use):
- ${q}`;
- }

--- Removed VO6 (pretty-v2.1.19.js:270472-270669)
- function VO6(A) {
-   if (!A || A.trim() === "")
-     return `Your task is to create a detailed summary of the conversation so far, paying close attention to the user's explicit requests and your previous actions.
- This summary should be thorough in capturing technical details, code patterns, and architectural decisions that would be essential for continuing development work without losing context.
- 
- Before providing your final summary, wrap your analysis in <analysis> tags to organize your thoughts and ensure you've covered all necessary points. In your analysis process:
- 
- 1. Chronologically analyze each message and section of the conversation. For each section thoroughly identify:
-    - The user's explicit requests and intents
-    - Your approach to addressing the user's requests
-    - Key decisions, technical concepts and code patterns
-    - Specific details like:
-      - file names
-      - full code snippets
-      - function signatures
-      - file edits
-   - Errors that you ran into and how you fixed them
-   - Pay special attention to specific user feedback that you received, especially if the user told you to do something differently.
- 2. Double-check for technical accuracy and completeness, addressing each required element thoroughly.
- 
- Your summary should include the following sections:
- 
- 1. Primary Request and Intent: Capture all of the user's explicit requests and intents in detail
- 2. Key Technical Concepts: List all important technical concepts, technologies, and frameworks discussed.
- 3. Files and Code Sections: Enumerate specific files and code sections examined, modified, or created. Pay special attention to the most recent messages and include full code snippets where applicable and include a summary of why this file read or edit is important.
- 4. Errors and fixes: List all errors that you ran into, and how you fixed them. Pay special attention to specific user feedback that you received, especially if the user told you to do something differently.
- 5. Problem Solving: Document problems solved and any ongoing troubleshooting efforts.
- 6. All user messages: List ALL user messages that are not tool results. These are critical for understanding the users' feedback and changing intent.
- 6. Pending Tasks: Outline any pending tasks that you have explicitly been asked to work on.
- 7. Current Work: Describe in detail precisely what was being worked on immediately before this summary request, paying special attention to the most recent messages from both user and assistant. Include file names and code snippets where applicable.
- 8. Optional Next Step: List the next step that you will take that is related to the most recent work you were doing. IMPORTANT: ensure that this step is DIRECTLY in line with the user's most recent explicit requests, and the task you were working on immediately before this summary request. If your last task was concluded, then only list next steps if they are explicitly in line with the users request. Do not start on tangential requests or really old requests that were already completed without confirming with the user first.
-                        If there is a next step, include direct quotes from the most recent conversation showing exactly what task you were working on and where you left off. This should be verbatim to ensure there's no drift in task interpretation.
- 
- Here's an example of how your output should be structured:
- 
- <example>
- <analysis>
- [Your thought process, ensuring all points are covered thoroughly and accurately]
- </analysis>
- 
- <summary>
- 1. Primary Request and Intent:
-    [Detailed description]
- 
- 2. Key Technical Concepts:
-    - [Concept 1]
-    - [Concept 2]
-    - [...]
- 
- 3. Files and Code Sections:
-    - [File Name 1]
-       - [Summary of why this file is important]
-       - [Summary of the changes made to this file, if any]
-       - [Important Code Snippet]
-    - [File Name 2]
-       - [Important Code Snippet]
-    - [...]
- 
- 4. Errors and fixes:
-     - [Detailed description of error 1]:
-       - [How you fixed the error]
-       - [User feedback on the error if any]
-     - [...]
- 
- 5. Problem Solving:
-    [Description of solved problems and ongoing troubleshooting]
- 
- 6. All user messages: 
-     - [Detailed non tool use user message]
-     - [...]
- 
- 7. Pending Tasks:
-    - [Task 1]
-    - [Task 2]
-    - [...]
- 
- 8. Current Work:
-    [Precise description of current work]
- 
- 9. Optional Next Step:
-    [Optional Next step to take]
- 
- </summary>
- </example>
- 
- Please provide your summary based on the conversation so far, following this structure and ensuring precision and thoroughness in your response. 
- 
- There may be additional summarization instructions provided in the included context. If so, remember to follow these instructions when creating the above summary. Examples of instructions include:
- <example>
- ## Compact Instructions
- When summarizing the conversation focus on typescript code changes and also remember the mistakes you made and how you fixed them.
- </example>
- 
- <example>
- # Summary instructions
- When you are using compact - please focus on test output and code changes. Include file reads verbatim.
- </example>
- `;
-   return `Your task is to create a detailed summary of the conversation so far, paying close attention to the user's explicit requests and your previous actions.
- This summary should be thorough in capturing technical details, code patterns, and architectural decisions that would be essential for continuing development work without losing context.
- 
- Before providing your final summary, wrap your analysis in <analysis> tags to organize your thoughts and ensure you've covered all necessary points. In your analysis process:
- 
- 1. Chronologically analyze each message and section of the conversation. For each section thoroughly identify:
-    - The user's explicit requests and intents
-    - Your approach to addressing the user's requests
-    - Key decisions, technical concepts and code patterns
-    - Specific details like:
-      - file names
-      - full code snippets
-      - function signatures
-      - file edits
-   - Errors that you ran into and how you fixed them
-   - Pay special attention to specific user feedback that you received, especially if the user told you to do something differently.
- 2. Double-check for technical accuracy and completeness, addressing each required element thoroughly.
- 
- Your summary should include the following sections:
- 
- 1. Primary Request and Intent: Capture all of the user's explicit requests and intents in detail
- 2. Key Technical Concepts: List all important technical concepts, technologies, and frameworks discussed.
- 3. Files and Code Sections: Enumerate specific files and code sections examined, modified, or created. Pay special attention to the most recent messages and include full code snippets where applicable and include a summary of why this file read or edit is important.
- 4. Errors and fixes: List all errors that you ran into, and how you fixed them. Pay special attention to specific user feedback that you received, especially if the user told you to do something differently.
- 5. Problem Solving: Document problems solved and any ongoing troubleshooting efforts.
- 6. All user messages: List ALL user messages that are not tool results. These are critical for understanding the users' feedback and changing intent.
- 6. Pending Tasks: Outline any pending tasks that you have explicitly been asked to work on.
- 7. Current Work: Describe in detail precisely what was being worked on immediately before this summary request, paying special attention to the most recent messages from both user and assistant. Include file names and code snippets where applicable.
- 8. Optional Next Step: List the next step that you will take that is related to the most recent work you were doing. IMPORTANT: ensure that this step is DIRECTLY in line with the user's most recent explicit requests, and the task you were working on immediately before this summary request. If your last task was concluded, then only list next steps if they are explicitly in line with the users request. Do not start on tangential requests or really old requests that were already completed without confirming with the user first.
-                        If there is a next step, include direct quotes from the most recent conversation showing exactly what task you were working on and where you left off. This should be verbatim to ensure there's no drift in task interpretation.
- 
- Here's an example of how your output should be structured:
- 
- <example>
- <analysis>
- [Your thought process, ensuring all points are covered thoroughly and accurately]
- </analysis>
- 
- <summary>
- 1. Primary Request and Intent:
-    [Detailed description]
- 
- 2. Key Technical Concepts:
-    - [Concept 1]
-    - [Concept 2]
-    - [...]
- 
- 3. Files and Code Sections:
-    - [File Name 1]
-       - [Summary of why this file is important]
-       - [Summary of the changes made to this file, if any]
-       - [Important Code Snippet]
-    - [File Name 2]
-       - [Important Code Snippet]
-    - [...]
- 
- 4. Errors and fixes:
-     - [Detailed description of error 1]:
-       - [How you fixed the error]
-       - [User feedback on the error if any]
-     - [...]
- 
- 5. Problem Solving:
-    [Description of solved problems and ongoing troubleshooting]
- 
- 6. All user messages: 
-     - [Detailed non tool use user message]
-     - [...]
- 
- 7. Pending Tasks:
-    - [Task 1]
-    - [Task 2]
-    - [...]
- 
- 8. Current Work:
-    [Precise description of current work]
- 
- 9. Optional Next Step:
-    [Optional Next step to take]
- 
- </summary>
- </example>
- 
- Please provide your summary based on the conversation so far, following this structure and ensuring precision and thoroughness in your response. 
- 
- There may be additional summarization instructions provided in the included context. If so, remember to follow these instructions when creating the above summary. Examples of instructions include:
- <example>
- ## Compact Instructions
- When summarizing the conversation focus on typescript code changes and also remember the mistakes you made and how you fixed them.
- </example>
- 
- <example>
- # Summary instructions
- When you are using compact - please focus on test output and code changes. Include file reads verbatim.
- </example>
- 
- 
- Additional Instructions:
- ${A}`;
- }

--- Removed s47 (pretty-v2.1.19.js:270818-270838)
- function s47(A) {
-   let { matches: K } = A;
-   if (K.length === 0)
-     return RM.createElement(
-       v6,
-       null,
-       RM.createElement(f, { dimColor: !0 }, "No matching deferred tools found"),
-     );
-   return RM.createElement(
-     v6,
-     null,
-     RM.createElement(
-       f,
-       null,
-       "Found ",
-       RM.createElement(f, { bold: !0 }, K.length),
-       " ",
-       K.length === 1 ? "tool" : "tools",
-     ),
-   );
- }

--- Removed c_7 (pretty-v2.1.19.js:313311-313321)
- function c_7(A, K, q, Y = 4) {
-   let w = (A.split(K)[0] ?? "").split(/\r?\n/).length - 1,
-     H = GO1(A, K, q).split(/\r?\n/),
-     J = Math.max(0, w - Y),
-     X = w + Y + q.split(/\r?\n/).length;
-   return {
-     snippet: H.slice(J, X).join(`
- `),
-     startLine: J + 1,
-   };
- }

--- Removed hZ1 (pretty-v2.1.19.js:363130-363132)
- function hZ1(A, K) {
-   return parseInt(A.id, 10) - parseInt(K.id, 10);
- }

--- Removed _m7 (pretty-v2.1.19.js:372885-372887)
- function _m7(A, K) {
-   $m7.set(A, K);
- }

--- Removed GU7 (pretty-v2.1.19.js:384591-384973)
- function GU7({ attachment: A, addMargin: K, verbose: q }) {
-   let [{ tasks: Y }] = j6();
-   if (P8() && A.type === "teammate_mailbox") {
-     let z = A.messages.filter((w) => {
-       try {
-         return _6(w.text)?.type !== "idle_notification";
-       } catch {
-         return !0;
-       }
-     });
-     if (z.length === 0) return null;
-     return S7.default.createElement(
-       I,
-       { flexDirection: "column" },
-       S7.default.createElement(
-         M0,
-         { dimColor: !1 },
-         S7.default.createElement(
-           f,
-           { bold: !0 },
-           z.length,
-           " message",
-           z.length !== 1 ? "s" : "",
-           " in mailbox:",
-         ),
-       ),
-       z.map((w, H) => {
-         let J = null;
-         try {
-           J = _6(w.text);
-         } catch {}
-         if (J?.type === "task_assignment")
-           return S7.default.createElement(
-             I,
-             { key: H, paddingLeft: 2 },
-             S7.default.createElement(f, null, "● "),
-             S7.default.createElement(f, null, "Task assigned: "),
-             S7.default.createElement(f, { bold: !0 }, "#", J.taskId),
-             S7.default.createElement(f, null, " - ", J.subject),
-             S7.default.createElement(
-               f,
-               { dimColor: !0 },
-               " (from ",
-               J.assignedBy || w.from,
-               ")",
-             ),
-           );
-         let X = UG1(w.text, w.from);
-         if (X)
-           return S7.default.createElement(S7.default.Fragment, { key: H }, X);
-         let O = sT(w.color),
-           $ = pG1(w.text) ?? w.text;
-         return S7.default.createElement(
-           I,
-           { key: H, flexDirection: "column", paddingLeft: 5 },
-           S7.default.createElement(
-             f,
-             { color: O },
-             "● ",
-             S7.default.createElement(f, { bold: !0 }, w.from),
-           ),
-           S7.default.createElement(
-             I,
-             { paddingLeft: 5 },
-             S7.default.createElement(f, null, $),
-           ),
-         );
-       }),
-     );
-   }
-   switch (A.type) {
-     case "directory":
-       return S7.default.createElement(
-         M0,
-         null,
-         "Listed directory",
-         " ",
-         S7.default.createElement(f, { bold: !0 }, fqA(m1(), A.path) + e12),
-       );
-     case "file":
-     case "already_read_file":
-       if (A.content.type === "notebook")
-         return S7.default.createElement(
-           M0,
-           null,
-           "Read ",
-           S7.default.createElement(f, { bold: !0 }, fqA(m1(), A.filename)),
-           " (",
-           A.content.file.cells.length,
-           " cells)",
-         );
-       return S7.default.createElement(
-         M0,
-         null,
-         "Read ",
-         S7.default.createElement(f, { bold: !0 }, fqA(m1(), A.filename)),
-         " (",
-         A.content.type === "text"
-           ? `${A.content.file.numLines}${A.truncated ? "+" : ""} lines`
-           : IX(A.content.file.originalSize),
-         ")",
-       );
-     case "compact_file_reference":
-       return S7.default.createElement(
-         M0,
-         null,
-         "Referenced file",
-         " ",
-         S7.default.createElement(f, { bold: !0 }, fqA(m1(), A.filename)),
-       );
-     case "selected_lines_in_ide":
-       return S7.default.createElement(
-         M0,
-         null,
-         "⧉ Selected",
-         " ",
-         S7.default.createElement(f, { bold: !0 }, A.lineEnd - A.lineStart + 1),
-         " ",
-         "lines from ",
-         S7.default.createElement(f, { bold: !0 }, fqA(m1(), A.filename)),
-         " ",
-         "in ",
-         A.ideName,
-       );
-     case "nested_memory":
-       return S7.default.createElement(
-         M0,
-         null,
-         "Loaded ",
-         S7.default.createElement(f, { bold: !0 }, fqA(m1(), A.path)),
-       );
-     case "dynamic_skill": {
-       let z = fqA(m1(), A.skillDir),
-         w = A.skillNames.length;
-       return S7.default.createElement(
-         M0,
-         null,
-         "Loaded",
-         " ",
-         S7.default.createElement(
-           f,
-           { bold: !0 },
-           w,
-           " skill",
-           w !== 1 ? "s" : "",
-         ),
-         " ",
-         "from ",
-         S7.default.createElement(f, { bold: !0 }, z),
-       );
-     }
-     case "queued_command": {
-       let z = typeof A.prompt === "string" ? A.prompt : NqA(A.prompt) || "",
-         w = A.imagePasteIds && A.imagePasteIds.length > 0;
-       return S7.default.createElement(
-         I,
-         { flexDirection: "column" },
-         S7.default.createElement(PqA, {
-           addMargin: K,
-           param: { text: z, type: "text" },
-           verbose: q,
-         }),
-         w &&
-           A.imagePasteIds?.map((H) =>
-             S7.default.createElement(rG1, { key: H, imageId: H }),
-           ),
-       );
-     }
-     case "todo":
-       if (A.context === "post-compact")
-         return S7.default.createElement(
-           M0,
-           null,
-           "Todo list read (",
-           A.itemCount,
-           " ",
-           A.itemCount === 1 ? "item" : "items",
-           ")",
-         );
-       return null;
-     case "plan_file_reference":
-       return S7.default.createElement(
-         M0,
-         null,
-         "Plan file referenced (",
-         fq(A.planFilePath),
-         ")",
-       );
-     case "invoked_skills": {
-       if (A.skills.length === 0) return null;
-       let z = A.skills.map((w) => w.name).join(", ");
-       return S7.default.createElement(M0, null, "Skills restored (", z, ")");
-     }
-     case "diagnostics":
-       return S7.default.createElement(_U7, { attachment: A, verbose: q });
-     case "mcp_resource":
-       return S7.default.createElement(
-         M0,
-         null,
-         "Read MCP resource ",
-         S7.default.createElement(f, { bold: !0 }, A.name),
-         " from",
-         " ",
-         A.server,
-       );
-     case "command_permissions":
-       return null;
-     case "async_hook_response": {
-       if (A.hookEvent === "SessionStart" && !q) return null;
-       let z = A.response;
-       return S7.default.createElement(
-         M0,
-         null,
-         "Async hook ",
-         S7.default.createElement(f, { bold: !0 }, A.hookEvent),
-         " completed",
-         q &&
-           S7.default.createElement(
-             S7.default.Fragment,
-             null,
-             ":",
-             `
- `,
-             z.systemMessage
-               ? z.systemMessage
-               : z.hookSpecificOutput &&
-                   "additionalContext" in z.hookSpecificOutput &&
-                   z.hookSpecificOutput.additionalContext
-                 ? z.hookSpecificOutput.additionalContext
-                 : null,
-           ),
-       );
-     }
-     case "hook_blocking_error": {
-       if (A.hookEvent === "Stop" || A.hookEvent === "SubagentStop") return null;
-       if (q)
-         return S7.default.createElement(
-           M0,
-           { color: "error" },
-           A.hookName,
-           " hook returned blocking error:",
-           " ",
-           A.blockingError.blockingError,
-         );
-       return S7.default.createElement(
-         M0,
-         { color: "error" },
-         A.hookName,
-         " hook returned blocking error",
-       );
-     }
-     case "hook_non_blocking_error": {
-       if (A.hookEvent === "Stop" || A.hookEvent === "SubagentStop") return null;
-       if (q)
-         return S7.default.createElement(
-           M0,
-           { color: "error" },
-           A.hookName,
-           " hook error: ",
-           A.stderr,
-         );
-       return S7.default.createElement(
-         M0,
-         { color: "error" },
-         A.hookName,
-         " hook error",
-       );
-     }
-     case "hook_error_during_execution":
-       if (A.hookEvent === "Stop" || A.hookEvent === "SubagentStop") return null;
-       if (q)
-         return S7.default.createElement(
-           M0,
-           null,
-           A.hookName,
-           " hook warning: ",
-           A.content,
-         );
-       return S7.default.createElement(M0, null, A.hookName, " hook warning");
-     case "hook_success":
-       if (A.hookEvent === "Stop" || A.hookEvent === "SubagentStop") return null;
-       if (q)
-         return S7.default.createElement(
-           M0,
-           null,
-           A.hookName,
-           " hook succeeded",
-           A.content ? `: ${A.content}` : "",
-         );
-       return null;
-     case "hook_stopped_continuation":
-       if (A.hookEvent === "Stop" || A.hookEvent === "SubagentStop") return null;
-       return S7.default.createElement(
-         M0,
-         { color: "warning" },
-         A.hookName,
-         " hook stopped continuation: ",
-         A.message,
-       );
-     case "hook_system_message":
-       return S7.default.createElement(
-         M0,
-         null,
-         A.hookName,
-         " says: ",
-         A.content,
-       );
-     case "hook_permission_decision": {
-       let z = A.decision === "allow" ? "Allowed" : "Denied";
-       return S7.default.createElement(
-         M0,
-         null,
-         z,
-         " by ",
-         S7.default.createElement(f, { bold: !0 }, A.hookEvent),
-         " hook",
-       );
-     }
-     case "task_status": {
-       if (P8()) {
-         let w = Y[A.taskId];
-         if (
-           A.taskType === "in_process_teammate" &&
-           w?.type === "in_process_teammate"
-         ) {
-           let H = sT(w.identity.color),
-             J = A.status === "completed" ? "shut down gracefully" : A.status;
-           return S7.default.createElement(
-             I,
-             { flexDirection: "row", width: "100%", marginTop: 1 },
-             S7.default.createElement(f, { color: H }, mY, " "),
-             S7.default.createElement(
-               f,
-               { dimColor: !0 },
-               "Teammate ",
-               S7.default.createElement(f, { bold: !0 }, w.identity.agentName),
-               " ",
-               J,
-             ),
-           );
-         }
-       }
-       let z = A.status === "completed" ? "completed in background" : A.status;
-       return S7.default.createElement(
-         I,
-         { flexDirection: "row", width: "100%", marginTop: 1 },
-         S7.default.createElement(f, { dimColor: !0 }, mY, " "),
-         S7.default.createElement(
-           f,
-           { dimColor: !0 },
-           'Task "',
-           S7.default.createElement(f, { bold: !0 }, A.description),
-           '"',
-           " ",
-           z,
-         ),
-       );
-     }
-     case "task_progress":
-       return null;
-     case "agent_mention":
-     case "budget_usd":
-     case "critical_system_reminder":
-     case "delegate_mode":
-     case "delegate_mode_exit":
-     case "edited_image_file":
-     case "edited_text_file":
-     case "hook_additional_context":
-     case "hook_cancelled":
-     case "memory":
-     case "opened_file_in_ide":
-     case "output_style":
-     case "plan_mode":
-     case "plan_mode_exit":
-     case "plan_mode_reentry":
-     case "structured_output":
-     case "team_context":
-     case "todo_reminder":
-     case "ultramemory":
-     case "token_usage":
-       return null;
-   }
- }

--- Removed SU7 (pretty-v2.1.19.js:385596-385604)
- function SU7(A, K, q) {
-   return A;
-   function H() {
-     if (z.messages.length === 0) return;
-     Y.push(D62(z));
-     for (let J of w) Y.push(J);
-     ((w = []), (z = CU7()));
-   }
- }

--- Removed sU7 (pretty-v2.1.19.js:387499-387513)
- function sU7(A) {
-   let K = oU7.sep + A.split(g62).join(oU7.sep).replace(/^\/+/, ""),
-     q = u62(A).toLowerCase(),
-     Y = m62(A).toLowerCase();
-   if (F62.has(q)) return !0;
-   if (aU7.has(Y)) return !0;
-   let z = q.split(".");
-   if (z.length > 2) {
-     let w = "." + z.slice(-2).join(".");
-     if (aU7.has(w)) return !0;
-   }
-   for (let w of Q62) if (K.includes(w)) return !0;
-   for (let w of U62) if (w.test(q)) return !0;
-   return !1;
- }

--- Removed tU7 (pretty-v2.1.19.js:387515-387579)
- var tU7 = C(() => {
-   ((F62 = new Set([
-     "package-lock.json",
-     "yarn.lock",
-     "pnpm-lock.yaml",
-     "bun.lockb",
-     "bun.lock",
-     "composer.lock",
-     "gemfile.lock",
-     "cargo.lock",
-     "poetry.lock",
-     "pipfile.lock",
-     "shrinkwrap.json",
-     "npm-shrinkwrap.json",
-   ])),
-     (aU7 = new Set([
-       ".lock",
-       ".min.js",
-       ".min.css",
-       ".min.html",
-       ".bundle.js",
-       ".bundle.css",
-       ".generated.ts",
-       ".generated.js",
-       ".d.ts",
-     ])),
-     (Q62 = [
-       "/dist/",
-       "/build/",
-       "/out/",
-       "/output/",
-       "/node_modules/",
-       "/vendor/",
-       "/vendored/",
-       "/third_party/",
-       "/third-party/",
-       "/external/",
-       "/.next/",
-       "/.nuxt/",
-       "/.svelte-kit/",
-       "/coverage/",
-       "/__pycache__/",
-       "/.tox/",
-       "/venv/",
-       "/.venv/",
-       "/target/release/",
-       "/target/debug/",
-     ]),
-     (U62 = [
-       /^.*\.min\.[a-z]+$/i,
-       /^.*-min\.[a-z]+$/i,
-       /^.*\.bundle\.[a-z]+$/i,
-       /^.*\.generated\.[a-z]+$/i,
-       /^.*\.gen\.[a-z]+$/i,
-       /^.*\.auto\.[a-z]+$/i,
-       /^.*_generated\.[a-z]+$/i,
-       /^.*_gen\.[a-z]+$/i,
-       /^.*\.pb\.(go|js|ts|py|rb)$/i,
-       /^.*_pb2?\.py$/i,
-       /^.*\.pb\.h$/i,
-       /^.*\.grpc\.[a-z]+$/i,
-       /^.*\.swagger\.[a-z]+$/i,
-       /^.*\.openapi\.[a-z]+$/i,
-     ]));
- });

--- Removed Yp7 (pretty-v2.1.19.js:387593-387603)
- function Yp7(A) {
-   if (A.includes("opus-4-5")) return "claude-opus-4-5";
-   if (A.includes("opus-4-1")) return "claude-opus-4-1";
-   if (A.includes("opus-4")) return "claude-opus-4";
-   if (A.includes("sonnet-4-5")) return "claude-sonnet-4-5";
-   if (A.includes("sonnet-4")) return "claude-sonnet-4";
-   if (A.includes("sonnet-3-7")) return "claude-sonnet-3-7";
-   if (A.includes("haiku-4-5")) return "claude-haiku-4-5";
-   if (A.includes("haiku-3-5")) return "claude-haiku-3-5";
-   return "claude";
- }

--- Removed wW1 (pretty-v2.1.19.js:387613-387628)
- function wW1(A) {
-   let K = hA(),
-     q = t6();
-   if (!Kp7(A)) return A;
-   let Y = A,
-     z = q;
-   try {
-     Y = K.realpathSync(A);
-   } catch {}
-   try {
-     z = K.realpathSync(q);
-   } catch {}
-   if (Y.startsWith(z + "/") || Y === z) return eU7(z, Y);
-   if (A.startsWith(q + "/") || A === q) return eU7(q, A);
-   return A;
- }

--- Removed i62 (pretty-v2.1.19.js:387629-387632)
- function i62(A) {
-   if (Kp7(A)) return A;
-   return Uv6(t6(), A);
- }

--- Removed JW1 (pretty-v2.1.19.js:387647-387679)
- function JW1(A, K, q, Y, z) {
-   let w = wW1(K),
-     H = hA(),
-     J = i62(w);
-   try {
-     let X;
-     if (z) X = Math.max(0, Y.length - q.length);
-     else if (q === "") X = Y.length;
-     else {
-       X = Math.max(0, Y.length - q.length);
-       let W = Math.abs(Y.length - q.length);
-       X = Math.max(X, W);
-     }
-     let $ = A.fileStates.get(w)?.claudeContribution ?? 0,
-       _;
-     try {
-       _ = H.statSync(J).mtimeMs;
-     } catch {
-       _ = Date.now();
-     }
-     let Z = { contentHash: l62(Y), claudeContribution: $ + X, mtime: _ },
-       G = new Map(A.fileStates);
-     return (
-       G.set(w, Z),
-       h(
-         `Attribution: Tracked ${X} chars for ${w} (total: ${Z.claudeContribution})`,
-       ),
-       { ...A, fileStates: G }
-     );
-   } catch (X) {
-     return (qA(X), A);
-   }
- }

--- Removed zp7 (pretty-v2.1.19.js:387680-387682)
- function zp7(A, K, q) {
-   return JW1(A, K, "", q, !1);
- }

--- Removed wp7 (pretty-v2.1.19.js:387683-387697)
- function wp7(A, K, q) {
-   let Y = wW1(K),
-     w = A.fileStates.get(Y)?.claudeContribution ?? 0,
-     H = q.length,
-     J = w + H,
-     X = { contentHash: "", claudeContribution: J, mtime: Date.now() },
-     O = new Map(A.fileStates);
-   return (
-     O.set(Y, X),
-     h(
-       `Attribution: Tracked deletion of ${Y} (${H} chars removed, total contribution: ${J})`,
-     ),
-     { ...A, fileStates: O }
-   );
- }

--- Removed dv6 (pretty-v2.1.19.js:387698-387806)
- async function dv6(A, K) {
-   let q = hA(),
-     Y = t6(),
-     z = n1(),
-     w = {},
-     H = [],
-     J = new Set(),
-     X = {},
-     O = 0,
-     $ = 0,
-     _ = new Map(),
-     Z = new Map();
-   for (let M of A) {
-     J.add(M.surface);
-     let P =
-       M.sessionBaselines instanceof Map
-         ? M.sessionBaselines
-         : new Map(Object.entries(M.sessionBaselines ?? {}));
-     for (let [N, T] of P) if (!Z.has(N)) Z.set(N, T);
-     let V =
-       M.fileStates instanceof Map
-         ? M.fileStates
-         : new Map(Object.entries(M.fileStates ?? {}));
-     for (let [N, T] of V) {
-       let k = _.get(N);
-       if (k)
-         _.set(N, {
-           ...T,
-           claudeContribution: k.claudeContribution + T.claudeContribution,
-         });
-       else _.set(N, T);
-     }
-   }
-   let G = await Promise.all(
-     K.map(async (M) => {
-       if (sU7(M)) return { type: "generated", file: M };
-       let P = Uv6(Y, M),
-         V = _.get(M),
-         N = Z.get(M),
-         T = A[0].surface,
-         k = 0,
-         R = 0;
-       if (await n62(M))
-         if (V) ((k = V.claudeContribution), (R = 0));
-         else {
-           let b = await Ap7(M);
-           R = b > 0 ? b : 100;
-         }
-       else
-         try {
-           let b = q.readFileSync(P, { encoding: "utf-8" });
-           if (V) ((k = V.claudeContribution), (R = 0));
-           else if (N) {
-             let Q = await Ap7(M);
-             R = Q > 0 ? Q : b.length;
-           } else R = b.length;
-         } catch {
-           return null;
-         }
-       ((k = Math.max(0, k)), (R = Math.max(0, R)));
-       let S = k + R,
-         g = S > 0 ? Math.round((k / S) * 100) : 0;
-       return {
-         type: "file",
-         file: M,
-         claudeChars: k,
-         humanChars: R,
-         percent: g,
-         surface: T,
-       };
-     }),
-   );
-   for (let M of G) {
-     if (!M) continue;
-     if (M.type === "generated") {
-       H.push(M.file);
-       continue;
-     }
-     ((w[M.file] = {
-       claudeChars: M.claudeChars,
-       humanChars: M.humanChars,
-       percent: M.percent,
-       surface: M.surface,
-     }),
-       (O += M.claudeChars),
-       ($ += M.humanChars),
-       (X[M.surface] = (X[M.surface] ?? 0) + M.claudeChars));
-   }
-   let W = O + $,
-     D = W > 0 ? Math.round((O / W) * 100) : 0,
-     j = {};
-   for (let [M, P] of Object.entries(X)) {
-     let V = W > 0 ? Math.round((P / W) * 100) : 0;
-     j[M] = { claudeChars: P, percent: V };
-   }
-   return {
-     version: 1,
-     summary: {
-       claudePercent: D,
-       claudeChars: O,
-       humanChars: $,
-       surfaces: Array.from(J),
-     },
-     files: w,
-     surfaceBreakdown: j,
-     excludedGenerated: H,
-     sessions: [z],
-   };
- }

--- Removed Ap7 (pretty-v2.1.19.js:387807-387834)
- async function Ap7(A) {
-   let K = t6();
-   try {
-     let q = await F4("git", ["diff", "--cached", "--stat", "--", A], {
-       cwd: K,
-       timeout: 5000,
-     });
-     if (q.code !== 0 || !q.stdout) return 0;
-     let Y = q.stdout
-         .split(
-           `
- `,
-         )
-         .filter(Boolean),
-       z = 0;
-     for (let w of Y)
-       if (w.includes("file changed") || w.includes("files changed")) {
-         let H = w.match(/(\d+) insertions?/),
-           J = w.match(/(\d+) deletions?/),
-           X = H ? parseInt(H[1], 10) : 0,
-           O = J ? parseInt(J[1], 10) : 0;
-         z += (X + O) * 40;
-       }
-     return z;
-   } catch {
-     return 0;
-   }
- }

--- Removed n62 (pretty-v2.1.19.js:387835-387845)
- async function n62(A) {
-   let K = t6();
-   try {
-     let q = await F4("git", ["diff", "--cached", "--name-status", "--", A], {
-       cwd: K,
-       timeout: 5000,
-     });
-     if (q.code === 0 && q.stdout) return q.stdout.trim().startsWith("D\t");
-   } catch {}
-   return !1;
- }

--- Removed Hp7 (pretty-v2.1.19.js:387846-387858)
- function Hp7(A, K = !1) {
-   let q = Object.entries(A.surfaceBreakdown)
-       .filter(([w, H]) => H.percent > 0)
-       .sort((w, H) => H[1].percent - w[1].percent)
-       .map(([w, H]) => ({ surface: K ? c62(w) : w, percent: H.percent })),
-     Y = {};
-   for (let w of q) Y[w.surface] = (Y[w.surface] ?? 0) + w.percent;
-   let z = Object.entries(Y)
-     .sort((w, H) => H[1] - w[1])
-     .map(([w, H]) => `${w}=${H}%`);
-   if (z.length === 0) return "";
-   return `Claude-Generated-By: Claude Code (${z.join(" ")})`;
- }

--- Removed Jp7 (pretty-v2.1.19.js:387859-387876)
- async function Jp7() {
-   let A = t6(),
-     K = hA();
-   return (
-     await Promise.all(
-       [
-         ".git/rebase-merge",
-         ".git/rebase-apply",
-         ".git/MERGE_HEAD",
-         ".git/CHERRY_PICK_HEAD",
-         ".git/BISECT_LOG",
-       ].map(async (z) => {
-         let w = Uv6(A, z);
-         return K.existsSync(w);
-       }),
-     )
-   ).some((z) => z);
- }

--- Removed cv6 (pretty-v2.1.19.js:387877-387892)
- function cv6(A, K) {
-   let q = {};
-   for (let [Y, z] of A.fileStates) q[Y] = z;
-   return {
-     type: "attribution-snapshot",
-     messageId: K,
-     surface: A.surface,
-     fileStates: q,
-     promptCount: A.promptCount,
-     promptCountAtLastCommit: A.promptCountAtLastCommit,
-     permissionPromptCount: A.permissionPromptCount,
-     permissionPromptCountAtLastCommit: A.permissionPromptCountAtLastCommit,
-     escapeCount: A.escapeCount,
-     escapeCountAtLastCommit: A.escapeCountAtLastCommit,
-   };
- }

--- Removed zgA (pretty-v2.1.19.js:391494-391537)
- var zgA = C(() => {
-   zO();
-   P1();
-   I1();
-   zO();
-   $NA();
-   UX();
-   ZE6 = w6(async (A) => {
-     let K = await eI(A),
-       q = K.map((z) => z.userFacingName()).join(", ");
-     h(`Skills and commands included in Skill tool: ${q}`);
-     let Y = u82(K);
-     return `Execute a skill within the main conversation
- 
- When users ask you to perform tasks, check if any of the available skills below can help complete the task more effectively. Skills provide specialized capabilities and domain knowledge.
- 
- When users ask you to run a "slash command" or reference "/<something>" (e.g., "/commit", "/review-pr"), they are referring to a skill. Use this tool to invoke the corresponding skill.
- 
- Example:
-   User: "run /commit"
-   Assistant: [Calls Skill tool with skill: "commit"]
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
- - When a skill is relevant, you must invoke this tool IMMEDIATELY as your first action
- - NEVER just announce or mention a skill in your text response without actually calling this tool
- - This is a BLOCKING REQUIREMENT: invoke the relevant Skill tool BEFORE generating any other response about the task
- - Skills listed below are available for invocation
- - Do not invoke a skill that is already running
- - Do not use this tool for built-in CLI commands (like /help, /clear, etc.)
- - If you see a <${XM}> tag in the current conversation turn (e.g., <${XM}>/commit</${XM}>), the skill has ALREADY been loaded and its instructions follow in the next message. Do NOT call this tool - just follow the skill instructions directly.
- 
- Available skills:
- ${Y}
- `;
-   });
- });

--- Removed r82 (pretty-v2.1.19.js:392044-392046)
- function r82(A) {
-   return Dd7("sha256").update(A).digest("hex");
- }

--- Removed os7 (pretty-v2.1.19.js:419496-419583)
- var os7 = C(() => {
-   rs7 = `Use this tool proactively when you're about to start a non-trivial implementation task. Getting user sign-off on your approach before writing code prevents wasted effort and ensures alignment. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
-    - If you would use ${_X} to clarify the approach, use EnterPlanMode instead
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
- 5. Use ${_X} if you need to clarify approaches
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
- `;
- });

--- Removed _t7 (pretty-v2.1.19.js:420055-420057)
- function _t7() {
-   return AP.createElement(f, { dimColor: !0 }, "Creating task…");
- }

--- Removed Wt7 (pretty-v2.1.19.js:420064-420075)
- function Wt7(A) {
-   let { task: K } = A;
-   return AP.createElement(
-     I,
-     null,
-     AP.createElement(f, { color: "success" }, aA.tick, " "),
-     AP.createElement(f, null, "Task "),
-     AP.createElement(f, { bold: !0 }, "#", K.id),
-     AP.createElement(f, null, " created: "),
-     AP.createElement(f, null, K.subject),
-   );
- }

--- Removed Rt7 (pretty-v2.1.19.js:420300-420363)
-   Rt7 = `Use this tool to update a task in the task list.
- 
- ## When to Use This Tool
- 
- **Mark tasks as resolved:**
- - When you have completed the work described in a task
- - When a task is no longer needed or has been superseded
- - IMPORTANT: Always mark your assigned tasks as resolved when you finish them
- - After resolving, call TaskList to find your next task
- 
- - ONLY mark a task as completed when you have FULLY accomplished it
- - If you encounter errors, blockers, or cannot finish, keep the task as in_progress
- - When blocked, create a new task describing what needs to be resolved
- - Never mark a task as completed if:
-   - Tests are failing
-   - Implementation is partial
-   - You encountered unresolved errors
-   - You couldn't find necessary files or dependencies
- 
- **Update task details:**
- - When requirements change or become clearer
- - When establishing dependencies between tasks
- 
- ## Fields You Can Update
- 
- - **status**: The task status (see Status Workflow below)
- - **subject**: Change the task title (imperative form, e.g., "Run tests")
- - **description**: Change the task description
- - **activeForm**: Present continuous form shown in spinner when in_progress (e.g., "Running tests")
- - **owner**: Change the task owner (agent name)
- - **metadata**: Merge metadata keys into the task (set a key to null to delete it)
- - **addBlocks**: Mark tasks that cannot start until this one completes
- - **addBlockedBy**: Mark tasks that must complete before this one can start
- 
- ## Status Workflow
- 
- Status progresses: \`pending\` → \`in_progress\` → \`completed\`
- 
- ## Staleness
- 
- Make sure to read a task's latest state using \`TaskGet\` before updating it.
- 
- ## Examples
- 
- Mark task as in progress when starting work:
- \`\`\`json
- {"taskId": "1", "status": "in_progress"}
- \`\`\`
- 
- Mark task as completed after finishing work:
- \`\`\`json
- {"taskId": "1", "status": "completed"}
- \`\`\`
- 
- Claim a task by setting owner:
- \`\`\`json
- {"taskId": "1", "owner": "my-name"}
- \`\`\`
- 
- Set up task dependencies:
- \`\`\`json
- {"taskId": "2", "addBlockedBy": ["1"]}
- \`\`\`
- `;

--- Removed It7 (pretty-v2.1.19.js:420367-420369)
- function It7() {
-   return AJ.createElement(f, { dimColor: !0 }, "Updating task…");
- }

--- Removed bt7 (pretty-v2.1.19.js:420376-420401)
- function bt7(A) {
-   let { success: K, taskId: q, updatedFields: Y, statusChange: z } = A;
-   if (!K)
-     return AJ.createElement(
-       I,
-       null,
-       AJ.createElement(f, { color: "error" }, aA.cross, " "),
-       AJ.createElement(f, null, "Task "),
-       AJ.createElement(f, { bold: !0 }, "#", q),
-       AJ.createElement(f, null, " not found"),
-     );
-   let w = Y.map((J) => {
-       if (J === "status" && z) return `status → ${v22(z.to)}`;
-       return J;
-     }),
-     H = w.length > 0 ? w.join(", ") : "no fields";
-   return AJ.createElement(
-     I,
-     null,
-     AJ.createElement(f, { color: "success" }, aA.tick, " "),
-     AJ.createElement(f, null, "Task "),
-     AJ.createElement(f, { bold: !0 }, "#", q),
-     AJ.createElement(f, null, " updated: "),
-     AJ.createElement(f, { dimColor: !0 }, H),
-   );
- }

--- Removed v22 (pretty-v2.1.19.js:420402-420404)
- function v22(A) {
-   return A.replace(/_/g, " ");
- }

--- Removed Ut7 (pretty-v2.1.19.js:420649-420655)
- function Ut7() {
-   return bw.createElement(
-     v6,
-     { height: 1 },
-     bw.createElement(f, { dimColor: !0 }, "Loading tasks…"),
-   );
- }

--- Removed ct7 (pretty-v2.1.19.js:420662-420693)
- function ct7(A) {
-   let { tasks: K } = A;
-   if (K.length === 0)
-     return bw.createElement(f, { dimColor: !0 }, "No tasks found");
-   let q = K.filter((H) => H.status === "completed").length,
-     Y = K.filter((H) => H.status === "pending").length,
-     z = K.length - q - Y,
-     w = [`${q} done`];
-   if (z > 0) w.push(`${z} in progress`);
-   return (
-     w.push(`${Y} open`),
-     bw.createElement(
-       I,
-       { flexDirection: "column" },
-       bw.createElement(
-         I,
-         { marginBottom: 1 },
-         bw.createElement(
-           f,
-           { dimColor: !0 },
-           K.length,
-           " task",
-           K.length !== 1 ? "s" : "",
-           " (",
-           w.join(", "),
-           ")",
-         ),
-       ),
-       K.map((H) => bw.createElement(C22, { key: H.id, task: H })),
-     )
-   );
- }

--- Removed C22 (pretty-v2.1.19.js:420694-420763)
- function C22(A) {
-   let K = a(20),
-     { task: q } = A,
-     Y = q.status === "completed",
-     z = q.status !== "completed" && q.status !== "pending",
-     w = q.blockedBy.length > 0,
-     H = Y ? aA.tick : aA.squareSmallFilled,
-     J;
-   if (Y) J = "success";
-   else if (w) J = "warning";
-   let X;
-   if (K[0] !== J || K[1] !== H)
-     ((X = bw.createElement(f, { color: J }, H, " ")),
-       (K[0] = J),
-       (K[1] = H),
-       (K[2] = X));
-   else X = K[2];
-   let O;
-   if (K[3] !== q.id)
-     ((O = bw.createElement(f, { dimColor: !0 }, "#", q.id, " ")),
-       (K[3] = q.id),
-       (K[4] = O));
-   else O = K[4];
-   let $;
-   if (K[5] !== Y || K[6] !== z || K[7] !== q.subject)
-     (($ = bw.createElement(
-       f,
-       { strikethrough: Y, dimColor: Y, bold: z },
-       q.subject,
-     )),
-       (K[5] = Y),
-       (K[6] = z),
-       (K[7] = q.subject),
-       (K[8] = $));
-   else $ = K[8];
-   let _;
-   if (K[9] !== q.owner)
-     ((_ = q.owner && bw.createElement(f, { dimColor: !0 }, " (", q.owner, ")")),
-       (K[9] = q.owner),
-       (K[10] = _));
-   else _ = K[10];
-   let Z;
-   if (K[11] !== w || K[12] !== q.blockedBy)
-     ((Z =
-       w &&
-       bw.createElement(
-         f,
-         { color: "warning" },
-         " ",
-         aA.warning,
-         " blocked by",
-         " ",
-         q.blockedBy.map(L22).join(", "),
-       )),
-       (K[11] = w),
-       (K[12] = q.blockedBy),
-       (K[13] = Z));
-   else Z = K[13];
-   let G;
-   if (K[14] !== X || K[15] !== O || K[16] !== $ || K[17] !== _ || K[18] !== Z)
-     ((G = bw.createElement(I, null, X, O, $, _, Z)),
-       (K[14] = X),
-       (K[15] = O),
-       (K[16] = $),
-       (K[17] = _),
-       (K[18] = Z),
-       (K[19] = G));
-   else G = K[19];
-   return G;
- }

--- Removed n8K (pretty-v2.1.19.js:434869-434875)
- function n8K() {
-   if (aDA)
-     ((os = aDA), h(`[TeammateModeSnapshot] Captured from CLI override: ${os}`));
-   else
-     ((os = f1().teammateMode ?? "auto"),
-       h(`[TeammateModeSnapshot] Captured from config: ${os}`));
- }

--- Removed Q$2 (pretty-v2.1.19.js:436371-436373)
- function Q$2(A) {
-   return "operation" in A && A.operation === "broadcast";
- }

--- Removed l$2 (pretty-v2.1.19.js:436403-436405)
- function l$2(A) {
-   return "requestId" in A && "success" in A && "target" in A && "message" in A;
- }

--- Removed H_2 (pretty-v2.1.19.js:437027-437045)
- async function H_2(A, K) {
-   let { target_agent_id: q, reason: Y } = A,
-     z = await K.getAppState(),
-     w = A.team_name || j9(z.teamContext);
-   if (!q)
-     throw Error(
-       "target_agent_id is required for requestShutdown operation to specify which teammate to shut down",
-     );
-   let H = v4K(q),
-     { requestId: J, target: X } = xFA(H, w, Y);
-   return {
-     data: {
-       success: !0,
-       message: `Shutdown request sent to ${X}. Request ID: ${J}`,
-       requestId: J,
-       target: X,
-     },
-   };
- }

--- Removed J_2 (pretty-v2.1.19.js:437046-437160)
- async function J_2(A, K) {
-   let q = A.team_name || j9(),
-     Y = r$(),
-     z = PY() || "teammate";
-   if (
-     (h(
-       `[handleApproveShutdown] Identity: teamName=${q}, agentId=${Y}, agentName=${z}`,
-     ),
-     !A.request_id)
-   )
-     throw Error(
-       "request_id is required for approveShutdown. Use the requestId from the shutdown_request message.",
-     );
-   let w = A.request_id,
-     H,
-     J;
-   if (q) {
-     let O = Cz(q);
-     if (
-       (h(
-         `[handleApproveShutdown] Team file found: ${!!O}, members: ${O?.members?.length ?? 0}`,
-       ),
-       O && Y)
-     ) {
-       let $ = O.members.find((_) => _.agentId === Y);
-       if (
-         (h(
-           `[handleApproveShutdown] selfMember found: ${!!$}, backendType: ${$?.backendType ?? "undefined"}, looking for agentId: ${Y}`,
-         ),
-         $)
-       )
-         ((H = $.tmuxPaneId), (J = $.backendType));
-     }
-   } else h("[handleApproveShutdown] WARNING: teamName is undefined!");
-   let X = Pv6({ requestId: w, from: z, paneId: H, backendType: J });
-   if (
-     (U3(
-       ZH,
-       {
-         from: z,
-         text: UA(X),
-         timestamp: new Date().toISOString(),
-         color: l0(),
-       },
-       q,
-     ),
-     h(
-       `[handleApproveShutdown] Backend type decision: ownBackendType=${J}, isInProcess=${J === "in-process"}`,
-     ),
-     J === "in-process")
-   )
-     if (
-       (h(
-         `[TeammateTool] In-process teammate ${z} approving shutdown - signaling abort`,
-       ),
-       Y)
-     ) {
-       let O = await K.getAppState(),
-         $ = Object.keys(O.tasks ?? {}).length,
-         _ = Object.keys(O.tasks ?? {});
-       h(`[handleApproveShutdown] AppState has ${$} tasks: [${_.join(", ")}]`);
-       let Z = Y3A(Y, O.tasks);
-       if (
-         (h(
-           `[handleApproveShutdown] findTeammateTaskByAgentId(${Y}): found=${!!Z}, hasAbortController=${!!Z?.abortController}, taskId=${Z?.id ?? "N/A"}`,
-         ),
-         Z?.abortController)
-       )
-         (h(
-           `[handleApproveShutdown] AbortController state before abort: aborted=${Z.abortController.signal.aborted}`,
-         ),
-           Z.abortController.abort(),
-           h(
-             `[handleApproveShutdown] AbortController state after abort: aborted=${Z.abortController.signal.aborted}`,
-           ),
-           h(`[TeammateTool] Aborted controller for in-process teammate ${z}`));
-       else
-         h(
-           `[TeammateTool] Warning: Could not find task/abortController for ${z}`,
-         );
-     } else
-       h(
-         "[handleApproveShutdown] WARNING: agentId is undefined, cannot look up task!",
-       );
-   else {
-     if (Y) {
-       let O = await K.getAppState(),
-         $ = Y3A(Y, O.tasks);
-       if ($?.abortController)
-         return (
-           h(
-             `[handleApproveShutdown] Fallback: Found in-process task for ${z} via AppState, aborting`,
-           ),
-           $.abortController.abort(),
-           {
-             data: {
-               success: !0,
-               message: `Shutdown approved (fallback path). Agent ${z} is now exiting.`,
-               requestId: w,
-             },
-           }
-         );
-     }
-     setImmediate(async () => {
-       await o5(0, "other");
-     });
-   }
-   return {
-     data: {
-       success: !0,
-       message: `Shutdown approved. Sent confirmation to team-lead. Agent ${z} is now exiting.`,
-       requestId: w,
-     },
-   };
- }

--- Removed j_2 (pretty-v2.1.19.js:438060-438106)
- function j_2(A) {
-   if (!A?.length) return [];
-   let K = [],
-     q = 80;
-   for (let Y = A.length - 1; Y >= 0 && K.length < 3; Y--) {
-     let z = A[Y];
-     if (
-       !z ||
-       (z.type !== "user" && z.type !== "assistant") ||
-       !z.message?.content?.length
-     )
-       continue;
-     let w = z.message.content;
-     for (let H of w) {
-       if (K.length >= 3) break;
-       if (!H || typeof H !== "object") continue;
-       if ("type" in H && H.type === "tool_use" && "name" in H) {
-         let J = "input" in H ? H.input : null,
-           X = `Using ${H.name}…`;
-         if (J) {
-           let $ =
-             J.description || J.prompt || J.command || J.query || J.pattern;
-           if ($)
-             X =
-               $.split(`
- `)[0] ?? X;
-         }
-         let O = X.length > q ? X.slice(0, q - 1) + "…" : X;
-         K.push(O);
-       } else if ("type" in H && H.type === "text" && "text" in H) {
-         let J = H.text
-           .split(
-             `
- `,
-           )
-           .filter((X) => X.trim());
-         for (let X = J.length - 1; X >= 0 && K.length < 3; X--) {
-           let O = J[X];
-           if (!O) continue;
-           let $ = O.length > q ? O.slice(0, q - 1) + "…" : O;
-           K.push($);
-         }
-       }
-     }
-   }
-   return K.reverse();
- }

--- Removed L4K (pretty-v2.1.19.js:438107-438206)
- function L4K({
-   teammate: A,
-   isLast: K,
-   frame: q,
-   isSelected: Y,
-   isViewing: z,
-   allTeammatesIdle: w,
-   showPreview: H,
- }) {
-   let [J] = KjA.useState(() => eP(SZ1)),
-     [X] = KjA.useState(() => eP(hWA)),
-     O = K ? "└─" : "├─",
-     $ = sT(A.identity.color),
-     _ = KjA.useRef(null),
-     Z = KjA.useRef(null);
-   if (A.isIdle && _.current === null) _.current = Date.now();
-   else if (!A.isIdle) _.current = null;
-   if (!w && Z.current !== null) Z.current = null;
-   let G = w3A(_.current ?? Date.now(), A.isIdle && !w);
-   if (w && Z.current === null) Z.current = Dw(Date.now() - A.startTime);
-   let W = w ? Z.current : G,
-     D = () => {
-       if (A.shutdownRequested)
-         return Bq.createElement(f, { dimColor: !0 }, "[stopping]");
-       if (A.awaitingPlanApproval)
-         return Bq.createElement(f, { color: "warning" }, "[awaiting approval]");
-       if (A.isIdle) {
-         if (w)
-           return Bq.createElement(
-             I,
-             { flexDirection: "row" },
-             Bq.createElement(f, { dimColor: !0 }, `${da} ${X} for ${W}`),
-           );
-         return Bq.createElement(
-           I,
-           { flexDirection: "row" },
-           Bq.createElement(
-             f,
-             { dimColor: !0 },
-             `${da} Idle for ${G}… (shift+↑/↓ to select)`,
-           ),
-         );
-       }
-       return Bq.createElement(
-         I,
-         { flexDirection: "row" },
-         Bq.createElement(n5A, { frame: q, messageColor: "claude" }),
-         Bq.createElement(f, { color: "claude" }, J, "…"),
-       );
-     },
-     j = A.progress?.toolUseCount ?? 0,
-     M = A.progress?.tokenCount ?? 0,
-     P = H ? j_2(A.messages) : [],
-     V = K ? "   " : "│  ";
-   return Bq.createElement(
-     I,
-     { flexDirection: "column" },
-     Bq.createElement(
-       I,
-       { paddingLeft: 3 },
-       Bq.createElement(
-         f,
-         { color: Y ? "suggestion" : void 0, bold: Y },
-         Y ? aA.pointer : " ",
-       ),
-       Bq.createElement(f, { dimColor: !Y }, O, " "),
-       Bq.createElement(
-         f,
-         { bold: !0, color: Y ? "suggestion" : $ },
-         A.identity.agentName,
-       ),
-       z && Bq.createElement(f, { color: "success" }, " [viewing]"),
-       Bq.createElement(f, { dimColor: !Y }, ": "),
-       D(),
-       Bq.createElement(
-         f,
-         { dimColor: !Y },
-         " ",
-         "· ",
-         j,
-         " tool ",
-         j === 1 ? "use" : "uses",
-         " ·",
-         " ",
-         M3(M),
-         " tokens",
-       ),
-       Y && !z && Bq.createElement(f, { dimColor: !0 }, " · enter to view"),
-     ),
-     P.map((N, T) =>
-       Bq.createElement(
-         I,
-         { key: T, paddingLeft: 3 },
-         Bq.createElement(f, { dimColor: !0 }, " "),
-         Bq.createElement(f, { dimColor: !0 }, V, " "),
-         Bq.createElement(f, { dimColor: !0 }, N),
-       ),
-     ),
-   );
- }

--- Removed yM1 (pretty-v2.1.19.js:438220-438320)
- function yM1(A) {
-   let K = a(22),
-     {
-       frame: q,
-       selectedIndex: Y,
-       isInSelectionMode: z,
-       allTeammatesIdle: w,
-     } = A,
-     [H] = j6(),
-     { tasks: J, viewingAgentTaskId: X, showTeammateMessagePreview: O } = H,
-     $,
-     _,
-     Z,
-     G,
-     W;
-   if (
-     K[0] !== w ||
-     K[1] !== q ||
-     K[2] !== z ||
-     K[3] !== Y ||
-     K[4] !== O ||
-     K[5] !== J ||
-     K[6] !== X
-   ) {
-     W = Symbol.for("react.early_return_sentinel");
-     A: {
-       let j = as(J).filter(P_2).sort(M_2);
-       if (j.length === 0) {
-         W = null;
-         break A;
-       }
-       let M = z && Y === -1,
-         P = X === void 0;
-       if (
-         (($ = I),
-         (_ = "column"),
-         K[12] !== z || K[13] !== M || K[14] !== P || K[15] !== X)
-       )
-         ((Z =
-           (z || X) &&
-           TW.createElement(
-             I,
-             { paddingLeft: 3 },
-             TW.createElement(
-               f,
-               { color: M ? "suggestion" : void 0, bold: M },
-               M ? aA.pointer : " ",
-             ),
-             TW.createElement(f, { dimColor: !M }, " "),
-             TW.createElement(
-               f,
-               { bold: !0, color: M ? "suggestion" : void 0 },
-               "team-lead",
-             ),
-             P && TW.createElement(f, { color: "success" }, " [viewing]"),
-             M && TW.createElement(f, { dimColor: !0 }, " · enter to view"),
-           )),
-           (K[12] = z),
-           (K[13] = M),
-           (K[14] = P),
-           (K[15] = X),
-           (K[16] = Z));
-       else Z = K[16];
-       G = j.map((V, N) =>
-         TW.createElement(L4K, {
-           key: V.id,
-           teammate: V,
-           isLast: N === j.length - 1,
-           frame: q,
-           isSelected: z && Y === N,
-           isViewing: X === V.id,
-           allTeammatesIdle: w,
-           showPreview: O,
-         }),
-       );
-     }
-     ((K[0] = w),
-       (K[1] = q),
-       (K[2] = z),
-       (K[3] = Y),
-       (K[4] = O),
-       (K[5] = J),
-       (K[6] = X),
-       (K[7] = $),
-       (K[8] = _),
-       (K[9] = Z),
-       (K[10] = G),
-       (K[11] = W));
-   } else (($ = K[7]), (_ = K[8]), (Z = K[9]), (G = K[10]), (W = K[11]));
-   if (W !== Symbol.for("react.early_return_sentinel")) return W;
-   let D;
-   if (K[17] !== $ || K[18] !== _ || K[19] !== Z || K[20] !== G)
-     ((D = TW.createElement($, { flexDirection: _ }, Z, G)),
-       (K[17] = $),
-       (K[18] = _),
-       (K[19] = Z),
-       (K[20] = G),
-       (K[21] = D));
-   else D = K[21];
-   return D;
- }

--- Removed oZ2 (pretty-v2.1.19.js:448190-448215)
-   oZ2 = `You are coming up with a succinct title and git branch name for a coding session based on the provided description. The title should be clear, concise, and accurately reflect the content of the coding task.
- You should keep it short and simple, ideally no more than 6 words. Avoid using jargon or overly technical terms unless absolutely necessary. The title should be easy to understand for anyone reading it.
- Use sentence case for the title (capitalize only the first word and proper nouns), not Title Case.
- You should wrap the title in <title> tags.
- 
- The branch name should be clear, concise, and accurately reflect the content of the coding task.
- You should keep it short and simple, ideally no more than 4 words. The branch should always start with "claude/" and should be all lower case, with words separated by dashes.
- You should wrap the branch name in <branch> tags.
- 
- The title should always come first, followed by the branch. Do not include any other text other than the title and branch.
- 
- Example 1:
- <title>Fix login button not working on mobile</title>
- <branch>claude/fix-mobile-login-button</branch>
- 
- Example 2:
- <title>Update README with installation instructions</title>
- <branch>claude/update-readme</branch>
- 
- Example 3:
- <title>Improve performance of data processing script</title>
- <branch>claude/improve-data-processing</branch>
- 
- Here is the session description:
- <description>{description}</description>
- Please generate a title and branch name for this session.`;

--- Removed N5K (pretty-v2.1.19.js:448610-448613)
- async function N5K(A, K, q) {
-   if (q !== "repl_main_thread") return [];
-   return [];
- }

--- Removed T5K (pretty-v2.1.19.js:448617-448625)
- var T5K = C(() => {
-   r6();
-   e1();
-   Hf();
-   e6();
-   I1();
-   KM();
-   $I6 = f5K(f8(), "session-memory");
- });

--- Removed up (pretty-v2.1.19.js:452538-452544)
- async function up(A, K) {
-   let q = iqK(A);
-   return (
-     await wP().insertMessageChain(q, !1, void 0, void 0, K),
-     q[q.length - 1]?.uuid || null
-   );
- }

--- Removed aI6 (pretty-v2.1.19.js:452557-452559)
- async function aI6(A) {
-   await wP().insertAttributionSnapshot(A);
- }

--- Removed AV1 (pretty-v2.1.19.js:462393-462402)
- var AV1 = C(() => {
-   sq();
-   P1();
-   Q7();
-   bjA = w6(() => {
-     if (eP1()) return "homebrew";
-     if (gS6()) return "winget";
-     return "unknown";
-   });
- });

--- Removed XMA (pretty-v2.1.19.js:479247-479273)
- function XMA(A) {
-   let K = a(6),
-     { children: q, onComplete: Y } = A,
-     z = XUA.useRef(!1),
-     w,
-     H;
-   if (K[0] !== q || K[1] !== Y)
-     ((w = () => {
-       if (z.current) return;
-       ((z.current = !0),
-         XwK(q).then((X) => {
-           Y(X);
-         }));
-     }),
-       (H = [q, Y]),
-       (K[0] = q),
-       (K[1] = Y),
-       (K[2] = w),
-       (K[3] = H));
-   else ((w = K[2]), (H = K[3]));
-   XUA.useLayoutEffect(w, H);
-   let J;
-   if (K[4] !== q)
-     ((J = WL.createElement(WL.Fragment, null, q)), (K[4] = q), (K[5] = J));
-   else J = K[5];
-   return J;
- }

--- Removed VHK (pretty-v2.1.19.js:483273-483285)
- var VHK = C(() => {
-   U86();
-   d86();
-   F1();
-   Rv2 = {
-     context: "Chat",
-     bindings: {
-       "ctrl+k ctrl+c": "command:commit",
-       "ctrl+k ctrl+d": "command:diff",
-       "ctrl+k ctrl+r": "command:rebase-push",
-     },
-   };
- });

--- Removed H_K (pretty-v2.1.19.js:507150-507215)
- function H_K(A) {
-   let K = a(23),
-     { task: q } = A;
-   switch (q.type) {
-     case "local_bash": {
-       let Y;
-       if (K[0] !== q.command)
-         ((Y = MY(q.command, 40, !0)), (K[0] = q.command), (K[1] = Y));
-       else Y = K[1];
-       let z;
-       if (K[2] !== q)
-         ((z = bv.createElement(z_K, { shell: q })), (K[2] = q), (K[3] = z));
-       else z = K[3];
-       let w;
-       if (K[4] !== Y || K[5] !== z)
-         ((w = bv.createElement(f, null, Y, " ", z)),
-           (K[4] = Y),
-           (K[5] = z),
-           (K[6] = w));
-       else w = K[6];
-       return w;
-     }
-     case "remote_agent": {
-       let Y;
-       if (K[7] !== q.title)
-         ((Y = MY(q.title, 40, !0)), (K[7] = q.title), (K[8] = Y));
-       else Y = K[8];
-       let z;
-       if (K[9] !== q)
-         ((z = bv.createElement(ON1, { session: q })), (K[9] = q), (K[10] = z));
-       else z = K[10];
-       let w;
-       if (K[11] !== Y || K[12] !== z)
-         ((w = bv.createElement(f, null, Y, " ", z)),
-           (K[11] = Y),
-           (K[12] = z),
-           (K[13] = w));
-       else w = K[13];
-       return w;
-     }
-     case "local_agent": {
-       let Y;
-       if (K[14] !== q.description)
-         ((Y = MY(q.description, 40, !0)), (K[14] = q.description), (K[15] = Y));
-       else Y = K[15];
-       let z = q.status === "completed" ? "done" : void 0,
-         w = q.status === "completed" && !q.notified ? ", unread" : void 0,
-         H;
-       if (K[16] !== z || K[17] !== w || K[18] !== q.status)
-         ((H = bv.createElement(uMA, { status: q.status, label: z, suffix: w })),
-           (K[16] = z),
-           (K[17] = w),
-           (K[18] = q.status),
-           (K[19] = H));
-       else H = K[19];
-       let J;
-       if (K[20] !== Y || K[21] !== H)
-         ((J = bv.createElement(f, null, Y, " ", H)),
-           (K[20] = Y),
-           (K[21] = H),
-           (K[22] = J));
-       else J = K[22];
-       return J;
-     }
-   }
- }

--- Removed FB6 (pretty-v2.1.19.js:507588-507612)
- function FB6(A) {
-   let K = a(6),
-     { item: q, isSelected: Y } = A,
-     z = Y ? "suggestion" : void 0,
-     w = Y ? aA.pointer + " " : "  ",
-     H;
-   if (K[0] !== q.task)
-     ((H = T3.default.createElement(H_K, { task: q.task })),
-       (K[0] = q.task),
-       (K[1] = H));
-   else H = K[1];
-   let J;
-   if (K[2] !== z || K[3] !== w || K[4] !== H)
-     ((J = T3.default.createElement(
-       I,
-       { flexDirection: "row", gap: 1 },
-       T3.default.createElement(f, { color: z }, w, H),
-     )),
-       (K[2] = z),
-       (K[3] = w),
-       (K[4] = H),
-       (K[5] = J));
-   else J = K[5];
-   return J;
- }

--- Removed tGK (pretty-v2.1.19.js:519555-519602)
- var tGK = `
- # Claude in Chrome browser automation
- 
- You have access to browser automation tools (mcp__claude-in-chrome__*) for interacting with web pages in Chrome. Follow these guidelines for effective browser automation.
- 
- ## GIF recording
- 
- When performing multi-step browser interactions that the user may want to review or share, use mcp__claude-in-chrome__gif_creator to record them.
- 
- You must ALWAYS:
- * Capture extra frames before and after taking actions to ensure smooth playback
- * Name the file meaningfully to help the user identify it later (e.g., "login_process.gif")
- 
- ## Console log debugging
- 
- You can use mcp__claude-in-chrome__read_console_messages to read console output. Console output may be verbose. If you are looking for specific log entries, use the 'pattern' parameter with a regex-compatible pattern. This filters results efficiently and avoids overwhelming output. For example, use pattern: "[MyApp]" to filter for application-specific logs rather than reading all console output.
- 
- ## Alerts and dialogs
- 
- IMPORTANT: Do not trigger JavaScript alerts, confirms, prompts, or browser modal dialogs through your actions. These browser dialogs block all further browser events and will prevent the extension from receiving any subsequent commands. Instead, when possible, use console.log for debugging and then use the mcp__claude-in-chrome__read_console_messages tool to read those log messages. If a page has dialog-triggering elements:
- 1. Avoid clicking buttons or links that may trigger alerts (e.g., "Delete" buttons with confirmation dialogs)
- 2. If you must interact with such elements, warn the user first that this may interrupt the session
- 3. Use mcp__claude-in-chrome__javascript_tool to check for and dismiss any existing dialogs before proceeding
- 
- If you accidentally trigger a dialog and lose responsiveness, inform the user they need to manually dismiss it in the browser.
- 
- ## Avoid rabbit holes and loops
- 
- When using browser automation tools, stay focused on the specific task. If you encounter any of the following, stop and ask the user for guidance:
- - Unexpected complexity or tangential browser exploration
- - Browser tool calls failing or returning errors after 2-3 attempts
- - No response from the browser extension
- - Page elements not responding to clicks or input
- - Pages not loading or timing out
- - Unable to complete the browser task despite multiple approaches
- 
- Explain what you attempted, what went wrong, and ask how the user would like to proceed. Do not keep retrying the same failing browser action or explore unrelated pages without checking in first.
- 
- ## Tab context and session startup
- 
- IMPORTANT: At the start of each browser automation session, call mcp__claude-in-chrome__tabs_context_mcp first to get information about the user's current browser tabs. Use this context to understand what the user might want to work with before creating new tabs.
- 
- Never reuse tab IDs from a previous/other session. Follow these guidelines:
- 1. Only reuse an existing tab if the user explicitly asks to work with it
- 2. Otherwise, create a new tab with mcp__claude-in-chrome__tabs_create_mcp
- 3. If a tool returns an error indicating the tab doesn't exist or is invalid, call tabs_context_mcp to get fresh tab IDs
- 4. When a tab is closed by the user or a navigation error occurs, call tabs_context_mcp to see what tabs are available
- `,

--- Removed eGK (pretty-v2.1.19.js:519603-519614)
-   eGK = `
- **IMPORTANT: Before using any chrome browser tools, you MUST first load them using ToolSearch.**
- 
- Chrome browser tools are MCP tools that require loading before use. Before calling any mcp__claude-in-chrome__* tool:
- 1. Use ToolSearch with \`select:mcp__claude-in-chrome__<tool_name>\` to load the specific tool
- 2. Then call the tool
- 
- For example, to get tab context:
- 1. First: ToolSearch with query "select:mcp__claude-in-chrome__tabs_context_mcp"
- 2. Then: Call mcp__claude-in-chrome__tabs_context_mcp
- 
- `,

--- Removed Eu6 (pretty-v2.1.19.js:519615-519619)
-   Eu6 = `
- 
- **Browser Automation**: Chrome browser tools are available via the "claude-in-chrome" skill. CRITICAL: Before using any mcp__claude-in-chrome__* tools, invoke the skill by calling the Skill tool with skill: "claude-in-chrome". The skill provides browser automation instructions and enables the tools.
- 
- `;

--- Removed q9A (pretty-v2.1.19.js:519841-519853)
- var q9A = C(() => {
-   sq();
-   P1();
-   dK();
-   r6();
-   e1();
-   TN1();
-   PB();
-   l6();
-   F1();
-   kK();
-   KWK = `${ku6}.json`;
- });

--- Removed TDK (pretty-v2.1.19.js:525045-525046)
- var TDK =
-     "IMPORTANT: Assist with authorized security testing, defensive security, CTF challenges, and educational contexts. Refuse requests for destructive techniques, DoS attacks, mass targeting, supply chain compromise, or detection evasion for malicious purposes. Dual-use security tools (C2 frameworks, credential testing, exploit development) require clear authorization context: pentesting engagements, CTF competitions, security research, or defensive use cases.",

--- Removed Qp7 (pretty-v2.1.19.js:526919-526924)
- function Qp7(A, K) {
-   return (
-     A.ruleValue.toolName === K.toolName &&
-     (!A.ruleValue.ruleContent || A.ruleValue.ruleContent === K.ruleContent)
-   );
- }

--- Removed aS6 (pretty-v2.1.19.js:529709-529738)
- function aS6(A, K) {
-   if (TjK(A))
-     return {
-       behavior: "allow",
-       updatedInput: K,
-       decisionReason: {
-         type: "other",
-         reason: "Plan files for current session are allowed for writing",
-       },
-     };
-   if (EjK(A))
-     return {
-       behavior: "allow",
-       updatedInput: K,
-       decisionReason: {
-         type: "other",
-         reason: "Scratchpad files for current session are allowed for writing",
-       },
-     };
-   if (wO6(A))
-     return {
-       behavior: "allow",
-       updatedInput: K,
-       decisionReason: {
-         type: "other",
-         reason: "Agent memory files are allowed for writing",
-       },
-     };
-   return { behavior: "passthrough", message: "" };
- }

--- Removed yMK (pretty-v2.1.19.js:533174-533210)
- async function yMK() {
-   try {
-     if (!xg2() || !E1(process.env.CLAUDE_CODE_REMOTE)) return !1;
-     h("Settings sync: Download starting");
-     let A = await gg2();
-     if (!A.success)
-       return (
-         h(`Settings sync: Fetch failed - ${A.error}`),
-         n("tengu_settings_sync_download_fetch_failed", {}),
-         !1
-       );
-     if (A.isEmpty)
-       return (
-         h("Settings sync: No remote settings to download"),
-         n("tengu_settings_sync_download_empty", {}),
-         !1
-       );
-     let K = A.data.content.entries,
-       q = await hiA();
-     return (
-       h(`Settings sync: Applying ${Object.keys(K).length} entries`),
-       Fg2(K, q),
-       n("tengu_settings_sync_download_success", {
-         entryCount: Object.keys(K).length,
-       }),
-       !0
-     );
-   } catch (A) {
-     return (
-       h(
-         `Settings sync: Download error - ${A instanceof Error ? A.message : "unknown error"}`,
-       ),
-       n("tengu_settings_sync_download_error", {}),
-       !1
-     );
-   }
- }

--- Removed MF2 (pretty-v2.1.19.js:534322-534337)
- function MF2(A, K, q = !0) {
-   let Y = O9A(),
-     z = { messages: 0, errors: 0 },
-     w = hA();
-   try {
-     if (!w.existsSync(A)) return z;
-     let H = Kg6(A, Y, K, w);
-     if (((z.messages += H.messages), (z.errors += H.errors), q))
-       try {
-         if (w.isDirEmptySync(A)) w.rmdirSync(A);
-       } catch {}
-   } catch {
-     z.errors++;
-   }
-   return z;
- }

--- Removed $PK (pretty-v2.1.19.js:535007-535147)
- var $PK = C(() => {
-   T7();
-   pMA();
-   HU();
-   F1();
-   xF2 = `# Update Config Skill
- 
- Modify Claude Code configuration by updating settings.json files.
- 
- ## When Hooks Are Required (Not Memory)
- 
- If the user wants something to happen automatically in response to an EVENT, they need a **hook** configured in settings.json. Memory/preferences cannot trigger automated actions.
- 
- **These require hooks:**
- - "Before compacting, ask me what to preserve" → PreCompact hook
- - "After writing files, run prettier" → PostToolUse hook with Write|Edit matcher
- - "When I run bash commands, log them" → PreToolUse hook with Bash matcher
- - "Always run tests after code changes" → PostToolUse hook
- 
- **Hook events:** PreToolUse, PostToolUse, PreCompact, Stop, Notification, SessionStart
- 
- ## CRITICAL: Read Before Write
- 
- **Always read the existing settings file before making changes.** Merge new settings with existing ones - never replace the entire file.
- 
- ## CRITICAL: Use AskUserQuestion for Ambiguity
- 
- When the user's request is ambiguous, use AskUserQuestion to clarify:
- - Which settings file to modify (user/project/local)
- - Whether to add to existing arrays or replace them
- - Specific values when multiple options exist
- 
- ## Decision: Config Tool vs Direct Edit
- 
- **Use the Config tool** for these simple settings:
- - \`theme\`, \`editorMode\`, \`verbose\`, \`model\`
- - \`language\`, \`alwaysThinkingEnabled\`
- - \`permissions.defaultMode\`
- 
- **Edit settings.json directly** for:
- - Hooks (PreToolUse, PostToolUse, etc.)
- - Complex permission rules (allow/deny arrays)
- - Environment variables
- - MCP server configuration
- - Plugin configuration
- 
- ## Workflow
- 
- 1. **Clarify intent** - Ask if the request is ambiguous
- 2. **Read existing file** - Use Read tool on the target settings file
- 3. **Merge carefully** - Preserve existing settings, especially arrays
- 4. **Edit file** - Use Edit tool (if file doesn't exist, ask user to create it first)
- 5. **Confirm** - Tell user what was changed
- 
- ## Merging Arrays (Important!)
- 
- When adding to permission arrays or hook arrays, **merge with existing**, don't replace:
- 
- **WRONG** (replaces existing permissions):
- \`\`\`json
- { "permissions": { "allow": ["Bash(npm:*)"] } }
- \`\`\`
- 
- **RIGHT** (preserves existing + adds new):
- \`\`\`json
- {
-   "permissions": {
-     "allow": [
-       "Bash(git:*)",      // existing
-       "Edit(.claude)",    // existing
-       "Bash(npm:*)"       // new
-     ]
-   }
- }
- \`\`\`
- 
- ${hF2}
- 
- ${bF2}
- 
- ## Example Workflows
- 
- ### Adding a Hook
- 
- User: "Format my code after Claude writes it"
- 
- 1. **Clarify**: Which formatter? (prettier, gofmt, etc.)
- 2. **Read**: \`.claude/settings.json\` (or create if missing)
- 3. **Merge**: Add to existing hooks, don't replace
- 4. **Result**:
- \`\`\`json
- {
-   "hooks": {
-     "PostToolUse": [{
-       "matcher": "Write|Edit",
-       "hooks": [{
-         "type": "command",
-         "command": "jq -r '.tool_response.filePath // .tool_input.file_path' | xargs prettier --write 2>/dev/null || true"
-       }]
-     }]
-   }
- }
- \`\`\`
- 
- ### Adding Permissions
- 
- User: "Allow npm commands without prompting"
- 
- 1. **Read**: Existing permissions
- 2. **Merge**: Add \`Bash(npm:*)\` to allow array
- 3. **Result**: Combined with existing allows
- 
- ### Environment Variables
- 
- User: "Set DEBUG=true"
- 
- 1. **Decide**: User settings (global) or project settings?
- 2. **Read**: Target file
- 3. **Merge**: Add to env object
- \`\`\`json
- { "env": { "DEBUG": "true" } }
- \`\`\`
- 
- ## Common Mistakes to Avoid
- 
- 1. **Replacing instead of merging** - Always preserve existing settings
- 2. **Wrong file** - Ask user if scope is unclear
- 3. **Invalid JSON** - Validate syntax after changes
- 4. **Forgetting to read first** - Always read before write
- 
- ## Troubleshooting Hooks
- 
- If a hook isn't running:
- 1. **Check the settings file** - Read ~/.claude/settings.json or .claude/settings.json
- 2. **Verify JSON syntax** - Invalid JSON silently fails
- 3. **Check the matcher** - Does it match the tool name? (e.g., "Bash", "Write", "Edit")
- 4. **Check hook type** - Is it "command", "prompt", or "agent"?
- 5. **Test the command** - Run the hook command manually to see if it works
- 6. **Use --debug** - Run \`claude --debug\` to see hook execution logs
- `;
- });

--- Removed GPK (pretty-v2.1.19.js:535154-535156)
- function GPK() {
-   if ((wPK(), OPK(), _PK(), UMA())) JPK();
- }

--- Removed uF2 (pretty-v2.1.19.js:535393-535393)
- var uF2 = 300,

--- Removed LPK (pretty-v2.1.19.js:535543-535815)
- function LPK(A) {
-   let K = a(46),
-     {
-       request: q,
-       workerColor: Y,
-       onDone: z,
-       onApprove: w,
-       onApproveForTeam: H,
-       onDeny: J,
-     } = A,
-     X;
-   if (K[0] !== J || K[1] !== z)
-     ((X = () => {
-       (J(), z());
-     }),
-       (K[0] = J),
-       (K[1] = z),
-       (K[2] = X));
-   else X = K[2];
-   let O = X,
-     $;
-   if (K[3] === Symbol.for("react.memo_cache_sentinel"))
-     (($ = { context: "Confirmation" }), (K[3] = $));
-   else $ = K[3];
-   (i1("app:interrupt", O, $),
-     HPA(
-       `${q.workerName} needs permission for ${q.toolName}`,
-       "worker_permission_prompt",
-     ));
-   let _;
-   A: {
-     if (!iF2.includes(q.toolName)) {
-       _ = null;
-       break A;
-     }
-     let d = q.input;
-     if (
-       d &&
-       typeof d === "object" &&
-       "file_path" in d &&
-       typeof d.file_path === "string"
-     ) {
-       let o = d,
-         l;
-       if (K[4] !== o.file_path)
-         ((l = lF2(o.file_path)), (K[4] = o.file_path), (K[5] = l));
-       else l = K[5];
-       _ = l;
-       break A;
-     }
-     _ = null;
-   }
-   let Z = _,
-     G;
-   if (K[6] !== Z)
-     ((G = Z ? CPK(Z) || "this directory" : null), (K[6] = Z), (K[7] = G));
-   else G = K[7];
-   let W = G,
-     D = q.toolName === C5 ? "reads from" : "edits in",
-     j;
-   if (
-     K[8] !== Z ||
-     K[9] !== w ||
-     K[10] !== H ||
-     K[11] !== J ||
-     K[12] !== z ||
-     K[13] !== q.input
-   )
-     ((j = (d) => {
-       A: switch (d) {
-         case "yes": {
-           (w(q.input), z());
-           break A;
-         }
-         case "yes-team": {
-           if (Z && H) H(Z);
-           else w(q.input);
-           z();
-           break A;
-         }
-         case "no":
-           (J(), z());
-       }
-     }),
-       (K[8] = Z),
-       (K[9] = w),
-       (K[10] = H),
-       (K[11] = J),
-       (K[12] = z),
-       (K[13] = q.input),
-       (K[14] = j));
-   else j = K[14];
-   let M = j,
-     P;
-   if (K[15] === Symbol.for("react.memo_cache_sentinel"))
-     ((P = { label: "Yes, allow this action", value: "yes" }), (K[15] = P));
-   else P = K[15];
-   let V;
-   if (K[16] !== D || K[17] !== W || K[18] !== Z || K[19] !== H) {
-     if (((V = [P]), Z && H)) {
-       let o;
-       if (K[21] !== W) ((o = X1.bold(`${W}/`)), (K[21] = W), (K[22] = o));
-       else o = K[22];
-       let l = `Yes, allow all ${D} ${o} for all teammates`,
-         e;
-       if (K[23] !== l)
-         ((e = { label: l, value: "yes-team" }), (K[23] = l), (K[24] = e));
-       else e = K[24];
-       V.push(e);
-     }
-     let d;
-     if (K[25] === Symbol.for("react.memo_cache_sentinel"))
-       ((d = { label: "No, deny this action", value: "no" }), (K[25] = d));
-     else d = K[25];
-     (V.push(d),
-       (K[16] = D),
-       (K[17] = W),
-       (K[18] = Z),
-       (K[19] = H),
-       (K[20] = V));
-   } else V = K[20];
-   let N = V,
-     T;
-   A: {
-     if (q.toolName !== c5) {
-       T = null;
-       break A;
-     }
-     let d = q.input;
-     if (
-       d &&
-       typeof d === "object" &&
-       "file_path" in d &&
-       "old_string" in d &&
-       "new_string" in d &&
-       typeof d.file_path === "string" &&
-       typeof d.old_string === "string" &&
-       typeof d.new_string === "string"
-     ) {
-       T = d;
-       break A;
-     }
-     T = null;
-   }
-   let k = T,
-     R;
-   A: {
-     if (!q.input || typeof q.input !== "object") {
-       let o = String(q.input),
-         l;
-       if (K[26] !== o) ((l = [[null, o]]), (K[26] = o), (K[27] = l));
-       else l = K[27];
-       R = l;
-       break A;
-     }
-     let d;
-     if (K[28] !== q.input)
-       ((d = Object.entries(q.input).map(rF2)), (K[28] = q.input), (K[29] = d));
-     else d = K[29];
-     R = d;
-   }
-   let x = R,
-     S = `Worker permission request: ${q.toolName}`,
-     g = Y || q.workerColor || "cyan",
-     b;
-   if (K[30] !== q.workerName || K[31] !== g)
-     ((b = { name: q.workerName, color: g }),
-       (K[30] = q.workerName),
-       (K[31] = g),
-       (K[32] = b));
-   else b = K[32];
-   let Q = k ? 0 : 1,
-     F;
-   if (
-     K[33] !== k ||
-     K[34] !== x ||
-     K[35] !== M ||
-     K[36] !== N ||
-     K[37] !== q.description ||
-     K[38] !== q.toolName ||
-     K[39] !== q.workerName
-   )
-     ((F = k
-       ? WK.createElement(
-           WK.Fragment,
-           null,
-           WK.createElement(
-             I,
-             { flexDirection: "column", paddingX: 1, paddingY: 1 },
-             WK.createElement(
-               f,
-               null,
-               WK.createElement(f, { bold: !0 }, q.workerName),
-               WK.createElement(f, null, " wants to edit "),
-               WK.createElement(f, { bold: !0 }, CPK(k.file_path)),
-             ),
-           ),
-           WK.createElement(JPA, {
-             file_path: k.file_path,
-             edits: [
-               {
-                 old_string: k.old_string,
-                 new_string: k.new_string,
-                 replace_all: k.replace_all ?? !1,
-               },
-             ],
-           }),
-           WK.createElement(
-             I,
-             { flexDirection: "column", paddingX: 1 },
-             WK.createElement(f, null, "Do you want to allow this action?"),
-             WK.createElement(T6, {
-               options: N,
-               onChange: M,
-               onCancel: () => M("no"),
-             }),
-           ),
-         )
-       : WK.createElement(
-           WK.Fragment,
-           null,
-           WK.createElement(
-             I,
-             { flexDirection: "column", paddingX: 1, paddingY: 1 },
-             WK.createElement(
-               f,
-               null,
-               WK.createElement(f, { bold: !0 }, q.workerName),
-               WK.createElement(f, null, " wants to use "),
-               WK.createElement(f, { bold: !0 }, q.toolName),
-             ),
-             WK.createElement(f, { dimColor: !0 }, q.description),
-             WK.createElement(
-               I,
-               { marginTop: 1, flexDirection: "column" },
-               x.map(nF2),
-             ),
-           ),
-           WK.createElement(
-             I,
-             { flexDirection: "column", paddingX: 1 },
-             WK.createElement(f, null, "Do you want to allow this action?"),
-             WK.createElement(T6, {
-               options: N,
-               onChange: M,
-               onCancel: () => M("no"),
-             }),
-           ),
-         )),
-       (K[33] = k),
-       (K[34] = x),
-       (K[35] = M),
-       (K[36] = N),
-       (K[37] = q.description),
-       (K[38] = q.toolName),
-       (K[39] = q.workerName),
-       (K[40] = F));
-   else F = K[40];
-   let B;
-   if (K[41] !== b || K[42] !== Q || K[43] !== F || K[44] !== S)
-     ((B = WK.createElement(
-       P2,
-       { title: S, workerBadge: b, innerPaddingX: Q },
-       F,
-     )),
-       (K[41] = b),
-       (K[42] = Q),
-       (K[43] = F),
-       (K[44] = S),
-       (K[45] = B));
-   else B = K[45];
-   return B;
- }

--- Removed nF2 (pretty-v2.1.19.js:535816-535836)
- function nF2(A, K) {
-   let [q, Y] = A;
-   return WK.createElement(
-     f,
-     { key: K, dimColor: !0 },
-     q
-       ? WK.createElement(
-           WK.Fragment,
-           null,
-           WK.createElement(
-             f,
-             null,
-             q.charAt(0).toUpperCase() + q.slice(1),
-             ":",
-             " ",
-           ),
-           WK.createElement(f, null, Y),
-         )
-       : Y,
-   );
- }

--- Removed rF2 (pretty-v2.1.19.js:535837-535841)
- function rF2(A) {
-   let [K, q] = A,
-     Y = typeof q === "string" ? q : UA(q);
-   return [K, Y];
- }

--- Removed RPK (pretty-v2.1.19.js:535843-535855)
- var RPK = C(() => {
-   lA();
-   uA();
-   D8();
-   q9();
-   aM();
-   _T1();
-   H0();
-   ZT1();
-   Uq();
-   F1();
-   ((WK = r(JA(), 1)), (iF2 = [c5, C5]));
- });

--- Removed He (pretty-v2.1.19.js:536058-536072)
- var He = C(() => {
-   q6();
-   iO();
-   YP();
-   Z_();
-   b2();
-   MJ();
-   aq();
-   we();
-   BH();
-   F1();
-   A4();
-   ((uPK = r(JA(), 1)),
-     (mPK = { completion_type: "tool_use_single", language_name: "none" }));
- });

--- Removed VQ2 (pretty-v2.1.19.js:537407-537410)
- function VQ2(A, K) {
-   let q = A.toLowerCase().trimEnd();
-   return K.some((Y) => Y.toLowerCase().trimEnd() === q);
- }

--- Removed OVK (pretty-v2.1.19.js:538931-538943)
- function OVK(A) {
-   let K = a(2),
-     { visible: q, enabled: Y } = A;
-   if (!Y) return null;
-   let z = q ? "hide" : "explain",
-     w;
-   if (K[0] !== z)
-     ((w = oZ.default.createElement(f, { dimColor: !0 }, "ctrl+e to ", z)),
-       (K[0] = z),
-       (K[1] = w));
-   else w = K[1];
-   return w;
- }

--- Removed rQ2 (pretty-v2.1.19.js:539170-539582)
- function rQ2(A) {
-   let K = a(80),
-     {
-       toolUseConfirm: q,
-       toolUseContext: Y,
-       onDone: z,
-       onReject: w,
-       command: H,
-       description: J,
-     } = A,
-     [X] = p4(),
-     [O, $] = j6(),
-     _;
-   if (
-     K[0] !== q.description ||
-     K[1] !== q.input ||
-     K[2] !== q.tool.name ||
-     K[3] !== Y.messages
-   )
-     ((_ = {
-       toolName: q.tool.name,
-       toolInput: q.input,
-       toolDescription: q.description,
-       messages: Y.messages,
-     }),
-       (K[0] = q.description),
-       (K[1] = q.input),
-       (K[2] = q.tool.name),
-       (K[3] = Y.messages),
-       (K[4] = _));
-   else _ = K[4];
-   let Z = XVK(_),
-     [G, W] = gv.useState(!1),
-     [D, j] = gv.useState(""),
-     [M, P] = gv.useState(""),
-     [V, N] = gv.useState(J || ""),
-     T;
-   if (K[5] !== J) ((T = J?.trim()), (K[5] = J), (K[6] = T));
-   else T = K[6];
-   let [k, R] = gv.useState(!T),
-     { signal: x } = Y.abortController,
-     S,
-     g;
-   if (K[7] !== H || K[8] !== J || K[9] !== x)
-     ((S = () => {
-       if (!NS()) return;
-       n9K(H, J, x)
-         .then((tA) => {
-           if (tA && !x.aborted) (N(tA), R(!1));
-         })
-         .catch(sQ2);
-     }),
-       (g = [H, J, x]),
-       (K[7] = H),
-       (K[8] = J),
-       (K[9] = x),
-       (K[10] = S),
-       (K[11] = g));
-   else ((S = K[10]), (g = K[11]));
-   gv.useEffect(S, g);
-   let [b, Q] = gv.useState(!1),
-     [F, B] = gv.useState(!1),
-     [d, o] = gv.useState("yes"),
-     [l, e] = gv.useState(!1),
-     [XA, GA] = gv.useState(!1),
-     WA = l8.isSandboxingEnabled(),
-     ZA = WA && mjA(q.input),
-     t;
-   if (K[12] === Symbol.for("react.memo_cache_sentinel"))
-     ((t = { completion_type: "tool_use_single", language_name: "none" }),
-       (K[12] = t));
-   else t = K[12];
-   sf(q, t);
-   let VA;
-   if (K[13] !== O.toolPermissionContext)
-     ((VA = JV1(O.toolPermissionContext)),
-       (K[13] = O.toolPermissionContext),
-       (K[14] = VA));
-   else VA = K[14];
-   let MA = VA,
-     SA =
-       q.permissionResult.behavior === "ask"
-         ? q.permissionResult.suggestions
-         : void 0,
-     BA;
-   if (
-     K[15] !== V ||
-     K[16] !== MA ||
-     K[17] !== k ||
-     K[18] !== F ||
-     K[19] !== SA ||
-     K[20] !== q.permissionResult.decisionReason ||
-     K[21] !== b
-   )
-     ((BA = sPK({
-       suggestions: SA,
-       decisionReason: q.permissionResult.decisionReason,
-       onRejectFeedbackChange: j,
-       onAcceptFeedbackChange: P,
-       onClassifierDescriptionChange: N,
-       classifierDescription: V,
-       initialClassifierDescriptionEmpty: k,
-       existingAllowDescriptions: MA,
-       yesInputMode: b,
-       noInputMode: F,
-     })),
-       (K[15] = V),
-       (K[16] = MA),
-       (K[17] = k),
-       (K[18] = F),
-       (K[19] = SA),
-       (K[20] = q.permissionResult.decisionReason),
-       (K[21] = b),
-       (K[22] = BA));
-   else BA = K[22];
-   let s = BA,
-     AA;
-   if (K[23] === Symbol.for("react.memo_cache_sentinel"))
-     ((AA = () => {
-       W(aQ2);
-     }),
-       (K[23] = AA));
-   else AA = K[23];
-   let wA = AA,
-     KA;
-   if (K[24] === Symbol.for("react.memo_cache_sentinel"))
-     ((KA = { context: "Confirmation" }), (K[24] = KA));
-   else KA = K[24];
-   i1("permission:toggleDebug", wA, KA);
-   let zA;
-   if (K[25] !== F || K[26] !== q || K[27] !== b)
-     ((zA = function (O1) {
-       q.onUserInteraction();
-       let M1 = { toolName: VK(q.tool.name), isMcp: q.tool.isMcp ?? !1 };
-       if (O1 === "yes")
-         if (b) (Q(!1), n("tengu_accept_feedback_mode_collapsed", M1));
-         else (Q(!0), e(!0), n("tengu_accept_feedback_mode_entered", M1));
-       else if (O1 === "no")
-         if (F) (B(!1), n("tengu_reject_feedback_mode_collapsed", M1));
-         else (B(!0), GA(!0), n("tengu_reject_feedback_mode_entered", M1));
-     }),
-       (K[25] = F),
-       (K[26] = q),
-       (K[27] = b),
-       (K[28] = zA));
-   else zA = K[28];
-   let HA = zA,
-     vA;
-   if (K[29] !== z || K[30] !== w || K[31] !== $ || K[32] !== q)
-     ((vA = function (O1) {
-       let M1 = O1?.trim(),
-         u1 = !!M1;
-       if (!u1) (n("tengu_permission_request_escape", {}), $(oQ2));
-       if ((Rd("tool_use_single", q, "reject", u1), M1)) q.onReject(M1);
-       else q.onReject();
-       (w(), z());
-     }),
-       (K[29] = z),
-       (K[30] = w),
-       (K[31] = $),
-       (K[32] = q),
-       (K[33] = vA));
-   else vA = K[33];
-   let OA = vA,
-     LA;
-   if (
-     K[34] !== M ||
-     K[35] !== V ||
-     K[36] !== OA ||
-     K[37] !== XA ||
-     K[38] !== z ||
-     K[39] !== D ||
-     K[40] !== q ||
-     K[41] !== l
-   )
-     ((LA = function (O1) {
-       n("tengu_permission_request_option_selected", {
-         option_index: {
-           yes: 1,
-           "yes-apply-suggestions": 2,
-           "yes-classifier-reviewed": 3,
-           no: 4,
-         }[O1],
-       });
-       let u1 = VK(q.tool.name);
-       A: switch (O1) {
-         case "yes": {
-           let s1 = M.trim();
-           (Rd("tool_use_single", q, "accept"),
-             n("tengu_accept_submitted", {
-               toolName: u1,
-               isMcp: q.tool.isMcp ?? !1,
-               has_instructions: !!s1,
-               instructions_length: s1.length,
-               entered_feedback_mode: l,
-             }),
-             q.onAllow(q.input, [], s1 || void 0),
-             z());
-           break A;
-         }
-         case "yes-apply-suggestions": {
-           Rd("tool_use_single", q, "accept");
-           let s1 =
-             "suggestions" in q.permissionResult
-               ? q.permissionResult.suggestions || []
-               : [];
-           (q.onAllow(q.input, s1), z());
-           break A;
-         }
-         case "yes-classifier-reviewed": {
-           let s1 = V.trim();
-           if ((Rd("tool_use_single", q, "accept"), !s1)) {
-             (q.onAllow(q.input, []), z());
-             break A;
-           }
-           let H6 = [
-             {
-               type: "addRules",
-               rules: [{ toolName: c7.name, ruleContent: HV1(s1) }],
-               behavior: "allow",
-               destination: "session",
-             },
-           ];
-           (q.onAllow(q.input, H6), z());
-           break A;
-         }
-         case "no": {
-           let s1 = D.trim();
-           (n("tengu_reject_submitted", {
-             toolName: u1,
-             isMcp: q.tool.isMcp ?? !1,
-             has_instructions: !!s1,
-             instructions_length: s1.length,
-             entered_feedback_mode: XA,
-           }),
-             OA(s1 || void 0));
-         }
-       }
-     }),
-       (K[34] = M),
-       (K[35] = V),
-       (K[36] = OA),
-       (K[37] = XA),
-       (K[38] = z),
-       (K[39] = D),
-       (K[40] = q),
-       (K[41] = l),
-       (K[42] = LA));
-   else LA = K[42];
-   let FA = LA,
-     RA = WA && !ZA ? "Bash command (unsandboxed)" : "Bash command",
-     yA;
-   if (K[43] !== Z.enabled || K[44] !== Z.visible)
-     ((yA = QJ.default.createElement(OVK, {
-       visible: Z.visible,
-       enabled: Z.enabled,
-     })),
-       (K[43] = Z.enabled),
-       (K[44] = Z.visible),
-       (K[45] = yA));
-   else yA = K[45];
-   let rA = Z.visible,
-     w1;
-   if (K[46] !== H || K[47] !== J || K[48] !== X)
-     ((w1 = c7.renderToolUseMessage(
-       { command: H, description: J },
-       { theme: X, verbose: !0 },
-     )),
-       (K[46] = H),
-       (K[47] = J),
-       (K[48] = X),
-       (K[49] = w1));
-   else w1 = K[49];
-   let _1;
-   if (K[50] !== Z.visible || K[51] !== w1)
-     ((_1 = QJ.default.createElement(f, { dimColor: rA }, w1)),
-       (K[50] = Z.visible),
-       (K[51] = w1),
-       (K[52] = _1));
-   else _1 = K[52];
-   let N1;
-   if (K[53] !== Z.visible || K[54] !== q.description)
-     ((N1 =
-       !Z.visible &&
-       QJ.default.createElement(f, { dimColor: !0 }, q.description)),
-       (K[53] = Z.visible),
-       (K[54] = q.description),
-       (K[55] = N1));
-   else N1 = K[55];
-   let C1;
-   if (K[56] !== Z.promise || K[57] !== Z.visible)
-     ((C1 = QJ.default.createElement($VK, {
-       visible: Z.visible,
-       promise: Z.promise,
-     })),
-       (K[56] = Z.promise),
-       (K[57] = Z.visible),
-       (K[58] = C1));
-   else C1 = K[58];
-   let S1;
-   if (K[59] !== _1 || K[60] !== N1 || K[61] !== C1)
-     ((S1 = QJ.default.createElement(
-       I,
-       { flexDirection: "column", paddingX: 2, paddingY: 1 },
-       _1,
-       N1,
-       C1,
-     )),
-       (K[59] = _1),
-       (K[60] = N1),
-       (K[61] = C1),
-       (K[62] = S1));
-   else S1 = K[62];
-   let j1;
-   if (
-     K[63] !== M ||
-     K[64] !== d ||
-     K[65] !== HA ||
-     K[66] !== OA ||
-     K[67] !== F ||
-     K[68] !== FA ||
-     K[69] !== s ||
-     K[70] !== D ||
-     K[71] !== G ||
-     K[72] !== q ||
-     K[73] !== b
-   )
-     ((j1 = G
-       ? QJ.default.createElement(
-           QJ.default.Fragment,
-           null,
-           QJ.default.createElement(AVK, {
-             permissionResult: q.permissionResult,
-             toolName: "Bash",
-           }),
-           q.toolUseContext.options.debug &&
-             QJ.default.createElement(
-               I,
-               { justifyContent: "flex-end", marginTop: 1 },
-               QJ.default.createElement(
-                 f,
-                 { dimColor: !0 },
-                 "Ctrl-D to hide debug info",
-               ),
-             ),
-         )
-       : QJ.default.createElement(
-           QJ.default.Fragment,
-           null,
-           QJ.default.createElement(
-             I,
-             { flexDirection: "column" },
-             QJ.default.createElement(tf, {
-               permissionResult: q.permissionResult,
-               toolType: "command",
-             }),
-             QJ.default.createElement(f, null, "Do you want to proceed?"),
-             QJ.default.createElement(T6, {
-               options: s,
-               inlineDescriptions: !0,
-               onChange: FA,
-               onCancel: () => OA(),
-               onFocus: (tA) => {
-                 if (tA !== d) q.onUserInteraction();
-                 if (tA !== "yes" && b && !M.trim()) Q(!1);
-                 if (tA !== "no" && F && !D.trim()) B(!1);
-                 o(tA);
-               },
-               onInputModeToggle: HA,
-             }),
-           ),
-           QJ.default.createElement(
-             I,
-             { justifyContent: "space-between", marginTop: 1 },
-             QJ.default.createElement(
-               f,
-               { dimColor: !0 },
-               "Esc to cancel",
-               ((d === "yes" && !b) || (d === "no" && !F)) &&
-                 " · Tab to add additional instructions",
-             ),
-             q.toolUseContext.options.debug &&
-               QJ.default.createElement(
-                 f,
-                 { dimColor: !0 },
-                 "Ctrl+d to show debug info",
-               ),
-           ),
-         )),
-       (K[63] = M),
-       (K[64] = d),
-       (K[65] = HA),
-       (K[66] = OA),
-       (K[67] = F),
-       (K[68] = FA),
-       (K[69] = s),
-       (K[70] = D),
-       (K[71] = G),
-       (K[72] = q),
-       (K[73] = b),
-       (K[74] = j1));
-   else j1 = K[74];
-   let d1;
-   if (K[75] !== RA || K[76] !== yA || K[77] !== S1 || K[78] !== j1)
-     ((d1 = QJ.default.createElement(P2, { title: RA, titleRight: yA }, S1, j1)),
-       (K[75] = RA),
-       (K[76] = yA),
-       (K[77] = S1),
-       (K[78] = j1),
-       (K[79] = d1));
-   else d1 = K[79];
-   return d1;
- }

--- Removed oQ2 (pretty-v2.1.19.js:539583-539591)
- function oQ2(A) {
-   return {
-     ...A,
-     attribution: {
-       ...A.attribution,
-       escapeCount: A.attribution.escapeCount + 1,
-     },
-   };
- }

--- Removed QVK (pretty-v2.1.19.js:543289-543401)
- function QVK({ toolUseConfirm: A, onDone: K, onReject: q }) {
-   let Y = pmA.safeParse(A.input),
-     z = Y.success ? (Y.data.allowed_tools ?? FVK) : FVK,
-     w = Y.success ? Y.data.description : void 0,
-     H = Y.success ? Y.data.prompt : void 0;
-   sf(A, mPK);
-   let J = Ng6.useCallback(
-       (O, $) => {
-         switch (O) {
-           case "yes":
-             (Fw({
-               completion_type: "tool_use_single",
-               event: "accept",
-               metadata: {
-                 language_name: "none",
-                 message_id: A.assistantMessage.message.id,
-                 platform: S6.platform,
-               },
-             }),
-               A.onAllow(A.input, [], $),
-               K());
-             break;
-           case "yes-session": {
-             (Fw({
-               completion_type: "tool_use_single",
-               event: "accept",
-               metadata: {
-                 language_name: "none",
-                 message_id: A.assistantMessage.message.id,
-                 platform: S6.platform,
-               },
-             }),
-               A.onAllow(
-                 A.input,
-                 [
-                   {
-                     type: "addRules",
-                     rules: z.map((_) => ({ toolName: _ })),
-                     behavior: "allow",
-                     destination: "session",
-                   },
-                 ],
-                 $,
-               ),
-               K());
-             break;
-           }
-           case "no":
-             (Fw({
-               completion_type: "tool_use_single",
-               event: "reject",
-               metadata: {
-                 language_name: "none",
-                 message_id: A.assistantMessage.message.id,
-                 platform: S6.platform,
-               },
-             }),
-               A.onReject($),
-               q(),
-               K());
-             break;
-         }
-       },
-       [A, K, q, z],
-     ),
-     X = Ng6.useCallback(() => {
-       (Fw({
-         completion_type: "tool_use_single",
-         event: "reject",
-         metadata: {
-           language_name: "none",
-           message_id: A.assistantMessage.message.id,
-           platform: S6.platform,
-         },
-       }),
-         A.onReject(),
-         q(),
-         K());
-     }, [A, K, q]);
-   return Qv.default.createElement(
-     P2,
-     { title: "Agent tool permissions" },
-     Qv.default.createElement(
-       I,
-       { flexDirection: "column", paddingX: 2, paddingY: 1 },
-       Qv.default.createElement(f, null, "Agent requests tool permissions"),
-       w && Qv.default.createElement(f, { dimColor: !0 }, "Task: ", w),
-       Qv.default.createElement(
-         I,
-         { marginTop: 1, flexDirection: "column" },
-         Qv.default.createElement(f, { bold: !0 }, "Requested tools:"),
-         z.map((O) => Qv.default.createElement(f, { key: O }, " ", O)),
-       ),
-       H &&
-         Qv.default.createElement(
-           I,
-           { marginTop: 1, flexDirection: "column" },
-           Qv.default.createElement(f, { bold: !0 }, "Purpose:"),
-           Qv.default.createElement(f, { dimColor: !0 }, Wq1(H, 3)),
-         ),
-     ),
-     Qv.default.createElement(
-       I,
-       { flexDirection: "column" },
-       Qv.default.createElement($e, {
-         options: LU2,
-         onSelect: J,
-         onCancel: X,
-         toolAnalyticsContext: RU2,
-       }),
-     ),
-   );
- }

--- Removed UVK (pretty-v2.1.19.js:543403-543420)
- var UVK = C(() => {
-   uA();
-   aM();
-   we();
-   aq();
-   He();
-   dpA();
-   ZWA();
-   ((Qv = r(JA(), 1)),
-     (Ng6 = r(JA(), 1)),
-     (FVK = []),
-     (LU2 = [
-       { label: "Allow", value: "yes", feedbackConfig: { type: "accept" } },
-       { label: "Allow for session", value: "yes-session" },
-       { label: "Deny", value: "no", feedbackConfig: { type: "reject" } },
-     ]),
-     (RU2 = { toolName: l5, isMcp: !1 }));
- });

--- Removed yfK (pretty-v2.1.19.js:545586-545586)
-   yfK = 10,

--- Removed Dd2 (pretty-v2.1.19.js:551115-551120)
- function Dd2(A) {
-   return `<${A_}>
- <${IG}>+${A} more tasks completed</${IG}>
- <${yG}>completed</${yG}>
- </${A_}>`;
- }

--- Removed SvK (pretty-v2.1.19.js:555188-555214)
- function SvK({
-   isLoading: A,
-   queuedCommandsLength: K,
-   lastQueryCompletionTime: q,
-   getAppState: Y,
-   setAppState: z,
-   executeQueuedInput: w,
-   hasActiveLocalJsxUI: H,
-   setIsLoading: J,
- }) {
-   let X = tT1.useRef(!1);
-   tT1.useEffect(() => {
-     if (A) return;
-     if (K === 0) return;
-     if (H) return;
-     if (X.current) return;
-     ((X.current = !0),
-       J(!0),
-       yvK({ getAppState: Y, setAppState: z, executeInput: w })
-         .then((O) => {
-           if (!O.processed) J(!1);
-         })
-         .finally(() => {
-           X.current = !1;
-         }));
-   }, [A, K, q, Y, z, w, H, J]);
- }

--- Removed pvK (pretty-v2.1.19.js:555397-555434)
- function pvK({ idleStartTime: A, turnDurationMs: K }) {
-   let [q, Y] = fPA.useState(0),
-     [{ tasks: z, selectedIPAgentIndex: w, viewSelectionMode: H }] = j6(),
-     [J] = fPA.useState(() => eP(hWA)),
-     X = as(z).filter((M) => M.status === "running"),
-     O = X.length > 0,
-     $ = O && X.every((M) => M.isIdle),
-     _ = fPA.useRef(!1),
-     Z = fPA.useRef(null);
-   if ($ && !_.current) _.current = !0;
-   else if (!O) ((_.current = !1), (Z.current = null));
-   let G = _.current || $,
-     W = w3A(A ?? Date.now(), O && A !== null && !G);
-   if (G && Z.current === null) Z.current = Dw(K);
-   let D = G ? Z.current : W;
-   if ((zY(() => Y((M) => M + 1), O && !G ? 120 : null), !O)) return null;
-   return ud.createElement(
-     I,
-     { flexDirection: "column", width: "100%", alignItems: "flex-start" },
-     ud.createElement(
-       I,
-       { flexDirection: "row", marginTop: 1 },
-       ud.createElement(
-         f,
-         { dimColor: !0 },
-         G
-           ? `${da} ${J} for ${D} (shift+↑/↓ to select)`
-           : `${da} Idle for ${W} (shift+↑/↓ to select)`,
-       ),
-     ),
-     ud.createElement(yM1, {
-       frame: q,
-       selectedIndex: w,
-       isInSelectionMode: H === "selecting-agent",
-       allTeammatesIdle: G,
-     }),
-   );
- }

--- Removed aF6 (pretty-v2.1.19.js:565139-565146)
- function aF6(A) {
-   let K = Uo();
-   if (A === K.HOME) return "home";
-   if (A === K.DESKTOP || A.startsWith(K.DESKTOP + oF6)) return "desktop";
-   if (A === K.DOCUMENTS || A.startsWith(K.DOCUMENTS + oF6)) return "documents";
-   if (A === K.DOWNLOADS || A.startsWith(K.DOWNLOADS + oF6)) return "downloads";
-   return "other";
- }

--- Removed NdA (pretty-v2.1.19.js:565179-565192)
- function NdA(A, K) {
-   if (A.length === 0) return "";
-   let q = K === 0 ? void 0 : K;
-   if (!q || A.length <= q) {
-     if (A.length === 1) return A[0];
-     if (A.length === 2) return `${A[0]} and ${A[1]}`;
-     let w = A[A.length - 1];
-     return `${A.slice(0, -1).join(", ")}, and ${w}`;
-   }
-   let Y = A.slice(0, q),
-     z = A.length - q;
-   if (Y.length === 1) return `${Y[0]} and ${z} more`;
-   return `${Y.join(", ")}, and ${z} more`;
- }

--- Removed ESK (pretty-v2.1.19.js:565245-565292)
- var ESK = C(() => {
-   vSK = {
-     control: {
-       title: "Do you trust the files in this folder?",
-       bodyText: null,
-       showDetailedPermissions: !0,
-       learnMoreText: "Learn more",
-       yesButtonLabel: "Yes, proceed",
-       noButtonLabel: "No, exit",
-     },
-     variant_positive_attitude: {
-       title: "Ready to code here?",
-       bodyText: `I'll need permission to work with your files.
- 
- This means I can:
- - Read any file in this folder
- - Create, edit, or delete files
- - Run commands (like npm, git, tests, ls, rm)
- - Use tools defined in .mcp.json`,
-       showDetailedPermissions: !1,
-       learnMoreText: "Learn more",
-       yesButtonLabel: "Yes, continue",
-       noButtonLabel: "No, exit",
-     },
-     variant_normalize_action: {
-       title: "Accessing workspace:",
-       bodyText: `Quick safety check: Is this a project you created or one you trust? (Like your own code, a well-known open source project, or work from your team). If not, take a moment to review what's in this folder first.
- 
- Claude Code'll be able to read, edit, and execute files here.`,
-       showDetailedPermissions: !1,
-       learnMoreText: "Security guide",
-       yesButtonLabel: "Yes, I trust this folder",
-       noButtonLabel: "No, exit",
-     },
-     variant_explicit: {
-       title: "Do you want to work in this folder?",
-       bodyText: `In order to work in this folder, we need your permission for Claude Code to read, edit, and execute files.
- 
- If this folder has malicious code or untrusted scripts, Claude Code could run them while trying to help.
- 
- Only continue if this is your code or a project you trust.`,
-       showDetailedPermissions: !1,
-       learnMoreText: "Security details",
-       yesButtonLabel: "Yes, continue",
-       noButtonLabel: "No, exit",
-     },
-   };
- });

--- Removed CSK (pretty-v2.1.19.js:565294-565670)
- function CSK(A) {
-   let K = a(46),
-     { onDone: q, commands: Y } = A,
-     z;
-   if (K[0] === Symbol.for("react.memo_cache_sentinel"))
-     ((z = oX("project")), (K[0] = z));
-   else z = K[0];
-   let { servers: w } = z,
-     H;
-   if (K[1] === Symbol.for("react.memo_cache_sentinel"))
-     ((H = Bk("trust_folder_dialog_copy", "variant", "control")), (K[1] = H));
-   else H = K[1];
-   let J = H,
-     X = vSK[J],
-     O;
-   if (K[2] === Symbol.for("react.memo_cache_sentinel"))
-     ((O = Object.keys(w)), (K[2] = O));
-   else O = K[2];
-   let $ = O.length > 0,
-     _,
-     Z,
-     G,
-     W,
-     D,
-     j,
-     M;
-   if (K[3] === Symbol.for("react.memo_cache_sentinel")) {
-     let _1 = jSK();
-     ((D = _1.length > 0), (_ = MSK()));
-     let N1 = VSK();
-     Z = N1.length > 0;
-     let C1 = fSK();
-     G = C1.length > 0;
-     let S1 = PSK();
-     j = S1.length > 0;
-     let j1 = NSK();
-     ((W = j1.length > 0),
-       (M = [...new Set([..._1, ..._, ...N1, ...C1, ...S1, ...j1])]),
-       (K[3] = _),
-       (K[4] = Z),
-       (K[5] = G),
-       (K[6] = W),
-       (K[7] = D),
-       (K[8] = j),
-       (K[9] = M));
-   } else
-     ((_ = K[3]),
-       (Z = K[4]),
-       (G = K[5]),
-       (W = K[6]),
-       (D = K[7]),
-       (j = K[8]),
-       (M = K[9]));
-   let P = M,
-     V = Y?.filter(vi2) ?? [],
-     N = Y?.filter(Ni2) ?? [],
-     T = V.length > 0,
-     k = N.length > 0,
-     R = V.map(fi2),
-     x = N.map(Vi2),
-     S = _.length > 0 || T || k,
-     g = $ || D || S || Z || G || j || W,
-     b = jw(D || S || Z || G || j || W),
-     Q,
-     F;
-   if (K[10] === Symbol.for("react.memo_cache_sentinel"))
-     ((Q = () => $),
-       (F = () => {
-         let _1 = {
-           enabledMcpjsonServers: Object.keys(w),
-           enableAllProjectMcpServers: !0,
-         };
-         I4("localSettings", _1);
-       }),
-       (K[10] = Q),
-       (K[11] = F));
-   else ((Q = K[10]), (F = K[11]));
-   let B;
-   if (K[12] !== S)
-     ((B = [
-       { name: "MCP servers", shouldShowWarning: Q, onChange: F },
-       { name: "hooks", shouldShowWarning: () => D },
-       { name: "bash commands", shouldShowWarning: () => S },
-       {
-         name: "OpenTelemetry headers helper commands",
-         shouldShowWarning: () => j,
-       },
-       { name: "dangerous environment variables", shouldShowWarning: () => W },
-     ].filter(Pi2)),
-       (K[12] = S),
-       (K[13] = B));
-   else B = K[13];
-   let d = B,
-     o;
-   if (K[14] !== d) ((o = new Set(d.map(Mi2))), (K[14] = d), (K[15] = o));
-   else o = K[15];
-   let l = o,
-     e = Object.keys(w),
-     XA;
-   if (K[16] !== l)
-     ((XA = function () {
-       let N1 = ["files"];
-       if (l.has("MCP servers")) N1.push("MCP servers");
-       if (l.has("hooks")) N1.push("hooks");
-       if (l.has("bash commands")) N1.push("bash commands");
-       if (l.has("OpenTelemetry headers helper commands"))
-         N1.push("OpenTelemetry headers helper commands");
-       if (l.has("dangerous environment variables"))
-         N1.push("environment variables");
-       return NdA(N1);
-     }),
-       (K[16] = l),
-       (K[17] = XA));
-   else XA = K[17];
-   let GA = XA,
-     WA,
-     ZA;
-   if (K[18] !== S)
-     ((WA = () => {
-       let _1 = kSK() === m1();
-       n("tengu_trust_dialog_shown", {
-         isHomeDir: _1,
-         hasMcpServers: $,
-         hasHooks: D,
-         hasBashExecution: S,
-         hasApiKeyHelper: Z,
-         hasAwsCommands: G,
-         hasOtelHeadersHelper: j,
-         hasDangerousEnvVars: W,
-         folderType: aF6(m1()),
-         copyVariant: J,
-       });
-     }),
-       (ZA = [$, D, S, Z, G, j, W, J]),
-       (K[18] = S),
-       (K[19] = WA),
-       (K[20] = ZA));
-   else ((WA = K[19]), (ZA = K[20]));
-   KY.default.useEffect(WA, ZA);
-   let t;
-   if (K[21] !== d || K[22] !== S || K[23] !== q)
-     ((t = function (N1) {
-       if (N1 === "exit") {
-         Hq(1);
-         return;
-       }
-       let C1 = kSK() === m1();
-       if (
-         (n("tengu_trust_dialog_accept", {
-           isHomeDir: C1,
-           hasMcpServers: $,
-           hasHooks: D,
-           hasBashExecution: S,
-           hasApiKeyHelper: Z,
-           hasAwsCommands: G,
-           hasOtelHeadersHelper: j,
-           hasDangerousEnvVars: W,
-           enableMcp: !0,
-           folderType: aF6(m1()),
-           copyVariant: J,
-         }),
-         C1)
-       )
-         Mc6(!0);
-       else Mz(ji2);
-       (d.forEach(Di2), q());
-     }),
-       (K[21] = d),
-       (K[22] = S),
-       (K[23] = q),
-       (K[24] = t));
-   else t = K[24];
-   let $A = t,
-     VA = W8(),
-     MA;
-   if (K[25] === Symbol.for("react.memo_cache_sentinel"))
-     ((MA = { context: "Confirmation" }), (K[25] = MA));
-   else MA = K[25];
-   if ((i1("confirm:no", Wi2, MA), b)) return (setTimeout(q), null);
-   let SA = P2,
-     BA = "warning",
-     s = "warning",
-     AA = I,
-     wA = "column",
-     KA = 1,
-     zA = 1,
-     HA;
-   if (K[26] === Symbol.for("react.memo_cache_sentinel"))
-     ((HA = KY.default.createElement(f, { bold: !0 }, hA().cwd())),
-       (K[26] = HA));
-   else HA = K[26];
-   let vA;
-   if (K[27] !== GA)
-     ((vA =
-       X.bodyText !== null
-         ? KY.default.createElement(f, null, X.bodyText)
-         : KY.default.createElement(
-             f,
-             null,
-             "Claude Code may read, write, or execute files contained in this directory. This can pose security risks, so only use",
-             " ",
-             GA(),
-             " from trusted sources.",
-           )),
-       (K[27] = GA),
-       (K[28] = vA));
-   else vA = K[28];
-   let OA =
-       X.showDetailedPermissions &&
-       g &&
-       KY.default.createElement(
-         I,
-         { flexDirection: "column", gap: 1 },
-         KY.default.createElement(f, { dimColor: !0 }, "Execution allowed by:"),
-         $ &&
-           KY.default.createElement(
-             I,
-             { paddingLeft: 2 },
-             KY.default.createElement(
-               f,
-               null,
-               KY.default.createElement(f, { dimColor: !0 }, "• "),
-               KY.default.createElement(f, { bold: !0 }, ".mcp.json"),
-               e.length > 0 &&
-                 KY.default.createElement(
-                   f,
-                   { dimColor: !0 },
-                   " ",
-                   "(",
-                   NdA(e, 3),
-                   ")",
-                 ),
-             ),
-           ),
-         P.length > 0 &&
-           KY.default.createElement(
-             I,
-             { paddingLeft: 2 },
-             KY.default.createElement(
-               f,
-               null,
-               KY.default.createElement(f, { dimColor: !0 }, "• "),
-               KY.default.createElement(f, { bold: !0 }, P.join(", ")),
-             ),
-           ),
-         T &&
-           KY.default.createElement(
-             I,
-             { paddingLeft: 2 },
-             KY.default.createElement(
-               f,
-               null,
-               KY.default.createElement(f, { dimColor: !0 }, "• "),
-               KY.default.createElement(f, { bold: !0 }, ".claude/commands"),
-               KY.default.createElement(
-                 f,
-                 { dimColor: !0 },
-                 " ",
-                 "(",
-                 NdA(R, 3),
-                 ")",
-               ),
-             ),
-           ),
-         k &&
-           KY.default.createElement(
-             I,
-             { paddingLeft: 2 },
-             KY.default.createElement(
-               f,
-               null,
-               KY.default.createElement(f, { dimColor: !0 }, "• "),
-               KY.default.createElement(f, { bold: !0 }, ".claude/skills"),
-               KY.default.createElement(
-                 f,
-                 { dimColor: !0 },
-                 " (",
-                 NdA(x, 3),
-                 ")",
-               ),
-             ),
-           ),
-       ),
-     LA;
-   if (K[29] === Symbol.for("react.memo_cache_sentinel"))
-     ((LA = KY.default.createElement(
-       f,
-       { dimColor: !0 },
-       KY.default.createElement(
-         M7,
-         { url: "https://code.claude.com/docs/en/security" },
-         X.learnMoreText,
-       ),
-     )),
-       (K[29] = LA));
-   else LA = K[29];
-   let FA;
-   if (K[30] === Symbol.for("react.memo_cache_sentinel"))
-     ((FA = [
-       { label: X.yesButtonLabel, value: "enable_all" },
-       { label: X.noButtonLabel, value: "exit" },
-     ]),
-       (K[30] = FA));
-   else FA = K[30];
-   let RA;
-   if (K[31] !== $A)
-     ((RA = KY.default.createElement(T6, {
-       options: FA,
-       onChange: (_1) => $A(_1),
-       onCancel: () => $A("exit"),
-     })),
-       (K[31] = $A),
-       (K[32] = RA));
-   else RA = K[32];
-   let yA;
-   if (K[33] !== VA.keyName || K[34] !== VA.pending)
-     ((yA = KY.default.createElement(
-       f,
-       { dimColor: !0 },
-       VA.pending
-         ? KY.default.createElement(
-             KY.default.Fragment,
-             null,
-             "Press ",
-             VA.keyName,
-             " again to exit",
-           )
-         : KY.default.createElement(
-             KY.default.Fragment,
-             null,
-             "Enter to confirm · Esc to cancel",
-           ),
-     )),
-       (K[33] = VA.keyName),
-       (K[34] = VA.pending),
-       (K[35] = yA));
-   else yA = K[35];
-   let rA;
-   if (
-     K[36] !== AA ||
-     K[37] !== HA ||
-     K[38] !== vA ||
-     K[39] !== OA ||
-     K[40] !== RA ||
-     K[41] !== yA
-   )
-     ((rA = KY.default.createElement(
-       AA,
-       { flexDirection: wA, gap: KA, paddingTop: zA },
-       HA,
-       vA,
-       OA,
-       LA,
-       RA,
-       yA,
-     )),
-       (K[36] = AA),
-       (K[37] = HA),
-       (K[38] = vA),
-       (K[39] = OA),
-       (K[40] = RA),
-       (K[41] = yA),
-       (K[42] = rA));
-   else rA = K[42];
-   let w1;
-   if (K[43] !== SA || K[44] !== rA)
-     ((w1 = KY.default.createElement(
-       SA,
-       { color: BA, titleColor: s, title: X.title },
-       rA,
-     )),
-       (K[43] = SA),
-       (K[44] = rA),
-       (K[45] = w1));
-   else w1 = K[45];
-   return w1;
- }

--- Removed mSK (pretty-v2.1.19.js:566250-566253)
- function mSK(A) {
-   let K = A.slice(A.lastIndexOf(".")).toLowerCase();
-   return Ii2.has(K);
- }

--- Removed gSK (pretty-v2.1.19.js:566254-566263)
- function gSK(A) {
-   let K = Math.min(A.length, Si2),
-     q = 0;
-   for (let Y = 0; Y < K; Y++) {
-     let z = A[Y];
-     if (z === 0) return !0;
-     if (z < 32 && z !== 9 && z !== 10 && z !== 13) q++;
-   }
-   return q / K > 0.1;
- }

--- Removed Si2 (pretty-v2.1.19.js:566265-566265)
-   Si2 = 8192;

--- Removed FSK (pretty-v2.1.19.js:566266-566323)
- var FSK = C(() => {
-   Ii2 = new Set([
-     ".png",
-     ".jpg",
-     ".jpeg",
-     ".gif",
-     ".bmp",
-     ".ico",
-     ".webp",
-     ".svg",
-     ".tiff",
-     ".tif",
-     ".mp4",
-     ".mov",
-     ".avi",
-     ".mkv",
-     ".webm",
-     ".mp3",
-     ".wav",
-     ".ogg",
-     ".flac",
-     ".zip",
-     ".tar",
-     ".gz",
-     ".bz2",
-     ".7z",
-     ".rar",
-     ".exe",
-     ".dll",
-     ".so",
-     ".dylib",
-     ".bin",
-     ".o",
-     ".a",
-     ".pdf",
-     ".doc",
-     ".docx",
-     ".xls",
-     ".xlsx",
-     ".ppt",
-     ".pptx",
-     ".ttf",
-     ".otf",
-     ".woff",
-     ".woff2",
-     ".eot",
-     ".pyc",
-     ".pyo",
-     ".class",
-     ".jar",
-     ".war",
-     ".node",
-     ".wasm",
-     ".sqlite",
-     ".db",
-     ".data",
-   ]);
- });

--- Removed QSK (pretty-v2.1.19.js:566324-566326)
- function QSK(A) {
-   return /\bgit\s+commit(?:\s|$)/.test(A);
- }

--- Removed USK (pretty-v2.1.19.js:566327-566338)
- function USK(A, K, q) {
-   if (q !== void 0) return q === 0;
-   let Y = [
-       /\[\w+[^\]]*\]\s+/,
-       /create mode/,
-       /\d+ files? changed/,
-       /\d+ insertions?/,
-       /\d+ deletions?/,
-     ],
-     z = A + K;
-   return Y.some((w) => w.test(z));
- }

--- Removed hi2 (pretty-v2.1.19.js:566339-566358)
- async function hi2() {
-   let A = t6();
-   try {
-     let K = await F4(
-       "git",
-       ["diff-tree", "--root", "--no-commit-id", "--name-only", "-r", "HEAD"],
-       { cwd: A, timeout: 5000 },
-     );
-     if (K.code === 0 && K.stdout)
-       return K.stdout
-         .split(
-           `
- `,
-         )
-         .filter(Boolean);
-   } catch (K) {
-     qA(K);
-   }
-   return [];
- }

--- Removed bi2 (pretty-v2.1.19.js:566359-566372)
- async function bi2() {
-   let A = t6();
-   try {
-     let K = await F4("git", ["log", "-1", "--format=%B"], {
-       cwd: A,
-       timeout: 5000,
-     });
-     if (K.code === 0 && K.stdout)
-       return K.stdout.includes("Claude-Generated-By:");
-   } catch (K) {
-     qA(K);
-   }
-   return !1;
- }

--- Removed xi2 (pretty-v2.1.19.js:566373-566393)
- function xi2(A) {
-   let K = A;
-   return (
-     (K = K.replace(/^Claude-Generated-By:.*$/gm, "")),
-     (K = K.replace(/^Claude-Steers:.*$/gm, "")),
-     (K = K.replace(/^Claude-Permission-Prompts:.*$/gm, "")),
-     (K = K.replace(/^Claude-Escapes:.*$/gm, "")),
-     (K = K.replace(/^Claude-Session:.*$/gm, "")),
-     (K = K.replace(
-       /\nClaude-Plan:\n<claude-plan>[\s\S]*?<\/claude-plan>/g,
-       "",
-     )),
-     (K = K.replace(
-       /\n{3,}/g,
-       `
- 
- `,
-     ).trim()),
-     K
-   );
- }

--- Removed Bi2 (pretty-v2.1.19.js:566394-566396)
- function Bi2(A) {
-   return /\bgit\s+commit\b.*--amend/.test(A);
- }

--- Removed ui2 (pretty-v2.1.19.js:566397-566403)
- function ui2() {
-   let A = process.env.CLAUDE_CODE_REMOTE_SESSION_ID;
-   if (!A) return null;
-   let K = process.env.SESSION_INGRESS_URL;
-   if (K?.includes("localhost")) return null;
-   return `Claude-Session: ${uWA(A, K)}`;
- }

--- Removed mi2 (pretty-v2.1.19.js:566404-566465)
- async function mi2(A, K = !1) {
-   let q = t6();
-   try {
-     let Y = await F4("git", ["log", "-1", "--format=%B"], {
-       cwd: q,
-       timeout: 5000,
-     });
-     if (Y.code !== 0) return !1;
-     let z = Y.stdout.trim();
-     if (
-       (h(`Attribution: currentMessage length=${z.length}`),
-       h(`Attribution: currentMessage:
- ${z}`),
-       K)
-     )
-       z = xi2(z);
-     let w = /^[A-Za-z][A-Za-z0-9-]*:\s+.+$/,
-       H = z.split(`
- `),
-       J = -1;
-     for (let $ = H.length - 1; $ >= 0; $--) {
-       let _ = H[$];
-       if (_ === "") {
-         if (J > $) J = $ + 1;
-         break;
-       }
-       if (w.test(_)) J = $;
-       else {
-         J = -1;
-         break;
-       }
-     }
-     let X;
-     if (J > 0 && A.length > 0)
-       X =
-         z +
-         `
- ` +
-         A.join(`
- `);
-     else if (A.length > 0)
-       X =
-         z +
-         `
- 
- ` +
-         A.join(`
- `);
-     else X = z;
-     h(`Attribution: newMessage:
- ${X}`);
-     let O = await F4("git", ["commit", "--amend", "-m", X], {
-       cwd: q,
-       timeout: 1e4,
-     });
-     if (O.code === 0)
-       return (h("Attribution: Successfully amended commit with trailers"), !0);
-     else return (h(`Attribution: Failed to amend commit: ${O.stderr}`), !1);
-   } catch (Y) {
-     return (qA(Y), !1);
-   }
- }

--- Removed pSK (pretty-v2.1.19.js:566466-566522)
- async function pSK(A, K) {
-   h(
-     `Attribution: handlePostCommitAttribution called with ${A.fileStates.size} tracked files`,
-   );
-   try {
-     if (await Jp7())
-       return (
-         h("Attribution: Skipping - transient git state"),
-         { success: !1 }
-       );
-     if (!(await YW1())) return { success: !1 };
-     let Y = K ? Bi2(K) : !1,
-       z = await bi2();
-     if (z && !Y)
-       return (
-         h("Attribution: Skipping - commit already has trailers"),
-         { success: !1 }
-       );
-     let w = z && Y;
-     if (w)
-       h(
-         "Attribution: Amend detected - will recalculate and replace existing trailers",
-       );
-     let H = await hi2();
-     if (H.length === 0)
-       return (h("Attribution: Skipping - no files in commit"), { success: !1 });
-     let J = await dv6([A], H);
-     if (J.summary.claudePercent === 0)
-       return (
-         h("Attribution: Skipping - 0% Claude contribution"),
-         { success: !1 }
-       );
-     let X = [],
-       O = Hp7(J);
-     if (O) X.push(O);
-     let $ = Math.max(0, A.promptCount - A.promptCountAtLastCommit - 1);
-     X.push(`Claude-Steers: ${$}`);
-     let _ = A.permissionPromptCount - A.permissionPromptCountAtLastCommit;
-     X.push(`Claude-Permission-Prompts: ${_}`);
-     let Z = A.escapeCount - A.escapeCountAtLastCommit;
-     X.push(`Claude-Escapes: ${Z}`);
-     let G = ui2();
-     if (G) X.push(G);
-     if (X.length > 0) {
-       if (await mi2(X, w))
-         return {
-           success: !0,
-           newPromptCountAtLastCommit: A.promptCount,
-           newPermissionPromptCountAtLastCommit: A.permissionPromptCount,
-           newEscapeCountAtLastCommit: A.escapeCount,
-         };
-     }
-     return { success: !1 };
-   } catch (q) {
-     return (qA(q), { success: !1 });
-   }
- }

--- Removed Fi2 (pretty-v2.1.19.js:566533-566539)
- async function Fi2(A, K, q) {
-   let Y = TdA.get(A);
-   if (Y && Y.mtime === q) return (Y.refCount++, Y.content);
-   let z = await K(A);
-   if (z) TdA.set(A, { content: z, mtime: q, refCount: 1 });
-   return z;
- }

--- Removed sF6 (pretty-v2.1.19.js:566546-566548)
- function sF6(A) {
-   for (let K of A) Qi2(K);
- }

--- Removed iSK (pretty-v2.1.19.js:566549-566562)
- function iSK(A) {
-   let K = new Map(),
-     q = A.split(
-       `
- `,
-     ).filter(Boolean);
-   for (let Y of q) {
-     let z = Y.slice(0, 2),
-       w = Y.slice(3);
-     if (w.startsWith('"') && w.endsWith('"')) w = w.slice(1, -1);
-     K.set(w, z);
-   }
-   return K;
- }

--- Removed Ui2 (pretty-v2.1.19.js:566563-566571)
- async function Ui2() {
-   let A = t6(),
-     K = await F4("git", ["--no-optional-locks", "status", "--porcelain"], {
-       cwd: A,
-       timeout: 5000,
-     });
-   if (K.code !== 0) return new Map();
-   return iSK(K.stdout);
- }

--- Removed tF6 (pretty-v2.1.19.js:566582-566612)
- async function tF6(A) {
-   if (mSK(A))
-     return (h(`Attribution hook: Skipping binary extension file ${A}`), "");
-   let K = t6(),
-     q = AQ6(K, A);
-   try {
-     let Y = await eF6(q);
-     if (Y.isDirectory()) return "";
-     if (Y.size > di2)
-       return (
-         h(`Attribution hook: Skipping large file ${A} (${Y.size} bytes)`),
-         ""
-       );
-     let z = await gi2(q, "r");
-     try {
-       let w = Buffer.alloc(Math.min(bv1, Y.size));
-       if ((await z.read(w, 0, w.length, 0), gSK(w)))
-         return (h(`Attribution hook: Skipping binary content file ${A}`), "");
-       if (Y.size <= bv1) return w.toString("utf-8");
-       let H = Buffer.alloc(Y.size - bv1);
-       return (
-         await z.read(H, 0, H.length, bv1),
-         w.toString("utf-8") + H.toString("utf-8")
-       );
-     } finally {
-       await z.close();
-     }
-   } catch {
-     return "";
-   }
- }

--- Removed cSK (pretty-v2.1.19.js:566613-566618)
- async function cSK(A) {
-   let K = t6(),
-     q = await F4("git", ["show", `HEAD:${A}`], { cwd: K, timeout: 5000 });
-   if (q.code !== 0) return "";
-   return q.stdout;
- }

--- Removed KQ6 (pretty-v2.1.19.js:566619-566637)
- async function KQ6(A, K, q, Y, z) {
-   h(`Attribution hook: Tracking file modification for ${K}`);
-   let w = await A.getAppState(),
-     H = w.mainLoopModelForSession ?? w.mainLoopModel ?? Y8A(),
-     J = Pz(H),
-     X = pv6(zW1(), J),
-     O = w.attribution;
-   A.setAppState(($) => {
-     let _ = { ...$.attribution, surface: X };
-     O = JW1(_, K, q, Y, z);
-     let Z = cv6(O, lSK());
-     return (
-       aI6(Z).catch((G) => {
-         h(`Attribution hook: Failed to save snapshot: ${G}`);
-       }),
-       { ...$, attribution: O }
-     );
-   });
- }

--- Removed ii2 (pretty-v2.1.19.js:566654-566677)
- async function ii2(A, K, q, Y, z) {
-   if (A.hook_event_name !== "PostToolUse") return {};
-   if (!z?.setAppState || !z?.getAppState)
-     return (
-       h("Attribution hook: No setAppState/getAppState available, skipping"),
-       {}
-     );
-   let w = wD1.safeParse(A.tool_response);
-   if (!w.success)
-     return (
-       h(`Attribution hook: Failed to parse Edit response: ${w.error.message}`),
-       {}
-     );
-   let {
-       filePath: H,
-       originalFile: J,
-       oldString: X,
-       newString: O,
-       replaceAll: $,
-       userModified: _,
-     } = w.data,
-     Z = GO1(J, X, O, $);
-   return (KQ6(z, H, J, Z, _), {});
- }

--- Removed ri2 (pretty-v2.1.19.js:566702-566730)
- async function ri2(A, K, q, Y, z) {
-   if (A.hook_event_name !== "PreToolUse") return {};
-   if (!K) return {};
-   let w = await Ui2(),
-     H = Array.from(w.entries())
-       .filter(([$, _]) => !_.startsWith("?"))
-       .map(([$]) => $),
-     J = new Set(),
-     X = t6(),
-     O = H.map(async ($) => {
-       let _ = AQ6(X, $);
-       try {
-         let Z = await eF6(_);
-         if (Z.size > ci2) {
-           h(
-             `Attribution hook: Skipping large file ${$} (${Z.size} bytes) in PreToolUse`,
-           );
-           return;
-         }
-         if (await Fi2($, tF6, Z.mtimeMs)) J.add($);
-       } catch {}
-     });
-   return (
-     await Promise.all(O),
-     v9A.set(K, { gitStatus: w, cachedFiles: J }),
-     h(`Attribution hook: Captured git status for bash ${K} (${w.size} files)`),
-     {}
-   );
- }

--- Removed oi2 (pretty-v2.1.19.js:566731-566811)
- async function oi2(A, K) {
-   let q = v9A.get(A);
-   if (!q) {
-     h(`Attribution hook: No pre-state found for bash ${A}`);
-     return;
-   }
-   v9A.delete(A);
-   let Y = await pi2(),
-     z = q.gitStatus,
-     w = q.cachedFiles,
-     H = (Z) => {
-       return TdA.get(Z)?.content;
-     },
-     J = [];
-   try {
-     for (let [Z, G] of Y) {
-       let W = z.get(Z);
-       if (W !== G) {
-         let D = await tF6(Z);
-         if (W === void 0 && G === "??")
-           J.push({ path: Z, type: "created", oldContent: "", newContent: D });
-         else if (G?.includes("D")) {
-           let j = H(Z);
-           if (j === void 0 && W === void 0) j = await cSK(Z);
-           ((j = j ?? ""),
-             J.push({
-               path: Z,
-               type: "deleted",
-               oldContent: j,
-               newContent: "",
-             }));
-         } else {
-           let j = H(Z);
-           if (j === void 0 && W === void 0) j = await cSK(Z);
-           if (((j = j ?? ""), D !== j))
-             J.push({ path: Z, type: "modified", oldContent: j, newContent: D });
-         }
-       }
-     }
-     for (let [Z, G] of z)
-       if (!Y.has(Z)) {
-         if ((await tF6(Z)) === "") {
-           let D = t6(),
-             j = AQ6(D, Z);
-           try {
-             await eF6(j);
-           } catch {
-             let M = H(Z) ?? "";
-             J.push({ path: Z, type: "deleted", oldContent: M, newContent: "" });
-           }
-         }
-       }
-   } finally {
-     sF6(w);
-   }
-   if (J.length === 0) {
-     h(`Attribution hook: No file changes detected for bash ${A}`);
-     return;
-   }
-   h(`Attribution hook: Detected ${J.length} file changes from bash ${A}`);
-   let X = await K.getAppState(),
-     O = X.mainLoopModelForSession ?? X.mainLoopModel ?? Y8A(),
-     $ = Pz(O),
-     _ = pv6(zW1(), $);
-   K.setAppState((Z) => {
-     let G = { ...Z.attribution, surface: _ };
-     for (let D of J) {
-       let j = wW1(D.path);
-       if (D.type === "created") G = zp7(G, j, D.newContent);
-       else if (D.type === "deleted") G = wp7(G, j, D.oldContent);
-       else G = JW1(G, j, D.oldContent, D.newContent, !1);
-     }
-     let W = cv6(G, lSK());
-     return (
-       aI6(W).catch((D) => {
-         h(`Attribution hook: Failed to save snapshot: ${D}`);
-       }),
-       { ...Z, attribution: G }
-     );
-   });
- }

--- Removed ai2 (pretty-v2.1.19.js:566812-566858)
- async function ai2(A, K, q, Y, z) {
-   if (A.hook_event_name !== "PostToolUse") return {};
-   let w = _V1.safeParse(A.tool_input);
-   if (!w.success) return {};
-   let { command: H } = w.data,
-     J = $h6.safeParse(A.tool_response);
-   if (!J.success) {
-     if (
-       (h(`Attribution hook: Failed to parse Bash response: ${J.error.message}`),
-       K)
-     ) {
-       let $ = v9A.get(K);
-       if ($) (sF6($.cachedFiles), v9A.delete(K));
-     }
-     return {};
-   }
-   let { stdout: X, stderr: O } = J.data;
-   if (!z?.getAppState || !z?.setAppState) {
-     if (
-       (h("Attribution hook: No getAppState/setAppState available, skipping"), K)
-     ) {
-       let $ = v9A.get(K);
-       if ($) (sF6($.cachedFiles), v9A.delete(K));
-     }
-     return {};
-   }
-   if (K) oi2(K, z);
-   if (QSK(H)) {
-     if (!USK(X ?? "", O ?? "", void 0))
-       return (h("Attribution hook: Commit was not successful, skipping"), {});
-     h("Attribution hook: Commit succeeded, adding trailers via amend");
-     let $ = await z.getAppState(),
-       _ = await pSK($.attribution, H);
-     if (_.success && _.newPromptCountAtLastCommit !== void 0)
-       z.setAppState((Z) => ({
-         ...Z,
-         attribution: {
-           ...Z.attribution,
-           promptCountAtLastCommit: _.newPromptCountAtLastCommit,
-           permissionPromptCountAtLastCommit:
-             _.newPermissionPromptCountAtLastCommit,
-           escapeCountAtLastCommit: _.newEscapeCountAtLastCommit,
-         },
-       }));
-   }
-   return {};
- }

--- Removed di2 (pretty-v2.1.19.js:566864-566864)
-   di2 = 10485760,

--- Removed ci2 (pretty-v2.1.19.js:566865-566865)
-   ci2 = 51200,

--- Removed bv1 (pretty-v2.1.19.js:566866-566866)
-   bv1 = 8192;

--- Removed hn2 (pretty-v2.1.19.js:568834-568834)
-   hn2 = 1e4;

--- Removed ZbK (pretty-v2.1.19.js:570239-570304)
- var ZbK = C(() => {
-   rm6();
-   GQ6();
-   ehK();
-   zO();
-   _W();
-   q6();
-   P1();
-   DC();
-   QT();
-   I1();
-   dR6();
-   AgA();
-   eZA();
-   Ny();
-   Gs();
-   XM1();
-   JP1();
-   _H();
-   KbK();
-   g4();
-   BzA();
-   dS1();
-   cS1();
-   xp();
-   b2();
-   B0();
-   _Q6();
-   Hz();
-   uQA();
-   Ya();
-   _u();
-   u8();
-   cn();
-   U4();
-   e1();
-   Aa();
-   zbK();
-   X5();
-   Dp();
-   Gf();
-   QM();
-   FN();
-   sZA();
-   QM();
-   VZ();
-   qGA();
-   ZN1();
-   gB6();
-   J7();
-   e1();
-   lM();
-   OdA();
-   BH();
-   JFA();
-   F1();
-   JT1();
-   zO();
-   r6();
-   HbK();
-   F2();
-   eH();
-   Gv();
-   uX();
-   ObK = new Set();
- });

--- Removed ljK (pretty-v2.1.19.js:575490-575490)
-   ljK = void 0;

--- Removed import@256463 (pretty-v2.1.19.js:256464-256464)
- import zo9 from "crypto";

--- Removed import@256472 (pretty-v2.1.19.js:256473-256473)
- import wo9 from "crypto";

--- Removed import@261713 (pretty-v2.1.19.js:261714-261714)
- import X1Y from "path";

--- Removed import@567639 (pretty-v2.1.19.js:567640-567640)
- import { dirname as _n2, join as ThK } from "path";

--- Removed import@568212 (pretty-v2.1.19.js:568213-568213)
- import { posix as En2 } from "path";

--- Removed import@572400 (pretty-v2.1.19.js:572401-572401)
- import { resolve as kQ6 } from "path";

=== Added ===

+++ Added va6 (pretty-v2.1.20.js:5444-5444)
+   va6 = "bash-stdout",

+++ Added Ea6 (pretty-v2.1.20.js:5445-5445)
+   Ea6 = "bash-stderr",

+++ Added l2A (pretty-v2.1.20.js:5446-5446)
+   l2A = "local-command-stdout",

+++ Added mnA (pretty-v2.1.20.js:5447-5447)
+   mnA = "local-command-stderr",

+++ Added IO (pretty-v2.1.20.js:5456-5456)
+   IO = "teammate-message",

+++ Added R1 (pretty-v2.1.20.js:5571-5584)
+ var R1 = C(() => {
+   Y6();
+   efA();
+   z8();
+   d7();
+   r6();
+   B1();
+   $z();
+   FnA = [];
+   r2A = [];
+   iJz = K6(() => {
+     return process.argv.includes("--hard-fail");
+   });
+ });

+++ Added eaK (pretty-v2.1.20.js:6275-6278)
+ function eaK(A) {
+   let K = A.split(":")[0] ?? "";
+   return K === "localhost" || /^127\.\d{1,3}\.\d{1,3}\.\d{1,3}$/.test(K);
+ }

+++ Added a_q (pretty-v2.1.20.js:29079-29102)
+ function a_q(A) {
+   let K = HY8,
+     q = A.length,
+     Y = K(A);
+   if (!Y.error || Y.done || Y.read >= q) return Y.values;
+   let { values: z, read: w } = Y;
+   while (w < q) {
+     let H =
+       typeof A === "string"
+         ? A.indexOf(
+             `
+ `,
+             w,
+           )
+         : A.indexOf(10, w);
+     if (H === -1) break;
+     w = H + 1;
+     let J = K(A, w);
+     if (J.values.length > 0) z = z.concat(J.values);
+     if (!J.error || J.done || J.read >= q) break;
+     w = J.read;
+   }
+   return z;
+ }

+++ Added s_q (pretty-v2.1.20.js:29103-29118)
+ function s_q(A) {
+   let K = A.length,
+     q = 0;
+   if (A[0] === 239 && A[1] === 187 && A[2] === 191) q = 3;
+   let Y = [];
+   while (q < K) {
+     let z = A.indexOf(10, q);
+     if (z === -1) z = K;
+     let w = A.toString("utf8", q, z).trim();
+     if (((q = z + 1), !w)) continue;
+     try {
+       Y.push(JSON.parse(w));
+     } catch {}
+   }
+   return Y;
+ }

+++ Added t_q (pretty-v2.1.20.js:29119-29138)
+ function t_q(A) {
+   let K = tzA(A),
+     q = K.length,
+     Y = 0,
+     z = [];
+   while (Y < q) {
+     let w = K.indexOf(
+       `
+ `,
+       Y,
+     );
+     if (w === -1) w = q;
+     let H = K.substring(Y, w).trim();
+     if (((Y = w + 1), !H)) continue;
+     try {
+       z.push(JSON.parse(H));
+     } catch {}
+   }
+   return z;
+ }

+++ Added K1A (pretty-v2.1.20.js:29139-29143)
+ function K1A(A) {
+   if (HY8) return a_q(A);
+   if (typeof A === "string") return t_q(A);
+   return s_q(A);
+ }

+++ Added q1A (pretty-v2.1.20.js:29144-29152)
+ async function q1A(A) {
+   try {
+     let K = await r_q(A);
+     if (K.length === 0) return [];
+     return K1A(K);
+   } catch (K) {
+     return (qA(Error(`Error opening file ${A}: ${K}`)), []);
+   }
+ }

+++ Added lw (pretty-v2.1.20.js:29177-29197)
+ var lw = C(() => {
+   R1();
+   zY8();
+   d7();
+   B1();
+   a3 = K6((A, K = !0) => {
+     if (!A) return null;
+     try {
+       return JSON.parse(tzA(A));
+     } catch (q) {
+       if (K) qA(q);
+       return null;
+     }
+   });
+   HY8 = (() => {
+     if (typeof Bun > "u") return !1;
+     let K = Bun.JSONL;
+     if (!K?.parseChunk) return !1;
+     return K.parseChunk;
+   })();
+ });

+++ Added og (pretty-v2.1.20.js:89433-89443)
+ function og(A) {
+   switch (A) {
+     case "acceptEdits":
+     case "bypassPermissions":
+     case "default":
+     case "delegate":
+     case "dontAsk":
+     case "plan":
+       return A;
+   }
+ }

+++ Added Rp1 (pretty-v2.1.20.js:94233-94237)
+ var Rp1 = C(() => {
+   ((pq5 =
+     typeof global == "object" && global && global.Object === Object && global),
+     (wA1 = pq5));
+ });

+++ Added yR (pretty-v2.1.20.js:94239-94244)
+ var yR = C(() => {
+   Rp1();
+   ((dq5 = typeof self == "object" && self && self.Object === Object && self),
+     (cq5 = wA1 || dq5 || Function("return this")()),
+     (FX = cq5));
+ });

+++ Added HA1 (pretty-v2.1.20.js:94246-94249)
+ var HA1 = C(() => {
+   yR();
+   ((lq5 = FX.Symbol), (wF = lq5));
+ });

+++ Added rq5 (pretty-v2.1.20.js:94250-94262)
+ function rq5(A) {
+   var K = iq5.call(A, pEA),
+     q = A[pEA];
+   try {
+     A[pEA] = void 0;
+     var Y = !0;
+   } catch (w) {}
+   var z = nq5.call(A);
+   if (Y)
+     if (K) A[pEA] = q;
+     else delete A[pEA];
+   return z;
+ }

+++ Added LR8 (pretty-v2.1.20.js:94264-94271)
+ var LR8 = C(() => {
+   HA1();
+   ((kR8 = Object.prototype),
+     (iq5 = kR8.hasOwnProperty),
+     (nq5 = kR8.toString),
+     (pEA = wF ? wF.toStringTag : void 0));
+   CR8 = rq5;
+ });

+++ Added yR8 (pretty-v2.1.20.js:94276-94279)
+ var yR8 = C(() => {
+   ((oq5 = Object.prototype), (aq5 = oq5.toString));
+   RR8 = sq5;
+ });

+++ Added A55 (pretty-v2.1.20.js:94280-94283)
+ function A55(A) {
+   if (A == null) return A === void 0 ? eq5 : tq5;
+   return IR8 && IR8 in Object(A) ? CR8(A) : RR8(A);
+ }

+++ Added tq5 (pretty-v2.1.20.js:94284-94284)
+ var tq5 = "[object Null]",

+++ Added eq5 (pretty-v2.1.20.js:94285-94285)
+   eq5 = "[object Undefined]",

+++ Added dEA (pretty-v2.1.20.js:94288-94294)
+ var dEA = C(() => {
+   HA1();
+   LR8();
+   yR8();
+   IR8 = wF ? wF.toStringTag : void 0;
+   HF = A55;
+ });

+++ Added K55 (pretty-v2.1.20.js:94295-94297)
+ function K55(A) {
+   return A != null && typeof A == "object";
+ }

+++ Added JA1 (pretty-v2.1.20.js:94303-94305)
+ var JA1 = C(() => {
+   ((q55 = Array.isArray), (CHA = q55));
+ });

+++ Added Y55 (pretty-v2.1.20.js:94306-94309)
+ function Y55(A) {
+   var K = typeof A;
+   return A != null && (K == "object" || K == "function");
+ }

+++ Added O55 (pretty-v2.1.20.js:94314-94318)
+ function O55(A) {
+   if (!_b(A)) return !1;
+   var K = HF(A);
+   return K == w55 || K == H55 || K == z55 || K == J55;
+ }

+++ Added z55 (pretty-v2.1.20.js:94319-94319)
+ var z55 = "[object AsyncFunction]",

+++ Added w55 (pretty-v2.1.20.js:94320-94320)
+   w55 = "[object Function]",

+++ Added H55 (pretty-v2.1.20.js:94321-94321)
+   H55 = "[object GeneratorFunction]",

+++ Added J55 (pretty-v2.1.20.js:94322-94322)
+   J55 = "[object Proxy]",

+++ Added SR8 (pretty-v2.1.20.js:94330-94333)
+ var SR8 = C(() => {
+   yR();
+   ((X55 = FX["__core-js_shared__"]), (XA1 = X55));
+ });

+++ Added $55 (pretty-v2.1.20.js:94334-94336)
+ function $55(A) {
+   return !!hR8 && hR8 in A;
+ }

+++ Added xR8 (pretty-v2.1.20.js:94338-94345)
+ var xR8 = C(() => {
+   SR8();
+   hR8 = (function () {
+     var A = /[^.]+$/.exec((XA1 && XA1.keys && XA1.keys.IE_PROTO) || "");
+     return A ? "Symbol(src)_1." + A : "";
+   })();
+   bR8 = $55;
+ });

+++ Added G55 (pretty-v2.1.20.js:94346-94356)
+ function G55(A) {
+   if (A != null) {
+     try {
+       return Z55.call(A);
+     } catch (K) {}
+     try {
+       return A + "";
+     } catch (K) {}
+   }
+   return "";
+ }

+++ Added Ip1 (pretty-v2.1.20.js:94358-94361)
+ var Ip1 = C(() => {
+   ((_55 = Function.prototype), (Z55 = _55.toString));
+   JF = G55;
+ });

+++ Added N55 (pretty-v2.1.20.js:94362-94366)
+ function N55(A) {
+   if (!_b(A) || bR8(A)) return !1;
+   var K = OA1(A) ? f55 : D55;
+   return K.test(JF(A));
+ }

+++ Added BR8 (pretty-v2.1.20.js:94368-94390)
+ var BR8 = C(() => {
+   yp1();
+   xR8();
+   LHA();
+   Ip1();
+   ((W55 = /[\\^$.*+?()[\]{}|]/g),
+     (D55 = /^\[object .+?Constructor\]$/),
+     (M55 = Function.prototype),
+     (j55 = Object.prototype),
+     (P55 = M55.toString),
+     (V55 = j55.hasOwnProperty),
+     (f55 = RegExp(
+       "^" +
+         P55.call(V55)
+           .replace(W55, "\\$&")
+           .replace(
+             /hasOwnProperty|(function).*?(?=\\\()| for .+?(?=\\\])/g,
+             "$1.*?",
+           ) +
+         "$",
+     )));
+   uR8 = N55;
+ });

+++ Added T55 (pretty-v2.1.20.js:94391-94393)
+ function T55(A, K) {
+   return A == null ? void 0 : A[K];
+ }

+++ Added v55 (pretty-v2.1.20.js:94398-94401)
+ function v55(A, K) {
+   var q = mR8(A, K);
+   return uR8(q) ? q : void 0;
+ }

+++ Added FR8 (pretty-v2.1.20.js:94409-94413)
+ var FR8 = C(() => {
+   Gi();
+   yR();
+   ((E55 = $V(FX, "WeakMap")), ($A1 = E55));
+ });

+++ Added pR8 (pretty-v2.1.20.js:94415-94429)
+ var pR8 = C(() => {
+   LHA();
+   ((QR8 = Object.create),
+     (k55 = (function () {
+       function A() {}
+       return function (K) {
+         if (!_b(K)) return {};
+         if (QR8) return QR8(K);
+         A.prototype = K;
+         var q = new A();
+         return ((A.prototype = void 0), q);
+       };
+     })()),
+     (UR8 = k55));
+ });

+++ Added C55 (pretty-v2.1.20.js:94430-94436)
+ function C55(A, K) {
+   var q = -1,
+     Y = A.length;
+   K || (K = Array(Y));
+   while (++q < Y) K[q] = A[q];
+   return K;
+ }

+++ Added cR8 (pretty-v2.1.20.js:94438-94440)
+ var cR8 = C(() => {
+   dR8 = C55;
+ });

+++ Added lR8 (pretty-v2.1.20.js:94442-94451)
+ var lR8 = C(() => {
+   Gi();
+   ((L55 = (function () {
+     try {
+       var A = $V(Object, "defineProperty");
+       return (A({}, "", {}), A);
+     } catch (K) {}
+   })()),
+     (Sp1 = L55));
+ });

+++ Added R55 (pretty-v2.1.20.js:94452-94457)
+ function R55(A, K) {
+   var q = -1,
+     Y = A == null ? 0 : A.length;
+   while (++q < Y) if (K(A[q], q, A) === !1) break;
+   return A;
+ }

+++ Added nR8 (pretty-v2.1.20.js:94459-94461)
+ var nR8 = C(() => {
+   iR8 = R55;
+ });

+++ Added S55 (pretty-v2.1.20.js:94462-94472)
+ function S55(A, K) {
+   var q = typeof A;
+   return (
+     (K = K == null ? y55 : K),
+     !!K &&
+       (q == "number" || (q != "symbol" && I55.test(A))) &&
+       A > -1 &&
+       A % 1 == 0 &&
+       A < K
+   );
+ }

+++ Added y55 (pretty-v2.1.20.js:94473-94473)
+ var y55 = 9007199254740991,

+++ Added oR8 (pretty-v2.1.20.js:94476-94479)
+ var oR8 = C(() => {
+   I55 = /^(?:0|[1-9]\d*)$/;
+   rR8 = S55;
+ });

+++ Added h55 (pretty-v2.1.20.js:94480-94484)
+ function h55(A, K, q) {
+   if (K == "__proto__" && Sp1)
+     Sp1(A, K, { configurable: !0, enumerable: !0, value: q, writable: !0 });
+   else A[K] = q;
+ }

+++ Added b55 (pretty-v2.1.20.js:94490-94492)
+ function b55(A, K) {
+   return A === K || (A !== A && K !== K);
+ }

+++ Added bp1 (pretty-v2.1.20.js:94494-94496)
+ var bp1 = C(() => {
+   ZA1 = b55;
+ });

+++ Added B55 (pretty-v2.1.20.js:94497-94501)
+ function B55(A, K, q) {
+   var Y = A[K];
+   if (!(u55.call(A, K) && ZA1(Y, q)) || (q === void 0 && !(K in A)))
+     _A1(A, K, q);
+ }

+++ Added xp1 (pretty-v2.1.20.js:94503-94508)
+ var xp1 = C(() => {
+   hp1();
+   bp1();
+   ((x55 = Object.prototype), (u55 = x55.hasOwnProperty));
+   GA1 = B55;
+ });

+++ Added m55 (pretty-v2.1.20.js:94509-94522)
+ function m55(A, K, q, Y) {
+   var z = !q;
+   q || (q = {});
+   var w = -1,
+     H = K.length;
+   while (++w < H) {
+     var J = K[w],
+       O = Y ? Y(q[J], A[J], J, q, A) : void 0;
+     if (O === void 0) O = A[J];
+     if (z) _A1(q, J, O);
+     else GA1(q, J, O);
+   }
+   return q;
+ }

+++ Added cEA (pretty-v2.1.20.js:94524-94528)
+ var cEA = C(() => {
+   xp1();
+   hp1();
+   Wi = m55;
+ });

+++ Added F55 (pretty-v2.1.20.js:94529-94531)
+ function F55(A) {
+   return typeof A == "number" && A > -1 && A % 1 == 0 && A <= g55;
+ }

+++ Added g55 (pretty-v2.1.20.js:94532-94532)
+ var g55 = 9007199254740991,

+++ Added up1 (pretty-v2.1.20.js:94534-94536)
+ var up1 = C(() => {
+   WA1 = F55;
+ });

+++ Added Q55 (pretty-v2.1.20.js:94537-94539)
+ function Q55(A) {
+   return A != null && WA1(A.length) && !OA1(A);
+ }

+++ Added Bp1 (pretty-v2.1.20.js:94541-94545)
+ var Bp1 = C(() => {
+   yp1();
+   up1();
+   DA1 = Q55;
+ });

+++ Added p55 (pretty-v2.1.20.js:94546-94550)
+ function p55(A) {
+   var K = A && A.constructor,
+     q = (typeof K == "function" && K.prototype) || U55;
+   return A === q;
+ }

+++ Added MA1 (pretty-v2.1.20.js:94552-94555)
+ var MA1 = C(() => {
+   U55 = Object.prototype;
+   RHA = p55;
+ });

+++ Added d55 (pretty-v2.1.20.js:94556-94561)
+ function d55(A, K) {
+   var q = -1,
+     Y = Array(A);
+   while (++q < A) Y[q] = K(q);
+   return Y;
+ }

+++ Added sR8 (pretty-v2.1.20.js:94563-94565)
+ var sR8 = C(() => {
+   aR8 = d55;
+ });

+++ Added l55 (pretty-v2.1.20.js:94566-94568)
+ function l55(A) {
+   return $b(A) && HF(A) == c55;
+ }

+++ Added c55 (pretty-v2.1.20.js:94569-94569)
+ var c55 = "[object Arguments]",

+++ Added tR8 (pretty-v2.1.20.js:94571-94575)
+ var tR8 = C(() => {
+   dEA();
+   kHA();
+   mp1 = l55;
+ });

+++ Added Ky8 (pretty-v2.1.20.js:94577-94593)
+ var Ky8 = C(() => {
+   tR8();
+   kHA();
+   ((eR8 = Object.prototype),
+     (i55 = eR8.hasOwnProperty),
+     (n55 = eR8.propertyIsEnumerable),
+     (r55 = mp1(
+       (function () {
+         return arguments;
+       })(),
+     )
+       ? mp1
+       : function (A) {
+           return $b(A) && i55.call(A, "callee") && !n55.call(A, "callee");
+         }),
+     (Ay8 = r55));
+ });

+++ Added Yy8 (pretty-v2.1.20.js:94598-94600)
+ var Yy8 = C(() => {
+   qy8 = o55;
+ });

+++ Added gp1 (pretty-v2.1.20.js:94604-94614)
+ var gp1 = C(() => {
+   yR();
+   Yy8();
+   ((Hy8 = typeof PA1 == "object" && PA1 && !PA1.nodeType && PA1),
+     (zy8 = Hy8 && typeof jA1 == "object" && jA1 && !jA1.nodeType && jA1),
+     (a55 = zy8 && zy8.exports === Hy8),
+     (wy8 = a55 ? FX.Buffer : void 0),
+     (s55 = wy8 ? wy8.isBuffer : void 0),
+     (t55 = s55 || qy8),
+     (lEA = t55));
+ });

+++ Added v35 (pretty-v2.1.20.js:94615-94617)
+ function v35(A) {
+   return $b(A) && WA1(A.length) && !!IH[HF(A)];
+ }

+++ Added e55 (pretty-v2.1.20.js:94618-94618)
+ var e55 = "[object Arguments]",

+++ Added A35 (pretty-v2.1.20.js:94619-94619)
+   A35 = "[object Array]",

+++ Added K35 (pretty-v2.1.20.js:94620-94620)
+   K35 = "[object Boolean]",

+++ Added q35 (pretty-v2.1.20.js:94621-94621)
+   q35 = "[object Date]",

+++ Added Y35 (pretty-v2.1.20.js:94622-94622)
+   Y35 = "[object Error]",

+++ Added z35 (pretty-v2.1.20.js:94623-94623)
+   z35 = "[object Function]",

+++ Added w35 (pretty-v2.1.20.js:94624-94624)
+   w35 = "[object Map]",

+++ Added H35 (pretty-v2.1.20.js:94625-94625)
+   H35 = "[object Number]",

+++ Added J35 (pretty-v2.1.20.js:94626-94626)
+   J35 = "[object Object]",

+++ Added O35 (pretty-v2.1.20.js:94627-94627)
+   O35 = "[object RegExp]",

+++ Added X35 (pretty-v2.1.20.js:94628-94628)
+   X35 = "[object Set]",

+++ Added $35 (pretty-v2.1.20.js:94629-94629)
+   $35 = "[object String]",

+++ Added _35 (pretty-v2.1.20.js:94630-94630)
+   _35 = "[object WeakMap]",

+++ Added Z35 (pretty-v2.1.20.js:94631-94631)
+   Z35 = "[object ArrayBuffer]",

+++ Added G35 (pretty-v2.1.20.js:94632-94632)
+   G35 = "[object DataView]",

+++ Added W35 (pretty-v2.1.20.js:94633-94633)
+   W35 = "[object Float32Array]",

+++ Added D35 (pretty-v2.1.20.js:94634-94634)
+   D35 = "[object Float64Array]",

+++ Added M35 (pretty-v2.1.20.js:94635-94635)
+   M35 = "[object Int8Array]",

+++ Added j35 (pretty-v2.1.20.js:94636-94636)
+   j35 = "[object Int16Array]",

+++ Added P35 (pretty-v2.1.20.js:94637-94637)
+   P35 = "[object Int32Array]",

+++ Added V35 (pretty-v2.1.20.js:94638-94638)
+   V35 = "[object Uint8Array]",

+++ Added f35 (pretty-v2.1.20.js:94639-94639)
+   f35 = "[object Uint8ClampedArray]",

+++ Added N35 (pretty-v2.1.20.js:94640-94640)
+   N35 = "[object Uint16Array]",

+++ Added T35 (pretty-v2.1.20.js:94641-94641)
+   T35 = "[object Uint32Array]",

+++ Added Oy8 (pretty-v2.1.20.js:94644-94676)
+ var Oy8 = C(() => {
+   dEA();
+   up1();
+   kHA();
+   IH = {};
+   IH[W35] =
+     IH[D35] =
+     IH[M35] =
+     IH[j35] =
+     IH[P35] =
+     IH[V35] =
+     IH[f35] =
+     IH[N35] =
+     IH[T35] =
+       !0;
+   IH[e55] =
+     IH[A35] =
+     IH[Z35] =
+     IH[K35] =
+     IH[G35] =
+     IH[q35] =
+     IH[Y35] =
+     IH[z35] =
+     IH[w35] =
+     IH[H35] =
+     IH[J35] =
+     IH[O35] =
+     IH[X35] =
+     IH[$35] =
+     IH[_35] =
+       !1;
+   Jy8 = v35;
+ });

+++ Added E35 (pretty-v2.1.20.js:94677-94681)
+ function E35(A) {
+   return function (K) {
+     return A(K);
+   };
+ }

+++ Added VA1 (pretty-v2.1.20.js:94683-94685)
+ var VA1 = C(() => {
+   yHA = E35;
+ });

+++ Added TA1 (pretty-v2.1.20.js:94689-94703)
+ var TA1 = C(() => {
+   Rp1();
+   ((Xy8 = typeof NA1 == "object" && NA1 && !NA1.nodeType && NA1),
+     (iEA = Xy8 && typeof fA1 == "object" && fA1 && !fA1.nodeType && fA1),
+     (k35 = iEA && iEA.exports === Xy8),
+     (Fp1 = k35 && wA1.process),
+     (C35 = (function () {
+       try {
+         var A = iEA && iEA.require && iEA.require("util").types;
+         if (A) return A;
+         return Fp1 && Fp1.binding && Fp1.binding("util");
+       } catch (K) {}
+     })()),
+     (Zb = C35));
+ });

+++ Added Zy8 (pretty-v2.1.20.js:94705-94710)
+ var Zy8 = C(() => {
+   Oy8();
+   VA1();
+   TA1();
+   (($y8 = Zb && Zb.isTypedArray), (L35 = $y8 ? yHA($y8) : Jy8), (_y8 = L35));
+ });

+++ Added I35 (pretty-v2.1.20.js:94711-94732)
+ function I35(A, K) {
+   var q = CHA(A),
+     Y = !q && Ay8(A),
+     z = !q && !Y && lEA(A),
+     w = !q && !Y && !z && _y8(A),
+     H = q || Y || z || w,
+     J = H ? aR8(A.length, String) : [],
+     O = J.length;
+   for (var X in A)
+     if (
+       (K || y35.call(A, X)) &&
+       !(
+         H &&
+         (X == "length" ||
+           (z && (X == "offset" || X == "parent")) ||
+           (w && (X == "buffer" || X == "byteLength" || X == "byteOffset")) ||
+           rR8(X, O))
+       )
+     )
+       J.push(X);
+   return J;
+ }

+++ Added Qp1 (pretty-v2.1.20.js:94734-94743)
+ var Qp1 = C(() => {
+   sR8();
+   Ky8();
+   JA1();
+   gp1();
+   oR8();
+   Zy8();
+   ((R35 = Object.prototype), (y35 = R35.hasOwnProperty));
+   vA1 = I35;
+ });

+++ Added S35 (pretty-v2.1.20.js:94744-94748)
+ function S35(A, K) {
+   return function (q) {
+     return A(K(q));
+   };
+ }

+++ Added Up1 (pretty-v2.1.20.js:94750-94752)
+ var Up1 = C(() => {
+   EA1 = S35;
+ });

+++ Added Wy8 (pretty-v2.1.20.js:94754-94757)
+ var Wy8 = C(() => {
+   Up1();
+   ((h35 = EA1(Object.keys, Object)), (Gy8 = h35));
+ });

+++ Added u35 (pretty-v2.1.20.js:94758-94763)
+ function u35(A) {
+   if (!RHA(A)) return Gy8(A);
+   var K = [];
+   for (var q in Object(A)) if (x35.call(A, q) && q != "constructor") K.push(q);
+   return K;
+ }

+++ Added My8 (pretty-v2.1.20.js:94765-94770)
+ var My8 = C(() => {
+   MA1();
+   Wy8();
+   ((b35 = Object.prototype), (x35 = b35.hasOwnProperty));
+   Dy8 = u35;
+ });

+++ Added B35 (pretty-v2.1.20.js:94771-94773)
+ function B35(A) {
+   return DA1(A) ? vA1(A) : Dy8(A);
+ }

+++ Added kA1 (pretty-v2.1.20.js:94775-94780)
+ var kA1 = C(() => {
+   Qp1();
+   My8();
+   Bp1();
+   IHA = B35;
+ });

+++ Added m35 (pretty-v2.1.20.js:94781-94785)
+ function m35(A) {
+   var K = [];
+   if (A != null) for (var q in Object(A)) K.push(q);
+   return K;
+ }

+++ Added Py8 (pretty-v2.1.20.js:94787-94789)
+ var Py8 = C(() => {
+   jy8 = m35;
+ });

+++ Added Q35 (pretty-v2.1.20.js:94790-94797)
+ function Q35(A) {
+   if (!_b(A)) return jy8(A);
+   var K = RHA(A),
+     q = [];
+   for (var Y in A)
+     if (!(Y == "constructor" && (K || !F35.call(A, Y)))) q.push(Y);
+   return q;
+ }

+++ Added fy8 (pretty-v2.1.20.js:94799-94805)
+ var fy8 = C(() => {
+   LHA();
+   MA1();
+   Py8();
+   ((g35 = Object.prototype), (F35 = g35.hasOwnProperty));
+   Vy8 = Q35;
+ });

+++ Added U35 (pretty-v2.1.20.js:94806-94808)
+ function U35(A) {
+   return DA1(A) ? vA1(A, !0) : Vy8(A);
+ }

+++ Added CA1 (pretty-v2.1.20.js:94810-94815)
+ var CA1 = C(() => {
+   Qp1();
+   fy8();
+   Bp1();
+   SHA = U35;
+ });

+++ Added nEA (pretty-v2.1.20.js:94817-94820)
+ var nEA = C(() => {
+   Gi();
+   ((p35 = $V(Object, "create")), (OF = p35));
+ });

+++ Added d35 (pretty-v2.1.20.js:94821-94823)
+ function d35() {
+   ((this.__data__ = OF ? OF(null) : {}), (this.size = 0));
+ }

+++ Added c35 (pretty-v2.1.20.js:94829-94832)
+ function c35(A) {
+   var K = this.has(A) && delete this.__data__[A];
+   return ((this.size -= K ? 1 : 0), K);
+ }

+++ Added Ey8 (pretty-v2.1.20.js:94834-94836)
+ var Ey8 = C(() => {
+   vy8 = c35;
+ });

+++ Added r35 (pretty-v2.1.20.js:94837-94844)
+ function r35(A) {
+   var K = this.__data__;
+   if (OF) {
+     var q = K[A];
+     return q === l35 ? void 0 : q;
+   }
+   return n35.call(K, A) ? K[A] : void 0;
+ }

+++ Added l35 (pretty-v2.1.20.js:94845-94845)
+ var l35 = "__lodash_hash_undefined__",

+++ Added Cy8 (pretty-v2.1.20.js:94849-94853)
+ var Cy8 = C(() => {
+   nEA();
+   ((i35 = Object.prototype), (n35 = i35.hasOwnProperty));
+   ky8 = r35;
+ });

+++ Added s35 (pretty-v2.1.20.js:94854-94857)
+ function s35(A) {
+   var K = this.__data__;
+   return OF ? K[A] !== void 0 : a35.call(K, A);
+ }

+++ Added Ry8 (pretty-v2.1.20.js:94859-94863)
+ var Ry8 = C(() => {
+   nEA();
+   ((o35 = Object.prototype), (a35 = o35.hasOwnProperty));
+   Ly8 = s35;
+ });

+++ Added e35 (pretty-v2.1.20.js:94864-94871)
+ function e35(A, K) {
+   var q = this.__data__;
+   return (
+     (this.size += this.has(A) ? 0 : 1),
+     (q[A] = OF && K === void 0 ? t35 : K),
+     this
+   );
+ }

+++ Added t35 (pretty-v2.1.20.js:94872-94872)
+ var t35 = "__lodash_hash_undefined__",

+++ Added hHA (pretty-v2.1.20.js:94878-94886)
+ function hHA(A) {
+   var K = -1,
+     q = A == null ? 0 : A.length;
+   this.clear();
+   while (++K < q) {
+     var Y = A[K];
+     this.set(Y[0], Y[1]);
+   }
+ }

+++ Added Sy8 (pretty-v2.1.20.js:94888-94900)
+ var Sy8 = C(() => {
+   Ty8();
+   Ey8();
+   Cy8();
+   Ry8();
+   Iy8();
+   hHA.prototype.clear = Ny8;
+   hHA.prototype.delete = vy8;
+   hHA.prototype.get = ky8;
+   hHA.prototype.has = Ly8;
+   hHA.prototype.set = yy8;
+   pp1 = hHA;
+ });

+++ Added A95 (pretty-v2.1.20.js:94901-94903)
+ function A95() {
+   ((this.__data__ = []), (this.size = 0));
+ }

+++ Added by8 (pretty-v2.1.20.js:94905-94907)
+ var by8 = C(() => {
+   hy8 = A95;
+ });

+++ Added K95 (pretty-v2.1.20.js:94908-94912)
+ function K95(A, K) {
+   var q = A.length;
+   while (q--) if (ZA1(A[q][0], K)) return q;
+   return -1;
+ }

+++ Added z95 (pretty-v2.1.20.js:94918-94926)
+ function z95(A) {
+   var K = this.__data__,
+     q = Di(K, A);
+   if (q < 0) return !1;
+   var Y = K.length - 1;
+   if (q == Y) K.pop();
+   else Y95.call(K, q, 1);
+   return (--this.size, !0);
+ }

+++ Added uy8 (pretty-v2.1.20.js:94928-94932)
+ var uy8 = C(() => {
+   rEA();
+   ((q95 = Array.prototype), (Y95 = q95.splice));
+   xy8 = z95;
+ });

+++ Added w95 (pretty-v2.1.20.js:94933-94937)
+ function w95(A) {
+   var K = this.__data__,
+     q = Di(K, A);
+   return q < 0 ? void 0 : K[q][1];
+ }

+++ Added H95 (pretty-v2.1.20.js:94943-94945)
+ function H95(A) {
+   return Di(this.__data__, A) > -1;
+ }

+++ Added J95 (pretty-v2.1.20.js:94951-94957)
+ function J95(A, K) {
+   var q = this.__data__,
+     Y = Di(q, A);
+   if (Y < 0) (++this.size, q.push([A, K]));
+   else q[Y][1] = K;
+   return this;
+ }

+++ Added bHA (pretty-v2.1.20.js:94963-94971)
+ function bHA(A) {
+   var K = -1,
+     q = A == null ? 0 : A.length;
+   this.clear();
+   while (++K < q) {
+     var Y = A[K];
+     this.set(Y[0], Y[1]);
+   }
+ }

+++ Added oEA (pretty-v2.1.20.js:94973-94985)
+ var oEA = C(() => {
+   by8();
+   uy8();
+   my8();
+   Fy8();
+   Uy8();
+   bHA.prototype.clear = hy8;
+   bHA.prototype.delete = xy8;
+   bHA.prototype.get = By8;
+   bHA.prototype.has = gy8;
+   bHA.prototype.set = Qy8;
+   Mi = bHA;
+ });

+++ Added LA1 (pretty-v2.1.20.js:94987-94991)
+ var LA1 = C(() => {
+   Gi();
+   yR();
+   ((O95 = $V(FX, "Map")), (ji = O95));
+ });

+++ Added X95 (pretty-v2.1.20.js:94992-94999)
+ function X95() {
+   ((this.size = 0),
+     (this.__data__ = {
+       hash: new pp1(),
+       map: new (ji || Mi)(),
+       string: new pp1(),
+     }));
+ }

+++ Added dy8 (pretty-v2.1.20.js:95001-95006)
+ var dy8 = C(() => {
+   Sy8();
+   oEA();
+   LA1();
+   py8 = X95;
+ });

+++ Added $95 (pretty-v2.1.20.js:95007-95012)
+ function $95(A) {
+   var K = typeof A;
+   return K == "string" || K == "number" || K == "symbol" || K == "boolean"
+     ? A !== "__proto__"
+     : A === null;
+ }

+++ Added ly8 (pretty-v2.1.20.js:95014-95016)
+ var ly8 = C(() => {
+   cy8 = $95;
+ });

+++ Added _95 (pretty-v2.1.20.js:95017-95020)
+ function _95(A, K) {
+   var q = A.__data__;
+   return cy8(K) ? q[typeof K == "string" ? "string" : "hash"] : q.map;
+ }

+++ Added Z95 (pretty-v2.1.20.js:95026-95029)
+ function Z95(A) {
+   var K = Pi(this, A).delete(A);
+   return ((this.size -= K ? 1 : 0), K);
+ }

+++ Added ny8 (pretty-v2.1.20.js:95031-95034)
+ var ny8 = C(() => {
+   aEA();
+   iy8 = Z95;
+ });

+++ Added G95 (pretty-v2.1.20.js:95035-95037)
+ function G95(A) {
+   return Pi(this, A).get(A);
+ }

+++ Added oy8 (pretty-v2.1.20.js:95039-95042)
+ var oy8 = C(() => {
+   aEA();
+   ry8 = G95;
+ });

+++ Added W95 (pretty-v2.1.20.js:95043-95045)
+ function W95(A) {
+   return Pi(this, A).has(A);
+ }

+++ Added sy8 (pretty-v2.1.20.js:95047-95050)
+ var sy8 = C(() => {
+   aEA();
+   ay8 = W95;
+ });

+++ Added D95 (pretty-v2.1.20.js:95051-95055)
+ function D95(A, K) {
+   var q = Pi(this, A),
+     Y = q.size;
+   return (q.set(A, K), (this.size += q.size == Y ? 0 : 1), this);
+ }

+++ Added ey8 (pretty-v2.1.20.js:95057-95060)
+ var ey8 = C(() => {
+   aEA();
+   ty8 = D95;
+ });

+++ Added xHA (pretty-v2.1.20.js:95061-95069)
+ function xHA(A) {
+   var K = -1,
+     q = A == null ? 0 : A.length;
+   this.clear();
+   while (++K < q) {
+     var Y = A[K];
+     this.set(Y[0], Y[1]);
+   }
+ }

+++ Added KI8 (pretty-v2.1.20.js:95071-95083)
+ var KI8 = C(() => {
+   dy8();
+   ny8();
+   oy8();
+   sy8();
+   ey8();
+   xHA.prototype.clear = py8;
+   xHA.prototype.delete = iy8;
+   xHA.prototype.get = ry8;
+   xHA.prototype.has = ay8;
+   xHA.prototype.set = ty8;
+   AI8 = xHA;
+ });

+++ Added M95 (pretty-v2.1.20.js:95084-95090)
+ function M95(A, K) {
+   var q = -1,
+     Y = K.length,
+     z = A.length;
+   while (++q < Y) A[z + q] = K[q];
+   return A;
+ }

+++ Added dp1 (pretty-v2.1.20.js:95092-95094)
+ var dp1 = C(() => {
+   RA1 = M95;
+ });

+++ Added cp1 (pretty-v2.1.20.js:95096-95099)
+ var cp1 = C(() => {
+   Up1();
+   ((j95 = EA1(Object.getPrototypeOf, Object)), (yA1 = j95));
+ });

+++ Added P95 (pretty-v2.1.20.js:95100-95102)
+ function P95() {
+   ((this.__data__ = new Mi()), (this.size = 0));
+ }

+++ Added YI8 (pretty-v2.1.20.js:95104-95107)
+ var YI8 = C(() => {
+   oEA();
+   qI8 = P95;
+ });

+++ Added V95 (pretty-v2.1.20.js:95108-95112)
+ function V95(A) {
+   var K = this.__data__,
+     q = K.delete(A);
+   return ((this.size = K.size), q);
+ }

+++ Added wI8 (pretty-v2.1.20.js:95114-95116)
+ var wI8 = C(() => {
+   zI8 = V95;
+ });

+++ Added f95 (pretty-v2.1.20.js:95117-95119)
+ function f95(A) {
+   return this.__data__.get(A);
+ }

+++ Added JI8 (pretty-v2.1.20.js:95121-95123)
+ var JI8 = C(() => {
+   HI8 = f95;
+ });

+++ Added N95 (pretty-v2.1.20.js:95124-95126)
+ function N95(A) {
+   return this.__data__.has(A);
+ }

+++ Added XI8 (pretty-v2.1.20.js:95128-95130)
+ var XI8 = C(() => {
+   OI8 = N95;
+ });

+++ Added v95 (pretty-v2.1.20.js:95131-95140)
+ function v95(A, K) {
+   var q = this.__data__;
+   if (q instanceof Mi) {
+     var Y = q.__data__;
+     if (!ji || Y.length < T95 - 1)
+       return (Y.push([A, K]), (this.size = ++q.size), this);
+     q = this.__data__ = new AI8(Y);
+   }
+   return (q.set(A, K), (this.size = q.size), this);
+ }

+++ Added _I8 (pretty-v2.1.20.js:95143-95148)
+ var _I8 = C(() => {
+   oEA();
+   LA1();
+   KI8();
+   $I8 = v95;
+ });

+++ Added uHA (pretty-v2.1.20.js:95149-95152)
+ function uHA(A) {
+   var K = (this.__data__ = new Mi(A));
+   this.size = K.size;
+ }

+++ Added GI8 (pretty-v2.1.20.js:95154-95167)
+ var GI8 = C(() => {
+   oEA();
+   YI8();
+   wI8();
+   JI8();
+   XI8();
+   _I8();
+   uHA.prototype.clear = qI8;
+   uHA.prototype.delete = zI8;
+   uHA.prototype.get = HI8;
+   uHA.prototype.has = OI8;
+   uHA.prototype.set = $I8;
+   ZI8 = uHA;
+ });

+++ Added E95 (pretty-v2.1.20.js:95168-95170)
+ function E95(A, K) {
+   return A && Wi(K, IHA(K), A);
+ }

+++ Added DI8 (pretty-v2.1.20.js:95172-95176)
+ var DI8 = C(() => {
+   cEA();
+   kA1();
+   WI8 = E95;
+ });

+++ Added k95 (pretty-v2.1.20.js:95177-95179)
+ function k95(A, K) {
+   return A && Wi(K, SHA(K), A);
+ }

+++ Added jI8 (pretty-v2.1.20.js:95181-95185)
+ var jI8 = C(() => {
+   cEA();
+   CA1();
+   MI8 = k95;
+ });

+++ Added L95 (pretty-v2.1.20.js:95188-95193)
+ function L95(A, K) {
+   if (K) return A.slice();
+   var q = A.length,
+     Y = fI8 ? fI8(q) : new A.constructor(q);
+   return (A.copy(Y), Y);
+ }

+++ Added TI8 (pretty-v2.1.20.js:95195-95203)
+ var TI8 = C(() => {
+   yR();
+   ((NI8 = typeof SA1 == "object" && SA1 && !SA1.nodeType && SA1),
+     (PI8 = NI8 && typeof IA1 == "object" && IA1 && !IA1.nodeType && IA1),
+     (C95 = PI8 && PI8.exports === NI8),
+     (VI8 = C95 ? FX.Buffer : void 0),
+     (fI8 = VI8 ? VI8.allocUnsafe : void 0));
+   lp1 = L95;
+ });

+++ Added R95 (pretty-v2.1.20.js:95204-95214)
+ function R95(A, K) {
+   var q = -1,
+     Y = A == null ? 0 : A.length,
+     z = 0,
+     w = [];
+   while (++q < Y) {
+     var H = A[q];
+     if (K(H, q, A)) w[z++] = H;
+   }
+   return w;
+ }

+++ Added EI8 (pretty-v2.1.20.js:95216-95218)
+ var EI8 = C(() => {
+   vI8 = R95;
+ });

+++ Added ip1 (pretty-v2.1.20.js:95223-95225)
+ var ip1 = C(() => {
+   hA1 = y95;
+ });

+++ Added bA1 (pretty-v2.1.20.js:95227-95245)
+ var bA1 = C(() => {
+   EI8();
+   ip1();
+   ((I95 = Object.prototype),
+     (S95 = I95.propertyIsEnumerable),
+     (kI8 = Object.getOwnPropertySymbols),
+     (h95 = !kI8
+       ? hA1
+       : function (A) {
+           if (A == null) return [];
+           return (
+             (A = Object(A)),
+             vI8(kI8(A), function (K) {
+               return S95.call(A, K);
+             })
+           );
+         }),
+     (BHA = h95));
+ });

+++ Added b95 (pretty-v2.1.20.js:95246-95248)
+ function b95(A, K) {
+   return Wi(A, BHA(A), K);
+ }

+++ Added LI8 (pretty-v2.1.20.js:95250-95254)
+ var LI8 = C(() => {
+   cEA();
+   bA1();
+   CI8 = b95;
+ });

+++ Added np1 (pretty-v2.1.20.js:95256-95270)
+ var np1 = C(() => {
+   dp1();
+   cp1();
+   bA1();
+   ip1();
+   ((x95 = Object.getOwnPropertySymbols),
+     (u95 = !x95
+       ? hA1
+       : function (A) {
+           var K = [];
+           while (A) (RA1(K, BHA(A)), (A = yA1(A)));
+           return K;
+         }),
+     (xA1 = u95));
+ });

+++ Added B95 (pretty-v2.1.20.js:95271-95273)
+ function B95(A, K) {
+   return Wi(A, xA1(A), K);
+ }

+++ Added yI8 (pretty-v2.1.20.js:95275-95279)
+ var yI8 = C(() => {
+   cEA();
+   np1();
+   RI8 = B95;
+ });

+++ Added m95 (pretty-v2.1.20.js:95280-95283)
+ function m95(A, K, q) {
+   var Y = K(A);
+   return CHA(A) ? Y : RA1(Y, q(A));
+ }

+++ Added rp1 (pretty-v2.1.20.js:95285-95289)
+ var rp1 = C(() => {
+   dp1();
+   JA1();
+   uA1 = m95;
+ });

+++ Added g95 (pretty-v2.1.20.js:95290-95292)
+ function g95(A) {
+   return uA1(A, IHA, BHA);
+ }

+++ Added SI8 (pretty-v2.1.20.js:95294-95299)
+ var SI8 = C(() => {
+   rp1();
+   bA1();
+   kA1();
+   II8 = g95;
+ });

+++ Added F95 (pretty-v2.1.20.js:95300-95302)
+ function F95(A) {
+   return uA1(A, SHA, xA1);
+ }

+++ Added bI8 (pretty-v2.1.20.js:95304-95309)
+ var bI8 = C(() => {
+   rp1();
+   np1();
+   CA1();
+   hI8 = F95;
+ });

+++ Added xI8 (pretty-v2.1.20.js:95311-95315)
+ var xI8 = C(() => {
+   Gi();
+   yR();
+   ((Q95 = $V(FX, "DataView")), (BA1 = Q95));
+ });

+++ Added uI8 (pretty-v2.1.20.js:95317-95321)
+ var uI8 = C(() => {
+   Gi();
+   yR();
+   ((U95 = $V(FX, "Promise")), (mA1 = U95));
+ });

+++ Added BI8 (pretty-v2.1.20.js:95323-95327)
+ var BI8 = C(() => {
+   Gi();
+   yR();
+   ((p95 = $V(FX, "Set")), (gA1 = p95));
+ });

+++ Added mI8 (pretty-v2.1.20.js:95328-95328)
+ var mI8 = "[object Map]",

+++ Added d95 (pretty-v2.1.20.js:95329-95329)
+   d95 = "[object Object]",

+++ Added gI8 (pretty-v2.1.20.js:95330-95330)
+   gI8 = "[object Promise]",

+++ Added FI8 (pretty-v2.1.20.js:95331-95331)
+   FI8 = "[object Set]",

+++ Added QI8 (pretty-v2.1.20.js:95332-95332)
+   QI8 = "[object WeakMap]",

+++ Added UI8 (pretty-v2.1.20.js:95333-95333)
+   UI8 = "[object DataView]",

+++ Added FA1 (pretty-v2.1.20.js:95341-95382)
+ var FA1 = C(() => {
+   xI8();
+   LA1();
+   uI8();
+   BI8();
+   FR8();
+   dEA();
+   Ip1();
+   ((c95 = JF(BA1)),
+     (l95 = JF(ji)),
+     (i95 = JF(mA1)),
+     (n95 = JF(gA1)),
+     (r95 = JF($A1)),
+     (Y6A = HF));
+   if (
+     (BA1 && Y6A(new BA1(new ArrayBuffer(1))) != UI8) ||
+     (ji && Y6A(new ji()) != mI8) ||
+     (mA1 && Y6A(mA1.resolve()) != gI8) ||
+     (gA1 && Y6A(new gA1()) != FI8) ||
+     ($A1 && Y6A(new $A1()) != QI8)
+   )
+     Y6A = function (A) {
+       var K = HF(A),
+         q = K == d95 ? A.constructor : void 0,
+         Y = q ? JF(q) : "";
+       if (Y)
+         switch (Y) {
+           case c95:
+             return UI8;
+           case l95:
+             return mI8;
+           case i95:
+             return gI8;
+           case n95:
+             return FI8;
+           case r95:
+             return QI8;
+         }
+       return K;
+     };
+   mHA = Y6A;
+ });

+++ Added s95 (pretty-v2.1.20.js:95383-95389)
+ function s95(A) {
+   var K = A.length,
+     q = new A.constructor(K);
+   if (K && typeof A[0] == "string" && a95.call(A, "index"))
+     ((q.index = A.index), (q.input = A.input));
+   return q;
+ }

+++ Added dI8 (pretty-v2.1.20.js:95391-95394)
+ var dI8 = C(() => {
+   ((o95 = Object.prototype), (a95 = o95.hasOwnProperty));
+   pI8 = s95;
+ });

+++ Added cI8 (pretty-v2.1.20.js:95396-95399)
+ var cI8 = C(() => {
+   yR();
+   ((t95 = FX.Uint8Array), (op1 = t95));
+ });

+++ Added e95 (pretty-v2.1.20.js:95400-95403)
+ function e95(A) {
+   var K = new A.constructor(A.byteLength);
+   return (new op1(K).set(new op1(A)), K);
+ }

+++ Added QA1 (pretty-v2.1.20.js:95405-95408)
+ var QA1 = C(() => {
+   cI8();
+   gHA = e95;
+ });

+++ Added AY5 (pretty-v2.1.20.js:95409-95412)
+ function AY5(A, K) {
+   var q = K ? gHA(A.buffer) : A.buffer;
+   return new A.constructor(q, A.byteOffset, A.byteLength);
+ }

+++ Added iI8 (pretty-v2.1.20.js:95414-95417)
+ var iI8 = C(() => {
+   QA1();
+   lI8 = AY5;
+ });

+++ Added qY5 (pretty-v2.1.20.js:95418-95421)
+ function qY5(A) {
+   var K = new A.constructor(A.source, KY5.exec(A));
+   return ((K.lastIndex = A.lastIndex), K);
+ }

+++ Added rI8 (pretty-v2.1.20.js:95423-95426)
+ var rI8 = C(() => {
+   KY5 = /\w*$/;
+   nI8 = qY5;
+ });

+++ Added YY5 (pretty-v2.1.20.js:95427-95429)
+ function YY5(A) {
+   return aI8 ? Object(aI8.call(A)) : {};
+ }

+++ Added tI8 (pretty-v2.1.20.js:95431-95435)
+ var tI8 = C(() => {
+   HA1();
+   ((oI8 = wF ? wF.prototype : void 0), (aI8 = oI8 ? oI8.valueOf : void 0));
+   sI8 = YY5;
+ });

+++ Added zY5 (pretty-v2.1.20.js:95436-95439)
+ function zY5(A, K) {
+   var q = K ? gHA(A.buffer) : A.buffer;
+   return new A.constructor(q, A.byteOffset, A.length);
+ }

+++ Added AS8 (pretty-v2.1.20.js:95441-95444)
+ var AS8 = C(() => {
+   QA1();
+   eI8 = zY5;
+ });

+++ Added EY5 (pretty-v2.1.20.js:95445-95477)
+ function EY5(A, K, q) {
+   var Y = A.constructor;
+   switch (K) {
+     case GY5:
+       return gHA(A);
+     case wY5:
+     case HY5:
+       return new Y(+A);
+     case WY5:
+       return lI8(A, q);
+     case DY5:
+     case MY5:
+     case jY5:
+     case PY5:
+     case VY5:
+     case fY5:
+     case NY5:
+     case TY5:
+     case vY5:
+       return eI8(A, q);
+     case JY5:
+       return new Y();
+     case OY5:
+     case _Y5:
+       return new Y(A);
+     case XY5:
+       return nI8(A);
+     case $Y5:
+       return new Y();
+     case ZY5:
+       return sI8(A);
+   }
+ }

+++ Added wY5 (pretty-v2.1.20.js:95478-95478)
+ var wY5 = "[object Boolean]",

+++ Added HY5 (pretty-v2.1.20.js:95479-95479)
+   HY5 = "[object Date]",

+++ Added JY5 (pretty-v2.1.20.js:95480-95480)
+   JY5 = "[object Map]",

+++ Added OY5 (pretty-v2.1.20.js:95481-95481)
+   OY5 = "[object Number]",

+++ Added XY5 (pretty-v2.1.20.js:95482-95482)
+   XY5 = "[object RegExp]",

+++ Added $Y5 (pretty-v2.1.20.js:95483-95483)
+   $Y5 = "[object Set]",

+++ Added _Y5 (pretty-v2.1.20.js:95484-95484)
+   _Y5 = "[object String]",

+++ Added ZY5 (pretty-v2.1.20.js:95485-95485)
+   ZY5 = "[object Symbol]",

+++ Added GY5 (pretty-v2.1.20.js:95486-95486)
+   GY5 = "[object ArrayBuffer]",

+++ Added WY5 (pretty-v2.1.20.js:95487-95487)
+   WY5 = "[object DataView]",

+++ Added DY5 (pretty-v2.1.20.js:95488-95488)
+   DY5 = "[object Float32Array]",

+++ Added MY5 (pretty-v2.1.20.js:95489-95489)
+   MY5 = "[object Float64Array]",

+++ Added jY5 (pretty-v2.1.20.js:95490-95490)
+   jY5 = "[object Int8Array]",

+++ Added PY5 (pretty-v2.1.20.js:95491-95491)
+   PY5 = "[object Int16Array]",

+++ Added VY5 (pretty-v2.1.20.js:95492-95492)
+   VY5 = "[object Int32Array]",

+++ Added fY5 (pretty-v2.1.20.js:95493-95493)
+   fY5 = "[object Uint8Array]",

+++ Added NY5 (pretty-v2.1.20.js:95494-95494)
+   NY5 = "[object Uint8ClampedArray]",

+++ Added TY5 (pretty-v2.1.20.js:95495-95495)
+   TY5 = "[object Uint16Array]",

+++ Added vY5 (pretty-v2.1.20.js:95496-95496)
+   vY5 = "[object Uint32Array]",

+++ Added kY5 (pretty-v2.1.20.js:95506-95508)
+ function kY5(A) {
+   return typeof A.constructor == "function" && !RHA(A) ? UR8(yA1(A)) : {};
+ }

+++ Added zS8 (pretty-v2.1.20.js:95510-95515)
+ var zS8 = C(() => {
+   pR8();
+   cp1();
+   MA1();
+   YS8 = kY5;
+ });

+++ Added LY5 (pretty-v2.1.20.js:95516-95518)
+ function LY5(A) {
+   return $b(A) && mHA(A) == CY5;
+ }

+++ Added CY5 (pretty-v2.1.20.js:95519-95519)
+ var CY5 = "[object Map]",

+++ Added HS8 (pretty-v2.1.20.js:95521-95525)
+ var HS8 = C(() => {
+   FA1();
+   kHA();
+   wS8 = LY5;
+ });

+++ Added XS8 (pretty-v2.1.20.js:95527-95532)
+ var XS8 = C(() => {
+   HS8();
+   VA1();
+   TA1();
+   ((JS8 = Zb && Zb.isMap), (RY5 = JS8 ? yHA(JS8) : wS8), (OS8 = RY5));
+ });

+++ Added IY5 (pretty-v2.1.20.js:95533-95535)
+ function IY5(A) {
+   return $b(A) && mHA(A) == yY5;
+ }

+++ Added yY5 (pretty-v2.1.20.js:95536-95536)
+ var yY5 = "[object Set]",

+++ Added _S8 (pretty-v2.1.20.js:95538-95542)
+ var _S8 = C(() => {
+   FA1();
+   kHA();
+   $S8 = IY5;
+ });

+++ Added WS8 (pretty-v2.1.20.js:95544-95549)
+ var WS8 = C(() => {
+   _S8();
+   VA1();
+   TA1();
+   ((ZS8 = Zb && Zb.isSet), (SY5 = ZS8 ? yHA(ZS8) : $S8), (GS8 = SY5));
+ });

+++ Added UA1 (pretty-v2.1.20.js:95550-95593)
+ function UA1(A, K, q, Y, z, w) {
+   var H,
+     J = K & hY5,
+     O = K & bY5,
+     X = K & xY5;
+   if (q) H = z ? q(A, Y, z, w) : q(A);
+   if (H !== void 0) return H;
+   if (!_b(A)) return A;
+   var $ = CHA(A);
+   if ($) {
+     if (((H = pI8(A)), !J)) return dR8(A, H);
+   } else {
+     var _ = mHA(A),
+       Z = _ == MS8 || _ == FY5;
+     if (lEA(A)) return lp1(A, J);
+     if (_ == jS8 || _ == DS8 || (Z && !z)) {
+       if (((H = O || Z ? {} : YS8(A)), !J))
+         return O ? RI8(A, MI8(H, A)) : CI8(A, WI8(H, A));
+     } else {
+       if (!ow[_]) return z ? A : {};
+       H = KS8(A, _, J);
+     }
+   }
+   w || (w = new ZI8());
+   var G = w.get(A);
+   if (G) return G;
+   if ((w.set(A, H), GS8(A)))
+     A.forEach(function (M) {
+       H.add(UA1(M, K, q, M, A, w));
+     });
+   else if (OS8(A))
+     A.forEach(function (M, j) {
+       H.set(j, UA1(M, K, q, j, A, w));
+     });
+   var W = X ? (O ? hI8 : II8) : O ? SHA : IHA,
+     D = $ ? void 0 : W(A);
+   return (
+     iR8(D || A, function (M, j) {
+       if (D) ((j = M), (M = A[j]));
+       GA1(H, j, UA1(M, K, q, j, A, w));
+     }),
+     H
+   );
+ }

+++ Added DS8 (pretty-v2.1.20.js:95597-95597)
+   DS8 = "[object Arguments]",

+++ Added uY5 (pretty-v2.1.20.js:95598-95598)
+   uY5 = "[object Array]",

+++ Added BY5 (pretty-v2.1.20.js:95599-95599)
+   BY5 = "[object Boolean]",

+++ Added mY5 (pretty-v2.1.20.js:95600-95600)
+   mY5 = "[object Date]",

+++ Added gY5 (pretty-v2.1.20.js:95601-95601)
+   gY5 = "[object Error]",

+++ Added MS8 (pretty-v2.1.20.js:95602-95602)
+   MS8 = "[object Function]",

+++ Added FY5 (pretty-v2.1.20.js:95603-95603)
+   FY5 = "[object GeneratorFunction]",

+++ Added QY5 (pretty-v2.1.20.js:95604-95604)
+   QY5 = "[object Map]",

+++ Added UY5 (pretty-v2.1.20.js:95605-95605)
+   UY5 = "[object Number]",

+++ Added jS8 (pretty-v2.1.20.js:95606-95606)
+   jS8 = "[object Object]",

+++ Added pY5 (pretty-v2.1.20.js:95607-95607)
+   pY5 = "[object RegExp]",

+++ Added dY5 (pretty-v2.1.20.js:95608-95608)
+   dY5 = "[object Set]",

+++ Added cY5 (pretty-v2.1.20.js:95609-95609)
+   cY5 = "[object String]",

+++ Added lY5 (pretty-v2.1.20.js:95610-95610)
+   lY5 = "[object Symbol]",

+++ Added iY5 (pretty-v2.1.20.js:95611-95611)
+   iY5 = "[object WeakMap]",

+++ Added nY5 (pretty-v2.1.20.js:95612-95612)
+   nY5 = "[object ArrayBuffer]",

+++ Added rY5 (pretty-v2.1.20.js:95613-95613)
+   rY5 = "[object DataView]",

+++ Added oY5 (pretty-v2.1.20.js:95614-95614)
+   oY5 = "[object Float32Array]",

+++ Added aY5 (pretty-v2.1.20.js:95615-95615)
+   aY5 = "[object Float64Array]",

+++ Added sY5 (pretty-v2.1.20.js:95616-95616)
+   sY5 = "[object Int8Array]",

+++ Added tY5 (pretty-v2.1.20.js:95617-95617)
+   tY5 = "[object Int16Array]",

+++ Added eY5 (pretty-v2.1.20.js:95618-95618)
+   eY5 = "[object Int32Array]",

+++ Added A25 (pretty-v2.1.20.js:95619-95619)
+   A25 = "[object Uint8Array]",

+++ Added K25 (pretty-v2.1.20.js:95620-95620)
+   K25 = "[object Uint8ClampedArray]",

+++ Added q25 (pretty-v2.1.20.js:95621-95621)
+   q25 = "[object Uint16Array]",

+++ Added Y25 (pretty-v2.1.20.js:95622-95622)
+   Y25 = "[object Uint32Array]",

+++ Added VS8 (pretty-v2.1.20.js:95625-95674)
+ var VS8 = C(() => {
+   GI8();
+   nR8();
+   xp1();
+   DI8();
+   jI8();
+   TI8();
+   cR8();
+   LI8();
+   yI8();
+   SI8();
+   bI8();
+   FA1();
+   dI8();
+   qS8();
+   zS8();
+   JA1();
+   gp1();
+   XS8();
+   LHA();
+   WS8();
+   kA1();
+   CA1();
+   ow = {};
+   ow[DS8] =
+     ow[uY5] =
+     ow[nY5] =
+     ow[rY5] =
+     ow[BY5] =
+     ow[mY5] =
+     ow[oY5] =
+     ow[aY5] =
+     ow[sY5] =
+     ow[tY5] =
+     ow[eY5] =
+     ow[QY5] =
+     ow[UY5] =
+     ow[jS8] =
+     ow[pY5] =
+     ow[dY5] =
+     ow[cY5] =
+     ow[lY5] =
+     ow[A25] =
+     ow[K25] =
+     ow[q25] =
+     ow[Y25] =
+       !0;
+   ow[gY5] = ow[MS8] = ow[iY5] = !1;
+   PS8 = UA1;
+ });

+++ Added H25 (pretty-v2.1.20.js:95675-95677)
+ function H25(A) {
+   return PS8(A, z25 | w25);
+ }

+++ Added fS8 (pretty-v2.1.20.js:95681-95684)
+ var fS8 = C(() => {
+   VS8();
+   ap1 = H25;
+ });

+++ Added LS8 (pretty-v2.1.20.js:95903-95945)
+ function LS8() {
+   let A = [];
+   try {
+     let q = _25("npm root -g", {
+       encoding: "utf8",
+       timeout: 5000,
+       stdio: ["pipe", "pipe", "ignore"],
+     }).trim();
+     if (q) A.push(BE(q, "@anthropic-ai", "sandbox-runtime"));
+   } catch {}
+   let K = Z25();
+   return (
+     A.push(
+       BE("/usr", "lib", "node_modules", "@anthropic-ai", "sandbox-runtime"),
+       BE(
+         "/usr",
+         "local",
+         "lib",
+         "node_modules",
+         "@anthropic-ai",
+         "sandbox-runtime",
+       ),
+       BE(
+         "/opt",
+         "homebrew",
+         "lib",
+         "node_modules",
+         "@anthropic-ai",
+         "sandbox-runtime",
+       ),
+       BE(K, ".npm", "lib", "node_modules", "@anthropic-ai", "sandbox-runtime"),
+       BE(
+         K,
+         ".npm-global",
+         "lib",
+         "node_modules",
+         "@anthropic-ai",
+         "sandbox-runtime",
+       ),
+     ),
+     A
+   );
+ }

+++ Added RS8 (pretty-v2.1.20.js:95973-95979)
+ function RS8(A) {
+   let K = Yd1();
+   if (!K) return [];
+   let q = X25($25(import.meta.url)),
+     Y = BE("vendor", "seccomp", K, A);
+   return [BE(q, Y), BE(q, "..", "..", Y), BE(q, "..", Y)];
+ }

+++ Added zd1 (pretty-v2.1.20.js:95980-95985)
+ function zd1(A) {
+   let K = A ?? "";
+   if (Kd1.has(K)) return Kd1.get(K);
+   let q = G25(A);
+   return (Kd1.set(K, q), q);
+ }

+++ Added G25 (pretty-v2.1.20.js:95986-96026)
+ function G25(A) {
+   if (A) {
+     if (z6A.existsSync(A))
+       return (
+         C8(`[SeccompFilter] Using BPF filter from explicit path: ${A}`),
+         A
+       );
+     C8(`[SeccompFilter] Explicit path provided but file not found: ${A}`);
+   }
+   let K = Yd1();
+   if (!K)
+     return (
+       C8(
+         `[SeccompFilter] Cannot find pre-generated BPF filter: unsupported architecture ${process.arch}`,
+       ),
+       null
+     );
+   C8(`[SeccompFilter] Detected architecture: ${K}`);
+   for (let q of RS8("unix-block.bpf"))
+     if (z6A.existsSync(q))
+       return (
+         C8(`[SeccompFilter] Found pre-generated BPF filter: ${q} (${K})`),
+         q
+       );
+   for (let q of LS8()) {
+     let Y = BE(q, "vendor", "seccomp", K, "unix-block.bpf");
+     if (z6A.existsSync(Y))
+       return (
+         C8(
+           `[SeccompFilter] Found pre-generated BPF filter in global install: ${Y} (${K})`,
+         ),
+         Y
+       );
+   }
+   return (
+     C8(
+       `[SeccompFilter] Pre-generated BPF filter not found in any expected location (${K})`,
+     ),
+     null
+   );
+ }

+++ Added AkA (pretty-v2.1.20.js:96027-96032)
+ function AkA(A) {
+   let K = A ?? "";
+   if (qd1.has(K)) return qd1.get(K);
+   let q = W25(A);
+   return (qd1.set(K, q), q);
+ }

+++ Added W25 (pretty-v2.1.20.js:96033-96072)
+ function W25(A) {
+   if (A) {
+     if (z6A.existsSync(A))
+       return (
+         C8(
+           `[SeccompFilter] Using apply-seccomp binary from explicit path: ${A}`,
+         ),
+         A
+       );
+     C8(`[SeccompFilter] Explicit path provided but file not found: ${A}`);
+   }
+   let K = Yd1();
+   if (!K)
+     return (
+       C8(
+         `[SeccompFilter] Cannot find apply-seccomp binary: unsupported architecture ${process.arch}`,
+       ),
+       null
+     );
+   C8(`[SeccompFilter] Looking for apply-seccomp binary for architecture: ${K}`);
+   for (let q of RS8("apply-seccomp"))
+     if (z6A.existsSync(q))
+       return (C8(`[SeccompFilter] Found apply-seccomp binary: ${q} (${K})`), q);
+   for (let q of LS8()) {
+     let Y = BE(q, "vendor", "seccomp", K, "apply-seccomp");
+     if (z6A.existsSync(Y))
+       return (
+         C8(
+           `[SeccompFilter] Found apply-seccomp binary in global install: ${Y} (${K})`,
+         ),
+         Y
+       );
+   }
+   return (
+     C8(
+       `[SeccompFilter] apply-seccomp binary not found in any expected location (${K})`,
+     ),
+     null
+   );
+ }

+++ Added sS8 (pretty-v2.1.20.js:97153-97167)
+ function sS8(A) {
+   if (!aS8()) return { errors: ["Unsupported platform"], warnings: [] };
+   let K = [],
+     q = [],
+     Y = A ?? m5?.ripgrep ?? { command: "rg" };
+   if (
+     I25("which", [Y.command], { stdio: "ignore", timeout: 1000 }).status !== 0
+   )
+     K.push(`ripgrep (${Y.command}) not found`);
+   if (uE() === "linux") {
+     let H = uS8(m5?.seccomp);
+     (K.push(...H.errors), q.push(...H.warnings));
+   }
+   return { errors: K, warnings: q };
+ }

+++ Added Dd1 (pretty-v2.1.20.js:97800-97804)
+ var Dd1 = C(() => {
+   oA1();
+   qkA();
+   $F = a25;
+ });

+++ Added aA1 (pretty-v2.1.20.js:97812-97815)
+ var aA1 = C(() => {
+   Dd1();
+   Oh8 = $F;
+ });

+++ Added Xb8 (pretty-v2.1.20.js:102813-102820)
+ function Xb8() {
+   try {
+     let A = q5();
+     return Ob8(A);
+   } catch (A) {
+     return (h(`Failed to check enabledPlatforms: ${A}`), !0);
+   }
+ }

+++ Added NH5 (pretty-v2.1.20.js:103044-103048)
+ function NH5() {
+   if (i4("tengu_marble_kite", !1)) return "";
+   return `
+ - If this is an existing file, you MUST use the ${K5} tool first to read the file's contents. This tool will fail if you did not read the file first.`;
+ }

+++ Added Iw4 (pretty-v2.1.20.js:160490-160674)
+ var Iw4 = C(() => {
+   Rw4 = `Use this tool to create and manage a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user.
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
+ * Uses the ${n5} tool to add a comment to the calculateTotal function *
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

+++ Added Kj (pretty-v2.1.20.js:160878-160884)
+ function Kj() {
+   if (process.env.CLAUDE_CODE_TASK_LIST_ID)
+     return process.env.CLAUDE_CODE_TASK_LIST_ID;
+   let A = fk();
+   if (A) return A.parentSessionId;
+   return e3() || i1();
+ }

+++ Added gw4 (pretty-v2.1.20.js:160952-160968)
+ function gw4(A, K) {
+   let q = SRA(A, K);
+   if (!qQ(q)) return !1;
+   try {
+     Bw4(q);
+     let Y = JZ(A);
+     for (let z of Y) {
+       let w = z.blocks.filter((J) => J !== K),
+         H = z.blockedBy.filter((J) => J !== K);
+       if (w.length !== z.blocks.length || H.length !== z.blockedBy.length)
+         _y(A, z.id, { blocks: w, blockedBy: H });
+     }
+     return (Jq1(), !0);
+   } catch {
+     return !1;
+   }
+ }

+++ Added Cr3 (pretty-v2.1.20.js:160990-160992)
+ function Cr3(A) {
+   return IRA(Zy(A), ".lock");
+ }

+++ Added Lr3 (pretty-v2.1.20.js:160993-160998)
+ function Lr3(A) {
+   EOA(A);
+   let K = Cr3(A);
+   if (!qQ(K)) c8(K, "");
+   return K;
+ }

+++ Added j46 (pretty-v2.1.20.js:160999-161029)
+ function j46(A, K, q, Y = {}) {
+   let z = SRA(A, K);
+   if (!qQ(z)) return { success: !1, reason: "task_not_found" };
+   if (Y.checkAgentBusy) return Rr3(A, K, q);
+   let w;
+   try {
+     w = Hq1.default.lockSync(z);
+     let H = YQ(A, K);
+     if (!H) return { success: !1, reason: "task_not_found" };
+     if (H.owner && H.owner !== q)
+       return { success: !1, reason: "already_claimed", task: H };
+     if (H.status === "completed")
+       return { success: !1, reason: "already_resolved", task: H };
+     let J = JZ(A),
+       O = new Set(J.filter((_) => _.status !== "completed").map((_) => _.id)),
+       X = H.blockedBy.filter((_) => O.has(_));
+     if (X.length > 0)
+       return { success: !1, reason: "blocked", task: H, blockedByTasks: X };
+     return { success: !0, task: _y(A, K, { owner: q }) };
+   } catch (H) {
+     return (
+       h(
+         `[Tasks] Failed to claim task ${K}: ${H instanceof Error ? H.message : String(H)}`,
+       ),
+       qA(H instanceof Error ? H : Error(String(H))),
+       { success: !1, reason: "task_not_found" }
+     );
+   } finally {
+     if (w) w();
+   }
+ }

+++ Added Rr3 (pretty-v2.1.20.js:161030-161068)
+ function Rr3(A, K, q) {
+   let Y = Lr3(A),
+     z;
+   try {
+     z = Hq1.default.lockSync(Y);
+     let w = JZ(A),
+       H = w.find((_) => _.id === K);
+     if (!H) return { success: !1, reason: "task_not_found" };
+     if (H.owner && H.owner !== q)
+       return { success: !1, reason: "already_claimed", task: H };
+     if (H.status === "completed")
+       return { success: !1, reason: "already_resolved", task: H };
+     let J = new Set(w.filter((_) => _.status !== "completed").map((_) => _.id)),
+       O = H.blockedBy.filter((_) => J.has(_));
+     if (O.length > 0)
+       return { success: !1, reason: "blocked", task: H, blockedByTasks: O };
+     let X = w.filter(
+       (_) => _.status !== "completed" && _.owner === q && _.id !== K,
+     );
+     if (X.length > 0)
+       return {
+         success: !1,
+         reason: "agent_busy",
+         task: H,
+         busyWithTasks: X.map((_) => _.id),
+       };
+     return { success: !0, task: _y(A, K, { owner: q }) };
+   } catch (w) {
+     return (
+       h(
+         `[Tasks] Failed to claim task ${K} with busy check: ${w instanceof Error ? w.message : String(w)}`,
+       ),
+       qA(w instanceof Error ? w : Error(String(w))),
+       { success: !1, reason: "task_not_found" }
+     );
+   } finally {
+     if (z) z();
+   }
+ }

+++ Added Bn (pretty-v2.1.20.js:169933-169971)
+ var Bn = C(() => {
+   ((D3 = {
+     All: "all",
+     Horizontal: "horizontal",
+     Vertical: "vertical",
+     Left: "left",
+     Right: "right",
+     Top: "top",
+     Bottom: "bottom",
+     Start: "start",
+     End: "end",
+   }),
+     (jq1 = { All: "all", Column: "column", Row: "row" }),
+     (hV = { Flex: "flex", None: "none" }),
+     (BRA = {
+       Row: "row",
+       RowReverse: "row-reverse",
+       Column: "column",
+       ColumnReverse: "column-reverse",
+     }),
+     (wQ = {
+       Auto: "auto",
+       Stretch: "stretch",
+       FlexStart: "flex-start",
+       Center: "center",
+       FlexEnd: "flex-end",
+     }),
+     (I8A = {
+       FlexStart: "flex-start",
+       Center: "center",
+       FlexEnd: "flex-end",
+       SpaceBetween: "space-between",
+       SpaceAround: "space-around",
+       SpaceEvenly: "space-evenly",
+     }),
+     (Pq1 = { NoWrap: "nowrap", Wrap: "wrap", WrapReverse: "wrap-reverse" }),
+     (U46 = { Relative: "relative", Absolute: "absolute" }),
+     (HQ = { Undefined: "undefined", Exactly: "exactly", AtMost: "at-most" }));
+ });

+++ Added o46 (pretty-v2.1.20.js:171120-171122)
+ var o46 = C(() => {
+   QH4 = r46;
+ });

+++ Added K76 (pretty-v2.1.20.js:171433-171435)
+ var K76 = C(() => {
+   ((Fn = new WeakMap()), (bOA = new WeakMap()));
+ });

+++ Added z76 (pretty-v2.1.20.js:173478-173663)
+ class z76 {
+   yoga;
+   constructor(A) {
+     this.yoga = A;
+   }
+   insertChild(A, K) {
+     this.yoga.insertChild(A.yoga, K);
+   }
+   removeChild(A) {
+     this.yoga.removeChild(A.yoga);
+   }
+   getChildCount() {
+     return this.yoga.getChildCount();
+   }
+   getParent() {
+     let A = this.yoga.getParent();
+     return A ? new z76(A) : null;
+   }
+   calculateLayout(A, K) {
+     this.yoga.calculateLayout(A, void 0, B8A.LTR);
+   }
+   setMeasureFunc(A) {
+     this.yoga.setMeasureFunc((K, q) => {
+       let Y =
+         q === BOA.Exactly
+           ? HQ.Exactly
+           : q === BOA.AtMost
+             ? HQ.AtMost
+             : HQ.Undefined;
+       return A(K, Y);
+     });
+   }
+   unsetMeasureFunc() {
+     this.yoga.unsetMeasureFunc();
+   }
+   markDirty() {
+     this.yoga.markDirty();
+   }
+   getComputedLeft() {
+     return this.yoga.getComputedLeft();
+   }
+   getComputedTop() {
+     return this.yoga.getComputedTop();
+   }
+   getComputedWidth() {
+     return this.yoga.getComputedWidth();
+   }
+   getComputedHeight() {
+     return this.yoga.getComputedHeight();
+   }
+   getComputedBorder(A) {
+     return this.yoga.getComputedBorder(URA[A]);
+   }
+   getComputedPadding(A) {
+     return this.yoga.getComputedPadding(URA[A]);
+   }
+   setWidth(A) {
+     this.yoga.setWidth(A);
+   }
+   setWidthPercent(A) {
+     this.yoga.setWidthPercent(A);
+   }
+   setWidthAuto() {
+     this.yoga.setWidthAuto();
+   }
+   setHeight(A) {
+     this.yoga.setHeight(A);
+   }
+   setHeightPercent(A) {
+     this.yoga.setHeightPercent(A);
+   }
+   setHeightAuto() {
+     this.yoga.setHeightAuto();
+   }
+   setMinWidth(A) {
+     this.yoga.setMinWidth(A);
+   }
+   setMinWidthPercent(A) {
+     this.yoga.setMinWidthPercent(A);
+   }
+   setMinHeight(A) {
+     this.yoga.setMinHeight(A);
+   }
+   setMinHeightPercent(A) {
+     this.yoga.setMinHeightPercent(A);
+   }
+   setMaxWidth(A) {
+     this.yoga.setMaxWidth(A);
+   }
+   setMaxWidthPercent(A) {
+     this.yoga.setMaxWidthPercent(A);
+   }
+   setMaxHeight(A) {
+     this.yoga.setMaxHeight(A);
+   }
+   setMaxHeightPercent(A) {
+     this.yoga.setMaxHeightPercent(A);
+   }
+   setFlexDirection(A) {
+     let K = {
+       row: JQ.Row,
+       "row-reverse": JQ.RowReverse,
+       column: JQ.Column,
+       "column-reverse": JQ.ColumnReverse,
+     };
+     this.yoga.setFlexDirection(K[A]);
+   }
+   setFlexGrow(A) {
+     this.yoga.setFlexGrow(A);
+   }
+   setFlexShrink(A) {
+     this.yoga.setFlexShrink(A);
+   }
+   setFlexBasis(A) {
+     this.yoga.setFlexBasis(A);
+   }
+   setFlexBasisPercent(A) {
+     this.yoga.setFlexBasisPercent(A);
+   }
+   setFlexWrap(A) {
+     let K = {
+       nowrap: F8A.NoWrap,
+       wrap: F8A.Wrap,
+       "wrap-reverse": F8A.WrapReverse,
+     };
+     this.yoga.setFlexWrap(K[A]);
+   }
+   setAlignItems(A) {
+     let K = {
+       auto: oX.Auto,
+       stretch: oX.Stretch,
+       "flex-start": oX.FlexStart,
+       center: oX.Center,
+       "flex-end": oX.FlexEnd,
+     };
+     this.yoga.setAlignItems(K[A]);
+   }
+   setAlignSelf(A) {
+     let K = {
+       auto: oX.Auto,
+       stretch: oX.Stretch,
+       "flex-start": oX.FlexStart,
+       center: oX.Center,
+       "flex-end": oX.FlexEnd,
+     };
+     this.yoga.setAlignSelf(K[A]);
+   }
+   setJustifyContent(A) {
+     let K = {
+       "flex-start": PT.FlexStart,
+       center: PT.Center,
+       "flex-end": PT.FlexEnd,
+       "space-between": PT.SpaceBetween,
+       "space-around": PT.SpaceAround,
+       "space-evenly": PT.SpaceEvenly,
+     };
+     this.yoga.setJustifyContent(K[A]);
+   }
+   setDisplay(A) {
+     this.yoga.setDisplay(A === "flex" ? m8A.Flex : m8A.None);
+   }
+   getDisplay() {
+     return this.yoga.getDisplay() === m8A.None ? hV.None : hV.Flex;
+   }
+   setPositionType(A) {
+     this.yoga.setPositionType(A === "absolute" ? mOA.Absolute : mOA.Relative);
+   }
+   setMargin(A, K) {
+     this.yoga.setMargin(URA[A], K);
+   }
+   setPadding(A, K) {
+     this.yoga.setPadding(URA[A], K);
+   }
+   setBorder(A, K) {
+     this.yoga.setBorder(URA[A], K);
+   }
+   setGap(A, K) {
+     this.yoga.setGap(No3[A], K);
+   }
+   free() {
+     this.yoga.free();
+   }
+   freeRecursive() {
+     this.yoga.freeRecursive();
+   }
+ }

+++ Added _J4 (pretty-v2.1.20.js:173664-173667)
+ async function _J4() {
+   if (hq1) return;
+   hq1 = await XJ4();
+ }

+++ Added ZJ4 (pretty-v2.1.20.js:173668-173671)
+ function ZJ4() {
+   if (!hq1) throw Error("Yoga not loaded");
+   return new z76(hq1.Node.create());
+ }

+++ Added GJ4 (pretty-v2.1.20.js:173673-173688)
+ var GJ4 = C(() => {
+   $J4();
+   Bn();
+   ((URA = {
+     all: K_.All,
+     horizontal: K_.Horizontal,
+     vertical: K_.Vertical,
+     left: K_.Left,
+     right: K_.Right,
+     top: K_.Top,
+     bottom: K_.Bottom,
+     start: K_.Start,
+     end: K_.End,
+   }),
+     (No3 = { all: g8A.All, column: g8A.Column, row: g8A.Row }));
+ });

+++ Added pRA (pretty-v2.1.20.js:173689-173696)
+ function pRA(A, K) {
+   return {
+     top: A.top + K.top,
+     right: A.right + K.right,
+     bottom: A.bottom + K.bottom,
+     left: A.left + K.left,
+   };
+ }

+++ Added xq1 (pretty-v2.1.20.js:173704-173708)
+ function xq1(A, K, q) {
+   if (K !== void 0 && A < K) return K;
+   if (q !== void 0 && A > q) return q;
+   return A;
+ }

+++ Added H76 (pretty-v2.1.20.js:173710-173712)
+ function H76(A) {
+   return { type: "fixed", value: A };
+ }

+++ Added J76 (pretty-v2.1.20.js:173713-173715)
+ function J76(A) {
+   return { type: "percent", value: A };
+ }

+++ Added WJ4 (pretty-v2.1.20.js:173717-174325)
+ var WJ4 = C(() => {
+   w76();
+   _x = class _x {
+     style;
+     measureFunc;
+     children = [];
+     parent = null;
+     layout = { x: 0, y: 0, width: 0, height: 0 };
+     dirty = !0;
+     lastConstraints = null;
+     constructor(A = {}, K) {
+       ((this.style = A), (this.measureFunc = K ?? null));
+     }
+     appendChild(A) {
+       ((A.parent = this), this.children.push(A), this.markDirty());
+     }
+     insertChild(A, K) {
+       ((A.parent = this), this.children.splice(K, 0, A), this.markDirty());
+     }
+     removeChild(A) {
+       let K = this.children.indexOf(A);
+       if (K !== -1)
+         ((A.parent = null), this.children.splice(K, 1), this.markDirty());
+     }
+     markDirty() {
+       if (this.dirty) return;
+       ((this.dirty = !0), this.parent?.markDirty());
+     }
+     calculateLayout(A, K) {
+       (this.measureNode(A, K),
+         (this.layout.x = 0),
+         (this.layout.y = 0),
+         this.positionChildren(),
+         (this.dirty = !1));
+     }
+     measureNode(A, K) {
+       let q =
+         this.lastConstraints !== null &&
+         this.lastConstraints.width === A &&
+         this.lastConstraints.height === K;
+       if (!this.dirty && q) return;
+       this.lastConstraints = { width: A, height: K };
+       let { style: Y } = this,
+         z = this.getPadding(),
+         w = this.getBorder(),
+         H = pRA(z, w),
+         J = this.resolveDimension(Y.width, A, Y.minWidth, Y.maxWidth);
+       if (J === void 0 && !Y.width && A !== void 0 && !this.parent) J = A;
+       let O = this.resolveDimension(Y.height, K, Y.minHeight, Y.maxHeight);
+       if (this.measureFunc && this.children.length === 0) {
+         let X = J ?? A,
+           $ = X !== void 0 ? X - H.left - H.right : void 0,
+           _ = O !== void 0 ? O - H.top - H.bottom : void 0,
+           Z = this.measureFunc($, _);
+         if (J === void 0) J = Z.width + H.left + H.right;
+         if (O === void 0) O = Z.height + H.top + H.bottom;
+       }
+       if (this.children.length > 0) {
+         let X = this.measureChildren(J ?? A, O, H);
+         if (J === void 0) J = X.contentWidth + H.left + H.right;
+         if (O === void 0) O = X.contentHeight + H.top + H.bottom;
+       }
+       ((J = xq1(J ?? H.left + H.right, Y.minWidth, Y.maxWidth)),
+         (O = xq1(O ?? H.top + H.bottom, Y.minHeight, Y.maxHeight)),
+         (this.layout.width = J),
+         (this.layout.height = O),
+         (this.dirty = !1));
+     }
+     measureChildren(A, K, q) {
+       let { style: Y, children: z } = this,
+         w = Y.flexDirection ?? "column",
+         H = w === "row" || w === "row-reverse",
+         O = (Y.flexWrap ?? "nowrap") !== "nowrap",
+         X = H ? (Y.columnGap ?? Y.gap ?? 0) : (Y.rowGap ?? Y.gap ?? 0),
+         $ = H ? (Y.rowGap ?? Y.gap ?? 0) : (Y.columnGap ?? Y.gap ?? 0),
+         _ = X,
+         G = z.filter((R) => !R.isHidden()).filter((R) => !R.isAbsolute()),
+         W = A !== void 0 ? A - q.left - q.right : void 0,
+         D = K !== void 0 ? K - q.top - q.bottom : void 0,
+         M = 0,
+         j = 0,
+         P = 0,
+         V = [];
+       for (let R of G) {
+         let b = this.getGrowFactor(R, H);
+         P += b;
+         let S = R.getMargin(),
+           B = H ? S.left + S.right : S.top + S.bottom,
+           x = H ? S.top + S.bottom : S.left + S.right;
+         R.measureNode(W, D);
+         let F = (H ? R.layout.height : R.layout.width) + x,
+           Q;
+         if (R.style.flexBasis !== void 0) {
+           let u = R.style.flexBasis;
+           if (H) R.layout.width = u;
+           else R.layout.height = u;
+           Q = u + B;
+         } else if (b > 0)
+           if ((H ? W : D) !== void 0) {
+             if (H) R.layout.width = 0;
+             else R.layout.height = 0;
+             Q = B;
+           } else Q = (H ? R.layout.width : R.layout.height) + B;
+         else Q = (H ? R.layout.width : R.layout.height) + B;
+         (V.push({ main: Q, cross: F, grow: b }),
+           (M += Q),
+           (j = Math.max(j, F)));
+       }
+       let N = G.length > 1 ? _ * (G.length - 1) : 0,
+         T = H ? W : D,
+         k = M + N;
+       if (T !== void 0 && P > 0) {
+         let R = Math.max(0, T - M - N),
+           b = 0,
+           S = 0;
+         for (let B = 0; B < G.length; B++) {
+           let x = G[B],
+             F = V[B];
+           if (F.grow > 0) {
+             S += F.grow;
+             let Q = Math.round((R * S) / P),
+               u = Q - b;
+             b = Q;
+             let a = (H ? x.layout.width : x.layout.height) + u;
+             if (H) x.layout.width = a;
+             else x.layout.height = a;
+             let l = x.getMargin(),
+               e = H ? l.left + l.right : l.top + l.bottom;
+             V[B] = { main: a + e, cross: F.cross, grow: F.grow };
+           }
+         }
+         k = T;
+       }
+       if (T !== void 0 && k > T) {
+         let R = k - T,
+           b = G.map((B, x) => {
+             let F = B.style.flexShrink ?? 0,
+               Q = H ? B.layout.width : B.layout.height,
+               u = H ? (B.style.minWidth ?? 0) : (B.style.minHeight ?? 0);
+             return {
+               index: x,
+               child: B,
+               shrinkFactor: F,
+               currentSize: Q,
+               minSize: u,
+               canShrink: F > 0 && Q > u,
+             };
+           }),
+           S = 0;
+         for (let B of b) if (B.canShrink) S += B.currentSize * B.shrinkFactor;
+         if (S > 0) {
+           let B = 0,
+             x = 0;
+           for (let F of b) {
+             if (!F.canShrink) continue;
+             let Q = F.currentSize * F.shrinkFactor;
+             x += Q;
+             let d = Math.round((R * x) / S) - B,
+               a = F.currentSize - F.minSize;
+             if (d > a) d = a;
+             if (((B += d), (F.currentSize -= d), H))
+               F.child.layout.width = F.currentSize;
+             else F.child.layout.height = F.currentSize;
+             let l = F.child.getMargin(),
+               e = H ? l.left + l.right : l.top + l.bottom;
+             V[F.index] = {
+               main: F.currentSize + e,
+               cross: V[F.index].cross,
+               grow: V[F.index].grow,
+             };
+           }
+         }
+         k = N;
+         for (let B of V) k += B.main;
+       }
+       if (O && G.length > 0) {
+         let R = H ? W : D,
+           b = this.calculateFlexLines(G, R, H, X),
+           S = 0,
+           B = 0;
+         for (let x = 0; x < b.length; x++) {
+           let F = b[x];
+           ((S = Math.max(S, F.mainSize)), (B += F.crossSize + (x > 0 ? $ : 0)));
+         }
+         return { contentWidth: H ? S : B, contentHeight: H ? B : S };
+       }
+       return { contentWidth: H ? k : j, contentHeight: H ? j : k };
+     }
+     positionChildren() {
+       let { style: A, children: K, layout: q } = this;
+       if (K.length === 0) return;
+       let Y = K.filter((x) => !x.isHidden()),
+         z = Y.filter((x) => !x.isAbsolute()),
+         w = Y.filter((x) => x.isAbsolute()),
+         H = pRA(this.getPadding(), this.getBorder()),
+         J = q.width - H.left - H.right,
+         O = q.height - H.top - H.bottom;
+       for (let x of w) {
+         x.measureNode(J, O);
+         let F;
+         if (x.style.left !== void 0) F = q.x + H.left + x.style.left;
+         else if (x.style.right !== void 0)
+           F = q.x + H.left + J - x.layout.width - x.style.right;
+         else F = q.x + H.left;
+         let Q;
+         if (x.style.top !== void 0) Q = q.y + H.top + x.style.top;
+         else if (x.style.bottom !== void 0)
+           Q = q.y + H.top + O - x.layout.height - x.style.bottom;
+         else Q = q.y + H.top;
+         ((x.layout.x = F), (x.layout.y = Q), x.positionChildren());
+       }
+       if (z.length === 0) return;
+       let X = A.flexDirection ?? "column",
+         $ = A.alignItems ?? "stretch",
+         _ = A.justifyContent ?? "start",
+         Z = X === "row" || X === "row-reverse",
+         G = A.flexWrap ?? "nowrap",
+         W = G !== "nowrap",
+         D = Z ? (A.columnGap ?? A.gap ?? 0) : (A.rowGap ?? A.gap ?? 0),
+         M = Z ? (A.rowGap ?? A.gap ?? 0) : (A.columnGap ?? A.gap ?? 0),
+         j = D,
+         P = X === "row-reverse" || X === "column-reverse";
+       if (W) {
+         this.positionWrappedChildren(z, q, H, J, O, Z, G, $, _, D, M, P);
+         return;
+       }
+       let V = 0;
+       for (let x of z) {
+         let F = x.getMargin(),
+           Q = Z ? F.left + F.right : F.top + F.bottom;
+         V += (Z ? x.layout.width : x.layout.height) + Q;
+       }
+       if (z.length > 1) V += j * (z.length - 1);
+       let N = Z ? J : O,
+         T = N - V,
+         k = P ? (_ === "start" ? "end" : _ === "end" ? "start" : _) : _,
+         R =
+           P &&
+           (_ === "space-between" ||
+             _ === "space-around" ||
+             _ === "space-evenly"),
+         b = P && !R ? [...z].reverse() : z,
+         S = 0;
+       switch (k) {
+         case "start":
+           S = 0;
+           break;
+         case "center":
+           S = Math.round(T / 2);
+           break;
+         case "end":
+           S = T;
+           break;
+         case "space-between":
+           S = 0;
+           break;
+         case "space-around":
+         case "space-evenly":
+           break;
+       }
+       if (R) {
+         let x = z.length,
+           F = Math.max(0, T);
+         for (let Q = 0; Q < x; Q++) {
+           let u = z[Q],
+             d = u.getMargin(),
+             a = Z ? u.layout.width : u.layout.height,
+             l = Z ? u.layout.height : u.layout.width,
+             e = Z ? O : J,
+             JA = Z ? d.top : d.left,
+             OA = Z ? d.bottom : d.right,
+             HA = Z ? d.right : d.bottom,
+             DA;
+           if (_ === "space-between" && x > 1)
+             DA = Math.round((F * Q) / (x - 1));
+           else if (_ === "space-around") {
+             let bA = x * 2,
+               YA = Q * 2 + 1;
+             DA = Math.round((F * YA) / bA);
+           } else DA = Math.round((F * (Q + 1)) / (x + 1));
+           let o = 0;
+           for (let bA = 0; bA < Q; bA++) {
+             let YA = z[bA],
+               KA = YA.getMargin(),
+               zA = Z ? KA.left + KA.right : KA.top + KA.bottom;
+             ((o += Z ? YA.layout.width : YA.layout.height), (o += zA + j));
+           }
+           let _A = N - DA - o - a - HA,
+             PA =
+               u.style.alignSelf && u.style.alignSelf !== "auto"
+                 ? u.style.alignSelf
+                 : $,
+             jA = JA + l + OA,
+             yA = JA;
+           switch (PA) {
+             case "start":
+               yA = JA;
+               break;
+             case "center":
+               yA = Math.round((e - jA) / 2) + JA;
+               break;
+             case "end":
+               yA = e - l - OA;
+               break;
+             case "stretch": {
+               if (
+                 ((yA = JA),
+                 !(Z
+                   ? u.style.height?.type === "fixed"
+                   : u.style.width?.type === "fixed"))
+               )
+                 _x.stretchChild(u, Z, e - JA - OA);
+               break;
+             }
+           }
+           if (Z)
+             ((u.layout.x = q.x + H.left + _A), (u.layout.y = q.y + H.top + yA));
+           else
+             ((u.layout.x = q.x + H.left + yA), (u.layout.y = q.y + H.top + _A));
+           u.positionChildren();
+         }
+         return;
+       }
+       let B = S;
+       for (let x = 0; x < b.length; x++) {
+         let F = b[x],
+           Q = F.getMargin(),
+           u = Z ? F.layout.width : F.layout.height,
+           d = Z ? F.layout.height : F.layout.width,
+           a = Z ? O : J,
+           l = Z ? Q.left : Q.top,
+           e = Z ? Q.right : Q.bottom,
+           JA = Z ? Q.top : Q.left,
+           OA = Z ? Q.bottom : Q.right,
+           HA = Math.max(0, T);
+         if (k === "space-between" && b.length > 1) {
+           B = Math.round((HA * x) / (b.length - 1));
+           for (let PA = 0; PA < x; PA++) {
+             let jA = b[PA],
+               yA = jA.getMargin(),
+               bA = Z ? yA.left + yA.right : yA.top + yA.bottom;
+             ((B += Z ? jA.layout.width : jA.layout.height), (B += bA + j));
+           }
+         } else if (k === "space-around") {
+           let PA = b.length * 2,
+             jA = x * 2 + 1;
+           B = Math.round((HA * jA) / PA);
+           for (let yA = 0; yA < x; yA++) {
+             let bA = b[yA],
+               YA = bA.getMargin(),
+               KA = Z ? YA.left + YA.right : YA.top + YA.bottom;
+             ((B += Z ? bA.layout.width : bA.layout.height), (B += KA + j));
+           }
+         } else if (k === "space-evenly") {
+           let PA = b.length + 1;
+           B = Math.round((HA * (x + 1)) / PA);
+           for (let jA = 0; jA < x; jA++) {
+             let yA = b[jA],
+               bA = yA.getMargin(),
+               YA = Z ? bA.left + bA.right : bA.top + bA.bottom;
+             ((B += Z ? yA.layout.width : yA.layout.height), (B += YA + j));
+           }
+         }
+         let DA =
+             F.style.alignSelf && F.style.alignSelf !== "auto"
+               ? F.style.alignSelf
+               : $,
+           o = JA + d + OA,
+           _A = JA;
+         switch (DA) {
+           case "start":
+             _A = JA;
+             break;
+           case "center":
+             _A = Math.round((a - o) / 2) + JA;
+             break;
+           case "end":
+             _A = a - d - OA;
+             break;
+           case "stretch": {
+             if (
+               ((_A = JA),
+               !(Z
+                 ? F.style.height?.type === "fixed"
+                 : F.style.width?.type === "fixed"))
+             )
+               _x.stretchChild(F, Z, a - JA - OA);
+             break;
+           }
+         }
+         if (Z)
+           ((F.layout.x = q.x + H.left + B + l),
+             (F.layout.y = q.y + H.top + _A));
+         else
+           ((F.layout.x = q.x + H.left + _A),
+             (F.layout.y = q.y + H.top + B + l));
+         if (
+           (F.positionChildren(), k === "start" || k === "center" || k === "end")
+         )
+           B += u + l + e + j;
+       }
+     }
+     resolveDimension(A, K, q, Y) {
+       if (!A) return;
+       let z;
+       switch (A.type) {
+         case "fixed":
+           z = A.value;
+           break;
+         case "percent":
+           z = K !== void 0 ? (K * A.value) / 100 : void 0;
+           break;
+         case "fit":
+         case "grow":
+           z = void 0;
+           break;
+       }
+       return z !== void 0 ? xq1(z, q, Y) : void 0;
+     }
+     static stretchChild(A, K, q) {
+       if (K) {
+         let Y = q !== A.layout.height;
+         if (((A.layout.height = q), Y && A.children.length > 0)) {
+           let z = pRA(A.getPadding(), A.getBorder());
+           A.measureChildren(A.layout.width, q, z);
+         }
+       } else {
+         let Y = q !== A.layout.width;
+         if (((A.layout.width = q), Y && A.children.length > 0)) {
+           let z = pRA(A.getPadding(), A.getBorder());
+           A.measureChildren(q, A.layout.height, z);
+         }
+       }
+     }
+     getGrowFactor(A, K) {
+       if (A.style.flexGrow !== void 0) return A.style.flexGrow;
+       let q = K ? A.style.width : A.style.height;
+       if (q?.type === "grow") return q.factor;
+       return 0;
+     }
+     static ZERO = { top: 0, right: 0, bottom: 0, left: 0 };
+     getPadding() {
+       return this.style.padding ?? _x.ZERO;
+     }
+     getMargin() {
+       return this.style.margin ?? _x.ZERO;
+     }
+     getBorder() {
+       return this.style.border ?? _x.ZERO;
+     }
+     isHidden() {
+       return this.style.display === "none";
+     }
+     isAbsolute() {
+       return this.style.position === "absolute";
+     }
+     positionWrappedChildren(A, K, q, Y, z, w, H, J, O, X, $, _) {
+       let Z = w ? Y : z,
+         G = w ? z : Y,
+         W = this.calculateFlexLines(A, Z, w, X);
+       if (H === "wrap-reverse") W.reverse();
+       let D = 0;
+       for (let j = 0; j < W.length; j++) D += W[j].crossSize + (j > 0 ? $ : 0);
+       let M = 0;
+       if (H === "wrap-reverse") M = G - D;
+       for (let j = 0; j < W.length; j++) {
+         let P = W[j],
+           V = Z - P.mainSize,
+           N = _ ? (O === "start" ? "end" : O === "end" ? "start" : O) : O,
+           T = 0;
+         switch (N) {
+           case "start":
+             T = 0;
+             break;
+           case "center":
+             T = Math.round(V / 2);
+             break;
+           case "end":
+             T = V;
+             break;
+           case "space-between":
+           case "space-around":
+           case "space-evenly":
+             break;
+         }
+         let k = _ ? [...P.children].reverse() : P.children,
+           R = T;
+         for (let b = 0; b < k.length; b++) {
+           let S = k[b],
+             B = S.getMargin(),
+             x = w ? S.layout.width : S.layout.height,
+             F = w ? S.layout.height : S.layout.width,
+             Q = w ? B.left : B.top,
+             u = w ? B.right : B.bottom,
+             d = w ? B.top : B.left,
+             a = w ? B.bottom : B.right,
+             l = Math.max(0, V),
+             e = k.length;
+           if (N === "space-between" && e > 1) {
+             R = Math.round((l * b) / (e - 1));
+             for (let DA = 0; DA < b; DA++) {
+               let o = k[DA],
+                 _A = o.getMargin(),
+                 PA = w ? _A.left + _A.right : _A.top + _A.bottom;
+               ((R += w ? o.layout.width : o.layout.height), (R += PA + X));
+             }
+           } else if (N === "space-around") {
+             let DA = e * 2,
+               o = b * 2 + 1;
+             R = Math.round((l * o) / DA);
+             for (let _A = 0; _A < b; _A++) {
+               let PA = k[_A],
+                 jA = PA.getMargin(),
+                 yA = w ? jA.left + jA.right : jA.top + jA.bottom;
+               ((R += w ? PA.layout.width : PA.layout.height), (R += yA + X));
+             }
+           } else if (N === "space-evenly") {
+             let DA = e + 1;
+             R = Math.round((l * (b + 1)) / DA);
+             for (let o = 0; o < b; o++) {
+               let _A = k[o],
+                 PA = _A.getMargin(),
+                 jA = w ? PA.left + PA.right : PA.top + PA.bottom;
+               ((R += w ? _A.layout.width : _A.layout.height), (R += jA + X));
+             }
+           }
+           let JA =
+               S.style.alignSelf && S.style.alignSelf !== "auto"
+                 ? S.style.alignSelf
+                 : J,
+             OA = d + F + a,
+             HA = d;
+           switch (JA) {
+             case "start":
+               HA = d;
+               break;
+             case "center":
+               HA = Math.round((P.crossSize - OA) / 2) + d;
+               break;
+             case "end":
+               HA = P.crossSize - F - a;
+               break;
+             case "stretch": {
+               if (
+                 ((HA = d),
+                 !(w
+                   ? S.style.height?.type === "fixed"
+                   : S.style.width?.type === "fixed"))
+               )
+                 _x.stretchChild(S, w, P.crossSize - d - a);
+               break;
+             }
+           }
+           if (w)
+             ((S.layout.x = K.x + q.left + R + Q),
+               (S.layout.y = K.y + q.top + M + HA));
+           else
+             ((S.layout.x = K.x + q.left + M + HA),
+               (S.layout.y = K.y + q.top + R + Q));
+           if (
+             (S.positionChildren(),
+             N === "start" || N === "center" || N === "end")
+           )
+             R += x + Q + u + X;
+         }
+         M += P.crossSize + $;
+       }
+     }
+     calculateFlexLines(A, K, q, Y) {
+       if (
+         !((this.style.flexWrap ?? "nowrap") !== "nowrap" && K !== void 0) ||
+         A.length === 0
+       ) {
+         let $ = 0,
+           _ = 0;
+         for (let Z = 0; Z < A.length; Z++) {
+           let G = A[Z],
+             W = G.getMargin(),
+             D = q ? W.left + W.right : W.top + W.bottom,
+             M = q ? W.top + W.bottom : W.left + W.right,
+             j = (q ? G.layout.width : G.layout.height) + D,
+             P = (q ? G.layout.height : G.layout.width) + M;
+           (($ += j + (Z > 0 ? Y : 0)), (_ = Math.max(_, P)));
+         }
+         return [{ children: A, mainSize: $, crossSize: _ }];
+       }
+       let H = [],
+         J = [],
+         O = 0,
+         X = 0;
+       for (let $ of A) {
+         let _ = $.getMargin(),
+           Z = q ? _.left + _.right : _.top + _.bottom,
+           G = q ? _.top + _.bottom : _.left + _.right,
+           W = (q ? $.layout.width : $.layout.height) + Z,
+           D = (q ? $.layout.height : $.layout.width) + G,
+           M = J.length > 0 ? Y : 0;
+         if (J.length > 0 && O + M + W > K)
+           (H.push({ children: J, mainSize: O, crossSize: X }),
+             (J = [$]),
+             (O = W),
+             (X = D));
+         else (J.push($), (O += M + W), (X = Math.max(X, D)));
+       }
+       if (J.length > 0) H.push({ children: J, mainSize: O, crossSize: X });
+       return H;
+     }
+   };
+ });

+++ Added MJ4 (pretty-v2.1.20.js:174326-174527)
+ class MJ4 {
+   node;
+   mutableStyle = {};
+   measureFunc = null;
+   parentAdapter = null;
+   childAdapters = [];
+   constructor() {
+     this.node = new _x({});
+   }
+   insertChild(A, K) {
+     let q = A;
+     ((q.parentAdapter = this),
+       this.childAdapters.splice(K, 0, q),
+       this.node.insertChild(q.node, K));
+   }
+   removeChild(A) {
+     let K = A;
+     K.parentAdapter = null;
+     let q = this.childAdapters.indexOf(K);
+     if (q !== -1) this.childAdapters.splice(q, 1);
+     this.node.removeChild(K.node);
+   }
+   getChildCount() {
+     return this.childAdapters.length;
+   }
+   getParent() {
+     return this.parentAdapter;
+   }
+   calculateLayout(A, K) {
+     (this.syncStyleTree(), this.node.calculateLayout(A, void 0));
+   }
+   setMeasureFunc(A) {
+     this.measureFunc = A;
+   }
+   unsetMeasureFunc() {
+     this.measureFunc = null;
+   }
+   markDirty() {
+     this.node.markDirty();
+   }
+   getComputedLeft() {
+     let A = this.parentAdapter?.node.layout.x ?? 0;
+     return this.node.layout.x - A;
+   }
+   getComputedTop() {
+     let A = this.parentAdapter?.node.layout.y ?? 0;
+     return this.node.layout.y - A;
+   }
+   getComputedWidth() {
+     return this.node.layout.width;
+   }
+   getComputedHeight() {
+     return this.node.layout.height;
+   }
+   getComputedBorder(A) {
+     let K = this.mutableStyle.border;
+     if (!K) return 0;
+     switch (A) {
+       case D3.Left:
+         return K.left;
+       case D3.Right:
+         return K.right;
+       case D3.Top:
+         return K.top;
+       case D3.Bottom:
+         return K.bottom;
+       default:
+         return 0;
+     }
+   }
+   getComputedPadding(A) {
+     let K = this.mutableStyle.padding;
+     if (!K) return 0;
+     switch (A) {
+       case D3.Left:
+         return K.left;
+       case D3.Right:
+         return K.right;
+       case D3.Top:
+         return K.top;
+       case D3.Bottom:
+         return K.bottom;
+       default:
+         return 0;
+     }
+   }
+   setWidth(A) {
+     this.mutableStyle.width = H76(A);
+   }
+   setWidthPercent(A) {
+     this.mutableStyle.width = J76(A);
+   }
+   setWidthAuto() {
+     this.mutableStyle.width = void 0;
+   }
+   setHeight(A) {
+     this.mutableStyle.height = H76(A);
+   }
+   setHeightPercent(A) {
+     this.mutableStyle.height = J76(A);
+   }
+   setHeightAuto() {
+     this.mutableStyle.height = void 0;
+   }
+   setMinWidth(A) {
+     this.mutableStyle.minWidth = A;
+   }
+   setMinWidthPercent(A) {}
+   setMinHeight(A) {
+     this.mutableStyle.minHeight = A;
+   }
+   setMinHeightPercent(A) {}
+   setMaxWidth(A) {
+     this.mutableStyle.maxWidth = A;
+   }
+   setMaxWidthPercent(A) {}
+   setMaxHeight(A) {
+     this.mutableStyle.maxHeight = A;
+   }
+   setMaxHeightPercent(A) {}
+   setFlexDirection(A) {
+     this.mutableStyle.flexDirection = A;
+   }
+   setFlexGrow(A) {
+     this.mutableStyle.flexGrow = A;
+   }
+   setFlexShrink(A) {
+     this.mutableStyle.flexShrink = A;
+   }
+   setFlexBasis(A) {
+     this.mutableStyle.flexBasis = A;
+   }
+   setFlexBasisPercent(A) {}
+   setFlexWrap(A) {
+     this.mutableStyle.flexWrap = A;
+   }
+   setAlignItems(A) {
+     this.mutableStyle.alignItems = DJ4[A];
+   }
+   setAlignSelf(A) {
+     this.mutableStyle.alignSelf = DJ4[A];
+   }
+   setJustifyContent(A) {
+     this.mutableStyle.justifyContent = To3[A];
+   }
+   setDisplay(A) {
+     this.mutableStyle.display = A;
+   }
+   getDisplay() {
+     return this.mutableStyle.display === "none" ? hV.None : hV.Flex;
+   }
+   setPositionType(A) {
+     this.mutableStyle.position = A;
+   }
+   setMargin(A, K) {
+     this.mutableStyle.margin = O76(this.mutableStyle.margin, A, K);
+   }
+   setPadding(A, K) {
+     this.mutableStyle.padding = O76(this.mutableStyle.padding, A, K);
+   }
+   setBorder(A, K) {
+     this.mutableStyle.border = O76(this.mutableStyle.border, A, K);
+   }
+   setGap(A, K) {
+     switch (A) {
+       case "all":
+         this.mutableStyle.gap = K;
+         break;
+       case "column":
+         this.mutableStyle.columnGap = K;
+         break;
+       case "row":
+         this.mutableStyle.rowGap = K;
+         break;
+     }
+   }
+   free() {}
+   freeRecursive() {}
+   syncStyleTree() {
+     this.syncStyle();
+     for (let A of this.childAdapters) A.syncStyleTree();
+   }
+   syncStyle() {
+     let A = this.measureFunc,
+       K = A
+         ? (Y) => {
+             if (Y === void 0) return A(1 / 0, HQ.Undefined);
+             return A(Y, HQ.AtMost);
+           }
+         : void 0,
+       q = new _x(this.mutableStyle, K);
+     q.layout = this.node.layout;
+     for (let Y of this.childAdapters) q.appendChild(Y.node);
+     if (this.parentAdapter) {
+       let Y = this.parentAdapter.node.children.indexOf(this.node);
+       if (Y !== -1)
+         (this.parentAdapter.node.removeChild(this.node),
+           this.parentAdapter.node.insertChild(q, Y));
+     }
+     this.node = q;
+   }
+ }

+++ Added O76 (pretty-v2.1.20.js:174528-174552)
+ function O76(A, K, q) {
+   let Y = A ?? { top: 0, right: 0, bottom: 0, left: 0 };
+   switch (K) {
+     case "all":
+       return { top: q, right: q, bottom: q, left: q };
+     case "horizontal":
+       return { ...Y, left: q, right: q };
+     case "vertical":
+       return { ...Y, top: q, bottom: q };
+     case "left":
+       return { ...Y, left: q };
+     case "right":
+       return { ...Y, right: q };
+     case "top":
+       return { ...Y, top: q };
+     case "bottom":
+       return { ...Y, bottom: q };
+     case "start":
+       return { ...Y, left: q };
+     case "end":
+       return { ...Y, right: q };
+     default:
+       return Y;
+   }
+ }

+++ Added PJ4 (pretty-v2.1.20.js:174557-174575)
+ var PJ4 = C(() => {
+   WJ4();
+   Bn();
+   ((DJ4 = {
+     "flex-start": "start",
+     "flex-end": "end",
+     center: "center",
+     stretch: "stretch",
+     auto: "auto",
+   }),
+     (To3 = {
+       "flex-start": "start",
+       "flex-end": "end",
+       center: "center",
+       "space-between": "space-between",
+       "space-around": "space-around",
+       "space-evenly": "space-evenly",
+     }));
+ });

+++ Added VJ4 (pretty-v2.1.20.js:174576-174578)
+ function VJ4() {
+   return (h("Layout engine: yoga"), "yoga");
+ }

+++ Added fJ4 (pretty-v2.1.20.js:174579-174581)
+ async function fJ4() {
+   if (VJ4() === "yoga") await _J4();
+ }

+++ Added NJ4 (pretty-v2.1.20.js:174582-174585)
+ function NJ4() {
+   if (VJ4() === "bento") return jJ4();
+   return ZJ4();
+ }

+++ Added xo3 (pretty-v2.1.20.js:174846-174855)
+   xo3 = (A, K = {}, q) => {
+     (Co3(A, K),
+       Lo3(A, K),
+       Ro3(A, K),
+       yo3(A, K),
+       Io3(A, K),
+       So3(A, K),
+       ho3(A, K, q),
+       bo3(A, K));
+   },

+++ Added EJ4 (pretty-v2.1.20.js:174857-174860)
+ var EJ4 = C(() => {
+   Bn();
+   W76 = xo3;
+ });

+++ Added IJ4 (pretty-v2.1.20.js:175113-175116)
+ var IJ4 = C(() => {
+   Bn();
+   yJ4 = uo3;
+ });

+++ Added I04 (pretty-v2.1.20.js:177265-177267)
+ var I04 = C(() => {
+   y04 = Ta3;
+ });

+++ Added h04 (pretty-v2.1.20.js:177286-177289)
+ var h04 = C(() => {
+   I04();
+   S04 = Ea3;
+ });

+++ Added V$4 (pretty-v2.1.20.js:182457-182464)
+ var V$4 = C(() => {
+   P$4();
+   X76();
+   sRA();
+   i6();
+   D1();
+   W9 = TA9;
+ });

+++ Added A_4 (pretty-v2.1.20.js:183767-183769)
+ var A_4 = C(() => {
+   hK6 = _19;
+ });

+++ Added B56 (pretty-v2.1.20.js:192728-192736)
+ function B56(A) {
+   if (!A.startsWith("mcp__")) return;
+   let K = A.split("__");
+   if (K.length < 3) return;
+   let q = K[1],
+     Y = K.slice(2).join("__");
+   if (!q || !Y) return;
+   return { serverName: q, mcpToolName: Y };
+ }

+++ Added m56 (pretty-v2.1.20.js:192737-192747)
+ function m56(A, K) {
+   if (A !== "Skill") return;
+   if (
+     typeof K === "object" &&
+     K !== null &&
+     "skill" in K &&
+     typeof K.skill === "string"
+   )
+     return K.skill;
+   return;
+ }

+++ Added g$9 (pretty-v2.1.20.js:193934-193943)
+ function g$9(A) {
+   if (!H8.isAxiosError(A)) return A instanceof Error ? A.message : String(A);
+   let K = [],
+     q = A.response?.headers?.["request-id"];
+   if (q) K.push(`request-id=${q}`);
+   if (A.response?.status) K.push(`status=${A.response.status}`);
+   if (A.code) K.push(`code=${A.code}`);
+   if (A.message) K.push(A.message);
+   return K.join(", ");
+ }

+++ Added lI4 (pretty-v2.1.20.js:202674-202689)
+ function lI4(A) {
+   if (!A) return [];
+   let K = kD(),
+     q = `@${A}`,
+     Y = new Set(),
+     z = !1;
+   for (let w of Object.keys(K.plugins)) {
+     if (!w.endsWith(q)) continue;
+     for (let H of K.plugins[w] ?? []) if (H.installPath) Y.add(H.installPath);
+     (delete K.plugins[w],
+       (z = !0),
+       h(`Removed installed plugin for marketplace removal: ${w}`));
+   }
+   if (z) y91(K);
+   return Array.from(Y);
+ }

+++ Added ZSA (pretty-v2.1.20.js:221537-221540)
+ var ZSA = C(() => {
+   Ez6();
+   Cz6 = kz6;
+ });

+++ Added S21 (pretty-v2.1.20.js:221883-221886)
+ var S21 = C(() => {
+   I21();
+   bz6 = hz6;
+ });

+++ Added tH6 (pretty-v2.1.20.js:243991-243994)
+ var tH6 = C(() => {
+   Va4();
+   sH6 = aH6;
+ });

+++ Added jt4 (pretty-v2.1.20.js:246533-246537)
+ var jt4 = C(() => {
+   cy();
+   Dt4();
+   K06 = cz1;
+ });

+++ Added ez1 (pretty-v2.1.20.js:246730-246733)
+ var ez1 = C(() => {
+   t$A();
+   Y_A = cV;
+ });

+++ Added HJ1 (pretty-v2.1.20.js:265095-265136)
+ function HJ1(A) {
+   let K = A.filter(eV);
+   if (K.length === 0) {
+     if (No !== void 0 && No !== "")
+       n("tengu_tool_prompt_changed", {
+         tool: "ToolSearchTool",
+         previousDeferredCount: No.split(`
+ `).length,
+         newDeferredCount: 0,
+       });
+     return ((No = ""), nK7);
+   }
+   let q = i4("tengu_kv7_prompt_sort", !1)
+     ? K.map((Y) => Y.name).sort().join(`
+ `)
+     : K.map((Y) => Y.name).join(`
+ `);
+   if (No !== void 0 && q !== No) {
+     let Y = No.split(
+         `
+ `,
+       ).filter(Boolean).length,
+       z = q
+         .split(
+           `
+ `,
+         )
+         .filter(Boolean).length;
+     n("tengu_tool_prompt_changed", {
+       tool: "ToolSearchTool",
+       previousDeferredCount: Y,
+       newDeferredCount: z,
+     });
+   }
+   return (
+     (No = q),
+     `${nK7}
+ 
+ Available deferred tools (must be loaded before use):
+ ${q}`
+   );
+ }

+++ Added o$6 (pretty-v2.1.20.js:266621-266729)
+ function o$6(A) {
+   let K = `Your task is to create a detailed summary of the conversation so far, paying close attention to the user's explicit requests and your previous actions.
+ This summary should be thorough in capturing technical details, code patterns, and architectural decisions that would be essential for continuing development work without losing context.
+ 
+ Before providing your final summary, wrap your analysis in <analysis> tags to organize your thoughts and ensure you've covered all necessary points. In your analysis process:
+ 
+ 1. Chronologically analyze each message and section of the conversation. For each section thoroughly identify:
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
+ 1. Primary Request and Intent: Capture all of the user's explicit requests and intents in detail
+ 2. Key Technical Concepts: List all important technical concepts, technologies, and frameworks discussed.
+ 3. Files and Code Sections: Enumerate specific files and code sections examined, modified, or created. Pay special attention to the most recent messages and include full code snippets where applicable and include a summary of why this file read or edit is important.
+ 4. Errors and fixes: List all errors that you ran into, and how you fixed them. Pay special attention to specific user feedback that you received, especially if the user told you to do something differently.
+ 5. Problem Solving: Document problems solved and any ongoing troubleshooting efforts.
+ 6. All user messages: List ALL user messages that are not tool results. These are critical for understanding the users' feedback and changing intent.
+ 6. Pending Tasks: Outline any pending tasks that you have explicitly been asked to work on.
+ 7. Current Work: Describe in detail precisely what was being worked on immediately before this summary request, paying special attention to the most recent messages from both user and assistant. Include file names and code snippets where applicable.
+ 8. Optional Next Step: List the next step that you will take that is related to the most recent work you were doing. IMPORTANT: ensure that this step is DIRECTLY in line with the user's most recent explicit requests, and the task you were working on immediately before this summary request. If your last task was concluded, then only list next steps if they are explicitly in line with the users request. Do not start on tangential requests or really old requests that were already completed without confirming with the user first.
+                        If there is a next step, include direct quotes from the most recent conversation showing exactly what task you were working on and where you left off. This should be verbatim to ensure there's no drift in task interpretation.
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
+    - [...]
+ 
+ 3. Files and Code Sections:
+    - [File Name 1]
+       - [Summary of why this file is important]
+       - [Summary of the changes made to this file, if any]
+       - [Important Code Snippet]
+    - [File Name 2]
+       - [Important Code Snippet]
+    - [...]
+ 
+ 4. Errors and fixes:
+     - [Detailed description of error 1]:
+       - [How you fixed the error]
+       - [User feedback on the error if any]
+     - [...]
+ 
+ 5. Problem Solving:
+    [Description of solved problems and ongoing troubleshooting]
+ 
+ 6. All user messages: 
+     - [Detailed non tool use user message]
+     - [...]
+ 
+ 7. Pending Tasks:
+    - [Task 1]
+    - [Task 2]
+    - [...]
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
+ Please provide your summary based on the conversation so far, following this structure and ensuring precision and thoroughness in your response. 
+ 
+ There may be additional summarization instructions provided in the included context. If so, remember to follow these instructions when creating the above summary. Examples of instructions include:
+ <example>
+ ## Compact Instructions
+ When summarizing the conversation focus on typescript code changes and also remember the mistakes you made and how you fixed them.
+ </example>
+ 
+ <example>
+ # Summary instructions
+ When you are using compact - please focus on test output and code changes. Include file reads verbatim.
+ </example>
+ `;
+   if (A && A.trim() !== "")
+     K += `
+ 
+ Additional Instructions:
+ ${A}`;
+   return (
+     (K += `
+ 
+ IMPORTANT: Do NOT use any tools. You MUST respond with ONLY the <summary>...</summary> block as your text output.`),
+     K
+   );
+ }

+++ Added Cq7 (pretty-v2.1.20.js:266881-266893)
+ function Cq7(A) {
+   return IU.createElement(
+     f,
+     { dimColor: !0 },
+     "Loaded ",
+     IU.createElement(f, { bold: !0 }, A),
+     " ",
+     A === 1 ? "tool" : "tools",
+     " ·",
+     " ",
+     "/context",
+   );
+ }

+++ Added Bw7 (pretty-v2.1.20.js:282085-282098)
+ function Bw7() {
+   let A = [],
+     K = zuA();
+   try {
+     let w = lGY(K);
+     for (let H of w) if (H.endsWith(".sock")) A.push(EC(K, H));
+   } catch {}
+   let q = `claude-mcp-browser-bridge-${aG6()}`,
+     Y = EC(dGY(), q),
+     z = `/tmp/${q}`;
+   if (!A.includes(Y)) A.push(Y);
+   if (Y !== z && !A.includes(z)) A.push(z);
+   return A;
+ }

+++ Added rGY (pretty-v2.1.20.js:282099-282101)
+ function rGY() {
+   return `claude-mcp-browser-bridge-${aG6()}`;
+ }

+++ Added Aj6 (pretty-v2.1.20.js:309864-309867)
+ function Aj6() {
+   CW7++;
+   for (let A of E$1) A();
+ }

+++ Added IW7 (pretty-v2.1.20.js:309871-309873)
+ function IW7() {
+   if (C$1.length > 0) Aj6();
+ }

+++ Added SW7 (pretty-v2.1.20.js:309874-309878)
+ function SW7() {
+   let A = C$1.shift();
+   if (A !== void 0) Aj6();
+   return A;
+ }

+++ Added FW7 (pretty-v2.1.20.js:310185-310213)
+ function FW7(A, K) {
+   let q = [],
+     Y = uW7(),
+     z = [];
+   function w() {
+     if (Y.messages.length === 0) return;
+     q.push(CCY(Y));
+     for (let H of z) q.push(H);
+     ((z = []), (Y = uW7()));
+   }
+   for (let H of A)
+     if (vCY(H, K)) {
+       if (VCY(H, K).isSearch) Y.searchCount += xW7(H);
+       else {
+         let O = kCY(H);
+         for (let X of O) Y.readFilePaths.add(X);
+         if (O.length === 0) Y.readOperationCount += xW7(H);
+       }
+       for (let O of BW7(H)) Y.toolUseIds.add(O);
+       Y.messages.push(H);
+     } else if (ECY(H, Y.toolUseIds)) Y.messages.push(H);
+     else if (TCY(H))
+       if (Y.messages.length > 0) z.push(H);
+       else q.push(H);
+     else if (fCY(H)) (w(), q.push(H));
+     else if (NCY(H, K)) (w(), q.push(H));
+     else (w(), q.push(H));
+   return (w(), q);
+ }

+++ Added vGA (pretty-v2.1.20.js:310237-310249)
+ function vGA(A) {
+   if (A.length === 0) return;
+   let K = 0,
+     q = 0;
+   for (let z = A.length - 1; z >= 0; z--) {
+     let w = A[z];
+     if (w.isSearch) K++;
+     else if (w.isRead) q++;
+     else break;
+   }
+   if (K + q >= 2) return Yj6(K, q, !0);
+   return A[A.length - 1]?.activityDescription;
+ }

+++ Added NBA (pretty-v2.1.20.js:310399-310403)
+ function NBA(A) {
+   return (K, q) => {
+     return GQ(A, K)?.getActivityDescription?.(q) ?? void 0;
+   };
+ }

+++ Added pCY (pretty-v2.1.20.js:312141-312143)
+ function pCY() {
+   return i$1.size > 0;
+ }

+++ Added n$1 (pretty-v2.1.20.js:312553-312560)
+ function n$1(A) {
+   if (typeof A === "string") return A;
+   if (typeof A === "number") return String(A);
+   if (!A) return "";
+   if (Array.isArray(A)) return A.map(n$1).join("");
+   if (g7.default.isValidElement(A)) return n$1(A.props.children);
+   return "";
+ }

+++ Added DbY (pretty-v2.1.20.js:318858-318862)
+ function DbY() {
+   if (i4("tengu_marble_kite", !1)) return "";
+   return `
+ - You must use your \`${K5}\` tool at least once in the conversation before editing. This tool will error if you attempt an edit without reading the file. `;
+ }

+++ Added JV7 (pretty-v2.1.20.js:318863-318872)
+ function JV7() {
+   return `Performs exact string replacements in files.
+ 
+ Usage:${DbY()}
+ - When editing text from Read tool output, ensure you preserve the exact indentation (tabs/spaces) as it appears AFTER the line number prefix. The line number prefix format is: spaces + line number + tab. Everything after that tab is the actual file content to match. Never include any part of the line number prefix in the old_string or new_string.
+ - ALWAYS prefer editing existing files in the codebase. NEVER write new files unless explicitly required.
+ - Only use emojis if the user explicitly requests it. Avoid adding emojis to files unless asked.
+ - The edit will FAIL if \`old_string\` is not unique in the file. Either provide a larger string with more surrounding context to make it unique or use \`replace_all\` to change every instance of \`old_string\`.
+ - Use \`replace_all\` for replacing and renaming strings across the file. This parameter is useful if you want to rename a variable for instance.`;
+ }

+++ Added PM1 (pretty-v2.1.20.js:388229-388234)
+ function PM1(A, K) {
+   let q = parseInt(A.id, 10),
+     Y = parseInt(K.id, 10);
+   if (!isNaN(q) && !isNaN(Y)) return q - Y;
+   return A.id.localeCompare(K.id);
+ }

+++ Added Ea7 (pretty-v2.1.20.js:388917-388949)
+ function Ea7(A) {
+   let K = s(7),
+     { text: q } = A,
+     Y;
+   if (K[0] === Symbol.for("react.memo_cache_sentinel"))
+     ((Y = Date.now()), (K[0] = Y));
+   else Y = K[0];
+   let z = TM1.useRef(Y),
+     [w, H] = TM1.useState(0),
+     J;
+   if (K[1] === Symbol.for("react.memo_cache_sentinel"))
+     ((J = () => {
+       let _ = Date.now() - z.current;
+       if (_ < va7) return;
+       let Z = (_ - va7) / 1000;
+       H((Math.sin((Z * Math.PI * 2) / hO2) + 1) / 2);
+     }),
+       (K[1] = J));
+   else J = K[1];
+   wY(J, 50);
+   let O;
+   if (K[2] !== w) ((O = os(np(IO2, SO2, w))), (K[2] = w), (K[3] = O));
+   else O = K[3];
+   let X = O,
+     $;
+   if (K[4] !== X || K[5] !== q)
+     (($ = ML6.createElement(f, { color: X }, q)),
+       (K[4] = X),
+       (K[5] = q),
+       (K[6] = $));
+   else $ = K[6];
+   return $;
+ }

+++ Added ka7 (pretty-v2.1.20.js:388956-388964)
+ var ka7 = C(() => {
+   cA();
+   BA();
+   a0();
+   ((ML6 = r(XA(), 1)),
+     (TM1 = r(XA(), 1)),
+     (IO2 = { r: 153, g: 153, b: 153 }),
+     (SO2 = { r: 185, g: 185, b: 185 }));
+ });

+++ Added QO2 (pretty-v2.1.20.js:389489-389495)
+ function QO2(A) {
+   if (!A) return;
+   let K = A.filter((Y) => Y.status === "pending");
+   if (K.length === 0) return;
+   let q = new Set(A.filter((Y) => Y.status !== "completed").map((Y) => Y.id));
+   return K.find((Y) => !Y.blockedBy.some((z) => q.has(z))) ?? K[0];
+ }

+++ Added a6K (pretty-v2.1.20.js:409275-409881)
+ function a6K(A) {
+   let K = s(127),
+     { attachment: q, addMargin: Y, verbose: z } = A;
+   if (j8() && q.type === "teammate_mailbox") return null;
+   switch (q.type) {
+     case "directory": {
+       let w;
+       if (K[0] !== q.path)
+         ((w = w3A(u1(), q.path)), (K[0] = q.path), (K[1] = w));
+       else w = K[1];
+       let H = w + _G2,
+         J;
+       if (K[2] !== H)
+         ((J = O5.default.createElement(
+           ZO,
+           null,
+           "Listed directory",
+           " ",
+           O5.default.createElement(f, { bold: !0 }, H),
+         )),
+           (K[2] = H),
+           (K[3] = J));
+       else J = K[3];
+       return J;
+     }
+     case "file":
+     case "already_read_file": {
+       if (q.content.type === "notebook") {
+         let X;
+         if (K[4] !== q.filename)
+           ((X = w3A(u1(), q.filename)), (K[4] = q.filename), (K[5] = X));
+         else X = K[5];
+         let $;
+         if (K[6] !== X)
+           (($ = O5.default.createElement(f, { bold: !0 }, X)),
+             (K[6] = X),
+             (K[7] = $));
+         else $ = K[7];
+         let _;
+         if (K[8] !== q.content.file.cells.length || K[9] !== $)
+           ((_ = O5.default.createElement(
+             ZO,
+             null,
+             "Read ",
+             $,
+             " (",
+             q.content.file.cells.length,
+             " cells)",
+           )),
+             (K[8] = q.content.file.cells.length),
+             (K[9] = $),
+             (K[10] = _));
+         else _ = K[10];
+         return _;
+       }
+       let w;
+       if (K[11] !== q.filename)
+         ((w = w3A(u1(), q.filename)), (K[11] = q.filename), (K[12] = w));
+       else w = K[12];
+       let H;
+       if (K[13] !== w)
+         ((H = O5.default.createElement(f, { bold: !0 }, w)),
+           (K[13] = w),
+           (K[14] = H));
+       else H = K[14];
+       let J;
+       if (
+         K[15] !== q.content.file.numLines ||
+         K[16] !== q.content.file.originalSize ||
+         K[17] !== q.content.type ||
+         K[18] !== q.truncated
+       )
+         ((J =
+           q.content.type === "text"
+             ? `${q.content.file.numLines}${q.truncated ? "+" : ""} lines`
+             : BO(q.content.file.originalSize)),
+           (K[15] = q.content.file.numLines),
+           (K[16] = q.content.file.originalSize),
+           (K[17] = q.content.type),
+           (K[18] = q.truncated),
+           (K[19] = J));
+       else J = K[19];
+       let O;
+       if (K[20] !== H || K[21] !== J)
+         ((O = O5.default.createElement(ZO, null, "Read ", H, " (", J, ")")),
+           (K[20] = H),
+           (K[21] = J),
+           (K[22] = O));
+       else O = K[22];
+       return O;
+     }
+     case "compact_file_reference": {
+       let w;
+       if (K[23] !== q.filename)
+         ((w = w3A(u1(), q.filename)), (K[23] = q.filename), (K[24] = w));
+       else w = K[24];
+       let H;
+       if (K[25] !== w)
+         ((H = O5.default.createElement(
+           ZO,
+           null,
+           "Referenced file",
+           " ",
+           O5.default.createElement(f, { bold: !0 }, w),
+         )),
+           (K[25] = w),
+           (K[26] = H));
+       else H = K[26];
+       return H;
+     }
+     case "selected_lines_in_ide": {
+       let w = q.lineEnd - q.lineStart + 1,
+         H;
+       if (K[27] !== w)
+         ((H = O5.default.createElement(f, { bold: !0 }, w)),
+           (K[27] = w),
+           (K[28] = H));
+       else H = K[28];
+       let J;
+       if (K[29] !== q.filename)
+         ((J = w3A(u1(), q.filename)), (K[29] = q.filename), (K[30] = J));
+       else J = K[30];
+       let O;
+       if (K[31] !== J)
+         ((O = O5.default.createElement(f, { bold: !0 }, J)),
+           (K[31] = J),
+           (K[32] = O));
+       else O = K[32];
+       let X;
+       if (K[33] !== q.ideName || K[34] !== H || K[35] !== O)
+         ((X = O5.default.createElement(
+           ZO,
+           null,
+           "⧉ Selected",
+           " ",
+           H,
+           " ",
+           "lines from ",
+           O,
+           " ",
+           "in ",
+           q.ideName,
+         )),
+           (K[33] = q.ideName),
+           (K[34] = H),
+           (K[35] = O),
+           (K[36] = X));
+       else X = K[36];
+       return X;
+     }
+     case "nested_memory": {
+       let w;
+       if (K[37] !== q.path)
+         ((w = w3A(u1(), q.path)), (K[37] = q.path), (K[38] = w));
+       else w = K[38];
+       let H;
+       if (K[39] !== w)
+         ((H = O5.default.createElement(
+           ZO,
+           null,
+           "Loaded ",
+           O5.default.createElement(f, { bold: !0 }, w),
+         )),
+           (K[39] = w),
+           (K[40] = H));
+       else H = K[40];
+       return H;
+     }
+     case "dynamic_skill": {
+       let w;
+       if (K[41] !== q.skillDir)
+         ((w = w3A(u1(), q.skillDir)), (K[41] = q.skillDir), (K[42] = w));
+       else w = K[42];
+       let H = w,
+         J = q.skillNames.length,
+         O = J !== 1 ? "s" : "",
+         X;
+       if (K[43] !== J || K[44] !== O)
+         ((X = O5.default.createElement(f, { bold: !0 }, J, " skill", O)),
+           (K[43] = J),
+           (K[44] = O),
+           (K[45] = X));
+       else X = K[45];
+       let $;
+       if (K[46] !== H)
+         (($ = O5.default.createElement(f, { bold: !0 }, H)),
+           (K[46] = H),
+           (K[47] = $));
+       else $ = K[47];
+       let _;
+       if (K[48] !== X || K[49] !== $)
+         ((_ = O5.default.createElement(
+           ZO,
+           null,
+           "Loaded",
+           " ",
+           X,
+           " ",
+           "from ",
+           $,
+         )),
+           (K[48] = X),
+           (K[49] = $),
+           (K[50] = _));
+       else _ = K[50];
+       return _;
+     }
+     case "queued_command": {
+       let w;
+       if (K[51] !== q.prompt)
+         ((w = typeof q.prompt === "string" ? q.prompt : H3A(q.prompt) || ""),
+           (K[51] = q.prompt),
+           (K[52] = w));
+       else w = K[52];
+       let H = w,
+         J = q.imagePasteIds && q.imagePasteIds.length > 0,
+         O;
+       if (K[53] !== H)
+         ((O = { text: H, type: "text" }), (K[53] = H), (K[54] = O));
+       else O = K[54];
+       let X;
+       if (K[55] !== Y || K[56] !== O || K[57] !== z)
+         ((X = O5.default.createElement(Y3A, {
+           addMargin: Y,
+           param: O,
+           verbose: z,
+         })),
+           (K[55] = Y),
+           (K[56] = O),
+           (K[57] = z),
+           (K[58] = X));
+       else X = K[58];
+       let $;
+       if (K[59] !== q.imagePasteIds || K[60] !== J)
+         (($ = J && q.imagePasteIds?.map(GG2)),
+           (K[59] = q.imagePasteIds),
+           (K[60] = J),
+           (K[61] = $));
+       else $ = K[61];
+       let _;
+       if (K[62] !== X || K[63] !== $)
+         ((_ = O5.default.createElement(I, { flexDirection: "column" }, X, $)),
+           (K[62] = X),
+           (K[63] = $),
+           (K[64] = _));
+       else _ = K[64];
+       return _;
+     }
+     case "todo": {
+       if (q.context === "post-compact") {
+         let w = q.itemCount === 1 ? "item" : "items",
+           H;
+         if (K[65] !== q.itemCount || K[66] !== w)
+           ((H = O5.default.createElement(
+             ZO,
+             null,
+             "Todo list read (",
+             q.itemCount,
+             " ",
+             w,
+             ")",
+           )),
+             (K[65] = q.itemCount),
+             (K[66] = w),
+             (K[67] = H));
+         else H = K[67];
+         return H;
+       }
+       return null;
+     }
+     case "plan_file_reference": {
+       let w;
+       if (K[68] !== q.planFilePath)
+         ((w = N5(q.planFilePath)), (K[68] = q.planFilePath), (K[69] = w));
+       else w = K[69];
+       let H;
+       if (K[70] !== w)
+         ((H = O5.default.createElement(
+           ZO,
+           null,
+           "Plan file referenced (",
+           w,
+           ")",
+         )),
+           (K[70] = w),
+           (K[71] = H));
+       else H = K[71];
+       return H;
+     }
+     case "invoked_skills": {
+       if (q.skills.length === 0) return null;
+       let w;
+       if (K[72] !== q.skills)
+         ((w = q.skills.map(ZG2).join(", ")), (K[72] = q.skills), (K[73] = w));
+       else w = K[73];
+       let H = w,
+         J;
+       if (K[74] !== H)
+         ((J = O5.default.createElement(ZO, null, "Skills restored (", H, ")")),
+           (K[74] = H),
+           (K[75] = J));
+       else J = K[75];
+       return J;
+     }
+     case "diagnostics": {
+       let w;
+       if (K[76] !== q || K[77] !== z)
+         ((w = O5.default.createElement(r6K, { attachment: q, verbose: z })),
+           (K[76] = q),
+           (K[77] = z),
+           (K[78] = w));
+       else w = K[78];
+       return w;
+     }
+     case "mcp_resource": {
+       let w;
+       if (K[79] !== q.name)
+         ((w = O5.default.createElement(f, { bold: !0 }, q.name)),
+           (K[79] = q.name),
+           (K[80] = w));
+       else w = K[80];
+       let H;
+       if (K[81] !== q.server || K[82] !== w)
+         ((H = O5.default.createElement(
+           ZO,
+           null,
+           "Read MCP resource ",
+           w,
+           " from",
+           " ",
+           q.server,
+         )),
+           (K[81] = q.server),
+           (K[82] = w),
+           (K[83] = H));
+       else H = K[83];
+       return H;
+     }
+     case "command_permissions":
+       return null;
+     case "async_hook_response": {
+       if (q.hookEvent === "SessionStart" && !z) return null;
+       let w = q.response,
+         H;
+       if (K[84] !== q.hookEvent)
+         ((H = O5.default.createElement(f, { bold: !0 }, q.hookEvent)),
+           (K[84] = q.hookEvent),
+           (K[85] = H));
+       else H = K[85];
+       let J;
+       if (K[86] !== w || K[87] !== z)
+         ((J =
+           z &&
+           O5.default.createElement(
+             O5.default.Fragment,
+             null,
+             ":",
+             `
+ `,
+             w.systemMessage
+               ? w.systemMessage
+               : w.hookSpecificOutput &&
+                   "additionalContext" in w.hookSpecificOutput &&
+                   w.hookSpecificOutput.additionalContext
+                 ? w.hookSpecificOutput.additionalContext
+                 : null,
+           )),
+           (K[86] = w),
+           (K[87] = z),
+           (K[88] = J));
+       else J = K[88];
+       let O;
+       if (K[89] !== H || K[90] !== J)
+         ((O = O5.default.createElement(
+           ZO,
+           null,
+           "Async hook ",
+           H,
+           " completed",
+           J,
+         )),
+           (K[89] = H),
+           (K[90] = J),
+           (K[91] = O));
+       else O = K[91];
+       return O;
+     }
+     case "hook_blocking_error": {
+       if (q.hookEvent === "Stop" || q.hookEvent === "SubagentStop") return null;
+       if (z) {
+         let H;
+         if (K[92] !== q.blockingError.blockingError || K[93] !== q.hookName)
+           ((H = O5.default.createElement(
+             ZO,
+             { color: "error" },
+             q.hookName,
+             " hook returned blocking error:",
+             " ",
+             q.blockingError.blockingError,
+           )),
+             (K[92] = q.blockingError.blockingError),
+             (K[93] = q.hookName),
+             (K[94] = H));
+         else H = K[94];
+         return H;
+       }
+       let w;
+       if (K[95] !== q.hookName)
+         ((w = O5.default.createElement(
+           ZO,
+           { color: "error" },
+           q.hookName,
+           " hook returned blocking error",
+         )),
+           (K[95] = q.hookName),
+           (K[96] = w));
+       else w = K[96];
+       return w;
+     }
+     case "hook_non_blocking_error": {
+       if (q.hookEvent === "Stop" || q.hookEvent === "SubagentStop") return null;
+       if (z) {
+         let H;
+         if (K[97] !== q.hookName || K[98] !== q.stderr)
+           ((H = O5.default.createElement(
+             ZO,
+             { color: "error" },
+             q.hookName,
+             " hook error: ",
+             q.stderr,
+           )),
+             (K[97] = q.hookName),
+             (K[98] = q.stderr),
+             (K[99] = H));
+         else H = K[99];
+         return H;
+       }
+       let w;
+       if (K[100] !== q.hookName)
+         ((w = O5.default.createElement(
+           ZO,
+           { color: "error" },
+           q.hookName,
+           " hook error",
+         )),
+           (K[100] = q.hookName),
+           (K[101] = w));
+       else w = K[101];
+       return w;
+     }
+     case "hook_error_during_execution": {
+       if (q.hookEvent === "Stop" || q.hookEvent === "SubagentStop") return null;
+       if (z) {
+         let H;
+         if (K[102] !== q.content || K[103] !== q.hookName)
+           ((H = O5.default.createElement(
+             ZO,
+             null,
+             q.hookName,
+             " hook warning: ",
+             q.content,
+           )),
+             (K[102] = q.content),
+             (K[103] = q.hookName),
+             (K[104] = H));
+         else H = K[104];
+         return H;
+       }
+       let w;
+       if (K[105] !== q.hookName)
+         ((w = O5.default.createElement(ZO, null, q.hookName, " hook warning")),
+           (K[105] = q.hookName),
+           (K[106] = w));
+       else w = K[106];
+       return w;
+     }
+     case "hook_success": {
+       if (q.hookEvent === "Stop" || q.hookEvent === "SubagentStop") return null;
+       if (z) {
+         let w = q.content ? `: ${q.content}` : "",
+           H;
+         if (K[107] !== q.hookName || K[108] !== w)
+           ((H = O5.default.createElement(
+             ZO,
+             null,
+             q.hookName,
+             " hook succeeded",
+             w,
+           )),
+             (K[107] = q.hookName),
+             (K[108] = w),
+             (K[109] = H));
+         else H = K[109];
+         return H;
+       }
+       return null;
+     }
+     case "hook_stopped_continuation": {
+       if (q.hookEvent === "Stop" || q.hookEvent === "SubagentStop") return null;
+       let w;
+       if (K[110] !== q.hookName || K[111] !== q.message)
+         ((w = O5.default.createElement(
+           ZO,
+           { color: "warning" },
+           q.hookName,
+           " hook stopped continuation: ",
+           q.message,
+         )),
+           (K[110] = q.hookName),
+           (K[111] = q.message),
+           (K[112] = w));
+       else w = K[112];
+       return w;
+     }
+     case "hook_system_message": {
+       let w;
+       if (K[113] !== q.content || K[114] !== q.hookName)
+         ((w = O5.default.createElement(
+           ZO,
+           null,
+           q.hookName,
+           " says: ",
+           q.content,
+         )),
+           (K[113] = q.content),
+           (K[114] = q.hookName),
+           (K[115] = w));
+       else w = K[115];
+       return w;
+     }
+     case "hook_permission_decision": {
+       let w = q.decision === "allow" ? "Allowed" : "Denied",
+         H;
+       if (K[116] !== q.hookEvent)
+         ((H = O5.default.createElement(f, { bold: !0 }, q.hookEvent)),
+           (K[116] = q.hookEvent),
+           (K[117] = H));
+       else H = K[117];
+       let J;
+       if (K[118] !== w || K[119] !== H)
+         ((J = O5.default.createElement(ZO, null, w, " by ", H, " hook")),
+           (K[118] = w),
+           (K[119] = H),
+           (K[120] = J));
+       else J = K[120];
+       return J;
+     }
+     case "task_status": {
+       if (j8() && q.taskType === "in_process_teammate") return null;
+       let w = q.status === "completed" ? "completed in background" : q.status,
+         H;
+       if (K[121] === Symbol.for("react.memo_cache_sentinel"))
+         ((H = O5.default.createElement(f, { dimColor: !0 }, uY, " ")),
+           (K[121] = H));
+       else H = K[121];
+       let J;
+       if (K[122] !== q.description)
+         ((J = O5.default.createElement(f, { bold: !0 }, q.description)),
+           (K[122] = q.description),
+           (K[123] = J));
+       else J = K[123];
+       let O;
+       if (K[124] !== w || K[125] !== J)
+         ((O = O5.default.createElement(
+           I,
+           { flexDirection: "row", width: "100%", marginTop: 1 },
+           H,
+           O5.default.createElement(
+             f,
+             { dimColor: !0 },
+             'Task "',
+             J,
+             '"',
+             " ",
+             w,
+           ),
+         )),
+           (K[124] = w),
+           (K[125] = J),
+           (K[126] = O));
+       else O = K[126];
+       return O;
+     }
+     case "task_progress":
+       return null;
+     case "agent_mention":
+     case "budget_usd":
+     case "critical_system_reminder":
+     case "delegate_mode":
+     case "delegate_mode_exit":
+     case "edited_image_file":
+     case "edited_text_file":
+     case "hook_additional_context":
+     case "hook_cancelled":
+     case "opened_file_in_ide":
+     case "output_style":
+     case "plan_mode":
+     case "plan_mode_exit":
+     case "plan_mode_reentry":
+     case "structured_output":
+     case "team_context":
+     case "todo_reminder":
+     case "ultramemory":
+     case "token_usage":
+       return null;
+   }
+ }

+++ Added GG2 (pretty-v2.1.20.js:409885-409887)
+ function GG2(A) {
+   return O5.default.createElement(vj1, { key: A, imageId: A });
+ }

+++ Added AW2 (pretty-v2.1.20.js:413972-413974)
+ function AW2(A) {
+   return "success" in A && "message" in A && !("lead_agent_id" in A);
+ }

+++ Added V4K (pretty-v2.1.20.js:415575-415577)
+ function V4K() {
+   Ny6 = null;
+ }

+++ Added $P1 (pretty-v2.1.20.js:419948-420017)
+ var $P1 = C(() => {
+   i5();
+   D1();
+   d7();
+   ((xy6 = K6(() => {
+     if (s6() !== "linux") return !1;
+     let K = process.execPath || process.argv[0] || "";
+     try {
+       let q = OP1("pacman", ["-Qo", K], {
+         encoding: "utf8",
+         timeout: 5000,
+         stdio: ["ignore", "pipe", "pipe"],
+       });
+       if (q.status === 0 && q.stdout)
+         return (h(`Detected pacman installation: ${q.stdout.trim()}`), !0);
+     } catch {}
+     return !1;
+   })),
+     (uy6 = K6(() => {
+       if (s6() !== "linux") return !1;
+       let K = process.execPath || process.argv[0] || "";
+       try {
+         let q = OP1("dpkg", ["-S", K], {
+           encoding: "utf8",
+           timeout: 5000,
+           stdio: ["ignore", "pipe", "pipe"],
+         });
+         if (q.status === 0 && q.stdout)
+           return (h(`Detected deb installation: ${q.stdout.trim()}`), !0);
+       } catch {}
+       return !1;
+     })),
+     (By6 = K6(() => {
+       if (s6() !== "linux") return !1;
+       let K = process.execPath || process.argv[0] || "";
+       try {
+         let q = OP1("rpm", ["-qf", K], {
+           encoding: "utf8",
+           timeout: 5000,
+           stdio: ["ignore", "pipe", "pipe"],
+         });
+         if (q.status === 0 && q.stdout)
+           return (h(`Detected rpm installation: ${q.stdout.trim()}`), !0);
+       } catch {}
+       return !1;
+     })),
+     (my6 = K6(() => {
+       if (s6() !== "linux") return !1;
+       let K = process.execPath || process.argv[0] || "";
+       try {
+         let q = OP1("apk", ["info", "--who-owns", K], {
+           encoding: "utf8",
+           timeout: 5000,
+           stdio: ["ignore", "pipe", "pipe"],
+         });
+         if (q.status === 0 && q.stdout)
+           return (h(`Detected apk installation: ${q.stdout.trim()}`), !0);
+       } catch {}
+       return !1;
+     })),
+     (BMA = K6(() => {
+       if (XP1()) return "homebrew";
+       if (by6()) return "winget";
+       if (xy6()) return "pacman";
+       if (my6()) return "apk";
+       if (uy6()) return "deb";
+       if (By6()) return "rpm";
+       return "unknown";
+     })));
+ });

+++ Added UB (pretty-v2.1.20.js:421718-421720)
+ function UB() {
+   return !1;
+ }

+++ Added N7K (pretty-v2.1.20.js:422002-422009)
+ function N7K(A, K, q, Y) {
+   if (!UB()) return;
+   let z = QMA(K);
+   if (z.length === 0) return;
+   let w = u1(),
+     H = UMA(A, w, z, "allow", q, Y);
+   KI6.set(A, H);
+ }

+++ Added PP1 (pretty-v2.1.20.js:422015-422021)
+ async function PP1(A, K, q) {
+   let { command: Y, cwd: z, descriptions: w } = A,
+     H = T7K(Y),
+     J = H ? await H : await UMA(Y, z, w, "allow", K, q);
+   MP1(Y, "allow", w, J);
+   return;
+ }

+++ Added PM2 (pretty-v2.1.20.js:422592-422599)
+ function PM2(A) {
+   let K = new Set(A.filter((q) => q.status !== "completed").map((q) => q.id));
+   return A.find((q) => {
+     if (q.status !== "pending") return !1;
+     if (q.owner) return !1;
+     return q.blockedBy.every((Y) => !K.has(Y));
+   });
+ }

+++ Added VM2 (pretty-v2.1.20.js:422600-422609)
+ function VM2(A) {
+   let K = `Complete all open tasks. Start with task #${A.id}: 
+ 
+  ${A.subject}`;
+   if (A.description)
+     K += `
+ 
+ ${A.description}`;
+   return K;
+ }

+++ Added C7K (pretty-v2.1.20.js:422610-422629)
+ function C7K(A, K) {
+   try {
+     let q = JZ(A),
+       Y = PM2(q);
+     if (!Y) return;
+     let z = j46(A, Y.id, K);
+     if (!z.success) {
+       h(`[inProcessRunner] Failed to claim task #${Y.id}: ${z.reason}`);
+       return;
+     }
+     return (
+       _y(A, Y.id, { status: "in_progress" }),
+       h(`[inProcessRunner] Claimed task #${Y.id}: ${Y.subject}`),
+       VM2(Y)
+     );
+   } catch (q) {
+     h(`[inProcessRunner] Error checking task list: ${q}`);
+     return;
+   }
+ }

+++ Added R7K (pretty-v2.1.20.js:423129-423131)
+ function R7K() {
+   return new L7K();
+ }

+++ Added h7K (pretty-v2.1.20.js:423206-423212)
+ function h7K() {
+   if (dMA)
+     ((jt = dMA), h(`[TeammateModeSnapshot] Captured from CLI override: ${jt}`));
+   else
+     ((jt = P1().teammateMode ?? "auto"),
+       h(`[TeammateModeSnapshot] Captured from config: ${jt}`));
+ }

+++ Added LM2 (pretty-v2.1.20.js:423924-423924)
+   LM2 = 200;

+++ Added _KK (pretty-v2.1.20.js:425168-425211)
+ function _KK(
+   A,
+   {
+     teammateId: K,
+     sanitizedName: q,
+     teamName: Y,
+     teammateColor: z,
+     prompt: w,
+     plan_mode_required: H,
+     paneId: J,
+     insideTmux: O,
+   },
+ ) {
+   let X = Yp("in_process_teammate"),
+     $ = `${q}: ${w.substring(0, 50)}${w.length > 50 ? "..." : ""}`,
+     _ = new AbortController(),
+     Z = {
+       ...lj(X, "in_process_teammate", $),
+       type: "in_process_teammate",
+       status: "running",
+       identity: {
+         agentId: K,
+         agentName: q,
+         teamName: Y,
+         color: z,
+         planModeRequired: H ?? !1,
+         parentSessionId: i1(),
+       },
+       prompt: w,
+       abortController: _,
+       awaitingPlanApproval: !1,
+       permissionMode: H ? "plan" : "default",
+       isIdle: !1,
+       shutdownRequested: !1,
+       lastReportedToolCount: 0,
+       lastReportedTokenCount: 0,
+       pendingUserMessages: [],
+     };
+   (ij(Z, A),
+     _.signal.addEventListener("abort", () => {
+       let W = !O ? ["-L", ZMA(), "kill-pane", "-t", J] : ["kill-pane", "-t", J];
+       u6(XM, W);
+     }));
+ }

+++ Added Hj2 (pretty-v2.1.20.js:425416-425419)
+ function Hj2(A, K) {
+   if (!j8()) return;
+   return A.team_name || K.teamContext?.teamName;
+ }

+++ Added NQA (pretty-v2.1.20.js:426027-426084)
+ var NQA = C(() => {
+   OX();
+   D1();
+   R1();
+   OX();
+   toA();
+   $z();
+   o7();
+   a1();
+   cI6 = K6(async (A) => {
+     let K = await fS(A),
+       q = i4("tengu_kv7_prompt_sort", !1)
+         ? [...K].sort((H, J) => H.name.localeCompare(J.name))
+         : K,
+       Y = q.map((H) => H.userFacingName()).join(", ");
+     h(`Skills and commands included in Skill tool: ${Y}`);
+     let z = $j2(q),
+       w = `Execute a skill within the main conversation
+ 
+ When users ask you to perform tasks, check if any of the available skills below can help complete the task more effectively. Skills provide specialized capabilities and domain knowledge.
+ 
+ When users ask you to run a "slash command" or reference "/<something>" (e.g., "/commit", "/review-pr"), they are referring to a skill. Use this tool to invoke the corresponding skill.
+ 
+ Example:
+   User: "run /commit"
+   Assistant: [Calls Skill tool with skill: "commit"]
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
+ - When a skill is relevant, you must invoke this tool IMMEDIATELY as your first action
+ - NEVER just announce or mention a skill in your text response without actually calling this tool
+ - This is a BLOCKING REQUIREMENT: invoke the relevant Skill tool BEFORE generating any other response about the task
+ - Skills listed below are available for invocation
+ - Do not invoke a skill that is already running
+ - Do not use this tool for built-in CLI commands (like /help, /clear, etc.)
+ - If you see a <${uM}> tag in the current conversation turn (e.g., <${uM}>/commit</${uM}>), the skill has ALREADY been loaded and its instructions follow in the next message. Do NOT call this tool - just follow the skill instructions directly.
+ 
+ Available skills:
+ ${z}
+ `;
+     if (VQA !== void 0 && w !== VQA)
+       n("tengu_tool_prompt_changed", {
+         tool: "SkillTool",
+         previousLength: VQA.length,
+         newLength: w.length,
+         previousCommandCount: (VQA.match(/^- /gm) ?? []).length,
+         newCommandCount: (w.match(/^- /gm) ?? []).length,
+       });
+     return ((VQA = w), w);
+   });
+ });

+++ Added bYK (pretty-v2.1.20.js:446638-446791)
+ var bYK = C(() => {
+   ((RT2 = `Use this tool proactively when you're about to start a non-trivial implementation task. Getting user sign-off on your approach before writing code prevents wasted effort and ensures alignment. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
+    - If you would use ${xJ} to clarify the approach, use EnterPlanMode instead
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
+ 5. Use ${xJ} if you need to clarify approaches
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
+     (paH = `Use this tool when a task has genuine ambiguity about the right approach and getting user input before coding would prevent significant rework. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
+ When in doubt, prefer starting work and using ${xJ} for specific questions over entering a full planning phase.
+ 
+ ## What Happens in Plan Mode
+ 
+ In plan mode, you'll:
+ 1. Explore the codebase using Glob, Grep, and Read tools
+ 2. Understand existing patterns and architecture
+ 3. Design an implementation approach
+ 4. Present your plan to the user for approval
+ 5. Use ${xJ} if you need to clarify approaches
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

+++ Added tYK (pretty-v2.1.20.js:447272-447274)
+ function tYK(A) {
+   return null;
+ }

+++ Added _2K (pretty-v2.1.20.js:447492-447566)
+   _2K = `Use this tool to update a task in the task list.
+ 
+ ## When to Use This Tool
+ 
+ **Mark tasks as resolved:**
+ - When you have completed the work described in a task
+ - When a task is no longer needed or has been superseded
+ - IMPORTANT: Always mark your assigned tasks as resolved when you finish them
+ - After resolving, call TaskList to find your next task
+ 
+ - ONLY mark a task as completed when you have FULLY accomplished it
+ - If you encounter errors, blockers, or cannot finish, keep the task as in_progress
+ - When blocked, create a new task describing what needs to be resolved
+ - Never mark a task as completed if:
+   - Tests are failing
+   - Implementation is partial
+   - You encountered unresolved errors
+   - You couldn't find necessary files or dependencies
+ 
+ **Delete tasks:**
+ - When a task is no longer relevant or was created in error
+ - Setting status to \`deleted\` permanently removes the task
+ 
+ **Update task details:**
+ - When requirements change or become clearer
+ - When establishing dependencies between tasks
+ 
+ ## Fields You Can Update
+ 
+ - **status**: The task status (see Status Workflow below)
+ - **subject**: Change the task title (imperative form, e.g., "Run tests")
+ - **description**: Change the task description
+ - **activeForm**: Present continuous form shown in spinner when in_progress (e.g., "Running tests")
+ - **owner**: Change the task owner (agent name)
+ - **metadata**: Merge metadata keys into the task (set a key to null to delete it)
+ - **addBlocks**: Mark tasks that cannot start until this one completes
+ - **addBlockedBy**: Mark tasks that must complete before this one can start
+ 
+ ## Status Workflow
+ 
+ Status progresses: \`pending\` → \`in_progress\` → \`completed\`
+ 
+ Use \`deleted\` to permanently remove a task.
+ 
+ ## Staleness
+ 
+ Make sure to read a task's latest state using \`TaskGet\` before updating it.
+ 
+ ## Examples
+ 
+ Mark task as in progress when starting work:
+ \`\`\`json
+ {"taskId": "1", "status": "in_progress"}
+ \`\`\`
+ 
+ Mark task as completed after finishing work:
+ \`\`\`json
+ {"taskId": "1", "status": "completed"}
+ \`\`\`
+ 
+ Delete a task:
+ \`\`\`json
+ {"taskId": "1", "status": "deleted"}
+ \`\`\`
+ 
+ Claim a task by setting owner:
+ \`\`\`json
+ {"taskId": "1", "owner": "my-name"}
+ \`\`\`
+ 
+ Set up task dependencies:
+ \`\`\`json
+ {"taskId": "2", "addBlockedBy": ["1"]}
+ \`\`\`
+ `;

+++ Added M2K (pretty-v2.1.20.js:447579-447581)
+ function M2K(A) {
+   return null;
+ }

+++ Added E2K (pretty-v2.1.20.js:447830-447832)
+ function E2K() {
+   return null;
+ }

+++ Added k2K (pretty-v2.1.20.js:447833-447835)
+ function k2K() {
+   return null;
+ }

+++ Added C2K (pretty-v2.1.20.js:447836-447838)
+ function C2K(A) {
+   return null;
+ }

+++ Added tQA (pretty-v2.1.20.js:447930-447930)
+ var tQA = "SendMessage";

+++ Added I2K (pretty-v2.1.20.js:447931-448077)
+ function I2K() {
+   return `
+ # SendMessageTool
+ 
+ Send messages to teammates and handle protocol requests/responses in a swarm.
+ 
+ ## Message Types
+ 
+ ### type: "message" - Send a Direct Message
+ 
+ Send a message to a **single specific teammate**. You MUST specify the recipient.
+ 
+ **IMPORTANT for teammates**: Your plain text output is NOT visible to the team lead or other teammates. To communicate with anyone on your team, you **MUST** use this tool. Just typing a response or acknowledgment in text is not enough.
+ 
+ \`\`\`
+ {
+   "type": "message",
+   "recipient": "researcher",
+   "content": "Your message here"
+ }
+ \`\`\`
+ 
+ - **recipient**: The name of the teammate to message (required)
+ - **content**: The message text (required)
+ 
+ ### type: "broadcast" - Send Message to ALL Teammates (USE SPARINGLY)
+ 
+ Send the **same message to everyone** on the team at once.
+ 
+ **WARNING: Broadcasting is expensive.** Each broadcast sends a separate message to every teammate, which means:
+ - N teammates = N separate message deliveries
+ - Each delivery consumes API resources
+ - Costs scale linearly with team size
+ 
+ \`\`\`
+ {
+   "type": "broadcast",
+   "content": "Message to send to all teammates"
+ }
+ \`\`\`
+ 
+ - **content**: The message content to broadcast (required)
+ 
+ **CRITICAL: Use broadcast only when absolutely necessary.** Valid use cases:
+ - Critical issues requiring immediate team-wide attention (e.g., "stop all work, blocking bug found")
+ - Major announcements that genuinely affect every teammate equally
+ 
+ **Default to "message" instead of "broadcast".** Use "message" for:
+ - Responding to a single teammate
+ - Normal back-and-forth communication
+ - Following up on a task with one person
+ - Sharing findings relevant to only some teammates
+ - Any message that doesn't require everyone's attention
+ 
+ ### type: "request" - Send a Protocol Request
+ 
+ #### subtype: "shutdown" - Request a Teammate to Shut Down
+ 
+ Use this to ask a teammate to gracefully shut down:
+ 
+ \`\`\`
+ {
+   "type": "request",
+   "subtype": "shutdown",
+   "recipient": "researcher",
+   "content": "Task complete, wrapping up the session"
+ }
+ \`\`\`
+ 
+ The teammate will receive a shutdown request and can either approve (exit) or reject (continue working).
+ 
+ #### subtype: "plan_approval" - Approve or Reject a Teammate's Plan
+ 
+ Not used as a request. Plan approval/rejection is done via "response" type.
+ 
+ ### type: "response" - Respond to a Protocol Request
+ 
+ #### Approve Shutdown
+ 
+ When you receive a shutdown request as a JSON message with \`type: "shutdown_request"\`, you **MUST** respond to approve or reject it. Do NOT just acknowledge the request in text - you must actually call this tool.
+ 
+ \`\`\`
+ {
+   "type": "response",
+   "subtype": "shutdown",
+   "request_id": "abc-123",
+   "approve": true
+ }
+ \`\`\`
+ 
+ **IMPORTANT**: Extract the \`requestId\` from the JSON message and pass it as \`request_id\` to the tool. Simply saying "I'll shut down" is not enough - you must call the tool.
+ 
+ This will send confirmation to the leader and terminate your process.
+ 
+ #### Reject Shutdown
+ 
+ \`\`\`
+ {
+   "type": "response",
+   "subtype": "shutdown",
+   "request_id": "abc-123",
+   "approve": false,
+   "content": "Still working on task #3, need 5 more minutes"
+ }
+ \`\`\`
+ 
+ The leader will receive your rejection with the reason.
+ 
+ #### Approve Plan
+ 
+ When a teammate with \`plan_mode_required\` calls ExitPlanMode, they send you a plan approval request as a JSON message with \`type: "plan_approval_request"\`. Use this to approve their plan:
+ 
+ \`\`\`
+ {
+   "type": "response",
+   "subtype": "plan_approval",
+   "request_id": "abc-123",
+   "recipient": "researcher",
+   "approve": true
+ }
+ \`\`\`
+ 
+ After approval, the teammate will automatically exit plan mode and can proceed with implementation.
+ 
+ #### Reject Plan
+ 
+ \`\`\`
+ {
+   "type": "response",
+   "subtype": "plan_approval",
+   "request_id": "abc-123",
+   "recipient": "researcher",
+   "approve": false,
+   "content": "Please add error handling for the API calls"
+ }
+ \`\`\`
+ 
+ The teammate will receive the rejection with your feedback and can revise their plan.
+ 
+ ## Important Notes
+ 
+ - Messages from teammates are automatically delivered to you. You do NOT need to manually check your inbox.
+ - When reporting on teammate messages, you do NOT need to quote the original message - it's already rendered to the user.
+ - **IMPORTANT**: Always refer to teammates by their NAME (e.g., "team-lead", "researcher", "tester"), never by UUID.
+ - Do NOT send structured JSON status messages. Use TaskUpdate to mark tasks completed and the system will automatically send idle notifications when you stop.
+ `.trim();
+ }

+++ Added y2K (pretty-v2.1.20.js:448078-448079)
+ var y2K =
+   "Send messages to teammates and handle protocol requests (shutdown, plan approval)";

+++ Added S2K (pretty-v2.1.20.js:448080-448106)
+ function S2K(A) {
+   switch (A.type) {
+     case "message": {
+       let K = A.content ? `: "${o9(String(A.content), 50)}"` : "";
+       return `send message to @${A.recipient}${K}`;
+     }
+     case "broadcast":
+       return `broadcast message to all teammates${A.content ? `: "${o9(String(A.content), 50)}"` : ""}`;
+     case "request": {
+       if (A.subtype === "shutdown") return `request shutdown: ${A.recipient}`;
+       return `send ${A.subtype} request to @${A.recipient}`;
+     }
+     case "response": {
+       if (A.subtype === "shutdown")
+         return A.approve
+           ? "approve shutdown"
+           : `reject shutdown: ${A.content || "no reason"}`;
+       if (A.subtype === "plan_approval")
+         return A.approve
+           ? `approve plan from: ${A.recipient}`
+           : `reject plan from: ${A.recipient}`;
+       return `respond to ${A.subtype} request`;
+     }
+     default:
+       return "agent message operation";
+   }
+ }

+++ Added h2K (pretty-v2.1.20.js:448107-448109)
+ function h2K() {
+   return null;
+ }

+++ Added b2K (pretty-v2.1.20.js:448110-448112)
+ function b2K() {
+   return dh6.default.createElement(b9, null);
+ }

+++ Added x2K (pretty-v2.1.20.js:448113-448115)
+ function x2K(A, { verbose: K }) {
+   return dh6.default.createElement(S3, { result: A, verbose: K });
+ }

+++ Added u2K (pretty-v2.1.20.js:448116-448118)
+ function u2K() {
+   return null;
+ }

+++ Added nT2 (pretty-v2.1.20.js:448207-448238)
+ async function nT2(A, K) {
+   let q = await K.getAppState(),
+     Y = e3(q.teamContext);
+   if (!A.recipient)
+     throw Error(
+       "recipient is required for shutdown request to specify which teammate to shut down",
+     );
+   let z = g2K(A.recipient),
+     w = I9() || T2,
+     H = wt("shutdown", z),
+     J = MMA({ requestId: H, from: w, reason: A.content });
+   return (
+     d3(
+       z,
+       {
+         from: w,
+         text: QA(J),
+         timestamp: new Date().toISOString(),
+         color: VJ(),
+       },
+       Y,
+     ),
+     {
+       data: {
+         success: !0,
+         message: `Shutdown request sent to ${z}. Request ID: ${H}`,
+         request_id: H,
+         target: z,
+       },
+     }
+   );
+ }

+++ Added rT2 (pretty-v2.1.20.js:448239-448321)
+ async function rT2(A, K) {
+   let q = e3(),
+     Y = A_(),
+     z = I9() || "teammate";
+   if (!A.request_id)
+     throw Error(
+       "request_id is required for shutdown response. Use the requestId from the shutdown_request message.",
+     );
+   let w = A.request_id;
+   h(
+     `[SendMessageTool] handleShutdownApproval: teamName=${q}, agentId=${Y}, agentName=${z}`,
+   );
+   let H, J;
+   if (q) {
+     let X = N3A(q);
+     if (X && Y) {
+       let $ = X.members.find((_) => _.agentId === Y);
+       if ($) ((H = $.tmuxPaneId), (J = $.backendType));
+     }
+   }
+   let O = hR6({ requestId: w, from: z, paneId: H, backendType: J });
+   if (
+     (d3(
+       T2,
+       {
+         from: z,
+         text: QA(O),
+         timestamp: new Date().toISOString(),
+         color: VJ(),
+       },
+       q,
+     ),
+     J === "in-process")
+   ) {
+     if (
+       (h(
+         `[SendMessageTool] In-process teammate ${z} approving shutdown - signaling abort`,
+       ),
+       Y)
+     ) {
+       let X = await K.getAppState(),
+         $ = G3A(Y, X.tasks);
+       if ($?.abortController)
+         ($.abortController.abort(),
+           h(
+             `[SendMessageTool] Aborted controller for in-process teammate ${z}`,
+           ));
+       else
+         h(
+           `[SendMessageTool] Warning: Could not find task/abortController for ${z}`,
+         );
+     }
+   } else {
+     if (Y) {
+       let X = await K.getAppState(),
+         $ = G3A(Y, X.tasks);
+       if ($?.abortController)
+         return (
+           h(
+             `[SendMessageTool] Fallback: Found in-process task for ${z} via AppState, aborting`,
+           ),
+           $.abortController.abort(),
+           {
+             data: {
+               success: !0,
+               message: `Shutdown approved (fallback path). Agent ${z} is now exiting.`,
+               request_id: w,
+             },
+           }
+         );
+     }
+     setImmediate(async () => {
+       await rq(0, "other");
+     });
+   }
+   return {
+     data: {
+       success: !0,
+       message: `Shutdown approved. Sent confirmation to team-lead. Agent ${z} is now exiting.`,
+       request_id: w,
+     },
+   };
+ }

+++ Added Q2K (pretty-v2.1.20.js:448433-448610)
+ var Q2K = C(() => {
+   G7();
+   B2K();
+   oH();
+   j2();
+   FI6();
+   D1();
+   m4();
+   S9();
+   ZH();
+   W3A();
+   B1();
+   m2K = U.strictObject({
+     type: U.enum(["message", "broadcast", "request", "response"]).describe(
+       'Message type: "message" for DMs, "broadcast" to all teammates, "request" for protocol requests (shutdown, plan approval), "response" for protocol responses',
+     ),
+     recipient: U.string()
+       .optional()
+       .describe(
+         "Agent name of the recipient (required for message and request types)",
+       ),
+     content: U.string()
+       .optional()
+       .describe("Message text, reason, or feedback"),
+     subtype: U.enum(["shutdown", "plan_approval"])
+       .optional()
+       .describe("Protocol subtype (required for request and response types)"),
+     request_id: U.string()
+       .optional()
+       .describe("Request ID to respond to (required for response type)"),
+     approve: U.boolean()
+       .optional()
+       .describe("Whether to approve the request (required for response type)"),
+   });
+   tT2 = {
+     name: tQA,
+     maxResultSizeChars: 1e5,
+     userFacingName() {
+       if (j8()) return "";
+       return "SendMessage";
+     },
+     inputSchema: m2K,
+     isEnabled() {
+       return j8() && Qj1();
+     },
+     isConcurrencySafe(A) {
+       return !1;
+     },
+     isReadOnly(A) {
+       return A.type === "message" || A.type === "broadcast";
+     },
+     async checkPermissions(A, K) {
+       return { behavior: "allow", updatedInput: A };
+     },
+     async validateInput(A, K) {
+       if (A.type === "message") {
+         if (!A.recipient || A.recipient.trim().length === 0)
+           return {
+             result: !1,
+             message: "recipient is required for message type",
+             errorCode: 1,
+           };
+         if (!A.content || A.content.trim().length === 0)
+           return {
+             result: !1,
+             message: "content is required for message type",
+             errorCode: 2,
+           };
+       }
+       if (A.type === "broadcast") {
+         if (!A.content || A.content.trim().length === 0)
+           return {
+             result: !1,
+             message: "content is required for broadcast type",
+             errorCode: 3,
+           };
+       }
+       if (A.type === "request") {
+         if (!A.subtype)
+           return {
+             result: !1,
+             message: "subtype is required for request type",
+             errorCode: 4,
+           };
+         if (!A.recipient || A.recipient.trim().length === 0)
+           return {
+             result: !1,
+             message: "recipient is required for request type",
+             errorCode: 5,
+           };
+       }
+       if (A.type === "response") {
+         if (!A.subtype)
+           return {
+             result: !1,
+             message: "subtype is required for response type",
+             errorCode: 6,
+           };
+         if (!A.request_id || A.request_id.trim().length === 0)
+           return {
+             result: !1,
+             message: "request_id is required for response type",
+             errorCode: 7,
+           };
+         if (A.approve === void 0)
+           return {
+             result: !1,
+             message: "approve is required for response type",
+             errorCode: 8,
+           };
+         if (
+           A.subtype === "shutdown" &&
+           !A.approve &&
+           (!A.content || A.content.trim().length === 0)
+         )
+           return {
+             result: !1,
+             message:
+               "content (reason) is required when rejecting a shutdown request",
+             errorCode: 9,
+           };
+         if (
+           A.subtype === "plan_approval" &&
+           (!A.recipient || A.recipient.trim().length === 0)
+         )
+           return {
+             result: !1,
+             message:
+               "recipient is required for plan approval/rejection responses",
+             errorCode: 10,
+           };
+       }
+       return { result: !0 };
+     },
+     async description() {
+       return y2K;
+     },
+     async prompt() {
+       return I2K();
+     },
+     mapToolResultToToolResultBlockParam(A, K) {
+       return {
+         tool_use_id: K,
+         type: "tool_result",
+         content: [{ type: "text", text: QA(A, null, 2) }],
+       };
+     },
+     async call(A, K) {
+       if (A.type === "message") return lT2(A, K);
+       if (A.type === "broadcast") return iT2(A, K);
+       if (A.type === "request") {
+         if (A.subtype === "shutdown") return nT2(A, K);
+         throw Error(
+           `Unsupported request subtype: ${A.subtype}. Use "shutdown" for shutdown requests.`,
+         );
+       }
+       if (A.type === "response") {
+         if (A.subtype === "shutdown") {
+           if (A.approve) return rT2(A, K);
+           return oT2(A);
+         }
+         if (A.subtype === "plan_approval") {
+           if (A.approve) return aT2(A, K);
+           return sT2(A, K);
+         }
+         throw Error(
+           `Unsupported response subtype: ${A.subtype}. Use "shutdown" or "plan_approval".`,
+         );
+       }
+       throw Error(`Unknown message type: ${A.type}`);
+     },
+     renderToolUseMessage: S2K,
+     renderToolUseProgressMessage: h2K,
+     renderToolUseRejectedMessage: b2K,
+     renderToolUseErrorMessage: x2K,
+     renderToolResultMessage: u2K,
+   };
+ });

+++ Added Av2 (pretty-v2.1.20.js:448679-448679)
+   Av2 = () => (Q2K(), _h(F2K)).SendMessageTool,

+++ Added Hk2 (pretty-v2.1.20.js:459193-459208)
+   Hk2 = `You are coming up with a succinct title and git branch name for a coding session based on the provided description. The title should be clear, concise, and accurately reflect the content of the coding task.
+ You should keep it short and simple, ideally no more than 6 words. Avoid using jargon or overly technical terms unless absolutely necessary. The title should be easy to understand for anyone reading it.
+ Use sentence case for the title (capitalize only the first word and proper nouns), not Title Case.
+ 
+ The branch name should be clear, concise, and accurately reflect the content of the coding task.
+ You should keep it short and simple, ideally no more than 4 words. The branch should always start with "claude/" and should be all lower case, with words separated by dashes.
+ 
+ Return a JSON object with "title" and "branch" fields.
+ 
+ Example 1: {"title": "Fix login button not working on mobile", "branch": "claude/fix-mobile-login-button"}
+ Example 2: {"title": "Update README with installation instructions", "branch": "claude/update-readme"}
+ Example 3: {"title": "Improve performance of data processing script", "branch": "claude/improve-data-processing"}
+ 
+ Here is the session description:
+ <description>{description}</description>
+ Please generate a title and branch name for this session.`;

+++ Added MC2 (pretty-v2.1.20.js:460815-460824)
+ function MC2() {
+   return async () => ({
+     behavior: "deny",
+     message: "Tool use is not allowed during compaction",
+     decisionReason: {
+       type: "other",
+       reason: "compaction agent should only produce text summary",
+     },
+   });
+ }

+++ Added jHK (pretty-v2.1.20.js:461110-461112)
+ function jHK(A) {
+   OHK = A;
+ }

+++ Added eHK (pretty-v2.1.20.js:463237-463239)
+ function eHK() {
+   return null;
+ }

+++ Added O0K (pretty-v2.1.20.js:469449-469517)
+ function O0K(A) {
+   let K = [],
+     q = !1;
+   for (let Y = 0; Y < A.length; Y++) {
+     let z = A[Y];
+     if ((K.push(z), z.type !== "assistant")) continue;
+     let w = z.message.content
+       .filter(($) => $.type === "tool_use")
+       .map(($) => $.id);
+     if (w.length === 0) continue;
+     let H = A[Y + 1],
+       J = new Set();
+     if (H?.type === "user") {
+       let $ = H.message.content;
+       if (Array.isArray($)) {
+         for (let _ of $)
+           if (typeof _ === "object" && "type" in _ && _.type === "tool_result")
+             J.add(_.tool_use_id);
+       }
+     }
+     let O = w.filter(($) => !J.has($));
+     if (O.length === 0) continue;
+     q = !0;
+     let X = O.map(($) => ({
+       type: "tool_result",
+       tool_use_id: $,
+       content: "[Tool result missing due to internal error]",
+       is_error: !0,
+     }));
+     if (H?.type === "user") {
+       let $ = Array.isArray(H.message.content)
+           ? H.message.content
+           : [{ type: "text", text: H.message.content }],
+         _ = { ...H, message: { ...H.message, content: [...X, ...$] } };
+       (Y++, K.push(_));
+     } else K.push(q6({ content: X, isMeta: !0 }));
+   }
+   if (q) {
+     let Y = A.map((z, w) => {
+       if (z.type === "assistant") {
+         let H = z.message.content
+           .filter((J) => J.type === "tool_use")
+           .map((J) => J.id);
+         return `[${w}] assistant(id=${z.message.id}, tool_uses=[${H.join(",")}])`;
+       }
+       if (z.type === "user" && Array.isArray(z.message.content)) {
+         let H = z.message.content
+           .filter(
+             (J) =>
+               typeof J === "object" && "type" in J && J.type === "tool_result",
+           )
+           .map((J) => J.tool_use_id);
+         if (H.length > 0) return `[${w}] user(tool_results=[${H.join(",")}])`;
+       }
+       return `[${w}] ${z.type}`;
+     });
+     (n("tengu_tool_result_pairing_repaired", {
+       messageCount: A.length,
+       repairedMessageCount: K.length,
+       messageTypes: Y.join("; "),
+     }),
+       qA(
+         Error(
+           `ensureToolResultPairing: repaired missing tool_result blocks (${A.length} -> ${K.length} messages). Message structure: ${Y.join("; ")}`,
+         ),
+       ));
+   }
+   return K;
+ }

+++ Added pR2 (pretty-v2.1.20.js:469534-469535)
+   pR2 =
+     "IMPORTANT: You *may* attempt to accomplish this action using other tools that might naturally be used to accomplish this goal, e.g. using head instead of cat. But you *should not* attempt to work around this denial in malicious ways, e.g. do not use your ability to run tests to execute non-test actions. You should only try to work around this restriction in reasonable ways that do not attempt to bypass the intent behind this denial. If you believe this capability is essential to complete the user's request, STOP and explain to the user what you were trying to do and why you need this permission. Let the user decide how to proceed.",

+++ Added Vd (pretty-v2.1.20.js:470024-470035)
+ async function Vd(A, K) {
+   let q = E0K(A),
+     Y = i1(),
+     z = await Xu6(Y),
+     w = [],
+     H;
+   for (let J of q)
+     if (z.has(J.uuid)) H = J.uuid;
+     else w.push(J);
+   if (w.length > 0) await of().insertMessageChain(w, !1, void 0, H, K);
+   return q[q.length - 1]?.uuid || null;
+ }

+++ Added iu6 (pretty-v2.1.20.js:475817-475817)
+ var iu6 = {};

+++ Added RS2 (pretty-v2.1.20.js:476405-476409)
+ function RS2(A) {
+   return A.filter((K) => K.type === "text" && K.text).map((K) => K.text).join(`
+ 
+ `);
+ }

+++ Added GXK (pretty-v2.1.20.js:476411-476446)
+ var GXK = C(() => {
+   Cp();
+   P8();
+   c2();
+   ((yS2 = {
+     type: "local",
+     name: "copy",
+     description: "Copy Claude's last response to clipboard as markdown",
+     isEnabled: () => !0,
+     isHidden: !1,
+     supportsNonInteractive: !1,
+     async call(A, K) {
+       l7("copy");
+       let q = Uf(K.messages);
+       if (!q) return { type: "text", value: "No assistant message to copy" };
+       let Y = q.message.content;
+       if (!Array.isArray(Y) || Y.length === 0)
+         return { type: "text", value: "No content to copy" };
+       let z = RS2(Y);
+       if (!z) return { type: "text", value: "No text content to copy" };
+       if (await KM(z)) {
+         let H = z.split(`
+ `).length;
+         return {
+           type: "text",
+           value: `Copied to clipboard (${z.length} characters, ${H} lines)`,
+         };
+       }
+       return { type: "text", value: bWA() };
+     },
+     userFacingName() {
+       return "copy";
+     },
+   }),
+     (ZXK = yS2));
+ });

+++ Added SS2 (pretty-v2.1.20.js:476452-476475)
+ async function SS2(A, K) {
+   let q = await A.getAppState(),
+     Y = await df(
+       A.options.tools,
+       A.options.mainLoopModel,
+       Array.from(q.toolPermissionContext.additionalWorkingDirectories.keys()),
+       A.options.mcpClients,
+     ),
+     z = p_A({
+       mainThreadAgentDefinition: void 0,
+       toolUseContext: A,
+       customSystemPrompt: A.options.customSystemPrompt,
+       defaultSystemPrompt: Y,
+       appendSystemPrompt: A.options.appendSystemPrompt,
+     }),
+     [w, H] = await Promise.all([nO(), iO()]);
+   return {
+     systemPrompt: z,
+     userContext: w,
+     systemContext: H,
+     toolUseContext: A,
+     forkContextMessages: K,
+   };
+ }

+++ Added mXK (pretty-v2.1.20.js:478129-478131)
+ function mXK() {
+   return [];
+ }

+++ Added D$K (pretty-v2.1.20.js:482624-482624)
+   D$K = "\x1B[?2026h",

+++ Added Pb2 (pretty-v2.1.20.js:482625-482625)
+   Pb2 = "\x1B[?2026l";

+++ Added p$K (pretty-v2.1.20.js:484237-484280)
+ function p$K() {
+   let A = s(2);
+   if (!x8.isSupportedPlatform()) return null;
+   if (!x8.isSandboxEnabledInSettings()) return null;
+   let K, q;
+   if (A[0] === Symbol.for("react.memo_cache_sentinel")) {
+     q = Symbol.for("react.early_return_sentinel");
+     A: {
+       let Y = x8.checkDependencies(),
+         z = Y.errors.length > 0,
+         w = Y.warnings.length > 0;
+       if (!z && !w) {
+         q = null;
+         break A;
+       }
+       K = eZ.default.createElement(
+         I,
+         { flexDirection: "column" },
+         eZ.default.createElement(f, { bold: !0 }, "Sandbox"),
+         eZ.default.createElement(
+           f,
+           null,
+           "└ Status: ",
+           eZ.default.createElement(
+             f,
+             { color: z ? "error" : "warning" },
+             z ? "Missing dependencies" : "Available (with warnings)",
+           ),
+         ),
+         Y.errors.map(cb2),
+         Y.warnings.map(db2),
+         z &&
+           eZ.default.createElement(
+             f,
+             { dimColor: !0 },
+             "└ Run /sandbox for install instructions",
+           ),
+       );
+     }
+     ((A[0] = K), (A[1] = q));
+   } else ((K = A[0]), (q = A[1]));
+   if (q !== Symbol.for("react.early_return_sentinel")) return q;
+   return K;
+ }

+++ Added db2 (pretty-v2.1.20.js:484281-484283)
+ function db2(A, K) {
+   return eZ.default.createElement(f, { key: K, color: "warning" }, "└ ", A);
+ }

+++ Added cb2 (pretty-v2.1.20.js:484284-484286)
+ function cb2(A, K) {
+   return eZ.default.createElement(f, { key: K, color: "error" }, "└ ", A);
+ }

+++ Added I_K (pretty-v2.1.20.js:486654-486666)
+ var I_K = C(() => {
+   T51();
+   v51();
+   B1();
+   Rx2 = {
+     context: "Chat",
+     bindings: {
+       "ctrl+k ctrl+h": "command:help",
+       "ctrl+k ctrl+k": "command:compact",
+       "ctrl+k ctrl+m": "command:model",
+     },
+   };
+ });

+++ Added ou2 (pretty-v2.1.20.js:498995-498997)
+ function ou2() {
+   return null;
+ }

+++ Added Hg6 (pretty-v2.1.20.js:504543-504543)
+   Hg6 = 4,

+++ Added fU2 (pretty-v2.1.20.js:508417-508417)
+   fU2 = 4,

+++ Added Jp2 (pretty-v2.1.20.js:510471-510485)
+ function Jp2(A, K, q) {
+   let Y = K.find((z) => z.name === A.toolName);
+   if (!Y) return A.toolName;
+   try {
+     let z = Y.inputSchema.safeParse(A.input),
+       w = z.success ? z.data : {},
+       H = Y.userFacingName(w);
+     if (!H) return A.toolName;
+     let J = Y.renderToolUseMessage(w, { theme: q, verbose: !1 });
+     if (J) return QY.default.createElement(f, null, H, "(", J, ")");
+     return H;
+   } catch {
+     return A.toolName;
+   }
+ }

+++ Added GjK (pretty-v2.1.20.js:510486-510798)
+ function GjK(A) {
+   let K = s(66),
+     { teammate: q, onDone: Y, onKill: z, onBack: w, onForeground: H } = A,
+     [J] = b4(),
+     O;
+   if (K[0] === Symbol.for("react.memo_cache_sentinel"))
+     ((O = L$(q_())), (K[0] = O));
+   else O = K[0];
+   let X = O,
+     $ = $dA(q.startTime, q.status === "running"),
+     _;
+   if (K[1] !== Y)
+     ((_ = { "confirm:no": Y, "confirm:yes": Y }), (K[1] = Y), (K[2] = _));
+   else _ = K[2];
+   let Z;
+   if (K[3] === Symbol.for("react.memo_cache_sentinel"))
+     ((Z = { context: "Confirmation" }), (K[3] = Z));
+   else Z = K[3];
+   X7(_, Z);
+   let G;
+   if (K[4] !== w || K[5] !== Y || K[6] !== H || K[7] !== z || K[8] !== q.status)
+     ((G = (HA, DA) => {
+       if (HA === " ") Y();
+       else if (DA.leftArrow && w) w();
+       else if (HA === "k" && q.status === "running" && z) z();
+       else if (HA === "f" && q.status === "running" && H) H();
+     }),
+       (K[4] = w),
+       (K[5] = Y),
+       (K[6] = H),
+       (K[7] = z),
+       (K[8] = q.status),
+       (K[9] = G));
+   else G = K[9];
+   K8(G);
+   let W = k8(),
+     D;
+   if (
+     K[10] !== q.awaitingPlanApproval ||
+     K[11] !== q.isIdle ||
+     K[12] !== q.progress ||
+     K[13] !== q.shutdownRequested
+   )
+     ((D = q.shutdownRequested
+       ? "stopping"
+       : q.awaitingPlanApproval
+         ? "awaiting approval"
+         : q.isIdle
+           ? "idle"
+           : ((q.progress?.recentActivities &&
+               vGA(q.progress.recentActivities)) ??
+             q.progress?.lastActivity?.activityDescription ??
+             "working")),
+       (K[10] = q.awaitingPlanApproval),
+       (K[11] = q.isIdle),
+       (K[12] = q.progress),
+       (K[13] = q.shutdownRequested),
+       (K[14] = D));
+   else D = K[14];
+   let M = D,
+     j = q.result?.totalTokens ?? q.progress?.tokenCount,
+     P = q.result?.totalToolUseCount ?? q.progress?.toolUseCount,
+     V = q.prompt.length > 300 ? q.prompt.substring(0, 297) + "…" : q.prompt,
+     N;
+   if (K[15] !== q.identity.color)
+     ((N = YL(q.identity.color)), (K[15] = q.identity.color), (K[16] = N));
+   else N = K[16];
+   let T;
+   if (K[17] !== N || K[18] !== q.identity.agentName)
+     ((T = QY.default.createElement(f, { color: N }, "@", q.identity.agentName)),
+       (K[17] = N),
+       (K[18] = q.identity.agentName),
+       (K[19] = T));
+   else T = K[19];
+   let k;
+   if (K[20] !== M)
+     ((k = QY.default.createElement(f, { dimColor: !0 }, " (", M, ")")),
+       (K[20] = M),
+       (K[21] = k));
+   else k = K[21];
+   let R;
+   if (K[22] !== T || K[23] !== k)
+     ((R = QY.default.createElement(I, null, T, k)),
+       (K[22] = T),
+       (K[23] = k),
+       (K[24] = R));
+   else R = K[24];
+   let b;
+   if (K[25] !== q.status)
+     ((b =
+       q.status !== "running" &&
+       QY.default.createElement(
+         f,
+         { color: q.status === "completed" ? "success" : "error" },
+         q.status === "completed"
+           ? "Completed"
+           : q.status === "failed"
+             ? "Failed"
+             : "Killed",
+         " · ",
+       )),
+       (K[25] = q.status),
+       (K[26] = b));
+   else b = K[26];
+   let S;
+   if (K[27] !== j)
+     ((S =
+       j !== void 0 &&
+       j > 0 &&
+       QY.default.createElement(
+         QY.default.Fragment,
+         null,
+         " · ",
+         G3(j),
+         " tokens",
+       )),
+       (K[27] = j),
+       (K[28] = S));
+   else S = K[28];
+   let B;
+   if (K[29] !== P)
+     ((B =
+       P !== void 0 &&
+       P > 0 &&
+       QY.default.createElement(
+         QY.default.Fragment,
+         null,
+         " ",
+         "· ",
+         P,
+         " ",
+         P === 1 ? "tool" : "tools",
+       )),
+       (K[29] = P),
+       (K[30] = B));
+   else B = K[30];
+   let x;
+   if (K[31] !== $ || K[32] !== S || K[33] !== B)
+     ((x = QY.default.createElement(f, { dimColor: !0 }, $, S, B)),
+       (K[31] = $),
+       (K[32] = S),
+       (K[33] = B),
+       (K[34] = x));
+   else x = K[34];
+   let F;
+   if (K[35] !== b || K[36] !== x)
+     ((F = QY.default.createElement(I, null, b, x)),
+       (K[35] = b),
+       (K[36] = x),
+       (K[37] = F));
+   else F = K[37];
+   let Q;
+   if (K[38] !== q.progress || K[39] !== q.status || K[40] !== J)
+     ((Q =
+       q.status === "running" &&
+       q.progress?.recentActivities &&
+       q.progress.recentActivities.length > 0 &&
+       QY.default.createElement(
+         I,
+         { flexDirection: "column", marginTop: 1 },
+         QY.default.createElement(f, { bold: !0, dimColor: !0 }, "Progress"),
+         q.progress.recentActivities.map((HA, DA) =>
+           QY.default.createElement(
+             f,
+             {
+               key: DA,
+               dimColor: DA < q.progress.recentActivities.length - 1,
+               wrap: "truncate-end",
+             },
+             DA === q.progress.recentActivities.length - 1 ? "› " : "  ",
+             Jp2(HA, X, J),
+           ),
+         ),
+       )),
+       (K[38] = q.progress),
+       (K[39] = q.status),
+       (K[40] = J),
+       (K[41] = Q));
+   else Q = K[41];
+   let u;
+   if (K[42] === Symbol.for("react.memo_cache_sentinel"))
+     ((u = QY.default.createElement(f, { bold: !0, dimColor: !0 }, "Prompt")),
+       (K[42] = u));
+   else u = K[42];
+   let d;
+   if (K[43] !== V)
+     ((d = QY.default.createElement(
+       I,
+       { flexDirection: "column", marginTop: 1 },
+       u,
+       QY.default.createElement(f, { wrap: "wrap" }, V),
+     )),
+       (K[43] = V),
+       (K[44] = d));
+   else d = K[44];
+   let a;
+   if (K[45] !== q.error || K[46] !== q.status)
+     ((a =
+       q.status === "failed" &&
+       q.error &&
+       QY.default.createElement(
+         I,
+         { flexDirection: "column", marginTop: 1 },
+         QY.default.createElement(f, { bold: !0, color: "error" }, "Error"),
+         QY.default.createElement(f, { color: "error", wrap: "wrap" }, q.error),
+       )),
+       (K[45] = q.error),
+       (K[46] = q.status),
+       (K[47] = a));
+   else a = K[47];
+   let l;
+   if (K[48] !== Q || K[49] !== d || K[50] !== a)
+     ((l = QY.default.createElement(I, { flexDirection: "column" }, Q, d, a)),
+       (K[48] = Q),
+       (K[49] = d),
+       (K[50] = a),
+       (K[51] = l));
+   else l = K[51];
+   let e;
+   if (K[52] !== F || K[53] !== l || K[54] !== R)
+     ((e = QY.default.createElement(
+       I,
+       { width: "100%" },
+       QY.default.createElement(
+         I,
+         {
+           borderStyle: "round",
+           borderColor: "background",
+           flexDirection: "column",
+           marginTop: 1,
+           paddingLeft: 1,
+           paddingRight: 1,
+           width: "100%",
+         },
+         R,
+         F,
+         l,
+       ),
+     )),
+       (K[52] = F),
+       (K[53] = l),
+       (K[54] = R),
+       (K[55] = e));
+   else e = K[55];
+   let JA;
+   if (
+     K[56] !== W.keyName ||
+     K[57] !== W.pending ||
+     K[58] !== w ||
+     K[59] !== H ||
+     K[60] !== z ||
+     K[61] !== q.status
+   )
+     ((JA = QY.default.createElement(
+       I,
+       { marginLeft: 2 },
+       W.pending
+         ? QY.default.createElement(
+             f,
+             { dimColor: !0 },
+             "Press ",
+             W.keyName,
+             " again to exit",
+           )
+         : QY.default.createElement(
+             f,
+             { dimColor: !0 },
+             QY.default.createElement(
+               w8,
+               null,
+               w &&
+                 QY.default.createElement(M6, {
+                   shortcut: "←",
+                   action: "go back",
+                 }),
+               QY.default.createElement(M6, {
+                 shortcut: "Esc/Enter/Space",
+                 action: "close",
+               }),
+               q.status === "running" &&
+                 z &&
+                 QY.default.createElement(M6, { shortcut: "k", action: "kill" }),
+               q.status === "running" &&
+                 H &&
+                 QY.default.createElement(M6, {
+                   shortcut: "f",
+                   action: "foreground",
+                 }),
+             ),
+           ),
+     )),
+       (K[56] = W.keyName),
+       (K[57] = W.pending),
+       (K[58] = w),
+       (K[59] = H),
+       (K[60] = z),
+       (K[61] = q.status),
+       (K[62] = JA));
+   else JA = K[62];
+   let OA;
+   if (K[63] !== e || K[64] !== JA)
+     ((OA = QY.default.createElement(
+       I,
+       { width: "100%", flexDirection: "column" },
+       e,
+       JA,
+     )),
+       (K[63] = e),
+       (K[64] = JA),
+       (K[65] = OA));
+   else OA = K[65];
+   return OA;
+ }

+++ Added VjK (pretty-v2.1.20.js:510906-511033)
+ function VjK(A) {
+   let K = s(44),
+     { task: q, maxActivityWidth: Y } = A,
+     z = Y ?? 40;
+   switch (q.type) {
+     case "local_bash": {
+       let w;
+       if (K[0] !== z || K[1] !== q.command)
+         ((w = o9(q.command, z, !0)),
+           (K[0] = z),
+           (K[1] = q.command),
+           (K[2] = w));
+       else w = K[2];
+       let H;
+       if (K[3] !== q)
+         ((H = C_.createElement(jjK, { shell: q })), (K[3] = q), (K[4] = H));
+       else H = K[4];
+       let J;
+       if (K[5] !== w || K[6] !== H)
+         ((J = C_.createElement(f, null, w, " ", H)),
+           (K[5] = w),
+           (K[6] = H),
+           (K[7] = J));
+       else J = K[7];
+       return J;
+     }
+     case "remote_agent": {
+       let w;
+       if (K[8] !== z || K[9] !== q.title)
+         ((w = o9(q.title, z, !0)), (K[8] = z), (K[9] = q.title), (K[10] = w));
+       else w = K[10];
+       let H;
+       if (K[11] !== q)
+         ((H = C_.createElement(Yv1, { session: q })), (K[11] = q), (K[12] = H));
+       else H = K[12];
+       let J;
+       if (K[13] !== w || K[14] !== H)
+         ((J = C_.createElement(f, null, w, " ", H)),
+           (K[13] = w),
+           (K[14] = H),
+           (K[15] = J));
+       else J = K[15];
+       return J;
+     }
+     case "local_agent": {
+       let w;
+       if (K[16] !== z || K[17] !== q.description)
+         ((w = o9(q.description, z, !0)),
+           (K[16] = z),
+           (K[17] = q.description),
+           (K[18] = w));
+       else w = K[18];
+       let H = q.status === "completed" ? "done" : void 0,
+         J = q.status === "completed" && !q.notified ? ", unread" : void 0,
+         O;
+       if (K[19] !== H || K[20] !== J || K[21] !== q.status)
+         ((O = C_.createElement(xPA, { status: q.status, label: H, suffix: J })),
+           (K[19] = H),
+           (K[20] = J),
+           (K[21] = q.status),
+           (K[22] = O));
+       else O = K[22];
+       let X;
+       if (K[23] !== w || K[24] !== O)
+         ((X = C_.createElement(f, null, w, " ", O)),
+           (K[23] = w),
+           (K[24] = O),
+           (K[25] = X));
+       else X = K[25];
+       return X;
+     }
+     case "in_process_teammate": {
+       let w;
+       if (
+         K[26] !== q.awaitingPlanApproval ||
+         K[27] !== q.isIdle ||
+         K[28] !== q.progress ||
+         K[29] !== q.shutdownRequested
+       )
+         ((w = q.shutdownRequested
+           ? "stopping"
+           : q.awaitingPlanApproval
+             ? "awaiting approval"
+             : q.isIdle
+               ? "idle"
+               : ((q.progress?.recentActivities &&
+                   vGA(q.progress.recentActivities)) ??
+                 q.progress?.lastActivity?.activityDescription ??
+                 "working")),
+           (K[26] = q.awaitingPlanApproval),
+           (K[27] = q.isIdle),
+           (K[28] = q.progress),
+           (K[29] = q.shutdownRequested),
+           (K[30] = w));
+       else w = K[30];
+       let H = w,
+         J;
+       if (K[31] !== q.identity.color)
+         ((J = YL(q.identity.color)), (K[31] = q.identity.color), (K[32] = J));
+       else J = K[32];
+       let O;
+       if (K[33] !== J || K[34] !== q.identity.agentName)
+         ((O = C_.createElement(f, { color: J }, "@", q.identity.agentName)),
+           (K[33] = J),
+           (K[34] = q.identity.agentName),
+           (K[35] = O));
+       else O = K[35];
+       let X;
+       if (K[36] !== H || K[37] !== z)
+         ((X = o9(H, z, !0)), (K[36] = H), (K[37] = z), (K[38] = X));
+       else X = K[38];
+       let $;
+       if (K[39] !== X)
+         (($ = C_.createElement(f, { dimColor: !0 }, ": ", X)),
+           (K[39] = X),
+           (K[40] = $));
+       else $ = K[40];
+       let _;
+       if (K[41] !== O || K[42] !== $)
+         ((_ = C_.createElement(f, null, O, $)),
+           (K[41] = O),
+           (K[42] = $),
+           (K[43] = _));
+       else _ = K[43];
+       return _;
+     }
+   }
+ }

+++ Added _dA (pretty-v2.1.20.js:511571-511608)
+ function _dA(A) {
+   let K = s(10),
+     { item: q, isSelected: Y } = A,
+     { columns: z } = V8(),
+     w = Math.max(30, z - 26),
+     H = Y ? K1.pointer + " " : "  ",
+     J = Y ? "suggestion" : void 0,
+     O;
+   if (K[0] !== q.task || K[1] !== q.type || K[2] !== w)
+     ((O =
+       q.type === "leader"
+         ? bK.default.createElement(f, null, "@", T2)
+         : bK.default.createElement(VjK, { task: q.task, maxActivityWidth: w })),
+       (K[0] = q.task),
+       (K[1] = q.type),
+       (K[2] = w),
+       (K[3] = O));
+   else O = K[3];
+   let X;
+   if (K[4] !== J || K[5] !== O)
+     ((X = bK.default.createElement(f, { color: J }, O)),
+       (K[4] = J),
+       (K[5] = O),
+       (K[6] = X));
+   else X = K[6];
+   let $;
+   if (K[7] !== H || K[8] !== X)
+     (($ = bK.default.createElement(
+       I,
+       { flexDirection: "row" },
+       bK.default.createElement(f, null, H, X),
+     )),
+       (K[7] = H),
+       (K[8] = X),
+       (K[9] = $));
+   else $ = K[9];
+   return $;
+ }

+++ Added xjK (pretty-v2.1.20.js:512101-512103)
+ function xjK() {
+   return pd;
+ }

+++ Added fp2 (pretty-v2.1.20.js:512104-512106)
+ function fp2() {
+   return Vp2;
+ }

+++ Added ujK (pretty-v2.1.20.js:512107-512109)
+ function ujK() {
+   return `thinkback@${xjK()}`;
+ }

+++ Added Tc2 (pretty-v2.1.20.js:521584-521586)
+ function Tc2(A, K) {
+   return Pq.createElement(f, { key: K, dimColor: !0 }, A);
+ }

+++ Added HF6 (pretty-v2.1.20.js:521788-521937)
+ function HF6(A) {
+   let K = s(31),
+     { depCheck: q } = A,
+     Y;
+   if (K[0] !== q.errors)
+     ((Y = q.errors.some(Ec2)), (K[0] = q.errors), (K[1] = Y));
+   else Y = K[1];
+   let z = Y,
+     w;
+   if (K[2] !== q.errors)
+     ((w = q.errors.some(vc2)), (K[2] = q.errors), (K[3] = w));
+   else w = K[3];
+   let H = w,
+     J = q.warnings.length > 0,
+     O,
+     X;
+   if (K[4] !== z)
+     ((O = fX.default.createElement(
+       f,
+       null,
+       "bubblewrap (bwrap):",
+       " ",
+       z
+         ? fX.default.createElement(f, { color: "error" }, "not installed")
+         : fX.default.createElement(f, { color: "success" }, "installed"),
+     )),
+       (X =
+         z &&
+         fX.default.createElement(
+           f,
+           { dimColor: !0 },
+           "  ",
+           "· apt install bubblewrap",
+         )),
+       (K[4] = z),
+       (K[5] = O),
+       (K[6] = X));
+   else ((O = K[5]), (X = K[6]));
+   let $;
+   if (K[7] !== O || K[8] !== X)
+     (($ = fX.default.createElement(I, { flexDirection: "column" }, O, X)),
+       (K[7] = O),
+       (K[8] = X),
+       (K[9] = $));
+   else $ = K[9];
+   let _, Z;
+   if (K[10] !== H)
+     ((_ = fX.default.createElement(
+       f,
+       null,
+       "socat:",
+       " ",
+       H
+         ? fX.default.createElement(f, { color: "error" }, "not installed")
+         : fX.default.createElement(f, { color: "success" }, "installed"),
+     )),
+       (Z =
+         H &&
+         fX.default.createElement(
+           f,
+           { dimColor: !0 },
+           "  ",
+           "· apt install socat",
+         )),
+       (K[10] = H),
+       (K[11] = _),
+       (K[12] = Z));
+   else ((_ = K[11]), (Z = K[12]));
+   let G;
+   if (K[13] !== _ || K[14] !== Z)
+     ((G = fX.default.createElement(I, { flexDirection: "column" }, _, Z)),
+       (K[13] = _),
+       (K[14] = Z),
+       (K[15] = G));
+   else G = K[15];
+   let W, D;
+   if (K[16] !== J)
+     ((D = J
+       ? fX.default.createElement(f, { color: "warning" }, "not installed")
+       : fX.default.createElement(f, { color: "success" }, "installed")),
+       (W =
+         J &&
+         fX.default.createElement(
+           f,
+           { dimColor: !0 },
+           " (required to block unix domain sockets)",
+         )),
+       (K[16] = J),
+       (K[17] = W),
+       (K[18] = D));
+   else ((W = K[17]), (D = K[18]));
+   let M;
+   if (K[19] !== W || K[20] !== D)
+     ((M = fX.default.createElement(f, null, "seccomp filter:", " ", D, W)),
+       (K[19] = W),
+       (K[20] = D),
+       (K[21] = M));
+   else M = K[21];
+   let j;
+   if (K[22] !== J)
+     ((j =
+       J &&
+       fX.default.createElement(
+         I,
+         { flexDirection: "column" },
+         fX.default.createElement(
+           f,
+           { dimColor: !0 },
+           "  ",
+           "· npm install -g @anthropic-ai/sandbox-runtime",
+         ),
+         fX.default.createElement(
+           f,
+           { dimColor: !0 },
+           "  ",
+           "· or copy vendor/seccomp/* from sandbox-runtime and set",
+         ),
+         fX.default.createElement(
+           f,
+           { dimColor: !0 },
+           "    ",
+           "sandbox.seccomp.bpfPath and applyPath in settings.json",
+         ),
+       )),
+       (K[22] = J),
+       (K[23] = j));
+   else j = K[23];
+   let P;
+   if (K[24] !== M || K[25] !== j)
+     ((P = fX.default.createElement(I, { flexDirection: "column" }, M, j)),
+       (K[24] = M),
+       (K[25] = j),
+       (K[26] = P));
+   else P = K[26];
+   let V;
+   if (K[27] !== P || K[28] !== $ || K[29] !== G)
+     ((V = fX.default.createElement(
+       I,
+       { flexDirection: "column", paddingY: 1, gap: 1 },
+       $,
+       G,
+       P,
+     )),
+       (K[27] = P),
+       (K[28] = $),
+       (K[29] = G),
+       (K[30] = V));
+   else V = K[30];
+   return V;
+ }

+++ Added JfK (pretty-v2.1.20.js:523636-523793)
+ class JfK {
+   clients = new Map();
+   tabRoutes = new Map();
+   context;
+   notificationHandler = null;
+   constructor(A) {
+     this.context = A;
+   }
+   setNotificationHandler(A) {
+     this.notificationHandler = A;
+     for (let K of this.clients.values()) K.setNotificationHandler(A);
+   }
+   async ensureConnected() {
+     let { logger: A, serverName: K } = this.context;
+     this.refreshClients();
+     let q = [];
+     for (let z of this.clients.values())
+       if (!z.isConnected()) q.push(z.ensureConnected().catch(() => !1));
+     if (q.length > 0) await Promise.all(q);
+     let Y = this.getConnectedClients().length;
+     if (Y === 0) return (A.info(`[${K}] No connected sockets in pool`), !1);
+     return (A.info(`[${K}] Socket pool: ${Y} connected`), !0);
+   }
+   async callTool(A, K) {
+     if (A === "tabs_context_mcp") return this.callTabsContext(K);
+     let q = K.tabId;
+     if (q !== void 0) {
+       let z = this.tabRoutes.get(q);
+       if (z) {
+         let w = this.clients.get(z);
+         if (w?.isConnected()) return w.callTool(A, K);
+       }
+     }
+     let Y = this.getConnectedClients();
+     if (Y.length === 0)
+       throw new nS(
+         `[${this.context.serverName}] No connected sockets available`,
+       );
+     return Y[0].callTool(A, K);
+   }
+   isConnected() {
+     return this.getConnectedClients().length > 0;
+   }
+   disconnect() {
+     for (let A of this.clients.values()) A.disconnect();
+     (this.clients.clear(), this.tabRoutes.clear());
+   }
+   getConnectedClients() {
+     return [...this.clients.values()].filter((A) => A.isConnected());
+   }
+   async callTabsContext(A) {
+     let { logger: K, serverName: q } = this.context,
+       Y = this.getConnectedClients();
+     if (Y.length === 0) throw new nS(`[${q}] No connected sockets available`);
+     if (Y.length === 1) {
+       let H = await Y[0].callTool("tabs_context_mcp", A);
+       return (this.updateTabRoutes(H, this.getSocketPathForClient(Y[0])), H);
+     }
+     let z = await Promise.allSettled(
+         Y.map(async (H) => {
+           let J = await H.callTool("tabs_context_mcp", A),
+             O = this.getSocketPathForClient(H);
+           return { result: J, socketPath: O };
+         }),
+       ),
+       w = [];
+     this.tabRoutes.clear();
+     for (let H of z) {
+       if (H.status !== "fulfilled") {
+         K.info(`[${q}] tabs_context_mcp failed on one socket: ${H.reason}`);
+         continue;
+       }
+       let { result: J, socketPath: O } = H.value;
+       this.updateTabRoutes(J, O);
+       let X = this.extractTabs(J);
+       if (X) w.push(...X);
+     }
+     if (w.length > 0) {
+       let H = w.map((J) => {
+         let O = J;
+         return `  • tabId ${O.tabId}: "${O.title}" (${O.url})`;
+       }).join(`
+ `);
+       return {
+         result: {
+           content: [
+             { type: "text", text: JSON.stringify({ availableTabs: w }) },
+             {
+               type: "text",
+               text: `
+ 
+ Tab Context:
+ - Available tabs:
+ ${H}`,
+             },
+           ],
+         },
+       };
+     }
+     for (let H of z) if (H.status === "fulfilled") return H.value.result;
+     throw new nS(`[${q}] All sockets failed for tabs_context_mcp`);
+   }
+   updateTabRoutes(A, K) {
+     let q = this.extractTabs(A);
+     if (!q) return;
+     for (let Y of q)
+       if (typeof Y === "object" && Y !== null && "tabId" in Y) {
+         let z = Y.tabId;
+         this.tabRoutes.set(z, K);
+       }
+   }
+   extractTabs(A) {
+     if (!A || typeof A !== "object") return null;
+     let q = A.result?.content;
+     if (!q || !Array.isArray(q)) return null;
+     for (let Y of q)
+       if (Y.type === "text" && Y.text)
+         try {
+           let z = JSON.parse(Y.text);
+           if (Array.isArray(z)) return z;
+           if (z && Array.isArray(z.availableTabs)) return z.availableTabs;
+         } catch {}
+     return null;
+   }
+   getSocketPathForClient(A) {
+     for (let [K, q] of this.clients.entries()) if (q === A) return K;
+     return "";
+   }
+   refreshClients() {
+     let A = this.getAvailableSocketPaths(),
+       { logger: K, serverName: q } = this.context;
+     for (let Y of A)
+       if (!this.clients.has(Y)) {
+         K.info(`[${q}] Adding socket to pool: ${Y}`);
+         let z = {
+             ...this.context,
+             socketPath: Y,
+             getSocketPath: void 0,
+             getSocketPaths: void 0,
+           },
+           w = Vv1(z);
+         if (((w.disableAutoReconnect = !0), this.notificationHandler))
+           w.setNotificationHandler(this.notificationHandler);
+         this.clients.set(Y, w);
+       }
+     for (let [Y, z] of this.clients.entries())
+       if (!A.includes(Y)) {
+         (K.info(`[${q}] Removing stale socket from pool: ${Y}`),
+           z.disconnect(),
+           this.clients.delete(Y));
+         for (let [w, H] of this.tabRoutes.entries())
+           if (H === Y) this.tabRoutes.delete(w);
+       }
+   }
+   getAvailableSocketPaths() {
+     return this.context.getSocketPaths?.() ?? [];
+   }
+ }

+++ Added OfK (pretty-v2.1.20.js:523794-523796)
+ function OfK(A) {
+   return new JfK(A);
+ }

+++ Added WfK (pretty-v2.1.20.js:524005-524050)
+ var WfK = `# Claude in Chrome browser automation
+ 
+ You have access to browser automation tools (mcp__claude-in-chrome__*) for interacting with web pages in Chrome. Follow these guidelines for effective browser automation.
+ 
+ ## GIF recording
+ 
+ When performing multi-step browser interactions that the user may want to review or share, use mcp__claude-in-chrome__gif_creator to record them.
+ 
+ You must ALWAYS:
+ * Capture extra frames before and after taking actions to ensure smooth playback
+ * Name the file meaningfully to help the user identify it later (e.g., "login_process.gif")
+ 
+ ## Console log debugging
+ 
+ You can use mcp__claude-in-chrome__read_console_messages to read console output. Console output may be verbose. If you are looking for specific log entries, use the 'pattern' parameter with a regex-compatible pattern. This filters results efficiently and avoids overwhelming output. For example, use pattern: "[MyApp]" to filter for application-specific logs rather than reading all console output.
+ 
+ ## Alerts and dialogs
+ 
+ IMPORTANT: Do not trigger JavaScript alerts, confirms, prompts, or browser modal dialogs through your actions. These browser dialogs block all further browser events and will prevent the extension from receiving any subsequent commands. Instead, when possible, use console.log for debugging and then use the mcp__claude-in-chrome__read_console_messages tool to read those log messages. If a page has dialog-triggering elements:
+ 1. Avoid clicking buttons or links that may trigger alerts (e.g., "Delete" buttons with confirmation dialogs)
+ 2. If you must interact with such elements, warn the user first that this may interrupt the session
+ 3. Use mcp__claude-in-chrome__javascript_tool to check for and dismiss any existing dialogs before proceeding
+ 
+ If you accidentally trigger a dialog and lose responsiveness, inform the user they need to manually dismiss it in the browser.
+ 
+ ## Avoid rabbit holes and loops
+ 
+ When using browser automation tools, stay focused on the specific task. If you encounter any of the following, stop and ask the user for guidance:
+ - Unexpected complexity or tangential browser exploration
+ - Browser tool calls failing or returning errors after 2-3 attempts
+ - No response from the browser extension
+ - Page elements not responding to clicks or input
+ - Pages not loading or timing out
+ - Unable to complete the browser task despite multiple approaches
+ 
+ Explain what you attempted, what went wrong, and ask how the user would like to proceed. Do not keep retrying the same failing browser action or explore unrelated pages without checking in first.
+ 
+ ## Tab context and session startup
+ 
+ IMPORTANT: At the start of each browser automation session, call mcp__claude-in-chrome__tabs_context_mcp first to get information about the user's current browser tabs. Use this context to understand what the user might want to work with before creating new tabs.
+ 
+ Never reuse tab IDs from a previous/other session. Follow these guidelines:
+ 1. Only reuse an existing tab if the user explicitly asks to work with it
+ 2. Otherwise, create a new tab with mcp__claude-in-chrome__tabs_create_mcp
+ 3. If a tool returns an error indicating the tab doesn't exist or is invalid, call tabs_context_mcp to get fresh tab IDs
+ 4. When a tab is closed by the user or a navigation error occurs, call tabs_context_mcp to see what tabs are available`,

+++ Added DfK (pretty-v2.1.20.js:524051-524059)
+   DfK = `**IMPORTANT: Before using any chrome browser tools, you MUST first load them using ToolSearch.**
+ 
+ Chrome browser tools are MCP tools that require loading before use. Before calling any mcp__claude-in-chrome__* tool:
+ 1. Use ToolSearch with \`select:mcp__claude-in-chrome__<tool_name>\` to load the specific tool
+ 2. Then call the tool
+ 
+ For example, to get tab context:
+ 1. First: ToolSearch with query "select:mcp__claude-in-chrome__tabs_context_mcp"
+ 2. Then: Call mcp__claude-in-chrome__tabs_context_mcp`,

+++ Added ZF6 (pretty-v2.1.20.js:524060-524061)
+   ZF6 =
+     '**Browser Automation**: Chrome browser tools are available via the "claude-in-chrome" skill. CRITICAL: Before using any mcp__claude-in-chrome__* tools, invoke the skill by calling the Skill tool with skill: "claude-in-chrome". The skill provides browser automation instructions and enables the tools.';

+++ Added Iv1 (pretty-v2.1.20.js:526441-526441)
+ var Iv1 = 1,

+++ Added Qi2 (pretty-v2.1.20.js:529217-529227)
+ function Qi2(A) {
+   return `
+ You are an interactive CLI tool that helps users ${A !== null ? 'according to your "Output Style" below, which describes how you should respond to user queries.' : "with software engineering tasks."} Use the instructions below and the tools available to you to assist the user.
+ 
+ ${gNK}.
+ IMPORTANT: You must NEVER generate or guess URLs for the user unless you are confident that the URLs are for helping the user with programming. You may use URLs provided by the user in their messages or local files.
+ 
+ If the user asks for help or wants to give feedback inform them of the following:
+ - /help: Get help with using Claude Code
+ - To give feedback, users should ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.ISSUES_EXPLAINER}`;
+ }

+++ Added Ui2 (pretty-v2.1.20.js:529228-529242)
+ function Ui2(A) {
+   if (A !== null) return null;
+   return `# Tone and style
+ - Only use emojis if the user explicitly requests it. Avoid using emojis in all communication unless asked.
+ - Your output will be displayed on a command line interface. Your responses should be short and concise. You can use Github-flavored markdown for formatting, and will be rendered in a monospace font using the CommonMark specification.
+ - Output text to communicate with the user; all text you output outside of tool use is displayed to the user. Only use tools to complete tasks. Never use tools like ${k7} or code comments as means to communicate with the user during the session.
+ - NEVER create files unless they're absolutely necessary for achieving your goal. ALWAYS prefer editing an existing file to creating a new one. This includes markdown files.
+ - Do not use a colon before tool calls. Your tool calls may not be shown directly in the output, so text like "Let me read the file:" followed by a read tool call should just be "Let me read the file." with a period.
+ 
+ # Professional objectivity
+ Prioritize technical accuracy and truthfulness over validating the user's beliefs. Focus on facts and problem-solving, providing direct, objective technical info without any unnecessary superlatives, praise, or emotional validation. It is best for the user if Claude honestly applies the same rigorous standards to all ideas and disagrees when necessary, even if it may not be what the user wants to hear. Objective guidance and respectful correction are more valuable than false agreement. Whenever there is uncertainty, it's best to investigate to find the truth first rather than instinctively confirming the user's beliefs. Avoid using over-the-top validation or excessive praise when responding to users such as "You're absolutely right" or similar phrases.
+ 
+ # No time estimates
+ Never give time estimates or predictions for how long tasks will take, whether for your own work or for users planning their projects. Avoid phrases like "this will take me a few minutes," "should be done in about 5 minutes," "this is a quick fix," "this will take 2-3 weeks," or "we can do this later." Focus on what needs to be done, not how long it might take. Break work into actionable steps and let users judge timing for themselves.`;
+ }

+++ Added di2 (pretty-v2.1.20.js:529291-529296)
+ function di2(A) {
+   if (!A.has(xJ)) return null;
+   return `# Asking questions as you work
+ 
+ You have access to the ${xJ} tool to ask the user questions when you need clarification, want to validate assumptions, or need to make a decision you're unsure about. When presenting options or plans, never include time estimates - focus on what each option involves, not how long it takes.`;
+ }

+++ Added ci2 (pretty-v2.1.20.js:529297-529299)
+ function ci2() {
+   return "Users may configure 'hooks', shell commands that execute in response to events like tool calls, in settings. Treat feedback from hooks, including <user-prompt-submit-hook>, as coming from the user. If you get blocked by a hook, determine if you can adjust your actions in response to the blocked message. If not, ask the user to check their hooks configuration.";
+ }

+++ Added ii2 (pretty-v2.1.20.js:529328-529331)
+ function ii2() {
+   return `- Tool results and user messages may include <system-reminder> tags. <system-reminder> tags contain useful information and reminders. They are automatically added by the system, and bear no direct relation to the specific tool results or user messages in which they appear.
+ - The conversation has unlimited context through automatic summarization.`;
+ }

+++ Added ri2 (pretty-v2.1.20.js:529361-529364)
+ function ri2(A) {
+   if (!A.has(UO.name)) return null;
+   return `IMPORTANT: Always use the ${UO.name} tool to plan and track tasks throughout the conversation.`;
+ }

+++ Added oi2 (pretty-v2.1.20.js:529365-529374)
+ function oi2() {
+   return `# Code References
+ 
+ When referencing specific functions or pieces of code include the pattern \`file_path:line_number\` to allow the user to easily navigate to the source code location.
+ 
+ <example>
+ user: Where are errors from the client handled?
+ assistant: Clients are marked as failed in the \`connectToServer\` function in src/services/process.ts:712.
+ </example>`;
+ }

+++ Added ai2 (pretty-v2.1.20.js:529375-529377)
+ function ai2() {
+   return null;
+ }

+++ Added si2 (pretty-v2.1.20.js:529378-529380)
+ function si2() {
+   return null;
+ }

+++ Added ti2 (pretty-v2.1.20.js:529381-529385)
+ function ti2(A) {
+   if (!A) return null;
+   return `# Language
+ Always respond in ${A}. Use ${A} for all explanations, comments, and communications with the user. Technical terms and code identifiers should remain in their original form.`;
+ }

+++ Added ei2 (pretty-v2.1.20.js:529386-529390)
+ function ei2(A) {
+   if (A === null) return null;
+   return `# Output Style: ${A.name}
+ ${A.prompt}`;
+ }

+++ Added An2 (pretty-v2.1.20.js:529391-529394)
+ function An2(A) {
+   if (!A || A.length === 0) return null;
+   return Kn2(A);
+ }

+++ Added qn2 (pretty-v2.1.20.js:529590-529600)
+ function qn2(A) {
+   if (A.includes("claude-opus-4-5")) return "May 2025";
+   else if (A.includes("claude-haiku-4")) return "February 2025";
+   else if (
+     A.includes("claude-opus-4") ||
+     A.includes("claude-sonnet-4-5") ||
+     A.includes("claude-sonnet-4")
+   )
+     return "January 2025";
+   return null;
+ }

+++ Added gNK (pretty-v2.1.20.js:529641-529642)
+ var gNK =
+     "IMPORTANT: Assist with defensive security tasks only. Refuse to create, modify, or improve code that may be used maliciously. Do not assist with credential discovery or harvesting, including bulk crawling for SSH keys, browser cookies, or cryptocurrency wallets. Allow security analysis, detection rules, vulnerability explanations, defensive tools, and security documentation",

+++ Added tNK (pretty-v2.1.20.js:531400-531430)
+ function tNK(A) {
+   return {
+     type: "custom",
+     name: A.toolName,
+     description: A.description,
+     input_schema: {
+       type: "object",
+       properties: {
+         [A.primaryField.name]: {
+           type: "boolean",
+           description: A.primaryField.description,
+         },
+         matchedDescription: {
+           type: "string",
+           description:
+             "The rule or category that matched, if any. Set when the primary condition is true.",
+         },
+         confidence: {
+           type: "string",
+           enum: ["high", "medium", "low"],
+           description: "Confidence level of the classification",
+         },
+         reason: {
+           type: "string",
+           description: "Brief explanation of the classification decision",
+         },
+       },
+       required: [A.primaryField.name, "confidence", "reason"],
+     },
+   };
+ }

+++ Added eNK (pretty-v2.1.20.js:531432-531446)
+ var eNK = C(() => {
+   G7();
+   ((WY0 = U.object({
+     matches: U.boolean(),
+     matchedDescription: U.string().optional(),
+     confidence: U.enum(["high", "medium", "low"]),
+     reason: U.string(),
+   })),
+     (In2 = U.object({
+       shouldBlock: U.boolean(),
+       matchedDescription: U.string().optional(),
+       confidence: U.enum(["high", "medium", "low"]),
+       reason: U.string(),
+     })));
+ });

+++ Added Sn2 (pretty-v2.1.20.js:531447-531447)
+ var Sn2 = "classify_result",

+++ Added ATK (pretty-v2.1.20.js:531449-531467)
+ var ATK = C(() => {
+   P8();
+   Aw();
+   H7();
+   B1();
+   D1();
+   eNK();
+   r6();
+   LY0 = tNK({
+     toolName: Sn2,
+     description:
+       "Report the security classification result for the agent action",
+     primaryField: {
+       name: "shouldBlock",
+       description:
+         "Whether the action should be blocked (true) or allowed (false)",
+     },
+   });
+ });

+++ Added eF6 (pretty-v2.1.20.js:533153-533162)
+ async function eF6() {
+   if (process.env.CLAUDE_CODE_OAUTH_TOKEN || Qv1()) return lK();
+   try {
+     let q = (await Wf().readAsync())?.claudeAiOauth;
+     if (!q?.accessToken) return null;
+     return q;
+   } catch (A) {
+     return (qA(A), null);
+   }
+ }

+++ Added Rj (pretty-v2.1.20.js:533163-533174)
+ function Rj(A = 0, K = !1) {
+   if (A === 0 && !K) {
+     if (SdA) return SdA;
+     return (
+       (SdA = AQ6(A, K).finally(() => {
+         SdA = null;
+       })),
+       SdA
+     );
+   }
+   return AQ6(A, K);
+ }

+++ Added oy6 (pretty-v2.1.20.js:534403-534452)
+ function oy6(A, K) {
+   if (UTK(A))
+     return {
+       behavior: "allow",
+       updatedInput: K,
+       decisionReason: {
+         type: "other",
+         reason: "Plan files for current session are allowed for writing",
+       },
+     };
+   if (dTK(A))
+     return {
+       behavior: "allow",
+       updatedInput: K,
+       decisionReason: {
+         type: "other",
+         reason: "Scratchpad files for current session are allowed for writing",
+       },
+     };
+   if (B$6(A))
+     return {
+       behavior: "allow",
+       updatedInput: K,
+       decisionReason: {
+         type: "other",
+         reason: "Agent memory files are allowed for writing",
+       },
+     };
+   let q = Qv(M8(), "teams") + IL;
+   if (A === q.slice(0, -1) || A.startsWith(q))
+     return {
+       behavior: "allow",
+       updatedInput: K,
+       decisionReason: {
+         type: "other",
+         reason: "Team files are allowed for writing",
+       },
+     };
+   let Y = Qv(M8(), "tasks") + IL;
+   if (A === Y.slice(0, -1) || A.startsWith(Y))
+     return {
+       behavior: "allow",
+       updatedInput: K,
+       decisionReason: {
+         type: "other",
+         reason: "Task files are allowed for writing",
+       },
+     };
+   return { behavior: "passthrough", message: "" };
+ }

+++ Added sTK (pretty-v2.1.20.js:535068-535082)
+ function sTK(A) {
+   let K = uA(),
+     q = gdA(A),
+     Y = WQ6(A);
+   try {
+     let z = K.readdirStringSync(q)
+       .filter((H) => H.startsWith(`${Y}.backup.`))
+       .sort()
+       .reverse();
+     if (z.length > 0) return jm(q, z[0]);
+     let w = `${A}.backup`;
+     if (K.existsSync(w)) return w;
+   } catch {}
+   return null;
+ }

+++ Added pvK (pretty-v2.1.20.js:537363-537363)
+ var pvK = {};

+++ Added cvK (pretty-v2.1.20.js:537892-537892)
+ var cvK = {};

+++ Added ovK (pretty-v2.1.20.js:537936-537977)
+ async function ovK() {
+   try {
+     if (!_a2())
+       return (
+         L8("info", "settings_sync_download_skipped"),
+         n("tengu_settings_sync_download_skipped", {}),
+         !1
+       );
+     L8("info", "settings_sync_download_starting");
+     let A = await Da2();
+     if (!A.success)
+       return (
+         L8("warn", "settings_sync_download_fetch_failed"),
+         n("tengu_settings_sync_download_fetch_failed", {}),
+         !1
+       );
+     if (A.isEmpty)
+       return (
+         L8("info", "settings_sync_download_empty"),
+         n("tengu_settings_sync_download_empty", {}),
+         !1
+       );
+     let K = A.data.content.entries,
+       q = await dnA();
+     return (
+       L8("info", "settings_sync_download_applying", {
+         entryCount: Object.keys(K).length,
+       }),
+       Ma2(K, q),
+       n("tengu_settings_sync_download_success", {
+         entryCount: Object.keys(K).length,
+       }),
+       !0
+     );
+   } catch {
+     return (
+       L8("error", "settings_sync_download_error"),
+       n("tengu_settings_sync_download_error", {}),
+       !1
+     );
+   }
+ }

+++ Added ka2 (pretty-v2.1.20.js:538430-538437)
+ function ka2(A) {
+   return (
+     KVA.add(A),
+     () => {
+       KVA.delete(A);
+     }
+   );
+ }

+++ Added fEK (pretty-v2.1.20.js:539020-539041)
+ async function fEK(A, K, q, Y) {
+   let z = { messages: 0, errors: 0 },
+     w;
+   try {
+     w = await Y.readdir(A);
+   } catch (J) {
+     if (J instanceof Error && "code" in J && J.code === "ENOENT") return z;
+     throw J;
+   }
+   let H = w.filter((J) => J.isFile() && J.name.endsWith(q));
+   for (let J of H)
+     try {
+       let O = NP(A, J.name);
+       if ((await Y.stat(O)).mtime < K) (await Y.unlink(O), z.messages++);
+     } catch {
+       z.errors++;
+     }
+   try {
+     await Y.rmdir(A);
+   } catch {}
+   return z;
+ }

+++ Added iQ6 (pretty-v2.1.20.js:539354-539364)
+ var iQ6 = C(() => {
+   D1();
+   R1();
+   i6();
+   gG();
+   Z0();
+   fPA();
+   F4A();
+   Y6();
+   ED();
+ });

+++ Added bEK (pretty-v2.1.20.js:539953-540094)
+ var bEK = C(() => {
+   G7();
+   ((rQ6 = [
+     "Global",
+     "Chat",
+     "Autocomplete",
+     "Confirmation",
+     "Help",
+     "Transcript",
+     "HistorySearch",
+     "Task",
+     "ThemePicker",
+     "Settings",
+     "Tabs",
+     "Attachments",
+     "Footer",
+     "MessageSelector",
+     "DiffDialog",
+     "ModelPicker",
+     "Select",
+     "Plugin",
+   ]),
+     (hEK = {
+       Global: "Active everywhere, regardless of focus",
+       Chat: "When the chat input is focused",
+       Autocomplete: "When autocomplete menu is visible",
+       Confirmation: "When a confirmation/permission dialog is shown",
+       Help: "When the help overlay is open",
+       Transcript: "When viewing the transcript",
+       HistorySearch: "When searching command history (ctrl+r)",
+       Task: "When a task/agent is running in the foreground",
+       ThemePicker: "When the theme picker is open",
+       Settings: "When the settings menu is open",
+       Tabs: "When tab navigation is active",
+       Attachments: "When the attachment bar is focused",
+       Footer: "When footer indicators are focused",
+       MessageSelector: "When the message selector (rewind) is open",
+       DiffDialog: "When the diff dialog is open",
+       ModelPicker: "When the model picker is open",
+       Select: "When a select/list component is focused",
+       Plugin: "When the plugin dialog is open",
+     }),
+     (oQ6 = [
+       "app:interrupt",
+       "app:exit",
+       "app:toggleTodos",
+       "app:toggleTranscript",
+       "app:toggleTeammatePreview",
+       "history:search",
+       "history:previous",
+       "history:next",
+       "chat:cancel",
+       "chat:cycleMode",
+       "chat:modelPicker",
+       "chat:thinkingToggle",
+       "chat:submit",
+       "chat:undo",
+       "chat:externalEditor",
+       "chat:stash",
+       "chat:imagePaste",
+       "autocomplete:accept",
+       "autocomplete:dismiss",
+       "autocomplete:previous",
+       "autocomplete:next",
+       "confirm:yes",
+       "confirm:no",
+       "confirm:previous",
+       "confirm:next",
+       "confirm:nextField",
+       "confirm:previousField",
+       "confirm:cycleMode",
+       "confirm:toggleExplanation",
+       "tabs:next",
+       "tabs:previous",
+       "transcript:toggleShowAll",
+       "transcript:exit",
+       "historySearch:next",
+       "historySearch:accept",
+       "historySearch:cancel",
+       "historySearch:execute",
+       "task:background",
+       "theme:toggleSyntaxHighlighting",
+       "help:dismiss",
+       "attachments:next",
+       "attachments:previous",
+       "attachments:remove",
+       "attachments:exit",
+       "footer:next",
+       "footer:previous",
+       "footer:openSelected",
+       "footer:clearSelection",
+       "messageSelector:up",
+       "messageSelector:down",
+       "messageSelector:top",
+       "messageSelector:bottom",
+       "messageSelector:select",
+       "diff:dismiss",
+       "diff:previousSource",
+       "diff:nextSource",
+       "diff:back",
+       "diff:viewDetails",
+       "diff:previousFile",
+       "diff:nextFile",
+       "modelPicker:decreaseEffort",
+       "modelPicker:increaseEffort",
+       "select:next",
+       "select:previous",
+       "select:accept",
+       "select:cancel",
+       "plugin:toggle",
+       "plugin:install",
+       "permission:toggleDebug",
+       "settings:search",
+       "settings:retry",
+     ]),
+     (Zs2 = U.object({
+       context: U.enum(rQ6).describe(
+         "UI context where these bindings apply. Global bindings work everywhere.",
+       ),
+       bindings: U.record(
+         U.string().describe('Keystroke pattern (e.g., "ctrl+k", "shift+tab")'),
+         U.union([
+           U.enum(oQ6),
+           U.string()
+             .regex(/^command:[a-zA-Z0-9:\-_]+$/)
+             .describe(
+               'Command binding (e.g., "command:help", "command:compact"). Executes the slash command as if typed.',
+             ),
+           U.null().describe("Set to null to unbind a default shortcut"),
+         ]).describe("Action to trigger, command to invoke, or null to unbind"),
+       ).describe("Map of keystroke patterns to actions"),
+     }).describe("A block of keybindings for a specific context")),
+     (M$0 = U.object({
+       $schema: U.string()
+         .optional()
+         .describe("JSON Schema URL for editor validation"),
+       $docs: U.string().optional().describe("Documentation URL"),
+       bindings: U.array(Zs2).describe("Array of keybinding blocks by context"),
+     }).describe(
+       "Claude Code keybindings configuration. Customize keyboard shortcuts by context.",
+     )));
+ });

+++ Added Gs2 (pretty-v2.1.20.js:540095-540100)
+ function Gs2() {
+   return aQ6(
+     ["Context", "Description"],
+     rQ6.map((A) => [`\`${A}\``, hEK[A]]),
+   );
+ }

+++ Added Ws2 (pretty-v2.1.20.js:540101-540118)
+ function Ws2() {
+   let A = {};
+   for (let K of sOA)
+     for (let [q, Y] of Object.entries(K.bindings))
+       if (Y) {
+         if (!A[Y]) A[Y] = { keys: [], context: K.context };
+         A[Y].keys.push(q);
+       }
+   return aQ6(
+     ["Action", "Default Key(s)", "Context"],
+     oQ6.map((K) => {
+       let q = A[K],
+         Y = q ? q.keys.map((w) => `\`${w}\``).join(", ") : "(none)",
+         z = q ? q.context : Ds2(K);
+       return [`\`${K}\``, Y, z];
+     }),
+   );
+ }

+++ Added Ds2 (pretty-v2.1.20.js:540119-540143)
+ function Ds2(A) {
+   let K = A.split(":")[0];
+   return (
+     {
+       app: "Global",
+       history: "Global or Chat",
+       chat: "Chat",
+       autocomplete: "Autocomplete",
+       confirm: "Confirmation",
+       tabs: "Tabs",
+       transcript: "Transcript",
+       historySearch: "HistorySearch",
+       task: "Task",
+       theme: "ThemePicker",
+       help: "Help",
+       attachments: "Attachments",
+       footer: "Footer",
+       messageSelector: "MessageSelector",
+       diff: "DiffDialog",
+       modelPicker: "ModelPicker",
+       select: "Select",
+       permission: "Confirmation",
+     }[K ?? ""] ?? "Unknown"
+   );
+ }

+++ Added Ms2 (pretty-v2.1.20.js:540144-540157)
+ function Ms2() {
+   let A = [];
+   A.push("### Non-rebindable (errors)");
+   for (let K of WyA) A.push(`- \`${K.key}\` — ${K.reason}`);
+   (A.push(""), A.push("### Terminal reserved (errors/warnings)"));
+   for (let K of jK6)
+     A.push(
+       `- \`${K.key}\` — ${K.reason} (${K.severity === "error" ? "will not work" : "may conflict"})`,
+     );
+   (A.push(""), A.push("### macOS reserved (errors)"));
+   for (let K of PK6) A.push(`- \`${K.key}\` — ${K.reason}`);
+   return A.join(`
+ `);
+ }

+++ Added xEK (pretty-v2.1.20.js:540158-540203)
+ function xEK() {
+   RL({
+     name: "keybindings-help",
+     description:
+       'Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: "rebind ctrl+s", "add a chord shortcut", "change the submit key", "customize keybindings".',
+     allowedTools: ["Read"],
+     userInvocable: !1,
+     isEnabled: Lk,
+     async getPromptForCommand(A) {
+       let K = Gs2(),
+         q = Ws2(),
+         Y = Ms2(),
+         z = [
+           Ns2,
+           Ts2,
+           vs2,
+           Es2,
+           ks2,
+           Cs2,
+           Ls2,
+           Rs2,
+           `## Reserved Shortcuts
+ 
+ ${Y}`,
+           `## Available Contexts
+ 
+ ${K}`,
+           `## Available Actions
+ 
+ ${q}`,
+         ];
+       if (A)
+         z.push(`## User Request
+ 
+ ${A}`);
+       return [
+         {
+           type: "text",
+           text: z.join(`
+ 
+ `),
+         },
+       ];
+     },
+   });
+ }

+++ Added aQ6 (pretty-v2.1.20.js:540204-540212)
+ function aQ6(A, K) {
+   let q = A.map(() => "---");
+   return [
+     `| ${A.join(" | ")} |`,
+     `| ${q.join(" | ")} |`,
+     ...K.map((Y) => `| ${Y.join(" | ")} |`),
+   ].join(`
+ `);
+ }

+++ Added uEK (pretty-v2.1.20.js:540214-540381)
+ var uEK = C(() => {
+   Pe();
+   bEK();
+   T51();
+   v51();
+   t8A();
+   B1();
+   ((js2 = {
+     $schema:
+       "https://platform.claude.com/docs/schemas/claude-code/keybindings.json",
+     $docs: "https://code.claude.com/docs/en/keybindings",
+     bindings: [
+       { context: "Chat", bindings: { "ctrl+e": "chat:externalEditor" } },
+     ],
+   }),
+     (Ps2 = { context: "Chat", bindings: { "ctrl+s": null } }),
+     (Vs2 = {
+       context: "Chat",
+       bindings: { "ctrl+g": null, "ctrl+e": "chat:externalEditor" },
+     }),
+     (fs2 = {
+       context: "Global",
+       bindings: { "ctrl+k ctrl+t": "app:toggleTodos" },
+     }),
+     (Ns2 = [
+       "# Keybindings Skill",
+       "",
+       "Create or modify `~/.claude/keybindings.json` to customize keyboard shortcuts.",
+       "",
+       "## CRITICAL: Read Before Write",
+       "",
+       "**Always read `~/.claude/keybindings.json` first** (it may not exist yet). Merge changes with existing bindings — never replace the entire file.",
+       "",
+       "- Use **Edit** tool for modifications to existing files",
+       "- Use **Write** tool only if the file does not exist yet",
+     ].join(`
+ `)),
+     (Ts2 = [
+       "## File Format",
+       "",
+       "```json",
+       QA(js2, null, 2),
+       "```",
+       "",
+       "Always include the `$schema` and `$docs` fields.",
+     ].join(`
+ `)),
+     (vs2 = [
+       "## Keystroke Syntax",
+       "",
+       "**Modifiers** (combine with `+`):",
+       "- `ctrl` (alias: `control`)",
+       "- `alt` (aliases: `opt`, `option`) — note: `alt` and `meta` are identical in terminals",
+       "- `shift`",
+       "- `meta` (aliases: `cmd`, `command`)",
+       "",
+       "**Special keys**: `escape`/`esc`, `enter`/`return`, `tab`, `space`, `backspace`, `delete`, `up`, `down`, `left`, `right`",
+       "",
+       "**Chords**: Space-separated keystrokes, e.g. `ctrl+k ctrl+s` (1-second timeout between keystrokes)",
+       "",
+       "**Examples**: `ctrl+shift+p`, `alt+enter`, `ctrl+k ctrl+n`",
+     ].join(`
+ `)),
+     (Es2 = [
+       "## Unbinding Default Shortcuts",
+       "",
+       "Set a key to `null` to remove its default binding:",
+       "",
+       "```json",
+       QA(Ps2, null, 2),
+       "```",
+     ].join(`
+ `)),
+     (ks2 = [
+       "## How User Bindings Interact with Defaults",
+       "",
+       "- User bindings are **additive** — they are appended after the default bindings",
+       "- To **move** a binding to a different key: unbind the old key (`null`) AND add the new binding",
+       "- A context only needs to appear in the user's file if they want to change something in that context",
+     ].join(`
+ `)),
+     (Cs2 = [
+       "## Common Patterns",
+       "",
+       "### Rebind a key",
+       "To change the external editor shortcut from `ctrl+g` to `ctrl+e`:",
+       "```json",
+       QA(Vs2, null, 2),
+       "```",
+       "",
+       "### Add a chord binding",
+       "```json",
+       QA(fs2, null, 2),
+       "```",
+     ].join(`
+ `)),
+     (Ls2 = [
+       "## Behavioral Rules",
+       "",
+       "1. Only include contexts the user wants to change (minimal overrides)",
+       "2. Validate that actions and contexts are from the known lists below",
+       "3. Warn the user proactively if they choose a key that conflicts with reserved shortcuts or common tools like tmux (`ctrl+b`) and screen (`ctrl+a`)",
+       "4. When adding a new binding for an existing action, the new binding is additive (existing default still works unless explicitly unbound)",
+       "5. To fully replace a default binding, unbind the old key AND add the new one",
+     ].join(`
+ `)),
+     (Rs2 = [
+       "## Validation with /doctor",
+       "",
+       'The `/doctor` command includes a "Keybinding Configuration Issues" section that validates `~/.claude/keybindings.json`.',
+       "",
+       "### Common Issues and Fixes",
+       "",
+       aQ6(
+         ["Issue", "Cause", "Fix"],
+         [
+           [
+             '`keybindings.json must have a "bindings" array`',
+             "Missing wrapper object",
+             'Wrap bindings in `{ "bindings": [...] }`',
+           ],
+           [
+             '`"bindings" must be an array`',
+             "`bindings` is not an array",
+             'Set `"bindings"` to an array: `[{ context: ..., bindings: ... }]`',
+           ],
+           [
+             '`Unknown context "X"`',
+             "Typo or invalid context name",
+             "Use exact context names from the Available Contexts table",
+           ],
+           [
+             '`Duplicate key "X" in Y bindings`',
+             "Same key defined twice in one context",
+             "Remove the duplicate; JSON uses only the last value",
+           ],
+           [
+             '`"X" may not work: ...`',
+             "Key conflicts with terminal/OS reserved shortcut",
+             "Choose a different key (see Reserved Shortcuts section)",
+           ],
+           [
+             '`Could not parse keystroke "X"`',
+             "Invalid key syntax",
+             "Check syntax: use `+` between modifiers, valid key names",
+           ],
+           [
+             '`Invalid action for "X"`',
+             "Action value is not a string or null",
+             'Actions must be strings like `"app:help"` or `null` to unbind',
+           ],
+         ],
+       ),
+       "",
+       "### Example /doctor Output",
+       "",
+       "```",
+       "Keybinding Configuration Issues",
+       "Location: ~/.claude/keybindings.json",
+       '  └ [Error] Unknown context "chat"',
+       "    → Valid contexts: Global, Chat, Autocomplete, ...",
+       '  └ [Warning] "ctrl+c" may not work: Terminal interrupt (SIGINT)',
+       "```",
+       "",
+       "**Errors** prevent bindings from working and must be fixed. **Warnings** indicate potential conflicts but the binding may still work.",
+     ].join(`
+ `)));
+ });

+++ Added ys2 (pretty-v2.1.20.js:540391-540634)
+ var ys2 = `The skill enables you to be a verification specialist for Claude Code. Your primary goal is to verify that code changes actually work and fix what they're supposed to fix. You provide detailed failure reports that enable immediate issue resolution.
+ 
+ ## Your Mission
+ 
+ **Main Goal: Verify functionality works correctly.** You will be given information about what needs to be verified. Your job is to:
+ 1. Understand what was changed (from the prompt or by checking git)
+ 2. Discover available verifier skills in the project
+ 3. Create a verification plan and write it to a plan file
+ 4. Trigger the appropriate verifier skill(s) to execute the plan — multiple verifiers may run if changes span different areas
+ 5. Report results
+ 
+ If a previous verification plan exists and the changes/objective are the same, pass the plan in your prompt to reuse it.
+ 
+ ## Phase 1: Discover Verifier Skills
+ 
+ Check your available skills (listed in the Skill tool's "Available skills" section) for any with "verifier" in the name (case-insensitive). These are your verifier skills (e.g., \`verifier-playwright\`, \`my-verifier\`, \`unit-test-verifier\`). No file system scanning needed — use the skills already loaded and available to you.
+ 
+ ### How to Choose a Verifier
+ 
+ 1. Run \`git status\` or use provided context to identify changed files
+ 2. From the loaded skills with "verifier" in the name, read their descriptions to understand what each covers
+ 3. Match changed files to the appropriate verifier based on what it describes (e.g., a playwright verifier for UI files, an API verifier for backend files)
+ 
+ **If no verifier skills are found:**
+ - Suggest running \`/init-verifiers\` to create one
+ - Do not proceed with verification until a verifier skill is configured
+ 
+ ## Phase 2: Analyze Changes
+ 
+ If no context is provided, check git:
+ - Run \`git status\` to see modified files
+ - Run \`git diff\` to see the actual changes
+ - Infer what functionality needs verification
+ 
+ ## Phase 3: Choose Verifier(s)
+ 
+ Based on the changed files and available verifiers:
+ 1. Match each file to the most appropriate verifier based on the verifier's description
+ 2. If multiple verifiers could apply, choose based on change type:
+    - UI changes → prefer playwright/e2e verifiers
+    - API changes → prefer http/api verifiers
+    - CLI changes → prefer cli/tmux verifiers
+ 3. Group files by verifier for batch execution
+ 
+ ## Phase 4: Generate Verification Plan
+ 
+ **If a plan was passed in your prompt**, compare its "Files Being Verified" and "Change Summary" against the current git diff. If they still match, reuse the plan as-is (skip to Phase 5). If the changes have diverged, create a fresh plan below.
+ 
+ **If no plan was provided**, create a structured, deterministic plan that can be executed exactly.
+ 
+ Write the plan to a plan file:
+ - Plans are stored in \`~/.claude/plans/<slug>.md\`
+ - Use the Write tool to create the plan file
+ - Include the verifier skill to use in the metadata
+ 
+ ### Plan Format
+ 
+ \`\`\`markdown
+ # Verification Plan
+ 
+ ## Metadata
+ - **Verifier Skills**: <list of verifier skills to use>
+ - **Project Type**: <e.g., React web app, Express API, CLI tool, Python library>
+ - **Created**: <timestamp>
+ - **Change Summary**: <brief description>
+ 
+ ## Files Being Verified
+ <Map each changed file to the appropriate verifier. In multi-project repos, verifiers are named verifier-<project>-<type>.>
+ 
+ Example (single project):
+ - src/components/Button.tsx → verifier-playwright
+ - src/pages/Home.tsx → verifier-playwright
+ 
+ Example (multi-project):
+ - frontend/src/components/Button.tsx → verifier-frontend-playwright
+ - backend/src/routes/users.ts → verifier-backend-api
+ 
+ ## Preconditions
+ - <any setup requirements>
+ 
+ ## Setup Steps
+ 1. **<description>**
+    - Command: \`<command>\`
+    - Wait for: "<text indicating ready>"
+    - Timeout: <ms>
+ 
+ ## Verification Steps
+ 
+ ### Step 1: <description>
+ - **Action**: <action type>
+ - **Details**: <specifics>
+ - **Expected**: <what success looks like>
+ - **Success Criteria**: <how to determine pass/fail>
+ 
+ ### Step 2: ...
+ 
+ ## Cleanup Steps
+ 1. <cleanup actions>
+ 
+ ## Success Criteria
+ - All verification steps pass
+ - <additional criteria>
+ 
+ ## Execution Rules
+ 
+ **CRITICAL: Execute the plan EXACTLY as written.**
+ 
+ You MUST:
+ 1. Read this verification plan in full before starting
+ 2. Execute each step in order
+ 3. Report PASS or FAIL for each step
+ 4. Stop immediately on first FAIL
+ 
+ You MUST NOT:
+ - Skip steps
+ - Modify steps
+ - Add steps not in the plan
+ - Interpret ambiguous instructions (mark as FAIL instead)
+ - Round up "almost working" to "working"
+ 
+ ## Reporting Format
+ 
+ Report results inline in your response:
+ 
+ ### Verification Results
+ 
+ #### Step 1: <description> - PASS/FAIL
+ Command: \`<command>\`
+ Expected: <what was expected>
+ Actual: <what happened>
+ 
+ #### Step 2: ...
+ \`\`\`
+ 
+ ## Phase 5: Trigger Verifier Skill(s)
+ 
+ After writing the plan, trigger each applicable verifier. If files map to multiple verifiers, run them sequentially:
+ 
+ 1. For each verifier group (from Phase 3):
+    a. Use the Skill tool to invoke that verifier skill
+    b. Pass the plan file path and the subset of files in the prompt
+    c. Collect results before moving to the next verifier
+ 2. Aggregate results across all verifiers into a single report
+ 
+ Example (single project, single verifier):
+ \`\`\`
+ Use the Skill tool with:
+ - skill: "verifier-playwright"
+ - args: "Execute the verification plan at ~/.claude/plans/<slug>.md"
+ \`\`\`
+ 
+ Example (single project, multiple verifiers):
+ \`\`\`
+ # First: run playwright verifier for UI changes
+ Use the Skill tool with:
+ - skill: "verifier-playwright"
+ - args: "Execute the verification plan at ~/.claude/plans/<slug>.md for files: src/components/Button.tsx"
+ 
+ # Then: run API verifier for backend changes
+ Use the Skill tool with:
+ - skill: "verifier-api"
+ - args: "Execute the verification plan at ~/.claude/plans/<slug>.md for files: src/routes/users.ts"
+ \`\`\`
+ 
+ Example (multi-project repo):
+ \`\`\`
+ # Run frontend playwright verifier
+ Use the Skill tool with:
+ - skill: "verifier-frontend-playwright"
+ - args: "Execute the verification plan at ~/.claude/plans/<slug>.md for files: frontend/src/components/Button.tsx"
+ 
+ # Run backend API verifier
+ Use the Skill tool with:
+ - skill: "verifier-backend-api"
+ - args: "Execute the verification plan at ~/.claude/plans/<slug>.md for files: backend/src/routes/users.ts"
+ \`\`\`
+ 
+ ## Handling Different Scenarios
+ 
+ ### Scenario 1: Verifier Skills Exist
+ 1. Discover verifiers as described above
+ 2. Create plan and write to plan file (listing all applicable verifiers)
+ 3. Trigger each verifier skill sequentially with plan path and its file subset
+ 4. Aggregate results and report inline
+ 
+ ### Scenario 2: No Verifier Skills Found
+ 1. Inform the user: "No verifier skills found. Run \`/init-verifiers\` to create one."
+ 2. Do not proceed with verification until a verifier skill is configured.
+ 
+ ### Scenario 3: Pre-existing Plan Provided
+ 1. Parse the provided plan
+ 2. Compare the plan's "Files Being Verified" and "Change Summary" against the current git diff
+ 3. If the changes match (same files, same objective) → reuse the plan as-is
+ 4. If the changes are different (new files, different objective, or significant code differences) → create a fresh plan
+ 5. Write plan to plan file if not already there
+ 6. Trigger verifier skill
+ 
+ ## Reporting Results
+ 
+ Results are reported inline in the response (no separate file).
+ 
+ Report format:
+ \`\`\`
+ ## Verification Results
+ 
+ **Verifiers Used**: <list of verifiers triggered>
+ **Plan File**: ~/.claude/plans/<slug>.md
+ 
+ ### Summary
+ - Total Steps: X
+ - PASSED: Y
+ - FAILED: Z
+ 
+ ### <verifier-name> Results
+ (e.g., "verifier-playwright Results" or "verifier-frontend-playwright Results")
+ 
+ #### Step 1: <description> - PASS
+ - Command: \`<command>\`
+ - Expected: <expected>
+ - Actual: <actual>
+ 
+ #### Step 2: <description> - FAIL
+ - Command: \`<command>\`
+ - Expected: <expected>
+ - Actual: <actual>
+ - **Error**: <error details>
+ 
+ ### Overall: PASS/FAIL
+ 
+ ### Recommended Fixes (if any failures)
+ 1. <fix suggestion>
+ \`\`\`
+ 
+ ## Critical Guidelines
+ 
+ 1. **Discover verifiers first** - Always check for project-specific verifier skills
+ 2. **Require verifier skills** - Do not proceed without a configured verifier; suggest \`/init-verifiers\` if none found
+ 3. **Write plans to files** - Plans must be written to plan files so they can be re-executed
+ 4. **Delegate to verifiers** - Use the Skill tool to trigger verifier skills rather than executing directly; run multiple verifiers sequentially if changes span different areas
+ 5. **Report inline** - Results go in the response, not to a separate file
+ 6. **Match by description** - Choose the verifier whose description best matches the changed files
+ 7. **Focus on WHAT to verify, not HOW.** - Describe what was changed and the expected behavior.
+ 
+ `;

+++ Added UEK (pretty-v2.1.20.js:540641-540649)
+ var UEK = C(() => {
+   LEK();
+   yEK();
+   SEK();
+   uEK();
+   mEK();
+   FEK();
+   y9A();
+ });

+++ Added ft2 (pretty-v2.1.20.js:543953-543953)
+   ft2 = 1,

+++ Added xt2 (pretty-v2.1.20.js:544342-544580)
+ function xt2({
+   toolUseConfirm: A,
+   toolUseContext: K,
+   onDone: q,
+   onReject: Y,
+   verbose: z,
+   workerBadge: w,
+   command: H,
+   description: J,
+ }) {
+   let [O] = b4(),
+     [X, $] = k6(),
+     _ = hkK({
+       toolName: A.tool.name,
+       toolInput: A.input,
+       toolDescription: A.description,
+       messages: K.messages,
+     }),
+     [Z, G] = NX.useState(!1),
+     [W, D] = NX.useState(""),
+     [M, j] = NX.useState(""),
+     [P, V] = NX.useState(J || ""),
+     [N, T] = NX.useState(!J?.trim());
+   NX.useEffect(() => {
+     if (!UB()) return;
+     let YA = new AbortController();
+     return (
+       D7K(H, J, YA.signal)
+         .then((KA) => {
+           if (KA && !YA.signal.aborted) (V(KA), T(!1));
+         })
+         .catch(() => {}),
+       () => YA.abort()
+     );
+   }, [H, J]);
+   let [k, R] = NX.useState(!1),
+     [b, S] = NX.useState(!1),
+     [B, x] = NX.useState("yes"),
+     [F, Q] = NX.useState(!1),
+     [u, d] = NX.useState(!1),
+     a = NX.useRef(!1);
+   if (A.classifierCheckInProgress) a.current = !0;
+   let e = rp("requesting", "Attempting to auto-approve…", !0, !1),
+     JA = x8.isSandboxingEnabled(),
+     OA = JA && pMA(A.input),
+     HA = NX.useMemo(
+       () => ({ completion_type: "tool_use_single", language_name: "none" }),
+       [],
+     );
+   SL(A, HA);
+   let DA = NX.useMemo(
+       () => QMA(X.toolPermissionContext),
+       [X.toolPermissionContext],
+     ),
+     o = NX.useMemo(
+       () =>
+         NkK({
+           suggestions:
+             A.permissionResult.behavior === "ask"
+               ? A.permissionResult.suggestions
+               : void 0,
+           decisionReason: A.permissionResult.decisionReason,
+           onRejectFeedbackChange: D,
+           onAcceptFeedbackChange: j,
+           onClassifierDescriptionChange: V,
+           classifierDescription: P,
+           initialClassifierDescriptionEmpty: N,
+           existingAllowDescriptions: DA,
+           yesInputMode: k,
+           noInputMode: b,
+         }),
+       [A, P, N, DA, k, b],
+     ),
+     _A = NX.useCallback(() => {
+       G((YA) => !YA);
+     }, []);
+   s1("permission:toggleDebug", _A, { context: "Confirmation" });
+   function PA(YA) {
+     A.onUserInteraction();
+     let KA = { toolName: GK(A.tool.name), isMcp: A.tool.isMcp ?? !1 };
+     if (YA === "yes")
+       if (k) (R(!1), n("tengu_accept_feedback_mode_collapsed", KA));
+       else (R(!0), Q(!0), n("tengu_accept_feedback_mode_entered", KA));
+     else if (YA === "no")
+       if (b) (S(!1), n("tengu_reject_feedback_mode_collapsed", KA));
+       else (S(!0), d(!0), n("tengu_reject_feedback_mode_entered", KA));
+   }
+   function jA(YA) {
+     let KA = YA?.trim(),
+       zA = !!KA;
+     if (!zA)
+       (n("tengu_permission_request_escape", {}),
+         $((AA) => ({
+           ...AA,
+           attribution: {
+             ...AA.attribution,
+             escapeCount: AA.attribution.escapeCount + 1,
+           },
+         })));
+     if ((he("tool_use_single", A, "reject", zA), KA)) A.onReject(KA);
+     else A.onReject();
+     (Y(), q());
+   }
+   function yA(YA) {
+     n("tengu_permission_request_option_selected", {
+       option_index: { yes: 1, "yes-apply-suggestions": 2, no: 3 }[YA],
+     });
+     let zA = GK(A.tool.name);
+     switch (YA) {
+       case "yes": {
+         let AA = M.trim();
+         (he("tool_use_single", A, "accept"),
+           n("tengu_accept_submitted", {
+             toolName: zA,
+             isMcp: A.tool.isMcp ?? !1,
+             has_instructions: !!AA,
+             instructions_length: AA.length,
+             entered_feedback_mode: F,
+           }),
+           A.onAllow(A.input, [], AA || void 0),
+           q());
+         break;
+       }
+       case "yes-apply-suggestions": {
+         he("tool_use_single", A, "accept");
+         let AA =
+           "suggestions" in A.permissionResult
+             ? A.permissionResult.suggestions || []
+             : [];
+         (A.onAllow(A.input, AA), q());
+         break;
+       }
+       case "no": {
+         let AA = W.trim();
+         (n("tengu_reject_submitted", {
+           toolName: zA,
+           isMcp: A.tool.isMcp ?? !1,
+           has_instructions: !!AA,
+           instructions_length: AA.length,
+           entered_feedback_mode: u,
+         }),
+           jA(AA || void 0));
+         break;
+       }
+     }
+   }
+   return C0.default.createElement(
+     Iw,
+     {
+       workerBadge: w,
+       title: JA && !OA ? "Bash command (unsandboxed)" : "Bash command",
+       subtitle: void 0,
+     },
+     C0.default.createElement(
+       I,
+       { flexDirection: "column", paddingX: 2, paddingY: 1 },
+       C0.default.createElement(
+         f,
+         { dimColor: _.visible },
+         a7.renderToolUseMessage(
+           { command: H, description: J },
+           { theme: O, verbose: !0 },
+         ),
+       ),
+       !_.visible &&
+         C0.default.createElement(f, { dimColor: !0 }, A.description),
+       C0.default.createElement(bkK, { visible: _.visible, promise: _.promise }),
+     ),
+     Z
+       ? C0.default.createElement(
+           C0.default.Fragment,
+           null,
+           C0.default.createElement(EkK, {
+             permissionResult: A.permissionResult,
+             toolName: "Bash",
+           }),
+           A.toolUseContext.options.debug &&
+             C0.default.createElement(
+               I,
+               { justifyContent: "flex-end", marginTop: 1 },
+               C0.default.createElement(
+                 f,
+                 { dimColor: !0 },
+                 "Ctrl-D to hide debug info",
+               ),
+             ),
+         )
+       : C0.default.createElement(
+           C0.default.Fragment,
+           null,
+           C0.default.createElement(
+             I,
+             { flexDirection: "column" },
+             C0.default.createElement(YN, {
+               permissionResult: A.permissionResult,
+               toolType: "command",
+             }),
+             C0.default.createElement(
+               f,
+               { dimColor: A.classifierAutoApproved },
+               "Do you want to proceed?",
+             ),
+             C0.default.createElement(y6, {
+               options: A.classifierAutoApproved
+                 ? o.map((YA) => ({ ...YA, disabled: !0 }))
+                 : o,
+               isDisabled: A.classifierAutoApproved,
+               inlineDescriptions: !0,
+               onChange: yA,
+               onCancel: () => jA(),
+               onFocus: (YA) => {
+                 if (YA !== B) A.onUserInteraction();
+                 if (YA !== "yes" && k && !M.trim()) R(!1);
+                 if (YA !== "no" && b && !W.trim()) S(!1);
+                 x(YA);
+               },
+               onInputModeToggle: PA,
+             }),
+           ),
+           C0.default.createElement(
+             I,
+             { justifyContent: "space-between", marginTop: 1 },
+             C0.default.createElement(
+               f,
+               { dimColor: !0 },
+               "Esc to cancel",
+               ((B === "yes" && !k) || (B === "no" && !b)) && " · Tab to amend",
+               _.enabled && ` · ctrl+e to ${_.visible ? "hide" : "explain"}`,
+             ),
+             A.toolUseContext.options.debug &&
+               C0.default.createElement(
+                 f,
+                 { dimColor: !0 },
+                 "Ctrl+d to show debug info",
+               ),
+           ),
+         ),
+   );
+ }

+++ Added HLK (pretty-v2.1.20.js:550840-550840)
+   HLK = 0,

+++ Added pU6 (pretty-v2.1.20.js:552733-552736)
+ var pU6 = C(() => {
+   S9();
+   j2();
+ });

+++ Added JAz (pretty-v2.1.20.js:552880-552900)
+ function JAz(A) {
+   let K = A.length;
+   if (A.every((Y) => Y.type === A[0].type))
+     switch (A[0].type) {
+       case "local_bash":
+         return K === 1 ? "1 bash" : `${K} bashes`;
+       case "in_process_teammate": {
+         let Y = new Set(
+           A.map((z) =>
+             z.type === "in_process_teammate" ? z.identity.teamName : "",
+           ),
+         ).size;
+         return Y === 1 ? "1 team" : `${Y} teams`;
+       }
+       case "local_agent":
+         return K === 1 ? "1 local agent" : `${K} local agents`;
+       case "remote_agent":
+         return K === 1 ? "1 remote session" : `${K} remote sessions`;
+     }
+   return `${K} background ${K === 1 ? "task" : "tasks"}`;
+ }

+++ Added jAz (pretty-v2.1.20.js:553116-553126)
+ function jAz(A, K) {
+   if (A) return "draft";
+   switch (K) {
+     case "APPROVED":
+       return "approved";
+     case "CHANGES_REQUESTED":
+       return "changes_requested";
+     default:
+       return "pending";
+   }
+ }

+++ Added rLK (pretty-v2.1.20.js:553127-553145)
+ async function rLK() {
+   if (!(await aW())) return null;
+   let { stdout: K, code: q } = await u6(
+     "gh",
+     ["pr", "view", "--json", "number,url,reviewDecision,isDraft"],
+     { timeout: MAz, preserveOutputOnError: !1 },
+   );
+   if (q !== 0 || !K.trim()) return null;
+   try {
+     let Y = G6(K);
+     return {
+       number: Y.number,
+       url: Y.url,
+       reviewState: jAz(Y.isDraft, Y.reviewDecision),
+     };
+   } catch {
+     return null;
+   }
+ }

+++ Added aLK (pretty-v2.1.20.js:553152-553187)
+ function aLK() {
+   let [, A] = k6(),
+     K = MVA.useRef(null),
+     q = MVA.useCallback(async () => {
+       let Y = await rLK();
+       A((z) => {
+         let w = Y?.number ?? null,
+           H = Y?.reviewState ?? null;
+         if (z.prStatus.number === w && z.prStatus.reviewState === H) return z;
+         return {
+           ...z,
+           prStatus: {
+             number: w,
+             url: Y?.url ?? null,
+             reviewState: H,
+             lastUpdated: Date.now(),
+           },
+         };
+       });
+     }, [A]);
+   MVA.useEffect(() => {
+     let Y = !1;
+     async function z() {
+       let w = Date.now();
+       if ((await q(), Date.now() - w > VAz)) return;
+       if (!Y) K.current = setTimeout(() => void z(), PAz);
+     }
+     return (
+       z(),
+       () => {
+         if (((Y = !0), K.current))
+           (clearTimeout(K.current), (K.current = null));
+       }
+     );
+   }, [q]);
+ }

+++ Added VAz (pretty-v2.1.20.js:553190-553190)
+   VAz = 4000;

+++ Added TAz (pretty-v2.1.20.js:553588-553599)
+ function TAz(A) {
+   switch (A) {
+     case "approved":
+       return "success";
+     case "changes_requested":
+       return "error";
+     case "pending":
+       return "warning";
+     case "draft":
+       return;
+   }
+ }

+++ Added vAz (pretty-v2.1.20.js:553600-553602)
+ function vAz() {
+   return (aLK(), null);
+ }

+++ Added eLK (pretty-v2.1.20.js:553603-553605)
+ function eLK() {
+   return i4("tengu_pr_status_cli", !1) && (P1().prStatusFooterEnabled ?? !0);
+ }

+++ Added lRK (pretty-v2.1.20.js:556225-556225)
+   lRK = 2,

+++ Added G1z (pretty-v2.1.20.js:556473-556473)
+   G1z = 2;

+++ Added x1z (pretty-v2.1.20.js:558952-558952)
+   x1z = 60000;

+++ Added IyK (pretty-v2.1.20.js:558980-558982)
+ function IyK() {
+   return PVA.useContext(yyK);
+ }

+++ Added Ap6 (pretty-v2.1.20.js:558984-558987)
+ var Ap6 = C(() => {
+   cA();
+   ((PVA = r(XA(), 1)), (yyK = PVA.createContext(void 0)));
+ });

+++ Added zIK (pretty-v2.1.20.js:560338-560380)
+ function zIK({
+   isLoading: A,
+   queuedCommandsLength: K,
+   lastQueryCompletionTime: q,
+   getAppState: Y,
+   setAppState: z,
+   executeQueuedInput: w,
+   hasActiveLocalJsxUI: H,
+   setIsLoading: J,
+ }) {
+   let O = n9A.useRef(!1),
+     X = n9A.useSyncExternalStore(LW7, RW7);
+   (n9A.useEffect(() => {
+     if (A) return;
+     if (!yW7()) return;
+     if (H) return;
+     if (O.current) return;
+     let $ = SW7();
+     if (!$) return;
+     ((O.current = !0),
+       J(!0),
+       w($, {})
+         .catch(() => {})
+         .finally(() => {
+           ((O.current = !1), IW7());
+         }));
+   }, [X, A, H, w, J]),
+     n9A.useEffect(() => {
+       if (A) return;
+       if (K === 0) return;
+       if (H) return;
+       if (O.current) return;
+       ((O.current = !0),
+         J(!0),
+         qIK({ getAppState: Y, setAppState: z, executeInput: w })
+           .then(($) => {
+             if (!$.processed) J(!1);
+           })
+           .finally(() => {
+             O.current = !1;
+           }));
+     }, [A, K, q, Y, z, w, H, J]));
+ }

+++ Added VIK (pretty-v2.1.20.js:560707-560709)
+ function VIK(A) {
+   return;
+ }

+++ Added Y6z (pretty-v2.1.20.js:561700-561700)
+   Y6z = 3000,

+++ Added Ue (pretty-v2.1.20.js:562962-562964)
+ function Ue() {
+   return R6z;
+ }

+++ Added NVA (pretty-v2.1.20.js:562982-562985)
+ var NVA = C(() => {
+   vcA();
+   nv();
+ });

+++ Added Ep6 (pretty-v2.1.20.js:563095-563098)
+ var Ep6 = C(() => {
+   vp6();
+   nv();
+ });

+++ Added wBK (pretty-v2.1.20.js:564433-564433)
+ var wBK = () => {};

+++ Added p8z (pretty-v2.1.20.js:566223-566263)
+ function p8z(A) {
+   let K = s(4),
+     { showAllInTranscript: q } = A,
+     Y = FK("app:toggleTranscript", "Global", "ctrl+o"),
+     z = FK("transcript:toggleShowAll", "Transcript", "ctrl+e"),
+     w = q ? "collapse" : "show all",
+     H;
+   if (K[0] !== z || K[1] !== w || K[2] !== Y)
+     ((H = T4.createElement(
+       I,
+       {
+         alignItems: "center",
+         alignSelf: "center",
+         borderTopDimColor: !0,
+         borderBottom: !1,
+         borderLeft: !1,
+         borderRight: !1,
+         borderStyle: "single",
+         marginTop: 1,
+         paddingLeft: 2,
+         width: "100%",
+       },
+       T4.createElement(
+         f,
+         { dimColor: !0 },
+         "Showing detailed transcript · ",
+         Y,
+         " to toggle ·",
+         " ",
+         z,
+         " to ",
+         w,
+       ),
+     )),
+       (K[0] = z),
+       (K[1] = w),
+       (K[2] = Y),
+       (K[3] = H));
+   else H = K[3];
+   return H;
+ }

+++ Added PmK (pretty-v2.1.20.js:568201-568203)
+ var PmK = C(() => {
+   BA();
+ });

+++ Added omK (pretty-v2.1.20.js:570179-570417)
+ function omK(A) {
+   let K = s(34),
+     { onDone: q, commands: Y } = A,
+     z;
+   if (K[0] === Symbol.for("react.memo_cache_sentinel"))
+     ((z = AX("project")), (K[0] = z));
+   else z = K[0];
+   let { servers: w } = z,
+     H;
+   if (K[1] === Symbol.for("react.memo_cache_sentinel"))
+     ((H = Object.keys(w)), (K[1] = H));
+   else H = K[1];
+   let J = H.length > 0,
+     O;
+   if (K[2] === Symbol.for("react.memo_cache_sentinel"))
+     ((O = UmK()), (K[2] = O));
+   else O = K[2];
+   let $ = O.length > 0,
+     _;
+   if (K[3] === Symbol.for("react.memo_cache_sentinel"))
+     ((_ = pmK()), (K[3] = _));
+   else _ = K[3];
+   let Z = _,
+     G;
+   if (K[4] === Symbol.for("react.memo_cache_sentinel"))
+     ((G = cmK()), (K[4] = G));
+   else G = K[4];
+   let D = G.length > 0,
+     M;
+   if (K[5] === Symbol.for("react.memo_cache_sentinel"))
+     ((M = lmK()), (K[5] = M));
+   else M = K[5];
+   let P = M.length > 0,
+     V;
+   if (K[6] === Symbol.for("react.memo_cache_sentinel"))
+     ((V = dmK()), (K[6] = V));
+   else V = K[6];
+   let T = V.length > 0,
+     k;
+   if (K[7] === Symbol.for("react.memo_cache_sentinel"))
+     ((k = imK()), (K[7] = k));
+   else k = K[7];
+   let b = k.length > 0,
+     S,
+     B,
+     x;
+   if (K[8] !== Y) {
+     let yA = Y?.some(G4z) ?? !1,
+       bA = Y?.some(_4z) ?? !1;
+     ((S = Z.length > 0 || yA || bA),
+       (B = Mw($ || S || D || P || T || b)),
+       (x = [
+         {
+           name: "MCP servers",
+           shouldShowWarning: () => J,
+           onChange: () => {
+             let KA = {
+               enabledMcpjsonServers: Object.keys(w),
+               enableAllProjectMcpServers: !0,
+             };
+             h4("localSettings", KA);
+           },
+         },
+         { name: "hooks", shouldShowWarning: () => $ },
+         { name: "bash commands", shouldShowWarning: () => S },
+         {
+           name: "OpenTelemetry headers helper commands",
+           shouldShowWarning: () => T,
+         },
+         { name: "dangerous environment variables", shouldShowWarning: () => b },
+       ].filter($4z)),
+       (K[8] = Y),
+       (K[9] = S),
+       (K[10] = B),
+       (K[11] = x));
+   } else ((S = K[9]), (B = K[10]), (x = K[11]));
+   let F = x,
+     Q,
+     u;
+   if (K[12] !== S)
+     ((Q = () => {
+       let yA = rmK() === u1();
+       n("tengu_trust_dialog_shown", {
+         isHomeDir: yA,
+         hasMcpServers: J,
+         hasHooks: $,
+         hasBashExecution: S,
+         hasApiKeyHelper: D,
+         hasAwsCommands: P,
+         hasOtelHeadersHelper: T,
+         hasDangerousEnvVars: b,
+       });
+     }),
+       (u = [J, $, S, D, P, T, b]),
+       (K[12] = S),
+       (K[13] = Q),
+       (K[14] = u));
+   else ((Q = K[13]), (u = K[14]));
+   kP.default.useEffect(Q, u);
+   let d;
+   if (K[15] !== F || K[16] !== S || K[17] !== q)
+     ((d = function (bA) {
+       if (bA === "exit") {
+         H5(1);
+         return;
+       }
+       let YA = rmK() === u1();
+       if (
+         (n("tengu_trust_dialog_accept", {
+           isHomeDir: YA,
+           hasMcpServers: J,
+           hasHooks: $,
+           hasBashExecution: S,
+           hasApiKeyHelper: D,
+           hasAwsCommands: P,
+           hasOtelHeadersHelper: T,
+           hasDangerousEnvVars: b,
+           enableMcp: !0,
+         }),
+         YA)
+       )
+         Yn6(!0);
+       else Tz(X4z);
+       (F.forEach(O4z), q());
+     }),
+       (K[15] = F),
+       (K[16] = S),
+       (K[17] = q),
+       (K[18] = d));
+   else d = K[18];
+   let a = d,
+     l = k8(),
+     e;
+   if (K[19] === Symbol.for("react.memo_cache_sentinel"))
+     ((e = { context: "Confirmation" }), (K[19] = e));
+   else e = K[19];
+   if ((s1("confirm:no", J4z, e), B)) return (setTimeout(q), null);
+   let JA, OA, HA;
+   if (K[20] === Symbol.for("react.memo_cache_sentinel"))
+     ((JA = kP.default.createElement(f, { bold: !0 }, uA().cwd())),
+       (OA = kP.default.createElement(
+         f,
+         null,
+         "Quick safety check: Is this a project you created or one you trust? (Like your own code, a well-known open source project, or work from your team). If not, take a moment to review what",
+         "'",
+         "s in this folder first.",
+       )),
+       (HA = kP.default.createElement(
+         f,
+         null,
+         "Claude Code",
+         "'",
+         "ll be able to read, edit, and execute files here.",
+       )),
+       (K[20] = JA),
+       (K[21] = OA),
+       (K[22] = HA));
+   else ((JA = K[20]), (OA = K[21]), (HA = K[22]));
+   let DA;
+   if (K[23] === Symbol.for("react.memo_cache_sentinel"))
+     ((DA = kP.default.createElement(
+       f,
+       { dimColor: !0 },
+       kP.default.createElement(
+         D7,
+         { url: "https://code.claude.com/docs/en/security" },
+         "Security guide",
+       ),
+     )),
+       (K[23] = DA));
+   else DA = K[23];
+   let o;
+   if (K[24] === Symbol.for("react.memo_cache_sentinel"))
+     ((o = [
+       { label: "Yes, I trust this folder", value: "enable_all" },
+       { label: "No, exit", value: "exit" },
+     ]),
+       (K[24] = o));
+   else o = K[24];
+   let _A;
+   if (K[25] !== a)
+     ((_A = kP.default.createElement(y6, {
+       options: o,
+       onChange: (yA) => a(yA),
+       onCancel: () => a("exit"),
+     })),
+       (K[25] = a),
+       (K[26] = _A));
+   else _A = K[26];
+   let PA;
+   if (K[27] !== l.keyName || K[28] !== l.pending)
+     ((PA = kP.default.createElement(
+       f,
+       { dimColor: !0 },
+       l.pending
+         ? kP.default.createElement(
+             kP.default.Fragment,
+             null,
+             "Press ",
+             l.keyName,
+             " again to exit",
+           )
+         : kP.default.createElement(
+             kP.default.Fragment,
+             null,
+             "Enter to confirm · Esc to cancel",
+           ),
+     )),
+       (K[27] = l.keyName),
+       (K[28] = l.pending),
+       (K[29] = PA));
+   else PA = K[29];
+   let jA;
+   if (K[30] !== JA || K[31] !== _A || K[32] !== PA)
+     ((jA = kP.default.createElement(
+       Iw,
+       {
+         color: "warning",
+         titleColor: "warning",
+         title: "Accessing workspace:",
+       },
+       kP.default.createElement(
+         I,
+         { flexDirection: "column", gap: 1, paddingTop: 1 },
+         JA,
+         OA,
+         HA,
+         DA,
+         _A,
+         PA,
+       ),
+     )),
+       (K[30] = JA),
+       (K[31] = _A),
+       (K[32] = PA),
+       (K[33] = jA));
+   else jA = K[33];
+   return jA;
+ }

+++ Added j4z (pretty-v2.1.20.js:570726-570748)
+ function j4z() {
+   let A = s(2),
+     K;
+   if (A[0] === Symbol.for("react.memo_cache_sentinel"))
+     ((K = { context: "Global" }), (A[0] = K));
+   else K = A[0];
+   s1("app:interrupt", P4z, K);
+   let q;
+   if (A[1] === Symbol.for("react.memo_cache_sentinel"))
+     ((q = Hz.default.createElement(
+       I,
+       { flexDirection: "column" },
+       Hz.default.createElement(f, null, "No conversations found to resume."),
+       Hz.default.createElement(
+         f,
+         { dimColor: !0 },
+         "Press Ctrl+C to exit and start a new conversation.",
+       ),
+     )),
+       (A[1] = q));
+   else q = A[1];
+   return q;
+ }

+++ Added P4z (pretty-v2.1.20.js:570749-570751)
+ function P4z() {
+   process.exit(1);
+ }

+++ Added y4z (pretty-v2.1.20.js:571557-571557)
+   y4z = 5000,

+++ Added Gc (pretty-v2.1.20.js:571561-571561)
+   Gc = null,

+++ Added bk1 (pretty-v2.1.20.js:571562-571562)
+   bk1 = null,

+++ Added FgK (pretty-v2.1.20.js:571771-571774)
+ var FgK = C(() => {
+   a1();
+   OX();
+ });

+++ Added sp6 (pretty-v2.1.20.js:572110-572138)
+ class sp6 {
+   frameDurations = [];
+   firstRenderTime;
+   lastRenderTime;
+   record(A) {
+     let K = performance.now();
+     if (this.firstRenderTime === void 0) this.firstRenderTime = K;
+     ((this.lastRenderTime = K), this.frameDurations.push(A));
+   }
+   getMetrics() {
+     if (
+       this.frameDurations.length === 0 ||
+       this.firstRenderTime === void 0 ||
+       this.lastRenderTime === void 0
+     )
+       return;
+     let A = this.lastRenderTime - this.firstRenderTime;
+     if (A <= 0) return;
+     let q = this.frameDurations.length / (A / 1000),
+       Y = [...this.frameDurations].sort((J, O) => O - J),
+       z = Math.max(0, Math.ceil(Y.length * 0.01) - 1),
+       w = Y[z],
+       H = w > 0 ? 1000 / w : 0;
+     return {
+       averageFps: Math.round(q * 100) / 100,
+       low1PctFps: Math.round(H * 100) / 100,
+     };
+   }
+ }

+++ Added wFK (pretty-v2.1.20.js:572383-572387)
+ var wFK = C(() => {
+   i6();
+   g8();
+   g8();
+ });

+++ Added ZFK (pretty-v2.1.20.js:572989-572992)
+ var ZFK = C(() => {
+   D1();
+   ZH();
+ });

+++ Added DFK (pretty-v2.1.20.js:573024-573026)
+ var DFK = C(() => {
+   rI();
+ });

+++ Added jFK (pretty-v2.1.20.js:573046-573054)
+ var jFK = C(() => {
+   Zp6();
+   PPA();
+   ZdA();
+   kT1();
+   cO();
+   D1();
+   R1();
+ });

+++ Added wQK (pretty-v2.1.20.js:576492-576492)
+ var wQK = {};

+++ Added import@579630 (pretty-v2.1.20.js:579631-579640)
+ import {
+   existsSync as cr2,
+   unlinkSync as PQ6,
+   chmodSync as XvK,
+   statSync as lr2,
+   mkdirSync as ir2,
+   readdirSync as $vK,
+   rmdirSync as nr2,
+   appendFileSync as rr2,
+ } from "fs";

=== Structural Changes ===

@@@ function 'wVA' (was '$e') — structural (98.2%)
--- pretty-v2.1.19.js:538004
+++ pretty-v2.1.20.js:543163
@@ -173,7 +173,7 @@
       (K[42] = GA),
       (K[43] = WA));
   else WA = K[43];
-  let ZA = g && " · Tab to add additional instructions",
+  let DA = B && " · Tab to amend",
     t;
   if (K[44] !== ZA)
     ((t = ef.default.createElement(

@@@ function 'wT1' (was '_f1') — structural (98.0%)
--- pretty-v2.1.19.js:480929
+++ pretty-v2.1.20.js:484334
@@ -210,6 +210,7 @@
     ),
     i8.default.createElement($f1, null),
     i8.default.createElement(RwK, null),
+    n8.default.createElement(B$K, null),
     j.length > 0 &&
       i8.default.createElement(
         I,

@@@ function '_N1' (was 'NV1') — structural (97.5%)
--- pretty-v2.1.19.js:468552
+++ pretty-v2.1.20.js:471674
@@ -256,7 +256,7 @@
       }
     }
   }
-  let s = V && N ? { text: V.text, dim: N } : void 0;
+  let YA = V && N && V.insertPosition === T ? { text: V.text, dim: N } : void 0;
   return {
     onInput: BA,
     renderedValue: R.render(_, O, Z, s),

@@@ function 'jkK' (was 'nPK') — structural (97.3%)
--- pretty-v2.1.19.js:536551
+++ pretty-v2.1.20.js:541722
@@ -113,9 +113,7 @@
       (K[26] = k),
       (K[27] = R));
   else R = K[27];
-  let x =
-      ((_ === "yes" && !Z) || (_ === "no" && !G)) &&
-      " · Tab to add additional instructions",
+  let b = ((_ === "yes" && !Z) || (_ === "no" && !G)) && " · Tab to amend",
     S;
   if (K[28] !== x)
     ((S = kL.default.createElement(

@@@ variable 'kGA' (was 'nZA') — structural (96.0%)
--- pretty-v2.1.19.js:313995
+++ pretty-v2.1.20.js:310558
@@ -9,6 +9,7 @@
   X5();
   Aa();
   UX();
+  $z();
   bU = r(JA(), 1);
   vO1 = {
     name: "LocalAgentTask",

@@@ function 'mLK' (was 'MNK') — structural (96.0%)
--- pretty-v2.1.19.js:547483
+++ pretty-v2.1.20.js:552396
@@ -119,6 +119,13 @@
       return;
     }
     if (j.mode !== "NORMAL") return;
+    if (
+      M.command.type === "idle" &&
+      (W.upArrow || W.downArrow || W.leftArrow || W.rightArrow)
+    ) {
+      w.onInput(G, W);
+      return;
+    }
     let M = { ...O(D, !1), onUndo: A.onUndo, onDotRepeat: $ },
       P = G;
     if (W.leftArrow) P = "h";

@@@ variable 'XX8' (was 'DJ8') — structural (95.6%)
--- pretty-v2.1.19.js:56380
+++ pretty-v2.1.20.js:56536
@@ -273,8 +273,7 @@
       },
       w = { match: $w(/\./, xj(...vS1)), relevance: 0 },
       H = vS1.filter((AA) => typeof AA === "string").concat(["_|0"]),
-      J = vS1
-        .filter((AA) => typeof AA !== "string")
+      J = Tb1.filter((KA) => typeof KA !== "string")
         .concat(lZ5)
         .map(CS1),
       X = { variants: [{ className: "keyword", match: xj(...J, ...TS1) }] },

@@@ variable 'R2K' (was 'nt7') — structural (95.6%)
--- pretty-v2.1.19.js:420776
+++ pretty-v2.1.20.js:447840
@@ -2,7 +2,6 @@
   T7();
   Ft7();
   lt7();
-  uX();
   ((R22 = U.strictObject({})),
     (y22 = U.object({
       tasks: U.array(

@@@ variable 'qs' (was 'ks') — structural (95.5%)
--- pretty-v2.1.19.js:398529
+++ pretty-v2.1.20.js:333788
@@ -14,6 +14,7 @@
   Hf();
   e1();
   jgA();
+  IBA();
   Hk6 = w6(async (A) => {
     let K = hqA(f8(), "skills"),
       q = hqA(PT(), ".claude", "skills"),

@@@ function 'SAz' (was 'Fp2') — structural (95.5%)
--- pretty-v2.1.19.js:549285
+++ pretty-v2.1.20.js:554393
@@ -53,7 +53,7 @@
   else P = K[17];
   let V;
   if (K[18] !== q.name || K[19] !== X)
-    ((V = X ? l7.createElement(f, { color: X }, q.name) : q.name),
+    ((V = O ? n7.createElement(f, { color: O }, `@${q.name}`) : `@${q.name}`),
       (K[18] = q.name),
       (K[19] = X),
       (K[20] = V));

@@@ function 'S0K' (was 'SYK') — structural (95.2%)
--- pretty-v2.1.19.js:467956
+++ pretty-v2.1.20.js:471072
@@ -1,4 +1,8 @@
-function SYK({ permissionModeCli: A, dangerouslySkipPermissions: K }) {
+function S0K({
+  permissionModeCli: A,
+  dangerouslySkipPermissions: K,
+  dangerouslySkipPermissionsWithClassifiers: q,
+}) {
   let q = G8() || {},
     Y = sY("tengu_disable_bypass_permissions_mode"),
     z = q.permissions?.disableBypassPermissionsMode === "disable",

@@@ variable 'A2K' (was 'Mt7') — structural (95.1%)
--- pretty-v2.1.19.js:420083
+++ pretty-v2.1.20.js:447276
@@ -2,7 +2,6 @@
   T7();
   Ot7();
   Dt7();
-  uX();
   ((V22 = U.strictObject({
     subject: U.string().describe("A brief title for the task"),
     description: U.string().describe(

@@@ variable 'kQA' (was '_DA') — structural (95.0%)
--- pretty-v2.1.19.js:400326
+++ pretty-v2.1.20.js:427457
@@ -65,6 +65,10 @@
         return "Edit Notebook";
       },
       getToolUseSummary: Kn7,
+      getActivityDescription(A) {
+        let K = eI6(A);
+        return K ? `Editing notebook ${K}` : "Editing notebook";
+      },
       isEnabled() {
         return !0;
       },

@@@ variable 'Ia1' (was 'Hr1') — structural (94.6%)
--- pretty-v2.1.19.js:128351
+++ pretty-v2.1.20.js:130070
@@ -14,7 +14,10 @@
             q?.debug(
               "@aws-sdk/credential-provider-ini - credential_source is EcsContainer",
             ),
-            async () => CkA.chain(w(z ?? {}), H(z))().then(zr1)
+            async () =>
+              bCA
+                .chain(w(z ?? {}), H(z))()
+                .then(Ra1)
           );
         },
         Ec2InstanceMetadata: async (z) => {

@@@ function 'HNK' (was 'cWK') — structural (94.2%)
--- pretty-v2.1.19.js:522358
+++ pretty-v2.1.20.js:526811
@@ -1,5 +1,5 @@
 async function cWK() {
-  let A = mu6();
+  let A = await kF6();
   if (A.length === 0) return;
   await bu6(async () => {
     let K = xu6(),

@@@ variable 'JF6' (was 'Pu6') — structural (94.1%)
--- pretty-v2.1.19.js:518093
+++ pretty-v2.1.20.js:522329
@@ -28,7 +28,7 @@
     {
       name: "read_page",
       description:
-        "Get an accessibility tree representation of elements on the page. By default returns all elements including non-visible ones. Output is limited to 50000 characters. If the output exceeds this limit, you will receive an error asking you to specify a smaller depth or focus on a specific element using ref_id. Optionally filter for only interactive elements. If you don't have a valid tab ID, use tabs_context_mcp first to get available tabs.",
+        "Get an accessibility tree representation of elements on the page. By default returns all elements including non-visible ones. Output is limited to 50000 characters by default. If the output exceeds this limit, you will receive an error asking you to specify a smaller depth or focus on a specific element using ref_id. Optionally filter for only interactive elements. If you don't have a valid tab ID, use tabs_context_mcp first to get available tabs.",
       inputSchema: {
         type: "object",
         properties: {
@@ -53,6 +53,11 @@
             description:
               "Reference ID of a parent element to read. Will return the specified element and all its children. Use this to focus on a specific part of the page when output is too large.",
           },
+          max_chars: {
+            type: "number",
+            description:
+              "Maximum characters for output (default: 50000). Set to a higher value if your client can handle large outputs.",
+          },
         },
         required: ["tabId"],
       },

@@@ variable 'ZH' (was '_H') — structural (93.9%)
--- pretty-v2.1.19.js:467909
+++ pretty-v2.1.20.js:471023
@@ -7,6 +7,8 @@
   ab();
   t0A();
   lP();
+  Y6();
+  qq();
   IYK = w6(() => {
     if (
       (process.on("SIGINT", () => {

@@@ function 'WE1' (was 'WT1') — structural (93.8%)
--- pretty-v2.1.19.js:539620
+++ pretty-v2.1.20.js:544607
@@ -1,6 +1,12 @@
 function WT1(A) {
-  let K = a(58),
-    { toolUseConfirm: q, onDone: Y, onReject: z, verbose: w } = A,
+  let K = s(59),
+    {
+      toolUseConfirm: q,
+      onDone: Y,
+      onReject: z,
+      verbose: w,
+      workerBadge: H,
+    } = A,
     [H] = p4(),
     J,
     X;
@@ -239,11 +245,17 @@
       (K[54] = XA));
   else XA = K[54];
   let GA;
-  if (K[55] !== o || K[56] !== XA)
-    ((GA = LL.default.createElement(P2, { title: "Tool use" }, o, XA)),
+  if (K[55] !== l || K[56] !== OA || K[57] !== H)
+    ((HA = xL.default.createElement(
+      Iw,
+      { title: "Tool use", workerBadge: H },
+      l,
+      OA,
+    )),
       (K[55] = o),
       (K[56] = XA),
-      (K[57] = GA));
-  else GA = K[57];
+      (K[57] = H),
+      (K[58] = HA));
+  else HA = K[58];
   return GA;
 }

@@@ function 'Bl2' (was 'Lx2') — structural (93.3%)
--- pretty-v2.1.19.js:522273
+++ pretty-v2.1.20.js:526726
@@ -1,5 +1,5 @@
 async function Lx2() {
-  let A = mu6();
+  let A = await kF6();
   if (A.length === 0) return nWK();
   let K = await bu6(async () => {
       let z = xu6(),

@@@ variable 'RY6' (was 'm36') — structural (93.1%)
--- pretty-v2.1.19.js:214607
+++ pretty-v2.1.20.js:213529
@@ -107,14 +107,16 @@
                 V = {};
               for (let T of P.entries()) V[T[0]] = T[1];
               if (M.body == null)
-                return M.blob().then((T) => ({
-                  response: new gh4.HttpResponse({
-                    headers: V,
-                    reason: M.statusText,
-                    statusCode: M.status,
-                    body: T,
-                  }),
-                }));
+                return j
+                  .blob()
+                  .then((T) => ({
+                    response: new du4.HttpResponse({
+                      headers: V,
+                      reason: j.statusText,
+                      statusCode: j.status,
+                      body: T,
+                    }),
+                  }));
               return {
                 response: new gh4.HttpResponse({
                   headers: V,

@@@ function 'fMK' (was 'O$K') — structural (93.0%)
--- pretty-v2.1.19.js:501731
+++ pretty-v2.1.20.js:505130
@@ -26,7 +26,7 @@
   let Z = Math.max(K - 15, 20),
     G = MY(Y, Math.max(Z - 13, 6)),
     { shouldSplit: W, truncatedModel: D, truncatedBilling: j } = dOK(w, H, Z),
-    M = X ? Z - X.length - 3 : Z,
+    j = O ? Z - 1 - O.length - 3 : Z,
     P = cUA(z, Math.max(M, 10)),
     V;
   if (A[3] === Symbol.for("react.memo_cache_sentinel"))
@@ -63,7 +63,7 @@
       (A[9] = D),
       (A[10] = k));
   else k = A[10];
-  let R = X ? `${X} · ${P}` : P,
+  let R = O ? `@${O} · ${P}` : P,
     x;
   if (A[11] !== R)
     ((x = KK.createElement(f, { dimColor: !0 }, R)), (A[11] = R), (A[12] = x));

@@@ variable 'rMA' (was 'XDA') — structural (93.0%)
--- pretty-v2.1.19.js:399653
+++ pretty-v2.1.20.js:426776
@@ -114,6 +114,10 @@
         return "Search";
       },
       getToolUseSummary: Qi7,
+      getActivityDescription(A) {
+        let K = iI6(A);
+        return K ? `Searching for ${K}` : "Searching";
+      },
       isEnabled() {
         return !0;
       },

@@@ variable 'Za7' (was 'bN6') — structural (93.0%)
--- pretty-v2.1.19.js:362858
+++ pretty-v2.1.20.js:387956
@@ -109,6 +109,7 @@
     "Musing",
     "Nebulizing",
     "Nesting",
+    "Newspapering",
     "Noodling",
     "Nucleating",
     "Orbiting",

@@@ function 'ikK' (was 'TVK') — structural (92.9%)
--- pretty-v2.1.19.js:540439
+++ pretty-v2.1.20.js:545511
@@ -165,6 +165,7 @@
                     firstLine:
                       z.split(`
 `)[0] ?? null,
+                    fileContent: W,
                   }),
                 ),
                 JU2,

@@@ variable 'Z0' (was 'G0') — structural (92.7%)
--- pretty-v2.1.19.js:212210
+++ pretty-v2.1.20.js:465973
@@ -13,6 +13,8 @@
   fD();
   nn();
   F1();
+  gG();
+  GL();
   gI4 = { GIT_TERMINAL_PROMPT: "0", GIT_ASKPASS: "" };
   wM = w6(async (A) => {
     let K = await f9(),

@@@ class 'OvK' (was 'pjK') — structural (92.6%)
--- pretty-v2.1.19.js:575463
+++ pretty-v2.1.20.js:579609
@@ -2,6 +2,9 @@
   debug(A, ...K) {
     h(aN1(A, ...K), { level: "debug" });
   }
+  silly(A, ...K) {
+    h(UdA(A, ...K), { level: "debug" });
+  }
   info(A, ...K) {
     h(aN1(A, ...K), { level: "info" });
   }

@@@ function 'Px2' (was 'Pv2') — structural (92.6%)
--- pretty-v2.1.19.js:482812
+++ pretty-v2.1.20.js:486188
@@ -116,8 +116,12 @@
       !X$() &&
       cZ.default.createElement(
         f,
-        { dimColor: !0 },
-        "Tip: You can enable auto-connect to IDE in /config or with the --ide flag",
+        { marginTop: 1 },
+        T_.default.createElement(
+          f,
+          { dimColor: !0 },
+          "Tip: You can enable auto-connect to IDE in /config or with the --ide flag",
+        ),
       )),
       (K[24] = q.length),
       (K[25] = k));
@@ -128,7 +132,7 @@
       Y.length > 0 &&
       cZ.default.createElement(
         I,
-        { flexDirection: "column" },
+        { flexDirection: "column", marginTop: 1 },
         cZ.default.createElement(
           f,
           { dimColor: !0 },

@@@ function 'Y3A' (was 'PqA') — structural (92.5%)
--- pretty-v2.1.19.js:384047
+++ pretty-v2.1.20.js:408727
@@ -111,7 +111,7 @@
     else $ = K[27];
     return $;
   }
-  if (P8() && Y.text.includes("<teammate-message")) {
+  if (j8() && Y.text.includes(`<${IO}`)) {
     let $;
     if (K[28] !== q || K[29] !== Y)
       (($ = Ez.createElement(aQ7, { addMargin: q, param: Y })),

@@@ variable 'fu8' (was 'ky8') — structural (92.5%)
--- pretty-v2.1.19.js:104594
+++ pretty-v2.1.20.js:106312
@@ -76,14 +76,16 @@
               V = {};
             for (let T of P.entries()) V[T[0]] = T[1];
             if (M.body == null)
-              return M.blob().then((T) => ({
-                response: new vy8.HttpResponse({
-                  headers: V,
-                  reason: M.statusText,
-                  statusCode: M.status,
-                  body: T,
-                }),
-              }));
+              return j
+                .blob()
+                .then((T) => ({
+                  response: new Pu8.HttpResponse({
+                    headers: V,
+                    reason: j.statusText,
+                    statusCode: j.status,
+                    body: T,
+                  }),
+                }));
             return {
               response: new vy8.HttpResponse({
                 headers: V,

@@@ variable 'w14' (was '$o8') — structural (92.5%)
--- pretty-v2.1.19.js:137005
+++ pretty-v2.1.20.js:138727
@@ -76,14 +76,16 @@
               V = {};
             for (let T of P.entries()) V[T[0]] = T[1];
             if (M.body == null)
-              return M.blob().then((T) => ({
-                response: new Xo8.HttpResponse({
-                  headers: V,
-                  reason: M.statusText,
-                  statusCode: M.status,
-                  body: T,
-                }),
-              }));
+              return j
+                .blob()
+                .then((T) => ({
+                  response: new Y14.HttpResponse({
+                    headers: V,
+                    reason: j.statusText,
+                    statusCode: j.status,
+                    body: T,
+                  }),
+                }));
             return {
               response: new Xo8.HttpResponse({
                 headers: V,

@@@ function 'IAz' (was 'gp2') — structural (92.4%)
--- pretty-v2.1.19.js:549213
+++ pretty-v2.1.20.js:554320
@@ -55,6 +55,7 @@
       _,
       Z,
       G,
+      "@",
       q.name,
       W,
     )),

@@@ function 'KgK' (was 'hSK') — structural (92.3%)
--- pretty-v2.1.19.js:565855
+++ pretty-v2.1.20.js:570591
@@ -120,17 +120,7 @@
       hz.default.createElement(m7, null),
       hz.default.createElement(f, null, " Resuming conversation…"),
     );
-  if (Q.length === 0)
-    return hz.default.createElement(
-      I,
-      { flexDirection: "column" },
-      hz.default.createElement(f, null, "No conversations found to resume."),
-      hz.default.createElement(
-        f,
-        { dimColor: !0 },
-        "Press Ctrl+C to exit and start a new conversation.",
-      ),
-    );
+  if (F.length === 0) return Hz.default.createElement(j4z, null);
   return hz.default.createElement(ApA, {
     logs: Q,
     maxHeight: W,

@@@ variable 'FG' (was 'QG') — structural (92.3%)
--- pretty-v2.1.19.js:268182
+++ pretty-v2.1.20.js:211872
@@ -183,6 +183,25 @@
         q.push(...ex(_, "Local", Y, w));
       }
     }
+    if (N1(process.env.CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD)) {
+      let $ = Mn6();
+      for (let _ of $) {
+        let Z = LT(_, "CLAUDE.md");
+        q.push(...lk(Z, "Project", Y, w));
+        let G = LT(_, ".claude", "CLAUDE.md");
+        q.push(...lk(G, "Project", Y, w));
+        let W = LT(_, ".claude", "rules");
+        q.push(
+          ...s4A({
+            rulesDir: W,
+            type: "Project",
+            processedPaths: Y,
+            includeExternal: w,
+            conditionalRule: !1,
+          }),
+        );
+      }
+    }
     return (
       J4("info", "memory_files_completed", {
         duration_ms: Date.now() - K,

@@@ function 'DIK' (was 'cvK') — structural (92.2%)
--- pretty-v2.1.19.js:555448
+++ pretty-v2.1.20.js:560564
@@ -23,7 +23,12 @@
   else H = A[4];
   let J;
   if (A[5] !== w || A[6] !== z.identity.agentName)
-    ((J = vP.createElement(f, { color: w, bold: !0 }, z.identity.agentName)),
+    ((J = vP.createElement(
+      f,
+      { color: w, bold: !0 },
+      "@",
+      z.identity.agentName,
+    )),
       (A[5] = w),
       (A[6] = z.identity.agentName),
       (A[7] = J));

@@@ function 'ckK' (was 'fVK') — structural (92.0%)
--- pretty-v2.1.19.js:540253
+++ pretty-v2.1.20.js:545313
@@ -1,6 +1,12 @@
 function fVK(A) {
-  let K = a(40),
-    { toolUseConfirm: q, onDone: Y, onReject: z, verbose: w } = A,
+  let K = s(41),
+    {
+      toolUseConfirm: q,
+      onDone: Y,
+      onReject: z,
+      verbose: w,
+      workerBadge: H,
+    } = A,
     [H] = p4(),
     { url: J } = q.input,
     X;
@@ -162,11 +168,17 @@
       (K[36] = b));
   else b = K[36];
   let Q;
-  if (K[37] !== b || K[38] !== k)
-    ((Q = Fv.default.createElement(P2, { title: "Fetch" }, k, b)),
+  if (K[37] !== F || K[38] !== R || K[39] !== H)
+    ((Q = dv.default.createElement(
+      Iw,
+      { title: "Fetch", workerBadge: H },
+      R,
+      F,
+    )),
       (K[37] = b),
       (K[38] = k),
-      (K[39] = Q));
-  else Q = K[39];
+      (K[39] = H),
+      (K[40] = Q));
+  else Q = K[40];
   return Q;
 }

@@@ function 'UFA' (was 'KgA') — structural (91.9%)
--- pretty-v2.1.19.js:390745
+++ pretty-v2.1.20.js:412236
@@ -50,5 +50,6 @@
     fileReadingLimits: A.fileReadingLimits,
     userModified: A.userModified,
     criticalSystemReminder_EXPERIMENTAL: K?.criticalSystemReminder_EXPERIMENTAL,
+    requireCanUseTool: K?.requireCanUseTool,
   };
 }

@@@ function 'W8K' (was 'mU7') — structural (91.6%)
--- pretty-v2.1.19.js:386576
+++ pretty-v2.1.20.js:411278
@@ -42,6 +42,7 @@
     );
   }
   if (A.status === "teammate_spawned") {
+    if (j8()) return null;
     let D = A,
       j = D.color ? AX[D.color] : void 0;
     return B6.createElement(

@@@ function 'Tk2' (was 'DG2') — structural (91.3%)
--- pretty-v2.1.19.js:448844
+++ pretty-v2.1.20.js:459606
@@ -43,7 +43,6 @@
           xw("lsp_diagnostics", async () => pG2()),
           xw("unified_tasks", async () => rG2(K, z)),
           xw("async_hook_responses", async () => oG2()),
-          xw("memory", async () => N5K(K, z, w)),
           xw("token_usage", async () => Promise.resolve(tG2(z ?? []))),
           xw("budget_usd", async () =>
             Promise.resolve(eG2(K.options.maxBudgetUsd)),

@@@ function 'Uk1' (was 'pv1') — structural (91.1%)
--- pretty-v2.1.19.js:572676
+++ pretty-v2.1.20.js:576777
@@ -57,7 +57,6 @@
     nSK(),
     tSK(),
     khK(),
-    VhK(),
     HjK(h7()),
     ZK("setup_after_prefetch"));
   let { hasReleaseNotes: O } = FUA(f1().lastReleaseNotesSeen);
@@ -90,6 +89,8 @@
         $.lastTotalCacheCreationInputTokens,
       last_session_total_cache_read_input_tokens:
         $.lastTotalCacheReadInputTokens,
+      last_session_fps_average: $.lastFpsAverage,
+      last_session_fps_low_1_pct: $.lastFpsLow1Pct,
       last_session_id: $.lastSessionId,
     });
 }

@@@ function 'vMK' (was 'Z$K') — structural (90.9%)
--- pretty-v2.1.19.js:501877
+++ pretty-v2.1.20.js:505276
@@ -44,9 +44,9 @@
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.19",
+          VERSION: "2.1.20",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-01-23T21:13:41Z",
+          BUILD_TIME: "2026-01-27T00:38:42Z",
         }.VERSION
       )
         return;
@@ -180,7 +180,7 @@
       else v1 = K[20];
       PA = v1;
     }
-    let NA = Q ? H - 4 - Q.length - 3 : H - 4,
+    let NA = F ? H - 4 - 1 - F.length - 3 : H - 4,
       cA = cUA(x, Math.max(NA, 10)),
       z1;
     if (K[21] !== l)
@@ -241,7 +241,7 @@
         iA,
         j8.createElement(f, { dimColor: !0 }, F),
         j8.createElement(f, { dimColor: !0 }, g),
-        j8.createElement(f, { dimColor: !0 }, Q ? `${Q} · ${cA}` : cA),
+        f8.createElement(f, { dimColor: !0 }, F ? `@${F} · ${lA}` : lA),
       ),
       V1,
     );
@@ -251,9 +251,9 @@
       !process.env.IS_DEMO && W.oauthAccount?.organizationName
         ? `${F} · ${g} · ${W.oauthAccount.organizationName}`
         : `${F} · ${g}`,
-    GA = Q ? TB6 - Q.length - 3 : TB6,
+    OA = F ? _g6 - 1 - F.length - 3 : _g6,
     WA = cUA(x, Math.max(GA, 10)),
-    ZA = Q ? `${Q} · ${WA}` : WA,
+    DA = F ? `@${F} · ${HA}` : HA,
     t = QOK(e, ZA, XA),
     { leftWidth: $A, rightWidth: VA } = FOK(H, B, t),
     MA;

@@@ function 'xIK' (was 'OEK') — structural (90.6%)
--- pretty-v2.1.19.js:556294
+++ pretty-v2.1.20.js:561458
@@ -1,4 +1,4 @@
-function OEK(A, K, q, Y = "session") {
+function xIK(A, K, q, Y = "session", z = !1) {
   let z = zN.useRef("unknown");
   z.current = sI(A)?.message?.id || "unknown";
   let [w, H] = j6(),
@@ -55,6 +55,7 @@
     V = zN.useMemo(() => {
       if (W !== "closed") return !1;
       if (K) return !1;
+      if (z) return !1;
       if (
         process.env.CLAUDE_FORCE_DISPLAY_SURVEY &&
         !w.feedbackSurvey.timeLastShown
@@ -86,6 +87,7 @@
       W,
       K,
       P,
+      V,
       w.feedbackSurvey.timeLastShown,
       w.feedbackSurvey.submitCountAtLastAppearance,
       q,

@@@ function 'IiK' (was 'MQK') — structural (90.5%)
--- pretty-v2.1.19.js:1869
+++ pretty-v2.1.20.js:1869
@@ -70,6 +70,7 @@
     sdkBetas: void 0,
     mainThreadAgentType: void 0,
     isRemoteMode: !1,
+    additionalDirectoriesForClaudeMd: [],
     resumedTranscriptPath: null,
   };
 }

@@@ class 'dq1' (was 'l71') — structural (90.4%)
--- pretty-v2.1.19.js:173434
+++ pretty-v2.1.20.js:176411
@@ -104,14 +104,6 @@
           for (let M = 0; M < D.length; M++) {
             let P = D[M],
               V = P.value.codePointAt(0);
-            if (
-              V === 8203 ||
-              V === 8204 ||
-              V === 8205 ||
-              V === 65279 ||
-              V === 8288
-            )
-              continue;
             if (V !== void 0 && V <= 31) {
               if (V === 9) {
                 let x = 8 - (j % 8);
@@ -158,8 +150,10 @@
               }
               continue;
             }
+            let N = m7(P.value);
+            if (N === 0) continue;
             W[j] = P;
-            let N = P.fullWidth || P.value.length > 1,
+            let T = N >= 2,
               T = e94(P.styles),
               k = T ? AY4(P.styles) : P.styles;
             if (

@@@ function 'aRK' (was 'kTK') — structural (90.3%)
--- pretty-v2.1.19.js:551229
+++ pretty-v2.1.20.js:556353
@@ -46,7 +46,7 @@
             f,
             { key: k, color: sT(T.color), wrap: "wrap" },
             "● ",
-            FS.createElement(f, { bold: !0 }, T.from, ":"),
+            tS.createElement(f, { bold: !0 }, "@", T.from, ":"),
             " ",
             Td2(pG1(T.text), fd2, P),
           )),

@@@ function 'Mv1' (was 'VN1') — structural (90.3%)
--- pretty-v2.1.19.js:515713
+++ pretty-v2.1.20.js:519703
@@ -72,11 +72,19 @@
       { marginTop: 1 },
       G,
       $ === void 0 || $ === "automatic"
-        ? Bv.default.createElement(f, { inverse: !0, bold: !0 }, " ", q, " ")
+        ? Fv.default.createElement(
+            f,
+            { inverse: !0, bold: !0 },
+            " ",
+            "@",
+            q,
+            " ",
+          )
         : Bv.default.createElement(
             f,
             { backgroundColor: AX[$], color: "inverseText", bold: !0 },
             " ",
+            "@",
             q,
             " ",
           ),

@@@ variable 'z8' (was 'e6') — structural (90.1%)
--- pretty-v2.1.19.js:2494
+++ pretty-v2.1.20.js:2508
@@ -12,6 +12,18 @@
     async stat(A) {
       return VQK(A);
     },
+    async readdir(A) {
+      return biK(A, { withFileTypes: !0 });
+    },
+    async unlink(A) {
+      return xiK(A);
+    },
+    async rmdir(A) {
+      return uiK(A);
+    },
+    async rm(A, K) {
+      return BiK(A, K);
+    },
     statSync(A) {
       return yO(`statSync(${A})`, () => e5.statSync(A));
     },

@@@ variable 'qBA' (was 'wBA') — structural (90.0%)
--- pretty-v2.1.19.js:309345
+++ pretty-v2.1.20.js:305675
@@ -9,6 +9,7 @@
   PZ();
   sq();
   F1();
+  B1();
   ((FW6 = r(F$7(), 1)),
     (eMY = ["state", "nonce", "code_challenge", "code_verifier", "code"]));
   gZA = class gZA extends Error {

@@@ function 'oa2' (was 'PF2') — structural (89.7%)
--- pretty-v2.1.19.js:534338
+++ pretty-v2.1.20.js:539137
@@ -1,4 +1,4 @@
-function PF2() {
+async function oa2() {
   let A = af(f8(), "plans");
   return MF2(A, ".md");
 }

@@@ variable 'Tv' (was 'Wv') — structural (89.6%)
--- pretty-v2.1.19.js:458268
+++ pretty-v2.1.20.js:463451
@@ -20,7 +20,6 @@
   q6();
   PK();
   F1();
-  ks();
   Fj2 = String.fromCharCode(8239);
   Qj2 = [];
   OP1 = class OP1 extends Error {
@@ -203,6 +202,10 @@
       outputSchema: lj2,
       userFacingName: o3K,
       getToolUseSummary: a3K,
+      getActivityDescription(A) {
+        let K = Sx6(A);
+        return K ? `Reading ${K}` : "Reading file";
+      },
       isEnabled() {
         return !0;
       },

@@@ function 'f1z' (was 'Rd2') — structural (89.6%)
--- pretty-v2.1.19.js:552053
+++ pretty-v2.1.20.js:557180
@@ -144,7 +144,7 @@
       let $6 = [],
         V8 = OA.teamContext.teammates;
       if (!V8) return $6;
-      let l4 = /(^|\s)@@([\w-]+)/g,
+      let l4 = /(^|\s)@([\w-]+)/g,
         n4;
       while ((n4 = l4.exec(q4)) !== null) {
         let vq = n4[1] ?? "",
@@ -397,8 +397,9 @@
     fA = BK.useCallback(
       async ($6, V8 = !1) => {
         if (F || j1 || d || M1) return;
-        let l4 = OA.promptSuggestion.text;
-        if (($6.trim() === "" || $6 === l4) && l4) {
+        let l4 = Object.values(T).some((Y8) => Y8.type === "image"),
+          F4 = ZA.promptSuggestion.text;
+        if (($6.trim() === "" || $6 === F4) && F4 && !l4) {
           if (OA.speculation.status === "active") {
             (m4(),
               GA(
@@ -419,10 +420,10 @@
           let o6 = nNK($6);
           if (o6) {
             let w7 = rNK(o6.recipientName, o6.message, OA.teamContext, U3);
-            if (w7.success)
+            if (c4.success) {
               (hK({
                 key: "direct-message-sent",
-                text: `Sent to ${w7.recipientName}`,
+                text: `Sent to @${c4.recipientName}`,
                 priority: "immediate",
                 timeoutMs: 3000,
               }),
@@ -430,26 +431,10 @@
                 vA(0),
                 d8(),
                 B7());
-            else if (w7.error === "unknown_recipient")
-              hK({
-                key: "direct-message-error",
-                text: `Unknown recipient: ${w7.recipientName}`,
-                color: "error",
-                priority: "immediate",
-                timeoutMs: 5000,
-              });
-            else
-              hK({
-                key: "direct-message-error",
-                text: "No active team - cannot send direct message",
-                color: "error",
-                priority: "immediate",
-                timeoutMs: 5000,
-              });
-            return;
+              return;
+            } else if (c4.error === "no_team_context");
           }
         }
-        let vq = Object.values(T).some((o6) => o6.type === "image");
         if ($6.trim() === "" && !vq) return;
         let Eq =
           jK.suggestions.length > 0 &&
@@ -657,7 +642,7 @@
         (Tc6(!0), clA(!0));
       if ($6 === "plan") V6((l4) => ({ ...l4, lastPlanModeUse: Date.now() }));
       if ($6 === "acceptEdits") o7("auto-accept-mode");
-      let V8 = WY(q, { type: "setMode", mode: $6, destination: "session" });
+      let v8 = GY(q, { type: "setMode", mode: og($6), destination: "session" });
       if ((Y(V8), hy6($6, OA.teamContext?.teamName), MA)) SA(!1);
     }, [q, OA.teamContext, OA.viewingAgentTaskId, FA, LA, Y, MA]),
     ww = BK.useCallback(() => {
@@ -697,10 +682,8 @@
       "chat:thinkingToggle": ZY,
       "chat:cycleMode": vH,
       "chat:imagePaste": ww,
-      "history:previous": l3,
-      "history:next": T5,
     }),
-    [i4, JK, Fq, _Y, ZY, vH, ww, l3, T5],
+    [y4, wK, pq, cY, AY, wJ, uz],
   );
   (f7(MX, { context: "Chat", isActive: !s && !g1 }),
     i1(
@@ -982,6 +965,8 @@
       onSubmit: fA,
       onChange: y4,
       value: N1 ? h8A(typeof N1 === "string" ? N1 : N1.display) : Z,
+      onHistoryUp: v5,
+      onHistoryDown: N3,
       onHistoryReset: B7,
       onClearInput: R8,
       placeholder: VO,

@@@ variable 'XU2' (was 'OI2') — structural (89.6%)
--- pretty-v2.1.19.js:502845
+++ pretty-v2.1.20.js:506244
@@ -157,7 +157,7 @@
         z1 = BA ? cA.slice(-sUA) : cA;
       s = BA && cA.length > sUA;
       let { messages: dA } = EOK(z1, z, H);
-      ((AA = SU7(dA, H, z)),
+      ((KA = FW7(dA, z)),
         (wA = y3K(Q, z1)),
         (K[18] = SA),
         (K[19] = Q),

@@@ function 'ljA' (was 'cjA') — structural (89.4%)
--- pretty-v2.1.19.js:468196
+++ pretty-v2.1.20.js:471316
@@ -35,7 +35,6 @@
     feedbackSurvey: { timeLastShown: null, submitCountAtLastAppearance: null },
     sessionHooks: {},
     inbox: { messages: [] },
-    workerPermissions: { queue: [], selectedIndex: 0 },
     workerSandboxPermissions: { queue: [], selectedIndex: 0 },
     pendingWorkerRequest: null,
     pendingSandboxRequest: null,
@@ -56,6 +55,7 @@
       hunks: new Map(),
       lastUpdated: 0,
     },
+    prStatus: { number: null, url: null, reviewState: null, lastUpdated: 0 },
     authVersion: 0,
     initialMessage: null,
   };

@@@ variable 'SZ' (was 'Z_') — structural (89.2%)
--- pretty-v2.1.19.js:464875
+++ pretty-v2.1.20.js:464258
@@ -198,6 +198,10 @@
       if (q) return q;
       return MY(K, kx);
     },
+    getActivityDescription(A) {
+      if (!A?.command) return "Running command";
+      return `Running ${A.description ?? o9(A.command, _I)}`;
+    },
     isEnabled() {
       return !0;
     },

@@@ variable 'P76' (was 'p66') — structural (89.1%)
--- pretty-v2.1.19.js:171922
+++ pretty-v2.1.20.js:174899
@@ -138,7 +138,7 @@
             }
             u66(A, H, J);
           }
-        if (w && A.yogaNode) g66(A.yogaNode, w);
+        if (w && A.yogaNode) W76(A.yogaNode, w, Y.style);
       },
       commitTextUpdate(A, K, q) {
         xLA(A, q);

@@@ variable 'f7K' (was 't9K') — structural (89.1%)
--- pretty-v2.1.19.js:464397
+++ pretty-v2.1.20.js:422304
@@ -48,4 +48,4 @@
       decisionReason: _,
       suggestions: OV1(Y),
     };
-  };
+  },

@@@ function 'RkK' (was 'zVK') — structural (88.9%)
--- pretty-v2.1.19.js:538485
+++ pretty-v2.1.20.js:543651
@@ -1,5 +1,5 @@
 function zVK(A) {
-  let K = a(42),
+  let K = s(43),
     q,
     Y;
   if (K[0] !== A)
@@ -124,10 +124,11 @@
     K[34] !== q.onReject ||
     K[35] !== q.toolUseConfirm ||
     K[36] !== q.toolUseContext ||
-    K[37] !== N ||
+    K[37] !== q.workerBadge ||
     K[38] !== k ||
     K[39] !== R ||
-    K[40] !== x
+    K[40] !== R ||
+    K[41] !== b
   )
     ((S = OPA.default.createElement(Jm, {
       toolUseConfirm: j,
@@ -142,6 +143,7 @@
       completionType: "str_replace_single",
       languageName: x,
       parseInput: D,
+      workerBadge: q.workerBadge,
     })),
       (K[31] = z),
       (K[32] = D),
@@ -149,11 +151,12 @@
       (K[34] = q.onReject),
       (K[35] = q.toolUseConfirm),
       (K[36] = q.toolUseContext),
-      (K[37] = N),
+      (K[37] = q.workerBadge),
       (K[38] = k),
       (K[39] = R),
       (K[40] = x),
-      (K[41] = S));
-  else S = K[41];
+      (K[41] = b),
+      (K[42] = S));
+  else S = K[42];
   return S;
 }

@@@ function 'tK1' (was 'z71') — structural (88.4%)
--- pretty-v2.1.19.js:158523
+++ pretty-v2.1.20.js:160251
@@ -1,6 +1,6 @@
 function z71(A, K, q, Y) {
   if (process.env.CLAUDE_CODE_SUBAGENT_MODEL)
-    return process.env.CLAUDE_CODE_SUBAGENT_MODEL;
+    return Dw(process.env.CLAUDE_CODE_SUBAGENT_MODEL);
   let z = G16(K),
     w = (J) => {
       if (z && cK() === "bedrock") return r54(J, z);

@@@ function 'gn2' (was 'Ou2') — structural (88.3%)
--- pretty-v2.1.19.js:527223
+++ pretty-v2.1.20.js:531900
@@ -28,7 +28,7 @@
   let Y = OV(A),
     z = i$(Y.toolName);
   if (z) {
-    if (Y.ruleContent !== void 0)
+    if (Y.ruleContent !== void 0 || rF6(A, "(") > 0)
       return {
         valid: !1,
         error: "MCP rules do not support patterns in parentheses",
@@ -75,13 +75,6 @@
         error: "Prefix cannot be empty before :*",
         suggestion: "Specify a command prefix before :*",
         examples: ["Bash(npm:*)", "Bash(git:*)"],
-      };
-    if (H === "*")
-      return {
-        valid: !1,
-        error: 'Use "Bash" without parentheses to allow all commands',
-        suggestion: "Remove the parentheses or specify a command pattern",
-        examples: ["Bash", "Bash(npm:*)", "Bash(npm *)"],
       };
   }
   if (mDK(Y.toolName) && Y.ruleContent !== void 0) {

@@@ variable 'OX' (was 'zO') — structural (88.2%)
--- pretty-v2.1.19.js:524427
+++ pretty-v2.1.20.js:529007
@@ -90,6 +90,7 @@
   fDK();
   NDK();
   eJ();
+  sJ();
   ((su6 = w6(() => [
     Z2K,
     TGK,
@@ -150,6 +151,7 @@
     fZK,
     fWK,
     cGK,
+    YfK,
     ...(!qB() ? [vx7, $Q7()] : []),
     X_K,
     ...[],

@@@ function 'fm' (was 'Jm') — structural (88.1%)
--- pretty-v2.1.19.js:536710
+++ pretty-v2.1.20.js:541879
@@ -1,5 +1,5 @@
 function Jm(A) {
-  let K = a(69),
+  let K = s(70),
     {
       toolUseConfirm: q,
       toolUseContext: Y,
@@ -15,6 +15,7 @@
       parseInput: G,
       operationType: W,
       ideDiffSupport: D,
+      workerBadge: M,
     } = A,
     j = X === void 0 ? "Do you want to proceed?" : X,
     M = $ === void 0 ? "tool_use_single" : $,
@@ -211,7 +212,13 @@
   if (K[48] !== Q) ((s = (OA) => Q(OA)), (K[48] = Q), (K[49] = s));
   else s = K[49];
   let AA;
-  if (K[50] !== F || K[51] !== S || K[52] !== SA || K[53] !== BA || K[54] !== s)
+  if (
+    K[50] !== u ||
+    K[51] !== B ||
+    K[52] !== bA ||
+    K[53] !== YA ||
+    K[54] !== KA
+  )
     ((AA = Hm.default.createElement(T6, {
       options: S,
       inlineDescriptions: !0,
@@ -240,10 +247,10 @@
       (K[58] = wA));
   else wA = K[58];
   let KA;
-  if (K[59] !== O || K[60] !== J || K[61] !== wA || K[62] !== H)
+  if (K[59] !== X || K[60] !== J || K[61] !== AA || K[62] !== H || K[63] !== M)
     ((KA = Hm.default.createElement(
       P2,
-      { title: H, subtitle: J, innerPaddingX: 0 },
+      { title: H, subtitle: J, innerPaddingX: 0, workerBadge: M },
       O,
       wA,
     )),
@@ -251,27 +258,26 @@
       (K[60] = J),
       (K[61] = wA),
       (K[62] = H),
-      (K[63] = KA));
-  else KA = K[63];
-  let zA =
-      ((B === "yes" && !d) || (B === "no" && !o)) &&
-      " · Tab to add additional instructions",
+      (K[63] = M),
+      (K[64] = t));
+  else t = K[64];
+  let $A = ((d === "yes" && !a) || (d === "no" && !l)) && " · Tab to amend",
     HA;
-  if (K[64] !== zA)
+  if (K[65] !== $A)
     ((HA = Hm.default.createElement(
       I,
       { paddingX: 1, marginTop: 1 },
       Hm.default.createElement(f, { dimColor: !0 }, "Esc to cancel", zA),
     )),
-      (K[64] = zA),
-      (K[65] = HA));
-  else HA = K[65];
+      (K[65] = $A),
+      (K[66] = vA));
+  else vA = K[66];
   let vA;
-  if (K[66] !== KA || K[67] !== HA)
+  if (K[67] !== t || K[68] !== vA)
     ((vA = Hm.default.createElement(Hm.default.Fragment, null, KA, HA)),
-      (K[66] = KA),
       (K[67] = HA),
-      (K[68] = vA));
-  else vA = K[68];
+      (K[68] = vA),
+      (K[69] = ZA));
+  else ZA = K[69];
   return vA;
 }

@@@ function 'FNK' (was 'vDK') — structural (88.1%)
--- pretty-v2.1.19.js:524837
+++ pretty-v2.1.20.js:529442
@@ -1,8 +1,6 @@
 function vDK(A) {
   if (!aH() || !A || A.length === 0) return "";
-  return `
-
-# MCP CLI Command
+  return `# MCP CLI Command
 
 You have access to an \`mcp-cli\` CLI command for interacting with MCP (Model Context Protocol) servers.
 
@@ -114,6 +112,5 @@
 
 Use this command via ${I7} when you need to discover, inspect, or invoke MCP tools.
 
-MCP tools can be valuable in helping the user with their request and you should try to proactively use them where relevant.
-`;
+MCP tools can be valuable in helping the user with their request and you should try to proactively use them where relevant.`;
 }

@@@ function 'CF6' (was 'gu6') — structural (88.0%)
--- pretty-v2.1.19.js:522298
+++ pretty-v2.1.20.js:526751
@@ -1,6 +1,6 @@
 async function gu6(A) {
   if (A === "all") return Lx2();
-  let K = mu6();
+  let K = await kF6();
   if (K.length === 0) return nWK();
   let q = new Date(),
     Y = A === "7d" ? 7 : 30,

@@@ variable 'vQA' (was 'PgA') — structural (87.6%)
--- pretty-v2.1.19.js:400025
+++ pretty-v2.1.20.js:427152
@@ -34,6 +34,10 @@
       },
       userFacingName: pi7,
       getToolUseSummary: ri7,
+      getActivityDescription(A) {
+        let K = sI6(A);
+        return K ? `Finding ${K}` : "Finding files";
+      },
       isEnabled() {
         return !0;
       },

@@@ function 'qu6' (was 'tI6') — structural (87.6%)
--- pretty-v2.1.19.js:452608
+++ pretty-v2.1.20.js:470096
@@ -19,7 +19,7 @@
     }
     if (Y.match(/^<local-command-stdout>/)) continue;
     if (Y.match(/^<session-start-hook>/)) continue;
-    if (Y.match(/^<tick>/)) continue;
+    if (Y.startsWith(`<${ql}>`)) continue;
     let w = d7(Y, "bash-input");
     if (w) return `! ${w}`;
     return Y;

@@@ function 'TFK' (was '$bK') — structural (87.5%)
--- pretty-v2.1.19.js:569000
+++ pretty-v2.1.20.js:573057
@@ -29,6 +29,54 @@
       Hq(1));
     return;
   }
+  let O = Z7z(A, J);
+  if (J.outputFormat === "stream-json" && J.verbose)
+    TM7((N) => {
+      let T = (() => {
+        switch (N.type) {
+          case "started":
+            return {
+              type: "system",
+              subtype: "hook_started",
+              hook_id: N.hookId,
+              hook_name: N.hookName,
+              hook_event: N.hookEvent,
+              uuid: pL(),
+              session_id: i1(),
+            };
+          case "progress":
+            return {
+              type: "system",
+              subtype: "hook_progress",
+              hook_id: N.hookId,
+              hook_name: N.hookName,
+              hook_event: N.hookEvent,
+              stdout: N.stdout,
+              stderr: N.stderr,
+              output: N.output,
+              uuid: pL(),
+              session_id: i1(),
+            };
+          case "response":
+            return {
+              type: "system",
+              subtype: "hook_response",
+              hook_id: N.hookId,
+              hook_name: N.hookName,
+              hook_event: N.hookEvent,
+              output: N.output,
+              stdout: N.stdout,
+              stderr: N.stderr,
+              exit_code: N.exitCode,
+              outcome: N.outcome,
+              uuid: pL(),
+              session_id: i1(),
+            };
+        }
+      })();
+      O.write(T);
+    });
+  if (J.setupTrigger) await jf1(J.setupTrigger, !1);
   let X = await K(),
     O = await Qn2(q, {
       continue: J.continue,
@@ -80,7 +128,6 @@
   }
   let Z = xDA(X.mcp.tools, X.toolPermissionContext),
     G = aH() ? z : [...z, ...Z],
-    W = Un2(A, J),
     D = J.sdkUrl ? "stdio" : J.permissionPromptToolName,
     j = void 0,
     M = mn2(D, W, X.mcp.tools, j);

@@@ function 'ekK' (was 'yVK') — structural (86.9%)
--- pretty-v2.1.19.js:541726
+++ pretty-v2.1.20.js:546817
@@ -1,6 +1,6 @@
 function yVK(A) {
-  let K = a(50),
-    { toolUseConfirm: q, onDone: Y, onReject: z } = A,
+  let K = s(51),
+    { toolUseConfirm: q, onDone: Y, onReject: z, workerBadge: w } = A,
     w = VU2,
     H;
   if (K[0] !== q.input) ((H = w(q.input)), (K[0] = q.input), (K[1] = H));
@@ -274,12 +274,19 @@
       (K[45] = GA));
   else GA = K[45];
   let WA;
-  if (K[46] !== B || K[47] !== l || K[48] !== GA)
-    ((WA = qN.default.createElement(P2, { title: B }, d, l, GA)),
+  if (K[46] !== d || K[47] !== e || K[48] !== HA || K[49] !== w)
+    ((DA = JN.default.createElement(
+      Iw,
+      { title: d, workerBadge: w },
+      a,
+      e,
+      HA,
+    )),
       (K[46] = B),
       (K[47] = l),
       (K[48] = GA),
-      (K[49] = WA));
-  else WA = K[49];
+      (K[49] = w),
+      (K[50] = DA));
+  else DA = K[50];
   return WA;
 }

@@@ variable 'kh8' (was 'bC8') — structural (86.8%)
--- pretty-v2.1.19.js:99257
+++ pretty-v2.1.20.js:100948
@@ -36,11 +36,13 @@
       deniedDomains: Kq.array(sQ1).describe("List of denied domains"),
       allowUnixSockets: Kq.array(Kq.string())
         .optional()
-        .describe("Unix socket paths that are allowed (macOS only)"),
+        .describe(
+          "macOS only: Unix socket paths to allow. Ignored on Linux (seccomp cannot filter by path).",
+        ),
       allowAllUnixSockets: Kq.boolean()
         .optional()
         .describe(
-          "Allow ALL Unix sockets (Linux only - disables Unix socket blocking)",
+          "If true, allow all Unix sockets (disables blocking on both platforms).",
         ),
       allowLocalBinding: Kq.boolean()
         .optional()
@@ -61,9 +63,11 @@
         .describe(
           "Port of an external SOCKS proxy to use instead of starting a local one. When provided, the library will skip starting its own SOCKS proxy and use this port. The external proxy must handle domain filtering.",
         ),
-      mitmProxy: H8q.optional().describe(
-        "Optional MITM proxy configuration. Routes matching domains through an upstream proxy via Unix socket while SRT still handles allow/deny filtering.",
-      ),
+      mitmProxy: ez5
+        .optional()
+        .describe(
+          "Optional MITM proxy configuration. Routes matching domains through an upstream proxy via Unix socket while SRT still handles allow/deny filtering.",
+        ),
     })),
     (yC8 = Kq.object({
       denyRead: Kq.array(aQ1).describe("Paths denied for reading"),
@@ -109,9 +113,9 @@
         .describe(
           "Enable weaker nested sandbox mode (for Docker environments)",
         ),
-      ripgrep: SC8.optional().describe(
-        'Custom ripgrep configuration (default: { command: "rg" })',
-      ),
+      ripgrep: vh8
+        .optional()
+        .describe('Custom ripgrep configuration (default: { command: "rg" })'),
       mandatoryDenySearchDepth: Kq.number()
         .int()
         .min(1)

@@@ function 'WcA' (was 'lT1') — structural (86.8%)
--- pretty-v2.1.19.js:554491
+++ pretty-v2.1.20.js:559599
@@ -23,14 +23,6 @@
         ...(J !== void 0 && { waiting_for_user_permission_ms: J }),
       });
       break;
-    case "classifier":
-      n("tengu_tool_use_granted_by_classifier", {
-        messageID: Y,
-        toolName: VK(A.name),
-        sandboxEnabled: l8.isSandboxingEnabled(),
-        ...(J !== void 0 && { waiting_for_user_permission_ms: J }),
-      });
-      break;
   }
   let X = ed2(w);
   if (nT1(A.name)) {

@@@ function 'SE' (was 'OV') — structural (86.7%)
--- pretty-v2.1.19.js:526800
+++ pretty-v2.1.20.js:531478
@@ -7,7 +7,7 @@
   let Y = A.substring(0, K),
     z = A.substring(K + 1, q);
   if (!Y) return { toolName: A };
-  if (z === "") return { toolName: Y };
+  if (z === "" || z === "*") return { toolName: Y };
   let w = zu2(z);
   return { toolName: Y, ruleContent: w };
 }

@@@ function 'CkK' (was 'qVK') — structural (86.7%)
--- pretty-v2.1.19.js:538222
+++ pretty-v2.1.20.js:543381
@@ -1,9 +1,10 @@
 function qVK(A) {
-  let K = a(52),
+  let K = s(53),
     {
       toolUseConfirm: q,
       onDone: Y,
       onReject: z,
+      workerBadge: w,
       serverName: w,
       toolName: H,
       args: J,
@@ -236,11 +237,17 @@
       (K[48] = GA));
   else GA = K[48];
   let WA;
-  if (K[49] !== l || K[50] !== GA)
-    ((WA = CL.default.createElement(P2, { title: "Tool use" }, l, GA)),
+  if (K[49] !== e || K[50] !== HA || K[51] !== w)
+    ((DA = bL.default.createElement(
+      Iw,
+      { title: "Tool use", workerBadge: w },
+      e,
+      HA,
+    )),
       (K[49] = l),
       (K[50] = GA),
-      (K[51] = WA));
-  else WA = K[51];
+      (K[51] = w),
+      (K[52] = DA));
+  else DA = K[52];
   return WA;
 }

@@@ function 'mS8' (was 'lk8') — structural (86.7%)
--- pretty-v2.1.19.js:94677
+++ pretty-v2.1.20.js:96368
@@ -23,19 +23,22 @@
   let V = ["--new-session", "--die-with-parent"],
     N = void 0;
   try {
-    if (!$)
-      if (((N = mk8(D?.bpfPath) ?? void 0), !N))
-        C8(
-          "[Sandbox Linux] Seccomp filter not available (missing binaries). Continuing without Unix socket blocking - sandbox will still provide filesystem and network isolation but Unix sockets will be allowed.",
+    if (!$) {
+      N = yS8(D?.bpfPath) ?? void 0;
+      let x = AkA(D?.applyPath);
+      if (!N || !x)
+        (C8(
+          "[Sandbox Linux] Seccomp binaries not available - unix socket blocking disabled. Install @anthropic-ai/sandbox-runtime globally for full protection.",
           { level: "warn" },
-        );
+        ),
+          (N = void 0));
       else {
         if (!N.includes("/vendor/seccomp/")) (mQ1.add(N), L1q());
         C8(
           "[Sandbox Linux] Generated seccomp BPF filter for Unix socket blocking",
         );
       }
-    else if ($)
+    } else
       C8(
         "[Sandbox Linux] Skipping seccomp filter - allowAllUnixSockets is enabled",
       );

@@@ variable 'w4' (was 'A4') — structural (86.7%)
--- pretty-v2.1.19.js:468337
+++ pretty-v2.1.20.js:471458
@@ -10,6 +10,7 @@
   u8();
   P1();
   e1();
+  Y6();
   ((v$ = r(JA(), 1)), (A3A = { status: "idle" }));
   ((Ih6 = v$.default.createContext([{}, (A) => A])),
     (FYK = v$.default.createContext(!1)));

@@@ variable 'Wp6' (was 'NF6') — structural (86.2%)
--- pretty-v2.1.19.js:557193
+++ pretty-v2.1.20.js:562363
@@ -366,10 +366,7 @@
     {
       id: "guest-passes",
       content: async (A) => {
-        let K = F8("claude", A.theme);
-        return `┌──────────┐
-      ) CC ${K("✻")} ┊ (  You have free guest passes
-     └──────────┘ ${K("/passes")} to share`;
+        return `You have free guest passes to share · ${U8("claude", A.theme)("/passes")}`;
       },
       cooldownSessions: 3,
       isRelevant: async () => {

@@@ function 'AQ6' (was 'bD') — structural (86.1%)
--- pretty-v2.1.19.js:528475
+++ pretty-v2.1.20.js:533175
@@ -1,17 +1,13 @@
-async function bD(A = 0, K = !1) {
+async function AQ6(A, K) {
   let Y = FK();
   if (!K) {
     if (!Y?.refreshToken || !aF(Y.expiresAt)) return !1;
   }
   if (!Y?.refreshToken) return !1;
   if (!oF(Y.scopes)) return !1;
-  if (
-    (FK.cache?.clear?.(),
-    ro(),
-    (Y = FK()),
-    !Y?.refreshToken || !aF(Y.expiresAt))
-  )
-    return !1;
+  (lK.cache?.clear?.(), fa());
+  let z = await eF6();
+  if (!z?.refreshToken || !NQ(z.expiresAt)) return !1;
   let z = f8();
   hA().mkdirSync(z);
   let H;
@@ -41,19 +37,16 @@
     );
   }
   try {
-    if (
-      (FK.cache?.clear?.(),
-      ro(),
-      (Y = FK()),
-      !Y?.refreshToken || !aF(Y.expiresAt))
-    )
+    (lK.cache?.clear?.(), fa());
+    let O = await eF6();
+    if (!O?.refreshToken || !NQ(O.expiresAt))
       return (n("tengu_oauth_token_refresh_race_resolved", {}), !1);
     n("tengu_oauth_token_refresh_starting", {});
     let J = await qK6(Y.refreshToken);
     return (_jA(J), FK.cache?.clear?.(), ro(), !0);
   } catch (J) {
     (qA(J instanceof Error ? J : Error(String(J))), FK.cache?.clear?.(), ro());
-    let X = FK();
+    let X = await eF6();
     if (X && !aF(X.expiresAt))
       return (n("tengu_oauth_token_refresh_race_recovered", {}), !0);
     return !1;

@@@ function 'WO' (was 'GX') — structural (86.1%)
--- pretty-v2.1.19.js:526847
+++ pretty-v2.1.20.js:531525
@@ -27,8 +27,6 @@
         return `Tool '${K.permissionPromptToolName}' requires approval for this ${A} command`;
       case "sandboxOverride":
         return "Run outside of the sandbox";
-      case "classifier":
-        return `Classifier '${K.classifier}' requires approval for this ${A} command: ${K.reason}`;
       case "workingDir":
         return K.reason;
       case "other":

@@@ variable 'pz' (was 'Qz') — structural (86.0%)
--- pretty-v2.1.19.js:529809
+++ pretty-v2.1.20.js:534543
@@ -18,6 +18,7 @@
   OZ();
   so();
   ahA();
+  r6();
   ((fjK = r(FhA(), 1)),
     (du2 = [
       ".gitconfig",

@@@ function 'aRA' (was 'QLA') — structural (85.5%)
--- pretty-v2.1.19.js:173329
+++ pretty-v2.1.20.js:176304
@@ -22,6 +22,8 @@
         (A.styleIds[J] = A.emptyStyleId),
         (A.widths[J] = 2),
         (A.hyperlinkIds[J] = 0));
+      let O = A.damage;
+      if (O && H >= O.x + O.width) O.width = H - O.x + 1;
     }
   }
 }

@@@ function 'WE7' (was 'Xi7') — structural (85.5%)
--- pretty-v2.1.19.js:397806
+++ pretty-v2.1.20.js:333100
@@ -32,6 +32,7 @@
       firstLine:
         X.split(`
 `)[0] ?? null,
+      fileContent: O,
       style: w,
       verbose: H,
     });

@@@ function 'QB' (was 'Uu') — structural (85.5%)
--- pretty-v2.1.19.js:462413
+++ pretty-v2.1.20.js:420028
@@ -1,7 +1,8 @@
 async function Uu() {
   let [A] = PM2();
   if (r9()) {
-    if (eP1() || gS6()) return "package-manager";
+    if (XP1() || by6() || xy6() || uy6() || By6() || my6())
+      return "package-manager";
     return "native";
   }
   if (P9K()) return "npm-local";

@@@ function 'sXA' (was 'qOA') — structural (85.3%)
--- pretty-v2.1.19.js:202852
+++ pretty-v2.1.20.js:208637
@@ -134,7 +134,7 @@
     qA(Y);
     let z = n09(Y);
     n("tengu_image_resize_failed", { original_size_bytes: K, error_type: z });
-    let w = q === "jpg" ? "jpeg" : q,
+    let H = tXA(A).slice(6),
       H = Math.ceil((K * 4) / 3);
     if (H <= ZHA)
       return (

@@@ function 'hZK' (was 'NJK') — structural (85.1%)
--- pretty-v2.1.19.js:490383
+++ pretty-v2.1.20.js:493783
@@ -129,7 +129,8 @@
                 if (zA !== HA) return HA - zA;
                 return wA.entry.name.localeCompare(KA.entry.name);
               });
-            else s.sort((wA, KA) => wA.entry.name.localeCompare(KA.entry.name));
+            else
+              YA.sort((zA, AA) => zA.entry.name.localeCompare(AA.entry.name));
           } catch (AA) {
             (h(
               `Failed to fetch install counts: ${AA instanceof Error ? AA.message : String(AA)}`,

@@@ variable 'Q8A' (was 'j8A') — structural (84.7%)
--- pretty-v2.1.19.js:172257
+++ pretty-v2.1.20.js:175234
@@ -26,6 +26,7 @@
       text: "rgb(0,0,0)",
       inverseText: "rgb(255,255,255)",
       inactive: "rgb(102,102,102)",
+      inactiveShimmer: "rgb(142,142,142)",
       subtle: "rgb(175,175,175)",
       suggestion: "rgb(87,105,247)",
       remember: "rgb(0,0,255)",
@@ -75,6 +76,7 @@
       text: "ansi:black",
       inverseText: "ansi:white",
       inactive: "ansi:blackBright",
+      inactiveShimmer: "ansi:white",
       subtle: "ansi:blackBright",
       suggestion: "ansi:blue",
       remember: "ansi:blue",
@@ -124,6 +126,7 @@
       text: "ansi:whiteBright",
       inverseText: "ansi:black",
       inactive: "ansi:white",
+      inactiveShimmer: "ansi:whiteBright",
       subtle: "ansi:white",
       suggestion: "ansi:blueBright",
       remember: "ansi:blueBright",
@@ -173,6 +176,7 @@
       text: "rgb(0,0,0)",
       inverseText: "rgb(255,255,255)",
       inactive: "rgb(102,102,102)",
+      inactiveShimmer: "rgb(142,142,142)",
       subtle: "rgb(175,175,175)",
       suggestion: "rgb(51,102,255)",
       remember: "rgb(51,102,255)",
@@ -222,6 +226,7 @@
       text: "rgb(255,255,255)",
       inverseText: "rgb(0,0,0)",
       inactive: "rgb(153,153,153)",
+      inactiveShimmer: "rgb(193,193,193)",
       subtle: "rgb(80,80,80)",
       suggestion: "rgb(177,185,249)",
       remember: "rgb(177,185,249)",
@@ -271,6 +276,7 @@
       text: "rgb(255,255,255)",
       inverseText: "rgb(0,0,0)",
       inactive: "rgb(153,153,153)",
+      inactiveShimmer: "rgb(193,193,193)",
       subtle: "rgb(80,80,80)",
       suggestion: "rgb(153,204,255)",
       remember: "rgb(153,204,255)",

@@@ function 'sZ1' (was 'CW1') — structural (84.6%)
--- pretty-v2.1.19.js:390201
+++ pretty-v2.1.20.js:338900
@@ -3,6 +3,5 @@
     return parseInt(process.env.MAX_THINKING_TOKENS, 10) > 0;
   let { settings: A } = Hv();
   if (A.alwaysThinkingEnabled === !1) return !1;
-  if (A.alwaysThinkingEnabled === !0) return dp7(dq());
   return dp7(dq());
 }

@@@ function 'Nd' (was 'gp') — structural (84.5%)
--- pretty-v2.1.19.js:450907
+++ pretty-v2.1.20.js:461722
@@ -38,18 +38,7 @@
       return VjA.has(W) || $.has(W);
     },
     Z = new Set();
-  if (($.size > 0, $.size > 0))
-    A.filter(
-      (D) =>
-        D &&
-        D.type === "attachment" &&
-        D.attachment.type === "memory" &&
-        !fjA.has(D.uuid),
-    )
-      .map((D) => ({ uuid: D.uuid }))
-      .forEach((D) => {
-        (fjA.add(D.uuid), Z.add(D.uuid));
-      });
+  $.size > 0;
   let G = [];
   for (let W of A) {
     if (W.type === "attachment" && fjA.has(W.uuid)) continue;

@@@ function 'SE7' (was 'Ri7') — structural (84.5%)
--- pretty-v2.1.19.js:399050
+++ pretty-v2.1.20.js:334305
@@ -27,6 +27,7 @@
       operation: "update",
       patch: O,
       firstLine: $,
+      fileContent: O,
       style: q,
       verbose: Y,
     });

@@@ function 'GL2' (was 'a62') — structural (84.3%)
--- pretty-v2.1.19.js:388112
+++ pretty-v2.1.20.js:462808
@@ -67,7 +67,9 @@
    - Run a git diff command to see both staged and unstaged changes that will be committed
    - Check if the current branch tracks a remote branch and is up to date with the remote, so you know if you need to push to the remote
    - Run a git log command and \`git diff [base-branch]...HEAD\` to understand the full commit history for the current branch (from the time it diverged from the base branch)
-2. Analyze all changes that will be included in the pull request, making sure to look at all relevant commits (NOT just the latest commit, but ALL commits that will be included in the pull request!!!), and draft a pull request summary
+2. Analyze all changes that will be included in the pull request, making sure to look at all relevant commits (NOT just the latest commit, but ALL commits that will be included in the pull request!!!), and draft a pull request title and summary:
+   - Keep the PR title short (under 70 characters)
+   - Use the description/body for details, not the title
 3. ${A} run the following commands in parallel:
    - Create new branch if needed
    - Push to remote with -u flag if needed

@@@ variable 'ZjA' (was 'LDA') — structural (84.1%)
--- pretty-v2.1.19.js:416484
+++ pretty-v2.1.20.js:443621
@@ -36,6 +36,10 @@
       return "Fetch";
     },
     getToolUseSummary: pa7,
+    getActivityDescription(A) {
+      let K = Eh6(A);
+      return K ? `Fetching ${K}` : "Fetching web page";
+    },
     isEnabled() {
       return !0;
     },

@@@ function 'Zv2' (was 'A$2') — structural (84.1%)
--- pretty-v2.1.19.js:432655
+++ pretty-v2.1.20.js:449699
@@ -65,6 +65,15 @@
         },
       ]
     );
+  if (A.name === k7 && _.data && "command" in _.data) {
+    let R = await Y.getAppState();
+    N7K(
+      _.data.command,
+      R.toolPermissionContext,
+      Y.abortController.signal,
+      Y.options.isNonInteractiveSession,
+    );
+  }
   let G = [],
     W = _.data,
     D = !1,
@@ -119,14 +128,14 @@
     M !== void 0 &&
     M.behavior === "allow" &&
     !A.requiresUserInteraction?.() &&
-    !Y.agentId
+    !Y.requireCanUseTool
   )
     (h(`Hook approved tool use for ${A.name}, bypassing permission check`),
       (V = M));
   else if (
     M !== void 0 &&
     M.behavior === "allow" &&
-    (A.requiresUserInteraction?.() || Y.agentId)
+    (A.requiresUserInteraction?.() || Y.requireCanUseTool)
   ) {
     if (
       (h(`Hook approved tool use for ${A.name}, but canUseTool is required`),
@@ -282,7 +291,10 @@
       ...(J ? { requestId: J } : {}),
     }),
       P47(A.name));
-    let Q = xC(A) ? TW6(A.name) : null;
+    let F = cT(A) ? wM6(A.name) : null,
+      Q = u56(),
+      u = Q ? B56(A.name) : void 0,
+      d = Q ? m56(A.name, W) : void 0;
     RZ("tool_result", {
       tool_name: VK(A.name),
       success: "true",
@@ -290,7 +302,11 @@
       ...(Object.keys(N).length > 0 && { tool_parameters: UA(N) }),
       tool_result_size_bytes: String(g),
       ...(T && { decision_source: T.source, decision_type: T.decision }),
-      ...(Q && { mcp_server_scope: Q }),
+      ...(F ? { mcp_server_scope: F } : {}),
+      ...(u
+        ? { mcp_server_name: u.serverName, mcp_tool_name: u.mcpToolName }
+        : {}),
+      ...(d ? { skill_name: d } : {}),
     });
     let F = R.data,
       B = [],
@@ -369,7 +385,10 @@
         ...(O ? { mcpServerBaseUrl: O } : {}),
         ...(J ? { requestId: J } : {}),
       });
-      let Q = xC(A) ? TW6(A.name) : null;
+      let F = cT(A) ? wM6(A.name) : null,
+        Q = u56(),
+        u = Q ? B56(A.name) : void 0,
+        d = Q ? m56(A.name, W) : void 0;
       RZ("tool_result", {
         tool_name: VK(A.name),
         use_id: K,
@@ -378,7 +397,11 @@
         error: R instanceof Error ? R.message : String(R),
         ...(Object.keys(N).length > 0 && { tool_parameters: UA(N) }),
         ...(T && { decision_source: T.source, decision_type: T.decision }),
-        ...(Q && { mcp_server_scope: Q }),
+        ...(F ? { mcp_server_scope: F } : {}),
+        ...(u
+          ? { mcp_server_name: u.serverName, mcp_tool_name: u.mcpToolName }
+          : {}),
+        ...(d ? { skill_name: d } : {}),
       });
     }
     let S = WM1(R),

@@@ function 'tEK' (was 'vZ1') — structural (84.1%)
--- pretty-v2.1.19.js:361605
+++ pretty-v2.1.20.js:540889
@@ -7,7 +7,7 @@
   let w = z,
     H;
   if (K[2] !== q)
-    ((H = p5A.createElement(f, { bold: !0 }, q)), (K[2] = q), (K[3] = H));
+    ((H = g9A.createElement(f, { bold: !0 }, "@", q)), (K[2] = q), (K[3] = H));
   else H = K[3];
   let J;
   if (K[4] !== w || K[5] !== H)

@@@ variable 'P3A' (was 'SQA') — structural (83.3%)
--- pretty-v2.1.19.js:464448
+++ pretty-v2.1.20.js:422356
@@ -51,4 +51,5 @@
     "BLOCK_SIZE",
     "BLOCKSIZE",
   ]);
+  KI6 = new Map();
 });

@@@ function 'Q9Y' (was 'm6Y') — structural (83.1%)
--- pretty-v2.1.19.js:265336
+++ pretty-v2.1.20.js:264258
@@ -1,6 +1,6 @@
-function m6Y(A, K, q) {
+function Q9Y(A, K, q, Y) {
   return {
-    uuid: `UUID-${q}`,
+    uuid: Y ?? `UUID-${q}`,
     requestId: "REQUEST_ID",
     timestamp: A.timestamp,
     message: {

@@@ function 'ih6' (was 'qR6') — structural (83.1%)
--- pretty-v2.1.19.js:425162
+++ pretty-v2.1.20.js:448806
@@ -12,6 +12,7 @@
   if (Y) H.push({ text: Y, cacheScope: null });
   if (z) H.push({ text: z, cacheScope: "org" });
   let J = w.join(`
+
 `);
   if (J) H.push({ text: J, cacheScope: "org" });
   return H;

@@@ function 'v9A' (was 'o3A') — structural (83.0%)
--- pretty-v2.1.19.js:507066
+++ pretty-v2.1.20.js:510823
@@ -1,5 +1,4 @@
 function o3A(A) {
-  if (A.type === "in_process_teammate") return !1;
   if (A.status !== "running" && A.status !== "pending") return !1;
   if ("isBackgrounded" in A && A.isBackgrounded === !1) return !1;
   return !0;

@@@ function 'skK' (was 'LVK') — structural (82.9%)
--- pretty-v2.1.19.js:541593
+++ pretty-v2.1.20.js:546681
@@ -1,6 +1,6 @@
 function LVK(A) {
-  let K = a(15),
-    { toolUseConfirm: q, onDone: Y, onReject: z } = A,
+  let K = s(18),
+    { toolUseConfirm: q, onDone: Y, onReject: z, workerBadge: w } = A,
     [w] = j6(),
     H;
   if (K[0] !== w || K[1] !== Y || K[2] !== z || K[3] !== q)
@@ -95,27 +95,30 @@
   if (K[12] !== J || K[13] !== G)
     ((W = KN.default.createElement(
       P2,
-      { color: "planMode", title: "Enter plan mode?" },
+      { flexDirection: "column", marginTop: 1, paddingX: 1 },
+      X,
+      $,
+      _,
       KN.default.createElement(
         I,
-        { flexDirection: "column", marginTop: 1, paddingX: 1 },
-        X,
-        O,
-        $,
-        KN.default.createElement(
-          I,
-          { marginTop: 1 },
-          KN.default.createElement(T6, {
-            options: Z,
-            onChange: J,
-            onCancel: G,
-          }),
-        ),
+        { marginTop: 1 },
+        HN.default.createElement(y6, { options: G, onChange: O, onCancel: W }),
       ),
     )),
       (K[12] = J),
       (K[13] = G),
       (K[14] = W));
   else W = K[14];
+  let M;
+  if (K[15] !== D || K[16] !== w)
+    ((M = HN.default.createElement(
+      Iw,
+      { color: "planMode", title: "Enter plan mode?", workerBadge: w },
+      D,
+    )),
+      (K[15] = D),
+      (K[16] = w),
+      (K[17] = M));
+  else M = K[17];
   return W;
 }

@@@ function '$Y' (was 'OY') — structural (82.7%)
--- pretty-v2.1.19.js:468258
+++ pretty-v2.1.20.js:471378
@@ -43,11 +43,12 @@
         (X, O) => {
           h(`Settings changed from ${X}, updating AppState`);
           let $ = _tA();
-          H((_) => {
-            let Z = QYK(_.toolPermissionContext, $);
-            if (Z.isBypassPermissionsModeAvailable && gQA()) Z = FQA(Z);
-            return { ..._, settings: O, toolPermissionContext: Z };
-          });
+          (vqA(),
+            H((_) => {
+              let Z = Q0K(_.toolPermissionContext, $);
+              if (Z.isBypassPermissionsModeAvailable && lUA()) Z = iUA(Z);
+              return { ..._, settings: X, toolPermissionContext: Z };
+            }));
         },
         [H],
       ),

@@@ variable 'P_' (was '$_') — structural (82.5%)
--- pretty-v2.1.19.js:527104
+++ pretty-v2.1.20.js:531774
@@ -8,7 +8,10 @@
           decisionReason: { type: "mode", mode: "dontAsk" },
           message: L3K(A.name),
         };
-      if (H.toolPermissionContext.shouldAvoidPermissionPrompts)
+      if (
+        (H.toolPermissionContext.mode,
+        H.toolPermissionContext.shouldAvoidPermissionPrompts)
+      )
         return {
           behavior: "deny",
           decisionReason: {

@@@ variable 'uZ7' (was 'H$7') — structural (82.4%)
--- pretty-v2.1.19.js:307598
+++ pretty-v2.1.20.js:303911
@@ -16,6 +16,9 @@
         }
       return null;
     },
+    async readAsync() {
+      return this.read();
+    },
     update(A) {
       try {
         let { storageDir: K, storagePath: q } = SW6();

@@@ variable 'mh6' (was 'sC6') — structural (82.1%)
--- pretty-v2.1.19.js:419631
+++ pretty-v2.1.20.js:446839
@@ -15,7 +15,7 @@
         return "Requests permission to enter plan mode for complex tasks requiring exploration and design";
       },
       async prompt() {
-        return rs7;
+        return hYK();
       },
       inputSchema: Z22,
       outputSchema: G22,

@@@ variable 't2' (was 'o2') — structural (81.8%)
--- pretty-v2.1.19.js:438925
+++ pretty-v2.1.20.js:389501
@@ -20,8 +20,6 @@
   mx7();
   x9();
   xy6();
-  Up();
-  SV();
   ((h4 = r(JA(), 1)),
     (Mv = r(JA(), 1)),
     (y4K = YmA()),

@@@ variable 'rT' (was 'mB') — structural (81.8%)
--- pretty-v2.1.19.js:449689
+++ pretty-v2.1.20.js:460450
@@ -38,7 +38,6 @@
   eH();
   F2();
   Gv();
-  uX();
   ((XP1 = { TURNS_SINCE_WRITE: 10, TURNS_BETWEEN_REMINDERS: 10 }),
     (S5K = {
       TURNS_BETWEEN_ATTACHMENTS: 5,

@@@ variable 'nqA' (was 'Rs') — structural (81.7%)
--- pretty-v2.1.19.js:399165
+++ pretty-v2.1.20.js:334430
@@ -63,8 +63,12 @@
       },
       userFacingName: ki7,
       getToolUseSummary: Ci7,
+      getActivityDescription(A) {
+        let K = Gf6(A);
+        return K ? `Writing ${K}` : "Writing file";
+      },
       async prompt() {
-        return jL8;
+        return _b8();
       },
       isEnabled() {
         return !0;
@@ -101,7 +105,7 @@
           };
         if (!hA().existsSync(q)) return { result: !0 };
         let H = K.readFileState.get(q);
-        if (!H)
+        if (!H && !i4("tengu_marble_kite", !1))
           return {
             result: !1,
             message:
@@ -144,7 +148,8 @@
           let V = Aj(J),
             N = q.get(J);
           if (!N || V > N.timestamp)
-            if (N && N.offset === void 0 && N.limit === void 0) {
+            if (!N && i4("tengu_marble_kite", !1));
+            else if (N && N.offset === void 0 && N.limit === void 0) {
               let k = SO(J);
               if (
                 O.readFileSync(J, { encoding: k }).replaceAll(

@@@ variable 'P2K' (was 'ut7') — structural (81.5%)
--- pretty-v2.1.19.js:420412
+++ pretty-v2.1.20.js:447583
@@ -4,30 +4,32 @@
   uX();
   x9();
   F2();
-  eH();
-  ((E22 = U.strictObject({
-    taskId: U.string().describe("The ID of the task to update"),
-    subject: U.string().optional().describe("New subject for the task"),
-    description: U.string().optional().describe("New description for the task"),
-    activeForm: U.string()
-      .optional()
-      .describe(
-        'Present continuous form shown in spinner when in_progress (e.g., "Running tests")',
-      ),
-    status: w8A.optional().describe("New status for the task"),
-    addBlocks: U.array(U.string())
-      .optional()
-      .describe("Task IDs that this task blocks"),
-    addBlockedBy: U.array(U.string())
-      .optional()
-      .describe("Task IDs that block this task"),
-    owner: U.string().optional().describe("New owner for the task"),
-    metadata: U.record(U.string(), U.unknown())
-      .optional()
-      .describe(
-        "Metadata keys to merge into the task. Set a key to null to delete it.",
-      ),
-  })),
+  ((QT2 = y8A.or(U.literal("deleted"))),
+    (UT2 = U.strictObject({
+      taskId: U.string().describe("The ID of the task to update"),
+      subject: U.string().optional().describe("New subject for the task"),
+      description: U.string()
+        .optional()
+        .describe("New description for the task"),
+      activeForm: U.string()
+        .optional()
+        .describe(
+          'Present continuous form shown in spinner when in_progress (e.g., "Running tests")',
+        ),
+      status: QT2.optional().describe("New status for the task"),
+      addBlocks: U.array(U.string())
+        .optional()
+        .describe("Task IDs that this task blocks"),
+      addBlockedBy: U.array(U.string())
+        .optional()
+        .describe("Task IDs that block this task"),
+      owner: U.string().optional().describe("New owner for the task"),
+      metadata: U.record(U.string(), U.unknown())
+        .optional()
+        .describe(
+          "Metadata keys to merge into the task. Set a key to null to delete it.",
+        ),
+    })),
     (k22 = U.object({
       success: U.boolean(),
       taskId: U.string(),
@@ -104,6 +106,10 @@
         if (Y !== void 0 && Y !== _.activeForm)
           ((G.activeForm = Y), Z.push("activeForm"));
         if (w !== void 0 && w !== _.owner) ((G.owner = w), Z.push("owner"));
+        if (j8() && z === "in_progress" && w === void 0 && !_.owner) {
+          let W = I9();
+          if (W) ((G.owner = W), Z.push("owner"));
+        }
         if (X !== void 0) {
           let W = { ...(_.metadata ?? {}) };
           for (let [D, j] of Object.entries(X))
@@ -111,19 +117,20 @@
             else W[D] = j;
           ((G.metadata = W), Z.push("metadata"));
         }
-        if (z !== void 0 && z !== _.status) {
-          if (!i16.includes(z)) {
-            let W = i16.join(", ");
+        if (z !== void 0) {
+          if (z === "deleted") {
+            let W = gw4($, A);
             return {
               data: {
-                success: !1,
+                success: W,
                 taskId: A,
-                updatedFields: [],
-                error: `Invalid status "${z}". Valid statuses: ${W}`,
+                updatedFields: W ? ["deleted"] : [],
+                error: W ? void 0 : "Failed to delete task",
+                statusChange: W ? { from: _.status, to: "deleted" } : void 0,
               },
             };
           }
-          ((G.status = z), Z.push("status"));
+          if (z !== _.status) ((G.status = z), Z.push("status"));
         }
         if (Object.keys(G).length > 0) S0A($, A, G);
         if (G.owner && P8()) {

@@@ function 'hZ7' (was 'Y$7') — structural (81.4%)
--- pretty-v2.1.19.js:307473
+++ pretty-v2.1.20.js:303763
@@ -6,6 +6,11 @@
       if (q !== null && q !== void 0) return q;
       return K.read() || {};
     },
+    async readAsync() {
+      let q = await A.readAsync();
+      if (q !== null && q !== void 0) return q;
+      return (await K.readAsync()) || {};
+    },
     update(q) {
       let Y = A.read(),
         z = A.update(q);

@@@ variable 'oH' (was 'eH') — structural (81.4%)
--- pretty-v2.1.19.js:383036
+++ pretty-v2.1.20.js:407706
@@ -6,6 +6,7 @@
   F2();
   uX();
   F1();
+  B1();
   CWA = r(Ch(), 1);
   pQ7 = U.object({
     type: U.literal("mode_set_request"),

@@@ function 'QkK' (was 'jVK') — structural (81.3%)
--- pretty-v2.1.19.js:539997
+++ pretty-v2.1.20.js:545040
@@ -1,5 +1,5 @@
 function jVK(A) {
-  let K = a(27),
+  let K = s(28),
     q = qU2,
     Y;
   if (K[0] !== A.toolUseConfirm.input)
@@ -15,6 +15,7 @@
     $ = A.toolUseContext,
     _ = A.onDone,
     Z = A.onReject,
+    G = A.workerBadge,
     G = J ? "Overwrite file" : "Create file",
     W;
   if (K[2] !== w) ((W = AU2(m1(), w)), (K[2] = w), (K[3] = W));
@@ -60,17 +61,19 @@
     K[18] !== A.onReject ||
     K[19] !== A.toolUseConfirm ||
     K[20] !== A.toolUseContext ||
-    K[21] !== P ||
+    K[21] !== A.workerBadge ||
     K[22] !== V ||
     K[23] !== G ||
     K[24] !== W ||
-    K[25] !== M
+    K[25] !== W ||
+    K[26] !== D
   )
     ((N = cpA.default.createElement(Jm, {
       toolUseConfirm: O,
       toolUseContext: $,
       onDone: _,
       onReject: Z,
+      workerBadge: G,
       title: G,
       subtitle: W,
       question: M,
@@ -86,12 +89,13 @@
       (K[18] = A.onReject),
       (K[19] = A.toolUseConfirm),
       (K[20] = A.toolUseContext),
-      (K[21] = P),
+      (K[21] = A.workerBadge),
       (K[22] = V),
       (K[23] = G),
       (K[24] = W),
       (K[25] = M),
-      (K[26] = N));
-  else N = K[26];
+      (K[26] = D),
+      (K[27] = T));
+  else T = K[27];
   return N;
 }

@@@ function 'JI6' (was 'wh6') — structural (81.2%)
--- pretty-v2.1.19.js:464123
+++ pretty-v2.1.20.js:422029
@@ -18,7 +18,8 @@
   }
   let w = zh6(A, Y.toolPermissionContext);
   if (w.behavior === "deny") return w;
-  if (NS()) {
+  let H = !1;
+  if (UB() && !H) {
     let N = l9K(Y.toolPermissionContext);
     if (N.length > 0) {
       let T = await XV1(
@@ -41,7 +42,7 @@
         };
     }
   }
-  if (NS()) {
+  if (UB() && !H) {
     let N = i9K(Y.toolPermissionContext);
     if (N.length > 0) {
       let T = await XV1(

@@@ function 'GWA' (was 'ADA') — structural (81.1%)
--- pretty-v2.1.19.js:397583
+++ pretty-v2.1.20.js:332872
@@ -1,10 +1,11 @@
 function ADA(A) {
-  let K = a(41),
+  let K = s(43),
     {
       file_path: q,
       operation: Y,
       patch: z,
       firstLine: w,
+      fileContent: H,
       content: H,
       style: J,
       verbose: X,
@@ -104,9 +105,9 @@
     return M;
   }
   let D;
-  if (K[29] !== O || K[30] !== q || K[31] !== w || K[32] !== z) {
+  if (K[29] !== $ || K[30] !== H || K[31] !== q || K[32] !== w || K[33] !== z) {
     let M;
-    if (K[34] !== O || K[35] !== q || K[36] !== w)
+    if (K[35] !== $ || K[36] !== H || K[37] !== q || K[38] !== w)
       ((M = (P) =>
         f2.createElement(
           I,
@@ -117,30 +118,33 @@
             width: O - 12,
             filePath: q,
             firstLine: w,
+            fileContent: H,
           }),
         )),
-        (K[34] = O),
         (K[35] = q),
         (K[36] = w),
-        (K[37] = M));
-    else M = K[37];
+        (K[37] = q),
+        (K[38] = w),
+        (K[39] = P));
+    else P = K[39];
     ((D = Sf(z.map(M), CK2)),
       (K[29] = O),
       (K[30] = q),
       (K[31] = w),
       (K[32] = z),
-      (K[33] = D));
-  } else D = K[33];
+      (K[33] = z),
+      (K[34] = M));
+  } else M = K[34];
   let j;
-  if (K[38] !== D || K[39] !== W)
+  if (K[40] !== M || K[41] !== D)
     ((j = f2.createElement(
       v6,
       null,
       f2.createElement(I, { flexDirection: "column" }, W, D),
     )),
-      (K[38] = D),
-      (K[39] = W),
-      (K[40] = j));
-  else j = K[40];
+      (K[40] = M),
+      (K[41] = D),
+      (K[42] = j));
+  else j = K[42];
   return j;
 }

@@@ variable 'zP' (was 'YP') — structural (81.0%)
--- pretty-v2.1.19.js:526605
+++ pretty-v2.1.20.js:531204
@@ -6,6 +6,7 @@
   IDK();
   q6();
   Uq();
+  l5();
   IQA = /^cd(?:\s|$)/;
   NpA = new Set(["0", "1", "2"]);
   AYK = w6(
@@ -41,13 +42,8 @@
             ),
           );
         }, 1e4);
-        let H = await J$({
-          systemPrompt: [
-            `Your task is to process Bash commands that an AI coding agent wants to run.
-
-This policy spec defines how to determine the prefix of a Bash command:`,
-          ],
-          userPrompt: `<policy_spec>
+        let H = i4("tengu_cork_m4q", !1),
+          J = `<policy_spec>
 # Claude Code Code Bash command prefix detection
 
 This document defines risk levels for actions that the Claude Code agent may take. This classification system is part of a broader safety framework and is used to determine when additional user confirmation or oversight may be needed.
@@ -102,27 +98,41 @@
 The prefix must be a string prefix of the full command.
 
 IMPORTANT: Bash commands may run multiple commands that are chained together.
-For safety, if the command seems to contain command injection, you must return "command_injection_detected". 
-(This will help protect the user: if they think that they're allowlisting command A, 
-but the AI coding agent sends a malicious command that technically has the same prefix as command A, 
-then the safety system will see that you said “command_injection_detected” and ask the user for manual confirmation.)
+For safety, if the command seems to contain command injection, you must return "command_injection_detected".
+(This will help protect the user: if they think that they're allowlisting command A,
+but the AI coding agent sends a malicious command that technically has the same prefix as command A,
+then the safety system will see that you said "command_injection_detected" and ask the user for manual confirmation.)
 
 Note that not every command has a prefix. If a command has no prefix, return "none".
 
-ONLY return the prefix. Do not return any other text, markdown markers, or other content or formatting.
+ONLY return the prefix. Do not return any other text, markdown markers, or other content or formatting.`,
+          O = await Z$({
+            systemPrompt: H
+              ? [
+                  `Your task is to process Bash commands that an AI coding agent wants to run.
+
+${J}`,
+                ]
+              : [
+                  `Your task is to process Bash commands that an AI coding agent wants to run.
+
+This policy spec defines how to determine the prefix of a Bash command:`,
+                ],
+            userPrompt: H
+              ? `Command: ${A}`
+              : `${J}
 
-Command: ${A}
-`,
-          signal: K,
-          enablePromptCaching: !1,
-          options: {
-            querySource: "bash_extract_prefix",
-            agents: [],
-            isNonInteractiveSession: q,
-            hasAppendSystemPrompt: !1,
-            mcpTools: [],
-          },
-        });
+Command: ${A}`,
+            signal: K,
+            options: {
+              enablePromptCaching: H,
+              querySource: "bash_extract_prefix",
+              agents: [],
+              isNonInteractiveSession: q,
+              hasAppendSystemPrompt: !1,
+              mcpTools: [],
+            },
+          });
         clearTimeout(Y);
         let J = Date.now() - z,
           X =

@@@ class 'I51' (was 'SK1') — structural (80.7%)
--- pretty-v2.1.19.js:179154
+++ pretty-v2.1.20.js:182137
@@ -39,7 +39,6 @@
       (this.log = new w86({
         debug: A.debug,
         isTTY: A.stdout.isTTY || !1,
-        onFlicker: A.onFlicker,
         stylePool: this.stylePool,
       })),
       (this.scheduleRender = A.debug
@@ -63,7 +62,7 @@
         if (this.isUnmounted) return;
         if (this.rootNode.yogaNode)
           (this.rootNode.yogaNode.setWidth(this.terminalColumns),
-            this.rootNode.yogaNode.calculateLayout(void 0, void 0, H8A.LTR));
+            this.rootNode.yogaNode.calculateLayout(this.terminalColumns));
       }),
       (this.container = D8A.createContainer(
         this.rootNode,
@@ -114,7 +113,8 @@
   };
   onRender() {
     if (this.isUnmounted || this.isPaused) return;
-    let A = this.options.stdout.columns || 80,
+    let A = performance.now(),
+      K = this.options.stdout.columns || 80,
       K = this.options.stdout.rows || 24,
       q = this.renderer({
         frontFrame: this.frontFrame,
@@ -125,10 +125,19 @@
       }),
       Y = this.log.render(this.frontFrame, q);
     ((this.backFrame = this.frontFrame), (this.frontFrame = q));
+    let w = [];
     for (let z of Y)
       if (z.type === "clearTerminal")
-        this.options.onFlicker?.(q.screen.height, q.viewport.height, z.reason);
-    m86(this.terminal, F86(Y));
+        w.push({
+          desiredHeight: Y.screen.height,
+          availableHeight: Y.viewport.height,
+          reason: H.reason,
+        });
+    (GK6(this.terminal, DK6(z)),
+      this.options.onFrame?.({
+        durationMs: performance.now() - A,
+        flickers: w,
+      }));
   }
   pause() {
     (D8A.flushSyncFromReconciler(), this.onRender(), (this.isPaused = !0));
@@ -203,6 +212,7 @@
       ((this.isUnmounted = !0),
       this.scheduleRender.cancel?.(),
       D8A.updateContainer(null, this.container, null, Xg),
+      Qn.flushPassiveEffects(),
       eb.delete(this.options.stdout),
       A instanceof Error)
     )

@@@ function 'rq' (was 'o5') — structural (80.6%)
--- pretty-v2.1.19.js:467877
+++ pretty-v2.1.20.js:470990
@@ -23,8 +23,9 @@
       clearTimeout(Y),
       await q56(),
       kh6(),
+      Zu6(),
       Ch6(A));
   } catch {
-    (clearTimeout(Y), await q56(), kh6(), Ch6(A));
+    (clearTimeout(Y), await n56(), _u6(), Zu6(), Gu6(A));
   }
 }

@@@ variable 'AIK' (was 'LvK') — structural (80.5%)
--- pretty-v2.1.19.js:554906
+++ pretty-v2.1.20.js:560055
@@ -18,6 +18,7 @@
   x9();
   EFA();
   CFA();
+  sFA();
   ((kvK = r(JA(), 1)), (td2 = ["Edit", "Write", "NotebookEdit"]));
   CvK = Ac2;
 });

@@@ function 'vPK' (was '_ZK') — structural (80.1%)
--- pretty-v2.1.19.js:511888
+++ pretty-v2.1.20.js:515873
@@ -1,5 +1,5 @@
 function _ZK(A) {
-  let K = a(31),
+  let K = s(32),
     { selectedHook: q, eventSupportsMatcher: Y, onDelete: z, onCancel: w } = A,
     H;
   if (K[0] !== q.config) ((H = XP(q.config)), (K[0] = q.config), (K[1] = H));
@@ -69,28 +69,29 @@
       (K[22] = D));
   else D = K[22];
   let j;
-  if (K[23] !== W)
-    ((j = P_.createElement(T6, { onChange: W, options: D })),
+  if (K[23] !== w || K[24] !== W)
+    ((M = L_.createElement(y6, { onChange: W, onCancel: w, options: D })),
       (K[23] = W),
-      (K[24] = j));
-  else j = K[24];
+      (K[24] = W),
+      (K[25] = M));
+  else M = K[25];
   let M;
-  if (K[25] !== j || K[26] !== Z)
+  if (K[26] !== M || K[27] !== Z)
     ((M = P_.createElement(I, { flexDirection: "column", gap: 1 }, Z, G, j)),
-      (K[25] = j),
       (K[26] = Z),
-      (K[27] = M));
-  else M = K[27];
+      (K[27] = Z),
+      (K[28] = j));
+  else j = K[28];
   let P;
-  if (K[28] !== w || K[29] !== M)
+  if (K[29] !== w || K[30] !== j)
     ((P = P_.createElement(
       NK,
       { title: "Delete hook?", onCancel: w, borderDimColor: !1 },
       M,
     )),
-      (K[28] = w),
       (K[29] = M),
-      (K[30] = P));
-  else P = K[30];
+      (K[30] = j),
+      (K[31] = P));
+  else P = K[31];
   return P;
 }

@@@ class 'ZqA' (was 'nKA') — structural (80.1%)
--- pretty-v2.1.19.js:309077
+++ pretty-v2.1.20.js:305393
@@ -214,40 +214,54 @@
     return (h6(this.serverName, "Returning code verifier"), this._codeVerifier);
   }
   async refreshAuthorization(A) {
-    try {
-      h6(this.serverName, "Starting token refresh");
-      let K = APY(),
-        q = await KxA(new URL(this.serverConfig.url), { fetchFn: K });
-      if (!q) {
-        h6(this.serverName, "Failed to discover OAuth metadata");
+    for (let q = 1; q <= 3; q++)
+      try {
+        B6(this.serverName, "Starting token refresh");
+        let Y = JkY(),
+          z = await exA(new URL(this.serverConfig.url), { fetchFn: Y });
+        if (!z) {
+          B6(this.serverName, "Failed to discover OAuth metadata");
+          return;
+        }
+        let w = await this.clientInformation();
+        if (!w) {
+          B6(this.serverName, "No client information available");
+          return;
+        }
+        let H = await gG6(new URL(this.serverConfig.url), {
+          metadata: z,
+          clientInformation: w,
+          refreshToken: A,
+          resource: new URL(this.serverConfig.url),
+          fetchFn: Y,
+        });
+        if (H)
+          return (
+            B6(this.serverName, "Token refresh successful"),
+            await this.saveTokens(H),
+            H
+          );
+        B6(this.serverName, "Token refresh returned no tokens");
         return;
+      } catch (Y) {
+        let z =
+            Y instanceof Error &&
+            /timeout|timed out|etimedout|econnreset/i.test(Y.message),
+          w = Y instanceof Eu || Y instanceof LZA || Y instanceof RZA;
+        if (!(z || w) || q >= 3) {
+          B6(
+            this.serverName,
+            `Token refresh failed: ${Y instanceof Error ? Y.message : String(Y)}`,
+          );
+          return;
+        }
+        let J = 1000 * Math.pow(2, q - 1);
+        (B6(
+          this.serverName,
+          `Token refresh failed, retrying in ${J}ms (attempt ${q}/3)`,
+        ),
+          await new Promise((O) => setTimeout(O, J)));
       }
-      let Y = await this.clientInformation();
-      if (!Y) {
-        h6(this.serverName, "No client information available for refresh");
-        return;
-      }
-      let z = await JZ6(new URL(this.serverConfig.url), {
-        metadata: q,
-        clientInformation: Y,
-        refreshToken: A,
-        resource: new URL(this.serverConfig.url),
-        fetchFn: K,
-      });
-      if (z)
-        return (
-          h6(this.serverName, "Token refresh successful, saving new tokens"),
-          await this.saveTokens(z),
-          z
-        );
-      h6(this.serverName, "Token refresh returned no tokens");
-      return;
-    } catch (K) {
-      h6(
-        this.serverName,
-        `Token refresh failed: ${K instanceof Error ? K.message : String(K)}`,
-      );
-      return;
-    }
+    return;
   }
 }

@@@ class 'p56' (was 'sK6') — structural (80.1%)
--- pretty-v2.1.19.js:194471
+++ pretty-v2.1.20.js:193615
@@ -10,6 +10,7 @@
   backoffRetryTimer = null;
   backoffAttempt = 0;
   isRetrying = !1;
+  lastExportErrorContext;
   constructor(A = {}) {
     let K = process.env.ANTHROPIC_BASE_URL || "https://api.anthropic.com";
     ((this.endpoint = `${K}/api/event_logging/batch`),
@@ -28,19 +29,8 @@
   }
   async loadEventsFromFile(A) {
     try {
-      let q = (await Oz9(A, "utf8"))
-          .trim()
-          .split(
-            `
-`,
-          )
-          .filter(Boolean),
-        Y = [];
-      for (let z of q)
-        try {
-          Y.push(_6(z));
-        } catch {}
-      return Y;
+      let K = await x$9(A);
+      return K1A(K);
     } catch {
       return [];
     }
@@ -143,12 +133,14 @@
       }
       let z = await this.sendEventsInBatches(Y);
       if (z.length > 0) {
-        (await this.queueFailedEvents(z),
-          this.scheduleBackoffRetry(),
-          K({
-            code: w4A.ExportResultCode.FAILED,
-            error: Error(`Failed to export ${z.length} events`),
-          }));
+        (await this.queueFailedEvents(z), this.scheduleBackoffRetry());
+        let w = this.lastExportErrorContext
+          ? ` (${this.lastExportErrorContext})`
+          : "";
+        K({
+          code: T4A.ExportResultCode.FAILED,
+          error: Error(`Failed to export ${z.length} events${w}`),
+        });
         return;
       }
       if (
@@ -169,23 +161,29 @@
     let K = [];
     for (let Y = 0; Y < A.length; Y += this.maxBatchSize)
       K.push(A.slice(Y, Y + this.maxBatchSize));
-    let q = [];
+    let q = [],
+      Y;
     for (let Y = 0; Y < K.length; Y++) {
       let z = K[Y];
       try {
         await this.sendBatchWithRetry({ events: z });
-      } catch {
-        q.push(...z);
+      } catch (H) {
+        (q.push(...w), (Y = g$9(H)));
       }
       if (Y < K.length - 1 && this.batchDelayMs > 0)
         await new Promise((w) => setTimeout(w, this.batchDelayMs));
     }
+    if (q.length > 0 && Y) this.lastExportErrorContext = Y;
     return q;
   }
   async queueFailedEvents(A) {
     let K = this.getCurrentBatchFilePath();
-    (await this.appendEventsToFile(K, A),
-      qA(Error(`1P event logging: ${A.length} events failed to export`)));
+    await this.appendEventsToFile(K, A);
+    let q = this.lastExportErrorContext
+        ? ` (${this.lastExportErrorContext})`
+        : "",
+      Y = `1P event logging: ${A.length} events failed to export${q}`;
+    qA(Error(Y));
   }
   scheduleBackoffRetry() {
     if (this.backoffRetryTimer || this.isRetrying || this.isShutdown) return;

@@@ function 'XwK' (was 'J8K') — structural (80.0%)
--- pretty-v2.1.19.js:431220
+++ pretty-v2.1.20.js:455205
@@ -152,7 +152,7 @@
       querySource: "speculation",
       forkLabel: "speculation",
       maxTurns: LO2,
-      overrides: { abortController: z },
+      overrides: { abortController: z, requireCanUseTool: !0 },
       onMessage: (Z) => {
         if (Z.type === "assistant" || Z.type === "user") {
           if ((J.current.push(Z), J.current.length >= RO2)) z.abort();

@@@ function 'kPK' (was 'GZK') — structural (80.0%)
--- pretty-v2.1.19.js:511993
+++ pretty-v2.1.20.js:515979
@@ -31,9 +31,9 @@
       if (!X) continue;
       for (let O of H) {
         let $ = O.matcher || "";
-        if (!X[$]) X[$] = [];
         for (let _ of O.hooks)
-          if (_.type === "callback")
+          if (_.type === "callback") {
+            if (!O[$]) O[$] = [];
             X[$].push({
               event: J,
               config: { type: "command", command: "[Plugin Hook]" },
@@ -41,6 +41,16 @@
               source: "pluginHook",
               pluginName: O.pluginName,
             });
+          } else {
+            if (!O[$]) O[$] = [];
+            O[$].push({
+              event: J,
+              config: _,
+              matcher: X.matcher,
+              source: "pluginHook",
+              pluginName: X.pluginName,
+            });
+          }
       }
     }
   return q;

@@@ function '$F6' (was 'Tu6') — structural (79.7%)
--- pretty-v2.1.19.js:519464
+++ pretty-v2.1.20.js:523918
@@ -1,6 +1,6 @@
 function Tu6(A) {
   let { serverName: K, logger: q } = A,
-    Y = nGK(A),
+    Y = A.getSocketPaths ? OfK(A) : Vv1(A),
     z = new ZpA(
       { name: K, version: "1.0.0" },
       { capabilities: { tools: {}, logging: {} } },
@@ -21,9 +21,6 @@
         z.notification({ method: w.method, params: w.params }).catch((H) => {
           q.info(`[${K}] Failed to forward MCP notification: ${H.message}`);
         }));
-    }),
-    Y.ensureConnected().catch((w) => {
-      q.info(`[${K}] Initial socket connection failed:`, w);
     }),
     z
   );

@@@ function 'pPA' (was 'cMA') — structural (79.5%)
--- pretty-v2.1.19.js:522010
+++ pretty-v2.1.20.js:526453
@@ -7,6 +7,7 @@
     X = new Map(),
     O = 0,
     $ = {},
+    _ = void 0,
     _ = 20;
   for (let Z = 0; Z < A.length; Z += _) {
     let G = A.slice(Z, Z + _),
@@ -15,7 +16,7 @@
           try {
             if (q)
               try {
-                let M = z.statSync(D),
+                let P = await z.stat(M),
                   P = Ym(M.mtime);
                 if (dMA(P, q))
                   return {
@@ -120,5 +121,6 @@
     sessionStats: J,
     hourCounts: Object.fromEntries(X),
     totalMessages: O,
+    ...{},
   };
 }

@@@ function 'MH4' (was 'R34') — structural (79.4%)
--- pretty-v2.1.19.js:170686
+++ pretty-v2.1.20.js:170515
@@ -1,5 +1,5 @@
 function R34(A, K) {
-  if (K <= 0)
+  if (K <= 0 || !Number.isFinite(K))
     return A.split(`
 `).length;
   let q = 0;

@@@ function 'GE7' (was 'Ji7') — structural (79.3%)
--- pretty-v2.1.19.js:397789
+++ pretty-v2.1.20.js:333082
@@ -10,6 +10,7 @@
     firstLine:
       q.split(`
 `)[0] ?? null,
+    fileContent: q,
     style: z,
     verbose: w,
     previewHint: H ? "/plan to preview" : void 0,

@@@ function 'rM2' (was 'J82') — structural (79.3%)
--- pretty-v2.1.19.js:389092
+++ pretty-v2.1.20.js:424906
@@ -61,7 +61,7 @@
   await gp7(V, S, !M);
   let g = M ? "current" : Cf,
     b = M ? "current" : "swarm-view";
-  q((F) => ({
+  (q((Q) => ({
     ...F,
     teamContext: {
       ...F.teamContext,
@@ -81,7 +81,17 @@
         },
       },
     },
-  }));
+  })),
+    _KK(q, {
+      teammateId: W,
+      sanitizedName: G,
+      teamName: _,
+      teammateColor: P,
+      prompt: w,
+      plan_mode_required: O,
+      paneId: V,
+      insideTmux: j,
+    }));
   let Q = PW1(_);
   if (!Q)
     throw Error(

@@@ function 'PLK' (was 'tfK') — structural (79.2%)
--- pretty-v2.1.19.js:546139
+++ pretty-v2.1.20.js:551044
@@ -29,6 +29,19 @@
     [k] = j6(),
     R = Ek(),
     [x, S] = NH.useState(void 0),
+    B = mw.useMemo(() => {
+      if (H !== "prompt" || Z) return;
+      let zA = IE1(z, w);
+      if (!zA) return;
+      let AA = vU6(zA.partialCommand, A);
+      if (!AA) return;
+      return {
+        text: AA.suffix,
+        fullCommand: AA.fullCommand,
+        insertPosition: zA.startPos + 1 + zA.partialCommand.length,
+      };
+    }, [z, w, H, A, Z]),
+    x = Z ? void 0 : H === "prompt" ? B : b,
     g = NH.useRef(w);
   g.current = w;
   let b = NH.useRef(""),
@@ -83,23 +96,17 @@
         if (H === "prompt") {
           let HA = yg6(s, wA);
           if (HA) {
-            let vA = xfK(HA.partialCommand, A);
-            if (vA) {
-              (S({
-                text: vA.suffix,
-                fullCommand: vA.fullCommand,
-                insertPosition: HA.startPos + 1 + HA.partialCommand.length,
-              }),
-                X(() => ({
-                  commandArgumentHint: void 0,
-                  suggestions: [],
-                  selectedSuggestion: -1,
-                })),
+            if (vU6(ZA.partialCommand, A)) {
+              (O(() => ({
+                commandArgumentHint: void 0,
+                suggestions: [],
+                selectedSuggestion: -1,
+              })),
                 P("none"),
                 T(void 0));
               return;
-            } else S(void 0);
-          } else S(void 0);
+            }
+          }
         }
         if (H === "bash" && s.trim()) {
           F.current = s;
@@ -122,7 +129,7 @@
           } else S(void 0);
         }
         if (P8()) {
-          let HA = s.substring(0, wA).match(/(^|\s)@@([\w-]*)$/);
+          let ZA = zA.substring(0, t).match(/(^|\s)@([\w-]*)$/);
           if (HA && k.teamContext) {
             let vA = HA[2] ?? "",
               OA = Object.values(k.teamContext.teammates ?? {})
@@ -132,8 +139,8 @@
                 )
                 .map((LA) => ({
                   id: `dm-${LA.name}`,
-                  displayText: LA.name,
-                  description: "team member",
+                  displayText: `@${CA.name}`,
+                  description: "send message",
                 }));
             if (OA.length > 0) {
               (X((LA) => ({
@@ -275,7 +282,7 @@
           );
         if (M === "custom-title") o();
         if (M === "agent" && B.current.some((HA) => HA.id?.startsWith("dm-"))) {
-          if (!s.substring(0, wA).match(/(^|\s)@@[\w-]*$/)) o();
+          if (!zA.substring(0, t).match(/(^|\s)@([\w-]*)$/)) e();
         }
         if (KA && H !== "bash") {
           let HA = Sd(s, wA, !0);
@@ -339,10 +346,9 @@
             wA = z.slice(s.startPos + s.token.length),
             KA = AA + "/" + x.fullCommand + " " + wA,
             zA = s.startPos + 1 + x.fullCommand.length + 1;
-          (K(KA), Y(zA), S(void 0));
+          (K($A), Y(vA));
           return;
         }
-        S(void 0);
       }
       if (O.length > 0) {
         (o7("tab-completion"), e.cancel());
@@ -393,13 +399,13 @@
         ) {
           let wA = O[s];
           if (wA) {
-            let zA = z.slice(0, w).match(/(^|\s)@@[\w-]*$/);
+            let vA = z.slice(0, w).match(/(^|\s)@[\w-]*$/);
             if (zA && zA.index !== void 0) {
               let HA = zA.index + (zA[1]?.length ?? 0),
                 vA = z.slice(0, HA),
                 OA = z.slice(w),
-                LA = vA + "@@" + wA.displayText + " " + OA;
-              (K(LA), Y(vA.length + 2 + wA.displayText.length + 1), o());
+                CA = LA + t.displayText + " " + mA;
+              (K(CA), Y(LA.length + t.displayText.length + 1), e());
             }
           }
         } else if (M === "file" && O.length > 0) {
@@ -490,13 +496,13 @@
           (gg6(AA, z, w, K, Y, wA?.completionType), e.cancel(), o());
         }
       } else if (M === "agent" && $ < O.length && s?.id?.startsWith("dm-")) {
-        let wA = z.slice(0, w).match(/(^|\s)@@[\w-]*$/);
+        let t = z.slice(0, w).match(/(^|\s)@[\w-]*$/);
         if (wA && wA.index !== void 0) {
           let KA = wA.index + (wA[1]?.length ?? 0),
             zA = z.slice(0, KA),
             HA = z.slice(w),
-            vA = zA + "@@" + s.displayText + " " + HA;
-          (K(vA), Y(zA.length + 2 + s.displayText.length + 1), e.cancel(), o());
+            LA = vA + zA.displayText + " " + ZA;
+          (K(LA), Y(vA.length + zA.displayText.length + 1), OA.cancel(), e());
         }
       } else if (M === "file" && $ < O.length) {
         let AA = Sd(z, w, !0);
@@ -524,7 +530,9 @@
             let zA = z.indexOf(" "),
               HA = z.slice(0, zA + 1),
               vA =
-                yT1(s.metadata) && s.metadata.type === "directory" ? "/" : " ";
+                SE1(zA.metadata) && zA.metadata.type === "directory"
+                  ? "/"
+                  : " ";
             ((wA = HA + s.id + vA), (KA = wA.length), K(wA), Y(KA));
           } else {
             let HA = Sd(z, w, !0) ?? Sd(z, w, !1);

@@@ variable 'r0' (was 'uX') — structural (79.2%)
--- pretty-v2.1.19.js:159264
+++ pretty-v2.1.20.js:161091
@@ -8,9 +8,9 @@
   P1();
   F1();
   F2();
+  MT();
   ((Uq4 = r(Ch(), 1)), (p16 = new Set()));
-  ((i16 = ["pending", "in_progress", "completed"]),
-    (w8A = U.enum(["pending", "in_progress", "completed"])),
+  ((y8A = U.enum(["pending", "in_progress", "completed"])),
     (Sm3 = U.object({
       id: U.string(),
       subject: U.string(),

@@@ function 'TwK' (was 'f8K') — structural (78.9%)
--- pretty-v2.1.19.js:450793
+++ pretty-v2.1.20.js:461608
@@ -1,10 +1,10 @@
-async function f8K(A, K, q) {
+async function TwK(A, K, q, Y) {
   if (E1(process.env.DISABLE_COMPACT)) return { wasCompacted: !1 };
   if (!(await hW2(A, q))) return { wasCompacted: !1 };
   let z = await MP1(A, K.agentId, $qK());
   if (z) return (O3A(void 0), { wasCompacted: !0, compactionResult: z });
   try {
-    let w = await _P1(A, K, !0, void 0, !0);
+    let H = await Lf1(A, K, q, !0, void 0, !0);
     return (O3A(void 0), { wasCompacted: !0, compactionResult: w });
   } catch (w) {
     if (!ofA(w, _qA)) qA(w instanceof Error ? w : Error(String(w)));

@@@ function 'URK' (was 'jTK') — structural (78.7%)
--- pretty-v2.1.19.js:550988
+++ pretty-v2.1.20.js:556112
@@ -3,7 +3,7 @@
   return DTK.useMemo(() => {
     if (A !== "") return;
     if (q)
-      return `Message ${q.length > WTK ? q.slice(0, WTK - 3) + "..." : q}…`;
+      return `Message @${q.length > FRK ? q.slice(0, FRK - 3) + "..." : q}…`;
     if (Y.length > 0 && (f1().queuedCommandUpHintCount || 0) < $d2)
       return "Press up to edit queued messages";
     if (K < 1 && z) return ZTK();

@@@ function 't9A' (was 'N9A') — structural (78.6%)
--- pretty-v2.1.19.js:561088
+++ pretty-v2.1.20.js:566264
@@ -125,7 +125,6 @@
   let [NA, cA] = K8.useState(null),
     [z1, dA] = K8.useState(N?.hasInitialPrompt ?? !1),
     [iA, V1] = K8.useState(0),
-    [v1, g1] = K8.useState(null),
     [g6, k8] = K8.useState(void 0),
     w8 = K8.useRef(0),
     f4 = K8.useRef(0),
@@ -136,9 +135,7 @@
         ((w8.current = Date.now()),
           (f4.current = 0),
           (C4.current = null),
-          V1(0),
-          g1(null));
-      else g1(Date.now());
+          j1(0));
     }, []);
   zY(() => {
     if (!z1) return;
@@ -176,15 +173,16 @@
     }, []),
     [i7, SK] = K8.useState([]),
     [rq, c3] = K8.useState([]),
-    hK = i7.length > 0 || k.pendingWorkerRequest || k.pendingSandboxRequest;
+    Z5 = I8.length > 0 || k.pendingWorkerRequest || k.pendingSandboxRequest,
+    J3 = f4?.isLocalJSXCommand === !0;
   (K8.useEffect(() => {
-    if (z1 && !hK) CO7();
+    if (q1 && !Z5 && !J3) KZ7();
     else exA();
     return () => exA();
-  }, [z1, hK]),
+  }, [q1, Z5, J3]),
     K8.useEffect(() => {
-      if (z1 && !hK) return (fPK(), () => NPK());
-    }, [z1, hK]),
+      if (q1 && !Z5 && !J3) return (nEK(), () => rEK());
+    }, [q1, Z5, J3]),
     K8.useEffect(() => {
       return (F8K(SK), () => U8K());
     }, [SK]));
@@ -261,12 +259,18 @@
       resetLoadingState: cY,
       setAbortController: cA,
     }),
+    I_ = cj1(k.tasks).some((P6) => P6.status === "running"),
     $6 =
       (!Y7 || Y7.showSpinner === !0) &&
       i7.length === 0 &&
-      (z1 || g6) &&
+      (q1 || T1 || I_) &&
       !k.pendingWorkerRequest,
-    V8 = OEK(e4, z1, jK),
+    v8 =
+      I8.length > 0 ||
+      jK.length > 0 ||
+      k.elicitation.queue.length > 0 ||
+      k.workerSandboxPermissions.queue.length > 0,
+    l4 = xIK(S4, q1, N3, "session", v8),
     l4 = K8.useMemo(
       () => ({
         ...V8,
@@ -281,7 +285,7 @@
       }),
       [V8],
     ),
-    n4 = _EK(e4, z1);
+    u5 = BIK(S4, q1, v8);
   (AEK({
     autoConnectIdeFlag: $,
     ideToInstallExtension: zA,
@@ -352,7 +356,6 @@
     if (rq[0]) return "sandbox-permission";
     let K6 = !Y7 || Y7.shouldContinueAnimation;
     if (K6 && i7[0]) return "tool-permission";
-    if (K6 && k.workerPermissions.queue[0]) return "worker-permission";
     if (K6 && k.workerSandboxPermissions.queue[0])
       return "worker-sandbox-permission";
     if (K6 && k.elicitation.queue[0]) return "elicitation";
@@ -375,23 +378,7 @@
     if (Yz === "elicitation") return;
     if ((($J.current = !1), cY(), Yz === "tool-permission"))
       (i7[0]?.onAbort(), SK([]));
-    else if (Yz === "worker-permission") {
-      let K6 = k.workerPermissions.queue[0];
-      if (K6)
-        (oDA(
-          K6.workerName,
-          { decision: "rejected", resolvedBy: "leader" },
-          K6.id,
-          k.teamContext?.teamName,
-        ),
-          R((i6) => ({
-            ...i6,
-            workerPermissions: {
-              ...i6.workerPermissions,
-              queue: i6.workerPermissions.queue.slice(1),
-            },
-          })));
-    } else NA?.abort();
+    else NA?.abort();
   }
   let v_ = K8.useCallback(async () => {
       let K6 = await fO1(
@@ -461,22 +448,25 @@
         Hq(1, "other"));
     });
   let fX = K8.useCallback(
-      (K6) => {
-        (R((i6) => ({ ...i6, toolPermissionContext: K6 })),
-          setImmediate(() => {
-            SK((i6) => {
-              return (
-                i6.forEach((U8) => {
-                  U8.recheckPermission();
-                }),
-                i6
-              );
-            });
-          }));
-      },
-      [R, SK],
-    ),
-    xz = CvK(SK, fX),
+    (P6) => {
+      (R((u8) => ({ ...u8, toolPermissionContext: P6 })),
+        setImmediate(() => {
+          uK((u8) => {
+            return (
+              u8.forEach((K4) => {
+                K4.recheckPermission();
+              }),
+              u8
+            );
+          });
+        }));
+    },
+    [R, uK],
+  );
+  q8.useEffect(() => {
+    return (j4K(Uw), () => V4K());
+  }, [Uw]);
+  let b_ = eyK(uK, Uw),
     NX = K8.useCallback(
       (K6, i6, U8, B5, F7, L4) => {
         return {
@@ -773,7 +763,7 @@
           R((XK) => ({ ...XK, fileHistory: L4(XK.fileHistory) }));
         }, U8.message.uuid);
       let F7 = U8.message.message.content;
-      if (typeof F7 === "string")
+      if (typeof A7 === "string" && !K4.message.planContent)
         Nj(F7, {
           setCursorOffset: () => {},
           clearBuffer: () => {},
@@ -970,7 +960,7 @@
         limit: void 0,
       });
   }
-  (Xq4(),
+  (Yw4(IyK()),
     SPK(e4, e4.length === Y?.length),
     wvK(),
     K8.useEffect(() => {
@@ -1223,8 +1213,8 @@
       }),
       Y7 &&
         G4.createElement(I, { flexDirection: "column", width: "100%" }, Y7.jsx),
-      G4.createElement(uyK, null),
       G4.createElement(ol2, null),
+      T4.createElement(p8z, { showAllInTranscript: yA }),
     );
   let Ne = k_7(k, e4);
   return G4.createElement(
@@ -1291,6 +1281,7 @@
             hasActiveTools: _Y.size > 0,
           }),
         !$6 &&
+          !f4?.isLocalJSXCommand &&
           k.showExpandedTodos &&
           N1 &&
           N1.length > 0 &&
@@ -1300,6 +1291,7 @@
             G4.createElement(bZ1, { tasks: N1, isStandalone: !0 }),
           ),
         !$6 &&
+          !f4?.isLocalJSXCommand &&
           k.showExpandedTodos &&
           !(N1 && N1.length > 0) &&
           G4.createElement(
@@ -1332,9 +1324,9 @@
               }
               c3((L4) => {
                 return (
-                  L4.filter((XK) => XK.hostPattern.host === F7).forEach((XK) =>
-                    XK.resolvePromise(i6),
-                  ),
+                  v7
+                    .filter((vq) => vq.hostPattern.host === A7)
+                    .forEach((vq) => vq.resolvePromise(u8)),
                   L4.filter((XK) => XK.hostPattern.host !== F7)
                 );
               });
@@ -1348,139 +1340,7 @@
             toolUseConfirm: i7[0],
             toolUseContext: NX(e4, e4, NA ?? r7(), [], void 0, B),
             verbose: g,
-          }),
-        Yz === "worker-permission" &&
-          k.workerPermissions.queue[0] &&
-          G4.createElement(LPK, {
-            key: k.workerPermissions.queue[0].id,
-            request: k.workerPermissions.queue[0],
-            workerColor: P8()
-              ? Object.values(k.teamContext?.teammates ?? {}).find(
-                  (K6) => K6.name === k.workerPermissions.queue[0]?.workerName,
-                )?.color
-              : void 0,
-            onDone: () => {
-              R((K6) => ({
-                ...K6,
-                workerPermissions: {
-                  ...K6.workerPermissions,
-                  queue: K6.workerPermissions.queue.slice(1),
-                },
-              }));
-            },
-            onApprove: (K6) => {
-              let i6 = k.workerPermissions.queue[0];
-              if (i6)
-                oDA(
-                  i6.workerName,
-                  {
-                    decision: "approved",
-                    resolvedBy: "leader",
-                    updatedInput: K6,
-                  },
-                  i6.id,
-                  k.teamContext?.teamName,
-                );
-            },
-            onApproveForTeam: (K6) => {
-              let i6 = k.workerPermissions.queue[0],
-                U8 = k.teamContext?.teamName;
-              if (i6 && U8) {
-                let B5 = K6.startsWith("/") ? `/${K6}/**` : `${K6}/**`,
-                  F7 = {
-                    type: "addRules",
-                    rules: [{ toolName: i6.toolName, ruleContent: B5 }],
-                    behavior: "allow",
-                    destination: "session",
-                  };
-                (oDA(
-                  i6.workerName,
-                  {
-                    decision: "approved",
-                    resolvedBy: "leader",
-                    updatedInput: i6.input,
-                    permissionUpdates: [F7],
-                  },
-                  i6.id,
-                  U8,
-                ),
-                  Sy6(U8, K6, i6.toolName, "team-lead"));
-                let L4 = Cz(U8);
-                if (L4) {
-                  let Dq = UA({
-                      type: "team_permission_update",
-                      permissionUpdate: F7,
-                      directoryPath: K6,
-                      toolName: i6.toolName,
-                    }),
-                    oq = 0;
-                  for (let s5 of L4.members) {
-                    if (s5.name === i6.workerName) continue;
-                    if (s5.agentId === L4.leadAgentId) continue;
-                    (U3(
-                      s5.name,
-                      {
-                        from: "team-lead",
-                        text: Dq,
-                        timestamp: new Date().toISOString(),
-                      },
-                      U8,
-                    ),
-                      oq++);
-                  }
-                  if (P8())
-                    h(
-                      `[REPL] Broadcast team permission update to ${oq} teammate(s) for ${i6.toolName} in ${K6}`,
-                    );
-                }
-                let XK = [];
-                for (let Dq of k.workerPermissions.queue.slice(1)) {
-                  if (Dq.toolName !== i6.toolName) continue;
-                  let oq = Dq.input,
-                    s5 = oq?.file_path;
-                  if (typeof s5 === "string" && s5.startsWith(K6 + "/"))
-                    (oDA(
-                      Dq.workerName,
-                      {
-                        decision: "approved",
-                        resolvedBy: "leader",
-                        updatedInput: oq,
-                        permissionUpdates: [F7],
-                      },
-                      Dq.id,
-                      U8,
-                    ),
-                      XK.push(Dq.id));
-                }
-                if (XK.length > 0) {
-                  if (
-                    (R((Dq) => ({
-                      ...Dq,
-                      workerPermissions: {
-                        ...Dq.workerPermissions,
-                        queue: Dq.workerPermissions.queue.filter(
-                          (oq) => !XK.includes(oq.id),
-                        ),
-                      },
-                    })),
-                    P8())
-                  )
-                    h(
-                      `[REPL] Auto-approved ${XK.length} queued worker permission(s) matching ${i6.toolName} in ${K6}`,
-                    );
-                }
-              }
-            },
-            onDeny: (K6) => {
-              let i6 = k.workerPermissions.queue[0];
-              if (i6)
-                oDA(
-                  i6.workerName,
-                  { decision: "rejected", resolvedBy: "leader", feedback: K6 },
-                  i6.id,
-                  k.teamContext?.teamName,
-                );
-            },
+            workerBadge: I8[0]?.workerBadge,
           }),
         k.pendingWorkerRequest &&
           G4.createElement(Jg6, {
@@ -1602,9 +1462,6 @@
                   setInputValue: d8,
                 }),
             !1,
-            P8() &&
-              !z1 &&
-              G4.createElement(pvK, { idleStartTime: v1, turnDurationMs: iA }),
             G4.createElement(lTK, {
               debug: K,
               ideSelection: wA,

@@@ function 'l4A' (was 'Z4A') — structural (78.6%)
--- pretty-v2.1.19.js:203022
+++ pretty-v2.1.20.js:208807
@@ -31,12 +31,14 @@
         max_bytes: K,
       }),
       A.length <= K)
-    )
+    ) {
+      let H = tXA(A);
       return {
         base64: A.toString("base64"),
-        mediaType: `image/${z}`,
+        mediaType: H,
         originalSize: A.length,
       };
+    }
     throw new _4A(
       `Unable to compress image (${wQ(A.length)}) to fit within ${wQ(K)}. Please use a smaller image.`,
     );

@@@ function 'vqA' (was 'BQA') — structural (78.3%)
--- pretty-v2.1.19.js:465797
+++ pretty-v2.1.20.js:314345
@@ -1,4 +1,5 @@
 function BQA() {
+  U_();
   let A = Wh6();
   Gt = Dh6(A);
 }

@@@ function 'akK' (was 'CVK') — structural (78.2%)
--- pretty-v2.1.19.js:540978
+++ pretty-v2.1.20.js:546060
@@ -1,8 +1,7 @@
-function CVK({ toolUseConfirm: A, toolUseContext: K, onDone: q, onReject: Y }) {
+function akK({ toolUseConfirm: A, onDone: K, onReject: q, workerBadge: Y }) {
   let [z, w] = j6(),
     { addNotification: H } = A5(),
     [J, X] = AN.useState(""),
-    O = yqK(K.messages, z.toolPermissionContext.mode),
     [$, _] = AN.useState(null),
     [Z, G] = AN.useState(3),
     W = A.tool.name === ZC,
@@ -224,8 +223,7 @@
     }
     if (
       P8() &&
-      ($A === "yes-launch-swarm-accept-edits" ||
-        $A === "yes-launch-swarm-bypass")
+      (o === "yes-launch-swarm-accept-edits" || o === "yes-launch-swarm-bypass")
     ) {
       let KA =
         $A === "yes-launch-swarm-bypass" ? "bypassPermissions" : "acceptEdits";
@@ -294,7 +292,11 @@
     });
     return O3.default.createElement(
       P2,
-      { color: "planMode", title: "Push to remote unavailable" },
+      {
+        color: "planMode",
+        title: "Push to remote unavailable",
+        workerBadge: Y,
+      },
       O3.default.createElement(
         I,
         { flexDirection: "column", paddingX: 1, marginTop: 1 },
@@ -327,7 +329,7 @@
   if (x === "checking" || x === "creating")
     return O3.default.createElement(
       P2,
-      { color: "planMode", title: "Pushing to remote…" },
+      { color: "planMode", title: "Pushing to remote…", workerBadge: Y },
       O3.default.createElement(
         I,
         { flexDirection: "column", paddingX: 1, marginTop: 1 },
@@ -348,7 +350,7 @@
   if (V)
     return O3.default.createElement(
       P2,
-      { color: "planMode", title: "Exit plan mode?" },
+      { color: "planMode", title: "Exit plan mode?", workerBadge: Y },
       O3.default.createElement(
         I,
         { flexDirection: "column", paddingX: 1, marginTop: 1 },
@@ -407,7 +409,12 @@
     null,
     O3.default.createElement(
       P2,
-      { color: "planMode", title: "Ready to code?", innerPaddingX: 0 },
+      {
+        color: "planMode",
+        title: "Ready to code?",
+        innerPaddingX: 0,
+        workerBadge: Y,
+      },
       O3.default.createElement(
         I,
         { flexDirection: "column", marginTop: 1 },
@@ -468,7 +475,6 @@
             f,
             { dimColor: !0 },
             "Would you like to proceed?",
-            O !== null && ` (context ${O}% used)`,
           ),
           O3.default.createElement(
             I,

@@@ variable 'uq1' (was 'B71') — structural (78.2%)
--- pretty-v2.1.19.js:171633
+++ pretty-v2.1.20.js:174611
@@ -1,17 +1,16 @@
-  B71 = (A) => {
-    let K = Cg3(),
-      Y = {
-        nodeName: A,
-        style: {},
-        attributes: {},
-        childNodes: [],
-        parentNode: void 0,
-        yogaNode:
-          A !== "ink-virtual-text" && A !== "ink-link" && A !== "ink-progress"
-            ? K.Node.create()
-            : void 0,
-        dirty: !1,
-      };
+var uq1 = (A) => {
+    let q = {
+      nodeName: A,
+      style: {},
+      attributes: {},
+      childNodes: [],
+      parentNode: void 0,
+      yogaNode:
+        A !== "ink-virtual-text" && A !== "ink-link" && A !== "ink-progress"
+          ? NJ4()
+          : void 0,
+      dirty: !1,
+    };
     if (A === "ink-text") Y.yogaNode?.setMeasureFunc(Rg3.bind(null, Y));
     return Y;
   },

@@@ function 'NM2' (was 'T$2') — structural (78.2%)
--- pretty-v2.1.19.js:434435
+++ pretty-v2.1.20.js:422718
@@ -51,6 +51,7 @@
     j = zy6("team-lead", Y),
     M = j,
     P = !1;
+  C7K(K.parentSessionId, K.agentName);
   try {
     Qp(
       q,
@@ -68,6 +69,7 @@
         k = D.length > 0 ? [...D] : void 0;
       D.push(N);
       let R = NBA(),
+        b = NBA(H.options.tools),
         x = [],
         g = (await H.getAppState()).tasks[q],
         b =
@@ -82,7 +84,7 @@
               agentDefinition: Q,
               promptMessages: T,
               toolUseContext: H,
-              canUseTool: P$2(K, q, V),
+              canUseTool: DM2(K, V),
               isAsync: !0,
               canShowPermissionPrompts: !0,
               forkContextMessages: k,
@@ -101,7 +103,7 @@
                   (F = !0));
                 break;
               }
-              (x.push(d), D.push(d), iZA(R, d));
+              (S.push(a), D.push(a), EGA(R, a, b, H.options.tools));
               let o = TBA(R);
               Qp(
                 q,
@@ -120,7 +122,8 @@
                           "type" in GA &&
                           GA.type === "tool_result"
                         ) {
-                          if (e) ((e = new Set(e)), e.delete(GA.tool_use_id));
+                          if (JA)
+                            ((JA = new Set(JA)), JA.delete(HA.tool_use_id));
                         }
                     }
                   }
@@ -160,7 +163,7 @@
       ),
         p8K(K.agentName, K.color, K.teamName),
         h(`[inProcessRunner] ${K.agentId} finished prompt, waiting for next`));
-      let B = await N$2(K, J, q, H.getAppState, O);
+      let d = await fM2(K, J, q, H.getAppState, X, K.parentSessionId);
       switch (B.type) {
         case "shutdown_request":
           (h(

@@@ function 'OVA' (was '_PA') — structural (77.8%)
--- pretty-v2.1.19.js:540967
+++ pretty-v2.1.20.js:546049
@@ -1,5 +1,5 @@
 function _PA(A, K) {
-  let q = [{ type: "setMode", mode: A, destination: "session" }];
+  let q = [{ type: "setMode", mode: og(A), destination: "session" }];
   if (NS() && K && K.length > 0)
     q.push({
       type: "addRules",

@@@ variable 'jyK' (was 'iTK') — structural (77.8%)
--- pretty-v2.1.19.js:553219
+++ pretty-v2.1.20.js:558331
@@ -68,6 +68,7 @@
   qF6();
   SWA();
   dTK();
+  WyK();
   ((c4 = r(JA(), 1)), (BK = r(JA(), 1)));
   lTK = c4.memo(Rd2);
 });

@@@ function 'NZK' (was '$JK') — structural (77.6%)
--- pretty-v2.1.19.js:486712
+++ pretty-v2.1.20.js:490093
@@ -141,14 +141,33 @@
               _.capabilities?.tools?.listChanged)
             )
               _.client.setNotificationHandler(q$6, async () => {
-                (h6(
+                B6(
                   _.name,
                   "Received tools/list_changed notification, refreshing tools",
-                ),
-                  n("tengu_mcp_list_changed", { type: "tools" }));
+                );
                 try {
+                  let D = kI.cache.get(_);
                   hB.cache.delete(_);
-                  let D = await hB(_);
+                  let M = await kI(_),
+                    j = M.length;
+                  if (D)
+                    D.then(
+                      (P) => {
+                        n("tengu_mcp_list_changed", {
+                          type: "tools",
+                          previousCount: P.length,
+                          newCount: j,
+                        });
+                      },
+                      () => {
+                        n("tengu_mcp_list_changed", {
+                          type: "tools",
+                          newCount: j,
+                        });
+                      },
+                    );
+                  else
+                    n("tengu_mcp_list_changed", { type: "tools", newCount: j });
                   H({ ..._, tools: D });
                 } catch (D) {
                   _2(

@@@ function 'Kn2' (was 'yB2') — structural (77.0%)
--- pretty-v2.1.19.js:524821
+++ pretty-v2.1.20.js:529428
@@ -1,8 +1,7 @@
 function yB2(A) {
   let q = A.filter((z) => z.type === "connected").filter((z) => z.instructions);
-  if (q.length === 0) return "";
-  return `
-# MCP Server Instructions
+  if (q.length === 0) return null;
+  return `# MCP Server Instructions
 
 The following MCP servers have provided instructions for how to use their tools and resources:
 
@@ -11,6 +10,5 @@
 ${z.instructions}`;
 }).join(`
 
-`)}
-`;
+`)}`;
 }

@@@ function 'JvK' (was 'UjK') — structural (77.0%)
--- pretty-v2.1.19.js:575439
+++ pretty-v2.1.20.js:579584
@@ -4,6 +4,7 @@
       serverName: "Claude in Chrome",
       logger: A,
       socketPath: HxA(),
+      getSocketPaths: Bw7,
       clientTypeId: "claude-code",
       onAuthenticationError: () => {
         A.warn(

@@@ function 'E$6' (was 'bX6') — structural (76.7%)
--- pretty-v2.1.19.js:265252
+++ pretty-v2.1.20.js:264171
@@ -17,7 +17,10 @@
     );
   if (hA().existsSync(z)) {
     let H = _6(hA().readFileSync(z, { encoding: "utf8" }));
-    return (H.output.forEach(B6Y), H.output.map((J, X) => N87(J, g6Y, X)));
+    return (
+      H.output.forEach(g9Y),
+      H.output.map((J, O) => CK7(J, U9Y, O, B9Y()))
+    );
   }
   if (S6.isCI)
     throw Error(`Anthropic API fixture missing: ${z}. Re-run npm test locally, then commit the result. Input messages:

@@@ function 'qvK' (was 'ujK') — structural (76.5%)
--- pretty-v2.1.19.js:530267
+++ pretty-v2.1.20.js:535002
@@ -31,8 +31,20 @@
     );
     if (z.existsSync(A))
       try {
-        let Z = `${A}.backup`;
+        let Z = gdA(A),
+          G = WQ6(A),
+          W = `${A}.backup.${Date.now()}`;
         z.copyFileSync(A, Z);
+        let D = 5,
+          M = z
+            .readdirStringSync(Z)
+            .filter((j) => j.startsWith(`${G}.backup.`))
+            .sort()
+            .reverse();
+        for (let j of M.slice(D))
+          try {
+            z.unlinkSync(jm(Z, j));
+          } catch {}
       } catch (Z) {
         h(`Failed to backup config: ${Z}`, { level: "error" });
       }

@@@ variable 'gk' (was 'uk') — structural (76.5%)
--- pretty-v2.1.19.js:193535
+++ pretty-v2.1.20.js:192657
@@ -8,7 +8,6 @@
   r6();
   w0();
   KM();
-  kK();
   DE4 = [FVA];
   ((lK6 = w6((A) => {
     let K = [],
@@ -22,7 +21,7 @@
     E1(process.env.USE_API_CONTEXT_MANAGEMENT);
     let w = sY("tengu_tool_pear");
     if (cK6(A) && w) K.push(Id6);
-    if (z && Bk("tool_use_examples", "enabled", !1)) K.push(IlA);
+    if (z && i4("tengu_scarf_coffee", !1)) K.push(FiA);
     if (Y === "vertex" && F29(A)) K.push(Jk1);
     if (Y === "foundry") K.push(Jk1);
     if (process.env.ANTHROPIC_BETAS && !q)

@@@ variable 'FI6' (was 'bp7') — structural (76.5%)
--- pretty-v2.1.19.js:389480
+++ pretty-v2.1.20.js:425358
@@ -15,5 +15,7 @@
   MHA();
   F1();
   DC();
+  fqA();
+  yI();
   ((Lp7 = r(JA(), 1)), (av6 = c1A.firstParty));
 });

@@@ function 'THK' (was 'Vi2') — structural (76.5%)
--- pretty-v2.1.19.js:565686
+++ pretty-v2.1.20.js:461125
@@ -1,3 +1,3 @@
-function Vi2(A) {
-  return A.name;
+function THK() {
+  return hjA.toolCallsBetweenUpdates;
 }

@@@ function 'y6' (was 'T6') — structural (76.3%)
--- pretty-v2.1.19.js:196447
+++ pretty-v2.1.20.js:312561
@@ -1,5 +1,5 @@
 function T6(A) {
-  let K = a(59),
+  let K = s(63),
     {
       isDisabled: q,
       hideIndexes: Y,
@@ -175,9 +175,7 @@
               yA = !V && l.focusedValue === zA.value,
               rA = l.value === zA.value;
             if (zA.type === "input") {
-              let C1 = g.has(zA.value)
-                ? g.get(zA.value)
-                : zA.initialValue || "";
+              let L1 = B.has(t.value) ? B.get(t.value) : t.initialValue || "";
               return a7.default.createElement(iXA, {
                 key: String(zA.value),
                 option: zA,
@@ -269,9 +267,7 @@
               yA = !V && l.focusedValue === zA.value,
               rA = l.value === zA.value;
             if (zA.type === "input") {
-              let N1 = g.has(zA.value)
-                ? g.get(zA.value)
-                : zA.initialValue || "";
+              let k1 = B.has(t.value) ? B.get(t.value) : t.initialValue || "";
               return a7.default.createElement(iXA, {
                 key: String(zA.value),
                 option: zA,
@@ -418,67 +414,113 @@
         let wA;
         if (K[52] !== N || K[53] !== SA)
           ((wA = (KA) => {
+            if ($A.option.type === "input") return 0;
+            let vA = n$1($A.option.label),
+              ZA = N ? 0 : yA + 2,
+              LA = $A.isSelected ? 2 : 0;
+            return 2 + ZA + m7(vA) + LA;
+          }),
+            (K[52] = N),
+            (K[53] = yA),
+            (K[54] = zA));
+        else zA = K[54];
+        let AA = Math.max(...KA.map(zA)),
+          t;
+        if (K[55] !== N || K[56] !== yA || K[57] !== AA)
+          ((t = ($A) => {
             if (KA.option.type === "input") return null;
+            let vA = n$1($A.option.label),
+              ZA = N ? 0 : yA + 2,
+              LA = $A.isSelected ? 2 : 0,
+              mA = 2 + ZA + m7(vA) + LA,
+              CA = AA - mA;
             return a7.default.createElement(
               I,
-              { key: String(KA.option.value), flexDirection: "row", gap: 1 },
-              KA.isFocused
-                ? a7.default.createElement(
+              { key: String($A.option.value), flexDirection: "row" },
+              g7.default.createElement(
+                I,
+                { flexDirection: "row", flexShrink: 0 },
+                $A.isFocused
+                  ? g7.default.createElement(
+                      f,
+                      { color: "suggestion" },
+                      K1.pointer,
+                    )
+                  : $A.shouldShowDownArrow
+                    ? g7.default.createElement(
+                        f,
+                        { dimColor: !0 },
+                        K1.arrowDown,
+                      )
+                    : $A.shouldShowUpArrow
+                      ? g7.default.createElement(
+                          f,
+                          { dimColor: !0 },
+                          K1.arrowUp,
+                        )
+                      : g7.default.createElement(f, null, " "),
+                g7.default.createElement(f, null, " "),
+                g7.default.createElement(
+                  f,
+                  {
+                    dimColor: $A.isOptionDisabled,
+                    color: $A.isOptionDisabled
+                      ? void 0
+                      : $A.isSelected
+                        ? "success"
+                        : $A.isFocused
+                          ? "suggestion"
+                          : void 0,
+                  },
+                  !N &&
+                    g7.default.createElement(
+                      f,
+                      { dimColor: !0 },
+                      `${$A.index}.`.padEnd(yA + 2),
+                    ),
+                  $A.label,
+                ),
+                $A.isSelected &&
+                  g7.default.createElement(
                     f,
-                    { color: "suggestion" },
-                    aA.pointer,
-                  )
-                : KA.shouldShowDownArrow
-                  ? a7.default.createElement(f, { dimColor: !0 }, aA.arrowDown)
-                  : KA.shouldShowUpArrow
-                    ? a7.default.createElement(f, { dimColor: !0 }, aA.arrowUp)
-                    : a7.default.createElement(f, null, " "),
+                    { color: "success" },
+                    " ",
+                    K1.tick,
+                  ),
+                CA > 0 && g7.default.createElement(f, null, " ".repeat(CA)),
+              ),
               a7.default.createElement(
                 f,
-                {
-                  dimColor: KA.isOptionDisabled,
-                  color: KA.isOptionDisabled
-                    ? void 0
-                    : KA.isSelected
-                      ? "success"
-                      : KA.isFocused
-                        ? "suggestion"
-                        : void 0,
-                },
-                !N &&
+                { flexGrow: 1, marginLeft: 2 },
+                g7.default.createElement(
+                  f,
+                  {
+                    wrap: "wrap",
+                    dimColor:
+                      $A.isOptionDisabled || $A.option.dimDescription !== !1,
+                    color: $A.isOptionDisabled
+                      ? void 0
+                      : $A.isSelected
+                        ? "success"
+                        : $A.isFocused
+                          ? "suggestion"
+                          : void 0,
+                  },
                   a7.default.createElement(
                     f,
-                    { dimColor: !0 },
-                    `${KA.index}.`.padEnd(SA + 2),
+                    null,
+                    $A.option.description || " ",
                   ),
-                KA.label,
+                ),
               ),
-              KA.isSelected &&
-                a7.default.createElement(f, { color: "success" }, aA.tick),
             );
           }),
-            (K[52] = N),
-            (K[53] = SA),
-            (K[54] = wA));
-        else wA = K[54];
-        t = a7.default.createElement(
-          I,
-          { ...VA.container() },
-          a7.default.createElement(
-            I,
-            { flexDirection: "row" },
-            a7.default.createElement(
-              I,
-              { flexDirection: "column", flexShrink: 0 },
-              AA.map(wA),
-            ),
-            a7.default.createElement(
-              I,
-              { flexDirection: "column", flexGrow: 1, marginLeft: 2 },
-              AA.map(Bz9),
-            ),
-          ),
-        );
+            (K[55] = N),
+            (K[56] = yA),
+            (K[57] = AA),
+            (K[58] = t));
+        else t = K[58];
+        o = g7.default.createElement(I, { ...PA.container() }, KA.map(t));
         break A;
       }
       ((GA = I),
@@ -628,12 +670,12 @@
   } else ((GA = K[40]), (WA = K[41]), (ZA = K[42]), (t = K[43]));
   if (t !== Symbol.for("react.early_return_sentinel")) return t;
   let $A;
-  if (K[55] !== GA || K[56] !== WA || K[57] !== ZA)
+  if (K[59] !== OA || K[60] !== HA || K[61] !== DA)
     (($A = a7.default.createElement(GA, { ...WA }, ZA)),
-      (K[55] = GA),
-      (K[56] = WA),
-      (K[57] = ZA),
-      (K[58] = $A));
-  else $A = K[58];
+      (K[59] = OA),
+      (K[60] = HA),
+      (K[61] = DA),
+      (K[62] = _A));
+  else _A = K[62];
   return $A;
 }

@@@ function 'QC2' (was 'hW2') — structural (76.0%)
--- pretty-v2.1.19.js:450786
+++ pretty-v2.1.20.js:461601
@@ -1,5 +1,5 @@
 async function hW2(A, K) {
-  if (K === "session_memory") return !1;
+  if (K === "session_memory" || K === "compact") return !1;
   if (!rp()) return !1;
   let q = Fp(A),
     { isAboveAutoCompactThreshold: Y } = mp(q);

@@@ variable 'MXK' (was 'OzK') — structural (75.9%)
--- pretty-v2.1.19.js:473142
+++ pretty-v2.1.20.js:476477
@@ -12,6 +12,8 @@
   r6();
   U2();
   Q2();
+  c2();
+  d2();
   ((uf2 = {
     type: "local",
     name: "compact",
@@ -49,7 +51,7 @@
           }
         }
         let H = (await gp(Y, void 0, K)).messages,
-          J = await _P1(H, K, !1, z);
+          J = await Lf1(H, K, await SS2(K, H), !1, z, !1);
         (O3A(void 0), PjA(), K$.cache.clear?.(), nX.cache.clear?.());
         let X = XqA("tip"),
           O = cO("app:toggleTranscript", "Global", "ctrl+o"),

@@@ variable 'HL6' (was 'xN6') — structural (75.8%)
--- pretty-v2.1.19.js:363343
+++ pretty-v2.1.20.js:388481
@@ -8,6 +8,8 @@
   a0A();
   tK();
   x9();
+  EK();
+  zp();
   Q3 = r(JA(), 1);
   ((wWA = new Map()), (yx7 = new Set()));
 });

@@@ variable 'B2' (was 'b2') — structural (75.8%)
--- pretty-v2.1.19.js:527126
+++ pretty-v2.1.20.js:531799
@@ -14,5 +14,9 @@
   kK();
   F1();
   E8();
+  KTK();
+  P8();
+  a1();
+  s0();
   qm6 = [...bN, "cliArg", "command", "session"];
 });

@@@ function 'BIK' (was '_EK') — structural (75.7%)
--- pretty-v2.1.19.js:556429
+++ pretty-v2.1.20.js:561595
@@ -1,5 +1,6 @@
-function _EK(A, K) {
-  let q = a(17),
+function BIK(A, K, q) {
+  let Y = s(18),
+    z = q === void 0 ? !1 : q,
     [Y, z] = De.useState(null),
     w;
   if (q[0] === Symbol.for("react.memo_cache_sentinel"))
@@ -38,10 +39,12 @@
     q[8] !== K ||
     q[9] !== A ||
     q[10] !== Z ||
-    q[11] !== _
+    Y[11] !== W ||
+    Y[12] !== G
   )
     ((P = () => {
       if (_ !== "closed" || K) return;
+      if (z) return;
       if (Y !== !0) return;
       if (lO()) return;
       if (E1(process.env.CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY)) return;
@@ -55,7 +58,7 @@
       if (T.length > 0)
         ((H.current = new Set(M)), (J.current = T[T.length - 1]));
     }),
-      (V = [M, _, K, Y, A, Z]),
+      (T = [V, G, K, z, w, A, W]),
       (q[6] = M),
       (q[7] = Y),
       (q[8] = K),
@@ -63,15 +66,16 @@
       (q[10] = Z),
       (q[11] = _),
       (q[12] = P),
-      (q[13] = V));
-  else ((P = q[12]), (V = q[13]));
+      (Y[13] = N),
+      (Y[14] = T));
+  else ((N = Y[13]), (T = Y[14]));
   De.useEffect(P, V);
   let N;
-  if (q[14] !== G || q[15] !== _)
+  if (Y[15] !== D || Y[16] !== G)
     ((N = { state: _, handleSelect: G }),
-      (q[14] = G),
       (q[15] = _),
-      (q[16] = N));
-  else N = q[16];
+      (Y[16] = G),
+      (Y[17] = k));
+  else k = Y[17];
   return N;
 }

@@@ variable 'V$K' (was '_wK') — structural (75.7%)
--- pretty-v2.1.19.js:479425
+++ pretty-v2.1.20.js:482776
@@ -38,12 +38,9 @@
             K,
             void 0,
             H,
-          );
-        return $UA.createElement(
-          XMA,
-          { onComplete: A },
-          $UA.createElement(HwK, { data: $ }),
-        );
+          ),
+          _ = await ct(TB6.createElement(G$K, { data: $ }));
+        return (A(_), null);
       },
     }),
     ($wK = {

@@@ function '_E1' (was 'JPA') — structural (75.4%)
--- pretty-v2.1.19.js:535438
+++ pretty-v2.1.20.js:541077
@@ -1,5 +1,5 @@
 function JPA(A) {
-  let K = a(24),
+  let K = s(26),
     { file_path: q, edits: Y } = A,
     { columns: z } = N8(),
     w;
@@ -40,9 +40,9 @@
   else _ = K[12];
   let Z = _,
     G;
-  if (K[13] !== z || K[14] !== q || K[15] !== Z || K[16] !== $) {
+  if (K[13] !== z || K[14] !== H || K[15] !== q || K[16] !== Z || K[17] !== $) {
     let D;
-    if (K[18] !== z || K[19] !== q || K[20] !== Z)
+    if (K[19] !== z || K[20] !== H || K[21] !== q || K[22] !== Z)
       ((D = (j) =>
         Cd.createElement(hf, {
           key: j.newStart,
@@ -50,22 +50,25 @@
           dim: !1,
           filePath: q,
           firstLine: Z,
+          fileContent: H,
           width: z,
         })),
-        (K[18] = z),
         (K[19] = q),
         (K[20] = Z),
-        (K[21] = D));
-    else D = K[21];
+        (K[21] = q),
+        (K[22] = Z),
+        (K[23] = D));
+    else D = K[23];
     ((G = Sf($.map(D), cF2)),
       (K[13] = z),
       (K[14] = q),
       (K[15] = Z),
       (K[16] = $),
-      (K[17] = G));
-  } else G = K[17];
+      (K[17] = $),
+      (K[18] = G));
+  } else G = K[18];
   let W;
-  if (K[22] !== G)
+  if (K[24] !== G)
     ((W = Cd.createElement(
       I,
       { flexDirection: "column" },
@@ -82,8 +85,8 @@
         G,
       ),
     )),
-      (K[22] = G),
-      (K[23] = W));
-  else W = K[23];
+      (K[24] = G),
+      (K[25] = W));
+  else W = K[25];
   return W;
 }

@@@ variable 'tjK' (was 'Q_K') — structural (75.4%)
--- pretty-v2.1.19.js:509967
+++ pretty-v2.1.20.js:513961
@@ -16,11 +16,7 @@
     isEnabled: () => !0,
     isHidden: !1,
     async call(A, K, q) {
-      let {
-          options: { isNonInteractiveSession: Y },
-          getAppState: z,
-          setAppState: w,
-        } = K,
+      let { getAppState: Y, setAppState: z } = K,
         J = (await z()).toolPermissionContext.mode;
       if (J !== "plan")
         return (
@@ -47,16 +43,10 @@
         }
       let _ = LS(),
         Z = _ ? YX(_) : void 0,
-        G = v0.createElement(pS2, {
-          planContent: X,
-          planPath: O,
-          editorName: Z,
-        });
-      if (Y) {
-        let W = await JMA(G);
-        return (A(W), null);
-      }
-      return v0.createElement(XMA, { onComplete: A }, G);
+        G = await ct(
+          VX.createElement(cp2, { planContent: J, planPath: O, editorName: _ }),
+        );
+      return (A(G), null);
     },
     userFacingName() {
       return "plan";

@@@ function 'gkK' (was 'WVK') — structural (75.3%)
--- pretty-v2.1.19.js:539884
+++ pretty-v2.1.20.js:544918
@@ -1,5 +1,5 @@
 function WVK(A) {
-  let K = a(16),
+  let K = s(17),
     { file_path: q, content: Y } = A,
     { columns: z } = N8(),
     w = hA().existsSync(q),
@@ -48,7 +48,14 @@
   else $ = K[7];
   let _ = $,
     Z;
-  if (K[8] !== z || K[9] !== Y || K[10] !== q || K[11] !== _ || K[12] !== O)
+  if (
+    K[8] !== z ||
+    K[9] !== Y ||
+    K[10] !== q ||
+    K[11] !== _ ||
+    K[12] !== X ||
+    K[13] !== J
+  )
     ((Z = O
       ? Sf(
           O.map((W) =>
@@ -58,6 +65,7 @@
               dim: !1,
               filePath: q,
               firstLine: _,
+              fileContent: J,
               width: z - 2,
             }),
           ),
@@ -69,10 +77,11 @@
       (K[10] = q),
       (K[11] = _),
       (K[12] = O),
-      (K[13] = Z));
-  else Z = K[13];
+      (K[13] = J),
+      (K[14] = Z));
+  else Z = K[14];
   let G;
-  if (K[14] !== Z)
+  if (K[15] !== Z)
     ((G = gS.createElement(
       I,
       { flexDirection: "column" },
@@ -90,8 +99,8 @@
         Z,
       ),
     )),
-      (K[14] = Z),
-      (K[15] = G));
-  else G = K[15];
+      (K[15] = Z),
+      (K[16] = G));
+  else G = K[16];
   return G;
 }

@@@ function 'ke' (was 'et') — structural (75.1%)
--- pretty-v2.1.19.js:530321
+++ pretty-v2.1.20.js:535083
@@ -2,8 +2,8 @@
   if (!vm6) throw Error("Config accessed before allowed.");
   let Y = hA();
   if (!Y.existsSync(A)) {
-    let z = `${A}.backup`;
-    if (Y.existsSync(z))
+    let z = sTK(A);
+    if (z)
       process.stdout.write(`
 Claude configuration file not found at: ${A}
 A backup file exists at: ${z}
@@ -57,14 +57,14 @@
             h(`Corrupted config backed up to: ${X}`, { level: "error" }));
         } catch {}
       }
-      let _ = `${A}.backup`;
+      let _ = sTK(A);
       if (X)
         process.stdout.write(`The corrupted file has been backed up to: ${X}
 `);
       else if (O)
         process.stdout.write(`The corrupted file has already been backed up.
 `);
-      if (Y.existsSync(_))
+      if (_)
         process.stdout.write(`A backup file exists at: ${_}
 You can manually restore it by running: cp "${_}" "${A}"

@@@ function '_I6' (was 'zy6') — structural (75.0%)
--- pretty-v2.1.19.js:434322
+++ pretty-v2.1.20.js:422565
@@ -1,6 +1,6 @@
 function zy6(A, K, q) {
   let Y = q ? ` color="${q}"` : "";
-  return `<teammate-message teammate_id="${A}"${Y}>
+  return `<${IO} teammate_id="${A}"${Y}>
 ${K}
-</teammate-message>`;
+</${IO}>`;
 }

@@@ function 'PRK' (was 'nNK') — structural (75.0%)
--- pretty-v2.1.19.js:549556
+++ pretty-v2.1.20.js:554664
@@ -1,5 +1,5 @@
 function nNK(A) {
-  let K = A.match(/^@@([\w-]+)\s+(.+)$/s);
+  let K = A.match(/^@([\w-]+)\s+(.+)$/s);
   if (!K) return null;
   let [, q, Y] = K;
   if (!q || !Y) return null;

@@@ variable 'Of1' (was 'JM1') — structural (74.6%)
--- pretty-v2.1.19.js:430392
+++ pretty-v2.1.20.js:454376
@@ -13,14 +13,13 @@
   QK();
   sX();
   UX();
-  ((I6 = r(JA(), 1)),
-    (XO = r(JA(), 1)),
-    (ZO2 = [
-      { value: "both", label: "Restore code and conversation" },
-      { value: "conversation", label: "Restore conversation" },
-      { value: "code", label: "Restore code" },
-      { value: "nevermind", label: "Never mind" },
-    ]),
+  ((x6 = r(XA(), 1)), (ZX = r(XA(), 1)));
+  ((WE2 = [
+    { value: "both", label: "Restore code and conversation" },
+    { value: "conversation", label: "Restore conversation" },
+    { value: "code", label: "Restore code" },
+    { value: "nevermind", label: "Never mind" },
+  ]),
     (GO2 = [
       { value: "conversation", label: "Restore conversation" },
       { value: "nevermind", label: "Never mind" },

@@@ function '$0K' (was 'SqK') — structural (74.4%)
--- pretty-v2.1.19.js:452124
+++ pretty-v2.1.20.js:469610
@@ -39,9 +39,9 @@
       systemPrompt: [zD2(X)],
       userPrompt: O.join(`
 `),
-      enablePromptCaching: !0,
       signal: new AbortController().signal,
       options: {
+        enablePromptCaching: !0,
         querySource: "summarize_for_resume",
         agents: [],
         isNonInteractiveSession: !1,

@@@ function 'VPK' (was 'JZK') — structural (74.2%)
--- pretty-v2.1.19.js:511713
+++ pretty-v2.1.20.js:515697
@@ -1,5 +1,5 @@
 function JZK(A) {
-  let K = a(20),
+  let K = s(21),
     { selectedMatcher: q, selectedEvent: Y, onDelete: z, onCancel: w } = A,
     H;
   if (K[0] !== q)
@@ -43,28 +43,29 @@
       (K[11] = _));
   else _ = K[11];
   let Z;
-  if (K[12] !== $)
-    ((Z = MP.createElement(T6, { onChange: $, options: _ })),
+  if (K[12] !== w || K[13] !== $)
+    ((Z = MP.createElement(y6, { onChange: $, onCancel: w, options: _ })),
       (K[12] = $),
-      (K[13] = Z));
-  else Z = K[13];
+      (K[13] = $),
+      (K[14] = Z));
+  else Z = K[14];
   let G;
-  if (K[14] !== X || K[15] !== Z)
+  if (K[15] !== O || K[16] !== Z)
     ((G = MP.createElement(I, { flexDirection: "column", gap: 1 }, X, O, Z)),
-      (K[14] = X),
       (K[15] = Z),
-      (K[16] = G));
-  else G = K[16];
+      (K[16] = Z),
+      (K[17] = G));
+  else G = K[17];
   let W;
-  if (K[17] !== w || K[18] !== G)
+  if (K[18] !== w || K[19] !== G)
     ((W = MP.createElement(
       NK,
       { title: "Delete matcher?", onCancel: w, borderDimColor: !1 },
       G,
     )),
-      (K[17] = w),
       (K[18] = G),
-      (K[19] = W));
-  else W = K[19];
+      (K[19] = G),
+      (K[20] = W));
+  else W = K[20];
   return W;
 }

@@@ variable 'Jh8' (was 'DC8') — structural (74.2%)
--- pretty-v2.1.19.js:95762
+++ pretty-v2.1.20.js:97454
@@ -7,7 +7,6 @@
   ek8();
   lwA();
   IQ1();
-  FQ1();
   KeA = new rvA();
   q0 = {
     initialize: p1q,

@@@ variable 'aL4' (was 'SE4') — structural (74.2%)
--- pretty-v2.1.19.js:194795
+++ pretty-v2.1.20.js:193947
@@ -12,5 +12,6 @@
   CE4();
   r6();
   F1();
+  B1();
   ((w4A = r(P9(), 1)), (yE4 = Jz9()));
 });

@@@ function 'yv1' (was 'IN1') — structural (74.2%)
--- pretty-v2.1.19.js:521849
+++ pretty-v2.1.20.js:526291
@@ -10,5 +10,6 @@
     longestSession: null,
     firstSessionDate: null,
     hourCounts: {},
+    shotDistribution: {},
   };
 }

@@@ variable 'JE1' (was 'JT1') — structural (74.2%)
--- pretty-v2.1.19.js:533718
+++ pretty-v2.1.20.js:538486
@@ -6,6 +6,7 @@
   zO();
   zgA();
   e6();
+  a1();
   YPA = new Set();
   zPA = { initialize: ng2, dispose: QMK, subscribe: rg2, resetForTesting: ag2 };
 });

@@@ variable 'ABA' (was 'YBA') — structural (74.0%)
--- pretty-v2.1.19.js:307532
+++ pretty-v2.1.20.js:303827
@@ -4,6 +4,7 @@
   Ow();
   cP();
   F1();
+  B1();
   lKA = { data: null, valid: !1 };
   z$7 = {
     name: "keychain",
@@ -22,6 +23,23 @@
       }
       return ((lKA = { data: null, valid: !0 }), null);
     },
+    async readAsync() {
+      if (vI.valid) return vI.data;
+      try {
+        let A = tU("-credentials"),
+          K = ZGA(),
+          { stdout: q, code: Y } = await u6(
+            "security",
+            ["find-generic-password", "-a", K, "-w", "-s", A],
+            { useCwd: !1, preserveOutputOnError: !1 },
+          );
+        if (Y === 0 && q) {
+          let z = G6(q.trim());
+          return ((vI = { data: z, valid: !0 }), z);
+        }
+      } catch (A) {}
+      return ((vI = { data: null, valid: !0 }), null);
+    },
     update(A) {
       ro();
       try {

@@@ function 'Dt' (was 'Zt') — structural (73.9%)
--- pretty-v2.1.19.js:462612
+++ pretty-v2.1.20.js:420228
@@ -5,18 +5,18 @@
         "report the issue at https://github.com/anthropics/claude-code/issues",
       PACKAGE_URL: "@anthropic-ai/claude-code",
       README_URL: "https://code.claude.com/docs/en/overview",
-      VERSION: "2.1.19",
+      VERSION: "2.1.20",
       FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-      BUILD_TIME: "2026-01-23T21:13:41Z",
+      BUILD_TIME: "2026-01-27T00:38:42Z",
     }.VERSION
       ? {
           ISSUES_EXPLAINER:
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.19",
+          VERSION: "2.1.20",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-01-23T21:13:41Z",
+          BUILD_TIME: "2026-01-27T00:38:42Z",
         }.VERSION
       : "unknown",
     q = await VM2(),
@@ -40,23 +40,23 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.19",
+            VERSION: "2.1.20",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-01-23T21:13:41Z",
+            BUILD_TIME: "2026-01-27T00:38:42Z",
           }.PACKAGE_URL &&
           {
             ISSUES_EXPLAINER:
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.19",
+            VERSION: "2.1.20",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-01-23T21:13:41Z",
+            BUILD_TIME: "2026-01-27T00:38:42Z",
           }.PACKAGE_URL !== "@anthropic-ai/claude-code"
         )
-          j += ` && npm -g uninstall ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.19", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-23T21:13:41Z" }.PACKAGE_URL}`;
+          M += ` && npm -g uninstall ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.PACKAGE_URL}`;
         w.push({
           issue: `Leftover npm global installation at ${D.path}`,
           fix: `Run: ${j}`,

@@@ variable 'Ih6' (was 'cC6') — structural (73.8%)
--- pretty-v2.1.19.js:417495
+++ pretty-v2.1.20.js:444627
@@ -8,6 +8,7 @@
   I1();
   zs7();
   F1();
+  B1();
   ((hY2 = U.strictObject({
     query: U.string().min(2).describe("The search query to use"),
     allowed_domains: U.array(U.string())
@@ -44,6 +45,10 @@
       return "Web Search";
     },
     getToolUseSummary: Ys7,
+    getActivityDescription(A) {
+      let K = yh6(A);
+      return K ? `Searching for ${K}` : "Searching the web";
+    },
     isEnabled() {
       let A = cK(),
         K = dq();
@@ -97,20 +102,21 @@
         { query: H } = A,
         J = z6({ content: "Perform a web search for the query: " + H }),
         X = uY2(A),
+        X = i4("tengu_plum_vx3", !1),
         O = IDA({
           messages: [J],
           systemPrompt: [
             "You are an assistant for performing a web search tool use",
           ],
-          maxThinkingTokens: K.options.maxThinkingTokens,
+          maxThinkingTokens: X ? 0 : K.options.maxThinkingTokens,
           tools: [],
           signal: K.abortController.signal,
           options: {
             getToolPermissionContext: async () => {
               return (await K.getAppState()).toolPermissionContext;
             },
-            model: K.options.mainLoopModel,
-            toolChoice: void 0,
+            model: X ? $0() : K.options.mainLoopModel,
+            toolChoice: X ? { type: "tool", name: "web_search" } : void 0,
             isNonInteractiveSession: K.options.isNonInteractiveSession,
             hasAppendSystemPrompt: !!K.options.appendSystemPrompt,
             extraToolSchemas: [X],

@@@ function 'Ma2' (was 'Fg2') — structural (73.8%)
--- pretty-v2.1.19.js:533301
+++ pretty-v2.1.20.js:538068
@@ -6,9 +6,10 @@
       let $ = Buffer.byteLength(X, "utf8");
       if ($ > RMK)
         return (
-          h(
-            `Settings sync: Skipping ${O} - exceeds size limit (${$} > ${RMK} bytes)`,
-          ),
+          L8("info", "settings_sync_file_too_large", {
+            sizeBytes: $,
+            maxBytes: rvK,
+          }),
           !0
         );
       return !1;
@@ -47,5 +48,5 @@
   }
   if (Y) dW();
   if (z) nX.cache.clear?.();
-  h(`Settings sync: Applied ${q} entries from remote`);
+  L8("info", "settings_sync_applied", { appliedCount: q });
 }

@@@ function 'cKA' (was 'sKA') — structural (73.7%)
--- pretty-v2.1.19.js:453503
+++ pretty-v2.1.20.js:281794
@@ -1,7 +1,13 @@
 async function sKA(A, K) {
+  let q = Array.isArray(A);
+  if (q) {
+    if (A.some(($) => $.type !== "text"))
+      return {
+        error: "Cannot persist tool results containing non-text content",
+      };
+  }
   await RD2();
-  let q = Array.isArray(A),
-    Y = q ? "json" : "txt",
+  let Y = q ? "json" : "txt",
     z = HS6(RP1(), `${K}.${Y}`),
     w = q ? UA(A, null, 2) : A,
     H = !1;

@@@ function 'a8z' (was 'Yi2') — structural (73.7%)
--- pretty-v2.1.19.js:563633
+++ pretty-v2.1.20.js:568634
@@ -6,7 +6,9 @@
       null
     );
   let z = T9A.join(A, K, "uploads"),
-    H = [`${A}/${K}/uploads/`, "/uploads/"].find((X) => Y.startsWith(X)),
+    H = [FL.join(A, K, "uploads") + FL.sep, FL.sep + "uploads" + FL.sep].find(
+      (O) => Y.startsWith(O),
+    ),
     J = H ? Y.slice(H.length) : Y;
   return T9A.join(z, J);
 }

@@@ variable 'tuA' (was 'ABA') — structural (73.3%)
--- pretty-v2.1.19.js:306862
+++ pretty-v2.1.20.js:303151
@@ -8,5 +8,6 @@
   t66();
   SV();
   u86();
+  ZK6();
   vO7 = ["⠂", "⠐"];
 });

@@@ function 'z$K' (was 'szK') — structural (73.2%)
--- pretty-v2.1.19.js:476424
+++ pretty-v2.1.20.js:479761
@@ -1,5 +1,5 @@
 function szK(A) {
-  let K = a(187),
+  let K = s(190),
     {
       onClose: q,
       context: Y,
@@ -174,21 +174,20 @@
       (K[25] = M1),
       (K[26] = u1));
   else u1 = K[26];
-  let s1;
+  let X6 = PA ?? !0,
+    J6;
   if (K[27] !== ZA || K[28] !== VA)
-    ((s1 = [
-      {
-        id: "thinkingEnabled",
-        label: "Thinking mode",
-        value: VA ?? !0,
-        type: "boolean",
-        onChange(q1) {
-          (ZA((Z1) => ({ ...Z1, thinkingEnabled: q1 })),
-            I4("userSettings", { alwaysThinkingEnabled: q1 ? void 0 : !1 }),
-            n("tengu_thinking_toggled", { enabled: q1 }));
-        },
+    ((J6 = {
+      id: "thinkingEnabled",
+      label: "Thinking mode",
+      value: X6,
+      type: "boolean",
+      onChange(H1) {
+        (DA((t1) => ({ ...t1, thinkingEnabled: H1 })),
+          h4("userSettings", { alwaysThinkingEnabled: H1 ? void 0 : !1 }),
+          n("tengu_thinking_toggled", { enabled: H1 }));
       },
-    ]),
+    }),
       (K[27] = ZA),
       (K[28] = VA),
       (K[29] = s1));
@@ -273,7 +272,10 @@
     v1;
   if (K[43] === Symbol.for("react.memo_cache_sentinel")) {
     let q1 = P8() ? ["bypassPermissions"] : ["bypassPermissions", "delegate"];
-    ((v1 = [...V1, ...yE.filter((Z1) => !V1.includes(Z1) && !q1.includes(Z1))]),
+    ((U1 = [
+      ...T1,
+      ...n1A.filter((t1) => !T1.includes(t1) && !H1.includes(t1)),
+    ]),
       (K[43] = v1));
   } else v1 = K[43];
   let g1;
@@ -285,7 +287,7 @@
       options: v1,
       type: "enum",
       onChange(q1) {
-        let Z1 = WR(q1),
+        let t1 = og(kR(H1)),
           R1 = I4("userSettings", {
             permissions: { ...V?.permissions, defaultMode: Z1 },
           });
@@ -459,9 +461,32 @@
       (K[66] = _.codeDiffFooterEnabled),
       (K[67] = IK));
   else IK = K[67];
+  let BK;
+  if (K[68] !== _.prStatusFooterEnabled)
+    ((BK = i4("tengu_pr_status_cli", !1)
+      ? [
+          {
+            id: "prStatusFooterEnabled",
+            label: "Show PR status footer",
+            value: _.prStatusFooterEnabled ?? !0,
+            type: "boolean",
+            onChange(H1) {
+              (V6((t1) => {
+                if (t1.prStatusFooterEnabled === H1) return t1;
+                return { ...t1, prStatusFooterEnabled: H1 };
+              }),
+                Z({ ...P1(), prStatusFooterEnabled: H1 }),
+                n("tengu_pr_status_footer_setting_changed", { enabled: H1 }));
+            },
+          },
+        ]
+      : []),
+      (K[68] = _.prStatusFooterEnabled),
+      (K[69] = BK));
+  else BK = K[69];
   let i7 = t === null ? "Default (recommended)" : t,
     SK;
-  if (K[68] !== j1 || K[69] !== i7)
+  if (K[70] !== M1 || K[71] !== Z5)
     ((SK = {
       id: "model",
       label: "Model",
@@ -469,12 +494,12 @@
       type: "managedEnum",
       onChange: j1,
     }),
-      (K[68] = j1),
-      (K[69] = i7),
-      (K[70] = SK));
-  else SK = K[70];
+      (K[70] = M1),
+      (K[71] = Z5),
+      (K[72] = J3));
+  else J3 = K[72];
   let rq;
-  if (K[71] !== _.diffTool || K[72] !== RA)
+  if (K[73] !== _.diffTool || K[74] !== CA)
     ((rq = RA
       ? [
           {
@@ -494,12 +519,12 @@
           },
         ]
       : []),
-      (K[71] = _.diffTool),
-      (K[72] = RA),
-      (K[73] = rq));
-  else rq = K[73];
+      (K[73] = _.diffTool),
+      (K[74] = CA),
+      (K[75] = S4));
+  else S4 = K[75];
   let c3;
-  if (K[74] !== _.autoConnectIde)
+  if (K[76] !== _.autoConnectIde)
     ((c3 = !X$()
       ? [
           {
@@ -518,11 +543,11 @@
           },
         ]
       : []),
-      (K[74] = _.autoConnectIde),
-      (K[75] = c3));
-  else c3 = K[75];
+      (K[76] = _.autoConnectIde),
+      (K[77] = O7));
+  else O7 = K[77];
   let hK;
-  if (K[76] !== _.autoInstallIdeExtension)
+  if (K[78] !== _.autoInstallIdeExtension)
     ((hK = X$()
       ? [
           {
@@ -541,12 +566,12 @@
           },
         ]
       : []),
-      (K[76] = _.autoInstallIdeExtension),
-      (K[77] = hK));
-  else hK = K[77];
+      (K[78] = _.autoInstallIdeExtension),
+      (K[79] = hq));
+  else hq = K[79];
   let e4 = _.claudeInChromeDefaultEnabled ?? !0,
     TK;
-  if (K[78] !== e4)
+  if (K[80] !== V3)
     ((TK = {
       id: "claudeInChromeDefaultEnabled",
       label: "Claude in Chrome enabled by default",
@@ -558,11 +583,11 @@
           n("tengu_claude_in_chrome_setting_changed", { enabled: q1 }));
       },
     }),
-      (K[78] = e4),
-      (K[79] = TK));
-  else TK = K[79];
+      (K[80] = V3),
+      (K[81] = Nq));
+  else Nq = K[81];
   let Gq;
-  if (K[80] !== _.teammateMode)
+  if (K[82] !== _.teammateMode)
     ((Gq = P8()
       ? (() => {
           let q1 = Hy6();
@@ -585,11 +610,11 @@
           ];
         })()
       : []),
-      (K[80] = _.teammateMode),
-      (K[81] = Gq));
-  else Gq = K[81];
+      (K[82] = _.teammateMode),
+      (K[83] = d5));
+  else d5 = K[83];
   let q5;
-  if (K[82] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[84] === Symbol.for("react.memo_cache_sentinel"))
     ((q5 = _1
       ? [
           {
@@ -601,10 +626,10 @@
           },
         ]
       : []),
-      (K[82] = q5));
-  else q5 = K[82];
+      (K[84] = bq));
+  else bq = K[84];
   let nK;
-  if (K[83] !== _.customApiKeyResponses?.approved)
+  if (K[85] !== _.customApiKeyResponses?.approved)
     ((nK = process.env.ANTHROPIC_API_KEY
       ? [
           {
@@ -679,13 +704,11 @@
           },
         ]
       : []),
-      (K[83] = _.customApiKeyResponses?.approved),
-      (K[84] = nK));
-  else nK = K[84];
+      (K[85] = _.customApiKeyResponses?.approved),
+      (K[86] = sK));
+  else sK = K[86];
   let M6;
   if (
-    K[85] !== O1 ||
-    K[86] !== u1 ||
     K[87] !== s1 ||
     K[88] !== H6 ||
     K[89] !== PA ||
@@ -708,13 +731,16 @@
     K[106] !== hK ||
     K[107] !== TK ||
     K[108] !== Gq ||
-    K[109] !== nK
+    K[109] !== hq ||
+    K[110] !== Nq ||
+    K[111] !== d5 ||
+    K[112] !== sK
   )
     ((M6 = [
       O1,
       u1,
-      ...s1,
       H6,
+      fA,
       ...PA,
       ...NA,
       cA,
@@ -729,6 +755,7 @@
       R8,
       ...q4,
       ...IK,
+      ...BK,
       SK,
       ...rq,
       ...c3,
@@ -738,8 +765,6 @@
       ...q5,
       ...nK,
     ]),
-      (K[85] = O1),
-      (K[86] = u1),
       (K[87] = s1),
       (K[88] = H6),
       (K[89] = PA),
@@ -763,8 +788,11 @@
       (K[107] = TK),
       (K[108] = Gq),
       (K[109] = nK),
-      (K[110] = M6));
-  else M6 = K[110];
+      (K[110] = Nq),
+      (K[111] = d5),
+      (K[112] = sK),
+      (K[113] = W6));
+  else W6 = K[113];
   let v8 = M6,
     d8;
   A: {
@@ -773,7 +801,7 @@
       break A;
     }
     let q1;
-    if (K[111] !== vA || K[112] !== v8) {
+    if (K[114] !== vA || K[115] !== R4) {
       let Z1 = vA.toLowerCase();
       ((q1 = v8.filter((R1) => {
         if (R1.id.toLowerCase().includes(Z1)) return !0;
@@ -781,44 +809,44 @@
           .toLowerCase()
           .includes(Z1);
       })),
-        (K[111] = vA),
-        (K[112] = v8),
-        (K[113] = q1));
-    } else q1 = K[113];
+        (K[114] = vA),
+        (K[115] = R4),
+        (K[116] = H1));
+    } else H1 = K[116];
     d8 = q1;
   }
   let z7 = d8,
     y4,
     B7;
-  if (K[114] !== z7.length || K[115] !== F)
+  if (K[117] !== D4.length || K[118] !== Q)
     ((y4 = () => {
       if (F >= z7.length) B(Math.max(0, z7.length - 1));
     }),
       (B7 = [z7.length, F]),
-      (K[114] = z7.length),
-      (K[115] = F),
-      (K[116] = y4),
-      (K[117] = B7));
-  else ((y4 = K[116]), (B7 = K[117]));
+      (K[117] = D4.length),
+      (K[118] = Q),
+      (K[119] = xq),
+      (K[120] = pK));
+  else ((xq = K[119]), (pK = K[120]));
   G6.useEffect(y4, B7);
   let Tq;
   if (
-    K[118] !== BA ||
-    K[119] !== g ||
-    K[120] !== R ||
-    K[121] !== _.autoCompactEnabled ||
-    K[122] !== _.autoConnectIde ||
-    K[123] !== _.autoInstallIdeExtension ||
-    K[124] !== _.customApiKeyResponses?.approved ||
-    K[125] !== _.diffTool ||
-    K[126] !== _.editorMode ||
-    K[127] !== _.preferredNotifChannel ||
-    K[128] !== _.respectGitignore ||
-    K[129] !== _.terminalProgressBarEnabled ||
-    K[130] !== _.theme ||
-    K[131] !== q ||
-    K[132] !== V?.autoUpdatesChannel ||
-    K[133] !== AA
+    K[121] !== bA ||
+    K[122] !== B ||
+    K[123] !== R ||
+    K[124] !== _.autoCompactEnabled ||
+    K[125] !== _.autoConnectIde ||
+    K[126] !== _.autoInstallIdeExtension ||
+    K[127] !== _.customApiKeyResponses?.approved ||
+    K[128] !== _.diffTool ||
+    K[129] !== _.editorMode ||
+    K[130] !== _.preferredNotifChannel ||
+    K[131] !== _.respectGitignore ||
+    K[132] !== _.terminalProgressBarEnabled ||
+    K[133] !== _.theme ||
+    K[134] !== q ||
+    K[135] !== V?.autoUpdatesChannel ||
+    K[136] !== KA
   )
     ((Tq = () => {
       if (AA !== null) return;
@@ -885,42 +913,42 @@
         );
       else q("Config dialog dismissed", { display: "system" });
     }),
-      (K[118] = BA),
-      (K[119] = g),
-      (K[120] = R),
-      (K[121] = _.autoCompactEnabled),
-      (K[122] = _.autoConnectIde),
-      (K[123] = _.autoInstallIdeExtension),
-      (K[124] = _.customApiKeyResponses?.approved),
-      (K[125] = _.diffTool),
-      (K[126] = _.editorMode),
-      (K[127] = _.preferredNotifChannel),
-      (K[128] = _.respectGitignore),
-      (K[129] = _.terminalProgressBarEnabled),
-      (K[130] = _.theme),
-      (K[131] = q),
-      (K[132] = V?.autoUpdatesChannel),
-      (K[133] = AA),
-      (K[134] = Tq));
-  else Tq = K[134];
+      (K[121] = bA),
+      (K[122] = B),
+      (K[123] = R),
+      (K[124] = _.autoCompactEnabled),
+      (K[125] = _.autoConnectIde),
+      (K[126] = _.autoInstallIdeExtension),
+      (K[127] = _.customApiKeyResponses?.approved),
+      (K[128] = _.diffTool),
+      (K[129] = _.editorMode),
+      (K[130] = _.preferredNotifChannel),
+      (K[131] = _.respectGitignore),
+      (K[132] = _.terminalProgressBarEnabled),
+      (K[133] = _.theme),
+      (K[134] = q),
+      (K[135] = V?.autoUpdatesChannel),
+      (K[136] = KA),
+      (K[137] = f3));
+  else f3 = K[137];
   V?.autoUpdatesChannel;
   let n8 = Tq,
     V7 = AA === null,
     qK;
-  if (K[135] !== V7)
+  if (K[138] !== A8)
     ((qK = { context: "Settings", isActive: V7 }),
-      (K[135] = V7),
-      (K[136] = qK));
-  else qK = K[136];
+      (K[138] = A8),
+      (K[139] = z7));
+  else z7 = K[139];
   i1("confirm:no", n8, qK);
   let a8;
   if (
-    K[137] !== z7 ||
-    K[138] !== F ||
-    K[139] !== H ||
     K[140] !== w ||
     K[141] !== z ||
-    K[142] !== V?.autoUpdatesChannel
+    K[142] !== H ||
+    K[143] !== w ||
+    K[144] !== z ||
+    K[145] !== V?.autoUpdatesChannel
   )
     ((a8 = () => {
       let q1 = z7[F];
@@ -975,67 +1003,67 @@
         return;
       }
     }),
-      (K[137] = z7),
-      (K[138] = F),
-      (K[139] = H),
       (K[140] = w),
       (K[141] = z),
-      (K[142] = V?.autoUpdatesChannel),
-      (K[143] = a8));
-  else a8 = K[143];
+      (K[142] = H),
+      (K[143] = w),
+      (K[144] = z),
+      (K[145] = V?.autoUpdatesChannel),
+      (K[146] = v5));
+  else v5 = K[146];
   V?.autoUpdatesChannel;
   let vK = a8,
     l3;
-  if (K[144] !== F || K[145] !== e)
+  if (K[147] !== Q || K[148] !== e)
     ((l3 = () => {
       if (F === 0) e(!0);
       else B(FN2);
     }),
-      (K[144] = F),
-      (K[145] = e),
-      (K[146] = l3));
-  else l3 = K[146];
+      (K[147] = Q),
+      (K[148] = e),
+      (K[149] = tK));
+  else tK = K[149];
   let T5;
-  if (K[147] !== z7.length)
+  if (K[150] !== D4.length)
     ((T5 = () => {
       B((q1) => Math.min(z7.length - 1, q1 + 1));
     }),
-      (K[147] = z7.length),
-      (K[148] = T5));
-  else T5 = K[148];
+      (K[150] = D4.length),
+      (K[151] = u3));
+  else u3 = K[151];
   let jK;
-  if (K[149] !== e || K[150] !== OA)
+  if (K[152] !== e || K[153] !== ZA)
     ((jK = () => {
       (e(!0), OA(""));
     }),
-      (K[149] = e),
-      (K[150] = OA),
-      (K[151] = jK));
-  else jK = K[151];
+      (K[152] = e),
+      (K[153] = ZA),
+      (K[154] = oA));
+  else oA = K[154];
   let n9;
-  if (K[152] !== l3 || K[153] !== T5 || K[154] !== jK || K[155] !== vK)
+  if (K[155] !== tK || K[156] !== u3 || K[157] !== oA || K[158] !== N3)
     ((n9 = {
       "select:previous": l3,
       "select:next": T5,
       "select:accept": vK,
       "settings:search": jK,
     }),
-      (K[152] = l3),
-      (K[153] = T5),
-      (K[154] = jK),
       (K[155] = vK),
-      (K[156] = n9));
-  else n9 = K[156];
+      (K[156] = u3),
+      (K[157] = oA),
+      (K[158] = N3),
+      (K[159] = VA));
+  else VA = K[159];
   let eA = AA === null && !XA,
     fA;
-  if (K[157] !== eA)
+  if (K[160] !== WA)
     ((fA = { context: "Settings", isActive: eA }),
-      (K[157] = eA),
-      (K[158] = fA));
-  else fA = K[158];
+      (K[160] = WA),
+      (K[161] = xA));
+  else xA = K[161];
   f7(n9, fA);
   let DA;
-  if (K[159] !== vA || K[160] !== e || K[161] !== OA)
+  if (K[162] !== vA || K[163] !== e || K[164] !== ZA)
     ((DA = (q1, Z1) => {
       if (Z1.escape) {
         if (vA.length > 0) OA("");
@@ -1044,36 +1072,33 @@
       }
       if (Z1.return || Z1.downArrow) (e(!1), B(0));
     }),
-      (K[159] = vA),
-      (K[160] = e),
-      (K[161] = OA),
-      (K[162] = DA));
-  else DA = K[162];
+      (K[162] = vA),
+      (K[163] = e),
+      (K[164] = ZA),
+      (K[165] = UA));
+  else UA = K[165];
   let xA = XA && AA === null,
     QA;
-  if (K[163] !== xA) ((QA = { isActive: xA }), (K[163] = xA), (K[164] = QA));
-  else QA = K[164];
+  if (K[166] !== pA) ((G1 = { isActive: pA }), (K[166] = pA), (K[167] = G1));
+  else G1 = K[167];
   Y8(DA, QA);
   let pA;
-  if (K[165] !== e || K[166] !== OA)
+  if (K[168] !== e || K[169] !== ZA)
     ((pA = (q1, Z1) => {
       if (!Z1.ctrl && !Z1.meta && q1.length > 0 && !/^\s+$/.test(q1))
         (e(!0), OA(q1));
     }),
-      (K[165] = e),
-      (K[166] = OA),
-      (K[167] = pA));
-  else pA = K[167];
+      (K[168] = e),
+      (K[169] = ZA),
+      (K[170] = E1));
+  else E1 = K[170];
   let W1 = !XA && AA === null,
     L1;
-  if (K[168] !== W1) ((L1 = { isActive: W1 }), (K[168] = W1), (K[169] = L1));
-  else L1 = K[169];
+  if (K[171] !== S1) ((d1 = { isActive: S1 }), (K[171] = S1), (K[172] = d1));
+  else d1 = K[172];
   Y8(pA, L1);
   let x1;
   if (
-    K[170] !== g ||
-    K[171] !== R ||
-    K[172] !== z7 ||
     K[173] !== XA ||
     K[174] !== GA ||
     K[175] !== t ||
@@ -1086,7 +1111,10 @@
     K[182] !== z ||
     K[183] !== O ||
     K[184] !== AA ||
-    K[185] !== X
+    K[185] !== z ||
+    K[186] !== X ||
+    K[187] !== KA ||
+    K[188] !== O
   )
     ((x1 = G6.createElement(
       I,
@@ -1273,10 +1301,10 @@
                           "report the issue at https://github.com/anthropics/claude-code/issues",
                         PACKAGE_URL: "@anthropic-ai/claude-code",
                         README_URL: "https://code.claude.com/docs/en/overview",
-                        VERSION: "2.1.19",
+                        VERSION: "2.1.20",
                         FEEDBACK_CHANNEL:
                           "https://github.com/anthropics/claude-code/issues",
-                        BUILD_TIME: "2026-01-23T21:13:41Z",
+                        BUILD_TIME: "2026-01-27T00:38:42Z",
                       }.VERSION,
                       onChoice: (q1) => {
                         if ((wA(null), z(!1), q1 === "cancel")) return;
@@ -1288,10 +1316,10 @@
                             PACKAGE_URL: "@anthropic-ai/claude-code",
                             README_URL:
                               "https://code.claude.com/docs/en/overview",
-                            VERSION: "2.1.19",
+                            VERSION: "2.1.20",
                             FEEDBACK_CHANNEL:
                               "https://github.com/anthropics/claude-code/issues",
-                            BUILD_TIME: "2026-01-23T21:13:41Z",
+                            BUILD_TIME: "2026-01-27T00:38:42Z",
                           }.VERSION;
                         (I4("userSettings", Z1),
                           N((R1) => ({ ...R1, ...Z1 })),
@@ -1529,9 +1557,6 @@
                           ),
                     ),
     )),
-      (K[170] = g),
-      (K[171] = R),
-      (K[172] = z7),
       (K[173] = XA),
       (K[174] = GA),
       (K[175] = t),
@@ -1545,7 +1570,10 @@
       (K[183] = O),
       (K[184] = AA),
       (K[185] = X),
-      (K[186] = x1));
-  else x1 = K[186];
+      (K[186] = X),
+      (K[187] = KA),
+      (K[188] = O),
+      (K[189] = F1));
+  else F1 = K[189];
   return x1;
 }

@@@ function 'zy2' (was 'yj2') — structural (73.0%)
--- pretty-v2.1.19.js:456937
+++ pretty-v2.1.20.js:468724
@@ -210,10 +210,10 @@
           z = [
             {
               type: "text",
-              text: `The user sent the following message:
+              text: `The user sent a new message while you were working:
 ${q}
 
-Please address this message and continue with your tasks.`,
+IMPORTANT: After completing your current task, you MUST address the user's message above. Do not ignore it.`,
             },
             ...Y,
           ];
@@ -221,10 +221,10 @@
       }
       return c9([
         z6({
-          content: `The user sent the following message:
+          content: `The user sent a new message while you were working:
 ${A.prompt}
 
-Please address this message and continue with your tasks.`,
+IMPORTANT: After completing your current task, you MUST address the user's message above. Do not ignore it.`,
           isMeta: !0,
         }),
       ]);
@@ -383,32 +383,6 @@
           z6({ content: q.hookSpecificOutput.additionalContext, isMeta: !0 }),
         );
       return c9(Y);
-    }
-    case "memory": {
-      let q = A.memories.map((Y) => {
-        let z =
-          Y.remainingLines && Y.remainingLines > 0
-            ? ` (${Y.remainingLines} more lines in full file)`
-            : "";
-        return `## Previous Session (${(Y.lastModified instanceof Date ? Y.lastModified : new Date(Y.lastModified)).toLocaleDateString()})
-Full session notes: ${Y.fullPath}${z}
-
-${Y.content}`;
-      }).join(`
-
----
-
-`);
-      return c9([
-        z6({
-          content: `<session-memory>
-These session summaries are from PAST sessions that might not be related to the current task and may have outdated info. Do not assume the current task is related to these summaries, until the user's messages indicate so or reference similar tasks. Only a preview of each memory is shown - use the Read tool with the provided path to access full session memory when a session is relevant.
-
-${q}
-</session-memory>`,
-          isMeta: !0,
-        }),
-      ]);
     }
     case "token_usage":
       return [

@@@ function 'H7z' (was 'Bn2') — structural (72.8%)
--- pretty-v2.1.19.js:569163
+++ pretty-v2.1.20.js:573267
@@ -109,46 +109,6 @@
         if (WA) XA = [...XA, WA];
       }
       try {
-        v5K((ZA) => {
-          if (ZA.type === "started")
-            D.enqueue({
-              type: "system",
-              subtype: "hook_started",
-              hook_id: ZA.hookId,
-              hook_name: ZA.hookName,
-              hook_event: ZA.hookEvent,
-              uuid: xL(),
-              session_id: n1(),
-            });
-          else if (ZA.type === "progress")
-            D.enqueue({
-              type: "system",
-              subtype: "hook_progress",
-              hook_id: ZA.hookId,
-              hook_name: ZA.hookName,
-              hook_event: ZA.hookEvent,
-              stdout: ZA.stdout,
-              stderr: ZA.stderr,
-              output: ZA.output,
-              uuid: xL(),
-              session_id: n1(),
-            });
-          else if (ZA.type === "response")
-            D.enqueue({
-              type: "system",
-              subtype: "hook_response",
-              hook_id: ZA.hookId,
-              hook_name: ZA.hookName,
-              hook_event: ZA.hookEvent,
-              output: ZA.output,
-              stdout: ZA.stdout,
-              stderr: ZA.stderr,
-              exit_code: ZA.exitCode,
-              outcome: ZA.outcome,
-              uuid: xL(),
-              session_id: n1(),
-            });
-        });
         let WA;
         while ((WA = await PO1(J, X))) {
           if (
@@ -299,9 +259,9 @@
               let s = SA.map(
                 (
                   AA,
-                ) => `<teammate-message teammate_id="${AA.from}"${AA.color ? ` color="${AA.color}"` : ""}>
+                ) => `<${IO} teammate_id="${KA.from}"${KA.color ? ` color="${KA.color}"` : ""}>
 ${AA.text}
-</teammate-message>`,
+</${IO}>`,
               ).join(`
 
 `);
@@ -553,14 +513,15 @@
           }
           ObK.add(XA.uuid);
         }
-        (X((GA) => ({
-          ...GA,
-          queuedCommands: [
-            ...GA.queuedCommands,
-            { mode: "prompt", value: XA.message.content, uuid: XA.uuid },
-          ],
-          ...!1,
-        })),
+        (O((OA) => {
+          return {
+            ...OA,
+            queuedCommands: [
+              ...OA.queuedCommands,
+              { mode: "prompt", value: JA.message.content, uuid: JA.uuid },
+            ],
+          };
+        }),
           d());
       }
       if (((Z = !0), !_)) (B(), D.done());

@@@ function 'Vw4' (was 'Eq4') — structural (72.7%)
--- pretty-v2.1.19.js:158432
+++ pretty-v2.1.20.js:160160
@@ -1,5 +1,5 @@
 function Eq4(A) {
   let K = vq4(A);
   if (K) return `Claude ${K}`;
-  return "Claude";
+  return `Claude (${A})`;
 }

@@@ function 'kc2' (was 'Mb2') — structural (72.6%)
--- pretty-v2.1.19.js:517998
+++ pretty-v2.1.20.js:522229
@@ -9,12 +9,14 @@
       X = F8("error", z)(J);
     return (A(X), null);
   }
-  if (!l8.checkDependencies()) {
-    let J =
-        w === "linux" || w === "wsl"
-          ? "Error: Sandbox requires socat and bubblewrap. Please install these packages."
-          : "Error: Sandbox dependencies are not available on this system.",
-      X = F8("error", z)(J);
+  let H = x8.checkDependencies();
+  if (!x8.isPlatformInEnabledList()) {
+    let O = U8(
+      "error",
+      z,
+    )(
+      `Error: Sandboxing is disabled for this platform (${w}) via the enabledPlatforms setting.`,
+    );
     return (A(X), null);
   }
   if (l8.areSandboxSettingsLockedByPolicy()) {
@@ -27,7 +29,7 @@
     return (A(J), null);
   }
   let H = q?.trim() || "";
-  if (!H) return dGK.default.createElement(QGK, { onComplete: A });
+  if (!J) return qfK.default.createElement(eVK, { onComplete: A, depCheck: H });
   if (H) {
     let X = H.split(" ")[0];
     if (X === "exclude") {

@@@ function 'GyA' (was 'YRA') — structural (72.4%)
--- pretty-v2.1.19.js:177576
+++ pretty-v2.1.20.js:180547
@@ -30,6 +30,18 @@
       case "space":
         q.key = " ";
         break;
+      case "↑":
+        q.key = "up";
+        break;
+      case "↓":
+        q.key = "down";
+        break;
+      case "←":
+        q.key = "left";
+        break;
+      case "→":
+        q.key = "right";
+        break;
       default:
         q.key = z;
         break;

@@@ variable 'uZK' (was 'QB6') — structural (72.4%)
--- pretty-v2.1.19.js:507614
+++ pretty-v2.1.20.js:495221
@@ -16,5 +16,10 @@
   tK();
   I5();
   P1();
+  LpA();
+  aB6();
+  VT1();
+  $q();
+  iq();
   ((T3 = r(JA(), 1)), (a3A = r(JA(), 1)));
 });

@@@ variable 'Rg6' (was 'efK') — structural (72.4%)
--- pretty-v2.1.19.js:546777
+++ pretty-v2.1.20.js:511610
@@ -19,5 +19,7 @@
   uA();
   x9();
   jgA();
+  D1();
+  Hv1();
   ((NH = r(JA(), 1)), (Fg6 = r(JA(), 1)));
 });

@@@ variable 'BkK' (was 'iNK') — structural (72.4%)
--- pretty-v2.1.19.js:549532
+++ pretty-v2.1.20.js:544582
@@ -20,5 +20,6 @@
   A4();
   F1();
   qQ();
+  xkK();
   ((l7 = r(JA(), 1)), ($m = r(JA(), 1)));
 });

@@@ variable 'up6' (was 'pF6') — structural (72.4%)
--- pretty-v2.1.19.js:562816
+++ pretty-v2.1.20.js:567849
@@ -141,7 +141,5 @@
   RIK();
   SIK();
   bIK();
-  uIK();
-  mIK();
   ((G4 = r(JA(), 1)), (K8 = r(JA(), 1)));
 });

@@@ function 'Pi2' (was 'XB2') — structural (72.3%)
--- pretty-v2.1.19.js:523668
+++ pretty-v2.1.20.js:528122
@@ -7,7 +7,8 @@
     H = w[0],
     J = w.reduce(($, [, _]) => $ + _.inputTokens + _.outputTokens, 0),
     X = fP.useMemo(() => WDK(A, J), [A, J]),
-    O = q === "7d" ? 7 : q === "30d" ? 30 : A.totalDays;
+    X = q === "7d" ? 7 : q === "30d" ? 30 : A.totalDays,
+    $ = null;
   return D4.default.createElement(
     I,
     { flexDirection: "column", marginTop: 1 },
@@ -155,6 +156,131 @@
     ),
     X &&
       D4.default.createElement(
+        G8.default.Fragment,
+        null,
+        G8.default.createElement(
+          I,
+          { marginTop: 1 },
+          G8.default.createElement(f, null, "Shot distribution"),
+        ),
+        G8.default.createElement(
+          I,
+          { flexDirection: "row", gap: 4 },
+          G8.default.createElement(
+            I,
+            { flexDirection: "column", width: 28 },
+            G8.default.createElement(
+              f,
+              { wrap: "truncate" },
+              $.buckets[0].label,
+              ":",
+              " ",
+              G8.default.createElement(
+                f,
+                { color: "claude" },
+                $.buckets[0].count,
+              ),
+              G8.default.createElement(
+                f,
+                { color: "subtle" },
+                " (",
+                $.buckets[0].pct,
+                "%)",
+              ),
+            ),
+          ),
+          G8.default.createElement(
+            I,
+            { flexDirection: "column", width: 28 },
+            G8.default.createElement(
+              f,
+              { wrap: "truncate" },
+              $.buckets[1].label,
+              ":",
+              " ",
+              G8.default.createElement(
+                f,
+                { color: "claude" },
+                $.buckets[1].count,
+              ),
+              G8.default.createElement(
+                f,
+                { color: "subtle" },
+                " (",
+                $.buckets[1].pct,
+                "%)",
+              ),
+            ),
+          ),
+        ),
+        G8.default.createElement(
+          I,
+          { flexDirection: "row", gap: 4 },
+          G8.default.createElement(
+            I,
+            { flexDirection: "column", width: 28 },
+            G8.default.createElement(
+              f,
+              { wrap: "truncate" },
+              $.buckets[2].label,
+              ":",
+              " ",
+              G8.default.createElement(
+                f,
+                { color: "claude" },
+                $.buckets[2].count,
+              ),
+              G8.default.createElement(
+                f,
+                { color: "subtle" },
+                " (",
+                $.buckets[2].pct,
+                "%)",
+              ),
+            ),
+          ),
+          G8.default.createElement(
+            I,
+            { flexDirection: "column", width: 28 },
+            G8.default.createElement(
+              f,
+              { wrap: "truncate" },
+              $.buckets[3].label,
+              ":",
+              " ",
+              G8.default.createElement(
+                f,
+                { color: "claude" },
+                $.buckets[3].count,
+              ),
+              G8.default.createElement(
+                f,
+                { color: "subtle" },
+                " (",
+                $.buckets[3].pct,
+                "%)",
+              ),
+            ),
+          ),
+        ),
+        G8.default.createElement(
+          I,
+          { flexDirection: "row", gap: 4 },
+          G8.default.createElement(
+            I,
+            { flexDirection: "column", width: 28 },
+            G8.default.createElement(
+              f,
+              { wrap: "truncate" },
+              "Avg/session:",
+              " ",
+              G8.default.createElement(f, { color: "claude" }, $.avgShots),
+            ),
+          ),
+        ),
+      ),
+    O &&
+      G8.default.createElement(
         I,
         { marginTop: 1 },
         D4.default.createElement(f, { color: "suggestion" }, X),

@@@ function 'fH5' (was 'R4q') — structural (72.2%)
--- pretty-v2.1.19.js:101219
+++ pretty-v2.1.20.js:102921
@@ -7,6 +7,7 @@
     WL8.cache.clear?.(),
     PU1.cache.clear?.(),
     VU1.cache.clear?.(),
+    dd1.cache.clear?.(),
     (ol = void 0),
     q0.reset()
   );

@@@ function 'aQA' (was 'cgA') — structural (72.2%)
--- pretty-v2.1.19.js:418524
+++ pretty-v2.1.20.js:445662
@@ -8,6 +8,7 @@
       "<unknown location>"
     );
   let q = A.replace(/^file:\/\//, "");
+  if (/^\/[A-Za-z]:/.test(q)) q = q.slice(1);
   try {
     q = decodeURIComponent(q);
   } catch (Y) {
@@ -17,8 +18,8 @@
     });
   }
   if (K) {
-    let Y = tY2(K, q);
+    let Y = WT2(K, q).replaceAll("\\", "/");
     if (Y.length < q.length && !Y.startsWith("../../")) return Y;
   }
-  return q;
+  return q.replaceAll("\\", "/");
 }

@@@ function 'Yl' (was 'hc') — structural (72.1%)
--- pretty-v2.1.19.js:5403
+++ pretty-v2.1.20.js:5477
@@ -1,5 +1,5 @@
 function hc(A, K) {
-  let q = A.firstPrompt?.startsWith("<tick>"),
+  let q = A.firstPrompt?.startsWith(`<${ql}>`),
     Y = A.firstPrompt && !q;
   return (
     A.agentName ||

@@@ function 'l1z' (was 'ed2') — structural (71.8%)
--- pretty-v2.1.19.js:554481
+++ pretty-v2.1.20.js:559591
@@ -4,7 +4,5 @@
       return "hook";
     case "user":
       return A.permanent ? "user_permanent" : "user_temporary";
-    case "classifier":
-      return "classifier";
   }
 }

@@@ function 'oM2' (was 'X82') — structural (71.8%)
--- pretty-v2.1.19.js:389216
+++ pretty-v2.1.20.js:425040
@@ -55,7 +55,7 @@
     S = await m6(sM, ["send-keys", "-t", `${Cf}:${D}`, x, "Enter"]);
   if (S.code !== 0)
     throw Error(`Failed to send command to tmux window: ${S.stderr}`);
-  q((b) => ({
+  (q((x) => ({
     ...b,
     teamContext: {
       ...b.teamContext,
@@ -75,7 +75,17 @@
         },
       },
     },
-  }));
+  })),
+    _KK(q, {
+      teammateId: W,
+      sanitizedName: G,
+      teamName: _,
+      teammateColor: j,
+      prompt: w,
+      plan_mode_required: O,
+      paneId: V,
+      insideTmux: !1,
+    }));
   let g = PW1(_);
   if (!g)
     throw Error(

@@@ function 'ay6' (was 'sS6') — structural (71.7%)
--- pretty-v2.1.19.js:529739
+++ pretty-v2.1.20.js:534453
@@ -65,5 +65,25 @@
         reason: "Agent memory files are allowed for reading",
       },
     };
+  let w = Qv(M8(), "tasks") + IL;
+  if (A === w.slice(0, -1) || A.startsWith(w))
+    return {
+      behavior: "allow",
+      updatedInput: K,
+      decisionReason: {
+        type: "other",
+        reason: "Task files are allowed for reading",
+      },
+    };
+  let H = Qv(M8(), "teams") + IL;
+  if (A === H.slice(0, -1) || A.startsWith(H))
+    return {
+      behavior: "allow",
+      updatedInput: K,
+      decisionReason: {
+        type: "other",
+        reason: "Team files are allowed for reading",
+      },
+    };
   return { behavior: "passthrough", message: "" };
 }

@@@ function 'jjA' (was 'bDA') — structural (71.1%)
--- pretty-v2.1.19.js:419734
+++ pretty-v2.1.20.js:446942
@@ -20,9 +20,9 @@
           "report the issue at https://github.com/anthropics/claude-code/issues",
         PACKAGE_URL: "@anthropic-ai/claude-code",
         README_URL: "https://code.claude.com/docs/en/overview",
-        VERSION: "2.1.19",
+        VERSION: "2.1.20",
         FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-        BUILD_TIME: "2026-01-23T21:13:41Z",
+        BUILD_TIME: "2026-01-27T00:38:42Z",
       }.VERSION,
     ),
     W = J71(G),
@@ -40,7 +40,7 @@
       messages: Y,
       ...(z && { tools: z }),
       ...(w && { tool_choice: w }),
-      ...(H && { output_format: H }),
+      ...(H && { output_config: { format: H } }),
       ...(_.length > 0 && { betas: _ }),
       metadata: or(),
     },

@@@ function 'S9K' (was 'ia7') — structural (71.1%)
--- pretty-v2.1.19.js:416677
+++ pretty-v2.1.20.js:443818
@@ -1,5 +1,5 @@
 function ia7({ task_id: A, shell_id: K }) {
   let q = A ?? K;
   if (!q) return null;
-  return `Stop task: ${q}`;
+  return q;
 }

@@@ function 'rR6' (was 'uv6') — structural (70.7%)
--- pretty-v2.1.19.js:387006
+++ pretty-v2.1.20.js:411742
@@ -1,5 +1,5 @@
 function uv6(A) {
-  if (P8() && A?.team_name && A?.name) return a5A;
+  if (j8() && A?.name) return "";
   if (A?.subagent_type && A.subagent_type !== aw1.agentType)
     return A.subagent_type;
   return "Task";

@@@ function 'iiY' (was 'dp7') — structural (70.7%)
--- pretty-v2.1.19.js:390194
+++ pretty-v2.1.20.js:338894
@@ -1,7 +1,6 @@
 function dp7(A) {
-  let K = cK();
-  if (K === "foundry" || K === "firstParty")
-    return !A.toLowerCase().includes("claude-3-");
-  let q = A.toLowerCase();
+  let K = A.toLowerCase(),
+    q = gK();
+  if (q === "foundry" || q === "firstParty") return !K.includes("claude-3-");
   return q.includes("sonnet-4") || q.includes("opus-4");
 }

@@@ class 'GvK' (was 'njK') — structural (70.3%)
--- pretty-v2.1.19.js:575522
+++ pretty-v2.1.20.js:579675
@@ -3,21 +3,43 @@
   nextClientId = 1;
   server = null;
   running = !1;
+  socketPath = null;
   async start() {
     if (this.running) return;
-    let A = HxA();
-    if ((PO(`Creating socket listener: ${A}`), Lm6() !== "win32" && djK(A)))
+    if (((this.socketPath = TO1()), jQ6() !== "win32")) {
+      let A = zuA();
+      try {
+        if (!lr2(A).isDirectory()) PQ6(A);
+      } catch {}
+      ir2(A, { recursive: !0, mode: 448 });
+      try {
+        XvK(A, 448);
+      } catch {}
       try {
-        if (jm2(A).isSocket()) cjK(A);
+        let K = $vK(A);
+        for (let q of K) {
+          if (!q.endsWith(".sock")) continue;
+          let Y = parseInt(q.replace(".sock", ""), 10);
+          if (isNaN(Y)) continue;
+          try {
+            process.kill(Y, 0);
+          } catch {
+            try {
+              (PQ6(dr2(A, q)), k0(`Removed stale socket for PID ${Y}`));
+            } catch {}
+          }
+        }
       } catch {}
-    ((this.server = Wm2((K) => this.handleMcpClient(K))),
+    }
+    (k0(`Creating socket listener: ${this.socketPath}`),
+      (this.server = pr2((A) => this.handleMcpClient(A))),
       await new Promise((K, q) => {
-        (this.server.listen(A, () => {
+        (this.server.listen(this.socketPath, () => {
           if (
             (PO("Socket server listening for connections"), Lm6() !== "win32")
           )
             try {
-              (Dm2(A, 384), PO("Socket permissions set to 0600"));
+              (XvK(this.socketPath, 384), k0("Socket permissions set to 0600"));
             } catch (Y) {
               PO("Failed to set socket permissions:", Y);
             }
@@ -36,11 +58,15 @@
         this.server.close(() => K());
       }),
         (this.server = null));
-    let A = HxA();
-    if (Lm6() !== "win32" && djK(A))
+    if (jQ6() !== "win32" && this.socketPath && cr2(this.socketPath)) {
       try {
-        (cjK(A), PO("Cleaned up socket file"));
+        (PQ6(this.socketPath), k0("Cleaned up socket file"));
       } catch {}
+      try {
+        let A = zuA();
+        if ($vK(A).length === 0) (nr2(A), k0("Removed empty socket directory"));
+      } catch {}
+    }
     this.running = !1;
   }
   async isRunning() {

@@@ function 'LCK' (was 'HfK') — structural (70.0%)
--- pretty-v2.1.19.js:544500
+++ pretty-v2.1.20.js:549456
@@ -17,10 +17,10 @@
                 "report the issue at https://github.com/anthropics/claude-code/issues",
               PACKAGE_URL: "@anthropic-ai/claude-code",
               README_URL: "https://code.claude.com/docs/en/overview",
-              VERSION: "2.1.19",
+              VERSION: "2.1.20",
               FEEDBACK_CHANNEL:
                 "https://github.com/anthropics/claude-code/issues",
-              BUILD_TIME: "2026-01-23T21:13:41Z",
+              BUILD_TIME: "2026-01-27T00:38:42Z",
             }.VERSION,
             D,
             { loose: !0 },
@@ -28,7 +28,7 @@
           !SjA(D);
       if ((z(!!j), j))
         h(
-          `PackageManagerAutoUpdater: Update available ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.19", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-23T21:13:41Z" }.VERSION} -> ${D}`,
+          `PackageManagerAutoUpdater: Update available ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION} -> ${D}`,
         );
     }),
       (K[0] = H));
@@ -50,7 +50,9 @@
         ? "brew upgrade claude-code"
         : w === "winget"
           ? "winget upgrade Anthropic.ClaudeCode"
-          : "your package manager update command",
+          : w === "apk"
+            ? "apk upgrade claude-code"
+            : "your package manager update command",
     _;
   if (K[3] !== q)
     ((_ =
@@ -64,9 +66,9 @@
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.19",
+          VERSION: "2.1.20",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-01-23T21:13:41Z",
+          BUILD_TIME: "2026-01-27T00:38:42Z",
         }.VERSION,
       )),
       (K[3] = q),

@@@ function 'NkK' (was 'sPK') — structural (69.9%)
--- pretty-v2.1.19.js:537411
+++ pretty-v2.1.20.js:542591
@@ -26,19 +26,6 @@
       let _ = PQ2(A);
       if (_) $.push({ label: _, value: "yes-apply-suggestions" });
     }
-    if (NS() && z && !H && !VQ2(w ?? "", J) && K?.type !== "classifier")
-      $.push({
-        type: "input",
-        label: "Yes, and always allow Claude to",
-        value: "yes-classifier-reviewed",
-        placeholder: "describe what to allow...",
-        initialValue: w ?? "",
-        onChange: z,
-        allowEmptySubmitToCancel: !0,
-        showLabelWithValue: !0,
-        labelValueSeparator: ": ",
-        resetCursorOnUpdate: !0,
-      });
   }
   if (O)
     $.push({

@@@ function 'Lf1' (was '_P1') — structural (69.8%)
--- pretty-v2.1.19.js:449911
+++ pretty-v2.1.20.js:460671
@@ -1,4 +1,4 @@
-async function _P1(A, K, q, Y, z = !1) {
+async function Lf1(A, K, q, Y, z, w = !1) {
   try {
     if (A.length === 0) throw Error(sFA);
     let w = Fp(A),
@@ -29,7 +29,8 @@
     (K.setStreamMode?.("requesting"),
       K.setResponseLength?.(() => 0),
       K.setSpinnerMessage?.("Compacting conversation"));
-    let _ = VO6(Y),
+    let Z = i4("tengu_compact_cache_prefix", !1),
+      G = o$6(z),
       Z = z6({ content: _ }),
       G = await OW2({
         messages: A,
@@ -37,13 +38,18 @@
         appState: X,
         context: K,
         preCompactTokenCount: w,
+        cacheSafeParams: q,
       }),
       W = Bp(G);
     if (!W)
       throw (
+        h(`Compact failed: no summary text in response. Response: ${QA(D)}`, {
+          level: "error",
+        }),
         n("tengu_compact_failed", {
           reason: "no_summary",
           preCompactTokenCount: w,
+          promptCacheSharingEnabled: Z,
         }),
         Error(
           "Failed to generate conversation summary - response did not contain valid text content",
@@ -54,6 +60,7 @@
         n("tengu_compact_failed", {
           reason: "api_error",
           preCompactTokenCount: w,
+          promptCacheSharingEnabled: Z,
         }),
         Error(W)
       );
@@ -62,6 +69,7 @@
         n("tengu_compact_failed", {
           reason: "prompt_too_long",
           preCompactTokenCount: w,
+          promptCacheSharingEnabled: Z,
         }),
         Error(JW2)
       );
@@ -92,6 +100,7 @@
           (x.cache_read_input_tokens ?? 0) +
           x.output_tokens
         : 0,
+      promptCacheSharingEnabled: Z,
       ...J,
     });
     let S = ZP1(z ? "auto" : "manual", w ?? 0, A[A.length - 1]?.uuid),

@@@ function 'Wa2' (was 'mg2') — structural (69.7%)
--- pretty-v2.1.19.js:533230
+++ pretty-v2.1.20.js:537997
@@ -12,17 +12,17 @@
       });
     if (Y.status === 404)
       return (
-        h("Settings sync: No remote settings found (404)"),
+        L8("info", "settings_sync_fetch_empty"),
         { success: !0, isEmpty: !0 }
       );
     let z = CMK.safeParse(Y.data);
     if (!z.success)
       return (
-        h(`Settings sync: Invalid response format - ${z.error.message}`),
+        L8("warn", "settings_sync_fetch_invalid_format"),
         { success: !1, error: "Invalid settings sync response format" }
       );
     return (
-      h("Settings sync: Fetched successfully"),
+      L8("info", "settings_sync_fetch_success"),
       { success: !0, data: z.data, isEmpty: !1 }
     );
   } catch (A) {

@@@ function 'fb2' (was 'XwK') — structural (69.6%)
--- pretty-v2.1.19.js:479230
+++ pretty-v2.1.20.js:482605
@@ -8,6 +8,6 @@
       await (
         await M9(WL.createElement(TT2, null, A), { stdout: Y, debug: !0 })
       ).waitUntilExit(),
-      await K(q));
+      await K(Vb2(q)));
   });
 }

@@@ variable 'aZ1' (was 'ZWA') — structural (69.6%)
--- pretty-v2.1.19.js:389548
+++ pretty-v2.1.20.js:425432
@@ -62,11 +62,6 @@
         .describe(
           "Maximum number of agentic turns (API round-trips) before stopping. Used internally for warmup.",
         ),
-      allowed_tools: U.array(U.string())
-        .optional()
-        .describe(
-          'Tools to grant this agent. User will be prompted to approve if not already allowed. Example: ["Bash(git commit*)", "Read"]',
-        ),
     })),
     (G82 = U.object({
       name: U.string().optional().describe("Name for the spawned agent"),
@@ -145,7 +140,6 @@
         resume: z,
         run_in_background: w,
         max_turns: H,
-        allowed_tools: J,
         name: X,
         team_name: O,
         mode: $,
@@ -157,9 +151,10 @@
     ) {
       let D = Date.now(),
         j = await _.getAppState(),
-        M = j.toolPermissionContext.mode;
-      if (P8() && EG()) {
-        if ((O || j.teamContext?.teamName) && X)
+        M = D.toolPermissionContext.mode,
+        j = Hj2({ team_name: O }, D);
+      if (bG() && j) {
+        if (J)
           throw Error(
             "In-process teammates cannot spawn other teammates. Only the team leader can spawn teammates.",
           );
@@ -168,8 +163,7 @@
             "In-process teammates cannot spawn background agents. Use run_in_background=false for synchronous subagents.",
           );
       }
-      let P = O || j.teamContext?.teamName;
-      if (P8() && P && X) {
+      if (j && J) {
         let F = await hp7(
           {
             name: X,
@@ -226,7 +220,7 @@
       if (z) {
         let F = await vW1(vD(z));
         if (!F) throw Error(`No transcript found for agent ID: ${z}`);
-        R = F;
+        k = SP1(IP1(F));
       }
       let x = T?.forkContext ? _.messages : void 0,
         S;
@@ -258,7 +252,6 @@
           querySource: _.options.querySource ?? iU7(T.agentType, BD(T)),
           model: Y,
           maxTurns: H,
-          allowedTools: J,
           override: S ? { systemPrompt: S } : void 0,
         };
       if (w === !0 && !smA) {
@@ -276,7 +269,8 @@
           UXA(d, async () => {
             try {
               let o = [],
-                l = NBA();
+                a = VBA(),
+                l = NBA($.options.tools);
               for await (let GA of tC({
                 ...Q,
                 override: {
@@ -285,7 +279,9 @@
                   abortController: B.abortController,
                 },
               }))
-                (o.push(GA), iZA(l, GA), VD6(B.agentId, TBA(l), _.setAppState));
+                (d.push(OA),
+                  EGA(a, OA, l, $.options.tools),
+                  Hj6(Q.agentId, fBA(a), $.setAppState));
               let e = KE6(o, B.agentId, b),
                 XA = e.content
                   .filter((GA) => GA.type === "text")
@@ -378,8 +374,9 @@
                   return (
                     UXA(B, async () => {
                       try {
-                        let zA = NBA();
-                        for (let OA of d) iZA(zA, OA);
+                        let AA = VBA(),
+                          t = NBA($.options.tools);
+                        for (let ZA of u) EGA(AA, ZA, t, $.options.tools);
                         for await (let OA of tC({
                           ...Q,
                           isAsync: !0,
@@ -390,7 +387,7 @@
                           },
                         }))
                           (d.push(OA),
-                            iZA(zA, OA),
+                            EGA(AA, ZA, t, $.options.tools),
                             VD6(KA, TBA(zA), _.setAppState));
                         let HA = KE6(d, KA, b),
                           vA = HA.content
@@ -477,21 +474,11 @@
     },
     userFacingName: uv6,
     userFacingNameBackgroundColor: mv6,
-    async checkPermissions(A, K) {
-      if (!A.allowed_tools || A.allowed_tools.length === 0)
-        return { behavior: "allow", updatedInput: A };
-      let q = await K.getAppState(),
-        Y = Zs(q.toolPermissionContext),
-        z = A.allowed_tools.filter((w) => {
-          let H = OV(w);
-          return !Y.some((J) => Qp7(J, H));
-        });
-      if (z.length === 0) return { behavior: "allow", updatedInput: A };
-      return {
-        behavior: "ask",
-        message: `Agent requests tool permissions: ${z.join(", ")}`,
-        updatedInput: A,
-      };
+    getActivityDescription(A) {
+      return A?.description ?? "Running task";
+    },
+    async checkPermissions(A) {
+      return { behavior: "allow", updatedInput: A };
     },
     mapToolResultToToolResultBlockParam(A, K) {
       let q = A;

@@@ variable 't$6' (was 'TO6') — structural (69.5%)
--- pretty-v2.1.19.js:270946
+++ pretty-v2.1.20.js:267000
@@ -59,10 +59,19 @@
     },
     inputSchema: x4Y,
     outputSchema: B4Y,
-    async call(A, { options: { tools: K } }) {
+    async call(A, { options: { tools: K }, addNotification: q }) {
       let { query: q, max_results: Y = 5 } = A,
         z = K.filter(eV);
       m4Y(z);
+      function H($) {
+        if ($.length === 0) return;
+        q?.({
+          key: `tool-search-${Date.now()}`,
+          jsx: Cq7($.length),
+          priority: "immediate",
+          timeoutMs: 3000,
+        });
+      }
       function w(X, O) {
         n("tengu_tool_search_outcome", {
           query: q,
@@ -86,6 +95,7 @@
         return (
           h(`ToolSearchTool: selected "${X}"`),
           w([O.name], "select"),
+          H([_.name]),
           fO6([O.name], q, z.length)
         );
       }
@@ -95,6 +105,7 @@
           `ToolSearchTool: keyword search for "${q}", found ${J.length} matches`,
         ),
         w(J, "keyword"),
+        H(X),
         fO6(J, q, z.length)
       );
     },
@@ -102,7 +113,7 @@
       return { behavior: "allow", updatedInput: A };
     },
     renderToolUseMessage: n47,
-    userFacingName: () => "ToolSearch",
+    userFacingName: () => "",
     renderToolUseRejectedMessage: r47,
     renderToolUseErrorMessage: o47,
     renderToolUseProgressMessage: a47,

@@@ function 'qyK' (was 'STK') — structural (69.4%)
--- pretty-v2.1.19.js:551396
+++ pretty-v2.1.20.js:556520
@@ -13,7 +13,7 @@
       J = K?.selfAgentColor ?? l0();
     if (w && H) {
       let X = J ? AX[J] : "cyan_FOR_SUBAGENTS_ONLY";
-      return { text: `${w}@${H}`, bgColor: X };
+      return { text: `@${w}`, bgColor: O };
     }
   } else if (
     (K?.teammates ? Object.keys(K.teammates).length : 0) > 0 &&
@@ -30,11 +30,14 @@
         text: `View teammates: \`tmux -L ${gZ1()} a\``,
         bgColor: X ?? "cyan_FOR_SUBAGENTS_ONLY",
       };
-    else if (Y === !0 || O)
-      return {
-        text: `${J ? J.identity.agentName : ZH}@${K.teamName}`,
-        bgColor: X ?? "cyan_FOR_SUBAGENTS_ONLY",
-      };
+    else if (Y === !0 || X) {
+      if (J)
+        return {
+          text: `@${J.identity.agentName}`,
+          bgColor: O ?? "cyan_FOR_SUBAGENTS_ONLY",
+        };
+      return null;
+    }
   }
   if (P8()) {
     let w = yTK(A),

@@@ variable 'P$4' (was 'WU7') — structural (69.2%)
--- pretty-v2.1.19.js:384993
+++ pretty-v2.1.20.js:182385
@@ -14,5 +14,11 @@
   x9();
   dG1();
   rD();
+  UOA();
+  c8A();
+  $x();
+  iOA();
+  i6();
+  c2();
   S7 = r(JA(), 1);
 });

@@@ variable 'vp' (was 'Mp') — structural (69.2%)
--- pretty-v2.1.19.js:390210
+++ pretty-v2.1.20.js:338908
@@ -3,6 +3,5 @@
   w0();
   u8();
   J7();
-  l6();
   N82 = /\bultrathink\b/gi;
 });

@@@ variable 'Pd' (was 'xp') — structural (69.2%)
--- pretty-v2.1.19.js:448216
+++ pretty-v2.1.20.js:459209
@@ -28,5 +28,7 @@
   X5();
   F1();
   qp();
+  B1();
+  cp();
   YP1 = r(JA(), 1);
 });

@@@ variable 'kkK' (was 'Vf1') — structural (69.2%)
--- pretty-v2.1.19.js:487872
+++ pretty-v2.1.20.js:543074
@@ -10,16 +10,5 @@
   S4();
   wBA();
   o2();
-  Gf();
-  A4();
-  I1();
-  PZ();
-  Ax6();
-  uA();
-  FU();
-  Nt();
-  pD();
-  Ow();
-  U4();
   u4 = r(JA(), 1);
 });

@@@ function 'We2' (was 'yU2') — structural (69.2%)
--- pretty-v2.1.19.js:543421
+++ pretty-v2.1.20.js:548381
@@ -19,8 +19,6 @@
     case Hj1:
       return mVK;
     case ia:
-      return QVK;
-    case Is:
     case Cp:
     case d9:
       return PVK;

@@@ variable 'JU6' (was 'dVK') — structural (69.2%)
--- pretty-v2.1.19.js:543521
+++ pretty-v2.1.20.js:544869
@@ -10,22 +10,5 @@
   _T1();
   MVK();
   VVK();
-  _DA();
-  PgA();
-  XDA();
-  Wv();
-  LDA();
-  NVK();
-  kVK();
-  pgA();
-  Pg6();
-  sC6();
-  RVK();
-  QW1();
-  IVK();
-  Jj1();
-  gVK();
-  ZWA();
-  UVK();
   Tg6 = r(JA(), 1);
 });

@@@ variable '$CK' (was 'yNK') — structural (69.2%)
--- pretty-v2.1.19.js:548501
+++ pretty-v2.1.20.js:548479
@@ -17,5 +17,13 @@
   QK();
   kK();
   l6();
+  rQA();
+  GU6();
+  mh6();
+  tkK();
+  uP1();
+  ACK();
+  LV1();
+  OCK();
   _3 = r(JA(), 1);
 });

@@@ variable 'ARK' (was 'WvK') — structural (69.2%)
--- pretty-v2.1.19.js:554287
+++ pretty-v2.1.20.js:553607
@@ -3,5 +3,20 @@
   A4();
   Up();
   $F6();
+  d2();
+  n_();
+  ULK();
+  S9();
+  dLK();
+  yS();
+  w4();
+  lLK();
+  nLK();
+  sLK();
+  IK();
+  $q();
+  EK();
+  o7();
+  i6();
   wdA = r(JA(), 1);
 });

@@@ variable 'vIK' (was 'KEK') — structural (69.2%)
--- pretty-v2.1.19.js:556077
+++ pretty-v2.1.20.js:561177
@@ -1,7 +1,5 @@
 var KEK = C(() => {
   lA();
   l6();
-  sH();
-  r6();
   evK = r(JA(), 1);
 });

@@@ variable 'IIK' (was 'vEK') — structural (69.2%)
--- pretty-v2.1.19.js:557115
+++ pretty-v2.1.20.js:561382
@@ -1,9 +1,5 @@
 var vEK = C(() => {
   lA();
   uA();
-  Kw();
-  VF6();
-  I1();
-  P1();
   dv = r(JA(), 1);
 });

@@@ variable '_mK' (was 'uEK') — structural (69.2%)
--- pretty-v2.1.19.js:557754
+++ pretty-v2.1.20.js:568008
@@ -1,7 +1,5 @@
 var uEK = C(() => {
   lA();
   uA();
-  I3();
-  aM();
   Uw = r(JA(), 1);
 });

@@@ variable 'Bp6' (was 'DIK') — structural (69.2%)
--- pretty-v2.1.19.js:560612
+++ pretty-v2.1.20.js:568299
@@ -3,5 +3,6 @@
   Kw();
   VS();
   r6();
+  PmK();
   fv1 = r(JA(), 1);
 });

@@@ variable 'Qp6' (was 'nF6') — structural (69.2%)
--- pretty-v2.1.19.js:563923
+++ pretty-v2.1.20.js:568881
@@ -4,6 +4,5 @@
   l6();
   q9();
   CK();
-  S4();
   KG = r(JA(), 1);
 });

@@@ variable 'Up6' (was 'LSK') — structural (69.2%)
--- pretty-v2.1.19.js:565717
+++ pretty-v2.1.20.js:569876
@@ -2,20 +2,5 @@
   lA();
   uA();
   D8();
-  q9();
-  l6();
-  QM();
-  u8();
-  KM();
-  q6();
-  CK();
-  g4();
-  e1();
-  uA();
-  e6();
-  _H();
-  TSK();
-  ESK();
-  aM();
   KY = r(JA(), 1);
 });

@@@ variable 'qgK' (was 'JhK') — structural (69.2%)
--- pretty-v2.1.19.js:567241
+++ pretty-v2.1.20.js:570814
@@ -11,5 +11,14 @@
   tK();
   wq();
   I5();
+  Cp();
+  Vg6();
+  Y6();
+  qq();
+  jk();
+  ddA();
+  RZ();
+  w4();
+  fcA();
   Vj = r(JA(), 1);
 });

@@@ variable 'cp6' (was '_hK') — structural (69.2%)
--- pretty-v2.1.19.js:567447
+++ pretty-v2.1.20.js:571198
@@ -2,10 +2,5 @@
   uA();
   JhK();
   OhK();
-  A4();
-  QM();
-  PZ();
-  gB();
-  qp();
   E9A = r(JA(), 1);
 });

@@@ variable 'PgK' (was 'yhK') — structural (69.2%)
--- pretty-v2.1.19.js:567748
+++ pretty-v2.1.20.js:571325
@@ -1,4 +1,14 @@
 var yhK = C(() => {
   F1();
+  BA();
+  Bp6();
+  g8();
+  c_8();
+  cp6();
+  a1();
+  IK();
+  iq();
+  $q();
+  V2();
   Mn2 = r(zG1(), 1);
 });

@@@ variable 'CFK' (was 'bhK') — structural (69.2%)
--- pretty-v2.1.19.js:568070
+++ pretty-v2.1.20.js:574855
@@ -8,5 +8,7 @@
   D8();
   wf1();
   q9A();
+  ZH();
+  g8();
   pJ = r(JA(), 1);
 });

@@@ function 'zW2' (was 'c$2') — structural (69.0%)
--- pretty-v2.1.19.js:436394
+++ pretty-v2.1.20.js:413995
@@ -3,7 +3,6 @@
     "requestId" in A &&
     "success" in A &&
     !("member_name" in A) &&
-    !("status" in A) &&
-    !("target" in A)
+    !("status" in A)
   );
 }

@@@ function 'PWA' (was 'HDA') — structural (68.8%)
--- pretty-v2.1.19.js:398507
+++ pretty-v2.1.20.js:333753
@@ -1,14 +1,27 @@
 async function HDA(A) {
   if (A.length === 0) return;
-  let K = await Promise.all(A.map((Y) => _D1(Y, "projectSettings")));
+  let K = new Set(HmA.keys()),
+    q = await Promise.all(A.map((z) => LZ1(z, "projectSettings")));
   for (let Y = K.length - 1; Y >= 0; Y--)
     for (let { skill: z } of K[Y] ?? [])
       if (z.type === "prompt") Pi7.set(z.name, z);
   let q = K.flat().length;
-  if (q > 0)
-    h(
-      `[skills] Dynamically discovered ${q} skills from ${A.length} directories`,
-    );
+  if (Y > 0) {
+    let z = [...HmA.keys()].filter((w) => !K.has(w));
+    if (
+      (h(
+        `[skills] Dynamically discovered ${Y} skills from ${A.length} directories`,
+      ),
+      z.length > 0)
+    )
+      n("tengu_dynamic_skills_changed", {
+        source: "file_operation",
+        previousCount: K.size,
+        newCount: HmA.size,
+        addedCount: z.length,
+        directoryCount: A.length,
+      });
+  }
   for (let Y of Vi7)
     try {
       Y();

@@@ function 'kq7' (was 'yqK') — structural (68.8%)
--- pretty-v2.1.19.js:452073
+++ pretty-v2.1.20.js:266878
@@ -1,3 +1,3 @@
-function yqK(A, K) {
+function kq7(A) {
   return null;
 }

@@@ function 'r8K' (was 'M4K') — structural (68.6%)
--- pretty-v2.1.19.js:436406
+++ pretty-v2.1.20.js:414003
@@ -1,18 +1,7 @@
 function M4K(A, K, { verbose: q }) {
   let Y = typeof A === "string" ? _6(A) : A;
-  if (F$2(Y))
-    return FZ.default.createElement(f, { dimColor: !0 }, "  ", "Created team");
-  if (Q$2(Y))
-    return FZ.default.createElement(
-      f,
-      { dimColor: !0 },
-      "  ",
-      "broadcast to ",
-      Y.notifiedCount,
-      " teammate",
-      Y.notifiedCount === 1 ? "" : "s",
-      Y.notifiedCount > 0 ? `: ${Y.recipients.join(", ")}` : "",
-    );
+  if (eG2(Y)) return null;
+  if (AW2(Y)) return null;
   if (U$2(Y)) {
     let w = Y.teams.length;
     if (w === 0)
@@ -85,14 +74,6 @@
       "  ",
       "approved join request from ",
       Y.member_name,
-    );
-  if (l$2(Y))
-    return FZ.default.createElement(
-      f,
-      { dimColor: !0 },
-      "  ",
-      "shutdown request sent to ",
-      Y.target,
     );
   if (c$2(Y))
     return FZ.default.createElement(
@@ -101,13 +82,12 @@
       "  ",
       "rejected join request",
     );
-  if ("success" in Y && "message" in Y) {
-    let w = Y;
-    if (
-      w.message.includes("Plan approved") ||
-      w.message.includes("Plan rejected")
-    )
-      return FZ.default.createElement(f, { dimColor: !0 }, "  ", w.message);
-  }
-  return FZ.default.createElement(f, { dimColor: !0 }, "  ", Y.message);
+  if ("message" in Y)
+    return YP.default.createElement(f, { dimColor: !0 }, "  ", Y.message);
+  return YP.default.createElement(
+    f,
+    { dimColor: !0 },
+    "  ",
+    "operation complete",
+  );
 }

@@@ variable 'lqA' (was 'xqA') — structural (68.4%)
--- pretty-v2.1.19.js:398592
+++ pretty-v2.1.20.js:333852
@@ -23,7 +23,6 @@
   Kk6();
   kK();
   WgA();
-  ks();
   Kj = {
     name: c5,
     maxResultSizeChars: 1e5,
@@ -32,10 +31,14 @@
       return "A tool for editing files";
     },
     async prompt() {
-      return jd7;
+      return JV7();
     },
     userFacingName: XD1,
     getToolUseSummary: zi7,
+    getActivityDescription(A) {
+      let K = Hf6(A);
+      return K ? `Editing ${K}` : "Editing file";
+    },
     isEnabled() {
       return !0;
     },
@@ -119,7 +122,7 @@
           errorCode: 5,
         };
       let O = z.readFileState.get(w);
-      if (!O)
+      if (!X && !i4("tengu_marble_kite", !1))
         return {
           result: !1,
           behavior: "ask",
@@ -237,7 +240,8 @@
         let x = Aj(_),
           S = z.get(_);
         if (!S || x > S.timestamp) {
-          if (
+          if (!S && i4("tengu_marble_kite", !1));
+          else if (
             !(S && S.offset === void 0 && S.limit === void 0 && W === S.content)
           )
             throw Error(HEA);
@@ -315,7 +319,6 @@
     mapToolResultToToolResultBlockParam(
       {
         filePath: A,
-        originalFile: K,
         oldString: q,
         newString: Y,
         userModified: z,
@@ -332,18 +335,10 @@
           type: "tool_result",
           content: `The file ${A} has been updated${J}. All occurrences of '${q}' were successfully replaced with '${Y}'.`,
         };
-      if (Bk("tengu_file_edit_optimization", "enabled", !1))
-        return {
-          tool_use_id: H,
-          type: "tool_result",
-          content: `The file ${A} has been updated successfully${J}.`,
-        };
-      let { snippet: O, startLine: $ } = c_7(K || "", q, Y);
       return {
         tool_use_id: H,
         type: "tool_result",
-        content: `The file ${A} has been updated${J}. Here's the result of running \`cat -n\` on a snippet of the edited file:
-${eo({ content: O, startLine: $ })}`,
+        content: `The file ${A} has been updated successfully${H}.`,
       };
     },
   };

@@@ function 'jC2' (was 'OW2') — structural (68.1%)
--- pretty-v2.1.19.js:450046
+++ pretty-v2.1.20.js:460825
@@ -4,7 +4,36 @@
   appState: q,
   context: Y,
   preCompactTokenCount: z,
+  cacheSafeParams: w,
 }) {
+  if (i4("tengu_compact_cache_prefix", !1))
+    try {
+      let X = await PS({
+          promptMessages: [K],
+          cacheSafeParams: w,
+          canUseTool: MC2(),
+          querySource: "compact",
+          forkLabel: "compact",
+          maxTurns: 1,
+          maxOutputTokens: QiA,
+        }),
+        $ = Uf(X.messages);
+      if ($ && rB($)) return $;
+      (h(
+        `Compact cache sharing: no text in response, falling back. Response: ${QA($)}`,
+        { level: "warn" },
+      ),
+        n("tengu_compact_cache_sharing_fallback", {
+          reason: "no_text_response",
+          preCompactTokenCount: z,
+        }));
+    } catch (X) {
+      (qA(X instanceof Error ? X : Error(String(X))),
+        n("tengu_compact_cache_sharing_fallback", {
+          reason: "error",
+          preCompactTokenCount: z,
+        }));
+    }
   let w = lK("tengu_compact_streaming_retry", !1),
     H = w ? HW2 : 1;
   for (let J = 1; J <= H; J++) {
@@ -74,12 +103,17 @@
       continue;
     }
     throw (
+      h(
+        `Compact streaming failed after ${X} attempts. hasStartedStreaming=${$}`,
+        { level: "error" },
+      ),
       n("tengu_compact_failed", {
         reason: "no_streaming_response",
         preCompactTokenCount: z,
         hasStartedStreaming: X,
         retryEnabled: w,
         attempts: J,
+        promptCacheSharingEnabled: !1,
       }),
       Error(F5K)
     );

@@@ function 'iHK' (was 'g3K') — structural (68.1%)
--- pretty-v2.1.19.js:457783
+++ pretty-v2.1.20.js:462966
@@ -32,9 +32,9 @@
         ],
         userPrompt: `Command: ${A}
 Output: ${z}`,
-        enablePromptCaching: !0,
         signal: q,
         options: {
+          enablePromptCaching: !0,
           querySource: "bash_extract_command_paths",
           agents: [],
           isNonInteractiveSession: Y,

@@@ variable 'mPK' (was 'kZK') — structural (68.0%)
--- pretty-v2.1.19.js:513189
+++ pretty-v2.1.20.js:517177
@@ -5,7 +5,6 @@
   F1();
   F1();
   U2();
-  q6();
   ((jh2 = {
     type: "local-jsx",
     name: "fork",
@@ -15,14 +14,15 @@
     isHidden: !1,
     async call(A, K, q) {
       o7("fork");
-      let Y = q?.trim() || void 0;
+      let Y = q?.trim() || void 0,
+        z = i1();
       try {
         let {
             sessionId: z,
             title: w,
             forkPath: H,
             serializedMessages: J,
-          } = Gh2(Y),
+          } = await Pd2(Y),
           X = new Date(),
           O = J.find((j) => j.type === "user"),
           $ = (() => {
@@ -54,7 +54,9 @@
             customTitle: Z,
           },
           W = w ? ` "${w}"` : "",
-          D = `Forked conversation${W}. You are now in the fork.`;
+          M = `
+To resume the original: claude -r ${z}`,
+          j = `Forked conversation${D}. You are now in the fork.${M}`;
         if (K.resume)
           (await K.resume(z, G, "fork"), A(D, { display: "system" }));
         else A(`Forked conversation${W}. Resume with: /resume ${z}`);

@@@ function 'VEK' (was 'eMK') — structural (67.7%)
--- pretty-v2.1.19.js:534207
+++ pretty-v2.1.20.js:538976
@@ -1,11 +1,11 @@
-function eMK(A, K, q) {
+async function VEK(A, K, q) {
   let Y = { messages: 0, errors: 0 };
   try {
-    let z = hA().readdirSync(A);
+    let z = await uA().readdir(A);
     for (let w of z)
       try {
         if (WF2(w.name) < K)
-          if ((hA().unlinkSync(af(A, w.name)), q)) Y.messages++;
+          if ((await uA().unlink(NP(A, w.name)), q)) Y.messages++;
           else Y.errors++;
       } catch (H) {
         qA(H);

@@@ function 'AwK' (was 'e6K') — structural (67.3%)
--- pretty-v2.1.19.js:430175
+++ pretty-v2.1.20.js:454151
@@ -1,5 +1,5 @@
 function e6K(A) {
-  let K = a(30),
+  let K = s(31),
     {
       userMessage: q,
       color: Y,
@@ -23,6 +23,7 @@
     return V;
   }
   let X = q.message.content,
+    X = typeof O === "string" ? null : O[O.length - 1],
     O,
     $,
     _,
@@ -31,18 +32,25 @@
     W,
     D,
     j;
-  if (K[3] !== Y || K[4] !== J || K[5] !== X || K[6] !== z || K[7] !== H) {
+  if (
+    K[3] !== Y ||
+    K[4] !== J ||
+    K[5] !== O ||
+    K[6] !== z ||
+    K[7] !== X ||
+    K[8] !== H
+  ) {
     j = Symbol.for("react.early_return_sentinel");
     A: {
       let V =
         typeof X === "string"
           ? X.trim()
-          : X[X.length - 1]?.type === "text"
-            ? X[X.length - 1].text.trim()
+          : X && KwK(X)
+            ? X.text.trim()
             : "(no prompt)";
       if (kG1(V)) {
         let N;
-        if (K[16] !== Y || K[17] !== z)
+        if (K[17] !== Y || K[18] !== z)
           ((N = I6.createElement(
             I,
             { flexDirection: "row", width: "100%" },
@@ -52,10 +60,10 @@
               "((empty message))",
             ),
           )),
-            (K[16] = Y),
             (K[17] = z),
-            (K[18] = N));
-        else N = K[18];
+            (K[18] = z),
+            (K[19] = T));
+        else T = K[19];
         j = N;
         break A;
       }
@@ -63,10 +71,10 @@
         let N = d7(V, "bash-input");
         if (N) {
           let T;
-          if (K[19] === Symbol.for("react.memo_cache_sentinel"))
+          if (K[20] === Symbol.for("react.memo_cache_sentinel"))
             ((T = I6.createElement(f, { color: "bashBorder" }, "!")),
-              (K[19] = T));
-          else T = K[19];
+              (K[20] = k));
+          else k = K[20];
           j = I6.createElement(
             I,
             { flexDirection: "row", width: "100%" },
@@ -125,34 +133,35 @@
       (K[12] = G),
       (K[13] = W),
       (K[14] = D),
-      (K[15] = j));
+      (K[15] = M),
+      (K[16] = j));
   } else
-    ((O = K[8]),
-      ($ = K[9]),
+    (($ = K[9]),
       (_ = K[10]),
       (Z = K[11]),
       (G = K[12]),
       (W = K[13]),
       (D = K[14]),
-      (j = K[15]));
+      (M = K[15]),
+      (j = K[16]));
   if (j !== Symbol.for("react.early_return_sentinel")) return j;
   let M;
-  if (K[20] !== O || K[21] !== _ || K[22] !== Z || K[23] !== G)
+  if (K[21] !== $ || K[22] !== Z || K[23] !== G || K[24] !== W)
     ((M = I6.createElement(O, { color: _, dimColor: Z }, G)),
-      (K[20] = O),
       (K[21] = _),
       (K[22] = Z),
       (K[23] = G),
-      (K[24] = M));
-  else M = K[24];
+      (K[24] = W),
+      (K[25] = P));
+  else P = K[25];
   let P;
-  if (K[25] !== $ || K[26] !== W || K[27] !== D || K[28] !== M)
+  if (K[26] !== _ || K[27] !== D || K[28] !== M || K[29] !== P)
     ((P = I6.createElement($, { flexDirection: W, width: D }, M)),
-      (K[25] = $),
       (K[26] = W),
       (K[27] = D),
       (K[28] = M),
-      (K[29] = P));
-  else P = K[29];
+      (K[29] = P),
+      (K[30] = V));
+  else V = K[30];
   return P;
 }

@@@ function 'eZ2' (was 'U12') — structural (67.1%)
--- pretty-v2.1.19.js:383765
+++ pretty-v2.1.20.js:408436
@@ -1,7 +1,9 @@
 function U12(A) {
   let K = [],
-    q =
-      /<teammate-message\s+teammate_id="([^"]+)"(?:\s+color="([^"]+)")?>\n?([\s\S]*?)\n?<\/teammate-message>/g;
+    q = new RegExp(
+      `<${IO}\\s+teammate_id="([^"]+)"(?:\\s+color="([^"]+)")?>\\n?([\\s\\S]*?)\\n?<\\/${IO}>`,
+      "g",
+    );
   for (let Y of A.matchAll(q))
     if (Y[1] && Y[3])
       K.push({ teammateId: Y[1], color: Y[2], content: Y[3].trim() });

@@@ function 'djA' (was 'EjA') — structural (67.1%)
--- pretty-v2.1.19.js:452891
+++ pretty-v2.1.20.js:470379
@@ -9,21 +9,8 @@
     X = new Map();
   try {
     let G = await xqK(A),
-      W = G.length,
-      D = 0;
-    if (G[0] === 239 && G[1] === 187 && G[2] === 191) D = 3;
-    while (D < W) {
-      let j = G.indexOf(10, D);
-      if (j === -1) j = W;
-      let M = G.toString("utf8", D, j).trim();
-      if (((D = j + 1), !M)) continue;
-      let P;
-      try {
-        P = JSON.parse(M);
-      } catch (V) {
-        qA(Error(`Error parsing line in ${A}: ${V}`));
-        continue;
-      }
+      W = K1A(G);
+    for (let D of W)
       if (Ru(P)) {
         if (
           P.type === "progress" &&
@@ -46,7 +33,6 @@
         H.set(P.sessionId, P.agentColor);
       else if (P.type === "file-history-snapshot") J.set(P.messageId, P);
       else if (P.type === "attribution-snapshot") X.set(P.messageId, P);
-    }
   } catch {}
   let O = [...K.values()],
     $ = new Set(O.map((G) => G.parentUuid).filter((G) => G !== null)),

@@@ variable 'Xf1' (was 'XM1') — structural (66.7%)
--- pretty-v2.1.19.js:431073
+++ pretty-v2.1.20.js:455056
@@ -32,5 +32,7 @@
   I1();
   lM();
   JM1();
+  aj();
+  Of1();
   DFA = new Map();
 });

@@@ function 'Yy2' (was 'Cj2') — structural (66.7%)
--- pretty-v2.1.19.js:456867
+++ pretty-v2.1.20.js:468715
@@ -1,54 +1,9 @@
 function Cj2(A) {
-  let q = `Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits (with the exception of the plan file mentioned below), run any non-readonly tools (including changing configs or making commits), or otherwise make any changes to the system. This supercedes any other instructions you have received.
+  let q = `Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits, run any non-readonly tools (including changing configs or making commits), or otherwise make any changes to the system. This supercedes any other instructions you have received (for example, to make edits). Instead, you should:
 
 ## Plan File Info:
-${A.planExists ? `A plan file already exists at ${A.planFilePath}. You can read it and make incremental edits using the ${Kj.name} tool.` : `No plan file exists yet. You should create your plan at ${A.planFilePath} using the ${qj.name} tool.`}
-
-## Iterative Planning Workflow
-
-Your goal is to build a comprehensive plan through iterative refinement and interviewing the user. Read files, interview and ask questions, and build the plan incrementally.
-
-### How to Work
-
-0. Write your plan in the plan file specified above. This is the ONLY file you are allowed to edit.
-
-1. **Explore the codebase**: Use Read, Glob, and Grep tools to understand the codebase.
-You have access to the ${GC.agentType} agent type if you want to delegate search.
-Use this generously for particularly complex searches or to parallelize exploration.
-
-2. **Interview the user**: Use ${_X} to interview the user and ask questions that:
-   - Clarify ambiguous requirements
-   - Get user input on technical decisions and tradeoffs
-   - Understand preferences for UI/UX, performance, edge cases
-   - Validate your understanding before committing to an approach
-   Make sure to:
-   - Not ask any questions that you could find out yourself by exploring the codebase.
-   - Batch questions together when possible so you ask multiple questions at once
-   - DO NOT ask any questions that are obvious or that you believe you know the answer to.
-
-3. **Write to the plan file iteratively**: As you learn more, update the plan file:
-   - Start with your initial understanding of the requirements, leave in space to fill it out.
-   - Add sections as you explore and learn about the codebase
-   - Refine based on user answers to your questions
-   - The plan file is your working document - edit it as your understanding evolves
-
-4. **Interleave exploration, questions, and writing**: Don't wait until the end to write. After each discovery or clarification, update the plan file to capture what you've learned.
-
-5. **Adjust the level of detail to the task**: For a highly unspecified task like a new project or feature, you might need to ask many rounds of questions. Whereas for a smaller task you may need only some or a few.
-
-### Plan File Structure
-Your plan file should be divided into clear sections using markdown headers, based on the request. Fill out these sections as you go.
-- Include only your recommended approach, not all alternatives
-- Ensure that the plan file is concise enough to scan quickly, but detailed enough to execute effectively
-- Include the paths of critical files to be modified
-- Include a verification section describing how to test the changes end-to-end (run the code, use MCP tools, run tests)
-
-### Ending Your Turn
-
-Your turn should only end by either:
-- Using ${_X} to gather more information
-- Calling ${mZ.name} when the plan is ready for approval
-
-**Important:**: Use ${mZ.name} to request plan approval. Do NOT ask about plan approval via text or AskUserQuestion.`;
+${A.planExists ? `A plan file already exists at ${A.planFilePath}. You can read it and make incremental edits using the ${aD.name} tool if you need to.` : `No plan file exists yet. You should create your plan at ${A.planFilePath} using the ${sD.name} tool if you need to.`}
+You should build your plan incrementally by writing to or editing this file. NOTE that this is the only file you are allowed to edit - other than this you are only allowed to take READ-ONLY actions.
+Answer the user's query comprehensively, using the ${xJ} tool if you need to ask the user clarifying questions. If you do use the ${xJ}, make sure to ask all clarifying questions you need to fully understand the user's intent before proceeding.`;
   return c9([z6({ content: q, isMeta: !0 })]);
 }

@@@ variable 'EFK' (was 'rSK') — structural (66.7%)
--- pretty-v2.1.19.js:566867
+++ pretty-v2.1.20.js:574304
@@ -13,6 +13,55 @@
   Z_();
   _DA();
   dK();
-  TdA = new Map();
+  ba();
+  Xf1();
+  W_1();
+  ZH();
+  ZFK();
+  Q4();
+  DwA();
+  pb1();
+  db1();
+  Pd();
+  B2();
+  lw();
+  tp6();
+  Zz();
+  RBA();
+  It();
+  SB();
+  $z();
+  g8();
+  Gr();
+  m4();
+  Y6();
+  Ta();
+  DFK();
+  qq();
+  i4A();
+  Gf();
+  Uj();
+  nN();
+  qWA();
+  Uj();
+  RZ();
+  tWA();
+  Xv1();
+  Lg6();
+  H7();
+  Y6();
+  aj();
+  fcA();
+  hH();
+  YUA();
+  B1();
+  JE1();
+  OX();
+  r6();
+  jFK();
+  j2();
+  oH();
+  Vv();
+  r0();
   v9A = new Map();
 });

@@@ function 'i1z' (was 'Ac2') — structural (66.1%)
--- pretty-v2.1.19.js:554560
+++ pretty-v2.1.20.js:559660
@@ -54,8 +54,41 @@
                 return;
               }
               case "ask": {
-                let D = !1,
+                let V = function () {
+                    A((T) =>
+                      T.map((k) =>
+                        k.toolUseID === H
+                          ? { ...k, classifierCheckInProgress: !1 }
+                          : k,
+                      ),
+                    );
+                  },
+                  D = !1,
                   j = !1;
+                if (
+                  j8() &&
+                  yMA() &&
+                  q.name === k7 &&
+                  Z.pendingClassifierCheck
+                ) {
+                  let T = await PP1(
+                    Z.pendingClassifierCheck,
+                    z.abortController.signal,
+                    z.options.isNonInteractiveSession,
+                  );
+                  if (T) {
+                    (DcA(z, H, "accept", "classifier"),
+                      McA(q.name, "accept", "classifier"),
+                      WcA(q, Y, z, w.message.id, H, { type: "classifier" }),
+                      O({
+                        behavior: "allow",
+                        updatedInput: Z.updatedInput ?? Y,
+                        userModified: !1,
+                        decisionReason: T,
+                      }));
+                    return;
+                  }
+                }
                 if (P8() && vFA())
                   try {
                     let N = MM1({
@@ -146,8 +179,9 @@
                     toolUseID: H,
                     permissionResult: Z,
                     permissionPromptStartTimeMs: M,
+                    classifierCheckInProgress: !!Z.pendingClassifierCheck,
                     onUserInteraction() {
-                      j = !0;
+                      ((M = !0), V());
                     },
                     onAbort() {
                       if (D) return;
@@ -300,33 +334,48 @@
                     z.options.isNonInteractiveSession,
                     {
                       shouldContinue: () => !D && !j,
+                      onComplete: V,
                       onAllow: (N) => {
-                        if (
-                          ((D = !0),
-                          A((T) => T.filter((k) => k.toolUseID !== H)),
-                          N.type === "classifier")
-                        ) {
-                          let T =
-                            N.reason.match(
-                              /^Allowed by prompt rule: "(.+)"$/,
-                            )?.[1] ?? N.reason;
-                          _m7(H, T);
-                        }
-                        (lT1(
-                          q,
-                          Y,
-                          z,
-                          w.message.id,
-                          H,
-                          { type: "classifier" },
-                          M,
+                        D = !0;
+                        let k =
+                          T.type === "classifier"
+                            ? (T.reason.match(
+                                /^Allowed by prompt rule: "(.+)"$/,
+                              )?.[1] ?? T.reason)
+                            : void 0;
+                        (A((b) =>
+                          b.map((S) =>
+                            S.toolUseID === H
+                              ? {
+                                  ...S,
+                                  classifierCheckInProgress: !1,
+                                  classifierAutoApproved: !0,
+                                  classifierMatchedRule: k,
+                                }
+                              : S,
+                          ),
                         ),
+                          WcA(
+                            q,
+                            Y,
+                            z,
+                            w.message.id,
+                            H,
+                            { type: "classifier" },
+                            j,
+                          ),
                           X({
                             behavior: "allow",
                             updatedInput: Y,
                             userModified: !1,
                             decisionReason: N,
                           }));
+                        let R = setTimeout(() => {
+                          A((b) => b.filter((S) => S.toolUseID !== H));
+                        }, 800);
+                        z.abortController.signal.addEventListener("abort", () =>
+                          clearTimeout(R),
+                        );
                       },
                     },
                   );
@@ -335,7 +384,7 @@
             }
           })
           .catch((Z) => {
-            if (Z instanceof Xz) (O(), $(void 0, !0));
+            if (Z instanceof x2 || Z instanceof m2) (X(), $(void 0, !0));
             else qA(Z);
           });
       });

@@@ function 'Da2' (was 'gg2') — structural (65.9%)
--- pretty-v2.1.19.js:533276
+++ pretty-v2.1.20.js:538043
@@ -5,7 +5,12 @@
     if (A.skipRetry) return A;
     if (K > nm6) return A;
     let q = Q5A(K);
-    (h(`Settings sync: Retry ${K}/${nm6} after ${q}ms`), await ar(q));
+    (L8("info", "settings_sync_retry", {
+      attempt: K,
+      maxRetries: gQ6,
+      delayMs: q,
+    }),
+      await Eo(q));
   }
   return A;
 }

@@@ function 'KN1' (was 'i31') — structural (65.6%)
--- pretty-v2.1.19.js:212025
+++ pretty-v2.1.20.js:465786
@@ -16,13 +16,13 @@
       $ = {};
     if (X.extraKnownMarketplaces?.[A]) {
       let _ = { ...X.extraKnownMarketplaces };
-      (delete _[A], ($.extraKnownMarketplaces = _), (O = !0));
+      ((Z[A] = void 0), (_.extraKnownMarketplaces = Z), ($ = !0));
     }
     if (X.enabledPlugins) {
       let _ = `@${A}`,
         Z = { ...X.enabledPlugins },
         G = !1;
-      for (let W in Z) if (W.endsWith(_)) (delete Z[W], (G = !0));
+      for (let D in G) if (D.endsWith(Z)) ((G[D] = void 0), (W = !0));
       if (G) (($.enabledPlugins = Z), (O = !0));
     }
     if (O) {
@@ -35,5 +35,7 @@
       else h(`Cleaned up marketplace '${A}' from ${J} settings`);
     }
   }
+  let J = lI4(A);
+  for (let O of J) mjA(O);
   h(`Removed marketplace source: ${A}`);
 }

@@@ function 'S_q' (was 'GH5') — structural (65.6%)
--- pretty-v2.1.19.js:27530
+++ pretty-v2.1.20.js:27625
@@ -1,10 +1,14 @@
 async function GH5(A) {
   if (process.platform === "win32") {
-    let q = await YY(`where.exe ${A}`, { shell: !0, reject: !1 });
+    let q = await zY(`where.exe ${A}`, {
+      shell: !0,
+      stderr: "ignore",
+      reject: !1,
+    });
     if (q.exitCode !== 0 || !q.stdout) return null;
     return q.stdout.trim().split(/\r?\n/)[0] || null;
   }
-  let K = await YY(`which ${A}`, { shell: !0, reject: !1 });
+  let K = await zY(`which ${A}`, { shell: !0, stderr: "ignore", reject: !1 });
   if (K.exitCode !== 0 || !K.stdout) return null;
   return K.stdout.trim();
 }

@@@ function 'Xp2' (was 'XS2') — structural (65.5%)
--- pretty-v2.1.19.js:507560
+++ pretty-v2.1.20.js:511535
@@ -24,5 +24,13 @@
         status: A.status,
         task: A,
       };
+    case "in_process_teammate":
+      return {
+        id: A.id,
+        type: "in_process_teammate",
+        label: `@${A.identity.agentName}`,
+        status: A.status,
+        task: A,
+      };
   }
 }

@@@ function '_b8' (was 'ml9') — structural (65.2%)
--- pretty-v2.1.19.js:247283
+++ pretty-v2.1.20.js:103049
@@ -1,3 +1,9 @@
 function ml9() {
-  return `----AzSDKFormBoundary${xIA()}`;
+  return `Writes a file to the local filesystem.
+
+Usage:
+- This tool will overwrite the existing file if there is one at the provided path.${NH5()}
+- ALWAYS prefer editing existing files in the codebase. NEVER write new files unless explicitly required.
+- NEVER proactively create documentation files (*.md) or README files. Only create documentation files if explicitly requested by the User.
+- Only use emojis if the user explicitly requests it. Avoid writing emojis to files unless asked.`;
 }

@@@ function 'Fe9' (was 'hJY') — structural (65.2%)
--- pretty-v2.1.19.js:285552
+++ pretty-v2.1.20.js:246202
@@ -1,7 +1,3 @@
 function hJY() {
-  return `
-
-[OUTPUT TRUNCATED - exceeded ${O01()} token limit]
-
-The tool output was truncated. If this MCP server provides pagination or filtering tools, use them to retrieve specific portions of the data. If pagination is not available, inform the user that you are working with truncated output and results may be incomplete.`;
+  return `----AzSDKFormBoundary${USA()}`;
 }

@@@ function 'yGY' (was 'Y27') — structural (65.2%)
--- pretty-v2.1.19.js:285822
+++ pretty-v2.1.20.js:281667
@@ -1,3 +1,7 @@
 function Y27() {
-  return `claude-mcp-browser-bridge-${UJY()}`;
+  return `
+
+[OUTPUT TRUNCATED - exceeded ${GO1()} token limit]
+
+The tool output was truncated. If this MCP server provides pagination or filtering tools, use them to retrieve specific portions of the data. If pagination is not available, inform the user that you are working with truncated output and results may be incomplete.`;
 }

@@@ function 'zuA' (was 'v_K') — structural (65.2%)
--- pretty-v2.1.19.js:508113
+++ pretty-v2.1.20.js:282078
@@ -1,3 +1,3 @@
 function v_K() {
-  return `thinkback@${T_K()}`;
+  return `/tmp/claude-mcp-browser-bridge-${aG6()}`;
 }

@@@ function 'xE7' (was 'Si7') — structural (65.1%)
--- pretty-v2.1.19.js:399101
+++ pretty-v2.1.20.js:334357
@@ -1,11 +1,18 @@
 function Si7(
-  { filePath: A, content: K, structuredPatch: q, type: Y },
+  { filePath: A, content: K, structuredPatch: q, type: Y, originalFile: z },
   z,
   { style: w, verbose: H },
 ) {
   switch (Y) {
     case "create": {
-      if (w === "condensed" && !H) {
+      if (A.startsWith(aG()) && !J) {
+        if (H !== "condensed")
+          return Fq.createElement(
+            R6,
+            null,
+            Fq.createElement(f, { dimColor: !0 }, "/plan to preview"),
+          );
+      } else if (H === "condensed" && !J) {
         let J = K.split(vi7).length;
         return xq.createElement(
           f,
@@ -27,6 +34,8 @@
         firstLine:
           K.split(`
 `)[0] ?? null,
+        fileContent: z ?? void 0,
+        style: H,
         verbose: H,
         previewHint: J ? "/plan to preview" : void 0,
       });

@@@ function 'KG2' (was 'd12') — structural (64.9%)
--- pretty-v2.1.19.js:383825
+++ pretty-v2.1.20.js:408498
@@ -4,7 +4,10 @@
     z = UG1(A.content, Y);
   if (z) return lq.createElement(lq.Fragment, { key: K }, z);
   let w = cQ7(A.content);
-  if (w) return lq.createElement(lq.Fragment, { key: K }, w);
+  if (w) {
+    if (j8()) return null;
+    return Q5.createElement(Q5.Fragment, { key: K }, w);
+  }
   let H = iQ7(A.content);
   if (H) return lq.createElement(lq.Fragment, { key: K }, H);
   let J = rQ7(A.content);
@@ -18,13 +21,13 @@
     let O = X;
     return lq.createElement(
       I,
-      { key: K, flexDirection: "column" },
+      { key: K, flexDirection: "column", marginTop: 1 },
       lq.createElement(
         f,
         { color: q },
         mY,
         " ",
-        lq.createElement(f, { bold: !0 }, Y),
+        Q5.createElement(f, { bold: !0 }, "@", Y),
       ),
       lq.createElement(
         v6,
@@ -45,17 +48,18 @@
   if (X?.type === "teammate_terminated")
     return lq.createElement(
       I,
-      { key: K, flexDirection: "column" },
+      { key: K, flexDirection: "column", marginTop: 1 },
       lq.createElement(f, null, mY, " ", X.message),
     );
   return lq.createElement(
     I,
-    { key: K, flexDirection: "column" },
+    { key: K, flexDirection: "column", marginTop: 1 },
     lq.createElement(
       f,
       { color: q },
-      "● ",
-      lq.createElement(f, { bold: !0 }, Y),
+      uY,
+      " ",
+      Q5.createElement(f, { bold: !0 }, "@", Y),
       ":",
     ),
     lq.createElement(

@@@ function 'tLK' (was 'RNK') — structural (64.8%)
--- pretty-v2.1.19.js:548156
+++ pretty-v2.1.20.js:553196
@@ -1,5 +1,5 @@
 function RNK(A) {
-  let K = a(25),
+  let K = s(26),
     {
       exitMessage: q,
       vimMode: Y,
@@ -49,34 +49,38 @@
   else j = K[5];
   let M = j,
     P;
-  if (K[6] !== D || K[7] !== G || K[8] !== Z || K[9] !== W)
+  if (K[6] === Symbol.for("react.memo_cache_sentinel"))
+    ((P = eLK() && fq.createElement(vAz, null)), (K[6] = P));
+  else P = K[6];
+  let V;
+  if (K[7] !== D || K[8] !== G || K[9] !== Z || K[10] !== W)
     ((P =
       Z &&
       _3.createElement(ENK, { value: G, onChange: W, historyFailedMatch: D })),
-      (K[6] = D),
       (K[7] = G),
       (K[8] = Z),
       (K[9] = W),
-      (K[10] = P));
-  else P = K[10];
+      (K[10] = W),
+      (K[11] = V));
+  else V = K[11];
   let V;
-  if (K[11] !== M)
+  if (K[12] !== j)
     ((V = M
       ? _3.createElement(f, { dimColor: !0, key: "vim-insert" }, "-- INSERT --")
       : null),
-      (K[11] = M),
-      (K[12] = V));
-  else V = K[12];
+      (K[12] = j),
+      (K[13] = N));
+  else N = K[13];
   let N = !H && !M,
     T;
   if (
-    K[13] !== O ||
     K[14] !== $ ||
     K[15] !== z ||
     K[16] !== N ||
     K[17] !== J ||
     K[18] !== X ||
-    K[19] !== w
+    K[19] !== O ||
+    K[20] !== w
   )
     ((T = _3.createElement(Ip2, {
       mode: z,
@@ -87,28 +91,29 @@
       diffSelected: O,
       loopSelected: $,
     })),
-      (K[13] = O),
       (K[14] = $),
       (K[15] = z),
       (K[16] = N),
       (K[17] = J),
       (K[18] = X),
       (K[19] = w),
-      (K[20] = T));
-  else T = K[20];
+      (K[20] = w),
+      (K[21] = k));
+  else k = K[21];
   let k;
-  if (K[21] !== P || K[22] !== V || K[23] !== T)
+  if (K[22] !== V || K[23] !== N || K[24] !== k)
     ((k = _3.createElement(
       I,
       { justifyContent: "flex-start", gap: 1 },
       P,
       V,
       T,
+      k,
     )),
-      (K[21] = P),
       (K[22] = V),
       (K[23] = T),
-      (K[24] = k));
-  else k = K[24];
+      (K[24] = k),
+      (K[25] = R));
+  else R = K[25];
   return k;
 }

@@@ function 'DM2' (was 'P$2') — structural (64.8%)
--- pretty-v2.1.19.js:434190
+++ pretty-v2.1.20.js:422411
@@ -1,10 +1,17 @@
-function P$2(A, K, q) {
+function DM2(A, K) {
   return async (Y, z, w, H, J) => {
     let X = await $_(Y, z, w, H, J);
     if (X.behavior !== "ask") return X;
+    if (q.name === k7 && J.pendingClassifierCheck) {
+      let _ = await PP1(
+        J.pendingClassifierCheck,
+        K.signal,
+        z.options.isNonInteractiveSession,
+      );
+      if (_) return { behavior: "allow", updatedInput: Y, decisionReason: _ };
+    }
     if (q.signal.aborted) return { behavior: "ask", message: ZS };
     let O = await w.getAppState(),
-      $ = O.viewingAgentTaskId === K,
       _ = await Y.description(z, {
         isNonInteractiveSession: w.options.isNonInteractiveSession,
         toolPermissionContext: O.toolPermissionContext,
@@ -12,7 +19,7 @@
       });
     if (q.signal.aborted) return { behavior: "ask", message: ZS };
     let Z = Q8K();
-    if ($ && Z)
+    if ($)
       return new Promise((G) => {
         let W = !1,
           D = () => {
@@ -33,6 +40,9 @@
               toolUseID: J,
               permissionResult: X,
               permissionPromptStartTimeMs: Date.now(),
+              workerBadge: A.color
+                ? { name: A.agentName, color: A.color }
+                : void 0,
               onUserInteraction() {},
               onAbort() {
                 if (W) return;
@@ -42,7 +52,19 @@
               },
               async onAllow(M, P, V) {
                 if (W) return;
-                ((W = !0), q.signal.removeEventListener("abort", D), xg(P));
+                if (
+                  ((Z = !0),
+                  K.signal.removeEventListener("abort", G),
+                  sg(M),
+                  M.length > 0)
+                ) {
+                  let V = P4K();
+                  if (V) {
+                    let N = await z.getAppState(),
+                      T = pN(N.toolPermissionContext, M);
+                    V(T);
+                  }
+                }
                 let N = V?.trim();
                 G({
                   behavior: "allow",

@@@ function 'Md' (was 'cqA') — structural (64.4%)
--- pretty-v2.1.19.js:420892
+++ pretty-v2.1.20.js:448636
@@ -20,7 +20,7 @@
     ...(ew() ? [jt7, kt7, Bt7, it7] : []),
     ...(at7 ? [at7] : []),
     aC6,
-    ...(P8() ? [I22()] : []),
+    ...(j8() ? [eT2(), Av2()] : []),
     ...(ot7 ? [ot7] : []),
     LU,
     RU,

@@@ function 'Ky2' (was 'Rj2') — structural (64.3%)
--- pretty-v2.1.19.js:456928
+++ pretty-v2.1.20.js:468654
@@ -1,9 +1,54 @@
 function Rj2(A) {
-  let q = `Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits, run any non-readonly tools (including changing configs or making commits), or otherwise make any changes to the system. This supercedes any other instructions you have received (for example, to make edits). Instead, you should:
+  let q = `Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits (with the exception of the plan file mentioned below), run any non-readonly tools (including changing configs or making commits), or otherwise make any changes to the system. This supercedes any other instructions you have received.
 
 ## Plan File Info:
-${A.planExists ? `A plan file already exists at ${A.planFilePath}. You can read it and make incremental edits using the ${Kj.name} tool if you need to.` : `No plan file exists yet. You should create your plan at ${A.planFilePath} using the ${qj.name} tool if you need to.`}
-You should build your plan incrementally by writing to or editing this file. NOTE that this is the only file you are allowed to edit - other than this you are only allowed to take READ-ONLY actions.
-Answer the user's query comprehensively, using the ${_X} tool if you need to ask the user clarifying questions. If you do use the ${_X}, make sure to ask all clarifying questions you need to fully understand the user's intent before proceeding.`;
+${A.planExists ? `A plan file already exists at ${A.planFilePath}. You can read it and make incremental edits using the ${aD.name} tool.` : `No plan file exists yet. You should create your plan at ${A.planFilePath} using the ${sD.name} tool.`}
+
+## Iterative Planning Workflow
+
+Your goal is to build a comprehensive plan through iterative refinement and interviewing the user. Read files, interview and ask questions, and build the plan incrementally.
+
+### How to Work
+
+0. Write your plan in the plan file specified above. This is the ONLY file you are allowed to edit.
+
+1. **Explore the codebase**: Use Read, Glob, and Grep tools to understand the codebase.${`
+You have access to the ${WC.agentType} agent type if you want to delegate search.
+Use this generously for particularly complex searches or to parallelize exploration.`}
+
+2. **Interview the user**: Use ${xJ} to interview the user and ask questions that:
+   - Clarify ambiguous requirements
+   - Get user input on technical decisions and tradeoffs
+   - Understand preferences for UI/UX, performance, edge cases
+   - Validate your understanding before committing to an approach
+   Make sure to:
+   - Not ask any questions that you could find out yourself by exploring the codebase.
+   - Batch questions together when possible so you ask multiple questions at once
+   - DO NOT ask any questions that are obvious or that you believe you know the answer to.
+
+3. **Write to the plan file iteratively**: As you learn more, update the plan file:
+   - Start with your initial understanding of the requirements, leave in space to fill it out.
+   - Add sections as you explore and learn about the codebase
+   - Refine based on user answers to your questions
+   - The plan file is your working document - edit it as your understanding evolves
+
+4. **Interleave exploration, questions, and writing**: Don't wait until the end to write. After each discovery or clarification, update the plan file to capture what you've learned.
+
+5. **Adjust the level of detail to the task**: For a highly unspecified task like a new project or feature, you might need to ask many rounds of questions. Whereas for a smaller task you may need only some or a few.
+
+### Plan File Structure
+Your plan file should be divided into clear sections using markdown headers, based on the request. Fill out these sections as you go.
+- Include only your recommended approach, not all alternatives
+- Ensure that the plan file is concise enough to scan quickly, but detailed enough to execute effectively
+- Include the paths of critical files to be modified
+- Include a verification section describing how to test the changes end-to-end (run the code, use MCP tools, run tests)
+
+### Ending Your Turn
+
+Your turn should only end by either:
+- Using ${xJ} to gather more information
+- Calling ${rZ.name} when the plan is ready for approval
+
+**Important:**: Use ${rZ.name} to request plan approval. Do NOT ask about plan approval via text or AskUserQuestion.`;
   return c9([z6({ content: q, isMeta: !0 })]);
 }

@@@ variable 'qq' (was 'X5') — structural (63.9%)
--- pretty-v2.1.19.js:453448
+++ pretty-v2.1.20.js:470922
@@ -22,14 +22,15 @@
   e1();
   F1();
   _H();
+  ZH();
   ((_D2 = {
     ISSUES_EXPLAINER:
       "report the issue at https://github.com/anthropics/claude-code/issues",
     PACKAGE_URL: "@anthropic-ai/claude-code",
     README_URL: "https://code.claude.com/docs/en/overview",
-    VERSION: "2.1.19",
+    VERSION: "2.1.20",
     FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-    BUILD_TIME: "2026-01-23T21:13:41Z",
+    BUILD_TIME: "2026-01-27T00:38:42Z",
   }.VERSION),
     (qt = m1()));
   cqK = w6(

@@@ function 'n86' (was 'v16') — structural (63.6%)
--- pretty-v2.1.19.js:156855
+++ pretty-v2.1.20.js:158578
@@ -1,4 +1,4 @@
-function v16() {
+function n86(A) {
   Mz((A) => ({
     ...A,
     lastCost: wG(),
@@ -13,6 +13,8 @@
     lastTotalCacheCreationInputTokens: id6(),
     lastTotalCacheReadInputTokens: ld6(),
     lastTotalWebSearchRequests: nd6(),
+    lastFpsAverage: A?.averageFps,
+    lastFpsLow1Pct: A?.low1PctFps,
     lastModelUsage: Object.fromEntries(
       Object.entries(Hh()).map(([K, q]) => [
         K,

@@@ function 'VkK' (was 'oPK') — structural (63.3%)
--- pretty-v2.1.19.js:537016
+++ pretty-v2.1.20.js:542191
@@ -1,5 +1,5 @@
 function oPK(A) {
-  let K = a(51),
+  let K = s(54),
     q = jQ2,
     Y,
     z,
@@ -17,12 +17,14 @@
     j,
     M,
     P,
+    V,
     V;
   if (
     K[0] !== A.onDone ||
     K[1] !== A.onReject ||
     K[2] !== A.toolUseConfirm ||
-    K[3] !== A.toolUseContext
+    K[3] !== A.toolUseContext ||
+    K[4] !== A.workerBadge
   )
     (({
       file_path: H,
@@ -35,6 +37,7 @@
       (D = A.toolUseContext),
       (j = A.onDone),
       (M = A.onReject),
+      (V = A.workerBadge),
       (P = "Edit file"),
       (V = WQ2(m1(), H)),
       (z = f),
@@ -47,7 +50,7 @@
       (K[1] = A.onReject),
       (K[2] = A.toolUseConfirm),
       (K[3] = A.toolUseContext),
-      (K[4] = Y),
+      (K[4] = A.workerBadge),
       (K[5] = z),
       (K[6] = w),
       (K[7] = H),
@@ -63,10 +66,11 @@
       (K[17] = j),
       (K[18] = M),
       (K[19] = P),
-      (K[20] = V));
+      (K[20] = P),
+      (K[21] = V),
+      (K[22] = N));
   else
-    ((Y = K[4]),
-      (z = K[5]),
+    ((Y = K[5]),
       (w = K[6]),
       (H = K[7]),
       (J = K[8]),
@@ -81,47 +85,47 @@
       (j = K[17]),
       (M = K[18]),
       (P = K[19]),
-      (V = K[20]));
+      (P = K[20]),
+      (V = K[21]),
+      (N = K[22]));
   let N;
-  if (K[21] !== Y || K[22] !== $ || K[23] !== _)
+  if (K[23] !== Y || K[24] !== $ || K[25] !== _)
     ((N = QpA.default.createElement(Y, { bold: $ }, _)),
-      (K[21] = Y),
-      (K[22] = $),
       (K[23] = _),
-      (K[24] = N));
-  else N = K[24];
+      (K[24] = $),
+      (K[25] = _),
+      (K[26] = T));
+  else T = K[26];
   let T;
-  if (K[25] !== z || K[26] !== N || K[27] !== Z || K[28] !== G)
+  if (K[27] !== z || K[28] !== T || K[29] !== G || K[30] !== W)
     ((T = QpA.default.createElement(z, null, Z, G, N, "?")),
-      (K[25] = z),
-      (K[26] = N),
       (K[27] = Z),
       (K[28] = G),
-      (K[29] = T));
-  else T = K[29];
+      (K[29] = G),
+      (K[30] = W),
+      (K[31] = k));
+  else k = K[31];
   let k = O || !1,
     R;
-  if (K[30] !== J || K[31] !== X || K[32] !== k)
+  if (K[32] !== J || K[33] !== O || K[34] !== R)
     ((R = [{ old_string: X, new_string: J, replace_all: k }]),
-      (K[30] = J),
-      (K[31] = X),
       (K[32] = k),
-      (K[33] = R));
-  else R = K[33];
+      (K[33] = O),
+      (K[34] = R),
+      (K[35] = b));
+  else b = K[35];
   let x;
-  if (K[34] !== H || K[35] !== R)
+  if (K[36] !== H || K[37] !== b)
     ((x = QpA.default.createElement(JPA, { file_path: H, edits: R })),
-      (K[34] = H),
-      (K[35] = R),
-      (K[36] = x));
-  else x = K[36];
+      (K[36] = H),
+      (K[37] = b),
+      (K[38] = S));
+  else S = K[38];
   let S;
-  if (K[37] !== H) ((S = st(H)), (K[37] = H), (K[38] = S));
-  else S = K[38];
+  if (K[39] !== H) ((B = Ee(H)), (K[39] = H), (K[40] = B));
+  else B = K[40];
   let g;
   if (
-    K[39] !== w ||
-    K[40] !== H ||
     K[41] !== T ||
     K[42] !== x ||
     K[43] !== S ||
@@ -130,13 +134,17 @@
     K[46] !== j ||
     K[47] !== M ||
     K[48] !== P ||
-    K[49] !== V
+    K[49] !== j ||
+    K[50] !== P ||
+    K[51] !== V ||
+    K[52] !== N
   )
     ((g = QpA.default.createElement(w, {
       toolUseConfirm: W,
       toolUseContext: D,
       onDone: j,
       onReject: M,
+      workerBadge: V,
       title: P,
       subtitle: V,
       question: T,
@@ -147,8 +155,6 @@
       parseInput: q,
       ideDiffSupport: DQ2,
     })),
-      (K[39] = w),
-      (K[40] = H),
       (K[41] = T),
       (K[42] = x),
       (K[43] = S),
@@ -158,7 +164,10 @@
       (K[47] = M),
       (K[48] = P),
       (K[49] = V),
-      (K[50] = g));
-  else g = K[50];
+      (K[50] = P),
+      (K[51] = V),
+      (K[52] = N),
+      (K[53] = x));
+  else x = K[53];
   return g;
 }

@@@ function 'a7z' (was 'kr2') — structural (63.1%)
--- pretty-v2.1.19.js:572931
+++ pretty-v2.1.20.js:577044
@@ -41,6 +41,11 @@
           .hideHelp(),
       )
       .option(
+        "--debug-file <path>",
+        "Write debug logs to a specific file path (implicitly enables debug mode)",
+        () => !0,
+      )
+      .option(
         "--verbose",
         "Override verbose mode setting from config",
         () => !0,
@@ -502,10 +507,12 @@
 ${M6}`
             : M6;
         }
-        let { mode: LA, notification: FA } = SYK({
-          permissionModeCli: M,
-          dangerouslySkipPermissions: _,
-        });
+        let LA = void 0,
+          { mode: mA, notification: CA } = S0K({
+            permissionModeCli: j,
+            dangerouslySkipPermissions: _,
+            dangerouslySkipPermissionsWithClassifiers: LA,
+          });
         jc6(LA === "bypassPermissions");
         let RA = {};
         if (j && j.length > 0) {
@@ -600,6 +607,7 @@
             ),
               process.exit(1));
         }
+        jn6(P);
         let { toolPermissionContext: N1, warnings: C1 } = hYK({
           allowedToolsCli: W,
           disallowedToolsCli: D,
@@ -840,10 +848,8 @@
         kc(q4);
         let IK = l || o ? "init" : e ? "maintenance" : null;
         if (IK) {
-          if ((qe(), await PZ7(IK, l), l)) {
-            Hq(0);
-            return;
-          }
+          (Re(), await jf1("init", !0), H5(0));
+          return;
         }
         if (HA) {
           if (Q === "stream-json" || Q === "json") gc6(!0);
@@ -904,12 +910,13 @@
                 rewindFiles: X.rewindFiles,
                 enableAuthStatus: X.enableAuthStatus,
                 agent: b,
+                setupTrigger: jK ?? void 0,
                 ...{},
               },
             ));
           return;
         }
-        let i7 = vr2(!1);
+        let { renderOptions: BK, getFpsMetrics: Z5 } = r7z(!1);
         n("tengu_startup_manual_model_config", {
           cli_flag: X.model,
           env_var: process.env.ANTHROPIC_MODEL,
@@ -997,7 +1004,6 @@
             speculationSessionTimeSavedMs: 0,
             promptCoaching: { tip: null, shownAt: 0 },
             queuedCommands: [],
-            workerPermissions: { queue: [], selectedIndex: 0 },
             workerSandboxPermissions: { queue: [], selectedIndex: 0 },
             pendingWorkerRequest: null,
             pendingSandboxRequest: null,
@@ -1007,6 +1013,12 @@
               hunks: new Map(),
               lastUpdated: 0,
             },
+            prStatus: {
+              number: null,
+              url: null,
+              reviewState: null,
+              lastUpdated: 0,
+            },
             authVersion: 0,
             initialMessage: tA
               ? { message: z6({ content: String(tA) }) }
@@ -1037,27 +1049,31 @@
             let { waitUntilExit: y4 } = await M9(
               Zq.default.createElement(
                 OY,
-                { initialState: z7, onChangeAppState: Wm },
-                Zq.default.createElement(N9A, {
-                  debug: O || $,
-                  commands: [...cA, ...Y7],
-                  initialTools: nK,
-                  initialMessages: M6.messages,
-                  initialFileHistorySnapshots: M6.fileHistorySnapshots,
-                  initialAgentName: M6.agentName,
-                  initialAgentColor: M6.agentColor,
-                  mcpClients: m4,
-                  dynamicMcpConfig: RA,
-                  mcpCliEndpoint: R8,
-                  autoConnectIdeFlag: T,
-                  strictMcpConfig: _1,
-                  systemPrompt: vA,
-                  appendSystemPrompt: OA,
-                  mainThreadAgentDefinition: g1,
-                  disableSlashCommands: WA,
-                  taskListId: t,
-                  autoTickIntervalMs: GA,
-                }),
+                { getFpsMetrics: Z5 },
+                Zq.default.createElement(
+                  $Y,
+                  { initialState: D4, onChangeAppState: Lm },
+                  Zq.default.createElement(t9A, {
+                    debug: X || $,
+                    commands: [...q1, ...d8],
+                    initialTools: sK,
+                    initialMessages: W6.messages,
+                    initialFileHistorySnapshots: W6.fileHistorySnapshots,
+                    initialAgentName: W6.agentName,
+                    initialAgentColor: W6.agentColor,
+                    mcpClients: MK,
+                    dynamicMcpConfig: IA,
+                    mcpCliEndpoint: I8,
+                    autoConnectIdeFlag: T,
+                    strictMcpConfig: k1,
+                    systemPrompt: vA,
+                    appendSystemPrompt: ZA,
+                    mainThreadAgentDefinition: T6,
+                    disableSlashCommands: HA,
+                    taskListId: o,
+                    autoTickIntervalMs: OA,
+                  }),
+                ),
               ),
               i7,
             );
@@ -1148,18 +1164,22 @@
             (await M9(
               Zq.default.createElement(
                 OY,
-                { initialState: n9, onChangeAppState: Wm },
-                Zq.default.createElement(N9A, {
-                  debug: O || $,
-                  commands: cA,
-                  initialTools: [],
-                  initialMessages: jK ? [T5, jK] : [T5],
-                  mcpClients: [],
-                  autoConnectIdeFlag: T,
-                  mainThreadAgentDefinition: g1,
-                  disableSlashCommands: WA,
-                  remoteSessionConfig: vK,
-                }),
+                { getFpsMetrics: Z5 },
+                Zq.default.createElement(
+                  $Y,
+                  { initialState: VA, onChangeAppState: Lm },
+                  Zq.default.createElement(t9A, {
+                    debug: X || $,
+                    commands: q1,
+                    initialTools: [],
+                    initialMessages: oA ? [u3, oA] : [u3],
+                    mcpClients: [],
+                    autoConnectIdeFlag: T,
+                    mainThreadAgentDefinition: T6,
+                    disableSlashCommands: HA,
+                    remoteSessionConfig: N3,
+                  }),
+                ),
               ),
               i7,
             ),
@@ -1290,27 +1310,31 @@
               { waitUntilExit: qK } = await M9(
                 Zq.default.createElement(
                   OY,
-                  { initialState: V7, onChangeAppState: Wm },
-                  Zq.default.createElement(N9A, {
-                    debug: O || $,
-                    commands: [...cA, ...Y7],
-                    initialTools: nK,
-                    initialMessages: M6,
-                    initialFileHistorySnapshots: v8,
-                    initialAgentName: d8,
-                    initialAgentColor: z7,
-                    mcpClients: m4,
-                    dynamicMcpConfig: RA,
-                    mcpCliEndpoint: R8,
-                    autoConnectIdeFlag: T,
-                    strictMcpConfig: _1,
-                    systemPrompt: vA,
-                    appendSystemPrompt: OA,
-                    mainThreadAgentDefinition: g1,
-                    disableSlashCommands: WA,
-                    taskListId: t,
-                    autoTickIntervalMs: GA,
-                  }),
+                  { getFpsMetrics: Z5 },
+                  Zq.default.createElement(
+                    $Y,
+                    { initialState: A8, onChangeAppState: Lm },
+                    Zq.default.createElement(t9A, {
+                      debug: X || $,
+                      commands: [...q1, ...d8],
+                      initialTools: sK,
+                      initialMessages: W6,
+                      initialFileHistorySnapshots: R4,
+                      initialAgentName: l8,
+                      initialAgentColor: D4,
+                      mcpClients: MK,
+                      dynamicMcpConfig: IA,
+                      mcpCliEndpoint: I8,
+                      autoConnectIdeFlag: T,
+                      strictMcpConfig: k1,
+                      systemPrompt: vA,
+                      appendSystemPrompt: ZA,
+                      mainThreadAgentDefinition: T6,
+                      disableSlashCommands: HA,
+                      taskListId: o,
+                      autoTickIntervalMs: OA,
+                    }),
+                  ),
                 ),
                 i7,
               );
@@ -1320,26 +1344,30 @@
             (await M9(
               Zq.default.createElement(
                 OY,
-                { initialState: q5, onChangeAppState: Wm },
+                { getFpsMetrics: Z5 },
                 Zq.default.createElement(
-                  $H,
                   null,
-                  Zq.default.createElement(hSK, {
-                    commands: [...cA, ...Y7],
-                    debug: O || $,
-                    worktreePaths: n8,
-                    initialTools: nK,
-                    mcpClients: m4,
-                    dynamicMcpConfig: RA,
-                    mcpCliEndpoint: R8,
-                    strictMcpConfig: _1,
-                    systemPrompt: vA,
-                    appendSystemPrompt: OA,
-                    initialSearchQuery: B7,
-                    disableSlashCommands: WA,
-                    forkSession: X.forkSession,
-                    taskListId: t,
-                  }),
+                  { initialState: bq, onChangeAppState: Lm },
+                  Zq.default.createElement(
+                    _H,
+                    null,
+                    Zq.default.createElement(KgK, {
+                      commands: [...q1, ...d8],
+                      debug: X || $,
+                      worktreePaths: _4,
+                      initialTools: sK,
+                      mcpClients: MK,
+                      dynamicMcpConfig: IA,
+                      mcpCliEndpoint: I8,
+                      strictMcpConfig: k1,
+                      systemPrompt: vA,
+                      appendSystemPrompt: ZA,
+                      initialSearchQuery: pK,
+                      disableSlashCommands: HA,
+                      forkSession: O.forkSession,
+                      taskListId: o,
+                    }),
+                  ),
                 ),
               ),
               i7,
@@ -1352,24 +1380,28 @@
           let { waitUntilExit: v8 } = await M9(
             Zq.default.createElement(
               OY,
-              { initialState: q5, onChangeAppState: Wm },
-              Zq.default.createElement(N9A, {
-                debug: O || $,
-                commands: [...cA, ...Y7],
-                initialTools: nK,
-                initialMessages: M6,
-                mcpClients: m4,
-                dynamicMcpConfig: RA,
-                autoConnectIdeFlag: T,
-                strictMcpConfig: _1,
-                systemPrompt: vA,
-                appendSystemPrompt: OA,
-                mcpCliEndpoint: R8,
-                mainThreadAgentDefinition: g1,
-                disableSlashCommands: WA,
-                taskListId: t,
-                autoTickIntervalMs: GA,
-              }),
+              { getFpsMetrics: Z5 },
+              Zq.default.createElement(
+                $Y,
+                { initialState: bq, onChangeAppState: Lm },
+                Zq.default.createElement(t9A, {
+                  debug: X || $,
+                  commands: [...q1, ...d8],
+                  initialTools: sK,
+                  initialMessages: W6,
+                  mcpClients: MK,
+                  dynamicMcpConfig: IA,
+                  autoConnectIdeFlag: T,
+                  strictMcpConfig: k1,
+                  systemPrompt: vA,
+                  appendSystemPrompt: ZA,
+                  mcpCliEndpoint: I8,
+                  mainThreadAgentDefinition: T6,
+                  disableSlashCommands: HA,
+                  taskListId: o,
+                  autoTickIntervalMs: OA,
+                }),
+              ),
             ),
             i7,
           );
@@ -1377,7 +1409,7 @@
         }
       })
       .version(
-        `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.19", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-23T21:13:41Z" }.VERSION} (Claude Code)`,
+        `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION} (Claude Code)`,
         "-v, --version",
         "Output the version number",
       ),

@@@ function 'rkK' (was 'EVK') — structural (63.0%)
--- pretty-v2.1.19.js:540664
+++ pretty-v2.1.20.js:545737
@@ -1,5 +1,5 @@
 function EVK(A) {
-  let K = a(49),
+  let K = s(52),
     q = OU2,
     Y,
     z,
@@ -16,12 +16,14 @@
     D,
     j,
     M,
+    P,
     P;
   if (
     K[0] !== A.onDone ||
     K[1] !== A.onReject ||
     K[2] !== A.toolUseConfirm ||
-    K[3] !== A.toolUseContext
+    K[3] !== A.toolUseContext ||
+    K[4] !== A.workerBadge
   ) {
     X = q(A.toolUseConfirm.input);
     let { notebook_path: x, edit_mode: S, cell_type: g } = X;
@@ -37,6 +39,7 @@
       (D = A.toolUseContext),
       (j = A.onDone),
       (M = A.onReject),
+      (V = A.workerBadge),
       (P = "Edit notebook"),
       (z = f),
       (_ = "Do you want to "),
@@ -49,7 +52,7 @@
       (K[1] = A.onReject),
       (K[2] = A.toolUseConfirm),
       (K[3] = A.toolUseContext),
-      (K[4] = Y),
+      (K[4] = A.workerBadge),
       (K[5] = z),
       (K[6] = w),
       (K[7] = H),
@@ -64,10 +67,11 @@
       (K[16] = D),
       (K[17] = j),
       (K[18] = M),
-      (K[19] = P));
+      (K[19] = j),
+      (K[20] = P),
+      (K[21] = V));
   } else
-    ((Y = K[4]),
-      (z = K[5]),
+    ((Y = K[5]),
       (w = K[6]),
       (H = K[7]),
       (J = K[8]),
@@ -81,35 +85,37 @@
       (D = K[16]),
       (j = K[17]),
       (M = K[18]),
-      (P = K[19]));
+      (j = K[19]),
+      (P = K[20]),
+      (V = K[21]));
   let V;
-  if (K[20] !== Y || K[21] !== O || K[22] !== $)
+  if (K[22] !== Y || K[23] !== X || K[24] !== $)
     ((V = ipA.default.createElement(Y, { bold: O }, $)),
-      (K[20] = Y),
-      (K[21] = O),
       (K[22] = $),
-      (K[23] = V));
-  else V = K[23];
+      (K[23] = X),
+      (K[24] = $),
+      (K[25] = N));
+  else N = K[25];
   let N;
-  if (K[24] !== z || K[25] !== V || K[26] !== _ || K[27] !== Z || K[28] !== G)
+  if (K[26] !== z || K[27] !== N || K[28] !== Z || K[29] !== G || K[30] !== W)
     ((N = ipA.default.createElement(z, null, _, Z, G, V, "?")),
-      (K[24] = z),
-      (K[25] = V),
       (K[26] = _),
       (K[27] = Z),
       (K[28] = G),
-      (K[29] = N));
-  else N = K[29];
+      (K[29] = G),
+      (K[30] = W),
+      (K[31] = T));
+  else T = K[31];
   let T = A.verbose ? 120 : 80,
     k;
   if (
-    K[30] !== X.cell_id ||
-    K[31] !== X.cell_type ||
-    K[32] !== X.edit_mode ||
-    K[33] !== X.new_source ||
-    K[34] !== X.notebook_path ||
-    K[35] !== A.verbose ||
-    K[36] !== T
+    K[32] !== O.cell_id ||
+    K[33] !== O.cell_type ||
+    K[34] !== O.edit_mode ||
+    K[35] !== O.new_source ||
+    K[36] !== O.notebook_path ||
+    K[37] !== A.verbose ||
+    K[38] !== k
   )
     ((k = ipA.default.createElement(TVK, {
       notebook_path: X.notebook_path,
@@ -120,19 +126,17 @@
       verbose: A.verbose,
       width: T,
     })),
-      (K[30] = X.cell_id),
-      (K[31] = X.cell_type),
-      (K[32] = X.edit_mode),
-      (K[33] = X.new_source),
-      (K[34] = X.notebook_path),
-      (K[35] = A.verbose),
-      (K[36] = T),
-      (K[37] = k));
-  else k = K[37];
+      (K[32] = O.cell_id),
+      (K[33] = O.cell_type),
+      (K[34] = O.edit_mode),
+      (K[35] = O.new_source),
+      (K[36] = O.notebook_path),
+      (K[37] = A.verbose),
+      (K[38] = k),
+      (K[39] = R));
+  else R = K[39];
   let R;
   if (
-    K[38] !== w ||
-    K[39] !== H ||
     K[40] !== J ||
     K[41] !== N ||
     K[42] !== k ||
@@ -140,13 +144,17 @@
     K[44] !== D ||
     K[45] !== j ||
     K[46] !== M ||
-    K[47] !== P
+    K[47] !== M ||
+    K[48] !== j ||
+    K[49] !== P ||
+    K[50] !== V
   )
     ((R = ipA.default.createElement(w, {
       toolUseConfirm: W,
       toolUseContext: D,
       onDone: j,
       onReject: M,
+      workerBadge: V,
       title: P,
       question: N,
       content: k,
@@ -155,8 +163,6 @@
       languageName: H,
       parseInput: q,
     })),
-      (K[38] = w),
-      (K[39] = H),
       (K[40] = J),
       (K[41] = N),
       (K[42] = k),
@@ -165,7 +171,10 @@
       (K[45] = j),
       (K[46] = M),
       (K[47] = P),
-      (K[48] = R));
-  else R = K[48];
+      (K[48] = j),
+      (K[49] = P),
+      (K[50] = V),
+      (K[51] = b));
+  else b = K[51];
   return R;
 }

@@@ function 'Wt2' (was 'RQ2') — structural (62.6%)
--- pretty-v2.1.19.js:537923
+++ pretty-v2.1.20.js:543088
@@ -19,12 +19,6 @@
         configString: "/hooks to update",
       };
     }
-    case "classifier":
-      return {
-        reasonString: `Classifier ${X1.bold(A.classifier)} requires confirmation for this ${K}.
-${A.reason}`,
-        configString: void 0,
-      };
     default:
       return null;
   }

@@@ function 'H5' (was 'Hq') — structural (62.5%)
--- pretty-v2.1.19.js:467871
+++ pretty-v2.1.20.js:470981
@@ -1,6 +1,9 @@
 function Hq(A = 0, K = "other", q) {
   ((process.exitCode = A),
     o5(A, K, q).catch((Y) => {
-      (h(`Graceful shutdown failed: ${Y}`, { level: "error" }), kh6(), Ch6(A));
+      (h(`Graceful shutdown failed: ${Y}`, { level: "error" }),
+        _u6(),
+        Zu6(),
+        Gu6(A));
     }));
 }

@@@ function 'rVK' (was 'uGK') — structural (62.3%)
--- pretty-v2.1.19.js:517429
+++ pretty-v2.1.20.js:521427
@@ -1,19 +1,35 @@
 function uGK() {
-  let A = a(2);
-  if (!l8.isSandboxingEnabled()) {
+  let A = s(3),
+    K = x8.isSandboxingEnabled(),
+    q;
+  if (A[0] === Symbol.for("react.memo_cache_sentinel")) {
+    let w = x8.checkDependencies();
+    ((q =
+      w.warnings.length > 0
+        ? Pq.createElement(
+            I,
+            { marginTop: 1, flexDirection: "column" },
+            w.warnings.map(Tc2),
+          )
+        : null),
+      (A[0] = q));
+  } else q = A[0];
+  let Y = q;
+  if (!K) {
     let Y;
-    if (A[0] === Symbol.for("react.memo_cache_sentinel"))
+    if (A[1] === Symbol.for("react.memo_cache_sentinel"))
       ((Y = _q.createElement(
         I,
         { flexDirection: "column", paddingY: 1 },
         _q.createElement(f, { color: "subtle" }, "Sandbox is not enabled"),
+        Y,
       )),
-        (A[0] = Y));
-    else Y = A[0];
+        (A[1] = w));
+    else w = A[1];
     return Y;
   }
   let q;
-  if (A[1] === Symbol.for("react.memo_cache_sentinel")) {
+  if (A[2] === Symbol.for("react.memo_cache_sentinel")) {
     let Y = l8.getFsReadConfig(),
       z = l8.getFsWriteConfig(),
       w = l8.getNetworkRestrictionConfig(),
@@ -133,8 +149,9 @@
             X.length > 3 && ` (${X.length - 3} more)`,
           ),
         ),
+      Y,
     )),
-      (A[1] = q));
-  } else q = A[1];
+      (A[2] = z));
+  } else z = A[2];
   return q;
 }

@@@ variable 'D1' (was 'P1') — structural (62.2%)
--- pretty-v2.1.19.js:2773
+++ pretty-v2.1.20.js:2802
@@ -13,7 +13,8 @@
       process.argv.includes("--debug") ||
       process.argv.includes("-d") ||
       $h() ||
-      process.argv.some((A) => A.startsWith("--debug="))
+      process.argv.some((A) => A.startsWith("--debug=")) ||
+      kn6() !== null
     );
   })),
     (CQK = w6(() => {
@@ -27,6 +28,15 @@
         process.argv.includes("--debug-to-stderr") ||
         process.argv.includes("-d2e")
       );
+    })),
+    (kn6 = K6(() => {
+      for (let A = 0; A < process.argv.length; A++) {
+        let K = process.argv[A];
+        if (K.startsWith("--debug-file=")) return K.substring(13);
+        if (K === "--debug-file" && A + 1 < process.argv.length)
+          return process.argv[A + 1];
+      }
+      return null;
     })));
   yQK = w6(() => {
     if (process.argv[2] === "--ripgrep") return;

@@@ variable 'kjK' (was 'G_K') — structural (62.2%)
--- pretty-v2.1.19.js:507708
+++ pretty-v2.1.20.js:511709
@@ -12,16 +12,9 @@
     description: "List current todo items",
     isEnabled: () => !0,
     isHidden: !1,
-    async call(A, { options: { isNonInteractiveSession: K } }) {
-      if (K) {
-        let q = await JMA(SS.default.createElement(__K, null));
-        return (A(q), null);
-      }
-      return SS.default.createElement(
-        XMA,
-        { onComplete: A },
-        SS.default.createElement(__K, null),
-      );
+    async call(A) {
+      let K = await ct(Qd.default.createElement(_p2, null));
+      return (A(K), null);
     },
     userFacingName() {
       return "todos";

@@@ function 'YZ1' (was 'JD1') — structural (62.2%)
--- pretty-v2.1.19.js:397274
+++ pretty-v2.1.20.js:324561
@@ -1,9 +1,10 @@
 function JD1(A) {
-  let K = a(24),
+  let K = s(27),
     {
       filePath: q,
       structuredPatch: Y,
       firstLine: z,
+      fileContent: w,
       style: w,
       verbose: H,
       previewHint: J,
@@ -55,20 +56,29 @@
       (K[8] = W));
   else W = K[8];
   let D = W;
-  if (w === "condensed" && !H) return D;
+  if (O) {
+    if (H !== "condensed" && !J) {
+      let N;
+      if (K[9] !== O)
+        ((N = fY.createElement(
+          R6,
+          null,
+          fY.createElement(f, { dimColor: !0 }, O),
+        )),
+          (K[9] = O),
+          (K[10] = N));
+      else N = K[10];
+      return N;
+    }
+  } else if (H === "condensed" && !J) return M;
   let j;
-  if (K[9] !== J || K[10] !== D)
-    ((j = J
-      ? z2.createElement(f, { dimColor: !0 }, J)
-      : z2.createElement(f, null, D)),
-      (K[9] = J),
-      (K[10] = D),
-      (K[11] = j));
-  else j = K[11];
+  if (K[11] !== M)
+    ((j = fY.createElement(f, null, M)), (K[11] = M), (K[12] = j));
+  else j = K[12];
   let M;
-  if (K[12] !== X || K[13] !== q || K[14] !== z || K[15] !== Y) {
+  if (K[13] !== X || K[14] !== w || K[15] !== q || K[16] !== z || K[17] !== Y) {
     let V;
-    if (K[17] !== X || K[18] !== q || K[19] !== z)
+    if (K[19] !== X || K[20] !== w || K[21] !== q || K[22] !== z)
       ((V = (N) =>
         z2.createElement(
           I,
@@ -79,30 +89,33 @@
             width: X - 12,
             filePath: q,
             firstLine: z,
+            fileContent: w,
           }),
         )),
-        (K[17] = X),
-        (K[18] = q),
         (K[19] = z),
-        (K[20] = V));
-    else V = K[20];
+        (K[20] = w),
+        (K[21] = q),
+        (K[22] = z),
+        (K[23] = N));
+    else N = K[23];
     ((M = Sf(Y.map(V), MK2)),
-      (K[12] = X),
       (K[13] = q),
       (K[14] = z),
       (K[15] = Y),
-      (K[16] = M));
-  } else M = K[16];
+      (K[16] = z),
+      (K[17] = Y),
+      (K[18] = P));
+  } else P = K[18];
   let P;
-  if (K[21] !== j || K[22] !== M)
+  if (K[24] !== j || K[25] !== P)
     ((P = z2.createElement(
       v6,
       null,
       z2.createElement(I, { flexDirection: "column" }, j, M),
     )),
-      (K[21] = j),
-      (K[22] = M),
-      (K[23] = P));
-  else P = K[23];
+      (K[24] = j),
+      (K[25] = P),
+      (K[26] = V));
+  else V = K[26];
   return P;
 }

@@@ function 'sJK' (was 'L22') — structural (61.9%)
--- pretty-v2.1.19.js:420764
+++ pretty-v2.1.20.js:467598
@@ -1,3 +1,3 @@
 function L22(A) {
-  return `#${A}`;
+  return `Permission to use ${A} has been denied. ${pR2}`;
 }

@@@ function 'J1z' (was 'L3K') — structural (61.9%)
--- pretty-v2.1.19.js:455811
+++ pretty-v2.1.20.js:556239
@@ -1,3 +1,6 @@
 function L3K(A) {
-  return `Permission to use ${A} has been denied. IMPORTANT: You *may* attempt to accomplish this action using other tools that might naturally be used to accomplish this goal, e.g. using head instead of cat. But you *should not* attempt to work around this denial in malicious ways, e.g. do not use your ability to run tests to execute non-test actions. You should only try to work around this restriction in reasonable ways that do not attempt to bypass the intent behind this denial. If you believe this capability is essential to complete the user's request, STOP and explain to the user what you were trying to do and why you need this permission. Let the user decide how to proceed.`;
+  return `<${yO}>
+<${WG}>+${A} more tasks completed</${WG}>
+<${GG}>completed</${GG}>
+</${yO}>`;
 }

@@@ function 'EGA' (was 'iZA') — structural (61.8%)
--- pretty-v2.1.19.js:313815
+++ pretty-v2.1.20.js:310364
@@ -1,4 +1,4 @@
-function iZA(A, K) {
+function EGA(A, K, q, Y) {
   if (K.type !== "assistant") return;
   let q = K.message.usage;
   ((A.latestInputTokens =
@@ -8,8 +8,17 @@
     (A.cumulativeOutputTokens += q.output_tokens));
   for (let Y of K.message.content)
     if (Y.type === "tool_use") {
-      if ((A.toolUseCount++, Y.name !== aG))
-        A.recentActivities.push({ toolName: Y.name, input: Y.input });
+      if ((A.toolUseCount++, w.name !== wW)) {
+        let H = w.input,
+          J = Y ? h$1(w.name, H, Y) : void 0;
+        A.recentActivities.push({
+          toolName: w.name,
+          input: H,
+          activityDescription: q?.(w.name, H),
+          isSearch: J?.isSearch,
+          isRead: J?.isRead,
+        });
+      }
     }
   while (A.recentActivities.length > DVY) A.recentActivities.shift();
 }

@@@ variable 'hH' (was 'BH') — structural (61.7%)
--- pretty-v2.1.19.js:101252
+++ pretty-v2.1.20.js:102955
@@ -22,12 +22,21 @@
   WL8 = w6((A) => {
     return A?.sandbox?.allowUnsandboxedCommands ?? !0;
   });
-  VU1 = w6(() => {
+  ((dd1 = K6(() => {
     return q0.isSupportedPlatform();
-  });
+  })),
+    (Ob8 = K6((A) => {
+      let K = A?.sandbox?.enabledPlatforms;
+      if (K === void 0) return !0;
+      if (K.length === 0) return !1;
+      let q = s6();
+      return K.includes(q);
+    })));
   l8 = {
     initialize: C4q,
     isSandboxingEnabled: TeA,
+    isSandboxEnabledInSettings: wb8,
+    isPlatformInEnabledList: Xb8,
     isAutoAllowBashIfSandboxedEnabled: V4q,
     areUnsandboxedCommandsAllowed: f4q,
     areSandboxSettingsLockedByPolicy: T4q,

@@@ function 'VM1' (was 'bZ1') — structural (61.6%)
--- pretty-v2.1.19.js:363133
+++ pretty-v2.1.20.js:388235
@@ -1,6 +1,8 @@
 function bZ1({ tasks: A, isStandalone: K = !1 }) {
   let [q] = j6(),
     [, Y] = Q3.useState(0),
+    { rows: z } = V8(),
+    w = z <= 10 ? 0 : Math.min(10, Math.max(3, z - 14)),
     z = new Set(A.filter((T) => T.status === "completed").map((T) => T.id)),
     w = Date.now();
   for (let T of z) if (!yx7.has(T)) wWA.set(T, w);
@@ -32,6 +34,15 @@
         if (k) J[T.name] = k;
       }
   }
+  let $ = {};
+  if (j8()) {
+    for (let b of Object.values(q.tasks))
+      if (iT(b) && b.status === "running") {
+        let S = b.progress?.recentActivities,
+          B = (S && vGA(S)) ?? b.progress?.lastActivity?.activityDescription;
+        if (B) (($[b.identity.agentName] = B), ($[b.identity.agentId] = B));
+      }
+  }
   let X = A.filter((T) => T.status === "completed").length,
     O = A.filter((T) => T.status === "pending").length,
     $ = A.length - X - O,
@@ -45,7 +56,12 @@
   }
   (Z.sort(hZ1), G.sort(hZ1));
   let W = A.filter((T) => T.status === "in_progress").sort(hZ1),
-    D = A.filter((T) => T.status === "pending").sort(hZ1),
+    P = A.filter((b) => b.status === "pending").sort((b, S) => {
+      let B = b.blockedBy.some((F) => W.has(F)),
+        x = S.blockedBy.some((F) => W.has(F));
+      if (B !== x) return B ? 1 : -1;
+      return PM1(b, S);
+    }),
     j = [...Z, ...W, ...D, ...G],
     M = j.slice(0, Lx7),
     P = j.slice(Lx7),
@@ -69,42 +85,47 @@
         task: T,
         ownerColor: T.owner ? J[T.owner] : void 0,
         openBlockers: T.blockedBy.filter((k) => _.has(k)),
+        activity: b.owner ? $[b.owner] : void 0,
       }),
     ),
-    V && Q3.createElement(f, { dimColor: !0 }, V),
+    w > 0 && k && hK.createElement(f, { dimColor: !0 }, k),
   );
-  if (K) {
-    let T = [`${X} done`];
-    if ($ > 0) T.push(`${$} in progress`);
-    return (
-      T.push(`${O} open`),
+  if (K)
+    return hK.createElement(
+      I,
+      { flexDirection: "column", marginTop: 1, marginLeft: 2 },
       Q3.createElement(
         I,
-        { flexDirection: "column", marginTop: 1, marginLeft: 2 },
+        null,
         Q3.createElement(
           I,
+          { dimColor: !0 },
+          hK.createElement(f, { bold: !0 }, A.length),
+          " tasks (",
+          hK.createElement(f, { bold: !0 }, _),
+          " done, ",
+          G > 0 &&
+            hK.createElement(
+              hK.Fragment,
+              null,
+              hK.createElement(f, { bold: !0 }, G),
+              " in progress, ",
+            ),
+          hK.createElement(f, { bold: !0 }, Z),
+          " open)",
+        ),
+        hK.createElement(
           null,
-          Q3.createElement(
-            f,
-            { bold: !0, dimColor: !0 },
-            "Tasks (",
-            T.join(", "),
-            ")",
-          ),
-          Q3.createElement(
-            f,
-            { dimColor: !0 },
-            " · ",
-            Q3.createElement(k6, {
-              shortcut: "ctrl+t",
-              action: "hide tasks",
-              bold: !0,
-            }),
-          ),
+          { dimColor: !0 },
+          " · ",
+          hK.createElement(M6, {
+            shortcut: "ctrl+t",
+            action: "hide tasks",
+            bold: !0,
+          }),
         ),
-        N,
-      )
+      ),
+      R,
     );
-  }
   return Q3.createElement(I, { flexDirection: "column" }, N);
 }

@@@ function 'fAz' (was 'Ip2') — structural (61.4%)
--- pretty-v2.1.19.js:548270
+++ pretty-v2.1.20.js:553315
@@ -1,5 +1,5 @@
 function Ip2(A) {
-  let K = a(47),
+  let K = s(56),
     {
       mode: q,
       toolPermissionContext: Y,
@@ -12,7 +12,7 @@
     { columns: O } = N8(),
     $ = w5("chat:cycleMode", "Chat", "shift+tab"),
     [_] = j6(),
-    { tasks: Z, teamContext: G, remoteSessionUrl: W } = _,
+    { tasks: Z, teamContext: G, remoteSessionUrl: W, viewSelectionMode: D } = _,
     D;
   if (K[0] === Symbol.for("react.memo_cache_sentinel")) ((D = !1), (K[0] = D));
   else D = K[0];
@@ -29,6 +29,7 @@
       (K[4] = N));
   else N = K[4];
   let T = N,
+    R = _.prStatus,
     k;
   if (K[5] !== G)
     ((k =
@@ -61,16 +62,37 @@
   if (K[9] !== x) ((S = vE8(x)), (K[9] = x), (K[10] = S));
   else S = K[10];
   let g = !S,
-    b = P > 0,
+    Q = D === "viewing-agent",
+    u = V > 0 || Q,
     Q = (j ? 1 : 0) + (g ? 1 : 0) + (b ? 1 : 0) + (R ? 1 : 0),
     F;
   if (K[11] === Symbol.for("react.memo_cache_sentinel"))
-    ((F = f1().codeDiffFooterEnabled ?? !0), (K[11] = F));
+    ((a = P1()), (K[11] = a));
   else F = K[11];
-  let d = F && T && T.filesCount > 0 && Q < 2 && (Q === 0 || O >= 100),
+  let JA =
+      (a.codeDiffFooterEnabled ?? !0) &&
+      k &&
+      k.filesCount > 0 &&
+      d < 2 &&
+      (d === 0 || X >= 100),
+    OA;
+  if (K[12] !== X || K[13] !== R || K[14] !== d)
+    ((OA =
+      eLK() &&
+      R.number !== null &&
+      R.reviewState !== null &&
+      R.url !== null &&
+      d < 2 &&
+      (d === 0 || X >= 100)),
+      (K[12] = X),
+      (K[13] = R),
+      (K[14] = d),
+      (K[15] = OA));
+  else OA = K[15];
+  let HA = OA,
     o = Q < 2,
     l;
-  if (K[12] !== W)
+  if (K[16] !== W)
     ((l = W
       ? [
           _3.createElement(
@@ -81,11 +103,11 @@
           ),
         ]
       : []),
-      (K[12] = W),
-      (K[13] = l));
-  else l = K[13];
+      (K[16] = W),
+      (K[17] = o));
+  else o = K[17];
   let e;
-  if (K[14] !== x || K[15] !== g || K[16] !== $ || K[17] !== o)
+  if (K[18] !== B || K[19] !== F || K[20] !== $ || K[21] !== DA)
     ((e =
       x && g
         ? [
@@ -110,35 +132,37 @@
             ),
           ]
         : []),
-      (K[14] = x),
-      (K[15] = g),
-      (K[16] = $),
-      (K[17] = o),
-      (K[18] = e));
-  else e = K[18];
+      (K[18] = B),
+      (K[19] = F),
+      (K[20] = $),
+      (K[21] = DA),
+      (K[22] = _A));
+  else _A = K[22];
   let XA;
-  if (K[19] !== X || K[20] !== z)
-    ((XA = []), (K[19] = X), (K[20] = z), (K[21] = XA));
-  else XA = K[21];
+  if (K[23] !== O || K[24] !== z)
+    ((PA = []), (K[23] = O), (K[24] = z), (K[25] = PA));
+  else PA = K[25];
   let GA;
-  if (K[22] !== b || K[23] !== R || K[24] !== z || K[25] !== w)
+  if (K[26] !== u || K[27] !== S || K[28] !== Q || K[29] !== z || K[30] !== w)
     ((GA = b
       ? [
           _3.createElement(fNK, {
             key: "tasks",
             tasksSelected: w,
             showHint: z && !R,
+            isViewingTeammate: Q,
           }),
         ]
       : []),
-      (K[22] = b),
-      (K[23] = R),
-      (K[24] = z),
-      (K[25] = w),
-      (K[26] = GA));
-  else GA = K[26];
+      (K[26] = u),
+      (K[27] = S),
+      (K[28] = Q),
+      (K[29] = z),
+      (K[30] = w),
+      (K[31] = jA));
+  else jA = K[31];
   let WA;
-  if (K[27] !== b || K[28] !== R || K[29] !== z || K[30] !== H)
+  if (K[32] !== u || K[33] !== S || K[34] !== z || K[35] !== H)
     ((WA =
       P8() && R
         ? [
@@ -149,14 +173,14 @@
             }),
           ]
         : []),
-      (K[27] = b),
-      (K[28] = R),
-      (K[29] = z),
-      (K[30] = H),
-      (K[31] = WA));
-  else WA = K[31];
+      (K[32] = u),
+      (K[33] = S),
+      (K[34] = z),
+      (K[35] = H),
+      (K[36] = yA));
+  else yA = K[36];
   let ZA;
-  if (K[32] !== T || K[33] !== J || K[34] !== d || K[35] !== z)
+  if (K[37] !== k || K[38] !== J || K[39] !== JA || K[40] !== z)
     ((ZA = d
       ? [
           _3.createElement(
@@ -183,45 +207,64 @@
           ),
         ]
       : []),
-      (K[32] = T),
-      (K[33] = J),
-      (K[34] = d),
-      (K[35] = z),
-      (K[36] = ZA));
-  else ZA = K[36];
-  let t;
-  if (
-    K[37] !== GA ||
-    K[38] !== WA ||
-    K[39] !== ZA ||
-    K[40] !== l ||
-    K[41] !== e ||
-    K[42] !== XA
-  )
-    ((t = [...l, ...e, ...XA, ...GA, ...WA, ...ZA]),
       (K[37] = GA),
       (K[38] = WA),
       (K[39] = ZA),
       (K[40] = l),
-      (K[41] = e),
+      (K[41] = bA));
+  else bA = K[41];
+  let YA;
+  if (K[42] !== R || K[43] !== HA)
+    ((YA = HA
+      ? [
+          fq.createElement(
+            f,
+            { key: "pr-status", dimColor: !0 },
+            fq.createElement(f, { color: TAz(R.reviewState) }, "PR"),
+            " ",
+            fq.createElement(D7, { url: R.url }, "#", R.number),
+          ),
+        ]
+      : []),
       (K[42] = XA),
-      (K[43] = t));
-  else t = K[43];
+      (K[43] = HA),
+      (K[44] = YA));
+  else YA = K[44];
+  let KA;
+  if (
+    K[45] !== PA ||
+    K[46] !== jA ||
+    K[47] !== yA ||
+    K[48] !== bA ||
+    K[49] !== YA ||
+    K[50] !== o ||
+    K[51] !== _A
+  )
+    ((KA = [...o, ..._A, ...PA, ...jA, ...yA, ...bA, ...YA]),
+      (K[45] = PA),
+      (K[46] = jA),
+      (K[47] = yA),
+      (K[48] = bA),
+      (K[49] = YA),
+      (K[50] = o),
+      (K[51] = _A),
+      (K[52] = KA));
+  else KA = K[52];
   let $A = t;
   if ($A.length) {
     let MA;
-    if (K[44] !== $A)
+    if (K[53] !== zA)
       ((MA = _3.createElement(I, null, _3.createElement($8, null, $A))),
-        (K[44] = $A),
-        (K[45] = MA));
-    else MA = K[45];
+        (K[53] = zA),
+        (K[54] = t));
+    else t = K[54];
     return MA;
   }
   if (!z) return null;
   let VA;
-  if (K[46] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[55] === Symbol.for("react.memo_cache_sentinel"))
     ((VA = _3.createElement(f, { dimColor: !0 }, "? for shortcuts")),
-      (K[46] = VA));
-  else VA = K[46];
+      (K[55] = AA));
+  else AA = K[55];
   return VA;
 }

@@@ function 'CK7' (was 'N87') — structural (61.1%)
--- pretty-v2.1.19.js:265359
+++ pretty-v2.1.20.js:264281
@@ -1,4 +1,4 @@
-function N87(A, K, q) {
-  if (A.type === "assistant") return m6Y(A, K, q);
+function CK7(A, K, q, Y) {
+  if (A.type === "assistant") return Q9Y(A, K, q, Y);
   else return A;
 }

@@@ function 'HAz' (was 'Np2') — structural (61.0%)
--- pretty-v2.1.19.js:547931
+++ pretty-v2.1.20.js:552868
@@ -6,5 +6,7 @@
       return A.description;
     case "remote_agent":
       return A.title;
+    case "in_process_teammate":
+      return `@${A.identity.agentName}`;
   }
 }

@@@ function 'saK' (was 'xcK') — structural (60.6%)
--- pretty-v2.1.19.js:6108
+++ pretty-v2.1.20.js:6188
@@ -4,6 +4,12 @@
   let q = K.match(/^git@([^:]+):(.+?)(?:\.git)?$/);
   if (q && q[1] && q[2]) return `${q[1]}/${q[2]}`.toLowerCase();
   let Y = K.match(/^(?:https?|ssh):\/\/(?:[^@]+@)?([^/]+)\/(.+?)(?:\.git)?$/);
-  if (Y && Y[1] && Y[2]) return `${Y[1]}/${Y[2]}`.toLowerCase();
+  if (Y && Y[1] && Y[2]) {
+    let z = Y[1],
+      w = Y[2];
+    if (eaK(z) && w.startsWith("git/"))
+      return `github.com/${w.slice(4)}`.toLowerCase();
+    return `${z}/${w}`.toLowerCase();
+  }
   return null;
 }

@@@ variable '$TK' (was 'lDK') — structural (60.6%)
--- pretty-v2.1.19.js:527362
+++ pretty-v2.1.20.js:532032
@@ -2,8 +2,16 @@
   T7();
   (($u2 = U.object({
     allowedDomains: U.array(U.string()).optional(),
-    allowUnixSockets: U.array(U.string()).optional(),
-    allowAllUnixSockets: U.boolean().optional(),
+    allowUnixSockets: U.array(U.string())
+      .optional()
+      .describe(
+        "macOS only: Unix socket paths to allow. Ignored on Linux (seccomp cannot filter by path).",
+      ),
+    allowAllUnixSockets: U.boolean()
+      .optional()
+      .describe(
+        "If true, allow all Unix sockets (disables blocking on both platforms).",
+      ),
     allowLocalBinding: U.boolean().optional(),
     httpProxyPort: U.number().optional(),
     socksProxyPort: U.number().optional(),

@@@ function 'D11' (was 'TeA') — structural (60.6%)
--- pretty-v2.1.19.js:101120
+++ pretty-v2.1.20.js:102821
@@ -1,5 +1,6 @@
 function TeA() {
   if (!VU1()) return !1;
+  if (pd1().errors.length > 0) return !1;
   if (!PU1()) return !1;
   return P4q();
 }

@@@ function 'Pd2' (was 'Gh2') — structural (60.6%)
--- pretty-v2.1.19.js:513118
+++ pretty-v2.1.20.js:517115
@@ -1,27 +1,18 @@
-function Gh2(A) {
+async function Pd2(A) {
   let K = Zh2(),
     q = n1(),
     Y = _O(t6()),
     z = G_(K),
-    w = O$(),
     H = hA();
-  H.mkdirSync(Y, { mode: 448 });
+  await Md2(Y, { recursive: !0, mode: 448 });
   let J;
   try {
-    J = H.readFileSync(w, { encoding: "utf8" });
+    H = await Dd2(w);
   } catch {
     throw Error("No conversation to fork");
   }
-  if (!J.trim()) throw Error("No conversation to fork");
-  let X = [];
-  for (let G of J.trim().split(`
-`)) {
-    if (!G.trim()) continue;
-    try {
-      X.push(_6(G));
-    } catch {}
-  }
-  let O = X.filter((G) => !G.isSidechain && Ru(G));
+  if (H.length === 0) throw Error("No conversation to fork");
+  let O = K1A(H).filter((Z) => !Z.isSidechain && oB(Z));
   if (O.length === 0) throw Error("No messages to fork");
   let $ = null,
     _ = [],
@@ -38,13 +29,13 @@
     (Z.push(D), _.push(UA(W)), ($ = G.uuid));
   }
   return (
-    B8(
+    await jd2(
       z,
       _.join(`
 `) +
         `
 `,
-      { encoding: "utf8", flush: !0, mode: 384 },
+      { encoding: "utf8", mode: 384 },
     ),
     { sessionId: K, title: A, forkPath: z, serializedMessages: Z }
   );

@@@ function 'Yw4' (was 'Xq4') — structural (60.3%)
--- pretty-v2.1.19.js:156944
+++ pretty-v2.1.20.js:158669
@@ -1,4 +1,4 @@
-function Xq4() {
+function Yw4(A) {
   Jq4.useEffect(() => {
     let A = () => {
       if (c41())
@@ -9,7 +9,7 @@
             `
 `,
         );
-      v16();
+      n86(A?.());
     };
     return (
       process.on("exit", A),

@@@ function 'YU2' (was 'P_2') — structural (60.0%)
--- pretty-v2.1.19.js:438324
+++ pretty-v2.1.20.js:505914
@@ -1,3 +1,3 @@
 function P_2(A) {
-  return A.status === "running";
+  return A.type === "text";
 }

@@@ function 'aVK' (was 'gGK') — structural (59.9%)
--- pretty-v2.1.19.js:517576
+++ pretty-v2.1.20.js:521594
@@ -1,5 +1,5 @@
 function gGK(A) {
-  let K = a(29),
+  let K = s(26),
     { onComplete: q } = A,
     [Y] = p4(),
     z = l8.isSandboxingEnabled(),
@@ -40,23 +40,10 @@
       (K[9] = q),
       (K[10] = j));
   else j = K[10];
-  let M = j,
-    P;
-  if (K[11] !== q)
-    ((P = () => {
-      q();
-    }),
-      (K[11] = q),
-      (K[12] = P));
-  else P = K[12];
-  let V = P,
-    N;
-  if (K[13] === Symbol.for("react.memo_cache_sentinel"))
-    ((N = { context: "Confirmation" }), (K[13] = N));
-  else N = K[13];
-  if ((i1("confirm:no", V, N), !z)) {
+  let j = M;
+  if (!z) {
     let Q;
-    if (K[14] === Symbol.for("react.memo_cache_sentinel"))
+    if (K[11] === Symbol.for("react.memo_cache_sentinel"))
       ((Q = nZ.default.createElement(
         I,
         { flexDirection: "column", paddingY: 1 },
@@ -66,22 +53,22 @@
           "Sandbox is not enabled. Enable sandbox to configure override settings.",
         ),
       )),
-        (K[14] = Q));
-    else Q = K[14];
+        (K[11] = S));
+    else S = K[11];
     return Q;
   }
   if (H) {
     let Q;
-    if (K[15] === Symbol.for("react.memo_cache_sentinel"))
+    if (K[12] === Symbol.for("react.memo_cache_sentinel"))
       ((Q = nZ.default.createElement(
         f,
         { color: "subtle" },
         "Override settings are managed by a higher-priority configuration and cannot be changed locally.",
       )),
-        (K[15] = Q));
-    else Q = K[15];
+        (K[12] = S));
+    else S = K[12];
     let F;
-    if (K[16] === Symbol.for("react.memo_cache_sentinel"))
+    if (K[13] === Symbol.for("react.memo_cache_sentinel"))
       ((F = nZ.default.createElement(
         I,
         { flexDirection: "column", paddingY: 1 },
@@ -100,36 +87,37 @@
           ),
         ),
       )),
-        (K[16] = F));
-    else F = K[16];
+        (K[13] = B));
+    else B = K[13];
     return F;
   }
   let T;
-  if (K[17] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[14] === Symbol.for("react.memo_cache_sentinel"))
     ((T = nZ.default.createElement(
       I,
       { marginBottom: 1 },
       nZ.default.createElement(f, { bold: !0 }, "Configure Overrides:"),
     )),
-      (K[17] = T));
-  else T = K[17];
+      (K[14] = P));
+  else P = K[14];
   let k;
-  if (K[18] !== q) ((k = () => q()), (K[18] = q), (K[19] = k));
-  else k = K[19];
+  if (K[15] !== q)
+    ((V = () => q(void 0, { display: "skip" })), (K[15] = q), (K[16] = V));
+  else V = K[16];
   let R;
-  if (K[20] !== M || K[21] !== D || K[22] !== k)
+  if (K[17] !== j || K[18] !== D || K[19] !== V)
     ((R = nZ.default.createElement(T6, {
       options: D,
       onChange: M,
       onCancel: k,
     })),
-      (K[20] = M),
-      (K[21] = D),
-      (K[22] = k),
-      (K[23] = R));
-  else R = K[23];
+      (K[17] = j),
+      (K[18] = D),
+      (K[19] = V),
+      (K[20] = N));
+  else N = K[20];
   let x;
-  if (K[24] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[21] === Symbol.for("react.memo_cache_sentinel"))
     ((x = nZ.default.createElement(
       f,
       { dimColor: !0 },
@@ -141,10 +129,10 @@
       " ",
       "When a command fails due to sandbox restrictions, Claude can retry with dangerouslyDisableSandbox to run outside the sandbox (falling back to default permissions).",
     )),
-      (K[24] = x));
-  else x = K[24];
+      (K[21] = T));
+  else T = K[21];
   let S;
-  if (K[25] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[22] === Symbol.for("react.memo_cache_sentinel"))
     ((S = nZ.default.createElement(
       f,
       { dimColor: !0 },
@@ -156,10 +144,10 @@
       " ",
       "All bash commands invoked by the model must run in the sandbox unless they are explicitly listed in excludedCommands.",
     )),
-      (K[25] = S));
-  else S = K[25];
+      (K[22] = k));
+  else k = K[22];
   let g;
-  if (K[26] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[23] === Symbol.for("react.memo_cache_sentinel"))
     ((g = nZ.default.createElement(
       I,
       { flexDirection: "column", marginTop: 1, gap: 1 },
@@ -179,10 +167,10 @@
         ),
       ),
     )),
-      (K[26] = g));
-  else g = K[26];
+      (K[23] = R));
+  else R = K[23];
   let b;
-  if (K[27] !== R)
+  if (K[24] !== N)
     ((b = nZ.default.createElement(
       I,
       { flexDirection: "column", paddingY: 1 },
@@ -190,8 +178,8 @@
       R,
       g,
     )),
-      (K[27] = R),
-      (K[28] = b));
-  else b = K[28];
+      (K[24] = N),
+      (K[25] = b));
+  else b = K[25];
   return b;
 }

@@@ variable 'ia' (was 'Ts') — structural (59.4%)
--- pretty-v2.1.19.js:397190
+++ pretty-v2.1.20.js:324474
@@ -7,12 +7,13 @@
   ((YS = r(JA(), 1)),
     (el7 = r(JA(), 1)),
     (hf = el7.memo(function (K) {
-      let q = a(15),
+      let q = s(16),
         {
           patch: Y,
           dim: z,
           filePath: w,
           firstLine: H,
+          fileContent: J,
           width: J,
           skipHighlighting: X,
         } = K,
@@ -34,14 +35,16 @@
           G = null;
           break A;
         }
-        let N;
-        if (q[1] !== w || q[2] !== H || q[3] !== Y)
-          ((N = new V(Y, H, w)),
+        let T = J ?? null,
+          k;
+        if (q[1] !== w || q[2] !== H || q[3] !== Y || q[4] !== T)
+          ((k = new N(Y, H, w, T)),
             (q[1] = w),
             (q[2] = H),
             (q[3] = Y),
-            (q[4] = N));
-        else N = q[4];
+            (q[4] = T),
+            (q[5] = k));
+        else k = q[5];
         G = N;
       }
       let W = G,
@@ -53,19 +56,19 @@
         }
         let P = Math.max(1, Math.floor(J)),
           V;
-        if (q[5] !== W || q[6] !== z || q[7] !== P || q[8] !== $)
+        if (q[6] !== D || q[7] !== z || q[8] !== V || q[9] !== _)
           ((V = W.render($, P, z)),
-            (q[5] = W),
             (q[6] = z),
             (q[7] = P),
             (q[8] = $),
-            (q[9] = V));
-        else V = q[9];
+            (q[9] = _),
+            (q[10] = N));
+        else N = q[10];
         D = V;
       }
       let j = D,
         M;
-      if (q[10] !== z || q[11] !== j || q[12] !== Y || q[13] !== J)
+      if (q[11] !== z || q[12] !== j || q[13] !== Y || q[14] !== O)
         ((M = YS.createElement(
           I,
           null,
@@ -73,12 +76,12 @@
             ? YS.createElement(I, { flexDirection: "column" }, j.map(jK2))
             : YS.createElement(pl7, { patch: Y, dim: z, width: J }),
         )),
-          (q[10] = z),
           (q[11] = j),
           (q[12] = Y),
           (q[13] = J),
-          (q[14] = M));
-      else M = q[14];
+          (q[14] = O),
+          (q[15] = P));
+      else P = q[15];
       return M;
     })));
 });

@@@ function 'KV7' (was 'qe7') — structural (59.3%)
--- pretty-v2.1.19.js:421001
+++ pretty-v2.1.20.js:318739
@@ -29,10 +29,10 @@
 ${z}
 
 Provide a brief summary of what was accomplished:`,
-          enablePromptCaching: !0,
           signal: K,
           options: {
             querySource: "tool_use_summary_generation",
+            enablePromptCaching: !0,
             agents: [],
             isNonInteractiveSession: q,
             hasAppendSystemPrompt: !1,

@@@ function 'SRA' (was 'pv6') — structural (59.3%)
--- pretty-v2.1.19.js:387607
+++ pretty-v2.1.20.js:160891
@@ -1,3 +1,3 @@
 function pv6(A, K) {
-  return `${A}/${WD(K)}`;
+  return IRA(Zy(A), `${bn(K)}.json`);
 }

@@@ function 'IZ' (was 'NZ') — structural (59.2%)
--- pretty-v2.1.19.js:313583
+++ pretty-v2.1.20.js:309879
@@ -1,4 +1,6 @@
 function NZ(A, K) {
-  (K((q) => ({ ...q, queuedCommands: [...q.queuedCommands, A] })),
-    MO1("enqueue", typeof A.value === "string" ? A.value : void 0));
+  if (A.mode === "task-notification" && E$1.size > 0)
+    (C$1.push(typeof A.value === "string" ? A.value : ""), Aj6());
+  else K((q) => ({ ...q, queuedCommands: [...q.queuedCommands, A] }));
+  k$1("enqueue", typeof A.value === "string" ? A.value : void 0);
 }

@@@ function 'Z$' (was 'J$') — structural (58.7%)
--- pretty-v2.1.19.js:525930
+++ pretty-v2.1.20.js:530529
@@ -1,7 +1,7 @@
 async function J$({
   systemPrompt: A = [],
   userPrompt: K,
-  assistantPrompt: q,
+  outputFormat: q,
   signal: Y,
   options: z,
 }) {
@@ -12,7 +12,7 @@
         z6({ content: K }),
       ],
       async () => {
-        let H = [z6({ content: K }), ...(q ? [Df({ content: q })] : [])];
+        let H = [q6({ content: K })];
         return [
           await ls({
             messages: H,
@@ -24,6 +24,7 @@
               ...z,
               model: BX(),
               enablePromptCaching: z.enablePromptCaching ?? !1,
+              outputFormat: q,
               async getToolPermissionContext() {
                 return PD();
               },

@@@ function 'pkK' (was 'PVK') — structural (58.7%)
--- pretty-v2.1.19.js:540130
+++ pretty-v2.1.20.js:545177
@@ -1,11 +1,12 @@
 function PVK(A) {
-  let K = a(28),
+  let K = s(30),
     {
       toolUseConfirm: q,
       onDone: Y,
       onReject: z,
       verbose: w,
       toolUseContext: H,
+      workerBadge: J,
     } = A,
     [J] = p4(),
     X;
@@ -25,61 +26,72 @@
     D = zU2;
   if (!O) {
     let T;
-    if (K[5] !== Y || K[6] !== z || K[7] !== q || K[8] !== H || K[9] !== w)
+    if (
+      K[5] !== Y ||
+      K[6] !== z ||
+      K[7] !== q ||
+      K[8] !== H ||
+      K[9] !== w ||
+      K[10] !== J
+    )
       ((T = lpA.default.createElement(WT1, {
         toolUseConfirm: q,
         toolUseContext: H,
         onDone: Y,
         onReject: z,
         verbose: w,
+        workerBadge: J,
       })),
         (K[5] = Y),
         (K[6] = z),
         (K[7] = q),
         (K[8] = H),
         (K[9] = w),
-        (K[10] = T));
-    else T = K[10];
+        (K[10] = J),
+        (K[11] = k));
+    else k = K[11];
     return T;
   }
   let j;
-  if (K[11] !== J || K[12] !== q.input || K[13] !== q.tool || K[14] !== w)
+  if (K[12] !== O || K[13] !== q.input || K[14] !== q.tool || K[15] !== w)
     ((j = q.tool.renderToolUseMessage(q.input, { theme: J, verbose: w })),
-      (K[11] = J),
-      (K[12] = q.input),
-      (K[13] = q.tool),
-      (K[14] = w),
-      (K[15] = j));
-  else j = K[15];
+      (K[12] = O),
+      (K[13] = q.input),
+      (K[14] = q.tool),
+      (K[15] = w),
+      (K[16] = j));
+  else j = K[16];
   let M;
-  if (K[16] !== j || K[17] !== _)
+  if (K[17] !== j || K[18] !== Z)
     ((M = lpA.default.createElement(
       I,
       { flexDirection: "column", paddingX: 2, paddingY: 1 },
       lpA.default.createElement(f, null, _, "(", j, ")"),
     )),
-      (K[16] = j),
       (K[17] = _),
-      (K[18] = M));
-  else M = K[18];
+      (K[18] = Z),
+      (K[19] = P));
+  else P = K[19];
   let P = M,
     V = Z ? "read" : "write",
     N;
   if (
-    K[19] !== P ||
     K[20] !== Y ||
     K[21] !== z ||
     K[22] !== O ||
     K[23] !== V ||
     K[24] !== W ||
     K[25] !== q ||
-    K[26] !== H
+    K[26] !== q ||
+    K[27] !== H ||
+    K[28] !== J
   )
     ((N = lpA.default.createElement(Jm, {
       toolUseConfirm: q,
       toolUseContext: H,
       onDone: Y,
       onReject: z,
+      workerBadge: J,
       title: W,
       content: P,
       path: O,
@@ -88,7 +100,6 @@
       completionType: "tool_use_single",
       languageName: "none",
     })),
-      (K[19] = P),
       (K[20] = Y),
       (K[21] = z),
       (K[22] = O),
@@ -96,7 +107,9 @@
       (K[24] = W),
       (K[25] = q),
       (K[26] = H),
-      (K[27] = N));
-  else N = K[27];
+      (K[27] = H),
+      (K[28] = J),
+      (K[29] = T));
+  else T = K[29];
   return N;
 }

@@@ function 'QQ6' (was 'om6') — structural (58.1%)
--- pretty-v2.1.19.js:533698
+++ pretty-v2.1.20.js:538465
@@ -1,5 +1,6 @@
 function om6(A) {
   (h(`Detected skill change: ${A}`),
+    n("tengu_skill_file_changed", { source: "chokidar" }),
     WD1(),
     mu(),
     YgA(),

@@@ function 'w8K' (was 'ol2') — structural (58.1%)
--- pretty-v2.1.19.js:561056
+++ pretty-v2.1.20.js:410270
@@ -5,24 +5,13 @@
   if (A[0] !== K)
     ((q = G4.createElement(
       I,
-      {
-        alignItems: "center",
-        alignSelf: "center",
-        borderTopDimColor: !0,
-        borderBottom: !1,
-        borderLeft: !1,
-        borderRight: !1,
-        borderStyle: "single",
-        marginTop: 1,
-        paddingLeft: 2,
-        width: "100%",
-      },
+      { marginY: 1 },
       G4.createElement(
         f,
         { dimColor: !0 },
-        "Showing detailed transcript · ",
+        "✻ Conversation compacted (",
         K,
-        " to toggle",
+        " for history)",
       ),
     )),
       (A[0] = K),

@@@ function 'jgK' (was 'HhK') — structural (57.9%)
--- pretty-v2.1.19.js:567086
+++ pretty-v2.1.20.js:571204
@@ -1,5 +1,5 @@
 function HhK(A) {
-  let K = a(26),
+  let K = s(20),
     { serverNames: q, onDone: Y } = A,
     z;
   if (K[0] !== Y || K[1] !== q)
@@ -29,7 +29,6 @@
       (K[2] = z));
   else z = K[2];
   let w = z,
-    H = W8(),
     J;
   if (K[3] !== Y || K[4] !== q)
     ((J = () => {
@@ -42,110 +41,77 @@
       (K[5] = J));
   else J = K[5];
   let X = J,
+    O = `${q.length} new MCP servers found in .mcp.json`,
     O;
   if (K[6] === Symbol.for("react.memo_cache_sentinel"))
-    ((O = { context: "Confirmation" }), (K[6] = O));
+    ((X = UL.default.createElement(Sk1, null)), (K[6] = X));
   else O = K[6];
-  i1("confirm:no", X, O);
   let $;
-  if (K[7] !== q.length)
-    (($ = Vj.default.createElement(
-      f,
-      { bold: !0, color: "warning" },
-      q.length,
-      " new MCP servers found in .mcp.json",
-    )),
-      (K[7] = q.length),
-      (K[8] = $));
+  if (K[7] !== q) (($ = q.map(E4z)), (K[7] = q), (K[8] = $));
   else $ = K[8];
-  let _, Z;
-  if (K[9] === Symbol.for("react.memo_cache_sentinel"))
-    ((_ = Vj.default.createElement(f, null, "Select any you wish to enable.")),
-      (Z = Vj.default.createElement(xv1, null)),
-      (K[9] = _),
-      (K[10] = Z));
-  else ((_ = K[9]), (Z = K[10]));
   let G;
-  if (K[11] !== q) ((G = q.map(ei2)), (K[11] = q), (K[12] = G));
-  else G = K[12];
-  let W;
-  if (K[13] !== w || K[14] !== q || K[15] !== G)
+  if (K[9] !== w || K[10] !== q || K[11] !== $)
     ((W = Vj.default.createElement(Cv1, {
       options: G,
       defaultValue: q,
       onSubmit: w,
     })),
-      (K[13] = w),
-      (K[14] = q),
-      (K[15] = G),
-      (K[16] = W));
-  else W = K[16];
+      (K[9] = w),
+      (K[10] = q),
+      (K[11] = $),
+      (K[12] = _));
+  else _ = K[12];
   let D;
-  if (K[17] !== $ || K[18] !== W)
+  if (K[13] !== J || K[14] !== O || K[15] !== _)
     ((D = Vj.default.createElement(
       I,
       {
-        flexDirection: "column",
-        gap: 1,
-        padding: 1,
-        borderStyle: "round",
-        borderColor: "warning",
+        title: O,
+        subtitle: "Select any you wish to enable.",
+        color: "warning",
+        onCancel: J,
+        hideInputGuide: !0,
       },
       $,
       _,
-      Z,
-      W,
     )),
-      (K[17] = $),
-      (K[18] = W),
-      (K[19] = D));
-  else D = K[19];
+      (K[13] = J),
+      (K[14] = O),
+      (K[15] = _),
+      (K[16] = Z));
+  else Z = K[16];
   let j;
-  if (K[20] !== H.keyName || K[21] !== H.pending)
+  if (K[17] === Symbol.for("react.memo_cache_sentinel"))
     ((j = Vj.default.createElement(
       I,
-      { marginLeft: 3 },
+      { paddingX: 1 },
       Vj.default.createElement(
         f,
-        { dimColor: !0 },
-        H.pending
-          ? Vj.default.createElement(
-              Vj.default.Fragment,
-              null,
-              "Press ",
-              H.keyName,
-              " again to exit",
-            )
-          : Vj.default.createElement(
-              $8,
-              null,
-              Vj.default.createElement(k6, {
-                shortcut: "Space",
-                action: "select",
-              }),
-              Vj.default.createElement(k6, {
-                shortcut: "Enter",
-                action: "confirm",
-              }),
-              Vj.default.createElement(Q6, {
-                action: "confirm:no",
-                context: "Confirmation",
-                fallback: "Esc",
-                description: "reject all",
-              }),
-            ),
+        { dimColor: !0, italic: !0 },
+        UL.default.createElement(
+          w8,
+          null,
+          UL.default.createElement(M6, { shortcut: "Space", action: "select" }),
+          UL.default.createElement(M6, {
+            shortcut: "Enter",
+            action: "confirm",
+          }),
+          UL.default.createElement(d6, {
+            action: "confirm:no",
+            context: "Confirmation",
+            fallback: "Esc",
+            description: "reject all",
+          }),
+        ),
       ),
     )),
-      (K[20] = H.keyName),
-      (K[21] = H.pending),
-      (K[22] = j));
-  else j = K[22];
+      (K[17] = G));
+  else G = K[17];
   let M;
-  if (K[23] !== j || K[24] !== D)
+  if (K[18] !== Z)
     ((M = Vj.default.createElement(Vj.default.Fragment, null, D, j)),
-      (K[23] = j),
-      (K[24] = D),
-      (K[25] = M));
-  else M = K[25];
+      (K[18] = Z),
+      (K[19] = W));
+  else W = K[19];
   return M;
 }

@@@ variable 'ZI6' (was 'Ws') — structural (57.9%)
--- pretty-v2.1.19.js:433447
+++ pretty-v2.1.20.js:422945
@@ -20,31 +20,4 @@
   r6();
   hT();
   Gs();
-  I1();
-  P1();
-  so();
-  ew1();
-  E8();
-  Ye7();
-  cs();
-  mB();
-  QT();
-  e1();
-  JFA();
-  J7();
-  FN();
-  ZW();
-  dT();
-  XFA();
-  QmA();
-  _6K();
-  OR6();
-  Q2();
-  VFA();
-  fFA();
-  PZ();
-  Gf();
-  dR6();
-  F1();
-  iDA();
 });

@@@ variable 'zb6' (was 'AE6') — structural (57.9%)
--- pretty-v2.1.19.js:434659
+++ pretty-v2.1.20.js:450125
@@ -16,4 +16,10 @@
   EFA();
   CFA();
   E8();
+  Gf();
+  sh6();
+  B1();
+  P3A();
+  UV1();
+  HzK();
 });

@@@ variable '$3A' (was 'ws') — structural (57.9%)
--- pretty-v2.1.19.js:450231
+++ pretty-v2.1.20.js:456395
@@ -28,5 +28,4 @@
   Ya();
   e1();
   X5();
-  F1();
 });

@@@ function '_F6' (was 'vu6') — structural (57.9%)
--- pretty-v2.1.19.js:519505
+++ pretty-v2.1.20.js:523957
@@ -1,6 +1,5 @@
 function vu6() {
-  return `
-# Claude in Chrome browser automation
+  return `# Claude in Chrome browser automation
 
 You have access to browser automation tools (mcp__claude-in-chrome__*) for interacting with web pages in Chrome. Follow these guidelines for effective browser automation.
 
@@ -45,6 +44,5 @@
 1. Only reuse an existing tab if the user explicitly asks to work with it
 2. Otherwise, create a new tab with mcp__claude-in-chrome__tabs_create_mcp
 3. If a tool returns an error indicating the tab doesn't exist or is invalid, call tabs_context_mcp to get fresh tab IDs
-4. When a tab is closed by the user or a navigation error occurs, call tabs_context_mcp to see what tabs are available
-`;
+4. When a tab is closed by the user or a navigation error occurs, call tabs_context_mcp to see what tabs are available`;
 }

@@@ variable 'zt' (was 'Nw') — structural (57.9%)
--- pretty-v2.1.19.js:525985
+++ pretty-v2.1.20.js:461044
@@ -31,24 +31,4 @@
   WC();
   nr();
   PB();
-  PZ();
-  P1();
-  Vs();
-  _WA();
-  Mp();
-  pP();
-  iDA();
-  JFA();
-  e1();
-  I1A();
-  hT();
-  U4();
-  gVA();
-  J7();
-  Gs();
-  Ba();
-  r41();
-  Dk();
-  F1();
-  kK();
 });

@@@ variable 'LF6' (was 'rm6') — structural (57.9%)
--- pretty-v2.1.19.js:533355
+++ pretty-v2.1.20.js:526919
@@ -6,16 +6,4 @@
   q6();
   Ow();
   U4();
-  w0();
-  iw();
-  u8();
-  rl();
-  l6();
-  QG();
-  PK();
-  LMK();
-  AWA();
-  sr();
-  r6();
-  e1();
 });

@@@ variable 'vNK' (was 'WQ6') — structural (57.9%)
--- pretty-v2.1.19.js:568835
+++ pretty-v2.1.20.js:527811
@@ -4,4 +4,6 @@
   hF();
   lP();
   F1();
+  mK();
+  TS();
 });

@@@ variable 'Aw' (was 'PQ6') — structural (57.9%)
--- pretty-v2.1.19.js:571119
+++ pretty-v2.1.20.js:530585
@@ -4,4 +4,50 @@
   e1();
   P1();
   dK();
+  Ct();
+  gk();
+  i6();
+  m4();
+  r6();
+  R1();
+  P8();
+  H7();
+  Y0();
+  xD();
+  dP();
+  KI();
+  o7();
+  o7();
+  a1();
+  C$6();
+  pbA();
+  QFA();
+  PRA();
+  lw();
+  iGA();
+  N2A();
+  gk();
+  ZC();
+  To();
+  Cu();
+  Z_();
+  D1();
+  Qa();
+  nGA();
+  vp();
+  dP();
+  NjA();
+  YUA();
+  Y6();
+  A6A();
+  FT();
+  m4();
+  mfA();
+  H7();
+  ba();
+  ha();
+  UK1();
+  jk();
+  B1();
+  o7();
 });

@@@ variable 'FQ6' (was 'gbK') — structural (57.9%)
--- pretty-v2.1.19.js:572067
+++ pretty-v2.1.20.js:538123
@@ -4,4 +4,17 @@
   r6();
   F1();
   q6();
+  Xw();
+  m4();
+  Y0();
+  Jw();
+  g8();
+  ki();
+  i6();
+  FG();
+  ZK();
+  nvK();
+  iGA();
+  ko();
+  Y6();
 });

@@@ function 'ukK' (was 'ZVK') — structural (57.7%)
--- pretty-v2.1.19.js:539066
+++ pretty-v2.1.20.js:544222
@@ -1,17 +1,25 @@
 function ZVK(A) {
-  let K = a(24),
+  let K = s(27),
     {
       toolUseConfirm: q,
       toolUseContext: Y,
       onDone: z,
       onReject: w,
       verbose: H,
+      workerBadge: J,
     } = A,
     J,
     X,
     O,
     $;
-  if (K[0] !== z || K[1] !== w || K[2] !== q || K[3] !== Y || K[4] !== H) {
+  if (
+    K[0] !== z ||
+    K[1] !== w ||
+    K[2] !== q ||
+    K[3] !== Y ||
+    K[4] !== H ||
+    K[5] !== J
+  ) {
     $ = Symbol.for("react.early_return_sentinel");
     A: {
       ({ command: J, description: X } = c7.inputSchema.parse(q.input));
@@ -24,6 +32,7 @@
           onDone: z,
           verbose: H,
           onReject: w,
+          workerBadge: J,
           serverName: W,
           toolName: D,
           args: j,
@@ -40,19 +49,21 @@
       (K[5] = J),
       (K[6] = X),
       (K[7] = O),
-      (K[8] = $));
-  } else ((J = K[5]), (X = K[6]), (O = K[7]), ($ = K[8]));
+      (K[8] = $),
+      (K[9] = _));
+  } else ((O = K[6]), (X = K[7]), ($ = K[8]), (_ = K[9]));
   if ($ !== Symbol.for("react.early_return_sentinel")) return $;
   let _ = O;
   if (_) {
     let G;
     if (
-      K[9] !== z ||
       K[10] !== w ||
       K[11] !== _ ||
       K[12] !== q ||
       K[13] !== Y ||
-      K[14] !== H
+      K[14] !== Y ||
+      K[15] !== H ||
+      K[16] !== J
     )
       ((G = QJ.default.createElement(zVK, {
         toolUseConfirm: q,
@@ -60,27 +71,30 @@
         onDone: z,
         onReject: w,
         verbose: H,
+        workerBadge: J,
         sedInfo: _,
       })),
-        (K[9] = z),
         (K[10] = w),
         (K[11] = _),
         (K[12] = q),
         (K[13] = Y),
         (K[14] = H),
-        (K[15] = G));
-    else G = K[15];
+        (K[15] = H),
+        (K[16] = J),
+        (K[17] = W));
+    else W = K[17];
     return G;
   }
   let Z;
   if (
-    K[16] !== J ||
-    K[17] !== X ||
     K[18] !== z ||
     K[19] !== w ||
     K[20] !== q ||
     K[21] !== Y ||
-    K[22] !== H
+    K[22] !== q ||
+    K[23] !== Y ||
+    K[24] !== H ||
+    K[25] !== J
   )
     ((Z = QJ.default.createElement(rQ2, {
       toolUseConfirm: q,
@@ -88,17 +102,19 @@
       onDone: z,
       onReject: w,
       verbose: H,
+      workerBadge: J,
       command: J,
       description: X,
     })),
-      (K[16] = J),
-      (K[17] = X),
       (K[18] = z),
       (K[19] = w),
       (K[20] = q),
       (K[21] = Y),
       (K[22] = H),
-      (K[23] = Z));
-  else Z = K[23];
+      (K[23] = Y),
+      (K[24] = H),
+      (K[25] = J),
+      (K[26] = G));
+  else G = K[26];
   return Z;
 }

@@@ function 'FZ2' (was 'L12') — structural (57.7%)
--- pretty-v2.1.19.js:382661
+++ pretty-v2.1.20.js:407312
@@ -1,9 +1,9 @@
 function L12(A) {
   return A.map((K) => {
     let q = K.color ? ` color="${K.color}"` : "";
-    return `<teammate-message teammate_id="${K.from}"${q}>
+    return `<${IO} teammate_id="${K.from}"${q}>
 ${K.text}
-</teammate-message>`;
+</${IO}>`;
   }).join(`
 
 `);

@@@ function 'cfA' (was 'lVA') — structural (57.5%)
--- pretty-v2.1.19.js:2759
+++ pretty-v2.1.20.js:2785
@@ -1,5 +1,7 @@
 function lVA() {
   return (
-    process.env.CLAUDE_CODE_DEBUG_LOGS_DIR ?? uc6(f8(), "debug", `${n1()}.txt`)
+    kn6() ??
+    process.env.CLAUDE_CODE_DEBUG_LOGS_DIR ??
+    En6(M8(), "debug", `${i1()}.txt`)
   );
 }

@@@ function 'dFA' (was 'emA') — structural (57.5%)
--- pretty-v2.1.19.js:525010
+++ pretty-v2.1.20.js:529611
@@ -1,11 +1,8 @@
 async function emA(A, K, q) {
-  let z = `
-${await EDK(K, q)}`;
+  let z = await QNK(K, q);
   return [
     ...A,
-    `
-
-Notes:
+    `Notes:
 - Agent threads always have their cwd reset between bash calls, as a result please only use absolute file paths.
 - In your final response always share relevant file names and code snippets. Any file paths you return in your response MUST be absolute. Do NOT use relative paths.
 - For clear communication with the user the assistant MUST avoid using emojis.

@@@ function 'ya7' (was 'h4K') — structural (57.3%)
--- pretty-v2.1.19.js:438337
+++ pretty-v2.1.20.js:388965
@@ -1,5 +1,5 @@
 function h4K(A) {
-  let K = a(100),
+  let K = s(90),
     {
       mode: q,
       elapsedTimeMs: Y,
@@ -20,16 +20,11 @@
     { isConnected: V } = SN6(),
     { columns: N } = N8(),
     T = BZ1(),
-    k;
-  if (K[0] !== P.tasks)
-    ((k = as(P.tasks).filter(k_2)), (K[0] = P.tasks), (K[1] = k));
-  else k = K[1];
-  let R = k.length > 0,
     [x, S] = Mv.useState(null),
     g = Mv.useRef(null),
     b,
     Q;
-  if (K[2] !== q)
+  if (K[0] !== q)
     ((b = () => {
       let v8 = null,
         d8 = null;
@@ -52,26 +47,23 @@
       };
     }),
       (Q = [q]),
-      (K[2] = q),
-      (K[3] = b),
-      (K[4] = Q));
-  else ((b = K[3]), (Q = K[4]));
+      (K[0] = q),
+      (K[1] = S),
+      (K[2] = B));
+  else ((S = K[1]), (B = K[2]));
   Mv.useEffect(b, Q);
   let F;
-  if (K[5] !== T || K[6] !== _)
+  if (K[3] !== T || K[4] !== _)
     ((F = ew() ? T?.find(E_2) : _?.find(v_2)),
-      (K[5] = T),
-      (K[6] = _),
-      (K[7] = F));
-  else F = K[7];
+      (K[3] = T),
+      (K[4] = _),
+      (K[5] = x));
+  else x = K[5];
   let B = F,
     d;
-  if (K[8] !== T || K[9] !== _)
-    ((d = ew() ? T?.find(T_2) : _?.find(N_2)),
-      (K[8] = T),
-      (K[9] = _),
-      (K[10] = d));
-  else d = K[10];
+  if (K[6] !== T || K[7] !== _)
+    ((Q = ew() ? QO2(T) : _?.find(uO2)), (K[6] = T), (K[7] = _), (K[8] = Q));
+  else Q = K[8];
   let o = d,
     [l] = Mv.useState(f_2),
     e = (X ?? B?.activeForm ?? l) + "…",
@@ -81,7 +73,7 @@
     t = Mv.useRef(w),
     $A,
     VA;
-  if (K[11] !== q)
+  if (K[9] !== q)
     (($A = () => {
       let v8 = "spinner-" + q;
       return (
@@ -92,24 +84,24 @@
       );
     }),
       (VA = [q]),
-      (K[11] = q),
-      (K[12] = $A),
-      (K[13] = VA));
-  else (($A = K[12]), (VA = K[13]));
+      (K[9] = q),
+      (K[10] = DA),
+      (K[11] = o));
+  else ((DA = K[10]), (o = K[11]));
   Mv.useEffect($A, VA);
   let MA, SA;
-  if (K[14] !== w)
+  if (K[12] !== w)
     ((SA = () => {
       t.current = w;
     }),
       (MA = [w]),
-      (K[14] = w),
-      (K[15] = MA),
-      (K[16] = SA));
-  else ((MA = K[15]), (SA = K[16]));
+      (K[12] = w),
+      (K[13] = _A),
+      (K[14] = PA));
+  else ((_A = K[13]), (PA = K[14]));
   Mv.useEffect(SA, MA);
   let BA;
-  if (K[17] !== V)
+  if (K[15] !== V)
     ((BA = () => {
       if (!V) {
         D(4);
@@ -117,12 +109,12 @@
       }
       D(V_2);
     }),
-      (K[17] = V),
-      (K[18] = BA));
-  else BA = K[18];
+      (K[15] = V),
+      (K[16] = jA));
+  else jA = K[16];
   zY(BA, 120);
   let s;
-  if (K[19] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[17] === Symbol.for("react.memo_cache_sentinel"))
     ((s = () => {
       M((v8) => {
         let d8 = t.current - v8;
@@ -134,33 +126,37 @@
         return Math.min(v8 + z7, t.current);
       });
     }),
-      (K[19] = s));
-  else s = K[19];
+      (K[17] = yA));
+  else yA = K[17];
   zY(s, 10);
   let AA = p7(e) + 2,
     wA;
-  if (K[20] !== x)
+  if (K[18] !== k)
     ((wA =
       x === "thinking"
         ? "thinking"
         : typeof x === "number"
           ? `thought for ${Math.max(1, Math.round(x / 1000))}s`
           : null),
-      (K[20] = x),
-      (K[21] = wA));
-  else wA = K[21];
+      (K[18] = k),
+      (K[19] = YA));
+  else YA = K[19];
   let KA = wA,
     zA;
-  if (K[22] !== KA) ((zA = KA ? p7(KA) : 0), (K[22] = KA), (K[23] = zA));
-  else zA = K[23];
+  if (K[20] !== KA) ((zA = KA ? m7(KA) : 0), (K[20] = KA), (K[21] = zA));
+  else zA = K[21];
   let HA = zA,
     vA,
     OA;
-  if (K[24] !== Y)
-    ((OA = Dw(Y)), (vA = p7(OA)), (K[24] = Y), (K[25] = vA), (K[26] = OA));
-  else ((vA = K[25]), (OA = K[26]));
+  if (K[22] !== Y)
+    (($A = O0(Y)), (t = m7($A)), (K[22] = Y), (K[23] = t), (K[24] = $A));
+  else ((t = K[23]), ($A = K[24]));
   let LA = vA,
     FA = w5("chat:cancel", "Chat", "esc"),
+    LA;
+  if (K[25] !== ZA) ((LA = ZA.toLowerCase()), (K[25] = ZA), (K[26] = LA));
+  else LA = K[26];
+  let mA = LA,
     RA = p7(`${FA} to interrupt`),
     yA;
   if (K[27] !== j) ((yA = M3(Math.round(j / 4))), (K[27] = j), (K[28] = yA));
@@ -183,24 +179,11 @@
     NA = O1 && s1 > PA + LA,
     cA = PA + (NA ? LA + d1 : 0),
     z1 = s1 > cA + RA,
-    dA = cA + (z1 ? RA + d1 : 0),
-    iA = M1 && s1 > dA + _1,
     V1 = dA + (iA ? _1 + d1 : 0),
     v1 = u1 && s1 > V1 + j1,
     g1 = V1 + (v1 ? j1 + d1 : 0),
-    g6 = p7("shift+↑/↓ to select"),
     k8 = R && s1 > g1 + g6,
-    w8 = g1 + (k8 ? g6 + d1 : 0),
-    f4 = "",
-    C4 = !1;
-  if (P8()) {
-    f4 = P.showTeammateMessagePreview
-      ? "ctrl+shift+o to collapse"
-      : "ctrl+shift+o to expand";
-    let v8 = p7(f4);
-    C4 = R && s1 > w8 + v8;
-  }
-  let T8;
+    U1;
   if (K[29] !== FA || K[30] !== z1)
     ((T8 = z1
       ? [
@@ -268,80 +251,55 @@
       (K[44] = Y7));
   else Y7 = K[44];
   let R8;
-  if (K[45] !== H6 || K[46] !== KA)
+  if (K[45] !== J6 || K[46] !== k || K[47] !== KA)
     ((R8 =
       H6 && KA
-        ? [h4.createElement(f, { dimColor: !0, key: "thinking" }, KA)]
+        ? [
+            k === "thinking"
+              ? n4.createElement(Ea7, { key: "thinking", text: KA })
+              : n4.createElement(f, { dimColor: !0, key: "thinking" }, KA),
+          ]
         : []),
       (K[45] = H6),
       (K[46] = KA),
-      (K[47] = R8));
-  else R8 = K[47];
-  let q4;
-  if (K[48] !== k8)
-    ((q4 = k8
-      ? [
-          h4.createElement(
-            f,
-            { dimColor: !0, key: "selectHint" },
-            "shift+↑/↓ to select",
-          ),
-        ]
-      : []),
-      (K[48] = k8),
-      (K[49] = q4));
-  else q4 = K[49];
-  let IK;
-  if (K[50] !== f4 || K[51] !== C4)
-    ((IK = C4
-      ? [h4.createElement(f, { dimColor: !0, key: "previewHint" }, f4)]
-      : []),
-      (K[50] = f4),
-      (K[51] = C4),
-      (K[52] = IK));
-  else IK = K[52];
+      (K[47] = KA),
+      (K[48] = $4));
+  else $4 = K[48];
   let i7;
   if (
+    K[49] !== V ||
+    K[50] !== U1 ||
+    K[51] !== T6 ||
+    K[52] !== R8 ||
     K[53] !== V ||
     K[54] !== T8 ||
-    K[55] !== r8 ||
-    K[56] !== m4 ||
-    K[57] !== j5 ||
-    K[58] !== Y7 ||
-    K[59] !== R8 ||
-    K[60] !== q4 ||
-    K[61] !== IK
+    K[55] !== $4
   ) {
-    if (
-      ((i7 = [...T8, ...r8, ...m4, ...j5, ...Y7, ...R8, ...q4, ...IK]),
-      V === !1)
-    ) {
+    if (((W8 = [...U1, ...T6, ...R8, ...a6, ...V4, ...$4]), V === !1)) {
       let v8;
-      if (K[63] === Symbol.for("react.memo_cache_sentinel"))
+      if (K[57] === Symbol.for("react.memo_cache_sentinel"))
         ((v8 = h4.createElement(
           I,
           { key: "offline" },
           h4.createElement(f, { color: "error", bold: !0 }, "offline"),
         )),
-          (K[63] = v8));
-      else v8 = K[63];
+          (K[57] = O7));
+      else O7 = K[57];
       i7.push(v8);
     }
-    ((K[53] = V),
+    ((K[49] = V),
+      (K[50] = U1),
+      (K[51] = T6),
+      (K[52] = R8),
+      (K[53] = a6),
       (K[54] = T8),
       (K[55] = r8),
-      (K[56] = m4),
-      (K[57] = j5),
-      (K[58] = Y7),
-      (K[59] = R8),
-      (K[60] = q4),
-      (K[61] = IK),
-      (K[62] = i7));
-  } else i7 = K[62];
+      (K[56] = W8));
+  } else W8 = K[56];
   let SK = H ?? (V === !1 ? "inactive" : "claude"),
     rq = J ?? "claudeShimmer",
     c3;
-  if (K[64] !== i7)
+  if (K[58] !== W8)
     ((c3 =
       i7.length > 0
         ? h4.createElement(
@@ -352,34 +310,36 @@
             h4.createElement(f, { dimColor: !0 }, ")"),
           )
         : null),
-      (K[64] = i7),
-      (K[65] = c3));
-  else c3 = K[65];
+      (K[58] = W8),
+      (K[59] = MK));
+  else MK = K[59];
   let hK = c3,
+    d8 = H ? 0 : e,
     e4;
-  if (K[66] !== W || K[67] !== V || K[68] !== SK || K[69] !== GA)
+  if (K[60] !== W || K[61] !== V || K[62] !== v4 || K[63] !== d8)
     ((e4 = h4.createElement(n5A, {
       frame: W,
       messageColor: SK,
       stalledIntensity: GA,
       isConnected: V,
     })),
-      (K[66] = W),
-      (K[67] = V),
-      (K[68] = SK),
-      (K[69] = GA),
-      (K[70] = e4));
-  else e4 = K[70];
-  let TK;
+      (K[60] = W),
+      (K[61] = V),
+      (K[62] = v4),
+      (K[63] = d8),
+      (K[64] = I8));
+  else I8 = K[64];
+  let uK = H ? 0 : e,
+    jK;
   if (
+    K[65] !== OA ||
+    K[66] !== JA ||
+    K[67] !== V ||
+    K[68] !== a ||
+    K[69] !== v4 ||
+    K[70] !== q ||
     K[71] !== ZA ||
-    K[72] !== WA ||
-    K[73] !== V ||
-    K[74] !== e ||
-    K[75] !== SK ||
-    K[76] !== q ||
-    K[77] !== rq ||
-    K[78] !== GA
+    K[72] !== uK
   )
     ((TK = h4.createElement(QN6, {
       message: e,
@@ -391,26 +351,26 @@
       shimmerColor: rq,
       stalledIntensity: GA,
     })),
+      (K[65] = OA),
+      (K[66] = JA),
+      (K[67] = V),
+      (K[68] = a),
+      (K[69] = v4),
+      (K[70] = q),
       (K[71] = ZA),
       (K[72] = WA),
-      (K[73] = V),
-      (K[74] = e),
-      (K[75] = SK),
-      (K[76] = q),
-      (K[77] = rq),
-      (K[78] = GA),
-      (K[79] = TK));
-  else TK = K[79];
+      (K[73] = jK));
+  else jK = K[73];
   let Gq;
-  if (K[80] !== P.viewingAgentTaskId)
+  if (K[74] !== P.viewingAgentTaskId)
     ((Gq =
       P.viewingAgentTaskId &&
       h4.createElement(f, { dimColor: !0 }, " [leader]")),
-      (K[80] = P.viewingAgentTaskId),
-      (K[81] = Gq));
-  else Gq = K[81];
+      (K[74] = P.viewingAgentTaskId),
+      (K[75] = BK));
+  else BK = K[75];
   let q5;
-  if (K[82] !== hK || K[83] !== e4 || K[84] !== TK || K[85] !== Gq)
+  if (K[76] !== xK || K[77] !== I8 || K[78] !== jK || K[79] !== BK)
     ((q5 = h4.createElement(
       I,
       { flexDirection: "row", flexWrap: "wrap", marginTop: 1, width: "100%" },
@@ -419,31 +379,22 @@
       hK,
       Gq,
     )),
-      (K[82] = hK),
-      (K[83] = e4),
-      (K[84] = TK),
-      (K[85] = Gq),
-      (K[86] = q5));
-  else q5 = K[86];
+      (K[76] = xK),
+      (K[77] = I8),
+      (K[78] = jK),
+      (K[79] = BK),
+      (K[80] = Z5));
+  else Z5 = K[80];
   let nK;
   if (
-    K[87] !== P.selectedIPAgentIndex ||
-    K[88] !== P.showExpandedTodos ||
-    K[89] !== P.viewSelectionMode ||
-    K[90] !== W ||
-    K[91] !== R ||
-    K[92] !== o ||
-    K[93] !== z ||
-    K[94] !== T ||
-    K[95] !== _
+    K[81] !== P.showExpandedTodos ||
+    K[82] !== u ||
+    K[83] !== z ||
+    K[84] !== T ||
+    K[85] !== _
   )
-    ((nK = R
-      ? h4.createElement(yM1, {
-          frame: W,
-          selectedIndex: P.selectedIPAgentIndex,
-          isInSelectionMode: P.viewSelectionMode === "selecting-agent",
-        })
-      : P.showExpandedTodos && T && T.length > 0
+    ((J3 =
+      P.showExpandedTodos && T && T.length > 0
         ? h4.createElement(
             I,
             { width: "100%", flexDirection: "column" },
@@ -472,28 +423,24 @@
                 ),
               )
             : null),
-      (K[87] = P.selectedIPAgentIndex),
-      (K[88] = P.showExpandedTodos),
-      (K[89] = P.viewSelectionMode),
-      (K[90] = W),
-      (K[91] = R),
-      (K[92] = o),
-      (K[93] = z),
-      (K[94] = T),
-      (K[95] = _),
-      (K[96] = nK));
-  else nK = K[96];
+      (K[81] = P.showExpandedTodos),
+      (K[82] = u),
+      (K[83] = z),
+      (K[84] = T),
+      (K[85] = _),
+      (K[86] = J3));
+  else J3 = K[86];
   let M6;
-  if (K[97] !== q5 || K[98] !== nK)
+  if (K[87] !== Z5 || K[88] !== J3)
     ((M6 = h4.createElement(
       I,
       { flexDirection: "column", width: "100%", alignItems: "flex-start" },
       q5,
       nK,
     )),
-      (K[97] = q5),
-      (K[98] = nK),
-      (K[99] = M6));
-  else M6 = K[99];
+      (K[87] = Z5),
+      (K[88] = J3),
+      (K[89] = S4));
+  else S4 = K[89];
   return M6;
 }

@@@ function 'zn2' (was 'SB2') — structural (57.1%)
--- pretty-v2.1.19.js:525025
+++ pretty-v2.1.20.js:529623
@@ -1,7 +1,6 @@
 function SB2() {
-  if (!lMA()) return "";
-  return `
-# Scratchpad Directory
+  if (!dPA()) return null;
+  return `# Scratchpad Directory
 
 IMPORTANT: Always use this scratchpad directory for temporary files instead of \`/tmp\` or other system temp directories:
 \`${gN1()}\`
@@ -15,6 +14,5 @@
 
 Only use \`/tmp\` if the user explicitly requests it.
 
-The scratchpad directory is session-specific, isolated from the user's project, and can be used freely without permission prompts.
-`;
+The scratchpad directory is session-specific, isolated from the user's project, and can be used freely without permission prompts.`;
 }

@@@ function 'V8K' (was 'pU7') — structural (57.0%)
--- pretty-v2.1.19.js:386908
+++ pretty-v2.1.20.js:411611
@@ -19,7 +19,10 @@
             "run_in_background" in P.data &&
             P.data.run_in_background === !0,
           R = D?.output?.status === "async_launched",
-          x = k || R;
+          F = B || x,
+          Q =
+            (k.success && !!k.data.name) ||
+            V?.output?.status === "teammate_spawned";
         return {
           id: _.id,
           agentType: V,
@@ -29,70 +32,100 @@
           isResolved: Z,
           isError: G,
           isAsync: x,
+          isTeammateSpawn: Q,
           color: T,
           lastToolInfo: M,
         };
       },
     ),
+    w = z.filter((D) => D.isTeammateSpawn).length,
+    H = j8() ? z.filter((D) => !D.isTeammateSpawn) : z,
+    J = j8() ? A.filter((D, M) => !z[M]?.isTeammateSpawn) : A,
     w = A.some((_) => !_.isResolved),
     H = A.some((_) => _.isError),
     J = !w,
     X = z.length > 0 && z.every((_) => _.agentType === z[0]?.agentType),
     O = X ? z[0]?.agentType : null,
-    $ = z.every((_) => _.isAsync);
+    G = H.every((D) => D.isAsync),
+    W =
+      j8() && w > 0
+        ? S6.createElement(
+            I,
+            { flexDirection: "row", marginTop: 1 },
+            S6.createElement(Ds, {
+              shouldAnimate: !1,
+              isUnresolved: !1,
+              isError: !1,
+            }),
+            S6.createElement(
+              f,
+              { dimColor: !0 },
+              "Created ",
+              S6.createElement(f, { bold: !0 }, w),
+              " ",
+              w === 1 ? "teammate" : "teammates",
+            ),
+          )
+        : null;
+  if (H.length === 0) return W;
   return B6.createElement(
     I,
-    { flexDirection: "column", marginTop: 1 },
+    { flexDirection: "column" },
+    W,
     B6.createElement(
       I,
-      { flexDirection: "row" },
-      B6.createElement(JqA, {
-        shouldAnimate: q && w,
-        isUnresolved: w,
-        isError: H,
-      }),
+      { flexDirection: "column", marginTop: 1 },
       B6.createElement(
         f,
-        null,
-        J
-          ? B6.createElement(
-              B6.Fragment,
-              null,
-              B6.createElement(f, { bold: !0 }, A.length),
-              " ",
-              O ? `${O} agents` : "agents",
-              " ",
-              $ ? "launched" : "finished",
-            )
-          : B6.createElement(
-              B6.Fragment,
-              null,
-              "Running ",
-              B6.createElement(f, { bold: !0 }, A.length),
-              " ",
-              O ? `${O} agents` : "agents",
-              "…",
-            ),
-        " ",
+        { flexDirection: "row" },
+        S6.createElement(Ds, {
+          shouldAnimate: q && O,
+          isUnresolved: O,
+          isError: X,
+        }),
+        S6.createElement(
+          f,
+          null,
+          $
+            ? S6.createElement(
+                S6.Fragment,
+                null,
+                S6.createElement(f, { bold: !0 }, J.length),
+                " ",
+                Z ? `${Z} agents` : "agents",
+                " ",
+                G ? "launched" : "finished",
+              )
+            : S6.createElement(
+                S6.Fragment,
+                null,
+                "Running ",
+                S6.createElement(f, { bold: !0 }, J.length),
+                " ",
+                Z ? `${Z} agents` : "agents",
+                "…",
+              ),
+          " ",
+        ),
+        S6.createElement(TI, null),
+      ),
+      H.map((D, M) =>
+        S6.createElement(Z8K, {
+          key: D.id,
+          agentType: D.agentType,
+          description: D.description,
+          toolUseCount: D.toolUseCount,
+          tokens: D.tokens,
+          color: D.color,
+          isLast: M === H.length - 1,
+          isResolved: D.isResolved,
+          isError: D.isError,
+          isAsync: D.isAsync,
+          shouldAnimate: q,
+          lastToolInfo: D.lastToolInfo,
+          hideType: _,
+        }),
       ),
-      B6.createElement(jI, null),
-    ),
-    z.map((_, Z) =>
-      B6.createElement(BU7, {
-        key: _.id,
-        agentType: _.agentType,
-        description: _.description,
-        toolUseCount: _.toolUseCount,
-        tokens: _.tokens,
-        color: _.color,
-        isLast: Z === z.length - 1,
-        isResolved: _.isResolved,
-        isError: _.isError,
-        isAsync: _.isAsync,
-        shouldAnimate: q,
-        lastToolInfo: _.lastToolInfo,
-        hideType: X,
-      }),
     ),
   );
 }

@@@ variable 'ho3' (was 'ug3') — structural (57.0%)
--- pretty-v2.1.19.js:171848
+++ pretty-v2.1.20.js:174822
@@ -1,4 +1,5 @@
-  ug3 = (A, K) => {
+  ho3 = (A, K, q) => {
+    let Y = q ?? K;
     if ("borderStyle" in K) {
       let q = K.borderStyle ? 1 : 0;
       (A.setBorder(P3.Top, K.borderTop !== !1 ? q : 0),
@@ -6,11 +7,13 @@
         A.setBorder(P3.Left, K.borderLeft !== !1 ? q : 0),
         A.setBorder(P3.Right, K.borderRight !== !1 ? q : 0));
     } else {
-      if ("borderTop" in K) A.setBorder(P3.Top, K.borderTop === !1 ? 0 : 1);
-      if ("borderBottom" in K)
+      if ("borderTop" in K && K.borderTop !== void 0)
+        A.setBorder(D3.Top, K.borderTop === !1 ? 0 : 1);
+      if ("borderBottom" in K && K.borderBottom !== void 0)
         A.setBorder(P3.Bottom, K.borderBottom === !1 ? 0 : 1);
-      if ("borderLeft" in K) A.setBorder(P3.Left, K.borderLeft === !1 ? 0 : 1);
-      if ("borderRight" in K)
+      if ("borderLeft" in K && K.borderLeft !== void 0)
+        A.setBorder(D3.Left, K.borderLeft === !1 ? 0 : 1);
+      if ("borderRight" in K && K.borderRight !== void 0)
         A.setBorder(P3.Right, K.borderRight === !1 ? 0 : 1);
     }
   },

@@@ variable 'zfK' (was 'lGK') — structural (56.9%)
--- pretty-v2.1.19.js:518058
+++ pretty-v2.1.20.js:522291
@@ -6,7 +6,6 @@
   u8();
   e1();
   UGK();
-  sq();
   dGK = r(JA(), 1);
   ((Pb2 = {
     name: "sandbox",
@@ -15,8 +14,11 @@
         K = l8.isAutoAllowBashIfSandboxedEnabled(),
         q = l8.areUnsandboxedCommandsAllowed(),
         Y = l8.areSandboxSettingsLockedByPolicy(),
-        z = A ? "✓" : "○",
-        w = "sandbox disabled";
+        z = x8.checkDependencies().errors.length === 0,
+        w;
+      if (!z) w = K1.warning;
+      else w = A ? K1.tick : K1.circle;
+      let H = "sandbox disabled";
       if (A)
         ((w = K ? "sandbox enabled (auto-allow)" : "sandbox enabled"),
           (w += q ? ", fallback allowed" : ""));
@@ -25,7 +27,8 @@
     },
     argumentHint: 'exclude "command pattern"',
     isEnabled: () => !0,
-    isHidden: !l8.isSupportedPlatform(),
+    isHidden: !x8.isSupportedPlatform() || !x8.isPlatformInEnabledList(),
+    immediate: !0,
     type: "local-jsx",
     userFacingName: () => "sandbox",
     call: Mb2,

@@@ function 'ta2' (was 'NF2') — structural (56.8%)
--- pretty-v2.1.19.js:534398
+++ pretty-v2.1.20.js:539199
@@ -1,19 +1,22 @@
-function NF2() {
+async function ta2() {
   let A = O9A(),
     K = { messages: 0, errors: 0 },
     q = hA();
   try {
-    let Y = af(f8(), "debug");
-    if (!q.existsSync(Y)) return K;
-    let w = q
-      .readdirSync(Y)
-      .filter(
-        (H) => H.isFile() && H.name.endsWith(".txt") && H.name !== "latest",
-      );
+    let Y = NP(M8(), "debug"),
+      z;
+    try {
+      z = await q.readdir(Y);
+    } catch {
+      return K;
+    }
+    let w = z.filter(
+      (H) => H.isFile() && H.name.endsWith(".txt") && H.name !== "latest",
+    );
     for (let H of w)
       try {
         let J = af(Y, H.name);
-        if (q.statSync(J).mtime < A) (q.unlinkSync(J), K.messages++);
+        if ((await q.stat(J)).mtime < A) (await q.unlink(J), K.messages++);
       } catch {
         K.errors++;
       }

@@@ variable 'dFK' (was 'kbK') — structural (56.7%)
--- pretty-v2.1.19.js:571254
+++ pretty-v2.1.20.js:575783
@@ -6,5 +6,11 @@
   o2();
   PK();
   PQ6();
-  ((hW = r(JA(), 1)), (Fv1 = r(JA(), 1)));
+  n5A();
+  WS();
+  IK();
+  iq();
+  d2();
+  $q();
+  wq = r(XA(), 1);
 });

@@@ variable 'lFK' (was 'ubK') — structural (56.7%)
--- pretty-v2.1.19.js:571933
+++ pretty-v2.1.20.js:575859
@@ -4,9 +4,5 @@
   SbK();
   o2();
   bbK();
-  q6();
-  A4();
-  P1();
-  gB();
-  ((CP = r(JA(), 1)), (xbK = r(JA(), 1)));
+  Fk1 = r(XA(), 1);
 });

@@@ function 'XR7' (was 'Gm7') — structural (56.6%)
--- pretty-v2.1.19.js:372895
+++ pretty-v2.1.20.js:340011
@@ -1,5 +1,5 @@
 function Gm7(A) {
-  let K = a(23),
+  let K = s(29),
     {
       message: q,
       messages: Y,
@@ -45,34 +45,27 @@
   else W = K[9];
   let D = W,
     j;
-  if (K[10] !== D)
-    ((j =
-      D &&
-      Kv.createElement(
-        I,
-        { marginTop: -2 },
-        Kv.createElement(
-          f,
-          { dimColor: !0 },
-          "  ⎿  ",
-          "Auto-allowed by bash classifier · matched",
-          " ",
-          `"${D}"`,
-        ),
-      )),
-      (K[10] = D),
-      (K[11] = j));
+  if (K[10] !== z) ((M = OR7(z)), (K[10] = z), (K[11] = M));
   else j = K[11];
+  let j = M,
+    P;
+  if (K[12] !== D || K[13] !== X)
+    ((P = !1), (K[12] = D), (K[13] = X), (K[14] = P));
+  else P = K[14];
   let M;
-  if (K[12] !== G || K[13] !== j || K[14] !== $)
-    ((M = Kv.createElement(I, { flexDirection: "column", width: $ }, G, j)),
-      (K[12] = G),
-      (K[13] = j),
-      (K[14] = $),
-      (K[15] = M));
-  else M = K[15];
+  if (K[15] !== j) ((V = !1), (K[15] = j), (K[16] = V));
+  else V = K[16];
+  let N;
+  if (K[17] !== G || K[18] !== P || K[19] !== V || K[20] !== $)
+    ((N = Ep.createElement(I, { flexDirection: "column", width: $ }, G, P, V)),
+      (K[17] = G),
+      (K[18] = P),
+      (K[19] = V),
+      (K[20] = $),
+      (K[21] = N));
+  else N = K[21];
   let P;
-  if (K[16] !== Y || K[17] !== z || K[18] !== O)
+  if (K[22] !== Y || K[23] !== z || K[24] !== X)
     ((P = Kv.createElement(
       wqA,
       null,
@@ -83,17 +76,17 @@
         verbose: O,
       }),
     )),
-      (K[16] = Y),
-      (K[17] = z),
-      (K[18] = O),
-      (K[19] = P));
-  else P = K[19];
+      (K[22] = Y),
+      (K[23] = z),
+      (K[24] = X),
+      (K[25] = T));
+  else T = K[25];
   let V;
-  if (K[20] !== M || K[21] !== P)
+  if (K[26] !== N || K[27] !== T)
     ((V = Kv.createElement(I, { flexDirection: "column" }, M, P)),
-      (K[20] = M),
-      (K[21] = P),
-      (K[22] = V));
-  else V = K[22];
+      (K[26] = N),
+      (K[27] = T),
+      (K[28] = k));
+  else k = K[28];
   return V;
 }

@@@ function 'bM7' (was 'PYK') — structural (56.6%)
--- pretty-v2.1.19.js:466009
+++ pretty-v2.1.20.js:315929
@@ -11,21 +11,16 @@
       W = setTimeout(() => {
         G.abort();
       }, Z),
-      { signal: D, cleanup: j } = $L(z, G.signal),
-      M = [..._, Df({ content: "{" })];
+      { signal: D, cleanup: M } = FC(z, G.signal);
     try {
       let P = await ls({
         messages: M,
         systemPrompt: [
           `You are evaluating a hook in Claude Code.
 
-CRITICAL: You MUST return ONLY valid JSON with no other text, explanation, or commentary before or after the JSON. Do not include any markdown code blocks, thinking, or additional text.
-
-Your response must be a single JSON object matching one of the following schemas:
+Your response must be a JSON object matching one of the following schemas:
 1. If the condition is met, return: {"ok": true}
-2. If the condition is not met, return: {"ok": false, "reason": "Reason for why it is not met"}
-
-Return the JSON object directly with no preamble or explanation.`,
+2. If the condition is not met, return: {"ok": false, "reason": "Reason for why it is not met"}`,
         ],
         maxThinkingTokens: 0,
         tools: w.options.tools,
@@ -42,6 +37,18 @@
           querySource: "hook_prompt",
           mcpTools: [],
           agentId: w.agentId,
+          outputFormat: {
+            type: "json_schema",
+            schema: {
+              type: "object",
+              properties: {
+                ok: { type: "boolean" },
+                reason: { type: "string" },
+              },
+              required: ["ok"],
+              additionalProperties: !1,
+            },
+          },
         },
       });
       (clearTimeout(W), j());
@@ -50,7 +57,7 @@
         .map((R) => R.text)
         .join("");
       w.setResponseLength((R) => R + V.length);
-      let N = ("{" + V).trim();
+      let V = P.trim();
       h(`Hooks: Model response: ${N}`);
       let T = S9(N);
       if (!T)

@@@ function 'kFK' (was 'GbK') — structural (56.5%)
--- pretty-v2.1.19.js:570305
+++ pretty-v2.1.20.js:574371
@@ -1,6 +1,6 @@
 async function GbK() {
   (n("tengu_update_check", {}),
-    s7(`Current version: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.19", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-23T21:13:41Z" }.VERSION}
+    E7(`Current version: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION}
 `));
   let A = hq()?.autoUpdatesChannel ?? "latest";
   (s7(`Checking for updates to ${A} version...
@@ -92,16 +92,16 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.19",
+            VERSION: "2.1.20",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-01-23T21:13:41Z",
+            BUILD_TIME: "2026-01-27T00:38:42Z",
           }.VERSION,
           $,
           { loose: !0 },
         )
       )
-        (s7(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.19", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-23T21:13:41Z" }.VERSION} → ${$}
+        (E7(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION} → ${$}
 `),
           s7(`
 `),
@@ -127,16 +127,16 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.19",
+            VERSION: "2.1.20",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-01-23T21:13:41Z",
+            BUILD_TIME: "2026-01-27T00:38:42Z",
           }.VERSION,
           $,
           { loose: !0 },
         )
       )
-        (s7(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.19", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-23T21:13:41Z" }.VERSION} → ${$}
+        (E7(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION} → ${$}
 `),
           s7(`
 `),
@@ -150,6 +150,41 @@
       else
         s7(`Claude is up to date!
 `);
+    } else if (X === "apk") {
+      E7(`Claude is managed by apk.
+`);
+      let $ = await Od(A);
+      if (
+        $ &&
+        !mk1.gte(
+          {
+            ISSUES_EXPLAINER:
+              "report the issue at https://github.com/anthropics/claude-code/issues",
+            PACKAGE_URL: "@anthropic-ai/claude-code",
+            README_URL: "https://code.claude.com/docs/en/overview",
+            VERSION: "2.1.20",
+            FEEDBACK_CHANNEL:
+              "https://github.com/anthropics/claude-code/issues",
+            BUILD_TIME: "2026-01-27T00:38:42Z",
+          }.VERSION,
+          $,
+          { loose: !0 },
+        )
+      )
+        (E7(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION} → ${$}
+`),
+          E7(`
+`),
+          E7(`To update, run:
+`),
+          E7(
+            O1.bold("  apk upgrade claude-code") +
+              `
+`,
+          ));
+      else
+        E7(`Claude is up to date!
+`);
     } else
       (s7(`Claude is managed by a package manager.
 `),
@@ -218,14 +253,14 @@
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.19",
+          VERSION: "2.1.20",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-01-23T21:13:41Z",
+          BUILD_TIME: "2026-01-27T00:38:42Z",
         }.VERSION
       )
         s7(
           X1.green(
-            `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.19", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-23T21:13:41Z" }.VERSION})`,
+            `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION})`,
           ) +
             `
 `,
@@ -233,7 +268,7 @@
       else
         s7(
           X1.green(
-            `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.19", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-23T21:13:41Z" }.VERSION} to version ${O.latestVersion}`,
+            `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION} to version ${X.latestVersion}`,
           ) +
             `
 `,
@@ -255,10 +290,10 @@
   if (q.installMethod !== "native") await eQA();
   (h("update: Checking npm registry for latest version"),
     h(
-      `update: Package URL: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.19", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-23T21:13:41Z" }.PACKAGE_URL}`,
+      `update: Package URL: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.PACKAGE_URL}`,
     ));
   let Y = A === "stable" ? "stable" : "latest",
-    z = `npm view ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.19", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-23T21:13:41Z" }.PACKAGE_URL}@${Y} version`;
+    z = `npm view ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.PACKAGE_URL}@${Y} version`;
   h(`update: Running: ${z}`);
   let w = await _t(A);
   if ((h(`update: Latest version from npm: ${w || "FAILED"}`), !w)) {
@@ -286,18 +321,18 @@
           "report the issue at https://github.com/anthropics/claude-code/issues",
         PACKAGE_URL: "@anthropic-ai/claude-code",
         README_URL: "https://code.claude.com/docs/en/overview",
-        VERSION: "2.1.19",
+        VERSION: "2.1.20",
         FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-        BUILD_TIME: "2026-01-23T21:13:41Z",
+        BUILD_TIME: "2026-01-27T00:38:42Z",
       }.PACKAGE_URL &&
         !{
           ISSUES_EXPLAINER:
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.19",
+          VERSION: "2.1.20",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-01-23T21:13:41Z",
+          BUILD_TIME: "2026-01-27T00:38:42Z",
         }.PACKAGE_URL.startsWith("@anthropic"))
     )
       process.stderr.write(`  • Internal/development build not published to npm
@@ -316,9 +351,9 @@
           "report the issue at https://github.com/anthropics/claude-code/issues",
         PACKAGE_URL: "@anthropic-ai/claude-code",
         README_URL: "https://code.claude.com/docs/en/overview",
-        VERSION: "2.1.19",
+        VERSION: "2.1.20",
         FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-        BUILD_TIME: "2026-01-23T21:13:41Z",
+        BUILD_TIME: "2026-01-27T00:38:42Z",
       }.PACKAGE_URL || "@anthropic-ai/claude-code";
     (process.stderr.write(`  • Manually check: npm view ${O} version
 `),
@@ -333,20 +368,20 @@
         "report the issue at https://github.com/anthropics/claude-code/issues",
       PACKAGE_URL: "@anthropic-ai/claude-code",
       README_URL: "https://code.claude.com/docs/en/overview",
-      VERSION: "2.1.19",
+      VERSION: "2.1.20",
       FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-      BUILD_TIME: "2026-01-23T21:13:41Z",
+      BUILD_TIME: "2026-01-27T00:38:42Z",
     }.VERSION
   )
     (s7(
       X1.green(
-        `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.19", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-23T21:13:41Z" }.VERSION})`,
+        `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION})`,
       ) +
         `
 `,
     ),
       await o5(0));
-  (s7(`New version available: ${w} (current: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.19", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-23T21:13:41Z" }.VERSION})
+  (E7(`New version available: ${w} (current: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION})
 `),
     s7(`Installing update...
 `));
@@ -393,7 +428,7 @@
     case "success":
       s7(
         X1.green(
-          `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.19", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-23T21:13:41Z" }.VERSION} to version ${w}`,
+          `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION} to version ${w}`,
         ) +
           `
 `,
@@ -408,7 +443,7 @@
         (process.stderr.write(`Try manually updating with:
 `),
           process.stderr
-            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.19", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-23T21:13:41Z" }.PACKAGE_URL}
+            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.PACKAGE_URL}
 `));
       else
         (process.stderr.write(`Try running with sudo or fix npm permissions
@@ -427,7 +462,7 @@
         (process.stderr.write(`Try manually updating with:
 `),
           process.stderr
-            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.19", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-23T21:13:41Z" }.PACKAGE_URL}
+            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.PACKAGE_URL}
 `));
       else
         process.stderr

@@@ variable 'W_' (was '_W') — structural (56.4%)
--- pretty-v2.1.19.js:420954
+++ pretty-v2.1.20.js:448699
@@ -41,6 +41,22 @@
   st7 = ["default"];
   ((jj1 = new Set([yDA, mZ.name, $j1, l5, _X, Kj1, ...(rt7 ? [rt7] : [])])),
     (S22 = new Set([...jj1])),
-    (h22 = new Set([C5, gE, BF, ow, z0, uH, I7, c5, x2, F_, hZ, aG, UG, a5A])),
-    (tt7 = new Set([a5A, Ao, Gj1, Wj1, XU, l5])));
+    (qv2 = new Set([
+      K5,
+      QE,
+      KQ,
+      dz,
+      q0,
+      bH,
+      k7,
+      n5,
+      cz,
+      JD,
+      cZ,
+      wW,
+      oG,
+      yFA,
+      tQA,
+    ])),
+    (l2K = new Set([yFA, tQA, Ro, bV1, xV1, SU, j5])));
 });

@@@ variable 'n_' (was 'sW') — structural (56.2%)
--- pretty-v2.1.19.js:89344
+++ pretty-v2.1.20.js:89514
@@ -1,5 +1,5 @@
 var sW = C(() => {
   T7();
   TE8();
-  $tA = N7.enum(yE);
+  ((jL8 = T7.enum(wi)), (PL8 = T7.enum(n1A)));
 });

@@@ variable 'Mf' (was 'QT') — structural (56.1%)
--- pretty-v2.1.19.js:313668
+++ pretty-v2.1.20.js:309969
@@ -1,5 +1,6 @@
 var QT = C(() => {
   X5();
   e1();
+  ((C$1 = []), (E$1 = new Set()));
   JVY = new Set(["task-notification"]);
 });

@@@ function 'ia2' (was 'DF2') — structural (55.8%)
--- pretty-v2.1.19.js:534224
+++ pretty-v2.1.20.js:538993
@@ -3,18 +3,22 @@
     K = O9A(),
     q = Sc.errors(),
     Y = Sc.baseLogs(),
-    z = eMK(q, K, !1);
+    z = await VEK(q, K, !1);
   try {
-    if (A.existsSync(Y)) {
-      let H = A.readdirSync(Y)
-        .filter((J) => J.isDirectory() && J.name.startsWith("mcp-logs-"))
-        .map((J) => af(Y, J.name));
-      for (let J of H) {
-        z = GF2(z, eMK(J, K, !0));
-        try {
-          if (A.isDirEmptySync(J)) A.rmdirSync(J);
-        } catch {}
-      }
+    let w;
+    try {
+      w = await A.readdir(Y);
+    } catch {
+      return z;
+    }
+    let H = w
+      .filter((J) => J.isDirectory() && J.name.startsWith("mcp-logs-"))
+      .map((J) => NP(Y, J.name));
+    for (let J of H) {
+      z = ca2(z, await VEK(J, K, !0));
+      try {
+        await A.rmdir(J);
+      } catch {}
     }
   } catch (w) {
     if (w instanceof Error && "code" in w && w.code !== "ENOENT") qA(w);

@@@ function 'Lk' (was 'Yx') — structural (55.6%)
--- pretty-v2.1.19.js:178412
+++ pretty-v2.1.20.js:181395
@@ -1,3 +1,3 @@
 function Yx() {
-  return lK("tengu_keybinding_customization", !1);
+  return i4("tengu_keybinding_customization_release", !1);
 }

@@@ function 'U8K' (was '$4K') — structural (55.6%)
--- pretty-v2.1.19.js:435868
+++ pretty-v2.1.20.js:413623
@@ -22,92 +22,6 @@
 - A team file at \`~/.claude/teams/{team-name}.json\`
 - A corresponding task list directory at \`~/.claude/tasks/{team-name}/\`
 
-### approvePlan - Approve a Teammate's Plan
-
-When a teammate with \`plan_mode_required\` calls ExitPlanMode, they send you a plan approval request as a JSON message with \`type: "plan_approval_request"\`. Use \`approvePlan\` to approve their plan:
-- **target_agent_id**: Use the \`from\` field from the plan_approval_request message (REQUIRED)
-- **request_id**: Use the \`requestId\` field from the plan_approval_request message (REQUIRED)
-
-Example: If you receive a message like \`{"type":"plan_approval_request","from":"architect","requestId":"abc-123",...}\`, use:
-\`\`\`
-{
-  "operation": "approvePlan",
-  "target_agent_id": "architect",
-  "request_id": "abc-123"
-}
-\`\`\`
-
-After approval, the teammate will automatically exit plan mode and can proceed with implementation.
-
-### rejectPlan - Reject a Teammate's Plan
-
-Use \`rejectPlan\` to reject a plan and provide feedback:
-- **target_agent_id**: Use the \`from\` field from the plan_approval_request message (REQUIRED)
-- **request_id**: Use the \`requestId\` field from the plan_approval_request message (REQUIRED)
-- **feedback**: (Optional) Explanation of why the plan was rejected and what changes are needed
-
-\`\`\`
-{
-  "operation": "rejectPlan",
-  "target_agent_id": "architect",
-  "request_id": "abc-123",
-  "feedback": "Please add error handling for the API calls"
-}
-\`\`\`
-
-The teammate will receive the rejection with your feedback and can revise their plan.
-
-### requestShutdown - Request a Teammate to Shut Down (Leader Only)
-
-Use \`requestShutdown\` to ask a teammate to gracefully shut down:
-- **target_agent_id**: Name of the teammate to shut down (REQUIRED)
-- **reason**: (Optional) Explanation of why shutdown is requested
-
-\`\`\`
-{
-  "operation": "requestShutdown",
-  "target_agent_id": "researcher",
-  "reason": "Task complete, wrapping up the session"
-}
-\`\`\`
-
-The teammate will receive a shutdown request and can either approve (exit) or reject (continue working).
-
-### approveShutdown - Accept Shutdown Request (Teammate Only)
-
-When you receive a shutdown request as a JSON message with \`type: "shutdown_request"\`, you **MUST** call the Teammate tool with \`approveShutdown\` operation to accept and exit gracefully. Do NOT just acknowledge the request in text - you must actually call the tool.
-
-- **request_id**: The \`requestId\` from the shutdown_request message (REQUIRED)
-
-**IMPORTANT**: Extract the \`requestId\` from the JSON message and pass it to the tool. Simply saying "I'll shut down" is not enough - you must call the tool.
-
-Example: If you receive a message like \`{"type":"shutdown_request","from":"team-lead","requestId":"abc-123",...}\`, you MUST call:
-\`\`\`
-{
-  "operation": "approveShutdown",
-  "request_id": "abc-123"
-}
-\`\`\`
-
-This will send confirmation to the leader and terminate your process.
-
-### rejectShutdown - Decline Shutdown Request (Teammate Only)
-
-Use \`rejectShutdown\` to decline a shutdown request and continue working. You **MUST** call this tool - do NOT just say "I'm not ready" in text.
-
-- **request_id**: The \`requestId\` from the shutdown_request message (REQUIRED)
-- **reason**: Explanation of why you need to continue working (REQUIRED)
-
-\`\`\`
-{
-  "operation": "rejectShutdown",
-  "request_id": "abc-123",
-  "reason": "Still working on task #3, need 5 more minutes"
-}
-\`\`\`
-
-The leader will receive your rejection with the reason.
-
 ### discoverTeams - Discover Available Teams
 
 List teams that are available to join. Returns teams from \`~/.claude/teams/\` that you are not already a member of.
@@ -195,61 +109,9 @@
 - Removes the task directory (\`~/.claude/tasks/{team-name}/\`)
 - Clears team context from the current session
 
-**IMPORTANT**: \`cleanup\` will fail if the team still has active members. Use \`requestShutdown\` to gracefully terminate teammates first, then call \`cleanup\` after all teammates have approved shutdown.
+**IMPORTANT**: \`cleanup\` will fail if the team still has active members. Gracefully terminate teammates first, then call \`cleanup\` after all teammates have shut down.
 
 Use this when all teammates have finished their work and you want to clean up the team resources. The team name is automatically determined from the \`CLAUDE_CODE_TEAM_NAME\` environment variable.
-
-### write - Send Message to ONE Teammate
-
-Use \`write\` to send a message to a **single specific teammate**. You MUST specify the recipient.
-
-**IMPORTANT for teammates**: Your plain text output is NOT visible to the team lead or other teammates. To communicate with anyone on your team, you **MUST** call the Teammate tool with the \`write\` operation. Just typing a response or acknowledgment in text is not enough - you must use the tool.
-
-\`\`\`
-{
-  "operation": "write",
-  "target_agent_id": "recipient-agent-id",
-  "value": "Your message here"
-}
-\`\`\`
-
-- **target_agent_id**: The name of the teammate to message (required)
-- **value**: The message content (required)
-
-### broadcast - Send Message to ALL Teammates (USE SPARINGLY)
-
-Use \`broadcast\` to send the **same message to everyone** on the team at once.
-
-**WARNING: Broadcasting is expensive.** Each broadcast sends a separate message to every teammate, which means:
-- N teammates = N separate message deliveries
-- Each delivery consumes API resources
-- Costs scale linearly with team size
-
-\`\`\`
-{
-  "operation": "broadcast",
-  "name": "your-agent-name",
-  "value": "Message to send to all teammates",
-}
-\`\`\`
-
-- **value**: The message content to broadcast (required)
-- **name**: Your name as sender - use your own agent name (required if CLAUDE_CODE_AGENT_NAME is not set)
-- **key**: (Optional) A key/label for the message
-- **team_name**: (Optional) Team name - automatically determined from team context
-
-**CRITICAL: Use broadcast only when absolutely necessary.** Valid use cases:
-- Critical issues requiring immediate team-wide attention (e.g., "stop all work, blocking bug found")
-- Major announcements that genuinely affect every teammate equally
-
-**Default to \`write\` instead of \`broadcast\`.** Use \`write\` for:
-- Responding to a single teammate
-- Normal back-and-forth communication
-- Following up on a task with one person
-- Sharing findings relevant to only some teammates
-- Any message that doesn't require everyone's attention
-
-**Rule of thumb**: If you're unsure whether to broadcast, use \`write\` to specific teammates instead. Ask yourself: "Does every single teammate absolutely need to see this exact message right now?" If not, use \`write\`.
 
 ## Team Workflow

@@@ class 'HfK' (was 'iGK') — structural (55.1%)
--- pretty-v2.1.19.js:519119
+++ pretty-v2.1.20.js:523361
@@ -10,6 +10,7 @@
   reconnectDelay = 1000;
   reconnectTimer = null;
   context;
+  disableAutoReconnect = !1;
   constructor(A) {
     this.context = A;
   }
@@ -20,7 +21,7 @@
       return;
     }
     (this.closeSocket(), (this.connecting = !0));
-    let q = this.context.socketPath;
+    let q = this.context.getSocketPath?.() ?? this.context.socketPath;
     K.info(`[${A}] Attempting to connect to: ${q}`);
     try {
       await this.validateSocketSecurity(q);
@@ -28,13 +29,20 @@
       ((this.connecting = !1), K.info(`[${A}] Security validation failed:`, Y));
       return;
     }
-    ((this.socket = Nb2(q)),
-      this.socket.on("connect", () => {
-        ((this.connected = !0),
-          (this.connecting = !1),
-          (this.reconnectAttempts = 0),
-          K.info(`[${A}] Successfully connected to bridge server`));
-      }),
+    this.socket = Lc2(q);
+    let Y = setTimeout(() => {
+      if (!this.connected)
+        (K.info(`[${A}] Connection attempt timed out after 5000ms`),
+          this.closeSocket(),
+          this.scheduleReconnect());
+    }, 5000);
+    (this.socket.on("connect", () => {
+      (clearTimeout(Y),
+        (this.connected = !0),
+        (this.connecting = !1),
+        (this.reconnectAttempts = 0),
+        K.info(`[${A}] Successfully connected to bridge server`));
+    }),
       this.socket.on("data", (Y) => {
         this.responseBuffer = Buffer.concat([this.responseBuffer, Y]);
         while (this.responseBuffer.length >= 4) {
@@ -61,40 +69,60 @@
       }),
       this.socket.on("error", (Y) => {
         if (
-          (K.info(`[${A}] Socket error:`, Y),
+          (clearTimeout(Y),
+          K.info(`[${A}] Socket error (code: ${z.code}):`, z),
           (this.connected = !1),
           (this.connecting = !1),
-          Y.code && ["ECONNREFUSED", "ECONNRESET", "EPIPE"].includes(Y.code))
+          z.code &&
+            [
+              "ECONNREFUSED",
+              "ECONNRESET",
+              "EPIPE",
+              "ENOENT",
+              "EOPNOTSUPP",
+              "ECONNABORTED",
+            ].includes(z.code))
         )
           this.scheduleReconnect();
       }),
       this.socket.on("close", () => {
-        ((this.connected = !1),
+        (clearTimeout(Y),
+          (this.connected = !1),
           (this.connecting = !1),
           this.scheduleReconnect());
       }));
   }
   scheduleReconnect() {
     let { serverName: A, logger: K } = this.context;
+    if (this.disableAutoReconnect) return;
     if (this.reconnectTimer) {
       K.info(`[${A}] Reconnect already scheduled, skipping`);
       return;
     }
-    if (this.reconnectAttempts >= this.maxReconnectAttempts) {
-      (K.info(`[${A}] Max reconnection attempts reached`), this.cleanup());
+    this.reconnectAttempts++;
+    let q = 100;
+    if (this.reconnectAttempts > q) {
+      (K.info(
+        `[${A}] Giving up after ${q} attempts. Will retry on next tool call.`,
+      ),
+        (this.reconnectAttempts = 0));
       return;
     }
-    this.reconnectAttempts++;
     let q = Math.min(
       this.reconnectDelay * Math.pow(1.5, this.reconnectAttempts - 1),
       30000,
     );
-    (K.info(
-      `[${A}] Reconnecting in ${Math.round(q)}ms (attempt ${this.reconnectAttempts})`,
-    ),
-      (this.reconnectTimer = setTimeout(() => {
-        ((this.reconnectTimer = null), this.connect());
-      }, q)));
+    if (this.reconnectAttempts <= this.maxReconnectAttempts)
+      K.info(
+        `[${A}] Reconnecting in ${Math.round(Y)}ms (attempt ${this.reconnectAttempts})`,
+      );
+    else if (this.reconnectAttempts % 10 === 0)
+      K.info(
+        `[${A}] Still polling for native host (attempt ${this.reconnectAttempts})`,
+      );
+    this.reconnectTimer = setTimeout(() => {
+      ((this.reconnectTimer = null), this.connect());
+    }, Y);
   }
   handleResponse(A) {
     if (this.responseCallback) {
@@ -110,20 +138,21 @@
     if (this.connected && this.socket) return !0;
     if (!this.socket && !this.connecting) await this.connect();
     return new Promise((K, q) => {
-      let Y = setTimeout(() => {
+      let Y = null,
+        z = setTimeout(() => {
+          if (Y) clearTimeout(Y);
           q(new K9A(`[${A}] Connection attempt timed out after 5000ms`));
         }, 5000),
         z = () => {
           if (this.connected) (clearTimeout(Y), K(!0));
-          else setTimeout(z, 100);
+          else Y = setTimeout(w, 500);
         };
       z();
     });
   }
   async sendRequest(A, K = 30000) {
     let { serverName: q } = this.context;
-    if (!this.socket)
-      throw new K9A(`[${q}] Cannot send request: not connected`);
+    if (!this.socket) throw new nS(`[${q}] Cannot send request: not connected`);
     let Y = this.socket;
     return new Promise((z, w) => {
       let H = setTimeout(() => {
@@ -190,13 +219,32 @@
     let { serverName: K, logger: q } = this.context;
     if (fb2() === "win32") return;
     try {
+      let Y = yc2(A);
+      if ((Y.split("/").pop() || "").startsWith("claude-mcp-browser-bridge-"))
+        try {
+          let X = await wfK.stat(Y);
+          if (X.isDirectory()) {
+            let $ = X.mode & 511;
+            if ($ !== 448)
+              throw Error(
+                `[${K}] Insecure socket directory permissions: ${$.toString(8)} (expected 0700). Directory may have been tampered with.`,
+              );
+            let _ = process.getuid?.();
+            if (_ !== void 0 && X.uid !== _)
+              throw Error(
+                `Socket directory not owned by current user (uid: ${_}, dir uid: ${X.uid}). Potential security risk.`,
+              );
+          }
+        } catch (X) {
+          if (X.code !== "ENOENT") throw X;
+        }
       let Y = await Vb2.stat(A);
       if (!Y.isSocket())
         throw Error(`[${K}] Path exists but it's not a socket: ${A}`);
       let z = Y.mode & 511;
       if (z !== 384)
         throw Error(
-          `[${K}] Insecure socket permissions: ${z.toString(8)} (expected 0600). Socket may have been tampered with. `,
+          `[${K}] Insecure socket permissions: ${J.toString(8)} (expected 0600). Socket may have been tampered with.`,
         );
       let w = process.getuid?.();
       if (w !== void 0 && Y.uid !== w)

@@@ function 'vkK' (was 'ePK') — structural (55.1%)
--- pretty-v2.1.19.js:537474
+++ pretty-v2.1.20.js:542641
@@ -18,7 +18,5 @@
         : `${X1.bold(A.hookName)} hook`;
     case "asyncAgent":
       return A.reason;
-    case "classifier":
-      return `${X1.bold(A.classifier)} classifier: ${A.reason}`;
   }
 }

@@@ function 'jn6' (was 'fi2') — structural (55.0%)
--- pretty-v2.1.19.js:565689
+++ pretty-v2.1.20.js:2393
@@ -1,3 +1,3 @@
 function fi2(A) {
-  return A.name;
+  L6.additionalDirectoriesForClaudeMd = A;
 }

@@@ variable 'SEK' (was 'Md7') — structural (54.8%)
--- pretty-v2.1.19.js:392063
+++ pretty-v2.1.20.js:539811
@@ -1,12 +1,141 @@
 var Md7 = C(() => {
   H0();
-  jd7 = `Performs exact string replacements in files. 
+  Pe();
+  RU();
+  B1();
+  _s2 = `# Update Config Skill
 
-Usage:
-- You must use your \`${C5}\` tool at least once in the conversation before editing. This tool will error if you attempt an edit without reading the file. 
-- When editing text from Read tool output, ensure you preserve the exact indentation (tabs/spaces) as it appears AFTER the line number prefix. The line number prefix format is: spaces + line number + tab. Everything after that tab is the actual file content to match. Never include any part of the line number prefix in the old_string or new_string.
-- ALWAYS prefer editing existing files in the codebase. NEVER write new files unless explicitly required.
-- Only use emojis if the user explicitly requests it. Avoid adding emojis to files unless asked.
-- The edit will FAIL if \`old_string\` is not unique in the file. Either provide a larger string with more surrounding context to make it unique or use \`replace_all\` to change every instance of \`old_string\`. 
-- Use \`replace_all\` for replacing and renaming strings across the file. This parameter is useful if you want to rename a variable for instance.`;
+Modify Claude Code configuration by updating settings.json files.
+
+## When Hooks Are Required (Not Memory)
+
+If the user wants something to happen automatically in response to an EVENT, they need a **hook** configured in settings.json. Memory/preferences cannot trigger automated actions.
+
+**These require hooks:**
+- "Before compacting, ask me what to preserve" → PreCompact hook
+- "After writing files, run prettier" → PostToolUse hook with Write|Edit matcher
+- "When I run bash commands, log them" → PreToolUse hook with Bash matcher
+- "Always run tests after code changes" → PostToolUse hook
+
+**Hook events:** PreToolUse, PostToolUse, PreCompact, Stop, Notification, SessionStart
+
+## CRITICAL: Read Before Write
+
+**Always read the existing settings file before making changes.** Merge new settings with existing ones - never replace the entire file.
+
+## CRITICAL: Use AskUserQuestion for Ambiguity
+
+When the user's request is ambiguous, use AskUserQuestion to clarify:
+- Which settings file to modify (user/project/local)
+- Whether to add to existing arrays or replace them
+- Specific values when multiple options exist
+
+## Decision: Config Tool vs Direct Edit
+
+**Use the Config tool** for these simple settings:
+- \`theme\`, \`editorMode\`, \`verbose\`, \`model\`
+- \`language\`, \`alwaysThinkingEnabled\`
+- \`permissions.defaultMode\`
+
+**Edit settings.json directly** for:
+- Hooks (PreToolUse, PostToolUse, etc.)
+- Complex permission rules (allow/deny arrays)
+- Environment variables
+- MCP server configuration
+- Plugin configuration
+
+## Workflow
+
+1. **Clarify intent** - Ask if the request is ambiguous
+2. **Read existing file** - Use Read tool on the target settings file
+3. **Merge carefully** - Preserve existing settings, especially arrays
+4. **Edit file** - Use Edit tool (if file doesn't exist, ask user to create it first)
+5. **Confirm** - Tell user what was changed
+
+## Merging Arrays (Important!)
+
+When adding to permission arrays or hook arrays, **merge with existing**, don't replace:
+
+**WRONG** (replaces existing permissions):
+\`\`\`json
+{ "permissions": { "allow": ["Bash(npm:*)"] } }
+\`\`\`
+
+**RIGHT** (preserves existing + adds new):
+\`\`\`json
+{
+  "permissions": {
+    "allow": [
+      "Bash(git:*)",      // existing
+      "Edit(.claude)",    // existing
+      "Bash(npm:*)"       // new
+    ]
+  }
+}
+\`\`\`
+
+${Xs2}
+
+${$s2}
+
+## Example Workflows
+
+### Adding a Hook
+
+User: "Format my code after Claude writes it"
+
+1. **Clarify**: Which formatter? (prettier, gofmt, etc.)
+2. **Read**: \`.claude/settings.json\` (or create if missing)
+3. **Merge**: Add to existing hooks, don't replace
+4. **Result**:
+\`\`\`json
+{
+  "hooks": {
+    "PostToolUse": [{
+      "matcher": "Write|Edit",
+      "hooks": [{
+        "type": "command",
+        "command": "jq -r '.tool_response.filePath // .tool_input.file_path' | xargs prettier --write 2>/dev/null || true"
+      }]
+    }]
+  }
+}
+\`\`\`
+
+### Adding Permissions
+
+User: "Allow npm commands without prompting"
+
+1. **Read**: Existing permissions
+2. **Merge**: Add \`Bash(npm:*)\` to allow array
+3. **Result**: Combined with existing allows
+
+### Environment Variables
+
+User: "Set DEBUG=true"
+
+1. **Decide**: User settings (global) or project settings?
+2. **Read**: Target file
+3. **Merge**: Add to env object
+\`\`\`json
+{ "env": { "DEBUG": "true" } }
+\`\`\`
+
+## Common Mistakes to Avoid
+
+1. **Replacing instead of merging** - Always preserve existing settings
+2. **Wrong file** - Ask user if scope is unclear
+3. **Invalid JSON** - Validate syntax after changes
+4. **Forgetting to read first** - Always read before write
+
+## Troubleshooting Hooks
+
+If a hook isn't running:
+1. **Check the settings file** - Read ~/.claude/settings.json or .claude/settings.json
+2. **Verify JSON syntax** - Invalid JSON silently fails
+3. **Check the matcher** - Does it match the tool name? (e.g., "Bash", "Write", "Edit")
+4. **Check hook type** - Is it "command", "prompt", or "agent"?
+5. **Test the command** - Run the hook command manually to see if it works
+6. **Use --debug** - Run \`claude --debug\` to see hook execution logs
+`;
 });

@@@ function 'JT1' (was 'Gf1') — structural (54.2%)
--- pretty-v2.1.19.js:481842
+++ pretty-v2.1.20.js:485249
@@ -1,5 +1,5 @@
 function Gf1(A) {
-  let K = a(82),
+  let K = s(84),
     { dimColor: q, fixedWidth: Y, gap: z, paddingX: w } = A,
     H = w5("app:toggleTranscript", "Global", "ctrl+o"),
     J;
@@ -31,62 +31,62 @@
   if (K[10] !== T) ((k = ZMA(T)), (K[10] = T), (K[11] = k));
   else k = K[11];
   let R = k,
+    b = FK("chat:externalEditor", "Chat", "ctrl+g"),
     x;
-  if (K[12] === Symbol.for("react.memo_cache_sentinel"))
-    ((x = P8()), (K[12] = x));
-  else x = K[12];
+  if (K[12] !== b) ((S = J9A(b)), (K[12] = b), (K[13] = S));
+  else S = K[13];
   let S = x,
     g = Y ? 24 : void 0,
     b;
-  if (K[13] !== q)
+  if (K[14] !== q)
     ((b = V4.createElement(
       I,
       null,
       V4.createElement(f, { dimColor: q }, "! for bash mode"),
     )),
-      (K[13] = q),
-      (K[14] = b));
-  else b = K[14];
+      (K[14] = q),
+      (K[15] = F));
+  else F = K[15];
   let Q;
-  if (K[15] !== q)
+  if (K[16] !== q)
     ((Q = V4.createElement(
       I,
       null,
       V4.createElement(f, { dimColor: q }, "/ for commands"),
     )),
-      (K[15] = q),
-      (K[16] = Q));
-  else Q = K[16];
+      (K[16] = q),
+      (K[17] = Q));
+  else Q = K[17];
   let F;
-  if (K[17] !== q)
+  if (K[18] !== q)
     ((F = V4.createElement(
       I,
       null,
       V4.createElement(f, { dimColor: q }, "@ for file paths"),
     )),
-      (K[17] = q),
-      (K[18] = F));
-  else F = K[18];
+      (K[18] = q),
+      (K[19] = u));
+  else u = K[19];
   let B, d;
-  if (K[19] !== q)
+  if (K[20] !== q)
     ((B = V4.createElement(
       I,
       null,
       V4.createElement(f, { dimColor: q }, "& for background"),
     )),
       (d = !1),
-      (K[19] = q),
       (K[20] = B),
-      (K[21] = d));
-  else ((B = K[20]), (d = K[21]));
+      (K[21] = d),
+      (K[22] = a));
+  else ((d = K[21]), (a = K[22]));
   let o;
   if (
-    K[22] !== g ||
     K[23] !== b ||
     K[24] !== Q ||
     K[25] !== F ||
     K[26] !== B ||
-    K[27] !== d
+    K[27] !== d ||
+    K[28] !== a
   )
     ((o = V4.createElement(
       I,
@@ -97,76 +97,76 @@
       B,
       d,
     )),
-      (K[22] = g),
       (K[23] = b),
       (K[24] = Q),
       (K[25] = F),
       (K[26] = B),
       (K[27] = d),
-      (K[28] = o));
-  else o = K[28];
+      (K[28] = a),
+      (K[29] = l));
+  else l = K[29];
   let l = Y ? 35 : void 0,
     e;
-  if (K[29] !== q)
+  if (K[30] !== q)
     ((e = V4.createElement(
       I,
       null,
       V4.createElement(f, { dimColor: q }, "double tap esc to clear input"),
     )),
-      (K[29] = q),
-      (K[30] = e));
-  else e = K[30];
+      (K[30] = q),
+      (K[31] = JA));
+  else JA = K[31];
   let XA;
-  if (K[31] !== N || K[32] !== q)
+  if (K[32] !== N || K[33] !== q)
     ((XA = V4.createElement(
       I,
       null,
       V4.createElement(f, { dimColor: q }, N, " to auto-accept edits"),
     )),
-      (K[31] = N),
       (K[32] = q),
-      (K[33] = XA));
-  else XA = K[33];
+      (K[33] = q),
+      (K[34] = OA));
+  else OA = K[34];
   let GA;
-  if (K[34] !== q || K[35] !== X)
+  if (K[35] !== q || K[36] !== O)
     ((GA = V4.createElement(
       I,
       null,
       V4.createElement(f, { dimColor: q }, X, " for verbose output"),
     )),
-      (K[34] = q),
       (K[35] = X),
-      (K[36] = GA));
-  else GA = K[36];
+      (K[36] = O),
+      (K[37] = HA));
+  else HA = K[37];
   let WA;
-  if (K[37] !== q || K[38] !== _)
+  if (K[38] !== q || K[39] !== _)
     ((WA = V4.createElement(
       I,
       null,
       V4.createElement(f, { dimColor: q }, _, " to show todos"),
     )),
-      (K[37] = q),
       (K[38] = _),
-      (K[39] = WA));
-  else WA = K[39];
-  let ZA;
-  if (K[40] === Symbol.for("react.memo_cache_sentinel"))
-    ((ZA = ewK()), (K[40] = ZA));
+      (K[39] = _),
+      (K[40] = DA));
   else ZA = K[40];
   let t;
-  if (K[41] !== q)
+  if (K[41] === Symbol.for("react.memo_cache_sentinel"))
+    ((o = X_K()), (K[41] = o));
+  else o = K[41];
+  let _A;
+  if (K[42] !== q)
     ((t = V4.createElement(I, null, V4.createElement(f, { dimColor: q }, ZA))),
-      (K[41] = q),
-      (K[42] = t));
-  else t = K[42];
+      (K[42] = q),
+      (K[43] = _A));
+  else _A = K[43];
   let $A;
   if (
-    K[43] !== l ||
     K[44] !== e ||
     K[45] !== XA ||
     K[46] !== GA ||
     K[47] !== WA ||
-    K[48] !== t
+    K[48] !== DA ||
+    K[49] !== _A
   )
     (($A = V4.createElement(
       I,
@@ -177,27 +177,27 @@
       WA,
       t,
     )),
-      (K[43] = l),
       (K[44] = e),
       (K[45] = XA),
       (K[46] = GA),
       (K[47] = WA),
       (K[48] = t),
-      (K[49] = $A));
-  else $A = K[49];
+      (K[49] = _A),
+      (K[50] = PA));
+  else PA = K[50];
   let VA;
-  if (K[50] !== q || K[51] !== W)
+  if (K[51] !== q || K[52] !== W)
     ((VA = V4.createElement(
       I,
       null,
       V4.createElement(f, { dimColor: q }, W, " to undo"),
     )),
-      (K[50] = q),
       (K[51] = W),
-      (K[52] = VA));
-  else VA = K[52];
+      (K[52] = W),
+      (K[53] = jA));
+  else jA = K[53];
   let MA;
-  if (K[53] !== q)
+  if (K[54] !== q)
     ((MA =
       Wq8 &&
       V4.createElement(
@@ -205,47 +205,58 @@
         null,
         V4.createElement(f, { dimColor: q }, "ctrl + z to suspend"),
       )),
-      (K[53] = q),
-      (K[54] = MA));
-  else MA = K[54];
+      (K[54] = q),
+      (K[55] = yA));
+  else yA = K[55];
   let SA;
-  if (K[55] === Symbol.for("react.memo_cache_sentinel"))
-    ((SA = ijA.displayText.replace("+", " + ")), (K[55] = SA));
-  else SA = K[55];
+  if (K[56] === Symbol.for("react.memo_cache_sentinel"))
+    ((bA = njA.displayText.replace("+", " + ")), (K[56] = bA));
+  else bA = K[56];
   let BA;
-  if (K[56] !== q)
+  if (K[57] !== q)
     ((BA = V4.createElement(
       I,
       null,
       V4.createElement(f, { dimColor: q }, SA, " to paste images"),
     )),
-      (K[56] = q),
-      (K[57] = BA));
-  else BA = K[57];
+      (K[57] = q),
+      (K[58] = YA));
+  else YA = K[58];
   let s;
-  if (K[58] !== q || K[59] !== R)
+  if (K[59] !== q || K[60] !== R)
     ((s = V4.createElement(
       I,
       null,
       V4.createElement(f, { dimColor: q }, R, " to switch model"),
     )),
-      (K[58] = q),
       (K[59] = R),
-      (K[60] = s));
-  else s = K[60];
+      (K[60] = R),
+      (K[61] = KA));
+  else KA = K[61];
   let AA;
-  if (K[61] !== q || K[62] !== M)
+  if (K[62] !== q || K[63] !== j)
     ((AA = V4.createElement(
       I,
       null,
       V4.createElement(f, { dimColor: q }, M, " to stash prompt"),
     )),
-      (K[61] = q),
       (K[62] = M),
-      (K[63] = AA));
-  else AA = K[63];
+      (K[63] = j),
+      (K[64] = zA));
+  else zA = K[64];
+  let AA;
+  if (K[65] !== q || K[66] !== B)
+    ((AA = Z7.createElement(
+      I,
+      null,
+      Z7.createElement(f, { dimColor: q }, B, " to edit in $EDITOR"),
+    )),
+      (K[65] = q),
+      (K[66] = B),
+      (K[67] = AA));
+  else AA = K[67];
   let wA;
-  if (K[64] !== q)
+  if (K[68] !== q)
     ((wA =
       Yx() &&
       V4.createElement(
@@ -253,17 +264,18 @@
         null,
         V4.createElement(f, { dimColor: q }, "/keybindings to customize"),
       )),
-      (K[64] = q),
-      (K[65] = wA));
-  else wA = K[65];
+      (K[68] = q),
+      (K[69] = t));
+  else t = K[69];
   let KA;
   if (
-    K[66] !== VA ||
-    K[67] !== MA ||
-    K[68] !== BA ||
-    K[69] !== s ||
     K[70] !== AA ||
-    K[71] !== wA
+    K[71] !== yA ||
+    K[72] !== YA ||
+    K[73] !== KA ||
+    K[74] !== zA ||
+    K[75] !== AA ||
+    K[76] !== t
   )
     ((KA = V4.createElement(
       I,
@@ -274,74 +286,32 @@
       s,
       AA,
       wA,
+      t,
     )),
-      (K[66] = VA),
-      (K[67] = MA),
-      (K[68] = BA),
-      (K[69] = s),
       (K[70] = AA),
       (K[71] = wA),
-      (K[72] = KA));
-  else KA = K[72];
-  let zA;
-  if (K[73] !== q)
-    ((zA =
-      S &&
-      V4.createElement(
-        I,
-        { flexDirection: "column" },
-        V4.createElement(
-          I,
-          null,
-          V4.createElement(f, { dimColor: q, bold: !0 }, "Teammates"),
-        ),
-        V4.createElement(
-          I,
-          null,
-          V4.createElement(
-            f,
-            { dimColor: q },
-            "shift + ↑/↓ to select teammate",
-          ),
-        ),
-        V4.createElement(
-          I,
-          null,
-          V4.createElement(f, { dimColor: q }, "enter to view transcript"),
-        ),
-        V4.createElement(
-          I,
-          null,
-          V4.createElement(f, { dimColor: q }, "select leader to return"),
-        ),
-      )),
+      (K[72] = YA),
       (K[73] = q),
-      (K[74] = zA));
-  else zA = K[74];
+      (K[74] = zA),
+      (K[75] = AA),
+      (K[76] = t),
+      (K[77] = $A));
+  else $A = K[77];
   let HA;
-  if (
-    K[75] !== z ||
-    K[76] !== w ||
-    K[77] !== o ||
-    K[78] !== $A ||
-    K[79] !== KA ||
-    K[80] !== zA
-  )
+  if (K[78] !== z || K[79] !== w || K[80] !== l || K[81] !== PA || K[82] !== $A)
     ((HA = V4.createElement(
       I,
       { paddingX: w, flexDirection: "row", gap: z },
-      o,
       $A,
       KA,
       zA,
     )),
-      (K[75] = z),
-      (K[76] = w),
-      (K[77] = o),
       (K[78] = $A),
       (K[79] = KA),
       (K[80] = zA),
-      (K[81] = HA));
-  else HA = K[81];
+      (K[81] = PA),
+      (K[82] = $A),
+      (K[83] = vA));
+  else vA = K[83];
   return HA;
 }

@@@ function 'vc2' (was 'k_2') — structural (53.8%)
--- pretty-v2.1.19.js:438854
+++ pretty-v2.1.20.js:521938
@@ -1,3 +1,3 @@
 function k_2(A) {
-  return A.status === "running";
+  return A.includes("socat");
 }

@@@ function 'Ec2' (was 'pE2') — structural (53.8%)
--- pretty-v2.1.19.js:495096
+++ pretty-v2.1.20.js:521941
@@ -1,3 +1,3 @@
 function pE2(A) {
-  return A.status === "pending";
+  return A.includes("bwrap");
 }

@@@ function 'cPA' (was 'iMA') — structural (53.4%)
--- pretty-v2.1.19.js:525119
+++ pretty-v2.1.20.js:529715
@@ -1,9 +1,7 @@
 function iMA(A) {
   return {
     type: "ephemeral",
-    ...(Bk("prompt_cache_1h_experiment", "use_1h_cache", !1)
-      ? { ttl: "1h" }
-      : {}),
+    ...(Z4() && !Af.isUsingOverage ? { ttl: "1h" } : {}),
     ...(A === "global" ? { scope: A } : {}),
   };
 }

@@@ variable 'AVK' (was 'pj') — structural (53.3%)
--- pretty-v2.1.19.js:101334
+++ pretty-v2.1.20.js:518407
@@ -1,11 +1,80 @@
 var pj = C(() => {
   H0();
-  jL8 = `Writes a file to the local filesystem.
+  P8();
+  ik();
+  a1();
+  Ct();
+  B1();
+  dd2 = `You are an elite AI agent architect specializing in crafting high-performance agent configurations. Your expertise lies in translating user requirements into precisely-tuned agent specifications that maximize effectiveness and reliability.
+
+**Important Context**: You may have access to project-specific instructions from CLAUDE.md files and other context that may include coding standards, project structure, and custom requirements. Consider this context when creating agents to ensure they align with the project's established patterns and practices.
+
+When a user describes what they want an agent to do, you will:
+
+1. **Extract Core Intent**: Identify the fundamental purpose, key responsibilities, and success criteria for the agent. Look for both explicit requirements and implicit needs. Consider any project-specific context from CLAUDE.md files. For agents that are meant to review code, you should assume that the user is asking to review recently written code and not the whole codebase, unless the user has explicitly instructed you otherwise.
+
+2. **Design Expert Persona**: Create a compelling expert identity that embodies deep domain knowledge relevant to the task. The persona should inspire confidence and guide the agent's decision-making approach.
+
+3. **Architect Comprehensive Instructions**: Develop a system prompt that:
+   - Establishes clear behavioral boundaries and operational parameters
+   - Provides specific methodologies and best practices for task execution
+   - Anticipates edge cases and provides guidance for handling them
+   - Incorporates any specific requirements or preferences mentioned by the user
+   - Defines output format expectations when relevant
+   - Aligns with project-specific coding standards and patterns from CLAUDE.md
 
-Usage:
-- This tool will overwrite the existing file if there is one at the provided path.
-- If this is an existing file, you MUST use the ${C5} tool first to read the file's contents. This tool will fail if you did not read the file first.
-- ALWAYS prefer editing existing files in the codebase. NEVER write new files unless explicitly required.
-- NEVER proactively create documentation files (*.md) or README files. Only create documentation files if explicitly requested by the User.
-- Only use emojis if the user explicitly requests it. Avoid writing emojis to files unless asked.`;
+4. **Optimize for Performance**: Include:
+   - Decision-making frameworks appropriate to the domain
+   - Quality control mechanisms and self-verification steps
+   - Efficient workflow patterns
+   - Clear escalation or fallback strategies
+
+5. **Create Identifier**: Design a concise, descriptive identifier that:
+   - Uses lowercase letters, numbers, and hyphens only
+   - Is typically 2-4 words joined by hyphens
+   - Clearly indicates the agent's primary function
+   - Is memorable and easy to type
+   - Avoids generic terms like "helper" or "assistant"
+
+6 **Example agent descriptions**:
+  - in the 'whenToUse' field of the JSON object, you should include examples of when this agent should be used.
+  - examples should be of the form:
+    - <example>
+      Context: The user is creating a test-runner agent that should be called after a logical chunk of code is written.
+      user: "Please write a function that checks if a number is prime"
+      assistant: "Here is the relevant function: "
+      <function call omitted for brevity only for this example>
+      <commentary>
+      Since a significant piece of code was written, use the ${j5} tool to launch the test-runner agent to run the tests.
+      </commentary>
+      assistant: "Now let me use the test-runner agent to run the tests"
+    </example>
+    - <example>
+      Context: User is creating an agent to respond to the word "hello" with a friendly jok.
+      user: "Hello"
+      assistant: "I'm going to use the ${j5} tool to launch the greeting-responder agent to respond with a friendly joke"
+      <commentary>
+      Since the user is greeting, use the greeting-responder agent to respond with a friendly joke. 
+      </commentary>
+    </example>
+  - If the user mentioned or implied that the agent should be used proactively, you should include examples of this.
+- NOTE: Ensure that in the examples, you are making the assistant use the Agent tool and not simply respond directly to the task.
+
+Your output must be a valid JSON object with exactly these fields:
+{
+  "identifier": "A unique, descriptive identifier using lowercase letters, numbers, and hyphens (e.g., 'test-runner', 'api-docs-writer', 'code-formatter')",
+  "whenToUse": "A precise, actionable description starting with 'Use this agent when...' that clearly defines the triggering conditions and use cases. Ensure you include examples as described above.",
+  "systemPrompt": "The complete system prompt that will govern the agent's behavior, written in second person ('You are...', 'You will...') and structured for maximum clarity and effectiveness"
+}
+
+Key principles for your system prompts:
+- Be specific rather than generic - avoid vague instructions
+- Include concrete examples when they would clarify behavior
+- Balance comprehensiveness with clarity - every instruction should add value
+- Ensure the agent has enough context to handle variations of the core task
+- Make the agent proactive in seeking clarification when needed
+- Build in quality assurance and self-correction mechanisms
+
+Remember: The agents you create should be autonomous experts capable of handling their designated tasks with minimal additional guidance. Your system prompts are their complete operational manual.
+`;
 });

@@@ variable 'y9A' (was 'pZK') — structural (53.3%)
--- pretty-v2.1.19.js:514417
+++ pretty-v2.1.20.js:524283
@@ -5,76 +5,9 @@
   q6();
   cs();
   F1();
-  gh2 = `You are an elite AI agent architect specializing in crafting high-performance agent configurations. Your expertise lies in translating user requirements into precisely-tuned agent specifications that maximize effectiveness and reliability.
-
-**Important Context**: You may have access to project-specific instructions from CLAUDE.md files and other context that may include coding standards, project structure, and custom requirements. Consider this context when creating agents to ensure they align with the project's established patterns and practices.
-
-When a user describes what they want an agent to do, you will:
-
-1. **Extract Core Intent**: Identify the fundamental purpose, key responsibilities, and success criteria for the agent. Look for both explicit requirements and implicit needs. Consider any project-specific context from CLAUDE.md files. For agents that are meant to review code, you should assume that the user is asking to review recently written code and not the whole codebase, unless the user has explicitly instructed you otherwise.
-
-2. **Design Expert Persona**: Create a compelling expert identity that embodies deep domain knowledge relevant to the task. The persona should inspire confidence and guide the agent's decision-making approach.
-
-3. **Architect Comprehensive Instructions**: Develop a system prompt that:
-   - Establishes clear behavioral boundaries and operational parameters
-   - Provides specific methodologies and best practices for task execution
-   - Anticipates edge cases and provides guidance for handling them
-   - Incorporates any specific requirements or preferences mentioned by the user
-   - Defines output format expectations when relevant
-   - Aligns with project-specific coding standards and patterns from CLAUDE.md
-
-4. **Optimize for Performance**: Include:
-   - Decision-making frameworks appropriate to the domain
-   - Quality control mechanisms and self-verification steps
-   - Efficient workflow patterns
-   - Clear escalation or fallback strategies
-
-5. **Create Identifier**: Design a concise, descriptive identifier that:
-   - Uses lowercase letters, numbers, and hyphens only
-   - Is typically 2-4 words joined by hyphens
-   - Clearly indicates the agent's primary function
-   - Is memorable and easy to type
-   - Avoids generic terms like "helper" or "assistant"
-
-6 **Example agent descriptions**:
-  - in the 'whenToUse' field of the JSON object, you should include examples of when this agent should be used.
-  - examples should be of the form:
-    - <example>
-      Context: The user is creating a test-runner agent that should be called after a logical chunk of code is written.
-      user: "Please write a function that checks if a number is prime"
-      assistant: "Here is the relevant function: "
-      <function call omitted for brevity only for this example>
-      <commentary>
-      Since a significant piece of code was written, use the ${l5} tool to launch the test-runner agent to run the tests.
-      </commentary>
-      assistant: "Now let me use the test-runner agent to run the tests"
-    </example>
-    - <example>
-      Context: User is creating an agent to respond to the word "hello" with a friendly jok.
-      user: "Hello"
-      assistant: "I'm going to use the ${l5} tool to launch the greeting-responder agent to respond with a friendly joke"
-      <commentary>
-      Since the user is greeting, use the greeting-responder agent to respond with a friendly joke. 
-      </commentary>
-    </example>
-  - If the user mentioned or implied that the agent should be used proactively, you should include examples of this.
-- NOTE: Ensure that in the examples, you are making the assistant use the Agent tool and not simply respond directly to the task.
-
-Your output must be a valid JSON object with exactly these fields:
-{
-  "identifier": "A unique, descriptive identifier using lowercase letters, numbers, and hyphens (e.g., 'test-runner', 'api-docs-writer', 'code-formatter')",
-  "whenToUse": "A precise, actionable description starting with 'Use this agent when...' that clearly defines the triggering conditions and use cases. Ensure you include examples as described above.",
-  "systemPrompt": "The complete system prompt that will govern the agent's behavior, written in second person ('You are...', 'You will...') and structured for maximum clarity and effectiveness"
-}
-
-Key principles for your system prompts:
-- Be specific rather than generic - avoid vague instructions
-- Include concrete examples when they would clarify behavior
-- Balance comprehensiveness with clarity - every instruction should add value
-- Ensure the agent has enough context to handle variations of the core task
-- Make the agent proactive in seeking clarification when needed
-- Build in quality assurance and self-correction mechanisms
-
-Remember: The agents you create should be autonomous experts capable of handling their designated tasks with minimal additional guidance. Your system prompts are their complete operational manual.
-`;
+  Cu();
+  i6();
+  B1();
+  o7();
+  jfK = `${GF6}.json`;
 });

@@@ function 'aT2' (was 'O_2') — structural (53.1%)
--- pretty-v2.1.19.js:437195
+++ pretty-v2.1.20.js:448355
@@ -1,30 +1,38 @@
 async function O_2(A, K) {
-  let { target_agent_id: q, request_id: Y, team_name: z } = A,
-    w = await K.getAppState(),
-    H = z || w.teamContext?.teamName;
+  let q = await K.getAppState(),
+    Y = q.teamContext?.teamName;
   if (!o$(w.teamContext))
     throw Error(
       "Only the team lead can approve plans. Teammates cannot approve their own or other plans.",
     );
-  if (!q || !Y)
+  if (!A.request_id)
+    throw Error(
+      "request_id is required for plan approval response. Use the requestId from the plan_approval_request message.",
+    );
+  if (!A.recipient)
     throw Error(
-      'target_agent_id and request_id are required for approvePlan. Use the "from" and "requestId" fields from the plan_approval_request message you received.',
+      'recipient is required for plan approval to specify whose plan to approve. Use the "from" field from the plan_approval_request message.',
     );
   let J = w.toolPermissionContext.mode,
     X = J === "plan" || J === "delegate" ? "default" : J,
     O = {
       type: "plan_approval_response",
-      requestId: Y,
+      requestId: A.request_id,
       approved: !0,
       timestamp: new Date().toISOString(),
       permissionMode: X,
     };
   return (
-    U3(q, { from: ZH, text: UA(O), timestamp: new Date().toISOString() }, H),
+    d3(
+      A.recipient,
+      { from: T2, text: QA(H), timestamp: new Date().toISOString() },
+      Y,
+    ),
     {
       data: {
         success: !0,
-        message: `Plan approved for ${q}. They will receive the approval and can proceed with implementation.`,
+        message: `Plan approved for ${A.recipient}. They will receive the approval and can proceed with implementation.`,
+        request_id: A.request_id,
       },
     }
   );

@@@ function 'OR7' (was 'nd2') — structural (52.9%)
--- pretty-v2.1.19.js:554023
+++ pretty-v2.1.20.js:340004
@@ -1,3 +1,3 @@
 function nd2(A) {
-  return !A;
+  return;
 }

@@@ function 'fM2' (was 'N$2') — structural (52.8%)
--- pretty-v2.1.19.js:434349
+++ pretty-v2.1.20.js:422630
@@ -1,4 +1,4 @@
-async function N$2(A, K, q, Y, z) {
+async function fM2(A, K, q, Y, z, w) {
   h(
     `[inProcessRunner] ${A.agentName} starting poll loop (abort=${K.signal.aborted})`,
   );
@@ -76,6 +76,8 @@
     } catch (O) {
       h(`[inProcessRunner] ${A.agentName} poll error: ${O}`);
     }
+    let $ = C7K(w, A.agentName);
+    if ($) return { type: "new_message", message: $, from: "task-list" };
   }
   return (
     h(

@@@ function 'u9K' (was 'aa7') — structural (52.6%)
--- pretty-v2.1.19.js:416691
+++ pretty-v2.1.20.js:443832
@@ -3,14 +3,6 @@
     I,
     null,
     RDA.default.createElement(f, null, "  ⎿  "),
-    RDA.default.createElement(
-      f,
-      null,
-      "Task ",
-      A.task_id,
-      " (",
-      A.task_type,
-      ") stopped",
-    ),
+    GjA.default.createElement(f, null, "Task stopped"),
   );
 }

@@@ function 'QLK' (was 'fNK') — structural (52.6%)
--- pretty-v2.1.19.js:547817
+++ pretty-v2.1.20.js:552737
@@ -1,6 +1,6 @@
 function fNK(A) {
-  let K = a(30),
-    { tasksSelected: q, showHint: Y } = A,
+  let K = s(36),
+    { tasksSelected: q, showHint: Y, isViewingTeammate: z } = A,
     { columns: z } = N8(),
     w;
   if (K[0] === Symbol.for("react.memo_cache_sentinel"))
@@ -39,75 +39,92 @@
     ((_ = Object.values(X ?? {}).filter(o3A)), (K[4] = X), (K[5] = _));
   else _ = K[5];
   let Z = _;
-  if (Z.length === 0) return null;
-  if (Z.length > 1 || z < 150) {
-    let G = Z.length === 1 ? "task" : "tasks",
-      W;
-    if (K[6] !== Z.length || K[7] !== G || K[8] !== q)
-      ((W = zw.createElement(
-        f,
-        { color: "background", inverse: q },
-        Z.length,
-        " background",
-        " ",
-        G,
-      )),
-        (K[6] = Z.length),
-        (K[7] = G),
-        (K[8] = q),
-        (K[9] = W));
-    else W = K[9];
-    let D;
-    if (K[10] !== $ || K[11] !== W)
-      ((D = zw.createElement(zw.Fragment, null, W, $)),
-        (K[10] = $),
-        (K[11] = W),
-        (K[12] = D));
-    else D = K[12];
+  if (G.length === 0) {
+    if (z) {
+      let W;
+      if (K[6] !== q)
+        ((W = kY.createElement(
+          f,
+          { color: "background", inverse: q },
+          "1 team",
+        )),
+          (K[6] = q),
+          (K[7] = W));
+      else W = K[7];
+      let D;
+      if (K[8] !== _ || K[9] !== W)
+        ((D = kY.createElement(kY.Fragment, null, W, _)),
+          (K[8] = _),
+          (K[9] = W),
+          (K[10] = D));
+      else D = K[10];
+      return D;
+    }
     return D;
   }
-  if (Z.length === 1) {
+  if (G.length === 1 && w >= 150) {
     let G = Z[0],
       W,
       D,
       j,
       M;
-    if (K[13] !== G || K[14] !== q) {
+    if (K[11] !== W || K[12] !== q) {
       let T = Np2(G);
       ((W = f),
         (D = "background"),
         (j = q),
         (M = MY(T, 40, !0)),
+        (K[11] = W),
+        (K[12] = q),
         (K[13] = G),
         (K[14] = q),
         (K[15] = W),
-        (K[16] = D),
-        (K[17] = j),
-        (K[18] = M));
-    } else ((W = K[15]), (D = K[16]), (j = K[17]), (M = K[18]));
+        (K[16] = P));
+    } else ((D = K[13]), (M = K[14]), (j = K[15]), (P = K[16]));
     let P;
-    if (K[19] !== G.status)
+    if (K[17] !== W.status)
       ((P = zw.createElement(f, { dimColor: !0 }, "(", G.status, ")")),
-        (K[19] = G.status),
-        (K[20] = P));
-    else P = K[20];
+        (K[17] = W.status),
+        (K[18] = V));
+    else V = K[18];
     let V;
-    if (K[21] !== W || K[22] !== D || K[23] !== j || K[24] !== M || K[25] !== P)
+    if (K[19] !== D || K[20] !== M || K[21] !== j || K[22] !== P || K[23] !== V)
       ((V = zw.createElement(W, { color: D, inverse: j }, M, " ", P)),
+        (K[19] = D),
+        (K[20] = M),
         (K[21] = W),
         (K[22] = D),
         (K[23] = j),
-        (K[24] = M),
+        (K[24] = N));
+    else N = K[24];
+    let T;
+    if (K[25] !== _ || K[26] !== N)
+      ((T = kY.createElement(kY.Fragment, null, N, _)),
         (K[25] = P),
-        (K[26] = V));
-    else V = K[26];
+        (K[26] = N),
+        (K[27] = T));
+    else T = K[27];
+    return T;
+  }
+  if (G.length >= 1) {
     let N;
-    if (K[27] !== $ || K[28] !== V)
-      ((N = zw.createElement(zw.Fragment, null, V, $)),
-        (K[27] = $),
-        (K[28] = V),
-        (K[29] = N));
+    if (K[28] !== G) ((W = JAz(G)), (K[28] = G), (K[29] = W));
     else N = K[29];
+    let D = W,
+      M;
+    if (K[30] !== D || K[31] !== q)
+      ((M = kY.createElement(f, { color: "background", inverse: q }, D)),
+        (K[30] = D),
+        (K[31] = q),
+        (K[32] = M));
+    else M = K[32];
+    let j;
+    if (K[33] !== _ || K[34] !== M)
+      ((j = kY.createElement(kY.Fragment, null, M, _)),
+        (K[33] = _),
+        (K[34] = M),
+        (K[35] = j));
+    else j = K[35];
     return N;
   }
   return null;

@@@ variable 'ML8' (was 'TE8') — structural (52.4%)
--- pretty-v2.1.19.js:89264
+++ pretty-v2.1.20.js:89421
@@ -1,10 +1,12 @@
 var TE8 = C(() => {
-  yE = [
+  ((n1A = [
     "acceptEdits",
     "bypassPermissions",
     "default",
     "delegate",
     "dontAsk",
     "plan",
-  ];
+  ]),
+    (QK5 = [...n1A]),
+    (wi = QK5));
 });

@@@ function 'QEK' (was 'Yh2') — structural (52.4%)
--- pretty-v2.1.19.js:513020
+++ pretty-v2.1.20.js:540638
@@ -1,3 +1,3 @@
 function Yh2() {
-  BQA();
+  if ((CEK(), IEK(), xEK(), BEK(), gEK(), QPA())) REK();
 }

@@@ function 'l6K' (was 'XU7') — structural (52.3%)
--- pretty-v2.1.19.js:384269
+++ pretty-v2.1.20.js:408949
@@ -1,20 +1,24 @@
-function XU7() {
+async function l6K() {
   let A = hA(),
     K = iG1(f8(), qU7),
     q = n1();
   try {
-    if (!A.existsSync(K)) return;
-    let Y = A.readdirSync(K);
+    let Y;
+    try {
+      Y = await A.readdir(K);
+    } catch {
+      return;
+    }
     for (let z of Y) {
       if (z.name === q) continue;
       let w = iG1(K, z.name);
       try {
-        (A.rmSync(w, { recursive: !0, force: !0 }),
+        (await A.rm(w, { recursive: !0, force: !0 }),
           h(`Cleaned up old image cache: ${w}`));
       } catch {}
     }
     try {
-      if (A.isDirEmptySync(K)) A.rmdirSync(K);
+      if ((await A.readdir(K)).length === 0) await A.rmdir(K);
     } catch {}
   } catch {}
 }

@@@ function 'TO1' (was 'HxA') — structural (52.3%)
--- pretty-v2.1.19.js:285818
+++ pretty-v2.1.20.js:282081
@@ -1,4 +1,4 @@
 function HxA() {
   if (uJY() === "win32") return `\\\\.\\pipe\\${Y27()}`;
-  return jB(mJY(), Y27());
+  return EC(zuA(), `${process.pid}.sock`);
 }

@@@ function 'M6z' (was 'M_2') — structural (52.0%)
--- pretty-v2.1.19.js:438321
+++ pretty-v2.1.20.js:562008
@@ -1,3 +1,3 @@
-function M_2(A, K) {
-  return A.identity.agentName.localeCompare(K.identity.agentName);
+function M6z() {
+  return N1(process.env.CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL);
 }

@@@ function 'Jv1' (was '$N1') — structural (51.8%)
--- pretty-v2.1.19.js:507229
+++ pretty-v2.1.20.js:511072
@@ -9,35 +9,52 @@
       return { mode: "list" };
     }),
     [$, _] = a3A.useState(0);
-  h(
-    `[BackgroundTasksDialog] Rendering with ${Object.keys(Y).length} tasks: ${JSON.stringify(Object.keys(Y))}`,
-  );
+  (gC("background-tasks-dialog"),
+    h(
+      `[BackgroundTasksDialog] Rendering with ${Object.keys(Y).length} tasks: ${JSON.stringify(Object.keys(Y))}`,
+    ));
   let {
       bashTasks: Z,
       remoteSessions: G,
       agentTasks: W,
+      teammateTasks: D,
       allSelectableItems: D,
     } = a3A.useMemo(() => {
       h(
         `[BackgroundTasksDialog] useMemo recalculating, tasks: ${JSON.stringify(Object.keys(H ?? {}))}`,
       );
-      let b = [
-          ...Object.values(H ?? {})
-            .filter(o3A)
-            .map(XS2),
-        ].sort((d, o) => {
-          if (d.status === "running" && o.status !== "running") return -1;
-          if (d.status !== "running" && o.status === "running") return 1;
-          return o.task.startTime - d.task.startTime;
-        }),
+      let u = Object.values(H ?? {})
+          .filter(v9A)
+          .map(Xp2)
+          .sort((OA, HA) => {
+            let DA = OA.status,
+              o = HA.status;
+            if (DA === "running" && o !== "running") return -1;
+            if (DA !== "running" && o === "running") return 1;
+            let _A = "task" in OA ? OA.task.startTime : 0;
+            return ("task" in HA ? HA.task.startTime : 0) - _A;
+          }),
         Q = b.filter((d) => d.type === "local_bash"),
         F = b.filter((d) => d.type === "remote_agent"),
-        B = b.filter((d) => d.type === "local_agent" && d.id !== z);
+        l = u.filter((OA) => OA.type === "local_agent" && OA.id !== z),
+        e = u.filter((OA) => OA.type === "in_process_teammate"),
+        JA =
+          e.length > 0
+            ? [
+                {
+                  id: "__leader__",
+                  type: "leader",
+                  label: `@${T2}`,
+                  status: "running",
+                },
+              ]
+            : [];
       return {
         bashTasks: Q,
         remoteSessions: F,
         agentTasks: B,
-        allSelectableItems: [...Q, ...F, ...B],
+        teammateTasks: [...JA, ...e],
+        allSelectableItems: [...JA, ...e, ...d, ...a, ...l],
       };
     }, [H, z]),
     j = D[$] ?? null;
@@ -49,7 +66,10 @@
       "confirm:next": () => _((S) => Math.min(D.length - 1, S + 1)),
       "confirm:yes": () => {
         let S = D[$];
-        if (S) O({ mode: "detail", itemId: S.id });
+        if (F)
+          if (F.type === "leader")
+            (Oe(w), A("Viewing leader", { display: "system" }));
+          else X({ mode: "detail", itemId: F.id });
       },
     },
     { context: "Confirmation", isActive: X.mode === "list" },
@@ -61,9 +81,15 @@
       if (S === "k") {
         if (b.type === "local_bash" && b.status === "running") P(b.id);
         else if (b.type === "local_agent" && b.status === "running") V(b.id);
+        else if (u.type === "in_process_teammate" && u.status === "running")
+          T(u.id);
       }
       if (S === "f") {
         if (b.type === "local_agent" && b.status === "running" && K) K(b.id);
+        else if (u.type === "in_process_teammate" && u.status === "running")
+          (uPA(u.id, w), A("Viewing teammate", { display: "system" }));
+        else if (u.type === "leader")
+          (Oe(w), A("Viewing leader", { display: "system" }));
       }
     }));
   let M = W8();
@@ -81,6 +107,13 @@
       setAppState: w,
     });
   }
+  async function T(F) {
+    await dj1.kill(F, {
+      abortController: q.abortController,
+      getAppState: q.getAppState,
+      setAppState: w,
+    });
+  }
   a3A.useEffect(() => {
     if (X.mode !== "list" && !Object.keys(H ?? {}).includes(X.itemId))
       O({ mode: "list" });
@@ -121,20 +154,44 @@
           onBack: N,
           key: `session-${S.id}`,
         });
-      default:
-        return null;
+      case "in_process_teammate":
+        return bK.default.createElement(GjK, {
+          teammate: F,
+          onDone: A,
+          onKill: F.status === "running" ? () => void T(F.id) : void 0,
+          onBack: k,
+          onForeground:
+            F.status === "running"
+              ? () => {
+                  (uPA(F.id, w), A("Viewing teammate", { display: "system" }));
+                }
+              : void 0,
+          key: `teammate-${F.id}`,
+        });
     }
   }
   let T = Z.filter((S) => S.status === "running").length,
     k =
       G.filter((S) => S.status === "running" || S.status === "pending").length +
       W.filter((S) => S.status === "running").length,
+    S = D.filter((F) => F.status === "running").length,
     R = Sf(
       [
         ...(T > 0
           ? [
               T3.default.createElement(
                 f,
+                { key: "teammates" },
+                S,
+                " ",
+                S !== 1 ? "agents" : "agent",
+              ),
+            ]
+          : []),
+        ...(R > 0
+          ? [
+              bK.default.createElement(
+                f,
                 { key: "shells" },
                 T,
                 " ",
@@ -168,7 +225,8 @@
         action: "view",
       }),
       ...[],
-      ...(j?.type === "local_agent" && j.status === "running" && K
+      ...((j?.type === "local_agent" && j.status === "running" && K) ||
+      (j?.type === "in_process_teammate" && j.status === "running")
         ? [
             T3.default.createElement(k6, {
               key: "foreground",
@@ -177,7 +235,9 @@
             }),
           ]
         : []),
-      ...((j?.type === "local_bash" || j?.type === "local_agent") &&
+      ...((j?.type === "local_bash" ||
+        j?.type === "local_agent" ||
+        j?.type === "in_process_teammate") &&
       j.status === "running"
         ? [
             T3.default.createElement(k6, {
@@ -226,10 +286,78 @@
               T3.default.createElement(
                 I,
                 { flexDirection: "column" },
-                (G.length > 0 || W.length > 0) &&
+                (Z.length > 0 || G.length > 0 || W.length > 0) &&
                   T3.default.createElement(
                     f,
                     { dimColor: !0 },
+                    bK.default.createElement(f, { bold: !0 }, "  ", "Agents"),
+                    " (",
+                    D.filter((F) => F.type !== "leader").length,
+                    ")",
+                  ),
+                bK.default.createElement(
+                  I,
+                  { flexDirection: "column" },
+                  (() => {
+                    let F = D.filter((l) => l.type === "leader"),
+                      Q = D.filter((l) => l.type === "in_process_teammate"),
+                      u = new Map();
+                    for (let l of Q) {
+                      let e = l.task.identity.teamName,
+                        JA = u.get(e);
+                      if (JA) JA.push(l);
+                      else u.set(e, [l]);
+                    }
+                    let d = [...u.entries()],
+                      a = 0;
+                    return bK.default.createElement(
+                      bK.default.Fragment,
+                      null,
+                      F.map((l) => {
+                        let e = a++;
+                        return bK.default.createElement(_dA, {
+                          key: l.id,
+                          item: l,
+                          isSelected: e === $,
+                        });
+                      }),
+                      d.map(([l, e]) => {
+                        let JA = e.length + F.length;
+                        return bK.default.createElement(
+                          I,
+                          { key: l, flexDirection: "column" },
+                          bK.default.createElement(
+                            f,
+                            { dimColor: !0 },
+                            "  ",
+                            "Team: ",
+                            l,
+                            " (",
+                            JA,
+                            ")",
+                          ),
+                          e.map((OA) => {
+                            let HA = a++;
+                            return bK.default.createElement(_dA, {
+                              key: OA.id,
+                              item: OA,
+                              isSelected: HA === $,
+                            });
+                          }),
+                        );
+                      }),
+                    );
+                  })(),
+                ),
+              ),
+            Z.length > 0 &&
+              bK.default.createElement(
+                I,
+                { flexDirection: "column", marginTop: D.length > 0 ? 1 : 0 },
+                (D.length > 0 || G.length > 0 || W.length > 0) &&
+                  bK.default.createElement(
+                    f,
+                    { dimColor: !0 },
                     T3.default.createElement(f, { bold: !0 }, "  ", "Bashes"),
                     " (",
                     Z.length,
@@ -242,7 +370,7 @@
                     T3.default.createElement(FB6, {
                       key: S.id,
                       item: S,
-                      isSelected: g === $,
+                      isSelected: D.length + Q === $,
                     }),
                   ),
                 ),
@@ -250,7 +378,10 @@
             G.length > 0 &&
               T3.default.createElement(
                 I,
-                { flexDirection: "column", marginTop: Z.length > 0 ? 1 : 0 },
+                {
+                  flexDirection: "column",
+                  marginTop: D.length > 0 || Z.length > 0 ? 1 : 0,
+                },
                 T3.default.createElement(
                   f,
                   { dimColor: !0 },
@@ -271,7 +402,7 @@
                     T3.default.createElement(FB6, {
                       key: S.id,
                       item: S,
-                      isSelected: Z.length + g === $,
+                      isSelected: D.length + Z.length + Q === $,
                     }),
                   ),
                 ),
@@ -281,7 +412,8 @@
                 I,
                 {
                   flexDirection: "column",
-                  marginTop: Z.length > 0 || G.length > 0 ? 1 : 0,
+                  marginTop:
+                    D.length > 0 || Z.length > 0 || G.length > 0 ? 1 : 0,
                 },
                 T3.default.createElement(
                   f,
@@ -303,7 +435,7 @@
                     T3.default.createElement(FB6, {
                       key: S.id,
                       item: S,
-                      isSelected: Z.length + G.length + g === $,
+                      isSelected: D.length + Z.length + G.length + Q === $,
                     }),
                   ),
                 ),

@@@ function 'QNK' (was 'EDK') — structural (51.7%)
--- pretty-v2.1.19.js:524956
+++ pretty-v2.1.20.js:529558
@@ -9,25 +9,14 @@
         ? `Additional working directories: ${K.join(", ")}
 `
         : "",
-    J = "";
-  if (A.includes("claude-opus-4-5"))
-    J = `
+    J = qn2(A),
+    O = J
+      ? `
 
-Assistant knowledge cutoff is May 2025.`;
-  else if (A.includes("claude-haiku-4"))
-    J = `
-
-Assistant knowledge cutoff is February 2025.`;
-  else if (
-    A.includes("claude-opus-4") ||
-    A.includes("claude-sonnet-4-5") ||
-    A.includes("claude-sonnet-4")
-  )
+Assistant knowledge cutoff is ${J}.`
+      : "",
     J = `
 
-Assistant knowledge cutoff is January 2025.`;
-  let X = `
-
 <claude_background_info>
 The most recent frontier Claude model is ${LB2} (model ID: '${RB2}').
 </claude_background_info>`;
@@ -39,6 +28,5 @@
 OS Version: ${Y}
 Today's date: ${OEA()}
 </env>
-${w}${J}${X}
-`;
+${w}${O}${X}`;
 }

@@@ function 'VgK' (was 'XhK') — structural (51.6%)
--- pretty-v2.1.19.js:567256
+++ pretty-v2.1.20.js:571339
@@ -1,5 +1,5 @@
 function XhK(A) {
-  let K = a(19),
+  let K = s(13),
     { serverName: q, onDone: Y } = A,
     z;
   if (K[0] !== Y || K[1] !== q)
@@ -29,29 +29,16 @@
       (K[2] = z));
   else z = K[2];
   let w = z,
-    H = W8(),
+    H = `New MCP server found in .mcp.json: ${q}`,
     J;
-  if (K[3] === Symbol.for("react.memo_cache_sentinel"))
-    ((J = { context: "Confirmation" }), (K[3] = J));
-  else J = K[3];
-  i1("confirm:no", Y, J);
+  if (K[3] !== w) ((J = () => w("no")), (K[3] = w), (K[4] = J));
+  else J = K[4];
   let X;
-  if (K[4] !== q)
-    ((X = iv.default.createElement(
-      f,
-      { bold: !0, color: "warning" },
-      "New MCP server found in .mcp.json: ",
-      q,
-    )),
-      (K[4] = q),
-      (K[5] = X));
+  if (K[5] === Symbol.for("react.memo_cache_sentinel"))
+    ((O = hk1.default.createElement(Sk1, null)), (K[5] = O));
   else X = K[5];
   let O;
   if (K[6] === Symbol.for("react.memo_cache_sentinel"))
-    ((O = iv.default.createElement(xv1, null)), (K[6] = O));
-  else O = K[6];
-  let $;
-  if (K[7] === Symbol.for("react.memo_cache_sentinel"))
     (($ = [
       {
         label: "Use this and all future MCP servers in this project",
@@ -60,70 +47,30 @@
       { label: "Use this MCP server", value: "yes" },
       { label: "Continue without using this MCP server", value: "no" },
     ]),
-      (K[7] = $));
-  else $ = K[7];
+      (K[6] = X));
+  else X = K[6];
   let _;
-  if (K[8] !== w)
+  if (K[7] !== w)
     ((_ = iv.default.createElement(T6, {
       options: $,
       onChange: (D) => w(D),
       onCancel: () => w("no"),
     })),
-      (K[8] = w),
-      (K[9] = _));
-  else _ = K[9];
+      (K[7] = w),
+      (K[8] = $));
+  else $ = K[8];
   let Z;
-  if (K[10] !== X || K[11] !== _)
+  if (K[9] !== H || K[10] !== J || K[11] !== $)
     ((Z = iv.default.createElement(
       I,
-      {
-        flexDirection: "column",
-        gap: 1,
-        padding: 1,
-        borderStyle: "round",
-        borderColor: "warning",
-      },
-      X,
+      { title: H, color: "warning", onCancel: J },
       O,
       _,
     )),
+      (K[9] = H),
       (K[10] = X),
       (K[11] = _),
       (K[12] = Z));
   else Z = K[12];
-  let G;
-  if (K[13] !== H.keyName || K[14] !== H.pending)
-    ((G = iv.default.createElement(
-      I,
-      { marginLeft: 3 },
-      iv.default.createElement(
-        f,
-        { dimColor: !0 },
-        H.pending
-          ? iv.default.createElement(
-              iv.default.Fragment,
-              null,
-              "Press ",
-              H.keyName,
-              " again to exit",
-            )
-          : iv.default.createElement(
-              iv.default.Fragment,
-              null,
-              "Enter to confirm · Esc to reject",
-            ),
-      ),
-    )),
-      (K[13] = H.keyName),
-      (K[14] = H.pending),
-      (K[15] = G));
-  else G = K[15];
-  let W;
-  if (K[16] !== Z || K[17] !== G)
-    ((W = iv.default.createElement(iv.default.Fragment, null, Z, G)),
-      (K[16] = Z),
-      (K[17] = G),
-      (K[18] = W));
-  else W = K[18];
   return W;
 }

@@@ function 'v7K' (was 'e9K') — structural (51.3%)
--- pretty-v2.1.19.js:464112
+++ pretty-v2.1.20.js:422022
@@ -1,11 +1,7 @@
 async function e9K(A, K, q, Y) {
   let { command: z, cwd: w, descriptions: H } = A,
-    J = await XV1(z, w, H, "allow", K, q);
+    J = T7K(z),
+    O = J ? await J : await UMA(z, w, H, "allow", K, q);
   if ((eS6(z, "allow", H, J), !Y.shouldContinue())) return;
-  if (J.matches && J.confidence === "high")
-    Y.onAllow({
-      type: "classifier",
-      classifier: "bash_allow",
-      reason: `Allowed by prompt rule: "${J.matchedDescription}"`,
-    });
+  Y.onComplete?.();
 }

@@@ function 'T7K' (was 'Qi2') — structural (51.3%)
--- pretty-v2.1.19.js:566540
+++ pretty-v2.1.20.js:422010
@@ -1,6 +1,5 @@
 function Qi2(A) {
   let K = TdA.get(A);
-  if (K) {
-    if ((K.refCount--, K.refCount <= 0)) TdA.delete(A);
-  }
+  if (K) KI6.delete(A);
+  return K;
 }

@@@ function 'Lk1' (was 'yv1') — structural (51.0%)
--- pretty-v2.1.19.js:563762
+++ pretty-v2.1.20.js:568765
@@ -1,5 +1,5 @@
 function yv1(A) {
-  let K = a(21),
+  let K = s(17),
     { customApiKeyTruncated: q, onDone: Y } = A,
     z;
   if (K[0] !== q || K[1] !== Y)
@@ -32,47 +32,40 @@
       (K[2] = z));
   else z = K[2];
   let w = z,
-    H = W8(),
     J;
-  if (K[3] === Symbol.for("react.memo_cache_sentinel"))
-    ((J = KG.default.createElement(
-      f,
-      { bold: !0, color: "warning" },
-      "Detected a custom API key in your environment",
-    )),
-      (K[3] = J));
-  else J = K[3];
+  if (K[3] !== w) ((H = () => w("no")), (K[3] = w), (K[4] = H));
+  else H = K[4];
   let X;
-  if (K[4] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[5] === Symbol.for("react.memo_cache_sentinel"))
     ((X = KG.default.createElement(f, { bold: !0 }, "ANTHROPIC_API_KEY")),
-      (K[4] = X));
-  else X = K[4];
+      (K[5] = J));
+  else J = K[5];
   let O;
-  if (K[5] !== q)
+  if (K[6] !== q)
     ((O = KG.default.createElement(
       f,
       null,
       X,
       KG.default.createElement(f, null, ": sk-ant-...", q),
     )),
-      (K[5] = q),
-      (K[6] = O));
-  else O = K[6];
+      (K[6] = q),
+      (K[7] = O));
+  else O = K[7];
   let $;
-  if (K[7] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[8] === Symbol.for("react.memo_cache_sentinel"))
     (($ = KG.default.createElement(
       f,
       null,
       "Do you want to use this API key?",
     )),
-      (K[7] = $));
-  else $ = K[7];
-  let _;
-  if (K[8] === Symbol.for("react.memo_cache_sentinel"))
-    ((_ = { label: "Yes", value: "yes" }), (K[8] = _));
+      (K[8] = X));
   else _ = K[8];
   let Z;
   if (K[9] === Symbol.for("react.memo_cache_sentinel"))
+    (($ = { label: "Yes", value: "yes" }), (K[9] = $));
+  else $ = K[9];
+  let _;
+  if (K[10] === Symbol.for("react.memo_cache_sentinel"))
     ((Z = [
       _,
       {
@@ -86,10 +79,10 @@
         value: "no",
       },
     ]),
-      (K[9] = Z));
-  else Z = K[9];
+      (K[10] = _));
+  else _ = K[10];
   let G;
-  if (K[10] !== w)
+  if (K[11] !== w)
     ((G = KG.default.createElement(T6, {
       defaultValue: "no",
       defaultFocusValue: "no",
@@ -97,64 +90,26 @@
       onChange: (M) => w(M),
       onCancel: () => w("no"),
     })),
-      (K[10] = w),
-      (K[11] = G));
-  else G = K[11];
+      (K[11] = w),
+      (K[12] = Z));
+  else Z = K[12];
   let W;
-  if (K[12] !== O || K[13] !== G)
+  if (K[13] !== H || K[14] !== O || K[15] !== Z)
     ((W = KG.default.createElement(
       I,
       {
-        flexDirection: "column",
-        gap: 1,
-        padding: 1,
-        borderStyle: "round",
-        borderColor: "warning",
+        title: "Detected a custom API key in your environment",
+        color: "warning",
+        onCancel: H,
       },
-      J,
       O,
       $,
       G,
     )),
-      (K[12] = O),
       (K[13] = G),
-      (K[14] = W));
-  else W = K[14];
-  let D;
-  if (K[15] !== H.keyName || K[16] !== H.pending)
-    ((D = KG.default.createElement(
-      I,
-      { marginLeft: 3 },
-      KG.default.createElement(
-        f,
-        { dimColor: !0 },
-        H.pending
-          ? KG.default.createElement(
-              KG.default.Fragment,
-              null,
-              "Press ",
-              H.keyName,
-              " again to exit",
-            )
-          : KG.default.createElement(
-              KG.default.Fragment,
-              null,
-              "Enter to confirm ",
-              aA.dot,
-              " Esc to cancel",
-            ),
-      ),
-    )),
-      (K[15] = H.keyName),
-      (K[16] = H.pending),
-      (K[17] = D));
-  else D = K[17];
-  let j;
-  if (K[18] !== D || K[19] !== W)
-    ((j = KG.default.createElement(KG.default.Fragment, null, W, D)),
-      (K[18] = D),
-      (K[19] = W),
-      (K[20] = j));
-  else j = K[20];
+      (K[14] = O),
+      (K[15] = Z),
+      (K[16] = G));
+  else G = K[16];
   return j;
 }

@@@ function 'VVA' (was 'fU7') — structural (50.5%)
--- pretty-v2.1.19.js:385360
+++ pretty-v2.1.20.js:558968
@@ -1,10 +1,9 @@
-function fU7() {
+function VVA(A) {
   let A = a(3),
-    { columns: K } = N8(),
-    Y = `Conversation compacted · ${w5("app:toggleTranscript", "Global", "ctrl+o")} for history`,
+    { getFpsMetrics: q, children: Y } = A,
     z;
   if (A[0] !== K || A[1] !== Y)
-    ((z = hv6.createElement(V3, { dividerChar: "═", title: Y, width: K })),
+    ((z = PVA.default.createElement(yyK.Provider, { value: q }, Y)),
       (A[0] = K),
       (A[1] = Y),
       (A[2] = z));

@@@ function 'lDA' (was 'KWA') — structural (50.2%)
--- pretty-v2.1.19.js:361553
+++ pretty-v2.1.20.js:386650
@@ -1,6 +1,6 @@
 function KWA(A) {
-  let K = a(8),
-    { title: q, subtitle: Y, color: z } = A,
+  let K = s(13),
+    { title: q, subtitle: Y, color: z, workerBadge: w } = A,
     w = z === void 0 ? "permission" : z,
     H;
   if (K[0] !== w || K[1] !== q)
@@ -11,20 +11,33 @@
   else H = K[2];
   let J;
   if (K[3] !== Y)
-    ((J = Y !== void 0 && Kp.createElement(f, { wrap: "truncate-start" }, Y)),
+    ((O = w && $S.createElement(f, { dimColor: !0 }, "· ", "@", w.name)),
       (K[3] = Y),
       (K[4] = J));
   else J = K[4];
   let X;
   if (K[5] !== H || K[6] !== J)
-    ((X = Kp.createElement(
-      I,
-      { flexDirection: "column" },
-      Kp.createElement(I, { flexDirection: "row", gap: 1 }, H, J),
-    )),
+    ((X = $S.createElement(I, { flexDirection: "row", gap: 1 }, J, O)),
       (K[5] = H),
       (K[6] = J),
       (K[7] = X));
   else X = K[7];
+  let $;
+  if (K[8] !== Y)
+    (($ =
+      Y != null &&
+      (typeof Y === "string"
+        ? $S.createElement(f, { dimColor: !0, wrap: "truncate-start" }, Y)
+        : Y)),
+      (K[8] = Y),
+      (K[9] = $));
+  else $ = K[9];
+  let _;
+  if (K[10] !== X || K[11] !== $)
+    ((_ = $S.createElement(I, { flexDirection: "column" }, X, $)),
+      (K[10] = X),
+      (K[11] = $),
+      (K[12] = _));
+  else _ = K[12];
   return X;
 }

@@@ function 'qZ7' (was 'LO7') — structural (50.0%)
--- pretty-v2.1.19.js:306769
+++ pretty-v2.1.20.js:303049
@@ -1,29 +1,38 @@
 async function LO7(A) {
   if (E1(process.env.CLAUDE_CODE_DISABLE_TERMINAL_TITLE)) return;
-  if (A.startsWith("<local-command-stdout>")) return;
-  let K = "{";
+  if (A.startsWith(`<${l2A}>`)) return;
   try {
-    let q = await J$({
-        systemPrompt: [
-          "Analyze if this message indicates a new conversation topic. If it does, extract a 2-3 word title that captures the new topic. Format your response as a JSON object with two fields: 'isNewTopic' (boolean) and 'title' (string, or null if isNewTopic is false). Only include these fields, no other text. ONLY generate the JSON object, no other text (eg. no markdown).",
-        ],
-        userPrompt: A,
-        assistantPrompt: K,
-        signal: new AbortController().signal,
-        options: {
-          querySource: "terminal_update_title",
-          agents: [],
-          isNonInteractiveSession: !1,
-          hasAppendSystemPrompt: !1,
-          mcpTools: [],
-        },
-      }),
-      Y =
-        K +
-        q.message.content
-          .filter((w) => w.type === "text")
-          .map((w) => w.text)
-          .join(""),
+    let q = (
+        await Z$({
+          systemPrompt: [
+            "Analyze if this message indicates a new conversation topic. If it does, extract a 2-3 word title that captures the new topic. Format your response as a JSON object with two fields: 'isNewTopic' (boolean) and 'title' (string, or null if isNewTopic is false).",
+          ],
+          userPrompt: A,
+          outputFormat: {
+            type: "json_schema",
+            schema: {
+              type: "object",
+              properties: {
+                isNewTopic: { type: "boolean" },
+                title: { anyOf: [{ type: "string" }, { type: "null" }] },
+              },
+              required: ["isNewTopic", "title"],
+              additionalProperties: !1,
+            },
+          },
+          signal: new AbortController().signal,
+          options: {
+            querySource: "terminal_update_title",
+            agents: [],
+            isNonInteractiveSession: !1,
+            hasAppendSystemPrompt: !1,
+            mcpTools: [],
+          },
+        })
+      ).message.content
+        .filter((z) => z.type === "text")
+        .map((z) => z.text)
+        .join(""),
       z = S9(Y);
     if (z && typeof z === "object" && "isNewTopic" in z && "title" in z) {
       if (z.isNewTopic && z.title) yX1(z.title);

@@@ function 'VmK' (was 'rIK') — structural (49.7%)
--- pretty-v2.1.19.js:563276
+++ pretty-v2.1.20.js:568307
@@ -1,5 +1,5 @@
 function rIK(A) {
-  let K = a(40),
+  let K = s(33),
     { servers: q, scope: Y, onDone: z } = A,
     w;
   if (K[0] !== q) ((w = Object.keys(q)), (K[0] = q), (K[1] = w));
@@ -47,7 +47,6 @@
       }
       P(XA);
     },
-    D = W8(),
     [j] = p4(),
     M;
   if (K[8] !== z || K[9] !== Y || K[10] !== j)
@@ -76,38 +75,9 @@
       (K[13] = V));
   else V = K[13];
   let N = V,
-    T;
-  if (K[14] === Symbol.for("react.memo_cache_sentinel"))
-    ((T = { context: "Confirmation" }), (K[14] = T));
-  else T = K[14];
-  i1("confirm:no", N, T);
-  let k;
-  if (K[15] === Symbol.for("react.memo_cache_sentinel"))
-    ((k = kP.default.createElement(
-      f,
-      { bold: !0, color: "success" },
-      "Import MCP Servers from Claude Desktop",
-    )),
-      (K[15] = k));
-  else k = K[15];
-  let R = H.length !== 1 ? "s" : "",
+    N = `Found ${H.length} MCP server${H.length !== 1 ? "s" : ""} in Claude Desktop.`,
     x;
-  if (K[16] !== H.length || K[17] !== R)
-    ((x = kP.default.createElement(
-      f,
-      null,
-      "Found ",
-      H.length,
-      " MCP server",
-      R,
-      " in Claude Desktop.",
-    )),
-      (K[16] = H.length),
-      (K[17] = R),
-      (K[18] = x));
-  else x = K[18];
-  let S;
-  if (K[19] !== G.length)
+  if (K[14] !== G.length)
     ((S =
       G.length > 0 &&
       kP.default.createElement(
@@ -115,97 +85,95 @@
         { color: "warning" },
         "Note: Some servers already exist with the same name. If selected, they will be imported with a numbered suffix.",
       )),
-      (K[19] = G.length),
-      (K[20] = S));
-  else S = K[20];
+      (K[14] = G.length),
+      (K[15] = T));
+  else T = K[15];
   let g;
-  if (K[21] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[16] === Symbol.for("react.memo_cache_sentinel"))
     ((g = kP.default.createElement(
       f,
       null,
       "Please select the servers you want to import:",
     )),
-      (K[21] = g));
-  else g = K[21];
+      (K[16] = k));
+  else k = K[16];
   let b, Q;
-  if (K[22] !== G || K[23] !== H)
+  if (K[17] !== G || K[18] !== H)
     ((b = H.map((l) => ({
       label: `${l}${G.includes(l) ? " (already exists)" : ""}`,
       value: l,
     }))),
       (Q = H.filter((l) => !G.includes(l))),
-      (K[22] = G),
-      (K[23] = H),
-      (K[24] = b),
-      (K[25] = Q));
-  else ((b = K[24]), (Q = K[25]));
+      (K[17] = G),
+      (K[18] = H),
+      (K[19] = R),
+      (K[20] = b));
+  else ((R = K[19]), (b = K[20]));
   let F;
-  if (K[26] !== W || K[27] !== b || K[28] !== Q)
+  if (K[21] !== W || K[22] !== R || K[23] !== b)
     ((F = kP.default.createElement(Cv1, {
       options: b,
       defaultValue: Q,
       onSubmit: W,
     })),
-      (K[26] = W),
-      (K[27] = b),
-      (K[28] = Q),
-      (K[29] = F));
-  else F = K[29];
+      (K[21] = W),
+      (K[22] = R),
+      (K[23] = b),
+      (K[24] = S));
+  else S = K[24];
   let B;
-  if (K[30] !== x || K[31] !== S || K[32] !== F)
+  if (K[25] !== V || K[26] !== S || K[27] !== N || K[28] !== T)
     ((B = kP.default.createElement(
       I,
       {
-        flexDirection: "column",
-        gap: 1,
-        padding: 1,
-        borderStyle: "round",
-        borderColor: "success",
+        title: "Import MCP Servers from Claude Desktop",
+        subtitle: N,
+        color: "success",
+        onCancel: V,
+        hideInputGuide: !0,
       },
-      k,
-      x,
       S,
       g,
       F,
     )),
-      (K[30] = x),
-      (K[31] = S),
-      (K[32] = F),
-      (K[33] = B));
-  else B = K[33];
+      (K[25] = V),
+      (K[26] = S),
+      (K[27] = N),
+      (K[28] = T),
+      (K[29] = B));
+  else B = K[29];
   let d;
-  if (K[34] !== D.keyName || K[35] !== D.pending)
+  if (K[30] === Symbol.for("react.memo_cache_sentinel"))
     ((d = kP.default.createElement(
       I,
-      { marginLeft: 3 },
+      { paddingX: 1 },
       kP.default.createElement(
         f,
-        { dimColor: !0 },
-        D.pending
-          ? kP.default.createElement(
-              kP.default.Fragment,
-              null,
-              "Press ",
-              D.keyName,
-              " again to exit",
-            )
-          : kP.default.createElement(
-              kP.default.Fragment,
-              null,
-              "Space to select · Enter to confirm · Esc to cancel",
-            ),
+        { dimColor: !0, italic: !0 },
+        ov.default.createElement(
+          w8,
+          null,
+          ov.default.createElement(M6, { shortcut: "Space", action: "select" }),
+          ov.default.createElement(M6, {
+            shortcut: "Enter",
+            action: "confirm",
+          }),
+          ov.default.createElement(d6, {
+            action: "confirm:no",
+            context: "Confirmation",
+            fallback: "Esc",
+            description: "cancel",
+          }),
+        ),
       ),
     )),
-      (K[34] = D.keyName),
-      (K[35] = D.pending),
-      (K[36] = d));
-  else d = K[36];
+      (K[30] = x));
+  else x = K[30];
   let o;
-  if (K[37] !== B || K[38] !== d)
+  if (K[31] !== B)
     ((o = kP.default.createElement(kP.default.Fragment, null, B, d)),
-      (K[37] = B),
-      (K[38] = d),
-      (K[39] = o));
-  else o = K[39];
+      (K[31] = B),
+      (K[32] = F));
+  else F = K[32];
   return o;
 }

@@@ function 'aa2' (was 'VF2') — structural (49.6%)
--- pretty-v2.1.19.js:534342
+++ pretty-v2.1.20.js:539141
@@ -1,25 +1,26 @@
-function VF2() {
+async function aa2() {
   let A = O9A(),
     K = { messages: 0, errors: 0 },
     q = hA();
   try {
     let Y = f8(),
-      z = af(Y, "file-history");
-    if (!q.existsSync(z)) return K;
-    let H = q
-      .readdirSync(z)
-      .filter((J) => J.isDirectory())
-      .map((J) => af(z, J.name));
+      z = NP(Y, "file-history"),
+      w;
+    try {
+      w = await q.readdir(z);
+    } catch {
+      return K;
+    }
+    let H = w.filter((J) => J.isDirectory()).map((J) => NP(z, J.name));
     for (let J of H)
       try {
-        if (!q.existsSync(J)) continue;
-        if (q.statSync(J).mtime < A)
-          (q.rmSync(J, { recursive: !0, force: !0 }), K.messages++);
+        if ((await q.stat(J)).mtime < A)
+          (await q.rm(J, { recursive: !0, force: !0 }), K.messages++);
       } catch {
         K.errors++;
       }
     try {
-      if (q.isDirEmptySync(z)) q.rmdirSync(z);
+      await q.rmdir(z);
     } catch {}
   } catch (Y) {
     qA(Y);

@@@ function 'sa2' (was 'fF2') — structural (49.6%)
--- pretty-v2.1.19.js:534370
+++ pretty-v2.1.20.js:539170
@@ -1,25 +1,26 @@
-function fF2() {
+async function sa2() {
   let A = O9A(),
     K = { messages: 0, errors: 0 },
     q = hA();
   try {
     let Y = f8(),
-      z = af(Y, "session-env");
-    if (!q.existsSync(z)) return K;
-    let H = q
-      .readdirSync(z)
-      .filter((J) => J.isDirectory())
-      .map((J) => af(z, J.name));
+      z = NP(Y, "session-env"),
+      w;
+    try {
+      w = await q.readdir(z);
+    } catch {
+      return K;
+    }
+    let H = w.filter((J) => J.isDirectory()).map((J) => NP(z, J.name));
     for (let J of H)
       try {
-        if (!q.existsSync(J)) continue;
-        if (q.statSync(J).mtime < A)
-          (q.rmSync(J, { recursive: !0, force: !0 }), K.messages++);
+        if ((await q.stat(J)).mtime < A)
+          (await q.rm(J, { recursive: !0, force: !0 }), K.messages++);
       } catch {
         K.errors++;
       }
     try {
-      if (q.isDirEmptySync(z)) q.rmdirSync(z);
+      await q.rmdir(z);
     } catch {}
   } catch (Y) {
     qA(Y);

@@@ variable 'Vv' (was 'Gv') — structural (49.5%)
--- pretty-v2.1.19.js:437548
+++ pretty-v2.1.20.js:414792
@@ -16,49 +16,26 @@
   Up();
   e1();
   J7();
-  F1();
-  x9();
   f4K = U.strictObject({
     operation: U.enum([
       "spawnTeam",
       "cleanup",
-      "write",
-      "broadcast",
-      "requestShutdown",
-      "approveShutdown",
-      "rejectShutdown",
-      "approvePlan",
-      "rejectPlan",
       "discoverTeams",
       "requestJoin",
       "approveJoin",
       "rejectJoin",
     ]).describe(
-      "Operation: spawnTeam to create a team, cleanup to remove team and task directories, write mailbox messages, requestShutdown to ask a teammate to shut down, approveShutdown to accept a shutdown request and exit, rejectShutdown to decline a shutdown request, approvePlan to approve a teammate plan, rejectPlan to reject a teammate plan with feedback, discoverTeams to list available teams to join, requestJoin to request joining a team, approveJoin to approve a join request from another agent, rejectJoin to reject a join request from another agent. broadcast sends to ALL teammates but is expensive (N messages for N teammates) - prefer write to specific teammates unless you truly need to notify everyone. Note: Messages from teammates are automatically delivered.",
+      "Operation: spawnTeam to create a team, cleanup to remove team and task directories, discoverTeams to list available teams to join, requestJoin to request joining a team, approveJoin to approve a join request from another agent, rejectJoin to reject a join request from another agent.",
     ),
-    name: U.string()
+    target_agent_id: U.string()
       .optional()
       .describe(
-        "Your name when broadcasting (required for broadcast operation)",
+        "Agent name/ID of the target (required for approveJoin/rejectJoin operations)",
       ),
-    key: U.string()
-      .optional()
-      .describe("Key for the data being stored (write)"),
-    value: U.string()
-      .optional()
-      .describe("Value to store - JSON string for complex data (write)"),
-    target_agent_id: U.string()
-      .optional()
-      .describe("Agent ID of the recipient (required for write operation)"),
     agent_type: U.string()
       .optional()
       .describe(
         'Type/role of the team lead (e.g., "researcher", "test-runner"). Used for team file and inter-agent coordination.',
-      ),
-    agent_id: U.string()
-      .optional()
-      .describe(
-        "Your registered agent ID (for write operations). Use this to identify yourself as a registered agent.",
       ),
     team_name: U.string()
       .optional()
@@ -68,18 +45,11 @@
       .describe("Team description/purpose (only used with spawnTeam)."),
     reason: U.string()
       .optional()
-      .describe(
-        "Reason for the operation. For requestShutdown: optional explanation why shutdown is requested. For rejectShutdown: required explanation why shutdown is declined.",
-      ),
+      .describe("Reason for the operation (optional for rejectJoin)."),
     request_id: U.string()
-      .optional()
-      .describe(
-        "Request ID for shutdown, plan approval, or join operations. For approveShutdown/rejectShutdown: ID of the shutdown request. For approvePlan/rejectPlan: ID of the plan approval request. For approveJoin/rejectJoin: ID of the join request.",
-      ),
-    feedback: U.string()
       .optional()
       .describe(
-        "Feedback for plan rejection (optional for rejectPlan operation)",
+        "Request ID for join operations. For approveJoin/rejectJoin: ID of the join request.",
       ),
     assigned_name: U.string()
       .optional()
@@ -104,7 +74,7 @@
     name: a5A,
     maxResultSizeChars: 1e5,
     userFacingName() {
-      return "Teammate";
+      return "";
     },
     inputSchema: f4K,
     isEnabled() {
@@ -114,7 +84,7 @@
       return !1;
     },
     isReadOnly(A) {
-      return A.operation === "write" || A.operation === "broadcast";
+      return !1;
     },
     async checkPermissions(A, K) {
       return { behavior: "allow", updatedInput: A };
@@ -128,54 +98,6 @@
             errorCode: 9,
           };
       }
-      if (A.operation === "write") {
-        if (!A.target_agent_id)
-          return {
-            result: !1,
-            message: "target_agent_id is required for write operations",
-            errorCode: 4,
-          };
-        if (A.value === void 0)
-          return {
-            result: !1,
-            message: "Value is required for write operations",
-            errorCode: 5,
-          };
-      }
-      if (A.operation === "requestShutdown") {
-        if (!A.target_agent_id || A.target_agent_id.trim().length === 0)
-          return {
-            result: !1,
-            message:
-              "target_agent_id is required for requestShutdown operation to specify which teammate to shut down",
-            errorCode: 13,
-          };
-      }
-      if (A.operation === "rejectShutdown") {
-        if (!A.reason || A.reason.trim().length === 0)
-          return {
-            result: !1,
-            message:
-              "reason is required for rejectShutdown operation to explain why shutdown is declined",
-            errorCode: 14,
-          };
-      }
-      if (A.operation === "approvePlan" || A.operation === "rejectPlan") {
-        if (!A.target_agent_id || A.target_agent_id.trim().length === 0)
-          return {
-            result: !1,
-            message:
-              "target_agent_id is required for approvePlan/rejectPlan operations",
-            errorCode: 15,
-          };
-        if (!A.request_id || A.request_id.trim().length === 0)
-          return {
-            result: !1,
-            message:
-              "request_id is required for approvePlan/rejectPlan operations",
-            errorCode: 16,
-          };
-      }
       if (A.operation === "requestJoin") {
         if (!A.team_name || A.team_name.trim().length === 0)
           return {
@@ -218,13 +140,6 @@
     async call(A, K) {
       if (A.operation === "spawnTeam") return Y_2(A, K);
       if (A.operation === "cleanup") return q_2(A, K);
-      if (A.operation === "write") return z_2(A, K);
-      if (A.operation === "broadcast") return w_2(A, K);
-      if (A.operation === "requestShutdown") return H_2(A, K);
-      if (A.operation === "approveShutdown") return await J_2(A, K);
-      if (A.operation === "rejectShutdown") return X_2(A, K);
-      if (A.operation === "approvePlan") return O_2(A, K);
-      if (A.operation === "rejectPlan") return $_2(A, K);
       if (A.operation === "discoverTeams") return W_2(A, K);
       if (A.operation === "requestJoin") return __2(A, K);
       if (A.operation === "approveJoin") return Z_2(A, K);

@@@ function 'r7z' (was 'vr2') — structural (49.0%)
--- pretty-v2.1.19.js:572898
+++ pretty-v2.1.20.js:577000
@@ -2,14 +2,25 @@
   let K = 0,
     q = Lw(A);
   if (q.stdin) n("tengu_stdin_interactive", {});
+  let Y = new sp6();
   return {
-    ...q,
-    onFlicker: (Y, z, w) => {
-      if (w === "resize") return;
-      let H = Date.now();
-      if (H - K < 1000)
-        n("tengu_flicker", { desiredHeight: Y, actualHeight: z, reason: w });
-      K = H;
+    getFpsMetrics: () => Y.getMetrics(),
+    renderOptions: {
+      ...q,
+      onFrame: (z) => {
+        Y.record(z.durationMs);
+        for (let w of z.flickers) {
+          if (w.reason === "resize") continue;
+          let H = Date.now();
+          if (H - K < 1000)
+            n("tengu_flicker", {
+              desiredHeight: w.desiredHeight,
+              actualHeight: w.availableHeight,
+              reason: w.reason,
+            });
+          K = H;
+        }
+      },
     },
   };
 }

@@@ function 'sT2' (was '$_2') — structural (48.8%)
--- pretty-v2.1.19.js:437226
+++ pretty-v2.1.20.js:448394
@@ -1,28 +1,37 @@
 async function $_2(A, K) {
-  let { target_agent_id: q, request_id: Y, feedback: z, team_name: w } = A,
-    H = await K.getAppState(),
-    J = w || H.teamContext?.teamName;
+  let q = await K.getAppState(),
+    Y = q.teamContext?.teamName;
   if (!o$(H.teamContext))
     throw Error(
       "Only the team lead can reject plans. Teammates cannot reject their own or other plans.",
     );
-  if (!q || !Y)
+  if (!A.request_id)
     throw Error(
-      'target_agent_id and request_id are required for rejectPlan. Use the "from" and "requestId" fields from the plan_approval_request message you received.',
+      "request_id is required for plan rejection response. Use the requestId from the plan_approval_request message.",
     );
-  let X = {
-    type: "plan_approval_response",
-    requestId: Y,
-    approved: !1,
-    feedback: z || "Plan needs revision",
-    timestamp: new Date().toISOString(),
-  };
+  if (!A.recipient)
+    throw Error(
+      'recipient is required for plan rejection to specify whose plan to reject. Use the "from" field from the plan_approval_request message.',
+    );
+  let z = A.content || "Plan needs revision",
+    w = {
+      type: "plan_approval_response",
+      requestId: A.request_id,
+      approved: !1,
+      feedback: z,
+      timestamp: new Date().toISOString(),
+    };
   return (
-    U3(q, { from: ZH, text: UA(X), timestamp: new Date().toISOString() }, J),
+    d3(
+      A.recipient,
+      { from: T2, text: QA(w), timestamp: new Date().toISOString() },
+      Y,
+    ),
     {
       data: {
         success: !0,
-        message: `Plan rejected for ${q} with feedback: "${z || "Plan needs revision"}"`,
+        message: `Plan rejected for ${A.recipient} with feedback: "${z}"`,
+        request_id: A.request_id,
       },
     }
   );

@@@ function 'EKK' (was 'Bi7') — structural (47.9%)
--- pretty-v2.1.19.js:399550
+++ pretty-v2.1.20.js:426687
@@ -1,20 +1,6 @@
-function Bi7(
-  {
-    pattern: A,
-    path: K,
-    glob: q,
-    type: Y,
-    output_mode: z = "files_with_matches",
-    head_limit: w,
-  },
-  { verbose: H },
-) {
+function EKK({ pattern: A, path: K }, { verbose: q }) {
   if (!A) return null;
   let J = [`pattern: "${A}"`];
   if (K) J.push(`path: "${H ? K : fq(K)}"`);
-  if (q) J.push(`glob: "${q}"`);
-  if (Y) J.push(`type: "${Y}"`);
-  if (z !== "files_with_matches") J.push(`output_mode: "${z}"`);
-  if (w !== void 0) J.push(`head_limit: ${w}`);
   return J.join(", ");
 }

@@@ function 'Iw' (was 'P2') — structural (46.9%)
--- pretty-v2.1.19.js:361637
+++ pretty-v2.1.20.js:386699
@@ -1,5 +1,5 @@
 function P2(A) {
-  let K = a(19),
+  let K = s(15),
     {
       title: q,
       subtitle: Y,
@@ -13,42 +13,39 @@
     $ = z === void 0 ? "permission" : z,
     _ = H === void 0 ? 1 : H,
     Z;
-  if (K[0] !== J)
-    ((Z = J && tT.createElement(vZ1, { name: J.name, color: J.color })),
+  if (K[0] !== Y || K[1] !== q || K[2] !== w || K[3] !== J)
+    ((Z = _S.createElement(lDA, {
+      title: q,
+      subtitle: Y,
+      color: w,
+      workerBadge: J,
+    })),
       (K[0] = J),
-      (K[1] = Z));
-  else Z = K[1];
-  let G;
-  if (K[2] !== Y || K[3] !== q || K[4] !== w)
-    ((G = tT.createElement(KWA, { title: q, subtitle: Y, color: w })),
+      (K[1] = q),
       (K[2] = Y),
       (K[3] = q),
-      (K[4] = w),
-      (K[5] = G));
-  else G = K[5];
+      (K[4] = Z));
+  else Z = K[4];
   let W;
-  if (K[6] !== G || K[7] !== X)
-    ((W = tT.createElement(I, { justifyContent: "space-between" }, G, X)),
+  if (K[5] !== Z || K[6] !== O)
+    ((G = _S.createElement(
+      I,
+      { paddingX: 1, flexDirection: "column" },
+      _S.createElement(I, { justifyContent: "space-between" }, Z, O),
+    )),
+      (K[5] = Z),
       (K[6] = G),
-      (K[7] = X),
-      (K[8] = W));
-  else W = K[8];
+      (K[7] = G));
+  else G = K[7];
   let D;
-  if (K[9] !== Z || K[10] !== W)
-    ((D = tT.createElement(I, { paddingX: 1, flexDirection: "column" }, Z, W)),
+  if (K[8] !== X || K[9] !== _)
+    ((W = _S.createElement(I, { flexDirection: "column", paddingX: _ }, X)),
+      (K[8] = X),
       (K[9] = Z),
-      (K[10] = W),
-      (K[11] = D));
-  else D = K[11];
+      (K[10] = W));
+  else W = K[10];
   let j;
-  if (K[12] !== O || K[13] !== _)
-    ((j = tT.createElement(I, { flexDirection: "column", paddingX: _ }, O)),
-      (K[12] = O),
-      (K[13] = _),
-      (K[14] = j));
-  else j = K[14];
-  let M;
-  if (K[15] !== $ || K[16] !== D || K[17] !== j)
+  if (K[11] !== $ || K[12] !== G || K[13] !== W)
     ((M = tT.createElement(
       I,
       {
@@ -63,10 +60,10 @@
       D,
       j,
     )),
-      (K[15] = $),
-      (K[16] = D),
-      (K[17] = j),
-      (K[18] = M));
-  else M = K[18];
+      (K[11] = $),
+      (K[12] = G),
+      (K[13] = W),
+      (K[14] = D));
+  else D = K[14];
   return M;
 }

@@@ function 'u25' (was 'p1q') — structural (46.5%)
--- pretty-v2.1.19.js:95407
+++ pretty-v2.1.20.js:97101
@@ -3,15 +3,10 @@
     await pl;
     return;
   }
-  if (((Lq = A), !wC8())) {
-    let Y = QN(),
-      z = "Sandbox dependencies are not available on this system.";
-    if (Y === "linux")
-      z += " Required: ripgrep (rg), bubblewrap (bwrap), and socat.";
-    else if (Y === "macos") z += " Required: ripgrep (rg).";
-    else z += ` Platform '${Y}' is not supported.`;
-    throw Error(z);
-  }
+  m5 = A;
+  let Y = sS8();
+  if (Y.errors.length > 0)
+    throw Error(`Sandbox dependencies not available: ${Y.errors.join(", ")}`);
   if (q && QN() === "macos")
     ((AeA = tk8(KeA.addViolation.bind(KeA), Lq.ignoreViolations)),
       C8("Started macOS sandbox log monitor"));

@@@ function 'Jk2' (was 'aZ2') — structural (46.3%)
--- pretty-v2.1.19.js:447757
+++ pretty-v2.1.20.js:458749
@@ -3,12 +3,22 @@
     Y = "claude/task";
   try {
     let z = oZ2.replace("{description}", A),
-      w = "<title>",
       J = (
         await J$({
           systemPrompt: [],
           userPrompt: z,
-          assistantPrompt: "<title>",
+          outputFormat: {
+            type: "json_schema",
+            schema: {
+              type: "object",
+              properties: {
+                title: { type: "string" },
+                branch: { type: "string" },
+              },
+              required: ["title", "branch"],
+              additionalProperties: !1,
+            },
+          },
           signal: K,
           options: {
             querySource: "teleport_generate_title",
@@ -20,13 +30,14 @@
         })
       ).message.content[0];
     if (J?.type !== "text") return { title: q, branchName: "claude/task" };
-    let X = "<title>" + J.text.trim(),
-      O = X.match(/<title>(.*?)<\/title>/s),
-      $ = X.match(/<branch>(.*?)<\/branch>/s);
-    return {
-      title: O?.[1]?.trim() || q,
-      branchName: $?.[1]?.trim() || "claude/task",
-    };
+    let J = a3(H.text.trim()),
+      O = U.object({ title: U.string(), branch: U.string() }).safeParse(J);
+    if (O.success)
+      return {
+        title: O.data.title || q,
+        branchName: O.data.branch || "claude/task",
+      };
+    return { title: q, branchName: "claude/task" };
   } catch (z) {
     return (
       qA(Error(`Error generating title and branch: ${z}`)),

@@@ function 'NIK' (was 'avK') — structural (46.1%)
--- pretty-v2.1.19.js:555609
+++ pretty-v2.1.20.js:560730
@@ -28,7 +28,7 @@
                 ...B,
                 toolPermissionContext: WY(B.toolPermissionContext, {
                   type: "setMode",
-                  mode: F,
+                  mode: og(Q),
                   destination: "session",
                 }),
               })),
@@ -75,43 +75,82 @@
       }
       if (j.length > 0 && o$(G.teamContext)) {
         h(`[InboxPoller] Found ${j.length} permission request(s)`);
-        let b = [];
+        let x = sj1(),
+          F = G.teamContext?.teamName;
         for (let Q of j) {
           let F = RG1(Q.text);
           if (!F) continue;
-          b.push({
-            id: F.requestId,
-            workerId: F.workerId,
-            workerName: F.workerName,
-            workerColor: F.workerColor,
-            teamName: G.teamContext?.teamName || "",
-            toolName: F.toolName,
-            toolUseId: F.toolUseId,
-            description: F.description,
-            input: F.input,
-            permissionSuggestions: F.permissionSuggestions,
-            status: "pending",
-            createdAt: F.createdAt,
-          });
-        }
-        if (b.length > 0) {
-          w((F) => ({
-            ...F,
-            workerPermissions: {
-              ...F.workerPermissions,
-              queue: [...F.workerPermissions.queue, ...b],
-            },
-          }));
-          let Q = b[0];
-          if (Q && !A && !K)
-            Bu(
-              {
-                message: `${Q.workerName} needs permission for ${Q.toolName}`,
-                notificationType: "worker_permission_prompt",
+          if (x) {
+            let a = GQ(Md(), d.toolName);
+            if (!a) {
+              h(
+                `[InboxPoller] Unknown tool ${d.toolName}, skipping permission request`,
+              );
+              continue;
+            }
+            let l = {
+              assistantMessage: zL({ content: "" }),
+              tool: a,
+              description: d.description,
+              input: d.input,
+              toolUseContext: {},
+              toolUseID: d.toolUseId,
+              permissionResult: { behavior: "ask", message: d.description },
+              permissionPromptStartTimeMs: Date.now(),
+              workerBadge: {
+                name: d.workerName,
+                color: d.workerColor || "cyan",
               },
-              H,
+              onUserInteraction() {},
+              onAbort() {
+                nj1(
+                  d.workerName,
+                  { decision: "rejected", resolvedBy: "leader" },
+                  d.requestId,
+                  F,
+                );
+              },
+              onAllow(e, JA) {
+                nj1(
+                  d.workerName,
+                  {
+                    decision: "approved",
+                    resolvedBy: "leader",
+                    updatedInput: e,
+                    permissionUpdates: JA,
+                  },
+                  d.requestId,
+                  F,
+                );
+              },
+              onReject(e) {
+                nj1(
+                  d.workerName,
+                  { decision: "rejected", resolvedBy: "leader", feedback: e },
+                  d.requestId,
+                  F,
+                );
+              },
+              async recheckPermission() {},
+            };
+            x((e) => {
+              if (e.some((JA) => JA.toolUseID === d.toolUseId)) return e;
+              return [...e, l];
+            });
+          } else
+            h(
+              `[InboxPoller] ToolUseConfirmQueue unavailable, dropping permission request from ${d.workerName}`,
             );
         }
+        let Q = bFA(M[0]?.text ?? "");
+        if (Q && !A && !K)
+          LB(
+            {
+              message: `${Q.workerName} needs permission for ${Q.toolName}`,
+              notificationType: "worker_permission_prompt",
+            },
+            H,
+          );
       }
       if (M.length > 0 && lz()) {
         h(`[InboxPoller] Found ${M.length} permission response(s)`);
@@ -232,7 +271,7 @@
               ...o,
               toolPermissionContext: WY(o.toolPermissionContext, {
                 type: "setMode",
-                mode: F,
+                mode: og(Q),
                 destination: "session",
               }),
             })));
@@ -303,9 +342,9 @@
       let S = x.map((b) => {
           let Q = b.color ? ` color="${b.color}"` : "",
             F = b.text;
-          return `<teammate-message teammate_id="${b.from}"${Q}>
+          return `<${IO} teammate_id="${x.from}"${F}>
 ${F}
-</teammate-message>`;
+</${IO}>`;
         }).join(`
 
 `),
@@ -358,9 +397,9 @@
     h(`[InboxPoller] Session idle, delivering ${j.length} pending message(s)`);
     let N = j.map((k) => {
       let R = k.color ? ` color="${k.color}"` : "";
-      return `<teammate-message teammate_id="${k.from}"${R}>
+      return `<${IO} teammate_id="${k.from}"${R}>
 ${k.text}
-</teammate-message>`;
+</${IO}>`;
     }).join(`
 
 `);

@@@ function 'uS8' (was 'dk8') — structural (45.9%)
--- pretty-v2.1.19.js:94491
+++ pretty-v2.1.20.js:96188
@@ -1,19 +1,13 @@
-function dk8(A = !1, K) {
-  try {
-    let q = uQ1("which", ["bwrap"], { stdio: "ignore", timeout: 1000 }),
-      Y = uQ1("which", ["socat"], { stdio: "ignore", timeout: 1000 }),
-      z = q.status === 0 && Y.status === 0;
-    if (!A) {
-      let w = xQ1(K?.bpfPath) !== null,
-        H = ttA(K?.applyPath) !== null;
-      if (!w || !H)
-        C8(
-          `[Sandbox Linux] Seccomp filtering not available (missing binaries for ${process.arch}). Sandbox will run without Unix socket blocking (allowAllUnixSockets mode). This is less restrictive but still provides filesystem and network isolation.`,
-          { level: "warn" },
-        );
-    }
-    return z;
-  } catch {
-    return !1;
-  }
+function uS8(A) {
+  let K = [],
+    q = [],
+    Y = Hd1("which", ["bwrap"], { stdio: "ignore", timeout: 1000 }),
+    z = Hd1("which", ["socat"], { stdio: "ignore", timeout: 1000 });
+  if (Y.status !== 0) K.push("bubblewrap (bwrap) not installed");
+  if (z.status !== 0) K.push("socat not installed");
+  let w = zd1(A?.bpfPath) !== null,
+    H = AkA(A?.applyPath) !== null;
+  if (!w || !H)
+    q.push("seccomp not available - unix socket access not restricted");
+  return { warnings: q, errors: K };
 }

@@@ function 'na2' (was 'jF2') — structural (45.7%)
--- pretty-v2.1.19.js:534265
+++ pretty-v2.1.20.js:539042
@@ -1,50 +1,60 @@
-function jF2() {
+async function na2() {
   let A = O9A(),
     K = { messages: 0, errors: 0 },
     q = _3A(),
     Y = hA();
   try {
-    if (!Y.existsSync(q)) return K;
-    let w = Y.readdirSync(q)
-      .filter((H) => H.isDirectory())
-      .map((H) => af(q, H.name));
+    let z;
+    try {
+      z = await Y.readdir(q);
+    } catch {
+      return K;
+    }
+    let w = z.filter((H) => H.isDirectory()).map((H) => NP(q, H.name));
     for (let H of w)
       try {
-        let J = Kg6(H, A, ".jsonl", Y);
-        if (
-          ((K.messages += J.messages), (K.errors += J.errors), Y.existsSync(H))
-        )
-          try {
-            let X = Y.readdirSync(H);
-            for (let O of X) {
-              if (!O.isDirectory()) continue;
-              let $ = af(H, O.name, JS6);
-              if (!Y.existsSync($)) continue;
-              try {
-                let _ = Y.readdirSync($);
-                for (let Z of _) {
-                  if (!Z.isDirectory()) continue;
-                  let G = af($, Z.name),
-                    W = Kg6(G, A, "", Y);
-                  ((K.messages += W.messages), (K.errors += W.errors));
-                  try {
-                    if (Y.isDirEmptySync(G)) Y.rmdirSync(G);
-                  } catch {}
-                }
+        let J = await fEK(H, A, ".jsonl", Y);
+        ((K.messages += J.messages), (K.errors += J.errors));
+        let O;
+        try {
+          O = await Y.readdir(H);
+        } catch {
+          continue;
+        }
+        try {
+          for (let X of O) {
+            if (!X.isDirectory()) continue;
+            let $ = NP(H, X.name, iG6),
+              _;
+            try {
+              _ = await Y.readdir($);
+            } catch {
+              continue;
+            }
+            try {
+              for (let Z of _) {
+                if (!Z.isDirectory()) continue;
+                let G = NP($, Z.name),
+                  W = await fEK(G, A, "", Y);
+                ((K.messages += W.messages), (K.errors += W.errors));
                 try {
-                  if (Y.isDirEmptySync($)) Y.rmdirSync($);
+                  await Y.rmdir(G);
                 } catch {}
-                try {
-                  let Z = af(H, O.name);
-                  if (Y.isDirEmptySync(Z)) Y.rmdirSync(Z);
-                } catch {}
+              }
+              try {
+                await Y.rmdir($);
+              } catch {}
+              try {
+                let Z = NP(H, X.name);
+                await Y.rmdir(Z);
               } catch {}
-            }
-          } catch {
-            K.errors++;
+            } catch {}
           }
+        } catch {
+          K.errors++;
+        }
         try {
-          if (Y.isDirEmptySync(H)) Y.rmdirSync(H);
+          await Y.rmdir(H);
         } catch {}
       } catch {
         K.errors++;

@@@ function 'ZUA' (was 'WFA') — structural (44.3%)
--- pretty-v2.1.19.js:430362
+++ pretty-v2.1.20.js:454347
@@ -8,17 +8,16 @@
   if (EW1(A)) return !1;
   if (A.isMeta) return !1;
   let K = A.message.content,
-    q =
-      typeof K === "string"
-        ? K.trim()
-        : K[K.length - 1]?.type === "text"
-          ? K[K.length - 1].text.trim()
-          : "";
+    q = typeof K === "string" ? null : K[K.length - 1],
+    Y = typeof K === "string" ? K.trim() : q && KwK(q) ? q.text.trim() : "";
   if (
-    q.indexOf("<local-command-stdout>") !== -1 ||
-    q.indexOf("<local-command-stderr>") !== -1 ||
-    q.indexOf("<bash-stdout>") !== -1 ||
-    q.indexOf("<bash-stderr>") !== -1
+    Y.indexOf(`<${l2A}>`) !== -1 ||
+    Y.indexOf(`<${mnA}>`) !== -1 ||
+    Y.indexOf(`<${va6}>`) !== -1 ||
+    Y.indexOf(`<${Ea6}>`) !== -1 ||
+    Y.indexOf(`<${yO}>`) !== -1 ||
+    Y.indexOf(`<${ql}>`) !== -1 ||
+    Y.indexOf(`<${IO}`) !== -1
   )
     return !1;
   return !0;

@@@ function 'kF6' (was 'mu6') — structural (44.0%)
--- pretty-v2.1.19.js:522134
+++ pretty-v2.1.20.js:526579
@@ -1,42 +1,50 @@
-function mu6() {
+async function kF6() {
   let A = _3A(),
     K = hA();
   try {
-    K.statSync(A);
+    await K.stat(A);
   } catch {
     return [];
   }
-  let q = K.readdirSync(A)
-      .filter((z) => z.isDirectory())
-      .map((z) => hN1(A, z.name)),
-    Y = [];
-  for (let z of q)
-    try {
-      let w = K.readdirSync(z),
-        H = w
-          .filter((X) => X.isFile() && X.name.endsWith(".jsonl"))
-          .map((X) => hN1(z, X.name));
-      Y.push(...H);
-      let J = w.filter((X) => X.isDirectory());
-      for (let X of J) {
-        let O = hN1(z, X.name, "subagents");
+  let Y = (await K.readdir(A))
+    .filter((w) => w.isDirectory())
+    .map((w) => Sv1(A, w.name));
+  return (
+    await Promise.all(
+      Y.map(async (w) => {
         try {
-          let $ = K.readdirSync(O)
-            .filter(
-              (_) =>
-                _.isFile() &&
-                _.name.endsWith(".jsonl") &&
-                _.name.startsWith("agent-"),
-            )
-            .map((_) => hN1(O, _.name));
-          Y.push(...$);
-        } catch {}
-      }
-    } catch (w) {
-      h(
-        `Failed to read project directory ${z}: ${w instanceof Error ? w.message : String(w)}`,
-      );
-      continue;
-    }
-  return Y;
+          let H = await K.readdir(w),
+            J = H.filter(($) => $.isFile() && $.name.endsWith(".jsonl")).map(
+              ($) => Sv1(w, $.name),
+            ),
+            O = H.filter(($) => $.isDirectory()),
+            X = await Promise.all(
+              O.map(async ($) => {
+                let _ = Sv1(w, $.name, "subagents");
+                try {
+                  return (await K.readdir(_))
+                    .filter(
+                      (G) =>
+                        G.isFile() &&
+                        G.name.endsWith(".jsonl") &&
+                        G.name.startsWith("agent-"),
+                    )
+                    .map((G) => Sv1(_, G.name));
+                } catch {
+                  return [];
+                }
+              }),
+            );
+          return [...J, ...X.flat()];
+        } catch (H) {
+          return (
+            h(
+              `Failed to read project directory ${w}: ${H instanceof Error ? H.message : String(H)}`,
+            ),
+            []
+          );
+        }
+      }),
+    )
+  ).flat();
 }

@@@ function 'c8K' (was 'G4K') — structural (44.0%)
--- pretty-v2.1.19.js:436325
+++ pretty-v2.1.20.js:413942
@@ -2,24 +2,8 @@
   switch (A.operation) {
     case "spawnTeam":
       return `create team: ${A.team_name}`;
-    case "write": {
-      let K = A.value ? `: "${MY(String(A.value), 50)}"` : "";
-      return `send message to: ${A.target_agent_id}${K}`;
-    }
-    case "broadcast":
-      return `broadcast message to all teammates${A.value ? `: "${MY(String(A.value), 50)}"` : ""}`;
     case "cleanup":
-      return `cleanup team: ${A.team_name || "current"}`;
-    case "requestShutdown":
-      return `request shutdown: ${A.target_agent_id}`;
-    case "approveShutdown":
-      return "approve shutdown";
-    case "rejectShutdown":
-      return `reject shutdown: ${A.reason || "no reason"}`;
-    case "approvePlan":
-      return `approve plan from: ${A.target_agent_id}`;
-    case "rejectPlan":
-      return `reject plan from: ${A.target_agent_id}`;
+      return null;
     case "discoverTeams":
       return "discover available teams";
     case "requestJoin":

@@@ function 'eVK' (was 'QGK') — structural (43.8%)
--- pretty-v2.1.19.js:517783
+++ pretty-v2.1.20.js:521950
@@ -1,46 +1,53 @@
 function QGK(A) {
-  let K = a(34),
-    { onComplete: q } = A,
+  let K = s(43),
+    { onComplete: q, depCheck: Y } = A,
     [Y] = p4(),
     z = l8.isSandboxingEnabled(),
     w = l8.isAutoAllowBashIfSandboxedEnabled(),
+    J = Y.warnings.length > 0,
+    O;
+  if (K[0] === Symbol.for("react.memo_cache_sentinel"))
+    ((O = X8()), (K[0] = O));
+  else O = K[0];
+  let $ = O.sandbox?.network?.allowAllUnixSockets,
+    _ = J && !$,
     J = (() => {
       if (!z) return "disabled";
       if (w) return "auto-allow";
       return "regular";
     })(),
     X;
-  if (K[0] !== Y) ((X = F8("success", Y)("(current)")), (K[0] = Y), (K[1] = X));
-  else X = K[1];
+  if (K[1] !== z) ((W = U8("success", z)("(current)")), (K[1] = z), (K[2] = W));
+  else W = K[2];
   let O = X,
     $ =
       J === "auto-allow"
         ? `Sandbox BashTool, with auto-allow ${O}`
         : "Sandbox BashTool, with auto-allow",
     _;
-  if (K[2] !== $)
-    ((_ = { label: $, value: "auto-allow" }), (K[2] = $), (K[3] = _));
-  else _ = K[3];
+  if (K[3] !== M)
+    ((j = { label: M, value: "auto-allow" }), (K[3] = M), (K[4] = j));
+  else j = K[4];
   let Z =
       J === "regular"
         ? `Sandbox BashTool, with regular permissions ${O}`
         : "Sandbox BashTool, with regular permissions",
     G;
-  if (K[4] !== Z)
-    ((G = { label: Z, value: "regular" }), (K[4] = Z), (K[5] = G));
-  else G = K[5];
+  if (K[5] !== P)
+    ((V = { label: P, value: "regular" }), (K[5] = P), (K[6] = V));
+  else V = K[6];
   let W = J === "disabled" ? `No Sandbox ${O}` : "No Sandbox",
     D;
-  if (K[6] !== W)
-    ((D = { label: W, value: "disabled" }), (K[6] = W), (K[7] = D));
-  else D = K[7];
+  if (K[7] !== N)
+    ((T = { label: N, value: "disabled" }), (K[7] = N), (K[8] = T));
+  else T = K[8];
   let j;
-  if (K[8] !== _ || K[9] !== G || K[10] !== D)
-    ((j = [_, G, D]), (K[8] = _), (K[9] = G), (K[10] = D), (K[11] = j));
-  else j = K[11];
+  if (K[9] !== j || K[10] !== V || K[11] !== T)
+    ((k = [j, V, T]), (K[9] = j), (K[10] = V), (K[11] = T), (K[12] = k));
+  else k = K[12];
   let M = j,
     P;
-  if (K[12] !== q)
+  if (K[13] !== q)
     ((P = async function (l) {
       let e = l;
       A: switch (e) {
@@ -68,50 +75,64 @@
             q("○ Sandbox disabled"));
       }
     }),
-      (K[12] = q),
-      (K[13] = P));
-  else P = K[13];
+      (K[13] = q),
+      (K[14] = b));
+  else b = K[14];
   let V = P,
     N;
-  if (K[14] !== q)
-    ((N = () => {
-      q();
-    }),
-      (K[14] = q),
-      (K[15] = N));
-  else N = K[15];
-  let T = N,
-    k;
-  if (K[16] === Symbol.for("react.memo_cache_sentinel"))
-    ((k = { context: "Confirmation" }), (K[16] = k));
+  if (K[15] !== q)
+    ((B = { "confirm:no": () => q(void 0, { display: "skip" }) }),
+      (K[15] = q),
+      (K[16] = B));
   else k = K[16];
-  i1("confirm:no", T, k);
   let R;
   if (K[17] === Symbol.for("react.memo_cache_sentinel"))
+    ((x = { context: "Settings" }), (K[17] = x));
+  else x = K[17];
+  X7(B, x);
+  let F;
+  if (K[18] !== _)
+    ((F =
+      _ &&
+      v0.default.createElement(
+        I,
+        { marginBottom: 1 },
+        v0.default.createElement(
+          f,
+          { color: "warning" },
+          "Cannot block unix domain sockets (see Dependencies tab)",
+        ),
+      )),
+      (K[18] = _),
+      (K[19] = F));
+  else F = K[19];
+  let Q;
+  if (K[20] === Symbol.for("react.memo_cache_sentinel"))
     ((R = LW.default.createElement(
       I,
       { marginBottom: 1 },
       LW.default.createElement(f, { bold: !0 }, "Configure Mode:"),
     )),
-      (K[17] = R));
-  else R = K[17];
+      (K[20] = Q));
+  else Q = K[20];
   let x;
-  if (K[18] !== q) ((x = () => q()), (K[18] = q), (K[19] = x));
-  else x = K[19];
+  if (K[21] !== q)
+    ((u = () => q(void 0, { display: "skip" })), (K[21] = q), (K[22] = u));
+  else u = K[22];
   let S;
-  if (K[20] !== V || K[21] !== M || K[22] !== x)
+  if (K[23] !== S || K[24] !== R || K[25] !== u)
     ((S = LW.default.createElement(T6, {
       options: M,
       onChange: V,
       onCancel: x,
     })),
-      (K[20] = V),
-      (K[21] = M),
-      (K[22] = x),
-      (K[23] = S));
-  else S = K[23];
+      (K[23] = S),
+      (K[24] = R),
+      (K[25] = u),
+      (K[26] = d));
+  else d = K[26];
   let g;
-  if (K[24] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[27] === Symbol.for("react.memo_cache_sentinel"))
     ((g = LW.default.createElement(
       f,
       { dimColor: !0 },
@@ -123,10 +144,10 @@
       " ",
       "Commands will try to run in the sandbox automatically, and attempts to run outside of the sandbox fallback to regular permissions. Explicit ask/deny rules are always respected.",
     )),
-      (K[24] = g));
-  else g = K[24];
+      (K[27] = a));
+  else a = K[27];
   let b;
-  if (K[25] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[28] === Symbol.for("react.memo_cache_sentinel"))
     ((b = LW.default.createElement(
       I,
       { flexDirection: "column", marginTop: 1, gap: 1 },
@@ -143,10 +164,10 @@
         ),
       ),
     )),
-      (K[25] = b));
-  else b = K[25];
+      (K[28] = l));
+  else l = K[28];
   let Q;
-  if (K[26] !== S)
+  if (K[29] !== F || K[30] !== d)
     ((Q = LW.default.createElement(
       uJ,
       { key: "mode", title: "Mode" },
@@ -156,32 +177,76 @@
         R,
         S,
         b,
+        l,
       ),
     )),
-      (K[26] = S),
-      (K[27] = Q));
-  else Q = K[27];
-  let F;
-  if (K[28] !== q)
+      (K[29] = F),
+      (K[30] = d),
+      (K[31] = e));
+  else e = K[31];
+  let JA = e,
+    OA;
+  if (K[32] !== q)
     ((F = LW.default.createElement(
       uJ,
       { key: "overrides", title: "Overrides" },
       LW.default.createElement(gGK, { onComplete: q }),
     )),
-      (K[28] = q),
-      (K[29] = F));
-  else F = K[29];
-  let B;
-  if (K[30] === Symbol.for("react.memo_cache_sentinel"))
+      (K[32] = q),
+      (K[33] = OA));
+  else OA = K[33];
+  let HA = OA,
+    DA;
+  if (K[34] === Symbol.for("react.memo_cache_sentinel"))
     ((B = LW.default.createElement(
       uJ,
       { key: "config", title: "Config" },
       LW.default.createElement(uGK, null),
     )),
-      (K[30] = B));
-  else B = K[30];
-  let d;
-  if (K[31] !== Q || K[32] !== F)
+      (K[34] = DA));
+  else DA = K[34];
+  let o = DA,
+    _A = Y.errors.length > 0,
+    PA;
+  if (
+    K[35] !== Y ||
+    K[36] !== _A ||
+    K[37] !== J ||
+    K[38] !== JA ||
+    K[39] !== HA
+  )
+    ((PA = _A
+      ? [
+          v0.default.createElement(
+            MH,
+            { key: "dependencies", title: "Dependencies" },
+            v0.default.createElement(HF6, { depCheck: Y }),
+          ),
+        ]
+      : [
+          JA,
+          ...(J
+            ? [
+                v0.default.createElement(
+                  MH,
+                  { key: "dependencies", title: "Dependencies" },
+                  v0.default.createElement(HF6, { depCheck: Y }),
+                ),
+              ]
+            : []),
+          HA,
+          o,
+        ]),
+      (K[35] = Y),
+      (K[36] = _A),
+      (K[37] = J),
+      (K[38] = JA),
+      (K[39] = HA),
+      (K[40] = PA));
+  else PA = K[40];
+  let jA = PA,
+    yA;
+  if (K[41] !== jA)
     ((d = LW.default.createElement(
       I,
       { flexDirection: "column" },
@@ -189,13 +254,10 @@
         GL,
         { title: "Sandbox:", color: "permission", defaultTab: "Mode" },
         Q,
-        F,
-        B,
       ),
     )),
-      (K[31] = Q),
-      (K[32] = F),
-      (K[33] = d));
-  else d = K[33];
+      (K[41] = jA),
+      (K[42] = yA));
+  else yA = K[42];
   return d;
 }

@@@ function 'wE1' (was 'wT1') — structural (43.7%)
--- pretty-v2.1.19.js:533287
+++ pretty-v2.1.20.js:538059
@@ -2,13 +2,8 @@
   try {
     let q = hg2(A);
     if (q) Ig2(q, { recursive: !0 });
-    return (Sg2(A, K, "utf8"), h(`Settings sync: Wrote ${A}`), !0);
-  } catch (q) {
-    return (
-      h(
-        `Settings sync: Failed to write ${A} - ${q instanceof Error ? q.message : "unknown error"}`,
-      ),
-      !1
-    );
+    return (Oa2(A, K, "utf8"), L8("info", "settings_sync_file_written"), !0);
+  } catch {
+    return (L8("warn", "settings_sync_file_write_failed"), !1);
   }
 }

@@@ function 'LRK' (was 'qTK') — structural (43.3%)
--- pretty-v2.1.19.js:549996
+++ pretty-v2.1.20.js:555104
@@ -1,5 +1,5 @@
 function qTK(A) {
-  let K = a(47),
+  let K = s(53),
     {
       filePath: q,
       hunks: Y,
@@ -12,52 +12,66 @@
     O;
   A: {
     if (!q) {
+      let b;
+      if (K[0] === Symbol.for("react.memo_cache_sentinel"))
+        ((b = { firstLine: null, fileContent: void 0 }), (K[0] = b));
+      else b = K[0];
       O = null;
       break A;
     }
-    let V;
-    if (K[0] !== q) {
+    let N, T;
+    if (K[1] !== q) {
       let N = Ad2(m1(), q);
-      ((V =
-        IjK(N)?.split(`
+      ((N = oTK(b)),
+        (T =
+          N?.split(`
 `)[0] ?? null),
-        (K[0] = q),
-        (K[1] = V));
-    } else V = K[1];
+        (K[1] = q),
+        (K[2] = N),
+        (K[3] = T));
+    } else ((N = K[2]), (T = K[3]));
+    let k = N ?? void 0,
+      R;
+    if (K[4] !== T || K[5] !== k)
+      ((R = { firstLine: T, fileContent: k }),
+        (K[4] = T),
+        (K[5] = k),
+        (K[6] = R));
+    else R = K[6];
     O = V;
   }
-  let $ = O;
+  let { firstLine: $, fileContent: _ } = X;
   if (J) {
     let V;
-    if (K[2] !== q)
+    if (K[7] !== q)
       ((V = Az.default.createElement(f, { bold: !0 }, q)),
-        (K[2] = q),
-        (K[3] = V));
-    else V = K[3];
+        (K[7] = q),
+        (K[8] = N));
+    else N = K[8];
     let N;
-    if (K[4] === Symbol.for("react.memo_cache_sentinel"))
+    if (K[9] === Symbol.for("react.memo_cache_sentinel"))
       ((N = Az.default.createElement(f, { dimColor: !0 }, " (untracked)")),
-        (K[4] = N));
-    else N = K[4];
+        (K[9] = T));
+    else T = K[9];
     let T;
-    if (K[5] !== V)
-      ((T = Az.default.createElement(I, null, V, N)), (K[5] = V), (K[6] = T));
-    else T = K[6];
+    if (K[10] !== N)
+      ((k = zz.default.createElement(I, null, N, T)), (K[10] = N), (K[11] = k));
+    else k = K[11];
     let k;
-    if (K[7] === Symbol.for("react.memo_cache_sentinel"))
-      ((k = Az.default.createElement(Qt, { padding: 4 })), (K[7] = k));
-    else k = K[7];
+    if (K[12] === Symbol.for("react.memo_cache_sentinel"))
+      ((R = zz.default.createElement(We, { padding: 4 })), (K[12] = R));
+    else R = K[12];
     let R;
-    if (K[8] === Symbol.for("react.memo_cache_sentinel"))
+    if (K[13] === Symbol.for("react.memo_cache_sentinel"))
       ((R = Az.default.createElement(
         f,
         { dimColor: !0, italic: !0 },
         "New file not yet staged.",
       )),
-        (K[8] = R));
-    else R = K[8];
+        (K[13] = b));
+    else b = K[13];
     let x;
-    if (K[9] !== q)
+    if (K[14] !== q)
       ((x = Az.default.createElement(
         I,
         { flexDirection: "column" },
@@ -70,11 +84,11 @@
           "` to see line counts.",
         ),
       )),
-        (K[9] = q),
-        (K[10] = x));
-    else x = K[10];
+        (K[14] = q),
+        (K[15] = S));
+    else S = K[15];
     let S;
-    if (K[11] !== T || K[12] !== x)
+    if (K[16] !== k || K[17] !== S)
       ((S = Az.default.createElement(
         I,
         { flexDirection: "column", width: "100%" },
@@ -82,29 +96,29 @@
         k,
         x,
       )),
-        (K[11] = T),
-        (K[12] = x),
-        (K[13] = S));
-    else S = K[13];
+        (K[16] = k),
+        (K[17] = S),
+        (K[18] = B));
+    else B = K[18];
     return S;
   }
   if (w) {
     let V;
-    if (K[14] !== q)
+    if (K[19] !== q)
       ((V = Az.default.createElement(
         I,
         null,
         Az.default.createElement(f, { bold: !0 }, q),
       )),
-        (K[14] = q),
-        (K[15] = V));
-    else V = K[15];
+        (K[19] = q),
+        (K[20] = N));
+    else N = K[20];
     let N;
-    if (K[16] === Symbol.for("react.memo_cache_sentinel"))
-      ((N = Az.default.createElement(Qt, { padding: 4 })), (K[16] = N));
-    else N = K[16];
+    if (K[21] === Symbol.for("react.memo_cache_sentinel"))
+      ((T = zz.default.createElement(We, { padding: 4 })), (K[21] = T));
+    else T = K[21];
     let T;
-    if (K[17] === Symbol.for("react.memo_cache_sentinel"))
+    if (K[22] === Symbol.for("react.memo_cache_sentinel"))
       ((T = Az.default.createElement(
         I,
         { flexDirection: "column" },
@@ -114,10 +128,10 @@
           "Binary file - cannot display diff",
         ),
       )),
-        (K[17] = T));
-    else T = K[17];
+        (K[22] = k));
+    else k = K[22];
     let k;
-    if (K[18] !== V)
+    if (K[23] !== N)
       ((k = Az.default.createElement(
         I,
         { flexDirection: "column", width: "100%" },
@@ -125,28 +139,28 @@
         N,
         T,
       )),
-        (K[18] = V),
-        (K[19] = k));
-    else k = K[19];
+        (K[23] = N),
+        (K[24] = R));
+    else R = K[24];
     return k;
   }
   if (z) {
     let V;
-    if (K[20] !== q)
+    if (K[25] !== q)
       ((V = Az.default.createElement(
         I,
         null,
         Az.default.createElement(f, { bold: !0 }, q),
       )),
-        (K[20] = q),
-        (K[21] = V));
-    else V = K[21];
+        (K[25] = q),
+        (K[26] = N));
+    else N = K[26];
     let N;
-    if (K[22] === Symbol.for("react.memo_cache_sentinel"))
-      ((N = Az.default.createElement(Qt, { padding: 4 })), (K[22] = N));
-    else N = K[22];
+    if (K[27] === Symbol.for("react.memo_cache_sentinel"))
+      ((T = zz.default.createElement(We, { padding: 4 })), (K[27] = T));
+    else T = K[27];
     let T;
-    if (K[23] === Symbol.for("react.memo_cache_sentinel"))
+    if (K[28] === Symbol.for("react.memo_cache_sentinel"))
       ((T = Az.default.createElement(
         I,
         { flexDirection: "column" },
@@ -156,10 +170,10 @@
           "Large file - diff exceeds 1 MB limit",
         ),
       )),
-        (K[23] = T));
-    else T = K[23];
+        (K[28] = k));
+    else k = K[28];
     let k;
-    if (K[24] !== V)
+    if (K[29] !== N)
       ((k = Az.default.createElement(
         I,
         { flexDirection: "column", width: "100%" },
@@ -167,36 +181,36 @@
         N,
         T,
       )),
-        (K[24] = V),
-        (K[25] = k));
-    else k = K[25];
+        (K[29] = N),
+        (K[30] = R));
+    else R = K[30];
     return k;
   }
   let _;
-  if (K[26] !== q)
+  if (K[31] !== q)
     ((_ = Az.default.createElement(f, { bold: !0 }, q)),
-      (K[26] = q),
-      (K[27] = _));
-  else _ = K[27];
+      (K[31] = q),
+      (K[32] = Z));
+  else Z = K[32];
   let Z;
-  if (K[28] !== H)
+  if (K[33] !== H)
     ((Z = H && Az.default.createElement(f, { dimColor: !0 }, " (truncated)")),
-      (K[28] = H),
-      (K[29] = Z));
-  else Z = K[29];
+      (K[33] = H),
+      (K[34] = G));
+  else G = K[34];
   let G;
-  if (K[30] !== _ || K[31] !== Z)
+  if (K[35] !== Z || K[36] !== G)
     ((G = Az.default.createElement(I, null, _, Z)),
-      (K[30] = _),
-      (K[31] = Z),
-      (K[32] = G));
-  else G = K[32];
+      (K[35] = Z),
+      (K[36] = G),
+      (K[37] = W));
+  else W = K[37];
   let W;
-  if (K[33] === Symbol.for("react.memo_cache_sentinel"))
-    ((W = Az.default.createElement(Qt, { padding: 4 })), (K[33] = W));
-  else W = K[33];
+  if (K[38] === Symbol.for("react.memo_cache_sentinel"))
+    ((D = zz.default.createElement(We, { padding: 4 })), (K[38] = D));
+  else D = K[38];
   let D;
-  if (K[34] !== X || K[35] !== q || K[36] !== $ || K[37] !== Y)
+  if (K[39] !== O || K[40] !== _ || K[41] !== q || K[42] !== $ || K[43] !== Y)
     ((D =
       Y.length === 0
         ? Az.default.createElement(f, { dimColor: !0 }, "No diff content")
@@ -206,24 +220,26 @@
               patch: V,
               filePath: q,
               firstLine: $,
+              fileContent: _,
               dim: !1,
               width: X - 2 - 2,
             }),
           )),
-      (K[34] = X),
-      (K[35] = q),
-      (K[36] = $),
-      (K[37] = Y),
-      (K[38] = D));
-  else D = K[38];
+      (K[39] = O),
+      (K[40] = _),
+      (K[41] = q),
+      (K[42] = $),
+      (K[43] = Y),
+      (K[44] = M));
+  else M = K[44];
   let j;
-  if (K[39] !== D)
+  if (K[45] !== M)
     ((j = Az.default.createElement(I, { flexDirection: "column" }, D)),
-      (K[39] = D),
-      (K[40] = j));
-  else j = K[40];
+      (K[45] = M),
+      (K[46] = j));
+  else j = K[46];
   let M;
-  if (K[41] !== H)
+  if (K[47] !== H)
     ((M =
       H &&
       Az.default.createElement(
@@ -231,11 +247,11 @@
         { dimColor: !0, italic: !0 },
         "… diff truncated (exceeded 400 line limit)",
       )),
-      (K[41] = H),
-      (K[42] = M));
-  else M = K[42];
+      (K[47] = H),
+      (K[48] = P));
+  else P = K[48];
   let P;
-  if (K[43] !== G || K[44] !== j || K[45] !== M)
+  if (K[49] !== W || K[50] !== j || K[51] !== P)
     ((P = Az.default.createElement(
       I,
       { flexDirection: "column", width: "100%" },
@@ -244,10 +260,10 @@
       j,
       M,
     )),
-      (K[43] = G),
-      (K[44] = j),
-      (K[45] = M),
-      (K[46] = P));
-  else P = K[46];
+      (K[49] = W),
+      (K[50] = j),
+      (K[51] = P),
+      (K[52] = V));
+  else V = K[52];
   return P;
 }

@@@ function 'vO2' (was 'bnY') — structural (43.3%)
--- pretty-v2.1.19.js:363253
+++ pretty-v2.1.20.js:388376
@@ -1,12 +1,14 @@
 function bnY(A) {
-  let K = a(23),
-    { task: q, ownerColor: Y, openBlockers: z } = A,
+  let K = s(27),
+    { task: q, ownerColor: Y, openBlockers: z, activity: w } = A,
     w = q.status === "completed",
     H = q.status === "in_progress",
+    O = z.length > 0,
     J;
   if (K[0] !== q.status) ((J = hnY(q.status)), (K[0] = q.status), (K[1] = J));
   else J = K[1];
   let { icon: X, color: O } = J,
+    Z = J && !O && w,
     $;
   if (K[2] !== O || K[3] !== X)
     (($ = Q3.createElement(f, { color: O }, X, " ")),
@@ -14,45 +16,39 @@
       (K[3] = X),
       (K[4] = $));
   else $ = K[4];
-  let _;
-  if (K[5] !== q.id)
-    ((_ = Q3.createElement(f, { dimColor: !0 }, "#", q.id, " ")),
-      (K[5] = q.id),
-      (K[6] = _));
-  else _ = K[6];
-  let Z = w || z.length > 0,
+  let W = H || O,
     G;
-  if (K[7] !== w || K[8] !== H || K[9] !== Z || K[10] !== q.subject)
+  if (K[5] !== H || K[6] !== J || K[7] !== W || K[8] !== q.subject)
     ((G = Q3.createElement(
       f,
       { bold: H, strikethrough: w, dimColor: Z },
       q.subject,
     )),
+      (K[5] = H),
+      (K[6] = J),
       (K[7] = w),
-      (K[8] = H),
-      (K[9] = Z),
-      (K[10] = q.subject),
-      (K[11] = G));
-  else G = K[11];
+      (K[8] = q.subject),
+      (K[9] = D));
+  else D = K[9];
   let W;
-  if (K[12] !== Y || K[13] !== q.owner)
+  if (K[10] !== Y || K[11] !== q.owner)
     ((W =
       q.owner &&
       Q3.createElement(
         f,
-        null,
+        { dimColor: !0 },
         " (",
-        Y ? Q3.createElement(f, { color: Y }, q.owner) : q.owner,
+        Y ? hK.createElement(f, { color: Y }, "@", q.owner) : `@${q.owner}`,
         ")",
       )),
-      (K[12] = Y),
-      (K[13] = q.owner),
-      (K[14] = W));
-  else W = K[14];
+      (K[10] = Y),
+      (K[11] = q.owner),
+      (K[12] = M));
+  else M = K[12];
   let D;
-  if (K[15] !== z)
+  if (K[13] !== O || K[14] !== z)
     ((D =
-      z.length > 0 &&
+      O &&
       Q3.createElement(
         f,
         { dimColor: !0 },
@@ -62,18 +58,38 @@
         " ",
         [...z].sort(BnY).map(xnY).join(", "),
       )),
-      (K[15] = z),
-      (K[16] = D));
-  else D = K[16];
+      (K[13] = O),
+      (K[14] = z),
+      (K[15] = j));
+  else j = K[15];
   let j;
-  if (K[17] !== $ || K[18] !== _ || K[19] !== G || K[20] !== W || K[21] !== D)
-    ((j = Q3.createElement(I, null, $, _, G, W, D)),
+  if (K[16] !== G || K[17] !== D || K[18] !== M || K[19] !== j)
+    ((P = hK.createElement(I, null, G, D, M, j)),
+      (K[16] = G),
       (K[17] = $),
       (K[18] = _),
       (K[19] = G),
-      (K[20] = W),
+      (K[20] = P));
+  else P = K[20];
+  let V;
+  if (K[21] !== w || K[22] !== Z)
+    ((V =
+      Z &&
+      hK.createElement(
+        I,
+        null,
+        hK.createElement(f, { dimColor: !0 }, "  ", w, K1.ellipsis),
+      )),
       (K[21] = D),
-      (K[22] = j));
-  else j = K[22];
+      (K[22] = Z),
+      (K[23] = V));
+  else V = K[23];
+  let N;
+  if (K[24] !== P || K[25] !== V)
+    ((N = hK.createElement(I, { flexDirection: "column" }, P, V)),
+      (K[24] = P),
+      (K[25] = V),
+      (K[26] = N));
+  else N = K[26];
   return j;
 }

@@@ function 'ra2' (was 'Kg6') — structural (41.7%)
--- pretty-v2.1.19.js:534247
+++ pretty-v2.1.20.js:539109
@@ -1,16 +1,26 @@
-function Kg6(A, K, q, Y) {
-  let z = { messages: 0, errors: 0 };
-  if (!Y.existsSync(A)) return z;
-  let H = Y.readdirSync(A).filter((J) => J.isFile() && J.name.endsWith(q));
-  for (let J of H)
+async function ra2(A, K, q = !0) {
+  let Y = B9A(),
+    z = { messages: 0, errors: 0 },
+    w = uA();
+  try {
+    let H;
     try {
-      let X = af(A, J.name);
-      if (Y.statSync(X).mtime < K) (Y.unlinkSync(X), z.messages++);
+      H = await w.readdir(A);
     } catch {
-      z.errors++;
+      return z;
     }
-  try {
-    if (Y.isDirEmptySync(A)) Y.rmdirSync(A);
+    let J = H.filter((O) => O.isFile() && O.name.endsWith(K));
+    for (let O of J)
+      try {
+        let X = NP(A, O.name);
+        if ((await w.stat(X)).mtime < Y) (await w.unlink(X), z.messages++);
+      } catch {
+        z.errors++;
+      }
+    if (q)
+      try {
+        await w.rmdir(A);
+      } catch {}
   } catch {
     z.errors++;
   }

@@@ function 'oT2' (was 'X_2') — structural (41.6%)
--- pretty-v2.1.19.js:437161
+++ pretty-v2.1.20.js:448322
@@ -1,17 +1,16 @@
-function X_2(A, K) {
-  let { reason: q } = A,
-    Y = A.team_name || j9();
-  if (!q)
+function oT2(A) {
+  let K = e3(),
+    q = I9() || "teammate";
+  if (!A.request_id)
     throw Error(
-      "reason is required for rejectShutdown operation to explain why shutdown is declined",
+      "request_id is required for shutdown response. Use the requestId from the shutdown_request message.",
     );
-  let z = PY() || "teammate";
-  if (!A.request_id)
+  if (!A.content)
     throw Error(
-      "request_id is required for rejectShutdown. Use the requestId from the shutdown_request message.",
+      "content (reason) is required when rejecting a shutdown request to explain why shutdown is declined",
     );
   let w = A.request_id,
-    H = Vv6({ requestId: w, from: z, reason: q });
+    z = bR6({ requestId: Y, from: q, reason: A.content });
   return (
     U3(
       ZH,
@@ -26,8 +25,8 @@
     {
       data: {
         success: !0,
-        message: `Shutdown rejected. Reason: "${q}". Continuing to work.`,
-        requestId: w,
+        message: `Shutdown rejected. Reason: "${A.content}". Continuing to work.`,
+        request_id: Y,
       },
     }
   );

@@@ function 'Vb2' (was 'c62') — structural (41.3%)
--- pretty-v2.1.19.js:387585
+++ pretty-v2.1.20.js:482597
@@ -1,8 +1,8 @@
 function c62(A) {
-  let K = A.lastIndexOf("/");
+  let K = A.indexOf(D$K);
+  if (K === -1) return A;
+  let q = K + D$K.length,
+    Y = A.indexOf(Pb2, q);
   if (K === -1) return A;
-  let q = A.slice(0, K),
-    Y = A.slice(K + 1),
-    z = Yp7(Y);
-  return `${q}/${z}`;
+  return A.slice(q, Y);
 }

@@@ function 'iT2' (was 'w_2') — structural (41.1%)
--- pretty-v2.1.19.js:436958
+++ pretty-v2.1.20.js:448159
@@ -1,22 +1,19 @@
 async function w_2(A, K) {
-  let { getAppState: q } = K,
-    Y = await q(),
-    z = A.team_name || j9(Y.teamContext);
+  let q = await K.getAppState(),
+    Y = e3(q.teamContext);
   if (!z)
     throw Error(
-      "team_name is required for broadcast operation. Either provide team_name in input, set CLAUDE_CODE_TEAM_NAME, or create a team with spawnTeam first.",
+      "Not in a team context. Create a team with Teammate spawnTeam first, or set CLAUDE_CODE_TEAM_NAME.",
     );
-  if (A.value === void 0)
-    throw Error("value is required for broadcast operation");
+  if (!A.content) throw Error("content is required for broadcast type");
   let w = Cz(z);
   if (!w) throw Error(`Team "${z}" does not exist`);
-  let H = PY() || A.name;
+  let w = I9() || (p2() ? "teammate" : T2);
   if (!H)
     throw Error(
-      'Cannot broadcast: sender name is required. Provide "name" parameter or set CLAUDE_CODE_AGENT_NAME.',
+      "Cannot broadcast: sender name is required. Set CLAUDE_CODE_AGENT_NAME.",
     );
-  let J = A.key ? `[${A.key}] ${A.value}` : String(A.value),
-    X = l0(),
+  let H = VJ(),
     O = [];
   for (let $ of w.members) {
     if ($.name.toLowerCase() === H.toLowerCase()) continue;
@@ -26,25 +23,26 @@
     return {
       data: {
         success: !0,
-        operation: "broadcast",
-        notifiedCount: 0,
+        message: "No teammates to broadcast to (you are the only team member)",
         recipients: [],
-        message: "No teammates to broadcast to (you are the only team member)",
       },
     };
   for (let $ of O)
     U3(
       $,
-      { from: H, text: J, timestamp: new Date().toISOString(), color: X },
+      {
+        from: w,
+        text: A.content,
+        timestamp: new Date().toISOString(),
+        color: H,
+      },
       z,
     );
   return {
     data: {
       success: !0,
-      operation: "broadcast",
-      notifiedCount: O.length,
+      message: `Message broadcast to ${J.length} teammate(s): ${J.join(", ")}`,
       recipients: O,
-      message: `Message broadcast to ${O.length} teammate(s): ${O.join(", ")}`,
     },
   };
 }

@@@ function 'lT2' (was 'z_2') — structural (41.0%)
--- pretty-v2.1.19.js:436930
+++ pretty-v2.1.20.js:448134
@@ -1,28 +1,25 @@
 async function z_2(A, K) {
-  let { getAppState: q } = K,
-    Y = await q(),
-    z = A.team_name || j9(Y.teamContext),
-    w = PY() || A.name || (lz() ? "teammate" : ZH);
-  if (!A.target_agent_id)
+  let q = await K.getAppState(),
+    Y = e3(q.teamContext),
+    z = I9() || (p2() ? "teammate" : T2);
+  if (!A.recipient)
     throw Error(
-      "target_agent_id is required for write operation to specify the recipient",
+      "recipient is required for message type to specify who to send to",
     );
-  let H = v4K(A.target_agent_id),
-    J = A.key ? `[${A.key}] ${A.value}` : String(A.value),
+  if (!A.content) throw Error("content is required for message type");
+  let w = g2K(A.recipient),
     X = l0();
   return (
     U3(
       H,
-      { from: w, text: J, timestamp: new Date().toISOString(), color: X },
+      {
+        from: z,
+        text: A.content,
+        timestamp: new Date().toISOString(),
+        color: H,
+      },
       z,
     ),
-    {
-      data: {
-        success: !0,
-        operation: "write",
-        notifiedCount: 1,
-        message: `Message sent to ${H}'s inbox`,
-      },
-    }
+    { data: { success: !0, message: `Message sent to ${w}'s inbox` } }
   );
 }

@@@ function 'sCK' (was 'IfK') — structural (40.5%)
--- pretty-v2.1.19.js:545426
+++ pretty-v2.1.20.js:550384
@@ -1,44 +1,33 @@
 function IfK(A, K, q, Y, z) {
-  let w = a(28),
-    [H, J] = yL.useState(0),
+  let [w, H] = L0.useState(0),
     [X, O] = yL.useState(void 0),
     $ = yL.useRef(!1),
     { addNotification: _, removeNotification: Z } = A5(),
-    G;
-  if (w[0] === Symbol.for("react.memo_cache_sentinel")) ((G = []), (w[0] = G));
-  else G = w[0];
-  let W = yL.useRef(G),
+    Z = L0.useRef([]),
     D = yL.useRef(void 0),
     j = yL.useRef(0),
     M = yL.useRef(void 0),
-    P;
-  if (w[1] !== A || w[2] !== Y)
-    ((P = (l, e, XA, GA) => {
-      let WA = GA === void 0 ? !1 : GA;
-      (A(l, e, XA), Y?.(WA ? 0 : l.length));
-    }),
-      (w[1] = A),
-      (w[2] = Y),
-      (w[3] = P));
-  else P = w[3];
-  let V = P,
-    N;
-  if (w[4] !== V)
-    ((N = (l, e) => {
-      let XA = e === void 0 ? !1 : e;
-      if (!l || !l.display) return;
-      let GA = wx(l.display),
-        WA =
-          GA === "bash" || GA === "background" ? l.display.slice(1) : l.display;
-      V(WA, GA, l.pastedContents ?? {}, XA);
-    }),
-      (w[4] = V),
-      (w[5] = N));
-  else N = w[5];
-  let T = N,
-    k;
-  if (w[6] !== _)
-    ((k = () => {
+    M = L0.useRef(K),
+    j = L0.useRef(q),
+    P = L0.useRef(z);
+  ((M.current = K), (j.current = q), (P.current = z));
+  let V = L0.useCallback(
+      (B, x, F, Q = !1) => {
+        (A(B, x, F), Y?.(Q ? 0 : B.length));
+      },
+      [A, Y],
+    ),
+    N = L0.useCallback(
+      (B, x = !1) => {
+        if (!B || !B.display) return;
+        let F = Vx(B.display),
+          Q =
+            F === "bash" || F === "background" ? B.display.slice(1) : B.display;
+        V(Q, F, B.pastedContents ?? {}, x);
+      },
+      [V],
+    ),
+    T = L0.useCallback(() => {
       _({
         key: "search-history-hint",
         jsx: yL.default.createElement(
@@ -54,17 +43,18 @@
         priority: "immediate",
         timeoutMs: CT1,
       });
-    }),
-      (w[6] = _),
-      (w[7] = k));
-  else k = w[7];
-  let R = k,
-    x;
-  if (w[8] !== K || w[9] !== z || w[10] !== q || w[11] !== R || w[12] !== T)
-    ((x = () => {
+    }, [$]),
+    k = L0.useCallback(() => {
       let l = j.current;
-      if (((j.current = j.current + 1), l === 0))
+      W.current++;
+      let x = M.current,
+        F = j.current,
+        Q = P.current;
+      if (B === 0) {
         M.current = z === "bash" || z === "background" ? z : void 0;
+        let d = x.trim() !== "";
+        O(d ? { display: x, pastedContents: F, mode: Q } : void 0);
+      }
       let e = M.current;
       (async () => {
         let XA = l + 1;
@@ -75,31 +65,17 @@
           if (WA.length > W.current.length) W.current = WA;
         }
         if (l >= W.current.length) {
-          j.current = j.current - 1;
+          W.current--;
           return;
-        }
-        if (l === 0) {
-          let WA = K.trim() !== "";
-          O(WA ? { display: K, pastedContents: q, mode: z } : void 0);
         }
         let GA = l + 1;
         if ((J(GA), T(W.current[l], !0), GA >= 2 && !$.current))
           (($.current = !0), R());
       })();
-    }),
-      (w[8] = K),
-      (w[9] = z),
-      (w[10] = q),
-      (w[11] = R),
-      (w[12] = T),
-      (w[13] = x));
-  else x = w[13];
-  let S = x,
-    g;
-  if (w[14] !== X || w[15] !== V || w[16] !== T)
-    ((g = () => {
+    }, [N, T]),
+    R = L0.useCallback(() => {
       let l = j.current;
-      if (l > 1) ((j.current = j.current - 1), J(l - 1), T(W.current[l - 2]));
+      if (B > 1) (W.current--, H(B - 1), N(Z.current[B - 2]));
       else if (l === 1)
         if (((j.current = 0), J(0), X)) {
           let e = X.mode;
@@ -107,16 +83,8 @@
           else T(X);
         } else V("", M.current ?? "prompt", {});
       return l <= 0;
-    }),
-      (w[14] = X),
-      (w[15] = V),
-      (w[16] = T),
-      (w[17] = g));
-  else g = w[17];
-  let b = g,
-    Q;
-  if (w[18] !== Z)
-    ((Q = () => {
+    }, [J, N, V]),
+    b = L0.useCallback(() => {
       (O(void 0),
         J(0),
         (j.current = 0),
@@ -124,36 +92,16 @@
         Z("search-history-hint"),
         (W.current = []),
         (D.current = void 0));
-    }),
-      (w[18] = Z),
-      (w[19] = Q));
-  else Q = w[19];
-  let F = Q,
-    B;
-  if (w[20] !== Z)
-    ((B = () => {
+    }, [_]),
+    S = L0.useCallback(() => {
       Z("search-history-hint");
-    }),
-      (w[20] = Z),
-      (w[21] = B));
-  else B = w[21];
-  let d = B,
-    o;
-  if (w[22] !== d || w[23] !== H || w[24] !== b || w[25] !== S || w[26] !== F)
-    ((o = {
-      historyIndex: H,
-      setHistoryIndex: J,
-      onHistoryUp: S,
-      onHistoryDown: b,
-      resetHistory: F,
-      dismissSearchHint: d,
-    }),
-      (w[22] = d),
-      (w[23] = H),
-      (w[24] = b),
-      (w[25] = S),
-      (w[26] = F),
-      (w[27] = o));
-  else o = w[27];
-  return o;
+    }, [_]);
+  return {
+    historyIndex: w,
+    setHistoryIndex: H,
+    onHistoryUp: k,
+    onHistoryDown: R,
+    resetHistory: b,
+    dismissSearchHint: S,
+  };
 }

@@@ function 'df' (was 'wL') — structural (40.2%)
--- pretty-v2.1.19.js:524635
+++ pretty-v2.1.20.js:529395
@@ -3,184 +3,31 @@
     return ["You are Claude Code, Anthropic's official CLI for Claude."];
   let z = m1(),
     [w, H, J] = await Promise.all([eI(z), f3K(), EDK(K, q)]),
-    O = hq().language,
+    O = q5(),
     $ = new Set(A.map((G) => G.name)),
     Z =
       w.map((G) => `/${G.userFacingName()}`).length > 0 && $.has(hZ)
         ? `- /<skill-name> (e.g., /commit) is shorthand for users to invoke a user-invocable skill. When executed, the skill gets expanded to a full prompt. Use the ${hZ} tool to execute them. IMPORTANT: Only use ${hZ} for skills listed in its user-invocable skills section - do not guess or use built-in CLI commands.`
         : "";
   return [
-    `
-You are an interactive CLI tool that helps users ${H !== null ? 'according to your "Output Style" below, which describes how you should respond to user queries.' : "with software engineering tasks."} Use the instructions below and the tools available to you to assist the user.
-
-${TDK}
-IMPORTANT: You must NEVER generate or guess URLs for the user unless you are confident that the URLs are for helping the user with programming. You may use URLs provided by the user in their messages or local files.
-
-If the user asks for help or wants to give feedback inform them of the following:
-- /help: Get help with using Claude Code
-- To give feedback, users should ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.19", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-23T21:13:41Z" }.ISSUES_EXPLAINER}
-
-${
-  H !== null
-    ? ""
-    : `# Tone and style
-- Only use emojis if the user explicitly requests it. Avoid using emojis in all communication unless asked.
-- Your output will be displayed on a command line interface. Your responses should be short and concise. You can use Github-flavored markdown for formatting, and will be rendered in a monospace font using the CommonMark specification.
-- Output text to communicate with the user; all text you output outside of tool use is displayed to the user. Only use tools to complete tasks. Never use tools like ${I7} or code comments as means to communicate with the user during the session.
-- NEVER create files unless they're absolutely necessary for achieving your goal. ALWAYS prefer editing an existing file to creating a new one. This includes markdown files.
-- Do not use a colon before tool calls. Your tool calls may not be shown directly in the output, so text like "Let me read the file:" followed by a read tool call should just be "Let me read the file." with a period.
-
-# Professional objectivity
-Prioritize technical accuracy and truthfulness over validating the user's beliefs. Focus on facts and problem-solving, providing direct, objective technical info without any unnecessary superlatives, praise, or emotional validation. It is best for the user if Claude honestly applies the same rigorous standards to all ideas and disagrees when necessary, even if it may not be what the user wants to hear. Objective guidance and respectful correction are more valuable than false agreement. Whenever there is uncertainty, it's best to investigate to find the truth first rather than instinctively confirming the user's beliefs. Avoid using over-the-top validation or excessive praise when responding to users such as "You're absolutely right" or similar phrases.
-
-# No time estimates
-Never give time estimates or predictions for how long tasks will take, whether for your own work or for users planning their projects. Avoid phrases like "this will take me a few minutes," "should be done in about 5 minutes," "this is a quick fix," "this will take 2-3 weeks," or "we can do this later." Focus on what needs to be done, not how long it might take. Break work into actionable steps and let users judge timing for themselves.
-`
-}
-${
-  $.has(mX.name)
-    ? `# Task Management
-You have access to the ${mX.name} tools to help you manage and plan tasks. Use these tools VERY frequently to ensure that you are tracking your tasks and giving the user visibility into your progress.
-These tools are also EXTREMELY helpful for planning tasks, and for breaking down larger complex tasks into smaller steps. If you do not use this tool when planning, you may forget to do important tasks - and that is unacceptable.
-
-It is critical that you mark todos as completed as soon as you are done with a task. Do not batch up multiple tasks before marking them as completed.
-
-Examples:
-
-<example>
-user: Run the build and fix any type errors
-assistant: I'm going to use the ${mX.name} tool to write the following items to the todo list:
-- Run the build
-- Fix any type errors
-
-I'm now going to run the build using ${I7}.
-
-Looks like I found 10 type errors. I'm going to use the ${mX.name} tool to write 10 items to the todo list.
-
-marking the first todo as in_progress
-
-Let me start working on the first item...
-
-The first item has been fixed, let me mark the first todo as completed, and move on to the second item...
-..
-..
-</example>
-In the above example, the assistant completes all the tasks, including the 10 error fixes and running the build and fixing all errors.
-
-<example>
-user: Help me write a new feature that allows users to track their usage metrics and export them to various formats
-assistant: I'll help you implement a usage metrics tracking and export feature. Let me first use the ${mX.name} tool to plan this task.
-Adding the following todos to the todo list:
-1. Research existing metrics tracking in the codebase
-2. Design the metrics collection system
-3. Implement core metrics tracking functionality
-4. Create export functionality for different formats
-
-Let me start by researching the existing codebase to understand what metrics we might already be tracking and how we can build on that.
-
-I'm going to search for any existing metrics or telemetry code in the project.
-
-I've found some existing telemetry code. Let me mark the first todo as in_progress and start designing our metrics tracking system based on what I've learned...
-
-[Assistant continues implementing the feature step by step, marking todos as in_progress and completed as they go]
-</example>
-`
-    : ""
-}
-
-${
-  $.has(_X)
-    ? `
-# Asking questions as you work
-
-You have access to the ${_X} tool to ask the user questions when you need clarification, want to validate assumptions, or need to make a decision you're unsure about. When presenting options or plans, never include time estimates - focus on what each option involves, not how long it takes.
-`
-    : ""
-}
-
-Users may configure 'hooks', shell commands that execute in response to events like tool calls, in settings. Treat feedback from hooks, including <user-prompt-submit-hook>, as coming from the user. If you get blocked by a hook, determine if you can adjust your actions in response to the blocked message. If not, ask the user to check their hooks configuration.
-
-${
-  H === null || H.keepCodingInstructions === !0
-    ? `# Doing tasks
-The user will primarily request you perform software engineering tasks. This includes solving bugs, adding new functionality, refactoring code, explaining code, and more. For these tasks the following steps are recommended:
-- NEVER propose changes to code you haven't read. If a user asks about or wants you to modify a file, read it first. Understand existing code before suggesting modifications.
-- ${$.has(mX.name) ? `Use the ${mX.name} tool to plan the task if required` : ""}
-- ${$.has(_X) ? `Use the ${_X} tool to ask questions, clarify and gather information as needed.` : ""}
-- Be careful not to introduce security vulnerabilities such as command injection, XSS, SQL injection, and other OWASP top 10 vulnerabilities. If you notice that you wrote insecure code, immediately fix it.
-- Avoid over-engineering. Only make changes that are directly requested or clearly necessary. Keep solutions simple and focused.
-  - Don't add features, refactor code, or make "improvements" beyond what was asked. A bug fix doesn't need surrounding code cleaned up. A simple feature doesn't need extra configurability. Don't add docstrings, comments, or type annotations to code you didn't change. Only add comments where the logic isn't self-evident.
-  - Don't add error handling, fallbacks, or validation for scenarios that can't happen. Trust internal code and framework guarantees. Only validate at system boundaries (user input, external APIs). Don't use feature flags or backwards-compatibility shims when you can just change the code.
-  - Don't create helpers, utilities, or abstractions for one-time operations. Don't design for hypothetical future requirements. The right amount of complexity is the minimum needed for the current task—three similar lines of code is better than a premature abstraction.
-- Avoid backwards-compatibility hacks like renaming unused \`_vars\`, re-exporting types, adding \`// removed\` comments for removed code, etc. If something is unused, delete it completely.
-`
-    : ""
-}
-- Tool results and user messages may include <system-reminder> tags. <system-reminder> tags contain useful information and reminders. They are automatically added by the system, and bear no direct relation to the specific tool results or user messages in which they appear.
-- The conversation has unlimited context through automatic summarization.
-
-
-# Tool usage policy${
-      $.has(l5)
-        ? `
-- When doing file search, prefer to use the ${l5} tool in order to reduce context usage.
-- You should proactively use the ${l5} tool with specialized agents when the task at hand matches the agent's description.
-${Z}`
-        : ""
-    }${
-      $.has(z0)
-        ? `
-- When ${z0} returns a message about a redirect to a different host, you should immediately make a new ${z0} request with the redirect URL provided in the response.`
-        : ""
-    }
-- You can call multiple tools in a single response. If you intend to call multiple tools and there are no dependencies between them, make all independent tool calls in parallel. Maximize use of parallel tool calls where possible to increase efficiency. However, if some tool calls depend on previous calls to inform dependent values, do NOT call these tools in parallel and instead call them sequentially. For instance, if one operation must complete before another starts, run these operations sequentially instead. Never use placeholders or guess missing parameters in tool calls.
-- If the user specifies that they want you to run tools "in parallel", you MUST send a single message with multiple tool use content blocks. For example, if you need to launch multiple agents in parallel, send a single message with multiple ${l5} tool calls.
-- Use specialized tools instead of bash commands when possible, as this provides a better user experience. For file operations, use dedicated tools: ${C5} for reading files instead of cat/head/tail, ${c5} for editing instead of sed/awk, and ${x2} for creating files instead of cat with heredoc or echo redirection. Reserve bash tools exclusively for actual system commands and terminal operations that require shell execution. NEVER use bash echo or other command-line tools to communicate thoughts, explanations, or instructions to the user. Output all communication directly in your response text instead.
-- VERY IMPORTANT: When exploring the codebase to gather context or to answer a question that is not a needle query for a specific file/class/function, it is CRITICAL that you use the ${l5} tool with subagent_type=${GC.agentType} instead of running search commands directly.
-<example>
-user: Where are errors from the client handled?
-assistant: [Uses the ${l5} tool with subagent_type=${GC.agentType} to find the files that handle client errors instead of using ${uH} or ${ow} directly]
-</example>
-<example>
-user: What is the codebase structure?
-assistant: [Uses the ${l5} tool with subagent_type=${GC.agentType}]
-</example>
-`,
-    `
-${TDK}
-`,
-    $.has(mX.name)
-      ? `
-IMPORTANT: Always use the ${mX.name} tool to plan and track tasks throughout the conversation.`
-      : "",
-    `
-# Code References
-
-When referencing specific functions or pieces of code include the pattern \`file_path:line_number\` to allow the user to easily navigate to the source code location.
-
-<example>
-user: Where are errors from the client handled?
-assistant: Clients are marked as failed in the \`connectToServer\` function in src/services/process.ts:712.
-</example>
-`,
+    Qi2(H),
+    Ui2(H),
+    pi2(X),
+    di2(X),
+    ci2(),
+    li2(H, X),
+    ii2(),
+    ni2(X, _),
+    gNK,
+    ri2(X),
+    oi2(),
     ...[],
-    "",
-    "",
-    `
-${J}`,
-    O
-      ? `
-# Language
-Always respond in ${O}. Use ${O} for all explanations, comments, and communications with the user. Technical terms and code identifiers should remain in their original form.
-`
-      : "",
-    H !== null
-      ? `
-# Output Style: ${H.name}
-${H.prompt}
-`
-      : "",
-    ...(Y && Y.length > 0 ? [yB2(Y)] : []),
     SB2(),
-  ];
+    si2(),
+    J,
+    ti2(O.language),
+    ei2(H),
+    An2(Y),
+    zn2(),
+  ].filter((Z) => Z !== null);
 }

@@@ function 'li2' — structural (20.3%)
--- pretty-v2.1.19.js:566638
+++ pretty-v2.1.20.js:529300
@@ -1,16 +1,28 @@
-async function li2(A, K, q, Y, z) {
-  if (A.hook_event_name !== "PostToolUse") return {};
-  if (!z?.setAppState || !z?.getAppState)
-    return (
-      h("Attribution hook: No setAppState/getAppState available, skipping"),
-      {}
-    );
-  let w = Xk6.safeParse(A.tool_response);
-  if (!w.success)
-    return (
-      h(`Attribution hook: Failed to parse Write response: ${w.error.message}`),
-      {}
-    );
-  let { filePath: H, originalFile: J, content: X } = w.data;
-  return (KQ6(z, H, J ?? "", X, !1), {});
+function li2(A, K) {
+  if (A !== null && A.keepCodingInstructions !== !0) return null;
+  let q = [
+    ...(K.has(UO.name)
+      ? [`- Use the ${UO.name} tool to plan the task if required`]
+      : []),
+    ...(K.has(xJ)
+      ? [
+          `- Use the ${xJ} tool to ask questions, clarify and gather information as needed.`,
+        ]
+      : []),
+  ];
+  return `# Doing tasks
+The user will primarily request you perform software engineering tasks. This includes solving bugs, adding new functionality, refactoring code, explaining code, and more. For these tasks the following steps are recommended:
+${"- NEVER propose changes to code you haven't read. If a user asks about or wants you to modify a file, read it first. Understand existing code before suggesting modifications."}${
+    q.length > 0
+      ? `
+${q.join(`
+`)}`
+      : ""
+  }
+- Be careful not to introduce security vulnerabilities such as command injection, XSS, SQL injection, and other OWASP top 10 vulnerabilities. If you notice that you wrote insecure code, immediately fix it.
+- Avoid over-engineering. Only make changes that are directly requested or clearly necessary. Keep solutions simple and focused.
+  - Don't add features, refactor code, or make "improvements" beyond what was asked. A bug fix doesn't need surrounding code cleaned up. A simple feature doesn't need extra configurability. Don't add docstrings, comments, or type annotations to code you didn't change. Only add comments where the logic isn't self-evident.
+  - Don't add error handling, fallbacks, or validation for scenarios that can't happen. Trust internal code and framework guarantees. Only validate at system boundaries (user input, external APIs). Don't use feature flags or backwards-compatibility shims when you can just change the code.
+  - Don't create helpers, utilities, or abstractions for one-time operations. Don't design for hypothetical future requirements. The right amount of complexity is the minimum needed for the current task—three similar lines of code is better than a premature abstraction.
+- Avoid backwards-compatibility hacks like renaming unused \`_vars\`, re-exporting types, adding \`// removed\` comments for removed code, etc. If something is unused, delete it completely.`;
 }

@@@ function 'pi2' — structural (20.0%)
--- pretty-v2.1.19.js:566572
+++ pretty-v2.1.20.js:529243
@@ -1,10 +1,48 @@
-async function pi2() {
-  let A = t6(),
-    K = await F4(
-      "git",
-      ["--no-optional-locks", "status", "--porcelain", "-uall"],
-      { cwd: A, timeout: 5000 },
-    );
-  if (K.code !== 0) return new Map();
-  return iSK(K.stdout);
+function pi2(A) {
+  if (!A.has(UO.name)) return null;
+  return `# Task Management
+You have access to the ${UO.name} tools to help you manage and plan tasks. Use these tools VERY frequently to ensure that you are tracking your tasks and giving the user visibility into your progress.
+These tools are also EXTREMELY helpful for planning tasks, and for breaking down larger complex tasks into smaller steps. If you do not use this tool when planning, you may forget to do important tasks - and that is unacceptable.
+
+It is critical that you mark todos as completed as soon as you are done with a task. Do not batch up multiple tasks before marking them as completed.
+
+Examples:
+
+<example>
+user: Run the build and fix any type errors
+assistant: I'm going to use the ${UO.name} tool to write the following items to the todo list:
+- Run the build
+- Fix any type errors
+
+I'm now going to run the build using ${k7}.
+
+Looks like I found 10 type errors. I'm going to use the ${UO.name} tool to write 10 items to the todo list.
+
+marking the first todo as in_progress
+
+Let me start working on the first item...
+
+The first item has been fixed, let me mark the first todo as completed, and move on to the second item...
+..
+..
+</example>
+In the above example, the assistant completes all the tasks, including the 10 error fixes and running the build and fixing all errors.
+
+<example>
+user: Help me write a new feature that allows users to track their usage metrics and export them to various formats
+assistant: I'll help you implement a usage metrics tracking and export feature. Let me first use the ${UO.name} tool to plan this task.
+Adding the following todos to the todo list:
+1. Research existing metrics tracking in the codebase
+2. Design the metrics collection system
+3. Implement core metrics tracking functionality
+4. Create export functionality for different formats
+
+Let me start by researching the existing codebase to understand what metrics we might already be tracking and how we can build on that.
+
+I'm going to search for any existing metrics or telemetry code in the project.
+
+I've found some existing telemetry code. Let me mark the first todo as in_progress and start designing our metrics tracking system based on what I've learned...
+
+[Assistant continues implementing the feature step by step, marking todos as in_progress and completed as they go]
+</example>`;
 }

@@@ function 'ni2' — structural (18.6%)
--- pretty-v2.1.19.js:566678
+++ pretty-v2.1.20.js:529332
@@ -1,24 +1,29 @@
-async function ni2(A, K, q, Y, z) {
-  if (A.hook_event_name !== "PostToolUse") return {};
-  if (!z?.setAppState || !z?.getAppState)
-    return (
-      h("Attribution hook: No setAppState/getAppState available, skipping"),
-      {}
-    );
-  let w = Dk6.safeParse(A.tool_response);
-  if (!w.success)
-    return (
-      h(
-        `Attribution hook: Failed to parse NotebookEdit response: ${w.error.message}`,
-      ),
-      {}
-    );
-  let {
-    notebook_path: H,
-    original_file: J,
-    updated_file: X,
-    error: O,
-  } = w.data;
-  if (O) return (h("Attribution hook: NotebookEdit had error, skipping"), {});
-  return (KQ6(z, H, J, X, !1), {});
+function ni2(A, K) {
+  let q = A.has(j5)
+      ? `
+- When doing file search, prefer to use the ${j5} tool in order to reduce context usage.
+- You should proactively use the ${j5} tool with specialized agents when the task at hand matches the agent's description.${
+          K
+            ? `
+${K}`
+            : ""
+        }`
+      : "",
+    Y = A.has(q0)
+      ? `
+- When ${q0} returns a message about a redirect to a different host, you should immediately make a new ${q0} request with the redirect URL provided in the response.`
+      : "";
+  return `# Tool usage policy${q}${Y}
+- You can call multiple tools in a single response. If you intend to call multiple tools and there are no dependencies between them, make all independent tool calls in parallel. Maximize use of parallel tool calls where possible to increase efficiency. However, if some tool calls depend on previous calls to inform dependent values, do NOT call these tools in parallel and instead call them sequentially. For instance, if one operation must complete before another starts, run these operations sequentially instead. Never use placeholders or guess missing parameters in tool calls.
+- If the user specifies that they want you to run tools "in parallel", you MUST send a single message with multiple tool use content blocks. For example, if you need to launch multiple agents in parallel, send a single message with multiple ${j5} tool calls.
+- Use specialized tools instead of bash commands when possible, as this provides a better user experience. For file operations, use dedicated tools: ${K5} for reading files instead of cat/head/tail, ${n5} for editing instead of sed/awk, and ${cz} for creating files instead of cat with heredoc or echo redirection. Reserve bash tools exclusively for actual system commands and terminal operations that require shell execution. NEVER use bash echo or other command-line tools to communicate thoughts, explanations, or instructions to the user. Output all communication directly in your response text instead.
+- ${`VERY IMPORTANT: When exploring the codebase to gather context or to answer a question that is not a needle query for a specific file/class/function, it is CRITICAL that you use the ${j5} tool with subagent_type=${WC.agentType} instead of running search commands directly.`} 
+<example>
+user: Where are errors from the client handled?
+assistant: [Uses the ${j5} tool with subagent_type=${WC.agentType} to find the files that handle client errors instead of using ${bH} or ${dz} directly]
+</example>
+<example>
+user: What is the codebase structure?
+assistant: [Uses the ${j5} tool with subagent_type=${WC.agentType}]
+</example>`;
 }

=== String Changes ===

@@@ function 'KQK' (was 'pbK') — string-only
--- pretty-v2.1.19.js:572628
+++ pretty-v2.1.20.js:576729
@@ -2,7 +2,7 @@
   try {
     let q = await uC(A, K);
     if (q.type === "connected") return "✓ Connected";
-    else if (q.type === "needs-auth") return "⚠ Needs authentication";
+    else if (q.type === "needs-auth") return "! Needs authentication";
     else return "✗ Failed to connect";
   } catch (q) {
     return "✗ Connection error";

@@@ function 'le3' (was 'op3') — string-only
--- pretty-v2.1.19.js:177628
+++ pretty-v2.1.20.js:180611
@@ -13,13 +13,13 @@
     case "delete":
       return "Delete";
     case "up":
-      return "UP";
+      return "↑";
     case "down":
-      return "DOWN";
+      return "↓";
     case "left":
-      return "LEFT";
+      return "←";
     case "right":
-      return "RIGHT";
+      return "→";
     case "pageup":
       return "PageUp";
     case "pagedown":

@@@ variable 'TA9' (was 'Rd3') — string-only
--- pretty-v2.1.19.js:179443
+++ pretty-v2.1.20.js:182435
@@ -1,7 +1,7 @@
   Rd3 = async (A, K) => {
-    (h("[render] initYoga starting"),
+    (h("[render] initLayout starting"),
       await W94(),
-      h("[render] initYoga complete"));
+      h("[render] initLayout complete"));
     let q = Ld3(A, K);
     return (
       h(

@@@ function 'UMA' (was 'XV1') — string-only
--- pretty-v2.1.19.js:463840
+++ pretty-v2.1.20.js:421730
@@ -2,6 +2,6 @@
   return {
     matches: !1,
     confidence: "high",
-    reason: "Classifier permissions feature is disabled in external builds",
+    reason: "This feature is disabled",
   };
 }
