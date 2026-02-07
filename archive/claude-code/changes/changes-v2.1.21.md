--- archive/claude-code/pretty/pretty-v2.1.20.js
+++ archive/claude-code/pretty/pretty-v2.1.21.js
Structural similarity: 99.2%
Matched: 14216/14262 vs 14329
Changes: 113 added, 46 removed, 631 structural, 35 string-only (13550 unchanged)

Filtered: 47 version bumps, 490 reformatting-only changes

=== Import Style Changes ===

"child_process":
  - import M9Y from "child_process";
  - import j9Y from "child_process";
  + import { spawn as Ez5, spawnSync as kz5 } from "child_process";

"crypto":
  - import H8Y from "crypto";
  - import J8Y from "crypto";
  + import { createHash as jq7, randomUUID as UYY } from "crypto";
  + import { createHash as OCY, randomBytes as XCY } from "crypto";
  + import { randomBytes as po2, randomUUID as do2 } from "crypto";
  + import { randomUUID as nL } from "crypto";
  + import { randomBytes as sKz, timingSafeEqual as tKz } from "crypto";

"https":
  - import fA7 from "https";
  + import { Agent as xn3 } from "https";

"node:child_process":
  - import fR1 from "node:child_process";
  - import i77 from "node:child_process";
  + import { execFile as s9Y, execFileSync as vFw } from "node:child_process";
  + import { execFileSync as DR2, spawn as jR2 } from "node:child_process";

"node:fs":
  - import b3Y from "node:fs";
  - import B3Y from "node:fs";
  + import {
  +   existsSync as oUA,
  +   statSync as qR2,
  +   mkdirSync as YR2,
  +   realpathSync as zR2,
  + } from "node:fs";
  + import {
  +   constants as _R2,
  +   readFileSync as ZR2,
  +   existsSync as GR2,
  +   unlinkSync as WR2,
  + } from "node:fs";

"node:os":
  - import u3Y from "node:os";
  + import { homedir as BKz } from "node:os";

"node:path":
  - import l77 from "node:path";
  + import {
  +   join as GX,
  +   dirname as id,
  +   resolve as Wm,
  +   delimiter as zb2,
  +   basename as wb2,
  + } from "node:path";

"node:process":
  - import HvK from "node:process";
  + import { cwd as v04 } from "node:process";

"node:util":
  - import Ft9 from "node:util";
  + import { isDeepStrictEqual as ZgK } from "node:util";

"path":
  - import $3Y from "path";
  + import { extname as m4z, join as g4z } from "path";
  + import { posix as HFK, win32 as JFK } from "path";
  + import { dirname as KKz, join as hFK } from "path";

"stream":
  - import ZzA from "stream";
  + import { PassThrough as kKz } from "stream";

=== Removed ===

--- Removed Cc6 (pretty-v2.1.20.js:519-526)
- function Cc6() {
-   (process.stdout.on("error", (A) => {
-     if (A.code === "EPIPE") process.stdout.destroy();
-   }),
-     process.stderr.on("error", (A) => {
-       if (A.code === "EPIPE") process.stderr.destroy();
-     }));
- }

--- Removed E7 (pretty-v2.1.20.js:527-531)
- function E7(A) {
-   if (process.stdout.destroyed) return;
-   for (let K = 0; K < A.length; K += 2000)
-     process.stdout.write(A.substring(K, K + 2000));
- }

--- Removed nc (pretty-v2.1.20.js:532-536)
- function nc(A) {
-   if (process.stderr.destroyed) return;
-   for (let K = 0; K < A.length; K += 2000)
-     process.stderr.write(A.substring(K, K + 2000));
- }

--- Removed Mi6 (pretty-v2.1.20.js:1794-1794)
-   Mi6 = "structured-outputs-2025-09-17",

--- Removed Iw4 (pretty-v2.1.20.js:160490-160674)
- var Iw4 = C(() => {
-   Rw4 = `Use this tool to create and manage a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user.
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
- * Uses the ${n5} tool to add a comment to the calculateTotal function *
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

--- Removed kr3 (pretty-v2.1.20.js:160910-160915)
- function kr3(A) {
-   EOA(A);
-   let K = W46.get(A);
-   if (K === void 0) K = Er3(A);
-   return (K++, W46.set(A, K), String(K));
- }

--- Removed Xq1 (pretty-v2.1.20.js:160916-160921)
- function Xq1(A, K) {
-   let q = kr3(A),
-     Y = { id: q, ...K },
-     z = SRA(A, q);
-   return (c8(z, QA(Y, null, 2)), Jq1(), q);
- }

--- Removed VJ4 (pretty-v2.1.20.js:174576-174578)
- function VJ4() {
-   return (h("Layout engine: yoga"), "yoga");
- }

--- Removed Xa3 (pretty-v2.1.20.js:176333-176338)
- function Xa3(A, K) {
-   let q = A.charStringMap.get(K);
-   if (q !== void 0) return q;
-   let Y = A.charStrings.length;
-   return (A.charStrings.push(K), A.charStringMap.set(K, Y), Y);
- }

--- Removed H04 (pretty-v2.1.20.js:176354-176356)
- function H04(A) {
-   return A.filter((K) => !z04.test(K.code));
- }

--- Removed UOA (pretty-v2.1.20.js:176405-176410)
- var UOA = C(() => {
-   w76();
-   y76();
-   u8A();
-   z04 = new RegExp(`^${b8A}\\]8${x8A}${x8A}([^${gn}]*)${gn}$`);
- });

--- Removed h56 (pretty-v2.1.20.js:192633-192635)
- function h56(A) {
-   return A.includes("-structured-");
- }

--- Removed UG1 (pretty-v2.1.20.js:344703-344709)
- function UG1(A, K, q) {
-   let Y = QG1();
-   if (!Y) return q;
-   let z = Y.client.getExperiment(A);
-   if (!z) return q;
-   return z.get(K, q);
- }

--- Removed h7K (pretty-v2.1.20.js:423206-423212)
- function h7K() {
-   if (dMA)
-     ((jt = dMA), h(`[TeammateModeSnapshot] Captured from CLI override: ${jt}`));
-   else
-     ((jt = P1().teammateMode ?? "auto"),
-       h(`[TeammateModeSnapshot] Captured from config: ${jt}`));
- }

--- Removed bYK (pretty-v2.1.20.js:446638-446791)
- var bYK = C(() => {
-   ((RT2 = `Use this tool proactively when you're about to start a non-trivial implementation task. Getting user sign-off on your approach before writing code prevents wasted effort and ensures alignment. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
-    - If you would use ${xJ} to clarify the approach, use EnterPlanMode instead
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
- 5. Use ${xJ} if you need to clarify approaches
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
-     (paH = `Use this tool when a task has genuine ambiguity about the right approach and getting user input before coding would prevent significant rework. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
- When in doubt, prefer starting work and using ${xJ} for specific questions over entering a full planning phase.
- 
- ## What Happens in Plan Mode
- 
- In plan mode, you'll:
- 1. Explore the codebase using Glob, Grep, and Read tools
- 2. Understand existing patterns and architecture
- 3. Design an implementation approach
- 4. Present your plan to the user for approval
- 5. Use ${xJ} if you need to clarify approaches
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

--- Removed Fx6 (pretty-v2.1.20.js:465243-465245)
- function Fx6(A) {
-   return rf1(A, XR2);
- }

--- Removed z$K (pretty-v2.1.20.js:479761-481339)
- function z$K(A) {
-   let K = s(190),
-     {
-       onClose: q,
-       context: Y,
-       setTabsHidden: z,
-       setIsWarning: w,
-       setHideMargin: H,
-       onSearchModeChange: J,
-     } = A,
-     [O, X] = b4(),
-     $;
-   if (K[0] === Symbol.for("react.memo_cache_sentinel"))
-     (($ = P1()), (K[0] = $));
-   else $ = K[0];
-   let [_, Z] = wm.useState($),
-     G;
-   if (K[1] === Symbol.for("react.memo_cache_sentinel"))
-     ((G = jwK()), (K[1] = G));
-   else G = K[1];
-   let [W, D] = wm.useState(G),
-     M;
-   if (K[2] === Symbol.for("react.memo_cache_sentinel"))
-     ((M = P1()), (K[2] = M));
-   else M = K[2];
-   let j = Z6.useRef(M),
-     P;
-   if (K[3] === Symbol.for("react.memo_cache_sentinel"))
-     ((P = q5()), (K[3] = P));
-   else P = K[3];
-   let [V, N] = wm.useState(P),
-     T;
-   if (K[4] === Symbol.for("react.memo_cache_sentinel"))
-     ((T = q5()), (K[4] = T));
-   else T = K[4];
-   let k = Z6.useRef(T),
-     [R, b] = wm.useState(V?.outputStyle || dZ),
-     S = Z6.useRef(R),
-     [B, x] = wm.useState(V?.language),
-     F = Z6.useRef(B),
-     [Q, u] = wm.useState(0),
-     [d, a] = wm.useState(!0),
-     l;
-   if (K[5] !== J)
-     ((l = (H1) => {
-       (a(H1), J?.(H1));
-     }),
-       (K[5] = J),
-       (K[6] = l));
-   else l = K[6];
-   let e = l,
-     JA = d,
-     OA = vD(),
-     [HA, DA] = k6(),
-     {
-       mainLoopModel: o,
-       verbose: _A,
-       thinkingEnabled: PA,
-       promptSuggestionEnabled: jA,
-     } = HA,
-     yA;
-   if (K[7] === Symbol.for("react.memo_cache_sentinel"))
-     ((yA = {}), (K[7] = yA));
-   else yA = K[7];
-   let [bA, YA] = wm.useState(yA),
-     [KA, zA] = wm.useState(null),
-     AA = JA && KA === null,
-     t;
-   if (K[8] !== e)
-     ((t = () => {
-       e(!1);
-     }),
-       (K[8] = e),
-       (K[9] = t));
-   else t = K[9];
-   let $A;
-   if (K[10] !== t || K[11] !== AA)
-     (($A = { isActive: AA, onExit: t }),
-       (K[10] = t),
-       (K[11] = AA),
-       (K[12] = $A));
-   else $A = K[12];
-   let { query: vA, setQuery: ZA, cursorOffset: LA } = mS($A),
-     mA;
-   if (K[13] !== Y.options.mcpClients)
-     ((mA = G$1(Y.options.mcpClients)),
-       (K[13] = Y.options.mcpClients),
-       (K[14] = mA));
-   else mA = K[14];
-   let CA = mA,
-     IA;
-   if (K[15] === Symbol.for("react.memo_cache_sentinel"))
-     ((IA = N1(process.env.CLAUDE_CODE_DISABLE_FILE_CHECKPOINTING)),
-       (K[15] = IA));
-   else IA = K[15];
-   let sA = !IA,
-     w1;
-   if (K[16] === Symbol.for("react.memo_cache_sentinel"))
-     ((w1 = $Y6()), (K[16] = w1));
-   else w1 = K[16];
-   let _1 = w1,
-     k1;
-   if (K[17] === Symbol.for("react.memo_cache_sentinel"))
-     ((k1 = mMA()), (K[17] = k1));
-   else k1 = K[17];
-   let L1 = k1,
-     x1;
-   if (K[18] !== o || K[19] !== DA)
-     ((x1 = async function (t1) {
-       (n("tengu_config_model_changed", { from_model: o, to_model: t1 }),
-         DA((r8) => ({ ...r8, mainLoopModel: t1 })),
-         YA((r8) => {
-           let y4 = $y(t1);
-           if ("model" in r8) {
-             let { model: wK, ...pq } = r8;
-             return { ...pq, model: y4 };
-           }
-           return { ...r8, model: y4 };
-         }));
-     }),
-       (K[18] = o),
-       (K[19] = DA),
-       (K[20] = x1));
-   else x1 = K[20];
-   let M1 = x1,
-     c1;
-   if (K[21] !== DA)
-     ((c1 = function (t1) {
-       (V6((b6) => ({ ...b6, verbose: t1 })),
-         Z({ ...P1(), verbose: t1 }),
-         DA((b6) => ({ ...b6, verbose: t1 })),
-         YA((b6) => {
-           if ("verbose" in b6) {
-             let { verbose: r8, ...y4 } = b6;
-             return y4;
-           }
-           return { ...b6, verbose: t1 };
-         }));
-     }),
-       (K[21] = DA),
-       (K[22] = c1));
-   else c1 = K[22];
-   let z1 = c1,
-     $1;
-   if (K[23] !== _.autoCompactEnabled)
-     (($1 = {
-       id: "autoCompactEnabled",
-       label: "Auto-compact",
-       value: _.autoCompactEnabled,
-       type: "boolean",
-       onChange(H1) {
-         (V6((t1) => ({ ...t1, autoCompactEnabled: H1 })),
-           Z({ ...P1(), autoCompactEnabled: H1 }),
-           n("tengu_auto_compact_setting_changed", { enabled: H1 }));
-       },
-     }),
-       (K[23] = _.autoCompactEnabled),
-       (K[24] = $1));
-   else $1 = K[24];
-   let V1 = V?.spinnerTipsEnabled ?? !0,
-     b1;
-   if (K[25] !== V1)
-     ((b1 = {
-       id: "spinnerTipsEnabled",
-       label: "Show tips",
-       value: V1,
-       type: "boolean",
-       onChange(H1) {
-         (h4("localSettings", { spinnerTipsEnabled: H1 }),
-           N((t1) => ({ ...t1, spinnerTipsEnabled: H1 })),
-           n("tengu_tips_setting_changed", { enabled: H1 }));
-       },
-     }),
-       (K[25] = V1),
-       (K[26] = b1));
-   else b1 = K[26];
-   let X6 = PA ?? !0,
-     J6;
-   if (K[27] !== DA || K[28] !== X6)
-     ((J6 = {
-       id: "thinkingEnabled",
-       label: "Thinking mode",
-       value: X6,
-       type: "boolean",
-       onChange(H1) {
-         (DA((t1) => ({ ...t1, thinkingEnabled: H1 })),
-           h4("userSettings", { alwaysThinkingEnabled: H1 ? void 0 : !1 }),
-           n("tengu_thinking_toggled", { enabled: H1 }));
-       },
-     }),
-       (K[27] = DA),
-       (K[28] = X6),
-       (K[29] = J6));
-   else J6 = K[29];
-   let fA;
-   if (K[30] !== jA || K[31] !== DA)
-     ((fA = {
-       id: "promptSuggestionEnabled",
-       label: "Prompt suggestions",
-       value: jA,
-       type: "boolean",
-       onChange(H1) {
-         (DA((t1) => ({ ...t1, promptSuggestionEnabled: H1 })),
-           h4("userSettings", { promptSuggestionEnabled: H1 ? void 0 : !1 }));
-       },
-     }),
-       (K[30] = jA),
-       (K[31] = DA),
-       (K[32] = fA));
-   else fA = K[32];
-   let NA;
-   if (K[33] !== _.speculationEnabled)
-     ((NA = []), (K[33] = _.speculationEnabled), (K[34] = NA));
-   else NA = K[34];
-   let lA;
-   if (K[35] !== _.fileCheckpointingEnabled)
-     ((lA = sA
-       ? [
-           {
-             id: "fileCheckpointingEnabled",
-             label: "Rewind code (checkpoints)",
-             value: _.fileCheckpointingEnabled,
-             type: "boolean",
-             onChange(H1) {
-               (V6((t1) => ({ ...t1, fileCheckpointingEnabled: H1 })),
-                 Z({ ...P1(), fileCheckpointingEnabled: H1 }),
-                 n("tengu_file_history_snapshots_setting_changed", {
-                   enabled: H1,
-                 }));
-             },
-           },
-         ]
-       : []),
-       (K[35] = _.fileCheckpointingEnabled),
-       (K[36] = lA));
-   else lA = K[36];
-   let q1;
-   if (K[37] !== z1 || K[38] !== _A)
-     ((q1 = {
-       id: "verbose",
-       label: "Verbose output",
-       value: _A,
-       type: "boolean",
-       onChange: z1,
-     }),
-       (K[37] = z1),
-       (K[38] = _A),
-       (K[39] = q1));
-   else q1 = K[39];
-   let dA;
-   if (K[40] !== _.terminalProgressBarEnabled)
-     ((dA = {
-       id: "terminalProgressBarEnabled",
-       label: "Terminal progress bar",
-       value: _.terminalProgressBarEnabled,
-       type: "boolean",
-       onChange(H1) {
-         (V6((t1) => ({ ...t1, terminalProgressBarEnabled: H1 })),
-           Z({ ...P1(), terminalProgressBarEnabled: H1 }),
-           n("tengu_terminal_progress_bar_setting_changed", { enabled: H1 }));
-       },
-     }),
-       (K[40] = _.terminalProgressBarEnabled),
-       (K[41] = dA));
-   else dA = K[41];
-   let iA = V?.permissions?.defaultMode || "default",
-     j1;
-   if (K[42] === Symbol.for("react.memo_cache_sentinel"))
-     ((j1 = ["default", "plan"]), (K[42] = j1));
-   else j1 = K[42];
-   let T1 = j1,
-     U1;
-   if (K[43] === Symbol.for("react.memo_cache_sentinel")) {
-     let H1 = j8() ? ["bypassPermissions"] : ["bypassPermissions", "delegate"];
-     ((U1 = [
-       ...T1,
-       ...n1A.filter((t1) => !T1.includes(t1) && !H1.includes(t1)),
-     ]),
-       (K[43] = U1));
-   } else U1 = K[43];
-   let T6;
-   if (K[44] !== V?.permissions || K[45] !== iA)
-     ((T6 = {
-       id: "defaultPermissionMode",
-       label: "Default permission mode",
-       value: iA,
-       options: U1,
-       type: "enum",
-       onChange(H1) {
-         let t1 = og(kR(H1)),
-           b6 = h4("userSettings", {
-             permissions: { ...V?.permissions, defaultMode: t1 },
-           });
-         if (b6.error) {
-           qA(b6.error);
-           return;
-         }
-         (N((r8) => ({
-           ...r8,
-           permissions: { ...r8?.permissions, defaultMode: t1 },
-         })),
-           YA((r8) => ({ ...r8, defaultPermissionMode: H1 })),
-           n("tengu_config_changed", {
-             setting: "defaultPermissionMode",
-             value: H1,
-           }));
-       },
-     }),
-       (K[44] = V?.permissions),
-       (K[45] = iA),
-       (K[46] = T6));
-   else T6 = K[46];
-   let R8;
-   if (K[47] !== _.respectGitignore)
-     ((R8 = {
-       id: "respectGitignore",
-       label: "Respect .gitignore in file picker",
-       value: _.respectGitignore,
-       type: "boolean",
-       onChange(H1) {
-         (V6((t1) => ({ ...t1, respectGitignore: H1 })),
-           Z({ ...P1(), respectGitignore: H1 }),
-           n("tengu_respect_gitignore_setting_changed", { enabled: H1 }));
-       },
-     }),
-       (K[47] = _.respectGitignore),
-       (K[48] = R8));
-   else R8 = K[48];
-   let a6;
-   if (K[49] !== V?.autoUpdatesChannel)
-     ((a6 = L1
-       ? {
-           id: "autoUpdatesChannel",
-           label: "Auto-update channel",
-           value: "disabled",
-           type: "managedEnum",
-           onChange() {},
-         }
-       : {
-           id: "autoUpdatesChannel",
-           label: "Auto-update channel",
-           value: V?.autoUpdatesChannel ?? "latest",
-           type: "managedEnum",
-           onChange() {},
-         }),
-       (K[49] = V?.autoUpdatesChannel),
-       (K[50] = a6));
-   else a6 = K[50];
-   let V4;
-   if (K[51] !== X || K[52] !== O)
-     ((V4 = {
-       id: "theme",
-       label: "Theme",
-       value: O,
-       type: "managedEnum",
-       onChange: X,
-     }),
-       (K[51] = X),
-       (K[52] = O),
-       (K[53] = V4));
-   else V4 = K[53];
-   let $4;
-   if (K[54] === Symbol.for("react.memo_cache_sentinel"))
-     (($4 = [
-       "auto",
-       "iterm2",
-       "terminal_bell",
-       "iterm2_with_bell",
-       "kitty",
-       "ghostty",
-       "notifications_disabled",
-     ]),
-       (K[54] = $4));
-   else $4 = K[54];
-   let W8;
-   if (K[55] !== _.preferredNotifChannel)
-     ((W8 = {
-       id: "notifChannel",
-       label: "Notifications",
-       value: _.preferredNotifChannel,
-       options: $4,
-       type: "enum",
-       onChange(H1) {
-         (V6((t1) => ({ ...t1, preferredNotifChannel: H1 })),
-           Z({ ...P1(), preferredNotifChannel: H1 }));
-       },
-     }),
-       (K[55] = _.preferredNotifChannel),
-       (K[56] = W8));
-   else W8 = K[56];
-   let v4;
-   if (K[57] !== R)
-     ((v4 = {
-       id: "outputStyle",
-       label: "Output style",
-       value: R,
-       type: "managedEnum",
-       onChange: Fh2,
-     }),
-       (K[57] = R),
-       (K[58] = v4));
-   else v4 = K[58];
-   let f4 = B ?? "Default (English)",
-     MK;
-   if (K[59] !== f4)
-     ((MK = {
-       id: "language",
-       label: "Language",
-       value: f4,
-       type: "managedEnum",
-       onChange: gh2,
-     }),
-       (K[59] = f4),
-       (K[60] = MK));
-   else MK = K[60];
-   let xK = _.editorMode === "emacs" ? "normal" : _.editorMode || "normal",
-     d8;
-   if (K[61] === Symbol.for("react.memo_cache_sentinel"))
-     ((d8 = ["normal", "vim"]), (K[61] = d8));
-   else d8 = K[61];
-   let I8;
-   if (K[62] !== xK)
-     ((I8 = {
-       id: "editorMode",
-       label: "Editor mode",
-       value: xK,
-       options: d8,
-       type: "enum",
-       onChange(H1) {
-         (V6((t1) => ({ ...t1, editorMode: H1 })),
-           Z({ ...P1(), editorMode: H1 }),
-           n("tengu_editor_mode_changed", { mode: H1, source: "config_panel" }));
-       },
-     }),
-       (K[62] = xK),
-       (K[63] = I8));
-   else I8 = K[63];
-   let uK;
-   if (K[64] !== W) ((uK = []), (K[64] = W), (K[65] = uK));
-   else uK = K[65];
-   let jK;
-   if (K[66] !== _.codeDiffFooterEnabled)
-     ((jK = i4("tengu_code_diff_cli", !1)
-       ? [
-           {
-             id: "codeDiffFooterEnabled",
-             label: "Show code diff footer",
-             value: _.codeDiffFooterEnabled ?? !0,
-             type: "boolean",
-             onChange(H1) {
-               (V6((t1) => {
-                 if (t1.codeDiffFooterEnabled === H1) return t1;
-                 return { ...t1, codeDiffFooterEnabled: H1 };
-               }),
-                 Z({ ...P1(), codeDiffFooterEnabled: H1 }),
-                 n("tengu_code_diff_footer_setting_changed", { enabled: H1 }));
-             },
-           },
-         ]
-       : []),
-       (K[66] = _.codeDiffFooterEnabled),
-       (K[67] = jK));
-   else jK = K[67];
-   let BK;
-   if (K[68] !== _.prStatusFooterEnabled)
-     ((BK = i4("tengu_pr_status_cli", !1)
-       ? [
-           {
-             id: "prStatusFooterEnabled",
-             label: "Show PR status footer",
-             value: _.prStatusFooterEnabled ?? !0,
-             type: "boolean",
-             onChange(H1) {
-               (V6((t1) => {
-                 if (t1.prStatusFooterEnabled === H1) return t1;
-                 return { ...t1, prStatusFooterEnabled: H1 };
-               }),
-                 Z({ ...P1(), prStatusFooterEnabled: H1 }),
-                 n("tengu_pr_status_footer_setting_changed", { enabled: H1 }));
-             },
-           },
-         ]
-       : []),
-       (K[68] = _.prStatusFooterEnabled),
-       (K[69] = BK));
-   else BK = K[69];
-   let Z5 = o === null ? "Default (recommended)" : o,
-     J3;
-   if (K[70] !== M1 || K[71] !== Z5)
-     ((J3 = {
-       id: "model",
-       label: "Model",
-       value: Z5,
-       type: "managedEnum",
-       onChange: M1,
-     }),
-       (K[70] = M1),
-       (K[71] = Z5),
-       (K[72] = J3));
-   else J3 = K[72];
-   let S4;
-   if (K[73] !== _.diffTool || K[74] !== CA)
-     ((S4 = CA
-       ? [
-           {
-             id: "diffTool",
-             label: "Diff tool",
-             value: _.diffTool ?? "auto",
-             options: ["terminal", "auto"],
-             type: "enum",
-             onChange(H1) {
-               (V6((t1) => ({ ...t1, diffTool: H1 })),
-                 Z({ ...P1(), diffTool: H1 }),
-                 n("tengu_diff_tool_changed", {
-                   tool: H1,
-                   source: "config_panel",
-                 }));
-             },
-           },
-         ]
-       : []),
-       (K[73] = _.diffTool),
-       (K[74] = CA),
-       (K[75] = S4));
-   else S4 = K[75];
-   let O7;
-   if (K[76] !== _.autoConnectIde)
-     ((O7 = !G$()
-       ? [
-           {
-             id: "autoConnectIde",
-             label: "Auto-connect to IDE (external terminal)",
-             value: _.autoConnectIde ?? !1,
-             type: "boolean",
-             onChange(H1) {
-               (V6((t1) => ({ ...t1, autoConnectIde: H1 })),
-                 Z({ ...P1(), autoConnectIde: H1 }),
-                 n("tengu_auto_connect_ide_changed", {
-                   enabled: H1,
-                   source: "config_panel",
-                 }));
-             },
-           },
-         ]
-       : []),
-       (K[76] = _.autoConnectIde),
-       (K[77] = O7));
-   else O7 = K[77];
-   let hq;
-   if (K[78] !== _.autoInstallIdeExtension)
-     ((hq = G$()
-       ? [
-           {
-             id: "autoInstallIdeExtension",
-             label: "Auto-install IDE extension",
-             value: _.autoInstallIdeExtension ?? !0,
-             type: "boolean",
-             onChange(H1) {
-               (V6((t1) => ({ ...t1, autoInstallIdeExtension: H1 })),
-                 Z({ ...P1(), autoInstallIdeExtension: H1 }),
-                 n("tengu_auto_install_ide_extension_changed", {
-                   enabled: H1,
-                   source: "config_panel",
-                 }));
-             },
-           },
-         ]
-       : []),
-       (K[78] = _.autoInstallIdeExtension),
-       (K[79] = hq));
-   else hq = K[79];
-   let V3 = _.claudeInChromeDefaultEnabled ?? !0,
-     Nq;
-   if (K[80] !== V3)
-     ((Nq = {
-       id: "claudeInChromeDefaultEnabled",
-       label: "Claude in Chrome enabled by default",
-       value: V3,
-       type: "boolean",
-       onChange(H1) {
-         (V6((t1) => ({ ...t1, claudeInChromeDefaultEnabled: H1 })),
-           Z({ ...P1(), claudeInChromeDefaultEnabled: H1 }),
-           n("tengu_claude_in_chrome_setting_changed", { enabled: H1 }));
-       },
-     }),
-       (K[80] = V3),
-       (K[81] = Nq));
-   else Nq = K[81];
-   let d5;
-   if (K[82] !== _.teammateMode)
-     ((d5 = j8()
-       ? (() => {
-           let H1 = GI6();
-           return [
-             {
-               id: "teammateMode",
-               label: H1 ? `Teammate mode [overridden: ${H1}]` : "Teammate mode",
-               value: _.teammateMode ?? "auto",
-               options: ["auto", "tmux", "in-process"],
-               type: "enum",
-               onChange(b6) {
-                 if (b6 !== "auto" && b6 !== "tmux" && b6 !== "in-process")
-                   return;
-                 (WI6(b6),
-                   V6((r8) => ({ ...r8, teammateMode: b6 })),
-                   Z({ ...P1(), teammateMode: b6 }),
-                   n("tengu_teammate_mode_changed", { mode: b6 }));
-               },
-             },
-           ];
-         })()
-       : []),
-       (K[82] = _.teammateMode),
-       (K[83] = d5));
-   else d5 = K[83];
-   let bq;
-   if (K[84] === Symbol.for("react.memo_cache_sentinel"))
-     ((bq = _1
-       ? [
-           {
-             id: "showExternalIncludesDialog",
-             label: "External CLAUDE.md includes",
-             value: mh2(),
-             type: "managedEnum",
-             onChange() {},
-           },
-         ]
-       : []),
-       (K[84] = bq));
-   else bq = K[84];
-   let sK;
-   if (K[85] !== _.customApiKeyResponses?.approved)
-     ((sK = process.env.ANTHROPIC_API_KEY
-       ? [
-           {
-             id: "apiKey",
-             label: Z6.createElement(
-               f,
-               null,
-               "Use custom API key:",
-               " ",
-               Z6.createElement(
-                 f,
-                 { bold: !0 },
-                 hv(process.env.ANTHROPIC_API_KEY),
-               ),
-             ),
-             searchText: "Use custom API key",
-             value: Boolean(
-               process.env.ANTHROPIC_API_KEY &&
-                 _.customApiKeyResponses?.approved?.includes(
-                   hv(process.env.ANTHROPIC_API_KEY),
-                 ),
-             ),
-             type: "boolean",
-             onChange(H1) {
-               (V6((t1) => {
-                 let b6 = { ...t1 };
-                 if (!b6.customApiKeyResponses)
-                   b6.customApiKeyResponses = { approved: [], rejected: [] };
-                 if (!b6.customApiKeyResponses.approved)
-                   b6.customApiKeyResponses = {
-                     ...b6.customApiKeyResponses,
-                     approved: [],
-                   };
-                 if (!b6.customApiKeyResponses.rejected)
-                   b6.customApiKeyResponses = {
-                     ...b6.customApiKeyResponses,
-                     rejected: [],
-                   };
-                 if (process.env.ANTHROPIC_API_KEY) {
-                   let r8 = hv(process.env.ANTHROPIC_API_KEY);
-                   if (H1)
-                     b6.customApiKeyResponses = {
-                       ...b6.customApiKeyResponses,
-                       approved: [
-                         ...(b6.customApiKeyResponses.approved ?? []).filter(
-                           (y4) => y4 !== r8,
-                         ),
-                         r8,
-                       ],
-                       rejected: (
-                         b6.customApiKeyResponses.rejected ?? []
-                       ).filter((y4) => y4 !== r8),
-                     };
-                   else
-                     b6.customApiKeyResponses = {
-                       ...b6.customApiKeyResponses,
-                       approved: (
-                         b6.customApiKeyResponses.approved ?? []
-                       ).filter((y4) => y4 !== r8),
-                       rejected: [
-                         ...(b6.customApiKeyResponses.rejected ?? []).filter(
-                           (y4) => y4 !== r8,
-                         ),
-                         r8,
-                       ],
-                     };
-                 }
-                 return b6;
-               }),
-                 Z(P1()));
-             },
-           },
-         ]
-       : []),
-       (K[85] = _.customApiKeyResponses?.approved),
-       (K[86] = sK));
-   else sK = K[86];
-   let W6;
-   if (
-     K[87] !== $1 ||
-     K[88] !== b1 ||
-     K[89] !== J6 ||
-     K[90] !== fA ||
-     K[91] !== NA ||
-     K[92] !== lA ||
-     K[93] !== q1 ||
-     K[94] !== dA ||
-     K[95] !== T6 ||
-     K[96] !== R8 ||
-     K[97] !== a6 ||
-     K[98] !== V4 ||
-     K[99] !== W8 ||
-     K[100] !== v4 ||
-     K[101] !== MK ||
-     K[102] !== I8 ||
-     K[103] !== uK ||
-     K[104] !== jK ||
-     K[105] !== BK ||
-     K[106] !== J3 ||
-     K[107] !== S4 ||
-     K[108] !== O7 ||
-     K[109] !== hq ||
-     K[110] !== Nq ||
-     K[111] !== d5 ||
-     K[112] !== sK
-   )
-     ((W6 = [
-       $1,
-       b1,
-       J6,
-       fA,
-       ...NA,
-       ...lA,
-       q1,
-       dA,
-       T6,
-       R8,
-       a6,
-       V4,
-       W8,
-       v4,
-       MK,
-       I8,
-       ...uK,
-       ...jK,
-       ...BK,
-       J3,
-       ...S4,
-       ...O7,
-       ...hq,
-       Nq,
-       ...d5,
-       ...bq,
-       ...sK,
-     ]),
-       (K[87] = $1),
-       (K[88] = b1),
-       (K[89] = J6),
-       (K[90] = fA),
-       (K[91] = NA),
-       (K[92] = lA),
-       (K[93] = q1),
-       (K[94] = dA),
-       (K[95] = T6),
-       (K[96] = R8),
-       (K[97] = a6),
-       (K[98] = V4),
-       (K[99] = W8),
-       (K[100] = v4),
-       (K[101] = MK),
-       (K[102] = I8),
-       (K[103] = uK),
-       (K[104] = jK),
-       (K[105] = BK),
-       (K[106] = J3),
-       (K[107] = S4),
-       (K[108] = O7),
-       (K[109] = hq),
-       (K[110] = Nq),
-       (K[111] = d5),
-       (K[112] = sK),
-       (K[113] = W6));
-   else W6 = K[113];
-   let R4 = W6,
-     l8;
-   A: {
-     if (!vA) {
-       l8 = R4;
-       break A;
-     }
-     let H1;
-     if (K[114] !== vA || K[115] !== R4) {
-       let t1 = vA.toLowerCase();
-       ((H1 = R4.filter((b6) => {
-         if (b6.id.toLowerCase().includes(t1)) return !0;
-         return ("searchText" in b6 ? b6.searchText : b6.label)
-           .toLowerCase()
-           .includes(t1);
-       })),
-         (K[114] = vA),
-         (K[115] = R4),
-         (K[116] = H1));
-     } else H1 = K[116];
-     l8 = H1;
-   }
-   let D4 = l8,
-     xq,
-     pK;
-   if (K[117] !== D4.length || K[118] !== Q)
-     ((xq = () => {
-       if (Q >= D4.length) u(Math.max(0, D4.length - 1));
-     }),
-       (pK = [D4.length, Q]),
-       (K[117] = D4.length),
-       (K[118] = Q),
-       (K[119] = xq),
-       (K[120] = pK));
-   else ((xq = K[119]), (pK = K[120]));
-   Z6.useEffect(xq, pK);
-   let f3;
-   if (
-     K[121] !== bA ||
-     K[122] !== B ||
-     K[123] !== R ||
-     K[124] !== _.autoCompactEnabled ||
-     K[125] !== _.autoConnectIde ||
-     K[126] !== _.autoInstallIdeExtension ||
-     K[127] !== _.customApiKeyResponses?.approved ||
-     K[128] !== _.diffTool ||
-     K[129] !== _.editorMode ||
-     K[130] !== _.preferredNotifChannel ||
-     K[131] !== _.respectGitignore ||
-     K[132] !== _.terminalProgressBarEnabled ||
-     K[133] !== _.theme ||
-     K[134] !== q ||
-     K[135] !== V?.autoUpdatesChannel ||
-     K[136] !== KA
-   )
-     ((f3 = () => {
-       if (KA !== null) return;
-       let H1 = Object.entries(bA).map(Bh2),
-         t1 = Boolean(
-           process.env.ANTHROPIC_API_KEY &&
-             j.current.customApiKeyResponses?.approved?.includes(
-               hv(process.env.ANTHROPIC_API_KEY),
-             ),
-         ),
-         b6 = Boolean(
-           process.env.ANTHROPIC_API_KEY &&
-             _.customApiKeyResponses?.approved?.includes(
-               hv(process.env.ANTHROPIC_API_KEY),
-             ),
-         );
-       if (t1 !== b6)
-         (H1.push(`${b6 ? "Enabled" : "Disabled"} custom API key`),
-           n("tengu_config_changed", {
-             key: "env.ANTHROPIC_API_KEY",
-             value: b6,
-           }));
-       if (_.theme !== j.current.theme)
-         H1.push(`Set theme to ${O1.bold(_.theme)}`);
-       if (_.preferredNotifChannel !== j.current.preferredNotifChannel)
-         H1.push(`Set notifications to ${O1.bold(_.preferredNotifChannel)}`);
-       if (R !== S.current) H1.push(`Set output style to ${O1.bold(R)}`);
-       if (B !== F.current)
-         H1.push(
-           `Set response language to ${O1.bold(B ?? "Default (English)")}`,
-         );
-       if (_.editorMode !== j.current.editorMode)
-         H1.push(`Set editor mode to ${O1.bold(_.editorMode || "emacs")}`);
-       if (_.diffTool !== j.current.diffTool)
-         H1.push(`Set diff tool to ${O1.bold(_.diffTool)}`);
-       if (_.autoConnectIde !== j.current.autoConnectIde)
-         H1.push(
-           `${_.autoConnectIde ? "Enabled" : "Disabled"} auto-connect to IDE`,
-         );
-       if (_.autoInstallIdeExtension !== j.current.autoInstallIdeExtension)
-         H1.push(
-           `${_.autoInstallIdeExtension ? "Enabled" : "Disabled"} auto-install IDE extension`,
-         );
-       if (_.autoCompactEnabled !== j.current.autoCompactEnabled)
-         H1.push(
-           `${_.autoCompactEnabled ? "Enabled" : "Disabled"} auto-compact`,
-         );
-       if (_.respectGitignore !== j.current.respectGitignore)
-         H1.push(
-           `${_.respectGitignore ? "Enabled" : "Disabled"} respect .gitignore in file picker`,
-         );
-       if (_.terminalProgressBarEnabled !== j.current.terminalProgressBarEnabled)
-         H1.push(
-           `${_.terminalProgressBarEnabled ? "Enabled" : "Disabled"} terminal progress bar`,
-         );
-       if (V?.autoUpdatesChannel !== k.current?.autoUpdatesChannel)
-         H1.push(
-           `Set auto-update channel to ${O1.bold(V?.autoUpdatesChannel ?? "latest")}`,
-         );
-       if (H1.length > 0)
-         q(
-           H1.join(`
- `),
-         );
-       else q("Config dialog dismissed", { display: "system" });
-     }),
-       (K[121] = bA),
-       (K[122] = B),
-       (K[123] = R),
-       (K[124] = _.autoCompactEnabled),
-       (K[125] = _.autoConnectIde),
-       (K[126] = _.autoInstallIdeExtension),
-       (K[127] = _.customApiKeyResponses?.approved),
-       (K[128] = _.diffTool),
-       (K[129] = _.editorMode),
-       (K[130] = _.preferredNotifChannel),
-       (K[131] = _.respectGitignore),
-       (K[132] = _.terminalProgressBarEnabled),
-       (K[133] = _.theme),
-       (K[134] = q),
-       (K[135] = V?.autoUpdatesChannel),
-       (K[136] = KA),
-       (K[137] = f3));
-   else f3 = K[137];
-   V?.autoUpdatesChannel;
-   let _4 = f3,
-     A8 = KA === null,
-     z7;
-   if (K[138] !== A8)
-     ((z7 = { context: "Settings", isActive: A8 }),
-       (K[138] = A8),
-       (K[139] = z7));
-   else z7 = K[139];
-   s1("confirm:no", _4, z7);
-   let v5;
-   if (
-     K[140] !== D4 ||
-     K[141] !== Q ||
-     K[142] !== H ||
-     K[143] !== w ||
-     K[144] !== z ||
-     K[145] !== V?.autoUpdatesChannel
-   )
-     ((v5 = () => {
-       let H1 = D4[Q];
-       if (!H1 || !H1.onChange) return;
-       if (H1.type === "boolean") {
-         H1.onChange(!H1.value);
-         return;
-       }
-       if (
-         H1.id === "theme" ||
-         H1.id === "model" ||
-         H1.id === "showExternalIncludesDialog" ||
-         H1.id === "outputStyle" ||
-         H1.id === "language"
-       )
-         switch (H1.id) {
-           case "theme": {
-             (zA(0), z(!0), H(!0));
-             return;
-           }
-           case "model": {
-             (zA(1), z(!0));
-             return;
-           }
-           case "showExternalIncludesDialog": {
-             (zA(2), z(!0), w(!0));
-             return;
-           }
-           case "outputStyle": {
-             (zA(3), z(!0));
-             return;
-           }
-           case "language": {
-             (zA(5), z(!0));
-             return;
-           }
-         }
-       if (H1.id === "autoUpdatesChannel") {
-         if ((V?.autoUpdatesChannel ?? "latest") === "latest") (zA(4), z(!0));
-         else
-           (h4("userSettings", {
-             autoUpdatesChannel: "latest",
-             minimumVersion: void 0,
-           }),
-             N(uh2),
-             n("tengu_autoupdate_channel_changed", { channel: "latest" }));
-         return;
-       }
-       if (H1.type === "enum") {
-         let b6 = (H1.options.indexOf(H1.value) + 1) % H1.options.length;
-         H1.onChange(H1.options[b6]);
-         return;
-       }
-     }),
-       (K[140] = D4),
-       (K[141] = Q),
-       (K[142] = H),
-       (K[143] = w),
-       (K[144] = z),
-       (K[145] = V?.autoUpdatesChannel),
-       (K[146] = v5));
-   else v5 = K[146];
-   V?.autoUpdatesChannel;
-   let N3 = v5,
-     tK;
-   if (K[147] !== Q || K[148] !== e)
-     ((tK = () => {
-       if (Q === 0) e(!0);
-       else u(xh2);
-     }),
-       (K[147] = Q),
-       (K[148] = e),
-       (K[149] = tK));
-   else tK = K[149];
-   let u3;
-   if (K[150] !== D4.length)
-     ((u3 = () => {
-       u((H1) => Math.min(D4.length - 1, H1 + 1));
-     }),
-       (K[150] = D4.length),
-       (K[151] = u3));
-   else u3 = K[151];
-   let oA;
-   if (K[152] !== e || K[153] !== ZA)
-     ((oA = () => {
-       (e(!0), ZA(""));
-     }),
-       (K[152] = e),
-       (K[153] = ZA),
-       (K[154] = oA));
-   else oA = K[154];
-   let VA;
-   if (K[155] !== tK || K[156] !== u3 || K[157] !== oA || K[158] !== N3)
-     ((VA = {
-       "select:previous": tK,
-       "select:next": u3,
-       "select:accept": N3,
-       "settings:search": oA,
-     }),
-       (K[155] = tK),
-       (K[156] = u3),
-       (K[157] = oA),
-       (K[158] = N3),
-       (K[159] = VA));
-   else VA = K[159];
-   let WA = KA === null && !JA,
-     xA;
-   if (K[160] !== WA)
-     ((xA = { context: "Settings", isActive: WA }),
-       (K[160] = WA),
-       (K[161] = xA));
-   else xA = K[161];
-   X7(VA, xA);
-   let UA;
-   if (K[162] !== vA || K[163] !== e || K[164] !== ZA)
-     ((UA = (H1, t1) => {
-       if (t1.escape) {
-         if (vA.length > 0) ZA("");
-         else e(!1);
-         return;
-       }
-       if (t1.return || t1.downArrow) (e(!1), u(0));
-     }),
-       (K[162] = vA),
-       (K[163] = e),
-       (K[164] = ZA),
-       (K[165] = UA));
-   else UA = K[165];
-   let pA = JA && KA === null,
-     G1;
-   if (K[166] !== pA) ((G1 = { isActive: pA }), (K[166] = pA), (K[167] = G1));
-   else G1 = K[167];
-   K8(UA, G1);
-   let E1;
-   if (K[168] !== e || K[169] !== ZA)
-     ((E1 = (H1, t1) => {
-       if (!t1.ctrl && !t1.meta && H1.length > 0 && !/^\s+$/.test(H1))
-         (e(!0), ZA(H1));
-     }),
-       (K[168] = e),
-       (K[169] = ZA),
-       (K[170] = E1));
-   else E1 = K[170];
-   let S1 = !JA && KA === null,
-     d1;
-   if (K[171] !== S1) ((d1 = { isActive: S1 }), (K[171] = S1), (K[172] = d1));
-   else d1 = K[172];
-   K8(E1, d1);
-   let F1;
-   if (
-     K[173] !== B ||
-     K[174] !== R ||
-     K[175] !== D4 ||
-     K[176] !== JA ||
-     K[177] !== OA ||
-     K[178] !== o ||
-     K[179] !== M1 ||
-     K[180] !== LA ||
-     K[181] !== vA ||
-     K[182] !== Q ||
-     K[183] !== H ||
-     K[184] !== w ||
-     K[185] !== z ||
-     K[186] !== X ||
-     K[187] !== KA ||
-     K[188] !== O
-   )
-     ((F1 = Z6.createElement(
-       I,
-       { flexDirection: "column", width: "100%" },
-       KA === 0
-         ? Z6.createElement(
-             Z6.Fragment,
-             null,
-             Z6.createElement(YPA, {
-               initialTheme: O,
-               onThemeSelect: (H1) => {
-                 (X(H1), zA(null), H(!1), z(!1));
-               },
-               onCancel: () => {
-                 (zA(null), H(!1), z(!1));
-               },
-               hideEscToCancel: !0,
-               skipExitHandling: !0,
-             }),
-             Z6.createElement(
-               I,
-               { marginLeft: 1 },
-               Z6.createElement(
-                 f,
-                 { dimColor: !0, italic: !0 },
-                 Z6.createElement(
-                   w8,
-                   null,
-                   Z6.createElement(M6, { shortcut: "Enter", action: "select" }),
-                   Z6.createElement(d6, {
-                     action: "confirm:no",
-                     context: "Confirmation",
-                     fallback: "Esc",
-                     description: "cancel",
-                   }),
-                 ),
-               ),
-             ),
-           )
-         : KA === 1
-           ? Z6.createElement(
-               Z6.Fragment,
-               null,
-               Z6.createElement(zPA, {
-                 initial: o,
-                 onSelect: (H1, t1) => {
-                   (M1(H1), zA(null), z(!1));
-                 },
-                 onCancel: () => {
-                   (zA(null), z(!1));
-                 },
-               }),
-               Z6.createElement(
-                 f,
-                 { dimColor: !0 },
-                 Z6.createElement(
-                   w8,
-                   null,
-                   Z6.createElement(M6, {
-                     shortcut: "Enter",
-                     action: "confirm",
-                   }),
-                   Z6.createElement(d6, {
-                     action: "confirm:no",
-                     context: "Confirmation",
-                     fallback: "Esc",
-                     description: "cancel",
-                   }),
-                 ),
-               ),
-             )
-           : KA === 2
-             ? Z6.createElement(
-                 Z6.Fragment,
-                 null,
-                 Z6.createElement(oN1, {
-                   onDone: () => {
-                     (zA(null), z(!1), w(!1));
-                   },
-                   externalIncludes: rIA(),
-                 }),
-                 Z6.createElement(
-                   f,
-                   { dimColor: !0 },
-                   Z6.createElement(
-                     w8,
-                     null,
-                     Z6.createElement(M6, {
-                       shortcut: "Enter",
-                       action: "confirm",
-                     }),
-                     Z6.createElement(d6, {
-                       action: "confirm:no",
-                       context: "Confirmation",
-                       fallback: "Esc",
-                       description: "disable external includes",
-                     }),
-                   ),
-                 ),
-               )
-             : KA === 3
-               ? Z6.createElement(
-                   Z6.Fragment,
-                   null,
-                   Z6.createElement(aN1, {
-                     initialStyle: R,
-                     onComplete: (H1) => {
-                       (b(H1 ?? dZ),
-                         zA(null),
-                         z(!1),
-                         h4("localSettings", { outputStyle: H1 }),
-                         n("tengu_output_style_changed", {
-                           style: H1 ?? dZ,
-                           source: "config_panel",
-                           settings_source: "localSettings",
-                         }));
-                     },
-                     onCancel: () => {
-                       (zA(null), z(!1));
-                     },
-                   }),
-                   Z6.createElement(
-                     f,
-                     { dimColor: !0 },
-                     Z6.createElement(
-                       w8,
-                       null,
-                       Z6.createElement(M6, {
-                         shortcut: "Enter",
-                         action: "confirm",
-                       }),
-                       Z6.createElement(d6, {
-                         action: "confirm:no",
-                         context: "Confirmation",
-                         fallback: "Esc",
-                         description: "cancel",
-                       }),
-                     ),
-                   ),
-                 )
-               : KA === 5
-                 ? Z6.createElement(
-                     Z6.Fragment,
-                     null,
-                     Z6.createElement(q$K, {
-                       initialLanguage: B,
-                       onComplete: (H1) => {
-                         (x(H1),
-                           zA(null),
-                           z(!1),
-                           h4("userSettings", { language: H1 }),
-                           n("tengu_language_changed", {
-                             language: H1 ?? "default",
-                             source: "config_panel",
-                           }));
-                       },
-                       onCancel: () => {
-                         (zA(null), z(!1));
-                       },
-                     }),
-                     Z6.createElement(
-                       f,
-                       { dimColor: !0 },
-                       Z6.createElement(
-                         w8,
-                         null,
-                         Z6.createElement(M6, {
-                           shortcut: "Enter",
-                           action: "confirm",
-                         }),
-                         Z6.createElement(d6, {
-                           action: "confirm:no",
-                           context: "Settings",
-                           fallback: "Esc",
-                           description: "cancel",
-                         }),
-                       ),
-                     ),
-                   )
-                 : KA === 4
-                   ? Z6.createElement(eXK, {
-                       currentVersion: {
-                         ISSUES_EXPLAINER:
-                           "report the issue at https://github.com/anthropics/claude-code/issues",
-                         PACKAGE_URL: "@anthropic-ai/claude-code",
-                         README_URL: "https://code.claude.com/docs/en/overview",
-                         VERSION: "2.1.20",
-                         FEEDBACK_CHANNEL:
-                           "https://github.com/anthropics/claude-code/issues",
-                         BUILD_TIME: "2026-01-27T00:38:42Z",
-                       }.VERSION,
-                       onChoice: (H1) => {
-                         if ((zA(null), z(!1), H1 === "cancel")) return;
-                         let t1 = { autoUpdatesChannel: "stable" };
-                         if (H1 === "stay")
-                           t1.minimumVersion = {
-                             ISSUES_EXPLAINER:
-                               "report the issue at https://github.com/anthropics/claude-code/issues",
-                             PACKAGE_URL: "@anthropic-ai/claude-code",
-                             README_URL:
-                               "https://code.claude.com/docs/en/overview",
-                             VERSION: "2.1.20",
-                             FEEDBACK_CHANNEL:
-                               "https://github.com/anthropics/claude-code/issues",
-                             BUILD_TIME: "2026-01-27T00:38:42Z",
-                           }.VERSION;
-                         (h4("userSettings", t1),
-                           N((b6) => ({ ...b6, ...t1 })),
-                           n("tengu_autoupdate_channel_changed", {
-                             channel: "stable",
-                             minimum_version_set: H1 === "stay",
-                           }));
-                       },
-                     })
-                   : Z6.createElement(
-                       I,
-                       { flexDirection: "column", marginY: 1, gap: 1 },
-                       Z6.createElement(
-                         f,
-                         null,
-                         "Configure Claude Code preferences",
-                       ),
-                       Z6.createElement(BS, {
-                         query: vA,
-                         isFocused: JA,
-                         isTerminalFocused: OA,
-                         cursorOffset: LA,
-                         placeholder: "Search settings...",
-                       }),
-                       Z6.createElement(
-                         I,
-                         { flexDirection: "column" },
-                         D4.length === 0
-                           ? Z6.createElement(
-                               f,
-                               { dimColor: !0, italic: !0 },
-                               'No settings match "',
-                               vA,
-                               '"',
-                             )
-                           : D4.map((H1, t1) => {
-                               let b6 = t1 === Q;
-                               return Z6.createElement(
-                                 I,
-                                 { key: H1.id },
-                                 Z6.createElement(
-                                   I,
-                                   { width: 44 },
-                                   Z6.createElement(
-                                     f,
-                                     { color: b6 ? "suggestion" : void 0 },
-                                     b6 ? K1.pointer : " ",
-                                     " ",
-                                     H1.label,
-                                   ),
-                                 ),
-                                 Z6.createElement(
-                                   I,
-                                   { key: b6 ? "selected" : "unselected" },
-                                   H1.type === "boolean"
-                                     ? Z6.createElement(
-                                         f,
-                                         { color: b6 ? "suggestion" : void 0 },
-                                         H1.value.toString(),
-                                       )
-                                     : H1.id === "theme"
-                                       ? Z6.createElement(
-                                           f,
-                                           { color: b6 ? "suggestion" : void 0 },
-                                           (() => {
-                                             return (
-                                               {
-                                                 dark: "Dark mode",
-                                                 light: "Light mode",
-                                                 "dark-daltonized":
-                                                   "Dark mode (colorblind-friendly)",
-                                                 "light-daltonized":
-                                                   "Light mode (colorblind-friendly)",
-                                                 "dark-ansi":
-                                                   "Dark mode (ANSI colors only)",
-                                                 "light-ansi":
-                                                   "Light mode (ANSI colors only)",
-                                               }[H1.value.toString()] ||
-                                               H1.value.toString()
-                                             );
-                                           })(),
-                                         )
-                                       : H1.id === "notifChannel"
-                                         ? Z6.createElement(
-                                             f,
-                                             {
-                                               color: b6 ? "suggestion" : void 0,
-                                             },
-                                             (() => {
-                                               switch (H1.value.toString()) {
-                                                 case "auto":
-                                                   return "Auto";
-                                                 case "iterm2":
-                                                   return Z6.createElement(
-                                                     Z6.Fragment,
-                                                     null,
-                                                     "iTerm2 ",
-                                                     Z6.createElement(
-                                                       f,
-                                                       { dimColor: !0 },
-                                                       "(OSC 9)",
-                                                     ),
-                                                   );
-                                                 case "terminal_bell":
-                                                   return Z6.createElement(
-                                                     Z6.Fragment,
-                                                     null,
-                                                     "Terminal Bell ",
-                                                     Z6.createElement(
-                                                       f,
-                                                       { dimColor: !0 },
-                                                       "(\\a)",
-                                                     ),
-                                                   );
-                                                 case "kitty":
-                                                   return Z6.createElement(
-                                                     Z6.Fragment,
-                                                     null,
-                                                     "Kitty ",
-                                                     Z6.createElement(
-                                                       f,
-                                                       { dimColor: !0 },
-                                                       "(OSC 99)",
-                                                     ),
-                                                   );
-                                                 case "ghostty":
-                                                   return Z6.createElement(
-                                                     Z6.Fragment,
-                                                     null,
-                                                     "Ghostty ",
-                                                     Z6.createElement(
-                                                       f,
-                                                       { dimColor: !0 },
-                                                       "(OSC 777)",
-                                                     ),
-                                                   );
-                                                 case "iterm2_with_bell":
-                                                   return "iTerm2 w/ Bell";
-                                                 case "notifications_disabled":
-                                                   return "Disabled";
-                                                 default:
-                                                   return H1.value.toString();
-                                               }
-                                             })(),
-                                           )
-                                         : H1.id === "defaultPermissionMode"
-                                           ? Z6.createElement(
-                                               f,
-                                               {
-                                                 color: b6
-                                                   ? "suggestion"
-                                                   : void 0,
-                                               },
-                                               ag(H1.value),
-                                             )
-                                           : H1.id === "autoUpdatesChannel" && L1
-                                             ? Z6.createElement(
-                                                 I,
-                                                 { flexDirection: "column" },
-                                                 Z6.createElement(
-                                                   f,
-                                                   {
-                                                     color: b6
-                                                       ? "suggestion"
-                                                       : void 0,
-                                                   },
-                                                   "disabled",
-                                                 ),
-                                                 Z6.createElement(
-                                                   f,
-                                                   { dimColor: !0 },
-                                                   "(",
-                                                   L1,
-                                                   ")",
-                                                 ),
-                                               )
-                                             : Z6.createElement(
-                                                 f,
-                                                 {
-                                                   color: b6
-                                                     ? "suggestion"
-                                                     : void 0,
-                                                 },
-                                                 H1.value.toString(),
-                                               ),
-                                 ),
-                               );
-                             }),
-                       ),
-                       JA
-                         ? Z6.createElement(
-                             f,
-                             { dimColor: !0 },
-                             Z6.createElement(
-                               w8,
-                               null,
-                               Z6.createElement(f, null, "Type to filter"),
-                               Z6.createElement(M6, {
-                                 shortcut: "Enter/↓",
-                                 action: "select",
-                               }),
-                               Z6.createElement(d6, {
-                                 action: "confirm:no",
-                                 context: "Settings",
-                                 fallback: "Esc",
-                                 description: "clear",
-                               }),
-                             ),
-                           )
-                         : Z6.createElement(
-                             f,
-                             { dimColor: !0 },
-                             Z6.createElement(
-                               w8,
-                               null,
-                               Z6.createElement(d6, {
-                                 action: "select:accept",
-                                 context: "Settings",
-                                 fallback: "Enter/Space",
-                                 description: "change",
-                               }),
-                               Z6.createElement(d6, {
-                                 action: "settings:search",
-                                 context: "Settings",
-                                 fallback: "/",
-                                 description: "search",
-                               }),
-                               Z6.createElement(d6, {
-                                 action: "confirm:no",
-                                 context: "Settings",
-                                 fallback: "Esc",
-                                 description: "cancel",
-                               }),
-                             ),
-                           ),
-                     ),
-     )),
-       (K[173] = B),
-       (K[174] = R),
-       (K[175] = D4),
-       (K[176] = JA),
-       (K[177] = OA),
-       (K[178] = o),
-       (K[179] = M1),
-       (K[180] = LA),
-       (K[181] = vA),
-       (K[182] = Q),
-       (K[183] = H),
-       (K[184] = w),
-       (K[185] = z),
-       (K[186] = X),
-       (K[187] = KA),
-       (K[188] = O),
-       (K[189] = F1));
-   else F1 = K[189];
-   return F1;
- }

--- Removed uh2 (pretty-v2.1.20.js:481343-481345)
- function uh2(A) {
-   return { ...A, autoUpdatesChannel: "latest", minimumVersion: void 0 };
- }

--- Removed Bh2 (pretty-v2.1.20.js:481346-481352)
- function Bh2(A) {
-   let [K, q] = A;
-   return (
-     n("tengu_config_changed", { key: K, value: q }),
-     `Set ${K} to ${O1.bold(q)}`
-   );
- }

--- Removed mh2 (pretty-v2.1.20.js:481353-481356)
- function mh2() {
-   if (M2().hasClaudeMdExternalIncludesApproved) return "true";
-   else return "false";
- }

--- Removed j_K (pretty-v2.1.20.js:485894-486024)
- function j_K(A) {
-   let K = s(18),
-     { onComplete: q } = A,
-     Y = k8(),
-     z;
-   if (K[0] !== q)
-     ((z = async (M) => {
-       let j = M === "yes";
-       (V6((P) => ({
-         ...P,
-         autoConnectIde: j,
-         hasIdeAutoConnectDialogBeenShown: !0,
-       })),
-         q());
-     }),
-       (K[0] = q),
-       (K[1] = z));
-   else z = K[1];
-   let w = z,
-     H;
-   if (K[2] === Symbol.for("react.memo_cache_sentinel"))
-     ((H = { context: "Confirmation" }), (K[2] = H));
-   else H = K[2];
-   s1("confirm:no", q, H);
-   let J;
-   if (K[3] === Symbol.for("react.memo_cache_sentinel"))
-     ((J = [
-       { label: "Yes", value: "yes" },
-       { label: "No", value: "no" },
-     ]),
-       (K[3] = J));
-   else J = K[3];
-   let O = J,
-     X;
-   if (K[4] === Symbol.for("react.memo_cache_sentinel"))
-     ((X = eH.default.createElement(
-       I,
-       { marginBottom: 1 },
-       eH.default.createElement(
-         f,
-         { color: "ide" },
-         "Do you wish to enable auto-connect to IDE?",
-       ),
-     )),
-       (K[4] = X));
-   else X = K[4];
-   let $;
-   if (K[5] !== w)
-     (($ = eH.default.createElement(
-       I,
-       { flexDirection: "column", paddingX: 1 },
-       eH.default.createElement(y6, {
-         options: O,
-         onChange: w,
-         defaultValue: "yes",
-       }),
-     )),
-       (K[5] = w),
-       (K[6] = $));
-   else $ = K[6];
-   let _;
-   if (K[7] === Symbol.for("react.memo_cache_sentinel"))
-     ((_ = eH.default.createElement(
-       I,
-       { marginTop: 1 },
-       eH.default.createElement(
-         f,
-         { dimColor: !0 },
-         "You can also configure this in /config or with the --ide flag",
-       ),
-     )),
-       (K[7] = _));
-   else _ = K[7];
-   let Z;
-   if (K[8] !== $)
-     ((Z = eH.default.createElement(
-       I,
-       {
-         flexDirection: "column",
-         borderStyle: "round",
-         borderColor: "ide",
-         paddingX: 2,
-         paddingY: 1,
-         width: "100%",
-       },
-       X,
-       $,
-       _,
-     )),
-       (K[8] = $),
-       (K[9] = Z));
-   else Z = K[9];
-   let G;
-   if (K[10] !== Y.keyName || K[11] !== Y.pending)
-     ((G = Y.pending
-       ? eH.default.createElement(
-           eH.default.Fragment,
-           null,
-           "Press ",
-           Y.keyName,
-           " again to exit",
-         )
-       : "Enter to confirm"),
-       (K[10] = Y.keyName),
-       (K[11] = Y.pending),
-       (K[12] = G));
-   else G = K[12];
-   let W;
-   if (K[13] !== G)
-     ((W = eH.default.createElement(
-       I,
-       { paddingX: 1 },
-       eH.default.createElement(f, { dimColor: !0 }, G),
-     )),
-       (K[13] = G),
-       (K[14] = W));
-   else W = K[14];
-   let D;
-   if (K[15] !== Z || K[16] !== W)
-     ((D = eH.default.createElement(
-       I,
-       { marginTop: 1, flexDirection: "column" },
-       Z,
-       W,
-     )),
-       (K[15] = Z),
-       (K[16] = W),
-       (K[17] = D));
-   else D = K[17];
-   return D;
- }

--- Removed I_K (pretty-v2.1.20.js:486654-486666)
- var I_K = C(() => {
-   T51();
-   v51();
-   B1();
-   Rx2 = {
-     context: "Chat",
-     bindings: {
-       "ctrl+k ctrl+h": "command:help",
-       "ctrl+k ctrl+k": "command:compact",
-       "ctrl+k ctrl+m": "command:model",
-     },
-   };
- });

--- Removed fMK (pretty-v2.1.20.js:505130-505219)
- function fMK() {
-   let A = s(20),
-     { columns: K } = V8(),
-     [q] = k6(),
-     {
-       version: Y,
-       cwd: z,
-       modelDisplayName: w,
-       billingType: H,
-       agentName: J,
-     } = iT1(),
-     O = q.agent ?? J,
-     X = aT1(),
-     $,
-     _;
-   if (A[0] !== X)
-     (($ = () => {
-       if (X) sT1();
-     }),
-       (_ = [X]),
-       (A[0] = X),
-       (A[1] = $),
-       (A[2] = _));
-   else (($ = A[1]), (_ = A[2]));
-   VMK.useEffect($, _);
-   let Z = Math.max(K - 15, 20),
-     G = o9(Y, Math.max(Z - 13, 6)),
-     { shouldSplit: W, truncatedModel: D, truncatedBilling: M } = AMK(w, H, Z),
-     j = O ? Z - 1 - O.length - 3 : Z,
-     P = opA(z, Math.max(j, 10)),
-     V;
-   if (A[3] === Symbol.for("react.memo_cache_sentinel"))
-     ((V = AK.createElement(sQ2, null)), (A[3] = V));
-   else V = A[3];
-   let N;
-   if (A[4] === Symbol.for("react.memo_cache_sentinel"))
-     ((N = AK.createElement(f, { bold: !0 }, "Claude Code")), (A[4] = N));
-   else N = A[4];
-   let T;
-   if (A[5] !== G)
-     ((T = AK.createElement(
-       f,
-       null,
-       N,
-       " ",
-       AK.createElement(f, { dimColor: !0 }, "v", G),
-     )),
-       (A[5] = G),
-       (A[6] = T));
-   else T = A[6];
-   let k;
-   if (A[7] !== W || A[8] !== M || A[9] !== D)
-     ((k = W
-       ? AK.createElement(
-           AK.Fragment,
-           null,
-           AK.createElement(f, { dimColor: !0 }, D),
-           AK.createElement(f, { dimColor: !0 }, M),
-         )
-       : AK.createElement(f, { dimColor: !0 }, D, " · ", M)),
-       (A[7] = W),
-       (A[8] = M),
-       (A[9] = D),
-       (A[10] = k));
-   else k = A[10];
-   let R = O ? `@${O} · ${P}` : P,
-     b;
-   if (A[11] !== R)
-     ((b = AK.createElement(f, { dimColor: !0 }, R)), (A[11] = R), (A[12] = b));
-   else b = A[12];
-   let S;
-   if (A[13] !== X)
-     ((S = X && AK.createElement(PMK, null)), (A[13] = X), (A[14] = S));
-   else S = A[14];
-   let B;
-   if (A[15] !== T || A[16] !== k || A[17] !== b || A[18] !== S)
-     ((B = AK.createElement(
-       I,
-       { flexDirection: "row", gap: 2, alignItems: "center" },
-       V,
-       AK.createElement(I, { flexDirection: "column" }, T, k, b, S),
-     )),
-       (A[15] = T),
-       (A[16] = k),
-       (A[17] = b),
-       (A[18] = S),
-       (A[19] = B));
-   else B = A[19];
-   return B;
- }

--- Removed vMK (pretty-v2.1.20.js:505276-505779)
- function vMK(A) {
-   let K = s(75),
-     { isBeforeFirstMessage: q } = A,
-     Y = lDK(q),
-     z = eDK(),
-     w = P1().oauthAccount?.displayName ?? "",
-     { columns: H } = V8(),
-     J;
-   if (K[0] === Symbol.for("react.memo_cache_sentinel"))
-     ((J = W_4()), (K[0] = J));
-   else J = K[0];
-   let O = J,
-     X;
-   if (K[1] === Symbol.for("react.memo_cache_sentinel"))
-     ((X = x8.isSandboxingEnabled()), (K[1] = X));
-   else X = K[1];
-   let $ = X,
-     _ = aT1(),
-     Z = sj(),
-     [G] = k6(),
-     W = P1(),
-     D;
-   try {
-     D = KMK(3);
-   } catch {
-     D = [];
-   }
-   let M = Z.companyAnnouncements,
-     [j] = KdA.useState(() =>
-       M && M.length > 0
-         ? W.numStartups === 1
-           ? M[0]
-           : M[Math.floor(Math.random() * M.length)]
-         : void 0,
-     ),
-     { hasReleaseNotes: P } = cpA(W.lastReleaseNotesSeen),
-     V;
-   if (K[2] === Symbol.for("react.memo_cache_sentinel"))
-     ((V = () => {
-       if (
-         P1().lastReleaseNotesSeen ===
-         {
-           ISSUES_EXPLAINER:
-             "report the issue at https://github.com/anthropics/claude-code/issues",
-           PACKAGE_URL: "@anthropic-ai/claude-code",
-           README_URL: "https://code.claude.com/docs/en/overview",
-           VERSION: "2.1.20",
-           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-           BUILD_TIME: "2026-01-27T00:38:42Z",
-         }.VERSION
-       )
-         return;
-       if ((V6(KU2), O)) D_4();
-     }),
-       (K[2] = V));
-   else V = K[2];
-   let N;
-   if (K[3] !== W) ((N = [W, O]), (K[3] = W), (K[4] = N));
-   else N = K[4];
-   KdA.useEffect(V, N);
-   let T, k;
-   if (K[5] !== _)
-     ((T = () => {
-       if (_ && !O) sT1();
-     }),
-       (k = [_, O]),
-       (K[5] = _),
-       (K[6] = T),
-       (K[7] = k));
-   else ((T = K[6]), (k = K[7]));
-   KdA.useEffect(T, k);
-   let {
-       version: R,
-       cwd: b,
-       modelDisplayName: S,
-       billingType: B,
-       agentName: x,
-     } = iT1(),
-     F = G.agent ?? x,
-     Q = o9(S, _g6 - 20);
-   if (!P && !O && !N1(process.env.CLAUDE_CODE_FORCE_FULL_LOGO)) {
-     let fA, NA, lA, q1, dA;
-     if (K[8] === Symbol.for("react.memo_cache_sentinel"))
-       ((lA = f8.createElement(I, null)),
-         (q1 = f8.createElement(fMK, null)),
-         (dA =
-           u2A() &&
-           f8.createElement(
-             I,
-             { paddingLeft: 2, flexDirection: "column" },
-             f8.createElement(f, { color: "warning" }, "Debug mode enabled"),
-             f8.createElement(
-               f,
-               { dimColor: !0 },
-               "Logging to: ",
-               Eh() ? "stderr" : cfA(),
-             ),
-           )),
-         (fA = f8.createElement($g6, null)),
-         (NA =
-           process.env.CLAUDE_CODE_TMUX_SESSION &&
-           f8.createElement(
-             I,
-             { paddingLeft: 2, flexDirection: "column" },
-             f8.createElement(
-               f,
-               { dimColor: !0 },
-               "tmux session: ",
-               process.env.CLAUDE_CODE_TMUX_SESSION,
-             ),
-             f8.createElement(
-               f,
-               { dimColor: !0 },
-               process.env.CLAUDE_CODE_TMUX_PREFIX_CONFLICTS
-                 ? `Detach: ${process.env.CLAUDE_CODE_TMUX_PREFIX} ${process.env.CLAUDE_CODE_TMUX_PREFIX} d (press prefix twice - Claude uses ${process.env.CLAUDE_CODE_TMUX_PREFIX})`
-                 : `Detach: ${process.env.CLAUDE_CODE_TMUX_PREFIX} d`,
-             ),
-           )),
-         (K[8] = fA),
-         (K[9] = NA),
-         (K[10] = lA),
-         (K[11] = q1),
-         (K[12] = dA));
-     else ((fA = K[8]), (NA = K[9]), (lA = K[10]), (q1 = K[11]), (dA = K[12]));
-     let iA;
-     if (K[13] !== j || K[14] !== W)
-       ((iA =
-         j &&
-         f8.createElement(
-           I,
-           { paddingLeft: 2, flexDirection: "column" },
-           !process.env.IS_DEMO &&
-             W.oauthAccount?.organizationName &&
-             f8.createElement(
-               f,
-               { dimColor: !0 },
-               "Message from ",
-               W.oauthAccount.organizationName,
-               ":",
-             ),
-           f8.createElement(f, null, j),
-         )),
-         (K[13] = j),
-         (K[14] = W),
-         (K[15] = iA));
-     else iA = K[15];
-     let j1, T1;
-     if (K[16] === Symbol.for("react.memo_cache_sentinel"))
-       ((j1 = !1), (T1 = !1), (K[16] = j1), (K[17] = T1));
-     else ((j1 = K[16]), (T1 = K[17]));
-     let U1;
-     if (K[18] !== iA)
-       ((U1 = f8.createElement(
-         f8.Fragment,
-         null,
-         lA,
-         q1,
-         dA,
-         fA,
-         NA,
-         iA,
-         j1,
-         T1,
-       )),
-         (K[18] = iA),
-         (K[19] = U1));
-     else U1 = K[19];
-     return U1;
-   }
-   let u = oDK(H),
-     d = P1().theme,
-     a = ` ${U8("claude", d)("Claude Code")} ${U8("inactive", d)(`v${R}`)} `,
-     l = U8("claude", d)(" Claude Code ");
-   if (u === "compact") {
-     let fA = lT1(w);
-     if (fA.length > H - 4) {
-       let T1;
-       if (K[20] === Symbol.for("react.memo_cache_sentinel"))
-         ((T1 = lT1(null)), (K[20] = T1));
-       else T1 = K[20];
-       fA = T1;
-     }
-     let NA = F ? H - 4 - 1 - F.length - 3 : H - 4,
-       lA = opA(b, Math.max(NA, 10)),
-       q1;
-     if (K[21] !== l)
-       ((q1 = { content: l, position: "top", align: "start", offset: 1 }),
-         (K[21] = l),
-         (K[22] = q1));
-     else q1 = K[22];
-     let dA;
-     if (K[23] === Symbol.for("react.memo_cache_sentinel"))
-       ((dA = f8.createElement(Og6, null)), (K[23] = dA));
-     else dA = K[23];
-     let iA;
-     if (K[24] !== Y)
-       ((iA = f8.createElement(
-         I,
-         { marginY: 1 },
-         f8.createElement(
-           I,
-           { height: 5, flexDirection: "column", justifyContent: "flex-end" },
-           f8.createElement(I, { marginBottom: Y }, dA),
-         ),
-       )),
-         (K[24] = Y),
-         (K[25] = iA));
-     else iA = K[25];
-     let j1;
-     if (K[26] !== $)
-       ((j1 =
-         $ &&
-         f8.createElement(
-           I,
-           { marginTop: 1, flexDirection: "column" },
-           f8.createElement(
-             f,
-             { color: "warning" },
-             "Your bash commands will be sandboxed. Disable with /sandbox.",
-           ),
-         )),
-         (K[26] = $),
-         (K[27] = j1));
-     else j1 = K[27];
-     return f8.createElement(
-       f8.Fragment,
-       null,
-       f8.createElement(
-         I,
-         {
-           flexDirection: "column",
-           borderStyle: "round",
-           borderColor: "claude",
-           borderText: q1,
-           paddingX: 1,
-           paddingY: 1,
-           alignItems: "center",
-           width: H,
-         },
-         f8.createElement(f, { bold: !0 }, fA),
-         iA,
-         f8.createElement(f, { dimColor: !0 }, Q),
-         f8.createElement(f, { dimColor: !0 }, B),
-         f8.createElement(f, { dimColor: !0 }, F ? `@${F} · ${lA}` : lA),
-       ),
-       j1,
-     );
-   }
-   let e = lT1(w),
-     JA =
-       !process.env.IS_DEMO && W.oauthAccount?.organizationName
-         ? `${Q} · ${B} · ${W.oauthAccount.organizationName}`
-         : `${Q} · ${B}`,
-     OA = F ? _g6 - 1 - F.length - 3 : _g6,
-     HA = opA(b, Math.max(OA, 10)),
-     DA = F ? `@${F} · ${HA}` : HA,
-     o = sDK(e, DA, JA),
-     { leftWidth: _A, rightWidth: PA } = aDK(H, u, o),
-     jA;
-   if (K[28] === Symbol.for("react.memo_cache_sentinel"))
-     ((jA = f8.createElement(I, null)), (K[28] = jA));
-   else jA = K[28];
-   let yA = I,
-     bA = "column",
-     YA = "round",
-     KA = "claude",
-     zA;
-   if (K[29] !== a)
-     ((zA = { content: a, position: "top", align: "start", offset: 3 }),
-       (K[29] = a),
-       (K[30] = zA));
-   else zA = K[30];
-   let AA = I,
-     t = u === "horizontal" ? "row" : "column",
-     $A = 1,
-     vA = 1,
-     ZA;
-   if (K[31] !== e)
-     ((ZA = f8.createElement(
-       I,
-       { marginTop: 1 },
-       f8.createElement(f, { bold: !0 }, e),
-     )),
-       (K[31] = e),
-       (K[32] = ZA));
-   else ZA = K[32];
-   let LA;
-   if (K[33] === Symbol.for("react.memo_cache_sentinel"))
-     ((LA = f8.createElement(Og6, null)), (K[33] = LA));
-   else LA = K[33];
-   let mA;
-   if (K[34] !== Y)
-     ((mA = f8.createElement(
-       I,
-       { height: 5, flexDirection: "column", justifyContent: "flex-end" },
-       f8.createElement(I, { marginBottom: Y }, LA),
-     )),
-       (K[34] = Y),
-       (K[35] = mA));
-   else mA = K[35];
-   let CA;
-   if (K[36] !== JA)
-     ((CA = f8.createElement(f, { dimColor: !0 }, JA)),
-       (K[36] = JA),
-       (K[37] = CA));
-   else CA = K[37];
-   let IA;
-   if (K[38] !== DA)
-     ((IA = f8.createElement(f, { dimColor: !0 }, DA)),
-       (K[38] = DA),
-       (K[39] = IA));
-   else IA = K[39];
-   let sA;
-   if (K[40] !== CA || K[41] !== IA)
-     ((sA = f8.createElement(
-       I,
-       { flexDirection: "column", alignItems: "center" },
-       CA,
-       IA,
-     )),
-       (K[40] = CA),
-       (K[41] = IA),
-       (K[42] = sA));
-   else sA = K[42];
-   let w1;
-   if (K[43] !== _A || K[44] !== ZA || K[45] !== mA || K[46] !== sA)
-     ((w1 = f8.createElement(
-       I,
-       {
-         flexDirection: "column",
-         width: _A,
-         justifyContent: "space-between",
-         alignItems: "center",
-         minHeight: 9,
-       },
-       ZA,
-       mA,
-       sA,
-     )),
-       (K[43] = _A),
-       (K[44] = ZA),
-       (K[45] = mA),
-       (K[46] = sA),
-       (K[47] = w1));
-   else w1 = K[47];
-   let _1;
-   if (K[48] !== u)
-     ((_1 =
-       u === "horizontal" &&
-       f8.createElement(U3, {
-         orientation: "vertical",
-         dividerColor: "claude",
-       })),
-       (K[48] = u),
-       (K[49] = _1));
-   else _1 = K[49];
-   let k1 =
-       u === "horizontal" &&
-       f8.createElement(HMK, {
-         feeds: O
-           ? [WMK(mK6()), oT1(z)]
-           : _
-             ? [oT1(z), DMK()]
-             : [oT1(z), GMK(D)],
-         maxWidth: PA,
-       }),
-     L1;
-   if (
-     K[50] !== AA ||
-     K[51] !== t ||
-     K[52] !== w1 ||
-     K[53] !== _1 ||
-     K[54] !== k1
-   )
-     ((L1 = f8.createElement(
-       AA,
-       { flexDirection: t, paddingX: $A, gap: vA },
-       w1,
-       _1,
-       k1,
-     )),
-       (K[50] = AA),
-       (K[51] = t),
-       (K[52] = w1),
-       (K[53] = _1),
-       (K[54] = k1),
-       (K[55] = L1));
-   else L1 = K[55];
-   let x1;
-   if (K[56] !== yA || K[57] !== zA || K[58] !== L1)
-     ((x1 = f8.createElement(
-       yA,
-       { flexDirection: bA, borderStyle: YA, borderColor: KA, borderText: zA },
-       L1,
-     )),
-       (K[56] = yA),
-       (K[57] = zA),
-       (K[58] = L1),
-       (K[59] = x1));
-   else x1 = K[59];
-   let M1, c1, z1;
-   if (K[60] === Symbol.for("react.memo_cache_sentinel"))
-     ((M1 =
-       u2A() &&
-       f8.createElement(
-         I,
-         { paddingLeft: 2, flexDirection: "column" },
-         f8.createElement(f, { color: "warning" }, "Debug mode enabled"),
-         f8.createElement(
-           f,
-           { dimColor: !0 },
-           "Logging to: ",
-           Eh() ? "stderr" : cfA(),
-         ),
-       )),
-       (c1 = f8.createElement($g6, null)),
-       (z1 =
-         process.env.CLAUDE_CODE_TMUX_SESSION &&
-         f8.createElement(
-           I,
-           { paddingLeft: 2, flexDirection: "column" },
-           f8.createElement(
-             f,
-             { dimColor: !0 },
-             "tmux session: ",
-             process.env.CLAUDE_CODE_TMUX_SESSION,
-           ),
-           f8.createElement(
-             f,
-             { dimColor: !0 },
-             process.env.CLAUDE_CODE_TMUX_PREFIX_CONFLICTS
-               ? `Detach: ${process.env.CLAUDE_CODE_TMUX_PREFIX} ${process.env.CLAUDE_CODE_TMUX_PREFIX} d (press prefix twice - Claude uses ${process.env.CLAUDE_CODE_TMUX_PREFIX})`
-               : `Detach: ${process.env.CLAUDE_CODE_TMUX_PREFIX} d`,
-           ),
-         )),
-       (K[60] = M1),
-       (K[61] = c1),
-       (K[62] = z1));
-   else ((M1 = K[60]), (c1 = K[61]), (z1 = K[62]));
-   let $1;
-   if (K[63] !== j || K[64] !== W)
-     (($1 =
-       j &&
-       f8.createElement(
-         I,
-         { paddingLeft: 2, flexDirection: "column" },
-         !process.env.IS_DEMO &&
-           W.oauthAccount?.organizationName &&
-           f8.createElement(
-             f,
-             { dimColor: !0 },
-             "Message from ",
-             W.oauthAccount.organizationName,
-             ":",
-           ),
-         f8.createElement(f, null, j),
-       )),
-       (K[63] = j),
-       (K[64] = W),
-       (K[65] = $1));
-   else $1 = K[65];
-   let V1;
-   if (K[66] !== $)
-     ((V1 =
-       $ &&
-       f8.createElement(
-         I,
-         { paddingLeft: 2, flexDirection: "column" },
-         f8.createElement(
-           f,
-           { color: "warning" },
-           "Your bash commands will be sandboxed. Disable with /sandbox.",
-         ),
-       )),
-       (K[66] = $),
-       (K[67] = V1));
-   else V1 = K[67];
-   let b1, X6;
-   if (K[68] === Symbol.for("react.memo_cache_sentinel"))
-     ((b1 = !1), (X6 = !1), (K[68] = b1), (K[69] = X6));
-   else ((b1 = K[68]), (X6 = K[69]));
-   let J6;
-   if (K[70] !== x1 || K[71] !== $1 || K[72] !== V1 || K[73] !== jA)
-     ((J6 = f8.createElement(
-       f8.Fragment,
-       null,
-       jA,
-       x1,
-       M1,
-       c1,
-       z1,
-       $1,
-       V1,
-       b1,
-       X6,
-     )),
-       (K[70] = x1),
-       (K[71] = $1),
-       (K[72] = V1),
-       (K[73] = jA),
-       (K[74] = J6));
-   else J6 = K[74];
-   return J6;
- }

--- Removed KU2 (pretty-v2.1.20.js:505780-505806)
- function KU2(A) {
-   if (
-     A.lastReleaseNotesSeen ===
-     {
-       ISSUES_EXPLAINER:
-         "report the issue at https://github.com/anthropics/claude-code/issues",
-       PACKAGE_URL: "@anthropic-ai/claude-code",
-       README_URL: "https://code.claude.com/docs/en/overview",
-       VERSION: "2.1.20",
-       FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-       BUILD_TIME: "2026-01-27T00:38:42Z",
-     }.VERSION
-   )
-     return A;
-   return {
-     ...A,
-     lastReleaseNotesSeen: {
-       ISSUES_EXPLAINER:
-         "report the issue at https://github.com/anthropics/claude-code/issues",
-       PACKAGE_URL: "@anthropic-ai/claude-code",
-       README_URL: "https://code.claude.com/docs/en/overview",
-       VERSION: "2.1.20",
-       FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-       BUILD_TIME: "2026-01-27T00:38:42Z",
-     }.VERSION,
-   };
- }

--- Removed gEK (pretty-v2.1.20.js:540388-540390)
- function gEK() {
-   return;
- }

--- Removed aAz (pretty-v2.1.20.js:555902-555904)
- function aAz(A) {
-   return Math.max(0, A - 1);
- }

--- Removed V6z (pretty-v2.1.20.js:562303-562303)
- function V6z() {}

--- Removed kBK (pretty-v2.1.20.js:565279-565279)
- function kBK() {}

--- Removed MFK (pretty-v2.1.20.js:573027-573045)
- async function MFK() {
-   h("installPluginsForHeadless: starting");
-   try {
-     let [, A, K] = await Promise.all([wk1(), RpA(), ypA()]),
-       Y = A.filter((w) => !K.includes(w)).filter((w) => w.endsWith(`@${pd}`));
-     if (Y.length === 0)
-       return (h("installPluginsForHeadless: no plugins to install"), !1);
-     let z = await vT1(Y, () => {});
-     if (z.installed.length > 0) sB();
-     return (
-       h(
-         `installPluginsForHeadless: ${z.installed.length} installed, ${z.failed.length} failed`,
-       ),
-       z.installed.length > 0
-     );
-   } catch (A) {
-     return (qA(A instanceof Error ? A : Error(String(A))), !1);
-   }
- }

--- Removed import@476812 (pretty-v2.1.20.js:476813-476813)
- import { createHash as BS2 } from "node:crypto";

=== Added ===

+++ Added Yl6 (pretty-v2.1.21.js:519-523)
+ function Yl6(A) {
+   return (K) => {
+     if (K.code === "EPIPE") A.destroy();
+   };
+ }

+++ Added zl6 (pretty-v2.1.21.js:524-527)
+ function zl6() {
+   (process.stdout.on("error", Yl6(process.stdout)),
+     process.stderr.on("error", Yl6(process.stderr)));
+ }

+++ Added wl6 (pretty-v2.1.21.js:528-531)
+ function wl6(A, K) {
+   if (A.destroyed) return;
+   A.write(K);
+ }

+++ Added k7 (pretty-v2.1.21.js:532-534)
+ function k7(A) {
+   wl6(process.stdout, A);
+ }

+++ Added wl (pretty-v2.1.21.js:535-537)
+ function wl(A) {
+   wl6(process.stderr, A);
+ }

+++ Added Ol (pretty-v2.1.21.js:1795-1795)
+   Ol = "structured-outputs-2025-12-15",

+++ Added ib8 (pretty-v2.1.21.js:103129-103135)
+ function ib8(A) {
+   let { hasThinking: K = !1 } = A ?? {},
+     q = [];
+   if (K && V4("tengu_marble_anvil", !1))
+     q.push({ type: "clear_thinking_20251015", keep: "all" });
+   return q.length > 0 ? { edits: q } : void 0;
+ }

+++ Added JH4 (pretty-v2.1.21.js:160522-160706)
+ var JH4 = C(() => {
+   wH4 = `Use this tool to create and manage a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user.
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
+ * Uses the ${l5} tool to add a comment to the calculateTotal function *
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

+++ Added jH4 (pretty-v2.1.21.js:160882-160884)
+ function jH4(A) {
+   return i0A(Lk(A), Co3);
+ }

+++ Added B46 (pretty-v2.1.21.js:160885-160894)
+ function B46(A) {
+   let K = jH4(A);
+   try {
+     let q = GH4(K, "utf-8").trim(),
+       Y = parseInt(q, 10);
+     return isNaN(Y) ? 0 : Y;
+   } catch {
+     return 0;
+   }
+ }

+++ Added MH4 (pretty-v2.1.21.js:160895-160898)
+ function MH4(A, K) {
+   let q = jH4(A);
+   b8(q, String(K));
+ }

+++ Added Lo3 (pretty-v2.1.21.js:160965-160969)
+ function Lo3(A) {
+   let K = PH4(A),
+     q = B46(A);
+   return Math.max(K, q);
+ }

+++ Added n0A (pretty-v2.1.21.js:160970-160983)
+ function n0A(A, K) {
+   let q = VH4(A),
+     Y;
+   try {
+     Y = aRA.default.lockSync(q);
+     let z = Lo3(A),
+       w = String(z + 1),
+       H = { id: w, ...K },
+       J = sRA(A, w);
+     return (b8(J, QA(H, null, 2)), Cq1(), w);
+   } finally {
+     if (Y) Y();
+   }
+ }

+++ Added Co3 (pretty-v2.1.21.js:161156-161156)
+   Co3 = ".highwatermark",

+++ Added KO4 (pretty-v2.1.21.js:174642-174645)
+ function KO4() {
+   if (!AO4) ((AO4 = !0), h("Layout engine: yoga"));
+   return "yoga";
+ }

+++ Added Os3 (pretty-v2.1.21.js:176277-176280)
+ function Os3() {
+   let A = new Int32Array(128);
+   return (A.fill(-1), (A[32] = wr), A);
+ }

+++ Added t76 (pretty-v2.1.21.js:176362-176365)
+ function t76(A, K, q) {
+   if (K < 0 || q < 0 || K >= A.width || q >= A.height) return;
+   return $s3(A, q * A.width + K);
+ }

+++ Added $s3 (pretty-v2.1.21.js:176366-176375)
+ function $s3(A, K) {
+   let q = A.chars[K],
+     Y = A.styleIds[K];
+   return {
+     char: A.charStrings[q] ?? " ",
+     styleId: Y === fQ ? A.emptyStyleId : Y,
+     width: A.widths[K],
+     hyperlink: gO4(A, A.hyperlinkIds[K]),
+   };
+ }

+++ Added J51 (pretty-v2.1.21.js:176376-176383)
+ function J51(A, K, q) {
+   let Y = A.chars[K],
+     z = A.styleIds[K];
+   ((q.char = A.charStrings[Y] ?? " "),
+     (q.styleId = z === fQ ? A.emptyStyleId : z),
+     (q.width = A.widths[K]),
+     (q.hyperlink = gO4(A, A.hyperlinkIds[K])));
+ }

+++ Added QO4 (pretty-v2.1.21.js:176440-176454)
+ function QO4(A, K) {
+   if (K.length === 1) {
+     let z = K.charCodeAt(0);
+     if (z < 128) {
+       let w = A.charAscii[z];
+       if (w !== -1) return w;
+       let H = A.charStrings.length;
+       return (A.charStrings.push(K), (A.charAscii[z] = H), H);
+     }
+   }
+   let q = A.charStringMap.get(K);
+   if (q !== void 0) return q;
+   let Y = A.charStrings.length;
+   return (A.charStrings.push(K), A.charStringMap.set(K, Y), Y);
+ }

+++ Added UO4 (pretty-v2.1.21.js:176455-176489)
+ function UO4(A, K, q, Y) {
+   if (q < 0 || Y < 0 || q >= A.width || Y >= A.height) return;
+   if (q >= K.width || Y >= K.height) return;
+   let z = Y * K.width + q,
+     w = Y * A.width + q,
+     H = K.charStrings[K.chars[z]];
+   A.chars[w] = QO4(A, H);
+   let J = K.styleIds[z];
+   ((A.styleIds[w] = J === fQ ? A.emptyStyleId : J),
+     (A.widths[w] = K.widths[z]));
+   let O = K.hyperlinkIds[z];
+   if (O === 0) A.hyperlinkIds[w] = 0;
+   else A.hyperlinkIds[w] = mO4(A, K.hyperlinks[O]);
+   let X = A.damage;
+   if (X) {
+     let $ = X.x + X.width,
+       _ = X.y + X.height;
+     if (q < X.x) ((X.width += X.x - q), (X.x = q));
+     else if (q >= $) X.width = q - X.x + 1;
+     if (Y < X.y) ((X.height += X.y - Y), (X.y = Y));
+     else if (Y >= _) X.height = Y - X.y + 1;
+   } else A.damage = { x: q, y: Y, width: 1, height: 1 };
+   if (K.widths[z] === 1) {
+     let $ = q + 1;
+     if ($ < A.width) {
+       let _ = Y * A.width + $;
+       ((A.chars[_] = O51),
+         (A.styleIds[_] = A.emptyStyleId),
+         (A.widths[_] = 2),
+         (A.hyperlinkIds[_] = 0));
+       let Z = A.damage;
+       if (Z && $ >= Z.x + Z.width) Z.width = $ - Z.x + 1;
+     }
+   }
+ }

+++ Added iO4 (pretty-v2.1.21.js:176507-176509)
+ function iO4(A) {
+   return A.filter((K) => !K.code.startsWith(cO4) || !dO4.test(K.code));
+ }

+++ Added OXA (pretty-v2.1.21.js:176590-176596)
+ var OXA = C(() => {
+   C76();
+   a76();
+   t8A();
+   ((dO4 = new RegExp(`^${tn}\\]8${Ar}${Ar}([^${en}]*)${en}$`)),
+     (cO4 = `${tn}]8${Ar}`));
+ });

+++ Added u$4 (pretty-v2.1.21.js:180560-180582)
+ function u$4() {
+   let A = process.env.TERM_PROGRAM,
+     K = process.env.TERM;
+   if (
+     A === "iTerm.app" ||
+     A === "WezTerm" ||
+     A === "ghostty" ||
+     A === "contour" ||
+     A === "vscode" ||
+     A === "alacritty"
+   )
+     return !0;
+   if (K?.includes("kitty") || process.env.KITTY_WINDOW_ID) return !0;
+   if (K === "xterm-ghostty") return !0;
+   if (K?.startsWith("foot")) return !0;
+   if (K?.includes("alacritty")) return !0;
+   if (process.env.WT_SESSION) return !0;
+   let q = process.env.VTE_VERSION;
+   if (q) {
+     if (parseInt(q, 10) >= 6800) return !0;
+   }
+   return !1;
+ }

+++ Added o$4 (pretty-v2.1.21.js:181618-181622)
+ function o$4(A) {
+   let K = new Date().toISOString().slice(0, 10);
+   if (i$4 === K) return;
+   ((i$4 = K), n("tengu_custom_keybindings_loaded", { user_binding_count: A }));
+ }

+++ Added D4A (pretty-v2.1.21.js:183999-184026)
+ function D4A() {
+   let A = mk.useContext(ZXA),
+     K = mk.useRef(null),
+     [q, Y] = mk.useState(!0),
+     z = mk.useCallback((H) => {
+       K.current = H;
+     }, []);
+   mk.useLayoutEffect(() => {
+     let H = K.current;
+     if (!H?.yogaNode || !A) return;
+     let J = H.yogaNode.getComputedHeight(),
+       O = A.rows,
+       X = H.yogaNode.getComputedTop(),
+       $ = 0,
+       _ = H.yogaNode.getParent();
+     while (_)
+       ((X += _.getComputedTop()),
+         ($ = _.getComputedHeight()),
+         (_ = _.getParent()));
+     let Z = X + J,
+       G = Math.max(0, $ - O),
+       W = G + O,
+       D = Z > G && X < W;
+     Y(D);
+   });
+   let w = mk.useMemo(() => ({ isVisible: q }), [q]);
+   return [z, w];
+ }

+++ Added r8 (pretty-v2.1.21.js:184202-184204)
+ function r8(A, K) {
+   return n_4(O7, K, A);
+ }

+++ Added k69 (pretty-v2.1.21.js:185096-185132)
+ function k69() {
+   let A = process.env.SHELL || "",
+     K = E69(),
+     q = Pr(K, ".claude");
+   if (A.endsWith("/zsh") || A.endsWith("/zsh.exe")) {
+     let Y = Pr(q, "completion.zsh");
+     return {
+       name: "zsh",
+       rcFile: Pr(K, ".zshrc"),
+       cacheFile: Y,
+       completionLine: `[[ -f "${Y}" ]] && source "${Y}"`,
+       shellFlag: "zsh",
+     };
+   }
+   if (A.endsWith("/bash") || A.endsWith("/bash.exe")) {
+     let Y = Pr(q, "completion.bash");
+     return {
+       name: "bash",
+       rcFile: Pr(K, ".bashrc"),
+       cacheFile: Y,
+       completionLine: `[ -f "${Y}" ] && source "${Y}"`,
+       shellFlag: "bash",
+     };
+   }
+   if (A.endsWith("/fish") || A.endsWith("/fish.exe")) {
+     let Y = process.env.XDG_CONFIG_HOME || Pr(K, ".config"),
+       z = Pr(q, "completion.fish");
+     return {
+       name: "fish",
+       rcFile: Pr(Y, "fish", "config.fish"),
+       cacheFile: z,
+       completionLine: `[ -f "${z}" ] && source "${z}"`,
+       shellFlag: "fish",
+     };
+   }
+   return null;
+ }

+++ Added wq6 (pretty-v2.1.21.js:185133-185146)
+ async function wq6() {
+   let A = k69();
+   if (!A) return;
+   h(`update: Regenerating ${A.name} completion cache`);
+   let K = process.argv[1] || "claude";
+   if (
+     (await L6(K, ["completion", A.shellFlag, "--output", A.cacheFile])).code !==
+     0
+   ) {
+     h(`update: Failed to regenerate ${A.name} completion cache`);
+     return;
+   }
+   h(`update: Regenerated ${A.name} completion cache at ${A.cacheFile}`);
+ }

+++ Added W_9 (pretty-v2.1.21.js:192954-192963)
+ function W_9(A) {
+   let K = VK();
+   if (K === "foundry") return !0;
+   if (K === "firstParty") return !A.includes("claude-3-");
+   return (
+     A.includes("claude-opus-4") ||
+     A.includes("claude-sonnet-4") ||
+     A.includes("claude-haiku-4")
+   );
+ }

+++ Added A36 (pretty-v2.1.21.js:192964-192971)
+ function A36(A) {
+   return (
+     A.includes("claude-sonnet-4-5") ||
+     A.includes("claude-opus-4-1") ||
+     A.includes("claude-opus-4-5") ||
+     A.includes("claude-haiku-4-5")
+   );
+ }

+++ Added Ua (pretty-v2.1.21.js:312036-312040)
+ function Ua(A) {
+   return A.replace(/[０-９]/g, (K) =>
+     String.fromCharCode(K.charCodeAt(0) - 65248),
+   );
+ }

+++ Added rD7 (pretty-v2.1.21.js:312111-312111)
+ var rD7 = 67108736;

+++ Added sa7 (pretty-v2.1.21.js:387987-387992)
+ var sa7 = C(() => {
+   J7();
+   vL6 = U.object({
+     restrictions: U.record(U.string(), U.object({ allowed: U.boolean() })),
+   });
+ });

+++ Added kX2 (pretty-v2.1.21.js:387996-387998)
+ function kX2(A) {
+   return A instanceof Error;
+ }

+++ Added As7 (pretty-v2.1.21.js:387999-388011)
+ function As7() {
+   if (z3A) return;
+   if (BB())
+     z3A = new Promise((A) => {
+       ((Yd = A),
+         setTimeout(() => {
+           if (Yd)
+             (h("Policy limits: Loading promise timed out, resolving anyway"),
+               Yd(),
+               (Yd = null));
+         }, yX2));
+     });
+ }

+++ Added kL6 (pretty-v2.1.21.js:388018-388027)
+ function kL6(A) {
+   if (Array.isArray(A)) return A.map(kL6);
+   if (A !== null && typeof A === "object") {
+     let K = {};
+     for (let [q, Y] of Object.entries(A).sort(([z], [w]) => z.localeCompare(w)))
+       K[q] = kL6(Y);
+     return K;
+   }
+   return A;
+ }

+++ Added SX2 (pretty-v2.1.21.js:388028-388032)
+ function SX2(A) {
+   let K = kL6(A),
+     q = QA(K);
+   return `sha256:${vX2("sha256").update(q).digest("hex")}`;
+ }

+++ Added BB (pretty-v2.1.21.js:388033-388045)
+ function BB() {
+   if (VK() !== "firstParty") return !1;
+   if (!LJA()) return !1;
+   try {
+     let { key: K } = Y0({ skipRetrievingKeyFromApiKeyHelper: !0 });
+     if (K) return !0;
+   } catch {}
+   let A = EK();
+   if (!A?.accessToken) return !1;
+   if (!A.scopes?.includes(ch)) return !1;
+   if (A.subscriptionType !== "enterprise") return !1;
+   return !0;
+ }

+++ Added CL6 (pretty-v2.1.21.js:388046-388048)
+ async function CL6() {
+   if (z3A) await z3A;
+ }

+++ Added hX2 (pretty-v2.1.21.js:388049-388063)
+ function hX2() {
+   try {
+     let { key: K } = Y0({ skipRetrievingKeyFromApiKeyHelper: !0 });
+     if (K) return { headers: { "x-api-key": K } };
+   } catch {}
+   let A = EK();
+   if (A?.accessToken)
+     return {
+       headers: {
+         Authorization: `Bearer ${A.accessToken}`,
+         "anthropic-beta": EE,
+       },
+     };
+   return { headers: {}, error: "No authentication available" };
+ }

+++ Added bX2 (pretty-v2.1.21.js:388064-388074)
+ async function bX2(A) {
+   let K = null;
+   for (let q = 1; q <= EL6 + 1; q++) {
+     if (((K = await xX2(A)), K.success)) return K;
+     if (K.skipRetry) return K;
+     if (q > EL6) return K;
+     let Y = Ep(q);
+     (h(`Policy limits: Retry ${q}/${EL6} after ${Y}ms`), await Nu(Y));
+   }
+   return K;
+ }

+++ Added xX2 (pretty-v2.1.21.js:388075-388131)
+ async function xX2(A) {
+   try {
+     await iG();
+     let K = hX2();
+     if (K.error)
+       return {
+         success: !1,
+         error: "Authentication required for policy limits",
+         skipRetry: !0,
+       };
+     let q = IX2(),
+       Y = { ...K.headers, "User-Agent": BH() };
+     if (A) Y["If-None-Match"] = `"${A}"`;
+     let z = await t6.get(q, {
+       headers: Y,
+       timeout: LX2,
+       validateStatus: (H) => H === 200 || H === 304 || H === 404,
+     });
+     if (z.status === 304)
+       return (
+         h("Policy limits: Using cached restrictions (304)"),
+         { success: !0, restrictions: null, etag: A }
+       );
+     if (z.status === 404)
+       return (
+         h("Policy limits: No restrictions found (404)"),
+         { success: !0, restrictions: {}, etag: void 0 }
+       );
+     let w = vL6.safeParse(z.data);
+     if (!w.success)
+       return (
+         h(`Policy limits: Invalid response format - ${w.error.message}`),
+         { success: !1, error: "Invalid policy limits format" }
+       );
+     return (
+       h("Policy limits: Fetched successfully"),
+       { success: !0, restrictions: w.data.restrictions }
+     );
+   } catch (K) {
+     if (t6.isAxiosError(K)) {
+       if (K.response?.status === 401 || K.response?.status === 403)
+         return {
+           success: !1,
+           error: "Not authorized for policy limits",
+           skipRetry: !0,
+         };
+       if (K.code === "ECONNABORTED")
+         return { success: !1, error: "Policy limits request timeout" };
+       if (K.code === "ECONNREFUSED" || K.code === "ENOTFOUND")
+         return { success: !1, error: "Cannot connect to server" };
+     }
+     return {
+       success: !1,
+       error: K instanceof Error ? K.message : "Unknown error",
+     };
+   }
+ }

+++ Added Ks7 (pretty-v2.1.21.js:388132-388142)
+ function Ks7() {
+   try {
+     let A = EX2(Bj1(), "utf-8"),
+       K = f3(A, !1),
+       q = vL6.safeParse(K);
+     if (!q.success) return null;
+     return q.data.restrictions;
+   } catch {
+     return null;
+   }
+ }

+++ Added uX2 (pretty-v2.1.21.js:388143-388153)
+ function uX2(A) {
+   try {
+     let K = Bj1();
+     (qf(K, QA({ restrictions: A }, null, 2), { encoding: "utf-8", mode: 384 }),
+       h(`Policy limits: Saved to ${K}`));
+   } catch (K) {
+     h(
+       `Policy limits: Failed to save - ${K instanceof Error ? K.message : "unknown error"}`,
+     );
+   }
+ }

+++ Added LL6 (pretty-v2.1.21.js:388154-388196)
+ async function LL6() {
+   if (!BB()) return null;
+   let A = Ks7(),
+     K = A ? SX2(A) : void 0;
+   try {
+     let q = await bX2(K);
+     if (!q.success) {
+       if (A)
+         return (
+           h("Policy limits: Using stale cache after fetch failure"),
+           (_v = A),
+           A
+         );
+       return null;
+     }
+     if (q.restrictions === null && A)
+       return (
+         h("Policy limits: Cache still valid (304 Not Modified)"),
+         (_v = A),
+         A
+       );
+     let Y = q.restrictions || {};
+     if (Object.keys(Y).length > 0)
+       return (
+         (_v = Y),
+         uX2(Y),
+         h("Policy limits: Applied new restrictions successfully"),
+         Y
+       );
+     _v = Y;
+     try {
+       (ea7(Bj1()), h("Policy limits: Deleted cached file (404 response)"));
+     } catch (w) {
+       if (kX2(w) && w.code !== "ENOENT")
+         h(`Policy limits: Failed to delete cached file - ${w.message}`);
+     }
+     return Y;
+   } catch {
+     if (A)
+       return (h("Policy limits: Using stale cache after error"), (_v = A), A);
+     return null;
+   }
+ }

+++ Added YP (pretty-v2.1.21.js:388197-388203)
+ function YP(A) {
+   let K = BX2();
+   if (!K) return !0;
+   let q = K[A];
+   if (!q) return !0;
+   return q.allowed;
+ }

+++ Added BX2 (pretty-v2.1.21.js:388204-388210)
+ function BX2() {
+   if (!BB()) return null;
+   if (_v) return _v;
+   let A = Ks7();
+   if (A) return ((_v = A), A);
+   return null;
+ }

+++ Added qs7 (pretty-v2.1.21.js:388211-388221)
+ async function qs7() {
+   if (BB() && !z3A)
+     z3A = new Promise((A) => {
+       Yd = A;
+     });
+   try {
+     if ((await LL6(), BB())) gX2();
+   } finally {
+     if (Yd) (Yd(), (Yd = null));
+   }
+ }

+++ Added Ys7 (pretty-v2.1.21.js:388222-388225)
+ async function Ys7() {
+   if ((RL6(), !BB())) return;
+   (await LL6(), h("Policy limits: Refreshed after auth change"));
+ }

+++ Added RL6 (pretty-v2.1.21.js:388226-388231)
+ function RL6() {
+   (zs7(), (_v = null), (z3A = null), (Yd = null));
+   try {
+     ea7(Bj1());
+   } catch {}
+ }

+++ Added mX2 (pretty-v2.1.21.js:388232-388239)
+ async function mX2() {
+   if (!BB()) return;
+   let A = _v ? QA(_v) : null;
+   try {
+     if ((await LL6(), (_v ? QA(_v) : null) !== A))
+       h("Policy limits: Changed during background poll");
+   } catch {}
+ }

+++ Added gX2 (pretty-v2.1.21.js:388240-388250)
+ function gX2() {
+   if (jFA !== null) return;
+   if (!BB()) return;
+   if (
+     ((jFA = setInterval(() => {
+       mX2();
+     }, RX2)),
+     !ta7)
+   )
+     ((ta7 = !0), IK(async () => zs7()));
+ }

+++ Added CX2 (pretty-v2.1.21.js:388254-388254)
+ var CX2 = "policy-limits.json",

+++ Added RKK (pretty-v2.1.21.js:423864-423870)
+ function RKK() {
+   if (XMA)
+     ((mt = XMA), h(`[TeammateModeSnapshot] Captured from CLI override: ${mt}`));
+   else
+     ((mt = D1().teammateMode ?? "auto"),
+       h(`[TeammateModeSnapshot] Captured from config: ${mt}`));
+ }

+++ Added y2K (pretty-v2.1.21.js:447299-447452)
+ var y2K = C(() => {
+   ((rv2 = `Use this tool proactively when you're about to start a non-trivial implementation task. Getting user sign-off on your approach before writing code prevents wasted effort and ensures alignment. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
+    - If you would use ${gJ} to clarify the approach, use EnterPlanMode instead
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
+ 5. Use ${gJ} if you need to clarify approaches
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
+     (ttH = `Use this tool when a task has genuine ambiguity about the right approach and getting user input before coding would prevent significant rework. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
+ When in doubt, prefer starting work and using ${gJ} for specific questions over entering a full planning phase.
+ 
+ ## What Happens in Plan Mode
+ 
+ In plan mode, you'll:
+ 1. Explore the codebase using Glob, Grep, and Read tools
+ 2. Understand existing patterns and architecture
+ 3. Design an implementation approach
+ 4. Present your plan to the user for approval
+ 5. Use ${gJ} if you need to clarify approaches
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

+++ Added cL2 (pretty-v2.1.21.js:460649-460666)
+ async function cL2(A, K, q, Y) {
+   let z = await mL2(A, K, q, Y);
+   if (z !== null) {
+     let J = $JK(Y);
+     return {
+       enabled: z >= J,
+       debugDescription: `${z} tokens (threshold: ${J}, ${Qx6()}% of context)`,
+       metrics: { deferredToolTokens: z, threshold: J },
+     };
+   }
+   let w = await UL2(A, K, q),
+     H = _JK(Y);
+   return {
+     enabled: w >= H,
+     debugDescription: `${w} chars (threshold: ${H}, ${Qx6()}% of context) (char fallback)`,
+     metrics: { deferredToolDescriptionChars: w, charThreshold: H },
+   };
+ }

+++ Added c$K (pretty-v2.1.21.js:478459-479589)
+ function c$K({
+   onClose: A,
+   context: K,
+   setTabsHidden: q,
+   setIsWarning: Y,
+   setHideMargin: z,
+   onSearchModeChange: w,
+ }) {
+   let [H, J] = R4(),
+     [O, X] = _P.useState(D1()),
+     [$, _] = _P.useState(xwK()),
+     Z = K6.useRef(D1()),
+     [G, W] = _P.useState(oq()),
+     D = K6.useRef(oq()),
+     [j, M] = _P.useState(G?.outputStyle || pZ),
+     P = K6.useRef(j),
+     [V, N] = _P.useState(G?.language),
+     T = K6.useRef(V),
+     [E, R] = _P.useState(0),
+     [b, S] = _P.useState(!0),
+     B = _P.useCallback(
+       (VA) => {
+         (S(VA), w?.(VA));
+       },
+       [w],
+     ),
+     x = b,
+     F = vD(),
+     [
+       {
+         mainLoopModel: Q,
+         verbose: u,
+         thinkingEnabled: d,
+         promptSuggestionEnabled: o,
+       },
+       l,
+     ] = V6(),
+     [e, wA] = _P.useState({}),
+     HA = K6.useRef(d),
+     [OA, WA] = _P.useState(!1),
+     [a, _A] = _P.useState(null),
+     {
+       query: jA,
+       setQuery: PA,
+       cursorOffset: SA,
+     } = cS({
+       isActive: x && a === null,
+       onExit: () => {
+         B(!1);
+       },
+     }),
+     mA = m$1(K.options.mcpClients),
+     qA = !j1(process.env.CLAUDE_CODE_DISABLE_FILE_CHECKPOINTING),
+     YA = hY6(),
+     JA = qMA();
+   async function AA(VA) {
+     (n("tengu_config_model_changed", { from_model: Q, to_model: VA }),
+       l((CA) => ({ ...CA, mainLoopModel: VA })),
+       wA((CA) => {
+         let dA = Dy(VA);
+         if ("model" in CA) {
+           let { model: z1, ...oA } = CA;
+           return { ...oA, model: dA };
+         }
+         return { ...CA, model: dA };
+       }));
+   }
+   function t(VA) {
+     (D6((EA) => ({ ...EA, verbose: VA })),
+       X({ ...D1(), verbose: VA }),
+       l((EA) => ({ ...EA, verbose: VA })),
+       wA((EA) => {
+         if ("verbose" in EA) {
+           let { verbose: CA, ...dA } = EA;
+           return dA;
+         }
+         return { ...EA, verbose: VA };
+       }));
+   }
+   let ZA = [
+       {
+         id: "autoCompactEnabled",
+         label: "Auto-compact",
+         value: O.autoCompactEnabled,
+         type: "boolean",
+         onChange(VA) {
+           (D6((EA) => ({ ...EA, autoCompactEnabled: VA })),
+             X({ ...D1(), autoCompactEnabled: VA }),
+             n("tengu_auto_compact_setting_changed", { enabled: VA }));
+         },
+       },
+       {
+         id: "spinnerTipsEnabled",
+         label: "Show tips",
+         value: G?.spinnerTipsEnabled ?? !0,
+         type: "boolean",
+         onChange(VA) {
+           (C4("localSettings", { spinnerTipsEnabled: VA }),
+             W((EA) => ({ ...EA, spinnerTipsEnabled: VA })),
+             n("tengu_tips_setting_changed", { enabled: VA }));
+         },
+       },
+       {
+         id: "thinkingEnabled",
+         label: "Thinking mode",
+         value: d ?? !0,
+         type: "boolean",
+         onChange(VA) {
+           (l((EA) => ({ ...EA, thinkingEnabled: VA })),
+             C4("userSettings", { alwaysThinkingEnabled: VA ? void 0 : !1 }),
+             n("tengu_thinking_toggled", { enabled: VA }));
+         },
+       },
+       {
+         id: "promptSuggestionEnabled",
+         label: "Prompt suggestions",
+         value: o,
+         type: "boolean",
+         onChange(VA) {
+           (l((EA) => ({ ...EA, promptSuggestionEnabled: VA })),
+             C4("userSettings", { promptSuggestionEnabled: VA ? void 0 : !1 }));
+         },
+       },
+       ...[],
+       ...(qA
+         ? [
+             {
+               id: "fileCheckpointingEnabled",
+               label: "Rewind code (checkpoints)",
+               value: O.fileCheckpointingEnabled,
+               type: "boolean",
+               onChange(VA) {
+                 (D6((EA) => ({ ...EA, fileCheckpointingEnabled: VA })),
+                   X({ ...D1(), fileCheckpointingEnabled: VA }),
+                   n("tengu_file_history_snapshots_setting_changed", {
+                     enabled: VA,
+                   }));
+               },
+             },
+           ]
+         : []),
+       {
+         id: "verbose",
+         label: "Verbose output",
+         value: u,
+         type: "boolean",
+         onChange: t,
+       },
+       {
+         id: "terminalProgressBarEnabled",
+         label: "Terminal progress bar",
+         value: O.terminalProgressBarEnabled,
+         type: "boolean",
+         onChange(VA) {
+           (D6((EA) => ({ ...EA, terminalProgressBarEnabled: VA })),
+             X({ ...D1(), terminalProgressBarEnabled: VA }),
+             n("tengu_terminal_progress_bar_setting_changed", { enabled: VA }));
+         },
+       },
+       {
+         id: "defaultPermissionMode",
+         label: "Default permission mode",
+         value: G?.permissions?.defaultMode || "default",
+         options: (() => {
+           let VA = ["default", "plan"],
+             EA = D8()
+               ? ["bypassPermissions"]
+               : ["bypassPermissions", "delegate"];
+           return [
+             ...VA,
+             ...Z6A.filter((CA) => !VA.includes(CA) && !EA.includes(CA)),
+           ];
+         })(),
+         type: "enum",
+         onChange(VA) {
+           let EA = OF(yR(VA)),
+             CA = C4("userSettings", {
+               permissions: { ...G?.permissions, defaultMode: EA },
+             });
+           if (CA.error) {
+             KA(CA.error);
+             return;
+           }
+           (W((dA) => ({
+             ...dA,
+             permissions: { ...dA?.permissions, defaultMode: EA },
+           })),
+             wA((dA) => ({ ...dA, defaultPermissionMode: VA })),
+             n("tengu_config_changed", {
+               setting: "defaultPermissionMode",
+               value: VA,
+             }));
+         },
+       },
+       {
+         id: "respectGitignore",
+         label: "Respect .gitignore in file picker",
+         value: O.respectGitignore,
+         type: "boolean",
+         onChange(VA) {
+           (D6((EA) => ({ ...EA, respectGitignore: VA })),
+             X({ ...D1(), respectGitignore: VA }),
+             n("tengu_respect_gitignore_setting_changed", { enabled: VA }));
+         },
+       },
+       JA
+         ? {
+             id: "autoUpdatesChannel",
+             label: "Auto-update channel",
+             value: "disabled",
+             type: "managedEnum",
+             onChange() {},
+           }
+         : {
+             id: "autoUpdatesChannel",
+             label: "Auto-update channel",
+             value: G?.autoUpdatesChannel ?? "latest",
+             type: "managedEnum",
+             onChange() {},
+           },
+       {
+         id: "theme",
+         label: "Theme",
+         value: H,
+         type: "managedEnum",
+         onChange: J,
+       },
+       {
+         id: "notifChannel",
+         label: "Notifications",
+         value: O.preferredNotifChannel,
+         options: [
+           "auto",
+           "iterm2",
+           "terminal_bell",
+           "iterm2_with_bell",
+           "kitty",
+           "ghostty",
+           "notifications_disabled",
+         ],
+         type: "enum",
+         onChange(VA) {
+           (D6((EA) => ({ ...EA, preferredNotifChannel: VA })),
+             X({ ...D1(), preferredNotifChannel: VA }));
+         },
+       },
+       {
+         id: "outputStyle",
+         label: "Output style",
+         value: j,
+         type: "managedEnum",
+         onChange: () => {},
+       },
+       {
+         id: "language",
+         label: "Language",
+         value: V ?? "Default (English)",
+         type: "managedEnum",
+         onChange: () => {},
+       },
+       {
+         id: "editorMode",
+         label: "Editor mode",
+         value: O.editorMode === "emacs" ? "normal" : O.editorMode || "normal",
+         options: ["normal", "vim"],
+         type: "enum",
+         onChange(VA) {
+           (D6((EA) => ({ ...EA, editorMode: VA })),
+             X({ ...D1(), editorMode: VA }),
+             n("tengu_editor_mode_changed", {
+               mode: VA,
+               source: "config_panel",
+             }));
+         },
+       },
+       ...[],
+       ...(V4("tengu_code_diff_cli", !1)
+         ? [
+             {
+               id: "codeDiffFooterEnabled",
+               label: "Show code diff footer",
+               value: O.codeDiffFooterEnabled ?? !0,
+               type: "boolean",
+               onChange(VA) {
+                 (D6((EA) => {
+                   if (EA.codeDiffFooterEnabled === VA) return EA;
+                   return { ...EA, codeDiffFooterEnabled: VA };
+                 }),
+                   X({ ...D1(), codeDiffFooterEnabled: VA }),
+                   n("tengu_code_diff_footer_setting_changed", { enabled: VA }));
+               },
+             },
+           ]
+         : []),
+       ...(V4("tengu_pr_status_cli", !1)
+         ? [
+             {
+               id: "prStatusFooterEnabled",
+               label: "Show PR status footer",
+               value: O.prStatusFooterEnabled ?? !0,
+               type: "boolean",
+               onChange(VA) {
+                 (D6((EA) => {
+                   if (EA.prStatusFooterEnabled === VA) return EA;
+                   return { ...EA, prStatusFooterEnabled: VA };
+                 }),
+                   X({ ...D1(), prStatusFooterEnabled: VA }),
+                   n("tengu_pr_status_footer_setting_changed", { enabled: VA }));
+               },
+             },
+           ]
+         : []),
+       {
+         id: "model",
+         label: "Model",
+         value: Q === null ? "Default (recommended)" : Q,
+         type: "managedEnum",
+         onChange: AA,
+       },
+       ...(mA
+         ? [
+             {
+               id: "diffTool",
+               label: "Diff tool",
+               value: O.diffTool ?? "auto",
+               options: ["terminal", "auto"],
+               type: "enum",
+               onChange(VA) {
+                 (D6((EA) => ({ ...EA, diffTool: VA })),
+                   X({ ...D1(), diffTool: VA }),
+                   n("tengu_diff_tool_changed", {
+                     tool: VA,
+                     source: "config_panel",
+                   }));
+               },
+             },
+           ]
+         : []),
+       ...(!W$()
+         ? [
+             {
+               id: "autoConnectIde",
+               label: "Auto-connect to IDE (external terminal)",
+               value: O.autoConnectIde ?? !1,
+               type: "boolean",
+               onChange(VA) {
+                 (D6((EA) => ({ ...EA, autoConnectIde: VA })),
+                   X({ ...D1(), autoConnectIde: VA }),
+                   n("tengu_auto_connect_ide_changed", {
+                     enabled: VA,
+                     source: "config_panel",
+                   }));
+               },
+             },
+           ]
+         : []),
+       ...(W$()
+         ? [
+             {
+               id: "autoInstallIdeExtension",
+               label: "Auto-install IDE extension",
+               value: O.autoInstallIdeExtension ?? !0,
+               type: "boolean",
+               onChange(VA) {
+                 (D6((EA) => ({ ...EA, autoInstallIdeExtension: VA })),
+                   X({ ...D1(), autoInstallIdeExtension: VA }),
+                   n("tengu_auto_install_ide_extension_changed", {
+                     enabled: VA,
+                     source: "config_panel",
+                   }));
+               },
+             },
+           ]
+         : []),
+       {
+         id: "claudeInChromeDefaultEnabled",
+         label: "Claude in Chrome enabled by default",
+         value: O.claudeInChromeDefaultEnabled ?? !0,
+         type: "boolean",
+         onChange(VA) {
+           (D6((EA) => ({ ...EA, claudeInChromeDefaultEnabled: VA })),
+             X({ ...D1(), claudeInChromeDefaultEnabled: VA }),
+             n("tengu_claude_in_chrome_setting_changed", { enabled: VA }));
+         },
+       },
+       ...(D8()
+         ? (() => {
+             let VA = dI6();
+             return [
+               {
+                 id: "teammateMode",
+                 label: VA
+                   ? `Teammate mode [overridden: ${VA}]`
+                   : "Teammate mode",
+                 value: O.teammateMode ?? "auto",
+                 options: ["auto", "tmux", "in-process"],
+                 type: "enum",
+                 onChange(CA) {
+                   if (CA !== "auto" && CA !== "tmux" && CA !== "in-process")
+                     return;
+                   (cI6(CA),
+                     D6((dA) => ({ ...dA, teammateMode: CA })),
+                     X({ ...D1(), teammateMode: CA }),
+                     n("tengu_teammate_mode_changed", { mode: CA }));
+                 },
+               },
+             ];
+           })()
+         : []),
+       ...(YA
+         ? [
+             {
+               id: "showExternalIncludesDialog",
+               label: "External CLAUDE.md includes",
+               value: (() => {
+                 if (M2().hasClaudeMdExternalIncludesApproved) return "true";
+                 else return "false";
+               })(),
+               type: "managedEnum",
+               onChange() {},
+             },
+           ]
+         : []),
+       ...(process.env.ANTHROPIC_API_KEY
+         ? [
+             {
+               id: "apiKey",
+               label: K6.createElement(
+                 f,
+                 null,
+                 "Use custom API key:",
+                 " ",
+                 K6.createElement(
+                   f,
+                   { bold: !0 },
+                   Bv(process.env.ANTHROPIC_API_KEY),
+                 ),
+               ),
+               searchText: "Use custom API key",
+               value: Boolean(
+                 process.env.ANTHROPIC_API_KEY &&
+                   O.customApiKeyResponses?.approved?.includes(
+                     Bv(process.env.ANTHROPIC_API_KEY),
+                   ),
+               ),
+               type: "boolean",
+               onChange(VA) {
+                 (D6((EA) => {
+                   let CA = { ...EA };
+                   if (!CA.customApiKeyResponses)
+                     CA.customApiKeyResponses = { approved: [], rejected: [] };
+                   if (!CA.customApiKeyResponses.approved)
+                     CA.customApiKeyResponses = {
+                       ...CA.customApiKeyResponses,
+                       approved: [],
+                     };
+                   if (!CA.customApiKeyResponses.rejected)
+                     CA.customApiKeyResponses = {
+                       ...CA.customApiKeyResponses,
+                       rejected: [],
+                     };
+                   if (process.env.ANTHROPIC_API_KEY) {
+                     let dA = Bv(process.env.ANTHROPIC_API_KEY);
+                     if (VA)
+                       CA.customApiKeyResponses = {
+                         ...CA.customApiKeyResponses,
+                         approved: [
+                           ...(CA.customApiKeyResponses.approved ?? []).filter(
+                             (z1) => z1 !== dA,
+                           ),
+                           dA,
+                         ],
+                         rejected: (
+                           CA.customApiKeyResponses.rejected ?? []
+                         ).filter((z1) => z1 !== dA),
+                       };
+                     else
+                       CA.customApiKeyResponses = {
+                         ...CA.customApiKeyResponses,
+                         approved: (
+                           CA.customApiKeyResponses.approved ?? []
+                         ).filter((z1) => z1 !== dA),
+                         rejected: [
+                           ...(CA.customApiKeyResponses.rejected ?? []).filter(
+                             (z1) => z1 !== dA,
+                           ),
+                           dA,
+                         ],
+                       };
+                   }
+                   return CA;
+                 }),
+                   X(D1()));
+               },
+             },
+           ]
+         : []),
+     ],
+     kA = K6.useMemo(() => {
+       if (!jA) return ZA;
+       let VA = jA.toLowerCase();
+       return ZA.filter((EA) => {
+         if (EA.id.toLowerCase().includes(VA)) return !0;
+         return ("searchText" in EA ? EA.searchText : EA.label)
+           .toLowerCase()
+           .includes(VA);
+       });
+     }, [ZA, jA]);
+   K6.useEffect(() => {
+     if (E >= kA.length) R(Math.max(0, kA.length - 1));
+   }, [kA.length, E]);
+   let XA = _P.useCallback(() => {
+     if (a !== null) return;
+     let VA = Object.entries(e).map(([dA, z1]) => {
+         return (
+           n("tengu_config_changed", { key: dA, value: z1 }),
+           `Set ${dA} to ${O1.bold(z1)}`
+         );
+       }),
+       EA = Boolean(
+         process.env.ANTHROPIC_API_KEY &&
+           Z.current.customApiKeyResponses?.approved?.includes(
+             Bv(process.env.ANTHROPIC_API_KEY),
+           ),
+       ),
+       CA = Boolean(
+         process.env.ANTHROPIC_API_KEY &&
+           O.customApiKeyResponses?.approved?.includes(
+             Bv(process.env.ANTHROPIC_API_KEY),
+           ),
+       );
+     if (EA !== CA)
+       (VA.push(`${CA ? "Enabled" : "Disabled"} custom API key`),
+         n("tengu_config_changed", { key: "env.ANTHROPIC_API_KEY", value: CA }));
+     if (O.theme !== Z.current.theme)
+       VA.push(`Set theme to ${O1.bold(O.theme)}`);
+     if (O.preferredNotifChannel !== Z.current.preferredNotifChannel)
+       VA.push(`Set notifications to ${O1.bold(O.preferredNotifChannel)}`);
+     if (j !== P.current) VA.push(`Set output style to ${O1.bold(j)}`);
+     if (V !== T.current)
+       VA.push(`Set response language to ${O1.bold(V ?? "Default (English)")}`);
+     if (O.editorMode !== Z.current.editorMode)
+       VA.push(`Set editor mode to ${O1.bold(O.editorMode || "emacs")}`);
+     if (O.diffTool !== Z.current.diffTool)
+       VA.push(`Set diff tool to ${O1.bold(O.diffTool)}`);
+     if (O.autoConnectIde !== Z.current.autoConnectIde)
+       VA.push(
+         `${O.autoConnectIde ? "Enabled" : "Disabled"} auto-connect to IDE`,
+       );
+     if (O.autoInstallIdeExtension !== Z.current.autoInstallIdeExtension)
+       VA.push(
+         `${O.autoInstallIdeExtension ? "Enabled" : "Disabled"} auto-install IDE extension`,
+       );
+     if (O.autoCompactEnabled !== Z.current.autoCompactEnabled)
+       VA.push(`${O.autoCompactEnabled ? "Enabled" : "Disabled"} auto-compact`);
+     if (O.respectGitignore !== Z.current.respectGitignore)
+       VA.push(
+         `${O.respectGitignore ? "Enabled" : "Disabled"} respect .gitignore in file picker`,
+       );
+     if (O.terminalProgressBarEnabled !== Z.current.terminalProgressBarEnabled)
+       VA.push(
+         `${O.terminalProgressBarEnabled ? "Enabled" : "Disabled"} terminal progress bar`,
+       );
+     if (G?.autoUpdatesChannel !== D.current?.autoUpdatesChannel)
+       VA.push(
+         `Set auto-update channel to ${O1.bold(G?.autoUpdatesChannel ?? "latest")}`,
+       );
+     if (VA.length > 0)
+       A(
+         VA.join(`
+ `),
+       );
+     else A("Config dialog dismissed", { display: "system" });
+   }, [a, e, O, j, V, G?.autoUpdatesChannel, A]);
+   A6("confirm:no", XA, { context: "Settings", isActive: a === null });
+   let LA = _P.useCallback(() => {
+     let VA = kA[E];
+     if (!VA || !VA.onChange) return;
+     if (VA.type === "boolean") {
+       if ((VA.onChange(!VA.value), VA.id === "thinkingEnabled")) {
+         if (!VA.value === HA.current) WA(!1);
+         else if (K.messages.some((dA) => dA.type === "assistant")) WA(!0);
+       }
+       return;
+     }
+     if (
+       VA.id === "theme" ||
+       VA.id === "model" ||
+       VA.id === "showExternalIncludesDialog" ||
+       VA.id === "outputStyle" ||
+       VA.id === "language"
+     )
+       switch (VA.id) {
+         case "theme":
+           (_A(0), q(!0), z(!0));
+           return;
+         case "model":
+           (_A(1), q(!0));
+           return;
+         case "showExternalIncludesDialog":
+           (_A(2), q(!0), Y(!0));
+           return;
+         case "outputStyle":
+           (_A(3), q(!0));
+           return;
+         case "language":
+           (_A(5), q(!0));
+           return;
+       }
+     if (VA.id === "autoUpdatesChannel") {
+       if ((G?.autoUpdatesChannel ?? "latest") === "latest") (_A(4), q(!0));
+       else
+         (C4("userSettings", {
+           autoUpdatesChannel: "latest",
+           minimumVersion: void 0,
+         }),
+           W((CA) => ({
+             ...CA,
+             autoUpdatesChannel: "latest",
+             minimumVersion: void 0,
+           })),
+           n("tengu_autoupdate_channel_changed", { channel: "latest" }));
+       return;
+     }
+     if (VA.type === "enum") {
+       let CA = (VA.options.indexOf(VA.value) + 1) % VA.options.length;
+       VA.onChange(VA.options[CA]);
+       return;
+     }
+   }, [kA, E, G?.autoUpdatesChannel, q, z, Y]);
+   return (
+     O7(
+       {
+         "select:previous": () => {
+           if ((WA(!1), E === 0)) B(!0);
+           else R((VA) => Math.max(0, VA - 1));
+         },
+         "select:next": () => {
+           (WA(!1), R((VA) => Math.min(kA.length - 1, VA + 1)));
+         },
+         "select:accept": LA,
+         "settings:search": () => {
+           (B(!0), PA(""));
+         },
+       },
+       { context: "Settings", isActive: a === null && !x },
+     ),
+     e6(
+       (VA, EA) => {
+         if (EA.escape) {
+           if (jA.length > 0) PA("");
+           else B(!1);
+           return;
+         }
+         if (EA.return || EA.downArrow) (B(!1), R(0));
+       },
+       { isActive: x && a === null },
+     ),
+     e6(
+       (VA, EA) => {
+         if (!EA.ctrl && !EA.meta && VA.length > 0 && !/^\s+$/.test(VA))
+           (B(!0), PA(VA));
+       },
+       { isActive: !x && a === null },
+     ),
+     K6.createElement(
+       I,
+       { flexDirection: "column", width: "100%" },
+       a === 0
+         ? K6.createElement(
+             K6.Fragment,
+             null,
+             K6.createElement(TPA, {
+               initialTheme: H,
+               onThemeSelect: (VA) => {
+                 (J(VA), _A(null), z(!1), q(!1));
+               },
+               onCancel: () => {
+                 (_A(null), z(!1), q(!1));
+               },
+               hideEscToCancel: !0,
+               skipExitHandling: !0,
+             }),
+             K6.createElement(
+               I,
+               { marginLeft: 1 },
+               K6.createElement(
+                 f,
+                 { dimColor: !0, italic: !0 },
+                 K6.createElement(
+                   w8,
+                   null,
+                   K6.createElement(G6, { shortcut: "Enter", action: "select" }),
+                   K6.createElement(U6, {
+                     action: "confirm:no",
+                     context: "Confirmation",
+                     fallback: "Esc",
+                     description: "cancel",
+                   }),
+                 ),
+               ),
+             ),
+           )
+         : a === 1
+           ? K6.createElement(
+               K6.Fragment,
+               null,
+               K6.createElement(vPA, {
+                 initial: Q,
+                 onSelect: (VA, EA) => {
+                   (AA(VA), _A(null), q(!1));
+                 },
+                 onCancel: () => {
+                   (_A(null), q(!1));
+                 },
+               }),
+               K6.createElement(
+                 f,
+                 { dimColor: !0 },
+                 K6.createElement(
+                   w8,
+                   null,
+                   K6.createElement(G6, {
+                     shortcut: "Enter",
+                     action: "confirm",
+                   }),
+                   K6.createElement(U6, {
+                     action: "confirm:no",
+                     context: "Confirmation",
+                     fallback: "Esc",
+                     description: "cancel",
+                   }),
+                 ),
+               ),
+             )
+           : a === 2
+             ? K6.createElement(
+                 K6.Fragment,
+                 null,
+                 K6.createElement($T1, {
+                   onDone: () => {
+                     (_A(null), q(!1), Y(!1));
+                   },
+                   externalIncludes: GSA(),
+                 }),
+                 K6.createElement(
+                   f,
+                   { dimColor: !0 },
+                   K6.createElement(
+                     w8,
+                     null,
+                     K6.createElement(G6, {
+                       shortcut: "Enter",
+                       action: "confirm",
+                     }),
+                     K6.createElement(U6, {
+                       action: "confirm:no",
+                       context: "Confirmation",
+                       fallback: "Esc",
+                       description: "disable external includes",
+                     }),
+                   ),
+                 ),
+               )
+             : a === 3
+               ? K6.createElement(
+                   K6.Fragment,
+                   null,
+                   K6.createElement(_T1, {
+                     initialStyle: j,
+                     onComplete: (VA) => {
+                       (M(VA ?? pZ),
+                         _A(null),
+                         q(!1),
+                         C4("localSettings", { outputStyle: VA }),
+                         n("tengu_output_style_changed", {
+                           style: VA ?? pZ,
+                           source: "config_panel",
+                           settings_source: "localSettings",
+                         }));
+                     },
+                     onCancel: () => {
+                       (_A(null), q(!1));
+                     },
+                   }),
+                   K6.createElement(
+                     f,
+                     { dimColor: !0 },
+                     K6.createElement(
+                       w8,
+                       null,
+                       K6.createElement(G6, {
+                         shortcut: "Enter",
+                         action: "confirm",
+                       }),
+                       K6.createElement(U6, {
+                         action: "confirm:no",
+                         context: "Confirmation",
+                         fallback: "Esc",
+                         description: "cancel",
+                       }),
+                     ),
+                   ),
+                 )
+               : a === 5
+                 ? K6.createElement(
+                     K6.Fragment,
+                     null,
+                     K6.createElement(p$K, {
+                       initialLanguage: V,
+                       onComplete: (VA) => {
+                         (N(VA),
+                           _A(null),
+                           q(!1),
+                           C4("userSettings", { language: VA }),
+                           n("tengu_language_changed", {
+                             language: VA ?? "default",
+                             source: "config_panel",
+                           }));
+                       },
+                       onCancel: () => {
+                         (_A(null), q(!1));
+                       },
+                     }),
+                     K6.createElement(
+                       f,
+                       { dimColor: !0 },
+                       K6.createElement(
+                         w8,
+                         null,
+                         K6.createElement(G6, {
+                           shortcut: "Enter",
+                           action: "confirm",
+                         }),
+                         K6.createElement(U6, {
+                           action: "confirm:no",
+                           context: "Settings",
+                           fallback: "Esc",
+                           description: "cancel",
+                         }),
+                       ),
+                     ),
+                   )
+                 : a === 4
+                   ? K6.createElement(F$K, {
+                       currentVersion: {
+                         ISSUES_EXPLAINER:
+                           "report the issue at https://github.com/anthropics/claude-code/issues",
+                         PACKAGE_URL: "@anthropic-ai/claude-code",
+                         README_URL: "https://code.claude.com/docs/en/overview",
+                         VERSION: "2.1.21",
+                         FEEDBACK_CHANNEL:
+                           "https://github.com/anthropics/claude-code/issues",
+                         BUILD_TIME: "2026-01-28T01:36:50Z",
+                       }.VERSION,
+                       onChoice: (VA) => {
+                         if ((_A(null), q(!1), VA === "cancel")) return;
+                         let EA = { autoUpdatesChannel: "stable" };
+                         if (VA === "stay")
+                           EA.minimumVersion = {
+                             ISSUES_EXPLAINER:
+                               "report the issue at https://github.com/anthropics/claude-code/issues",
+                             PACKAGE_URL: "@anthropic-ai/claude-code",
+                             README_URL:
+                               "https://code.claude.com/docs/en/overview",
+                             VERSION: "2.1.21",
+                             FEEDBACK_CHANNEL:
+                               "https://github.com/anthropics/claude-code/issues",
+                             BUILD_TIME: "2026-01-28T01:36:50Z",
+                           }.VERSION;
+                         (C4("userSettings", EA),
+                           W((CA) => ({ ...CA, ...EA })),
+                           n("tengu_autoupdate_channel_changed", {
+                             channel: "stable",
+                             minimum_version_set: VA === "stay",
+                           }));
+                       },
+                     })
+                   : K6.createElement(
+                       I,
+                       { flexDirection: "column", marginY: 1, gap: 1 },
+                       K6.createElement(
+                         f,
+                         null,
+                         "Configure Claude Code preferences",
+                       ),
+                       K6.createElement(dS, {
+                         query: jA,
+                         isFocused: x,
+                         isTerminalFocused: F,
+                         cursorOffset: SA,
+                         placeholder: "Search settings...",
+                       }),
+                       K6.createElement(
+                         I,
+                         { flexDirection: "column" },
+                         kA.length === 0
+                           ? K6.createElement(
+                               f,
+                               { dimColor: !0, italic: !0 },
+                               'No settings match "',
+                               jA,
+                               '"',
+                             )
+                           : kA.map((VA, EA) => {
+                               let CA = EA === E;
+                               return K6.createElement(
+                                 K6.Fragment,
+                                 { key: VA.id },
+                                 K6.createElement(
+                                   I,
+                                   null,
+                                   K6.createElement(
+                                     I,
+                                     { width: 44 },
+                                     K6.createElement(
+                                       f,
+                                       { color: CA ? "suggestion" : void 0 },
+                                       CA ? q1.pointer : " ",
+                                       " ",
+                                       VA.label,
+                                     ),
+                                   ),
+                                   K6.createElement(
+                                     I,
+                                     { key: CA ? "selected" : "unselected" },
+                                     VA.type === "boolean"
+                                       ? K6.createElement(
+                                           K6.Fragment,
+                                           null,
+                                           K6.createElement(
+                                             f,
+                                             {
+                                               color: CA ? "suggestion" : void 0,
+                                             },
+                                             VA.value.toString(),
+                                           ),
+                                           OA &&
+                                             VA.id === "thinkingEnabled" &&
+                                             K6.createElement(
+                                               f,
+                                               { color: "warning" },
+                                               " ",
+                                               "Changing thinking mode mid-conversation will increase latency and may reduce quality.",
+                                             ),
+                                         )
+                                       : VA.id === "theme"
+                                         ? K6.createElement(
+                                             f,
+                                             {
+                                               color: CA ? "suggestion" : void 0,
+                                             },
+                                             (() => {
+                                               return (
+                                                 {
+                                                   dark: "Dark mode",
+                                                   light: "Light mode",
+                                                   "dark-daltonized":
+                                                     "Dark mode (colorblind-friendly)",
+                                                   "light-daltonized":
+                                                     "Light mode (colorblind-friendly)",
+                                                   "dark-ansi":
+                                                     "Dark mode (ANSI colors only)",
+                                                   "light-ansi":
+                                                     "Light mode (ANSI colors only)",
+                                                 }[VA.value.toString()] ||
+                                                 VA.value.toString()
+                                               );
+                                             })(),
+                                           )
+                                         : VA.id === "notifChannel"
+                                           ? K6.createElement(
+                                               f,
+                                               {
+                                                 color: CA
+                                                   ? "suggestion"
+                                                   : void 0,
+                                               },
+                                               (() => {
+                                                 switch (VA.value.toString()) {
+                                                   case "auto":
+                                                     return "Auto";
+                                                   case "iterm2":
+                                                     return K6.createElement(
+                                                       K6.Fragment,
+                                                       null,
+                                                       "iTerm2 ",
+                                                       K6.createElement(
+                                                         f,
+                                                         { dimColor: !0 },
+                                                         "(OSC 9)",
+                                                       ),
+                                                     );
+                                                   case "terminal_bell":
+                                                     return K6.createElement(
+                                                       K6.Fragment,
+                                                       null,
+                                                       "Terminal Bell ",
+                                                       K6.createElement(
+                                                         f,
+                                                         { dimColor: !0 },
+                                                         "(\\a)",
+                                                       ),
+                                                     );
+                                                   case "kitty":
+                                                     return K6.createElement(
+                                                       K6.Fragment,
+                                                       null,
+                                                       "Kitty ",
+                                                       K6.createElement(
+                                                         f,
+                                                         { dimColor: !0 },
+                                                         "(OSC 99)",
+                                                       ),
+                                                     );
+                                                   case "ghostty":
+                                                     return K6.createElement(
+                                                       K6.Fragment,
+                                                       null,
+                                                       "Ghostty ",
+                                                       K6.createElement(
+                                                         f,
+                                                         { dimColor: !0 },
+                                                         "(OSC 777)",
+                                                       ),
+                                                     );
+                                                   case "iterm2_with_bell":
+                                                     return "iTerm2 w/ Bell";
+                                                   case "notifications_disabled":
+                                                     return "Disabled";
+                                                   default:
+                                                     return VA.value.toString();
+                                                 }
+                                               })(),
+                                             )
+                                           : VA.id === "defaultPermissionMode"
+                                             ? K6.createElement(
+                                                 f,
+                                                 {
+                                                   color: CA
+                                                     ? "suggestion"
+                                                     : void 0,
+                                                 },
+                                                 XF(VA.value),
+                                               )
+                                             : VA.id === "autoUpdatesChannel" &&
+                                                 JA
+                                               ? K6.createElement(
+                                                   I,
+                                                   { flexDirection: "column" },
+                                                   K6.createElement(
+                                                     f,
+                                                     {
+                                                       color: CA
+                                                         ? "suggestion"
+                                                         : void 0,
+                                                     },
+                                                     "disabled",
+                                                   ),
+                                                   K6.createElement(
+                                                     f,
+                                                     { dimColor: !0 },
+                                                     "(",
+                                                     JA,
+                                                     ")",
+                                                   ),
+                                                 )
+                                               : K6.createElement(
+                                                   f,
+                                                   {
+                                                     color: CA
+                                                       ? "suggestion"
+                                                       : void 0,
+                                                   },
+                                                   VA.value.toString(),
+                                                 ),
+                                   ),
+                                 ),
+                               );
+                             }),
+                       ),
+                       x
+                         ? K6.createElement(
+                             f,
+                             { dimColor: !0 },
+                             K6.createElement(
+                               w8,
+                               null,
+                               K6.createElement(f, null, "Type to filter"),
+                               K6.createElement(G6, {
+                                 shortcut: "Enter/↓",
+                                 action: "select",
+                               }),
+                               K6.createElement(U6, {
+                                 action: "confirm:no",
+                                 context: "Settings",
+                                 fallback: "Esc",
+                                 description: "clear",
+                               }),
+                             ),
+                           )
+                         : K6.createElement(
+                             f,
+                             { dimColor: !0 },
+                             K6.createElement(
+                               w8,
+                               null,
+                               K6.createElement(U6, {
+                                 action: "select:accept",
+                                 context: "Settings",
+                                 fallback: "Enter/Space",
+                                 description: "change",
+                               }),
+                               K6.createElement(U6, {
+                                 action: "settings:search",
+                                 context: "Settings",
+                                 fallback: "/",
+                                 description: "search",
+                               }),
+                               K6.createElement(U6, {
+                                 action: "confirm:no",
+                                 context: "Settings",
+                                 fallback: "Esc",
+                                 description: "cancel",
+                               }),
+                             ),
+                           ),
+                     ),
+     )
+   );
+ }

+++ Added YZK (pretty-v2.1.21.js:484125-484188)
+ function YZK(A) {
+   let K = s(9),
+     { onComplete: q } = A,
+     Y;
+   if (K[0] !== q)
+     ((Y = async ($) => {
+       let _ = $ === "yes";
+       (D6((Z) => ({
+         ...Z,
+         autoConnectIde: _,
+         hasIdeAutoConnectDialogBeenShown: !0,
+       })),
+         q());
+     }),
+       (K[0] = q),
+       (K[1] = Y));
+   else Y = K[1];
+   let z = Y,
+     w;
+   if (K[2] === Symbol.for("react.memo_cache_sentinel"))
+     ((w = [
+       { label: "Yes", value: "yes" },
+       { label: "No", value: "no" },
+     ]),
+       (K[2] = w));
+   else w = K[2];
+   let H = w,
+     J;
+   if (K[3] !== z)
+     ((J = k9A.default.createElement(k6, {
+       options: H,
+       onChange: z,
+       defaultValue: "yes",
+     })),
+       (K[3] = z),
+       (K[4] = J));
+   else J = K[4];
+   let O;
+   if (K[5] === Symbol.for("react.memo_cache_sentinel"))
+     ((O = k9A.default.createElement(
+       f,
+       { dimColor: !0 },
+       "You can also configure this in /config or with the --ide flag",
+     )),
+       (K[5] = O));
+   else O = K[5];
+   let X;
+   if (K[6] !== q || K[7] !== J)
+     ((X = k9A.default.createElement(
+       y4,
+       {
+         title: "Do you wish to enable auto-connect to IDE?",
+         color: "ide",
+         onCancel: q,
+       },
+       J,
+       O,
+     )),
+       (K[6] = q),
+       (K[7] = J),
+       (K[8] = X));
+   else X = K[8];
+   return X;
+ }

+++ Added qMK (pretty-v2.1.21.js:503331-503382)
+ function qMK() {
+   let { columns: A } = M8(),
+     [K] = V6(),
+     [q, { isVisible: Y }] = D4A(),
+     z = Xv1(),
+     w = Dv1.useRef(z);
+   if (Y) w.current = z;
+   let {
+       version: H,
+       cwd: J,
+       modelDisplayName: O,
+       billingType: X,
+       agentName: $,
+     } = w.current,
+     _ = K.agent ?? $,
+     Z = Gv1();
+   Dv1.useEffect(() => {
+     if (Z) Wv1();
+   }, [Z]);
+   let G = Math.max(A - 15, 20),
+     D = a9(H, Math.max(G - "Claude Code v".length, 6)),
+     { shouldSplit: j, truncatedModel: M, truncatedBilling: P } = mjK(O, X, G),
+     V = " · ",
+     T = _ ? G - 1 - _.length - V.length : G,
+     E = WdA(J, Math.max(T, 10));
+   return KK.createElement(
+     I,
+     { ref: q, flexDirection: "row", gap: 2, alignItems: "center" },
+     KK.createElement(qp2, null),
+     KK.createElement(
+       I,
+       { flexDirection: "column" },
+       KK.createElement(
+         f,
+         null,
+         KK.createElement(f, { bold: !0 }, "Claude Code"),
+         " ",
+         KK.createElement(f, { dimColor: !0 }, "v", D),
+       ),
+       j
+         ? KK.createElement(
+             KK.Fragment,
+             null,
+             KK.createElement(f, { dimColor: !0 }, M),
+             KK.createElement(f, { dimColor: !0 }, P),
+           )
+         : KK.createElement(f, { dimColor: !0 }, M, " · ", P),
+       KK.createElement(f, { dimColor: !0 }, _ ? `@${_} · ${E}` : E),
+       Z && KK.createElement(KMK, null),
+     ),
+   );
+ }

+++ Added wMK (pretty-v2.1.21.js:503439-503782)
+ function wMK({ isBeforeFirstMessage: A }) {
+   let K = RjK(A),
+     q = BjK(),
+     Y = D1().oauthAccount?.displayName ?? "",
+     { columns: z } = M8(),
+     w = qZ4(),
+     H = I8.isSandboxingEnabled(),
+     J = Gv1(),
+     O = tM(),
+     [X] = V6(),
+     $ = D1(),
+     _;
+   try {
+     _ = gjK(3);
+   } catch {
+     _ = [];
+   }
+   let Z = O.companyAnnouncements,
+     [G] = Q9A.useState(() =>
+       Z && Z.length > 0
+         ? $.numStartups === 1
+           ? Z[0]
+           : Z[Math.floor(Math.random() * Z.length)]
+         : void 0,
+     ),
+     { hasReleaseNotes: W } = XdA($.lastReleaseNotesSeen);
+   (Q9A.useEffect(() => {
+     if (
+       D1().lastReleaseNotesSeen ===
+       {
+         ISSUES_EXPLAINER:
+           "report the issue at https://github.com/anthropics/claude-code/issues",
+         PACKAGE_URL: "@anthropic-ai/claude-code",
+         README_URL: "https://code.claude.com/docs/en/overview",
+         VERSION: "2.1.21",
+         FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
+         BUILD_TIME: "2026-01-28T01:36:50Z",
+       }.VERSION
+     )
+       return;
+     if (
+       (D6((jA) => {
+         if (
+           jA.lastReleaseNotesSeen ===
+           {
+             ISSUES_EXPLAINER:
+               "report the issue at https://github.com/anthropics/claude-code/issues",
+             PACKAGE_URL: "@anthropic-ai/claude-code",
+             README_URL: "https://code.claude.com/docs/en/overview",
+             VERSION: "2.1.21",
+             FEEDBACK_CHANNEL:
+               "https://github.com/anthropics/claude-code/issues",
+             BUILD_TIME: "2026-01-28T01:36:50Z",
+           }.VERSION
+         )
+           return jA;
+         return {
+           ...jA,
+           lastReleaseNotesSeen: {
+             ISSUES_EXPLAINER:
+               "report the issue at https://github.com/anthropics/claude-code/issues",
+             PACKAGE_URL: "@anthropic-ai/claude-code",
+             README_URL: "https://code.claude.com/docs/en/overview",
+             VERSION: "2.1.21",
+             FEEDBACK_CHANNEL:
+               "https://github.com/anthropics/claude-code/issues",
+             BUILD_TIME: "2026-01-28T01:36:50Z",
+           }.VERSION,
+         };
+       }),
+       w)
+     )
+       YZ4();
+   }, [$, w]),
+     Q9A.useEffect(() => {
+       if (J && !w) Wv1();
+     }, [J, w]));
+   let [D, { isVisible: j }] = D4A(),
+     M = Xv1(),
+     P = Q9A.useRef(M);
+   if (j) P.current = M;
+   let {
+       version: V,
+       cwd: N,
+       modelDisplayName: T,
+       billingType: E,
+       agentName: R,
+     } = P.current,
+     b = X.agent ?? R,
+     S = a9(T, Bg6 - 20);
+   if (!W && !w && !j1(process.env.CLAUDE_CODE_FORCE_FULL_LOGO))
+     return P8.createElement(
+       P8.Fragment,
+       null,
+       P8.createElement(I, null),
+       P8.createElement(qMK, null),
+       KzA() &&
+         P8.createElement(
+           I,
+           { paddingLeft: 2, flexDirection: "column" },
+           P8.createElement(f, { color: "warning" }, "Debug mode enabled"),
+           P8.createElement(
+             f,
+             { dimColor: !0 },
+             "Logging to: ",
+             hh() ? "stderr" : ZNA(),
+           ),
+         ),
+       P8.createElement(ug6, null),
+       process.env.CLAUDE_CODE_TMUX_SESSION &&
+         P8.createElement(
+           I,
+           { paddingLeft: 2, flexDirection: "column" },
+           P8.createElement(
+             f,
+             { dimColor: !0 },
+             "tmux session: ",
+             process.env.CLAUDE_CODE_TMUX_SESSION,
+           ),
+           P8.createElement(
+             f,
+             { dimColor: !0 },
+             process.env.CLAUDE_CODE_TMUX_PREFIX_CONFLICTS
+               ? `Detach: ${process.env.CLAUDE_CODE_TMUX_PREFIX} ${process.env.CLAUDE_CODE_TMUX_PREFIX} d (press prefix twice - Claude uses ${process.env.CLAUDE_CODE_TMUX_PREFIX})`
+               : `Detach: ${process.env.CLAUDE_CODE_TMUX_PREFIX} d`,
+           ),
+         ),
+       G &&
+         P8.createElement(
+           I,
+           { paddingLeft: 2, flexDirection: "column" },
+           !process.env.IS_DEMO &&
+             $.oauthAccount?.organizationName &&
+             P8.createElement(
+               f,
+               { dimColor: !0 },
+               "Message from ",
+               $.oauthAccount.organizationName,
+               ":",
+             ),
+           P8.createElement(f, null, G),
+         ),
+       !1,
+       !1,
+     );
+   let B = hjK(z),
+     x = D1().theme,
+     F = ` ${S8("claude", x)("Claude Code")} ${S8("inactive", x)(`v${V}`)} `,
+     Q = S8("claude", x)(" Claude Code ");
+   if (B === "compact") {
+     let jA = Ov1(Y);
+     if (jA.length > z - 4) jA = Ov1(null);
+     let PA = " · ",
+       SA = "@",
+       mA = b ? z - 4 - SA.length - b.length - PA.length : z - 4,
+       qA = WdA(N, Math.max(mA, 10));
+     return P8.createElement(
+       P8.Fragment,
+       null,
+       P8.createElement(
+         I,
+         {
+           ref: D,
+           flexDirection: "column",
+           borderStyle: "round",
+           borderColor: "claude",
+           borderText: {
+             content: Q,
+             position: "top",
+             align: "start",
+             offset: 1,
+           },
+           paddingX: 1,
+           paddingY: 1,
+           alignItems: "center",
+           width: z,
+         },
+         P8.createElement(f, { bold: !0 }, jA),
+         P8.createElement(
+           I,
+           { marginY: 1 },
+           P8.createElement(
+             I,
+             { height: 5, flexDirection: "column", justifyContent: "flex-end" },
+             P8.createElement(
+               I,
+               { marginBottom: K },
+               P8.createElement(bg6, null),
+             ),
+           ),
+         ),
+         P8.createElement(f, { dimColor: !0 }, S),
+         P8.createElement(f, { dimColor: !0 }, E),
+         P8.createElement(f, { dimColor: !0 }, b ? `@${b} · ${qA}` : qA),
+       ),
+       H &&
+         P8.createElement(
+           I,
+           { marginTop: 1, flexDirection: "column" },
+           P8.createElement(
+             f,
+             { color: "warning" },
+             "Your bash commands will be sandboxed. Disable with /sandbox.",
+           ),
+         ),
+     );
+   }
+   let u = Ov1(Y),
+     d =
+       !process.env.IS_DEMO && $.oauthAccount?.organizationName
+         ? `${S} · ${E} · ${$.oauthAccount.organizationName}`
+         : `${S} · ${E}`,
+     o = " · ",
+     e = b ? Bg6 - 1 - b.length - o.length : Bg6,
+     wA = WdA(N, Math.max(e, 10)),
+     HA = b ? `@${b} · ${wA}` : wA,
+     OA = xjK(u, HA, d),
+     { leftWidth: WA, rightWidth: a } = bjK(z, B, OA);
+   return P8.createElement(
+     P8.Fragment,
+     null,
+     P8.createElement(I, null),
+     P8.createElement(
+       I,
+       {
+         ref: D,
+         flexDirection: "column",
+         borderStyle: "round",
+         borderColor: "claude",
+         borderText: { content: F, position: "top", align: "start", offset: 3 },
+       },
+       P8.createElement(
+         I,
+         {
+           flexDirection: B === "horizontal" ? "row" : "column",
+           paddingX: 1,
+           gap: 1,
+         },
+         P8.createElement(
+           I,
+           {
+             flexDirection: "column",
+             width: WA,
+             justifyContent: "space-between",
+             alignItems: "center",
+             minHeight: 9,
+           },
+           P8.createElement(
+             I,
+             { marginTop: 1 },
+             P8.createElement(f, { bold: !0 }, u),
+           ),
+           P8.createElement(
+             I,
+             { height: 5, flexDirection: "column", justifyContent: "flex-end" },
+             P8.createElement(
+               I,
+               { marginBottom: K },
+               P8.createElement(bg6, null),
+             ),
+           ),
+           P8.createElement(
+             I,
+             { flexDirection: "column", alignItems: "center" },
+             P8.createElement(f, { dimColor: !0 }, d),
+             P8.createElement(f, { dimColor: !0 }, HA),
+           ),
+         ),
+         B === "horizontal" &&
+           P8.createElement(m3, {
+             orientation: "vertical",
+             dividerColor: "claude",
+           }),
+         B === "horizontal" &&
+           P8.createElement(djK, {
+             feeds: w
+               ? [sjK(Yq6()), Zv1(q)]
+               : J
+                 ? [Zv1(q), tjK()]
+                 : [Zv1(q), ajK(_)],
+             maxWidth: a,
+           }),
+       ),
+     ),
+     KzA() &&
+       P8.createElement(
+         I,
+         { paddingLeft: 2, flexDirection: "column" },
+         P8.createElement(f, { color: "warning" }, "Debug mode enabled"),
+         P8.createElement(
+           f,
+           { dimColor: !0 },
+           "Logging to: ",
+           hh() ? "stderr" : ZNA(),
+         ),
+       ),
+     P8.createElement(ug6, null),
+     process.env.CLAUDE_CODE_TMUX_SESSION &&
+       P8.createElement(
+         I,
+         { paddingLeft: 2, flexDirection: "column" },
+         P8.createElement(
+           f,
+           { dimColor: !0 },
+           "tmux session: ",
+           process.env.CLAUDE_CODE_TMUX_SESSION,
+         ),
+         P8.createElement(
+           f,
+           { dimColor: !0 },
+           process.env.CLAUDE_CODE_TMUX_PREFIX_CONFLICTS
+             ? `Detach: ${process.env.CLAUDE_CODE_TMUX_PREFIX} ${process.env.CLAUDE_CODE_TMUX_PREFIX} d (press prefix twice - Claude uses ${process.env.CLAUDE_CODE_TMUX_PREFIX})`
+             : `Detach: ${process.env.CLAUDE_CODE_TMUX_PREFIX} d`,
+         ),
+       ),
+     G &&
+       P8.createElement(
+         I,
+         { paddingLeft: 2, flexDirection: "column" },
+         !process.env.IS_DEMO &&
+           $.oauthAccount?.organizationName &&
+           P8.createElement(
+             f,
+             { dimColor: !0 },
+             "Message from ",
+             $.oauthAccount.organizationName,
+             ":",
+           ),
+         P8.createElement(f, null, G),
+       ),
+     H &&
+       P8.createElement(
+         I,
+         { paddingLeft: 2, flexDirection: "column" },
+         P8.createElement(
+           f,
+           { color: "warning" },
+           "Your bash commands will be sandboxed. Disable with /sandbox.",
+         ),
+       ),
+     !1,
+     !1,
+   );
+ }

+++ Added $i2 (pretty-v2.1.21.js:522899-522918)
+ function $i2({ children: A }) {
+   let { bindings: K } = uyA(),
+     q = Lm.useRef(null),
+     Y = Lm.useRef(new Map()),
+     z = Lm.useRef(new Set()).current;
+   return Lm.default.createElement(
+     d51,
+     {
+       bindings: K,
+       pendingChordRef: q,
+       pendingChord: null,
+       setPendingChord: () => {},
+       activeContexts: z,
+       registerActiveContext: () => {},
+       unregisterActiveContext: () => {},
+       handlerRegistryRef: Y,
+     },
+     A,
+   );
+ }

+++ Added QNK (pretty-v2.1.21.js:524280-524282)
+ function QNK() {
+   return Bi2(H8(), gi2);
+ }

+++ Added Kr2 (pretty-v2.1.21.js:527373-527393)
+ function Kr2() {
+   if (!V4("tengu_coral_fern", !1)) return null;
+   return `# Accessing Past Sessions
+ You have access to past session data that may contain valuable context. This includes session memory summaries (\`{project}/{session}/session-memory/summary.md\`) and full transcript logs (\`{project}/{sessionId}.jsonl\`), stored under \`~/.claude/projects/\`.
+ 
+ ## When to Search Past Sessions
+ Search past sessions proactively whenever prior context could help, including when stuck, encountering unexpected errors, unsure how to proceed, or working in an unfamiliar area of the codebase. Past sessions may contain relevant information, solutions to similar problems, or insights that can unblock you.
+ 
+ ## How to Search
+ **Session memory summaries** (structured notes - only set for some sessions):
+ \`\`\`
+ ${cz} with pattern="<search term>" path="${SJ(f8())}/" glob="**/session-memory/summary.md"
+ \`\`\`
+ 
+ **Session transcript logs** (full conversation history):
+ \`\`\`
+ ${cz} with pattern="<search term>" path="${SJ(f8())}/" glob="*.jsonl"
+ \`\`\`
+ 
+ Search for error messages, file paths, function names, commands, or keywords related to the current task.`;
+ }

+++ Added qo2 (pretty-v2.1.21.js:531404-531404)
+   qo2 = 3600000,

+++ Added Ms2 (pretty-v2.1.21.js:536005-536007)
+ function Ms2() {
+   return `${C7().BASE_API_URL}/api/claude_code/user_settings`;
+ }

+++ Added pEK (pretty-v2.1.21.js:536463-536463)
+   pEK = !1,

+++ Added cEK (pretty-v2.1.21.js:536504-536504)
+ var cEK = !1,

+++ Added hkK (pretty-v2.1.21.js:538818-538820)
+ function hkK() {
+   if (EVA !== null) (clearInterval(EVA), (EVA = null));
+ }

+++ Added ykK (pretty-v2.1.21.js:538856-538856)
+   ykK = !1;

+++ Added XYA (pretty-v2.1.21.js:549314-549314)
+   XYA = null,

+++ Added qp6 (pretty-v2.1.21.js:549660-549660)
+ var qp6 = null,

+++ Added aE1 (pretty-v2.1.21.js:550510-550510)
+   aE1 = null;

+++ Added N1z (pretty-v2.1.21.js:551929-551929)
+   N1z = 20000,

+++ Added q7z (pretty-v2.1.21.js:567384-567384)
+   q7z = () => {},

+++ Added dk1 (pretty-v2.1.21.js:567385-567385)
+   dk1 = null;

+++ Added G7z (pretty-v2.1.21.js:568264-568264)
+   G7z = 5;

+++ Added SgK (pretty-v2.1.21.js:568587-568597)
+ var SgK = C(() => {
+   lA();
+   BA();
+   wZ();
+   v1();
+   t2();
+   ygK();
+   i1();
+   n3();
+   ((lL = r($A(), 1)), (rVA = r($A(), 1)));
+ });

+++ Added t7z (pretty-v2.1.21.js:571096-571100)
+ function t7z() {
+   return (
+     parseInt(process.env.CLAUDE_CODE_DATADOG_FLUSH_INTERVAL_MS || "", 10) || d7z
+   );
+ }

+++ Added Ec (pretty-v2.1.21.js:571109-571109)
+   Ec = null,

+++ Added AC1 (pretty-v2.1.21.js:571110-571110)
+   AC1 = null,

+++ Added a7z (pretty-v2.1.21.js:571112-571112)
+   a7z = 30,

+++ Added zQK (pretty-v2.1.21.js:571887-571891)
+ var zQK = C(() => {
+   c6();
+   B8();
+   B8();
+ });

+++ Added VKz (pretty-v2.1.21.js:572157-572193)
+ async function VKz(A, K, q, Y, z) {
+   let H = (await Y.getAppState()).toolPermissionContext.mode,
+     J = BUA(A, K, q, Y, H, z, Y.abortController.signal);
+   for await (let O of J)
+     if (
+       O.permissionRequestResult &&
+       (O.permissionRequestResult.behavior === "allow" ||
+         O.permissionRequestResult.behavior === "deny")
+     ) {
+       let X = O.permissionRequestResult;
+       if (X.behavior === "allow") {
+         let $ = X.updatedInput || q,
+           _ = X.updatedPermissions ?? [];
+         if (_.length > 0) {
+           IR(_);
+           let Z = await Y.getAppState(),
+             G = pj(Z.toolPermissionContext, _);
+           Y.setAppState((W) => {
+             if (W.toolPermissionContext === G) return W;
+             return { ...W, toolPermissionContext: G };
+           });
+         }
+         return {
+           behavior: "allow",
+           updatedInput: $,
+           userModified: !1,
+           decisionReason: { type: "hook", hookName: "PermissionRequest" },
+         };
+       } else
+         return {
+           behavior: "deny",
+           message: X.message || "Permission denied by PermissionRequest hook",
+           decisionReason: { type: "hook", hookName: "PermissionRequest" },
+         };
+     }
+   return;
+ }

+++ Added TKz (pretty-v2.1.21.js:572436-572436)
+   TKz = 30000,

+++ Added vKz (pretty-v2.1.21.js:572437-572437)
+   vKz = 1e4;

+++ Added $QK (pretty-v2.1.21.js:572515-572998)
+ class $QK {
+   config;
+   mutableMessages;
+   abortController;
+   permissionDenials;
+   totalUsage;
+   hasHandledOrphanedPermission = !1;
+   constructor(A) {
+     ((this.config = A),
+       (this.mutableMessages = A.initialMessages ?? []),
+       (this.abortController = A.abortController ?? s7()),
+       (this.permissionDenials = []),
+       (this.totalUsage = Nv));
+   }
+   async *submitMessage(A, K) {
+     let {
+       cwd: q,
+       commands: Y,
+       tools: z,
+       mcpClients: w,
+       verbose: H = !1,
+       maxThinkingTokens: J,
+       maxTurns: O,
+       maxBudgetUsd: X,
+       canUseTool: $,
+       customSystemPrompt: _,
+       appendSystemPrompt: Z,
+       userSpecifiedModel: G,
+       fallbackModel: W,
+       jsonSchema: D,
+       getAppState: j,
+       setAppState: M,
+       replayUserMessages: P = !1,
+       includePartialMessages: V = !1,
+       agents: N = [],
+       setSDKStatus: T,
+       orphanedPermission: E,
+     } = this.config;
+     Lv(q);
+     let R = !$l(),
+       b = Date.now(),
+       S = async (oA, V1, y1, p1, S6, B6) => {
+         let J1 = await $(oA, V1, y1, p1, S6, B6);
+         if (J1.behavior !== "allow")
+           this.permissionDenials.push({
+             tool_name: oA.name,
+             tool_use_id: S6,
+             tool_input: V1,
+           });
+         return J1;
+       },
+       B = await j(),
+       x = G ? jw(G) : Z3(),
+       [F, Q, u] = await Promise.all([
+         lf(
+           z,
+           x,
+           Array.from(
+             B.toolPermissionContext.additionalWorkingDirectories.keys(),
+           ),
+           w,
+         ),
+         i0(),
+         typeof _ === "string" ? Promise.resolve({}) : l0(),
+       ]),
+       d = [...(typeof _ === "string" ? [_] : F), ...(Z ? [Z] : [])],
+       o = z.some((oA) => oA.name === wW);
+     if (D && o) U_1(M, F1());
+     let l = {
+       messages: this.mutableMessages,
+       setMessages: () => {},
+       onChangeAPIKey: () => {},
+       options: {
+         commands: Y,
+         debug: !1,
+         tools: z,
+         verbose: H,
+         mainLoopModel: x,
+         maxThinkingTokens: J ?? 0,
+         mcpClients: w,
+         mcpResources: {},
+         ideInstallationStatus: null,
+         isNonInteractiveSession: !0,
+         customSystemPrompt: _,
+         appendSystemPrompt: Z,
+         agentDefinitions: { activeAgents: N, allAgents: [] },
+         theme: D1().theme,
+         maxBudgetUsd: X,
+       },
+       getAppState: j,
+       setAppState: M,
+       abortController: this.abortController,
+       readFileState: n3A(this.mutableMessages, q),
+       setInProgressToolUseIDs: () => {},
+       setResponseLength: () => {},
+       updateFileHistoryState: (oA) => {
+         M((V1) => ({ ...V1, fileHistory: oA(V1.fileHistory) }));
+       },
+       updateAttributionState: (oA) => {
+         M((V1) => ({ ...V1, attribution: oA(V1.attribution) }));
+       },
+       setSDKStatus: T,
+     };
+     if (E && !this.hasHandledOrphanedPermission) {
+       this.hasHandledOrphanedPermission = !0;
+       for await (let oA of TwK(E, z, this.mutableMessages, l)) yield oA;
+     }
+     let {
+       messages: e,
+       shouldQuery: wA,
+       allowedTools: HA,
+       maxThinkingTokens: OA,
+       model: WA,
+       resultText: a,
+     } = await jk1({
+       input: A,
+       mode: "prompt",
+       setIsLoading: () => {},
+       setToolJSX: () => {},
+       context: { ...l, messages: this.mutableMessages },
+       messages: this.mutableMessages,
+       uuid: K?.uuid,
+       querySource: "sdk",
+     });
+     this.mutableMessages.push(...e);
+     let _A = J ?? OA ?? 0,
+       jA = [...this.mutableMessages],
+       PA = e.filter(
+         (oA) =>
+           (oA.type === "user" && !oA.isMeta && !oA.toolUseResult) ||
+           (oA.type === "system" && oA.subtype === "compact_boundary"),
+       ),
+       SA = P ? PA : [];
+     M((oA) => ({
+       ...oA,
+       toolPermissionContext: {
+         ...oA.toolPermissionContext,
+         alwaysAllowRules: {
+           ...oA.toolPermissionContext.alwaysAllowRules,
+           command: HA,
+         },
+       },
+     }));
+     let mA = WA ?? x,
+       qA = n3A(jA, q),
+       YA = v$A(qA, l.readFileState);
+     l = {
+       messages: jA,
+       setMessages: () => {},
+       onChangeAPIKey: () => {},
+       options: {
+         commands: Y,
+         debug: !1,
+         tools: z,
+         verbose: H,
+         mainLoopModel: mA,
+         maxThinkingTokens: _A,
+         mcpClients: w,
+         mcpResources: {},
+         ideInstallationStatus: null,
+         isNonInteractiveSession: !0,
+         customSystemPrompt: _,
+         appendSystemPrompt: Z,
+         theme: D1().theme,
+         agentDefinitions: { activeAgents: N, allAgents: [] },
+         maxBudgetUsd: X,
+       },
+       getAppState: j,
+       setAppState: M,
+       abortController: this.abortController,
+       readFileState: YA,
+       setInProgressToolUseIDs: () => {},
+       setResponseLength: () => {},
+       updateFileHistoryState: l.updateFileHistoryState,
+       updateAttributionState: l.updateAttributionState,
+       setSDKStatus: T,
+     };
+     let AA = O8()?.outputStyle ?? pZ,
+       [t, { enabled: ZA }] = await Promise.all([AV1(b1()), bY()]);
+     if (
+       (yield {
+         type: "system",
+         subtype: "init",
+         cwd: q,
+         session_id: F1(),
+         tools: z.map((oA) => oA.name),
+         mcp_servers: w.map((oA) => ({ name: oA.name, status: oA.type })),
+         model: mA,
+         permissionMode: B.toolPermissionContext.mode,
+         slash_commands: Y.map((oA) => oA.name),
+         apiKeySource: Y0().source,
+         betas: nP(),
+         claude_code_version: {
+           ISSUES_EXPLAINER:
+             "report the issue at https://github.com/anthropics/claude-code/issues",
+           PACKAGE_URL: "@anthropic-ai/claude-code",
+           README_URL: "https://code.claude.com/docs/en/overview",
+           VERSION: "2.1.21",
+           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
+           BUILD_TIME: "2026-01-28T01:36:50Z",
+         }.VERSION,
+         output_style: AA,
+         agents: N.map((oA) => oA.agentType),
+         skills: t.map((oA) => oA.name),
+         plugins: ZA.map((oA) => ({ name: oA.name, path: oA.path })),
+         uuid: JAA(),
+       },
+       i3A("system_message_yielded"),
+       !wA)
+     ) {
+       for (let oA of PA) {
+         if (
+           oA.type === "user" &&
+           typeof oA.message.content === "string" &&
+           (oA.message.content.includes(`<${_zA}>`) ||
+             oA.message.content.includes(`<${zrA}>`) ||
+             oA.isCompactSummary)
+         )
+           (jA.push(oA),
+             yield {
+               type: "user",
+               message: { ...oA.message, content: KH(oA.message.content) },
+               session_id: F1(),
+               parent_tool_use_id: null,
+               uuid: oA.uuid,
+               isReplay: !oA.isCompactSummary,
+             });
+         if (oA.type === "system" && oA.subtype === "compact_boundary")
+           (jA.push(oA),
+             yield {
+               type: "system",
+               subtype: "compact_boundary",
+               session_id: F1(),
+               uuid: oA.uuid,
+               compact_metadata: {
+                 trigger: oA.compactMetadata.trigger,
+                 pre_tokens: oA.compactMetadata.preTokens,
+               },
+             });
+       }
+       if (R) await Jm(jA);
+       yield {
+         type: "result",
+         subtype: "success",
+         is_error: !1,
+         duration_ms: Date.now() - b,
+         duration_api_ms: DE(),
+         num_turns: jA.length - 1,
+         result: a ?? "",
+         session_id: F1(),
+         total_cost_usd: $G(),
+         usage: Nv,
+         modelUsage: Rh(),
+         permission_denials: this.permissionDenials,
+         uuid: JAA(),
+       };
+       return;
+     }
+     if (s2() && R)
+       e.filter(WcA).forEach((oA) => {
+         TWA((V1) => {
+           M((y1) => ({ ...y1, fileHistory: V1(y1.fileHistory) }));
+         }, oA.uuid);
+       });
+     let kA = Nv,
+       XA = 1,
+       LA = !1,
+       VA,
+       EA = D ? Nu6(this.mutableMessages, wW) : 0;
+     for await (let oA of Uf({
+       messages: jA,
+       systemPrompt: d,
+       userContext: Q,
+       systemContext: u,
+       canUseTool: S,
+       toolUseContext: l,
+       fallbackModel: W,
+       querySource: "sdk",
+       maxTurns: O,
+     })) {
+       if (
+         oA.type === "assistant" ||
+         oA.type === "user" ||
+         (oA.type === "system" && oA.subtype === "compact_boundary")
+       ) {
+         if ((jA.push(oA), R)) await Jm(jA);
+         if (!LA && SA.length > 0) {
+           LA = !0;
+           for (let V1 of SA)
+             if (V1.type === "user")
+               yield {
+                 type: "user",
+                 message: V1.message,
+                 session_id: F1(),
+                 parent_tool_use_id: null,
+                 uuid: V1.uuid,
+                 isReplay: !0,
+               };
+         }
+       }
+       if (oA.type === "user") XA++;
+       switch (oA.type) {
+         case "tombstone":
+           break;
+         case "assistant":
+         case "progress":
+         case "user":
+           (this.mutableMessages.push(oA), yield* NwK(oA));
+           break;
+         case "stream_event":
+           if (oA.event.type === "message_start")
+             ((kA = Nv), (kA = ldA(kA, oA.event.message.usage)));
+           if (oA.event.type === "message_delta") kA = ldA(kA, oA.event.usage);
+           if (oA.event.type === "message_stop")
+             this.totalUsage = tM1(this.totalUsage, kA);
+           if (V)
+             yield {
+               type: "stream_event",
+               event: oA.event,
+               session_id: F1(),
+               parent_tool_use_id: null,
+               uuid: JAA(),
+             };
+           break;
+         case "attachment":
+           if (
+             (this.mutableMessages.push(oA),
+             oA.attachment.type === "structured_output")
+           )
+             VA = oA.attachment.data;
+           else if (oA.attachment.type === "max_turns_reached") {
+             yield {
+               type: "result",
+               subtype: "error_max_turns",
+               duration_ms: Date.now() - b,
+               duration_api_ms: DE(),
+               is_error: !1,
+               num_turns: oA.attachment.turnCount,
+               session_id: F1(),
+               total_cost_usd: $G(),
+               usage: this.totalUsage,
+               modelUsage: Rh(),
+               permission_denials: this.permissionDenials,
+               uuid: JAA(),
+               errors: [],
+             };
+             return;
+           } else if (P && oA.attachment.type === "queued_command")
+             yield {
+               type: "user",
+               message: { role: "user", content: oA.attachment.prompt },
+               session_id: F1(),
+               parent_tool_use_id: null,
+               uuid: oA.attachment.source_uuid || oA.uuid,
+               isReplay: !0,
+             };
+           break;
+         case "stream_request_start":
+           break;
+         case "system":
+           if (
+             (this.mutableMessages.push(oA),
+             oA.subtype === "compact_boundary" && oA.compactMetadata)
+           )
+             yield {
+               type: "system",
+               subtype: "compact_boundary",
+               session_id: F1(),
+               uuid: oA.uuid,
+               compact_metadata: {
+                 trigger: oA.compactMetadata.trigger,
+                 pre_tokens: oA.compactMetadata.preTokens,
+               },
+             };
+           break;
+         case "tool_use_summary":
+           yield {
+             type: "tool_use_summary",
+             summary: oA.summary,
+             preceding_tool_use_ids: oA.precedingToolUseIds,
+             session_id: F1(),
+             uuid: oA.uuid,
+           };
+           break;
+       }
+       if (X !== void 0 && $G() >= X) {
+         yield {
+           type: "result",
+           subtype: "error_max_budget_usd",
+           duration_ms: Date.now() - b,
+           duration_api_ms: DE(),
+           is_error: !1,
+           num_turns: XA,
+           session_id: F1(),
+           total_cost_usd: $G(),
+           usage: this.totalUsage,
+           modelUsage: Rh(),
+           permission_denials: this.permissionDenials,
+           uuid: JAA(),
+           errors: [],
+         };
+         return;
+       }
+       if (oA.type === "user" && D) {
+         let y1 = Nu6(this.mutableMessages, wW) - EA,
+           p1 = parseInt(process.env.MAX_STRUCTURED_OUTPUT_RETRIES || "5", 10);
+         if (y1 >= p1) {
+           yield {
+             type: "result",
+             subtype: "error_max_structured_output_retries",
+             duration_ms: Date.now() - b,
+             duration_api_ms: DE(),
+             is_error: !1,
+             num_turns: XA,
+             session_id: F1(),
+             total_cost_usd: $G(),
+             usage: this.totalUsage,
+             modelUsage: Rh(),
+             permission_denials: this.permissionDenials,
+             uuid: JAA(),
+             errors: [
+               `Failed to provide valid structured output after ${p1} attempts`,
+             ],
+           };
+           return;
+         }
+       }
+     }
+     let CA = oW(jA);
+     if (!fwK(CA)) {
+       yield {
+         type: "result",
+         subtype: "error_during_execution",
+         duration_ms: Date.now() - b,
+         duration_api_ms: DE(),
+         is_error: !1,
+         num_turns: XA,
+         session_id: F1(),
+         total_cost_usd: $G(),
+         usage: this.totalUsage,
+         modelUsage: Rh(),
+         permission_denials: this.permissionDenials,
+         uuid: JAA(),
+         errors: DzA().map((oA) => oA.error),
+       };
+       return;
+     }
+     let dA = "",
+       z1 = !1;
+     if (CA.type === "assistant") {
+       let oA = oW(CA.message.content);
+       if (oA?.type === "text") dA = oA.text;
+       z1 = Boolean(CA.isApiErrorMessage);
+     }
+     yield {
+       type: "result",
+       subtype: "success",
+       is_error: z1,
+       duration_ms: Date.now() - b,
+       duration_api_ms: DE(),
+       num_turns: XA,
+       result: dA,
+       session_id: F1(),
+       total_cost_usd: $G(),
+       usage: this.totalUsage,
+       modelUsage: Rh(),
+       permission_denials: this.permissionDenials,
+       structured_output: VA,
+       uuid: JAA(),
+     };
+   }
+   interrupt() {
+     this.abortController.abort();
+   }
+   getMessages() {
+     return this.mutableMessages;
+   }
+   getSessionId() {
+     return F1();
+   }
+   setModel(A) {
+     this.config.userSpecifiedModel = A;
+   }
+ }

+++ Added ZQK (pretty-v2.1.21.js:573052-573084)
+ var ZQK = C(() => {
+   y1A();
+   OX();
+   u4();
+   df();
+   tk();
+   vk();
+   L3A();
+   CD();
+   gd();
+   UK();
+   j8();
+   ga();
+   up6();
+   s1();
+   z7();
+   p_1();
+   yk();
+   _z();
+   L4();
+   EUA();
+   HQA();
+   Kw();
+   c6();
+   Gz();
+   cB();
+   B8();
+   d0();
+   v1();
+   sM();
+   RE1();
+   Mf1();
+ });

+++ Added PQK (pretty-v2.1.21.js:573144-573193)
+ async function PQK() {
+   h("installPluginsForHeadless: starting");
+   try {
+     let [, A, K, q] = await Promise.all([Ck1(), gT1(), npA(), rpA()]),
+       Y = [];
+     if (A.size > 0) {
+       let X = await FT1(A);
+       for (let $ of X) {
+         let _ = A.get($);
+         if (!_) continue;
+         try {
+           (await Rv(_.source),
+             Y.push($),
+             h(`installPluginsForHeadless: installed extra marketplace ${$}`));
+         } catch (Z) {
+           (KA(Z instanceof Error ? Z : Error(String(Z))),
+             h(
+               `installPluginsForHeadless: failed to install extra marketplace ${$}`,
+             ));
+         }
+       }
+       if (Y.length > 0) (YPA(), US());
+     }
+     let z = await U3(),
+       w = K.filter((X) => !q.includes(X)),
+       H = [],
+       J = [];
+     for (let X of w) {
+       let [, $] = X.split("@");
+       if (!$ || $ in z) H.push(X);
+       else J.push(X);
+     }
+     if (J.length > 0)
+       h(
+         `installPluginsForHeadless: skipping ${J.length} plugins from unknown marketplaces: ${J.join(", ")}`,
+       );
+     if (H.length === 0)
+       return (h("installPluginsForHeadless: no plugins to install"), !1);
+     let O = await QT1(H, () => {});
+     if (O.installed.length > 0) US();
+     return (
+       h(
+         `installPluginsForHeadless: ${O.installed.length} installed, ${O.failed.length} failed`,
+       ),
+       O.installed.length > 0
+     );
+   } catch (A) {
+     return (KA(A instanceof Error ? A : Error(String(A))), !1);
+   }
+ }

+++ Added VQK (pretty-v2.1.21.js:573194-573203)
+ var VQK = C(() => {
+   dp6();
+   mPA();
+   vm6();
+   kJ();
+   pT1();
+   d0();
+   W1();
+   v1();
+ });

+++ Added yQK (pretty-v2.1.21.js:575076-575085)
+ var yQK = C(() => {
+   i1();
+   Nd();
+   lS();
+   yS();
+   W1();
+   ZH();
+   bt();
+   B8();
+ });

+++ Added aQK (pretty-v2.1.21.js:576245-576257)
+ var aQK = C(() => {
+   lA();
+   BA();
+   lQK();
+   t2();
+   nQK();
+   i1();
+   A4();
+   uB();
+   W1();
+   xB();
+   ((Ej = r($A(), 1)), (rQK = r($A(), 1)));
+ });

+++ Added import@531966 (pretty-v2.1.21.js:531967-531967)
+ import { homedir as No2, tmpdir as To2 } from "os";

+++ Added import@579881 (pretty-v2.1.21.js:579882-579891)
+ import {
+   existsSync as oo2,
+   unlinkSync as dQ6,
+   chmodSync as ivK,
+   statSync as ao2,
+   mkdirSync as so2,
+   readdirSync as nvK,
+   rmdirSync as to2,
+   appendFileSync as eo2,
+ } from "fs";

=== Structural Changes ===

@@@ variable 'QX8' (was 'XX8') — structural (95.6%)
--- pretty-v2.1.20.js:56536
+++ pretty-v2.1.21.js:56538
@@ -273,7 +273,8 @@
       },
       w = { match: $w(/\./, mM(...Tb1)), relevance: 0 },
       H = Tb1.filter((KA) => typeof KA === "string").concat(["_|0"]),
-      J = Tb1.filter((KA) => typeof KA !== "string")
+      J = db1
+        .filter((YA) => typeof YA !== "string")
         .concat(ZVq)
         .map(kb1),
       O = { variants: [{ className: "keyword", match: mM(...J, ...Nb1) }] },

@@@ variable 'aY6' (was 'RY6') — structural (95.0%)
--- pretty-v2.1.20.js:213529
+++ pretty-v2.1.21.js:213875
@@ -107,16 +107,14 @@
                 V = {};
               for (let T of P.entries()) V[T[0]] = T[1];
               if (j.body == null)
-                return j
-                  .blob()
-                  .then((T) => ({
-                    response: new du4.HttpResponse({
-                      headers: V,
-                      reason: j.statusText,
-                      statusCode: j.status,
-                      body: T,
-                    }),
-                  }));
+                return M.blob().then((T) => ({
+                  response: new SB4.HttpResponse({
+                    headers: V,
+                    reason: M.statusText,
+                    statusCode: M.status,
+                    body: T,
+                  }),
+                }));
               return {
                 response: new du4.HttpResponse({
                   headers: V,

@@@ variable 'su8' (was 'fu8') — structural (94.8%)
--- pretty-v2.1.20.js:106312
+++ pretty-v2.1.21.js:106343
@@ -76,16 +76,14 @@
               V = {};
             for (let T of P.entries()) V[T[0]] = T[1];
             if (j.body == null)
-              return j
-                .blob()
-                .then((T) => ({
-                  response: new Pu8.HttpResponse({
-                    headers: V,
-                    reason: j.statusText,
-                    statusCode: j.status,
-                    body: T,
-                  }),
-                }));
+              return M.blob().then((T) => ({
+                response: new ou8.HttpResponse({
+                  headers: V,
+                  reason: M.statusText,
+                  statusCode: M.status,
+                  body: T,
+                }),
+              }));
             return {
               response: new Pu8.HttpResponse({
                 headers: V,

@@@ variable 'B14' (was 'w14') — structural (94.8%)
--- pretty-v2.1.20.js:138727
+++ pretty-v2.1.21.js:138758
@@ -76,16 +76,14 @@
               V = {};
             for (let T of P.entries()) V[T[0]] = T[1];
             if (j.body == null)
-              return j
-                .blob()
-                .then((T) => ({
-                  response: new Y14.HttpResponse({
-                    headers: V,
-                    reason: j.statusText,
-                    statusCode: j.status,
-                    body: T,
-                  }),
-                }));
+              return M.blob().then((T) => ({
+                response: new x14.HttpResponse({
+                  headers: V,
+                  reason: M.statusText,
+                  statusCode: M.status,
+                  body: T,
+                }),
+              }));
             return {
               response: new Y14.HttpResponse({
                 headers: V,

@@@ function 'o6K' (was 's1K') — structural (94.6%)
--- pretty-v2.1.20.js:400703
+++ pretty-v2.1.21.js:401310
@@ -19,7 +19,6 @@
     $ = w === "pro" || w === "max",
     _ = w === "team" || w === "enterprise",
     Z = J === "default_claude_max_20x",
-    G = UG1("hide_overages_option_at_rate_limit_hit", "enabled", !1),
     W;
   if (K[3] === Symbol.for("react.memo_cache_sentinel"))
     ((W = (d_A() || Z4()) && ($ || X)), (K[3] = W));
@@ -76,7 +75,7 @@
       b = d;
       break A;
     }
-    if (!_ && (G || !Q)) {
+    if (!_ && !F) {
       let d;
       if (K[10] === Symbol.for("react.memo_cache_sentinel"))
         ((d = DS.default.createElement(

@@@ class '$36' (was 'p56') — structural (93.6%)
--- pretty-v2.1.20.js:193615
+++ pretty-v2.1.21.js:193956
@@ -12,7 +12,10 @@
   isRetrying = !1;
   lastExportErrorContext;
   constructor(A = {}) {
-    let K = process.env.ANTHROPIC_BASE_URL || "https://api.anthropic.com";
+    let K =
+      process.env.ANTHROPIC_BASE_URL === "https://api-staging.anthropic.com"
+        ? "https://api-staging.anthropic.com"
+        : "https://api.anthropic.com";
     ((this.endpoint = `${K}/api/event_logging/batch`),
       (this.timeout = A.timeout || 1e4),
       (this.maxBatchSize = A.maxBatchSize || 200),

@@@ function 'zRK' (was 'PLK') — structural (93.6%)
--- pretty-v2.1.20.js:551044
+++ pretty-v2.1.21.js:549865
@@ -158,9 +158,9 @@
             }
           }
         }
-        let $A = zA
-            .substring(0, t)
-            .match(/(^|\s)@([a-zA-Z0-9_\-./\\()[\]~:]*|"[^"]*"?)$/),
+        let ZA = JA.substring(0, t).match(
+            /(^|\s)@([a-zA-Z0-9_\-./\\()[\]~:]*|"[^"]*"?)$/,
+          ),
           vA = t === zA.length && t > 0 && zA.length > 0 && zA[t - 1] === " ";
         if (H === "prompt" && Yc(zA) && t > 0) {
           let ZA = Ue2(zA);

@@@ function '$_K' (was 'E$K') — structural (93.2%)
--- pretty-v2.1.20.js:482894
+++ pretty-v2.1.21.js:481124
@@ -5,6 +5,7 @@
     J;
   if (K[0] !== q || K[1] !== w || K[2] !== z)
     ((J = ($, _) => {
+      let Z = Ua($);
       if (_.upArrow || $ === "k") H((Z) => (Z > 0 ? Z - 1 : q.length - 1));
       else if (_.downArrow || $ === "j")
         H((Z) => (Z < q.length - 1 ? Z + 1 : 0));

@@@ variable 'Pj7' (was 'yD7') — structural (92.8%)
--- pretty-v2.1.20.js:312185
+++ pretty-v2.1.21.js:312928
@@ -52,7 +52,8 @@
     (X7($, { context: "Select", isActive: !A }),
       K8(
         (_, Z, G) => {
-          let W = Y.find((M) => M.value === q.focusedValue),
+          let W = Ua(_),
+            D = Y.find((M) => M.value === q.focusedValue),
             D = W?.type === "input";
           if (Z.tab && J && q.focusedValue !== void 0) {
             J(q.focusedValue);

@@@ function 'at' (was 'ht') — structural (92.6%)
--- pretty-v2.1.20.js:458905
+++ pretty-v2.1.21.js:456959
@@ -1,4 +1,6 @@
 async function ht(A, K) {
+  if (!YP("allow_remote_sessions"))
+    throw Error("Remote sessions are disabled by your organization's policy.");
   h(`Resuming code session ID: ${A}`);
   try {
     let q = lK()?.accessToken;

@@@ function 'P19' (was 'jA9') — structural (92.2%)
--- pretty-v2.1.20.js:181424
+++ pretty-v2.1.21.js:181649
@@ -48,8 +48,9 @@
     }
     let w = j51(z);
     h(`[keybindings] Loaded ${w.length} user bindings from ${K}`);
-    let H = [...A, ...w],
-      O = [...VK6(q), ...fK6(z, H)];
+    let H = [...A, ...w];
+    o$4(w.length);
+    let O = [...QK6(q), ...UK6(z, H)];
     if (O.length > 0) h(`[keybindings] Found ${O.length} validation issue(s)`);
     return { bindings: H, warnings: O };
   } catch (q) {

@@@ function 'JQA' (was 'UFA') — structural (91.9%)
--- pretty-v2.1.20.js:412236
+++ pretty-v2.1.21.js:412841
@@ -35,9 +35,6 @@
     addNotification: void 0,
     setToolJSX: void 0,
     setStreamMode: void 0,
-    setSpinnerMessage: void 0,
-    setSpinnerColor: void 0,
-    setSpinnerShimmerColor: void 0,
     setSDKStatus: void 0,
     openMessageSelector: void 0,
     options: K?.options ?? A.options,

@@@ class 'rGA' (was 'RGA') — structural (91.9%)
--- pretty-v2.1.20.js:311314
+++ pretty-v2.1.21.js:312056
@@ -3,7 +3,7 @@
   content = "";
   isTruncated = !1;
   totalBytesReceived = 0;
-  constructor(A = 67108736) {
+  constructor(A = rD7) {
     this.maxSize = A;
   }
   append(A) {

@@@ function 'SKz' (was '_7z') — structural (91.8%)
--- pretty-v2.1.20.js:574039
+++ pretty-v2.1.21.js:574237
@@ -17,6 +17,10 @@
     }
   if (K.teleport)
     try {
+      if (!YP("allow_remote_sessions"))
+        throw Error(
+          "Remote sessions are disabled by your organization's policy.",
+        );
       if ((n("tengu_teleport_print", {}), typeof K.teleport !== "string"))
         throw Error("No session ID provided for teleport");
       await vf1();

@@@ variable 'l51' (was 'T51') — structural (91.6%)
--- pretty-v2.1.20.js:180880
+++ pretty-v2.1.21.js:181099
@@ -21,6 +21,7 @@
           "ctrl+o": "app:toggleTranscript",
           "ctrl+shift+o": "app:toggleTeammatePreview",
           "ctrl+r": "history:search",
+          ...{},
         },
       },
       {

@@@ function 'OVA' (was 'pPA') — structural (91.6%)
--- pretty-v2.1.20.js:526453
+++ pretty-v2.1.21.js:524445
@@ -8,6 +8,7 @@
     X = 0,
     $ = {},
     _ = void 0,
+    Z = new Set(),
     Z = 20;
   for (let G = 0; G < A.length; G += Z) {
     let W = A.slice(G, G + Z),

@@@ function 'K9A' (was 'S3A') — structural (91.6%)
--- pretty-v2.1.20.js:459087
+++ pretty-v2.1.21.js:457143
@@ -1,4 +1,6 @@
 async function S3A(A) {
+  if (!YP("allow_remote_sessions"))
+    throw Error("Remote sessions are disabled by your organization's policy.");
   let { initialMessage: K, description: q, signal: Y } = A;
   try {
     await Rj();

@@@ class '$51' (was 'dq1') — structural (91.4%)
--- pretty-v2.1.20.js:176411
+++ pretty-v2.1.21.js:176597
@@ -53,10 +53,7 @@
           G = Math.min($ + Z, this.height, J.height),
           W = Math.min(X + _, this.width, J.width);
         for (let D = $; D < G; D++)
-          for (let M = X; M < W; M++) {
-            let j = XQ(J, M, D);
-            if (j) (aRA(K, M, D, j), q++);
-          }
+          for (let j = X; j < W; j++) (UO4(K, J, j, D), q++);
       }
       if (H.type === "write") {
         let { text: J } = H,
@@ -152,9 +149,13 @@
             }
             let N = m7(P.value);
             if (N === 0) continue;
+            let T = N >= 2;
+            if (T && j + 2 > this.width) {
+              j++;
+              continue;
+            }
             W[M] = P;
-            let T = N >= 2,
-              k = w04(P.styles),
+            let E = lO4(P.styles),
               R = k ? H04(P.styles) : P.styles;
             if (
               (aRA(K, M, X + Z, {

@@@ class 'KlA' (was 'ucA') — structural (91.4%)
--- pretty-v2.1.20.js:572454
+++ pretty-v2.1.21.js:571959
@@ -129,6 +129,8 @@
     return async (K, q, Y, z, w) => {
       let H = await P_(K, q, Y, z, w);
       if (H.behavior === "allow" || H.behavior === "deny") return H;
+      let J = await VKz(K.name, w, q, Y, H.suggestions);
+      if (J) return J;
       try {
         A?.();
         let J = await this.sendRequest(

@@@ function 'xM6' (was '_j6') — structural (90.8%)
--- pretty-v2.1.20.js:311299
+++ pretty-v2.1.21.js:312041
@@ -1,4 +1,4 @@
-function _j6(A, K = ",", q = 67108736) {
+function xM6(A, K = ",", q = rD7) {
   let z = "";
   for (let w of A) {
     let H = z ? K : "",

@@@ variable 'uNK' (was 'efK') — structural (90.6%)
--- pretty-v2.1.20.js:526124
+++ pretty-v2.1.21.js:524117
@@ -8,7 +8,6 @@
   kFA();
   qB();
   i6();
-  KI();
   ((Cv1 = r(XA(), 1)),
     (sfK = r(XA(), 1)),
     (tfK = {

@@@ function 'mSK' (was 'gIK') — structural (90.4%)
--- pretty-v2.1.20.js:561714
+++ pretty-v2.1.21.js:561232
@@ -8,7 +8,7 @@
   if (K[0] !== Y || K[1] !== q || K[2] !== z)
     ((O = () => {
       if (Y !== J.current) {
-        let j = Y.slice(-1);
+        let M = Ua(Y.slice(-1));
         if ($p6(j)) (z(Y.slice(0, -1)), q(Z6z[j]));
       }
     }),

@@@ variable 'gj1' (was 'MM1') — structural (90.2%)
--- pretty-v2.1.20.js:387712
+++ pretty-v2.1.21.js:388314
@@ -11,6 +11,7 @@
   lC6();
   nDA();
   o7();
+  l7();
   KL6 = r(XA(), 1);
   Ja7 = {
     type: "local-jsx",

@@@ class 'vKK' (was 'L7K') — structural (90.0%)
--- pretty-v2.1.20.js:422968
+++ pretty-v2.1.21.js:423619
@@ -44,6 +44,11 @@
         teammateContext: K.teammateContext,
         toolUseContext: this.context,
         abortController: K.abortController,
+        model: A.model,
+        systemPrompt: A.systemPrompt,
+        systemPromptMode: A.systemPromptMode,
+        allowedTools: A.permissions,
+        allowPermissionPrompts: A.allowPermissionPrompts,
       }),
         h(`[InProcessBackend] Started agent execution for ${K.agentId}`));
     return {
@@ -132,6 +137,7 @@
         h(`[InProcessBackend] kill() failed: task not found for ${A}`),
         !1
       );
+    if (q.localTaskId) Rq1(q.identity.teamName, q.localTaskId);
     let Y = Uj1(q.id, this.context.setAppState);
     return (
       h(`[InProcessBackend] kill() ${Y ? "succeeded" : "failed"} for ${A}`),

@@@ function 'uyA' (was 'TK6') — structural (88.7%)
--- pretty-v2.1.20.js:181501
+++ pretty-v2.1.21.js:181727
@@ -40,6 +40,7 @@
     if (
       (h(`[keybindings] Loaded ${w.length} user bindings from ${K}`),
       (uG = [...A, ...w]),
+      o$4(w.length),
       (TD = [...VK6(q), ...fK6(z, uG)]),
       TD.length > 0)
     )

@@@ function 'jyA' (was 'oRA') — structural (88.5%)
--- pretty-v2.1.20.js:176231
+++ pretty-v2.1.21.js:176298
@@ -7,7 +7,7 @@
     A = Math.max(0, Math.floor(A) || 0);
   if (!Number.isInteger(K) || K < 0) K = Math.max(0, Math.floor(K) || 0);
   let Y = A * K,
-    z = new Uint32Array(Y);
+    z = new Int32Array(Y);
   z.fill(pq1);
   let w = new Uint16Array(Y);
   w.fill(QOA);
@@ -25,6 +25,7 @@
       [" ", pq1],
       ["", S76],
     ]),
+    charAscii: Os3(),
     hyperlinks: [""],
     hyperlinkMap: new Map(),
     emptyStyleId: q.none,

@@@ variable 'tk' (was 'ik') — structural (87.6%)
--- pretty-v2.1.20.js:212090
+++ pretty-v2.1.21.js:212435
@@ -5,6 +5,7 @@
   Jw();
   mK();
   BM();
+  l6();
   ((WY6 = K6(async () => {
     let A = Date.now();
     L8("info", "git_status_started");
@@ -76,7 +77,7 @@
     (iO = K6(async () => {
       let A = Date.now();
       L8("info", "system_context_started");
-      let K = await WY6();
+      let K = j1(process.env.CLAUDE_CODE_REMOTE) ? null : await BY6();
       return (
         L8("info", "system_context_completed", {
           duration_ms: Date.now() - A,

@@@ variable 'TJ' (was 'r0') — structural (87.5%)
--- pretty-v2.1.20.js:161091
+++ pretty-v2.1.21.js:161158
@@ -22,5 +22,4 @@
       blockedBy: U.array(U.string()),
       metadata: U.record(U.string(), U.unknown()).optional(),
     })));
-  W46 = new Map();
 });

@@@ variable 'WMA' (was 'rMA') — structural (87.2%)
--- pretty-v2.1.20.js:426776
+++ pretty-v2.1.21.js:427433
@@ -36,7 +36,8 @@
       .describe(
         'Number of lines to show after each match (rg -A). Requires output_mode: "content", ignored otherwise.',
       ),
-    "-C": U.number()
+    "-C": U.number().optional().describe("Alias for context."),
+    context: U.number()
       .optional()
       .describe(
         'Number of lines to show before and after each match (rg -C). Requires output_mode: "content", ignored otherwise.',
@@ -215,6 +216,7 @@
           "-B": w,
           "-A": H,
           "-C": J,
+          context: O,
           "-n": O = !0,
           "-i": X = !1,
           head_limit: $,
@@ -232,11 +234,13 @@
         if (z === "files_with_matches") M.push("-l");
         else if (z === "count") M.push("-c");
         if (O && z === "content") M.push("-n");
-        if (J !== void 0 && z === "content") M.push("-C", J.toString());
-        else if (z === "content") {
+        if (z === "content")
           if (w !== void 0) M.push("-B", w.toString());
-          if (H !== void 0) M.push("-A", H.toString());
-        }
+          else if (J !== void 0) M.push("-C", J.toString());
+          else {
+            if (w !== void 0) M.push("-B", w.toString());
+            if (H !== void 0) M.push("-A", H.toString());
+          }
         if (A.startsWith("-")) M.push("-e", A);
         else M.push(A);
         if (Y) M.push("--type", Y);

@@@ function 'VYA' (was 't9A') — structural (86.7%)
--- pretty-v2.1.20.js:566264
+++ pretty-v2.1.21.js:565782
@@ -536,9 +536,25 @@
           dynamicSkillDirTriggers: new Set(),
           setResponseLength: oA,
           setStreamMode: V1,
-          setSpinnerMessage: UA,
-          setSpinnerColor: G1,
-          setSpinnerShimmerColor: S1,
+          onCompactProgress: (FK) => {
+            switch (FK.type) {
+              case "hooks_start":
+                (G1("claudeBlue_FOR_SYSTEM_SPINNER"),
+                  S1("claudeBlueShimmer_FOR_SYSTEM_SPINNER"),
+                  UA(
+                    FK.hookType === "pre_compact"
+                      ? "Running PreCompact hooks…"
+                      : "Running SessionStart hooks…",
+                  ));
+                break;
+              case "compact_start":
+                UA("Compacting conversation");
+                break;
+              case "compact_end":
+                (UA(null), G1(null), S1(null));
+                break;
+            }
+          },
           setInProgressToolUseIDs: cY,
           resume: c5,
           setConversationId: r8,
@@ -1183,7 +1199,7 @@
     ce = hq ? S4.slice(0, hq.messagesLength) : S4,
     KYA = hq ? b1.slice(0, hq.streamingToolUsesLength) : b1,
     le = hq ? e2(Nq.slice(0, hq.messageHistoryLength)).filter(l3A) : _G;
-  if ((QyK(), oyK(), o === "transcript"))
+  if ((IIK(), q7z(), FIK(), a === "transcript"))
     return T4.createElement(
       _H,
       null,
@@ -1280,6 +1296,7 @@
             overrideShimmerColor: E1,
             hasActiveTools: pq.size > 0,
           }),
+        null,
         !$6 &&
           !f4?.isLocalJSXCommand &&
           k.showExpandedTodos &&
@@ -1324,9 +1341,9 @@
               }
               BK((v7) => {
                 return (
-                  v7
-                    .filter((vq) => vq.hostPattern.host === A7)
-                    .forEach((vq) => vq.resolvePromise(u8)),
+                  N7.filter((FK) => FK.hostPattern.host === r4).forEach((FK) =>
+                    FK.resolvePromise(h8),
+                  ),
                   v7.filter((vq) => vq.hostPattern.host !== A7)
                 );
               });
@@ -1462,6 +1479,7 @@
                   setInputValue: sK,
                 }),
             !1,
+            null,
             T4.createElement(MyK, {
               debug: K,
               ideSelection: zA,

@@@ variable 'OX' — structural (86.6%)
--- pretty-v2.1.20.js:529007
+++ pretty-v2.1.21.js:527004
@@ -144,6 +144,7 @@
     tfK,
     RjK,
     hjK,
+    ...(fTK ? [fTK] : []),
     BjK,
     gjK,
     ojK,

@@@ variable 'iEK' (was 'XEK') — structural (86.0%)
--- pretty-v2.1.20.js:538525
+++ pretty-v2.1.21.js:536506
@@ -29,6 +29,7 @@
   pz();
   D1();
   BM();
+  gj();
   OEK = K6(() => {
     let A = Date.now();
     (L8("info", "init_started"), XK("init_function_start"));
@@ -61,6 +62,7 @@
         sC6())
       )
         Ka7();
+      if (BB()) As7();
       (XK("init_after_remote_settings_check"), YvK());
       let z = Date.now();
       (h("[init] configureGlobalMTLS starting"),

@@@ function 'vd6' (was 'ip6') — structural (84.6%)
--- pretty-v2.1.20.js:571508
+++ pretty-v2.1.21.js:571050
@@ -5,7 +5,7 @@
   try {
     let Y = await qr({ model: K.model }),
       { envContext: z, ...w } = Y,
-      H = { ...w, ...z, ...K };
+      H = { ...w, ...z, ...K, userBucket: s7z() };
     if (typeof H.toolName === "string" && H.toolName.startsWith("mcp__"))
       H.toolName = "mcp";
     if (typeof H.model === "string" && !H.model.startsWith("claude-"))
@@ -25,7 +25,8 @@
     let J = H,
       X = {
         ddsource: "nodejs",
-        ddtags: S4z.filter(($) => J[$] !== void 0 && J[$] !== null)
+        ddtags: n7z
+          .filter(($) => J[$] !== void 0 && J[$] !== null)
           .map(($) => `${vgK($)}:${J[$]}`)
           .join(","),
         message: A,

@@@ function 'njA' (was 'RMA') — structural (83.5%)
--- pretty-v2.1.20.js:414947
+++ pretty-v2.1.21.js:415559
@@ -33,6 +33,14 @@
       });
     if (Zp()) J_1(X, q, Z);
     let D = `${q}: ${z.substring(0, 50)}${z.length > 50 ? "..." : ""}`,
+      j = n0A(Y, {
+        subject: q,
+        description: z.substring(0, 100),
+        status: "in_progress",
+        blocks: [],
+        blockedBy: [],
+        metadata: {},
+      }),
       M = {
         ...lj($, "in_process_teammate", D),
         type: "in_process_teammate",
@@ -48,6 +56,8 @@
         lastReportedToolCount: 0,
         lastReportedTokenCount: 0,
         pendingUserMessages: [],
+        messages: [],
+        localTaskId: j,
       },
       j = dK(async () => {
         (h(`[spawnInProcessTeammate] Cleanup called for ${X}`), _.abort());

@@@ function 'xa7' (was 'co7') — structural (82.8%)
--- pretty-v2.1.20.js:386274
+++ pretty-v2.1.21.js:386556
@@ -10,6 +10,8 @@
   submitButtonText: O,
   onSubmit: X,
   onDownFromLastItem: $,
+  onUpFromFirstItem: _,
+  initialFocusLast: Z,
 }) {
   let [_, Z] = g5A.useState(Y),
     [G, W] = g5A.useState(!1),
@@ -33,7 +35,7 @@
     P = c$1({
       visibleOptionCount: K,
       options: q,
-      initialFocusValue: void 0,
+      initialFocusValue: Z ? q[q.length - 1]?.value : void 0,
       onFocus: H,
       focusValue: J,
     });
@@ -58,7 +60,8 @@
   return (
     K8(
       (N, T, k) => {
-        let b = q.find((B) => B.value === P.focusedValue)?.type === "input";
+        let S = Ua(E),
+          x = q.find((Q) => Q.value === N.focusedValue)?.type === "input";
         if (b) {
           if (
             !(
@@ -90,6 +93,7 @@
         ) {
           if (G && $) $();
           else if (O && X && P.focusedValue === S && !G) W(!0);
+          else if (!O && $ && N.focusedValue === F) $();
           else if (!G) P.focusNextOption();
           return;
         }
@@ -99,6 +103,7 @@
           (!T.ctrl && !T.shift && N === "k")
         ) {
           if (O && X && G) (W(!1), P.focusOption(S));
+          else if (_ && N.focusedValue === q[0]?.value) _();
           else P.focusPreviousOption();
           return;
         }

@@@ function 'n_4' (was 'w_4') — structural (82.4%)
--- pretty-v2.1.20.js:183840
+++ pretty-v2.1.21.js:184097
@@ -1,12 +1,13 @@
-function w_4(A, K) {
+function n_4(A, K, q) {
   let { exit: q } = PyA(),
     [Y, z] = sn.useState({ pending: !1, keyName: null }),
     w = sn.useMemo(() => K ?? q, [K, q]),
     H = fy((_) => z({ pending: _, keyName: "Ctrl-C" }), w),
     J = fy((_) => z({ pending: _, keyName: "Ctrl-D" }), w),
     O = sn.useCallback(() => {
+      if (K?.()) return;
       H();
-    }, [H]),
+    }, [J, K]),
     X = sn.useCallback(() => {
       J();
     }, [J]),

@@@ variable 'OUK' (was 'HQK') — structural (82.2%)
--- pretty-v2.1.20.js:579386
+++ pretty-v2.1.21.js:579635
@@ -178,6 +178,8 @@
   RZ();
   ddA();
   BM();
+  JcA();
+  gj();
   Zq = r(XA(), 1);
   XK("main_tsx_entry");
   XK("main_tsx_imports_loaded");

@@@ variable 'M4A' (was 'K4A') — structural (81.6%)
--- pretty-v2.1.20.js:185209
+++ pretty-v2.1.21.js:185529
@@ -13,6 +13,7 @@
   BA();
   i5();
   B1();
+  Hq6();
   LyA = {
     ghostty: "Ghostty",
     kitty: "Kitty",

@@@ function 'eB' (was 'QB') — structural (81.0%)
--- pretty-v2.1.20.js:420028
+++ pretty-v2.1.21.js:420640
@@ -1,7 +1,14 @@
 async function QB() {
   let [A] = fD2();
   if (l9()) {
-    if (XP1() || by6() || xy6() || uy6() || By6() || my6())
+    if (
+      yP1() ||
+      XI6() ||
+      (await $I6()) ||
+      (await _I6()) ||
+      (await ZI6()) ||
+      (await GI6())
+    )
       return "package-manager";
     return "native";
   }

@@@ function 'FO4' (was 'q04') — structural (80.4%)
--- pretty-v2.1.20.js:176264
+++ pretty-v2.1.21.js:176332
@@ -8,7 +8,7 @@
   if (!Number.isInteger(q) || q < 0) q = Math.max(0, Math.floor(q) || 0);
   let Y = K * q;
   if (A.chars.length < Y)
-    ((A.chars = new Uint32Array(Y)),
+    ((A.chars = new Int32Array(Y)),
       (A.styleIds = new Uint16Array(Y)),
       (A.widths = new Uint8Array(Y)),
       (A.hyperlinkIds = new Uint16Array(Y)));
@@ -22,6 +22,8 @@
     A.charStringMap.clear(),
     A.charStringMap.set(" ", pq1),
     A.charStringMap.set("", S76),
+    A.charAscii.fill(-1),
+    (A.charAscii[32] = wr),
     (A.hyperlinks.length = 1),
     A.hyperlinkMap.clear(),
     (A.damage = void 0));

@@@ function 'jHK' (was 'iwK') — structural (80.2%)
--- pretty-v2.1.20.js:459243
+++ pretty-v2.1.21.js:457302
@@ -1,6 +1,8 @@
 async function iwK() {
-  let A = [],
-    [K, q, Y, z] = await Promise.all([Vf1(), UwK(), pwK(), GS()]);
+  let A = [];
+  if (!YP("allow_remote_sessions"))
+    return (A.push({ type: "policy_blocked" }), A);
+  let [K, q, Y, z] = await Promise.all([Lf1(), zHK(), wHK(), fS()]);
   if (K) A.push({ type: "not_logged_in" });
   if (!q) A.push({ type: "no_remote_environment" });
   if (!Y) A.push({ type: "not_in_git_repo" });

@@@ function 'WQ' (was 'YQ') — structural (79.5%)
--- pretty-v2.1.20.js:160922
+++ pretty-v2.1.21.js:160984
@@ -1,6 +1,5 @@
 function YQ(A, K) {
   let q = SRA(A, K);
-  if (!qQ(q)) return null;
   try {
     let Y = Tr3(q, "utf-8"),
       z = G6(Y),
@@ -12,6 +11,7 @@
       );
     return w.data;
   } catch (Y) {
+    if (Y.code === "ENOENT") return null;
     return (
       h(
         `[Tasks] Failed to read task ${K}: ${Y instanceof Error ? Y.message : String(Y)}`,

@@@ function 'jNK' (was 'xfK') — structural (79.5%)
--- pretty-v2.1.20.js:524924
+++ pretty-v2.1.21.js:522919
@@ -19,23 +19,27 @@
         ((O = kv1.default.createElement(
           $Y,
           null,
-          kv1.default.createElement(Je, {
-            messages: A,
-            normalizedMessageHistory: z,
-            tools: K,
-            commands: w,
-            verbose: !1,
-            toolJSX: null,
-            toolUseConfirmQueue: H,
-            inProgressToolUseIDs: J,
-            isMessageSelectorVisible: !1,
-            conversationId: "export",
-            screen: "prompt",
-            screenToggleId: 0,
-            streamingToolUses: [],
-            showAllInTranscript: !0,
-            isLoading: !1,
-          }),
+          Lm.default.createElement(
+            $i2,
+            null,
+            Lm.default.createElement(ke, {
+              messages: A,
+              normalizedMessageHistory: z,
+              tools: K,
+              commands: w,
+              verbose: !1,
+              toolJSX: null,
+              toolUseConfirmQueue: H,
+              inProgressToolUseIDs: J,
+              isMessageSelectorVisible: !1,
+              conversationId: "export",
+              screen: "prompt",
+              screenToggleId: 0,
+              streamingToolUses: [],
+              showAllInTranscript: !0,
+              isLoading: !1,
+            }),
+          ),
         )),
           (Y[4] = O));
       else O = Y[4];

@@@ variable 'QU6' (was 'GU6') — structural (79.5%)
--- pretty-v2.1.20.js:546651
+++ pretty-v2.1.21.js:545462
@@ -26,5 +26,6 @@
   pD();
   kb6();
   gUA();
+  YpA();
   ((w3 = r(XA(), 1)), (wN = r(XA(), 1)), (ZU6 = [2, 3, 4, 6, 8]));
 });

@@@ function 'HV6' (was 'gP6') — structural (78.8%)
--- pretty-v2.1.20.js:318703
+++ pretty-v2.1.21.js:318996
@@ -1,3 +1,3 @@
 function gP6(A) {
-  return A.toLowerCase().includes("opus-4-5") || !1 || !1;
+  return A.toLowerCase().includes("opus-4-5") || !1 || !1 || !1;
 }

@@@ function 'uGK' (was 'oZK') — structural (78.3%)
--- pretty-v2.1.20.js:496608
+++ pretty-v2.1.21.js:494777
@@ -101,6 +101,33 @@
           childMcps: sA.get(c1.plugin.name) || [],
         });
       }
+      let oA = new Set(z1.map(({ item: P1 }) => P1.id)),
+        V1 = new Set(z1.map(({ item: P1 }) => P1.name)),
+        y1 = new Map();
+      for (let P1 of CA) {
+        if (
+          oA.has(P1.source) ||
+          ("plugin" in P1 && typeof P1.plugin === "string" && V1.has(P1.plugin))
+        )
+          continue;
+        let z6 = y1.get(P1.source) || [];
+        (z6.push(P1), y1.set(P1.source, z6));
+      }
+      let p1 = [];
+      for (let [P1, z6] of y1) {
+        let J6 = P1.split("@"),
+          TA = J6[0] || P1,
+          fA = J6[1] || "unknown";
+        p1.push({
+          type: "failed-plugin",
+          id: P1,
+          name: TA,
+          marketplace: fA,
+          scope: "user",
+          errorCount: z6.length,
+          errors: z6,
+        });
+      }
       let _1 = [];
       for (let c1 of J.mcp.clients) {
         if (c1.name === "ide") continue;
@@ -149,6 +176,11 @@
         if (!x1.has(z1)) x1.set(z1, []);
         x1.get(z1).push(c1);
       }
+      for (let P1 of p1) {
+        let z6 = P1.scope;
+        if (!$1.has(z6)) $1.set(z6, []);
+        $1.get(z6).push(P1);
+      }
       let M1 = [...x1.keys()].sort((c1, z1) => (k1[c1] ?? 99) - (k1[z1] ?? 99));
       for (let c1 of M1) {
         let z1 = x1.get(c1),
@@ -157,7 +189,7 @@
           b1 = 0;
         while (b1 < z1.length) {
           let X6 = z1[b1];
-          if (X6.type === "plugin") {
+          if (cA.type === "plugin" || cA.type === "failed-plugin") {
             let J6 = [X6];
             b1++;
             let fA = z1[b1];

@@@ function 'HR2' (was 'pv2') — structural (78.3%)
--- pretty-v2.1.20.js:452208
+++ pretty-v2.1.21.js:461124
@@ -8,6 +8,8 @@
         "function rg {",
         "  if [[ -n $ZSH_VERSION ]]; then",
         `    ARGV0=rg ${K} "$@"`,
+        '  elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "win32" ]]; then',
+        `    ARGV0=rg ${K} "$@"`,
         "  elif [[ $BASHPID != $$ ]]; then",
         `    exec -a rg ${K} "$@"`,
         "  else",

@@@ function 'OMA' (was 'Lf1') — structural (78.2%)
--- pretty-v2.1.20.js:460671
+++ pretty-v2.1.21.js:458735
@@ -11,9 +11,7 @@
     }
     let X = await K.getAppState();
     (vJ1(X.toolPermissionContext, "summary"),
-      K.setSpinnerColor?.("claudeBlue_FOR_SYSTEM_SPINNER"),
-      K.setSpinnerShimmerColor?.("claudeBlueShimmer_FOR_SYSTEM_SPINNER"),
-      K.setSpinnerMessage?.("Running PreCompact hooks..."),
+      K.onCompactProgress?.({ type: "hooks_start", hookType: "pre_compact" }),
       K.setSDKStatus?.("compacting"));
     let $ = await ib6(
       { trigger: w ? "auto" : "manual", customInstructions: z ?? null },
@@ -28,7 +26,7 @@
     let _ = $.userDisplayMessage;
     (K.setStreamMode?.("requesting"),
       K.setResponseLength?.(() => 0),
-      K.setSpinnerMessage?.("Compacting conversation"));
+      K.onCompactProgress?.({ type: "compact_start" }));
     let Z = i4("tengu_compact_cache_prefix", !1),
       G = o$6(z),
       W = q6({ content: G }),
@@ -83,7 +81,7 @@
     if (k) N.push(k);
     let R = fC2();
     if (R) N.push(R);
-    K.setSpinnerMessage?.("Running SessionStart hooks...");
+    K.onCompactProgress?.({ type: "hooks_start", hookType: "session_start" });
     let b = await HP("compact", void 0, void 0, K.options.mainLoopModel),
       S = yj([D]),
       B = fo(D);
@@ -127,9 +125,7 @@
   } finally {
     (K.setStreamMode?.("requesting"),
       K.setResponseLength?.(() => 0),
-      K.setSpinnerMessage?.(null),
-      K.setSDKStatus?.(null),
-      K.setSpinnerColor?.(null),
-      K.setSpinnerShimmerColor?.(null));
+      K.onCompactProgress?.({ type: "compact_end" }),
+      K.setSDKStatus?.(null));
   }
 }

@@@ function 'rOK' (was 'O0K') — structural (77.8%)
--- pretty-v2.1.20.js:469449
+++ pretty-v2.1.21.js:468192
@@ -5,10 +5,9 @@
     let z = A[Y];
     if ((K.push(z), z.type !== "assistant")) continue;
     let w = z.message.content
-      .filter(($) => $.type === "tool_use")
-      .map(($) => $.id);
-    if (w.length === 0) continue;
-    let H = A[Y + 1],
+        .filter((Z) => Z.type === "tool_use")
+        .map((Z) => Z.id),
+      H = A[Y + 1],
       J = new Set();
     if (H?.type === "user") {
       let $ = H.message.content;
@@ -18,8 +17,10 @@
             J.add(_.tool_use_id);
       }
     }
-    let O = w.filter(($) => !J.has($));
-    if (O.length === 0) continue;
+    let O = new Set(w),
+      X = w.filter((Z) => !J.has(Z)),
+      $ = [...J].filter((Z) => !O.has(Z));
+    if (X.length === 0 && $.length === 0) continue;
     q = !0;
     let X = O.map(($) => ({
       type: "tool_result",
@@ -29,11 +30,22 @@
     }));
     if (H?.type === "user") {
       let $ = Array.isArray(H.message.content)
-          ? H.message.content
-          : [{ type: "text", text: H.message.content }],
-        _ = { ...H, message: { ...H.message, content: [...X, ...$] } };
-      (Y++, K.push(_));
-    } else K.push(q6({ content: X, isMeta: !0 }));
+        ? H.message.content
+        : [{ type: "text", text: H.message.content }];
+      if ($.length > 0) {
+        let W = new Set($);
+        Z = Z.filter((D) => {
+          if (typeof D === "object" && "type" in D && D.type === "tool_result")
+            return !W.has(D.tool_use_id);
+          return !0;
+        });
+      }
+      let G = [..._, ...Z];
+      if (G.length > 0) {
+        let W = { ...H, message: { ...H.message, content: G } };
+        (Y++, K.push(W));
+      } else Y++;
+    } else if (_.length > 0) K.push(t1({ content: _, isMeta: !0 }));
   }
   if (q) {
     let Y = A.map((z, w) => {

@@@ variable 'lk' (was 'gk') — structural (77.6%)
--- pretty-v2.1.20.js:192657
+++ pretty-v2.1.21.js:192993
@@ -18,7 +18,11 @@
     if (Z4()) K.push(Bh);
     if (A.includes("[1m]")) K.push(gfA);
     if (!N1(process.env.DISABLE_INTERLEAVED_THINKING) && X$9(A)) K.push(Wi6);
-    N1(process.env.USE_API_CONTEXT_MANAGEMENT);
+    if (
+      (j1(process.env.USE_API_CONTEXT_MANAGEMENT) && !1) ||
+      (W_9(A) && V4("tengu_marble_anvil", !1))
+    )
+      K.push(wnA);
     let w = eY("tengu_tool_pear");
     if (h56(A) && w) K.push(Mi6);
     if (z && i4("tengu_scarf_coffee", !1)) K.push(FiA);

@@@ function 'Rq1' (was 'gw4') — structural (77.3%)
--- pretty-v2.1.20.js:160952
+++ pretty-v2.1.21.js:161014
@@ -2,6 +2,11 @@
   let q = SRA(A, K);
   if (!qQ(q)) return !1;
   try {
+    let Y = parseInt(K, 10);
+    if (!isNaN(Y)) {
+      let w = B46(A);
+      if (Y > w) MH4(A, Y);
+    }
     Bw4(q);
     let Y = JZ(A);
     for (let z of Y) {

@@@ function '$7z' (was 'o8z') — structural (75.8%)
--- pretty-v2.1.20.js:568597
+++ pretty-v2.1.21.js:568137
@@ -30,7 +30,8 @@
     }
     if (w < ScA) {
       let H = r8z * Math.pow(2, w - 1);
-      (pe(`Retrying in ${H}ms...`), await new Promise((J) => setTimeout(J, H)));
+      (wAA(`Retrying in ${H}ms...`),
+        await new Promise((J) => setTimeout(J, H)));
     }
   }
   throw Error(`Failed to download file ${A} after ${ScA} attempts`);

@@@ variable 'Xr' (was 't8A') — structural (75.8%)
--- pretty-v2.1.20.js:181623
+++ pretty-v2.1.21.js:181851
@@ -7,5 +7,6 @@
   o7();
   T51();
   z$4();
+  c$4();
   ((TD = []), (DyA = new Set()));
 });

@@@ function 'p76' (was 'N76') — structural (75.7%)
--- pretty-v2.1.20.js:175812
+++ pretty-v2.1.21.js:175880
@@ -42,29 +42,13 @@
       });
       return;
     }
-    if (_ && A.dirty) {
-      let G = Math.floor(_.x),
-        W = Math.floor(_.y),
-        D = Math.floor(_.x + _.width),
-        M = Math.floor(_.y + _.height),
-        j = Math.floor(J),
-        P = Math.floor(O),
-        V = Math.floor(J + X),
-        N = Math.floor(O + $);
-      if (G !== j || W !== P)
-        K.clear({
-          x: G,
-          y: W,
-          width: Math.floor(_.width),
-          height: Math.floor(_.height),
-        });
-      else {
-        if (D > V)
-          K.clear({ x: V, y: W, width: D - V, height: Math.floor(_.height) });
-        if (M > N)
-          K.clear({ x: G, y: N, width: Math.floor(_.width), height: M - N });
-      }
-    }
+    if (_ && A.dirty)
+      K.clear({
+        x: Math.floor(_.x),
+        y: Math.floor(_.y),
+        width: Math.floor(_.width),
+        height: Math.floor(_.height),
+      });
     let Z = bOA.get(A);
     if (Z) {
       for (let G of Z)
@@ -124,23 +108,34 @@
             : void 0;
         K.clip({ x1: M, x2: j, y1: P, y2: V });
       }
-      for (let M of A.childNodes)
+      let j = qr.has(A),
+        M = !1;
+      for (let P of A.childNodes) {
+        let V = P;
+        if (V.dirty) M = !0;
         N76(M, K, {
           offsetX: J,
           offsetY: O,
           skipStaticElements: z,
-          prevScreen: w,
+          prevScreen: j || M ? void 0 : w,
         });
+      }
       if (D) K.unclip();
       mJ4(J, O, A, K);
-    } else if (A.nodeName === "ink-root")
-      for (let G of A.childNodes)
+    } else if (A.nodeName === "ink-root") {
+      let G = qr.has(A),
+        W = !1;
+      for (let D of A.childNodes) {
+        let j = D;
+        if (j.dirty) W = !0;
         N76(G, K, {
           offsetX: J,
           offsetY: O,
           skipStaticElements: z,
-          prevScreen: w,
+          prevScreen: G || W ? void 0 : w,
         });
+      }
+    }
     (Fn.set(A, { x: J, y: O, width: X, height: $ }), (A.dirty = !1));
   }
 }

@@@ function 'mMA' (was 'jjA') — structural (75.7%)
--- pretty-v2.1.20.js:446942
+++ pretty-v2.1.21.js:447603
@@ -11,8 +11,9 @@
       signal: X,
     } = A,
     $ = await ey({ maxRetries: O, model: K }),
-    _ = TT(K),
-    Z = ST2(Y),
+    _ = [...ET(K)];
+  if (H && !_.includes(Ol)) _.push(Ol);
+  let Z = sv2(Y),
     G = w46(
       Z,
       {
@@ -20,9 +21,9 @@
           "report the issue at https://github.com/anthropics/claude-code/issues",
         PACKAGE_URL: "@anthropic-ai/claude-code",
         README_URL: "https://code.claude.com/docs/en/overview",
-        VERSION: "2.1.20",
+        VERSION: "2.1.21",
         FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-        BUILD_TIME: "2026-01-27T00:38:42Z",
+        BUILD_TIME: "2026-01-28T01:36:50Z",
       }.VERSION,
     ),
     W = Kq1(G),

@@@ variable 'nb8' (was 'Mb8') — structural (75.0%)
--- pretty-v2.1.20.js:103110
+++ pretty-v2.1.21.js:103140
@@ -4,5 +4,6 @@
   d0();
   ZV();
   W6A();
+  b6A();
   ((TH5 = [k7, bH, dz, K5, q0, QE]), (vH5 = [n5, cz, JD]));
 });

@@@ function 'Wqz' (was 'r7z') — structural (74.7%)
--- pretty-v2.1.20.js:577000
+++ pretty-v2.1.21.js:577212
@@ -8,7 +8,7 @@
     renderOptions: {
       ...q,
       onFrame: (z) => {
-        Y.record(z.durationMs);
+        if ((Y.record(z.durationMs), u$4())) return;
         for (let w of z.flickers) {
           if (w.reason === "resize") continue;
           let H = Date.now();

@@@ function 'Bf1' (was 'qf1') — structural (74.5%)
--- pretty-v2.1.20.js:459266
+++ pretty-v2.1.21.js:457328
@@ -9,5 +9,7 @@
     case "github_app_not_installed":
       return `The Claude GitHub app must be installed on this repository first.
 https://github.com/apps/claude/installations/new`;
+    case "policy_blocked":
+      return "Remote sessions are disabled by your organization's policy.";
   }
 }

@@@ function 'n3A' (was 'EjA') — structural (74.4%)
--- pretty-v2.1.20.js:454986
+++ pretty-v2.1.21.js:452884
@@ -32,7 +32,7 @@
 `,
               )
               .map((G) => {
-                let W = G.match(/^\s*\d+→(.*)$/);
+                let W = G.match(/^\s*\d+\u2192(.*)$/);
                 return W ? W[1] : G;
               })
               .join(

@@@ function 'mCK' (was 'akK') — structural (74.1%)
--- pretty-v2.1.20.js:546060
+++ pretty-v2.1.21.js:544846
@@ -8,6 +8,80 @@
     W = G ? void 0 : A.input.plan,
     D = G ? Ij() : void 0,
     M = A.input.allowedPrompts,
+    M = Am() && j !== void 0 && j.length > 0,
+    [P, V] = zJ.useState("options"),
+    N = zJ.useMemo(() => (j ?? []).map((XA, LA) => LA), [j]),
+    [T, E] = zJ.useState(N),
+    R = zJ.useMemo(() => j?.filter((XA, LA) => T.includes(LA)), [j, T]),
+    b = zJ.useMemo(
+      () =>
+        (j ?? []).map((XA, LA) => ({
+          label: `${XA.tool}(${OKK} ${XA.prompt})`,
+          value: LA,
+        })),
+      [j],
+    ),
+    [S, B] = zJ.useState(void 0),
+    x = zJ.useCallback(() => {
+      if (M) (B(void 0), V("permissions"));
+    }, [M]),
+    F = zJ.useMemo(
+      () => [
+        ...(z.toolPermissionContext.isBypassPermissionsModeAvailable
+          ? [
+              {
+                label: "Yes, clear context and bypass permissions",
+                value: "yes-bypass-permissions",
+              },
+            ]
+          : [
+              {
+                label: "Yes, clear context and auto-accept edits (shift+tab)",
+                value: "yes-accept-edits",
+              },
+            ]),
+        ...[],
+        ...(D8()
+          ? [
+              {
+                label: `Yes, and launch swarm (${_} teammates [tab])`,
+                value: "yes-launch-swarm-accept-edits",
+              },
+              ...(z.toolPermissionContext.isBypassPermissionsModeAvailable
+                ? [
+                    {
+                      label: `Yes, and launch swarm (bypass, ${_} teammates [tab])`,
+                      value: "yes-launch-swarm-bypass",
+                    },
+                  ]
+                : []),
+            ]
+          : []),
+        {
+          label: z.toolPermissionContext.isBypassPermissionsModeAvailable
+            ? "Yes, and bypass permissions"
+            : "Yes, auto-accept edits",
+          value: "yes-accept-edits-keep-context",
+        },
+        {
+          label: "Yes, manually approve edits",
+          value: "yes-default-keep-context",
+        },
+        {
+          type: "input",
+          label: "No, keep planning",
+          value: "no",
+          placeholder: "Type here to tell Claude what to change",
+          onChange: O,
+        },
+      ],
+      [z.toolPermissionContext.isBypassPermissionsModeAvailable, _],
+    ),
+    Q = zJ.useCallback(() => {
+      let XA = F[0]?.value;
+      if (XA) B(XA);
+      V("options");
+    }, [F]),
     j = W ?? PZ(),
     P = !j || j.trim() === "",
     [V, N] = wN.useState(() => {
@@ -58,11 +132,12 @@
             });
           if (PA.content !== null && PA.content !== V) (N(PA.content), k(!0));
         }
-      if (_A.shift && _A.tab) {
+      if (LA.shift && LA.tab && P === "options") {
         OA("yes-accept-edits");
         return;
       }
       if (
+        P === "options" &&
         j8() &&
         _A.tab &&
         (X === "yes-launch-swarm-accept-edits" ||
@@ -223,7 +298,8 @@
     }
     if (
       j8() &&
-      (o === "yes-launch-swarm-accept-edits" || o === "yes-launch-swarm-bypass")
+      (XA === "yes-launch-swarm-accept-edits" ||
+        XA === "yes-launch-swarm-bypass")
     ) {
       let zA =
         o === "yes-launch-swarm-bypass" ? "bypassPermissions" : "acceptEdits";
@@ -317,11 +393,9 @@
             onCancel: () => b("default"),
           }),
         ),
-        o
-          .filter((_A) => _A.url)
-          .map((_A, PA) =>
-            w3.default.createElement(f, { key: PA, dimColor: !0 }, _A.url),
-          ),
+        XA.filter((LA) => LA.url).map((LA, VA) =>
+          F5.default.createElement(f, { key: VA, dimColor: !0 }, LA.url),
+        ),
         w3.default.createElement(f, { dimColor: !0 }, "← to go back"),
       ),
     );
@@ -445,9 +519,7 @@
             permissionResult: A.permissionResult,
             toolType: "tool",
           }),
-          UB() &&
-            M &&
-            M.length > 0 &&
+          M &&
             w3.default.createElement(
               I,
               { flexDirection: "column", marginBottom: 1 },
@@ -456,19 +528,20 @@
                 { bold: !0 },
                 "Requested permissions:",
               ),
-              M.map((o, _A) =>
-                w3.default.createElement(
-                  f,
-                  { key: _A, dimColor: !0 },
-                  "  ",
-                  "· ",
-                  o.tool,
-                  "(",
-                  Z7K,
-                  " ",
-                  o.prompt,
-                  ")",
-                ),
+              F5.default.createElement(
+                I,
+                { marginLeft: 2 },
+                F5.default.createElement($jA, {
+                  options: b,
+                  defaultValue: N,
+                  isDisabled: P !== "permissions",
+                  onChange: E,
+                  onDownFromLastItem: Q,
+                  onUpFromFirstItem: () => {},
+                  initialFocusLast: !0,
+                  onCancel: Q,
+                  hideIndexes: !0,
+                }),
               ),
             ),
           w3.default.createElement(
@@ -480,58 +553,7 @@
             I,
             { marginTop: 1 },
             w3.default.createElement(y6, {
-              options: [
-                ...(z.toolPermissionContext.isBypassPermissionsModeAvailable
-                  ? [
-                      {
-                        label: "Yes, clear context and bypass permissions",
-                        value: "yes-bypass-permissions",
-                      },
-                    ]
-                  : [
-                      {
-                        label:
-                          "Yes, clear context and auto-accept edits (shift+tab)",
-                        value: "yes-accept-edits",
-                      },
-                    ]),
-                ...[],
-                ...(j8()
-                  ? [
-                      {
-                        label: `Yes, and launch swarm (${_} teammates [tab])`,
-                        value: "yes-launch-swarm-accept-edits",
-                      },
-                      ...(z.toolPermissionContext
-                        .isBypassPermissionsModeAvailable
-                        ? [
-                            {
-                              label: `Yes, and launch swarm (bypass, ${_} teammates [tab])`,
-                              value: "yes-launch-swarm-bypass",
-                            },
-                          ]
-                        : []),
-                    ]
-                  : []),
-                {
-                  label: z.toolPermissionContext
-                    .isBypassPermissionsModeAvailable
-                    ? "Yes, and bypass permissions"
-                    : "Yes, auto-accept edits",
-                  value: "yes-accept-edits-keep-context",
-                },
-                {
-                  label: "Yes, manually approve edits",
-                  value: "yes-default-keep-context",
-                },
-                {
-                  type: "input",
-                  label: "No, keep planning",
-                  value: "no",
-                  placeholder: "Type here to tell Claude what to change",
-                  onChange: O,
-                },
-              ],
+              options: F,
               onChange: (o) => OA(o),
               onCancel: () => {
                 (n("tengu_plan_exit", {
@@ -544,6 +566,9 @@
                   A.onReject());
               },
               onFocus: $,
+              onUpFromFirstItem: x,
+              isDisabled: P !== "options",
+              defaultFocusValue: S,
             }),
           ),
         ),

@@@ function 'BU' (was 'CU') — structural (74.0%)
--- pretty-v2.1.20.js:462438
+++ pretty-v2.1.21.js:460499
@@ -1,12 +1,12 @@
 function CU() {
   let A = m3A(),
     K = A === "tst" || A === "tst-auto";
-  switch (
-    (h(
-      `[ToolSearch:optimistic] mode=${A}, ENABLE_TOOL_SEARCH=${process.env.ENABLE_TOOL_SEARCH}, result=${K}`,
-    ),
-    A)
-  ) {
+  if (!OJK)
+    ((OJK = !0),
+      h(
+        `[ToolSearch:optimistic] mode=${A}, ENABLE_TOOL_SEARCH=${process.env.ENABLE_TOOL_SEARCH}, result=${K}`,
+      ));
+  switch (A) {
     case "tst":
     case "tst-auto":
       return !0;

@@@ class 'YK6' (was 'u76') — structural (73.8%)
--- pretty-v2.1.20.js:176691
+++ pretty-v2.1.21.js:176878
@@ -83,19 +83,21 @@
       !z
     ) {
       let M = A.screen.height - A.viewport.height + 1,
-        j = h76(A.screen, K.screen),
-        P = j.filter(([V]) => V.y < M);
-      if (P.length > 0) {
-        let [V] = P[0],
-          N = V.y,
-          T = "";
+        P = -1;
+      if (
+        (AK6(A.screen, K.screen, (V, N) => {
+          if (N < M) return ((P = N), !0);
+        }),
+        P >= 0)
+      ) {
+        let V = "";
         for (let R = 0; R < A.screen.width; R++)
-          T += XQ(A.screen, R, N)?.char ?? " ";
+          V += e76(A.screen, T, P) ?? " ";
         let k = "";
         for (let R = 0; R < K.screen.width; R++)
-          k += XQ(K.screen, R, N)?.char ?? " ";
+          N += e76(K.screen, T, P) ?? " ";
         return (
-          h(`Full reset (scrollback changes): scrollbackRows=${M}, changes=${P.length}/${j.length}, firstChangeY=${N}
+          h(`Full reset (scrollback changes): scrollbackRows=${M}, firstChangeY=${P}
   prev: "${T}"
   next: "${k}"`),
           pOA(K, "offscreen", this.options.stylePool)
@@ -122,38 +124,43 @@
         ? Math.max(0, A.screen.height - A.viewport.height)
         : Math.max(A.screen.height, K.screen.height) - K.viewport.height,
       Z = [],
-      G = void 0;
-    for (let [D, M, j] of h76(A.screen, K.screen)) {
-      if ($ && D.y >= A.screen.height) continue;
-      if (j && (j.width === 2 || j.width === 3)) continue;
-      if (M && (M.width === 2 || M.width === 3) && !j) continue;
-      if (j && K04(K.screen, D.x, D.y) && !M) continue;
-      if (D.y < _) return pOA(K, "offscreen", this.options.stylePool);
-      if ((x76(J, D.x, D.y), j)) {
-        let P = j.hyperlink;
-        G = _04(J.diff, G, P);
-        let V = this.options.stylePool.get(j.styleId),
-          N = Gx(Z, V);
-        (G04(J, j, N), (Z = V));
-      } else if (M) {
-        let P = Z,
-          V = G;
-        ((Z = []),
-          (G = void 0),
-          J.txn(() => {
-            let N = [];
-            if (P.length > 0) {
-              let T = Gx(P, []);
-              if (T.length > 0) N.push({ type: "style", codes: T });
-            }
-            if (V !== void 0) N.push({ type: "hyperlink", uri: "" });
-            return (
-              N.push({ type: "stdout", content: " " }),
-              [N, { dx: 1, dy: 0 }]
-            );
-          }));
-      }
-    }
+      G = void 0,
+      W = !1;
+    if (
+      (AK6(A.screen, K.screen, (j, M, P, V) => {
+        if ($ && M >= A.screen.height) return;
+        if (V && (V.width === 2 || V.width === 3)) return;
+        if (P && (P.width === 2 || P.width === 3) && !V) return;
+        if (V && BO4(K.screen, j, M) && !P) return;
+        if (M < _) return ((W = !0), !0);
+        if ((qK6(J, j, M), V)) {
+          let N = V.hyperlink;
+          G = sO4(J.diff, G, N);
+          let T = this.options.stylePool.get(V.styleId),
+            E = Tx(Z, T);
+          (eO4(J, V, E), (Z = T));
+        } else if (P) {
+          let N = Z,
+            T = G;
+          ((Z = []),
+            (G = void 0),
+            J.txn(() => {
+              let E = [];
+              if (N.length > 0) {
+                let R = Tx(N, []);
+                if (R.length > 0) E.push({ type: "style", codes: R });
+              }
+              if (T !== void 0) E.push({ type: "hyperlink", uri: "" });
+              return (
+                E.push({ type: "stdout", content: " " }),
+                [E, { dx: 1, dy: 0 }]
+              );
+            }));
+        }
+      }),
+      W)
+    )
+      return XXA(K, "offscreen", this.options.stylePool);
     if (Z.length > 0) {
       let D = Gx(Z, []);
       if (D.length > 0) J.diff.push({ type: "style", codes: D });

@@@ function 'X51' (was 'aRA') — structural (73.2%)
--- pretty-v2.1.20.js:176304
+++ pretty-v2.1.21.js:176390
@@ -1,6 +1,27 @@
 function aRA(A, K, q, Y) {
   if (K < 0 || q < 0 || K >= A.width || q >= A.height) return;
-  let z = q * A.width + K;
+  let z = q * A.width + K,
+    w = A.widths[z];
+  if (w === 1 && Y.width !== 1) {
+    if (K + 1 < A.width) {
+      let O = z + 1;
+      if (A.widths[O] === 2)
+        ((A.chars[O] = wr),
+          (A.styleIds[O] = A.emptyStyleId),
+          (A.widths[O] = 0),
+          (A.hyperlinkIds[O] = 0));
+    }
+  }
+  if (w === 2 && Y.width !== 2) {
+    if (K > 0) {
+      let J = z - 1;
+      if (A.widths[J] === 1)
+        ((A.chars[J] = wr),
+          (A.styleIds[J] = A.emptyStyleId),
+          (A.widths[J] = 0),
+          (A.hyperlinkIds[J] = 0));
+    }
+  }
   ((A.chars[z] = Xa3(A, Y.char)),
     (A.styleIds[z] = Y.styleId),
     (A.widths[z] = Y.width),

@@@ function 'CKz' (was 'H7z') — structural (72.8%)
--- pretty-v2.1.20.js:573267
+++ pretty-v2.1.21.js:573416
@@ -364,14 +364,46 @@
             else $.maxThinkingTokens = JA.request.max_thinking_tokens;
             a(JA);
           } else if (JA.request.subtype === "mcp_status") {
-            let OA = [...K, ...T, ...b.clients].map((HA) => {
-              return {
-                name: HA.name,
-                status: HA.type,
-                serverInfo: HA.type === "connected" ? HA.serverInfo : void 0,
-                error: HA.type === "failed" ? HA.error : void 0,
-              };
-            });
+            let HA = await J(),
+              OA = HA.mcp.clients,
+              WA = HA.mcp.tools,
+              a = [...OA, ...T, ...b.clients].map((_A) => {
+                let jA;
+                if (_A.config.type === "sse" || _A.config.type === "http")
+                  jA = { type: _A.config.type, url: _A.config.url };
+                else if (_A.config.type === "claudeai-proxy")
+                  jA = {
+                    type: "claudeai-proxy",
+                    url: _A.config.url,
+                    id: _A.config.id,
+                  };
+                else if (_A.config.type === "stdio")
+                  jA = {
+                    type: "stdio",
+                    command: _A.config.command,
+                    args: _A.config.args,
+                  };
+                let PA =
+                  _A.type === "connected"
+                    ? ru(WA, _A.name).map((SA) => ({
+                        name: SA.originalMcpToolName ?? SA.name,
+                        annotations: {
+                          readOnly: SA.isReadOnly({}) || void 0,
+                          destructive: SA.isDestructive?.({}) || void 0,
+                          openWorld: SA.isOpenWorld?.({}) || void 0,
+                        },
+                      }))
+                    : void 0;
+                return {
+                  name: _A.name,
+                  status: _A.type,
+                  serverInfo: _A.type === "connected" ? _A.serverInfo : void 0,
+                  error: _A.type === "failed" ? _A.error : void 0,
+                  config: jA,
+                  scope: _A.config.scope,
+                  tools: PA,
+                };
+              });
             a(JA, { mcpServers: OA });
           } else if (JA.request.subtype === "mcp_message") {
             let OA = JA.request,
@@ -400,7 +432,7 @@
             if ((a(JA, OA), HA)) R();
           } else if (JA.request.subtype === "mcp_reconnect") {
             let { serverName: OA } = JA.request,
-              HA = NI(OA);
+              OA = LI(HA) ?? K.find((WA) => WA.name === HA)?.config ?? null;
             if (!HA) l(JA, `Server not found: ${OA}`);
             else {
               let DA = await Qu(OA, HA),
@@ -440,13 +472,30 @@
             }
           } else if (JA.request.subtype === "mcp_toggle") {
             let { serverName: OA, enabled: HA } = JA.request,
-              DA = NI(OA);
+              WA = LI(HA) ?? K.find((a) => a.name === HA)?.config ?? null;
             if (!DA) l(JA, `Server not found: ${OA}`);
             else if (!HA) {
               JGA(OA, !1);
               let o = [...K, ...T, ...b.clients].find((_A) => _A.name === OA);
               if (o && o.type === "connected") await Fu(OA, DA);
-              a(JA);
+              let _A = lHA(HA);
+              (O((jA) => ({
+                ...jA,
+                mcp: {
+                  ...jA.mcp,
+                  clients: jA.mcp.clients.map((PA) =>
+                    PA.name === HA
+                      ? { name: HA, type: "disabled", config: WA }
+                      : PA,
+                  ),
+                  tools: ah(jA.mcp.tools, (PA) => PA.name?.startsWith(_A)),
+                  commands: ah(jA.mcp.commands, (PA) =>
+                    PA.name?.startsWith(_A),
+                  ),
+                  resources: uwA(jA.mcp.resources, HA),
+                },
+              })),
+                o(wA));
             } else {
               JGA(OA, !0);
               let o = await Qu(OA, DA),

@@@ variable 'BGK' (was 'w$K') — structural (72.4%)
--- pretty-v2.1.20.js:481360
+++ pretty-v2.1.21.js:495880
@@ -31,6 +31,5 @@
   o7();
   S9();
   jQA();
-  a3A();
   ((Z6 = r(XA(), 1)), (wm = r(XA(), 1)));
 });

@@@ variable 'vCK' (was 'EMK') — structural (72.4%)
--- pretty-v2.1.20.js:505810
+++ pretty-v2.1.21.js:543287
@@ -21,6 +21,5 @@
   TMK();
   hH();
   Xg6();
-  w4();
   ((f8 = r(XA(), 1)), (KdA = r(XA(), 1)));
 });

@@@ variable 'tmK' (was 'up6') — structural (72.4%)
--- pretty-v2.1.20.js:567849
+++ pretty-v2.1.21.js:565553
@@ -5,141 +5,5 @@
   a0();
   Hw();
   jFA();
-  sEK();
-  r8A();
-  _j();
-  Y6();
-  D1();
-  B1();
-  Vv();
-  IMA();
-  sFA();
-  j2();
-  AkK();
-  W3A();
-  ha();
-  YkK();
-  Of1();
-  HkK();
-  $CK();
-  MCK();
-  jyK();
-  VyK();
-  LyK();
-  RyK();
-  t2();
-  Pv();
-  $J1();
-  ik();
-  FG();
-  nQ6();
-  jk();
-  Ap6();
-  byK();
-  Ny();
-  uyK();
-  ByK();
-  myK();
-  cp();
-  d2();
-  FyK();
-  UyK();
-  nyK();
-  ayK();
-  AIK();
-  yH();
-  GU6();
-  i6();
-  a1();
-  P8();
-  tuA();
-  $z();
-  vp();
-  ZH();
-  KIK();
-  wIK();
-  JIK();
-  NjA();
-  $3A();
-  $IK();
-  wy6();
-  qF6();
-  ZIK();
-  WIK();
-  Hp6();
-  hPA();
-  egA();
-  HL6();
-  MIK();
-  Ap();
-  JL6();
-  EyA();
-  It();
-  PIK();
-  W_();
-  tqA();
-  VFA();
-  w4();
-  Du();
-  VZ();
-  qq();
-  CjA();
-  Xf1();
-  g3A();
-  aj();
-  i4A();
-  qq();
-  fcA();
-  TIK();
-  S9();
-  vIK();
-  iH();
-  CIK();
-  DF6();
-  bN1();
-  Mf();
-  RIK();
-  B$1();
-  IIK();
-  DqA();
-  MUA();
-  bM6();
-  wL6();
-  Zz();
-  rt();
-  uIK();
-  mIK();
-  QIK();
-  dIK();
-  lIK();
-  rIK();
-  aIK();
-  KSK();
-  zSK();
-  hH();
-  HSK();
-  JSK();
-  OBK();
-  EB6();
-  _BK();
-  GBK();
-  EBK();
-  LBK();
-  IBK();
-  hBK();
-  xBK();
-  fj1();
-  BBK();
-  gBK();
-  QBK();
-  pBK();
-  cBK();
-  nBK();
-  aBK();
-  eBK();
-  qmK();
-  zmK();
-  JmK();
-  OmK();
   ((T4 = r(XA(), 1)), (q8 = r(XA(), 1)));
 });

@@@ variable 'Zd6' (was 'rFK') — structural (72.4%)
--- pretty-v2.1.20.js:576034
+++ pretty-v2.1.21.js:567386
@@ -8,5 +8,141 @@
   w4();
   D1();
   vB();
+  s1();
+  W1();
+  h1();
+  Tv();
+  ojA();
+  GH();
+  Pd();
+  PQA();
+  P2();
+  mkK();
+  Pd();
+  oa();
+  QkK();
+  RE1();
+  nkK();
+  sCK();
+  YLK();
+  zIK();
+  HIK();
+  WIK();
+  DIK();
+  t2();
+  PIK();
+  df();
+  xJ1();
+  tk();
+  BG();
+  PU6();
+  vk();
+  Rp6();
+  vIK();
+  ky();
+  kIK();
+  CIK();
+  LIK();
+  uB();
+  d2();
+  yIK();
+  SIK();
+  mIK();
+  QIK();
+  cIK();
+  ow();
+  QU6();
+  c6();
+  i1();
+  j8();
+  MBA();
+  _z();
+  xp();
+  ZH();
+  ASK();
+  zSK();
+  HSK();
+  UMA();
+  L3A();
+  XSK();
+  uy6();
+  LF6();
+  _SK();
+  GSK();
+  mp6();
+  sPA();
+  VFA();
+  xL6();
+  DSK();
+  Zp();
+  uL6();
+  cyA();
+  rt();
+  MSK();
+  Z_();
+  D5A();
+  FFA();
+  A4();
+  ku();
+  PZ();
+  UK();
+  dMA();
+  Mf1();
+  e3A();
+  sM();
+  O7A();
+  UK();
+  QcA();
+  NSK();
+  y9();
+  TSK();
+  nH();
+  kSK();
+  QF6();
+  rN1();
+  Pf();
+  LSK();
+  H_1();
+  ySK();
+  SqA();
+  bUA();
+  qM6();
+  bL6();
+  Gz();
+  Ze();
+  xSK();
+  BSK();
+  FSK();
+  pSK();
+  cSK();
+  nSK();
+  oSK();
+  AhK();
+  YhK();
+  hH();
+  whK();
+  HhK();
+  JmK();
+  rB6();
+  $mK();
+  ZmK();
+  vmK();
+  CmK();
+  ymK();
+  SmK();
+  bmK();
+  pM1();
+  umK();
+  mmK();
+  FmK();
+  UmK();
+  dmK();
+  imK();
+  omK();
+  tmK();
+  KgK();
+  YgK();
+  HgK();
+  JgK();
   ((CP = r(XA(), 1)), (iFK = r(XA(), 1)));
 });

@@@ function 'DP2' (was 'oM2') — structural (72.3%)
--- pretty-v2.1.20.js:425040
+++ pretty-v2.1.21.js:425698
@@ -45,8 +45,7 @@
       permissionMode: $.toolPermissionContext.mode,
     });
   if (X)
-    ((k = k
-      .split(" ")
+    ((E = E.split(" ")
       .filter((x, F, Q) => x !== "--model" && Q[F - 1] !== "--model")
       .join(" ")),
       (k = k ? `${k} --model ${I4([X])}` : `--model ${I4([X])}`));

@@@ function 'oQK' (was 'nFK') — structural (72.2%)
--- pretty-v2.1.20.js:575998
+++ pretty-v2.1.21.js:576205
@@ -6,27 +6,31 @@
         CP.default.createElement(
           $Y,
           null,
-          CP.default.createElement(y7z, {
-            onComplete: (q) => {
-              (K(), A(q));
-            },
-            onCancel: () => {
-              (K(), A(null));
-            },
-            onError: (q, Y) => {
-              (process.stderr.write(
-                Y
-                  ? Y +
-                      `
+          Ej.default.createElement(
+            Rz,
+            null,
+            Ej.default.createElement(oKz, {
+              onComplete: (q) => {
+                (K(), A(q));
+              },
+              onCancel: () => {
+                (K(), A(null));
+              },
+              onError: (q, Y) => {
+                (process.stderr.write(
+                  Y
+                    ? Y +
+                        `
 `
-                  : `Error: ${q}
+                    : `Error: ${q}
 `,
-              ),
-                K(),
-                A(null));
-            },
-            source: "cliArg",
-          }),
+                ),
+                  K(),
+                  A(null));
+              },
+              source: "cliArg",
+            }),
+          ),
         ),
         Sw(!1),
       );

@@@ variable 'vFK' (was 'EgK') — structural (71.9%)
--- pretty-v2.1.20.js:571564
+++ pretty-v2.1.21.js:571114
@@ -4,6 +4,7 @@
   R1();
   s0();
   WQ();
+  CQ();
   ((I4z = new Set([
     "tengu_api_error",
     "tengu_api_success",
@@ -33,6 +34,7 @@
       "platform",
       "provider",
       "toolName",
+      "userBucket",
       "userType",
       "version",
       "versionBase",
@@ -50,4 +52,9 @@
       return (qA(A instanceof Error ? A : Error(String(A))), (bk1 = !1), !1);
     }
   });
+  s7z = a1(() => {
+    let A = Ry(),
+      K = Q7z("sha256").update(A).digest("hex");
+    return parseInt(K.slice(0, 8), 16) % a7z;
+  });
 });

@@@ function 'ut' (was 'Dt') — structural (71.7%)
--- pretty-v2.1.20.js:420228
+++ pretty-v2.1.21.js:420847
@@ -5,18 +5,18 @@
         "report the issue at https://github.com/anthropics/claude-code/issues",
       PACKAGE_URL: "@anthropic-ai/claude-code",
       README_URL: "https://code.claude.com/docs/en/overview",
-      VERSION: "2.1.20",
+      VERSION: "2.1.21",
       FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-      BUILD_TIME: "2026-01-27T00:38:42Z",
+      BUILD_TIME: "2026-01-28T01:36:50Z",
     }.VERSION
       ? {
           ISSUES_EXPLAINER:
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.20",
+          VERSION: "2.1.21",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-01-27T00:38:42Z",
+          BUILD_TIME: "2026-01-28T01:36:50Z",
         }.VERSION
       : "unknown",
     q = await ND2(),
@@ -40,23 +40,23 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.20",
+            VERSION: "2.1.21",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-01-27T00:38:42Z",
+            BUILD_TIME: "2026-01-28T01:36:50Z",
           }.PACKAGE_URL &&
           {
             ISSUES_EXPLAINER:
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.20",
+            VERSION: "2.1.21",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-01-27T00:38:42Z",
+            BUILD_TIME: "2026-01-28T01:36:50Z",
           }.PACKAGE_URL !== "@anthropic-ai/claude-code"
         )
-          M += ` && npm -g uninstall ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.PACKAGE_URL}`;
+          j += ` && npm -g uninstall ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.21", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T01:36:50Z" }.PACKAGE_URL}`;
         w.push({
           issue: `Leftover npm global installation at ${D.path}`,
           fix: `Run: ${M}`,
@@ -87,7 +87,7 @@
       mode: X.mode,
       systemPath: X.mode === "system" ? X.path : null,
     },
-    _ = A === "package-manager" ? BMA() : void 0;
+    _ = A === "package-manager" ? await KMA() : void 0;
   return {
     installationType: A,
     version: K,

@@@ function 'Lq1' (was 'Oq1') — structural (71.2%)
--- pretty-v2.1.20.js:160856
+++ pretty-v2.1.21.js:160905
@@ -5,7 +5,13 @@
   if (!qQ(q)) c8(q, "");
   let Y;
   try {
-    if (((Y = Hq1.default.lockSync(q)), qQ(K))) {
+    Y = aRA.default.lockSync(q);
+    let z = PH4(A);
+    if (z > 0) {
+      let w = B46(A);
+      if (z > w) MH4(A, z);
+    }
+    if (ln(K)) {
       let z = D46(K);
       for (let w of z)
         if (w.endsWith(".json") && !w.startsWith(".")) {
@@ -15,7 +21,7 @@
           } catch {}
         }
     }
-    (W46.delete(A), Jq1());
+    Cq1();
   } finally {
     if (Y) Y();
   }

@@@ function 'LQK' (was 'kFK') — structural (70.6%)
--- pretty-v2.1.20.js:574371
+++ pretty-v2.1.21.js:574575
@@ -1,6 +1,6 @@
 async function kFK() {
   (n("tengu_update_check", {}),
-    E7(`Current version: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION}
+    k7(`Current version: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.21", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T01:36:50Z" }.VERSION}
 `));
   let A = q5()?.autoUpdatesChannel ?? "latest";
   (E7(`Checking for updates to ${A} version...
@@ -75,7 +75,7 @@
       ),
       await rq(1));
   if (K.installationType === "package-manager") {
-    let X = BMA();
+    let X = await KMA();
     if (
       (E7(`
 `),
@@ -92,16 +92,16 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.20",
+            VERSION: "2.1.21",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-01-27T00:38:42Z",
+            BUILD_TIME: "2026-01-28T01:36:50Z",
           }.VERSION,
           $,
           { loose: !0 },
         )
       )
-        (E7(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION} → ${$}
+        (k7(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.21", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T01:36:50Z" }.VERSION} → ${$}
 `),
           E7(`
 `),
@@ -127,16 +127,16 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.20",
+            VERSION: "2.1.21",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-01-27T00:38:42Z",
+            BUILD_TIME: "2026-01-28T01:36:50Z",
           }.VERSION,
           $,
           { loose: !0 },
         )
       )
-        (E7(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION} → ${$}
+        (k7(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.21", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T01:36:50Z" }.VERSION} → ${$}
 `),
           E7(`
 `),
@@ -162,16 +162,16 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.20",
+            VERSION: "2.1.21",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-01-27T00:38:42Z",
+            BUILD_TIME: "2026-01-28T01:36:50Z",
           }.VERSION,
           $,
           { loose: !0 },
         )
       )
-        (E7(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION} → ${$}
+        (k7(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.21", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T01:36:50Z" }.VERSION} → ${$}
 `),
           E7(`
 `),
@@ -253,26 +253,27 @@
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.20",
+          VERSION: "2.1.21",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-01-27T00:38:42Z",
+          BUILD_TIME: "2026-01-28T01:36:50Z",
         }.VERSION
       )
         E7(
           O1.green(
-            `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION})`,
+            `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.21", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T01:36:50Z" }.VERSION})`,
           ) +
             `
 `,
         );
       else
-        E7(
+        (k7(
           O1.green(
-            `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION} to version ${X.latestVersion}`,
+            `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.21", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T01:36:50Z" }.VERSION} to version ${X.latestVersion}`,
           ) +
             `
 `,
-        );
+        ),
+          await wq6());
       await rq(0);
     } catch (X) {
       (process.stderr.write(`Error: Failed to install native update
@@ -290,10 +291,10 @@
   if (q.installMethod !== "native") await HpA();
   (h("update: Checking npm registry for latest version"),
     h(
-      `update: Package URL: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.PACKAGE_URL}`,
+      `update: Package URL: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.21", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T01:36:50Z" }.PACKAGE_URL}`,
     ));
   let Y = A === "stable" ? "stable" : "latest",
-    z = `npm view ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.PACKAGE_URL}@${Y} version`;
+    z = `npm view ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.21", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T01:36:50Z" }.PACKAGE_URL}@${Y} version`;
   h(`update: Running: ${z}`);
   let w = await Od(A);
   if ((h(`update: Latest version from npm: ${w || "FAILED"}`), !w)) {
@@ -321,18 +322,18 @@
           "report the issue at https://github.com/anthropics/claude-code/issues",
         PACKAGE_URL: "@anthropic-ai/claude-code",
         README_URL: "https://code.claude.com/docs/en/overview",
-        VERSION: "2.1.20",
+        VERSION: "2.1.21",
         FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-        BUILD_TIME: "2026-01-27T00:38:42Z",
+        BUILD_TIME: "2026-01-28T01:36:50Z",
       }.PACKAGE_URL &&
         !{
           ISSUES_EXPLAINER:
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.20",
+          VERSION: "2.1.21",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-01-27T00:38:42Z",
+          BUILD_TIME: "2026-01-28T01:36:50Z",
         }.PACKAGE_URL.startsWith("@anthropic"))
     )
       process.stderr.write(`  • Internal/development build not published to npm
@@ -351,9 +352,9 @@
           "report the issue at https://github.com/anthropics/claude-code/issues",
         PACKAGE_URL: "@anthropic-ai/claude-code",
         README_URL: "https://code.claude.com/docs/en/overview",
-        VERSION: "2.1.20",
+        VERSION: "2.1.21",
         FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-        BUILD_TIME: "2026-01-27T00:38:42Z",
+        BUILD_TIME: "2026-01-28T01:36:50Z",
       }.PACKAGE_URL || "@anthropic-ai/claude-code";
     (process.stderr.write(`  • Manually check: npm view ${X} version
 `),
@@ -368,20 +369,20 @@
         "report the issue at https://github.com/anthropics/claude-code/issues",
       PACKAGE_URL: "@anthropic-ai/claude-code",
       README_URL: "https://code.claude.com/docs/en/overview",
-      VERSION: "2.1.20",
+      VERSION: "2.1.21",
       FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-      BUILD_TIME: "2026-01-27T00:38:42Z",
+      BUILD_TIME: "2026-01-28T01:36:50Z",
     }.VERSION
   )
     (E7(
       O1.green(
-        `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION})`,
+        `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.21", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T01:36:50Z" }.VERSION})`,
       ) +
         `
 `,
     ),
       await rq(0));
-  (E7(`New version available: ${w} (current: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION})
+  (k7(`New version available: ${w} (current: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.21", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T01:36:50Z" }.VERSION})
 `),
     E7(`Installing update...
 `));
@@ -426,13 +427,14 @@
       (O = await uMA()));
   switch ((h(`update: Installation status: ${O}`), O)) {
     case "success":
-      E7(
+      (k7(
         O1.green(
-          `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION} to version ${w}`,
+          `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.21", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T01:36:50Z" }.VERSION} to version ${w}`,
         ) +
           `
 `,
-      );
+      ),
+        await wq6());
       break;
     case "no_permissions":
       if (
@@ -443,7 +445,7 @@
         (process.stderr.write(`Try manually updating with:
 `),
           process.stderr
-            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.PACKAGE_URL}
+            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.21", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T01:36:50Z" }.PACKAGE_URL}
 `));
       else
         (process.stderr.write(`Try running with sudo or fix npm permissions
@@ -462,7 +464,7 @@
         (process.stderr.write(`Try manually updating with:
 `),
           process.stderr
-            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.PACKAGE_URL}
+            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.21", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T01:36:50Z" }.PACKAGE_URL}
 `));
       else
         process.stderr

@@@ function 'UM2' (was 'NM2') — structural (69.9%)
--- pretty-v2.1.20.js:422718
+++ pretty-v2.1.21.js:423337
@@ -8,6 +8,10 @@
       toolUseContext: H,
       abortController: J,
       model: O,
+      systemPrompt: X,
+      systemPromptMode: $,
+      allowedTools: _,
+      allowPermissionPrompts: Z,
     } = A,
     { setAppState: X } = H;
   h(`[inProcessRunner] Starting agent loop for ${K.agentId}`);
@@ -21,7 +25,10 @@
       isTeamLead: !1,
       agentType: "teammate",
     },
-    Z = [
+    D;
+  if ($ === "replace" && X) D = X;
+  else {
+    let E = [
       ...(await df(
         H.options.tools,
         H.options.mainLoopModel,
@@ -30,16 +37,18 @@
       )),
       Py6,
     ];
-  if (z) {
-    let V = z.getSystemPrompt();
-    if (V)
-      Z.push(`
+    if (z) {
+      let R = z.getSystemPrompt();
+      if (R)
+        E.push(`
 # Custom Agent Instructions
 ${V}`);
+    }
+    if ($ === "append" && X) E.push(X);
+    D = E.join(`
+`);
   }
-  let G = Z.join(`
-`),
-    W = {
+  let j = {
       agentType: K.agentName,
       whenToUse: `In-process teammate: ${K.agentName}`,
       getSystemPrompt: () => G,
@@ -66,7 +75,27 @@
       $d(q, (a) => ({ ...a, currentWorkAbortController: V }), X);
       let N = q6({ content: j }),
         T = [N],
-        k = D.length > 0 ? [...D] : void 0;
+        b = M,
+        S = wI(M);
+      if (S > QP1()) {
+        h(`[inProcessRunner] ${K.agentId} compacting history (${S} tokens)`);
+        let HA = await OMA(
+          M,
+          H,
+          {
+            systemPrompt: [],
+            userContext: {},
+            systemContext: {},
+            toolUseContext: H,
+            forkContextMessages: [],
+          },
+          !0,
+          void 0,
+          !0,
+        );
+        ((b = Rt(HA)), (M.length = 0), M.push(...b));
+      }
+      let B = b.length > 0 ? [...b] : void 0;
       D.push(N);
       let R = VBA(),
         b = NBA(H.options.tools),
@@ -86,11 +115,13 @@
               toolUseContext: H,
               canUseTool: DM2(K, V),
               isAsync: !0,
-              canShowPermissionPrompts: !0,
+              canShowPermissionPrompts: Z ?? !0,
               forkContextMessages: k,
               querySource: "agent:custom",
               override: { abortController: V },
               model: O,
+              shareSetAppState: !0,
+              allowedTools: _,
             })) {
               if (J.signal.aborted) {
                 h(`[inProcessRunner] ${K.agentId} lifecycle aborted`);
@@ -122,8 +153,7 @@
                           "type" in HA &&
                           HA.type === "tool_result"
                         ) {
-                          if (JA)
-                            ((JA = new Set(JA)), JA.delete(HA.tool_use_id));
+                          if (a) ((a = new Set(a)), a.delete(jA.tool_use_id));
                         }
                     }
                   }

@@@ variable 'xd' (was 'Pd') — structural (69.2%)
--- pretty-v2.1.20.js:459209
+++ pretty-v2.1.21.js:457267
@@ -30,5 +30,6 @@
   qq();
   B1();
   cp();
+  uB();
   Tf1 = r(XA(), 1);
 });

@@@ function 'IX2' (was 'Za2') — structural (69.2%)
--- pretty-v2.1.20.js:537983
+++ pretty-v2.1.21.js:388015
@@ -1,3 +1,3 @@
 function Za2() {
-  return `${u7().BASE_API_URL}/api/claude_code/user_settings`;
+  return `${C7().BASE_API_URL}/api/claude_code/policy_limits`;
 }

@@@ variable 'Gd6' (was 'JU6') — structural (69.2%)
--- pretty-v2.1.20.js:544869
+++ pretty-v2.1.21.js:567839
@@ -4,11 +4,5 @@
   Jv();
   F9A();
   $3();
-  Y6();
-  Q9A();
-  xe();
-  GE1();
-  s0();
-  IE();
   xL = r(XA(), 1);
 });

@@@ variable 'Md6' (was 'JSK') — structural (69.2%)
--- pretty-v2.1.20.js:562921
+++ pretty-v2.1.21.js:568422
@@ -3,5 +3,6 @@
   BA();
   h3();
   Jv();
+  Z9();
   gw = r(XA(), 1);
 });

@@@ variable 'sgK' (was 'QBK') — structural (69.2%)
--- pretty-v2.1.20.js:565779
+++ pretty-v2.1.21.js:570104
@@ -3,5 +3,11 @@
   Hw();
   TS();
   r6();
+  A4();
+  uB();
+  ZH();
+  oB6();
+  Z9();
+  xB();
   Pk1 = r(XA(), 1);
 });

@@@ variable 'VFK' (was 'PgK') — structural (69.2%)
--- pretty-v2.1.20.js:571325
+++ pretty-v2.1.21.js:570957
@@ -5,10 +5,5 @@
   g8();
   c_8();
   cp6();
-  a1();
-  IK();
-  iq();
-  $q();
-  V2();
   UL = r(XA(), 1);
 });

@@@ variable 'lQK' (was 'cgK') — structural (69.2%)
--- pretty-v2.1.20.js:572098
+++ pretty-v2.1.21.js:575990
@@ -8,5 +8,9 @@
   E8();
   eN1();
   y9A();
+  mK();
+  eq();
+  d2();
+  Zq();
   FJ = r(XA(), 1);
 });

@@@ variable 'nQK' (was 'CFK') — structural (69.2%)
--- pretty-v2.1.20.js:574855
+++ pretty-v2.1.21.js:576066
@@ -4,11 +4,5 @@
   $P1();
   i6();
   Gt();
-  gS();
-  TS();
-  l5();
-  D1();
-  ZH();
-  g8();
   mk1 = r(Vy(), 1);
 });

@@@ function 'Sp6' (was 'Yp6') — structural (68.6%)
--- pretty-v2.1.20.js:559231
+++ pretty-v2.1.21.js:558110
@@ -13,25 +13,27 @@
       inputMode: _,
       inputValue: Z,
     } = A,
-    [{ queuedCommands: G, viewSelectionMode: W }] = k6(),
+    [G, W] = V6(),
     D = gyK.useCallback(() => {
       if (w !== void 0 && !w.aborted) {
         (n("tengu_cancel", {}), K(() => []), q());
         return;
       }
-      if (G.length > 0) {
+      if (G.queuedCommands.length > 0) {
         if (H) {
           H();
           return;
         }
       }
       (n("tengu_cancel", {}), K(() => []), q());
-    }, [w, G, H, K, q]),
+    }, [G, W, w, H, K, q]),
     M = RD7(),
     j = w !== void 0 && !w.aborted,
-    P = G.length > 0,
+    P = G.queuedCommands.length > 0,
     V = !1,
     N = _ !== void 0 && _ !== "prompt" && !Z,
+    T = !1,
+    E = G.viewSelectionMode === "viewing-agent",
     k =
       z !== "transcript" &&
       !X &&
@@ -39,11 +41,11 @@
       !O &&
       !$ &&
       !M &&
-      W !== "viewing-agent" &&
+      !E &&
       !(it() && J === "INSERT") &&
-      (j || P || !1),
+      (M || P || !1 || T),
     R = k && !N,
-    b = k;
+    S = T || R;
   return (
     s1("chat:cancel", D, { context: "Chat", isActive: R }),
     s1("app:interrupt", D, { context: "Global", isActive: b }),

@@@ function 'e76' (was 'XQ') — structural (67.7%)
--- pretty-v2.1.20.js:176292
+++ pretty-v2.1.21.js:176384
@@ -1,12 +1,6 @@
 function XQ(A, K, q) {
   if (K < 0 || q < 0 || K >= A.width || q >= A.height) return;
   let Y = q * A.width + K,
-    z = A.chars[Y],
-    w = A.styleIds[Y];
-  return {
-    char: A.charStrings[z] ?? " ",
-    styleId: w === QOA ? A.emptyStyleId : w,
-    width: A.widths[Y],
-    hyperlink: Oa3(A, A.hyperlinkIds[Y]),
-  };
+    z = A.chars[Y];
+  return A.charStrings[z] ?? " ";
 }

@@@ variable 'UXK' (was 'KXK') — structural (67.0%)
--- pretty-v2.1.20.js:475787
+++ pretty-v2.1.21.js:474550
@@ -1,6 +1,7 @@
 var KXK = C(() => {
   du6();
   r6();
+  PS();
   lu6 = r(XA(), 1);
   ((_S2 = {
     aliases: ["bug"],
@@ -15,7 +16,9 @@
         N1(process.env.CLAUDE_CODE_USE_FOUNDRY) ||
         process.env.DISABLE_FEEDBACK_COMMAND ||
         process.env.DISABLE_BUG_COMMAND ||
-        process.env.CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC
+        process.env.CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC ||
+        !1 ||
+        !YP("allow_product_feedback")
       ),
     isHidden: !1,
     async call(A, { abortController: K, messages: q }, Y) {

@@@ variable 'U6K' (was 'd1K') — structural (66.7%)
--- pretty-v2.1.20.js:400334
+++ pretty-v2.1.21.js:400937
@@ -14,6 +14,7 @@
               X5A(),
               p1K(EZ2()),
               wa7(),
+              Ys7(),
               K.setAppState((Y) => ({ ...Y, authVersion: Y.authVersion + 1 })));
           A(q ? "Login successful" : "Login interrupted");
         },

@@@ variable 'Mf1' (was 'Xf1') — structural (66.7%)
--- pretty-v2.1.20.js:455056
+++ pretty-v2.1.21.js:452954
@@ -9,30 +9,5 @@
   $b6();
   _j();
   d0();
-  ZV();
-  jd();
-  Gz();
-  r6();
-  qq();
-  P8();
-  Ta();
-  Rb6();
-  Y6();
-  H7();
-  P_1();
-  Tk();
-  $z();
-  m4();
-  YUA();
-  QFA();
-  Aw();
-  i6();
-  Zz();
-  SB();
-  g8();
-  cO();
-  R1();
-  aj();
-  Of1();
   GUA = new Map();
 });

@@@ variable 'CQK' (was 'EFK') — structural (66.7%)
--- pretty-v2.1.20.js:574304
+++ pretty-v2.1.21.js:574506
@@ -63,5 +63,7 @@
   oH();
   Vv();
   r0();
+  Tv();
+  TJ();
   NFK = new Set();
 });

@@@ variable 'aO' (was 's0') — structural (66.3%)
--- pretty-v2.1.20.js:192920
+++ pretty-v2.1.21.js:193260
@@ -38,9 +38,9 @@
         "report the issue at https://github.com/anthropics/claude-code/issues",
       PACKAGE_URL: "@anthropic-ai/claude-code",
       README_URL: "https://code.claude.com/docs/en/overview",
-      VERSION: "2.1.20",
+      VERSION: "2.1.21",
       FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-      BUILD_TIME: "2026-01-27T00:38:42Z",
+      BUILD_TIME: "2026-01-28T01:36:50Z",
     }.VERSION.match(/^\d+\.\d+\.\d+(?:-[a-z]+)?/);
     return A ? A[0] : void 0;
   })),
@@ -66,6 +66,7 @@
           remoteEnvironmentType:
             process.env.CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE,
         }),
+        ...{},
         ...(process.env.CLAUDE_CODE_CONTAINER_ID && {
           claudeCodeContainerId: process.env.CLAUDE_CODE_CONTAINER_ID,
         }),
@@ -83,9 +84,9 @@
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.20",
+          VERSION: "2.1.21",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-01-27T00:38:42Z",
+          BUILD_TIME: "2026-01-28T01:36:50Z",
         }.VERSION,
         versionBase: f$9(),
         buildTime: {
@@ -93,9 +94,9 @@
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.20",
+          VERSION: "2.1.21",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-01-27T00:38:42Z",
+          BUILD_TIME: "2026-01-28T01:36:50Z",
         }.BUILD_TIME,
         deploymentEnvironment: p6.detectDeploymentEnvironment(),
         ...(N1(process.env.GITHUB_ACTIONS) && {

@@@ variable 'Z_' (was 'W_') — structural (66.2%)
--- pretty-v2.1.20.js:448699
+++ pretty-v2.1.21.js:449364
@@ -56,6 +56,7 @@
       wW,
       oG,
       yFA,
+      ...[],
       tQA,
     ])),
     (l2K = new Set([yFA, tQA, Ro, bV1, xV1, SU, j5])));

@@@ function 'jqz' (was 'a7z') — structural (65.8%)
--- pretty-v2.1.20.js:577044
+++ pretty-v2.1.21.js:577256
@@ -19,6 +19,7 @@
         U7z(),
         XK("preAction_after_migrations"),
         za7(),
+        qs7(),
         XK("preAction_after_remote_settings"),
         XK("preAction_after_settings_sync"));
     }),
@@ -64,7 +65,7 @@
       .addOption(
         new P3(
           "--init-only",
-          "Run Setup hooks with init trigger, then exit",
+          "Run Setup and SessionStart:startup hooks, then exit",
         ).hideHelp(),
       )
       .addOption(
@@ -786,7 +787,8 @@
           I8;
         if (bt())
           ((I8 = new Xd6(MK, xK)),
-            I8.start()
+            d8
+              .start()
               .then(({ url: W6 }) => {
                 let R4 = I8.getSecret();
                 (ePA({ url: W6, key: R4 }),
@@ -848,7 +850,7 @@
         ac(uK);
         let jK = l || a ? "init" : e ? "maintenance" : null;
         if (l) {
-          (Re(), await jf1("init", !0), H5(0));
+          (ie(), await kf1("init", !0), await Wj("startup"), A5(0));
           return;
         }
         if ($A) {
@@ -1099,6 +1101,13 @@
             }
           }
           if (AA !== null) {
+            if ((await CL6(), !YP("allow_remote_sessions")))
+              (process.stderr.write(
+                O1.red(`Error: Remote sessions are disabled by your organization's policy.
+`),
+              ),
+                await Eq(1),
+                process.exit(1));
             let _4 = AA.length > 0,
               A8 = i4("tengu_remote_backend", !1);
             if (!A8 && !_4)
@@ -1186,6 +1195,13 @@
               AYA());
             return;
           } else if (KA) {
+            if ((await CL6(), !YP("allow_remote_sessions")))
+              (process.stderr.write(
+                O1.red(`Error: Remote sessions are disabled by your organization's policy.
+`),
+              ),
+                await Eq(1),
+                process.exit(1));
             if (KA === !0 || KA === "") {
               n("tengu_teleport_interactive_mode", {});
               let _4 = await nFK();
@@ -1409,7 +1425,7 @@
         }
       })
       .version(
-        `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION} (Claude Code)`,
+        `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.21", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T01:36:50Z" }.VERSION} (Claude Code)`,
         "-v, --version",
         "Output the version number",
       ),
@@ -1798,13 +1814,17 @@
           X = jPA(),
           $ = Object.keys(O.plugins);
         if (J.json) {
-          let { enabled: _, disabled: Z } = await q2(),
+          let { enabled: Z, disabled: G, errors: W } = await bY(),
             G = [..._, ...Z],
             W = new Map(G.map((M) => [M.source, M])),
             D = [];
           for (let M of $.sort()) {
             let j = O.plugins[M];
             if (!j || j.length === 0) continue;
+            let N = P.split("@")[0],
+              T = W.filter(
+                (E) => E.source === P || ("plugin" in E && E.plugin === N),
+              ).map(JM);
             for (let P of j) {
               let V = W.get(M),
                 N;
@@ -1822,6 +1842,7 @@
                 lastUpdated: P.lastUpdated,
                 projectPath: P.projectPath,
                 mcpServers: N,
+                errors: T.length > 0 ? T : void 0,
               });
             }
           }
@@ -1855,20 +1876,32 @@
             "No plugins installed. Use `claude plugin install` to install a plugin.",
           ),
             process.exit(0));
+        let { errors: _ } = await bY();
         console.log(`Installed plugins:
 `);
         for (let _ of $.sort()) {
           let Z = O.plugins[_];
           if (!Z || Z.length === 0) continue;
+          let W = Z.split("@")[0],
+            D = _.filter(
+              (j) => j.source === Z || ("plugin" in j && j.plugin === W),
+            );
           for (let G of Z) {
-            let D = X.has(_) ? `${K1.tick} enabled` : `${K1.cross} disabled`,
+            let M = X.has(Z),
+              P =
+                D.length > 0
+                  ? `${q1.cross} failed to load`
+                  : M
+                    ? `${q1.tick} enabled`
+                    : `${q1.cross} disabled`,
               M = G.version || "unknown",
               j = G.scope;
             (console.log(`  ${K1.pointer} ${_}`),
               console.log(`    Version: ${M}`),
               console.log(`    Scope: ${j}`),
-              console.log(`    Status: ${D}`),
-              console.log(""));
+              console.log(`    Status: ${P}`));
+            for (let T of D) console.log(`    Error: ${JM(T)}`);
+            console.log("");
           }
         }
         process.exit(0);
@@ -2214,12 +2247,16 @@
                 null,
                 Zq.default.createElement(
                   $T1,
-                  { dynamicMcpConfig: void 0, isStrictMcpConfig: !1 },
-                  Zq.default.createElement(H, {
-                    onDone: () => {
-                      (O(), J());
-                    },
-                  }),
+                  null,
+                  eK.default.createElement(
+                    kT1,
+                    { dynamicMcpConfig: void 0, isStrictMcpConfig: !1 },
+                    eK.default.createElement(H, {
+                      onDone: () => {
+                        (O(), J());
+                      },
+                    }),
+                  ),
                 ),
               ),
               Sw(!1),

@@@ function 'XP1' (was 'Uj1') — structural (65.1%)
--- pretty-v2.1.20.js:415021
+++ pretty-v2.1.21.js:415643
@@ -11,7 +11,8 @@
         (z = J.identity.agentId),
         J.abortController.abort(),
         J.unregisterCleanup?.(),
-        (q = !0));
+        (q = !0),
+        J.onIdleCallbacks?.forEach((X) => X()));
       let O = w.teamContext;
       if (w.teamContext && w.teamContext.teammates && z) {
         let { [z]: X, ...$ } = w.teamContext.teammates;
@@ -22,7 +23,12 @@
         teamContext: O,
         tasks: {
           ...w.tasks,
-          [A]: { ...J, status: "killed", endTime: Date.now() },
+          [A]: {
+            ...J,
+            status: "killed",
+            endTime: Date.now(),
+            onIdleCallbacks: [],
+          },
         },
       };
     }),

@@@ function 'jzK' (was 'f2K') — structural (64.4%)
--- pretty-v2.1.20.js:447779
+++ pretty-v2.1.21.js:448442
@@ -13,8 +13,9 @@
 When working as a teammate:
 1. After completing your current task, call TaskList to find available work
 2. Look for tasks with status 'pending', no owner, and empty blockedBy
-3. Use claimTask to claim an available task, or wait for leader assignment
-4. If blocked, focus on unblocking tasks or notify the team lead
+3. **Prefer tasks in ID order** (lowest ID first) when multiple tasks are available, as earlier tasks often set up context for later ones
+4. Use claimTask to claim an available task, or wait for leader assignment
+5. If blocked, focus on unblocking tasks or notify the team lead
 `
       : "";
   return `Use this tool to list all tasks in the task list.
@@ -25,6 +26,7 @@
 - To check overall progress on the project
 - To find tasks that are blocked and need dependencies resolved
 ${A}- After completing a task, to check for newly unblocked work or claim the next available task
+- **Prefer working on tasks in ID order** (lowest ID first) when multiple tasks are available, as earlier tasks often set up context for later ones
 
 ## Output

@@@ function 'Nq1' (was 'Kq1') — structural (63.6%)
--- pretty-v2.1.20.js:160433
+++ pretty-v2.1.21.js:160465
@@ -1,7 +1,7 @@
 function Kq1(A) {
   if (!Gr3()) return "";
-  let K = `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION}.${A}`,
+  let K = `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.21", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T01:36:50Z" }.VERSION}.${A}`,
     q = process.env.CLAUDE_CODE_ENTRYPOINT ?? "unknown",
-    Y = `x-anthropic-billing-header: cc_version=${K}; cc_entrypoint=${q}`;
+    Y = `x-anthropic-billing-header: cc_version=${K}; cc_entrypoint=${q};`;
   return (h(`attribution header ${Y}`), Y);
 }

@@@ function 'r7z' (was 'h4z') — structural (63.6%)
--- pretty-v2.1.20.js:571502
+++ pretty-v2.1.21.js:571044
@@ -2,5 +2,5 @@
   if (Gc) return;
   Gc = setTimeout(() => {
     ((Gc = null), lp6());
-  }, L4z).unref();
+  }, t7z()).unref();
 }

@@@ variable 'mj1' (was 'DM1') — structural (63.0%)
--- pretty-v2.1.20.js:387702
+++ pretty-v2.1.21.js:388303
@@ -5,5 +5,6 @@
       Yr.cache?.clear?.(),
       Xa7(),
       Ts.cache?.clear?.(),
+      fL6(),
       tC6());
   },

@@@ function 'rMA' (was 'SjA') — structural (62.9%)
--- pretty-v2.1.20.js:461555
+++ pretty-v2.1.21.js:459615
@@ -1,5 +1,5 @@
 function SjA() {
   let A = W3(),
-    K = Mx6(A);
+    K = Math.min(Sx6(A), PL2);
   return rW(A, lP()) - K;
 }

@@@ function 'Kh7' (was 'QF6') — structural (61.5%)
--- pretty-v2.1.20.js:528969
+++ pretty-v2.1.21.js:344967
@@ -1,3 +1,3 @@
 function QF6() {
-  (cf.cache?.clear?.(), fS.cache?.clear?.(), bP1.cache?.clear?.());
+  (Ah7.cache?.clear?.(), Qp.cache?.clear?.());
 }

@@@ function 'eO4' (was 'G04') — structural (61.4%)
--- pretty-v2.1.20.js:176935
+++ pretty-v2.1.21.js:177129
@@ -1,7 +1,9 @@
 function G04(A, K, q) {
   A.txn((Y) => {
-    let z = K.width === 1 ? 2 : 1,
-      w = Y.x >= A.viewportWidth ? z - Y.x : z,
+    let z = K.width === 1 ? 2 : 1;
+    if (z === 2 && Y.x < A.viewportWidth && Y.x + 2 >= A.viewportWidth)
+      return [[], { dx: 0, dy: 0 }];
+    let w = Y.x >= A.viewportWidth ? z - Y.x : z,
       H = Y.x >= A.viewportWidth ? 1 : 0;
     return [
       q.length > 0

@@@ function 'bi2' (was 'Rl2') — structural (60.0%)
--- pretty-v2.1.20.js:525993
+++ pretty-v2.1.21.js:523995
@@ -1,5 +1,5 @@
 function Rl2(A) {
-  let K = s(22),
+  let K = s(21),
     { onDone: q, context: Y } = A,
     [z, w] = sfK.useState(null),
     H = vo(),
@@ -14,25 +14,16 @@
   else X = K[1];
   let $ = X,
     _ = g5()?.hasExtraUsageEnabled === !0,
-    Z = O === "pro",
-    G = O === "max",
-    W = G && $ === "default_claude_max_20x",
+    G = O === "max" && $ === "default_claude_max_20x",
     D = O === "team" || O === "enterprise",
     M;
   if (K[2] === Symbol.for("react.memo_cache_sentinel"))
-    ((M =
-      (Z || G) && UG1("hide_overages_option_at_rate_limit_hit", "enabled", !1)),
+    ((D = { label: "Stop and wait for limit to reset", value: "cancel" }),
       (K[2] = M));
   else M = K[2];
-  let j = M,
-    P;
-  if (K[3] === Symbol.for("react.memo_cache_sentinel"))
-    ((P = { label: "Stop and wait for limit to reset", value: "cancel" }),
-      (K[3] = P));
-  else P = K[3];
   let V;
-  if (K[4] !== H.overageDisabledReason || K[5] !== H.overageStatus) {
-    if (((V = [P]), !j && ep.isEnabled())) {
+  if (K[3] !== H.overageDisabledReason || K[4] !== H.overageStatus) {
+    if (((j = [D]), $d.isEnabled())) {
       let x = _u(),
         F = D && !x,
         Q =
@@ -51,34 +42,34 @@
             ? "Add funds to continue with extra usage"
             : "Switch to extra usage";
         let a;
-        if (K[7] !== d)
-          ((a = { label: d, value: "extra-usage" }), (K[7] = d), (K[8] = a));
-        else a = K[8];
+        if (K[6] !== F)
+          ((Q = { label: F, value: "extra-usage" }), (K[6] = F), (K[7] = Q));
+        else Q = K[7];
         V.push(a);
       }
     }
     if (!W && !D && TdA.isEnabled()) {
       let x;
-      if (K[9] === Symbol.for("react.memo_cache_sentinel"))
-        ((x = { label: "Upgrade your plan", value: "upgrade" }), (K[9] = x));
-      else x = K[9];
+      if (K[8] === Symbol.for("react.memo_cache_sentinel"))
+        ((b = { label: "Upgrade your plan", value: "upgrade" }), (K[8] = b));
+      else b = K[8];
       V.push(x);
     }
-    ((K[4] = H.overageDisabledReason), (K[5] = H.overageStatus), (K[6] = V));
-  } else V = K[6];
+    ((K[3] = H.overageDisabledReason), (K[4] = H.overageStatus), (K[5] = j));
+  } else j = K[5];
   let N = V,
     T;
-  if (K[10] !== q)
+  if (K[9] !== q)
     ((T = function () {
       (n("tengu_rate_limit_options_menu_cancel", {}),
         q(void 0, { display: "skip" }));
     }),
-      (K[10] = q),
-      (K[11] = T));
-  else T = K[11];
+      (K[9] = q),
+      (K[10] = P));
+  else P = K[10];
   let k = T,
     R;
-  if (K[12] !== Y || K[13] !== k || K[14] !== q)
+  if (K[11] !== Y || K[12] !== V || K[13] !== q)
     ((R = function (F) {
       if (F === "upgrade")
         (n("tengu_rate_limit_options_menu_select_upgrade", {}),
@@ -92,26 +83,26 @@
           }));
       else if (F === "cancel") k();
     }),
+      (K[11] = Y),
       (K[12] = Y),
       (K[13] = k),
-      (K[14] = q),
-      (K[15] = R));
-  else R = K[15];
+      (K[14] = N));
+  else N = K[14];
   let b = R;
   if (z) return z;
   let S;
-  if (K[16] !== b || K[17] !== N)
+  if (K[15] !== T || K[16] !== M)
     ((S = Cv1.default.createElement(y6, {
       options: N,
       onChange: b,
       visibleOptionCount: N.length,
     })),
+      (K[15] = T),
       (K[16] = b),
-      (K[17] = N),
-      (K[18] = S));
-  else S = K[18];
+      (K[17] = E));
+  else E = K[17];
   let B;
-  if (K[19] !== k || K[20] !== S)
+  if (K[18] !== V || K[19] !== E)
     ((B = Cv1.default.createElement(
       b7,
       {
@@ -122,9 +113,9 @@
       },
       S,
     )),
+      (K[18] = V),
       (K[19] = k),
-      (K[20] = S),
-      (K[21] = B));
-  else B = K[21];
+      (K[20] = R));
+  else R = K[20];
   return B;
 }

@@@ variable 'ZH' — structural (59.8%)
--- pretty-v2.1.20.js:471023
+++ pretty-v2.1.21.js:469778
@@ -9,6 +9,7 @@
   BM();
   Y6();
   qq();
+  UK();
   I0K = K6(() => {
     if (
       (process.on("SIGINT", () => {
@@ -23,17 +24,25 @@
         (L8("info", "shutdown_signal", { signal: "SIGHUP" }), rq(129));
       });
     (process.on("uncaughtException", (A) => {
-      L8("error", "uncaught_exception", {
+      (E8("error", "uncaught_exception", {
         error_name: A.name,
         error_message: A.message.slice(0, 2000),
-      });
+      }),
+        n("tengu_uncaught_exception", { error_name: A.name }));
     }),
       process.on("unhandledRejection", (A) => {
         let K =
-          A instanceof Error
-            ? { error_name: A.name, error_message: A.message.slice(0, 2000) }
-            : { error_message: String(A).slice(0, 2000) };
-        L8("error", "unhandled_rejection", K);
+            A instanceof Error
+              ? A.name
+              : typeof A === "string"
+                ? "string"
+                : "unknown",
+          q =
+            A instanceof Error
+              ? { error_name: A.name, error_message: A.message.slice(0, 2000) }
+              : { error_message: String(A).slice(0, 2000) };
+        (E8("error", "unhandled_rejection", q),
+          n("tengu_unhandled_rejection", { error_name: K }));
       }));
   });
 });

@@@ function '$jA' (was 'XM1') — structural (59.6%)
--- pretty-v2.1.20.js:386433
+++ pretty-v2.1.21.js:386720
@@ -1,5 +1,5 @@
 function XM1(A) {
-  let K = s(36),
+  let K = s(40),
     {
       isDisabled: q,
       visibleOptionCount: Y,
@@ -12,7 +12,10 @@
       submitButtonText: $,
       onSubmit: _,
       onDownFromLastItem: Z,
+      onUpFromFirstItem: G,
+      initialFocusLast: W,
       onOpenEditor: G,
+      hideIndexes: j,
     } = A,
     W = q === void 0 ? !1 : q,
     D = Y === void 0 ? 5 : Y,
@@ -20,6 +23,7 @@
   if (K[0] !== w) ((M = w === void 0 ? [] : w), (K[0] = w), (K[1] = M));
   else M = K[1];
   let j = M,
+    T = j === void 0 ? !1 : j,
     P;
   if (
     K[2] !== j ||
@@ -32,7 +36,9 @@
     K[9] !== _ ||
     K[10] !== z ||
     K[11] !== $ ||
-    K[12] !== D
+    K[12] !== z ||
+    K[13] !== $ ||
+    K[14] !== P
   )
     ((P = {
       isDisabled: W,
@@ -46,6 +52,8 @@
       submitButtonText: $,
       onSubmit: _,
       onDownFromLastItem: Z,
+      onUpFromFirstItem: G,
+      initialFocusLast: W,
     }),
       (K[2] = j),
       (K[3] = X),
@@ -58,22 +66,31 @@
       (K[10] = z),
       (K[11] = $),
       (K[12] = D),
-      (K[13] = P));
-  else P = K[13];
+      (K[13] = $),
+      (K[14] = P),
+      (K[15] = E));
+  else E = K[15];
   let V = co7(P),
     N,
     T,
     k,
     R,
     b;
-  if (K[14] !== H || K[15] !== G || K[16] !== z.length || K[17] !== V) {
+  if (
+    K[16] !== T ||
+    K[17] !== M ||
+    K[18] !== H ||
+    K[19] !== D ||
+    K[20] !== z.length ||
+    K[21] !== R
+  ) {
     let F = z.length.toString().length;
     ((T = I),
       (b = "column"),
       (N = I),
       (k = "column"),
       (R = V.visibleOptions.map((Q, u) => {
-        let d = V.focusedValue === Q.value && !V.isSubmitFocused,
+        let wA = !M && R.focusedValue === l.value && !R.isSubmitFocused,
           a = V.selectedValues.includes(Q.value),
           l = Q.index === V.visibleFromIndex,
           e = Q.index === V.visibleToIndex - 1,
@@ -129,10 +146,11 @@
               shouldShowUpArrow: OA && l,
               description: Q.description,
             },
-            wM.default.createElement(f, { dimColor: !0 }, `${HA}.`.padEnd(F)),
+            !T &&
+              wj.default.createElement(f, { dimColor: !0 }, `${jA}.`.padEnd(o)),
             wM.default.createElement(
               f,
-              { color: a ? "success" : void 0 },
+              { color: !T && HA ? "success" : void 0 },
               "[",
               a ? K1.tick : " ",
               "]",
@@ -145,26 +163,28 @@
           ),
         );
       })),
-      (K[14] = H),
-      (K[15] = G),
-      (K[16] = z.length),
+      (K[16] = T),
       (K[17] = V),
       (K[18] = N),
       (K[19] = T),
-      (K[20] = k),
+      (K[20] = z.length),
       (K[21] = R),
-      (K[22] = b));
-  } else ((N = K[18]), (T = K[19]), (k = K[20]), (R = K[21]), (b = K[22]));
-  let S;
-  if (K[23] !== N || K[24] !== k || K[25] !== R)
-    ((S = wM.default.createElement(N, { flexDirection: k }, R)),
+      (K[22] = b),
       (K[23] = N),
       (K[24] = k),
       (K[25] = R),
       (K[26] = S));
-  else S = K[26];
+  } else ((b = K[22]), (S = K[23]), (B = K[24]), (x = K[25]), (F = K[26]));
   let B;
-  if (K[27] !== _ || K[28] !== V.isSubmitFocused || K[29] !== $)
+  if (K[27] !== b || K[28] !== B || K[29] !== x)
+    ((Q = wj.default.createElement(b, { flexDirection: B }, x)),
+      (K[27] = b),
+      (K[28] = B),
+      (K[29] = x),
+      (K[30] = Q));
+  else Q = K[30];
+  let u;
+  if (K[31] !== _ || K[32] !== R.isSubmitFocused || K[33] !== $)
     ((B =
       $ &&
       _ &&
@@ -184,19 +204,19 @@
           ),
         ),
       )),
-      (K[27] = _),
-      (K[28] = V.isSubmitFocused),
-      (K[29] = $),
-      (K[30] = B));
-  else B = K[30];
+      (K[31] = _),
+      (K[32] = R.isSubmitFocused),
+      (K[33] = $),
+      (K[34] = u));
+  else u = K[34];
   let x;
-  if (K[31] !== T || K[32] !== B || K[33] !== b || K[34] !== S)
+  if (K[35] !== S || K[36] !== Q || K[37] !== u || K[38] !== F)
     ((x = wM.default.createElement(T, { flexDirection: b }, S, B)),
-      (K[31] = T),
-      (K[32] = B),
-      (K[33] = b),
-      (K[34] = S),
-      (K[35] = x));
-  else x = K[35];
+      (K[35] = S),
+      (K[36] = Q),
+      (K[37] = u),
+      (K[38] = F),
+      (K[39] = d));
+  else d = K[39];
   return x;
 }

@@@ function 'xRK' (was 'rLK') — structural (59.5%)
--- pretty-v2.1.20.js:553127
+++ pretty-v2.1.21.js:551948
@@ -1,13 +1,22 @@
 async function rLK() {
   if (!(await aW())) return null;
+  let [K, q] = await Promise.all([RN(), fE()]);
+  if (K === q) return null;
   let { stdout: K, code: q } = await u6(
     "gh",
-    ["pr", "view", "--json", "number,url,reviewDecision,isDraft"],
+    ["pr", "view", "--json", "number,url,reviewDecision,isDraft,headRefName"],
     { timeout: MAz, preserveOutputOnError: !1 },
   );
   if (q !== 0 || !K.trim()) return null;
   try {
-    let Y = G6(K);
+    let w = X6(Y),
+      H = await fE();
+    if (
+      w.headRefName === H ||
+      w.headRefName === "main" ||
+      w.headRefName === "master"
+    )
+      return null;
     return {
       number: Y.number,
       url: Y.url,

@@@ function 'NcA' (was '_UA') — structural (59.1%)
--- pretty-v2.1.20.js:452927
+++ pretty-v2.1.21.js:544754
@@ -1,5 +1,5 @@
 function _UA(A) {
-  let K = s(17),
+  let K = s(13),
     { issue: q, branchName: Y, onDone: z, color: w, loadingState: H } = A,
     J = w === void 0 ? "permission" : w,
     { hasUncommitted: O, hasUnpushed: X } = q,
@@ -20,81 +20,53 @@
     W =
       H === "committing" ? "Committing…" : H === "pushing" ? "Pushing…" : null,
     D;
-  if (K[2] !== J)
-    ((D = _X.createElement(
-      I,
-      { paddingX: 1 },
-      _X.createElement(
-        f,
-        { color: J, bold: !0 },
-        "Include local changes in the remote task?",
-      ),
-    )),
-      (K[2] = J),
-      (K[3] = D));
+  if (K[2] !== Z) ((D = () => Z("cancel")), (K[2] = Z), (K[3] = D));
   else D = K[3];
   let M;
-  if (K[4] !== $)
-    ((M = _X.createElement(f, { dimColor: !0 }, $)), (K[4] = $), (K[5] = M));
-  else M = K[5];
+  if (K[4] !== G || K[5] !== Z || K[6] !== W)
+    ((j = W
+      ? wh.createElement(
+          I,
+          { flexDirection: "row" },
+          wh.createElement(Q7, null),
+          wh.createElement(f, null, W),
+        )
+      : wh.createElement(k6, {
+          options: [
+            { label: G, value: "commit-push" },
+            {
+              label: "Run remote task without my local changes",
+              value: "continue",
+            },
+            { label: "Cancel", value: "cancel" },
+          ],
+          onChange: Z,
+          onCancel: () => Z("cancel"),
+          layout: "compact-vertical",
+        })),
+      (K[4] = G),
+      (K[5] = Z),
+      (K[6] = W),
+      (K[7] = j));
+  else j = K[7];
   let j;
-  if (K[6] !== G || K[7] !== Z || K[8] !== W)
+  if (K[8] !== J || K[9] !== $ || K[10] !== D || K[11] !== j)
     ((j = _X.createElement(
       I,
-      { marginTop: 1 },
-      W
-        ? _X.createElement(
-            I,
-            { flexDirection: "row" },
-            _X.createElement(Q7, null),
-            _X.createElement(f, null, W),
-          )
-        : _X.createElement(y6, {
-            options: [
-              { label: G, value: "commit-push" },
-              {
-                label: "Run remote task without my local changes",
-                value: "continue",
-              },
-              { label: "Cancel", value: "cancel" },
-            ],
-            onChange: Z,
-            onCancel: () => Z("cancel"),
-            layout: "compact-vertical",
-          }),
+      {
+        title: "Include local changes in the remote task?",
+        subtitle: $,
+        color: J,
+        onCancel: D,
+        hideInputGuide: !0,
+      },
+      j,
     )),
-      (K[6] = G),
-      (K[7] = Z),
       (K[8] = W),
-      (K[9] = j));
-  else j = K[9];
-  let P;
-  if (K[10] !== M || K[11] !== j)
-    ((P = _X.createElement(I, { flexDirection: "column", paddingX: 1 }, M, j)),
+      (K[9] = $),
       (K[10] = M),
       (K[11] = j),
       (K[12] = P));
   else P = K[12];
-  let V;
-  if (K[13] !== J || K[14] !== D || K[15] !== P)
-    ((V = _X.createElement(
-      I,
-      {
-        flexDirection: "column",
-        borderStyle: "round",
-        borderColor: J,
-        borderLeft: !1,
-        borderRight: !1,
-        borderBottom: !1,
-        marginTop: 1,
-      },
-      D,
-      P,
-    )),
-      (K[13] = J),
-      (K[14] = D),
-      (K[15] = P),
-      (K[16] = V));
-  else V = K[16];
   return V;
 }

@@@ variable 'gs' (was 'qB') — structural (58.8%)
--- pretty-v2.1.20.js:344716
+++ pretty-v2.1.21.js:345006
@@ -10,7 +10,7 @@
   s0();
   WQ();
   B1();
-  ((FG1 = r(JS7(), 1)), (SaY = {}));
+  XW1 = r(aS7(), 1);
   ((QG1 = K6(() => {
     if (tX()) return null;
     return haY(sZ8);
@@ -20,12 +20,4 @@
       if (!A) return null;
       return (await A.initialized, A.client);
     })));
-  baY = K6(async (A) => {
-    if (tX()) return !1;
-    let K = QG1();
-    if (!K) return !1;
-    await K.initialized;
-    let q = K.client.checkGate(A);
-    return ((SaY[A] = q), q);
-  });
 });

@@@ variable 'xb6' (was 'ZI6') — structural (57.9%)
--- pretty-v2.1.20.js:422945
+++ pretty-v2.1.21.js:450791
@@ -20,4 +20,6 @@
   yH();
   P8();
   P3A();
+  Of1();
+  YwK();
 });

@@@ variable 'ML' (was 'iQ6') — structural (57.9%)
--- pretty-v2.1.20.js:539354
+++ pretty-v2.1.21.js:464041
@@ -8,4 +8,5 @@
   F4A();
   Y6();
   ED();
+  pQA();
 });

@@@ variable 'pT1' (was 'lgK') — structural (57.9%)
--- pretty-v2.1.20.js:572178
+++ pretty-v2.1.21.js:496143
@@ -10,4 +10,5 @@
   m4();
   R1();
   ndA();
+  B8();
 });

@@@ variable 'up6' (was 'ZFK') — structural (57.9%)
--- pretty-v2.1.20.js:572989
+++ pretty-v2.1.21.js:559581
@@ -1,4 +1,16 @@
 var ZFK = C(() => {
   D1();
   ZH();
+  aT();
+  j8();
+  zP();
+  iIK();
+  oIK();
+  qP1();
+  sIK();
+  cx();
+  i1();
+  UMA();
+  s1();
+  UjA();
 });

@@@ variable 'tFK' (was 'aFK') — structural (57.9%)
--- pretty-v2.1.20.js:576168
+++ pretty-v2.1.21.js:571835
@@ -2,6 +2,4 @@
   Uj();
   Z_();
   r6();
-  B1();
-  a1();
 });

@@@ function 'GLK' (was 'LCK') — structural (56.4%)
--- pretty-v2.1.20.js:549456
+++ pretty-v2.1.21.js:548268
@@ -1,14 +1,18 @@
 function LCK(A) {
-  let K = s(8),
+  let K = s(10),
     { verbose: q } = A,
     [Y, z] = CCK.useState(!1),
-    w = BMA(),
+    [w, H] = nU6.useState("unknown"),
     H;
   if (K[0] === Symbol.for("react.memo_cache_sentinel"))
     ((H = async () => {
       if (td()) return;
-      let W = q5()?.autoUpdatesChannel ?? "latest",
-        D = await Od(W),
+      let [D, j] = await Promise.all([
+        Promise.resolve(oq()?.autoUpdatesChannel ?? "latest"),
+        KMA(),
+      ]);
+      H(j);
+      let M = await fd(D),
         M =
           D &&
           !kCK.gte(
@@ -17,10 +21,10 @@
                 "report the issue at https://github.com/anthropics/claude-code/issues",
               PACKAGE_URL: "@anthropic-ai/claude-code",
               README_URL: "https://code.claude.com/docs/en/overview",
-              VERSION: "2.1.20",
+              VERSION: "2.1.21",
               FEEDBACK_CHANNEL:
                 "https://github.com/anthropics/claude-code/issues",
-              BUILD_TIME: "2026-01-27T00:38:42Z",
+              BUILD_TIME: "2026-01-28T01:36:50Z",
             }.VERSION,
             D,
             { loose: !0 },
@@ -28,7 +32,7 @@
           !xMA(D);
       if ((z(!!M), M))
         h(
-          `PackageManagerAutoUpdater: Update available ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.20", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-27T00:38:42Z" }.VERSION} -> ${D}`,
+          `PackageManagerAutoUpdater: Update available ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.21", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T01:36:50Z" }.VERSION} -> ${M}`,
         );
     }),
       (K[0] = H));
@@ -66,27 +70,31 @@
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.20",
+          VERSION: "2.1.21",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-01-27T00:38:42Z",
+          BUILD_TIME: "2026-01-28T01:36:50Z",
         }.VERSION,
       )),
       (K[3] = q),
       (K[4] = _));
   else _ = K[4];
   let Z;
-  if (K[5] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[5] !== _)
     ((Z = ON.createElement(
       f,
       { color: "warning" },
       "Update available! Run: ",
       ON.createElement(f, { bold: !0 }, $),
     )),
-      (K[5] = Z));
-  else Z = K[5];
+      (K[5] = _),
+      (K[6] = G));
+  else G = K[6];
   let G;
-  if (K[6] !== _)
-    ((G = ON.createElement(ON.Fragment, null, _, Z)), (K[6] = _), (K[7] = G));
-  else G = K[7];
+  if (K[7] !== Z || K[8] !== G)
+    ((W = XN.createElement(XN.Fragment, null, Z, G)),
+      (K[7] = Z),
+      (K[8] = G),
+      (K[9] = W));
+  else W = K[9];
   return G;
 }

@@@ variable 'hNK' (was 'afK') — structural (54.8%)
--- pretty-v2.1.20.js:525905
+++ pretty-v2.1.21.js:523906
@@ -1,6 +1,7 @@
 var afK = C(() => {
   rfK();
   m4();
+  PS();
   ((PF6 = r(XA(), 1)),
     (ofK = {
       type: "local-jsx",
@@ -10,9 +11,9 @@
       },
       description:
         "Configure the default remote environment for teleport sessions",
-      isEnabled: () => Z4(),
+      isEnabled: () => O4() && YP("allow_remote_sessions"),
       get isHidden() {
-        return !Z4();
+        return !O4() || !YP("allow_remote_sessions");
       },
       async call(A) {
         return PF6.createElement(nfK, { onDone: A });

@@@ function 'UUA' (was 'vUA') — structural (53.5%)
--- pretty-v2.1.20.js:462479
+++ pretty-v2.1.21.js:460540
@@ -32,35 +32,35 @@
     case "tst":
       return (H(!0, J, "tst_enabled"), !0);
     case "tst-auto": {
-      let O = await qL2(K, q, Y, A);
-      if (O !== null) {
-        let Z = FHK(A),
-          G = O >= Z;
+      let {
+        enabled: O,
+        debugDescription: X,
+        metrics: $,
+      } = await cL2(K, q, Y, A);
+      if (O)
         return (
-          h(
-            `Auto tool search ${G ? "enabled" : "disabled"}: ${O} tokens (threshold: ${Z}, ${kx6()}% of context)` +
-              (z ? ` [source: ${z}]` : ""),
-          ),
-          H(G, J, G ? "auto_above_threshold" : "auto_below_threshold", {
-            deferredToolTokens: O,
-            threshold: Z,
-          }),
-          G
+          h(`Auto tool search enabled: ${X}` + (z ? ` [source: ${z}]` : "")),
+          H(!0, J, "auto_above_threshold", $),
+          !0
         );
-      }
-      let X = await HL2(K, q, Y),
-        $ = QHK(A),
-        _ = X >= $;
+      if (K.some((_) => IM(_)) && !sX())
+        try {
+          let _ = V4("tengu_tst_kx7", !1);
+          return (
+            h(
+              `Tool search ${_ ? "enabled" : "disabled"} via experiment (tengu_tst_kx7): below threshold, deferred tools present` +
+                (z ? ` [source: ${z}]` : ""),
+            ),
+            H(_, J, "experiment_enable_tst"),
+            _
+          );
+        } catch (_) {
+          h(`tengu_tst_kx7: GrowthBook not ready, skipping: ${_}`);
+        }
       return (
-        h(
-          `Auto tool search ${_ ? "enabled" : "disabled"} (char fallback): ${X} chars (threshold: ${$}, ${kx6()}% of context)` +
-            (z ? ` [source: ${z}]` : ""),
-        ),
-        H(_, J, _ ? "auto_above_threshold" : "auto_below_threshold", {
-          deferredToolDescriptionChars: X,
-          charThreshold: $,
-        }),
-        _
+        h(`Auto tool search disabled: ${X}` + (z ? ` [source: ${z}]` : "")),
+        H(!1, J, "auto_below_threshold", $),
+        !1
       );
     }
     case "mcp-cli":

@@@ function 'RGK' (was 'pZK') — structural (53.1%)
--- pretty-v2.1.20.js:496012
+++ pretty-v2.1.21.js:494094
@@ -1,5 +1,5 @@
 function pZK(A) {
-  let K = s(87),
+  let K = s(113),
     { item: q, isSelected: Y } = A,
     [z] = b4();
   if (q.type === "plugin") {
@@ -106,172 +106,259 @@
     else JA = K[31];
     return JA;
   }
+  if (q.type === "failed-plugin") {
+    let N;
+    if (K[32] !== z) ((N = S8("error", z)(q1.cross)), (K[32] = z), (K[33] = N));
+    else N = K[33];
+    let T = N,
+      E = `failed to load · ${q.errorCount} error${q.errorCount !== 1 ? "s" : ""}`,
+      R = Y ? "suggestion" : void 0,
+      b = Y ? `${q1.pointer} ` : "  ",
+      S;
+    if (K[34] !== R || K[35] !== b)
+      ((S = a7.createElement(f, { color: R }, b)),
+        (K[34] = R),
+        (K[35] = b),
+        (K[36] = S));
+    else S = K[36];
+    let B = Y ? "suggestion" : void 0,
+      x;
+    if (K[37] !== q.name || K[38] !== B)
+      ((x = a7.createElement(f, { color: B }, q.name)),
+        (K[37] = q.name),
+        (K[38] = B),
+        (K[39] = x));
+    else x = K[39];
+    let F = !Y,
+      Q;
+    if (K[40] === Symbol.for("react.memo_cache_sentinel"))
+      ((Q = a7.createElement(
+        f,
+        { backgroundColor: "userMessageBackground" },
+        "Plugin",
+      )),
+        (K[40] = Q));
+    else Q = K[40];
+    let u;
+    if (K[41] !== F)
+      ((u = a7.createElement(f, { dimColor: F }, " ", Q)),
+        (K[41] = F),
+        (K[42] = u));
+    else u = K[42];
+    let d;
+    if (K[43] !== q.marketplace)
+      ((d = a7.createElement(f, { dimColor: !0 }, " · ", q.marketplace)),
+        (K[43] = q.marketplace),
+        (K[44] = d));
+    else d = K[44];
+    let o = !Y,
+      l;
+    if (K[45] !== T || K[46] !== o)
+      ((l = a7.createElement(f, { dimColor: o }, " · ", T, " ")),
+        (K[45] = T),
+        (K[46] = o),
+        (K[47] = l));
+    else l = K[47];
+    let e = !Y,
+      wA;
+    if (K[48] !== E || K[49] !== e)
+      ((wA = a7.createElement(f, { dimColor: e }, E)),
+        (K[48] = E),
+        (K[49] = e),
+        (K[50] = wA));
+    else wA = K[50];
+    let HA;
+    if (
+      K[51] !== d ||
+      K[52] !== l ||
+      K[53] !== wA ||
+      K[54] !== S ||
+      K[55] !== x ||
+      K[56] !== u
+    )
+      ((HA = a7.createElement(I, null, S, x, u, d, l, wA)),
+        (K[51] = d),
+        (K[52] = l),
+        (K[53] = wA),
+        (K[54] = S),
+        (K[55] = x),
+        (K[56] = u),
+        (K[57] = HA));
+    else HA = K[57];
+    return HA;
+  }
   let w, H;
   if (q.status === "connected") {
     let N;
-    if (K[32] !== z)
-      ((N = U8("success", z)(K1.tick)), (K[32] = z), (K[33] = N));
-    else N = K[33];
+    if (K[58] !== z)
+      ((N = S8("success", z)(q1.tick)), (K[58] = z), (K[59] = N));
+    else N = K[59];
     ((w = N), (H = "connected"));
   } else if (q.status === "disabled") {
     let N;
-    if (K[34] !== z)
-      ((N = U8("inactive", z)(K1.radioOff)), (K[34] = z), (K[35] = N));
-    else N = K[35];
+    if (K[60] !== z)
+      ((N = S8("inactive", z)(q1.radioOff)), (K[60] = z), (K[61] = N));
+    else N = K[61];
     ((w = N), (H = "disabled"));
   } else if (q.status === "pending") {
     let N;
-    if (K[36] !== z)
-      ((N = U8("inactive", z)(K1.radioOff)), (K[36] = z), (K[37] = N));
-    else N = K[37];
+    if (K[62] !== z)
+      ((N = S8("inactive", z)(q1.radioOff)), (K[62] = z), (K[63] = N));
+    else N = K[63];
     ((w = N), (H = "connecting…"));
   } else if (q.status === "needs-auth") {
     let N;
-    if (K[38] !== z)
-      ((N = U8("warning", z)(K1.triangleUpOutline)), (K[38] = z), (K[39] = N));
-    else N = K[39];
+    if (K[64] !== z)
+      ((N = S8("warning", z)(q1.triangleUpOutline)), (K[64] = z), (K[65] = N));
+    else N = K[65];
     ((w = N), (H = "needs auth"));
   } else {
     let N;
-    if (K[40] !== z) ((N = U8("error", z)(K1.cross)), (K[40] = z), (K[41] = N));
-    else N = K[41];
+    if (K[66] !== z) ((N = S8("error", z)(q1.cross)), (K[66] = z), (K[67] = N));
+    else N = K[67];
     ((w = N), (H = "failed"));
   }
   if (q.indented) {
     let N = Y ? "suggestion" : void 0,
       T = Y ? `${K1.pointer} ` : "  ",
       k;
-    if (K[42] !== N || K[43] !== T)
+    if (K[68] !== N || K[69] !== T)
       ((k = $5.createElement(f, { color: N }, T)),
-        (K[42] = N),
-        (K[43] = T),
-        (K[44] = k));
-    else k = K[44];
+        (K[68] = N),
+        (K[69] = T),
+        (K[70] = E));
+    else E = K[70];
     let R = !Y,
       b;
-    if (K[45] !== R)
+    if (K[71] !== R)
       ((b = $5.createElement(f, { dimColor: R }, "└ ")),
-        (K[45] = R),
-        (K[46] = b));
-    else b = K[46];
+        (K[71] = R),
+        (K[72] = b));
+    else b = K[72];
     let S = Y ? "suggestion" : void 0,
       B;
-    if (K[47] !== q.name || K[48] !== S)
+    if (K[73] !== q.name || K[74] !== S)
       ((B = $5.createElement(f, { color: S }, q.name)),
-        (K[47] = q.name),
-        (K[48] = S),
-        (K[49] = B));
-    else B = K[49];
+        (K[73] = q.name),
+        (K[74] = S),
+        (K[75] = B));
+    else B = K[75];
     let x = !Y,
       F;
-    if (K[50] === Symbol.for("react.memo_cache_sentinel"))
+    if (K[76] === Symbol.for("react.memo_cache_sentinel"))
       ((F = $5.createElement(
         f,
         { backgroundColor: "userMessageBackground" },
         "MCP",
       )),
-        (K[50] = F));
-    else F = K[50];
+        (K[76] = F));
+    else F = K[76];
     let Q;
-    if (K[51] !== x)
+    if (K[77] !== x)
       ((Q = $5.createElement(f, { dimColor: x }, " ", F)),
-        (K[51] = x),
-        (K[52] = Q));
-    else Q = K[52];
+        (K[77] = x),
+        (K[78] = Q));
+    else Q = K[78];
     let u = !Y,
       d;
-    if (K[53] !== w || K[54] !== u)
+    if (K[79] !== w || K[80] !== u)
       ((d = $5.createElement(f, { dimColor: u }, " · ", w, " ")),
-        (K[53] = w),
-        (K[54] = u),
-        (K[55] = d));
-    else d = K[55];
+        (K[79] = w),
+        (K[80] = u),
+        (K[81] = d));
+    else d = K[81];
     let a = !Y,
       l;
-    if (K[56] !== H || K[57] !== a)
+    if (K[82] !== H || K[83] !== o)
       ((l = $5.createElement(f, { dimColor: a }, H)),
-        (K[56] = H),
-        (K[57] = a),
-        (K[58] = l));
-    else l = K[58];
+        (K[82] = H),
+        (K[83] = o),
+        (K[84] = l));
+    else l = K[84];
     let e;
     if (
-      K[59] !== Q ||
-      K[60] !== d ||
-      K[61] !== l ||
-      K[62] !== k ||
-      K[63] !== b ||
-      K[64] !== B
+      K[85] !== Q ||
+      K[86] !== d ||
+      K[87] !== l ||
+      K[88] !== E ||
+      K[89] !== b ||
+      K[90] !== B
     )
       ((e = $5.createElement(I, null, k, b, B, Q, d, l)),
-        (K[59] = Q),
-        (K[60] = d),
-        (K[61] = l),
-        (K[62] = k),
-        (K[63] = b),
-        (K[64] = B),
-        (K[65] = e));
-    else e = K[65];
+        (K[85] = Q),
+        (K[86] = d),
+        (K[87] = l),
+        (K[88] = E),
+        (K[89] = b),
+        (K[90] = B),
+        (K[91] = e));
+    else e = K[91];
     return e;
   }
   let J = Y ? "suggestion" : void 0,
     O = Y ? `${K1.pointer} ` : "  ",
     X;
-  if (K[66] !== J || K[67] !== O)
+  if (K[92] !== J || K[93] !== O)
     ((X = $5.createElement(f, { color: J }, O)),
-      (K[66] = J),
-      (K[67] = O),
-      (K[68] = X));
-  else X = K[68];
+      (K[92] = J),
+      (K[93] = O),
+      (K[94] = X));
+  else X = K[94];
   let $ = Y ? "suggestion" : void 0,
     _;
-  if (K[69] !== q.name || K[70] !== $)
+  if (K[95] !== q.name || K[96] !== $)
     ((_ = $5.createElement(f, { color: $ }, q.name)),
-      (K[69] = q.name),
-      (K[70] = $),
-      (K[71] = _));
-  else _ = K[71];
+      (K[95] = q.name),
+      (K[96] = $),
+      (K[97] = _));
+  else _ = K[97];
   let Z = !Y,
     G;
-  if (K[72] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[98] === Symbol.for("react.memo_cache_sentinel"))
     ((G = $5.createElement(
       f,
       { backgroundColor: "userMessageBackground" },
       "MCP",
     )),
-      (K[72] = G));
-  else G = K[72];
+      (K[98] = G));
+  else G = K[98];
   let W;
-  if (K[73] !== Z)
+  if (K[99] !== Z)
     ((W = $5.createElement(f, { dimColor: Z }, " ", G)),
-      (K[73] = Z),
-      (K[74] = W));
-  else W = K[74];
+      (K[99] = Z),
+      (K[100] = W));
+  else W = K[100];
   let D = !Y,
     M;
-  if (K[75] !== w || K[76] !== D)
+  if (K[101] !== w || K[102] !== D)
     ((M = $5.createElement(f, { dimColor: D }, " · ", w, " ")),
-      (K[75] = w),
-      (K[76] = D),
-      (K[77] = M));
-  else M = K[77];
+      (K[101] = w),
+      (K[102] = D),
+      (K[103] = j));
+  else j = K[103];
   let j = !Y,
     P;
-  if (K[78] !== H || K[79] !== j)
+  if (K[104] !== H || K[105] !== M)
     ((P = $5.createElement(f, { dimColor: j }, H)),
-      (K[78] = H),
-      (K[79] = j),
-      (K[80] = P));
-  else P = K[80];
+      (K[104] = H),
+      (K[105] = M),
+      (K[106] = P));
+  else P = K[106];
   let V;
-  if (K[81] !== M || K[82] !== P || K[83] !== X || K[84] !== _ || K[85] !== W)
+  if (
+    K[107] !== j ||
+    K[108] !== P ||
+    K[109] !== X ||
+    K[110] !== _ ||
+    K[111] !== W
+  )
     ((V = $5.createElement(I, null, X, _, W, M, P)),
-      (K[81] = M),
-      (K[82] = P),
-      (K[83] = X),
-      (K[84] = _),
-      (K[85] = W),
-      (K[86] = V));
-  else V = K[86];
+      (K[107] = j),
+      (K[108] = P),
+      (K[109] = X),
+      (K[110] = _),
+      (K[111] = W),
+      (K[112] = V));
+  else V = K[112];
   return V;
 }

@@@ function 'bs' (was 'Ds') — structural (52.4%)
--- pretty-v2.1.20.js:340330
+++ pretty-v2.1.21.js:340624
@@ -1,20 +1,25 @@
 function Ds(A) {
-  let K = s(4),
+  let K = s(7),
     { isError: q, isUnresolved: Y, shouldAnimate: z } = A,
-    w = MR7(z),
+    [w, H] = D4A(),
+    { isVisible: J } = H,
+    O = wy7(z && J),
     H = Y ? void 0 : q ? "error" : "success",
     J = !z || w || q || !Y ? uY : " ",
     O;
   if (K[0] !== H || K[1] !== Y || K[2] !== J)
-    ((O = fN6.default.createElement(
-      I,
-      { minWidth: 2 },
-      fN6.default.createElement(f, { color: H, dimColor: Y }, J),
-    )),
+    ((_ = pN6.default.createElement(f, { color: X, dimColor: Y }, $)),
       (K[0] = H),
       (K[1] = Y),
       (K[2] = J),
       (K[3] = O));
   else O = K[3];
+  let Z;
+  if (K[4] !== w || K[5] !== _)
+    ((Z = pN6.default.createElement(I, { ref: w, minWidth: 2 }, _)),
+      (K[4] = w),
+      (K[5] = _),
+      (K[6] = Z));
+  else Z = K[6];
   return O;
 }

@@@ function 'I3A' (was 'G3A') — structural (51.9%)
--- pretty-v2.1.20.js:415097
+++ pretty-v2.1.21.js:415726
@@ -1,5 +1,9 @@
 function G3A(A, K) {
+  let q;
   for (let q of Object.values(K))
-    if (iT(q) && q.identity.agentId === A) return q;
-  return;
+    if (rT(Y) && Y.identity.agentId === A) {
+      if (Y.status === "running") return Y;
+      if (!q) q = Y;
+    }
+  return q;
 }

@@@ function 'lO4' (was 'w04') — structural (51.8%)
--- pretty-v2.1.20.js:176347
+++ pretty-v2.1.21.js:176498
@@ -1,6 +1,8 @@
 function w04(A) {
   for (let K of A) {
-    let q = K.code.match(z04);
+    let q = K.code;
+    if (q.length < 5 || !q.startsWith(cO4)) continue;
+    let Y = q.match(dO4);
     if (q) return q[1] || null;
   }
   return null;

@@@ function 'QFK' (was 'UgK') — structural (51.3%)
--- pretty-v2.1.20.js:571780
+++ pretty-v2.1.21.js:571337
@@ -1,5 +1,5 @@
 function UgK(A) {
-  let K = s(15),
+  let K = s(7),
     { onAccept: q } = A,
     Y;
   if (K[0] === Symbol.for("react.memo_cache_sentinel")) ((Y = []), (K[0] = Y));
@@ -21,24 +21,9 @@
       (K[2] = z));
   else z = K[2];
   let w = z,
-    H = k8(),
     J = d4z,
     O;
   if (K[3] === Symbol.for("react.memo_cache_sentinel"))
-    ((O = { context: "Confirmation" }), (K[3] = O));
-  else O = K[3];
-  s1("confirm:no", J, O);
-  let X;
-  if (K[4] === Symbol.for("react.memo_cache_sentinel"))
-    ((X = XG.default.createElement(
-      f,
-      { bold: !0, color: "error" },
-      "WARNING: Claude Code running in Bypass Permissions mode",
-    )),
-      (K[4] = X));
-  else X = K[4];
-  let $;
-  if (K[5] === Symbol.for("react.memo_cache_sentinel"))
     (($ = XG.default.createElement(
       I,
       { flexDirection: "column", gap: 1 },
@@ -58,67 +43,30 @@
         url: "https://code.claude.com/docs/en/security",
       }),
     )),
-      (K[5] = $));
-  else $ = K[5];
+      (K[3] = J));
+  else J = K[3];
   let _;
-  if (K[6] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[4] === Symbol.for("react.memo_cache_sentinel"))
     ((_ = [
       { label: "No, exit", value: "decline" },
       { label: "Yes, I accept", value: "accept" },
     ]),
-      (K[6] = _));
-  else _ = K[6];
+      (K[4] = O));
+  else O = K[4];
   let Z;
-  if (K[7] !== w)
+  if (K[5] !== w)
     ((Z = XG.default.createElement(
       I,
       {
-        flexDirection: "column",
-        gap: 1,
-        padding: 1,
-        borderStyle: "round",
-        borderColor: "error",
+        title: "WARNING: Claude Code running in Bypass Permissions mode",
+        color: "error",
+        onCancel: H,
       },
       X,
-      $,
       XG.default.createElement(y6, { options: _, onChange: (D) => w(D) }),
     )),
-      (K[7] = w),
-      (K[8] = Z));
-  else Z = K[8];
-  let G;
-  if (K[9] !== H.keyName || K[10] !== H.pending)
-    ((G = XG.default.createElement(
-      I,
-      { marginLeft: 3 },
-      XG.default.createElement(
-        f,
-        { dimColor: !0 },
-        H.pending
-          ? XG.default.createElement(
-              XG.default.Fragment,
-              null,
-              "Press ",
-              H.keyName,
-              " again to exit",
-            )
-          : XG.default.createElement(
-              XG.default.Fragment,
-              null,
-              "Enter to confirm · Esc to cancel",
-            ),
-      ),
-    )),
-      (K[9] = H.keyName),
-      (K[10] = H.pending),
-      (K[11] = G));
-  else G = K[11];
-  let W;
-  if (K[12] !== Z || K[13] !== G)
-    ((W = XG.default.createElement(XG.default.Fragment, null, Z, G)),
-      (K[12] = Z),
-      (K[13] = G),
-      (K[14] = W));
-  else W = K[14];
+      (K[5] = w),
+      (K[6] = X));
+  else X = K[6];
   return W;
 }

@@@ function 'DZK' (was 'y_K') — structural (50.9%)
--- pretty-v2.1.20.js:486635
+++ pretty-v2.1.21.js:484731
@@ -1,18 +1,13 @@
 function y_K() {
-  let A = Lx2(sOA);
+  let K = {
+    $schema:
+      "https://platform.claude.com/docs/schemas/claude-code/keybindings.json",
+    $docs: "https://code.claude.com/docs/en/keybindings",
+    bindings: bu2(VXA),
+  };
   return (
-    A.push(Rx2),
-    QA(
-      {
-        $schema:
-          "https://platform.claude.com/docs/schemas/claude-code/keybindings.json",
-        $docs: "https://code.claude.com/docs/en/keybindings",
-        bindings: A,
-      },
-      null,
-      2,
-    ) +
-      `
+    QA(K, null, 2) +
+    `
 `
   );
 }

@@@ function '$T1' (was 'oN1') — structural (50.7%)
--- pretty-v2.1.20.js:479255
+++ pretty-v2.1.21.js:478021
@@ -1,5 +1,5 @@
 function oN1(A) {
-  let K = s(26),
+  let K = s(18),
     { onDone: q, isStandaloneDialog: Y, externalIncludes: z } = A,
     w;
   if (K[0] === Symbol.for("react.memo_cache_sentinel")) ((w = []), (K[0] = w));
@@ -18,7 +18,6 @@
       (K[2] = H));
   else H = K[2];
   let J = H,
-    O = k8(),
     X;
   if (K[3] !== J)
     ((X = () => {
@@ -28,31 +27,19 @@
       (K[4] = X));
   else X = K[4];
   let $ = X,
+    $ = !Y,
+    _ = !Y,
     _;
   if (K[5] === Symbol.for("react.memo_cache_sentinel"))
-    ((_ = { context: "Confirmation" }), (K[5] = _));
-  else _ = K[5];
-  s1("confirm:no", $, _);
-  let Z = Y ? 1 : 0,
-    G = Y ? "round" : void 0,
-    W,
-    D;
-  if (K[6] === Symbol.for("react.memo_cache_sentinel"))
     ((W = h$.default.createElement(
       f,
-      { bold: !0, color: "warning" },
-      "Allow external CLAUDE.md file imports?",
+      null,
+      "This project's CLAUDE.md imports files outside the current working directory. Never allow this for third-party repositories.",
     )),
-      (D = h$.default.createElement(
-        f,
-        null,
-        "This project's CLAUDE.md imports files outside the current working directory. Never allow this for third-party repositories.",
-      )),
-      (K[6] = W),
-      (K[7] = D));
-  else ((W = K[6]), (D = K[7]));
+      (K[5] = Z));
+  else Z = K[5];
   let M;
-  if (K[8] !== z)
+  if (K[6] !== z)
     ((M =
       z &&
       z.length > 0 &&
@@ -62,11 +49,11 @@
         h$.default.createElement(f, { dimColor: !0 }, "External imports:"),
         z.map(Rh2),
       )),
-      (K[8] = z),
-      (K[9] = M));
-  else M = K[9];
+      (K[6] = z),
+      (K[7] = G));
+  else G = K[7];
   let j;
-  if (K[10] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[8] === Symbol.for("react.memo_cache_sentinel"))
     ((j = h$.default.createElement(
       f,
       { dimColor: !0 },
@@ -77,95 +64,44 @@
       }),
       " ",
     )),
-      (K[10] = j));
-  else j = K[10];
+      (K[8] = W));
+  else W = K[8];
   let P;
-  if (K[11] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[9] === Symbol.for("react.memo_cache_sentinel"))
     ((P = [
       { label: "Yes, allow external imports", value: "yes" },
       { label: "No, disable external imports", value: "no" },
     ]),
-      (K[11] = P));
-  else P = K[11];
+      (K[9] = D));
+  else D = K[9];
   let V;
-  if (K[12] !== J)
+  if (K[10] !== J)
     ((V = h$.default.createElement(y6, { options: P, onChange: (R) => J(R) })),
-      (K[12] = J),
-      (K[13] = V));
-  else V = K[13];
+      (K[10] = J),
+      (K[11] = j));
+  else j = K[11];
   let N;
-  if (K[14] !== Y || K[15] !== V || K[16] !== Z || K[17] !== G || K[18] !== M)
+  if (K[12] !== X || K[13] !== j || K[14] !== $ || K[15] !== _ || K[16] !== G)
     ((N = h$.default.createElement(
       I,
       {
-        flexDirection: "column",
-        gap: 1,
-        paddingX: Z,
-        marginBottom: 1,
-        borderStyle: G,
-        borderTop: Y,
-        borderLeft: !1,
-        borderRight: !1,
-        borderBottom: !1,
-        borderColor: "warning",
+        title: "Allow external CLAUDE.md file imports?",
+        color: "warning",
+        onCancel: X,
+        hideBorder: $,
+        hideInputGuide: _,
       },
-      W,
       D,
       M,
       j,
       V,
     )),
+      (K[12] = X),
+      (K[13] = j),
       (K[14] = Y),
       (K[15] = V),
       (K[16] = Z),
-      (K[17] = G),
-      (K[18] = M),
-      (K[19] = N));
-  else N = K[19];
-  let T;
-  if (K[20] !== O || K[21] !== Y)
-    ((T =
-      Y &&
-      h$.default.createElement(
-        I,
-        { marginLeft: 1 },
-        h$.default.createElement(
-          f,
-          { dimColor: !0 },
-          O.pending
-            ? h$.default.createElement(
-                h$.default.Fragment,
-                null,
-                "Press ",
-                O.keyName,
-                " again to exit",
-              )
-            : h$.default.createElement(
-                w8,
-                null,
-                h$.default.createElement(M6, {
-                  shortcut: "Enter",
-                  action: "confirm",
-                }),
-                h$.default.createElement(d6, {
-                  action: "confirm:no",
-                  context: "Confirmation",
-                  fallback: "Esc",
-                  description: "disable external includes",
-                }),
-              ),
-        ),
-      )),
-      (K[20] = O),
-      (K[21] = Y),
-      (K[22] = T));
-  else T = K[22];
-  let k;
-  if (K[23] !== N || K[24] !== T)
-    ((k = h$.default.createElement(h$.default.Fragment, null, N, T)),
-      (K[23] = N),
-      (K[24] = T),
-      (K[25] = k));
-  else k = K[25];
+      (K[17] = M));
+  else M = K[17];
   return k;
 }

@@@ function 'NW7' (was 'bG7') — structural (46.7%)
--- pretty-v2.1.20.js:307418
+++ pretty-v2.1.21.js:308210
@@ -1,7 +1,6 @@
 function bG7(A) {
-  let K = s(31),
-    { onDone: q, installationStatus: Y } = A,
-    z = k8();
+  let K = s(23),
+    { onDone: q, installationStatus: Y } = A;
   RkY();
   let w;
   if (K[0] !== q)
@@ -29,72 +28,43 @@
   if (K[7] === Symbol.for("react.memo_cache_sentinel"))
     ((D = Cz.default.createElement(f, { color: "claude" }, "✻ ")), (K[7] = D));
   else D = K[7];
-  let M;
-  if (K[8] === Symbol.for("react.memo_cache_sentinel"))
-    ((M = Cz.default.createElement(f, { bold: !0 }, "Claude Code")),
-      (K[8] = M));
-  else M = K[8];
   let j;
-  if (K[9] !== _)
+  if (K[8] !== $)
     ((j = Cz.default.createElement(
-      f,
+      AX.default.Fragment,
       null,
-      "Welcome to ",
       M,
-      " for",
-      " ",
-      Cz.default.createElement(f, { color: "ide", bold: !0 }, _),
+      AX.default.createElement(f, null, "Welcome to Claude Code for ", $),
     )),
-      (K[9] = _),
+      (K[8] = $),
+      (K[9] = D));
+  else D = K[9];
+  let j = _ ? `installed ${Z} v${_}` : void 0,
+    M;
+  if (K[10] === Symbol.for("react.memo_cache_sentinel"))
+    ((M = AX.default.createElement(f, { color: "suggestion" }, "⧉ open files")),
       (K[10] = j));
   else j = K[10];
   let P;
-  if (K[11] !== Z || K[12] !== G)
-    ((P =
-      Z &&
-      Cz.default.createElement(f, { dimColor: !0 }, "installed ", G, " v", Z)),
-      (K[11] = Z),
-      (K[12] = G),
-      (K[13] = P));
-  else P = K[13];
-  let V;
-  if (K[14] !== j || K[15] !== P)
+  if (K[11] === Symbol.for("react.memo_cache_sentinel"))
     ((V = Cz.default.createElement(
       I,
       null,
-      D,
-      Cz.default.createElement(I, { flexDirection: "column" }, j, P),
-    )),
-      (K[14] = j),
-      (K[15] = P),
-      (K[16] = V));
-  else V = K[16];
-  let N;
-  if (K[17] === Symbol.for("react.memo_cache_sentinel"))
-    ((N = Cz.default.createElement(f, { color: "suggestion" }, "⧉ open files")),
-      (K[17] = N));
-  else N = K[17];
-  let T;
-  if (K[18] === Symbol.for("react.memo_cache_sentinel"))
-    ((T = Cz.default.createElement(
-      f,
+      "• Claude has context of ",
       null,
-      "• Claude has context of",
       " ",
-      N,
-      " and",
-      " ",
+      "and ",
       Cz.default.createElement(f, { color: "suggestion" }, "⧉ selected lines"),
     )),
-      (K[18] = T));
-  else T = K[18];
+      (K[11] = P));
+  else P = K[11];
   let k;
-  if (K[19] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[12] === Symbol.for("react.memo_cache_sentinel"))
     ((k = Cz.default.createElement(f, { color: "diffAddedWord" }, "+11")),
-      (K[19] = k));
-  else k = K[19];
+      (K[12] = V));
+  else V = K[12];
   let R;
-  if (K[20] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[13] === Symbol.for("react.memo_cache_sentinel"))
     ((R = Cz.default.createElement(
       f,
       null,
@@ -105,23 +75,23 @@
       Cz.default.createElement(f, { color: "diffRemovedWord" }, "-22"),
       " in the comfort of your IDE",
     )),
-      (K[20] = R));
-  else R = K[20];
+      (K[13] = N));
+  else N = K[13];
   let b;
-  if (K[21] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[14] === Symbol.for("react.memo_cache_sentinel"))
     ((b = Cz.default.createElement(
       f,
       null,
       "• Cmd+Esc",
       Cz.default.createElement(f, { dimColor: !0 }, " for Quick Launch"),
     )),
-      (K[21] = b));
-  else b = K[21];
+      (K[14] = T));
+  else T = K[14];
   let S;
-  if (K[22] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[15] === Symbol.for("react.memo_cache_sentinel"))
     ((S = Cz.default.createElement(
       I,
-      { flexDirection: "column", paddingLeft: 1, gap: 1 },
+      { flexDirection: "column", gap: 1 },
       T,
       R,
       b,
@@ -137,63 +107,38 @@
         ),
       ),
     )),
-      (K[22] = S));
-  else S = K[22];
+      (K[15] = E));
+  else E = K[15];
   let B;
-  if (K[23] !== V)
+  if (K[16] !== q || K[17] !== D || K[18] !== j)
     ((B = Cz.default.createElement(
       I,
-      {
-        flexDirection: "column",
-        borderStyle: "round",
-        borderColor: "ide",
-        paddingLeft: 1,
-        paddingRight: 1,
-        gap: 1,
-      },
-      V,
+      { title: D, subtitle: j, color: "ide", onCancel: q, hideInputGuide: !0 },
       S,
     )),
-      (K[23] = V),
-      (K[24] = B));
-  else B = K[24];
+      (K[16] = q),
+      (K[17] = D),
+      (K[18] = j),
+      (K[19] = R));
+  else R = K[19];
   let x;
-  if (K[25] !== z.keyName || K[26] !== z.pending)
+  if (K[20] === Symbol.for("react.memo_cache_sentinel"))
     ((x = Cz.default.createElement(
       I,
-      { marginLeft: 3 },
+      { paddingX: 1 },
       Cz.default.createElement(
         f,
-        { dimColor: !0 },
-        z.pending
-          ? Cz.default.createElement(
-              Cz.default.Fragment,
-              null,
-              "Press ",
-              z.keyName,
-              " again to exit",
-            )
-          : Cz.default.createElement(
-              Cz.default.Fragment,
-              null,
-              "Press Enter to continue",
-            ),
+        { dimColor: !0, italic: !0 },
+        "Press Enter to continue",
       ),
     )),
-      (K[25] = z.keyName),
-      (K[26] = z.pending),
-      (K[27] = x));
-  else x = K[27];
+      (K[20] = b));
+  else b = K[20];
   let F;
-  if (K[28] !== B || K[29] !== x)
-    ((F = Cz.default.createElement(
-      Cz.default.Fragment,
-      null,
-      Cz.default.createElement(I, { flexDirection: "column" }, B, x),
-    )),
-      (K[28] = B),
-      (K[29] = x),
-      (K[30] = F));
-  else F = K[30];
+  if (K[21] !== R)
+    ((S = AX.default.createElement(AX.default.Fragment, null, R, b)),
+      (K[21] = R),
+      (K[22] = S));
+  else S = K[22];
   return F;
 }

@@@ function 'tyK' (was '_yK') — structural (44.6%)
--- pretty-v2.1.20.js:556954
+++ pretty-v2.1.21.js:555784
@@ -1,7 +1,8 @@
 function _yK(A) {
-  let K = s(27),
+  let K = s(28),
     { currentValue: q, onSelect: Y, onCancel: z, isMidConversation: w } = A,
     H = k8(),
+    [J, O] = syK.useState(null),
     J;
   if (K[0] === Symbol.for("react.memo_cache_sentinel"))
     ((J = [
@@ -20,100 +21,116 @@
   else J = K[0];
   let O = J,
     X;
-  if (K[1] !== z)
+  if (K[1] !== J || K[2] !== z)
     ((X = () => {
-      z?.();
+      if (J !== null) O(null);
+      else z?.();
     }),
       (K[1] = z),
-      (K[2] = X));
-  else X = K[2];
+      (K[2] = z),
+      (K[3] = _));
+  else _ = K[3];
+  let Z;
+  if (K[4] === Symbol.for("react.memo_cache_sentinel"))
+    ((Z = { context: "Confirmation" }), (K[4] = Z));
+  else Z = K[4];
+  A6("confirm:no", _, Z);
   let $;
-  if (K[3] === Symbol.for("react.memo_cache_sentinel"))
-    (($ = { context: "Confirmation" }), (K[3] = $));
-  else $ = K[3];
+  if (K[5] !== J || K[6] !== Y)
+    ((G = () => {
+      if (J !== null) Y(J);
+    }),
+      (K[5] = J),
+      (K[6] = Y),
+      (K[7] = G));
+  else G = K[7];
+  let W = J !== null,
+    D;
+  if (K[8] !== W)
+    ((D = { context: "Confirmation", isActive: W }), (K[8] = W), (K[9] = D));
+  else D = K[9];
   s1("confirm:no", X, $);
   let _;
-  if (K[4] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[10] !== q || K[11] !== w || K[12] !== Y)
+    ((j = function (b) {
+      let S = b === "true";
+      if (w && S !== q) O(S);
+      else Y(S);
+    }),
+      (K[10] = q),
+      (K[11] = w),
+      (K[12] = Y),
+      (K[13] = j));
+  else j = K[13];
+  let M = j,
+    P;
+  if (K[14] === Symbol.for("react.memo_cache_sentinel"))
     ((_ = CY.createElement(U3, {
       dividerColor: "permission",
       dividerDimColor: !1,
     })),
-      (K[4] = _));
-  else _ = K[4];
-  let Z, G;
-  if (K[5] === Symbol.for("react.memo_cache_sentinel"))
+      (K[14] = P));
+  else P = K[14];
+  let V;
+  if (K[15] === Symbol.for("react.memo_cache_sentinel"))
     ((Z = CY.createElement(
       f,
-      { color: "remember", bold: !0 },
-      "Toggle thinking mode",
-    )),
-      (G = CY.createElement(
+      { marginBottom: 1, flexDirection: "column" },
+      Q5.createElement(
         f,
-        { dimColor: !0 },
-        "Enable or disable thinking for this session.",
-      )),
-      (K[5] = Z),
-      (K[6] = G));
-  else ((Z = K[5]), (G = K[6]));
-  let W;
-  if (K[7] !== w)
-    ((W =
-      w &&
+        { color: "remember", bold: !0 },
+        "Toggle thinking mode",
+      ),
       CY.createElement(
         f,
-        { color: "warning" },
-        "Changing mid-conversation may reduce quality. For best results, set this at the start of a session.",
-      )),
-      (K[7] = w),
-      (K[8] = W));
-  else W = K[8];
+        { dimColor: !0 },
+        "Enable or disable thinking for this session.",
+      ),
+    )),
+      (K[15] = V));
+  else V = K[15];
   let D;
-  if (K[9] !== W)
+  if (K[16] !== J || K[17] !== q || K[18] !== M || K[19] !== z)
     ((D = CY.createElement(
       I,
-      { marginBottom: 1, flexDirection: "column" },
+      { flexDirection: "column" },
       Z,
-      G,
-      W,
-    )),
-      (K[9] = W),
-      (K[10] = D));
-  else D = K[10];
-  let M = q ? "true" : "false",
-    j = q ? "true" : "false",
-    P;
-  if (K[11] !== Y) ((P = (b) => Y(b === "true")), (K[11] = Y), (K[12] = P));
-  else P = K[12];
-  let V = z ?? P1z,
-    N;
-  if (K[13] !== j || K[14] !== P || K[15] !== V || K[16] !== M)
-    ((N = CY.createElement(
-      I,
-      { flexDirection: "column", marginBottom: 1 },
-      CY.createElement(y6, {
-        defaultValue: M,
-        defaultFocusValue: j,
-        options: O,
-        onChange: P,
-        onCancel: V,
-        visibleOptionCount: 2,
-      }),
+      J !== null
+        ? Q5.createElement(
+            I,
+            { flexDirection: "column", marginBottom: 1, gap: 1 },
+            Q5.createElement(
+              f,
+              { color: "warning" },
+              "Changing thinking mode mid-conversation will increase latency and may reduce quality. For best results, set this at the start of a session.",
+            ),
+            Q5.createElement(
+              f,
+              { color: "warning" },
+              "Do you want to proceed?",
+            ),
+          )
+        : Q5.createElement(
+            I,
+            { flexDirection: "column", marginBottom: 1 },
+            Q5.createElement(k6, {
+              defaultValue: q ? "true" : "false",
+              defaultFocusValue: q ? "true" : "false",
+              options: $,
+              onChange: M,
+              onCancel: z ?? R6z,
+              visibleOptionCount: 2,
+            }),
+          ),
     )),
-      (K[13] = j),
-      (K[14] = P),
-      (K[15] = V),
       (K[16] = M),
-      (K[17] = N));
-  else N = K[17];
-  let T;
-  if (K[18] !== N || K[19] !== D)
-    ((T = CY.createElement(I, { flexDirection: "column" }, D, N)),
+      (K[17] = q),
       (K[18] = N),
       (K[19] = D),
       (K[20] = T));
   else T = K[20];
   let k;
-  if (K[21] !== H.keyName || K[22] !== H.pending)
+  if (K[21] !== J || K[22] !== H.keyName || K[23] !== H.pending)
     ((k = CY.createElement(
       f,
       { dimColor: !0, italic: !0 },
@@ -125,33 +142,46 @@
             H.keyName,
             " again to exit",
           )
-        : CY.createElement(
-            w8,
-            null,
-            CY.createElement(M6, { shortcut: "Enter", action: "confirm" }),
-            CY.createElement(d6, {
-              action: "confirm:no",
-              context: "Confirmation",
-              fallback: "Esc",
-              description: "exit",
-            }),
-          ),
+        : J !== null
+          ? Q5.createElement(
+              w8,
+              null,
+              Q5.createElement(G6, { shortcut: "Enter", action: "confirm" }),
+              Q5.createElement(U6, {
+                action: "confirm:no",
+                context: "Confirmation",
+                fallback: "Esc",
+                description: "cancel",
+              }),
+            )
+          : Q5.createElement(
+              w8,
+              null,
+              Q5.createElement(G6, { shortcut: "Enter", action: "confirm" }),
+              Q5.createElement(U6, {
+                action: "confirm:no",
+                context: "Confirmation",
+                fallback: "Esc",
+                description: "exit",
+              }),
+            ),
     )),
-      (K[21] = H.keyName),
-      (K[22] = H.pending),
-      (K[23] = k));
-  else k = K[23];
+      (K[21] = J),
+      (K[22] = H.keyName),
+      (K[23] = H.pending),
+      (K[24] = T));
+  else T = K[24];
   let R;
-  if (K[24] !== T || K[25] !== k)
+  if (K[25] !== N || K[26] !== T)
     ((R = CY.createElement(
       I,
       { flexDirection: "column", width: "100%" },
       _,
       CY.createElement(I, { flexDirection: "column", paddingX: 1 }, T, k),
     )),
-      (K[24] = T),
       (K[25] = k),
-      (K[26] = R));
-  else R = K[26];
+      (K[26] = T),
+      (K[27] = E));
+  else E = K[27];
   return R;
 }

@@@ function 'ks2' (was 'fa2') — structural (43.4%)
--- pretty-v2.1.20.js:538224
+++ pretty-v2.1.21.js:536246
@@ -1,30 +1,19 @@
 function fa2(A) {
-  let K = s(26),
+  let K = s(19),
     { filePath: q, errorDescription: Y, onExit: z, onReset: w } = A,
     H;
-  if (K[0] === Symbol.for("react.memo_cache_sentinel"))
-    ((H = { context: "Confirmation" }), (K[0] = H));
-  else H = K[0];
-  s1("confirm:no", z, H);
-  let J = k8(),
-    O;
-  if (K[1] !== z || K[2] !== w)
+  if (K[0] !== z || K[1] !== w)
     ((O = (N) => {
       if (N === "exit") z();
       else w();
     }),
+      (K[0] = z),
       (K[1] = z),
-      (K[2] = w),
-      (K[3] = O));
-  else O = K[3];
+      (K[2] = H));
+  else H = K[2];
   let X = O,
     $;
-  if (K[4] === Symbol.for("react.memo_cache_sentinel"))
-    (($ = hW.default.createElement(f, { bold: !0 }, "Configuration Error")),
-      (K[4] = $));
-  else $ = K[4];
-  let _;
-  if (K[5] !== q)
+  if (K[3] !== q)
     ((_ = hW.default.createElement(
       f,
       null,
@@ -32,91 +21,62 @@
       hW.default.createElement(f, { bold: !0 }, q),
       " contains invalid JSON.",
     )),
-      (K[5] = q),
-      (K[6] = _));
+      (K[3] = q),
+      (K[4] = O));
+  else O = K[4];
+  let X;
+  if (K[5] !== Y)
+    ((X = uL.default.createElement(f, null, Y)), (K[5] = Y), (K[6] = X));
   else _ = K[6];
   let Z;
-  if (K[7] !== Y)
-    ((Z = hW.default.createElement(f, null, Y)), (K[7] = Y), (K[8] = Z));
-  else Z = K[8];
-  let G;
-  if (K[9] !== _ || K[10] !== Z)
+  if (K[7] !== O || K[8] !== X)
     ((G = hW.default.createElement(
       I,
       { flexDirection: "column", gap: 1 },
       _,
       Z,
     )),
-      (K[9] = _),
-      (K[10] = Z),
-      (K[11] = G));
-  else G = K[11];
+      (K[7] = O),
+      (K[8] = X),
+      (K[9] = $));
+  else $ = K[9];
   let W;
-  if (K[12] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[10] === Symbol.for("react.memo_cache_sentinel"))
     ((W = hW.default.createElement(f, { bold: !0 }, "Choose an option:")),
-      (K[12] = W));
-  else W = K[12];
+      (K[10] = _));
+  else _ = K[10];
   let D;
-  if (K[13] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[11] === Symbol.for("react.memo_cache_sentinel"))
     ((D = [
       { label: "Exit and fix manually", value: "exit" },
       { label: "Reset with default configuration", value: "reset" },
     ]),
-      (K[13] = D));
-  else D = K[13];
+      (K[11] = Z));
+  else Z = K[11];
   let M;
-  if (K[14] !== X || K[15] !== z)
+  if (K[12] !== J || K[13] !== z)
     ((M = hW.default.createElement(
       I,
       { flexDirection: "column" },
       W,
       hW.default.createElement(y6, { options: D, onChange: X, onCancel: z }),
     )),
-      (K[14] = X),
-      (K[15] = z),
-      (K[16] = M));
-  else M = K[16];
+      (K[12] = J),
+      (K[13] = z),
+      (K[14] = G));
+  else G = K[14];
   let j;
-  if (K[17] !== G || K[18] !== M)
+  if (K[15] !== z || K[16] !== $ || K[17] !== G)
     ((j = hW.default.createElement(
       I,
-      {
-        flexDirection: "column",
-        borderColor: "error",
-        borderStyle: "round",
-        padding: 1,
-        width: 70,
-        gap: 1,
-      },
+      { title: "Configuration Error", color: "error", onCancel: z },
       $,
       G,
-      M,
     )),
+      (K[15] = z),
+      (K[16] = $),
       (K[17] = G),
-      (K[18] = M),
-      (K[19] = j));
-  else j = K[19];
-  let P;
-  if (K[20] !== J.keyName || K[21] !== J.pending)
-    ((P = J.pending
-      ? hW.default.createElement(
-          f,
-          { dimColor: !0 },
-          "Press ",
-          J.keyName,
-          " again to exit",
-        )
-      : hW.default.createElement(dO, null)),
-      (K[20] = J.keyName),
-      (K[21] = J.pending),
-      (K[22] = P));
-  else P = K[22];
-  let V;
-  if (K[23] !== j || K[24] !== P)
-    ((V = hW.default.createElement(hW.default.Fragment, null, j, P)),
-      (K[23] = j),
-      (K[24] = P),
-      (K[25] = V));
-  else V = K[25];
+      (K[18] = W));
+  else W = K[18];
   return V;
 }

@@@ variable 'IP1' (was '$P1') — structural (42.9%)
--- pretty-v2.1.20.js:419948
+++ pretty-v2.1.21.js:420580
@@ -2,69 +2,49 @@
   i5();
   D1();
   d7();
-  ((xy6 = K6(() => {
+  d7();
+  (($I6 = a1(async () => {
     if (s6() !== "linux") return !1;
-    let K = process.execPath || process.argv[0] || "";
-    try {
-      let q = OP1("pacman", ["-Qo", K], {
-        encoding: "utf8",
-        timeout: 5000,
-        stdio: ["ignore", "pipe", "pipe"],
-      });
-      if (q.status === 0 && q.stdout)
-        return (h(`Detected pacman installation: ${q.stdout.trim()}`), !0);
-    } catch {}
+    let K = process.execPath || process.argv[0] || "",
+      q = await L6("pacman", ["-Qo", K], { timeout: 5000, useCwd: !1 });
+    if (q.code === 0 && q.stdout)
+      return (h(`Detected pacman installation: ${q.stdout.trim()}`), !0);
     return !1;
   })),
-    (uy6 = K6(() => {
+    (_I6 = a1(async () => {
       if (s6() !== "linux") return !1;
-      let K = process.execPath || process.argv[0] || "";
-      try {
-        let q = OP1("dpkg", ["-S", K], {
-          encoding: "utf8",
-          timeout: 5000,
-          stdio: ["ignore", "pipe", "pipe"],
-        });
-        if (q.status === 0 && q.stdout)
-          return (h(`Detected deb installation: ${q.stdout.trim()}`), !0);
-      } catch {}
+      let K = process.execPath || process.argv[0] || "",
+        q = await L6("dpkg", ["-S", K], { timeout: 5000, useCwd: !1 });
+      if (q.code === 0 && q.stdout)
+        return (h(`Detected deb installation: ${q.stdout.trim()}`), !0);
       return !1;
     })),
-    (By6 = K6(() => {
+    (ZI6 = a1(async () => {
       if (s6() !== "linux") return !1;
-      let K = process.execPath || process.argv[0] || "";
-      try {
-        let q = OP1("rpm", ["-qf", K], {
-          encoding: "utf8",
-          timeout: 5000,
-          stdio: ["ignore", "pipe", "pipe"],
-        });
-        if (q.status === 0 && q.stdout)
-          return (h(`Detected rpm installation: ${q.stdout.trim()}`), !0);
-      } catch {}
+      let K = process.execPath || process.argv[0] || "",
+        q = await L6("rpm", ["-qf", K], { timeout: 5000, useCwd: !1 });
+      if (q.code === 0 && q.stdout)
+        return (h(`Detected rpm installation: ${q.stdout.trim()}`), !0);
       return !1;
     })),
-    (my6 = K6(() => {
+    (GI6 = a1(async () => {
       if (s6() !== "linux") return !1;
-      let K = process.execPath || process.argv[0] || "";
-      try {
-        let q = OP1("apk", ["info", "--who-owns", K], {
-          encoding: "utf8",
+      let K = process.execPath || process.argv[0] || "",
+        q = await L6("apk", ["info", "--who-owns", K], {
           timeout: 5000,
-          stdio: ["ignore", "pipe", "pipe"],
+          useCwd: !1,
         });
-        if (q.status === 0 && q.stdout)
-          return (h(`Detected apk installation: ${q.stdout.trim()}`), !0);
-      } catch {}
+      if (q.code === 0 && q.stdout)
+        return (h(`Detected apk installation: ${q.stdout.trim()}`), !0);
       return !1;
     })),
-    (BMA = K6(() => {
+    (KMA = a1(async () => {
       if (XP1()) return "homebrew";
       if (by6()) return "winget";
-      if (xy6()) return "pacman";
-      if (my6()) return "apk";
-      if (uy6()) return "deb";
-      if (By6()) return "rpm";
+      if (await $I6()) return "pacman";
+      if (await GI6()) return "apk";
+      if (await _I6()) return "deb";
+      if (await ZI6()) return "rpm";
       return "unknown";
     })));
 });

@@@ function 'LkK' (was 'cEK') — structural (42.4%)
--- pretty-v2.1.20.js:540760
+++ pretty-v2.1.21.js:538743
@@ -1,22 +1,11 @@
 function cEK(A) {
-  let K = s(5),
-    { onDone: q } = A;
-  k8();
-  let Y;
+  let K = s(7),
+    { onDone: q } = A,
+    Y;
   if (K[0] === Symbol.for("react.memo_cache_sentinel"))
-    ((Y = { context: "Confirmation" }), (K[0] = Y));
-  else Y = K[0];
-  s1("confirm:no", q, Y);
-  let z;
-  if (K[1] === Symbol.for("react.memo_cache_sentinel"))
     ((z = Ie.default.createElement(
       I,
-      { marginBottom: 1, flexDirection: "column" },
-      Ie.default.createElement(
-        f,
-        { bold: !0 },
-        "You've spent $5 on the Anthropic API this session.",
-      ),
+      { flexDirection: "column" },
       Ie.default.createElement(
         f,
         null,
@@ -26,31 +15,32 @@
         url: "https://code.claude.com/docs/en/costs",
       }),
     )),
-      (K[1] = z));
+      (K[0] = Y));
+  else Y = K[0];
+  let z;
+  if (K[1] === Symbol.for("react.memo_cache_sentinel"))
+    ((z = [{ value: "ok", label: "Got it, thanks!" }]), (K[1] = z));
   else z = K[1];
   let w;
-  if (K[2] === Symbol.for("react.memo_cache_sentinel"))
-    ((w = [{ value: "ok", label: "Got it, thanks!" }]), (K[2] = w));
-  else w = K[2];
+  if (K[2] !== q)
+    ((w = vVA.default.createElement(k6, { options: z, onChange: q })),
+      (K[2] = q),
+      (K[3] = w));
+  else w = K[3];
   let H;
-  if (K[3] !== q)
+  if (K[4] !== q || K[5] !== w)
     ((H = Ie.default.createElement(
       I,
       {
-        flexDirection: "column",
-        borderStyle: "round",
-        padding: 1,
-        borderDimColor: !0,
+        title: "You've spent $5 on the Anthropic API this session.",
+        onCancel: q,
       },
       z,
-      Ie.default.createElement(
-        I,
-        null,
-        Ie.default.createElement(y6, { options: w, onChange: q }),
-      ),
+      w,
     )),
-      (K[3] = q),
-      (K[4] = H));
-  else H = K[4];
+      (K[4] = q),
+      (K[5] = w),
+      (K[6] = H));
+  else H = K[6];
   return H;
 }

@@@ function 'wZK' (was 'V_K') — structural (40.9%)
--- pretty-v2.1.20.js:486033
+++ pretty-v2.1.21.js:484197
@@ -1,7 +1,6 @@
 function V_K(A) {
-  let K = s(20),
+  let K = s(11),
     { onComplete: q } = A,
-    Y = k8(),
     z;
   if (K[0] !== q)
     ((z = (P) => {
@@ -24,113 +23,47 @@
   let J = H,
     O;
   if (K[4] === Symbol.for("react.memo_cache_sentinel"))
-    ((O = { context: "Confirmation" }), (K[4] = O));
-  else O = K[4];
-  s1("confirm:no", J, O);
-  let X;
-  if (K[5] === Symbol.for("react.memo_cache_sentinel"))
     ((X = [
       { label: "Yes", value: "yes" },
       { label: "No", value: "no" },
     ]),
-      (K[5] = X));
-  else X = K[5];
+      (K[4] = J));
+  else J = K[4];
   let $ = X,
     _;
-  if (K[6] === Symbol.for("react.memo_cache_sentinel"))
-    ((_ = eH.default.createElement(
-      I,
-      { marginBottom: 1 },
-      eH.default.createElement(
-        f,
-        { color: "ide" },
-        "Do you wish to disable auto-connect to IDE?",
-      ),
-    )),
+  if (K[5] !== z)
+    ((X = k9A.default.createElement(k6, {
+      options: O,
+      onChange: z,
+      defaultValue: "yes",
+    })),
+      (K[5] = z),
       (K[6] = _));
   else _ = K[6];
   let Z;
-  if (K[7] !== w)
+  if (K[7] === Symbol.for("react.memo_cache_sentinel"))
     ((Z = eH.default.createElement(
       I,
-      { flexDirection: "column", paddingX: 1 },
-      eH.default.createElement(y6, {
-        options: $,
-        onChange: w,
-        defaultValue: "yes",
-      }),
+      { dimColor: !0 },
+      "You can also configure this in /config",
     )),
-      (K[7] = w),
-      (K[8] = Z));
-  else Z = K[8];
-  let G;
-  if (K[9] === Symbol.for("react.memo_cache_sentinel"))
-    ((G = eH.default.createElement(
-      I,
-      { marginTop: 1 },
-      eH.default.createElement(
-        f,
-        { dimColor: !0 },
-        "You can also configure this in /config",
-      ),
-    )),
-      (K[9] = G));
-  else G = K[9];
+      (K[7] = $));
+  else $ = K[7];
   let W;
-  if (K[10] !== Z)
+  if (K[8] !== H || K[9] !== X)
     ((W = eH.default.createElement(
       I,
       {
-        flexDirection: "column",
-        borderStyle: "round",
-        borderColor: "ide",
-        paddingX: 2,
-        paddingY: 1,
-        width: "100%",
+        title: "Do you wish to disable auto-connect to IDE?",
+        color: "ide",
+        onCancel: H,
       },
       _,
       Z,
-      G,
     )),
-      (K[10] = Z),
-      (K[11] = W));
-  else W = K[11];
-  let D;
-  if (K[12] !== Y.keyName || K[13] !== Y.pending)
-    ((D = Y.pending
-      ? eH.default.createElement(
-          eH.default.Fragment,
-          null,
-          "Press ",
-          Y.keyName,
-          " again to exit",
-        )
-      : "Enter to confirm"),
-      (K[12] = Y.keyName),
-      (K[13] = Y.pending),
-      (K[14] = D));
-  else D = K[14];
-  let M;
-  if (K[15] !== D)
-    ((M = eH.default.createElement(
-      I,
-      { paddingX: 1 },
-      eH.default.createElement(f, { dimColor: !0 }, D),
-    )),
-      (K[15] = D),
-      (K[16] = M));
-  else M = K[16];
-  let j;
-  if (K[17] !== M || K[18] !== W)
-    ((j = eH.default.createElement(
-      I,
-      { marginTop: 1, flexDirection: "column" },
-      W,
-      M,
-    )),
-      (K[17] = M),
-      (K[18] = W),
-      (K[19] = j));
-  else j = K[19];
+      (K[8] = H),
+      (K[9] = X),
+      (K[10] = _));
+  else _ = K[10];
   return j;
 }

@@@ function 'AK6' (was 'h76') — structural (40.0%)
--- pretty-v2.1.20.js:176357
+++ pretty-v2.1.21.js:176510
@@ -1,9 +1,22 @@
-function h76(A, K) {
-  let q = [],
-    Y = A.width,
+function AK6(A, K, q) {
+  let Y = A.width,
     z = K.width,
     w = A.height,
     H = K.height,
+    J = A.chars,
+    O = K.chars,
+    X = A.charStrings,
+    $ = K.charStrings,
+    _ = A.styleIds,
+    Z = K.styleIds,
+    G = A.widths,
+    W = K.widths,
+    D = A.hyperlinkIds,
+    j = K.hyperlinkIds,
+    M = A.hyperlinks,
+    P = K.hyperlinks,
+    V = A.emptyStyleId,
+    N = K.emptyStyleId,
     J;
   if (Y === 0 && w === 0) J = { x: 0, y: 0, width: z, height: H };
   else if (K.damage) {
@@ -15,30 +28,48 @@
   let O = Math.max(w, H),
     X = Math.max(Y, z),
     $ = Math.min(J.y + J.height, O),
-    _ = Math.min(J.x + J.width, X);
-  for (let Z = J.y; Z < $; Z++)
-    for (let G = J.x; G < _; G++) {
-      let W = Z < w && G < Y,
-        D = Z < H && G < z;
-      if (!W && !D) continue;
-      let M = W ? Z * Y + G : -1,
-        j = D ? Z * z + G : -1;
-      if (W && D) {
-        let N = A.charStrings[A.chars[M]],
-          T = K.charStrings[K.chars[j]],
-          k = A.hyperlinks[A.hyperlinkIds[M]],
-          R = K.hyperlinks[K.hyperlinkIds[j]],
-          b = A.styleIds[M],
-          S = K.styleIds[j],
-          B = b === QOA ? A.emptyStyleId : b,
-          x = S === QOA ? K.emptyStyleId : S;
-        if (N === T && B === x && A.widths[M] === K.widths[j] && k === R)
-          continue;
+    S = Math.min(T.x + T.width, R),
+    B = { char: " ", styleId: 0, width: 0, hyperlink: void 0 },
+    x = { char: " ", styleId: 0, width: 0, hyperlink: void 0 },
+    F = T.y * Y + T.x,
+    Q = T.y * z + T.x;
+  for (let u = T.y; u < b; u++) {
+    let d = u < w,
+      o = u < H,
+      l = d ? Math.min(S, Y) : T.x,
+      e = o ? Math.min(S, z) : T.x,
+      wA = Math.min(l, e),
+      HA = F,
+      OA = Q;
+    for (let WA = T.x; WA < wA; WA++, HA++, OA++) {
+      let a = X[J[HA]],
+        _A = $[O[OA]],
+        jA = M[D[HA]],
+        PA = P[j[OA]],
+        SA = _[HA],
+        mA = Z[OA];
+      if (
+        a === _A &&
+        (SA === fQ ? V : SA) === (mA === fQ ? N : mA) &&
+        G[HA] === W[OA] &&
+        jA === PA
+      )
+        continue;
+      if ((J51(A, HA, B), J51(K, OA, x), q(WA, u, B, x))) return !0;
+    }
+    if (l > wA) {
+      HA = F + (wA - T.x);
+      for (let WA = wA; WA < l; WA++, HA++)
+        if ((J51(A, HA, B), q(WA, u, B, void 0))) return !0;
+    }
+    if (e > wA) {
+      OA = Q + (wA - T.x);
+      for (let WA = wA; WA < e; WA++, OA++) {
+        if (Z[OA] === fQ) continue;
+        if ((J51(K, OA, x), q(WA, u, void 0, x))) return !0;
       }
-      if (!W && D && A04(K, j)) continue;
-      let P = W ? XQ(A, G, Z) : void 0,
-        V = D ? XQ(K, G, Z) : void 0;
-      q.push([{ x: G, y: Z }, P, V]);
     }
-  return q;
+    ((F += Y), (Q += z));
+  }
+  return !1;
 }

=== String Changes ===

@@@ function 'm4K' (was 'U8K') — string-only
--- pretty-v2.1.20.js:413623
+++ pretty-v2.1.21.js:414235
@@ -185,7 +185,7 @@
 
 Teammates should:
 1. Check TaskList periodically, **especially after completing each task**, to find available work or see newly unblocked tasks
-2. Claim unassigned, unblocked tasks with TaskUpdate (set \`owner\` to your name)
+2. Claim unassigned, unblocked tasks with TaskUpdate (set \`owner\` to your name). **Prefer tasks in ID order** (lowest ID first) when multiple tasks are available, as earlier tasks often set up context for later ones
 3. Create new tasks with \`TaskCreate\` when identifying additional work
 4. Mark tasks as completed with \`TaskUpdate\` when done, then check TaskList for next work
 5. Coordinate with other teammates by reading the task list status
