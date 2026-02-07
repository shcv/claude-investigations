--- archive/claude-code/pretty/pretty-v2.1.32.js
+++ archive/claude-code/pretty/pretty-v2.1.33.js
Structural similarity: 98.1%
Matched: 14534/14605 vs 14809
Changes: 275 added, 71 removed, 812 structural, 37 string-only (13685 unchanged)

Filtered: 53 version bumps, 584 reformatting-only changes

=== Import Style Changes ===

"child_process":
  - import s09 from "child_process";
  - import t09 from "child_process";
  + import { execFile as F9K, spawn as Q9K, spawnSync as U9K } from "child_process";
  + import { spawn as yD5, spawnSync as CD5 } from "child_process";

"crypto":
  - import Uw9 from "crypto";
  - import pw9 from "crypto";
  + import { randomBytes as _9z, randomUUID as J9z } from "crypto";
  + import { randomBytes as Z0z, timingSafeEqual as f0z } from "crypto";

"https":
  - import xu7 from "https";
  + import { Agent as RK5 } from "https";

"node:child_process":
  - import WL6 from "node:child_process";
  - import wU7 from "node:child_process";
  + import { execFile as os5, execFileSync as pF2 } from "node:child_process";
  + import { execFileSync as tgY, spawn as egY } from "node:child_process";

"node:fs":
  - import M09 from "node:fs";
  - import P09 from "node:fs";
  + import {
  +   existsSync as pU1,
  +   statSync as QgY,
  +   mkdirSync as UgY,
  +   realpathSync as ggY,
  + } from "node:fs";
  + import {
  +   constants as rgY,
  +   readFileSync as ogY,
  +   existsSync as agY,
  +   unlinkSync as sgY,
  + } from "node:fs";

"node:os":
  - import G09 from "node:os";
  + import { homedir as HMz } from "node:os";

"node:path":
  - import zU7 from "node:path";
  + import {
  +   join as vJ,
  +   dirname as Sd,
  +   resolve as jm,
  +   delimiter as _lY,
  +   basename as JlY,
  + } from "node:path";

"node:process":
  - import THq from "node:process";
  + import { cwd as U67 } from "node:process";

"node:util":
  - import V99 from "node:util";
  + import { isDeepStrictEqual as N7q } from "node:util";

"stream":
  - import gz1 from "stream";
  + import { PassThrough as aXz } from "stream";

=== Removed ===

--- Removed ST1 (pretty-v2.1.32.js:73353-73355)
- function ST1(A, q) {
-   return q.autoUpdate ?? sN.has(A.toLowerCase());
- }

--- Removed GD7 (pretty-v2.1.32.js:168920-169104)
- var GD7 = v(() => {
-   MD7 = `Use this tool to create and manage a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user.
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
- * Uses the ${aq} tool to add a comment to the calculateTotal function *
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

--- Removed Uz6 (pretty-v2.1.32.js:246357-246357)
-   Uz6 = "Invalid API key · Please run /login",

--- Removed ROA (pretty-v2.1.32.js:248725-248741)
- function ROA(A) {
-   let q = $o.useContext(qC1),
-     [K, Y] = $o.useState(() => q?.getTime() ?? 0),
-     [z] = $o.useState(() => Symbol("animation-timer"));
-   return (
-     $o.useEffect(() => {
-       if (!q) return;
-       let w = q.getTime(),
-         H = () => {
-           let O = q.getTime();
-           if (O - w >= A) ((w = O), Y(O));
-         };
-       return q.subscribe(z, !1, H);
-     }, [q, z, A]),
-     K
-   );
- }

--- Removed d41 (pretty-v2.1.32.js:250233-250304)
- var d41 = v(() => {
-   N3();
-   zo();
-   CI1();
-   IOA();
-   FA();
-   Z5();
-   Rq();
-   eA();
-   I6();
-   Pw();
-   k6();
-   u1();
-   u3();
-   I6();
-   bOA();
-   II1 = {
-     ghostty: "Ghostty",
-     kitty: "Kitty",
-     "iTerm.app": "iTerm2",
-     WezTerm: "WezTerm",
-   };
-   uZ9 = {
-     type: "local-jsx",
-     name: "terminal-setup",
-     userFacingName() {
-       return "terminal-setup";
-     },
-     description:
-       mA.terminal === "Apple_Terminal"
-         ? "Enable Option+Enter key binding for newlines and visual bell"
-         : "Install Shift+Enter key binding for newlines",
-     isEnabled: () => !0,
-     isHidden: bZ9(),
-     async call(A, q, K) {
-       if (mA.terminal && mA.terminal in II1) {
-         let z = `Shift+Enter is natively supported in ${II1[mA.terminal]}.
- 
- No configuration needed. Just use Shift+Enter to add newlines.`;
-         return (A(z), null);
-       }
-       if (!xI1()) {
-         let z = mA.terminal || "your current terminal",
-           w = iA(),
-           H = "";
-         if (w === "macos")
-           H = `   • macOS: Apple Terminal
- `;
-         else if (w === "windows")
-           H = `   • Windows: Windows Terminal
- `;
-         let O = `Terminal setup cannot be run from ${z}.
- 
- This command configures a convenient Shift+Enter shortcut for multi-line prompts.
- ${Y6.dim("Note: You can already use backslash (\\\\) + return to add newlines.")}
- 
- To set up the shortcut (optional):
- 1. Exit tmux/screen temporarily
- 2. Run /terminal-setup directly in one of these terminals:
- ${H}   • IDE: VSCode, Cursor, Windsurf, Zed
-    • Other: Alacritty, Warp
- 3. Return to tmux/screen - settings will persist
- 
- ${Y6.dim("Note: iTerm2, WezTerm, Ghostty, and Kitty support Shift+Enter natively.")}`;
-         return (A(O), null);
-       }
-       let Y = await FOA(q.options.theme);
-       return (A(Y), null);
-     },
-   };
-   p41 = uZ9;
- });

--- Removed Qo (pretty-v2.1.32.js:274213-274232)
- var Qo = v(() => {
-   g4();
-   _O6();
-   F6();
-   BA();
-   ((zA4 = `Search for or select deferred tools to make them available for use.
- 
- **MANDATORY PREREQUISITE - THIS IS A HARD REQUIREMENT**
- 
- You MUST use this tool to load deferred tools BEFORE calling them directly.
- 
- This is a BLOCKING REQUIREMENT - deferred tools listed below are NOT available until you load them using this tool. Both query modes (keyword search and direct selection) load the returned tools — once a tool appears in the results, it is immediately available to call.${wA4}`),
-     (Ix9 = `Search for or select deferred tools to make them available for use.
- 
- **MANDATORY PREREQUISITE - THIS IS A HARD REQUIREMENT**
- 
- You MUST use this tool to load deferred tools BEFORE calling them directly.
- 
- This is a BLOCKING REQUIREMENT - deferred tools are NOT available until you load them using this tool. Look for <available-deferred-tools> messages in the conversation for the list of tools you can discover. Both query modes (keyword search and direct selection) load the returned tools — once a tool appears in the results, it is immediately available to call.${wA4}`));
- });

--- Removed wu1 (pretty-v2.1.32.js:295655-295686)
- var wu1 = v(() => {
-   W_();
-   _6();
-   k6();
-   W_();
-   er1();
-   Wz();
-   DjA = qA(async (A) => {
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
- - If you see a <${Hf}> tag in the current conversation turn, the skill has ALREADY been loaded - follow the instructions directly instead of calling this tool again
- `;
-   });
- });

--- Removed BV (pretty-v2.1.32.js:297186-297186)
- var BV = "Teammate",

--- Removed VMA (pretty-v2.1.32.js:302250-302254)
- function VMA(A) {
-   if (typeof A !== "string") return null;
-   if (Pz4.test(A) || Gl9.test(A)) return A;
-   return null;
- }

--- Removed sS (pretty-v2.1.32.js:302260-302263)
- var sS = v(() => {
-   ((Pz4 = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i),
-     (Gl9 = /^[a-z][a-z0-9]*(_[a-z][a-z0-9]*)*_[0-9A-Za-z]+$/));
- });

--- Removed x06 (pretty-v2.1.32.js:355559-355597)
- var x06 = v(() => {
-   FA();
-   u1();
-   D7();
-   ga1();
-   cE();
-   ai();
-   $w();
-   uj1();
-   tfA();
-   Xm1();
-   PV();
-   g4();
-   HVA = a($1(), 1);
-   JE4 = {
-     type: "local-jsx",
-     name: "logout",
-     description: "Sign out from your Anthropic account",
-     isEnabled: () => !process.env.DISABLE_LOGOUT_COMMAND,
-     isHidden: !1,
-     async call() {
-       await OVA({ clearOnboarding: !0 });
-       let A = HVA.createElement(
-         f,
-         null,
-         "Successfully logged out from your Anthropic account.",
-       );
-       return (
-         setTimeout(() => {
-           O3(0, "logout");
-         }, 200),
-         A
-       );
-     },
-     userFacingName() {
-       return "logout";
-     },
-   };
- });

--- Removed IE4 (pretty-v2.1.32.js:357779-357782)
- function IE4() {
-   let A = process.env.HOME || process.env.USERPROFILE || ".";
-   return g06(A, ".claude", "teams");
- }

--- Removed ML4 (pretty-v2.1.32.js:366426-366432)
- function ML4() {
-   if (AW1)
-     ((Rs = AW1), h(`[TeammateModeSnapshot] Captured from CLI override: ${Rs}`));
-   else
-     ((Rs = M6().teammateMode ?? "auto"),
-       h(`[TeammateModeSnapshot] Captured from config: ${Rs}`));
- }

--- Removed pL4 (pretty-v2.1.32.js:367657-367666)
- function pL4(A) {
-   switch (A.operation) {
-     case "spawnTeam":
-       return `create team: ${A.team_name}`;
-     case "cleanup":
-       return `cleanup team: ${A.team_name || "current"}`;
-     default:
-       return "teammate operation";
-   }
- }

--- Removed SDY (pretty-v2.1.32.js:367676-367678)
- function SDY(A) {
-   return "team_name" in A && "lead_agent_id" in A;
- }

--- Removed BDY (pretty-v2.1.32.js:367735-367738)
- function BDY() {
-   let A = process.env.HOME || process.env.USERPROFILE || ".";
-   return bp(A, ".claude", "teams");
- }

--- Removed FDY (pretty-v2.1.32.js:367802-367812)
- function FDY(A, q) {
-   let K = f_(A);
-   if (!K) return !1;
-   let Y = K.hiddenPaneIds ?? [];
-   if (!Y.includes(q))
-     (Y.push(q),
-       (K.hiddenPaneIds = Y),
-       up(A, K),
-       h(`[TeammateTool] Added ${q} to hidden panes for team ${A}`));
-   return !0;
- }

--- Removed QDY (pretty-v2.1.32.js:367813-367824)
- function QDY(A, q) {
-   let K = f_(A);
-   if (!K) return !1;
-   let Y = K.hiddenPaneIds ?? [],
-     z = Y.indexOf(q);
-   if (z !== -1)
-     (Y.splice(z, 1),
-       (K.hiddenPaneIds = Y),
-       up(A, K),
-       h(`[TeammateTool] Removed ${q} from hidden panes for team ${A}`));
-   return !0;
- }

--- Removed gDY (pretty-v2.1.32.js:367858-367868)
- function gDY(A, q, K, Y) {
-   let z = f_(A);
-   if (!z) return !1;
-   let w = z.teamAllowedPaths ?? [];
-   if (!w.some((O) => O.path === q && O.toolName === K))
-     (w.push({ path: q, toolName: K, addedBy: Y, addedAt: Date.now() }),
-       (z.teamAllowedPaths = w),
-       up(A, z),
-       h(`[TeammateTool] Added team-wide allowed path ${q} for ${K} (by ${Y})`));
-   return !0;
- }

--- Removed pDY (pretty-v2.1.32.js:368000-368032)
- async function pDY(A, q) {
-   let { setAppState: K, getAppState: Y } = q,
-     w = (await Y()).teamContext?.teamName;
-   if (w) {
-     let H = f_(w);
-     if (H) {
-       let O = H.members.filter(($) => $.name !== h2);
-       if (O.length > 0) {
-         let $ = O.map((_) => _.name).join(", ");
-         return {
-           data: {
-             success: !1,
-             message: `Cannot cleanup team with ${O.length} active member(s): ${$}. Use requestShutdown to gracefully terminate teammates first.`,
-             team_name: w,
-           },
-         };
-       }
-     }
-     (await tL4(w), BL4(), kD7());
-   }
-   return (
-     K((H) => ({ ...H, teamContext: void 0, inbox: { messages: [] } })),
-     {
-       data: {
-         success: !0,
-         message: w
-           ? `Cleaned up directories and worktrees for team "${w}"`
-           : "No team name found, nothing to clean up",
-         team_name: w,
-       },
-     }
-   );
- }

--- Removed dDY (pretty-v2.1.32.js:368033-368095)
- async function dDY(A, q) {
-   let { setAppState: K, getAppState: Y } = q,
-     { team_name: z, description: w, agent_type: H } = A;
-   if (!z) throw Error("team_name is required for spawnTeam operation");
-   let O = await Y(),
-     $ = O.teamContext?.teamName;
-   if ($)
-     throw Error(
-       `Already leading team "${$}". A leader can only manage one team at a time. Use cleanup operation to end the current team before creating a new one.`,
-     );
-   let _ = mDY(z),
-     J = Wv(h2, _),
-     X = H || h2,
-     D = s9(O.mainLoopModelForSession ?? O.mainLoopModel ?? bk()),
-     j = AF1(_),
-     M = bp(j, "config.json"),
-     W = {
-       name: _,
-       description: w,
-       createdAt: Date.now(),
-       leadAgentId: J,
-       leadSessionId: u6(),
-       members: [
-         {
-           agentId: J,
-           name: h2,
-           agentType: X,
-           model: D,
-           joinedAt: Date.now(),
-           tmuxPaneId: "",
-           cwd: y6(),
-           subscriptions: [],
-         },
-       ],
-     };
-   up(_, W);
-   let G = mD6(_);
-   return (
-     Nq6(G),
-     Sy1(G),
-     ED7(mD6(_)),
-     K((P) => ({
-       ...P,
-       teamContext: {
-         teamName: _,
-         teamFilePath: M,
-         leadAgentId: J,
-         teammates: {
-           [J]: {
-             name: h2,
-             agentType: X,
-             color: xp(J),
-             tmuxSessionName: "",
-             tmuxPaneId: "",
-             cwd: y6(),
-             spawnedAt: Date.now(),
-           },
-         },
-       },
-     })),
-     { data: { team_name: _, team_file_path: M, lead_agent_id: J } }
-   );
- }

--- Removed Zv (pretty-v2.1.32.js:368097-368183)
- var Zv = v(() => {
-   A4();
-   R$6();
-   I6();
-   hD6();
-   Rq();
-   Z7();
-   oz();
-   nL4();
-   uO();
-   _6();
-   a6();
-   Q7();
-   I6();
-   N9();
-   a9();
-   aL4 = B.strictObject({
-     operation: B.enum(["spawnTeam", "cleanup"]).describe(
-       "Operation: spawnTeam to create a team, cleanup to remove team and task directories.",
-     ),
-     agent_type: B.string()
-       .optional()
-       .describe(
-         'Type/role of the team lead (e.g., "researcher", "test-runner"). Used for team file and inter-agent coordination.',
-       ),
-     team_name: B.string()
-       .optional()
-       .describe("Name for the new team to create (required for spawnTeam)."),
-     description: B.string()
-       .optional()
-       .describe("Team description/purpose (only used with spawnTeam)."),
-   });
-   cDY = {
-     name: BV,
-     maxResultSizeChars: 1e5,
-     userFacingName() {
-       return "";
-     },
-     inputSchema: aL4,
-     isEnabled() {
-       return F8();
-     },
-     isConcurrencySafe(A) {
-       return !1;
-     },
-     isReadOnly(A) {
-       return !1;
-     },
-     async checkPermissions(A, q) {
-       return { behavior: "allow", updatedInput: A };
-     },
-     async validateInput(A, q) {
-       if (A.operation === "spawnTeam") {
-         if (!A.team_name || A.team_name.trim().length === 0)
-           return {
-             result: !1,
-             message: "team_name is required for spawnTeam operation",
-             errorCode: 9,
-           };
-       }
-       return { result: !0 };
-     },
-     async description() {
-       return "Spawn teammates and coordinate with other agents running in parallel";
-     },
-     async prompt() {
-       return UL4();
-     },
-     mapToolResultToToolResultBlockParam(A, q) {
-       return {
-         tool_use_id: q,
-         type: "tool_result",
-         content: [{ type: "text", text: g1(A, null, 2) }],
-       };
-     },
-     async call(A, q) {
-       if (A.operation === "spawnTeam") return dDY(A, q);
-       if (A.operation === "cleanup") return pDY(A, q);
-       throw Error(`Unknown operation: ${A.operation}`);
-     },
-     renderToolUseMessage: pL4,
-     renderToolUseProgressMessage: dL4,
-     renderToolUseRejectedMessage: cL4,
-     renderToolUseErrorMessage: lL4,
-     renderToolResultMessage: iL4,
-   };
- });

--- Removed LF1 (pretty-v2.1.32.js:380382-380471)
- var LF1 = v(() => {
-   k6();
-   D7();
-   YG();
-   Zj6();
-   FA();
-   CI4();
-   ((SI4 = a($1(), 1)),
-     (pGY = {
-       type: "local-jsx",
-       name: "extra-usage",
-       description: "Configure extra usage to keep working when limits are hit",
-       isEnabled: () => {
-         if (process.env.DISABLE_EXTRA_USAGE_COMMAND) return !1;
-         if (!JC()) return !1;
-         if (DS()) return !0;
-         let A = TK();
-         return A === "pro" || A === "max";
-       },
-       isHidden: !1,
-       async call(A, q) {
-         if (!M6().hasVisitedExtraUsage)
-           OA(($) => ({ ...$, hasVisitedExtraUsage: !0 }));
-         let K = TK(),
-           Y = K === "team" || K === "enterprise",
-           z = ju(),
-           w = DS(),
-           H = z3()?.hasExtraUsageEnabled === !0;
-         if (!z && Y) {
-           if (w) {
-             try {
-               let $ = await yI4("limit_increase", ["pending", "dismissed"]);
-               if ($ && $.length > 0)
-                 return (
-                   A(
-                     "You have already submitted a request for extra usage to your admin.",
-                   ),
-                   null
-                 );
-             } catch ($) {
-               K1($);
-             }
-             try {
-               return (
-                 await RI4({ request_type: "limit_increase", details: null }),
-                 A(
-                   H
-                     ? "Request sent to your admin to increase extra usage."
-                     : "Request sent to your admin to enable extra usage.",
-                 ),
-                 null
-               );
-             } catch ($) {
-               K1($);
-             }
-           }
-           return (
-             A("Please contact your admin to manage extra usage settings."),
-             null
-           );
-         }
-         let O = Y
-           ? "https://claude.ai/admin-settings/usage"
-           : "https://claude.ai/settings/usage";
-         try {
-           return (
-             await NY(O),
-             SI4.default.createElement(vF1, {
-               startingMessage:
-                 "Starting new login following /extra-usage. Exit with Ctrl-C to use existing account.",
-               onDone: ($) => {
-                 (q.onChangeAPIKey(),
-                   A($ ? "Login successful" : "Login interrupted"));
-               },
-             })
-           );
-         } catch ($) {
-           (K1($),
-             A(
-               `Failed to open browser. Please visit ${O} to see your extra usage.`,
-             ));
-         }
-         return null;
-       },
-       userFacingName() {
-         return "extra-usage";
-       },
-     }),
-     (pp = pGY));
- });

--- Removed APY (pretty-v2.1.32.js:387264-387270)
- function APY(A) {
-   if (A.completedTaskId) {
-     let q = A.completedStatus || "completed";
-     return `Agent idle · Task ${A.completedTaskId} ${q}`;
-   }
-   return "Agent idle";
- }

--- Removed mPY (pretty-v2.1.32.js:391224-391227)
- function mPY() {
-   let A = process.env.HOME || process.env.USERPROFILE || ".";
-   return uj6(A, ".claude", "teams");
- }

--- Removed Ep4 (pretty-v2.1.32.js:418947-419100)
- var Ep4 = v(() => {
-   ((GLY = `Use this tool proactively when you're about to start a non-trivial implementation task. Getting user sign-off on your approach before writing code prevents wasted effort and ensures alignment. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
-    - If you would use ${kw} to clarify the approach, use EnterPlanMode instead
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
- 5. Use ${kw} if you need to clarify approaches
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
-     (MqH = `Use this tool when a task has genuine ambiguity about the right approach and getting user input before coding would prevent significant rework. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
- When in doubt, prefer starting work and using ${kw} for specific questions over entering a full planning phase.
- 
- ## What Happens in Plan Mode
- 
- In plan mode, you'll:
- 1. Explore the codebase using Glob, Grep, and Read tools
- 2. Understand existing patterns and architecture
- 3. Design an implementation approach
- 4. Present your plan to the user for approval
- 5. Use ${kw} if you need to clarify approaches
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

--- Removed od4 (pretty-v2.1.32.js:422365-422367)
- async function od4(A, q, K) {
-   return (A.load ? (await A.load()).call : A.call)(q, K);
- }

--- Removed HG1 (pretty-v2.1.32.js:422368-422370)
- async function HG1(A, q, K, Y) {
-   return (A.load ? (await A.load()).call : A.call)(q, K, Y);
- }

--- Removed xbY (pretty-v2.1.32.js:435077-435099)
-   xbY = `[SUGGESTION MODE: You are suggesting for a coordinator orchestrating workers.]
- 
- The user manages workers via the Task tool. Worker results arrive as <task-notification> messages that look like user messages but aren't.
- 
- FIRST: Check the conversation state.
- - Did a worker just report results? -> Suggest the coordinator's next action
- - Are workers still running? -> Silence (let them finish)
- - Did the user just give an instruction? -> Silence (coordinator is executing)
- 
- COORDINATOR ACTIONS (suggest these):
- - After worker research: "let me synthesize and implement the fix"
- - After worker implementation: "verify the changes" or "run the tests"
- - After all workers done: "commit the changes" or "create the PR"
- - After worker failure: a specific corrective instruction
- 
- NEVER SUGGEST:
- - Generic coding actions ("fix the bug", "add a test") — the coordinator delegates, not does
- - Questions or evaluative phrases
- - Claude-voice ("Let me...", "I'll...")
- - Actions the coordinator already started
- 
- Format: 2-12 words, match the user's style. Or nothing.
- Reply with ONLY the suggestion, no quotes or explanation.`,

--- Removed QyA (pretty-v2.1.32.js:443575-443579)
- function QyA(A) {
-   if ((A.type !== "assistant" && A.type !== "user") || !A.message?.content)
-     return 0;
-   return Va4(A.message?.content);
- }

--- Removed Ye4 (pretty-v2.1.32.js:452926-452974)
- function Ye4(A) {
-   let q = A1(4),
-     { text: K, highlights: Y } = A,
-     w = Ae4(K, Y === void 0 ? [] : Y),
-     H = tK1("requesting", K, !0, !1),
-     O;
-   if (q[0] !== H)
-     ((O = (J, X) => {
-       if (!J.highlight)
-         return SX.createElement(
-           f,
-           { key: X },
-           SX.createElement(R3, null, J.text),
-         );
-       let { style: D } = J.highlight;
-       if (D.type === "shimmer")
-         return J.text.split("").map((j, M) => {
-           let W = J.start + M;
-           return SX.createElement(Gm1, {
-             key: `${X}-${M}`,
-             char: j,
-             index: W,
-             glimmerIndex: H,
-             messageColor: D.baseColor,
-             shimmerColor: D.shimmerColor,
-           });
-         });
-       else if (D.type === "solid")
-         return SX.createElement(
-           f,
-           { key: X, color: D.color },
-           SX.createElement(R3, null, J.text),
-         );
-       return SX.createElement(
-         f,
-         { key: X },
-         SX.createElement(R3, null, J.text),
-       );
-     }),
-       (q[0] = H),
-       (q[1] = O));
-   else O = q[1];
-   let $ = w.map(O),
-     _;
-   if (q[2] !== $)
-     ((_ = SX.createElement(SX.Fragment, null, $)), (q[2] = $), (q[3] = _));
-   else _ = q[3];
-   return _;
- }

--- Removed OZ6 (pretty-v2.1.32.js:453991-454068)
- var OZ6 = v(() => {
-   d1();
-   x7();
-   N3();
-   u1();
-   az();
-   eA();
-   gz();
-   GSA();
-   sq();
-   V$();
-   vz();
-   ((kt = a($1(), 1)), (We4 = a($1(), 1)));
-   ((EUY = {
-     type: "local-jsx",
-     name: "add-dir",
-     description: "Add a new working directory",
-     argumentHint: "<path>",
-     isEnabled: () => !0,
-     isHidden: !1,
-     async call(A, q, K) {
-       B4("multi-directory");
-       let Y = K.trim(),
-         z = await q.getAppState(),
-         w = async (O, $ = !1) => {
-           let J = {
-               type: "addDirectories",
-               directories: [O],
-               destination: $ ? "localSettings" : "session",
-             },
-             X = await q.getAppState(),
-             D = t2(X.toolPermissionContext, J);
-           q.setAppState((W) => ({ ...W, toolPermissionContext: D }));
-           let j;
-           if ($)
-             try {
-               (Lb(J),
-                 (j = `Added ${Y6.bold(O)} as a working directory and saved to local settings`));
-             } catch (W) {
-               j = `Added ${Y6.bold(O)} as a working directory. Failed to save to local settings: ${W instanceof Error ? W.message : "Unknown error"}`;
-             }
-           else
-             j = `Added ${Y6.bold(O)} as a working directory for this session`;
-           let M = `${j} ${Y6.dim("· /permissions to manage")}`;
-           A(M);
-         };
-       if (!Y)
-         return kt.default.createElement(ng1, {
-           permissionContext: z.toolPermissionContext,
-           onAddDirectory: w,
-           onCancel: () => {
-             A("Did not add a working directory.");
-           },
-         });
-       let H = rg1(Y, z.toolPermissionContext);
-       if (H.resultType !== "success") {
-         let O = og1(H);
-         return kt.default.createElement(vUY, {
-           message: O,
-           args: K,
-           onDone: () => A(O),
-         });
-       }
-       return kt.default.createElement(ng1, {
-         directoryPath: H.absolutePath,
-         permissionContext: z.toolPermissionContext,
-         onAddDirectory: w,
-         onCancel: () => {
-           A(`Did not add ${Y6.bold(H.absolutePath)} as a working directory.`);
-         },
-       });
-     },
-     userFacingName() {
-       return "add-dir";
-     },
-   }),
-     (Ge4 = EUY));
- });

--- Removed Ne4 (pretty-v2.1.32.js:454261-454291)
- var Ne4 = v(() => {
-   d1();
-   u1();
-   PSA();
-   aV();
-   qv();
-   WVA();
-   dW();
-   P2();
-   ((nw = a($1(), 1)), (zP1 = a($1(), 1)));
-   ((yUY = {
-     type: "local-jsx",
-     name: "btw",
-     description:
-       "Ask a quick side question without interrupting the main conversation",
-     isEnabled: () => !1,
-     isHidden: !1,
-     immediate: !0,
-     argumentHint: "<question>",
-     async call(A, q, K) {
-       let Y = K?.trim();
-       if (!Y)
-         return (A("Usage: /btw <your question>", { display: "system" }), null);
-       return nw.createElement(LUY, { question: Y, context: q, onDone: A });
-     },
-     userFacingName() {
-       return "btw";
-     },
-   }),
-     (Ve4 = yUY));
- });

--- Removed V6q (pretty-v2.1.32.js:461527-461583)
- function V6q(A) {
-   let q = A1(3),
-     { variant: K } = A;
-   switch (K) {
-     case "promo-copper": {
-       let Y;
-       if (q[0] === Symbol.for("react.memo_cache_sentinel"))
-         ((Y = EG.createElement(
-           f,
-           { dimColor: !0 },
-           EG.createElement(
-             EG.Fragment,
-             null,
-             EG.createElement(
-               f,
-               { color: "claude" },
-               "Opus 4.6 is here · $50 free extra usage",
-             ),
-             " ",
-             "· /extra-usage to enable",
-           ),
-         )),
-           (q[0] = Y));
-       else Y = q[0];
-       return Y;
-     }
-     case "promo": {
-       let Y;
-       if (q[1] === Symbol.for("react.memo_cache_sentinel"))
-         ((Y = EG.createElement(
-           f,
-           { dimColor: !0 },
-           EG.createElement(
-             f,
-             { color: "claude" },
-             "Opus 4.6 is here · $50 free extra usage",
-           ),
-           " · /extra-usage to enable",
-         )),
-           (q[1] = Y));
-       else Y = q[1];
-       return Y;
-     }
-     case "launch-only": {
-       let Y;
-       if (q[2] === Symbol.for("react.memo_cache_sentinel"))
-         ((Y = EG.createElement(
-           f,
-           { dimColor: !0 },
-           "Opus 4.6 is here · Most capable for ambitious work",
-         )),
-           (q[2] = Y));
-       else Y = q[2];
-       return Y;
-     }
-   }
- }

--- Removed u6q (pretty-v2.1.32.js:462919-463002)
- var u6q = v(() => {
-   S6q();
-   wg1();
-   WU1();
-   e31();
-   J8();
-   vz();
-   a6();
-   EO();
-   j3();
-   ((NhA = a($1(), 1)),
-     (x6q = {
-       name: "context",
-       description: "Visualize current context usage as a colored grid",
-       isEnabled: () => !X4(),
-       isHidden: !1,
-       type: "local-jsx",
-       userFacingName() {
-         return this.name;
-       },
-       async call(A, q) {
-         let {
-           messages: K,
-           getAppState: Y,
-           options: { mainLoopModel: z, tools: w },
-         } = q;
-         B4("context");
-         let H = uv(K),
-           { messages: O } = await Dd(H),
-           $ = process.stdout.columns || 80,
-           _ = await Y(),
-           J = await tyA(
-             O,
-             z,
-             async () => _.toolPermissionContext,
-             w,
-             _.agentDefinitions,
-             $,
-             q,
-             void 0,
-             H,
-           ),
-           X = await VhA(NhA.createElement(C6q, { data: J }));
-         return (A(X), null);
-       },
-     }),
-     (b6q = {
-       type: "local",
-       name: "context",
-       supportsNonInteractive: !0,
-       description: "Show current context usage",
-       get isHidden() {
-         return !X4();
-       },
-       isEnabled() {
-         return X4();
-       },
-       userFacingName() {
-         return "context";
-       },
-       async call(A, q) {
-         let {
-             messages: K,
-             getAppState: Y,
-             options: { mainLoopModel: z, tools: w, agentDefinitions: H },
-           } = q,
-           O = uv(K),
-           { messages: $ } = await Dd(O),
-           _ = await Y(),
-           J = await tyA(
-             $,
-             z,
-             async () => _.toolPermissionContext,
-             w,
-             H,
-             void 0,
-             q,
-             void 0,
-             O,
-           );
-         return { type: "text", value: IcY(J) };
-       },
-     }));
- });

--- Removed gAq (pretty-v2.1.32.js:466122-466220)
- var gAq = v(() => {
-   d1();
-   u1();
-   a5();
-   BAq();
-   zO();
-   F6();
-   vz();
-   hq();
-   VP1();
-   Z7();
-   Rq();
-   N3();
-   ((R0 = a($1(), 1)), (Q51 = a($1(), 1)));
-   ((alY = {
-     type: "local-jsx",
-     name: "ide",
-     description: "Manage IDE integrations and show status",
-     isEnabled: () => !0,
-     isHidden: !1,
-     argumentHint: "[open]",
-     async call(A, q, K) {
-       (c("tengu_ext_ide_command", {}), B4("ide-integration"));
-       let {
-           options: { dynamicMcpConfig: Y },
-           onChangeDynamicMcpConfig: z,
-         } = q,
-         w = await ax1(!0);
-       if (w.length === 0 && q.onInstallIDEExtension && !jX()) {
-         let J = await XXA(),
-           X = (D) => {
-             if (q.onInstallIDEExtension)
-               if ((q.onInstallIDEExtension(D), CS(D)))
-                 A(`Installed plugin to ${Y6.bold(D_(D))}
- Please ${Y6.bold("restart your IDE")} completely for it to take effect`);
-               else A(`Installed extension to ${Y6.bold(D_(D))}`);
-           };
-         if (J.length > 1)
-           return R0.default.createElement(rlY, {
-             runningIDEs: J,
-             onSelectIDE: X,
-             onDone: () => {
-               A("No IDE selected.", { display: "system" });
-             },
-           });
-         else if (J.length === 1) {
-           let D = J[0];
-           return R0.default.createElement(() => {
-             let M = A1(1),
-               W;
-             if (M[0] === Symbol.for("react.memo_cache_sentinel"))
-               ((W = []), (M[0] = W));
-             else W = M[0];
-             return (Q51.useEffect(slY, W), null);
-           }, null);
-         }
-       }
-       let H = w.filter((J) => J.isValid),
-         O = w.filter((J) => !J.isValid),
-         $ = await nlY(H, Y);
-       return R0.default.createElement(clY, {
-         availableIDEs: H,
-         unavailableIDEs: O,
-         selectedIDE: $,
-         onClose: () => A("IDE selection cancelled", { display: "system" }),
-         onSelect: async (J) => {
-           try {
-             if (!z) {
-               A("Error connecting to IDE.");
-               return;
-             }
-             let X = { ...(Y || {}) };
-             if ($) delete X.ide;
-             if (!J) A($ ? `Disconnected from ${$.name}.` : "No IDE selected.");
-             else {
-               let D = J.url;
-               ((X.ide = {
-                 type: D.startsWith("ws:") ? "ws-ide" : "sse-ide",
-                 url: D,
-                 ideName: J.name,
-                 authToken: J.authToken,
-                 ideRunningInWindows: J.ideRunningInWindows,
-                 scope: "dynamic",
-               }),
-                 A(`Connected to ${J.name}.`));
-             }
-             z(X);
-           } catch (X) {
-             A("Error connecting to IDE.");
-           }
-         },
-       });
-     },
-     userFacingName() {
-       return "ide";
-     },
-   }),
-     (QAq = alY));
- });

--- Removed U8q (pretty-v2.1.32.js:469412-469446)
- var U8q = v(() => {
-   YG();
-   FA();
-   F6();
-   vz();
-   ((PiY = {
-     type: "local",
-     name: "install-slack-app",
-     description: "Install the Claude Slack app",
-     isEnabled: () => !0,
-     isHidden: !1,
-     supportsNonInteractive: !1,
-     async call() {
-       if (
-         (B4("slack-app"),
-         c("tengu_install_slack_app_clicked", {}),
-         OA((q) => ({
-           ...q,
-           slackAppInstallCount: (q.slackAppInstallCount ?? 0) + 1,
-         })),
-         await NY(Q8q))
-       )
-         return {
-           type: "text",
-           value: "Opening Slack app installation page in browser…",
-         };
-       else
-         return { type: "text", value: `Couldn't open browser. Visit: ${Q8q}` };
-     },
-     userFacingName() {
-       return "install-slack-app";
-     },
-   }),
-     (g8q = PiY));
- });

--- Removed u7q (pretty-v2.1.32.js:479735-479774)
- var u7q = v(() => {
-   d1();
-   s8q();
-   lhA();
-   ut();
-   Q8();
-   YIA();
-   ((xU1 = a($1(), 1)), (Vf6 = a($1(), 1)));
-   ((UnY = {
-     type: "local-jsx",
-     name: "mcp",
-     description: "Manage MCP servers",
-     isEnabled: () => !0,
-     isHidden: !1,
-     argumentHint: "[enable|disable [server-name]]",
-     async call(A, q, K) {
-       if (K) {
-         let Y = K.trim().split(/\s+/);
-         if (Y[0] === "no-redirect")
-           return xU1.default.createElement(Hf6, { onComplete: A });
-         if (Y[0] === "reconnect" && Y[1])
-           return xU1.default.createElement(chA, {
-             serverName: Y.slice(1).join(" "),
-             onComplete: A,
-           });
-         if (Y[0] === "enable" || Y[0] === "disable")
-           return xU1.default.createElement(FnY, {
-             action: Y[0],
-             target: Y.length > 1 ? Y.slice(1).join(" ") : "all",
-             onComplete: A,
-           });
-       }
-       return xU1.default.createElement(Hf6, { onComplete: A });
-     },
-     userFacingName() {
-       return "mcp";
-     },
-   }),
-     (b7q = UnY));
- });

--- Removed AKq (pretty-v2.1.32.js:483400-483427)
- var AKq = v(() => {
-   e51();
-   ((AtY = {
-     description: "View release notes",
-     isEnabled: () => !0,
-     isHidden: !1,
-     name: "release-notes",
-     userFacingName() {
-       return "release-notes";
-     },
-     type: "local",
-     supportsNonInteractive: !0,
-     async call() {
-       let A = [];
-       try {
-         let K = new Promise((Y, z) => {
-           setTimeout(() => z(Error("Timeout")), 500);
-         });
-         (await Promise.race([AxA(), K]), (A = qxA(t51())));
-       } catch {}
-       if (A.length > 0) return { type: "text", value: tqq(A) };
-       let q = qxA();
-       if (q.length > 0) return { type: "text", value: tqq(q) };
-       return { type: "text", value: `See the full changelog at: ${aqq}` };
-     },
-   }),
-     (eqq = AtY));
- });

--- Removed KKq (pretty-v2.1.32.js:483429-483476)
- var KKq = v(() => {
-   Eq();
-   a6();
-   N9();
-   oz();
-   W01();
-   R8();
-   ((qtY = {
-     type: "local",
-     name: "rename",
-     description: "Rename the current conversation",
-     isEnabled: () => !0,
-     isHidden: !1,
-     supportsNonInteractive: !1,
-     argumentHint: "<name>",
-     async call(A, q) {
-       if (F8() && rz())
-         return {
-           type: "text",
-           value:
-             "Cannot rename: This session is a swarm teammate. Teammate names are set by the team leader.",
-         };
-       if (!A || A.trim() === "")
-         return {
-           type: "text",
-           value: "Please provide a name for the session. Usage: /rename <name>",
-         };
-       let K = u6(),
-         Y = I$(),
-         z = A.trim();
-       if ((await A91(K, z, Y), jq().terminalTitleFromRename)) ii7(z);
-       if (F8())
-         return (
-           await KxA(K, z, Y),
-           q.setAppState((w) => ({
-             ...w,
-             standaloneAgentContext: { ...w.standaloneAgentContext, name: z },
-           })),
-           { type: "text", value: `Session and agent renamed to: ${z}` }
-         );
-       return { type: "text", value: `Session renamed to: ${z}` };
-     },
-     userFacingName() {
-       return "rename";
-     },
-   }),
-     (qKq = qtY));
- });

--- Removed L5q (pretty-v2.1.32.js:492496-492538)
- var L5q = v(() => {
-   g4();
-   IxA();
-   MM();
-   ef6();
-   ((y1z = {
-     type: "local",
-     name: "thinkback-play",
-     description: "Play the thinkback animation",
-     isEnabled: () => sY("tengu_thinkback"),
-     isHidden: !0,
-     supportsNonInteractive: !1,
-     async call() {
-       let A = DM(),
-         q = R1z(),
-         K = A.plugins[q];
-       if (!K || K.length === 0)
-         return {
-           type: "text",
-           value:
-             "Thinkback plugin not installed. Run /think-back first to install it.",
-         };
-       let Y = K[0];
-       if (!Y?.installPath)
-         return {
-           type: "text",
-           value: "Thinkback plugin installation path not found.",
-         };
-       let z = E5q(Y.installPath, "skills", L1z),
-         w = E5q(z, "year_in_review.js");
-       if (!k1z(w))
-         return {
-           type: "text",
-           value: "No animation found. Run /think-back first to generate one.",
-         };
-       return { type: "text", value: hxA(z).message };
-     },
-     userFacingName() {
-       return "thinkback-play";
-     },
-   }),
-     (k5q = y1z));
- });

--- Removed U5q (pretty-v2.1.32.js:493919-493974)
- var U5q = v(() => {
-   d1();
-   u1();
-   xD();
-   Dm();
-   zO();
-   WU1();
-   V$();
-   a6();
-   kJ = a($1(), 1);
-   ((U1z = {
-     type: "local-jsx",
-     name: "plan",
-     description: "Enable plan mode or view the current session plan",
-     argumentHint: "[open]",
-     isEnabled: () => !0,
-     isHidden: !1,
-     async call(A, q, K) {
-       let { getAppState: Y, setAppState: z } = q,
-         H = (await Y()).toolPermissionContext.mode;
-       if (H !== "plan")
-         return (
-           Zy(H, "plan"),
-           z((M) => ({
-             ...M,
-             toolPermissionContext: t2(M.toolPermissionContext, {
-               type: "setMode",
-               mode: "plan",
-               destination: "session",
-             }),
-           })),
-           A("Enabled plan mode"),
-           null
-         );
-       let O = ID(),
-         $ = qZ();
-       if (!O) return (A("Already in plan mode. No plan written yet."), null);
-       if (K.trim().split(/\s+/)[0] === "open")
-         try {
-           return (await Xm($), A(`Opened plan in editor: ${$}`), null);
-         } catch (M) {
-           return (A(`Failed to open plan in editor: ${M}`), null);
-         }
-       let J = _I(),
-         X = J ? D_(J) : void 0,
-         j = await GP1(
-           kJ.createElement(g1z, { planContent: O, planPath: $, editorName: X }),
-         );
-       return (A(j), null);
-     },
-     userFacingName() {
-       return "plan";
-     },
-   }),
-     (g5q = U1z));
- });

--- Removed e5q (pretty-v2.1.32.js:494851-494914)
- var e5q = v(() => {
-   qV6();
-   uj1();
-   F6();
-   D7();
-   ((Mp1 = a($1(), 1)),
-     (o1z = {
-       type: "local-jsx",
-       name: "privacy-settings",
-       description: "View and update your privacy settings",
-       isEnabled: () => {
-         return UA6();
-       },
-       isHidden: !1,
-       async call(A) {
-         if (!(await bj1())) return (A(s5q), null);
-         let [K, Y] = await Promise.all([xj1(), Qa()]);
-         if (!K.success) return (A(s5q), null);
-         let z = K.data,
-           w = Y.success ? Y.data : null;
-         async function H($) {
-           if ($ === "escape" || $ === "defer") {
-             A("Privacy settings dialog dismissed", { display: "system" });
-             return;
-           }
-           await O();
-         }
-         async function O() {
-           let $ = await xj1();
-           if (!$.success) {
-             A("Unable to retrieve updated privacy settings", {
-               display: "system",
-             });
-             return;
-           }
-           let _ = $.data,
-             J = _.grove_enabled ? "true" : "false";
-           if (
-             (A(`"Help improve Claude" set to ${J}.`),
-             z.grove_enabled !== null && z.grove_enabled !== _.grove_enabled)
-           )
-             c("tengu_grove_policy_toggled", {
-               state: _.grove_enabled,
-               location: "settings",
-             });
-         }
-         if (z.grove_enabled !== null)
-           return Mp1.createElement(o5q, {
-             settings: z,
-             domainExcluded: w?.domain_excluded,
-             onDone: O,
-           });
-         return Mp1.createElement(AV6, {
-           showIfAlreadyViewed: !0,
-           onDone: H,
-           location: "settings",
-         });
-       },
-       userFacingName() {
-         return "privacy-settings";
-       },
-     }),
-     (t5q = o1z));
- });

--- Removed R9q (pretty-v2.1.32.js:497003-497028)
- var R9q = v(() => {
-   Z7();
-   _M();
-   ((J6z = {
-     type: "local",
-     name: "files",
-     description: "List all files currently in context",
-     isEnabled: () => !1,
-     isHidden: !1,
-     supportsNonInteractive: !0,
-     async call(A, q) {
-       let K = q.readFileState ? hS(q.readFileState) : [];
-       if (K.length === 0) return { type: "text", value: "No files in context" };
-       return {
-         type: "text",
-         value: `Files in context:
- ${K.map((z) => _6z(y6(), z)).join(`
- `)}`,
-       };
-     },
-     userFacingName() {
-       return "files";
-     },
-   }),
-     (L9q = J6z));
- });

--- Removed C9q (pretty-v2.1.32.js:497093-497166)
- var C9q = v(() => {
-   Eq();
-   a6();
-   I6();
-   Pw();
-   vz();
-   F6();
-   ((Z6z = {
-     type: "local-jsx",
-     name: "fork",
-     description: "Create a fork of the current conversation at this point",
-     argumentHint: "[name]",
-     isEnabled: () => !0,
-     isHidden: !1,
-     async call(A, q, K) {
-       B4("fork");
-       let Y = K?.trim() || void 0,
-         z = u6();
-       try {
-         let {
-             sessionId: w,
-             title: H,
-             forkPath: O,
-             serializedMessages: $,
-           } = await W6z(Y),
-           _ = new Date(),
-           J = $.find((V) => V.type === "user"),
-           X = (() => {
-             let V = J?.message?.content;
-             if (!V) return "Forked conversation";
-             if (typeof V === "string") return V.slice(0, 100);
-             return (
-               V.find((N) => N.type === "text")?.text?.slice(0, 100) ??
-               "Forked conversation"
-             );
-           })(),
-           j = await G6z(H ?? X);
-         (await A91(w, j, O),
-           c("tengu_conversation_forked", {
-             message_count: $.length,
-             has_custom_title: !!H,
-           }));
-         let M = {
-             date: _.toISOString().split("T")[0],
-             messages: $,
-             fullPath: O,
-             value: _.getTime(),
-             created: _,
-             modified: _,
-             firstPrompt: X,
-             messageCount: $.length,
-             isSidechain: !1,
-             sessionId: w,
-             customTitle: j,
-           },
-           W = H ? ` "${H}"` : "",
-           G = `
- To resume the original: claude -r ${z}`,
-           P = `Forked conversation${W}. You are now in the fork.${G}`;
-         if (q.resume)
-           (await q.resume(w, M, "fork"), A(P, { display: "system" }));
-         else A(`Forked conversation${W}. Resume with: /resume ${w}`);
-         return null;
-       } catch (w) {
-         let H = w instanceof Error ? w.message : "Unknown error occurred";
-         return (A(`Failed to fork conversation: ${H}`), null);
-       }
-     },
-     userFacingName() {
-       return "fork";
-     },
-   }),
-     (y9q = Z6z));
- });

--- Removed Ezq (pretty-v2.1.32.js:505048-505072)
- var Ezq = v(() => {
-   YG();
-   ((tAz = {
-     type: "local",
-     name: "stickers",
-     description: "Order Claude Code stickers",
-     isEnabled: () => !0,
-     isHidden: !1,
-     supportsNonInteractive: !1,
-     async call() {
-       if (await NY("https://www.stickermule.com/claudecode"))
-         return { type: "text", value: "Opening sticker page in browser…" };
-       else
-         return {
-           type: "text",
-           value:
-             "Failed to open browser. Visit: https://www.stickermule.com/claudecode",
-         };
-     },
-     userFacingName() {
-       return "stickers";
-     },
-   }),
-     (vzq = tAz));
- });

--- Removed mzq (pretty-v2.1.32.js:505400-505456)
- var mzq = v(() => {
-   xzq();
-   VbA();
-   Z7();
-   I6();
-   vz();
-   uzq = a($1(), 1);
-   ((D8z = {
-     type: "local-jsx",
-     name: "export",
-     description: "Export the current conversation to a file or clipboard",
-     isEnabled: () => !0,
-     isHidden: !1,
-     argumentHint: "[filename]",
-     async call(A, q, K) {
-       B4("export");
-       let Y = await X8z(q);
-       if (K.trim()) {
-         let O = K.trim(),
-           $ = O.endsWith(".txt") ? O : O.replace(/\.[^.]+$/, "") + ".txt",
-           _ = O8z(y6(), $);
-         try {
-           return (
-             c8(_, Y, { encoding: "utf-8", flush: !0 }),
-             A(`Conversation exported to: ${$}`),
-             null
-           );
-         } catch (J) {
-           return (
-             A(
-               `Failed to export conversation: ${J instanceof Error ? J.message : "Unknown error"}`,
-             ),
-             null
-           );
-         }
-       }
-       let z = _8z(q.messages),
-         w = $8z(new Date()),
-         H;
-       if (z) {
-         let O = J8z(z);
-         H = O ? `${w.substring(0, 10)}-${O}.txt` : `conversation-${w}.txt`;
-       } else H = `conversation-${w}.txt`;
-       return uzq.default.createElement(Izq, {
-         content: Y,
-         defaultFilename: H,
-         onDone: (O) => {
-           A(O.message);
-         },
-       });
-     },
-     userFacingName() {
-       return "export";
-     },
-   }),
-     (Bzq = D8z));
- });

--- Removed czq (pretty-v2.1.32.js:505768-505796)
- var czq = v(() => {
-   d1();
-   u1();
-   a6();
-   Eq();
-   N3();
-   Wz();
-   k5();
-   hq();
-   F6();
-   F$ = a($1(), 1);
-   dzq = {
-     type: "local-jsx",
-     name: "tag",
-     userFacingName() {
-       return "tag";
-     },
-     description: "Toggle a searchable tag on the current session",
-     isEnabled: () => !1,
-     isHidden: !1,
-     argumentHint: "<tag-name>",
-     async call(A, q, K) {
-       if (((K = K?.trim() || ""), Vz1.includes(K) || fz1.includes(K)))
-         return F$.createElement(pzq, { onDone: A });
-       if (!K) return F$.createElement(pzq, { onDone: A });
-       return F$.createElement(v8z, { tagName: K, onDone: A });
-     },
-   };
- });

--- Removed izq (pretty-v2.1.32.js:505884-505927)
- var izq = v(() => {
-   d1();
-   jhA();
-   r8();
-   F6();
-   N3();
-   R8();
-   Hp();
-   lB();
-   Z7();
-   Wz();
-   ld = a($1(), 1);
-   lzq = {
-     type: "local-jsx",
-     name: "output-style",
-     userFacingName() {
-       return "output-style";
-     },
-     description: "Set the output style directly or from a selection menu",
-     isEnabled: () => !0,
-     isHidden: !1,
-     argumentHint: "[style]",
-     async call(A, q, K) {
-       if (((K = K?.trim() || ""), Vz1.includes(K)))
-         return (
-           c("tengu_output_style_command_inline_help", { args: K }),
-           ld.createElement(R8z, { onDone: A })
-         );
-       if (fz1.includes(K)) {
-         A(
-           "Run /output-style to open the output style selection menu, or /output-style [styleName] to set the output style.",
-           { display: "system" },
-         );
-         return;
-       }
-       if (K)
-         return (
-           c("tengu_output_style_command_inline", { args: K }),
-           ld.createElement(L8z, { args: K, onDone: A })
-         );
-       return ld.createElement(E8z, { onDone: A });
-     },
-   };
- });

--- Removed kbA (pretty-v2.1.32.js:506303-506368)
- var kbA = v(() => {
-   k6();
-   D7();
-   YG();
-   Zj6();
-   dT1();
-   ((EbA = a($1(), 1)),
-     (I8z = {
-       type: "local-jsx",
-       name: "upgrade",
-       description: "Upgrade to Max for higher rate limits and more Opus",
-       isEnabled: () =>
-         !process.env.DISABLE_UPGRADE_COMMAND && !XC() && TK() !== "enterprise",
-       isHidden: !1,
-       async call(A, q) {
-         try {
-           if (U8()) {
-             let Y = n4(),
-               z = !1;
-             if (Y?.subscriptionType && Y?.rateLimitTier)
-               z =
-                 Y.subscriptionType === "max" &&
-                 Y.rateLimitTier === "default_claude_max_20x";
-             else if (Y?.accessToken) {
-               let w = await Sw1(Y.accessToken);
-               z =
-                 w?.organization?.organization_type === "claude_max" &&
-                 w?.organization?.rate_limit_tier === "default_claude_max_20x";
-             }
-             if (z)
-               return (
-                 setTimeout(() => {
-                   A(
-                     "You are already on the highest Max subscription plan. For additional usage, run /login to switch to an API usage-billed account.",
-                   );
-                 }, 0),
-                 null
-               );
-           }
-           return (
-             await NY("https://claude.ai/upgrade/max"),
-             EbA.createElement(vF1, {
-               startingMessage:
-                 "Starting new login following /upgrade. Exit with Ctrl-C to use existing account.",
-               onDone: (Y) => {
-                 (q.onChangeAPIKey(),
-                   A(Y ? "Login successful" : "Login interrupted"));
-               },
-             })
-           );
-         } catch (K) {
-           (K1(K),
-             setTimeout(() => {
-               A(
-                 "Failed to open browser. Please visit https://claude.ai/upgrade/max to upgrade.",
-               );
-             }, 0));
-         }
-         return null;
-       },
-       userFacingName() {
-         return "upgrade";
-       },
-     }),
-     (Tp1 = I8z));
- });

--- Removed _4z (pretty-v2.1.32.js:510102-510878)
- function _4z(A, q) {
-   let K = (S) => {
-       if (!S) return "";
-       return S.split(
-         `
- 
- `,
-       ).map((m) => {
-         let b = D9(m);
-         return (
-           (b = b.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")),
-           (b = b.replace(/^- /gm, "• ")),
-           (b = b.replace(/\n/g, "<br>")),
-           `<p>${b}</p>`
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
-         ${Y.whats_working ? `<div class="glance-section"><strong>What's working:</strong> ${IV6(Y.whats_working)} <a href="#section-wins" class="see-more">Impressive Things You Did →</a></div>` : ""}
-         ${Y.whats_hindering ? `<div class="glance-section"><strong>What's hindering you:</strong> ${IV6(Y.whats_hindering)} <a href="#section-friction" class="see-more">Where Things Go Wrong →</a></div>` : ""}
-         ${Y.quick_wins ? `<div class="glance-section"><strong>Quick wins to try:</strong> ${IV6(Y.quick_wins)} <a href="#section-features" class="see-more">Features to Try →</a></div>` : ""}
-         ${Y.ambitious_workflows ? `<div class="glance-section"><strong>Ambitious workflows:</strong> ${IV6(Y.ambitious_workflows)} <a href="#section-horizon" class="see-more">On the Horizon →</a></div>` : ""}
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
-           (S) => `
-         <div class="project-area">
-           <div class="area-header">
-             <span class="area-name">${D9(S.name)}</span>
-             <span class="area-count">~${S.session_count} sessions</span>
-           </div>
-           <div class="area-desc">${D9(S.description)}</div>
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
-       ${O.key_pattern ? `<div class="key-insight"><strong>Key pattern:</strong> ${D9(O.key_pattern)}</div>` : ""}
-     </div>
-     `
-       : "",
-     _ = q.what_works,
-     J =
-       _?.impressive_workflows && _.impressive_workflows.length > 0
-         ? `
-     <h2 id="section-wins">Impressive Things You Did</h2>
-     ${_.intro ? `<p class="section-intro">${D9(_.intro)}</p>` : ""}
-     <div class="big-wins">
-       ${_.impressive_workflows
-         .map(
-           (S) => `
-         <div class="big-win">
-           <div class="big-win-title">${D9(S.title || "")}</div>
-           <div class="big-win-desc">${D9(S.description || "")}</div>
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
-     ${X.intro ? `<p class="section-intro">${D9(X.intro)}</p>` : ""}
-     <div class="friction-categories">
-       ${X.categories
-         .map(
-           (S) => `
-         <div class="friction-category">
-           <div class="friction-title">${D9(S.category || "")}</div>
-           <div class="friction-desc">${D9(S.description || "")}</div>
-           ${S.examples ? `<ul class="friction-examples">${S.examples.map((m) => `<li>${D9(m)}</li>`).join("")}</ul>` : ""}
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
-           (S, m) => `
-         <div class="claude-md-item">
-           <input type="checkbox" id="cmd-${m}" class="cmd-checkbox" checked data-text="${D9(S.prompt_scaffold || S.where || "Add to CLAUDE.md")}\\n\\n${D9(S.addition)}">
-           <label for="cmd-${m}">
-             <code class="cmd-code">${D9(S.addition)}</code>
-             <button class="copy-btn" onclick="copyCmdItem(${m})">Copy</button>
-           </label>
-           <div class="cmd-why">${D9(S.why)}</div>
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
-           (S) => `
-         <div class="feature-card">
-           <div class="feature-title">${D9(S.feature || "")}</div>
-           <div class="feature-oneliner">${D9(S.one_liner || "")}</div>
-           <div class="feature-why"><strong>Why for you:</strong> ${D9(S.why_for_you || "")}</div>
-           ${
-             S.example_code
-               ? `
-           <div class="feature-examples">
-             <div class="feature-example">
-               <div class="example-code-row">
-                 <code class="example-code">${D9(S.example_code)}</code>
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
-           (S) => `
-         <div class="pattern-card">
-           <div class="pattern-title">${D9(S.title || "")}</div>
-           <div class="pattern-summary">${D9(S.suggestion || "")}</div>
-           ${S.detail ? `<div class="pattern-detail">${D9(S.detail)}</div>` : ""}
-           ${
-             S.copyable_prompt
-               ? `
-           <div class="copyable-prompt-section">
-             <div class="prompt-label">Paste into Claude Code:</div>
-             <div class="copyable-prompt-row">
-               <code class="copyable-prompt">${D9(S.copyable_prompt)}</code>
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
-     G =
-       W?.opportunities && W.opportunities.length > 0
-         ? `
-     <h2 id="section-horizon">On the Horizon</h2>
-     ${W.intro ? `<p class="section-intro">${D9(W.intro)}</p>` : ""}
-     <div class="horizon-section">
-       ${W.opportunities
-         .map(
-           (S) => `
-         <div class="horizon-card">
-           <div class="horizon-title">${D9(S.title || "")}</div>
-           <div class="horizon-possible">${D9(S.whats_possible || "")}</div>
-           ${S.how_to_try ? `<div class="horizon-tip"><strong>Getting started:</strong> ${D9(S.how_to_try)}</div>` : ""}
-           ${S.copyable_prompt ? `<div class="pattern-prompt"><div class="prompt-label">Paste into Claude Code:</div><code>${D9(S.copyable_prompt)}</code><button class="copy-btn" onclick="copyText(this)">Copy</button></div>` : ""}
-         </div>
-       `,
-         )
-         .join("")}
-     </div>
-     `
-         : "",
-     P = [],
-     V = [],
-     Z =
-       P.length > 0 || V.length > 0
-         ? `
-     <h2 id="section-feedback" class="feedback-header">Closing the Loop: Feedback for Other Teams</h2>
-     <p class="feedback-intro">Suggestions for the CC product and model teams based on your usage patterns. Click to expand.</p>
-     ${
-       P.length > 0
-         ? `
-     <div class="collapsible-section">
-       <div class="collapsible-header" onclick="toggleCollapsible(this)">
-         <span class="collapsible-arrow">▶</span>
-         <h3>Product Improvements for CC Team</h3>
-       </div>
-       <div class="collapsible-content">
-         <div class="suggestions-section">
-           ${P.map(
-             (S) => `
-             <div class="feedback-card team-card">
-               <div class="feedback-title">${D9(S.title || "")}</div>
-               <div class="feedback-detail">${D9(S.detail || "")}</div>
-               ${S.evidence ? `<div class="feedback-evidence"><em>Evidence:</em> ${D9(S.evidence)}</div>` : ""}
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
-       V.length > 0
-         ? `
-     <div class="collapsible-section">
-       <div class="collapsible-header" onclick="toggleCollapsible(this)">
-         <span class="collapsible-arrow">▶</span>
-         <h3>Model Behavior Improvements</h3>
-       </div>
-       <div class="collapsible-content">
-         <div class="suggestions-section">
-           ${V.map(
-             (S) => `
-             <div class="feedback-card model-card">
-               <div class="feedback-title">${D9(S.title || "")}</div>
-               <div class="feedback-detail">${D9(S.detail || "")}</div>
-               ${S.evidence ? `<div class="feedback-evidence"><em>Evidence:</em> ${D9(S.evidence)}</div>` : ""}
-             </div>
-           `,
-           ).join("")}
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
-       <div class="fun-headline">"${D9(N.headline)}"</div>
-       ${N.detail ? `<div class="fun-detail">${D9(N.detail)}</div>` : ""}
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
-     u = `
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
-     const rawHourCounts = ${$4z(A.message_hours)};
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
-         ${od(A.goal_categories, "#2563eb")}
-       </div>
-       <div class="chart-card">
-         <div class="chart-title">Top Tools Used</div>
-         ${od(A.tool_counts, "#0891b2")}
-       </div>
-     </div>
- 
-     <div class="charts-row">
-       <div class="chart-card">
-         <div class="chart-title">Languages</div>
-         ${od(A.languages, "#10b981")}
-       </div>
-       <div class="chart-card">
-         <div class="chart-title">Session Types</div>
-         ${od(A.session_types || {}, "#8b5cf6")}
-       </div>
-     </div>
- 
-     ${$}
- 
-     <!-- Response Time Distribution -->
-     <div class="chart-card" style="margin: 24px 0;">
-       <div class="chart-title">User Response Time Distribution</div>
-       ${H4z(A.user_response_times)}
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
-         ${O4z(A.message_hours)}
-       </div>
-       <div class="chart-card">
-         <div class="chart-title">Tool Errors Encountered</div>
-         ${Object.keys(A.tool_error_categories).length > 0 ? od(A.tool_error_categories, "#dc2626") : '<p class="empty">No tool errors</p>'}
-       </div>
-     </div>
- 
-     ${J}
- 
-     <div class="charts-row">
-       <div class="chart-card">
-         <div class="chart-title">What Helped Most (Claude's Capabilities)</div>
-         ${od(A.success, "#16a34a")}
-       </div>
-       <div class="chart-card">
-         <div class="chart-title">Outcomes</div>
-         ${od(A.outcomes, "#8b5cf6", 6, w4z)}
-       </div>
-     </div>
- 
-     ${D}
- 
-     <div class="charts-row">
-       <div class="chart-card">
-         <div class="chart-title">Primary Friction Types</div>
-         ${od(A.friction, "#dc2626")}
-       </div>
-       <div class="chart-card">
-         <div class="chart-title">Inferred Satisfaction (model-estimated)</div>
-         ${od(A.satisfaction, "#eab308", 6, z4z)}
-       </div>
-     </div>
- 
-     ${M}
- 
-     ${G}
- 
-     ${T}
- 
-     ${Z}
-   </div>
-   <script>${u}</script>
- </body>
- </html>`;
- }

--- Removed OBA (pretty-v2.1.32.js:523367-523374)
- function OBA() {
-   if (YVA()) {
-     if (X4() && GX()) HBA();
-     OE4().then(() => {
-       (fe(), HBA());
-     });
-   } else HBA();
- }

--- Removed CBA (pretty-v2.1.32.js:531125-531133)
- var CBA = v(() => {
-   O71();
-   ZF1();
-   a4();
-   a6();
-   FA();
-   yBA = a($1(), 1);
-   sYz = qA(() => process.stdin.on("data", wz1));
- });

--- Removed OJq (pretty-v2.1.32.js:536363-536365)
- function OJq(A) {
-   return jd(A).isAboveWarningThreshold;
- }

--- Removed Wwz (pretty-v2.1.32.js:540398-540422)
- function Wwz(A, q, K, Y, z) {
-   return [
-     ...(A
-       ? [
-           m7.createElement(
-             f,
-             { dimColor: !0, key: "esc" },
-             m7.createElement(YA, { shortcut: q, action: "interrupt" }),
-           ),
-         ]
-       : []),
-     ...(Y
-       ? [
-           m7.createElement(
-             f,
-             { dimColor: !0, key: "toggle-tasks" },
-             m7.createElement(YA, {
-               shortcut: K,
-               action: z ? "hide tasks" : "show tasks",
-             }),
-           ),
-         ]
-       : []),
-   ];
- }

--- Removed v0q (pretty-v2.1.32.js:543204-543204)
-   v0q = 2,

--- Removed FHz (pretty-v2.1.32.js:546412-546414)
- function FHz(A) {
-   return { ...A, showExpandedTodos: !A.showExpandedTodos };
- }

=== Added ===

+++ Added MW (pretty-v2.1.33.js:3443-3445)
+ function MW() {
+   return mdA($8(), "teams");
+ }

+++ Added TT1 (pretty-v2.1.33.js:45263-45266)
+ function TT1(A, q) {
+   let K = A.toLowerCase();
+   return q.autoUpdate ?? (eN.has(K) && !zwK.has(K));
+ }

+++ Added v1A (pretty-v2.1.33.js:119126-119129)
+ function v1A(A) {
+   if (typeof Bun < "u") return Bun.YAML.parse(A);
+   return T1A(A);
+ }

+++ Added Ct8 (pretty-v2.1.33.js:132954-133138)
+ var Ct8 = v(() => {
+   Rt8 = `Use this tool to create and manage a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user.
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
+ * Uses the ${Rq} tool to add a comment to the calculateTotal function *
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

+++ Added l67 (pretty-v2.1.33.js:150497-150523)
+ function l67(A) {
+   let q = q1(7),
+     { children: K } = A,
+     [Y] = cn.useState(LZ5),
+     z = t_(),
+     w,
+     H;
+   if (q[0] !== Y || q[1] !== z)
+     ((w = () => {
+       Y.setTickInterval(z ? G_1 : kZ5);
+     }),
+       (H = [Y, z]),
+       (q[0] = Y),
+       (q[1] = z),
+       (q[2] = w),
+       (q[3] = H));
+   else ((w = q[2]), (H = q[3]));
+   cn.useEffect(w, H);
+   let $;
+   if (q[4] !== K || q[5] !== Y)
+     (($ = cn.default.createElement(Mq6.Provider, { value: Y }, K)),
+       (q[4] = K),
+       (q[5] = Y),
+       (q[6] = $));
+   else $ = q[6];
+   return $;
+ }

+++ Added QZ5 (pretty-v2.1.33.js:151063-151065)
+ function QZ5() {
+   return jU.trim().length > 0;
+ }

+++ Added gY6 (pretty-v2.1.33.js:210537-210537)
+   gY6 = "Not logged in · Please run /login",

+++ Added z49 (pretty-v2.1.33.js:214126-214160)
+ async function z49(A, q, K) {
+   if (SA.terminal && SA.terminal in JI1) {
+     let z = `Shift+Enter is natively supported in ${JI1[SA.terminal]}.
+ 
+ No configuration needed. Just use Shift+Enter to add newlines.`;
+     return (A(z), null);
+   }
+   if (!CX1()) {
+     let z = SA.terminal || "your current terminal",
+       w = oA(),
+       H = "";
+     if (w === "macos")
+       H = `   • macOS: Apple Terminal
+ `;
+     else if (w === "windows")
+       H = `   • Windows: Windows Terminal
+ `;
+     let $ = `Terminal setup cannot be run from ${z}.
+ 
+ This command configures a convenient Shift+Enter shortcut for multi-line prompts.
+ ${K6.dim("Note: You can already use backslash (\\\\) + return to add newlines.")}
+ 
+ To set up the shortcut (optional):
+ 1. Exit tmux/screen temporarily
+ 2. Run /terminal-setup directly in one of these terminals:
+ ${H}   • IDE: VSCode, Cursor, Windsurf, Zed
+    • Other: Alacritty, Warp
+ 3. Return to tmux/screen - settings will persist
+ 
+ ${K6.dim("Note: iTerm2, WezTerm, Ghostty, and Kitty support Shift+Enter natively.")}`;
+     return (A($), null);
+   }
+   let Y = await Gz6(q.options.theme);
+   return (A(Y), null);
+ }

+++ Added V41 (pretty-v2.1.33.js:214435-214457)
+ var V41 = v(() => {
+   w3();
+   sr();
+   $I1();
+   hwA();
+   mA();
+   N5();
+   eq();
+   K8();
+   I6();
+   Ww();
+   L6();
+   u1();
+   E3();
+   I6();
+   xwA();
+   JI1 = {
+     ghostty: "Ghostty",
+     kitty: "Kitty",
+     "iTerm.app": "iTerm2",
+     WezTerm: "WezTerm",
+   };
+ });

+++ Added O_A (pretty-v2.1.33.js:232316-232321)
+ function O_A(A) {
+   if ((A.type === "assistant" || A.type === "user") && A.message?.content)
+     return kS7(A.message?.content);
+   if (A.type === "attachment" && A.attachment) return fz(Q1(A.attachment));
+   return 0;
+ }

+++ Added Nb1 (pretty-v2.1.33.js:254829-254860)
+ var Nb1 = v(() => {
+   m$();
+   M6();
+   L6();
+   m$();
+   Li1();
+   Dz();
+   gXA = KA(async (A) => {
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
+ - If you see a <${_P}> tag in the current conversation turn, the skill has ALREADY been loaded - follow the instructions directly instead of calling this tool again
+ `;
+   });
+ });

+++ Added aS (pretty-v2.1.33.js:259089-259089)
+ var aS = "TeamCreate";

+++ Added yq1 (pretty-v2.1.33.js:259090-259090)
+ var yq1 = "TeamDelete";

+++ Added Oa (pretty-v2.1.33.js:259226-259245)
+ var Oa = v(() => {
+   F4();
+   I$6();
+   B6();
+   yA();
+   ((LQ7 = `Search for or select deferred tools to make them available for use.
+ 
+ **MANDATORY PREREQUISITE - THIS IS A HARD REQUIREMENT**
+ 
+ You MUST use this tool to load deferred tools BEFORE calling them directly.
+ 
+ This is a BLOCKING REQUIREMENT - deferred tools listed below are NOT available until you load them using this tool. Both query modes (keyword search and direct selection) load the returned tools — once a tool appears in the results, it is immediately available to call.${RQ7}`),
+     (If9 = `Search for or select deferred tools to make them available for use.
+ 
+ **MANDATORY PREREQUISITE - THIS IS A HARD REQUIREMENT**
+ 
+ You MUST use this tool to load deferred tools BEFORE calling them directly.
+ 
+ This is a BLOCKING REQUIREMENT - deferred tools are NOT available until you load them using this tool. Look for <available-deferred-tools> messages in the conversation for the list of tools you can discover. Both query modes (keyword search and direct selection) load the returned tools — once a tool appears in the results, it is immediately available to call.${RQ7}`));
+ });

+++ Added zh (pretty-v2.1.33.js:265638-265640)
+ var zh = v(() => {
+   Ov9 = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
+ });

+++ Added QJY (pretty-v2.1.33.js:353829-353842)
+ async function QJY() {
+   await h06({ clearOnboarding: !0 });
+   let A = _VA.createElement(
+     f,
+     null,
+     "Successfully logged out from your Anthropic account.",
+   );
+   return (
+     setTimeout(() => {
+       _3(0, "logout");
+     }, 200),
+     A
+   );
+ }

+++ Added iV (pretty-v2.1.33.js:355435-355466)
+ var iV = v(() => {
+   d7();
+   yA();
+   I6();
+   M6();
+   I6();
+   Zz();
+   eq();
+   Tw();
+   qY();
+   HBw = b.strictObject({
+     operation: b
+       .enum(["spawnTeam", "cleanup"])
+       .describe(
+         "Operation: spawnTeam to create a team, cleanup to remove team and task directories.",
+       ),
+     agent_type: b
+       .string()
+       .optional()
+       .describe(
+         'Type/role of the team lead (e.g., "researcher", "test-runner"). Used for team file and inter-agent coordination.',
+       ),
+     team_name: b
+       .string()
+       .optional()
+       .describe("Name for the new team to create (required for spawnTeam)."),
+     description: b
+       .string()
+       .optional()
+       .describe("Team description/purpose (only used with spawnTeam)."),
+   });
+ });

+++ Added JXY (pretty-v2.1.33.js:355637-355657)
+ function JXY(A, q, K, Y, z) {
+   let w = q.agentName,
+     H =
+       K === "completed"
+         ? `Teammate "${w}" completed their task.`
+         : K === "failed"
+           ? `Teammate "${w}" failed: ${Y || "Unknown error"}`
+           : K === "killed"
+             ? `Teammate "${w}" was stopped.`
+             : `Teammate "${w}" is idle and ready for new work.`,
+     $ = e2(A),
+     O = `<${$O}>
+ <${PW}>${A}</${PW}>
+ <${oN}>${$}</${oN}>
+ <${tX}>${K}</${tX}>
+ <${eX}>${H}</${eX}>
+ </${$O}>
+ Read the output file to retrieve the result: ${$}`;
+   (V0({ value: O, mode: "task-notification" }, z),
+     Q5(A, z, (_) => ({ ..._, notified: !0 })));
+ }

+++ Added DXY (pretty-v2.1.33.js:355664-355669)
+ function DXY(A, q) {
+   Q5(A, q, (K) => {
+     if (K.status !== "running" || !K.isIdle) return K;
+     return { ...K, isIdle: !1 };
+   });
+ }

+++ Added jXY (pretty-v2.1.33.js:355676-355681)
+ function jXY(A, q) {
+   Q5(A, q, (K) => {
+     if (!K.awaitingPlanApproval) return K;
+     return { ...K, awaitingPlanApproval: !1 };
+   });
+ }

+++ Added VVA (pretty-v2.1.33.js:355682-355687)
+ function VVA(A, q) {
+   Q5(A, q, (K) => {
+     if (K.status !== "running" || K.shutdownRequested) return K;
+     return { ...K, shutdownRequested: !0 };
+   });
+ }

+++ Added WXY (pretty-v2.1.33.js:355714-355724)
+ function WXY(A, q, K) {
+   let Y;
+   (Q5(A, K, (z) => {
+     if (z.status !== "running") return z;
+     return (
+       (Y = z.unregisterCleanup),
+       { ...z, status: "completed", result: q, endTime: Date.now() }
+     );
+   }),
+     Y?.());
+ }

+++ Added GXY (pretty-v2.1.33.js:355725-355735)
+ function GXY(A, q, K) {
+   let Y;
+   (Q5(A, K, (z) => {
+     if (z.status !== "running") return z;
+     return (
+       (Y = z.unregisterCleanup),
+       { ...z, status: "failed", error: q, endTime: Date.now() }
+     );
+   }),
+     Y?.());
+ }

+++ Added PXY (pretty-v2.1.33.js:355748-355752)
+ function PXY(A, q) {
+   return Zv(q).filter(
+     (K) => K.status === "running" && K.identity.teamName === A,
+   );
+ }

+++ Added XjY (pretty-v2.1.33.js:367411-367423)
+ async function XjY(A, q) {
+   return VG.createElement(Rj1, {
+     onDone: async (K) => {
+       if ((q.onChangeAPIKey(), q.setMessages(rC4), K))
+         (Kz1(),
+           iC4(JjY()),
+           XJ6(),
+           aY6(),
+           q.setAppState((Y) => ({ ...Y, authVersion: Y.authVersion + 1 })));
+       A(K ? "Login successful" : "Login interrupted");
+     },
+   });
+ }

+++ Added RNA (pretty-v2.1.33.js:367747-367807)
+ async function RNA(A, q) {
+   if (!j6().hasVisitedExtraUsage)
+     _A((O) => ({ ...O, hasVisitedExtraUsage: !0 }));
+   let K = JK(),
+     Y = K === "team" || K === "enterprise",
+     z = Pu(),
+     w = fL(),
+     H = L3()?.hasExtraUsageEnabled === !0;
+   if (!z && Y) {
+     if (w) {
+       try {
+         let O = await tC4("limit_increase", ["pending", "dismissed"]);
+         if (O && O.length > 0)
+           return (
+             A(
+               "You have already submitted a request for extra usage to your admin.",
+             ),
+             null
+           );
+       } catch (O) {
+         K1(O);
+       }
+       try {
+         return (
+           await sC4({ request_type: "limit_increase", details: null }),
+           A(
+             H
+               ? "Request sent to your admin to increase extra usage."
+               : "Request sent to your admin to enable extra usage.",
+           ),
+           null
+         );
+       } catch (O) {
+         K1(O);
+       }
+     }
+     return (
+       A("Please contact your admin to manage extra usage settings."),
+       null
+     );
+   }
+   let $ = Y
+     ? "https://claude.ai/admin-settings/usage"
+     : "https://claude.ai/settings/usage";
+   try {
+     return (
+       await NY($),
+       AS4.default.createElement(Rj1, {
+         startingMessage:
+           "Starting new login following /extra-usage. Exit with Ctrl-C to use existing account.",
+         onDone: (O) => {
+           (q.onChangeAPIKey(), A(O ? "Login successful" : "Login interrupted"));
+         },
+       })
+     );
+   } catch (O) {
+     (K1(O),
+       A(`Failed to open browser. Please visit ${$} to see your extra usage.`));
+   }
+   return null;
+ }

+++ Added Fm1 (pretty-v2.1.33.js:367819-367840)
+ var Fm1 = v(() => {
+   $7();
+   mA();
+   ((GjY = {
+     type: "local-jsx",
+     name: "extra-usage",
+     description: "Configure extra usage to keep working when limits are hit",
+     isEnabled: () => {
+       if (process.env.DISABLE_EXTRA_USAGE_COMMAND) return !1;
+       if (!VC()) return !1;
+       if (fL()) return !0;
+       let A = JK();
+       return A === "pro" || A === "max";
+     },
+     isHidden: !1,
+     load: () => Promise.resolve().then(() => (yNA(), qS4)),
+     userFacingName() {
+       return "extra-usage";
+     },
+   }),
+     (Xs = GjY));
+ });

+++ Added pWY (pretty-v2.1.33.js:376074-376082)
+ function pWY(A) {
+   let q = ["Agent idle"];
+   if (A.completedTaskId) {
+     let K = A.completedStatus || "completed";
+     q.push(`Task ${A.completedTaskId} ${K}`);
+   }
+   if (A.summary) q.push(`Last DM: ${A.summary}`);
+   return q.join(" · ");
+ }

+++ Added Kx4 (pretty-v2.1.33.js:387528-387534)
+ function Kx4() {
+   if (aj1)
+     ((ys = aj1), h(`[TeammateModeSnapshot] Captured from CLI override: ${ys}`));
+   else
+     ((ys = j6().teammateMode ?? "auto"),
+       h(`[TeammateModeSnapshot] Captured from config: ${ys}`));
+ }

+++ Added Mx4 (pretty-v2.1.33.js:387860-387862)
+ function Mx4() {
+   return j6().preferTmuxOverIterm2 === !0;
+ }

+++ Added ERY (pretty-v2.1.33.js:417012-417090)
+ function ERY() {
+   let A = uO() ? "" : vRY;
+   return `Use this tool proactively when you're about to start a non-trivial implementation task. Getting user sign-off on your approach before writing code prevents wasted effort and ensures alignment. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
+    - If you would use ${OH} to clarify the approach, use EnterPlanMode instead
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
+ ${A}## Examples
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
+ `;
+ }

+++ Added XLA (pretty-v2.1.33.js:418444-418446)
+ function XLA(A) {
+   return A.replace(/[^a-zA-Z0-9]/g, "-").toLowerCase();
+ }

+++ Added pRY (pretty-v2.1.33.js:418450-418455)
+ function pRY(A, q) {
+   let K = Dd4(A);
+   gRY(K, { recursive: !0 });
+   let Y = DLA(K, "config.json");
+   l8(Y, Q1(q, null, 2));
+ }

+++ Added jd4 (pretty-v2.1.33.js:418461-418594)
+ var jd4 = v(() => {
+   d7();
+   yA();
+   CF1();
+   V7();
+   lXA();
+   iV();
+   Tw();
+   s6();
+   o7();
+   I6();
+   k9();
+   I6();
+   Jd4();
+   Xd4 = b.strictObject({
+     team_name: b.string().describe("Name for the new team to create."),
+     description: b.string().optional().describe("Team description/purpose."),
+     agent_type: b
+       .string()
+       .optional()
+       .describe(
+         'Type/role of the team lead (e.g., "researcher", "test-runner"). Used for team file and inter-agent coordination.',
+       ),
+   });
+   cRY = {
+     name: aS,
+     maxResultSizeChars: 1e5,
+     userFacingName() {
+       return "";
+     },
+     inputSchema: Xd4,
+     isEnabled() {
+       return p8();
+     },
+     isConcurrencySafe(A) {
+       return !1;
+     },
+     isReadOnly(A) {
+       return !1;
+     },
+     async checkPermissions(A, q) {
+       return { behavior: "allow", updatedInput: A };
+     },
+     async validateInput(A, q) {
+       if (!A.team_name || A.team_name.trim().length === 0)
+         return {
+           result: !1,
+           message: "team_name is required for TeamCreate",
+           errorCode: 9,
+         };
+       return { result: !0 };
+     },
+     async description() {
+       return "Create a new team for coordinating multiple agents";
+     },
+     async prompt() {
+       return zd4();
+     },
+     mapToolResultToToolResultBlockParam(A, q) {
+       return {
+         tool_use_id: q,
+         type: "tool_result",
+         content: [{ type: "text", text: Q1(A, null, 2) }],
+       };
+     },
+     async call(A, q) {
+       let { setAppState: K, getAppState: Y } = q,
+         { team_name: z, description: w, agent_type: H } = A,
+         $ = await Y(),
+         O = $.teamContext?.teamName;
+       if (O)
+         throw Error(
+           `Already leading team "${O}". A leader can only manage one team at a time. Use TeamDelete to end the current team before creating a new one.`,
+         );
+       let _ = dRY(z),
+         J = Pv(rz, _),
+         X = H || rz,
+         D = zY($.mainLoopModelForSession ?? $.mainLoopModel ?? ck()),
+         M = Dd4(_),
+         j = DLA(M, "config.json"),
+         W = {
+           name: _,
+           description: w,
+           createdAt: Date.now(),
+           leadAgentId: J,
+           leadSessionId: U6(),
+           members: [
+             {
+               agentId: J,
+               name: rz,
+               agentType: X,
+               model: D,
+               joinedAt: Date.now(),
+               tmuxPaneId: "",
+               cwd: y6(),
+               subscriptions: [],
+             },
+           ],
+         };
+       pRY(_, W);
+       let G = XLA(_);
+       return (
+         V46(G),
+         $y1(G),
+         mt8(XLA(_)),
+         K((P) => ({
+           ...P,
+           teamContext: {
+             teamName: _,
+             teamFilePath: j,
+             leadAgentId: J,
+             teammates: {
+               [J]: {
+                 name: rz,
+                 agentType: X,
+                 color: op(J),
+                 tmuxSessionName: "",
+                 tmuxPaneId: "",
+                 cwd: y6(),
+                 spawnedAt: Date.now(),
+               },
+             },
+           },
+         })),
+         { data: { team_name: _, team_file_path: j, lead_agent_id: J } }
+       );
+     },
+     renderToolUseMessage: wd4,
+     renderToolUseProgressMessage: Hd4,
+     renderToolUseRejectedMessage: $d4,
+     renderToolUseErrorMessage: Od4,
+     renderToolResultMessage: _d4,
+   };
+ });

+++ Added Wd4 (pretty-v2.1.33.js:418595-418610)
+ function Wd4() {
+   return `
+ # TeamDelete
+ 
+ Remove team and task directories when the swarm work is complete.
+ 
+ This operation:
+ - Removes the team directory (\`~/.claude/teams/{team-name}/\`)
+ - Removes the task directory (\`~/.claude/tasks/{team-name}/\`)
+ - Clears team context from the current session
+ 
+ **IMPORTANT**: TeamDelete will fail if the team still has active members. Gracefully terminate teammates first, then call TeamDelete after all teammates have shut down.
+ 
+ Use this when all teammates have finished their work and you want to clean up the team resources. The team name is automatically determined from the current session's team context.
+ `.trim();
+ }

+++ Added Gd4 (pretty-v2.1.33.js:418611-418613)
+ function Gd4(A) {
+   return "cleanup team: current";
+ }

+++ Added Ed4 (pretty-v2.1.33.js:418638-418718)
+ var Ed4 = v(() => {
+   d7();
+   CF1();
+   iV();
+   I6();
+   k9();
+   Tw();
+   Nd4();
+   ((Td4 = b.strictObject({})),
+     (lRY = {
+       name: yq1,
+       maxResultSizeChars: 1e5,
+       userFacingName() {
+         return "";
+       },
+       inputSchema: Td4,
+       isEnabled() {
+         return p8();
+       },
+       isConcurrencySafe(A) {
+         return !1;
+       },
+       isReadOnly(A) {
+         return !1;
+       },
+       async checkPermissions(A, q) {
+         return { behavior: "allow", updatedInput: A };
+       },
+       async description() {
+         return "Clean up team and task directories when the swarm is complete";
+       },
+       async prompt() {
+         return Wd4();
+       },
+       mapToolResultToToolResultBlockParam(A, q) {
+         return {
+           tool_use_id: q,
+           type: "tool_result",
+           content: [{ type: "text", text: Q1(A, null, 2) }],
+         };
+       },
+       async call(A, q) {
+         let { setAppState: K, getAppState: Y } = q,
+           w = (await Y()).teamContext?.teamName;
+         if (w) {
+           let H = yX(w);
+           if (H) {
+             let $ = H.members.filter((O) => O.name !== rz);
+             if ($.length > 0) {
+               let O = $.map((_) => _.name).join(", ");
+               return {
+                 data: {
+                   success: !1,
+                   message: `Cannot cleanup team with ${$.length} active member(s): ${O}. Use requestShutdown to gracefully terminate teammates first.`,
+                   team_name: w,
+                 },
+               };
+             }
+           }
+           (await TE4(w), vx4(), Ft8());
+         }
+         return (
+           K((H) => ({ ...H, teamContext: void 0, inbox: { messages: [] } })),
+           {
+             data: {
+               success: !0,
+               message: w
+                 ? `Cleaned up directories and worktrees for team "${w}"`
+                 : "No team name found, nothing to clean up",
+               team_name: w,
+             },
+           }
+         );
+       },
+       renderToolUseMessage: Gd4,
+       renderToolUseProgressMessage: Pd4,
+       renderToolUseRejectedMessage: Zd4,
+       renderToolUseErrorMessage: fd4,
+       renderToolResultMessage: Vd4,
+     }));
+ });

+++ Added Cd4 (pretty-v2.1.33.js:418881-418883)
+ function Cd4() {
+   return TQ1.default.createElement(t5, null);
+ }

+++ Added Sd4 (pretty-v2.1.33.js:418884-418886)
+ function Sd4(A, { verbose: q }) {
+   return TQ1.default.createElement(a3, { result: A, verbose: q });
+ }

+++ Added _yY (pretty-v2.1.33.js:419440-419440)
+   _yY = () => (Bd4(), Ly(ud4)).SendMessageTool,

+++ Added DyY (pretty-v2.1.33.js:419549-419550)
+   DyY =
+     "Optional model to use for this agent. If not specified, inherits from parent. Prefer haiku for quick, straightforward tasks to minimize cost and latency.",

+++ Added uc4 (pretty-v2.1.33.js:422757-422759)
+ function uc4() {
+   bQ1 = !1;
+ }

+++ Added BuY (pretty-v2.1.33.js:432690-432713)
+ function BuY(A) {
+   let q = [];
+   for (let Y of A) {
+     if (Y.type !== "user") continue;
+     let z = Y.message.content,
+       w = (
+         typeof z === "string"
+           ? z
+           : z
+               .filter(($) => $.type === "text")
+               .map(($) => $.text)
+               .join("")
+       ).trim();
+     if (!w || w.includes("<task-notification>")) continue;
+     let H = w.length > 200 ? w.slice(0, 200) + "…" : w;
+     q.push(`- "${H}"`);
+   }
+   let K =
+     q.length > 0
+       ? q.slice(-10).join(`
+ `)
+       : "- (no user messages yet)";
+   return uuY.replace("{human_messages}", K);
+ }

+++ Added uuY (pretty-v2.1.33.js:432862-432879)
+   uuY = `[SUGGESTION MODE]
+ 
+ TASK: Find the user's stated next step. Return it, or nothing.
+ 
+ The conversation contains many automated <task-notification> messages from workers. Ignore those. Here is what the user actually typed:
+ {human_messages}
+ 
+ SEARCH FOR:
+ - Multi-part requests: "do X and Y and Z" → X done → return "Y"
+ - Stated intent: "then I'll...", "next...", "after that..." → return the next step
+ - Answer to Claude's question → "yes"
+ - User's full plan is complete → "/commit" or "/commit-push-pr"
+ 
+ NOTHING FOUND → return nothing.
+ This is correct most of the time. Only return text you can trace to the user's stated plan.
+ 
+ 2-12 words. User's phrasing. Never evaluate, never Claude-voice.
+ Output ONLY the suggestion, or nothing.`,

+++ Added fyA (pretty-v2.1.33.js:434360-434363)
+ function fyA(A) {
+   return `TeammateIdle hook feedback:
+ ${A.blockingError}`;
+ }

+++ Added VQ1 (pretty-v2.1.33.js:434364-434367)
+ function VQ1(A) {
+   return `TaskCompleted hook feedback:
+ ${A.blockingError}`;
+ }

+++ Added Jt4 (pretty-v2.1.33.js:446313-446319)
+ async function Jt4(A, q) {
+   return new (await Promise.resolve().then(() => (FU1(), BP6))).default(
+     A,
+     ["mcp"],
+     q,
+   );
+ }

+++ Added ut4 (pretty-v2.1.33.js:448498-448503)
+ function ut4(A, q) {
+   if (bt4(A, q) === "session_memory") return !0;
+   let K = xt4(A, q);
+   if (K && U$6(K)) return !0;
+   return !1;
+ }

+++ Added oe4 (pretty-v2.1.33.js:453048-453071)
+ function oe4(A) {
+   let q = q1(3),
+     { text: K, highlights: Y } = A,
+     z;
+   if (q[0] !== Y || q[1] !== K) {
+     let w = ie4(K, Y),
+       H = [[]];
+     for (let $ of w) {
+       let O = $.text.split(`
+ `);
+       for (let _ = 0; _ < O.length; _++) {
+         if (_ > 0) H.push([]);
+         let J = O[_];
+         if (J.length > 0)
+           H[H.length - 1].push({ text: J, highlight: $.highlight });
+       }
+     }
+     ((z = Uv.createElement(I, { flexDirection: "column" }, H.map(DdY))),
+       (q[0] = Y),
+       (q[1] = K),
+       (q[2] = z));
+   } else z = q[2];
+   return z;
+ }

+++ Added DdY (pretty-v2.1.33.js:453072-453074)
+ function DdY(A, q) {
+   return Uv.createElement(I, { key: q }, A.map(MdY));
+ }

+++ Added MdY (pretty-v2.1.33.js:453075-453083)
+ function MdY(A, q) {
+   if (A.highlight?.color)
+     return Uv.createElement(
+       f,
+       { key: q, color: A.highlight.color },
+       Uv.createElement(U3, null, A.text),
+     );
+   return Uv.createElement(f, { key: q }, Uv.createElement(U3, null, A.text));
+ }

+++ Added K1q (pretty-v2.1.33.js:453470-453470)
+   K1q = 300000,

+++ Added IdY (pretty-v2.1.33.js:454114-454167)
+ async function IdY(A, q, K) {
+   Q4("multi-directory");
+   let Y = (K ?? "").trim(),
+     z = await q.getAppState(),
+     w = async ($, O = !1) => {
+       let J = {
+           type: "addDirectories",
+           directories: [$],
+           destination: O ? "localSettings" : "session",
+         },
+         X = await q.getAppState(),
+         D = l2(X.toolPermissionContext, J);
+       q.setAppState((G) => ({ ...G, toolPermissionContext: D }));
+       let M = hy();
+       if (!M.includes($)) XV1([...M, $]);
+       F8.refreshConfig();
+       let j;
+       if (O)
+         try {
+           (Cb(J),
+             (j = `Added ${K6.bold($)} as a working directory and saved to local settings`));
+         } catch (G) {
+           j = `Added ${K6.bold($)} as a working directory. Failed to save to local settings: ${G instanceof Error ? G.message : "Unknown error"}`;
+         }
+       else j = `Added ${K6.bold($)} as a working directory for this session`;
+       let W = `${j} ${K6.dim("· /permissions to manage")}`;
+       A(W);
+     };
+   if (!Y)
+     return vt.default.createElement(aU1, {
+       permissionContext: z.toolPermissionContext,
+       onAddDirectory: w,
+       onCancel: () => {
+         A("Did not add a working directory.");
+       },
+     });
+   let H = nG1(Y, z.toolPermissionContext);
+   if (H.resultType !== "success") {
+     let $ = rG1(H);
+     return vt.default.createElement(hdY, {
+       message: $,
+       args: K ?? "",
+       onDone: () => A($),
+     });
+   }
+   return vt.default.createElement(aU1, {
+     directoryPath: H.absolutePath,
+     permissionContext: z.toolPermissionContext,
+     onAddDirectory: w,
+     onCancel: () => {
+       A(`Did not add ${K6.bold(H.absolutePath)} as a working directory.`);
+     },
+   });
+ }

+++ Added J1q (pretty-v2.1.33.js:454186-454200)
+ var J1q = v(() => {
+   ((xdY = {
+     type: "local-jsx",
+     name: "add-dir",
+     description: "Add a new working directory",
+     argumentHint: "<path>",
+     isEnabled: () => !0,
+     isHidden: !1,
+     load: () => Promise.resolve().then(() => (MZ6(), O1q)),
+     userFacingName() {
+       return "add-dir";
+     },
+   }),
+     (_1q = xdY));
+ });

+++ Added mdY (pretty-v2.1.33.js:454391-454396)
+ async function mdY(A, q, K) {
+   let Y = K?.trim();
+   if (!Y)
+     return (A("Usage: /btw <your question>", { display: "system" }), null);
+   return lw.createElement(udY, { question: Y, context: q, onDone: A });
+ }

+++ Added P1q (pretty-v2.1.33.js:454410-454426)
+ var P1q = v(() => {
+   ((FdY = {
+     type: "local-jsx",
+     name: "btw",
+     description:
+       "Ask a quick side question without interrupting the main conversation",
+     isEnabled: () => !1,
+     isHidden: !1,
+     immediate: !0,
+     argumentHint: "<question>",
+     load: () => Promise.resolve().then(() => (G1q(), W1q)),
+     userFacingName() {
+       return "btw";
+     },
+   }),
+     (bSA = FdY));
+ });

+++ Added ldY (pretty-v2.1.33.js:454979-454982)
+ async function ldY(A, q, K) {
+   let Y = K || "";
+   return k1q(A, q.abortController.signal, q.messages, Y);
+ }

+++ Added YiY (pretty-v2.1.33.js:461536-461545)
+ function YiY(A) {
+   switch (A) {
+     case "promo-copper":
+       return "Opus 4.6 is here · $50 free extra usage · /extra-usage to enable";
+     case "promo":
+       return "Opus 4.6 is here · $50 free extra usage · /extra-usage to enable";
+     case "launch-only":
+       return "Opus 4.6 is here · Most capable for ambitious work";
+   }
+ }

+++ Added ziY (pretty-v2.1.33.js:461546-461554)
+ function ziY(A) {
+   switch (A) {
+     case "promo-copper":
+     case "promo":
+       return 39;
+     case "launch-only":
+       return 0;
+   }
+ }

+++ Added DAq (pretty-v2.1.33.js:461555-461596)
+ function DAq(A) {
+   let q = q1(9),
+     { variant: K, maxWidth: Y } = A,
+     z,
+     w,
+     H;
+   if (q[0] !== Y || q[1] !== K) {
+     w = Symbol.for("react.early_return_sentinel");
+     A: {
+       let O = YiY(K);
+       if (((H = Y ? YY(O, Y) : O), (z = ziY(K)), z > 0 && z < H.length)) {
+         w = jI.createElement(
+           f,
+           { dimColor: !0 },
+           jI.createElement(f, { color: "claude" }, H.slice(0, z)),
+           H.slice(z),
+         );
+         break A;
+       }
+     }
+     ((q[0] = Y), (q[1] = K), (q[2] = z), (q[3] = w), (q[4] = H));
+   } else ((z = q[2]), (w = q[3]), (H = q[4]));
+   if (w !== Symbol.for("react.early_return_sentinel")) return w;
+   if (z > 0) {
+     let O;
+     if (q[5] !== H)
+       ((O = jI.createElement(
+         f,
+         { dimColor: !0 },
+         jI.createElement(f, { color: "claude" }, H),
+       )),
+         (q[5] = H),
+         (q[6] = O));
+     else O = q[6];
+     return O;
+   }
+   let $;
+   if (q[7] !== H)
+     (($ = jI.createElement(f, { dimColor: !0 }, H)), (q[7] = H), (q[8] = $));
+   else $ = q[8];
+   return $;
+ }

+++ Added UiY (pretty-v2.1.33.js:462794-462818)
+ async function UiY(A, q) {
+   let {
+     messages: K,
+     getAppState: Y,
+     options: { mainLoopModel: z, tools: w },
+   } = q;
+   Q4("context");
+   let H = HN(K),
+     { messages: $ } = await eB(H),
+     O = process.stdout.columns || 80,
+     _ = await Y(),
+     J = await YG6(
+       $,
+       z,
+       async () => _.toolPermissionContext,
+       w,
+       _.agentDefinitions,
+       O,
+       q,
+       void 0,
+       H,
+     ),
+     X = await xhA(bhA.createElement(NAq, { data: J }));
+   return (A(X), null);
+ }

+++ Added giY (pretty-v2.1.33.js:462831-462852)
+ async function giY(A, q) {
+   let {
+       messages: K,
+       getAppState: Y,
+       options: { mainLoopModel: z, tools: w, agentDefinitions: H },
+     } = q,
+     $ = HN(K),
+     { messages: O } = await eB($),
+     _ = await Y(),
+     J = await YG6(
+       O,
+       z,
+       async () => _.toolPermissionContext,
+       w,
+       H,
+       void 0,
+       q,
+       void 0,
+       $,
+     );
+   return { type: "text", value: piY(J) };
+ }

+++ Added hAq (pretty-v2.1.33.js:463001-463030)
+ var hAq = v(() => {
+   s6();
+   ((CAq = {
+     name: "context",
+     description: "Visualize current context usage as a colored grid",
+     isEnabled: () => !q4(),
+     isHidden: !1,
+     type: "local-jsx",
+     load: () => Promise.resolve().then(() => (LAq(), kAq)),
+     userFacingName() {
+       return this.name;
+     },
+   }),
+     (SAq = {
+       type: "local",
+       name: "context",
+       supportsNonInteractive: !0,
+       description: "Show current context usage",
+       get isHidden() {
+         return !q4();
+       },
+       isEnabled() {
+         return q4();
+       },
+       load: () => Promise.resolve().then(() => (yAq(), RAq)),
+       userFacingName() {
+         return "context";
+       },
+     }));
+ });

+++ Added IAq (pretty-v2.1.33.js:463031-463031)
+ var IAq = {};

+++ Added rAq (pretty-v2.1.33.js:463881-463881)
+ var rAq = {};

+++ Added aAq (pretty-v2.1.33.js:464637-464637)
+ var aAq = {};

+++ Added _8q (pretty-v2.1.33.js:464829-464829)
+ var _8q = {};

+++ Added Kf6 (pretty-v2.1.33.js:464943-464966)
+ var Kf6 = v(() => {
+   N5();
+   ((pnY = {
+     ghostty: "Ghostty",
+     kitty: "Kitty",
+     "iTerm.app": "iTerm2",
+     WezTerm: "WezTerm",
+   }),
+     (dnY = {
+       type: "local-jsx",
+       name: "terminal-setup",
+       userFacingName() {
+         return "terminal-setup";
+       },
+       description:
+         SA.terminal === "Apple_Terminal"
+           ? "Enable Option+Enter key binding for newlines and visual bell"
+           : "Install Shift+Enter key binding for newlines",
+       isEnabled: () => !0,
+       isHidden: SA.terminal !== null && SA.terminal in pnY,
+       load: () => Promise.resolve().then(() => (V41(), KT7)),
+     }),
+     (I51 = dnY));
+ });

+++ Added f8q (pretty-v2.1.33.js:465631-465631)
+ var f8q = {};

+++ Added S8q (pretty-v2.1.33.js:465843-465843)
+ var S8q = {};

+++ Added qrY (pretty-v2.1.33.js:466115-466186)
+ async function qrY(A, q, K) {
+   (l("tengu_ext_ide_command", {}), Q4("ide-integration"));
+   let {
+       options: { dynamicMcpConfig: Y },
+       onChangeDynamicMcpConfig: z,
+     } = q,
+     w = await Zx1(!0);
+   if (w.length === 0 && q.onInstallIDEExtension && !ZX()) {
+     let J = await A_A(),
+       X = (D) => {
+         if (q.onInstallIDEExtension)
+           if ((q.onInstallIDEExtension(D), bS(D)))
+             A(`Installed plugin to ${K6.bold(X_(D))}
+ Please ${K6.bold("restart your IDE")} completely for it to take effect`);
+           else A(`Installed extension to ${K6.bold(X_(D))}`);
+       };
+     if (J.length > 1)
+       return I0.default.createElement(enY, {
+         runningIDEs: J,
+         onSelectIDE: X,
+         onDone: () => {
+           A("No IDE selected.", { display: "system" });
+         },
+       });
+     else if (J.length === 1) {
+       let D = J[0];
+       return I0.default.createElement(() => {
+         let j = q1(1),
+           W;
+         if (j[0] === Symbol.for("react.memo_cache_sentinel"))
+           ((W = []), (j[0] = W));
+         else W = j[0];
+         return (b51.useEffect(KrY, W), null);
+       }, null);
+     }
+   }
+   let H = w.filter((J) => J.isValid),
+     $ = w.filter((J) => !J.isValid),
+     O = await tnY(H, Y);
+   return I0.default.createElement(onY, {
+     availableIDEs: H,
+     unavailableIDEs: $,
+     selectedIDE: O,
+     onClose: () => A("IDE selection cancelled", { display: "system" }),
+     onSelect: async (J) => {
+       try {
+         if (!z) {
+           A("Error connecting to IDE.");
+           return;
+         }
+         let X = { ...(Y || {}) };
+         if (O) delete X.ide;
+         if (!J) A(O ? `Disconnected from ${O.name}.` : "No IDE selected.");
+         else {
+           let D = J.url;
+           ((X.ide = {
+             type: D.startsWith("ws:") ? "ws-ide" : "sse-ide",
+             url: D,
+             ideName: J.name,
+             authToken: J.authToken,
+             ideRunningInWindows: J.ideRunningInWindows,
+             scope: "dynamic",
+           }),
+             A(`Connected to ${J.name}.`));
+         }
+         z(X);
+       } catch (X) {
+         A("Error connecting to IDE.");
+       }
+     },
+   });
+ }

+++ Added x8q (pretty-v2.1.33.js:466224-466238)
+ var x8q = v(() => {
+   ((YrY = {
+     type: "local-jsx",
+     name: "ide",
+     description: "Manage IDE integrations and show status",
+     isEnabled: () => !0,
+     isHidden: !1,
+     argumentHint: "[open]",
+     load: () => Promise.resolve().then(() => (h8q(), S8q)),
+     userFacingName() {
+       return "ide";
+     },
+   }),
+     (I8q = YrY));
+ });

+++ Added Q8q (pretty-v2.1.33.js:466314-466314)
+ var Q8q = {};

+++ Added l8q (pretty-v2.1.33.js:466389-466401)
+ var l8q = v(() => {
+   c8q = {
+     type: "local-jsx",
+     name: "logout",
+     description: "Sign out from your Anthropic account",
+     isEnabled: () => !process.env.DISABLE_LOGOUT_COMMAND,
+     isHidden: !1,
+     load: () => Promise.resolve().then(() => (I06(), ev4)),
+     userFacingName() {
+       return "logout";
+     },
+   };
+ });

+++ Added u7q (pretty-v2.1.33.js:468884-468884)
+ var u7q = {};

+++ Added TrY (pretty-v2.1.33.js:469407-469409)
+ async function TrY(A) {
+   return (Q4("github-app"), O$.default.createElement(NrY, { onDone: A }));
+ }

+++ Added F7q (pretty-v2.1.33.js:469454-469468)
+ var F7q = v(() => {
+   $7();
+   ((vrY = {
+     type: "local-jsx",
+     name: "install-github-app",
+     description: "Set up Claude GitHub Actions for a repository",
+     isEnabled: () => !process.env.DISABLE_INSTALL_GITHUB_APP_COMMAND && !NC(),
+     isHidden: !1,
+     load: () => Promise.resolve().then(() => (B7q(), u7q)),
+     userFacingName() {
+       return "install-github-app";
+     },
+   }),
+     (m7q = vrY));
+ });

+++ Added U7q (pretty-v2.1.33.js:469469-469469)
+ var U7q = {};

+++ Added ErY (pretty-v2.1.33.js:469471-469486)
+ async function ErY() {
+   if (
+     (Q4("slack-app"),
+     l("tengu_install_slack_app_clicked", {}),
+     _A((q) => ({
+       ...q,
+       slackAppInstallCount: (q.slackAppInstallCount ?? 0) + 1,
+     })),
+     await NY(Q7q))
+   )
+     return {
+       type: "text",
+       value: "Opening Slack app installation page in browser…",
+     };
+   else return { type: "text", value: `Couldn't open browser. Visit: ${Q7q}` };
+ }

+++ Added d7q (pretty-v2.1.33.js:469495-469509)
+ var d7q = v(() => {
+   ((krY = {
+     type: "local",
+     name: "install-slack-app",
+     description: "Install the Claude Slack app",
+     isEnabled: () => !0,
+     isHidden: !1,
+     supportsNonInteractive: !1,
+     load: () => Promise.resolve().then(() => (g7q(), U7q)),
+     userFacingName() {
+       return "install-slack-app";
+     },
+   }),
+     (p7q = krY));
+ });

+++ Added X4q (pretty-v2.1.33.js:475288-475288)
+ var X4q = {};

+++ Added zoY (pretty-v2.1.33.js:475338-475340)
+ function zoY(A) {
+   return A !== "flag";
+ }

+++ Added HoY (pretty-v2.1.33.js:475352-475375)
+ function HoY(A) {
+   let { entry: q, marketplaceInstallLocation: K } = A;
+   try {
+     let Y = x1();
+     if (typeof q.source === "string") {
+       if (!K) return !1;
+       let $ = Y.statSync(K).isDirectory() ? K : Pf6(K, ".."),
+         O = Pf6($, q.source);
+       return Y.existsSync(O);
+     }
+     let z = yg(),
+       w = q.name.replace(/[^a-zA-Z0-9-_]/g, "-"),
+       H = Pf6(z, w);
+     return Y.existsSync(H);
+   } catch (Y) {
+     return (
+       K1(Y instanceof Error ? Y : Error(String(Y))),
+       h(
+         `Unexpected error checking if plugin ${A.entry.name} is installed: ${Y}`,
+       ),
+       !1
+     );
+   }
+ }

+++ Added $oY (pretty-v2.1.33.js:475392-475395)
+ function $oY(A) {
+   let K = P8().skippedPlugins || [];
+   return A.filter((Y) => !K.includes(Y));
+ }

+++ Added OoY (pretty-v2.1.33.js:475430-475447)
+ async function OoY(A) {
+   let q = [],
+     Y = P8().skippedPlugins || [];
+   for (let z of A)
+     try {
+       if (!(await f0(z))) {
+         q.push(
+           `Plugin "${z}" is enabled but not found in any known marketplace`,
+         );
+         continue;
+       }
+       if (Y.includes(z))
+         q.push(`Plugin "${z}" is enabled but you chose not to install it`);
+     } catch {
+       q.push(`Plugin "${z}" is enabled but not found in any known marketplace`);
+     }
+   return q;
+ }

+++ Added loY (pretty-v2.1.33.js:479199-479201)
+ function loY() {
+   return null;
+ }

+++ Added u4q (pretty-v2.1.33.js:479736-479736)
+ var u4q = {};

+++ Added eoY (pretty-v2.1.33.js:479790-479808)
+ async function eoY(A, q, K) {
+   if (K) {
+     let Y = K.trim().split(/\s+/);
+     if (Y[0] === "no-redirect")
+       return yg1.default.createElement(Mf6, { onComplete: A });
+     if (Y[0] === "reconnect" && Y[1])
+       return yg1.default.createElement(YIA, {
+         serverName: Y.slice(1).join(" "),
+         onComplete: A,
+       });
+     if (Y[0] === "enable" || Y[0] === "disable")
+       return yg1.default.createElement(aoY, {
+         action: Y[0],
+         target: Y.length > 1 ? Y.slice(1).join(" ") : "all",
+         onComplete: A,
+       });
+   }
+   return yg1.default.createElement(Mf6, { onComplete: A });
+ }

+++ Added F4q (pretty-v2.1.33.js:479820-479834)
+ var F4q = v(() => {
+   ((AaY = {
+     type: "local-jsx",
+     name: "mcp",
+     description: "Manage MCP servers",
+     isEnabled: () => !0,
+     isHidden: !1,
+     argumentHint: "[enable|disable [server-name]]",
+     load: () => Promise.resolve().then(() => (B4q(), u4q)),
+     userFacingName() {
+       return "mcp";
+     },
+   }),
+     (m4q = AaY));
+ });

+++ Added cKq (pretty-v2.1.33.js:483047-483047)
+ var cKq = {};

+++ Added $1z (pretty-v2.1.33.js:483203-483205)
+ async function $1z(A) {
+   return LJ.createElement(K1z, { onDone: A });
+ }

+++ Added lKq (pretty-v2.1.33.js:483207-483222)
+ var lKq = v(() => {
+   d1();
+   u1();
+   z7();
+   DxA();
+   ((LJ = s(J1(), 1)),
+     (mg1 = s(J1(), 1)),
+     (MxA = {
+       ios: {
+         url: "https://apps.apple.com/app/claude-by-anthropic/id6473753684",
+       },
+       android: {
+         url: "https://play.google.com/store/apps/details?id=com.anthropic.claude",
+       },
+     }));
+ });

+++ Added Y3q (pretty-v2.1.33.js:483454-483454)
+ var Y3q = {};

+++ Added j1z (pretty-v2.1.33.js:483467-483479)
+ async function j1z() {
+   let A = [];
+   try {
+     let K = new Promise((Y, z) => {
+       setTimeout(() => z(Error("Timeout")), 500);
+     });
+     (await Promise.race([GxA(), K]), (A = PxA(n51())));
+   } catch {}
+   if (A.length > 0) return { type: "text", value: K3q(A) };
+   let q = PxA();
+   if (q.length > 0) return { type: "text", value: K3q(q) };
+   return { type: "text", value: `See the full changelog at: ${A3q}` };
+ }

+++ Added H3q (pretty-v2.1.33.js:483484-483498)
+ var H3q = v(() => {
+   ((W1z = {
+     description: "View release notes",
+     isEnabled: () => !0,
+     isHidden: !1,
+     name: "release-notes",
+     userFacingName() {
+       return "release-notes";
+     },
+     type: "local",
+     supportsNonInteractive: !0,
+     load: () => Promise.resolve().then(() => (z3q(), Y3q)),
+   }),
+     (w3q = W1z));
+ });

+++ Added $3q (pretty-v2.1.33.js:483499-483499)
+ var $3q = {};

+++ Added G1z (pretty-v2.1.33.js:483501-483527)
+ async function G1z(A, q) {
+   if (p8() && Kz())
+     return {
+       type: "text",
+       value:
+         "Cannot rename: This session is a swarm teammate. Teammate names are set by the team leader.",
+     };
+   if (!A || A.trim() === "")
+     return {
+       type: "text",
+       value: "Please provide a name for the session. Usage: /rename <name>",
+     };
+   let K = U6(),
+     Y = LO(),
+     z = A.trim();
+   if ((await r51(K, z, Y), Gq().terminalTitleFromRename)) eT7(z);
+   if (p8())
+     return (
+       await ZxA(K, z, Y),
+       q.setAppState((w) => ({
+         ...w,
+         standaloneAgentContext: { ...w.standaloneAgentContext, name: z },
+       })),
+       { type: "text", value: `Session and agent renamed to: ${z}` }
+     );
+   return { type: "text", value: `Session renamed to: ${z}` };
+ }

+++ Added J3q (pretty-v2.1.33.js:483537-483552)
+ var J3q = v(() => {
+   ((P1z = {
+     type: "local",
+     name: "rename",
+     description: "Rename the current conversation",
+     isEnabled: () => !0,
+     isHidden: !1,
+     supportsNonInteractive: !1,
+     argumentHint: "<name>",
+     load: () => Promise.resolve().then(() => (O3q(), $3q)),
+     userFacingName() {
+       return "rename";
+     },
+   }),
+     (_3q = P1z));
+ });

+++ Added u5q (pretty-v2.1.33.js:488845-488845)
+ var u5q = {};

+++ Added Q5q (pretty-v2.1.33.js:489123-489123)
+ var Q5q = {};

+++ Added l5q (pretty-v2.1.33.js:489502-489502)
+ var l5q = {};

+++ Added KAz (pretty-v2.1.33.js:489504-489506)
+ async function KAz(A, q) {
+   return dxA.createElement(d5q, { onExit: A, commands: q.options.commands });
+ }

+++ Added o5q (pretty-v2.1.33.js:489527-489527)
+ var o5q = {};

+++ Added zAz (pretty-v2.1.33.js:489529-489535)
+ async function zAz(A, q) {
+   return cxA.createElement($P1, {
+     onClose: A,
+     context: q,
+     defaultTab: "Status",
+   });
+ }

+++ Added M9q (pretty-v2.1.33.js:491663-491663)
+ var M9q = {};

+++ Added VAz (pretty-v2.1.33.js:491665-491671)
+ async function VAz(A, q) {
+   return rxA.createElement(OV6, {
+     toolUseContext: q,
+     onDone: A,
+     onForegroundTask: q.onForegroundTask,
+   });
+ }

+++ Added Z9q (pretty-v2.1.33.js:491697-491697)
+ var Z9q = {};

+++ Added vAz (pretty-v2.1.33.js:491747-491750)
+ async function vAz(A) {
+   let q = await OP1(Ud.default.createElement(TAz, null));
+   return (A(q), null);
+ }

+++ Added E9q (pretty-v2.1.33.js:492012-492012)
+ var E9q = {};

+++ Added R9q (pretty-v2.1.33.js:492040-492040)
+ var R9q = {};

+++ Added S9q (pretty-v2.1.33.js:492117-492117)
+ var S9q = {};

+++ Added u9q (pretty-v2.1.33.js:492157-492157)
+ var u9q = {};

+++ Added bAz (pretty-v2.1.33.js:492165-492167)
+ function bAz() {
+   return xAz;
+ }

+++ Added cAz (pretty-v2.1.33.js:492552-492554)
+ async function cAz(A) {
+   return q5.createElement(dAz, { onDone: A });
+ }

+++ Added Q9q (pretty-v2.1.33.js:492601-492601)
+ var Q9q = {};

+++ Added oAz (pretty-v2.1.33.js:492608-492632)
+ async function oAz() {
+   let A = Jj(),
+     q = rAz(),
+     K = A.plugins[q];
+   if (!K || K.length === 0)
+     return {
+       type: "text",
+       value:
+         "Thinkback plugin not installed. Run /think-back first to install it.",
+     };
+   let Y = K[0];
+   if (!Y?.installPath)
+     return {
+       type: "text",
+       value: "Thinkback plugin installation path not found.",
+     };
+   let z = F9q(Y.installPath, "skills", nAz),
+     w = F9q(z, "year_in_review.js");
+   if (!iAz(w))
+     return {
+       type: "text",
+       value: "No animation found. Run /think-back first to generate one.",
+     };
+   return { type: "text", value: JV6(z).message };
+ }

+++ Added p9q (pretty-v2.1.33.js:492640-492655)
+ var p9q = v(() => {
+   F4();
+   ((aAz = {
+     type: "local",
+     name: "thinkback-play",
+     description: "Play the thinkback animation",
+     isEnabled: () => oY("tengu_thinkback"),
+     isHidden: !0,
+     supportsNonInteractive: !1,
+     load: () => Promise.resolve().then(() => (U9q(), Q9q)),
+     userFacingName() {
+       return "thinkback-play";
+     },
+   }),
+     (g9q = aAz));
+ });

+++ Added t9q (pretty-v2.1.33.js:493968-493968)
+ var t9q = {};

+++ Added KYq (pretty-v2.1.33.js:493994-493994)
+ var KYq = {};

+++ Added _8z (pretty-v2.1.33.js:494037-494069)
+ async function _8z(A, q, K) {
+   let { getAppState: Y, setAppState: z } = q,
+     H = (await Y()).toolPermissionContext.mode;
+   if (H !== "plan")
+     return (
+       Cy(H, "plan"),
+       z((j) => ({
+         ...j,
+         toolPermissionContext: l2(j.toolPermissionContext, {
+           type: "setMode",
+           mode: "plan",
+           destination: "session",
+         }),
+       })),
+       A("Enabled plan mode"),
+       null
+     );
+   let $ = uD(),
+     O = zZ();
+   if (!$) return (A("Already in plan mode. No plan written yet."), null);
+   if (K.trim().split(/\s+/)[0] === "open")
+     try {
+       return (await fm(O), A(`Opened plan in editor: ${O}`), null);
+     } catch (j) {
+       return (A(`Failed to open plan in editor: ${j}`), null);
+     }
+   let J = WI(),
+     X = J ? X_(J) : void 0,
+     M = await OP1(
+       RJ.createElement(O8z, { planContent: $, planPath: O, editorName: X }),
+     );
+   return (A(M), null);
+ }

+++ Added zYq (pretty-v2.1.33.js:494083-494097)
+ var zYq = v(() => {
+   ((J8z = {
+     type: "local-jsx",
+     name: "plan",
+     description: "Enable plan mode or view the current session plan",
+     argumentHint: "[open]",
+     isEnabled: () => !0,
+     isHidden: !1,
+     load: () => Promise.resolve().then(() => (YYq(), KYq)),
+     userFacingName() {
+       return "plan";
+     },
+   }),
+     (YbA = J8z));
+ });

+++ Added OYq (pretty-v2.1.33.js:494283-494283)
+ var OYq = {};

+++ Added X8z (pretty-v2.1.33.js:494285-494299)
+ async function X8z(A) {
+   let K = !j6().hasVisitedPasses;
+   if (K) {
+     let Y = sf6();
+     _A((z) => ({
+       ...z,
+       hasVisitedPasses: !0,
+       passesLastSeenRemaining: Y ?? z.passesLastSeenRemaining,
+     }));
+   }
+   return (
+     l("tengu_guest_passes_visited", { is_first_visit: K }),
+     zbA.createElement(HYq, { onDone: A })
+   );
+ }

+++ Added GYq (pretty-v2.1.33.js:494950-494950)
+ var GYq = {};

+++ Added P8z (pretty-v2.1.33.js:494952-494993)
+ async function P8z(A) {
+   if (!(await JM1())) return (A(WYq), null);
+   let [K, Y] = await Promise.all([_M1(), Sa()]);
+   if (!K.success) return (A(WYq), null);
+   let z = K.data,
+     w = Y.success ? Y.data : null;
+   async function H(O) {
+     if (O === "escape" || O === "defer") {
+       A("Privacy settings dialog dismissed", { display: "system" });
+       return;
+     }
+     await $();
+   }
+   async function $() {
+     let O = await _M1();
+     if (!O.success) {
+       A("Unable to retrieve updated privacy settings", { display: "system" });
+       return;
+     }
+     let _ = O.data,
+       J = _.grove_enabled ? "true" : "false";
+     if (
+       (A(`"Help improve Claude" set to ${J}.`),
+       z.grove_enabled !== null && z.grove_enabled !== _.grove_enabled)
+     )
+       l("tengu_grove_policy_toggled", {
+         state: _.grove_enabled,
+         location: "settings",
+       });
+   }
+   if (z.grove_enabled !== null)
+     return Op1.createElement(MYq, {
+       settings: z,
+       domainExcluded: w?.domain_excluded,
+       onDone: $,
+     });
+   return Op1.createElement(XV6, {
+     showIfAlreadyViewed: !0,
+     onDone: H,
+     location: "settings",
+   });
+ }

+++ Added fYq (pretty-v2.1.33.js:495004-495020)
+ var fYq = v(() => {
+   $7();
+   ((Z8z = {
+     type: "local-jsx",
+     name: "privacy-settings",
+     description: "View and update your privacy settings",
+     isEnabled: () => {
+       return kA6();
+     },
+     isHidden: !1,
+     load: () => Promise.resolve().then(() => (PYq(), GYq)),
+     userFacingName() {
+       return "privacy-settings";
+     },
+   }),
+     (ZYq = Z8z));
+ });

+++ Added pYq (pretty-v2.1.33.js:497093-497093)
+ var pYq = {};

+++ Added iYq (pretty-v2.1.33.js:497123-497123)
+ var iYq = {};

+++ Added x8z (pretty-v2.1.33.js:497126-497135)
+ async function x8z(A, q) {
+   let K = q.readFileState ? oS(q.readFileState) : [];
+   if (K.length === 0) return { type: "text", value: "No files in context" };
+   return {
+     type: "text",
+     value: `Files in context:
+ ${K.map((z) => I8z(y6(), z)).join(`
+ `)}`,
+   };
+ }

+++ Added oYq (pretty-v2.1.33.js:497141-497155)
+ var oYq = v(() => {
+   ((b8z = {
+     type: "local",
+     name: "files",
+     description: "List all files currently in context",
+     isEnabled: () => !1,
+     isHidden: !1,
+     supportsNonInteractive: !0,
+     load: () => Promise.resolve().then(() => (nYq(), iYq)),
+     userFacingName() {
+       return "files";
+     },
+   }),
+     (rYq = b8z));
+ });

+++ Added aYq (pretty-v2.1.33.js:497156-497156)
+ var aYq = {};

+++ Added p8z (pretty-v2.1.33.js:497221-497273)
+ async function p8z(A, q, K) {
+   Q4("fork");
+   let Y = K?.trim() || void 0,
+     z = U6();
+   try {
+     let {
+         sessionId: w,
+         title: H,
+         forkPath: $,
+         serializedMessages: O,
+       } = await Q8z(Y),
+       _ = new Date(),
+       J = O.find((V) => V.type === "user"),
+       X = (() => {
+         let V = J?.message?.content;
+         if (!V) return "Forked conversation";
+         if (typeof V === "string") return V.slice(0, 100);
+         return (
+           V.find((N) => N.type === "text")?.text?.slice(0, 100) ??
+           "Forked conversation"
+         );
+       })(),
+       M = await U8z(H ?? X);
+     (await r51(w, M, $),
+       l("tengu_conversation_forked", {
+         message_count: O.length,
+         has_custom_title: !!H,
+       }));
+     let j = {
+         date: _.toISOString().split("T")[0],
+         messages: O,
+         fullPath: $,
+         value: _.getTime(),
+         created: _,
+         modified: _,
+         firstPrompt: X,
+         messageCount: O.length,
+         isSidechain: !1,
+         sessionId: w,
+         customTitle: M,
+       },
+       W = H ? ` "${H}"` : "",
+       G = `
+ To resume the original: claude -r ${z}`,
+       P = `Forked conversation${W}. You are now in the fork.${G}`;
+     if (q.resume) (await q.resume(w, j, "fork"), A(P, { display: "system" }));
+     else A(`Forked conversation${W}. Resume with: /resume ${w}`);
+     return null;
+   } catch (w) {
+     let H = w instanceof Error ? w.message : "Unknown error occurred";
+     return (A(`Failed to fork conversation: ${H}`), null);
+   }
+ }

+++ Added eYq (pretty-v2.1.33.js:497283-497297)
+ var eYq = v(() => {
+   ((d8z = {
+     type: "local-jsx",
+     name: "fork",
+     description: "Create a fork of the current conversation at this point",
+     argumentHint: "[name]",
+     isEnabled: () => !0,
+     isHidden: !1,
+     load: () => Promise.resolve().then(() => (sYq(), aYq)),
+     userFacingName() {
+       return "fork";
+     },
+   }),
+     (tYq = d8z));
+ });

+++ Added tzq (pretty-v2.1.33.js:501370-501370)
+ var tzq = {};

+++ Added y7z (pretty-v2.1.33.js:501372-501376)
+ async function y7z(A, q) {
+   let Y = (await q.getAppState()).toolPermissionContext,
+     z = C0(Y);
+   return kbA.createElement(azq, { tools: z, onExit: A });
+ }

+++ Added K2q (pretty-v2.1.33.js:501398-501398)
+ var K2q = {};

+++ Added S7z (pretty-v2.1.33.js:501400-501402)
+ async function S7z(A, q, K) {
+   return LbA.createElement(b4q, { onComplete: A, args: K });
+ }

+++ Added H2q (pretty-v2.1.33.js:501424-501424)
+ var H2q = {};

+++ Added I7z (pretty-v2.1.33.js:501426-501429)
+ async function I7z(A, q) {
+   if ((Q4("rewind"), q.openMessageSelector)) q.openMessageSelector();
+   return { type: "skip" };
+ }

+++ Added E2q (pretty-v2.1.33.js:502253-502253)
+ var E2q = {};

+++ Added Y91 (pretty-v2.1.33.js:504653-504666)
+ var Y91 = v(() => {
+   E3();
+   M6();
+   eq();
+   yA();
+   s6();
+   EV6();
+   JI();
+   mA();
+   I6();
+   F4();
+   d2q();
+   c2q = `${mbA}.json`;
+ });

+++ Added a2q (pretty-v2.1.33.js:504667-504667)
+ var a2q = {};

+++ Added Awq (pretty-v2.1.33.js:505010-505010)
+ var Awq = {};

+++ Added j4z (pretty-v2.1.33.js:505012-505021)
+ async function j4z() {
+   if (await NY("https://www.stickermule.com/claudecode"))
+     return { type: "text", value: "Opening sticker page in browser…" };
+   else
+     return {
+       type: "text",
+       value:
+         "Failed to open browser. Visit: https://www.stickermule.com/claudecode",
+     };
+ }

+++ Added Kwq (pretty-v2.1.33.js:505026-505040)
+ var Kwq = v(() => {
+   ((W4z = {
+     type: "local",
+     name: "stickers",
+     description: "Order Claude Code stickers",
+     isEnabled: () => !0,
+     isHidden: !1,
+     supportsNonInteractive: !1,
+     load: () => Promise.resolve().then(() => (qwq(), Awq)),
+     userFacingName() {
+       return "stickers";
+     },
+   }),
+     (QbA = W4z));
+ });

+++ Added Owq (pretty-v2.1.33.js:505093-505093)
+ var Owq = {};

+++ Added Pwq (pretty-v2.1.33.js:505327-505327)
+ var Pwq = {};

+++ Added R4z (pretty-v2.1.33.js:505373-505409)
+ async function R4z(A, q, K) {
+   Q4("export");
+   let Y = await L4z(q);
+   if (K.trim()) {
+     let $ = K.trim(),
+       O = $.endsWith(".txt") ? $ : $.replace(/\.[^.]+$/, "") + ".txt",
+       _ = E4z(y6(), O);
+     try {
+       return (
+         l8(_, Y, { encoding: "utf-8", flush: !0 }),
+         A(`Conversation exported to: ${O}`),
+         null
+       );
+     } catch (J) {
+       return (
+         A(
+           `Failed to export conversation: ${J instanceof Error ? J.message : "Unknown error"}`,
+         ),
+         null
+       );
+     }
+   }
+   let z = Wwq(q.messages),
+     w = k4z(new Date()),
+     H;
+   if (z) {
+     let $ = Gwq(z);
+     H = $ ? `${w.substring(0, 10)}-${$}.txt` : `conversation-${w}.txt`;
+   } else H = `conversation-${w}.txt`;
+   return jwq.default.createElement(Jwq, {
+     content: Y,
+     defaultFilename: H,
+     onDone: ($) => {
+       A($.message);
+     },
+   });
+ }

+++ Added Vwq (pretty-v2.1.33.js:505420-505434)
+ var Vwq = v(() => {
+   ((y4z = {
+     type: "local-jsx",
+     name: "export",
+     description: "Export the current conversation to a file or clipboard",
+     isEnabled: () => !0,
+     isHidden: !1,
+     argumentHint: "[filename]",
+     load: () => Promise.resolve().then(() => (Zwq(), Pwq)),
+     userFacingName() {
+       return "export";
+     },
+   }),
+     (fwq = y4z));
+ });

+++ Added Nwq (pretty-v2.1.33.js:505435-505435)
+ var Nwq = {};

+++ Added Lwq (pretty-v2.1.33.js:505580-505580)
+ var Lwq = {};

+++ Added U4z (pretty-v2.1.33.js:505747-505752)
+ async function U4z(A, q, K) {
+   if (((K = K?.trim() || ""), v21.includes(K) || T21.includes(K)))
+     return FO.createElement(kwq, { onDone: A });
+   if (!K) return FO.createElement(kwq, { onDone: A });
+   return FO.createElement(Q4z, { tagName: K, onDone: A });
+ }

+++ Added Cwq (pretty-v2.1.33.js:505767-505781)
+ var Cwq = v(() => {
+   ((g4z = {
+     type: "local-jsx",
+     name: "tag",
+     userFacingName() {
+       return "tag";
+     },
+     description: "Toggle a searchable tag on the current session",
+     isEnabled: () => !1,
+     isHidden: !1,
+     argumentHint: "<tag-name>",
+     load: () => Promise.resolve().then(() => (Rwq(), Lwq)),
+   }),
+     (ywq = g4z));
+ });

+++ Added Swq (pretty-v2.1.33.js:505782-505782)
+ var Swq = {};

+++ Added i4z (pretty-v2.1.33.js:505870-505889)
+ async function i4z(A, q, K) {
+   if (((K = K?.trim() || ""), v21.includes(K)))
+     return (
+       l("tengu_output_style_command_inline_help", { args: K }),
+       nd.createElement(l4z, { onDone: A })
+     );
+   if (T21.includes(K)) {
+     A(
+       "Run /output-style to open the output style selection menu, or /output-style [styleName] to set the output style.",
+       { display: "system" },
+     );
+     return;
+   }
+   if (K)
+     return (
+       l("tengu_output_style_command_inline", { args: K }),
+       nd.createElement(c4z, { args: K, onDone: A })
+     );
+   return nd.createElement(p4z, { onDone: A });
+ }

+++ Added xwq (pretty-v2.1.33.js:505905-505919)
+ var xwq = v(() => {
+   ((n4z = {
+     type: "local-jsx",
+     name: "output-style",
+     userFacingName() {
+       return "output-style";
+     },
+     description: "Set the output style directly or from a selection menu",
+     isEnabled: () => !0,
+     isHidden: !1,
+     argumentHint: "[style]",
+     load: () => Promise.resolve().then(() => (hwq(), Swq)),
+   }),
+     (Iwq = n4z));
+ });

+++ Added Fwq (pretty-v2.1.33.js:506271-506271)
+ var Fwq = {};

+++ Added t4z (pretty-v2.1.33.js:506273-506275)
+ async function t4z(A) {
+   return dbA.createElement(Bwq, { onDone: A });
+ }

+++ Added pwq (pretty-v2.1.33.js:506300-506300)
+ var pwq = {};

+++ Added lbA (pretty-v2.1.33.js:506302-506346)
+ async function lbA(A, q) {
+   try {
+     if (i8()) {
+       let Y = o4(),
+         z = !1;
+       if (Y?.subscriptionType && Y?.rateLimitTier)
+         z =
+           Y.subscriptionType === "max" &&
+           Y.rateLimitTier === "default_claude_max_20x";
+       else if (Y?.accessToken) {
+         let w = await Gw1(Y.accessToken);
+         z =
+           w?.organization?.organization_type === "claude_max" &&
+           w?.organization?.rate_limit_tier === "default_claude_max_20x";
+       }
+       if (z)
+         return (
+           setTimeout(() => {
+             A(
+               "You are already on the highest Max subscription plan. For additional usage, run /login to switch to an API usage-billed account.",
+             );
+           }, 0),
+           null
+         );
+     }
+     return (
+       await NY("https://claude.ai/upgrade/max"),
+       cbA.createElement(Rj1, {
+         startingMessage:
+           "Starting new login following /upgrade. Exit with Ctrl-C to use existing account.",
+         onDone: (Y) => {
+           (q.onChangeAPIKey(), A(Y ? "Login successful" : "Login interrupted"));
+         },
+       })
+     );
+   } catch (K) {
+     (K1(K),
+       setTimeout(() => {
+         A(
+           "Failed to open browser. Please visit https://claude.ai/upgrade/max to upgrade.",
+         );
+       }, 0));
+   }
+   return null;
+ }

+++ Added nbA (pretty-v2.1.33.js:506357-506372)
+ var nbA = v(() => {
+   $7();
+   ((e4z = {
+     type: "local-jsx",
+     name: "upgrade",
+     description: "Upgrade to Max for higher rate limits and more Opus",
+     isEnabled: () =>
+       !process.env.DISABLE_UPGRADE_COMMAND && !NC() && JK() !== "enterprise",
+     isHidden: !1,
+     load: () => Promise.resolve().then(() => (ibA(), pwq)),
+     userFacingName() {
+       return "upgrade";
+     },
+   }),
+     (CV6 = e4z));
+ });

+++ Added cwq (pretty-v2.1.33.js:506373-506373)
+ var cwq = {};

+++ Added qqz (pretty-v2.1.33.js:506496-506498)
+ async function qqz(A, q) {
+   return SV6.default.createElement(Aqz, { onDone: A, context: q });
+ }

+++ Added QZ (pretty-v2.1.33.js:507430-507432)
+ function QZ(A) {
+   return od[A];
+ }

+++ Added LHq (pretty-v2.1.33.js:509274-509274)
+ var LHq = {};

+++ Added GKz (pretty-v2.1.33.js:509473-509477)
+ function GKz(A) {
+   return (
+     !Number.isNaN(A.created.getTime()) && !Number.isNaN(A.modified.getTime())
+   );
+ }

+++ Added PKz (pretty-v2.1.33.js:509531-509545)
+ function PKz(A) {
+   let q = new Map();
+   for (let K of A) {
+     let Y = K.meta.session_id,
+       z = q.get(Y);
+     if (
+       !z ||
+       K.meta.user_message_count > z.meta.user_message_count ||
+       (K.meta.user_message_count === z.meta.user_message_count &&
+         K.meta.duration_minutes > z.meta.duration_minutes)
+     )
+       q.set(Y, K);
+   }
+   return [...q.values()];
+ }

+++ Added xKz (pretty-v2.1.33.js:510130-510906)
+ function xKz(A, q) {
+   let K = (S) => {
+       if (!S) return "";
+       return S.split(
+         `
+ 
+ `,
+       ).map((m) => {
+         let x = j9(m);
+         return (
+           (x = x.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")),
+           (x = x.replace(/^- /gm, "• ")),
+           (x = x.replace(/\n/g, "<br>")),
+           `<p>${x}</p>`
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
+         ${Y.whats_working ? `<div class="glance-section"><strong>What's working:</strong> ${pV6(Y.whats_working)} <a href="#section-wins" class="see-more">Impressive Things You Did →</a></div>` : ""}
+         ${Y.whats_hindering ? `<div class="glance-section"><strong>What's hindering you:</strong> ${pV6(Y.whats_hindering)} <a href="#section-friction" class="see-more">Where Things Go Wrong →</a></div>` : ""}
+         ${Y.quick_wins ? `<div class="glance-section"><strong>Quick wins to try:</strong> ${pV6(Y.quick_wins)} <a href="#section-features" class="see-more">Features to Try →</a></div>` : ""}
+         ${Y.ambitious_workflows ? `<div class="glance-section"><strong>Ambitious workflows:</strong> ${pV6(Y.ambitious_workflows)} <a href="#section-horizon" class="see-more">On the Horizon →</a></div>` : ""}
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
+             <span class="area-name">${j9(S.name)}</span>
+             <span class="area-count">~${S.session_count} sessions</span>
+           </div>
+           <div class="area-desc">${j9(S.description)}</div>
+         </div>
+       `,
+         )
+         .join("")}
+     </div>
+     `
+         : "",
+     $ = q.interaction_style,
+     O = $?.narrative
+       ? `
+     <h2 id="section-usage">How You Use Claude Code</h2>
+     <div class="narrative">
+       ${K($.narrative)}
+       ${$.key_pattern ? `<div class="key-insight"><strong>Key pattern:</strong> ${j9($.key_pattern)}</div>` : ""}
+     </div>
+     `
+       : "",
+     _ = q.what_works,
+     J =
+       _?.impressive_workflows && _.impressive_workflows.length > 0
+         ? `
+     <h2 id="section-wins">Impressive Things You Did</h2>
+     ${_.intro ? `<p class="section-intro">${j9(_.intro)}</p>` : ""}
+     <div class="big-wins">
+       ${_.impressive_workflows
+         .map(
+           (S) => `
+         <div class="big-win">
+           <div class="big-win-title">${j9(S.title || "")}</div>
+           <div class="big-win-desc">${j9(S.description || "")}</div>
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
+     ${X.intro ? `<p class="section-intro">${j9(X.intro)}</p>` : ""}
+     <div class="friction-categories">
+       ${X.categories
+         .map(
+           (S) => `
+         <div class="friction-category">
+           <div class="friction-title">${j9(S.category || "")}</div>
+           <div class="friction-desc">${j9(S.description || "")}</div>
+           ${S.examples ? `<ul class="friction-examples">${S.examples.map((m) => `<li>${j9(m)}</li>`).join("")}</ul>` : ""}
+         </div>
+       `,
+         )
+         .join("")}
+     </div>
+     `
+         : "",
+     M = q.suggestions,
+     j = M
+       ? `
+     ${
+       M.claude_md_additions && M.claude_md_additions.length > 0
+         ? `
+     <h2 id="section-features">Existing CC Features to Try</h2>
+     <div class="claude-md-section">
+       <h3>Suggested CLAUDE.md Additions</h3>
+       <p style="font-size: 12px; color: #64748b; margin-bottom: 12px;">Just copy this into Claude Code to add it to your CLAUDE.md.</p>
+       <div class="claude-md-actions">
+         <button class="copy-all-btn" onclick="copyAllCheckedClaudeMd()">Copy All Checked</button>
+       </div>
+       ${M.claude_md_additions
+         .map(
+           (S, m) => `
+         <div class="claude-md-item">
+           <input type="checkbox" id="cmd-${m}" class="cmd-checkbox" checked data-text="${j9(S.prompt_scaffold || S.where || "Add to CLAUDE.md")}\\n\\n${j9(S.addition)}">
+           <label for="cmd-${m}">
+             <code class="cmd-code">${j9(S.addition)}</code>
+             <button class="copy-btn" onclick="copyCmdItem(${m})">Copy</button>
+           </label>
+           <div class="cmd-why">${j9(S.why)}</div>
+         </div>
+       `,
+         )
+         .join("")}
+     </div>
+     `
+         : ""
+     }
+     ${
+       M.features_to_try && M.features_to_try.length > 0
+         ? `
+     <p style="font-size: 13px; color: #64748b; margin-bottom: 12px;">Just copy this into Claude Code and it'll set it up for you.</p>
+     <div class="features-section">
+       ${M.features_to_try
+         .map(
+           (S) => `
+         <div class="feature-card">
+           <div class="feature-title">${j9(S.feature || "")}</div>
+           <div class="feature-oneliner">${j9(S.one_liner || "")}</div>
+           <div class="feature-why"><strong>Why for you:</strong> ${j9(S.why_for_you || "")}</div>
+           ${
+             S.example_code
+               ? `
+           <div class="feature-examples">
+             <div class="feature-example">
+               <div class="example-code-row">
+                 <code class="example-code">${j9(S.example_code)}</code>
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
+       M.usage_patterns && M.usage_patterns.length > 0
+         ? `
+     <h2 id="section-patterns">New Ways to Use Claude Code</h2>
+     <p style="font-size: 13px; color: #64748b; margin-bottom: 12px;">Just copy this into Claude Code and it'll walk you through it.</p>
+     <div class="patterns-section">
+       ${M.usage_patterns
+         .map(
+           (S) => `
+         <div class="pattern-card">
+           <div class="pattern-title">${j9(S.title || "")}</div>
+           <div class="pattern-summary">${j9(S.suggestion || "")}</div>
+           ${S.detail ? `<div class="pattern-detail">${j9(S.detail)}</div>` : ""}
+           ${
+             S.copyable_prompt
+               ? `
+           <div class="copyable-prompt-section">
+             <div class="prompt-label">Paste into Claude Code:</div>
+             <div class="copyable-prompt-row">
+               <code class="copyable-prompt">${j9(S.copyable_prompt)}</code>
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
+     ${W.intro ? `<p class="section-intro">${j9(W.intro)}</p>` : ""}
+     <div class="horizon-section">
+       ${W.opportunities
+         .map(
+           (S) => `
+         <div class="horizon-card">
+           <div class="horizon-title">${j9(S.title || "")}</div>
+           <div class="horizon-possible">${j9(S.whats_possible || "")}</div>
+           ${S.how_to_try ? `<div class="horizon-tip"><strong>Getting started:</strong> ${j9(S.how_to_try)}</div>` : ""}
+           ${S.copyable_prompt ? `<div class="pattern-prompt"><div class="prompt-label">Paste into Claude Code:</div><code>${j9(S.copyable_prompt)}</code><button class="copy-btn" onclick="copyText(this)">Copy</button></div>` : ""}
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
+               <div class="feedback-title">${j9(S.title || "")}</div>
+               <div class="feedback-detail">${j9(S.detail || "")}</div>
+               ${S.evidence ? `<div class="feedback-evidence"><em>Evidence:</em> ${j9(S.evidence)}</div>` : ""}
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
+               <div class="feedback-title">${j9(S.title || "")}</div>
+               <div class="feedback-detail">${j9(S.detail || "")}</div>
+               ${S.evidence ? `<div class="feedback-evidence"><em>Evidence:</em> ${j9(S.evidence)}</div>` : ""}
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
+       <div class="fun-headline">"${j9(N.headline)}"</div>
+       ${N.detail ? `<div class="fun-detail">${j9(N.detail)}</div>` : ""}
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
+     const rawHourCounts = ${IKz(A.message_hours)};
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
+         ${sd(A.goal_categories, "#2563eb")}
+       </div>
+       <div class="chart-card">
+         <div class="chart-title">Top Tools Used</div>
+         ${sd(A.tool_counts, "#0891b2")}
+       </div>
+     </div>
+ 
+     <div class="charts-row">
+       <div class="chart-card">
+         <div class="chart-title">Languages</div>
+         ${sd(A.languages, "#10b981")}
+       </div>
+       <div class="chart-card">
+         <div class="chart-title">Session Types</div>
+         ${sd(A.session_types || {}, "#8b5cf6")}
+       </div>
+     </div>
+ 
+     ${O}
+ 
+     <!-- Response Time Distribution -->
+     <div class="chart-card" style="margin: 24px 0;">
+       <div class="chart-title">User Response Time Distribution</div>
+       ${SKz(A.user_response_times)}
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
+         ${hKz(A.message_hours)}
+       </div>
+       <div class="chart-card">
+         <div class="chart-title">Tool Errors Encountered</div>
+         ${Object.keys(A.tool_error_categories).length > 0 ? sd(A.tool_error_categories, "#dc2626") : '<p class="empty">No tool errors</p>'}
+       </div>
+     </div>
+ 
+     ${J}
+ 
+     <div class="charts-row">
+       <div class="chart-card">
+         <div class="chart-title">What Helped Most (Claude's Capabilities)</div>
+         ${sd(A.success, "#16a34a")}
+       </div>
+       <div class="chart-card">
+         <div class="chart-title">Outcomes</div>
+         ${sd(A.outcomes, "#8b5cf6", 6, CKz)}
+       </div>
+     </div>
+ 
+     ${D}
+ 
+     <div class="charts-row">
+       <div class="chart-card">
+         <div class="chart-title">Primary Friction Types</div>
+         ${sd(A.friction, "#dc2626")}
+       </div>
+       <div class="chart-card">
+         <div class="chart-title">Inferred Satisfaction (model-estimated)</div>
+         ${sd(A.satisfaction, "#eab308", 6, yKz)}
+       </div>
+     </div>
+ 
+     ${j}
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

+++ Added BHq (pretty-v2.1.33.js:511389-511391)
+ function BHq(A) {
+   return A.filter((q) => PuA.has(q));
+ }

+++ Added FKz (pretty-v2.1.33.js:511731-511731)
+ var FKz = 3600000,

+++ Added dHq (pretty-v2.1.33.js:511926-511928)
+ function dHq() {
+   return null;
+ }

+++ Added Ne4 (pretty-v2.1.33.js:517403-517403)
+ var Ne4 = {};

+++ Added A$ (pretty-v2.1.33.js:517514-517516)
+ function A$(A) {
+   return Sm(rd(), NN1(A));
+ }

+++ Added Xe (pretty-v2.1.33.js:520596-520598)
+ function Xe() {
+   return $M1();
+ }

+++ Added mRA (pretty-v2.1.33.js:520835-520835)
+ var mRA = {};

+++ Added vOq (pretty-v2.1.33.js:521131-521131)
+ var vOq = {};

+++ Added y9z (pretty-v2.1.33.js:521177-521179)
+ function y9z(A) {
+   return /^mcp-cli\s+(call|read)\s+/.test(A);
+ }

+++ Added sOq (pretty-v2.1.33.js:523110-523110)
+ var sOq = {};

+++ Added eOq (pretty-v2.1.33.js:523633-523633)
+ var eOq = {};

+++ Added Y_q (pretty-v2.1.33.js:523714-523714)
+ var Y_q = {};

+++ Added J_q (pretty-v2.1.33.js:523795-523795)
+ var J_q = {};

+++ Added f_q (pretty-v2.1.33.js:524153-524153)
+ var f_q = {};

+++ Added uBA (pretty-v2.1.33.js:524284-524291)
+ function uBA() {
+   if (vWA()) {
+     if (q4() && NX()) bBA();
+     LH4().then(async () => {
+       (je(), await bBA());
+     });
+   } else bBA();
+ }

+++ Added O2z (pretty-v2.1.33.js:528571-528571)
+   O2z = 1,

+++ Added NXq (pretty-v2.1.33.js:534771-534773)
+ function NXq(A, q) {
+   return Md(A, q).isAboveWarningThreshold;
+ }

+++ Added lXq (pretty-v2.1.33.js:535700-535700)
+   lXq = 0,

+++ Added xHz (pretty-v2.1.33.js:538789-538791)
+ function xHz(A) {
+   return A.type === "in_process_teammate" && A.status === "running";
+ }

+++ Added dHz (pretty-v2.1.33.js:538819-538855)
+ function dHz(A, q, K, Y, z, w) {
+   let H;
+   if (w)
+     switch (z) {
+       case "none":
+         H = "show tasks";
+         break;
+       case "tasks":
+         H = "show teammates";
+         break;
+       case "teammates":
+         H = "hide";
+         break;
+     }
+   else H = z === "tasks" ? "hide tasks" : "show tasks";
+   let $ = Y || z !== "none";
+   return [
+     ...(A
+       ? [
+           F7.createElement(
+             f,
+             { dimColor: !0, key: "esc" },
+             F7.createElement(HA, { shortcut: q, action: "interrupt" }),
+           ),
+         ]
+       : []),
+     ...($
+       ? [
+           F7.createElement(
+             f,
+             { dimColor: !0, key: "toggle-tasks" },
+             F7.createElement(HA, { shortcut: K, action: H }),
+           ),
+         ]
+       : []),
+   ];
+ }

+++ Added IMq (pretty-v2.1.33.js:545306-545306)
+ var IMq = {};

+++ Added UOz (pretty-v2.1.33.js:545578-545590)
+ function UOz(A) {
+   let { getAllInProcessTeammateTasks: q } = (PR(), Ly(vE4));
+   if (q(A.tasks).filter(gOz).length > 0)
+     switch (A.expandedView) {
+       case "none":
+         return { ...A, expandedView: "tasks" };
+       case "tasks":
+         return { ...A, expandedView: "teammates" };
+       case "teammates":
+         return { ...A, expandedView: "none" };
+     }
+   return { ...A, expandedView: A.expandedView === "tasks" ? "none" : "tasks" };
+ }

+++ Added gOz (pretty-v2.1.33.js:545591-545593)
+ function gOz(A) {
+   return A.status === "running";
+ }

+++ Added Re (pretty-v2.1.33.js:550286-550288)
+ function Re() {
+   return F_z;
+ }

+++ Added NVq (pretty-v2.1.33.js:551751-551751)
+ var NVq = () => {};

+++ Added TVq (pretty-v2.1.33.js:551752-551752)
+ var TVq = () => {};

+++ Added vVq (pretty-v2.1.33.js:551753-551753)
+ var vVq = () => {};

+++ Added EVq (pretty-v2.1.33.js:551754-551754)
+ var EVq = () => {};

+++ Added kVq (pretty-v2.1.33.js:551755-551755)
+ var kVq = () => {};

+++ Added LVq (pretty-v2.1.33.js:551756-551756)
+ var LVq = () => {};

+++ Added RVq (pretty-v2.1.33.js:551757-551757)
+ var RVq = () => {};

+++ Added yVq (pretty-v2.1.33.js:551758-551758)
+ var yVq = () => {};

+++ Added CVq (pretty-v2.1.33.js:551759-551759)
+ var CVq = () => {};

+++ Added SVq (pretty-v2.1.33.js:551760-551760)
+ var SVq = () => {};

+++ Added DNq (pretty-v2.1.33.js:553111-553117)
+ var DNq = v(() => {
+   d1();
+   nz();
+   lB();
+   yA();
+   pT6 = s(J1(), 1);
+ });

+++ Added SNq (pretty-v2.1.33.js:553450-553453)
+ var SNq = v(() => {
+   NxA();
+   cT6 = s(J1(), 1);
+ });

+++ Added uNq (pretty-v2.1.33.js:553499-553503)
+ var uNq = v(() => {
+   g8();
+   nz();
+   Cd1 = s(J1(), 1);
+ });

+++ Added KXz (pretty-v2.1.33.js:555429-555429)
+   KXz = () => {},

+++ Added nT6 (pretty-v2.1.33.js:555431-555431)
+   nT6 = null;

+++ Added nNq (pretty-v2.1.33.js:555965-555977)
+ var nNq = v(() => {
+   d1();
+   u1();
+   i9();
+   u1();
+   g8();
+   Gh();
+   EH();
+   FhA();
+   nq();
+   jB();
+   ye = s(J1(), 1);
+ });

+++ Added dFA (pretty-v2.1.33.js:556103-556108)
+ var dFA = v(() => {
+   d1();
+   u1();
+   u1();
+   pFA = s(J1(), 1);
+ });

+++ Added qTq (pretty-v2.1.33.js:556230-556243)
+ var qTq = v(() => {
+   d1();
+   u1();
+   wf6();
+   U8();
+   FlA();
+   dFA();
+   B6();
+   lq();
+   mK();
+   qK();
+   nq();
+   zy = s(J1(), 1);
+ });

+++ Added YTq (pretty-v2.1.33.js:556321-556329)
+ var YTq = v(() => {
+   d1();
+   i9();
+   U8();
+   dFA();
+   B6();
+   nq();
+   sT6 = s(J1(), 1);
+ });

+++ Added OQA (pretty-v2.1.33.js:562500-562505)
+ var OQA = v(() => {
+   d1();
+   u1();
+   N5();
+   UA = s(J1(), 1);
+ });

+++ Added bvq (pretty-v2.1.33.js:562506-562506)
+ var bvq = {};

+++ Added avq (pretty-v2.1.33.js:562803-562803)
+ var avq = {};

+++ Added TEq (pretty-v2.1.33.js:564976-564979)
+ var TEq = v(() => {
+   kI();
+   pW1();
+ });

+++ Added EEq (pretty-v2.1.33.js:564983-564994)
+ var EEq = v(() => {
+   KEq();
+   zEq();
+   HEq();
+   JEq();
+   DEq();
+   jEq();
+   GEq();
+   VEq();
+   TEq();
+   Y91();
+ });

+++ Added LEq (pretty-v2.1.33.js:565024-565028)
+ var LEq = v(() => {
+   L6();
+   mA();
+   K8();
+ });

+++ Added $v6 (pretty-v2.1.33.js:565121-565121)
+ var $v6 = {};

+++ Added Ov6 (pretty-v2.1.33.js:565229-565261)
+ var Ov6 = v(() => {
+   Hl();
+   N5();
+   vo();
+   AEq();
+   EEq();
+   rf6();
+   w3();
+   mA();
+   $7();
+   k9();
+   LEq();
+   hwA();
+   L6();
+   mD();
+   m$();
+   qY();
+   s6();
+   iFA();
+   IEq();
+   B6();
+   MI();
+   s6();
+   $51();
+   s6();
+   DP1();
+   BD();
+   eq();
+   Xm();
+   V7();
+   bP1();
+   ZW();
+ });

+++ Added xEq (pretty-v2.1.33.js:565262-565262)
+ var xEq = {};

+++ Added bEq (pretty-v2.1.33.js:565535-565560)
+ var bEq = v(() => {
+   d1();
+   u1();
+   z7();
+   S2();
+   mFA();
+   uxA();
+   L6();
+   V8();
+   oq();
+   QxA();
+   R31();
+   JG1();
+   Cq();
+   Jp();
+   BxA();
+   s6();
+   oq();
+   pk();
+   Fp1();
+   sD();
+   o7();
+   g8();
+   Pd1();
+   cY = s(J1(), 1);
+ });

+++ Added UEq (pretty-v2.1.33.js:565863-565863)
+ var UEq = {};

+++ Added cEq (pretty-v2.1.33.js:566030-566030)
+ var cEq = {};

+++ Added Se (pretty-v2.1.33.js:566118-566118)
+ var Se = {};

+++ Added pDz (pretty-v2.1.33.js:566140-566154)
+ async function pDz({ debug: A, verbose: q }) {
+   let K = UDz();
+   if ((l("tengu_mcp_start", {}), !gDz(K)))
+     (console.error(`Error: Directory ${K} does not exist`), process.exit(1));
+   try {
+     let { setup: Y } = await Promise.resolve().then(() => (Ov6(), $v6));
+     await Y(K, "default", !1, !1, void 0, !1);
+     let { startMCPServer: z } = await Promise.resolve().then(
+       () => (gEq(), UEq),
+     );
+     await z(K, A ?? !1, q ?? !1);
+   } catch (Y) {
+     (console.error("Error: Failed to start MCP server:", Y), process.exit(1));
+   }
+ }

+++ Added dDz (pretty-v2.1.33.js:566155-566214)
+ async function dDz(A, q) {
+   let K = RR(A),
+     Y = () => {
+       if (K && (K.type === "sse" || K.type === "http")) (NP6(A, K), As4(A, K));
+     };
+   try {
+     if (q.scope) {
+       let _ = vG1(q.scope);
+       (l("tengu_mcp_delete", { name: A, scope: _ }),
+         zCA(A, _),
+         Y(),
+         process.stdout.write(`Removed MCP server ${A} from ${_} config
+ `),
+         process.stdout.write(`File modified: ${bG(_)}
+ `),
+         process.exit(0));
+     }
+     let z = GY(),
+       w = j6(),
+       { servers: H } = VJ("project"),
+       $ = !!H[A],
+       O = [];
+     if (z.mcpServers?.[A]) O.push("local");
+     if ($) O.push("project");
+     if (w.mcpServers?.[A]) O.push("user");
+     if (O.length === 0)
+       (process.stderr.write(`No MCP server found with name: "${A}"
+ `),
+         process.exit(1));
+     else if (O.length === 1) {
+       let _ = O[0];
+       (l("tengu_mcp_delete", { name: A, scope: _ }),
+         zCA(A, _),
+         Y(),
+         process.stdout.write(`Removed MCP server "${A}" from ${_} config
+ `),
+         process.stdout.write(`File modified: ${bG(_)}
+ `),
+         process.exit(0));
+     } else
+       (process.stderr.write(`MCP server "${A}" exists in multiple scopes:
+ `),
+         O.forEach((_) => {
+           process.stderr.write(`  - ${vU1(_)} (${bG(_)})
+ `);
+         }),
+         process.stderr.write(`
+ To remove from a specific scope, use:
+ `),
+         O.forEach((_) => {
+           process.stderr.write(`  claude mcp remove "${A}" -s ${_}
+ `);
+         }),
+         process.exit(1));
+   } catch (z) {
+     (process.stderr.write(`${z.message}
+ `),
+       process.exit(1));
+   }
+ }

+++ Added cDz (pretty-v2.1.33.js:566215-566242)
+ async function cDz() {
+   l("tengu_mcp_list", {});
+   let { servers: A } = await wm();
+   if (Object.keys(A).length === 0)
+     console.log(
+       "No MCP servers configured. Use `claude mcp add` to add a server.",
+     );
+   else {
+     console.log(`Checking MCP server health...
+ `);
+     let q = Object.entries(A),
+       K = await WQA(
+         q,
+         async ([Y, z]) => ({ name: Y, server: z, status: await iEq(Y, z) }),
+         { concurrency: pCA() },
+       );
+     for (let { name: Y, server: z, status: w } of K)
+       if (z.type === "sse") console.log(`${Y}: ${z.url} (SSE) - ${w}`);
+       else if (z.type === "http") console.log(`${Y}: ${z.url} (HTTP) - ${w}`);
+       else if (z.type === "claudeai-proxy")
+         console.log(`${Y}: ${z.url} - ${w}`);
+       else if (!z.type || z.type === "stdio") {
+         let H = Array.isArray(z.args) ? z.args : [];
+         console.log(`${Y}: ${z.command} ${H.join(" ")} - ${w}`);
+       }
+   }
+   await RK(0);
+ }

+++ Added lDz (pretty-v2.1.33.js:566243-566291)
+ async function lDz(A) {
+   l("tengu_mcp_get", { name: A });
+   let q = RR(A);
+   if (!q)
+     (console.error(`No MCP server found with name: ${A}`), process.exit(1));
+   (console.log(`${A}:`), console.log(`  Scope: ${vU1(q.scope)}`));
+   let K = await iEq(A, q);
+   if ((console.log(`  Status: ${K}`), q.type === "sse")) {
+     if (
+       (console.log("  Type: sse"), console.log(`  URL: ${q.url}`), q.headers)
+     ) {
+       console.log("  Headers:");
+       for (let [Y, z] of Object.entries(q.headers))
+         console.log(`    ${Y}: ${z}`);
+     }
+     if (q.oauth?.clientId) {
+       let z = !!vCA(A, q)?.clientSecret,
+         w = ["client_id configured"];
+       if (z) w.push("client_secret configured");
+       if (q.oauth.callbackPort) w.push(`callback_port ${q.oauth.callbackPort}`);
+       console.log(`  OAuth: ${w.join(", ")}`);
+     }
+   } else if (q.type === "http") {
+     if (
+       (console.log("  Type: http"), console.log(`  URL: ${q.url}`), q.headers)
+     ) {
+       console.log("  Headers:");
+       for (let [Y, z] of Object.entries(q.headers))
+         console.log(`    ${Y}: ${z}`);
+     }
+     if (q.oauth?.clientId) {
+       let z = !!vCA(A, q)?.clientSecret,
+         w = ["client_id configured"];
+       if (z) w.push("client_secret configured");
+       if (q.oauth.callbackPort) w.push(`callback_port ${q.oauth.callbackPort}`);
+       console.log(`  OAuth: ${w.join(", ")}`);
+     }
+   } else if (q.type === "stdio") {
+     (console.log("  Type: stdio"), console.log(`  Command: ${q.command}`));
+     let Y = Array.isArray(q.args) ? q.args : [];
+     if ((console.log(`  Args: ${Y.join(" ")}`), q.env)) {
+       console.log("  Environment:");
+       for (let [z, w] of Object.entries(q.env)) console.log(`    ${z}=${w}`);
+     }
+   }
+   (console.log(`
+ To remove this server, run: claude mcp remove "${A}" -s ${q.scope}`),
+     await RK(0));
+ }

+++ Added iDz (pretty-v2.1.33.js:566292-566331)
+ async function iDz(A, q, K) {
+   try {
+     let Y = vG1(K.scope),
+       z = T5(q),
+       H =
+         K.clientSecret &&
+         z &&
+         typeof z === "object" &&
+         "type" in z &&
+         (z.type === "sse" || z.type === "http") &&
+         "url" in z &&
+         typeof z.url === "string" &&
+         "oauth" in z &&
+         z.oauth &&
+         typeof z.oauth === "object" &&
+         "clientId" in z.oauth
+           ? await RU1()
+           : void 0;
+     jt(A, z, Y);
+     let $ =
+       z && typeof z === "object" && "type" in z
+         ? String(z.type || "stdio")
+         : "stdio";
+     if (
+       H &&
+       z &&
+       typeof z === "object" &&
+       "type" in z &&
+       (z.type === "sse" || z.type === "http") &&
+       "url" in z &&
+       typeof z.url === "string"
+     )
+       yU1(A, { type: z.type, url: z.url }, H);
+     (l("tengu_mcp_add", { scope: Y, source: "json", type: $ }),
+       console.log(`Added ${$} MCP server ${A} to ${Y} config`),
+       process.exit(0));
+   } catch (Y) {
+     (console.error(Y.message), process.exit(1));
+   }
+ }

+++ Added nDz (pretty-v2.1.33.js:566332-566367)
+ async function nDz(A) {
+   try {
+     let q = vG1(A.scope),
+       K = oA();
+     l("tengu_mcp_add", { scope: q, platform: K, source: "desktop" });
+     let { readClaudeDesktopMcpServers: Y } = await Promise.resolve().then(
+         () => (lEq(), cEq),
+       ),
+       z = Y();
+     if (Object.keys(z).length === 0)
+       (console.log(
+         "No MCP servers found in Claude Desktop configuration or configuration file does not exist.",
+       ),
+         process.exit(0));
+     let { unmount: w } = await s5(
+       Jv6.default.createElement(
+         n9,
+         null,
+         Jv6.default.createElement(
+           iz,
+           null,
+           Jv6.default.createElement(mEq, {
+             servers: z,
+             scope: q,
+             onDone: () => {
+               w();
+             },
+           }),
+         ),
+       ),
+       { exitOnCtrlC: !0 },
+     );
+   } catch (q) {
+     (console.error(q.message), process.exit(1));
+   }
+ }

+++ Added rDz (pretty-v2.1.33.js:566368-566383)
+ async function rDz() {
+   (l("tengu_mcp_reset_mcpjson_choices", {}),
+     E2((A) => ({
+       ...A,
+       enabledMcpjsonServers: [],
+       disabledMcpjsonServers: [],
+       enableAllProjectMcpServers: !1,
+     })),
+     console.log(
+       "All project-scoped (.mcp.json) server approvals and rejections have been reset.",
+     ),
+     console.log(
+       "You will be prompted for approval next time you start Claude Code.",
+     ),
+     process.exit(0));
+ }

+++ Added he (pretty-v2.1.33.js:566385-566401)
+ var he = v(() => {
+   BEq();
+   u1();
+   g8();
+   Gh();
+   FEq();
+   B6();
+   hG();
+   xX();
+   M51();
+   YG();
+   mA();
+   E3();
+   Ww();
+   EH();
+   Jv6 = s(J1(), 1);
+ });

+++ Added Hy (pretty-v2.1.33.js:566402-566402)
+ var Hy = {};

+++ Added Bd1 (pretty-v2.1.33.js:566419-566425)
+ function Bd1(A, q) {
+   (K1(A instanceof Error ? A : Error(String(A))),
+     console.error(
+       `${r1.cross} Failed to ${q}: ${A instanceof Error ? A.message : String(A)}`,
+     ),
+     process.exit(1));
+ }

+++ Added oDz (pretty-v2.1.33.js:566426-566461)
+ function oDz(A, q) {
+   if (q.cowork) UN(!0);
+   try {
+     let K = Rf6(A);
+     if (
+       (console.log(`Validating ${K.fileType} manifest: ${K.filePath}
+ `),
+       K.errors.length > 0)
+     )
+       (console.log(`${r1.cross} Found ${K.errors.length} error${K.errors.length === 1 ? "" : "s"}:
+ `),
+         K.errors.forEach((Y) => {
+           console.log(`  ${r1.pointer} ${Y.path}: ${Y.message}`);
+         }),
+         console.log(""));
+     if (K.warnings.length > 0)
+       (console.log(`${r1.warning} Found ${K.warnings.length} warning${K.warnings.length === 1 ? "" : "s"}:
+ `),
+         K.warnings.forEach((Y) => {
+           console.log(`  ${r1.pointer} ${Y.path}: ${Y.message}`);
+         }),
+         console.log(""));
+     if (K.success) {
+       if (K.warnings.length > 0)
+         console.log(`${r1.tick} Validation passed with warnings`);
+       else console.log(`${r1.tick} Validation passed`);
+       process.exit(0);
+     } else (console.log(`${r1.cross} Validation failed`), process.exit(1));
+   } catch (K) {
+     (K1(K instanceof Error ? K : Error(String(K))),
+       console.error(
+         `${r1.cross} Unexpected error during validation: ${K instanceof Error ? K.message : String(K)}`,
+       ),
+       process.exit(2));
+   }
+ }

+++ Added aDz (pretty-v2.1.33.js:566462-566561)
+ async function aDz(A) {
+   if (A.cowork) UN(!0);
+   l("tengu_plugin_list_command", {});
+   let q = Jj(),
+     { getEnabledPluginsWithScopes: K } = await Promise.resolve().then(
+       () => (TP1(), X4q),
+     ),
+     Y = K(),
+     z = Object.keys(q.plugins);
+   if (A.json) {
+     let { enabled: H, disabled: $, errors: O } = await BY(),
+       _ = [...H, ...$],
+       J = new Map(_.map((D) => [D.source, D])),
+       X = [];
+     for (let D of z.sort()) {
+       let M = q.plugins[D];
+       if (!M || M.length === 0) continue;
+       let j = D.split("@")[0],
+         W = O.filter(
+           (G) => G.source === D || ("plugin" in G && G.plugin === j),
+         ).map(sP);
+       for (let G of M) {
+         let P = J.get(D),
+           V;
+         if (P) {
+           let Z = P.mcpServers || (await SXA(P));
+           if (Z && Object.keys(Z).length > 0) V = Z;
+         }
+         X.push({
+           id: D,
+           version: G.version || "unknown",
+           scope: G.scope,
+           enabled: Y.has(D),
+           installPath: G.installPath,
+           installedAt: G.installedAt,
+           lastUpdated: G.lastUpdated,
+           projectPath: G.projectPath,
+           mcpServers: V,
+           errors: W.length > 0 ? W : void 0,
+         });
+       }
+     }
+     if (A.available) {
+       let D = [];
+       try {
+         let [M, j] = await Promise.all([g5(), ZP1()]),
+           { marketplaces: W } = await Rg(M);
+         for (let { name: G, data: P } of W)
+           if (P)
+             for (let V of P.plugins) {
+               let Z = pu(V.name, G);
+               if (!Xj(Z))
+                 D.push({
+                   pluginId: Z,
+                   name: V.name,
+                   description: V.description,
+                   marketplaceName: G,
+                   version: V.version,
+                   source: V.source,
+                   installCount: j?.get(Z),
+                 });
+             }
+       } catch {}
+       console.log(Q1({ installed: X, available: D }, null, 2));
+     } else console.log(Q1(X, null, 2));
+     process.exit(0);
+   }
+   if (z.length === 0)
+     (console.log(
+       "No plugins installed. Use `claude plugin install` to install a plugin.",
+     ),
+       process.exit(0));
+   let { errors: w } = await BY();
+   console.log(`Installed plugins:
+ `);
+   for (let H of z.sort()) {
+     let $ = q.plugins[H];
+     if (!$ || $.length === 0) continue;
+     let O = H.split("@")[0],
+       _ = w.filter((J) => J.source === H || ("plugin" in J && J.plugin === O));
+     for (let J of $) {
+       let X = Y.has(H),
+         D =
+           _.length > 0
+             ? `${r1.cross} failed to load`
+             : X
+               ? `${r1.tick} enabled`
+               : `${r1.cross} disabled`,
+         M = J.version || "unknown",
+         j = J.scope;
+       (console.log(`  ${r1.pointer} ${H}`),
+         console.log(`    Version: ${M}`),
+         console.log(`    Scope: ${j}`),
+         console.log(`    Status: ${D}`));
+       for (let W of _) console.log(`    Error: ${sP(W)}`);
+       console.log("");
+     }
+   }
+   process.exit(0);
+ }

+++ Added sDz (pretty-v2.1.33.js:566562-566587)
+ async function sDz(A, q) {
+   if (q.cowork) UN(!0);
+   try {
+     let K = jf6(A);
+     if (!K)
+       (console.error(
+         `${r1.cross} Invalid marketplace source format. Try: owner/repo, https://..., or ./path`,
+       ),
+         process.exit(1));
+     if ("error" in K)
+       (console.error(`${r1.cross} ${K.error}`), process.exit(1));
+     let Y = K;
+     console.log("Adding marketplace...");
+     let { name: z } = await mv(Y, (H) => {
+       console.log(H);
+     });
+     cw();
+     let w = Y.source;
+     if (Y.source === "github") w = Y.repo;
+     (l("tengu_marketplace_added", { source_type: w }),
+       console.log(`${r1.tick} Successfully added marketplace: ${z}`),
+       process.exit(0));
+   } catch (K) {
+     Bd1(K, "add marketplace");
+   }
+ }

+++ Added tDz (pretty-v2.1.33.js:566588-566635)
+ async function tDz(A) {
+   if (A.cowork) UN(!0);
+   try {
+     let q = await g5(),
+       K = Object.keys(q);
+     if (A.json) {
+       let Y = K.sort().map((z) => {
+         let w = q[z],
+           H = w?.source;
+         return {
+           name: z,
+           source: H?.source,
+           ...(H?.source === "github" && { repo: H.repo }),
+           ...(H?.source === "git" && { url: H.url }),
+           ...(H?.source === "url" && { url: H.url }),
+           ...(H?.source === "directory" && { path: H.path }),
+           ...(H?.source === "file" && { path: H.path }),
+           installLocation: w?.installLocation,
+         };
+       });
+       (console.log(Q1(Y, null, 2)), process.exit(0));
+     }
+     if (K.length === 0)
+       (console.log("No marketplaces configured"), process.exit(0));
+     (console.log(`Configured marketplaces:
+ `),
+       K.forEach((Y) => {
+         let z = q[Y];
+         if ((console.log(`  ${r1.pointer} ${Y}`), z?.source)) {
+           let w = z.source;
+           if (w.source === "github")
+             console.log(`    Source: GitHub (${w.repo})`);
+           else if (w.source === "git")
+             console.log(`    Source: Git (${w.url})`);
+           else if (w.source === "url")
+             console.log(`    Source: URL (${w.url})`);
+           else if (w.source === "directory")
+             console.log(`    Source: Directory (${w.path})`);
+           else if (w.source === "file")
+             console.log(`    Source: File (${w.path})`);
+         }
+         console.log("");
+       }),
+       process.exit(0));
+   } catch (q) {
+     Bd1(q, "list marketplaces");
+   }
+ }

+++ Added eDz (pretty-v2.1.33.js:566636-566647)
+ async function eDz(A, q) {
+   if (q.cowork) UN(!0);
+   try {
+     (await sG6(A),
+       cw(),
+       l("tengu_marketplace_removed", { marketplace_name: A }),
+       console.log(`${r1.tick} Successfully removed marketplace: ${A}`),
+       process.exit(0));
+   } catch (K) {
+     Bd1(K, "remove marketplace");
+   }
+ }

+++ Added AMz (pretty-v2.1.33.js:566648-566677)
+ async function AMz(A, q) {
+   if (q.cowork) UN(!0);
+   try {
+     if (A)
+       (console.log(`Updating marketplace: ${A}...`),
+         await Mt(A, (K) => {
+           console.log(K);
+         }),
+         cw(),
+         l("tengu_marketplace_updated", { marketplace_name: A }),
+         console.log(`${r1.tick} Successfully updated marketplace: ${A}`),
+         process.exit(0));
+     else {
+       let K = await g5(),
+         Y = Object.keys(K);
+       if (Y.length === 0)
+         (console.log("No marketplaces configured"), process.exit(0));
+       (console.log(`Updating ${Y.length} marketplace(s)...`),
+         await So4(),
+         cw(),
+         l("tengu_marketplace_updated_all", { count: Y.length }),
+         console.log(
+           `${r1.tick} Successfully updated ${Y.length} marketplace(s)`,
+         ),
+         process.exit(0));
+     }
+   } catch (K) {
+     Bd1(K, "update marketplace(s)");
+   }
+ }

+++ Added qMz (pretty-v2.1.33.js:566678-566688)
+ async function qMz(A, q) {
+   if (q.cowork) UN(!0);
+   let K = q.scope || "user";
+   if (q.cowork && K !== "user")
+     (console.error("--cowork can only be used with user scope"),
+       process.exit(1));
+   if (!rj.includes(K))
+     (console.error(`Invalid scope: ${K}. Must be one of: ${rj.join(", ")}.`),
+       process.exit(1));
+   (l("tengu_plugin_install_command", { plugin: A, scope: K }), await rNq(A, K));
+ }

+++ Added KMz (pretty-v2.1.33.js:566689-566700)
+ async function KMz(A, q) {
+   if (q.cowork) UN(!0);
+   let K = q.scope || "user";
+   if (q.cowork && K !== "user")
+     (console.error("--cowork can only be used with user scope"),
+       process.exit(1));
+   if (!rj.includes(K))
+     (console.error(`Invalid scope: ${K}. Must be one of: ${rj.join(", ")}.`),
+       process.exit(1));
+   (l("tengu_plugin_uninstall_command", { plugin: A, scope: K }),
+     await oNq(A, K));
+ }

+++ Added YMz (pretty-v2.1.33.js:566701-566716)
+ async function YMz(A, q) {
+   if (q.cowork) UN(!0);
+   let K = "user";
+   if (q.scope) {
+     if (!rj.includes(q.scope))
+       (process.stderr
+         .write(`Invalid scope "${q.scope}". Valid scopes: ${rj.join(", ")}
+ `),
+         process.exit(1));
+     K = q.scope;
+   }
+   if (q.cowork && K !== "user")
+     (console.error("--cowork can only be used with user scope"),
+       process.exit(1));
+   (l("tengu_plugin_enable_command", { plugin: A, scope: K }), await aNq(A, K));
+ }

+++ Added zMz (pretty-v2.1.33.js:566717-566749)
+ async function zMz(A, q) {
+   if (q.all && A)
+     (process.stderr.write(`Cannot use --all with a specific plugin
+ `),
+       process.exit(1));
+   if (!q.all && !A)
+     (process.stderr
+       .write(`Please specify a plugin name or use --all to disable all plugins
+ `),
+       process.exit(1));
+   if (q.cowork) UN(!0);
+   if (q.all) {
+     if (q.scope)
+       (process.stderr.write(`Cannot use --scope with --all
+ `),
+         process.exit(1));
+     (l("tengu_plugin_disable_command", { plugin: "--all" }), await tNq());
+     return;
+   }
+   let K = "user";
+   if (q.scope) {
+     if (!rj.includes(q.scope))
+       (process.stderr
+         .write(`Invalid scope "${q.scope}". Valid scopes: ${rj.join(", ")}
+ `),
+         process.exit(1));
+     K = q.scope;
+   }
+   if (q.cowork && K !== "user")
+     (console.error("--cowork can only be used with user scope"),
+       process.exit(1));
+   (l("tengu_plugin_disable_command", { plugin: A, scope: K }), await sNq(A, K));
+ }

+++ Added wMz (pretty-v2.1.33.js:566750-566766)
+ async function wMz(A, q) {
+   if (q.cowork) UN(!0);
+   l("tengu_plugin_update_command", {});
+   let K = "user";
+   if (q.scope) {
+     if (!U51.includes(q.scope))
+       (process.stderr
+         .write(`Invalid scope "${q.scope}". Valid scopes: ${U51.join(", ")}
+ `),
+         process.exit(1));
+     K = q.scope;
+   }
+   if (q.cowork && K !== "user")
+     (console.error("--cowork can only be used with user scope"),
+       process.exit(1));
+   await eNq(A, K);
+ }

+++ Added $y (pretty-v2.1.33.js:566767-566784)
+ var $y = v(() => {
+   I7();
+   I6();
+   B6();
+   L6();
+   PIA();
+   u$();
+   Ro();
+   Dj();
+   hR();
+   Gf6();
+   wIA();
+   gFA();
+   Dj();
+   D_();
+   q$6();
+   s6();
+ });

+++ Added rEq (pretty-v2.1.33.js:566785-566785)
+ var rEq = {};

+++ Added Xv6 (pretty-v2.1.33.js:567066-567066)
+ var Xv6 = {};

+++ Added MMz (pretty-v2.1.33.js:567073-567108)
+ async function MMz() {
+   if ((l("tengu_setup_token_command", {}), await Oo(), !df()))
+     (process.stderr.write(
+       K6.yellow(`Warning: You already have authentication configured via environment variable or API key helper.
+ `),
+     ),
+       process.stderr.write(
+         K6.yellow(`The setup-token command will create a new OAuth token which you can use instead.
+ `),
+       ));
+   let { ConsoleOAuthFlow: A } = await Promise.resolve().then(
+     () => (Im1(), $R4),
+   );
+   (await new Promise(async (q) => {
+     let { unmount: K } = await s5(
+       WE.default.createElement(
+         n9,
+         { onChangeAppState: xI },
+         WE.default.createElement(
+           I,
+           { flexDirection: "column", gap: 1 },
+           WE.default.createElement(wv6, null),
+           WE.default.createElement(A, {
+             onDone: () => {
+               (K(), q());
+             },
+             mode: "setup-token",
+             startingMessage:
+               "This will guide you through long-lived (1-year) auth token setup for your Claude account. Claude subscription required.",
+           }),
+         ),
+       ),
+     );
+   }),
+     process.exit(0));
+ }

+++ Added GMz (pretty-v2.1.33.js:567125-567150)
+ async function GMz() {
+   (l("tengu_doctor_command", {}),
+     await new Promise(async (A) => {
+       let { unmount: q } = await s5(
+         WE.default.createElement(
+           n9,
+           null,
+           WE.default.createElement(
+             iz,
+             null,
+             WE.default.createElement(
+               $f6,
+               { dynamicMcpConfig: void 0, isStrictMcpConfig: !1 },
+               WE.default.createElement(WMz, {
+                 onDone: () => {
+                   (q(), A());
+                 },
+               }),
+             ),
+           ),
+         ),
+         mw(!1),
+       );
+     }),
+     process.exit(0));
+ }

+++ Added PMz (pretty-v2.1.33.js:567151-567167)
+ async function PMz(A, q) {
+   let { setup: K } = await Promise.resolve().then(() => (Ov6(), $v6));
+   await K(DMz(), "default", !1, !1, void 0, !1);
+   let { install: Y } = await Promise.resolve().then(() => (oEq(), rEq));
+   await new Promise((z) => {
+     let w = [];
+     if (A) w.push(A);
+     if (q.force) w.push("--force");
+     Y.call(
+       (H) => {
+         (z(), process.exit(H.includes("failed") ? 1 : 0));
+       },
+       {},
+       w,
+     );
+   });
+ }

+++ Added Dv6 (pretty-v2.1.33.js:567169-567189)
+ var Dv6 = v(() => {
+   d1();
+   w3();
+   u1();
+   jB();
+   g8();
+   Gh();
+   ht();
+   OQA();
+   rFA();
+   _FA();
+   B6();
+   $7();
+   L41();
+   WE = s(J1(), 1);
+   jMz = WE.default.lazy(() =>
+     Promise.resolve()
+       .then(() => (dhA(), rAq))
+       .then((A) => ({ default: A.Doctor })),
+   );
+ });

+++ Added aEq (pretty-v2.1.33.js:567190-567190)
+ var aEq = {};

+++ Added sEq (pretty-v2.1.33.js:567678-567692)
+ var sEq = v(() => {
+   B6();
+   vs();
+   ZM6();
+   mA();
+   Z31();
+   MI();
+   lB();
+   w3();
+   M6();
+   EH();
+   U8();
+   xwA();
+   Mv6 = s(nC(), 1);
+ });

+++ Added Ykq (pretty-v2.1.33.js:567693-567693)
+ var Ykq = {};

+++ Added PQA (pretty-v2.1.33.js:570082-570082)
+ function PQA(A) {}

+++ Added import@560160 (pretty-v2.1.33.js:560161-560161)
+ import { realpathSync as _0z, existsSync as J0z } from "fs";

+++ Added import@567699 (pretty-v2.1.33.js:567700-567700)
+ import { readFileSync as tEq, existsSync as Akq } from "fs";

+++ Added import@565028 (pretty-v2.1.33.js:565029-565029)
+ import { dirname as vDz, join as yEq } from "path";

+++ Added import@567071 (pretty-v2.1.33.js:567072-567072)
+ import { cwd as DMz } from "process";

+++ Added import@567700 (pretty-v2.1.33.js:567701-567701)
+ import { cwd as NMz } from "process";

=== Structural Changes ===

@@@ function 'xmA' (was 'XmA') — structural (98.9%)
--- pretty-v2.1.32.js:539268
+++ pretty-v2.1.33.js:537681
@@ -22,7 +22,7 @@
     ((M = Object.values(D ?? {}).filter(B2z)), (q[1] = D), (q[2] = M));
   else M = q[2];
   let W = M,
-    G = T6(u2z),
+    P = E6(_Hz) === "teammates",
     P = !G && W.length > 0 && W.every(b2z),
     V;
   if (q[3] !== W) ((V = W.filter(x2z).sort(I2z)), (q[3] = W), (q[4] = V));
@@ -202,7 +202,13 @@
         (q[51] = r));
     else r = q[51];
     let z1;
-    if (q[52] !== g || q[53] !== x || q[54] !== p || q[55] !== n || q[56] !== r)
+    if (
+      q[52] !== B ||
+      q[53] !== p ||
+      q[54] !== r ||
+      q[55] !== c ||
+      q[56] !== Y1
+    )
       ((z1 = l4.createElement(g, { color: x, inverse: p }, n, " ", r)),
         (q[52] = g),
         (q[53] = x),

@@@ variable 'zA7' (was 'lW7') — structural (98.5%)
--- pretty-v2.1.32.js:186921
+++ pretty-v2.1.33.js:151104
@@ -17,6 +17,7 @@
   Z5();
   BA();
   e81();
+  s6();
   ((gC = a($1(), 1)),
     (cW7 = ["iTerm.app", "kitty", "WezTerm", "ghostty"]),
     (Tp5 = process.platform !== "win32"));

@@@ function 'Yf6' (was 'aZ6') — structural (97.3%)
--- pretty-v2.1.32.js:465008
+++ pretty-v2.1.33.js:464985
@@ -153,7 +153,7 @@
     ((V1 = O4.createElement(
       I,
       null,
-      O4.createElement(f, { dimColor: K }, X, " to show todos"),
+      w4.createElement(f, { dimColor: K }, X, " to toggle tasks"),
     )),
       (q[43] = K),
       (q[44] = X),
@@ -311,7 +311,13 @@
       (q[83] = X1));
   else X1 = q[83];
   let S1;
-  if (q[84] !== z || q[85] !== w || q[86] !== D1 || q[87] !== s || q[88] !== X1)
+  if (
+    q[84] !== z ||
+    q[85] !== w ||
+    q[86] !== M1 ||
+    q[87] !== A1 ||
+    q[88] !== D1
+  )
     ((S1 = O4.createElement(
       I,
       { paddingX: w, flexDirection: "row", gap: z },

@@@ variable 'AD' (was 'n0') — structural (97.3%)
--- pretty-v2.1.32.js:73421
+++ pretty-v2.1.33.js:45333
@@ -2,7 +2,7 @@
   A4();
   La1();
   N61();
-  sN = new Set([
+  ((eN = new Set([
     "claude-code-marketplace",
     "claude-code-plugins",
     "claude-plugins-official",
@@ -10,17 +10,22 @@
     "anthropic-plugins",
     "agent-skills",
     "life-sciences",
-  ]);
+    "knowledge-work-plugins",
+  ])),
+    (zwK = new Set(["knowledge-work-plugins"])));
   ((JJK =
     /(?:official[^a-z0-9]*(anthropic|claude)|(?:anthropic|claude)[^a-z0-9]*official|^(?:anthropic|claude)[^a-z0-9]*(marketplace|plugins|official))/i),
     (XJK = /[^\u0020-\u007E]/));
   ((UF = B.string().startsWith("./")),
     (jw1 = UF.endsWith(".json")),
     (XX8 = B.union([
-      UF.refine((A) => A.endsWith(".mcpb") || A.endsWith(".dxt"), {
-        message: "MCPB file path must end with .mcpb or .dxt",
-      }).describe("Path to MCPB file relative to plugin root"),
-      B.string()
+      lF
+        .refine((A) => A.endsWith(".mcpb") || A.endsWith(".dxt"), {
+          message: "MCPB file path must end with .mcpb or .dxt",
+        })
+        .describe("Path to MCPB file relative to plugin root"),
+      b
+        .string()
         .url()
         .refine((A) => A.endsWith(".mcpb") || A.endsWith(".dxt"), {
           message: "MCPB URL must end with .mcpb or .dxt",
@@ -30,18 +35,22 @@
     (gB6 = UF.endsWith(".md")),
     (UB6 = B.union([gB6, UF])),
     (WX8 = B.object({
-      name: B.string()
+      name: b
+        .string()
         .min(1, "Author name cannot be empty")
         .describe("Display name of the plugin author or organization"),
-      email: B.string()
+      email: b
+        .string()
         .optional()
         .describe("Contact email for support or feedback"),
-      url: B.string()
+      url: b
+        .string()
         .optional()
         .describe("Website, GitHub profile, or organization URL"),
     })),
     (jJK = B.object({
-      name: B.string()
+      name: b
+        .string()
         .min(1, "Plugin name cannot be empty")
         .refine((A) => !A.includes(" "), {
           message:
@@ -50,93 +59,115 @@
         .describe(
           "Unique identifier for the plugin, used for namespacing (prefer kebab-case)",
         ),
-      version: B.string()
+      version: b
+        .string()
         .optional()
         .describe(
           "Semantic version (e.g., 1.2.3) following semver.org specification",
         ),
-      description: B.string()
+      description: b
+        .string()
         .optional()
         .describe("Brief, user-facing explanation of what the plugin provides"),
       author: WX8.optional().describe(
         "Information about the plugin creator or maintainer",
       ),
-      homepage: B.string()
+      homepage: b
+        .string()
         .url()
         .optional()
         .describe("Plugin homepage or documentation URL"),
       repository: B.string().optional().describe("Source code repository URL"),
-      license: B.string()
+      license: b
+        .string()
         .optional()
         .describe("SPDX license identifier (e.g., MIT, Apache-2.0)"),
-      keywords: B.array(B.string())
+      keywords: b
+        .array(b.string())
         .optional()
         .describe("Tags for plugin discovery and categorization"),
     })),
     (GX8 = B.object({
-      description: B.string()
+      description: b
+        .string()
         .optional()
         .describe("Brief, user-facing explanation of what these hooks provide"),
-      hooks: B.lazy(() => pE).describe(
-        "The hooks provided by the plugin, in the same format as the one used for settings",
-      ),
+      hooks: b
+        .lazy(() => dE)
+        .describe(
+          "The hooks provided by the plugin, in the same format as the one used for settings",
+        ),
     })),
     (MJK = B.object({
       hooks: B.union([
         jw1.describe(
           "Path to file with additional hooks (in addition to those in hooks/hooks.json, if it exists), relative to the plugin root",
         ),
-        B.lazy(() => pE).describe(
-          "Additional hooks (in addition to those in hooks/hooks.json, if it exists)",
-        ),
+        b
+          .lazy(() => dE)
+          .describe(
+            "Additional hooks (in addition to those in hooks/hooks.json, if it exists)",
+          ),
         B.array(
           B.union([
             jw1.describe(
               "Path to file with additional hooks (in addition to those in hooks/hooks.json, if it exists), relative to the plugin root",
             ),
-            B.lazy(() => pE).describe(
-              "Additional hooks (in addition to those in hooks/hooks.json, if it exists)",
-            ),
+            b
+              .lazy(() => dE)
+              .describe(
+                "Additional hooks (in addition to those in hooks/hooks.json, if it exists)",
+              ),
           ]),
         ),
       ]),
     })),
-    (WJK = B.object({
-      source: UB6.optional().describe(
-        "Path to command markdown file, relative to plugin root",
-      ),
-      content: B.string()
-        .optional()
-        .describe("Inline markdown content for the command"),
-      description: B.string()
-        .optional()
-        .describe("Command description override"),
-      argumentHint: B.string()
-        .optional()
-        .describe('Hint for command arguments (e.g., "[file]")'),
-      model: B.string().optional().describe("Default model for this command"),
-      allowedTools: B.array(B.string())
-        .optional()
-        .describe("Tools allowed when command runs"),
-    }).refine((A) => (A.source && !A.content) || (!A.source && A.content), {
-      message:
-        'Command must have either "source" (file path) or "content" (inline markdown), but not both',
-    })),
+    (JwK = b
+      .object({
+        source: CB6.optional().describe(
+          "Path to command markdown file, relative to plugin root",
+        ),
+        content: b
+          .string()
+          .optional()
+          .describe("Inline markdown content for the command"),
+        description: b
+          .string()
+          .optional()
+          .describe("Command description override"),
+        argumentHint: b
+          .string()
+          .optional()
+          .describe('Hint for command arguments (e.g., "[file]")'),
+        model: b.string().optional().describe("Default model for this command"),
+        allowedTools: b
+          .array(b.string())
+          .optional()
+          .describe("Tools allowed when command runs"),
+      })
+      .refine((A) => (A.source && !A.content) || (!A.source && A.content), {
+        message:
+          'Command must have either "source" (file path) or "content" (inline markdown), but not both',
+      })),
     (GJK = B.object({
       commands: B.union([
         UB6.describe(
           "Path to additional command file or skill directory (in addition to those in the commands/ directory, if it exists), relative to the plugin root",
         ),
-        B.array(
-          UB6.describe(
-            "Path to additional command file or skill directory (in addition to those in the commands/ directory, if it exists), relative to the plugin root",
+        b
+          .array(
+            CB6.describe(
+              "Path to additional command file or skill directory (in addition to those in the commands/ directory, if it exists), relative to the plugin root",
+            ),
+          )
+          .describe(
+            "List of paths to additional command files or skill directories",
+          ),
+        b
+          .record(b.string(), JwK)
+          .describe(
+            'Object mapping of command names to their metadata and source files. Command name becomes the slash command name (e.g., "about" → "/plugin:about")',
           ),
-        ).describe(
-          "List of paths to additional command files or skill directories",
-        ),
-        B.record(B.string(), WJK).describe(
-          'Object mapping of command names to their metadata and source files. Command name becomes the slash command name (e.g., "about" → "/plugin:about")',
-        ),
       ]),
     })),
     (PJK = B.object({
@@ -144,11 +175,13 @@
         gB6.describe(
           "Path to additional agent file (in addition to those in the agents/ directory, if it exists), relative to the plugin root",
         ),
-        B.array(
-          gB6.describe(
-            "Path to additional agent file (in addition to those in the agents/ directory, if it exists), relative to the plugin root",
-          ),
-        ).describe("List of paths to additional agent files"),
+        b
+          .array(
+            yB6.describe(
+              "Path to additional agent file (in addition to those in the agents/ directory, if it exists), relative to the plugin root",
+            ),
+          )
+          .describe("List of paths to additional agent files"),
       ]),
     })),
     (ZJK = B.object({
@@ -156,11 +189,13 @@
         UF.describe(
           "Path to additional skill directory (in addition to those in the skills/ directory, if it exists), relative to the plugin root",
         ),
-        B.array(
-          UF.describe(
-            "Path to additional skill directory (in addition to those in the skills/ directory, if it exists), relative to the plugin root",
-          ),
-        ).describe("List of paths to additional skill directories"),
+        b
+          .array(
+            lF.describe(
+              "Path to additional skill directory (in addition to those in the skills/ directory, if it exists), relative to the plugin root",
+            ),
+          )
+          .describe("List of paths to additional skill directories"),
       ]),
     })),
     (fJK = B.object({
@@ -168,13 +203,15 @@
         UF.describe(
           "Path to additional output styles directory or file (in addition to those in the output-styles/ directory, if it exists), relative to the plugin root",
         ),
-        B.array(
-          UF.describe(
-            "Path to additional output styles directory or file (in addition to those in the output-styles/ directory, if it exists), relative to the plugin root",
+        b
+          .array(
+            lF.describe(
+              "Path to additional output styles directory or file (in addition to those in the output-styles/ directory, if it exists), relative to the plugin root",
+            ),
+          )
+          .describe(
+            "List of paths to additional output styles directories or files",
           ),
-        ).describe(
-          "List of paths to additional output styles directories or files",
-        ),
       ]),
     })),
     (VJK = B.object({
@@ -184,31 +221,35 @@
         ),
         XX8.describe(
           "Path or URL to MCPB file containing MCP server configuration",
-        ),
-        B.record(B.string(), Ex).describe(
-          "MCP server configurations keyed by server name",
         ),
-        B.array(
-          B.union([
-            jw1.describe("Path to MCP servers configuration file"),
-            XX8.describe("Path or URL to MCPB file"),
-            B.record(B.string(), Ex).describe(
-              "Inline MCP server configurations",
-            ),
-          ]),
-        ).describe(
-          "Array of MCP server configurations (paths, MCPB files, or inline definitions)",
-        ),
+        b
+          .record(b.string(), Rx)
+          .describe("MCP server configurations keyed by server name"),
+        b
+          .array(
+            b.union([
+              Aw1.describe("Path to MCP servers configuration file"),
+              Tz8.describe("Path or URL to MCPB file"),
+              b
+                .record(b.string(), Rx)
+                .describe("Inline MCP server configurations"),
+            ]),
+          )
+          .describe(
+            "Array of MCP server configurations (paths, MCPB files, or inline definitions)",
+          ),
       ]),
     })),
     (DX8 = B.string().min(1)),
-    (NJK = B.string()
+    (GwK = b
+      .string()
       .min(2)
       .refine((A) => A.startsWith("."), {
         message: 'File extensions must start with dot (e.g., ".ts", not "ts")',
       })),
     (Mw1 = B.strictObject({
-      command: B.string()
+      command: b
+        .string()
         .min(1)
         .refine(
           (A) => {
@@ -223,49 +264,60 @@
         .describe(
           'Command to execute the LSP server (e.g., "typescript-language-server")',
         ),
-      args: B.array(DX8)
+      args: b
+        .array(vz8)
         .optional()
         .describe("Command-line arguments to pass to the server"),
-      extensionToLanguage: B.record(NJK, DX8)
+      extensionToLanguage: b
+        .record(GwK, vz8)
         .refine((A) => Object.keys(A).length > 0, {
           message: "extensionToLanguage must have at least one mapping",
         })
         .describe(
           "Mapping from file extension to LSP language ID. File extensions and languages are derived from this mapping.",
         ),
-      transport: B.enum(["stdio", "socket"])
+      transport: b
+        .enum(["stdio", "socket"])
         .default("stdio")
         .describe("Communication transport mechanism"),
-      env: B.record(B.string(), B.string())
+      env: b
+        .record(b.string(), b.string())
         .optional()
         .describe("Environment variables to set when starting the server"),
-      initializationOptions: B.unknown()
+      initializationOptions: b
+        .unknown()
         .optional()
         .describe(
           "Initialization options passed to the server during initialization",
         ),
-      settings: B.unknown()
+      settings: b
+        .unknown()
         .optional()
         .describe(
           "Settings passed to the server via workspace/didChangeConfiguration",
         ),
-      workspaceFolder: B.string()
+      workspaceFolder: b
+        .string()
         .optional()
         .describe("Workspace folder path to use for the server"),
-      startupTimeout: B.number()
+      startupTimeout: b
+        .number()
         .int()
         .positive()
         .optional()
         .describe("Maximum time to wait for server startup (milliseconds)"),
-      shutdownTimeout: B.number()
+      shutdownTimeout: b
+        .number()
         .int()
         .positive()
         .optional()
         .describe("Maximum time to wait for graceful shutdown (milliseconds)"),
-      restartOnCrash: B.boolean()
+      restartOnCrash: b
+        .boolean()
         .optional()
         .describe("Whether to restart the server if it crashes"),
-      maxRestarts: B.number()
+      maxRestarts: b
+        .number()
         .int()
         .nonnegative()
         .optional()
@@ -276,32 +328,37 @@
         jw1.describe(
           "Path to .lsp.json configuration file relative to plugin root",
         ),
-        B.record(B.string(), Mw1).describe(
-          "LSP server configurations keyed by server name",
-        ),
-        B.array(
-          B.union([
-            jw1.describe("Path to LSP configuration file"),
-            B.record(B.string(), Mw1).describe(
-              "Inline LSP server configurations",
-            ),
-          ]),
-        ).describe(
-          "Array of LSP server configurations (paths or inline definitions)",
-        ),
+        b
+          .record(b.string(), qw1)
+          .describe("LSP server configurations keyed by server name"),
+        b
+          .array(
+            b.union([
+              Aw1.describe("Path to LSP configuration file"),
+              b
+                .record(b.string(), qw1)
+                .describe("Inline LSP server configurations"),
+            ]),
+          )
+          .describe(
+            "Array of LSP server configurations (paths or inline definitions)",
+          ),
       ]),
     })),
-    (v61 = B.object({
-      ...jJK.shape,
-      ...MJK.partial().shape,
-      ...GJK.partial().shape,
-      ...PJK.partial().shape,
-      ...ZJK.partial().shape,
-      ...fJK.partial().shape,
-      ...VJK.partial().shape,
-      ...TJK.partial().shape,
-    }).strict()),
-    (PX8 = B.string()
+    (V61 = b
+      .object({
+        ...OwK.shape,
+        ..._wK.partial().shape,
+        ...XwK.partial().shape,
+        ...DwK.partial().shape,
+        ...MwK.partial().shape,
+        ...jwK.partial().shape,
+        ...WwK.partial().shape,
+        ...PwK.partial().shape,
+      })
+      .strict()),
+    (yz8 = b
+      .string()
       .refine(
         (A) => !A.includes("..") && !A.includes("//"),
         "Package name cannot contain path traversal patterns",
@@ -315,19 +372,22 @@
       B.object({
         source: B.literal("url"),
         url: B.string().url().describe("Direct URL to marketplace.json file"),
-        headers: B.record(B.string(), B.string())
+        headers: b
+          .record(b.string(), b.string())
           .optional()
           .describe("Custom HTTP headers (e.g., for authentication)"),
       }),
       B.object({
         source: B.literal("github"),
         repo: B.string().describe("GitHub repository in owner/repo format"),
-        ref: B.string()
+        ref: b
+          .string()
           .optional()
           .describe(
             'Git branch or tag to use (e.g., "main", "v1.0.0"). Defaults to repository default branch.',
           ),
-        path: B.string()
+        path: b
+          .string()
           .optional()
           .describe(
             "Path to marketplace.json within repo (defaults to .claude-plugin/marketplace.json)",
@@ -336,12 +396,14 @@
       B.object({
         source: B.literal("git"),
         url: B.string().endsWith(".git").describe("Full git repository URL"),
-        ref: B.string()
+        ref: b
+          .string()
           .optional()
           .describe(
             'Git branch or tag to use (e.g., "main", "v1.0.0"). Defaults to repository default branch.',
           ),
-        path: B.string()
+        path: b
+          .string()
           .optional()
           .describe(
             "Path to marketplace.json within repo (defaults to .claude-plugin/marketplace.json)",
@@ -357,18 +419,23 @@
       }),
       B.object({
         source: B.literal("directory"),
-        path: B.string().describe(
-          "Local directory containing .claude-plugin/marketplace.json",
-        ),
+        path: b
+          .string()
+          .describe(
+            "Local directory containing .claude-plugin/marketplace.json",
+          ),
       }),
       B.object({
         source: B.literal("hostPattern"),
-        hostPattern: B.string().describe(
-          'Regex pattern to match the host/domain extracted from any marketplace source type. For github sources, matches against "github.com". For git sources (SSH or HTTPS), extracts the hostname from the URL. Use in strictKnownMarketplaces to allow all marketplaces from a specific host (e.g., "^github\\.mycompany\\.com$").',
-        ),
+        hostPattern: b
+          .string()
+          .describe(
+            'Regex pattern to match the host/domain extracted from any marketplace source type. For github sources, matches against "github.com". For git sources (SSH or HTTPS), extracts the hostname from the URL. Use in strictKnownMarketplaces to allow all marketplaces from a specific host (e.g., "^github\\.mycompany\\.com$").',
+          ),
       }),
     ])),
-    (jX8 = B.string()
+    (Ez8 = b
+      .string()
       .length(40)
       .regex(
         /^[a-f0-9]{40}$/,
@@ -378,42 +445,56 @@
       UF.describe(
         "Path to the plugin root, relative to the marketplace directory",
       ),
-      B.object({
-        source: B.literal("npm"),
-        package: PX8.or(B.string()).describe(
-          "Package name (or url, or local path, or anything else that can be passed to `npm` as a package)",
-        ),
-        version: B.string()
-          .optional()
-          .describe("Specific version or version range (e.g., ^1.0.0, ~2.1.0)"),
-        registry: B.string()
-          .url()
-          .optional()
-          .describe(
-            "Custom NPM registry URL (defaults to using system default, likely npmjs.org)",
-          ),
-      }).describe("NPM package as plugin source"),
-      B.object({
-        source: B.literal("pip"),
-        package: B.string().describe(
-          "Python package name as it appears on PyPI",
-        ),
-        version: B.string()
-          .optional()
-          .describe("Version specifier (e.g., ==1.0.0, >=2.0.0, <3.0.0)"),
-        registry: B.string()
-          .url()
-          .optional()
-          .describe(
-            "Custom PyPI registry URL (defaults to using system default, likely pypi.org)",
-          ),
-      }).describe("Python package as plugin source"),
+      b
+        .object({
+          source: b.literal("npm"),
+          package: yz8
+            .or(b.string())
+            .describe(
+              "Package name (or url, or local path, or anything else that can be passed to `npm` as a package)",
+            ),
+          version: b
+            .string()
+            .optional()
+            .describe(
+              "Specific version or version range (e.g., ^1.0.0, ~2.1.0)",
+            ),
+          registry: b
+            .string()
+            .url()
+            .optional()
+            .describe(
+              "Custom NPM registry URL (defaults to using system default, likely npmjs.org)",
+            ),
+        })
+        .describe("NPM package as plugin source"),
+      b
+        .object({
+          source: b.literal("pip"),
+          package: b
+            .string()
+            .describe("Python package name as it appears on PyPI"),
+          version: b
+            .string()
+            .optional()
+            .describe("Version specifier (e.g., ==1.0.0, >=2.0.0, <3.0.0)"),
+          registry: b
+            .string()
+            .url()
+            .optional()
+            .describe(
+              "Custom PyPI registry URL (defaults to using system default, likely pypi.org)",
+            ),
+        })
+        .describe("Python package as plugin source"),
       B.object({
         source: B.literal("url"),
-        url: B.string()
+        url: b
+          .string()
           .endsWith(".git")
           .describe("Full git repository URL (https:// or git@)"),
-        ref: B.string()
+        ref: b
+          .string()
           .optional()
           .describe(
             'Git branch or tag to use (e.g., "main", "v1.0.0"). Defaults to repository default branch.',
@@ -423,7 +504,8 @@
       B.object({
         source: B.literal("github"),
         repo: B.string().describe("GitHub repository in owner/repo format"),
-        ref: B.string()
+        ref: b
+          .string()
           .optional()
           .describe(
             'Git branch or tag to use (e.g., "main", "v1.0.0"). Defaults to repository default branch.',
@@ -431,10 +513,10 @@
         sha: jX8.optional().describe("Specific commit SHA to use"),
       }),
     ])));
-  ((EJK = v61
-    .partial()
+  ((fwK = V61.partial()
     .extend({
-      name: B.string()
+      name: b
+        .string()
         .min(1, "Plugin name cannot be empty")
         .refine((A) => !A.includes(" "), {
           message:
@@ -442,15 +524,18 @@
         })
         .describe("Unique identifier matching the plugin name"),
       source: vJK.describe("Where to fetch the plugin from"),
-      category: B.string()
+      category: b
+        .string()
         .optional()
         .describe(
           'Category for organizing plugins (e.g., "productivity", "development")',
         ),
-      tags: B.array(B.string())
+      tags: b
+        .array(b.string())
         .optional()
         .describe("Tags for searchability and discovery"),
-      strict: B.boolean()
+      strict: b
+        .boolean()
         .optional()
         .default(!0)
         .describe(
@@ -459,7 +544,8 @@
     })
     .strict()),
     (Ww1 = B.object({
-      name: B.string()
+      name: b
+        .string()
         .min(1, "Marketplace must have a name")
         .refine((A) => !A.includes(" "), {
           message:
@@ -470,34 +556,44 @@
             'Marketplace name cannot impersonate official Anthropic/Claude marketplaces. Names containing "official", "anthropic", or "claude" in official-sounding combinations are reserved.',
         }),
       owner: WX8.describe("Marketplace maintainer or curator information"),
-      plugins: B.array(EJK).describe(
-        "Collection of available plugins in this marketplace",
-      ),
-      metadata: B.object({
-        pluginRoot: B.string()
-          .optional()
-          .describe("Base path for relative plugin sources"),
-        version: B.string().optional().describe("Marketplace version"),
-        description: B.string().optional().describe("Marketplace description"),
-      })
+      plugins: b
+        .array(fwK)
+        .describe("Collection of available plugins in this marketplace"),
+      metadata: b
+        .object({
+          pluginRoot: b
+            .string()
+            .optional()
+            .describe("Base path for relative plugin sources"),
+          version: b.string().optional().describe("Marketplace version"),
+          description: b
+            .string()
+            .optional()
+            .describe("Marketplace description"),
+        })
         .optional()
         .describe("Optional marketplace metadata"),
     })),
-    (T61 = B.string().regex(
-      /^[a-z0-9][-a-z0-9._]*@[a-z0-9][-a-z0-9._]*$/i,
-      "Plugin ID must be in format: plugin@marketplace",
-    )),
+    (f61 = b
+      .string()
+      .regex(
+        /^[a-z0-9][-a-z0-9._]*@[a-z0-9][-a-z0-9._]*$/i,
+        "Plugin ID must be in format: plugin@marketplace",
+      )),
     (Jiz = B.union([
       T61,
       B.object({
         id: T61.describe('Plugin identifier (e.g., "formatter@tools")'),
-        version: B.string()
+        version: b
+          .string()
           .optional()
           .describe('Version constraint (e.g., "^2.0.0")'),
-        required: B.boolean()
+        required: b
+          .boolean()
           .optional()
           .describe("If true, cannot be disabled"),
-        config: B.record(B.string(), B.unknown())
+        config: b
+          .record(b.string(), b.unknown())
           .optional()
           .describe("Plugin-specific configuration"),
       }),
@@ -505,13 +601,15 @@
     (kJK = B.object({
       version: B.string().describe("Currently installed version"),
       installedAt: B.string().describe("ISO 8601 timestamp of installation"),
-      lastUpdated: B.string()
+      lastUpdated: b
+        .string()
         .optional()
         .describe("ISO 8601 timestamp of last update"),
-      installPath: B.string().describe(
-        "Absolute path to the installed plugin directory",
-      ),
-      gitCommitSha: B.string()
+      installPath: b
+        .string()
+        .describe("Absolute path to the installed plugin directory"),
+      gitCommitSha: b
+        .string()
         .optional()
         .describe(
           "Git commit SHA for git-based plugins (for version tracking)",
@@ -519,46 +617,51 @@
     })),
     (IT1 = B.object({
       version: B.literal(1).describe("Schema version 1"),
-      plugins: B.record(T61, kJK).describe(
-        "Map of plugin IDs to their installation metadata",
-      ),
+      plugins: b
+        .record(f61, VwK)
+        .describe("Map of plugin IDs to their installation metadata"),
     })),
     (LJK = B.enum(["managed", "user", "project", "local"])),
     (RJK = B.object({
       scope: LJK.describe("Installation scope"),
-      projectPath: B.string()
+      projectPath: b
+        .string()
         .optional()
         .describe("Project path (required for project/local scopes)"),
-      installPath: B.string().describe(
-        "Absolute path to the versioned plugin directory",
-      ),
+      installPath: b
+        .string()
+        .describe("Absolute path to the versioned plugin directory"),
       version: B.string().optional().describe("Currently installed version"),
-      installedAt: B.string()
+      installedAt: b
+        .string()
         .optional()
         .describe("ISO 8601 timestamp of installation"),
-      lastUpdated: B.string()
+      lastUpdated: b
+        .string()
         .optional()
         .describe("ISO 8601 timestamp of last update"),
-      gitCommitSha: B.string()
+      gitCommitSha: b
+        .string()
         .optional()
         .describe("Git commit SHA for git-based plugins"),
     })),
     (xT1 = B.object({
       version: B.literal(2).describe("Schema version 2"),
-      plugins: B.record(T61, B.array(RJK)).describe(
-        "Map of plugin IDs to arrays of installation entries",
-      ),
+      plugins: b
+        .record(f61, b.array(TwK))
+        .describe("Map of plugin IDs to arrays of installation entries"),
     })),
     (Xiz = B.union([IT1, xT1])),
     (yJK = B.object({
       source: hT1.describe("Where to fetch the marketplace from"),
-      installLocation: B.string().describe(
-        "Local cache path where marketplace manifest is stored",
-      ),
-      lastUpdated: B.string().describe(
-        "ISO 8601 timestamp of last marketplace refresh",
-      ),
-      autoUpdate: B.boolean()
+      installLocation: b
+        .string()
+        .describe("Local cache path where marketplace manifest is stored"),
+      lastUpdated: b
+        .string()
+        .describe("ISO 8601 timestamp of last marketplace refresh"),
+      autoUpdate: b
+        .boolean()
         .optional()
         .describe(
           "Whether to automatically update this marketplace and its installed plugins on startup",

@@@ function 'YG6' (was 'tyA') — structural (97.0%)
--- pretty-v2.1.32.js:442971
+++ pretty-v2.1.33.js:427694
@@ -34,7 +34,7 @@
     g = U.skillFrontmatter.reduce((v1, U1) => v1 + U1.tokens, 0),
     x = m.totalTokens,
     p = Md(),
-    n = p ? A51() - FLA : void 0,
+    r = p ? n31(q) - uLA : void 0,
     r = [];
   if (j > 0)
     r.push({ name: "System prompt", tokens: j, color: "promptBorder" });

@@@ function 'HJ' (was 'j_') — structural (96.6%)
--- pretty-v2.1.32.js:515759
+++ pretty-v2.1.33.js:515876
@@ -82,6 +82,8 @@
     }
   }),
     kc7(H));
-  let O = gqz(CQ1(H));
+  let $ = LQ1(H),
+    O = _5z($),
+    _ = kQ1(O);
   return pqz(O);
 }

@@@ variable 'IS4' (was 'SE4') — structural (95.1%)
--- pretty-v2.1.32.js:357031
+++ pretty-v2.1.33.js:374290
@@ -17,9 +17,9 @@
       schema: B.record(B.string(), B.unknown()),
     })),
     (s_Y = B.enum(["user", "project", "org", "temporary"])),
-    (jIw = B.enum(["local", "user", "project"]).describe(
-      "Config scope for settings.",
-    )),
+    (gpw = b
+      .enum(["local", "user", "project"])
+      .describe("Config scope for settings.")),
     (MIw = B.literal("context-1m-2025-08-07")),
     (t_Y = B.object({
       type: B.literal("stdio").optional(),
@@ -45,52 +45,60 @@
       id: B.string(),
     })),
     (YJY = B.union([LE4, KJY])),
-    (WIw = B.object({
-      name: B.string().describe("Server name as configured"),
-      status: B.enum([
-        "connected",
-        "failed",
-        "needs-auth",
-        "pending",
-        "disabled",
-      ]).describe("Current connection status"),
-      serverInfo: B.object({ name: B.string(), version: B.string() })
-        .optional()
-        .describe("Server information (available when connected)"),
-      error: B.string()
-        .optional()
-        .describe("Error message (available when status is 'failed')"),
-      config: YJY.optional().describe(
-        "Server configuration (includes URL for HTTP/SSE servers)",
-      ),
-      scope: B.string()
-        .optional()
-        .describe(
-          "Configuration scope (e.g., project, user, local, claudeai, managed)",
+    (dpw = b
+      .object({
+        name: b.string().describe("Server name as configured"),
+        status: b
+          .enum(["connected", "failed", "needs-auth", "pending", "disabled"])
+          .describe("Current connection status"),
+        serverInfo: b
+          .object({ name: b.string(), version: b.string() })
+          .optional()
+          .describe("Server information (available when connected)"),
+        error: b
+          .string()
+          .optional()
+          .describe("Error message (available when status is 'failed')"),
+        config: CjY.optional().describe(
+          "Server configuration (includes URL for HTTP/SSE servers)",
         ),
-      tools: B.array(
-        B.object({
-          name: B.string(),
-          description: B.string().optional(),
-          annotations: B.object({
-            readOnly: B.boolean().optional(),
-            destructive: B.boolean().optional(),
-            openWorld: B.boolean().optional(),
-          }).optional(),
-        }),
-      )
-        .optional()
-        .describe("Tools provided by this server (available when connected)"),
-    }).describe("Status information for an MCP server connection.")),
-    (GIw = B.object({
-      added: B.array(B.string()).describe("Names of servers that were added"),
-      removed: B.array(B.string()).describe(
-        "Names of servers that were removed",
-      ),
-      errors: B.record(B.string(), B.string()).describe(
-        "Map of server names to error messages for servers that failed to connect",
-      ),
-    }).describe("Result of a setMcpServers operation.")),
+        scope: b
+          .string()
+          .optional()
+          .describe(
+            "Configuration scope (e.g., project, user, local, claudeai, managed)",
+          ),
+        tools: b
+          .array(
+            b.object({
+              name: b.string(),
+              description: b.string().optional(),
+              annotations: b
+                .object({
+                  readOnly: b.boolean().optional(),
+                  destructive: b.boolean().optional(),
+                  openWorld: b.boolean().optional(),
+                })
+                .optional(),
+            }),
+          )
+          .optional()
+          .describe("Tools provided by this server (available when connected)"),
+      })
+      .describe("Status information for an MCP server connection.")),
+    (cpw = b
+      .object({
+        added: b.array(b.string()).describe("Names of servers that were added"),
+        removed: b
+          .array(b.string())
+          .describe("Names of servers that were removed"),
+        errors: b
+          .record(b.string(), b.string())
+          .describe(
+            "Map of server names to error messages for servers that failed to connect",
+          ),
+      })
+      .describe("Result of a setMcpServers operation.")),
     (BM1 = B.enum([
       "userSettings",
       "projectSettings",
@@ -152,16 +160,18 @@
         toolUseID: B.string().optional(),
       }),
     ])),
-    (mM1 = B.enum([
-      "default",
-      "acceptEdits",
-      "bypassPermissions",
-      "plan",
-      "delegate",
-      "dontAsk",
-    ]).describe(
-      "Permission mode for controlling how tool executions are handled. 'default' - Standard behavior, prompts for dangerous operations. 'acceptEdits' - Auto-accept file edit operations. 'bypassPermissions' - Bypass all permission checks (requires allowDangerouslySkipPermissions). 'plan' - Planning mode, no actual tool execution. 'delegate' - Delegate mode, restricts team leader to only Teammate and Task tools. 'dontAsk' - Don't prompt for permissions, deny if not pre-approved.",
-    )),
+    (Ij1 = b
+      .enum([
+        "default",
+        "acceptEdits",
+        "bypassPermissions",
+        "plan",
+        "delegate",
+        "dontAsk",
+      ])
+      .describe(
+        "Permission mode for controlling how tool executions are handled. 'default' - Standard behavior, prompts for dangerous operations. 'acceptEdits' - Auto-accept file edit operations. 'bypassPermissions' - Bypass all permission checks (requires allowDangerouslySkipPermissions). 'plan' - Planning mode, no actual tool execution. 'delegate' - Delegate mode, restricts team leader to only Teammate and Task tools. 'dontAsk' - Don't prompt for permissions, deny if not pre-approved.",
+      )),
     (zJY = [
       "PreToolUse",
       "PostToolUse",
@@ -176,6 +186,8 @@
       "PreCompact",
       "PermissionRequest",
       "Setup",
+      "TeammateIdle",
+      "TaskCompleted",
     ]),
     (ZIw = B.enum(zJY)),
     (Gv = B.object({
@@ -276,6 +288,23 @@
         custom_instructions: B.string().nullable(),
       }),
     )),
+    (djY = ZZ.and(
+      b.object({
+        hook_event_name: b.literal("TeammateIdle"),
+        teammate_name: b.string(),
+        team_name: b.string(),
+      }),
+    )),
+    (cjY = ZZ.and(
+      b.object({
+        hook_event_name: b.literal("TaskCompleted"),
+        task_id: b.string(),
+        task_subject: b.string(),
+        task_description: b.string().optional(),
+        teammate_name: b.string().optional(),
+        team_name: b.string().optional(),
+      }),
+    )),
     (PJY = [
       "clear",
       "logout",
@@ -301,6 +330,8 @@
       GJY,
       HJY,
       DJY,
+      djY,
+      cjY,
     ])),
     (VJY = B.object({
       async: B.literal(!0),
@@ -364,96 +395,110 @@
       decision: B.enum(["approve", "block"]).optional(),
       systemMessage: B.string().optional(),
       reason: B.string().optional(),
-      hookSpecificOutput: B.union([
-        NJY,
-        TJY,
-        vJY,
-        EJY,
-        kJY,
-        LJY,
-        RJY,
-        yJY,
-        CJY,
-      ]).optional(),
+      hookSpecificOutput: b
+        .union([ojY, ajY, sjY, tjY, ejY, AWY, qWY, KWY, YWY])
+        .optional(),
     })),
     (VIw = B.union([VJY, SJY])),
-    (NIw = B.object({
-      name: B.string().describe("Skill name (without the leading slash)"),
-      description: B.string().describe("Description of what the skill does"),
-      argumentHint: B.string().describe(
-        'Hint for skill arguments (e.g., "<file>")',
-      ),
-    }).describe(
-      "Information about an available skill (invoked via /command syntax).",
-    )),
-    (TIw = B.object({
-      value: B.string().describe("Model identifier to use in API calls"),
-      displayName: B.string().describe("Human-readable display name"),
-      description: B.string().describe(
-        "Description of the model's capabilities",
-      ),
-    }).describe("Information about an available model.")),
-    (vIw = B.object({
-      email: B.string().optional(),
-      organization: B.string().optional(),
-      subscriptionType: B.string().optional(),
-      tokenSource: B.string().optional(),
-      apiKeySource: B.string().optional(),
-    }).describe("Information about the logged in user's account.")),
+    (opw = b
+      .object({
+        name: b.string().describe("Skill name (without the leading slash)"),
+        description: b.string().describe("Description of what the skill does"),
+        argumentHint: b
+          .string()
+          .describe('Hint for skill arguments (e.g., "<file>")'),
+      })
+      .describe(
+        "Information about an available skill (invoked via /command syntax).",
+      )),
+    (apw = b
+      .object({
+        value: b.string().describe("Model identifier to use in API calls"),
+        displayName: b.string().describe("Human-readable display name"),
+        description: b
+          .string()
+          .describe("Description of the model's capabilities"),
+      })
+      .describe("Information about an available model.")),
+    (spw = b
+      .object({
+        email: b.string().optional(),
+        organization: b.string().optional(),
+        subscriptionType: b.string().optional(),
+        tokenSource: b.string().optional(),
+        apiKeySource: b.string().optional(),
+      })
+      .describe("Information about the logged in user's account.")),
     (hJY = B.union([B.string(), B.record(B.string(), LE4)])),
-    (EIw = B.object({
-      description: B.string().describe(
-        "Natural language description of when to use this agent",
-      ),
-      tools: B.array(B.string())
-        .optional()
-        .describe(
-          "Array of allowed tool names. If omitted, inherits all tools from parent",
-        ),
-      disallowedTools: B.array(B.string())
-        .optional()
-        .describe("Array of tool names to explicitly disallow for this agent"),
-      prompt: B.string().describe("The agent's system prompt"),
-      model: B.enum(["sonnet", "opus", "haiku", "inherit"])
-        .optional()
-        .describe(
-          "Model to use for this agent. If omitted or 'inherit', uses the main model",
-        ),
-      mcpServers: B.array(hJY).optional(),
-      criticalSystemReminder_EXPERIMENTAL: B.string()
-        .optional()
-        .describe("Experimental: Critical reminder added to system prompt"),
-      skills: B.array(B.string())
-        .optional()
-        .describe("Array of skill names to preload into the agent context"),
-      maxTurns: B.number()
-        .int()
-        .positive()
-        .optional()
-        .describe(
-          "Maximum number of agentic turns (API round-trips) before stopping",
-        ),
-    }).describe(
-      "Definition for a custom subagent that can be invoked via the Task tool.",
-    )),
-    (kIw = B.enum(["user", "project", "local"]).describe(
-      "Source for loading filesystem-based settings. 'user' - Global user settings (~/.claude/settings.json). 'project' - Project settings (.claude/settings.json). 'local' - Local settings (.claude/settings.local.json).",
-    )),
-    (LIw = B.object({
-      type: B.literal("local").describe(
-        "Plugin type. Currently only 'local' is supported",
-      ),
-      path: B.string().describe(
-        "Absolute or relative path to the plugin directory",
-      ),
-    }).describe("Configuration for loading a plugin.")),
-    (RIw = B.object({
-      canRewind: B.boolean(),
-      error: B.string().optional(),
-      filesChanged: B.array(B.string()).optional(),
-      insertions: B.number().optional(),
-      deletions: B.number().optional(),
-    }).describe("Result of a rewindFiles operation.")),
+    (tpw = b
+      .object({
+        description: b
+          .string()
+          .describe("Natural language description of when to use this agent"),
+        tools: b
+          .array(b.string())
+          .optional()
+          .describe(
+            "Array of allowed tool names. If omitted, inherits all tools from parent",
+          ),
+        disallowedTools: b
+          .array(b.string())
+          .optional()
+          .describe(
+            "Array of tool names to explicitly disallow for this agent",
+          ),
+        prompt: b.string().describe("The agent's system prompt"),
+        model: b
+          .enum(["sonnet", "opus", "haiku", "inherit"])
+          .optional()
+          .describe(
+            "Model to use for this agent. If omitted or 'inherit', uses the main model",
+          ),
+        mcpServers: b.array(wWY).optional(),
+        criticalSystemReminder_EXPERIMENTAL: b
+          .string()
+          .optional()
+          .describe("Experimental: Critical reminder added to system prompt"),
+        skills: b
+          .array(b.string())
+          .optional()
+          .describe("Array of skill names to preload into the agent context"),
+        maxTurns: b
+          .number()
+          .int()
+          .positive()
+          .optional()
+          .describe(
+            "Maximum number of agentic turns (API round-trips) before stopping",
+          ),
+      })
+      .describe(
+        "Definition for a custom subagent that can be invoked via the Task tool.",
+      )),
+    (epw = b
+      .enum(["user", "project", "local"])
+      .describe(
+        "Source for loading filesystem-based settings. 'user' - Global user settings (~/.claude/settings.json). 'project' - Project settings (.claude/settings.json). 'local' - Local settings (.claude/settings.local.json).",
+      )),
+    (Adw = b
+      .object({
+        type: b
+          .literal("local")
+          .describe("Plugin type. Currently only 'local' is supported"),
+        path: b
+          .string()
+          .describe("Absolute or relative path to the plugin directory"),
+      })
+      .describe("Configuration for loading a plugin.")),
+    (qdw = b
+      .object({
+        canRewind: b.boolean(),
+        error: b.string().optional(),
+        filesChanged: b.array(b.string()).optional(),
+        insertions: b.number().optional(),
+        deletions: b.number().optional(),
+      })
+      .describe("Result of a rewindFiles operation.")),
     (IJY = B.unknown()),
     (xJY = B.unknown()),
     (bJY = B.unknown()),
@@ -489,26 +534,32 @@
       uuid: V0,
       session_id: B.string(),
     })),
-    (yIw = B.object({
-      type: B.literal("streamlined_text"),
-      text: B.string().describe(
-        "Text content preserved from the assistant message",
-      ),
-      session_id: B.string(),
-      uuid: V0,
-    }).describe(
-      "@internal Streamlined text message - replaces SDKAssistantMessage in streamlined output. Text content preserved, thinking and tool_use blocks removed.",
-    )),
-    (CIw = B.object({
-      type: B.literal("streamlined_tool_use_summary"),
-      tool_summary: B.string().describe(
-        'Summary of tool calls (e.g., "Read 2 files, wrote 1 file")',
-      ),
-      session_id: B.string(),
-      uuid: V0,
-    }).describe(
-      "@internal Streamlined tool use summary - replaces tool_use blocks in streamlined output with a cumulative summary string.",
-    )),
+    (Kdw = b
+      .object({
+        type: b.literal("streamlined_text"),
+        text: b
+          .string()
+          .describe("Text content preserved from the assistant message"),
+        session_id: b.string(),
+        uuid: L0,
+      })
+      .describe(
+        "@internal Streamlined text message - replaces SDKAssistantMessage in streamlined output. Text content preserved, thinking and tool_use blocks removed.",
+      )),
+    (Ydw = b
+      .object({
+        type: b.literal("streamlined_tool_use_summary"),
+        tool_summary: b
+          .string()
+          .describe(
+            'Summary of tool calls (e.g., "Read 2 files, wrote 1 file")',
+          ),
+        session_id: b.string(),
+        uuid: L0,
+      })
+      .describe(
+        "@internal Streamlined tool use summary - replaces tool_use blocks in streamlined output with a cumulative summary string.",
+      )),
     (CE4 = B.object({
       tool_name: B.string(),
       tool_use_id: B.string(),

@@@ variable 'dX1' (was 'P01') — structural (94.5%)
--- pretty-v2.1.32.js:253775
+++ pretty-v2.1.33.js:217928
@@ -8,62 +8,75 @@
   eA();
   Jn7();
   ((D$A = B.strictObject({
-    pattern: B.string().describe(
-      "The regular expression pattern to search for in file contents",
-    ),
-    path: B.string()
+    pattern: b
+      .string()
+      .describe(
+        "The regular expression pattern to search for in file contents",
+      ),
+    path: b
+      .string()
       .optional()
       .describe(
         "File or directory to search in (rg PATH). Defaults to current working directory.",
       ),
-    glob: B.string()
+    glob: b
+      .string()
       .optional()
       .describe(
         'Glob pattern to filter files (e.g. "*.js", "*.{ts,tsx}") - maps to rg --glob',
       ),
-    output_mode: B.enum(["content", "files_with_matches", "count"])
+    output_mode: b
+      .enum(["content", "files_with_matches", "count"])
       .optional()
       .describe(
         'Output mode: "content" shows matching lines (supports -A/-B/-C context, -n line numbers, head_limit), "files_with_matches" shows file paths (supports head_limit), "count" shows match counts (supports head_limit). Defaults to "files_with_matches".',
       ),
-    "-B": B.number()
+    "-B": b
+      .number()
       .optional()
       .describe(
         'Number of lines to show before each match (rg -B). Requires output_mode: "content", ignored otherwise.',
       ),
-    "-A": B.number()
+    "-A": b
+      .number()
       .optional()
       .describe(
         'Number of lines to show after each match (rg -A). Requires output_mode: "content", ignored otherwise.',
       ),
     "-C": B.number().optional().describe("Alias for context."),
-    context: B.number()
+    context: b
+      .number()
       .optional()
       .describe(
         'Number of lines to show before and after each match (rg -C). Requires output_mode: "content", ignored otherwise.',
       ),
-    "-n": B.boolean()
+    "-n": b
+      .boolean()
       .optional()
       .describe(
         'Show line numbers in output (rg -n). Requires output_mode: "content", ignored otherwise. Defaults to true.',
       ),
     "-i": B.boolean().optional().describe("Case insensitive search (rg -i)"),
-    type: B.string()
+    type: b
+      .string()
       .optional()
       .describe(
         "File type to search (rg --type). Common types: js, py, rust, go, java, etc. More efficient than include for standard file types.",
       ),
-    head_limit: B.number()
+    head_limit: b
+      .number()
       .optional()
       .describe(
         'Limit output to first N lines/entries, equivalent to "| head -N". Works across all output modes: content (limits output lines), files_with_matches (limits file paths), count (limits count entries). Defaults to 0 (unlimited).',
       ),
-    offset: B.number()
+    offset: b
+      .number()
       .optional()
       .describe(
         'Skip first N lines/entries before applying head_limit, equivalent to "| tail -n +N | head -N". Works across all output modes. Defaults to 0.',
       ),
-    multiline: B.boolean()
+    multiline: b
+      .boolean()
       .optional()
       .describe(
         "Enable multiline mode where . matches newlines and patterns can span lines (rg -U --multiline-dotall). Default: false.",

@@@ function 'fAA' (was 'a7A') — structural (94.1%)
--- pretty-v2.1.32.js:168439
+++ pretty-v2.1.33.js:130918
@@ -47,6 +47,8 @@
       }
     }
   } catch {}
+  let X = new Set([...(A.permissions?.additionalDirectories || []), ...hy()]);
+  z.push(...X);
   for (let D of Pf) {
     let j = f7(D);
     if (!j?.permissions) continue;

@@@ variable 'MBA' (was 'UuA') — structural (94.0%)
--- pretty-v2.1.32.js:520554
+++ pretty-v2.1.33.js:521283
@@ -155,12 +155,10 @@
         return j;
       }
       function O(j) {
-        return j
-          .join(
-            `
+        return M.join(
+          `
 `,
-          )
-          .replace(/^/gm, " ".repeat(2));
+        ).replace(/^/gm, " ".repeat(2));
       }
       let $ = [`Usage: ${q.commandUsage(A)}`, ""],
         _ = q.commandDescription(A);

@@@ variable 'i2' (was 'jH') — structural (92.8%)
--- pretty-v2.1.32.js:168681
+++ pretty-v2.1.33.js:131162
@@ -10,7 +10,6 @@
   er1();
   oH();
   Px();
-  az();
   ((t7A = qA(() => {
     let { rgPath: A, rgArgs: q } = B21();
     return T$.checkDependencies({ command: A, args: q });

@@@ function 'emA' (was 'RmA') — structural (92.7%)
--- pretty-v2.1.32.js:546236
+++ pretty-v2.1.33.js:545402
@@ -18,7 +18,7 @@
   if (q[0] !== D || q[1] !== X || q[2] !== J)
     ((j = () => {
       (c("tengu_toggle_todos", {
-        is_expanded: X,
+        is_expanded: X === "tasks",
         has_todos: J && J.length > 0,
       }),
         D(FHz));

@@@ function 'hHz' (was 'Ywz') — structural (92.5%)
--- pretty-v2.1.32.js:540088
+++ pretty-v2.1.33.js:538506
@@ -18,7 +18,7 @@
     W = T6(Xwz),
     G = T6(Jwz),
     P = T6(_wz),
-    V = T6($wz),
+    V = P === "teammates",
     Z = T6(Owz),
     T =
       cN6.useSyncExternalStore(
@@ -26,6 +26,7 @@
         LXq?.getNextTickAt ?? RXq,
         RXq,
       ) !== null,
+    k = !1,
     k;
   if (q[0] === Symbol.for("react.memo_cache_sentinel")) ((k = !1), (q[0] = k));
   else k = q[0];
@@ -117,6 +118,7 @@
               { color: jW(z1), key: "mode" },
               CT1(z1),
               " ",
+              !1,
               gF(z1).toLowerCase(),
               " on",
               q1 &&
@@ -133,7 +135,7 @@
             ),
           ]
         : []),
-      ...(t && !j1
+      ...(t && !H1 && !Ve(D, V)
         ? [
             m7.createElement(XmA, {
               key: "tasks",
@@ -203,7 +205,8 @@
           ]
         : []),
     ],
-    o = z ? Wwz(w, b, U, m, P) : [];
+    O1 = Object.values(D).some(xHz),
+    X1 = z ? dHz(w, g, U, x, P, O1) : [];
   if (D1)
     J1.push(
       m7.createElement(

@@@ function 'MV6' (was 'KV6') — structural (92.1%)
--- pretty-v2.1.32.js:495865
+++ pretty-v2.1.33.js:495971
@@ -13,6 +13,8 @@
       PreCompact: {},
       PermissionRequest: {},
       Setup: {},
+      TeammateIdle: {},
+      TaskCompleted: {},
     },
     Y = Wp1(q);
   It4(A).forEach((w) => {

@@@ variable 'z$' (was 'JO') — structural (91.6%)
--- pretty-v2.1.32.js:358266
+++ pretty-v2.1.33.js:375573
@@ -8,6 +8,7 @@
   uO();
   SE4();
   I6();
+  I6();
   Vm1 = a(Wx(), 1);
   ((xE4 = B.object({
     type: B.literal("plan_approval_request"),

@@@ function '_Z6' (was 'YZ6') — structural (91.5%)
--- pretty-v2.1.32.js:452984
+++ pretty-v2.1.33.js:453091
@@ -32,9 +32,22 @@
         ? w.highlights.filter(
             (S) => w.cursorOffset < S.start || w.cursorOffset >= S.end,
           )
-        : w.highlights,
-    P = G && G.length > 0,
-    V = I,
+        : w.highlights;
+  if (G && G.length > 0)
+    return Dm.default.createElement(
+      I,
+      null,
+      Dm.default.createElement(oe4, { text: $, highlights: G }),
+      W &&
+        Dm.default.createElement(
+          f,
+          { dimColor: !0 },
+          w.value?.endsWith(" ") ? "" : " ",
+          w.argumentHint,
+        ),
+      Y,
+    );
+  let V = I,
     Z = f,
     N = "truncate-end",
     T =
@@ -42,9 +55,7 @@
         ? w.placeholderElement
         : D && j
           ? Et.default.createElement(R3, null, j)
-          : P
-            ? Et.default.createElement(Ye4, { text: O, highlights: G })
-            : Et.default.createElement(R3, null, O),
+          : Dm.default.createElement(U3, null, $),
     k =
       W &&
       Et.default.createElement(

@@@ function 'T2z' (was 'nYz') — structural (91.5%)
--- pretty-v2.1.32.js:530566
+++ pretty-v2.1.33.js:528967
@@ -40,7 +40,8 @@
     [U, g] = C_.useState(!1),
     [x, p] = C_.useState(!1),
     n = C_.useRef(!1),
-    z1 = tK1("requesting", "Attempting to auto-approve…", !0, !1),
+    c = "Attempting to auto-approve…",
+    [Y1, f1] = Dm1("requesting", c, !0, !1),
     f1 = p8.isSandboxingEnabled(),
     Z1 = f1 && sM1(A.input),
     H1 = C_.useMemo(
@@ -90,7 +91,7 @@
     let j1 = s?.trim(),
       J1 = !!j1;
     if (!J1)
-      (c("tengu_permission_request_escape", {}),
+      (l("tengu_permission_request_escape", { explainer_visible: X.visible }),
         J((o) => ({
           ...o,
           attribution: {
@@ -105,6 +106,7 @@
   function E1(s) {
     c("tengu_permission_request_option_selected", {
       option_index: { yes: 1, "yes-apply-suggestions": 2, no: 3 }[s],
+      explainer_visible: X.visible,
     });
     let J1 = oq(A.tool.name);
     switch (s) {

@@@ variable 'm$' (was 'W_') — structural (91.5%)
--- pretty-v2.1.32.js:511404
+++ pretty-v2.1.33.js:511431
@@ -95,6 +95,7 @@
   p2q();
   d2q();
   EO();
+  P$();
   ((ibA = qA(() => [
     Ge4,
     yYq,
@@ -212,5 +213,24 @@
           []
         );
       }
-    })));
+    })),
+    (PuA = new Set([
+      pxA,
+      jp1,
+      JhA,
+      rhA,
+      sxA,
+      DhA,
+      txA,
+      uhA,
+      axA,
+      MhA,
+      bSA,
+      USA,
+      YbA,
+      ahA,
+      rbA,
+      QbA,
+      jxA,
+    ])));
 });

@@@ function 'Dh4' (was 'Rx4') — structural (91.4%)
--- pretty-v2.1.32.js:388982
+++ pretty-v2.1.33.js:377794
@@ -105,7 +105,7 @@
       if (q[24] !== g || q[25] !== x || q[26] !== U)
         ((p = Y2.default.createElement(
           f,
-          { key: "mem-read", color: "remember" },
+          { key: "mem-read" },
           U,
           " ",
           g,
@@ -138,11 +138,7 @@
       let g = `${U} memories`,
         x;
       if (q[29] !== g)
-        ((x = Y2.default.createElement(
-          f,
-          { key: "mem-search", color: "remember" },
-          g,
-        )),
+        ((B = oz.default.createElement(f, { key: "mem-search" }, U)),
           (q[29] = g),
           (q[30] = x));
       else x = q[30];
@@ -175,7 +171,7 @@
       if (q[34] !== g || q[35] !== x || q[36] !== U)
         ((p = Y2.default.createElement(
           f,
-          { key: "mem-write", color: "remember" },
+          { key: "mem-write" },
           U,
           " ",
           g,

@@@ variable 'okA' (was 'lkA') — structural (91.4%)
--- pretty-v2.1.32.js:416738
+++ pretty-v2.1.33.js:414714
@@ -11,10 +11,12 @@
   I6();
   ((IkY = B.strictObject({
     query: B.string().min(2).describe("The search query to use"),
-    allowed_domains: B.array(B.string())
+    allowed_domains: b
+      .array(b.string())
       .optional()
       .describe("Only include search results from these domains"),
-    blocked_domains: B.array(B.string())
+    blocked_domains: b
+      .array(b.string())
       .optional()
       .describe("Never include search results from these domains"),
   })),
@@ -28,12 +30,12 @@
     })),
     (ukY = B.object({
       query: B.string().describe("The search query that was executed"),
-      results: B.array(B.union([bkY, B.string()])).describe(
-        "Search results and/or text commentary from the model",
-      ),
-      durationSeconds: B.number().describe(
-        "Time taken to complete the search operation",
-      ),
+      results: b
+        .array(b.union([gLY, b.string()]))
+        .describe("Search results and/or text commentary from the model"),
+      durationSeconds: b
+        .number()
+        .describe("Time taken to complete the search operation"),
     })));
   JW6 = {
     name: bT,

@@@ class 'DWA' (was 'B6A') — structural (91.3%)
--- pretty-v2.1.32.js:148818
+++ pretty-v2.1.33.js:310042
@@ -271,6 +271,7 @@
             user_attributes: Y.user_attributes,
             experiment_metadata: Y.experiment_metadata,
             device_id: Y.device_id,
+            session_id: Y.session_id,
           }),
         });
         continue;

@@@ function 'PyA' (was 'GyA') — structural (91.2%)
--- pretty-v2.1.32.js:434957
+++ pretty-v2.1.33.js:432741
@@ -13,6 +13,7 @@
           K.startsWith("invalid api key") ||
           K.startsWith("image was too large"),
       ],
+      ["prefixed_label", () => /^\w+:\s/.test(A)],
       [
         "too_few_words",
         () => {

@@@ function 'bKz' (was 'J4z') — structural (91.0%)
--- pretty-v2.1.32.js:510879
+++ pretty-v2.1.33.js:510907
@@ -18,9 +18,10 @@
         }
       return !1;
     },
-    H = K.filter((T) => !Y(T) && !z(T))
-      .map((T) => ({ log: T, meta: lbA(T) }))
-      .sort((T, k) => k.meta.start_time.localeCompare(T.meta.start_time)),
+    w = K.filter((T) => !Y(T) && !z(T) && GKz(T)),
+    H = PKz(w.map((T) => ({ log: T, meta: juA(T) }))).sort((T, k) =>
+      k.meta.start_time.localeCompare(T.meta.start_time),
+    ),
     O = (T) => {
       if (T.user_message_count < 2) return !1;
       if (T.duration_minutes < 1) return !1;

@@@ function 'Aqz' (was 'x8z') — structural (89.9%)
--- pretty-v2.1.32.js:506369
+++ pretty-v2.1.33.js:506375
@@ -73,12 +73,12 @@
     ((N = function (S) {
       if (S === "upgrade")
         (c("tengu_rate_limit_options_menu_select_upgrade", {}),
-          Tp1.call(K, Y).then((m) => {
+          lbA(K, Y).then((m) => {
             if (m) w(m);
           }));
       else if (S === "extra-usage")
         (c("tengu_rate_limit_options_menu_select_extra_usage", {}),
-          pp.call(K, Y).then((m) => {
+          RNA(K, Y).then((m) => {
             if (m) w(m);
           }));
       else if (S === "cancel") Z();

@@@ function '$4q' (was 'w7q') — structural (89.6%)
--- pretty-v2.1.32.js:473766
+++ pretty-v2.1.33.js:473826
@@ -129,8 +129,7 @@
                 if (o !== _1) return _1 - o;
                 return j1.entry.name.localeCompare(J1.entry.name);
               });
-            else
-              q1.sort((j1, J1) => j1.entry.name.localeCompare(J1.entry.name));
+            else e.sort((_1, H1) => _1.entry.name.localeCompare(H1.entry.name));
           } catch (s) {
             (h(
               `Failed to fetch install counts: ${s instanceof Error ? s.message : String(s)}`,

@@@ function 'GyA' (was 'WyA') — structural (89.6%)
--- pretty-v2.1.32.js:434930
+++ pretty-v2.1.33.js:432714
@@ -1,6 +1,6 @@
 async function WyA(A, q, K, Y) {
   let z = Y ?? Ht(A),
-    w = bbY[K],
+    w = K === "coordinator" ? BuY(A.messages) : muY[K],
     H = async () => ({
       behavior: "deny",
       message: "No tools needed for suggestion",

@@@ function 'fZY' (was 'JDY') — structural (89.4%)
--- pretty-v2.1.32.js:365871
+++ pretty-v2.1.33.js:386973
@@ -54,7 +54,7 @@
       whenToUse: `In-process teammate: ${q.agentName}`,
       getSystemPrompt: () => G,
       tools: w?.tools
-        ? [...new Set([...w.tools, wB, BV, dS, eq1, AK1, aL])]
+        ? [...new Set([...w.tools, $B, aS, yq1, rS, Cq1, Sq1, cL])]
         : ["*"],
       source: "projectSettings",
       permissionMode: "default",
@@ -80,7 +80,7 @@
         u = [y],
         S = V,
         m = mL(V);
-      if (m > rm1()) {
+      if (m > EF1($.options.mainLoopModel)) {
         h(`[inProcessRunner] ${q.agentId} compacting history (${m} tokens)`);
         let e = {
             ...O,

@@@ function 'b$6' (was 'XO6') — structural (89.3%)
--- pretty-v2.1.32.js:274104
+++ pretty-v2.1.33.js:259115
@@ -17,10 +17,12 @@
     : q.map((Y) => Y.name).join(`
 `);
   if (Fo !== void 0 && K !== Fo) {
-    let Y = Fo.split(
-        `
+    let Y = $a
+        .split(
+          `
 `,
-      ).filter(Boolean).length,
+        )
+        .filter(Boolean).length,
       z = K.split(
         `
 `,

@@@ function 'p$z' (was 'jHz') — structural (89.3%)
--- pretty-v2.1.32.js:543954
+++ pretty-v2.1.33.js:542397
@@ -61,7 +61,7 @@
     V6 = T6((m6) => m6.speculationSessionTimeSavedMs),
     K6 = T6((m6) => m6.viewingAgentTaskId),
     d6 = T6((m6) => m6.viewSelectionMode),
-    AA = T6((m6) => m6.showSpinnerTree),
+    YA = E6((F6) => F6.expandedView) === "teammates",
     r1 = T6((m6) => m6.mainLoopModel),
     H6 = T6((m6) => m6.mainLoopModelForSession),
     j6 = T6((m6) => m6.thinkingEnabled),
@@ -187,28 +187,28 @@
         m6.push({
           start: O1,
           end: O1 + q6.length,
-          style: { type: "solid", color: "warning" },
+          color: "warning",
           priority: 20,
         });
       for (let sA of E4)
         m6.push({
           start: sA.start,
           end: sA.end,
-          style: { type: "solid", color: "warning" },
+          color: "warning",
           priority: 15,
         });
       for (let sA of $4)
         m6.push({
           start: sA.start,
           end: sA.end,
-          style: { type: "solid", color: "suggestion" },
+          color: "suggestion",
           priority: 5,
         });
       for (let sA of uq)
         m6.push({
           start: sA.start,
           end: sA.end,
-          style: { type: "solid", color: sA.themeColor },
+          color: T8.themeColor,
           priority: 5,
         });
       return m6;

@@@ function 'lZ5' (was 'vp5') — structural (89.1%)
--- pretty-v2.1.32.js:186890
+++ pretty-v2.1.33.js:151072
@@ -1,4 +1,5 @@
 function vp5(A, q, K, Y) {
+  if (q.length > 0) j11();
   for (let z of q) {
     let w = z.sequence;
     if (w === bj7) {

@@@ function 'EBY' (was 'NuY') — structural (89.0%)
--- pretty-v2.1.32.js:439231
+++ pretty-v2.1.33.js:437125
@@ -46,7 +46,9 @@
           lw("lsp_diagnostics", async () => ouY(q)),
           lw("unified_tasks", async () => KBY(q, z)),
           lw("async_hook_responses", async () => YBY()),
-          lw("token_usage", async () => Promise.resolve(HBY(z ?? []))),
+          dw("token_usage", async () =>
+            Promise.resolve(_mY(z ?? [], q.options.mainLoopModel)),
+          ),
           lw("budget_usd", async () =>
             Promise.resolve(OBY(q.options.maxBudgetUsd)),
           ),

@@@ variable 'WQ1' (was 'TQ1') — structural (88.8%)
--- pretty-v2.1.32.js:417126
+++ pretty-v2.1.33.js:415104
@@ -11,60 +11,77 @@
   a6();
   ((FkY = B.object({
     tool: B.enum(["Bash"]).describe("The tool this prompt applies to"),
-    prompt: B.string().describe(
-      'Semantic description of the action, e.g. "run tests", "install dependencies"',
-    ),
+    prompt: b
+      .string()
+      .describe(
+        'Semantic description of the action, e.g. "run tests", "install dependencies"',
+      ),
   })),
-    (hU4 = B.strictObject({
-      allowedPrompts: B.array(FkY)
-        .optional()
-        .describe(
-          "Prompt-based permissions needed to implement the plan. These describe categories of actions rather than specific commands.",
-        ),
-      pushToRemote: B.boolean()
-        .optional()
-        .describe("Whether to push the plan to a remote Claude.ai session"),
-      remoteSessionId: B.string()
-        .optional()
-        .describe("The remote session ID if pushed to remote"),
-      remoteSessionUrl: B.string()
-        .optional()
-        .describe("The remote session URL if pushed to remote"),
-      remoteSessionTitle: B.string()
-        .optional()
-        .describe("The remote session title if pushed to remote"),
-    }).passthrough()),
+    (Mg4 = b
+      .strictObject({
+        allowedPrompts: b
+          .array(lLY)
+          .optional()
+          .describe(
+            "Prompt-based permissions needed to implement the plan. These describe categories of actions rather than specific commands.",
+          ),
+        pushToRemote: b
+          .boolean()
+          .optional()
+          .describe("Whether to push the plan to a remote Claude.ai session"),
+        remoteSessionId: b
+          .string()
+          .optional()
+          .describe("The remote session ID if pushed to remote"),
+        remoteSessionUrl: b
+          .string()
+          .optional()
+          .describe("The remote session URL if pushed to remote"),
+        remoteSessionTitle: b
+          .string()
+          .optional()
+          .describe("The remote session title if pushed to remote"),
+      })
+      .passthrough()),
     (g7H = hU4.extend({
-      plan: B.string()
+      plan: b
+        .string()
         .optional()
         .describe(
           "The plan content (injected by normalizeToolInput from disk)",
         ),
     })),
     (QkY = B.object({
-      plan: B.string()
+      plan: b
+        .string()
         .nullable()
         .describe("The plan that was presented to the user"),
       isAgent: B.boolean(),
-      filePath: B.string()
+      filePath: b
+        .string()
         .optional()
         .describe("The file path where the plan was saved"),
-      pushToRemote: B.boolean()
+      pushToRemote: b
+        .boolean()
         .optional()
         .describe("Whether the plan was pushed to a remote session"),
       remoteSessionId: B.string().optional().describe("The remote session ID"),
-      remoteSessionUrl: B.string()
+      remoteSessionUrl: b
+        .string()
         .optional()
         .describe("The remote session URL"),
-      hasTaskTool: B.boolean()
+      hasTaskTool: b
+        .boolean()
         .optional()
         .describe("Whether the Task tool is available in the current context"),
-      awaitingLeaderApproval: B.boolean()
+      awaitingLeaderApproval: b
+        .boolean()
         .optional()
         .describe(
           "When true, the teammate has sent a plan approval request to the team leader",
         ),
-      requestId: B.string()
+      requestId: b
+        .string()
         .optional()
         .describe("Unique identifier for the plan approval request"),
     })),

@@@ variable 'Qj1' (was 'gM1') — structural (88.7%)
--- pretty-v2.1.32.js:358565
+++ pretty-v2.1.33.js:379716
@@ -6,6 +6,7 @@
   JO();
   oz();
   I6();
+  I6();
   ((JXY = a(Wx(), 1)),
     (zxw = B.object({
       id: B.string(),

@@@ variable 'DW6' — structural (88.4%)
--- pretty-v2.1.32.js:417421
+++ pretty-v2.1.33.js:415416
@@ -7,71 +7,89 @@
   yj();
   ((u$ = a($1(), 1)),
     (gkY = B.object({
-      label: B.string().describe(
-        "The display text for this option that the user will see and select. Should be concise (1-5 words) and clearly describe the choice.",
-      ),
-      description: B.string().describe(
-        "Explanation of what this option means or what will happen if chosen. Useful for providing context about trade-offs or implications.",
-      ),
+      label: b
+        .string()
+        .describe(
+          "The display text for this option that the user will see and select. Should be concise (1-5 words) and clearly describe the choice.",
+        ),
+      description: b
+        .string()
+        .describe(
+          "Explanation of what this option means or what will happen if chosen. Useful for providing context about trade-offs or implications.",
+        ),
     })),
     (xU4 = B.object({
-      question: B.string().describe(
-        'The complete question to ask the user. Should be clear, specific, and end with a question mark. Example: "Which library should we use for date formatting?" If multiSelect is true, phrase it accordingly, e.g. "Which features do you want to enable?"',
-      ),
-      header: B.string().describe(
-        `Very short label displayed as a chip/tag (max ${S$7} chars). Examples: "Auth method", "Library", "Approach".`,
-      ),
-      options: B.array(gkY)
+      question: b
+        .string()
+        .describe(
+          'The complete question to ask the user. Should be clear, specific, and end with a question mark. Example: "Which library should we use for date formatting?" If multiSelect is true, phrase it accordingly, e.g. "Which features do you want to enable?"',
+        ),
+      header: b
+        .string()
+        .describe(
+          `Very short label displayed as a chip/tag (max ${Jn8} chars). Examples: "Auth method", "Library", "Approach".`,
+        ),
+      options: b
+        .array(nLY)
         .min(2)
         .max(4)
         .describe(
           "The available choices for this question. Must have 2-4 options. Each option should be a distinct, mutually exclusive choice (unless multiSelect is enabled). There should be no 'Other' option, that will be provided automatically.",
         ),
-      multiSelect: B.boolean()
+      multiSelect: b
+        .boolean()
         .default(!1)
         .describe(
           "Set to true to allow the user to select multiple options instead of just one. Use when choices are not mutually exclusive.",
         ),
     })),
-    (ikA = B.strictObject({
-      questions: B.array(xU4)
-        .min(1)
-        .max(4)
-        .describe("Questions to ask the user (1-4 questions)"),
-      answers: B.record(B.string(), B.string())
-        .optional()
-        .describe("User answers collected by the permission component"),
-      metadata: B.object({
-        source: B.string()
+    (akA = b
+      .strictObject({
+        questions: b
+          .array(Wg4)
+          .min(1)
+          .max(4)
+          .describe("Questions to ask the user (1-4 questions)"),
+        answers: b
+          .record(b.string(), b.string())
+          .optional()
+          .describe("User answers collected by the permission component"),
+        metadata: b
+          .object({
+            source: b
+              .string()
+              .optional()
+              .describe(
+                'Optional identifier for the source of this question (e.g., "remember" for /remember command). Used for analytics tracking.',
+              ),
+          })
           .optional()
           .describe(
-            'Optional identifier for the source of this question (e.g., "remember" for /remember command). Used for analytics tracking.',
+            "Optional metadata for tracking and analytics purposes. Not displayed to user.",
           ),
       })
-        .optional()
-        .describe(
-          "Optional metadata for tracking and analytics purposes. Not displayed to user.",
-        ),
-    }).refine(
-      (A) => {
-        let q = A.questions.map((K) => K.question);
-        if (q.length !== new Set(q).size) return !1;
-        for (let K of A.questions) {
-          let Y = K.options.map((z) => z.label);
+      .refine(
+        (A) => {
+          let q = A.questions.map((K) => K.question);
           if (Y.length !== new Set(Y).size) return !1;
-        }
-        return !0;
-      },
-      {
-        message:
-          "Question texts must be unique, option labels must be unique within each question",
-      },
-    )),
+          for (let K of A.questions) {
+            let Y = K.options.map((z) => z.label);
+            if (Y.length !== new Set(Y).size) return !1;
+          }
+          return !0;
+        },
+        {
+          message:
+            "Question texts must be unique, option labels must be unique within each question",
+        },
+      )),
     (e7H = B.object({
       questions: B.array(xU4).describe("The questions that were asked"),
-      answers: B.record(B.string(), B.string()).describe(
-        "The answers provided by the user (question text -> answer string; multi-select answers are comma-separated)",
-      ),
+      answers: b
+        .record(b.string(), b.string())
+        .describe(
+          "The answers provided by the user (question text -> answer string; multi-select answers are comma-separated)",
+        ),
     })));
   XW6 = {
     name: kw,

@@@ function 'dG1' (was 'AP1') — structural (88.1%)
--- pretty-v2.1.32.js:451967
+++ pretty-v2.1.33.js:452127
@@ -8,8 +8,7 @@
     mainLoopModel: null,
     mainLoopModelForSession: null,
     statusLineText: void 0,
-    showExpandedTodos: !1,
-    showSpinnerTree: M6().showSpinnerTree ?? !1,
+    expandedView: "none",
     showTeammateMessagePreview: !1,
     selectedIPAgentIndex: -1,
     viewSelectionMode: "none",

@@@ class 'R0A' (was 'djA') — structural (88.1%)
--- pretty-v2.1.32.js:298963
+++ pretty-v2.1.33.js:260873
@@ -36,6 +36,7 @@
     return q.handleData.bind(q);
   }
   #V() {
+    if (this.#w.reason === "interrupt") return;
     this.kill();
   }
   #M(A, q) {

@@@ variable 'bv' (was 'xv') — structural (87.9%)
--- pretty-v2.1.32.js:449924
+++ pretty-v2.1.33.js:450064
@@ -117,17 +117,20 @@
     ])));
   ((bP6 = B.strictObject({
     file_path: B.string().describe("The absolute path to the file to read"),
-    offset: B.number()
+    offset: b
+      .number()
       .optional()
       .describe(
         "The line number to start reading from. Only provide if the file is too large to read at once",
       ),
-    limit: B.number()
+    limit: b
+      .number()
       .optional()
       .describe(
         "The number of lines to read. Only provide if the file is too large to read at once.",
       ),
-    pages: B.string()
+    pages: b
+      .string()
       .optional()
       .describe(
         `Page range for PDF files (e.g., "1-5", "3", "10-20"). Only applicable to PDF files. Maximum ${BX1} pages per request.`,
@@ -140,9 +143,9 @@
         file: B.object({
           filePath: B.string().describe("The path to the file that was read"),
           content: B.string().describe("The content of the file"),
-          numLines: B.number().describe(
-            "Number of lines in the returned content",
-          ),
+          numLines: b
+            .number()
+            .describe("Number of lines in the returned content"),
           startLine: B.number().describe("The starting line number"),
           totalLines: B.number().describe("Total number of lines in the file"),
         }),
@@ -153,20 +156,25 @@
           base64: B.string().describe("Base64-encoded image data"),
           type: MgY.describe("The MIME type of the image"),
           originalSize: B.number().describe("Original file size in bytes"),
-          dimensions: B.object({
-            originalWidth: B.number()
-              .optional()
-              .describe("Original image width in pixels"),
-            originalHeight: B.number()
-              .optional()
-              .describe("Original image height in pixels"),
-            displayWidth: B.number()
-              .optional()
-              .describe("Displayed image width in pixels (after resizing)"),
-            displayHeight: B.number()
-              .optional()
-              .describe("Displayed image height in pixels (after resizing)"),
-          })
+          dimensions: b
+            .object({
+              originalWidth: b
+                .number()
+                .optional()
+                .describe("Original image width in pixels"),
+              originalHeight: b
+                .number()
+                .optional()
+                .describe("Original image height in pixels"),
+              displayWidth: b
+                .number()
+                .optional()
+                .describe("Displayed image width in pixels (after resizing)"),
+              displayHeight: b
+                .number()
+                .optional()
+                .describe("Displayed image height in pixels (after resizing)"),
+            })
             .optional()
             .describe("Image dimension info for coordinate mapping"),
         }),
@@ -192,9 +200,9 @@
           filePath: B.string().describe("The path to the PDF file"),
           originalSize: B.number().describe("Original file size in bytes"),
           count: B.number().describe("Number of pages extracted"),
-          outputDir: B.string().describe(
-            "Directory containing extracted page images",
-          ),
+          outputDir: b
+            .string()
+            .describe("Directory containing extracted page images"),
         }),
       }),
     ])),

@@@ function 'vyA' (was 'VyA') — structural (87.6%)
--- pretty-v2.1.32.js:436424
+++ pretty-v2.1.33.js:434263
@@ -30,6 +30,9 @@
       case "SubagentStop":
         H = Y.agent_type;
         break;
+      case "TeammateIdle":
+      case "TaskCompleted":
+        break;
       default:
         break;
     }

@@@ variable 'NxA' (was 'wxA') — structural (87.5%)
--- pretty-v2.1.32.js:484130
+++ pretty-v2.1.33.js:484206
@@ -2,7 +2,6 @@
   Z7();
   Pw();
   J8();
-  FA();
   ((lU1 = ["19.0.0", "19.1.0", "19.1.1", "19.2.0"]),
     (If6 = [
       "react-server-dom-webpack",

@@@ variable 'PR' (was 'Lh') — structural (87.4%)
--- pretty-v2.1.32.js:368382
+++ pretty-v2.1.33.js:355754
@@ -7,91 +7,91 @@
   RD6();
   J8();
   _6();
-  ((Bp = a($1(), 1)),
-    (QD6 = {
-      name: "InProcessTeammateTask",
-      type: "in_process_teammate",
-      async spawn(A, q) {
-        let K = {
-            name: A.name,
-            teamName: A.teamName,
-            prompt: A.prompt,
-            color: A.color,
-            planModeRequired: A.planModeRequired,
-          },
-          Y = await eM1(K, { setAppState: q.setAppState });
-        if (!Y.success || !Y.taskId)
-          throw Error(Y.error || "Failed to spawn in-process teammate");
-        return {
-          taskId: Y.taskId,
-          cleanup: () => {
-            Y.abortController?.abort();
-          },
-        };
-      },
-      async kill(A, q) {
-        LD6(A, q.setAppState);
-      },
-      renderStatus(A) {
-        if (!h$(A)) return null;
-        let {
-            status: q,
-            identity: K,
-            progress: Y,
-            awaitingPlanApproval: z,
-            isIdle: w,
-          } = A,
-          H =
-            q === "running"
-              ? z
-                ? "warning"
-                : "success"
-              : q === "completed"
-                ? "success"
-                : q === "failed"
-                  ? "error"
-                  : q === "killed"
-                    ? "warning"
-                    : "inactive",
-          O = q === "killed" ? "stopped" : q;
-        if (q === "running" && w) O = "idle";
-        else if (q === "running" && z) O = "awaiting approval";
-        let $ = Y ? ` (${Y.toolUseCount} tools, ${Y.tokenCount} tokens)` : "";
-        return Bp.createElement(
+  bp = s(J1(), 1);
+  Wm1 = {
+    name: "InProcessTeammateTask",
+    type: "in_process_teammate",
+    async spawn(A, q) {
+      let K = {
+          name: A.name,
+          teamName: A.teamName,
+          prompt: A.prompt,
+          color: A.color,
+          planModeRequired: A.planModeRequired,
+        },
+        Y = await jj1(K, { setAppState: q.setAppState });
+      if (!Y.success || !Y.taskId)
+        throw Error(Y.error || "Failed to spawn in-process teammate");
+      return {
+        taskId: Y.taskId,
+        cleanup: () => {
+          Y.abortController?.abort();
+        },
+      };
+    },
+    async kill(A, q) {
+      c06(A, q.setAppState);
+    },
+    renderStatus(A) {
+      if (!F$(A)) return null;
+      let {
+          status: q,
+          identity: K,
+          progress: Y,
+          awaitingPlanApproval: z,
+          isIdle: w,
+        } = A,
+        H =
+          q === "running"
+            ? z
+              ? "warning"
+              : "success"
+            : q === "completed"
+              ? "success"
+              : q === "failed"
+                ? "error"
+                : q === "killed"
+                  ? "warning"
+                  : "inactive",
+        $ = q === "killed" ? "stopped" : q;
+      if (q === "running" && w) $ = "idle";
+      else if (q === "running" && z) $ = "awaiting approval";
+      let O = Y ? ` (${Y.toolUseCount} tools, ${Y.tokenCount} tokens)` : "";
+      return bp.createElement(
+        I,
+        null,
+        bp.createElement(
+          f,
+          { color: H },
+          "[",
           I,
+          "] ",
+          K.agentName,
+          "@",
+          K.teamName,
           null,
-          Bp.createElement(
-            f,
-            { color: H },
-            "[",
-            O,
-            "] ",
-            K.agentName,
-            "@",
-            K.teamName,
-            $,
-          ),
-        );
-      },
-      renderOutput(A) {
-        return Bp.createElement(I, null, Bp.createElement(f, null, A));
-      },
-      getProgressMessage(A) {
-        if (!h$(A)) return null;
-        let {
-          progress: q,
-          lastReportedToolCount: K,
-          lastReportedTokenCount: Y,
-          identity: z,
-        } = A;
-        if (!q) return null;
-        let w = q.toolUseCount - K,
-          H = q.tokenCount - Y;
-        if (w === 0 && H === 0) return null;
-        let O = [];
-        if (w > 0) O.push(`${w} new tool${w > 1 ? "s" : ""} used`);
-        if (H > 0) O.push(`${H} new tokens`);
-        return `Teammate ${z.agentName} progress: ${O.join(", ")}. Read ${A.outputFile} for output.`;
-      },
-    }));
+        ),
+      );
+    },
+    renderOutput(A) {
+      return bp.createElement(I, null, bp.createElement(f, null, A));
+    },
+    getProgressMessage(A) {
+      if (!F$(A)) return null;
+      let {
+        progress: q,
+        lastReportedToolCount: K,
+        lastReportedTokenCount: Y,
+        identity: z,
+      } = A;
+      if (!q) return null;
+      let w = q.toolUseCount - K,
+        H = q.tokenCount - Y;
+      if (w === 0 && H === 0) return null;
+      let $ = [];
+      if (w > 0) $.push(`${w} new tool${w > 1 ? "s" : ""} used`);
+      if (H > 0) $.push(`${H} new tokens`);
+      return `Teammate ${z.agentName} progress: ${$.join(", ")}. Read ${A.outputFile} for output.`;
+    },
+  };
 });

@@@ function 'Kkq' (was 'eTq') — structural (87.4%)
--- pretty-v2.1.32.js:565407
+++ pretty-v2.1.33.js:567764
@@ -2,29 +2,35 @@
   if ($6(!1) || process.env.IS_DEMO) return !1;
   let z = M6(),
     w = !1;
-  if (!z.theme || !z.hasCompletedOnboarding)
-    ((w = !0),
-      await Promise.all([o41(), is()]),
-      await new Promise(async (H) => {
-        let { unmount: O } = await O9(
+  if (!z.theme || !z.hasCompletedOnboarding) {
+    w = !0;
+    let [, , { Onboarding: H }] = await Promise.all([
+      Oo(),
+      ms(),
+      Promise.resolve().then(() => (uvq(), bvq)),
+    ]);
+    await new Promise(async ($) => {
+      let { unmount: O } = await s5(
+        x5.default.createElement(
+          n9,
+          { onChangeAppState: xI },
           MK.default.createElement(
             YY,
-            { onChangeAppState: xm },
-            MK.default.createElement(
-              x2,
-              null,
-              MK.default.createElement(yVq, {
-                onDone: async () => {
-                  (tTq(), O(), await o41(), H());
-                },
-              }),
-            ),
+            null,
+            x5.default.createElement(H, {
+              onDone: async () => {
+                (qkq(), O(), await Oo(), $());
+              },
+            }),
           ),
-          Uw(!1),
-        );
-      }));
+        ),
+        mw(!1),
+      );
+    });
+  }
   if (A !== "bypassPermissions" && !$6(process.env.CLAUBBIT)) {
-    let H = Tw(!1);
+    let H = Nw(!1),
+      { TrustDialog: $ } = await Promise.resolve().then(() => (svq(), avq));
     (await new Promise(async ($) => {
       let { unmount: _ } = await O9(
         MK.default.createElement(

@@@ function 'q5q' (was 'nKq') — structural (87.1%)
--- pretty-v2.1.32.js:485414
+++ pretty-v2.1.33.js:485489
@@ -51,7 +51,7 @@
         : r4.createElement(f, { dimColor: !0 }, V, " · ", Z),
       r4.createElement(f, { dimColor: !0 }, X ? `@${X} · ${y}` : y),
       D && r4.createElement(iKq, null),
-      !D && j && r4.createElement(V6q, { variant: j }),
+      !D && M && l4.createElement(DAq, { variant: M, maxWidth: j }),
     ),
   );
 }

@@@ variable 'yD' (was 'kD') — structural (87.1%)
--- pretty-v2.1.32.js:450870
+++ pretty-v2.1.33.js:451022
@@ -70,7 +70,8 @@
     (oP6 = $6(process.env.CLAUDE_CODE_DISABLE_BACKGROUND_TASKS)),
     (Lt4 = B.strictObject({
       command: B.string().describe("The command to execute"),
-      timeout: B.number()
+      timeout: b
+        .number()
         .optional()
         .describe(`Optional timeout in milliseconds (max ${QP6()})`),
       description: B.string().optional()
@@ -85,20 +86,20 @@
 - find . -name "*.tmp" -exec rm {} \\; → "Find and delete all .tmp files recursively"
 - git reset --hard origin/main → "Discard all local changes and match remote main"
 - curl -s url | jq '.data[]' → "Fetch JSON from URL and extract data array elements"`),
-      run_in_background: B.boolean()
+      run_in_background: b
+        .boolean()
         .optional()
         .describe(
           "Set to true to run this command in the background. Use TaskOutput to read the output later.",
         ),
-      dangerouslyDisableSandbox: B.boolean()
+      dangerouslyDisableSandbox: b
+        .boolean()
         .optional()
         .describe(
           "Set this to true to dangerously override sandbox mode and run commands without sandboxing.",
         ),
-      _simulatedSedEdit: B.object({
-        filePath: B.string(),
-        newContent: B.string(),
-      })
+      _simulatedSedEdit: b
+        .object({ filePath: b.string(), newContent: b.string() })
         .optional()
         .describe("Internal: pre-computed sed edit result from preview"),
     })),
@@ -130,32 +131,39 @@
   bgY = B.object({
     stdout: B.string().describe("The standard output of the command"),
     stderr: B.string().describe("The standard error output of the command"),
-    rawOutputPath: B.string()
+    rawOutputPath: b
+      .string()
       .optional()
       .describe("Path to raw output file for large MCP tool outputs"),
     interrupted: B.boolean().describe("Whether the command was interrupted"),
-    isImage: B.boolean()
+    isImage: b
+      .boolean()
       .optional()
       .describe("Flag to indicate if stdout contains image data"),
-    backgroundTaskId: B.string()
+    backgroundTaskId: b
+      .string()
       .optional()
       .describe(
         "ID of the background task if command is running in background",
       ),
-    backgroundedByUser: B.boolean()
+    backgroundedByUser: b
+      .boolean()
       .optional()
       .describe(
         "True if the user manually backgrounded the command with Ctrl+B",
       ),
-    dangerouslyDisableSandbox: B.boolean()
+    dangerouslyDisableSandbox: b
+      .boolean()
       .optional()
       .describe("Flag to indicate if sandbox mode was overridden"),
-    returnCodeInterpretation: B.string()
+    returnCodeInterpretation: b
+      .string()
       .optional()
       .describe(
         "Semantic interpretation for non-error exit codes with special meaning",
       ),
-    structuredContent: B.array(B.any())
+    structuredContent: b
+      .array(b.any())
       .optional()
       .describe("Structured content blocks from mcp-cli commands"),
   });

@@@ variable 'ph1' (was 's_1') — structural (86.9%)
--- pretty-v2.1.32.js:187324
+++ pretty-v2.1.33.js:204381
@@ -49,11 +49,11 @@
   );
   d3(
     "PRERELEASEIDENTIFIER",
-    `(?:${R4[y4.NONNUMERICIDENTIFIER]}|${R4[y4.NUMERICIDENTIFIER]})`,
+    `(?:${R4[y4.NUMERICIDENTIFIER]}|${R4[y4.NONNUMERICIDENTIFIER]})`,
   );
   d3(
     "PRERELEASEIDENTIFIERLOOSE",
-    `(?:${R4[y4.NONNUMERICIDENTIFIER]}|${R4[y4.NUMERICIDENTIFIERLOOSE]})`,
+    `(?:${R4[y4.NUMERICIDENTIFIERLOOSE]}|${R4[y4.NONNUMERICIDENTIFIER]})`,
   );
   d3(
     "PRERELEASE",

@@@ function 'eB' (was 'Dd') — structural (86.5%)
--- pretty-v2.1.32.js:425586
+++ pretty-v2.1.33.js:422834
@@ -31,8 +31,9 @@
     if ($ - _ > z) (J.add(M), (_ += H.get(M) || 0));
   }
   if (!Y) {
-    let M = RV(A);
-    if (!jd(M).isAboveWarningThreshold || _ < OyY) (J.clear(), (_ = 0));
+    let j = DZ(A),
+      W = K?.options.mainLoopModel ?? J5();
+    if (!Md(j, W).isAboveWarningThreshold || _ < KCY) (J.clear(), (_ = 0));
   }
   let X = (M) => {
       return GG1.has(M) || J.has(M);

@@@ function 'IE4' (was '_R4') — structural (86.4%)
--- pretty-v2.1.32.js:368861
+++ pretty-v2.1.33.js:356233
@@ -21,8 +21,9 @@
     P = FD().prefersReducedMotion ?? !1,
     V = T6((A8) => A8.tasks),
     Z = T6((A8) => A8.viewingAgentTaskId),
-    N = T6((A8) => A8.showExpandedTodos),
-    T = T6((A8) => A8.showSpinnerTree),
+    N = E6((xA) => xA.expandedView),
+    T = N === "tasks",
+    k = N === "teammates",
     k = T6((A8) => A8.selectedIPAgentIndex),
     y = T6((A8) => A8.viewSelectionMode),
     u = Z ? sL({ viewingAgentTaskId: Z, tasks: V }) : void 0,

@@@ variable 'PFA' (was 'lmA') — structural (86.0%)
--- pretty-v2.1.32.js:550502
+++ pretty-v2.1.33.js:549664
@@ -21,6 +21,7 @@
   rt();
   jU1();
   pW();
+  sW();
   ((SOz = [
     {
       id: "new-user-warmup",

@@@ function 'xI' (was 'xm') — structural (85.9%)
--- pretty-v2.1.32.js:560010
+++ pretty-v2.1.33.js:556723
@@ -3,12 +3,11 @@
     (_7("userSettings", { model: void 0 }), rG(null));
   if (A.mainLoopModel !== q.mainLoopModel && A.mainLoopModel !== null)
     (_7("userSettings", { model: A.mainLoopModel }), rG(A.mainLoopModel));
-  if (
-    A.showExpandedTodos !== q.showExpandedTodos &&
-    M6().showExpandedTodos !== A.showExpandedTodos
-  ) {
-    let K = A.showExpandedTodos;
-    OA((Y) => ({ ...Y, showExpandedTodos: K }));
+  if (A.expandedView !== q.expandedView) {
+    let K = A.expandedView === "tasks",
+      Y = A.expandedView === "teammates";
+    if (j6().showExpandedTodos !== K || j6().showSpinnerTree !== Y)
+      _A((z) => ({ ...z, showExpandedTodos: K, showSpinnerTree: Y }));
   }
   if (q !== null && A.todos !== q.todos)
     for (let K in A.todos) iq1(A.todos[K], K);

@@@ variable 'gM6' (was 'pj6') — structural (85.8%)
--- pretty-v2.1.32.js:391987
+++ pretty-v2.1.33.js:389954
@@ -19,15 +19,16 @@
   J8();
   Uj6();
   ((lPY = B.object({
-    skill: B.string().describe(
-      'The skill name. E.g., "commit", "review-pr", or "pdf"',
-    ),
+    skill: b
+      .string()
+      .describe('The skill name. E.g., "commit", "review-pr", or "pdf"'),
     args: B.string().optional().describe("Optional arguments for the skill"),
   })),
     (iPY = B.object({
       success: B.boolean().describe("Whether the skill is valid"),
       commandName: B.string().describe("The name of the skill"),
-      allowedTools: B.array(B.string())
+      allowedTools: b
+        .array(b.string())
         .optional()
         .describe("Tools allowed by this skill"),
       model: B.string().optional().describe("Model override if specified"),
@@ -37,9 +38,9 @@
       success: B.boolean().describe("Whether the skill completed successfully"),
       commandName: B.string().describe("The name of the skill"),
       status: B.literal("forked").describe("Execution status"),
-      agentId: B.string().describe(
-        "The ID of the sub-agent that executed the skill",
-      ),
+      agentId: b
+        .string()
+        .describe("The ID of the sub-agent that executed the skill"),
       result: B.string().describe("The result from the forked skill execution"),
     })),
     (rPY = B.union([iPY, nPY])),

@@@ function 'RK' (was '$K') — structural (85.6%)
--- pretty-v2.1.32.js:312505
+++ pretty-v2.1.33.js:310761
@@ -1,6 +1,11 @@
 async function $K(A = 0, q = "other", K) {
   if (PH4) return;
-  ((PH4 = !0), (process.exitCode = A));
+  ((wH4 = !0),
+    (Qu1 = setTimeout(() => {
+      zJ6(A);
+    }, 5000)),
+    Qu1.unref(),
+    (process.exitCode = A));
   try {
     let { executeSessionEndHooks: z } = await Promise.resolve().then(
       () => ($Z(), fH4),

@@@ variable 'g8' (was 'Q8') — structural (85.5%)
--- pretty-v2.1.32.js:452138
+++ pretty-v2.1.33.js:452297
@@ -9,7 +9,6 @@
   Kp();
   hG1();
   R8();
-  _6();
   ((k0 = a($1(), 1)), (_51 = { status: "idle" }));
   ((KSA = k0.default.createContext(null)),
     (dt4 = k0.default.createContext(!1)));

@@@ function 'NT6' (was 'HT6') — structural (85.1%)
--- pretty-v2.1.32.js:548142
+++ pretty-v2.1.33.js:547304
@@ -47,22 +47,18 @@
     if (z1 && z1.type === "local-jsx") {
       (H(""), y(0), u());
       let f1 = J(X, [], s4(), [], void 0, D),
-        H1 = await HG1(
-          z1,
-          (D1, t) => {
-            if (
-              (_({ jsx: null, shouldHidePromptInput: !1, clearLocalJSX: !0 }),
-              D1 && t?.display !== "skip" && A.addNotification)
-            )
-              A.addNotification({
-                key: `immediate-${z1.name}`,
-                text: D1,
-                priority: "low",
-              });
-          },
-          f1,
-          r,
-        );
+        P1 = (a, t) => {
+          if (
+            (_({ jsx: null, shouldHidePromptInput: !1, clearLocalJSX: !0 }),
+            a && t?.display !== "skip" && A.addNotification)
+          )
+            A.addNotification({
+              key: `immediate-${Y1.name}`,
+              text: a,
+              priority: "low",
+            });
+        },
+        M1 = await (await Y1.load()).call(P1, f1, c);
       if (H1) _({ jsx: H1, shouldHidePromptInput: !1, isLocalJSXCommand: !0 });
       return;
     }

@@@ function 'wZ9' (was 'Nd9') — structural (84.4%)
--- pretty-v2.1.32.js:295406
+++ pretty-v2.1.33.js:254573
@@ -13,6 +13,8 @@
     PreCompact: [],
     PermissionRequest: [],
     Setup: [],
+    TeammateIdle: [],
+    TaskCompleted: [],
   };
   if (!A.hooksConfig) return q;
   for (let [K, Y] of Object.entries(A.hooksConfig)) {

@@@ function 'o67' (was 'uW7') — structural (84.3%)
--- pretty-v2.1.32.js:186387
+++ pretty-v2.1.33.js:150557
@@ -9,10 +9,8 @@
   for (let J of w)
     if (J.type === "sequence")
       if (J.value === Ij7) ((O = !0), ($ = ""));
-      else if (J.value === xj7) {
-        if ($) H.push(IW7($));
-        ((O = !1), ($ = ""));
-      } else if (O) $ += J.value;
+      else if (J.value === ie8) (H.push(i67(O)), ($ = !1), (O = ""));
+      else if ($) O += J.value;
       else H.push(xW7(J.value));
     else if (J.type === "text")
       if (O) $ += J.value;

@@@ function 'CDz' (was 'nT6') — structural (84.1%)
--- pretty-v2.1.32.js:565621
+++ pretty-v2.1.33.js:565123
@@ -7,8 +7,13 @@
     ),
       process.exit(1));
   if (H) Yf(eW(H));
-  if (F8()) sTq().captureTeammateModeSnapshot();
   if (F8()) {
+    let { captureTeammateModeSnapshot: X } = await Promise.resolve().then(
+      () => (sj1(), aTA),
+    );
+    X();
+  }
+  if (p8()) {
     let X = TVq();
     if (X.status === "restored")
       console.log(
@@ -52,9 +57,14 @@
     Vq("setup_before_prefetch"),
     W8("info", "setup_prefetch_starting"),
     AN(mJ()),
-    iU(),
-    v54(),
-    cs4(),
+    Promise.resolve()
+      .then(() => (Vb1(), PF7))
+      .then((X) => {
+        (X.loadPluginHooks(), X.setupPluginHookHotReload());
+      }),
+    Promise.resolve()
+      .then(() => (iCA(), Bt4))
+      .then((X) => X.registerSessionFileAccessHooks()),
     kNq(),
     fNq(),
     Xs8(X4()),

@@@ variable 'gg4' (was 'wp4') — structural (83.9%)
--- pretty-v2.1.32.js:418432
+++ pretty-v2.1.33.js:416463
@@ -11,49 +11,57 @@
   _6();
   Kp4();
   ((zLY = B.strictObject({
-    operation: B.enum([
-      "goToDefinition",
-      "findReferences",
-      "hover",
-      "documentSymbol",
-      "workspaceSymbol",
-      "goToImplementation",
-      "prepareCallHierarchy",
-      "incomingCalls",
-      "outgoingCalls",
-    ]).describe("The LSP operation to perform"),
+    operation: b
+      .enum([
+        "goToDefinition",
+        "findReferences",
+        "hover",
+        "documentSymbol",
+        "workspaceSymbol",
+        "goToImplementation",
+        "prepareCallHierarchy",
+        "incomingCalls",
+        "outgoingCalls",
+      ])
+      .describe("The LSP operation to perform"),
     filePath: B.string().describe("The absolute or relative path to the file"),
-    line: B.number()
+    line: b
+      .number()
       .int()
       .positive()
       .describe("The line number (1-based, as shown in editors)"),
-    character: B.number()
+    character: b
+      .number()
       .int()
       .positive()
       .describe("The character offset (1-based, as shown in editors)"),
   })),
     (wLY = B.object({
-      operation: B.enum([
-        "goToDefinition",
-        "findReferences",
-        "hover",
-        "documentSymbol",
-        "workspaceSymbol",
-        "goToImplementation",
-        "prepareCallHierarchy",
-        "incomingCalls",
-        "outgoingCalls",
-      ]).describe("The LSP operation that was performed"),
+      operation: b
+        .enum([
+          "goToDefinition",
+          "findReferences",
+          "hover",
+          "documentSymbol",
+          "workspaceSymbol",
+          "goToImplementation",
+          "prepareCallHierarchy",
+          "incomingCalls",
+          "outgoingCalls",
+        ])
+        .describe("The LSP operation that was performed"),
       result: B.string().describe("The formatted result of the LSP operation"),
-      filePath: B.string().describe(
-        "The file path the operation was performed on",
-      ),
-      resultCount: B.number()
+      filePath: b
+        .string()
+        .describe("The file path the operation was performed on"),
+      resultCount: b
+        .number()
         .int()
         .nonnegative()
         .optional()
         .describe("Number of results (definitions, references, symbols)"),
-      fileCount: B.number()
+      fileCount: b
+        .number()
         .int()
         .nonnegative()
         .optional()

@@@ function 'h91' (was 'b91') — structural (83.8%)
--- pretty-v2.1.32.js:554494
+++ pretty-v2.1.33.js:553656
@@ -44,7 +44,7 @@
     f1 = !1,
     Z1 = void 0,
     H1 = T6((E6) => E6.spinnerTip),
-    D1 = T6((E6) => E6.showExpandedTodos),
+    M1 = E6((N6) => N6.expandedView) === "tasks",
     t = T6((E6) => E6.pendingWorkerRequest),
     e = T6((E6) => E6.pendingSandboxRequest),
     G1 = T6((E6) => E6.teamContext),
@@ -118,10 +118,13 @@
     ljq(r1, s, u.mode),
     vDq(s, Y));
   let _A = JV6(W6, m.tools, u),
-    LA = lA.useMemo(() => {
-      if (!k) return _A;
-      let { resolvedTools: E6 } = ha(k, _A, !1);
-      return E6;
+    { tools: rA, allowedAgentTypes: A8 } = cA.useMemo(() => {
+      if (!k) return { tools: i6, allowedAgentTypes: void 0 };
+      let N6 = fa(k, i6, !1);
+      return {
+        tools: N6.resolvedTools,
+        allowedAgentTypes: N6.allowedAgentTypes,
+      };
     }, [k, _A]),
     q8 = BmA(_1, b.commands),
     r7 = BmA(q8, m.commands),
@@ -208,7 +211,13 @@
         });
       else ((B1.current = E6), hz(E6));
     }, []),
-    [X6, N6] = lA.useState(null);
+    V6 = cA.useDeferredValue(x8),
+    x6 = x8.length - V6.length;
+  if (x6 > 0)
+    h(
+      `[useDeferredValue] Messages deferred by ${x6} (${V6.length}→${x8.length})`,
+    );
+  let [fA, gA] = cA.useState(null);
   AVq();
   let [g6, VA] = lA.useState([]),
     [yA, hA] = lA.useState(() => dW7()),
@@ -233,9 +242,8 @@
     }),
     i9 = lA.useCallback(
       (E6) => {
-        let M8 = new Set(E6),
-          k8 = new Set(["session", "exit", "clear"]);
-        O1((h7) => h7.filter((P4) => M8.has(P4.name) || k8.has(P4.name)));
+        let M8 = new Set(N6);
+        X1((S8) => S8.filter(($K) => M8.has($K.name) || PuA.has($K)));
       },
       [O1],
     ),
@@ -280,7 +288,10 @@
     [Z8, _q] = lA.useState(!1),
     [f3, rq] = lA.useState(!1),
     [lY, jY] = lA.useState(!1),
-    z4 = lA.useRef(!1),
+    F6 = t_(),
+    T8 = cA.useRef(F6);
+  T8.current = F6;
+  let M7 = cA.useRef(!1),
     m9 = lA.useRef(null),
     [iY] = M7(),
     m6 = lA.useCallback(() => {
@@ -463,7 +474,12 @@
     }, [c2, $q]));
   function Mc() {
     if (c2 === "elicitation") return;
-    if (((z4.current = !1), sA(), c2 === "tool-permission"))
+    if (
+      (h(`[onCancel] focusedInputDialog=${u_} streamMode=${G7}`),
+      (M7.current = !1),
+      dq(),
+      u_ === "tool-permission")
+    )
       ($4[0]?.onAbort(), uq([]));
     else if (BH.isRemoteMode) BH.cancelRequest();
     else V4?.abort();
@@ -586,7 +602,7 @@
             isNonInteractiveSession: !1,
             dynamicMcpConfig: X1,
             theme: iY,
-            agentDefinitions: U,
+            agentDefinitions: A8 ? { ...g, allowedAgentTypes: A8 } : g,
             customSystemPrompt: D,
             appendSystemPrompt: j,
           },
@@ -675,6 +691,7 @@
         D,
         j,
         AH,
+        bH,
       ],
     ),
     Gc = lA.useCallback(
@@ -704,7 +721,7 @@
             C$(),
             y$(),
           ]),
-          EN = { ...q9, ...e$z(r1) };
+          xJ = { ...G5, ...YXz(l1), ...{} };
         P3("query_context_loading_end");
         let KH = Z51({
           mainThreadAgentDefinition: k,
@@ -937,7 +954,7 @@
                   }
                 },
                 EN = d$(Y4, [], s4(), [], void 0, o),
-                KH = await HG1(q5, F9, EN, G9);
+                c0 = await (await bq.load()).call(B_, xJ, b5);
               if (KH)
                 E4({
                   jsx: KH,
@@ -1007,6 +1024,7 @@
           onBeforeQuery: M,
           canUseTool: eM,
           addNotification: AA,
+          streamMode: G7,
         });
       },
       [
@@ -1039,6 +1057,7 @@
         Iz,
         m1,
         AA,
+        G7,
       ],
     ),
     eR = lA.useCallback(
@@ -1440,9 +1459,9 @@
               }
               x5((p7) => {
                 return (
-                  p7
-                    .filter((J4) => J4.hostPattern.host === P4)
-                    .forEach((J4) => J4.resolvePromise(M8)),
+                  O4.filter((j7) => j7.hostPattern.host === B4).forEach((j7) =>
+                    j7.resolvePromise(M8),
+                  ),
                   p7.filter((J4) => J4.hostPattern.host !== P4)
                 );
               });

@@@ function 'aHz' (was 'Twz') — structural (83.8%)
--- pretty-v2.1.32.js:540807
+++ pretty-v2.1.33.js:539240
@@ -1,5 +1,5 @@
 function Twz(A) {
-  let q = A1(56),
+  let q = q1(55),
     {
       apiKeyStatus: K,
       debug: Y,
@@ -36,7 +36,6 @@
     r = m === void 0 ? !1 : m,
     z1 = b === void 0 ? !1 : b,
     f1 = FD(),
-    { columns: Z1 } = z8(),
     H1;
   if (q[0] !== g || q[1] !== f1 || q[2] !== P)
     ((H1 = P || DmA(f1) || g),
@@ -77,8 +76,7 @@
     else o = q[8];
     return o;
   }
-  let e = Z1 < 80 ? "column" : "row",
-    G1;
+  let M1;
   if (
     q[9] !== z ||
     q[10] !== r ||
@@ -206,12 +204,11 @@
       (q[46] = E1));
   else E1 = q[46];
   let q1;
-  if (q[47] !== e || q[48] !== V1 || q[49] !== E1)
+  if (q[47] !== t || q[48] !== j1)
     ((q1 = q$.createElement(
       I,
       {
-        flexDirection: e,
-        flexWrap: "wrap",
+        flexDirection: "row",
         justifyContent: "space-between",
         paddingX: 2,
         gap: 1,
@@ -221,22 +218,21 @@
     )),
       (q[47] = e),
       (q[48] = V1),
-      (q[49] = E1),
-      (q[50] = q1));
-  else q1 = q[50];
+      (q[49] = w1));
+  else w1 = q[49];
   let s = Z ? y : void 0,
     j1;
-  if (q[51] !== s)
+  if (q[50] !== V1)
     ((j1 = q$.createElement(xXq, { selectedIndex: s })),
-      (q[51] = s),
-      (q[52] = j1));
-  else j1 = q[52];
+      (q[50] = V1),
+      (q[51] = E1));
+  else E1 = q[51];
   let J1;
-  if (q[53] !== j1 || q[54] !== q1)
+  if (q[52] !== E1 || q[53] !== w1)
     ((J1 = q$.createElement(q$.Fragment, null, q1, j1)),
+      (q[52] = E1),
       (q[53] = j1),
-      (q[54] = q1),
-      (q[55] = J1));
-  else J1 = q[55];
+      (q[54] = e));
+  else e = q[54];
   return J1;
 }

@@@ variable 'dkA' (was 'QkA') — structural (83.6%)
--- pretty-v2.1.32.js:415957
+++ pretty-v2.1.33.js:413930
@@ -6,7 +6,8 @@
   KK1();
   fM();
   ((kkY = B.strictObject({
-    task_id: B.string()
+    task_id: b
+      .string()
       .optional()
       .describe("The ID of the background task to stop"),
     shell_id: B.string().optional().describe("Deprecated: use task_id instead"),
@@ -15,7 +16,8 @@
       message: B.string().describe("Status message about the operation"),
       task_id: B.string().describe("The ID of the task that was stopped"),
       task_type: B.string().describe("The type of the task that was stopped"),
-      command: B.string()
+      command: b
+        .string()
         .optional()
         .describe("The command or description of the stopped task"),
     })),

@@@ function 'B06' (was 'm06') — structural (83.6%)
--- pretty-v2.1.32.js:356091
+++ pretty-v2.1.33.js:354360
@@ -1,6 +1,7 @@
 function m06({ tasks: A, isStandalone: q = !1 }) {
   let K = T6((m) => m.teamContext),
     Y = T6((m) => m.tasks),
+    z = Object.values(Y).some((x) => F$(x) && x.status === "running"),
     [, z] = lq.useState(0),
     { rows: w, columns: H } = z8(),
     O = w <= 10 ? 0 : Math.min(10, Math.max(3, w - 14)),
@@ -124,7 +125,7 @@
           " · ",
           lq.createElement(YA, {
             shortcut: "ctrl+t",
-            action: "hide tasks",
+            action: z ? "show teammates" : "hide tasks",
             bold: !0,
           }),
         ),

@@@ function 'EF1' (was 'rm1') — structural (83.1%)
--- pretty-v2.1.32.js:425932
+++ pretty-v2.1.33.js:423181
@@ -1,5 +1,5 @@
-function rm1() {
-  let A = A51(),
+function EF1(A) {
+  let q = n31(A),
     q = A - FLA,
     K = process.env.CLAUDE_AUTOCOMPACT_PCT_OVERRIDE;
   if (K) {

@@@ variable 'Fp4' (was 'Ad4') — structural (82.8%)
--- pretty-v2.1.32.js:419723
+++ pretty-v2.1.33.js:417741
@@ -5,14 +5,16 @@
     taskId: B.string().describe("The ID of the task to retrieve"),
   })),
     (RLY = B.object({
-      task: B.object({
-        id: B.string(),
-        subject: B.string(),
-        description: B.string(),
-        status: g81,
-        blocks: B.array(B.string()),
-        blockedBy: B.array(B.string()),
-      }).nullable(),
+      task: b
+        .object({
+          id: b.string(),
+          subject: b.string(),
+          description: b.string(),
+          status: T81,
+          blocks: b.array(b.string()),
+          blockedBy: b.array(b.string()),
+        })
+        .nullable(),
     })),
     (ep4 = {
       name: eq1,
@@ -69,7 +71,6 @@
             tool_use_id: q,
             type: "tool_result",
             content: "Task not found",
-            is_error: !0,
           };
         let Y = [
           `Task #${K.id}: ${K.subject}`,

@@@ variable 'bW1' (was 'AG1') — structural (82.6%)
--- pretty-v2.1.32.js:415718
+++ pretty-v2.1.33.js:413691
@@ -13,12 +13,12 @@
       bytes: B.number().describe("Size of the fetched content in bytes"),
       code: B.number().describe("HTTP response code"),
       codeText: B.string().describe("HTTP response code text"),
-      result: B.string().describe(
-        "Processed result from applying the prompt to the content",
-      ),
-      durationMs: B.number().describe(
-        "Time taken to fetch and process the content",
-      ),
+      result: b
+        .string()
+        .describe("Processed result from applying the prompt to the content"),
+      durationMs: b
+        .number()
+        .describe("Time taken to fetch and process the content"),
       url: B.string().describe("The URL that was fetched"),
     })));
   sD = {

@@@ function 'KXq' (was 'p_q') — structural (82.3%)
--- pretty-v2.1.32.js:535075
+++ pretty-v2.1.33.js:533480
@@ -51,7 +51,8 @@
     { columns: T } = z8(),
     k = j !== void 0 ? D[j] : void 0,
     y = k && U_q(k.schema);
-  GN6("Claude Code needs your input", "elicitation_dialog");
+  (GV("elicitation"),
+    CN6("Claude Code needs your input", "elicitation_dialog"));
   function u(H1) {
     let D1 = D.length + 2,
       t =
@@ -110,7 +111,7 @@
     () => {
       g();
     },
-    { context: "Settings", isActive: p && P === "" },
+    { context: "Settings", isActive: p },
   ),
     Y8(
       (H1, D1) => {

@@@ variable 'zkq' (was 'qvq') — structural (82.2%)
--- pretty-v2.1.32.js:568410
+++ pretty-v2.1.33.js:570113
@@ -136,55 +136,6 @@
   ps();
   _6();
   BNq();
-  FNq();
-  gNq();
-  pNq();
-  cNq();
-  iNq();
-  rNq();
-  oNq();
-  e51();
-  fTq();
-  NTq();
-  TTq();
-  VP1();
-  xD();
-  Rq();
-  kTq();
-  Zd();
-  xh();
-  TmA();
-  IFA();
-  ITq();
-  BTq();
-  cTq();
-  Kp();
-  hG1();
-  $w();
-  Mz();
-  wH();
-  PZ();
-  RX();
-  iTq();
-  V51();
-  ah();
-  WMA();
-  eA();
-  kd();
-  Z7();
-  qV6();
-  lmA();
-  n41();
-  Vd1();
-  EO();
-  PFA();
-  e51();
-  Pt();
-  jH();
-  nTq();
-  iD();
-  pp1();
-  oG();
   MK = a($1(), 1);
   Vq("main_tsx_entry");
   Vq("main_tsx_imports_loaded");

@@@ function 'Md' (was 'jd') — structural (81.8%)
--- pretty-v2.1.32.js:425945
+++ pretty-v2.1.33.js:423194
@@ -1,13 +1,12 @@
-function jd(A) {
-  let q = rm1(),
-    K = Md() ? q : A51(),
+function Md(A, q) {
+  let K = EF1(q),
+    Y = jd() ? K : n31(q),
     Y = Math.max(0, Math.round(((K - A) / K) * 100)),
     z = K - VyY,
     w = K - NyY,
     H = A >= z,
     O = A >= w,
     $ = Md() && A >= q,
-    _ = H5(),
     X = _W(_, Zj()) - QLA,
     D = process.env.CLAUDE_CODE_BLOCKING_LIMIT_OVERRIDE,
     j = D ? parseInt(D, 10) : NaN,

@@@ function 'lY6' (was 'XOA') — structural (81.7%)
--- pretty-v2.1.32.js:246101
+++ pretty-v2.1.33.js:210279
@@ -142,6 +142,8 @@
         : `There's an issue with the selected model (${q}). It may not exist or you may not have access to it. Run /model to pick a different model.`,
       error: "invalid_request",
     });
+  if (A instanceof QW)
+    return IY({ content: `${vO}: ${WY6(A)}`, error: "unknown" });
   if (A instanceof Error)
     return zz({ content: `${J_}: ${A.message}`, error: "unknown" });
   return zz({ content: J_, error: "unknown" });

@@@ function 'aMq' (was 'NDq') — structural (81.7%)
--- pretty-v2.1.32.js:546813
+++ pretty-v2.1.33.js:545981
@@ -14,14 +14,7 @@
       `[Reconnection] Member ${K} not found in team ${q} - may have been removed`,
     );
   let w = z?.agentId,
-    H = process.env.HOME || process.env.USERPROFILE || ".",
-    O = fDq(
-      H,
-      ".claude",
-      "teams",
-      q.replace(/[^a-zA-Z0-9]/g, "-").toLowerCase(),
-      "config.json",
-    );
+    H = rMq(MW(), q.replace(/[^a-zA-Z0-9]/g, "-").toLowerCase(), "config.json");
   (A(($) => ({
     ...$,
     teamContext: {

@@@ function 'lZY' (was 'FPY') — structural (81.5%)
--- pretty-v2.1.32.js:391262
+++ pretty-v2.1.33.js:389228
@@ -58,7 +58,7 @@
       .join(" ")),
       (y = y ? `${y} --model ${k7([_])}` : `--model ${k7([_])}`));
   let u = y ? ` ${y}` : "",
-    S = `cd ${k7([W])} && CLAUDECODE=1 ${k7([T])} ${k}${u}`;
+    S = `cd ${E7([W])} && CLAUDECODE=1 CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 ${E7([T])} ${k}${u}`;
   await gL4(Z, S, !P);
   let m = P ? "current" : mV,
     b = P ? "current" : "swarm-view";

@@@ variable 'rD6' (was 'hj6') — structural (81.5%)
--- pretty-v2.1.32.js:421109
+++ pretty-v2.1.33.js:419560
@@ -35,29 +35,28 @@
   ((JLA = a($1(), 1)),
     (fW6 = $6(process.env.CLAUDE_CODE_DISABLE_BACKGROUND_TASKS)),
     (tLY = B.object({
-      description: B.string().describe(
-        "A short (3-5 word) description of the task",
-      ),
+      description: b
+        .string()
+        .describe("A short (3-5 word) description of the task"),
       prompt: B.string().describe("The task for the agent to perform"),
-      subagent_type: B.string().describe(
-        "The type of specialized agent to use for this task",
-      ),
-      model: B.enum(["sonnet", "opus", "haiku"])
-        .optional()
-        .describe(
-          "Optional model to use for this agent. If not specified, inherits from parent. Prefer haiku for quick, straightforward tasks to minimize cost and latency.",
-        ),
-      resume: B.string()
+      subagent_type: b
+        .string()
+        .describe("The type of specialized agent to use for this task"),
+      model: b.enum(["sonnet", "opus", "haiku"]).optional().describe(DyY),
+      resume: b
+        .string()
         .optional()
         .describe(
           "Optional agent ID to resume from. If provided, the agent will continue from the previous execution transcript.",
         ),
-      run_in_background: B.boolean()
+      run_in_background: b
+        .boolean()
         .optional()
         .describe(
           `Set to true to run this agent in the background. The tool result will include an output_file path - use ${Nq} tool or ${T4} tail to check on output.`,
         ),
-      max_turns: B.number()
+      max_turns: b
+        .number()
         .int()
         .positive()
         .optional()
@@ -67,7 +66,8 @@
     })),
     (eLY = B.object({
       name: B.string().optional().describe("Name for the spawned agent"),
-      team_name: B.string()
+      team_name: b
+        .string()
         .optional()
         .describe(
           "Team name for spawning. Uses current team context if omitted.",
@@ -91,15 +91,19 @@
         output_tokens: B.number(),
         cache_creation_input_tokens: B.number().nullable(),
         cache_read_input_tokens: B.number().nullable(),
-        server_tool_use: B.object({
-          web_search_requests: B.number(),
-          web_fetch_requests: B.number(),
-        }).nullable(),
+        server_tool_use: b
+          .object({
+            web_search_requests: b.number(),
+            web_fetch_requests: b.number(),
+          })
+          .nullable(),
         service_tier: B.enum(["standard", "priority", "batch"]).nullable(),
-        cache_creation: B.object({
-          ephemeral_1h_input_tokens: B.number(),
-          ephemeral_5m_input_tokens: B.number(),
-        }).nullable(),
+        cache_creation: b
+          .object({
+            ephemeral_1h_input_tokens: b.number(),
+            ephemeral_5m_input_tokens: b.number(),
+          })
+          .nullable(),
       }),
     })),
     (qRY = ARY.extend({ status: B.literal("completed"), prompt: B.string() })),
@@ -108,13 +112,18 @@
       agentId: B.string().describe("The ID of the async agent"),
       description: B.string().describe("The description of the task"),
       prompt: B.string().describe("The prompt for the agent"),
-      outputFile: B.string().describe(
-        "Path to the output file for checking agent progress",
-      ),
+      outputFile: b
+        .string()
+        .describe("Path to the output file for checking agent progress"),
     })),
     (YRY = B.union([qRY, KRY, Vz4])));
   ZW1 = {
-    async prompt({ agents: A, tools: q, getToolPermissionContext: K }) {
+    async prompt({
+      agents: A,
+      tools: q,
+      getToolPermissionContext: K,
+      allowedAgentTypes: Y,
+    }) {
       let Y = await K(),
         z = [];
       for (let $ of q)
@@ -124,7 +133,7 @@
         }
       let w = id4(A, z),
         H = _LA(w, Y, OK);
-      return await xx4(H, !1);
+      return await Zh4($, !1, Y);
     },
     name: OK,
     maxResultSizeChars: 1e5,
@@ -190,7 +199,12 @@
         return { data: { status: "teammate_spawned", prompt: A, ...n.data } };
       }
       let V = J.options.agentDefinitions.activeAgents,
-        Z = _LA(V, W.toolPermissionContext, OK),
+        { allowedAgentTypes: Z } = J.options.agentDefinitions,
+        N = ZLA(
+          Z ? V.filter((c) => Z.includes(c.agentType)) : V,
+          W.toolPermissionContext,
+          XK,
+        ),
         N = Z.find((n) => n.agentType === q);
       if (!N) {
         if (V.find((r) => r.agentType === q)) {

@@@ variable 'QYq' (was 'f9q') — structural (81.2%)
--- pretty-v2.1.32.js:495937
+++ pretty-v2.1.33.js:496045
@@ -124,6 +124,20 @@
           values: ["init", "maintenance"],
         },
       },
+      TeammateIdle: {
+        summary: "When a teammate is about to go idle",
+        description: `Input to command is JSON with teammate_name and team_name.
+Exit code 0 - stdout/stderr not shown
+Exit code 2 - show stderr to teammate and prevent idle (teammate continues working)
+Other exit codes - show stderr to user only`,
+      },
+      TaskCompleted: {
+        summary: "When a task is being marked as completed",
+        description: `Input to command is JSON with task_id, task_subject, task_description, teammate_name, and team_name.
+Exit code 0 - stdout/stderr not shown
+Exit code 2 - show stderr to model and prevent task completion
+Other exit codes - show stderr to user only`,
+      },
     };
   });
 });

@@@ variable 'np4' (was '_d4') — structural (81.1%)
--- pretty-v2.1.32.js:419906
+++ pretty-v2.1.33.js:417925
@@ -4,27 +4,33 @@
   N9();
   oz();
   JO();
+  jG();
   ((yLY = g81.or(B.literal("deleted"))),
     (CLY = B.strictObject({
       taskId: B.string().describe("The ID of the task to update"),
       subject: B.string().optional().describe("New subject for the task"),
-      description: B.string()
+      description: b
+        .string()
         .optional()
         .describe("New description for the task"),
-      activeForm: B.string()
+      activeForm: b
+        .string()
         .optional()
         .describe(
           'Present continuous form shown in spinner when in_progress (e.g., "Running tests")',
         ),
       status: yLY.optional().describe("New status for the task"),
-      addBlocks: B.array(B.string())
+      addBlocks: b
+        .array(b.string())
         .optional()
         .describe("Task IDs that this task blocks"),
-      addBlockedBy: B.array(B.string())
+      addBlockedBy: b
+        .array(b.string())
         .optional()
         .describe("Task IDs that block this task"),
       owner: B.string().optional().describe("New owner for the task"),
-      metadata: B.record(B.string(), B.unknown())
+      metadata: b
+        .record(b.string(), b.unknown())
         .optional()
         .describe(
           "Metadata keys to merge into the task. Set a key to null to delete it.",
@@ -84,8 +90,8 @@
       ) {
         let J = WP();
         _.setAppState((M) => {
-          if (M.showExpandedTodos) return M;
-          return { ...M, showExpandedTodos: !0 };
+          if (j.expandedView === "tasks") return j;
+          return { ...j, expandedView: "tasks" };
         });
         let X = Jg(J, A);
         if (!X)
@@ -130,7 +136,35 @@
               },
             };
           }
-          if (z !== X.status) ((j.status = z), D.push("status"));
+          if (z !== X.status) {
+            if (z === "completed") {
+              let j = [],
+                W = NQ1(
+                  A,
+                  X.subject,
+                  X.description,
+                  B5(),
+                  Q3(),
+                  void 0,
+                  _?.abortController?.signal,
+                  void 0,
+                  _,
+                );
+              for await (let G of W)
+                if (G.blockingError) j.push(VQ1(G.blockingError));
+              if (j.length > 0)
+                return {
+                  data: {
+                    success: !1,
+                    taskId: A,
+                    updatedFields: [],
+                    error: j.join(`
+`),
+                  },
+                };
+            }
+            ((M.status = z), D.push("status"));
+          }
         }
         if (Object.keys(j).length > 0) bC(J, A, j);
         if (j.owner && F8()) {
@@ -183,7 +217,6 @@
             tool_use_id: q,
             type: "tool_result",
             content: w || `Task #${Y} not found`,
-            is_error: !0,
           };
         let O = `Updated task #${Y} ${z.join(", ")}`;
         if (H?.to === "completed" && z0() && F8())

@@@ function 'h06' (was 'OVA') — structural (81.1%)
--- pretty-v2.1.32.js:355526
+++ pretty-v2.1.33.js:353806
@@ -1,4 +1,5 @@
 async function OVA({ clearOnboarding: A = !1 }) {
+  let { flushTelemetry: q } = await Promise.resolve().then(() => (OVA(), $VA));
   (await lv4(),
     await js8(),
     Cj().delete(),

@@@ function 'sm1' (was 'Rm1') — structural (81.1%)
--- pretty-v2.1.32.js:358236
+++ pretty-v2.1.33.js:375542
@@ -1,7 +1,9 @@
 function Rm1(A) {
   for (let q = A.length - 1; q >= 0; q--) {
     let K = A[q];
-    if (K?.type !== "assistant") continue;
+    if (!K) continue;
+    if (K.type === "user" && typeof K.message.content === "string") break;
+    if (K.type !== "assistant") continue;
     for (let Y of K.message.content)
       if (
         Y.type === "tool_use" &&
@@ -23,7 +25,6 @@
                 : void 0;
         if (w) return `[to ${z}] ${w}`;
       }
-    break;
   }
   return;
 }

@@@ function 'OV6' (was 'tf6') — structural (80.7%)
--- pretty-v2.1.32.js:491018
+++ pretty-v2.1.33.js:491112
@@ -1,7 +1,7 @@
 function tf6({ onDone: A, onForegroundTask: q, toolUseContext: K }) {
   let Y = T6((x) => x.tasks),
     z = T6((x) => x.foregroundedTaskId),
-    w = T6((x) => x.showSpinnerTree),
+    w = E6((p) => p.expandedView) === "teammates",
     H = L7(),
     O = Y,
     $ = DK.useRef(!1),
@@ -114,12 +114,18 @@
       setAppState: H,
     });
   }
+  let k = aq.useEffectEvent(A);
   K91.useEffect(() => {
-    if (_.mode !== "list" && !Object.keys(O ?? {}).includes(_.itemId))
-      J({ mode: "list" });
+    if (_.mode !== "list") {
+      let r = ($ ?? {})[_.itemId];
+      if (!r || !ZR(r))
+        if (O.current)
+          k("Background tasks dialog dismissed", { display: "system" });
+        else J({ mode: "list" });
+    }
     let x = P.length;
     if (X >= x && x > 0) D(x - 1);
-  }, [_, O, X, P]);
+  }, [_, $, X, P, k]);
   let k = () => {
     if ($.current)
       A("Background tasks dialog dismissed", { display: "system" });
@@ -224,7 +230,6 @@
         shortcut: "Enter",
         action: "view",
       }),
-      ...[],
       ...((V?.type === "local_agent" && V.status === "running" && q) ||
       (V?.type === "in_process_teammate" && V.status === "running")
         ? [

@@@ variable 'JMq' (was 'a0q') — structural (80.0%)
--- pretty-v2.1.32.js:545405
+++ pretty-v2.1.33.js:543873
@@ -4,7 +4,6 @@
   k6();
   uQ();
   Pz();
-  I6();
   ZHz = new Set([
     "assistant",
     "user",

@@@ function 'eXz' (was 'WJz') — structural (79.6%)
--- pretty-v2.1.32.js:561958
+++ pretty-v2.1.33.js:558922
@@ -285,6 +285,10 @@
       } finally {
         ((X = !1), x.start());
       }
+      if ((await $()).queuedCommands.length > 0) {
+        c();
+        return;
+      }
       {
         let G1 = (await O()).teamContext;
         if (G1 && cj(G1))

@@@ function 'mXA' (was 'hjA') — structural (79.2%)
--- pretty-v2.1.32.js:297423
+++ pretty-v2.1.33.js:254351
@@ -1,4 +1,5 @@
 function hjA(A, q) {
+  let K = eP9(A);
   switch (q) {
     case "project":
       return Va(y6(), ".claude", "agent-memory", A) + Jj1;

@@@ variable 'os' (was 'zt') — structural (78.9%)
--- pretty-v2.1.32.js:448021
+++ pretty-v2.1.33.js:448143
@@ -22,31 +22,38 @@
   nF1();
   ss();
   ((CCA = B.strictObject({
-    file_path: B.string().describe(
-      "The absolute path to the file to write (must be absolute, not relative)",
-    ),
+    file_path: b
+      .string()
+      .describe(
+        "The absolute path to the file to write (must be absolute, not relative)",
+      ),
     content: B.string().describe("The content to write to the file"),
   })),
     (VQY = B.object({
-      type: B.enum(["create", "update"]).describe(
-        "Whether a new file was created or an existing file was updated",
-      ),
+      type: b
+        .enum(["create", "update"])
+        .describe(
+          "Whether a new file was created or an existing file was updated",
+        ),
       filePath: B.string().describe("The path to the file that was written"),
       content: B.string().describe("The content that was written to the file"),
       structuredPatch: B.array(W$A).describe("Diff patch showing the changes"),
-      originalFile: B.string()
+      originalFile: b
+        .string()
         .nullable()
         .describe(
           "The original file content before the write (null for new files)",
         ),
-      gitDiff: B.object({
-        filename: B.string(),
-        status: B.enum(["modified", "added"]),
-        additions: B.number(),
-        deletions: B.number(),
-        changes: B.number(),
-        patch: B.string(),
-      }).optional(),
+      gitDiff: b
+        .object({
+          filename: b.string(),
+          status: b.enum(["modified", "added"]),
+          additions: b.number(),
+          deletions: b.number(),
+          changes: b.number(),
+          patch: b.string(),
+        })
+        .optional(),
     })),
     (fG = {
       name: B5,

@@@ function '_mY' (was 'HBY') — structural (78.8%)
--- pretty-v2.1.32.js:440097
+++ pretty-v2.1.33.js:437993
@@ -1,6 +1,6 @@
-function HBY(A) {
+function _mY(A, q) {
   if (!$6(process.env.CLAUDE_CODE_ENABLE_TOKEN_USAGE_ATTACHMENT)) return [];
-  let q = A51(),
+  let K = n31(q),
     K = RV(A);
   return [{ type: "token_usage", used: K, total: q, remaining: q - K }];
 }

@@@ function 'N89' (was 'eG9') — structural (78.7%)
--- pretty-v2.1.32.js:246383
+++ pretty-v2.1.33.js:210563
@@ -4,5 +4,5 @@
       "accessToken" in A
         ? { Authorization: `Bearer ${A.accessToken}`, "anthropic-beta": Wf }
         : { "x-api-key": A.apiKey };
-  return (await rA.get(q, { headers: K })).data.enabled;
+  return (await iA.get(q, { headers: K })).data;
 }

@@@ variable 'zLA' (was 'ALA') — structural (78.4%)
--- pretty-v2.1.32.js:419147
+++ pretty-v2.1.33.js:417155
@@ -4,6 +4,7 @@
   a6();
   Ep4();
   Sp4();
+  U31();
   ((PLY = B.strictObject({})),
     (ZLY = B.object({
       message: B.string().describe("Confirmation that plan mode was entered"),
@@ -67,7 +68,11 @@
       mapToolResultToToolResultBlockParam({ message: A }, q) {
         return {
           type: "tool_result",
-          content: `${A}
+          content: uO()
+            ? `${A}
+
+DO NOT write or edit any files except the plan file. Detailed workflow instructions will follow.`
+            : `${A}
 
 In plan mode, you should:
 1. Thoroughly explore the codebase to understand existing patterns

@@@ variable 'OJ6' (was 'y06') — structural (78.3%)
--- pretty-v2.1.32.js:354660
+++ pretty-v2.1.33.js:311550
@@ -28,6 +28,7 @@
       "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC",
       "CLAUDE_CODE_DISABLE_TERMINAL_TITLE",
       "CLAUDE_CODE_ENABLE_TELEMETRY",
+      "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS",
       "CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL",
       "CLAUDE_CODE_MAX_OUTPUT_TOKENS",
       "CLAUDE_CODE_SKIP_BEDROCK_AUTH",

@@@ function 'zG6' (was '$G6') — structural (78.3%)
--- pretty-v2.1.32.js:430147
+++ pretty-v2.1.33.js:427906
@@ -11,6 +11,7 @@
       getToolPermissionContext: q.getToolPermissionContext,
       tools: q.tools,
       agents: q.agents,
+      allowedAgentTypes: q.allowedAgentTypes,
     }),
     input_schema: Y,
   };

@@@ variable 'o0q' (was 'mXq') — structural (77.8%)
--- pretty-v2.1.32.js:541050
+++ pretty-v2.1.33.js:539479
@@ -8,7 +8,6 @@
   Hp();
   WSA();
   uhA();
-  jmA();
   ((q$ = a($1(), 1)), (uXq = a($1(), 1)));
   BXq = uXq.memo(Twz);
 });

@@@ variable 'ts' (was 'e31') — structural (77.1%)
--- pretty-v2.1.32.js:425715
+++ pretty-v2.1.33.js:422964
@@ -15,6 +15,7 @@
   OD();
   FU();
   I6();
+  I6();
   ((JyY = new Set([Nq, T4, t9, Kz, bT, bO, aq, B5])),
     (GG1 = new Set()),
     (FW6 = new Set()),

@@@ function 'fa' (was 'ha') — structural (76.8%)
--- pretty-v2.1.32.js:302336
+++ pretty-v2.1.33.js:265822
@@ -25,11 +25,12 @@
   let D = [],
     j = [],
     M = [],
-    W = new Set();
+    W = new Set(),
+    G;
   for (let G of Y) {
-    let { toolName: P } = MW(G);
+    let { toolName: V, ruleContent: Z } = VW(P);
     if (P === OK) {
-      D.push(G);
+      if ((D.push(P), Z)) G = Z.split(",").map((T) => T.trim());
       continue;
     }
     let V = X.get(P);
@@ -37,5 +38,11 @@
       if ((D.push(G), !W.has(V))) (M.push(V), W.add(V));
     } else j.push(G);
   }
-  return { hasWildcard: !1, validTools: D, invalidTools: j, resolvedTools: M };
+  return {
+    hasWildcard: !1,
+    validTools: D,
+    invalidTools: M,
+    resolvedTools: j,
+    allowedAgentTypes: G,
+  };
 }

@@@ variable 'TvA' (was 'ZvA') — structural (76.5%)
--- pretty-v2.1.32.js:391716
+++ pretty-v2.1.33.js:389682
@@ -17,5 +17,6 @@
   MR();
   tq1();
   lS();
+  tS();
   ((rx4 = a($1(), 1)), (MvA = gA1.firstParty));
 });

@@@ function 'b5z' (was 'JKz') — structural (76.2%)
--- pretty-v2.1.32.js:518636
+++ pretty-v2.1.33.js:518757
@@ -1,5 +1,7 @@
 function JKz(A) {
-  let q = 0;
+  let q = 0,
+    K = !1,
+    Y = "";
   while (q < A.length) {
     let K = A.indexOf(
         `
@@ -27,7 +29,17 @@
         if (_?.text && typeof _.text === "string") O = _.text;
       }
       if (!O) continue;
-      let $ = O.replace(/\n/g, " ").trim();
+      let J = _.replace(/\n/g, " ").trim(),
+        X = V4(J, _P);
+      if (X) {
+        let D = X.replace(/^\//, ""),
+          M = V4(J, "command-args")?.trim() || "";
+        if (ap().has(D) || !M) {
+          if (!Y) Y = X;
+          continue;
+        }
+        return M ? `${X} ${M}` : X;
+      }
       if (cwq.test($)) continue;
       if ($.length > 200) $ = $.slice(0, 200).trim() + "…";
       return $;
@@ -35,5 +47,6 @@
       continue;
     }
   }
+  if (Y) return Y;
   return "";
 }

@@@ function 'df' (was 'lf') — structural (76.0%)
--- pretty-v2.1.32.js:138459
+++ pretty-v2.1.33.js:111304
@@ -13,7 +13,6 @@
     A ||
     Y ||
     ((z === "ANTHROPIC_API_KEY" || z === "apiKeyHelper") &&
-      !$6(process.env.CLAUDE_CODE_REMOTE) &&
-      process.env.CLAUDE_CODE_ENVIRONMENT_KIND !== "bridge")
+      !_6(process.env.CLAUDE_CODE_REMOTE))
   );
 }

@@@ function 'K5z' (was 'xqz') — structural (76.0%)
--- pretty-v2.1.32.js:516149
+++ pretty-v2.1.33.js:516268
@@ -62,6 +62,7 @@
 
 ### Phase 4: Final Plan
 Goal: Write your final plan to the plan file (the only file you can edit).
+- Begin with a **Context** section: explain why this change is being made — the problem or need it addresses, what prompted it, and the intended outcome
 - Include only your recommended approach, not all alternatives
 - Ensure that the plan file is concise enough to scan quickly, but detailed enough to execute effectively
 - Include the paths of critical files to be modified

@@@ variable 'dz6' (was 'g26') — structural (75.8%)
--- pretty-v2.1.32.js:254288
+++ pretty-v2.1.33.js:218455
@@ -3,13 +3,16 @@
   ((Q26 = B.strictObject({
     file_path: B.string().describe("The absolute path to the file to modify"),
     old_string: B.string().describe("The text to replace"),
-    new_string: B.string().describe(
-      "The text to replace it with (must be different from old_string)",
-    ),
-    replace_all: B.boolean()
+    new_string: b
+      .string()
+      .describe(
+        "The text to replace it with (must be different from old_string)",
+      ),
+    replace_all: b
+      .boolean()
       .default(!1)
       .optional()
-      .describe("Replace all occurences of old_string (default false)"),
+      .describe("Replace all occurrences of old_string (default false)"),
   })),
     (W$A = B.object({
       oldStart: B.number(),
@@ -22,21 +25,23 @@
       filePath: B.string().describe("The file path that was edited"),
       oldString: B.string().describe("The original string that was replaced"),
       newString: B.string().describe("The new string that replaced it"),
-      originalFile: B.string().describe(
-        "The original file contents before editing",
-      ),
+      originalFile: b
+        .string()
+        .describe("The original file contents before editing"),
       structuredPatch: B.array(W$A).describe("Diff patch showing the changes"),
-      userModified: B.boolean().describe(
-        "Whether the user modified the proposed changes",
-      ),
+      userModified: b
+        .boolean()
+        .describe("Whether the user modified the proposed changes"),
       replaceAll: B.boolean().describe("Whether all occurrences were replaced"),
-      gitDiff: B.object({
-        filename: B.string(),
-        status: B.enum(["modified", "added"]),
-        additions: B.number(),
-        deletions: B.number(),
-        changes: B.number(),
-        patch: B.string(),
-      }).optional(),
+      gitDiff: b
+        .object({
+          filename: b.string(),
+          status: b.enum(["modified", "added"]),
+          additions: b.number(),
+          deletions: b.number(),
+          changes: b.number(),
+          patch: b.string(),
+        })
+        .optional(),
     })));
 });

@@@ variable 'Vb1' (was 'zu1') — structural (75.7%)
--- pretty-v2.1.32.js:295454
+++ pretty-v2.1.33.js:254626
@@ -20,6 +20,8 @@
         PreCompact: [],
         PermissionRequest: [],
         Setup: [],
+        TeammateIdle: [],
+        TaskCompleted: [],
       };
     for (let Y of A) {
       if (!Y.hooksConfig) continue;

@@@ variable 'r4' (was 'i4') — structural (75.5%)
--- pretty-v2.1.32.js:519861
+++ pretty-v2.1.33.js:519995
@@ -13,7 +13,11 @@
   az();
   u3();
   gz();
-  JHq = a(kh6(), 1);
+  Promise.resolve()
+    .then(() => s(bMA(), 1))
+    .then((A) => {
+      qOq = A.getLanguage;
+    });
   ds4 = qA(async () => {
     let A = s4();
     setTimeout(() => {

@@@ class 'Hx4' (was 'fL4') — structural (75.5%)
--- pretty-v2.1.32.js:366478
+++ pretty-v2.1.33.js:387580
@@ -58,7 +58,11 @@
             : `--model ${k7([A.model])}`));
       let J = _ ? ` ${_}` : "",
         X = A.cwd,
-        D = `cd ${k7([X])} && CLAUDECODE=1 ${k7([H])} ${O}${J}`;
+        D = ["CLAUDECODE=1"];
+      if (process.env.CLAUDE_CONFIG_DIR)
+        D.push(`CLAUDE_CONFIG_DIR=${E7([process.env.CLAUDE_CONFIG_DIR])}`);
+      let M = D.join(" "),
+        j = `cd ${E7([X])} && ${M} ${E7([H])} ${$}${J}`;
       if (
         (await this.backend.sendCommandToPane(Y, D, !w),
         this.spawnedTeammates.set(q, { paneId: Y, insideTmux: w }),

@@@ function 'cd4' (was 'gd4') — structural (74.9%)
--- pretty-v2.1.32.js:421818
+++ pretty-v2.1.33.js:420283
@@ -41,24 +41,6 @@
         ),
     );
   }
-  if (A.status === "teammate_spawned") {
-    let W = A,
-      G = W.color ? HO[W.color] : void 0;
-    return bA.createElement(
-      f,
-      null,
-      "  ",
-      G ? bA.createElement(f, { color: G }, KY) : null,
-      G ? " " : "",
-      bA.createElement(
-        f,
-        { dimColor: !0 },
-        "spawned ",
-        W.name,
-        W.is_splitpane ? " (split-pane)" : "",
-      ),
-    );
-  }
   if (A.status !== "completed") return null;
   let {
       agentId: w,

@@@ function 'SBY' (was 'RuY') — structural (74.6%)
--- pretty-v2.1.32.js:439391
+++ pretty-v2.1.33.js:437287
@@ -2,7 +2,7 @@
   let q = await A.getAppState();
   if (q.toolPermissionContext.mode !== "delegate") return [];
   if (!q.teamContext) return [];
-  let z = `${process.env.HOME || process.env.USERPROFILE || "."}/.claude/tasks/${q.teamContext.teamName}/`;
+  let Y = `${$8()}/tasks/${q.teamContext.teamName}/`;
   return [
     {
       type: "delegate_mode",

@@@ function 'NLA' (was 'DLA') — structural (74.4%)
--- pretty-v2.1.32.js:422262
+++ pretty-v2.1.33.js:420708
@@ -1,5 +1,4 @@
 function DLA(A) {
-  if (F8() && A?.team_name && A?.name) return BV;
   if (A?.subagent_type && A.subagent_type !== Jb1.agentType) {
     if (A.subagent_type === "worker") return "Task";
     return A.subagent_type;

@@@ function 'n31' (was 'A51') — structural (74.3%)
--- pretty-v2.1.32.js:425927
+++ pretty-v2.1.33.js:423177
@@ -1,5 +1,4 @@
-function A51() {
-  let A = H5(),
-    q = Math.min(gLA(A), fyY);
+function n31(A) {
+  let q = Math.min(mLA(A), jCY);
   return _W(A, Zj()) - q;
 }

@@@ function 'iZY' (was 'QPY') — structural (74.1%)
--- pretty-v2.1.32.js:391397
+++ pretty-v2.1.33.js:389363
@@ -51,7 +51,7 @@
       .join(" ")),
       (k = k ? `${k} --model ${k7([_])}` : `--model ${k7([_])}`));
   let y = k ? ` ${k}` : "",
-    u = `cd ${k7([G])} && CLAUDECODE=1 ${k7([N])} ${T}${y}`,
+    u = `cd ${E7([G])} && CLAUDECODE=1 CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 ${E7([N])} ${T}${y}`,
     S = await CA(tW, ["send-keys", "-t", `${mV}:${W}`, u, "Enter"]);
   if (S.code !== 0)
     throw Error(`Failed to send command to tmux window: ${S.stderr}`);

@@@ function 'dRY' (was 'mDY') — structural (74.1%)
--- pretty-v2.1.32.js:367739
+++ pretty-v2.1.33.js:418456
@@ -1,5 +1,4 @@
 function mDY(A) {
-  if (!A) return sD1();
   if (!f_(A)) return A;
   return sD1();
 }

@@@ variable 'R2q' (was 'tYq') — structural (74.0%)
--- pretty-v2.1.32.js:502362
+++ pretty-v2.1.33.js:502328
@@ -1,12 +1,6 @@
 var tYq = v(() => {
   jH();
   u1();
-  R8();
-  x7();
-  a6();
-  rYq();
-  u3();
-  aYq = a($1(), 1);
   ((TAz = {
     name: "sandbox",
     get description() {
@@ -31,7 +25,7 @@
     immediate: !0,
     type: "local-jsx",
     userFacingName: () => "sandbox",
-    call: NAz,
+    load: () => Promise.resolve().then(() => (k2q(), E2q)),
   }),
     (sYq = TAz));
 });

@@@ function 'OmY' (was 'wBY') — structural (73.6%)
--- pretty-v2.1.32.js:440077
+++ pretty-v2.1.33.js:437973
@@ -4,9 +4,9 @@
     Y = T9();
   if (!q || !K) return [];
   if (A.some(($) => $.type === "assistant")) return [];
-  let w = process.env.HOME || process.env.USERPROFILE || ".",
-    H = `${w}/.claude/teams/${q}/config.json`,
-    O = `${w}/.claude/tasks/${q}/`;
+  let w = $8(),
+    H = `${w}/teams/${q}/config.json`,
+    $ = `${w}/tasks/${q}/`;
   return [
     {
       type: "team_context",

@@@ function 'CN6' (was 'GN6') — structural (73.5%)
--- pretty-v2.1.32.js:531108
+++ pretty-v2.1.33.js:529511
@@ -1,7 +1,7 @@
 function GN6(A, q) {
   let K = cb();
   (yBA.useEffect(() => {
-    (sYz(), wz1());
+    j11();
   }, []),
     yBA.useEffect(() => {
       let Y = !1,

@@@ variable 'EH' (was '$w') — structural (73.4%)
--- pretty-v2.1.32.js:312539
+++ pretty-v2.1.33.js:310801
@@ -41,7 +41,11 @@
                 : "unknown",
           K =
             A instanceof Error
-              ? { error_name: A.name, error_message: A.message.slice(0, 2000) }
+              ? {
+                  error_name: A.name,
+                  error_message: A.message.slice(0, 2000),
+                  error_stack: A.stack?.slice(0, 4000),
+                }
               : { error_message: String(A).slice(0, 2000) };
         (W8("error", "unhandled_rejection", K),
           c("tengu_unhandled_rejection", { error_name: q }));

@@@ function '_e' (was 'We') — structural (73.3%)
--- pretty-v2.1.32.js:519838
+++ pretty-v2.1.33.js:519972
@@ -1,5 +1,5 @@
 function We(A) {
   let q = SuA(A);
   if (!q) return "unknown";
-  return JHq.getLanguage(q.slice(1))?.name ?? "unknown";
+  return qOq?.(q.slice(1))?.name ?? "unknown";
 }

@@@ function 'IyY' (was 'ZRY') — structural (72.9%)
--- pretty-v2.1.32.js:422588
+++ pretty-v2.1.33.js:421037
@@ -16,60 +16,56 @@
     switch ($.type) {
       case "local-jsx":
         return new Promise((_) => {
-          HG1(
-            $,
-            (X, D) => {
-              if (D?.display === "skip") {
+          let J = (X, D) => {
+            if (D?.display === "skip") {
+              _({ messages: [], shouldQuery: !1, command: O });
+              return;
+            }
+            let M = (D?.metaMessages ?? []).map((j) =>
+              g6({ content: j, isMeta: !0 }),
+            );
+            _({
+              messages:
+                D?.display === "system"
+                  ? [
+                      ELA(RQ1(O, q)),
+                      ELA(`<local-command-stdout>${X}</local-command-stdout>`),
+                      ...M,
+                    ]
+                  : [
+                      g6({
+                        content: TZ({
+                          inputString: RQ1(O, q),
+                          precedingInputBlocks: z,
+                        }),
+                      }),
+                      X
+                        ? g6({
+                            content: `<local-command-stdout>${X}</local-command-stdout>`,
+                          })
+                        : g6({
+                            content: `<local-command-stdout>${Tv}</local-command-stdout>`,
+                          }),
+                      ...M,
+                    ],
+              shouldQuery: D?.shouldQuery ?? !1,
+              command: O,
+            });
+          };
+          O.load()
+            .then((X) => X.call(J, Y, q))
+            .then((X) => {
+              if (Y.options.isNonInteractiveSession) {
                 _({ messages: [], shouldQuery: !1, command: $ });
                 return;
               }
-              let j = (D?.metaMessages ?? []).map((M) =>
-                p6({ content: M, isMeta: !0 }),
-              );
               _({
-                messages:
-                  D?.display === "system"
-                    ? [
-                        GLA(SQ1($, q)),
-                        GLA(
-                          `<local-command-stdout>${X}</local-command-stdout>`,
-                        ),
-                        ...j,
-                      ]
-                    : [
-                        p6({
-                          content: GZ({
-                            inputString: SQ1($, q),
-                            precedingInputBlocks: z,
-                          }),
-                        }),
-                        X
-                          ? p6({
-                              content: `<local-command-stdout>${X}</local-command-stdout>`,
-                            })
-                          : p6({
-                              content: `<local-command-stdout>${Tv}</local-command-stdout>`,
-                            }),
-                        ...j,
-                      ],
-                shouldQuery: D?.shouldQuery ?? !1,
-                command: $,
+                jsx: X,
+                shouldHidePromptInput: !0,
+                showSpinner: !1,
+                isLocalJSXCommand: !0,
               });
-            },
-            Y,
-            q,
-          ).then((X) => {
-            if (Y.options.isNonInteractiveSession) {
-              _({ messages: [], shouldQuery: !1, command: $ });
-              return;
-            }
-            K({
-              jsx: X,
-              shouldHidePromptInput: !0,
-              showSpinner: !1,
-              isLocalJSXCommand: !0,
             });
-          });
         });
       case "local": {
         let _ = p6({
@@ -77,7 +73,7 @@
         });
         try {
           let J = gM(),
-            X = await od4($, q, Y);
+            D = await (await O.load()).call(q, Y);
           if (X.type === "skip")
             return { messages: [], shouldQuery: !1, command: $ };
           if (X.type === "compact") {

@@@ variable 'Cp4' (was 'lp4') — structural (72.6%)
--- pretty-v2.1.32.js:419600
+++ pretty-v2.1.33.js:417616
@@ -4,15 +4,17 @@
   uO();
   ((ELY = B.strictObject({
     subject: B.string().describe("A brief title for the task"),
-    description: B.string().describe(
-      "A detailed description of what needs to be done",
-    ),
-    activeForm: B.string()
+    description: b
+      .string()
+      .describe("A detailed description of what needs to be done"),
+    activeForm: b
+      .string()
       .optional()
       .describe(
         'Present continuous form shown in spinner when in_progress (e.g., "Running tests")',
       ),
-    metadata: B.record(B.string(), B.unknown())
+    metadata: b
+      .record(b.string(), b.unknown())
       .optional()
       .describe("Arbitrary metadata to attach to the task"),
   })),
@@ -66,8 +68,8 @@
         });
         return (
           z.setAppState((H) => {
-            if (H.showExpandedTodos) return H;
-            return { ...H, showExpandedTodos: !0 };
+            if (H.expandedView === "tasks") return H;
+            return { ...H, expandedView: "tasks" };
           }),
           { data: { task: { id: w, subject: A } } }
         );

@@@ variable 'h8q' (was 'ne4') — structural (72.4%)
--- pretty-v2.1.32.js:456167
+++ pretty-v2.1.33.js:466208
@@ -1,5 +1,15 @@
 var ne4 = v(() => {
   d1();
   u1();
+  i9();
+  L8q();
+  eH();
+  B6();
+  cz();
+  nq();
+  DP1();
+  V7();
+  eq();
+  w3();
   ((WpY = a($1(), 1)), (ie4 = a($1(), 1)));
 });

@@@ variable 's2q' (was 'Z6q') — structural (72.4%)
--- pretty-v2.1.32.js:461431
+++ pretty-v2.1.33.js:504981
@@ -11,28 +11,5 @@
   F6();
   xZ6();
   Q8();
-  uZ6();
-  Q7();
-  DhA();
-  j6q();
-  hq();
-  a5();
-  jhA();
-  G6q();
-  vD();
-  Tq();
-  LK();
-  Cq();
-  k51();
-  zO();
-  R8();
-  lB();
-  BA();
-  Vg1();
-  g4();
-  N9();
-  em1();
-  L51();
-  pW();
   ((r6 = a($1(), 1)), (kZ = a($1(), 1)));
 });

@@@ variable 'EN6' (was 'RxA') — structural (72.4%)
--- pretty-v2.1.32.js:491540
+++ pretty-v2.1.33.js:525559
@@ -16,11 +16,5 @@
   q5q();
   E0();
   Wq();
-  Tq();
-  Cq();
-  hq();
-  _6();
-  Jp1();
-  fM();
   ((DK = a($1(), 1)), (K91 = a($1(), 1)));
 });

@@@ variable 'YXq' (was 'SN6') — structural (72.4%)
--- pretty-v2.1.32.js:536780
+++ pretty-v2.1.33.js:533919
@@ -13,11 +13,5 @@
   F6();
   Dm();
   zO();
-  rW();
-  J8();
-  ZJq();
-  LK();
-  jS();
-  D7();
   ((A5 = a($1(), 1)), (fJq = a($1(), 1)));
 });

@@@ variable 'p0q' (was 'yfq') — structural (72.4%)
--- pretty-v2.1.32.js:553727
+++ pretty-v2.1.33.js:538881
@@ -4,5 +4,21 @@
   K2();
   DBA();
   _6();
+  RM();
+  R0q();
+  Hd1();
+  k9();
+  C0q();
+  ch();
+  g8();
+  h0q();
+  x0q();
+  m0q();
+  lq();
+  qK();
+  Cq();
+  y3();
+  F4();
+  mA();
   ((Im = a($1(), 1)), (Rd1 = a($1(), 1)));
 });

@@@ variable '$Dq' (was 'XVq') — structural (72.4%)
--- pretty-v2.1.32.js:554438
+++ pretty-v2.1.33.js:540142
@@ -3,5 +3,22 @@
   u1();
   r8();
   Tq();
+  tW();
+  I7();
+  KDq();
+  eq();
+  M6();
+  Nj();
+  by1();
+  Tw();
+  nq();
+  iV();
+  ch();
+  z$();
+  ImA();
+  RM();
+  g8();
+  I6();
+  TS();
   ((oM = a($1(), 1)), (ST6 = a($1(), 1)));
 });

@@@ variable 'mFA' (was 'XFA') — structural (72.4%)
--- pretty-v2.1.32.js:556251
+++ pretty-v2.1.33.js:555432
@@ -149,5 +149,6 @@
   OVq();
   XVq();
   jVq();
+  m$();
   ((N7 = a($1(), 1)), (lA = a($1(), 1)));
 });

@@@ variable 'xvq' (was 'ITq') — structural (72.4%)
--- pretty-v2.1.32.js:564176
+++ pretty-v2.1.33.js:561670
@@ -6,5 +6,6 @@
   Ez();
   i4();
   IFA();
+  V5();
   ((sM = a($1(), 1)), (cT6 = a($1(), 1)));
 });

@@@ function 'je' (was 'fe') — structural (72.2%)
--- pretty-v2.1.32.js:523227
+++ pretty-v2.1.33.js:524140
@@ -2,5 +2,6 @@
   let A = f8() || {};
   (Object.assign(process.env, M6().env),
     Object.assign(process.env, A.env),
+    P_q(),
     POq());
 }

@@@ function 'oMq' (was 'VDq') — structural (71.6%)
--- pretty-v2.1.32.js:546775
+++ pretty-v2.1.33.js:545946
@@ -12,11 +12,8 @@
     K1(Error(`[computeInitialTeamContext] Could not read team file for ${q}`));
     return;
   }
-  let w = process.env.HOME || process.env.USERPROFILE || ".",
-    H = fDq(
-      w,
-      ".claude",
-      "teams",
+  let w = rMq(
+      MW(),
       q.replace(/[^a-zA-Z0-9]/g, "-").toLowerCase(),
       "config.json",
     ),

@@@ function 'Dm1' (was 'tK1') — structural (70.4%)
--- pretty-v2.1.32.js:356857
+++ pretty-v2.1.33.js:355127
@@ -1,9 +1,9 @@
 function tK1(A, q, K, Y) {
   let z = A === "requesting" ? 50 : 200,
-    w = ROA(z);
-  if (K === !1 || Y) return -100;
+    [w, H] = vL(z);
+  if (K === !1 || Y) return [w, -100];
   let H = Math.floor(w / z),
     O = q.length + 20;
-  if (A === "requesting") return (H % O) - 10;
-  return q.length + 10 - (H % O);
+  if (A === "requesting") return [w, ($ % O) - 10];
+  return [w, q.length + 10 - ($ % O)];
 }

@@@ class 'bd1' (was 'Bd1') — structural (70.3%)
--- pretty-v2.1.32.js:560579
+++ pretty-v2.1.33.js:557518
@@ -18,7 +18,7 @@
       (this.sessionId = K),
       (this.messageBuffer = new fu1(zJz)));
   }
-  connect() {
+  async connect() {
     if (this.state !== "idle" && this.state !== "reconnecting") {
       (h(`WebSocketTransport: Cannot connect, current state is ${this.state}`, {
         level: "error",
@@ -36,56 +36,82 @@
         h(
           `WebSocketTransport: Adding X-Last-Request-Id header: ${this.lastSentId}`,
         ));
-    let K =
-      typeof Bun < "u"
-        ? { headers: q, proxy: uA6(this.url.href) }
-        : { headers: q, agent: BA1(this.url.href) };
-    ((this.ws = new FP(this.url.href, K)),
-      this.ws.on("open", () => {
-        let Y = Date.now() - A;
-        (h("WebSocketTransport: Connected"),
-          W8("info", "cli_websocket_connect_connected", { duration_ms: Y }));
-        let z = this.ws.upgradeReq;
-        if (z?.headers?.["x-last-request-id"]) {
-          let w = z.headers["x-last-request-id"];
-          this.replayBufferedMessages(w);
-        }
-        ((this.reconnectAttempts = 0),
-          (this.state = "connected"),
-          this.startPingInterval(),
-          K64(() => {
-            if (this.state === "connected" && this.ws)
-              try {
-                (this.ws.send(
-                  g1({ type: "keep_alive" }) +
-                    `
+    if (typeof Bun < "u") {
+      let K = new globalThis.WebSocket(this.url.href, {
+        headers: q,
+        proxy: uA1(this.url.href),
+      });
+      ((this.ws = K),
+        K.addEventListener("open", () => {
+          this.handleOpenEvent(A);
+        }),
+        K.addEventListener("message", (Y) => {
+          let z = typeof Y.data === "string" ? Y.data : String(Y.data);
+          if (this.onData) this.onData(z);
+        }),
+        K.addEventListener("error", () => {
+          (h("WebSocketTransport: Error", { level: "error" }),
+            O8("error", "cli_websocket_connect_error"),
+            this.handleConnectionError());
+        }),
+        K.addEventListener("close", (Y) => {
+          (h(`WebSocketTransport: Closed: ${Y.code}`, { level: "error" }),
+            O8("error", "cli_websocket_connect_closed"),
+            this.handleConnectionError());
+        }));
+    } else {
+      let { default: K } = await Promise.resolve().then(() => (FU1(), BP6)),
+        Y = new K(this.url.href, { headers: q, agent: bA1(this.url.href) });
+      ((this.ws = Y),
+        Y.on("open", () => {
+          let z = Y.upgradeReq;
+          if (z?.headers?.["x-last-request-id"]) {
+            let w = z.headers["x-last-request-id"];
+            this.replayBufferedMessages(w);
+          }
+          this.handleOpenEvent(A);
+        }),
+        Y.on("message", (z) => {
+          let w = z.toString();
+          if (this.onData) this.onData(w);
+        }),
+        Y.on("error", (z) => {
+          (h(`WebSocketTransport: Error: ${z.message}`, { level: "error" }),
+            O8("error", "cli_websocket_connect_error"),
+            this.handleConnectionError());
+        }),
+        Y.on("close", (z, w) => {
+          (h(`WebSocketTransport: Closed: ${z}`, { level: "error" }),
+            O8("error", "cli_websocket_connect_closed"),
+            this.handleConnectionError());
+        }),
+        Y.on("pong", () => {
+          this.pongReceived = !0;
+        }));
+    }
+  }
+  handleOpenEvent(A) {
+    let q = Date.now() - A;
+    (h("WebSocketTransport: Connected"),
+      O8("info", "cli_websocket_connect_connected", { duration_ms: q }),
+      (this.reconnectAttempts = 0),
+      (this.state = "connected"),
+      this.startPingInterval(),
+      XS7(() => {
+        if (this.state === "connected" && this.ws)
+          try {
+            (this.ws.send(
+              Q1({ type: "keep_alive" }) +
+                `
 `,
-                ),
-                  h("WebSocketTransport: Sent keep_alive (activity signal)"));
-              } catch (w) {
-                (h(`WebSocketTransport: Keep-alive failed: ${w}`, {
-                  level: "error",
-                }),
-                  W8("error", "cli_websocket_keepalive_failed"));
-              }
-          }));
-      }),
-      this.ws.on("message", (Y) => {
-        let z = Y.toString();
-        if (this.onData) this.onData(z);
-      }),
-      this.ws.on("error", (Y) => {
-        (h(`WebSocketTransport: Error: ${Y.message}`, { level: "error" }),
-          W8("error", "cli_websocket_connect_error"),
-          this.handleConnectionError());
-      }),
-      this.ws.on("close", (Y, z) => {
-        (h(`WebSocketTransport: Closed: ${Y}`, { level: "error" }),
-          W8("error", "cli_websocket_connect_closed"),
-          this.handleConnectionError());
-      }),
-      this.ws.on("pong", () => {
-        this.pongReceived = !0;
+            ),
+              h("WebSocketTransport: Sent keep_alive (activity signal)"));
+          } catch (K) {
+            (h(`WebSocketTransport: Keep-alive failed: ${K}`, {
+              level: "error",
+            }),
+              O8("error", "cli_websocket_keepalive_failed"));
+          }
       }));
   }
   sendLine(A) {
@@ -216,8 +242,8 @@
     return "";
   }
   startPingInterval() {
-    (this.stopPingInterval(),
-      (this.pongReceived = !0),
+    if ((this.stopPingInterval(), typeof Bun < "u")) return;
+    ((this.pongReceived = !0),
       (this.pingInterval = setInterval(() => {
         if (this.state === "connected" && this.ws) {
           if (!this.pongReceived) {

@@@ function 'dc4' (was 'Yl4') — structural (70.3%)
--- pretty-v2.1.32.js:425983
+++ pretty-v2.1.33.js:423231
@@ -1,7 +1,8 @@
 async function Yl4(A, q, K, Y) {
   if ($6(process.env.DISABLE_COMPACT)) return { wasCompacted: !1 };
-  if (!(await TyY(A, Y))) return { wasCompacted: !1 };
-  let w = await pW6(A, q.agentId, rm1());
+  let z = q.options.mainLoopModel;
+  if (!(await PCY(A, z, Y))) return { wasCompacted: !1 };
+  let H = await bW6(A, q.agentId, EF1(z));
   if (w) return (s31(void 0), { wasCompacted: !0, compactionResult: w });
   try {
     let H = await tM1(A, q, K, !0, void 0, !0);

@@@ variable 'v_q' (was 'vOq') — structural (70.3%)
--- pretty-v2.1.32.js:523394
+++ pretty-v2.1.33.js:524314
@@ -26,9 +26,6 @@
   ps();
   az();
   _6();
-  oG();
-  ei();
-  pL1();
   TOq = qA(() => {
     let A = Date.now();
     (W8("info", "init_started"), Vq("init_function_start"));
@@ -46,7 +43,11 @@
         Vq("init_safe_env_vars_applied"),
         ZH4(),
         Vq("init_after_graceful_shutdown"),
-        Pw7(),
+        Promise.resolve()
+          .then(() => (mu1(), YH4))
+          .then((w) => {
+            w.initialize1PEventLogging();
+          }),
         Vq("init_after_1p_event_logging"),
         T08(),
         Vq("init_after_oauth_populate"),
@@ -84,7 +85,10 @@
       (W8("info", "init_completed", { duration_ms: Date.now() - A }),
         Vq("init_function_end"));
     } catch (q) {
-      if (q instanceof Gf) return fOq({ error: q });
+      if (q instanceof Wf)
+        return Promise.resolve()
+          .then(() => (V_q(), f_q))
+          .then((K) => K.showInvalidConfigDialog({ error: q }));
       else throw q;
     }
   });

@@@ function 'ge4' (was 'ot4') — structural (69.6%)
--- pretty-v2.1.32.js:452670
+++ pretty-v2.1.33.js:452828
@@ -1,9 +1,6 @@
 function ot4({ onPaste: A, onInput: q, onImagePaste: K }) {
   let [Y, z] = yR.default.useState({ chunks: [], timeoutId: null }),
     [w, H] = yR.default.useState(!1),
-    O = yR.default.useRef(!1),
-    $ = yR.default.useRef(!1),
-    _ = yR.default.useRef(!1),
     J = yR.default.useRef(!0),
     X = yR.default.useMemo(() => iA() === "macos", []);
   yR.default.useEffect(() => {
@@ -74,62 +71,30 @@
         }, wUY);
       },
       [j, X, K, A],
-    ),
-    { stdin: W } = wo();
-  return (
-    yR.default.useEffect(() => {
-      if (!W) return;
-      let P = (V) => {
-        let Z = V.toString();
-        if (Z.includes("\x1B[200~"))
-          (H(!0), (O.current = !0), ($.current = !1), (_.current = !1));
-        if (O.current && !_.current) {
-          if (
-            Z.replaceAll("\x1B[200~", "")
-              .replaceAll("\x1B[201~", "")
-              .replaceAll("\x1B[I", "")
-              .replaceAll("\x1B[O", "")
-              .replace(/\[[IO]$/, "").length > 0
-          )
-            _.current = !0;
-        }
-        if (Z.includes("\x1B[201~")) {
-          if (!_.current) H(!1);
-          if (X && O.current && !_.current && K) j();
-          if (((O.current = !1), ($.current = !1), !_.current))
-            z((N) => {
-              if (N.timeoutId) clearTimeout(N.timeoutId);
-              return { chunks: [], timeoutId: null };
-            });
-          _.current = !1;
-        }
-      };
-      return (
-        W.on("data", P),
-        () => {
-          (W.off("data", P), H(!1));
-        }
-      );
-    }, [W, K, j, X]),
-    {
-      wrappedOnInput: (P, V) => {
-        if (O.current) $.current = !0;
-        let Z = P.split(/ (?=\/|[A-Za-z]:\\)/)
-          .flatMap((T) =>
-            T.split(`
+    );
+  return {
+    wrappedOnInput: (M, j, W) => {
+      let G = W.keypress.isPasted;
+      if (G) H(!0);
+      let P = M.split(/ (?=\/|[A-Za-z]:\\)/)
+        .flatMap((Z) =>
+          Z.split(`
 `),
-          )
-          .some((T) => R26(T.trim()));
-        if (A && (P.length > L26 || Y.timeoutId || Z || w)) {
-          z(({ chunks: T, timeoutId: k }) => {
-            return { chunks: [...T, P], timeoutId: M(k) };
-          });
-          return;
-        }
-        if ((q(P, V), P.length > 10)) H(!1);
-      },
-      pasteState: Y,
-      isPasting: w,
-    }
-  );
+        )
+        .some((Z) => Sz6(Z.trim()));
+      if (G && M.length === 0 && O && K) {
+        (J(), H(!1));
+        return;
+      }
+      if (A && (M.length > Cz6 || Y.timeoutId || P || G)) {
+        z(({ chunks: Z, timeoutId: N }) => {
+          return { chunks: [...Z, M], timeoutId: X(N) };
+        });
+        return;
+      }
+      if ((q(M, j), M.length > 10)) H(!1);
+    },
+    pasteState: Y,
+    isPasting: w,
+  };
 }

@@@ function '$9q' (was 'r3q') — structural (69.4%)
--- pretty-v2.1.32.js:490421
+++ pretty-v2.1.33.js:490557
@@ -1,5 +1,5 @@
 function r3q(A) {
-  let q = A1(66),
+  let q = q1(61),
     { teammate: K, onDone: Y, onKill: z, onBack: w, onForeground: H } = A,
     [O] = M7(),
     $;
@@ -9,8 +9,7 @@
   let _ = $,
     J = M31(K.startTime, K.status === "running"),
     X;
-  if (q[1] !== Y)
-    ((X = { "confirm:no": Y, "confirm:yes": Y }), (q[1] = Y), (q[2] = X));
+  if (q[1] !== Y) ((X = { "confirm:yes": Y }), (q[1] = Y), (q[2] = X));
   else X = q[2];
   let D;
   if (q[3] === Symbol.for("react.memo_cache_sentinel"))
@@ -33,8 +32,7 @@
       (q[9] = j));
   else j = q[9];
   Y8(j);
-  let M = Kq(),
-    W;
+  let j;
   if (
     q[10] !== K.awaitingPlanApproval ||
     q[11] !== K.isIdle ||
@@ -85,7 +83,8 @@
       (q[23] = k),
       (q[24] = y));
   else y = q[24];
-  let u;
+  let y = k,
+    u;
   if (q[25] !== K.status)
     ((u =
       K.status !== "running" &&
@@ -156,15 +155,55 @@
       (q[36] = b),
       (q[37] = U));
   else U = q[37];
+  let U = g,
+    B;
+  if (q[38] !== w || q[39] !== H || q[40] !== z || q[41] !== K.status)
+    ((B = (P1) =>
+      P1.pending
+        ? $w.default.createElement(
+            f,
+            null,
+            "Press ",
+            P1.keyName,
+            " again to exit",
+          )
+        : $w.default.createElement(
+            nA,
+            null,
+            w &&
+              $w.default.createElement(HA, {
+                shortcut: "←",
+                action: "go back",
+              }),
+            $w.default.createElement(HA, {
+              shortcut: "Esc/Enter/Space",
+              action: "close",
+            }),
+            K.status === "running" &&
+              z &&
+              $w.default.createElement(HA, { shortcut: "k", action: "kill" }),
+            K.status === "running" &&
+              H &&
+              $w.default.createElement(HA, {
+                shortcut: "f",
+                action: "foreground",
+              }),
+          )),
+      (q[38] = w),
+      (q[39] = H),
+      (q[40] = z),
+      (q[41] = K.status),
+      (q[42] = B));
+  else B = q[42];
   let g;
-  if (q[38] !== K.progress || q[39] !== K.status || q[40] !== O)
+  if (q[43] !== K.progress || q[44] !== K.status || q[45] !== $)
     ((g =
       K.status === "running" &&
       K.progress?.recentActivities &&
       K.progress.recentActivities.length > 0 &&
       gY.default.createElement(
         I,
-        { flexDirection: "column", marginTop: 1 },
+        { flexDirection: "column" },
         gY.default.createElement(f, { bold: !0, dimColor: !0 }, "Progress"),
         K.progress.recentActivities.map((H1, D1) =>
           gY.default.createElement(
@@ -179,29 +218,29 @@
           ),
         ),
       )),
-      (q[38] = K.progress),
-      (q[39] = K.status),
-      (q[40] = O),
-      (q[41] = g));
-  else g = q[41];
+      (q[43] = K.progress),
+      (q[44] = K.status),
+      (q[45] = $),
+      (q[46] = p));
+  else p = q[46];
   let x;
-  if (q[42] === Symbol.for("react.memo_cache_sentinel"))
+  if (q[47] === Symbol.for("react.memo_cache_sentinel"))
     ((x = gY.default.createElement(f, { bold: !0, dimColor: !0 }, "Prompt")),
-      (q[42] = x));
-  else x = q[42];
+      (q[47] = r));
+  else r = q[47];
   let p;
-  if (q[43] !== Z)
+  if (q[48] !== V)
     ((p = gY.default.createElement(
       I,
       { flexDirection: "column", marginTop: 1 },
       x,
       gY.default.createElement(f, { wrap: "wrap" }, Z),
     )),
-      (q[43] = Z),
-      (q[44] = p));
-  else p = q[44];
+      (q[48] = V),
+      (q[49] = c));
+  else c = q[49];
   let n;
-  if (q[45] !== K.error || q[46] !== K.status)
+  if (q[50] !== K.error || q[51] !== K.status)
     ((n =
       K.status === "failed" &&
       K.error &&
@@ -211,110 +250,41 @@
         gY.default.createElement(f, { bold: !0, color: "error" }, "Error"),
         gY.default.createElement(f, { color: "error", wrap: "wrap" }, K.error),
       )),
-      (q[45] = K.error),
-      (q[46] = K.status),
-      (q[47] = n));
-  else n = q[47];
-  let r;
-  if (q[48] !== g || q[49] !== p || q[50] !== n)
-    ((r = gY.default.createElement(I, { flexDirection: "column" }, g, p, n)),
-      (q[48] = g),
-      (q[49] = p),
-      (q[50] = n),
-      (q[51] = r));
-  else r = q[51];
-  let z1;
-  if (q[52] !== U || q[53] !== r || q[54] !== y)
-    ((z1 = gY.default.createElement(
-      I,
-      { width: "100%" },
-      gY.default.createElement(
-        I,
-        {
-          borderStyle: "round",
-          borderColor: "background",
-          flexDirection: "column",
-          marginTop: 1,
-          paddingLeft: 1,
-          paddingRight: 1,
-          width: "100%",
-        },
-        y,
-        U,
-        r,
-      ),
-    )),
-      (q[52] = U),
-      (q[53] = r),
-      (q[54] = y),
-      (q[55] = z1));
-  else z1 = q[55];
+      (q[50] = K.error),
+      (q[51] = K.status),
+      (q[52] = Y1));
+  else Y1 = q[52];
   let f1;
   if (
-    q[56] !== M.keyName ||
-    q[57] !== M.pending ||
+    q[53] !== Y ||
+    q[54] !== U ||
+    q[55] !== B ||
+    q[56] !== p ||
+    q[57] !== c ||
     q[58] !== w ||
-    q[59] !== H ||
-    q[60] !== z ||
-    q[61] !== K.status
+    q[59] !== y
   )
     ((f1 = gY.default.createElement(
       I,
-      { marginLeft: 2 },
-      M.pending
-        ? gY.default.createElement(
-            f,
-            { dimColor: !0 },
-            "Press ",
-            M.keyName,
-            " again to exit",
-          )
-        : gY.default.createElement(
-            f,
-            { dimColor: !0 },
-            gY.default.createElement(
-              pA,
-              null,
-              w &&
-                gY.default.createElement(YA, {
-                  shortcut: "←",
-                  action: "go back",
-                }),
-              gY.default.createElement(YA, {
-                shortcut: "Esc/Enter/Space",
-                action: "close",
-              }),
-              K.status === "running" &&
-                z &&
-                gY.default.createElement(YA, { shortcut: "k", action: "kill" }),
-              K.status === "running" &&
-                H &&
-                gY.default.createElement(YA, {
-                  shortcut: "f",
-                  action: "foreground",
-                }),
-            ),
-          ),
-    )),
-      (q[56] = M.keyName),
-      (q[57] = M.pending),
-      (q[58] = w),
-      (q[59] = H),
-      (q[60] = z),
-      (q[61] = K.status),
-      (q[62] = f1));
-  else f1 = q[62];
-  let Z1;
-  if (q[63] !== z1 || q[64] !== f1)
-    ((Z1 = gY.default.createElement(
+      {
+        title: y,
+        subtitle: U,
+        onCancel: Y,
+        color: "background",
+        inputGuide: B,
+      },
       I,
-      { width: "100%", flexDirection: "column" },
       z1,
       f1,
     )),
-      (q[63] = z1),
-      (q[64] = f1),
-      (q[65] = Z1));
-  else Z1 = q[65];
+      (q[53] = Y),
+      (q[54] = U),
+      (q[55] = B),
+      (q[56] = p),
+      (q[57] = c),
+      (q[58] = Y1),
+      (q[59] = y),
+      (q[60] = f1));
+  else f1 = q[60];
   return Z1;
 }

@@@ variable 'R0q' (was 'R_q') — structural (69.2%)
--- pretty-v2.1.32.js:533420
+++ pretty-v2.1.33.js:538067
@@ -11,6 +11,5 @@
   k6();
   MN6();
   IO();
-  Qk();
   fN = a($1(), 1);
 });

@@@ variable 'Vjq' (was 'm_q') — structural (69.2%)
--- pretty-v2.1.32.js:534929
+++ pretty-v2.1.33.js:547027
@@ -8,22 +8,5 @@
   __q();
   RBA();
   CBA();
-  M_q();
-  G_q();
-  sF1();
-  dI1();
-  P01();
-  xv();
-  AG1();
-  Z_q();
-  T_q();
-  TQ1();
-  xBA();
-  ALA();
-  k_q();
-  pj6();
-  R_q();
-  DW6();
-  u_q();
   mBA = a($1(), 1);
 });

@@@ variable 'ajq' (was 'MXq') — structural (69.2%)
--- pretty-v2.1.32.js:539648
+++ pretty-v2.1.33.js:548492
@@ -3,14 +3,5 @@
   u1();
   x7();
   FA();
-  Q8();
-  Tq();
-  Wq();
-  j3();
-  jXq();
-  z_();
-  fM();
-  JM();
-  Jd1();
   l4 = a($1(), 1);
 });

@@@ variable 'qWq' (was 'xjq') — structural (69.2%)
--- pretty-v2.1.32.js:549816
+++ pretty-v2.1.33.js:548657
@@ -1,11 +1,5 @@
 var xjq = v(() => {
   d1();
   g4();
-  F6();
-  si();
-  BA();
-  J8();
-  gmA();
-  dW6();
   Ce = a($1(), 1);
 });

@@@ variable 'YWq' (was 'Vfq') — structural (69.2%)
--- pretty-v2.1.32.js:553431
+++ pretty-v2.1.33.js:548672
@@ -1,16 +1,4 @@
 var Vfq = v(() => {
   d1();
-  x7();
-  u1();
-  Q8();
-  K2();
-  FA();
-  a6();
-  k6();
-  _6();
-  Zfq();
-  Nd();
-  dO();
-  R8();
   oR = a($1(), 1);
 });

@@@ variable 'DFA' (was 'jNq') — structural (69.2%)
--- pretty-v2.1.32.js:559570
+++ pretty-v2.1.33.js:548729
@@ -1,11 +1,4 @@
 var jNq = v(() => {
   u1();
-  _Nq();
-  XNq();
-  Q8();
-  PZ();
-  RX();
-  IB();
-  xB();
   B91 = a($1(), 1);
 });

@@@ variable 'fWq' (was 'hNq') — structural (69.2%)
--- pretty-v2.1.32.js:559825
+++ pretty-v2.1.33.js:549558
@@ -5,7 +5,5 @@
   FA();
   F6();
   u1();
-  $w();
-  hq();
   jc = a($1(), 1);
 });

@@@ function 'hd4' (was 'Ld4') — structural (69.0%)
--- pretty-v2.1.32.js:420427
+++ pretty-v2.1.33.js:418887
@@ -1,21 +1,6 @@
 function Ld4(A, q, { verbose: K }) {
   let Y = typeof A === "string" ? JA(A) : A;
-  if ("routing" in Y && Y.routing) {
-    let { summary: z, content: w } = Y.routing;
-    if (K && w)
-      return oh.default.createElement(
-        HA,
-        null,
-        oh.default.createElement(f, null, w),
-      );
-    return oh.default.createElement(
-      HA,
-      null,
-      oh.default.createElement(f, null, z),
-      oh.default.createElement(f, null, " "),
-      oh.default.createElement(sT, null),
-    );
-  }
+  if ("routing" in Y && Y.routing) return null;
   if ("request_id" in Y && "target" in Y) return null;
   return oh.default.createElement(
     HA,

@@@ function 'BFA' (was 'JFA') — structural (68.4%)
--- pretty-v2.1.32.js:554414
+++ pretty-v2.1.33.js:553575
@@ -2,8 +2,9 @@
   return !1;
   switch (A) {
     case "feedback_survey_bad":
+      return !0;
     case "feedback_survey_good":
-      return !0;
+      return !1;
     default:
       return !1;
   }

@@@ variable 'YG' (was 'dP') — structural (68.4%)
--- pretty-v2.1.32.js:446666
+++ pretty-v2.1.33.js:446787
@@ -38,7 +38,6 @@
   iD();
   ah();
   Ns4();
-  I6();
   MG6 = class MG6 extends Error {
     serverName;
     constructor(A, q) {
@@ -102,48 +101,50 @@
       } else if (q.type === "ws-ide") {
         let S = Ke6(),
           m = {
-            headers: {
-              "User-Agent": qn(),
-              ...(q.authToken && {
-                "X-Claude-Code-Ide-Authorization": q.authToken,
-              }),
-            },
-            agent: BA1(q.url),
-            ...(S || {}),
+            "User-Agent": Rn(),
+            ...(q.authToken && {
+              "X-Claude-Code-Ide-Authorization": q.authToken,
+            }),
           },
-          b = new qx1.default(
-            q.url,
-            ["mcp"],
-            Object.keys(m).length > 0 ? m : void 0,
-          );
+          x;
+        if (typeof Bun < "u")
+          x = new globalThis.WebSocket(q.url, {
+            protocols: ["mcp"],
+            headers: m,
+            proxy: uA1(q.url),
+            tls: S || void 0,
+          });
+        else
+          x = await Jt4(q.url, { headers: m, agent: bA1(q.url), ...(S || {}) });
         z = new WP6(b);
       } else if (q.type === "ws") {
         SA(A, `Initializing WebSocket transport to ${q.url}`);
         let S = await CP6(A, q),
           m = Ke6(),
           b = {
-            headers: {
-              "User-Agent": qn(),
-              ...(w && { Authorization: `Bearer ${w}` }),
-              ...S,
-            },
-            agent: BA1(q.url),
-            ...(m || {}),
+            "User-Agent": Rn(),
+            ...(w && { Authorization: `Bearer ${w}` }),
+            ...S,
           },
           U = Object.fromEntries(
-            Object.entries(b.headers).map(([x, p]) =>
+            Object.entries(x).map(([B, p]) =>
               x.toLowerCase() === "authorization" ? [x, "[REDACTED]"] : [x, p],
             ),
           );
         SA(
           A,
           `WebSocket transport options: ${g1({ url: q.url, headers: U, hasSessionAuth: !!w })}`,
-        );
-        let g = new qx1.default(
-          q.url,
-          ["mcp"],
-          Object.keys(b).length > 0 ? b : void 0,
         );
+        let U;
+        if (typeof Bun < "u")
+          U = new globalThis.WebSocket(q.url, {
+            protocols: ["mcp"],
+            headers: x,
+            proxy: uA1(q.url),
+            tls: m || void 0,
+          });
+        else
+          U = await Jt4(q.url, { headers: x, agent: bA1(q.url), ...(m || {}) });
         z = new WP6(g);
       } else if (q.type === "http") {
         (SA(A, `Initializing HTTP transport to ${q.url}`),
@@ -254,10 +255,10 @@
                 "report the issue at https://github.com/anthropics/claude-code/issues",
               PACKAGE_URL: "@anthropic-ai/claude-code",
               README_URL: "https://code.claude.com/docs/en/overview",
-              VERSION: "2.1.32",
+              VERSION: "2.1.33",
               FEEDBACK_CHANNEL:
                 "https://github.com/anthropics/claude-code/issues",
-              BUILD_TIME: "2026-02-05T17:02:01Z",
+              BUILD_TIME: "2026-02-06T00:14:56Z",
             }.VERSION ?? "unknown",
         },
         { capabilities: { roots: {}, ...{} } },

@@@ variable 'fb1' (was 'kg1') — structural (68.4%)
--- pretty-v2.1.32.js:442300
+++ pretty-v2.1.33.js:254508
@@ -5,6 +5,11 @@
   _6();
   iQ();
   lU();
+  HG();
+  Dq1();
+  H0();
+  JH();
+  MF7 = ["user", "project", "local"];
   G51 = qA(async () => {
     let { enabled: A, errors: q } = await uY(),
       K = [];

@@@ function 'p8' (was 'F8') — structural (68.2%)
--- pretty-v2.1.32.js:147595
+++ pretty-v2.1.33.js:34159
@@ -1,5 +1,5 @@
 function F8() {
   if (!$6(process.env.CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS)) return !1;
-  if (!x8("tengu_amber_flint", !1)) return !1;
+  if (!Q8("tengu_amber_flint", !0)) return !1;
   return !0;
 }

@@@ function 'wzz' (was 'L5z') — structural (67.6%)
--- pretty-v2.1.32.js:523379
+++ pretty-v2.1.33.js:524296
@@ -1,5 +1,8 @@
-function L5z() {
-  let A = cv4();
+async function wzz() {
+  let { initializeTelemetry: A } = await Promise.resolve().then(
+      () => (OVA(), $VA),
+    ),
+    q = A();
   if (A)
     uE6(A, (K, Y) => {
       let z = A?.createCounter(K, Y);

@@@ function 'G2z' (was 'UYz') — structural (67.6%)
--- pretty-v2.1.32.js:530230
+++ pretty-v2.1.33.js:528626
@@ -1,20 +1,18 @@
 function UYz() {
-  let A = A1(4),
-    q = tK1("responding", z_q, !0, !1),
+  let A = q1(7),
+    [q, K] = Dm1("responding", ZJq, !0, !1),
     K;
   if (A[0] !== q)
-    ((K = z_q
-      .split("")
-      .map((z, w) =>
-        iM.default.createElement(Gm1, {
-          key: w,
-          char: z,
-          index: w,
-          glimmerIndex: q,
-          messageColor: "inactive",
-          shimmerColor: "text",
-        }),
-      )),
+    ((Y = ZJq.split("").map((H, $) =>
+      XM.default.createElement(GVA, {
+        key: $,
+        char: H,
+        index: $,
+        glimmerIndex: K,
+        messageColor: "inactive",
+        shimmerColor: "text",
+      }),
+    )),
       (A[0] = q),
       (A[1] = K));
   else K = A[1];
@@ -22,5 +20,12 @@
   if (A[2] !== K)
     ((Y = iM.default.createElement(f, null, K)), (A[2] = K), (A[3] = Y));
   else Y = A[3];
+  let w;
+  if (A[4] !== q || A[5] !== z)
+    ((w = XM.default.createElement(I, { ref: q }, z)),
+      (A[4] = q),
+      (A[5] = z),
+      (A[6] = w));
+  else w = A[6];
   return Y;
 }

@@@ function 'zc8' (was '$08') — structural (67.4%)
--- pretty-v2.1.32.js:76417
+++ pretty-v2.1.33.js:112179
@@ -28,6 +28,8 @@
         "Stop",
         "SubagentStop",
         "PreCompact",
+        "TeammateIdle",
+        "TaskCompleted",
       ]),
     };
   for (let w of Object.keys(q))

@@@ function 'dMz' (was '_Xz') — structural (67.4%)
--- pretty-v2.1.32.js:568964
+++ pretty-v2.1.33.js:570263
@@ -4,16 +4,23 @@
     A.length === 1 &&
     (A[0] === "--version" || A[0] === "-v" || A[0] === "-V")
   ) {
-    (Vq("cli_version_fast_path"),
-      console.log(
-        `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION} (Claude Code)`,
-      ));
+    console.log(
+      `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.33", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-06T00:14:56Z" }.VERSION} (Claude Code)`,
+    );
     return;
   }
-  if (A[0] === "--mcp-cli" && RH()) {
-    let Y = A.slice(1),
-      { mcpCliMain: z } = await Promise.resolve().then(() => (wOq(), zOq));
-    process.exit(await z(Y));
+  let { profileCheckpoint: q } = await Promise.resolve().then(
+    () => (Hl(), tdA),
+  );
+  if ((q("cli_entry"), A[0] === "--mcp-cli")) {
+    let { isMcpCliEnabled: w } = await Promise.resolve().then(
+      () => (sD(), vOq),
+    );
+    if (w()) {
+      let H = A.slice(1),
+        { mcpCliMain: $ } = await Promise.resolve().then(() => (tOq(), sOq));
+      process.exit(await $(H));
+    }
   }
   if (A[0] === "--ripgrep") {
     Vq("cli_ripgrep_path");
@@ -23,15 +30,24 @@
     return;
   }
   if (process.argv[2] === "--claude-in-chrome-mcp") {
-    (Vq("cli_claude_in_chrome_mcp_path"), await vHq());
+    q("cli_claude_in_chrome_mcp_path");
+    let { runClaudeInChromeMcpServer: w } = await Promise.resolve().then(
+      () => (z_q(), Y_q),
+    );
+    await w();
     return;
   } else if (process.argv[2] === "--chrome-native-host") {
-    (Vq("cli_chrome_native_host_path"), await yHq());
+    q("cli_chrome_native_host_path");
+    let { runChromeNativeHost: w } = await Promise.resolve().then(
+      () => (X_q(), J_q),
+    );
+    await w();
     return;
   }
   let q = A.includes("--tmux") || A.includes("--tmux=classic");
   if (A.length === 1 && (A[0] === "--update" || A[0] === "--upgrade"))
     process.argv = [process.argv[0], process.argv[1], "update"];
+  let { startCapturingEarlyInput: Y } = await Promise.resolve().then(() => KA7);
   (pW7(), Vq("cli_before_main_import"));
   let { main: K } = await Promise.resolve().then(() => (qvq(), Avq));
   (Vq("cli_after_main_import"), await K(), Vq("cli_after_main_complete"));

@@@ function 'fA6' (was 'aa8') — structural (67.3%)
--- pretty-v2.1.32.js:138025
+++ pretty-v2.1.33.js:110864
@@ -1,16 +1,22 @@
 function aa8() {
   let A = bQ(),
     q = ca8();
-  if (A) {
+  if (ZA6 !== void 0) (iA.interceptors.request.eject(ZA6), (ZA6 = void 0));
+  if (
+    ((iA.defaults.proxy = void 0),
+    (iA.defaults.httpAgent = void 0),
+    (iA.defaults.httpsAgent = void 0),
+    A)
+  ) {
     rA.defaults.proxy = !1;
     let K = ra8(A);
-    (rA.interceptors.request.use((Y) => {
+    ((ZA6 = iA.interceptors.request.use((Y) => {
       if (Y.url && sk1(Y.url))
         if (q) ((Y.httpsAgent = q), (Y.httpAgent = q));
         else (delete Y.httpsAgent, delete Y.httpAgent);
       else ((Y.httpsAgent = K), (Y.httpAgent = K));
       return Y;
-    }),
+    })),
       bA6(oa8(A)));
   } else if (q) {
     rA.defaults.httpsAgent = q;

@@@ function 'w46' (was 'k86') — structural (66.7%)
--- pretty-v2.1.32.js:147107
+++ pretty-v2.1.33.js:132400
@@ -1,6 +1,4 @@
 function k86() {
   if (x8("tengu_marble_lantern_disabled", !1)) return { hasAccess: !1 };
-  if (s7() !== "firstParty")
-    return { hasAccess: !x8("tengu_marble_lantern_3p_disabled", !1) };
   return { hasAccess: !U8() };
 }

@@@ function '_51' (was 'j51') — structural (66.7%)
--- pretty-v2.1.32.js:438556
+++ pretty-v2.1.33.js:436442
@@ -24,18 +24,26 @@
       { title: _, branchName: J } = await quY(K || q || "Background task", Y);
     if (H) {
       let [u, S] = H.split("/");
-      if (u && S)
-        ((O = {
-          type: "git_repository",
-          url: `https://github.com/${u}/${S}`,
-          revision: A.branchName,
-        }),
+      if (u && S) {
+        let m = A.branchName ?? (await TW()) ?? void 0;
+        (h(
+          `[teleportToRemote] Git source: ${u}/${S}, revision: ${m ?? "none"}`,
+        ),
+          ($ = {
+            type: "git_repository",
+            url: `https://github.com/${u}/${S}`,
+            revision: m,
+          }),
           ($ = {
             type: "git_repository",
             git_info: { type: "github", repo: `${u}/${S}`, branches: [J] },
           }));
-      else K1(Error(`Invalid repository format: ${H} - expected 'owner/name'`));
-    }
+      } else
+        K1(Error(`Invalid repository format: ${H} - expected 'owner/name'`));
+    } else
+      h(
+        "[teleportToRemote] No repository detected — session will have an empty sandbox",
+      );
     let X = await uG1();
     if (!X || X.length === 0)
       return (

@@@ function 'z5z' (was 'uqz') — structural (66.1%)
--- pretty-v2.1.32.js:516233
+++ pretty-v2.1.33.js:516353
@@ -1,54 +1,55 @@
 function uqz(A) {
-  let K = `Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits (with the exception of the plan file mentioned below), run any non-readonly tools (including changing configs or making commits), or otherwise make any changes to the system. This supercedes any other instructions you have received.
+  let q = A.planExists
+      ? `A plan file already exists at ${A.planFilePath}. You can read it and make incremental edits using the ${kG.name} tool.`
+      : `No plan file exists yet. You should create your plan at ${A.planFilePath} using the ${SG.name} tool.`,
+    K = `You can use the ${Jv.agentType} agent type to parallelize complex searches without filling your context, though for straightforward queries direct tools are simpler.`,
+    Y = `Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits (with the exception of the plan file mentioned below), run any non-readonly tools (including changing configs or making commits), or otherwise make any changes to the system. This supercedes any other instructions you have received.
 
 ## Plan File Info:
-${A.planExists ? `A plan file already exists at ${A.planFilePath}. You can read it and make incremental edits using the ${MG.name} tool.` : `No plan file exists yet. You should create your plan at ${A.planFilePath} using the ${fG.name} tool.`}
+${q}
 
 ## Iterative Planning Workflow
 
-Your goal is to build a comprehensive plan through iterative refinement and interviewing the user. Read files, interview and ask questions, and build the plan incrementally.
+You are pair-planning with the user. Explore the code to build context, ask the user questions when you hit decisions you can't make alone, and write your findings into the plan file as you go. The plan file (above) is the ONLY file you may edit — it starts as a rough skeleton and gradually becomes the final plan.
 
-### How to Work
+### The Loop
 
-0. Write your plan in the plan file specified above. This is the ONLY file you are allowed to edit.
+Repeat this cycle until the plan is complete:
 
-1. **Explore the codebase**: Use ${bqz()} tools to understand the codebase. Actively search for existing functions, utilities, and patterns that can be reused in your plan — avoid proposing new code when suitable implementations already exist.
-You can use the ${Yv.agentType} agent type to parallelize complex searches without filling your context, though for straightforward queries direct tools are simpler.
+1. **Explore** — Use ${Y5z()} to read code. Look for existing functions, utilities, and patterns to reuse. ${K}
+2. **Update the plan file** — After each discovery, immediately capture what you learned. Don't wait until the end.
+3. **Ask the user** — When you hit an ambiguity or decision you can't resolve from code alone, use ${OH}. Then go back to step 1.
 
-2. **Interview the user**: Use ${kw} to interview the user and ask questions that:
-   - Clarify ambiguous requirements
-   - Get user input on technical decisions and tradeoffs
-   - Understand preferences for UI/UX, performance, edge cases
-   - Validate your understanding before committing to an approach
-   Make sure to:
-   - Not ask any questions that you could find out yourself by exploring the codebase.
-   - Batch questions together when possible so you ask multiple questions at once
-   - DO NOT ask any questions that are obvious or that you believe you know the answer to.
+### First Turn
 
-3. **Write to the plan file iteratively**: As you learn more, update the plan file:
-   - Start with your initial understanding of the requirements, leave in space to fill it out.
-   - Add sections as you explore and learn about the codebase
-   - Refine based on user answers to your questions
-   - The plan file is your working document - edit it as your understanding evolves
+Start by quickly scanning a few key files to form an initial understanding of the task scope. Then write a skeleton plan (headers and rough notes) and ask the user your first round of questions. Don't explore exhaustively before engaging the user.
 
-4. **Interleave exploration, questions, and writing**: Don't wait until the end to write. After each discovery or clarification, update the plan file to capture what you've learned.
+### Asking Good Questions
 
-5. **Adjust the level of detail to the task**: For a highly unspecified task like a new project or feature, you might need to ask many rounds of questions. Whereas for a smaller task you may need only some or a few.
+- Never ask what you could find out by reading the code
+- Batch related questions together (use multi-question ${OH} calls)
+- Focus on things only the user can answer: requirements, preferences, tradeoffs, edge case priorities
+- Scale depth to the task — a vague feature request needs many rounds; a focused bug fix may need one or none
 
 ### Plan File Structure
 Your plan file should be divided into clear sections using markdown headers, based on the request. Fill out these sections as you go.
+- Begin with a **Context** section: explain why this change is being made — the problem or need it addresses, what prompted it, and the intended outcome
 - Include only your recommended approach, not all alternatives
 - Ensure that the plan file is concise enough to scan quickly, but detailed enough to execute effectively
 - Include the paths of critical files to be modified
 - Reference existing functions and utilities you found that should be reused, with their file paths
 - Include a verification section describing how to test the changes end-to-end (run the code, use MCP tools, run tests)
 
+### When to Converge
+
+Your plan is ready when you've addressed all ambiguities and it covers: what to change, which files to modify, what existing code to reuse (with file paths), and how to verify the changes. Call ${qM.name} when the plan is ready for approval.
+
 ### Ending Your Turn
 
 Your turn should only end by either:
 - Using ${kw} to gather more information
 - Calling ${QM.name} when the plan is ready for approval
 
-**Important:**: Use ${QM.name} to request plan approval. Do NOT ask about plan approval via text or AskUserQuestion.`;
+**Important:** Use ${qM.name} to request plan approval. Do NOT ask about plan approval via text or AskUserQuestion.`;
   return j9([p6({ content: K, isMeta: !0 })]);
 }

@@@ function 'oK5' (was 'tXK') — structural (65.7%)
--- pretty-v2.1.32.js:76459
+++ pretty-v2.1.33.js:112223
@@ -9,8 +9,28 @@
       z = new Set();
     for (let w of pl()) {
       if (w === "policySettings") {
-        let J = f7("policySettings");
-        if (J) q = ar1(q, J, K08);
+        let J = RA6();
+        if (J && Object.keys(J).length > 0) {
+          let X = cE.safeParse(J);
+          if (X.success) q = VV1(q, X.data, _e6);
+          else {
+            let D = Xa1(X.error, "remote managed settings");
+            for (let M of D) {
+              let j = `${M.file}:${M.path}:${M.message}`;
+              if (!Y.has(j)) (Y.add(j), K.push(M));
+            }
+          }
+        } else {
+          let X = Pw(w);
+          if (X) {
+            let { settings: D, errors: M } = yA6(X);
+            for (let j of M) {
+              let W = `${j.file}:${j.path}:${j.message}`;
+              if (!Y.has(W)) (Y.add(W), K.push(j));
+            }
+            if (D) q = VV1(q, D, _e6);
+          }
+        }
         continue;
       }
       let H = OH(w);

@@@ function 'PCY' (was 'TyY') — structural (65.7%)
--- pretty-v2.1.32.js:425973
+++ pretty-v2.1.33.js:423221
@@ -1,10 +1,10 @@
-async function TyY(A, q) {
+async function PCY(A, q, K) {
   if (q === "session_memory" || q === "compact") return !1;
   if (!Md()) return !1;
   let K = mL(A),
-    Y = rm1(),
-    z = A51();
+    z = EF1(q),
+    w = n31(q);
   h(`autocompact: tokens=${K} threshold=${Y} effectiveWindow=${z}`);
-  let { isAboveAutoCompactThreshold: w } = jd(K);
+  let { isAboveAutoCompactThreshold: H } = Md(Y, q);
   return w;
 }

@@@ function 'ZMz' (was 'VTq') — structural (65.4%)
--- pretty-v2.1.32.js:563193
+++ pretty-v2.1.33.js:567192
@@ -1,6 +1,6 @@
 async function VTq() {
   (c("tengu_update_check", {}),
-    k4(`Current version: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION}
+    h4(`Current version: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.33", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-06T00:14:56Z" }.VERSION}
 `));
   let A = jq()?.autoUpdatesChannel ?? "latest";
   (k4(`Checking for updates to ${A} version...
@@ -92,16 +92,16 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.32",
+            VERSION: "2.1.33",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-02-05T17:02:01Z",
+            BUILD_TIME: "2026-02-06T00:14:56Z",
           }.VERSION,
           J,
           { loose: !0 },
         )
       )
-        (k4(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION} → ${J}
+        (h4(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.33", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-06T00:14:56Z" }.VERSION} → ${J}
 `),
           k4(`
 `),
@@ -127,16 +127,16 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.32",
+            VERSION: "2.1.33",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-02-05T17:02:01Z",
+            BUILD_TIME: "2026-02-06T00:14:56Z",
           }.VERSION,
           J,
           { loose: !0 },
         )
       )
-        (k4(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION} → ${J}
+        (h4(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.33", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-06T00:14:56Z" }.VERSION} → ${J}
 `),
           k4(`
 `),
@@ -162,16 +162,16 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.32",
+            VERSION: "2.1.33",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-02-05T17:02:01Z",
+            BUILD_TIME: "2026-02-06T00:14:56Z",
           }.VERSION,
           J,
           { loose: !0 },
         )
       )
-        (k4(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION} → ${J}
+        (h4(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.33", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-06T00:14:56Z" }.VERSION} → ${J}
 `),
           k4(`
 `),
@@ -253,14 +253,14 @@
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.32",
+          VERSION: "2.1.33",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-02-05T17:02:01Z",
+          BUILD_TIME: "2026-02-06T00:14:56Z",
         }.VERSION
       )
         k4(
           Y6.green(
-            `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION})`,
+            `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.33", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-06T00:14:56Z" }.VERSION})`,
           ) +
             `
 `,
@@ -268,7 +268,7 @@
       else
         (k4(
           Y6.green(
-            `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION} to version ${_.latestVersion}`,
+            `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.33", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-06T00:14:56Z" }.VERSION} to version ${_.latestVersion}`,
           ) +
             `
 `,
@@ -291,10 +291,10 @@
   if (K.installMethod !== "native") await zU1();
   (h("update: Checking npm registry for latest version"),
     h(
-      `update: Package URL: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.PACKAGE_URL}`,
+      `update: Package URL: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.33", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-06T00:14:56Z" }.PACKAGE_URL}`,
     ));
   let Y = A === "stable" ? "stable" : "latest",
-    z = `npm view ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.PACKAGE_URL}@${Y} version`;
+    z = `npm view ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.33", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-06T00:14:56Z" }.PACKAGE_URL}@${Y} version`;
   h(`update: Running: ${z}`);
   let w = await w31(A);
   if ((h(`update: Latest version from npm: ${w || "FAILED"}`), !w)) {
@@ -322,18 +322,18 @@
           "report the issue at https://github.com/anthropics/claude-code/issues",
         PACKAGE_URL: "@anthropic-ai/claude-code",
         README_URL: "https://code.claude.com/docs/en/overview",
-        VERSION: "2.1.32",
+        VERSION: "2.1.33",
         FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-        BUILD_TIME: "2026-02-05T17:02:01Z",
+        BUILD_TIME: "2026-02-06T00:14:56Z",
       }.PACKAGE_URL &&
         !{
           ISSUES_EXPLAINER:
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.32",
+          VERSION: "2.1.33",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-02-05T17:02:01Z",
+          BUILD_TIME: "2026-02-06T00:14:56Z",
         }.PACKAGE_URL.startsWith("@anthropic"))
     )
       process.stderr.write(`  • Internal/development build not published to npm
@@ -352,9 +352,9 @@
           "report the issue at https://github.com/anthropics/claude-code/issues",
         PACKAGE_URL: "@anthropic-ai/claude-code",
         README_URL: "https://code.claude.com/docs/en/overview",
-        VERSION: "2.1.32",
+        VERSION: "2.1.33",
         FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-        BUILD_TIME: "2026-02-05T17:02:01Z",
+        BUILD_TIME: "2026-02-06T00:14:56Z",
       }.PACKAGE_URL || "@anthropic-ai/claude-code";
     (process.stderr.write(`  • Manually check: npm view ${_} version
 `),
@@ -369,20 +369,20 @@
         "report the issue at https://github.com/anthropics/claude-code/issues",
       PACKAGE_URL: "@anthropic-ai/claude-code",
       README_URL: "https://code.claude.com/docs/en/overview",
-      VERSION: "2.1.32",
+      VERSION: "2.1.33",
       FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-      BUILD_TIME: "2026-02-05T17:02:01Z",
+      BUILD_TIME: "2026-02-06T00:14:56Z",
     }.VERSION
   )
     (k4(
       Y6.green(
-        `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION})`,
+        `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.33", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-06T00:14:56Z" }.VERSION})`,
       ) +
         `
 `,
     ),
       await $K(0));
-  (k4(`New version available: ${w} (current: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION})
+  (h4(`New version available: ${w} (current: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.33", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-06T00:14:56Z" }.VERSION})
 `),
     k4(`Installing update...
 `));
@@ -429,7 +429,7 @@
     case "success":
       (k4(
         Y6.green(
-          `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION} to version ${w}`,
+          `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.33", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-06T00:14:56Z" }.VERSION} to version ${w}`,
         ) +
           `
 `,
@@ -445,7 +445,7 @@
         (process.stderr.write(`Try manually updating with:
 `),
           process.stderr
-            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.PACKAGE_URL}
+            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.33", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-06T00:14:56Z" }.PACKAGE_URL}
 `));
       else
         (process.stderr.write(`Try running with sudo or fix npm permissions
@@ -464,7 +464,7 @@
         (process.stderr.write(`Try manually updating with:
 `),
           process.stderr
-            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.PACKAGE_URL}
+            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.33", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-06T00:14:56Z" }.PACKAGE_URL}
 `));
       else
         process.stderr

@@@ function 'vO9' (was 'xQ1') — structural (65.2%)
--- pretty-v2.1.32.js:423260
+++ pretty-v2.1.33.js:232403
@@ -1,3 +1,7 @@
 function xQ1() {
-  return `/tmp/claude-mcp-browser-bridge-${ELA()}`;
+  return `
+
+[OUTPUT TRUNCATED - exceeded ${Fw6()} token limit]
+
+The tool output was truncated. If this MCP server provides pagination or filtering tools, use them to retrieve specific portions of the data. If pagination is not available, inform the user that you are working with truncated output and results may be incomplete.`;
 }

@@@ function 'PU1' (was 'hRY') — structural (65.2%)
--- pretty-v2.1.32.js:423281
+++ pretty-v2.1.33.js:440279
@@ -1,3 +1,3 @@
 function hRY() {
-  return `claude-mcp-browser-bridge-${ELA()}`;
+  return `/tmp/claude-mcp-browser-bridge-${ACA()}`;
 }

@@@ function 'smY' (was 'PmY') — structural (65.2%)
--- pretty-v2.1.32.js:443661
+++ pretty-v2.1.33.js:440300
@@ -1,7 +1,3 @@
 function PmY() {
-  return `
-
-[OUTPUT TRUNCATED - exceeded ${XP6()} token limit]
-
-The tool output was truncated. If this MCP server provides pagination or filtering tools, use them to retrieve specific portions of the data. If pagination is not available, inform the user that you are working with truncated output and results may be incomplete.`;
+  return `claude-mcp-browser-bridge-${ACA()}`;
 }

@@@ function 'rs' (was 'Yt') — structural (64.4%)
--- pretty-v2.1.32.js:420938
+++ pretty-v2.1.33.js:419386
@@ -21,7 +21,7 @@
     ...(bd4 ? [bd4] : []),
     ...(ud4 ? [ud4] : []),
     tkA,
-    ...(F8() ? [rLY(), oLY()] : []),
+    ...(p8() ? [$yY(), OyY(), _yY()] : []),
     ...(xd4 ? [xd4] : []),
     ...(Id4 ? [Id4] : []),
     zd,

@@@ function 'XP1' (was 'fP1') — structural (63.6%)
--- pretty-v2.1.32.js:511387
+++ pretty-v2.1.33.js:511413
@@ -1,8 +1,8 @@
 function fP1(A) {
   if (A.type !== "prompt") return A.description;
   if (A.source === "plugin") {
-    if (A.pluginInfo?.repository)
-      return `${A.description} (plugin:${A.pluginInfo.repository})`;
+    let q = A.pluginInfo?.pluginManifest.name;
+    if (q) return `(${q}) ${A.description}`;
     return `${A.description} (plugin)`;
   }
   if (A.source === "builtin" || A.source === "mcp") return A.description;

@@@ function 'bBA' (was 'HBA') — structural (62.9%)
--- pretty-v2.1.32.js:523375
+++ pretty-v2.1.33.js:524292
@@ -1,4 +1,4 @@
-function HBA() {
+async function bBA() {
   if (NOq) return;
-  ((NOq = !0), L5z());
+  ((N_q = !0), await wzz());
 }

@@@ function 'lMq' (was 'GDq') — structural (62.8%)
--- pretty-v2.1.32.js:546563
+++ pretty-v2.1.33.js:545742
@@ -18,7 +18,7 @@
             return { ...X, selectedIPAgentIndex: -1 };
           return { ...X, selectedIPAgentIndex: -1, viewSelectionMode: "none" };
         }
-        let M = X.showSpinnerTree ? j : j - 1;
+        let j = X.expandedView === "teammates" ? M : M - 1;
         if (j > 0 && X.selectedIPAgentIndex > M)
           return { ...X, selectedIPAgentIndex: M };
         return X;
@@ -51,16 +51,13 @@
       z((D) => {
         let M = tN6(D.tasks).length;
         if (M === 0) return D;
-        if (!D.showSpinnerTree)
-          return (
-            OA((G) => ({ ...G, showSpinnerTree: !0 })),
-            {
-              ...D,
-              showSpinnerTree: !0,
-              viewSelectionMode: "selecting-agent",
-              selectedIPAgentIndex: -1,
-            }
-          );
+        if (D.expandedView !== "teammates")
+          return {
+            ...D,
+            expandedView: "teammates",
+            viewSelectionMode: "selecting-agent",
+            selectedIPAgentIndex: -1,
+          };
         let W;
         if (D.selectedIPAgentIndex === 0) W = -1;
         else if (D.selectedIPAgentIndex === -1) W = M;
@@ -77,16 +74,13 @@
       z((D) => {
         let M = tN6(D.tasks).length;
         if (M === 0) return D;
-        if (!D.showSpinnerTree)
-          return (
-            OA((P) => ({ ...P, showSpinnerTree: !0 })),
-            {
-              ...D,
-              showSpinnerTree: !0,
-              viewSelectionMode: "selecting-agent",
-              selectedIPAgentIndex: -1,
-            }
-          );
+        if (D.expandedView !== "teammates")
+          return {
+            ...D,
+            expandedView: "teammates",
+            viewSelectionMode: "selecting-agent",
+            selectedIPAgentIndex: -1,
+          };
         let W = M,
           G = D.selectedIPAgentIndex >= W ? -1 : D.selectedIPAgentIndex + 1;
         return {
@@ -105,13 +99,12 @@
     if (X.return && q === "selecting-agent") {
       if (Y === -1) jI(z);
       else if (Y >= O)
-        (OA((D) => ({ ...D, showSpinnerTree: !1 })),
-          z((D) => ({
-            ...D,
-            showSpinnerTree: !1,
-            viewSelectionMode: "none",
-            selectedIPAgentIndex: -1,
-          })));
+        z((D) => ({
+          ...D,
+          expandedView: "none",
+          viewSelectionMode: "none",
+          selectedIPAgentIndex: -1,
+        }));
       else {
         let D = _();
         if (D) tt(D.taskId, z);

@@@ variable 'Gz8' (was 'wX8') — structural (62.8%)
--- pretty-v2.1.32.js:73186
+++ pretty-v2.1.33.js:45078
@@ -13,5 +13,7 @@
     "PreCompact",
     "PermissionRequest",
     "Setup",
+    "TeammateIdle",
+    "TaskCompleted",
   ];
 });

@@@ function 'zJ6' (was 'MWA') — structural (62.7%)
--- pretty-v2.1.32.js:312488
+++ pretty-v2.1.33.js:310743
@@ -1,4 +1,5 @@
 function MWA(A) {
+  if (Qu1 !== void 0) (clearTimeout(Qu1), (Qu1 = void 0));
   try {
     process.exit(A);
   } catch (q) {

@@@ class 'dmA' (was 'VmA') — structural (61.4%)
--- pretty-v2.1.32.js:545260
+++ pretty-v2.1.33.js:543703
@@ -14,7 +14,7 @@
     this.accessToken = K;
     this.callbacks = Y;
   }
-  connect() {
+  async connect() {
     if (this.state === "connecting") {
       h("[SessionsWebSocket] Already connecting");
       return;
@@ -23,35 +23,61 @@
     let q = `${D4().BASE_API_URL.replace("https://", "wss://")}/v1/sessions/ws/${this.sessionId}/subscribe?organization_uuid=${this.orgUuid}`;
     h(`[SessionsWebSocket] Connecting to ${q}`);
     let K = {
-        Authorization: `Bearer ${this.accessToken}`,
-        "anthropic-version": "2023-06-01",
-      },
-      Y =
-        typeof Bun < "u"
-          ? { headers: K, proxy: uA6(q) }
-          : { headers: K, agent: BA1(q) };
-    ((this.ws = new FP(q, Y)),
-      this.ws.on("open", () => {
-        (h("[SessionsWebSocket] Connection opened, authenticated via headers"),
-          (this.state = "connected"),
-          (this.reconnectAttempts = 0),
-          this.startPingInterval(),
-          this.callbacks.onConnected?.());
-      }),
-      this.ws.on("message", (z) => {
-        this.handleMessage(z.toString());
-      }),
-      this.ws.on("error", (z) => {
-        (K1(Error(`[SessionsWebSocket] Error: ${z.message}`)),
-          this.callbacks.onError?.(z));
-      }),
-      this.ws.on("close", (z, w) => {
-        (h(`[SessionsWebSocket] Closed: code=${z} reason=${w.toString()}`),
-          this.handleClose());
-      }),
-      this.ws.on("pong", () => {
-        h("[SessionsWebSocket] Pong received");
-      }));
+      Authorization: `Bearer ${this.accessToken}`,
+      "anthropic-version": "2023-06-01",
+    };
+    if (typeof Bun < "u") {
+      let Y = new globalThis.WebSocket(q, { headers: K, proxy: uA1(q) });
+      ((this.ws = Y),
+        Y.addEventListener("open", () => {
+          (h(
+            "[SessionsWebSocket] Connection opened, authenticated via headers",
+          ),
+            (this.state = "connected"),
+            (this.reconnectAttempts = 0),
+            this.startPingInterval(),
+            this.callbacks.onConnected?.());
+        }),
+        Y.addEventListener("message", (z) => {
+          let w = typeof z.data === "string" ? z.data : String(z.data);
+          this.handleMessage(w);
+        }),
+        Y.addEventListener("error", () => {
+          let z = Error("[SessionsWebSocket] WebSocket error");
+          (K1(z), this.callbacks.onError?.(z));
+        }),
+        Y.addEventListener("close", (z) => {
+          (h(`[SessionsWebSocket] Closed: code=${z.code} reason=${z.reason}`),
+            this.handleClose());
+        }));
+    } else {
+      let { default: Y } = await Promise.resolve().then(() => (FU1(), BP6)),
+        z = new Y(q, { headers: K, agent: bA1(q) });
+      ((this.ws = z),
+        z.on("open", () => {
+          (h(
+            "[SessionsWebSocket] Connection opened, authenticated via headers",
+          ),
+            (this.state = "connected"),
+            (this.reconnectAttempts = 0),
+            this.startPingInterval(),
+            this.callbacks.onConnected?.());
+        }),
+        z.on("message", (w) => {
+          this.handleMessage(w.toString());
+        }),
+        z.on("error", (w) => {
+          (K1(Error(`[SessionsWebSocket] Error: ${w.message}`)),
+            this.callbacks.onError?.(w));
+        }),
+        z.on("close", (w, H) => {
+          (h(`[SessionsWebSocket] Closed: code=${w} reason=${H.toString()}`),
+            this.handleClose());
+        }),
+        z.on("pong", () => {
+          h("[SessionsWebSocket] Pong received");
+        }));
+    }
   }
   handleMessage(A) {
     try {
@@ -88,13 +114,13 @@
       (h("[SessionsWebSocket] Not reconnecting"), this.callbacks.onClose?.());
   }
   startPingInterval() {
-    (this.stopPingInterval(),
-      (this.pingInterval = setInterval(() => {
-        if (this.ws && this.state === "connected")
-          try {
-            this.ws.ping();
-          } catch {}
-      }, PHz)));
+    if ((this.stopPingInterval(), typeof Bun < "u")) return;
+    this.pingInterval = setInterval(() => {
+      if (this.ws && this.state === "connected")
+        try {
+          this.ws.ping();
+        } catch {}
+    }, i$z);
   }
   stopPingInterval() {
     if (this.pingInterval)
@@ -127,8 +153,7 @@
       this.reconnectTimer)
     )
       (clearTimeout(this.reconnectTimer), (this.reconnectTimer = null));
-    if (this.ws)
-      (this.ws.removeAllListeners(), this.ws.close(), (this.ws = null));
+    if (this.ws) (this.ws.close(), (this.ws = null));
   }
   reconnect() {
     (h("[SessionsWebSocket] Force reconnecting"),

@@@ function 'eP9' (was 'WvA') — structural (61.3%)
--- pretty-v2.1.32.js:391202
+++ pretty-v2.1.33.js:254348
@@ -1,3 +1,3 @@
 function WvA(A) {
-  return A.replace(/@/g, "-");
+  return A.replace(/:/g, "-");
 }

@@@ function 'Vd4' (was 'iL4') — structural (61.1%)
--- pretty-v2.1.32.js:367679
+++ pretty-v2.1.33.js:418623
@@ -1,14 +1,5 @@
 function iL4(A, q, { verbose: K }) {
   let Y = typeof A === "string" ? JA(A) : A;
-  if (SDY(Y))
-    return zW1.default.createElement(f, { dimColor: !0 }, "  ", "Created team");
   if ("success" in Y && "team_name" in Y && "message" in Y) return null;
-  if ("message" in Y)
-    return zW1.default.createElement(f, { dimColor: !0 }, "  ", Y.message);
-  return zW1.default.createElement(
-    f,
-    { dimColor: !0 },
-    "  ",
-    "operation complete",
-  );
+  return null;
 }

@@@ function 'XU1' (was 'Tg1') — structural (60.9%)
--- pretty-v2.1.32.js:437599
+++ pretty-v2.1.33.js:435476
@@ -1,7 +1,15 @@
 function Tg1(A) {
   try {
     let q = A.map(lbY),
-      K = NW6(q),
+      K = new Set(kx);
+    for (let $ of q)
+      if (
+        $.type === "user" &&
+        $.permissionMode !== void 0 &&
+        !K.has($.permissionMode)
+      )
+        $.permissionMode = void 0;
+    let Y = NW6(q),
       Y = TW6(K),
       z = CQ1(Y);
     if (z[z.length - 1]?.type === "user") z.push(QL({ content: Q41 }));

@@@ function 'j4q' (was 'j7q') — structural (60.5%)
--- pretty-v2.1.32.js:475722
+++ pretty-v2.1.33.js:475846
@@ -1,5 +1,5 @@
 function j7q(A) {
-  let q = A1(68),
+  let q = q1(61),
     {
       pluginName: K,
       serverName: Y,
@@ -19,7 +19,6 @@
     [M, W] = Df6.useState(""),
     G = $[_],
     P = G ? z[G] : null,
-    V = Kq(H),
     Z;
   if (q[3] === Symbol.for("react.memo_cache_sentinel"))
     ((Z = { context: "Settings" }), (q[3] = Z));
@@ -28,7 +27,8 @@
   let N;
   if (q[4] !== G || q[5] !== _ || q[6] !== M || q[7] !== $.length)
     ((N = () => {
-      if (_ < $.length - 1 && G) (j((o) => ({ ...o, [G]: M })), J(znY), W(""));
+      if (_ < O.length - 1 && G)
+        (M((_1) => ({ ..._1, [G]: j })), J(GoY), W(""));
     }),
       (q[4] = G),
       (q[5] = _),
@@ -105,190 +105,120 @@
     ((g = b ? "*".repeat(M.length) : M), (q[22] = M), (q[23] = b), (q[24] = g));
   else g = q[24];
   let x = g,
+    B = `Configure ${Y}`,
+    p = `Plugin: ${K}`,
+    r = P.title || G,
     p;
   if (q[25] !== Y)
-    ((p = hH.default.createElement(f, { bold: !0 }, "Configure ", Y)),
+    ((c = x && DN.default.createElement(f, { color: "error" }, " *")),
       (q[25] = Y),
       (q[26] = p));
   else p = q[26];
   let n;
-  if (q[27] !== K)
-    ((n = hH.default.createElement(
-      I,
-      { marginLeft: 1 },
-      hH.default.createElement(f, { dimColor: !0 }, "Plugin: ", K),
-    )),
-      (q[27] = K),
-      (q[28] = n));
-  else n = q[28];
-  let r = P.title || G,
-    z1;
-  if (q[29] !== U)
-    ((z1 = U && hH.default.createElement(f, { color: "error" }, " *")),
-      (q[29] = U),
-      (q[30] = z1));
-  else z1 = q[30];
-  let f1;
-  if (q[31] !== r || q[32] !== z1)
+  if (q[27] !== r || q[28] !== c)
     ((f1 = hH.default.createElement(f, { bold: !0 }, r, z1)),
-      (q[31] = r),
-      (q[32] = z1),
-      (q[33] = f1));
-  else f1 = q[33];
+      (q[27] = r),
+      (q[28] = c),
+      (q[29] = Y1));
+  else Y1 = q[29];
   let Z1;
-  if (q[34] !== P.description)
+  if (q[30] !== P.description)
     ((Z1 =
       P.description &&
       hH.default.createElement(f, { dimColor: !0 }, P.description)),
-      (q[34] = P.description),
-      (q[35] = Z1));
-  else Z1 = q[35];
+      (q[30] = P.description),
+      (q[31] = f1));
+  else f1 = q[31];
   let H1;
-  if (q[36] === Symbol.for("react.memo_cache_sentinel"))
+  if (q[32] === Symbol.for("react.memo_cache_sentinel"))
     ((H1 = hH.default.createElement(f, null, n1.pointerSmall, " ")),
-      (q[36] = H1));
-  else H1 = q[36];
+      (q[32] = P1));
+  else P1 = q[32];
   let D1;
-  if (q[37] !== x)
-    ((D1 = hH.default.createElement(f, null, x)), (q[37] = x), (q[38] = D1));
-  else D1 = q[38];
+  if (q[33] !== U)
+    (($1 = DN.default.createElement(f, null, U)), (q[33] = U), (q[34] = $1));
+  else $1 = q[34];
   let t;
-  if (q[39] === Symbol.for("react.memo_cache_sentinel"))
-    ((t = hH.default.createElement(f, null, "█")), (q[39] = t));
-  else t = q[39];
+  if (q[35] === Symbol.for("react.memo_cache_sentinel"))
+    ((M1 = DN.default.createElement(f, null, "█")), (q[35] = M1));
+  else M1 = q[35];
   let e;
-  if (q[40] !== D1)
+  if (q[36] !== $1)
     ((e = hH.default.createElement(I, { marginTop: 1 }, H1, D1, t)),
+      (q[36] = $1),
+      (q[37] = a));
+  else a = q[37];
+  let t;
+  if (q[38] !== Y1 || q[39] !== f1 || q[40] !== a)
+    ((t = DN.default.createElement(I, { flexDirection: "column" }, Y1, f1, a)),
+      (q[38] = Y1),
+      (q[39] = f1),
       (q[40] = D1),
       (q[41] = e));
   else e = q[41];
-  let G1;
-  if (q[42] !== f1 || q[43] !== Z1 || q[44] !== e)
+  let j1 = _ + 1,
+    w1;
+  if (q[42] !== O.length || q[43] !== j1)
     ((G1 = hH.default.createElement(
-      I,
-      { marginTop: 1, flexDirection: "column" },
       f1,
-      Z1,
+      { dimColor: !0 },
+      "Field ",
       e,
+      " of ",
+      O.length,
     )),
-      (q[42] = f1),
+      (q[42] = O.length),
       (q[43] = Z1),
-      (q[44] = e),
-      (q[45] = G1));
-  else G1 = q[45];
-  let w1 = _ + 1,
-    V1;
-  if (q[46] !== $.length || q[47] !== w1)
-    ((V1 = hH.default.createElement(
-      I,
-      { marginTop: 1 },
-      hH.default.createElement(
-        f,
-        { dimColor: !0 },
-        "Field ",
-        w1,
-        " of ",
-        $.length,
-      ),
-    )),
-      (q[46] = $.length),
-      (q[47] = w1),
-      (q[48] = V1));
-  else V1 = q[48];
+      (q[44] = w1));
+  else w1 = q[44];
   let E1;
-  if (q[49] !== _ || q[50] !== $.length)
+  if (q[45] !== _ || q[46] !== O.length)
     ((E1 =
       _ < $.length - 1 &&
       hH.default.createElement(
         I,
-        null,
-        hH.default.createElement(
-          f,
-          { dimColor: !0 },
-          "Tab: Next field · Enter: Save and continue",
-        ),
+        { dimColor: !0 },
+        "Tab: Next field · Enter: Save and continue",
       )),
-      (q[49] = _),
-      (q[50] = $.length),
-      (q[51] = E1));
-  else E1 = q[51];
+      (q[45] = _),
+      (q[46] = O.length),
+      (q[47] = V1));
+  else V1 = q[47];
   let q1;
-  if (q[52] !== _ || q[53] !== $.length)
+  if (q[48] !== _ || q[49] !== O.length)
     ((q1 =
       _ === $.length - 1 &&
       hH.default.createElement(
         I,
-        null,
-        hH.default.createElement(
-          f,
-          { dimColor: !0 },
-          "Enter: Save configuration",
-        ),
+        { dimColor: !0 },
+        "Enter: Save configuration",
       )),
+      (q[48] = _),
+      (q[49] = O.length),
+      (q[50] = E1));
+  else E1 = q[50];
+  let e;
+  if (q[51] !== w1 || q[52] !== V1 || q[53] !== E1)
+    ((e = DN.default.createElement(I, { flexDirection: "column" }, w1, V1, E1)),
+      (q[51] = w1),
       (q[52] = _),
-      (q[53] = $.length),
+      (q[53] = E1),
       (q[54] = q1));
   else q1 = q[54];
   let s;
-  if (
-    q[55] !== p ||
-    q[56] !== n ||
-    q[57] !== G1 ||
-    q[58] !== V1 ||
-    q[59] !== E1 ||
-    q[60] !== q1
-  )
+  if (q[55] !== H || q[56] !== B || q[57] !== p || q[58] !== t || q[59] !== e)
     ((s = hH.default.createElement(
       I,
-      { flexDirection: "column", gap: 1, padding: 1, borderStyle: "round" },
-      p,
-      n,
+      { title: B, subtitle: p, onCancel: H, isCancelActive: !1 },
       G1,
       V1,
-      E1,
-      q1,
     )),
       (q[55] = p),
       (q[56] = n),
       (q[57] = G1),
       (q[58] = V1),
       (q[59] = E1),
-      (q[60] = q1),
-      (q[61] = s));
-  else s = q[61];
-  let j1;
-  if (q[62] !== V.keyName || q[63] !== V.pending)
-    ((j1 = hH.default.createElement(
-      I,
-      { marginLeft: 3 },
-      hH.default.createElement(
-        f,
-        { dimColor: !0 },
-        V.pending
-          ? hH.default.createElement(
-              hH.default.Fragment,
-              null,
-              "Press ",
-              V.keyName,
-              " again to exit",
-            )
-          : hH.default.createElement(
-              hH.default.Fragment,
-              null,
-              "Esc to cancel",
-            ),
-      ),
-    )),
-      (q[62] = V.keyName),
-      (q[63] = V.pending),
-      (q[64] = j1));
-  else j1 = q[64];
-  let J1;
-  if (q[65] !== s || q[66] !== j1)
-    ((J1 = hH.default.createElement(I, { flexDirection: "column" }, s, j1)),
-      (q[65] = s),
-      (q[66] = j1),
-      (q[67] = J1));
-  else J1 = q[67];
+      (q[60] = A1));
+  else A1 = q[60];
   return J1;
 }

@@@ function 'yyY' (was 'MRY') — structural (60.0%)
--- pretty-v2.1.32.js:422274
+++ pretty-v2.1.33.js:420719
@@ -1,4 +1,17 @@
 function MRY(A, q) {
+  let K = 0,
+    Y = 0;
+  for (let w = A.length - 1; w >= 0; w--) {
+    let H = A[w],
+      $ = sd4(H, q);
+    if ($ && ($.isSearch || $.isRead)) {
+      if (H.data.message.type === "user") {
+        if ($.isSearch) K++;
+        else if ($.isRead) Y++;
+      }
+    } else break;
+  }
+  if (K + Y >= 2) return d$6(K, Y, !0);
   let K = [...A].reverse().find((Y) => {
     let z = Y.data.message;
     return (

@@@ function 'WF7' (was 'za4') — structural (59.4%)
--- pretty-v2.1.32.js:442261
+++ pretty-v2.1.33.js:254444
@@ -12,18 +12,43 @@
       W = O.color,
       G = O.model,
       P = O.forkContext,
-      V = $.trim();
+      V = O.trim(),
+      Z = $.memory,
+      N;
+    if (Z !== void 0)
+      if (MF7.includes(Z)) N = Z;
+      else
+        h(
+          `Plugin agent file ${A} has invalid memory value '${Z}'. Valid options: ${MF7.join(", ")}`,
+        );
+    if (Iw() && N && M !== void 0) {
+      let T = new Set(M);
+      for (let k of [_5, Rq, Yq]) if (!T.has(k)) M = [...M, k];
+    }
     return {
       agentType: X,
       whenToUse: D,
       tools: j,
       ...(M !== void 0 ? { skills: M } : {}),
-      getSystemPrompt: () => V,
+      getSystemPrompt: () => {
+        if (Iw() && N) {
+          let T = Xq1(X, N);
+          return (
+            V +
+            `
+
+` +
+            T
+          );
+        }
+        return V;
+      },
       source: "plugin",
       color: W,
       model: G,
       filename: _,
       plugin: Y,
+      ...(N ? { memory: N } : {}),
       ...{},
     };
   } catch (H) {

@@@ function 'F64' (was 'zH4') — structural (58.5%)
--- pretty-v2.1.32.js:311595
+++ pretty-v2.1.33.js:303372
@@ -1,6 +1,7 @@
 function zH4(A) {
-  let [q, K] = Tu(YH4);
-  if (!A) return [q, !0];
+  let q = t_(),
+    [K, Y] = vL(A && q ? m64 : null);
+  if (!A || !q) return [K, !0];
   let Y = Math.floor(K / YH4) % 2 === 0;
   return [q, Y];
 }

@@@ variable 'jq6' (was 'WK6') — structural (58.1%)
--- pretty-v2.1.32.js:186358
+++ pretty-v2.1.33.js:150528
@@ -2,5 +2,5 @@
   d1();
   e81();
   n_1 = a($1(), 1);
-  qC1 = n_1.createContext(null);
+  ((Mq6 = cn.createContext(null)), (kZ5 = G_1 * 2));
 });

@@@ variable 'kf6' (was 'qt4') — structural (57.9%)
--- pretty-v2.1.32.js:449145
+++ pretty-v2.1.33.js:478139
@@ -11,5 +11,4 @@
   Px();
   Z7();
   C21();
-  iD();
 });

@@@ variable 'kjq' (was 'DBA') — structural (57.9%)
--- pretty-v2.1.32.js:524267
+++ pretty-v2.1.33.js:547515
@@ -8,4 +8,7 @@
   kq1();
   a6();
   n0();
+  EH();
+  wG1();
+  FN();
 });

@@@ variable 'nTq' (was 'KT6') — structural (57.9%)
--- pretty-v2.1.32.js:547190
+++ pretty-v2.1.33.js:558567
@@ -1,11 +1,3 @@
 var KT6 = v(() => {
   F6();
-  IO();
-  J8();
-  V$();
-  MK1();
-  Cp();
-  ImA();
-  $Z();
-  _6();
 });

@@@ variable 'aTq' (was 'BDq') — structural (57.9%)
--- pretty-v2.1.32.js:547380
+++ pretty-v2.1.33.js:558599
@@ -1,9 +1,4 @@
 var BDq = v(() => {
   F6();
   IO();
-  MK1();
-  HJ();
-  Cp();
-  e81();
-  KT6();
 });

@@@ variable 'eTq' (was 'bNq') — structural (57.9%)
--- pretty-v2.1.32.js:560050
+++ pretty-v2.1.33.js:558634
@@ -1,13 +1,3 @@
 var bNq = v(() => {
   FA();
-  FA();
-  a6();
-  R8();
-  zB();
-  YZ1();
-  iD();
-  pp1();
-  D7();
-  k6();
-  ip1();
 });

@@@ variable 'yvq' (was 'jTq') — structural (57.9%)
--- pretty-v2.1.32.js:561723
+++ pretty-v2.1.33.js:561188
@@ -5,6 +5,4 @@
   dO();
   Pf6();
   wJ();
-  _6();
-  k6();
 });

@@@ variable 'DEq' (was 'TTq') — structural (57.9%)
--- pretty-v2.1.32.js:563694
+++ pretty-v2.1.33.js:564282
@@ -1,10 +1,3 @@
 var TTq = v(() => {
   F6();
-  yp();
-  hR();
-  Nh();
-  _6();
-  $w();
-  Zs();
-  R8();
 });

@@@ variable 'jEq' (was 'IFA') — structural (57.9%)
--- pretty-v2.1.32.js:564041
+++ pretty-v2.1.33.js:564532
@@ -1,7 +1,3 @@
 var IFA = v(() => {
   V31();
-  FA();
-  a6();
-  _6();
-  h11();
 });

@@@ function 'Zh4' (was 'xx4') — structural (57.9%)
--- pretty-v2.1.32.js:390036
+++ pretty-v2.1.33.js:378844
@@ -1,5 +1,5 @@
-async function xx4(A, q) {
-  let K = A.map((z) => {
+async function Zh4(A, q, K) {
+  let z = (K ? A.filter((H) => K.includes(H.agentType)) : A).map((H) => {
       let w = "";
       if (z?.forkContext)
         w =
@@ -89,10 +89,5 @@
 </commentary>
 assistant: "I'm going to use the ${ZW1.name} tool to launch the greeting-responder agent"
 </example>
-${
-  !F8()
-    ? `
-Note: The "Agent Teams" feature (TeammateTool, SendMessage, spawnTeam) is not available on this plan. Only mention this if the user explicitly asks for "agent teams" by name, or asks for agents to send messages to each other (peer-to-peer messaging). Do NOT mention this limitation when users ask for parallel subagents, coordinating agents, launching a "team" of agents, or having agents work together — those are all normal Task tool usage and you should proceed normally.`
-    : ""
-}`;
+`;
 }

@@@ function 'ld4' (was 'Ud4') — structural (57.8%)
--- pretty-v2.1.32.js:421956
+++ pretty-v2.1.33.js:420403
@@ -1,6 +1,5 @@
-function Ud4({ description: A, prompt: q, name: K, team_name: Y }) {
+function ld4({ description: A, prompt: q }) {
   if (h9()) return null;
-  if (F8() && Y && K) return `spawn: ${K}`;
   if (!A || !q) return null;
   return A;
 }

@@@ variable 'hWq' (was 'cTq') — structural (56.7%)
--- pretty-v2.1.32.js:564850
+++ pretty-v2.1.33.js:550113
@@ -1,13 +1,4 @@
 var cTq = v(() => {
   d1();
-  u1();
-  QTq();
-  Ez();
-  UTq();
-  F6();
-  Q8();
-  xB();
-  _6();
-  IB();
-  ((IG = a($1(), 1)), (pTq = a($1(), 1)));
+  xT6 = s(J1(), 1);
 });

@@@ variable 'y1q' (was 'A1q') — structural (56.5%)
--- pretty-v2.1.32.js:456284
+++ pretty-v2.1.33.js:454989
@@ -1,8 +1,6 @@
 var A1q = v(() => {
   ySA();
   BA();
-  PV();
-  uSA = a($1(), 1);
   ((fpY = {
     aliases: ["bug"],
     type: "local-jsx",
@@ -21,10 +19,7 @@
         !X0("allow_product_feedback")
       ),
     isHidden: !1,
-    async call(A, { abortController: q, messages: K }, Y) {
-      let z = Y || "";
-      return ZpY(A, q.signal, K, z);
-    },
+    load: () => Promise.resolve().then(() => (R1q(), L1q)),
     userFacingName() {
       return "feedback";
     },

@@@ variable 'nwq' (was 'q2q') — structural (55.9%)
--- pretty-v2.1.32.js:506491
+++ pretty-v2.1.33.js:506515
@@ -1,31 +1,21 @@
 var q2q = v(() => {
   d1();
   k5();
-  hq();
-  F6();
-  D7();
-  kbA();
-  LF1();
-  FA();
-  jS();
-  ((VV6 = a($1(), 1)),
-    (ezq = a($1(), 1)),
-    (A2q = {
-      type: "local-jsx",
-      name: "rate-limit-options",
-      userFacingName() {
-        return "rate-limit-options";
-      },
-      description: "Show options when rate limit is reached",
-      isEnabled: () => {
-        if (!U8()) return !1;
-        if (DS()) return !0;
-        let A = TK();
-        return A === "pro" || A === "max";
-      },
-      isHidden: !0,
-      async call(A, q) {
-        return VV6.default.createElement(x8z, { onDone: A, context: q });
-      },
-    }));
+  ((Kqz = {
+    type: "local-jsx",
+    name: "rate-limit-options",
+    userFacingName() {
+      return "rate-limit-options";
+    },
+    description: "Show options when rate limit is reached",
+    isEnabled: () => {
+      if (!i8()) return !1;
+      if (fL()) return !0;
+      let A = JK();
+      return A === "pro" || A === "max";
+    },
+    isHidden: !0,
+    load: () => Promise.resolve().then(() => (lwq(), cwq)),
+  }),
+    (iwq = Kqz));
 });

@@@ function 'e6z' (was 'meY') — structural (55.7%)
--- pretty-v2.1.32.js:489341
+++ pretty-v2.1.33.js:489460
@@ -1,10 +1,18 @@
 function meY(A) {
   let q = BW1(A),
-    K = a64(q);
+    K = Oc7(q),
+    Y = A.source === "plugin" ? A.pluginInfo?.pluginManifest.name : void 0;
   return Cz.createElement(
     I,
     { key: `${A.name}-${A.source}` },
     Cz.createElement(f, null, A.userFacingName()),
-    Cz.createElement(f, { dimColor: !0 }, " · ", K, " description tokens"),
+    Ez.createElement(
+      f,
+      { dimColor: !0 },
+      Y ? ` · ${Y}` : "",
+      " · ",
+      K,
+      " description tokens",
+    ),
   );
 }

@@@ function 'zd4' (was 'UL4') — structural (55.6%)
--- pretty-v2.1.32.js:367525
+++ pretty-v2.1.33.js:418306
@@ -1,12 +1,6 @@
 function UL4() {
   return `
-# TeammateTool
-
-Manage teams and coordinate agents on your team. Use this tool to create and clean up teams. To spawn new teammates, use the Task tool with \`team_name\` and \`name\` parameters.
-
-## Operations
-
-### spawnTeam - Create a Team
+# TeamCreate
 
 ## When to Use
 
@@ -31,33 +25,18 @@
 
 \`\`\`
 {
-  "operation": "spawnTeam",
   "team_name": "my-project",
   "description": "Working on feature X"
 }
 \`\`\`
 
-This creates a team file and a corresponding task list directory.
-
-### cleanup - Clean Up Team Resources
-
-Remove team and task directories when work is complete:
-
-\`\`\`
-{
-  "operation": "cleanup"
-}
-\`\`\`
-
-This operation:
-- Removes the team and task directories
-- Clears team context from the current session
-
-**IMPORTANT**: \`cleanup\` will fail if the team still has active members. Gracefully terminate teammates first, then call \`cleanup\` after all teammates have shut down.
+This creates:
+- A team file at \`~/.claude/teams/{team-name}.json\`
+- A corresponding task list directory at \`~/.claude/tasks/{team-name}/\`
 
 ## Team Workflow
 
-1. **Create a team** with \`spawnTeam\` - this creates both the team and its task list
+1. **Create a team** with TeamCreate - this creates both the team and its task list
 2. **Create tasks** using the Task tools (TaskCreate, TaskList, etc.) - they automatically use the team's task list
 3. **Spawn teammates** using the Task tool with \`team_name\` and \`name\` parameters to create teammates that join the team
 4. **Assign tasks** using TaskUpdate with \`owner\` to give tasks to idle teammates
@@ -79,6 +58,8 @@
 - If you're busy (mid-turn), messages are queued and delivered when your turn ends
 - The UI shows a brief notification with the sender's name when messages are waiting
 
+Messages will be delivered automatically.
+
 When reporting on teammate messages, you do NOT need to quote the original message—it's already rendered to the user.
 
 ## Teammate Idle State
@@ -126,7 +107,7 @@
 - Your team cannot hear you if you do not use the SendMessage tool. Always send a message to your teammates if you are responding to them.
 - Do NOT send structured JSON status messages like \`{"type":"idle",...}\` or \`{"type":"task_completed",...}\`. Just communicate in plain text when you need to message teammates.
 - Use TaskUpdate to mark tasks completed.
-- If you are an agent in the team, the system will automatically send idle notifications to the team lead when you stop. 
+- If you are an agent in the team, the system will automatically send idle notifications to the team lead when you stop.
 
 `.trim();
 }

@@@ function 'bXq' (was 'VJq') — structural (55.1%)
--- pretty-v2.1.32.js:536524
+++ pretty-v2.1.33.js:534932
@@ -1,5 +1,5 @@
 function VJq(A) {
-  let q = A1(48),
+  let q = q1(49),
     {
       apiKeyStatus: K,
       autoUpdaterResult: Y,
@@ -20,9 +20,14 @@
     ((M = RV(q1)), (q[0] = O), (q[1] = M));
   } else M = q[1];
   let W = M,
+    G;
+  if (q[2] === Symbol.for("react.memo_cache_sentinel"))
+    ((G = J5()), (q[2] = G));
+  else G = q[2];
+  let P = G,
+    V = NXq(W, P),
     G = OJq(W),
     P = VZ1(X),
-    V = T6(dzz),
     { addNotification: Z, removeNotification: N } = Fq(),
     T = or(),
     y =
@@ -31,20 +36,20 @@
       Y?.status !== "success",
     u = T.isUsingOverage,
     S;
-  if (q[2] === Symbol.for("react.memo_cache_sentinel"))
-    ((S = TK()), (q[2] = S));
-  else S = q[2];
+  if (q[3] === Symbol.for("react.memo_cache_sentinel"))
+    ((x = JK()), (q[3] = x));
+  else x = q[3];
   let m = S,
     b = m === "team" || m === "enterprise",
     U;
-  if (q[3] === Symbol.for("react.memo_cache_sentinel"))
-    ((U = _I()), (q[3] = U));
-  else U = q[3];
+  if (q[4] === Symbol.for("react.memo_cache_sentinel"))
+    ((B = WI()), (q[4] = B));
+  else B = q[4];
   let g = U,
     x = j && !G && K !== "invalid" && K !== "missing" && g !== void 0,
     p,
     n;
-  if (q[4] !== Z || q[5] !== N || q[6] !== x)
+  if (q[5] !== T || q[6] !== k || q[7] !== r)
     ((p = () => {
       if (x && g)
         (c("tengu_external_editor_hint_shown", {}),
@@ -66,22 +71,22 @@
       else N("external-editor-hint");
     }),
       (n = [x, g, Z, N]),
-      (q[4] = Z),
       (q[5] = N),
       (q[6] = x),
       (q[7] = p),
-      (q[8] = n));
-  else ((p = q[7]), (n = q[8]));
+      (q[8] = c),
+      (q[9] = Y1));
+  else ((c = q[8]), (Y1 = q[9]));
   fJq.useEffect(p, n);
   let r;
-  if (q[9] !== J || q[10] !== X)
+  if (q[10] !== J || q[11] !== X)
     ((r = A5.createElement(JJq, { ideSelection: J, mcpClients: X })),
-      (q[9] = J),
       (q[10] = X),
-      (q[11] = r));
-  else r = q[11];
+      (q[11] = X),
+      (q[12] = f1));
+  else f1 = q[12];
   let z1;
-  if (q[12] !== V.current)
+  if (q[13] !== N.current)
     ((z1 =
       V.current &&
       ("jsx" in V.current
@@ -91,11 +96,11 @@
             { color: V.current.color, dimColor: !V.current.color },
             V.current.text,
           ))),
-      (q[12] = V.current),
-      (q[13] = z1));
-  else z1 = q[13];
+      (q[13] = N.current),
+      (q[14] = P1));
+  else P1 = q[14];
   let f1;
-  if (q[14] !== u)
+  if (q[15] !== m)
     ((f1 =
       u &&
       !b &&
@@ -104,35 +109,35 @@
         null,
         A5.createElement(f, { dimColor: !0 }, "Now using extra usage"),
       )),
-      (q[14] = u),
-      (q[15] = f1));
-  else f1 = q[15];
+      (q[15] = m),
+      (q[16] = $1));
+  else $1 = q[16];
   let Z1;
-  if (q[16] !== K)
+  if (q[17] !== K)
     ((Z1 =
       K === "invalid" &&
       A5.createElement(
         I,
         null,
-        A5.createElement(f, { color: "error" }, "Invalid API key · Run /login"),
+        Y5.createElement(f, { color: "error" }, "Not logged in · Run /login"),
       )),
-      (q[16] = K),
-      (q[17] = Z1));
-  else Z1 = q[17];
+      (q[17] = K),
+      (q[18] = M1));
+  else M1 = q[18];
   let H1;
-  if (q[18] !== K)
+  if (q[19] !== K)
     ((H1 =
       K === "missing" &&
       A5.createElement(
         I,
         null,
-        A5.createElement(f, { color: "error" }, "Missing API key · Run /login"),
+        Y5.createElement(f, { color: "error" }, "Not logged in · Run /login"),
       )),
-      (q[18] = K),
-      (q[19] = H1));
-  else H1 = q[19];
+      (q[19] = K),
+      (q[20] = a));
+  else a = q[20];
   let D1;
-  if (q[20] !== z)
+  if (q[21] !== z)
     ((D1 =
       z &&
       A5.createElement(
@@ -140,11 +145,11 @@
         null,
         A5.createElement(f, { color: "warning" }, "Debug mode"),
       )),
-      (q[20] = z),
-      (q[21] = D1));
-  else D1 = q[21];
+      (q[21] = z),
+      (q[22] = t));
+  else t = q[22];
   let t;
-  if (q[22] !== K || q[23] !== W || q[24] !== H)
+  if (q[23] !== K || q[24] !== W || q[25] !== H)
     ((t =
       K !== "invalid" &&
       K !== "missing" &&
@@ -154,24 +159,26 @@
         null,
         A5.createElement(f, { dimColor: !0 }, W, " tokens"),
       )),
-      (q[22] = K),
       (q[23] = W),
       (q[24] = H),
-      (q[25] = t));
-  else t = q[25];
+      (q[25] = H),
+      (q[26] = j1));
+  else j1 = q[26];
   let e;
-  if (q[26] !== W)
-    ((e = A5.createElement(wJq, { tokenUsage: W })), (q[26] = W), (q[27] = e));
-  else e = q[27];
+  if (q[27] !== W)
+    ((w1 = Y5.createElement(fXq, { tokenUsage: W, model: P })),
+      (q[27] = W),
+      (q[28] = w1));
+  else w1 = q[28];
   let G1;
   if (
-    q[28] !== Y ||
     q[29] !== w ||
     q[30] !== G ||
     q[31] !== $ ||
     q[32] !== _ ||
     q[33] !== y ||
-    q[34] !== H
+    q[34] !== S ||
+    q[35] !== H
   )
     ((G1 =
       y &&
@@ -183,25 +190,24 @@
         onChangeIsUpdating: _,
         showSuccessMessage: !G,
       })),
-      (q[28] = Y),
       (q[29] = w),
       (q[30] = G),
       (q[31] = $),
       (q[32] = _),
       (q[33] = y),
       (q[34] = H),
-      (q[35] = G1));
-  else G1 = q[35];
+      (q[35] = H),
+      (q[36] = V1));
+  else V1 = q[36];
   let w1, V1;
-  if (q[36] === Symbol.for("react.memo_cache_sentinel"))
+  if (q[37] === Symbol.for("react.memo_cache_sentinel"))
     ((w1 = A5.createElement(WJq, null)),
       (V1 = A5.createElement(PJq, null)),
-      (q[36] = w1),
-      (q[37] = V1));
-  else ((w1 = q[36]), (V1 = q[37]));
+      (q[37] = E1),
+      (q[38] = e));
+  else ((E1 = q[37]), (e = q[38]));
   let E1;
   if (
-    q[38] !== Z1 ||
     q[39] !== H1 ||
     q[40] !== D1 ||
     q[41] !== t ||
@@ -209,7 +215,8 @@
     q[43] !== G1 ||
     q[44] !== r ||
     q[45] !== z1 ||
-    q[46] !== f1
+    q[46] !== f1 ||
+    q[47] !== P1
   )
     ((E1 = A5.createElement(
       jK1,
@@ -235,7 +242,6 @@
         V1,
       ),
     )),
-      (q[38] = Z1),
       (q[39] = H1),
       (q[40] = D1),
       (q[41] = t),
@@ -244,7 +250,8 @@
       (q[44] = r),
       (q[45] = z1),
       (q[46] = f1),
-      (q[47] = E1));
-  else E1 = q[47];
+      (q[47] = P1),
+      (q[48] = A1));
+  else A1 = q[48];
   return E1;
 }

@@@ function 'vL' (was 'Tu') — structural (54.0%)
--- pretty-v2.1.32.js:248698
+++ pretty-v2.1.33.js:212870
@@ -1,20 +1,17 @@
 function Tu(A = 16) {
   let q = Oo.useContext(qC1),
     [K, { isVisible: Y }] = $U(),
-    [z, w] = Oo.useState(() => q?.getTime() ?? 0),
-    [H] = Oo.useState(() => Symbol("animation"));
+    [z, w] = EX1.useState(() => q?.now() ?? 0),
+    H = Y && A !== null;
   return (
     Oo.useEffect(() => {
-      if (!q) return;
-      let O = q.getTime(),
+      if (!q || !H) return;
+      let $ = q.now(),
         $ = () => {
-          let _ = q.getTime();
+          let _ = q.now();
           if (_ - O >= A) ((O = _), w(_));
         };
-      return q.subscribe(H, Y, $);
-    }, [q, H, A, Y]),
-    Oo.useEffect(() => {
-      q?.setVisibility(H, Y);
+      return q.subscribe(O, !0);
     }, [q, H, Y]),
     [K, z]
   );

@@@ variable '$G1' (was 'hG1') — structural (53.3%)
--- pretty-v2.1.32.js:435101
+++ pretty-v2.1.33.js:432881
@@ -12,5 +12,5 @@
   fg1();
   g4();
   fM();
-  bbY = { user_intent: hbY, stated_intent: IbY, coordinator: xbY };
+  muY = { user_intent: xuY, stated_intent: buY };
 });

@@@ variable 'Op4' (was 'n9q') — structural (53.3%)
--- pretty-v2.1.32.js:498344
+++ pretty-v2.1.33.js:417095
@@ -1,81 +1,14 @@
 var n9q = v(() => {
   iP();
-  NH();
-  J8();
-  qv();
-  F6();
-  Pt();
-  I6();
-  l9q = `You are an elite AI agent architect specializing in crafting high-performance agent configurations. Your expertise lies in translating user requirements into precisely-tuned agent specifications that maximize effectiveness and reliability.
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
-      Since a significant piece of code was written, use the ${OK} tool to launch the test-runner agent to run the tests.
-      </commentary>
-      assistant: "Now let me use the test-runner agent to run the tests"
-    </example>
-    - <example>
-      Context: User is creating an agent to respond to the word "hello" with a friendly jok.
-      user: "Hello"
-      assistant: "I'm going to use the ${OK} tool to launch the greeting-responder agent to respond with a friendly joke"
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
+  vRY = `## What Happens in Plan Mode
 
-Key principles for your system prompts:
-- Be specific rather than generic - avoid vague instructions
-- Include concrete examples when they would clarify behavior
-- Balance comprehensiveness with clarity - every instruction should add value
-- Ensure the agent has enough context to handle variations of the core task
-- Make the agent proactive in seeking clarification when needed
-- Build in quality assurance and self-correction mechanisms
+In plan mode, you'll:
+1. Thoroughly explore the codebase using Glob, Grep, and Read tools
+2. Understand existing patterns and architecture
+3. Design an implementation approach
+4. Present your plan to the user for approval
+5. Use ${OH} if you need to clarify approaches
+6. Exit plan mode with ExitPlanMode when ready to implement
 
-Remember: The agents you create should be autonomous experts capable of handling their designated tasks with minimal additional guidance. Your system prompts are their complete operational manual.
 `;
 });

@@@ variable 'Pzq' (was '$91') — structural (53.3%)
--- pretty-v2.1.32.js:504693
+++ pretty-v2.1.33.js:498475
@@ -6,9 +6,76 @@
   a6();
   MV6();
   ah();
-  FA();
-  I6();
-  g4();
-  Mzq();
-  Wzq = `${PbA}.json`;
+  Wzq = `You are an elite AI agent architect specializing in crafting high-performance agent configurations. Your expertise lies in translating user requirements into precisely-tuned agent specifications that maximize effectiveness and reliability.
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
+
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
+      Since a significant piece of code was written, use the ${XK} tool to launch the test-runner agent to run the tests.
+      </commentary>
+      assistant: "Now let me use the test-runner agent to run the tests"
+    </example>
+    - <example>
+      Context: User is creating an agent to respond to the word "hello" with a friendly jok.
+      user: "Hello"
+      assistant: "I'm going to use the ${XK} tool to launch the greeting-responder agent to respond with a friendly joke"
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

@@@ function 'Dc7' (was 'rY4') — structural (53.3%)
--- pretty-v2.1.32.js:301107
+++ pretty-v2.1.33.js:264477
@@ -1,4 +1,4 @@
-function rY4(A, q, K, Y) {
+function Dc7(A, q, K, Y, z) {
   try {
     let z = T_6(A, Y);
     if (!z) return;
@@ -6,7 +6,10 @@
     if (!w) return;
     if (ec9(w.model)) return;
     let H = w.prevCacheReadTokens;
-    if (((w.prevCacheReadTokens = q), H === null)) return;
+    H.prevCacheReadTokens = q;
+    let O = Y.findLast((Z) => Z.type === "assistant"),
+      _ = O ? Date.now() - new Date(O.timestamp).getTime() : null;
+    if ($ === null) return;
     let O = w.pendingChanges,
       $ = H - q;
     if (q >= H * 0.95 || $ < tc9) {
@@ -32,7 +35,9 @@
         _.push(`tools changed${M}`);
       }
     }
-    let D = `[PROMPT CACHE BREAK] ${_.length > 0 ? _.join(", ") : "unknown cause"} [source=${A}, call #${w.callCount}, cache read: ${H} → ${q}, creation: ${K}]`;
+    let j = _ !== null && _ > dT9,
+      W = _ !== null && _ > cT9,
+      P = `[PROMPT CACHE BREAK] ${D.length > 0 ? D.join(", ") : "unknown cause"} [source=${A}, call #${H.callCount}, cache read: ${$} → ${q}, creation: ${K}]`;
     (h(D, { level: "warn" }),
       c("tengu_prompt_cache_break", {
         systemPromptChanged: O?.systemPromptChanged ?? !1,
@@ -45,6 +50,9 @@
         prevCacheReadTokens: H,
         cacheReadTokens: q,
         cacheCreationTokens: K,
+        timeSinceLastAssistantMsg: _ ?? -1,
+        lastAssistantMsgOver5minAgo: j,
+        lastAssistantMsgOver1hAgo: W,
       }));
     let j;
     if (O?.prevDiffableContent)

@@@ function 'Rd4' (was 'Td4') — structural (52.9%)
--- pretty-v2.1.32.js:420398
+++ pretty-v2.1.33.js:418863
@@ -1,15 +1,10 @@
 function Td4(A) {
   switch (A.type) {
     case "message":
-      return `to @${A.recipient}`;
     case "broadcast":
-      return "to @team";
     case "shutdown_request":
-      return `request shutdown: ${A.recipient}`;
     case "shutdown_response":
-      return A.approve
-        ? "approve shutdown"
-        : `reject shutdown: ${A.content || "no reason"}`;
+      return null;
     case "plan_approval_response":
       return A.approve
         ? `approve plan from: ${A.recipient}`

@@@ variable 'gwq' (was 'tzq') — structural (52.9%)
--- pretty-v2.1.32.js:506280
+++ pretty-v2.1.33.js:506282
@@ -1,22 +1,18 @@
 var tzq = v(() => {
   azq();
   D7();
-  PV();
-  ((vbA = a($1(), 1)),
-    (szq = {
-      type: "local-jsx",
-      name: "remote-env",
-      userFacingName() {
-        return "remote-env";
-      },
-      description:
-        "Configure the default remote environment for teleport sessions",
-      isEnabled: () => U8() && X0("allow_remote_sessions"),
-      get isHidden() {
-        return !U8() || !X0("allow_remote_sessions");
-      },
-      async call(A) {
-        return vbA.createElement(ozq, { onDone: A });
-      },
-    }));
+  Uwq = {
+    type: "local-jsx",
+    name: "remote-env",
+    userFacingName() {
+      return "remote-env";
+    },
+    description:
+      "Configure the default remote environment for teleport sessions",
+    isEnabled: () => i8() && j0("allow_remote_sessions"),
+    get isHidden() {
+      return !i8() || !j0("allow_remote_sessions");
+    },
+    load: () => Promise.resolve().then(() => (Qwq(), Fwq)),
+  };
 });

@@@ function 'TE4' (was 'tL4') — structural (52.9%)
--- pretty-v2.1.32.js:367971
+++ pretty-v2.1.33.js:355406
@@ -7,18 +7,17 @@
   }
   for (let O of Y) await UDY(O);
   let z = AF1(A);
-  if (rL4(z))
-    try {
-      (UNA(z, { recursive: !0, force: !0 }),
-        h(`[TeammateTool] Cleaned up team directory: ${z}`));
-    } catch (O) {
-      h(
-        `[TeammateTool] Failed to clean up team directory ${z}: ${O instanceof Error ? O.message : String(O)}`,
-      );
-    }
+  try {
+    (await jE4(z, { recursive: !0, force: !0 }),
+      h(`[TeammateTool] Cleaned up team directory: ${z}`));
+  } catch (H) {
+    h(
+      `[TeammateTool] Failed to clean up team directory ${z}: ${H instanceof Error ? H.message : String(H)}`,
+    );
+  }
   let H = rk(q);
   try {
-    (UNA(H, { recursive: !0, force: !0 }),
+    (await jE4(w, { recursive: !0, force: !0 }),
       h(`[TeammateTool] Cleaned up tasks directory: ${H}`),
       T_1());
   } catch (O) {

@@@ function 'wd4' (was 'DOz') — structural (52.2%)
--- pretty-v2.1.32.js:549789
+++ pretty-v2.1.33.js:418419
@@ -1,3 +1,3 @@
 function DOz(A) {
-  return A.uuid;
+  return `create team: ${A.team_name}`;
 }

@@@ function 'FMz' (was 'zXz') — structural (52.0%)
--- pretty-v2.1.32.js:565889
+++ pretty-v2.1.33.js:568146
@@ -286,7 +286,7 @@
       )
       .option(
         "--session-id <id>",
-        "Use a specific session ID for the conversation (UUID or tagged ID)",
+        "Use a specific session ID for the conversation (must be a valid UUID)",
       )
       .option(
         "--agents <json>",
@@ -414,19 +414,21 @@
 `),
             ),
               process.exit(1));
-          let RA = VMA(k);
-          if (!RA)
-            (process.stderr.write(
-              Y6.red(`Error: Invalid session ID. Must be a valid UUID or tagged ID.
+          if (!j1) {
+            let XA = _v(N);
+            if (!XA)
+              (process.stderr.write(
+                K6.red(`Error: Invalid session ID. Must be a valid UUID.
 `),
-            ),
-              process.exit(1));
-          if (iu1(RA))
-            (process.stderr.write(
-              Y6.red(`Error: Session ID ${RA} is already in use.
+              ),
+                process.exit(1));
+            if (Uu1(XA))
+              (process.stderr.write(
+                K6.red(`Error: Session ID ${XA} is already in use.
 `),
-            ),
-              process.exit(1));
+              ),
+                process.exit(1));
+          }
         }
         let J1 = $.file;
         if (J1 && J1.length > 0) {
@@ -686,7 +688,8 @@
             });
         }
         (Vq("action_before_setup"), h("[STARTUP] Running setup()..."));
-        let U6 = Date.now();
+        let G6 = Date.now(),
+          { setup: Z6 } = await Promise.resolve().then(() => (Ov6(), $v6));
         (await nT6(mFA(), L1, D, e, t, G1, k ? VMA(k) : void 0),
           h(`[STARTUP] setup() completed in ${Date.now() - U6}ms`),
           Vq("action_after_setup"));
@@ -716,7 +719,12 @@
               `Warning: agent "${_A}" not found. Available agents: ${h6.activeAgents.map((RA) => RA.agentType).join(", ")}. Using default behavior.`,
             );
         }
-        if ((fy(LA?.agentType), LA?.agentType)) NuA(u6(), LA.agentType);
+        if ((Sy(i6?.agentType), i6))
+          l("tengu_agent_flag", {
+            agentType: T0(i6) ? i6.agentType : "custom",
+            ...(S && { source: "cli" }),
+          });
+        if (i6?.agentType) luA(U6(), i6.agentType);
         if (o && LA && !_1 && !tD(LA)) {
           let RA = LA.getSystemPrompt();
           if (RA) _1 = RA;
@@ -726,13 +734,7 @@
         (rG(q8), xE6(y86() || null));
         let r7 = AV1(),
           A8 = s9(r7 ?? bk());
-        if (
-          F8() &&
-          w1?.agentId &&
-          w1?.agentName &&
-          w1?.teamName &&
-          w1?.agentType
-        ) {
+        if (p8() && t?.agentId && t?.agentName && t?.teamName && t?.agentType) {
           let RA = h6.activeAgents.find((e8) => e8.agentType === w1.agentType);
           if (RA) {
             let e8;
@@ -894,7 +896,9 @@
           if ($.sessionPersistence === !1) Yk6(!0);
           (bE6(S08(N)),
             m91(),
-            _N6(),
+            Promise.resolve()
+              .then(() => (smA(), IMq))
+              .then((T4) => T4.startBackgroundHousekeeping()),
             PTq(
               j6,
               async () => $4.getState(),
@@ -976,8 +980,11 @@
             verbose: x ?? M6().verbose ?? !1,
             mainLoopModel: r7,
             mainLoopModelForSession: null,
-            showExpandedTodos: M6().showExpandedTodos ?? !1,
-            showSpinnerTree: M6().showSpinnerTree ?? !1,
+            expandedView: j6().showSpinnerTree
+              ? "teammates"
+              : j6().showExpandedTodos
+                ? "tasks"
+                : "none",
             showTeammateMessagePreview: F8() ? !1 : void 0,
             selectedIPAgentIndex: -1,
             viewSelectionMode: "none",
@@ -1087,6 +1094,7 @@
                 agentDefinitions: h6,
               };
             if (qEA(e8.messages)) is();
+            PQA(H);
             let { waitUntilExit: nK } = await O9(
               MK.default.createElement(
                 SZ1,
@@ -1169,7 +1177,12 @@
             c("tengu_remote_create_session", {
               has_initial_prompt: String(B1),
             });
-            let X6 = await To4(B1 ? j1 : null, new AbortController().signal);
+            let p1 = await yM(),
+              O6 = await _o4(
+                x8 ? e : null,
+                new AbortController().signal,
+                p1 || void 0,
+              );
             if (!X6)
               (c("tengu_remote_create_session_error", {
                 error: "unable_to_create_session",
@@ -1217,7 +1230,8 @@
                 "info",
               ),
               hA = B1 ? p6({ content: j1 }) : null,
-              V8 = { ...uH, remoteSessionUrl: VA };
+              v8 = { ...A3, remoteSessionUrl: fA },
+              sA = BHq($6);
             (await O9(
               MK.default.createElement(
                 SZ1,
@@ -1392,40 +1406,44 @@
                 ...(B1 && { agent: B1 }),
                 ...(m1 && { standaloneAgentContext: m1 }),
                 agentDefinitions: h6,
-              },
-              { waitUntilExit: g6 } = await O9(
+              };
+            PQA(H);
+            let { waitUntilExit: V6 } = await s5(
+              x5.default.createElement(
+                yZ1,
+                { getFpsMetrics: U9 },
                 MK.default.createElement(
                   SZ1,
-                  { getFpsMetrics: J2 },
-                  MK.default.createElement(
-                    YY,
-                    { initialState: N6, onChangeAppState: xm },
-                    MK.default.createElement(b91, {
-                      debug: _ || J,
-                      commands: [...q6, ...h5],
-                      initialTools: R7,
-                      initialMessages: e8,
-                      initialFileHistorySnapshots: E4,
-                      initialAgentName: $4,
-                      initialAgentColor: uq,
-                      mcpClients: HY,
-                      dynamicMcpConfig: X1,
-                      mcpCliEndpoint: I5,
-                      autoConnectIdeFlag: T,
-                      strictMcpConfig: e1,
-                      systemPrompt: _1,
-                      appendSystemPrompt: O1,
-                      mainThreadAgentDefinition: LA,
-                      disableSlashCommands: f1,
-                      taskListId: H1,
-                    }),
-                  ),
+                  { initialState: O6, onChangeAppState: xI },
+                  x5.default.createElement(h91, {
+                    debug: $ || O,
+                    commands: [...$6, ...Lz],
+                    initialTools: Ow,
+                    initialMessages: w8,
+                    initialFileHistorySnapshots: jq,
+                    initialAgentName: g4,
+                    initialAgentColor: T4,
+                    mcpClients: B7,
+                    dynamicMcpConfig: L1,
+                    mcpCliEndpoint: T3,
+                    autoConnectIdeFlag: Z,
+                    strictMcpConfig: T1,
+                    systemPrompt: H1,
+                    appendSystemPrompt: o,
+                    mainThreadAgentDefinition: i6,
+                    disableSlashCommands: c,
+                    taskListId: f1,
+                  }),
                 ),
-                OY,
-              );
+              ),
+              lY,
+            );
             (m91(), await g6(), await $K(0));
           } else {
-            let B1 = await Gm(N8());
+            let [x8, { ResumeConversation: F1 }] = await Promise.all([
+              Bd(R8()),
+              Promise.resolve().then(() => (bEq(), xEq)),
+            ]);
             (await O9(
               MK.default.createElement(
                 SZ1,
@@ -1463,7 +1481,7 @@
           }
         } else {
           if (K7 && FK.length === 0) FK = await K7;
-          Vq("action_after_hooks");
+          (TK("action_after_hooks"), PQA(H));
           let { waitUntilExit: RA } = await O9(
             MK.default.createElement(
               SZ1,
@@ -1495,7 +1513,7 @@
         }
       })
       .version(
-        `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.32", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-05T17:02:01Z" }.VERSION} (Claude Code)`,
+        `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.33", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-02-06T00:14:56Z" }.VERSION} (Claude Code)`,
         "-v, --version",
         "Output the version number",
       ),
@@ -1568,17 +1586,10 @@
     .option("-d, --debug", "Enable debug mode", () => !0)
     .option("--verbose", "Override verbose mode setting from config", () => !0)
     .action(async ({ debug: O, verbose: $ }) => {
-      let _ = mFA();
-      if ((c("tengu_mcp_start", {}), !FFA(_)))
-        (console.error(`Error: Directory ${_} does not exist`),
-          process.exit(1));
-      try {
-        (await nT6(_, "default", !1, !1, void 0, !1),
-          await eVq(_, O ?? !1, $ ?? !1));
-      } catch (J) {
-        (console.error("Error: Failed to start MCP server:", J),
-          process.exit(1));
-      }
+      let { mcpServeHandler: $ } = await Promise.resolve().then(
+        () => (he(), Se),
+      );
+      await $({ debug: w, verbose: H });
     }),
     lTq(K),
     K.command("remove <name>")
@@ -1589,162 +1600,28 @@
       )
       .helpOption("-h, --help", "Display help for command")
       .action(async (O, $) => {
-        let _ = fR(O),
-          J = () => {
-            if (_ && (_.type === "sse" || _.type === "http"))
-              (RP6(O, _), Zs4(O, _));
-          };
-        try {
-          if ($.scope) {
-            let G = $G1($.scope);
-            (c("tengu_mcp_delete", { name: O, scope: G }),
-              yLA(O, G),
-              J(),
-              process.stdout.write(`Removed MCP server ${O} from ${G} config
-`),
-              process.stdout.write(`File modified: ${VG(G)}
-`),
-              process.exit(0));
-          }
-          let X = SY(),
-            D = M6(),
-            { servers: j } = ZJ("project"),
-            M = !!j[O],
-            W = [];
-          if (X.mcpServers?.[O]) W.push("local");
-          if (M) W.push("project");
-          if (D.mcpServers?.[O]) W.push("user");
-          if (W.length === 0)
-            (process.stderr.write(`No MCP server found with name: "${O}"
-`),
-              process.exit(1));
-          else if (W.length === 1) {
-            let G = W[0];
-            (c("tengu_mcp_delete", { name: O, scope: G }),
-              yLA(O, G),
-              J(),
-              process.stdout.write(`Removed MCP server "${O}" from ${G} config
-`),
-              process.stdout.write(`File modified: ${VG(G)}
-`),
-              process.exit(0));
-          } else
-            (process.stderr.write(`MCP server "${O}" exists in multiple scopes:
-`),
-              W.forEach((G) => {
-                process.stderr.write(`  - ${hQ1(G)} (${VG(G)})
-`);
-              }),
-              process.stderr.write(`
-To remove from a specific scope, use:
-`),
-              W.forEach((G) => {
-                process.stderr.write(`  claude mcp remove "${O}" -s ${G}
-`);
-              }),
-              process.exit(1));
-        } catch (X) {
-          (process.stderr.write(`${X.message}
-`),
-            process.exit(1));
-        }
+        let { mcpRemoveHandler: $ } = await Promise.resolve().then(
+          () => (he(), Se),
+        );
+        await $(w, H);
       }),
     K.command("list")
       .description("List configured MCP servers")
       .helpOption("-h, --help", "Display help for command")
       .action(async () => {
-        c("tengu_mcp_list", {});
-        let { servers: O } = await _d();
-        if (Object.keys(O).length === 0)
-          console.log(
-            "No MCP servers configured. Use `claude mcp add` to add a server.",
-          );
-        else {
-          console.log(`Checking MCP server health...
-`);
-          let $ = Object.entries(O),
-            _ = await PBA(
-              $,
-              async ([J, X]) => ({
-                name: J,
-                server: X,
-                status: await aTq(J, X),
-              }),
-              { concurrency: LCA() },
-            );
-          for (let { name: J, server: X, status: D } of _)
-            if (X.type === "sse") console.log(`${J}: ${X.url} (SSE) - ${D}`);
-            else if (X.type === "http")
-              console.log(`${J}: ${X.url} (HTTP) - ${D}`);
-            else if (X.type === "claudeai-proxy")
-              console.log(`${J}: ${X.url} - ${D}`);
-            else if (!X.type || X.type === "stdio") {
-              let j = Array.isArray(X.args) ? X.args : [];
-              console.log(`${J}: ${X.command} ${j.join(" ")} - ${D}`);
-            }
-        }
-        await $K(0);
+        let { mcpListHandler: w } = await Promise.resolve().then(
+          () => (he(), Se),
+        );
+        await w();
       }),
     K.command("get <name>")
       .description("Get details about an MCP server")
       .helpOption("-h, --help", "Display help for command")
       .action(async (O) => {
-        c("tengu_mcp_get", { name: O });
-        let $ = fR(O);
-        if (!$)
-          (console.error(`No MCP server found with name: ${O}`),
-            process.exit(1));
-        (console.log(`${O}:`), console.log(`  Scope: ${hQ1($.scope)}`));
-        let _ = await aTq(O, $);
-        if ((console.log(`  Status: ${_}`), $.type === "sse")) {
-          if (
-            (console.log("  Type: sse"),
-            console.log(`  URL: ${$.url}`),
-            $.headers)
-          ) {
-            console.log("  Headers:");
-            for (let [J, X] of Object.entries($.headers))
-              console.log(`    ${J}: ${X}`);
-          }
-          if ($.oauth?.clientId) {
-            let X = !!TCA(O, $)?.clientSecret,
-              D = ["client_id configured"];
-            if (X) D.push("client_secret configured");
-            if ($.oauth.callbackPort)
-              D.push(`callback_port ${$.oauth.callbackPort}`);
-            console.log(`  OAuth: ${D.join(", ")}`);
-          }
-        } else if ($.type === "http") {
-          if (
-            (console.log("  Type: http"),
-            console.log(`  URL: ${$.url}`),
-            $.headers)
-          ) {
-            console.log("  Headers:");
-            for (let [J, X] of Object.entries($.headers))
-              console.log(`    ${J}: ${X}`);
-          }
-          if ($.oauth?.clientId) {
-            let X = !!TCA(O, $)?.clientSecret,
-              D = ["client_id configured"];
-            if (X) D.push("client_secret configured");
-            if ($.oauth.callbackPort)
-              D.push(`callback_port ${$.oauth.callbackPort}`);
-            console.log(`  OAuth: ${D.join(", ")}`);
-          }
-        } else if ($.type === "stdio") {
-          (console.log("  Type: stdio"),
-            console.log(`  Command: ${$.command}`));
-          let J = Array.isArray($.args) ? $.args : [];
-          if ((console.log(`  Args: ${J.join(" ")}`), $.env)) {
-            console.log("  Environment:");
-            for (let [X, D] of Object.entries($.env))
-              console.log(`    ${X}=${D}`);
-          }
-        }
-        (console.log(`
-To remove this server, run: claude mcp remove "${O}" -s ${$.scope}`),
-          await $K(0));
+        let { mcpGetHandler: H } = await Promise.resolve().then(
+          () => (he(), Se),
+        );
+        await H(w);
       }),
     K.command("add-json <name> <json>")
       .description("Add an MCP server (stdio or SSE) with a JSON string")
@@ -1759,44 +1636,10 @@
       )
       .helpOption("-h, --help", "Display help for command")
       .action(async (O, $, _) => {
-        try {
-          let J = $G1(_.scope),
-            X = f5($),
-            j =
-              _.clientSecret &&
-              X &&
-              typeof X === "object" &&
-              "type" in X &&
-              (X.type === "sse" || X.type === "http") &&
-              "url" in X &&
-              typeof X.url === "string" &&
-              "oauth" in X &&
-              X.oauth &&
-              typeof X.oauth === "object" &&
-              "clientId" in X.oauth
-                ? await bg1()
-                : void 0;
-          wt(O, X, J);
-          let M =
-            X && typeof X === "object" && "type" in X
-              ? String(X.type || "stdio")
-              : "stdio";
-          if (
-            j &&
-            X &&
-            typeof X === "object" &&
-            "type" in X &&
-            (X.type === "sse" || X.type === "http") &&
-            "url" in X &&
-            typeof X.url === "string"
-          )
-            ug1(O, { type: X.type, url: X.url }, j);
-          (c("tengu_mcp_add", { scope: J, source: "json", type: M }),
-            console.log(`Added ${M} MCP server ${O} to ${J} config`),
-            process.exit(0));
-        } catch (J) {
-          (console.error(J.message), process.exit(1));
-        }
+        let { mcpAddJsonHandler: O } = await Promise.resolve().then(
+          () => (he(), Se),
+        );
+        await O(w, H, $);
       }),
     K.command("add-from-claude-desktop")
       .description("Import MCP servers from Claude Desktop (Mac and WSL only)")
@@ -1807,37 +1650,10 @@
       )
       .helpOption("-h, --help", "Display help for command")
       .action(async (O) => {
-        try {
-          let $ = $G1(O.scope),
-            _ = iA();
-          c("tengu_mcp_add", { scope: $, platform: _, source: "desktop" });
-          let J = PVq();
-          if (Object.keys(J).length === 0)
-            (console.log(
-              "No MCP servers found in Claude Desktop configuration or configuration file does not exist.",
-            ),
-              process.exit(0));
-          let { unmount: X } = await O9(
-            MK.default.createElement(
-              YY,
-              null,
-              MK.default.createElement(
-                x2,
-                null,
-                MK.default.createElement(MVq, {
-                  servers: J,
-                  scope: $,
-                  onDone: () => {
-                    X();
-                  },
-                }),
-              ),
-            ),
-            { exitOnCtrlC: !0 },
-          );
-        } catch ($) {
-          (console.error($.message), process.exit(1));
-        }
+        let { mcpAddFromDesktopHandler: H } = await Promise.resolve().then(
+          () => (he(), Se),
+        );
+        await H(w);
       }),
     K.command("reset-project-choices")
       .description(
@@ -1845,76 +1661,27 @@
       )
       .helpOption("-h, --help", "Display help for command")
       .action(async () => {
-        (c("tengu_mcp_reset_mcpjson_choices", {}),
-          R2((O) => ({
-            ...O,
-            enabledMcpjsonServers: [],
-            disabledMcpjsonServers: [],
-            enableAllProjectMcpServers: !1,
-          })),
-          console.log(
-            "All project-scoped (.mcp.json) server approvals and rejections have been reset.",
-          ),
-          console.log(
-            "You will be prompted for approval next time you start Claude Code.",
-          ),
-          process.exit(0));
+        let { mcpResetChoicesHandler: w } = await Promise.resolve().then(
+          () => (he(), Se),
+        );
+        await w();
       }));
-  function Y(O, $) {
-    (K1(O instanceof Error ? O : Error(String(O))),
-      console.error(
-        `${n1.cross} Failed to ${$}: ${O instanceof Error ? O.message : String(O)}`,
-      ),
-      process.exit(1));
-  }
   let z = q
     .command("plugin")
     .description("Manage Claude Code plugins")
     .helpOption("-h, --help", "Display help for command")
     .configureHelp(A());
-  (z
-    .command("validate <path>")
+  (Y.command("validate <path>")
     .description("Validate a plugin or marketplace manifest")
     .addOption(new D5("--cowork", "Use cowork_plugins directory").hideHelp())
     .helpOption("-h, --help", "Display help for command")
-    .action((O, $) => {
-      if ($.cowork) QN(!0);
-      try {
-        let _ = ff6(O);
-        if (
-          (console.log(`Validating ${_.fileType} manifest: ${_.filePath}
-`),
-          _.errors.length > 0)
-        )
-          (console.log(`${n1.cross} Found ${_.errors.length} error${_.errors.length === 1 ? "" : "s"}:
-`),
-            _.errors.forEach((J) => {
-              console.log(`  ${n1.pointer} ${J.path}: ${J.message}`);
-            }),
-            console.log(""));
-        if (_.warnings.length > 0)
-          (console.log(`${n1.warning} Found ${_.warnings.length} warning${_.warnings.length === 1 ? "" : "s"}:
-`),
-            _.warnings.forEach((J) => {
-              console.log(`  ${n1.pointer} ${J.path}: ${J.message}`);
-            }),
-            console.log(""));
-        if (_.success) {
-          if (_.warnings.length > 0)
-            console.log(`${n1.tick} Validation passed with warnings`);
-          else console.log(`${n1.tick} Validation passed`);
-          process.exit(0);
-        } else (console.log(`${n1.cross} Validation failed`), process.exit(1));
-      } catch (_) {
-        (K1(_ instanceof Error ? _ : Error(String(_))),
-          console.error(
-            `${n1.cross} Unexpected error during validation: ${_ instanceof Error ? _.message : String(_)}`,
-          ),
-          process.exit(2));
-      }
+    .action(async (w, H) => {
+      let { pluginValidateHandler: $ } = await Promise.resolve().then(
+        () => ($y(), Hy),
+      );
+      $(w, H);
     }),
-    z
-      .command("list")
+    Y.command("list")
       .description("List installed plugins")
       .option("--json", "Output as JSON")
       .option(
@@ -1924,140 +1691,27 @@
       .addOption(new D5("--cowork", "Use cowork_plugins directory").hideHelp())
       .helpOption("-h, --help", "Display help for command")
       .action(async (O) => {
-        if (O.cowork) QN(!0);
-        c("tengu_plugin_list_command", {});
-        let $ = DM(),
-          _ = c51(),
-          J = Object.keys($.plugins);
-        if (O.json) {
-          let { enabled: D, disabled: j, errors: M } = await uY(),
-            W = [...D, ...j],
-            G = new Map(W.map((V) => [V.source, V])),
-            P = [];
-          for (let V of J.sort()) {
-            let Z = $.plugins[V];
-            if (!Z || Z.length === 0) continue;
-            let N = V.split("@")[0],
-              T = M.filter(
-                (k) => k.source === V || ("plugin" in k && k.plugin === N),
-              ).map(rP);
-            for (let k of Z) {
-              let y = G.get(V),
-                u;
-              if (y) {
-                let S = y.mcpServers || (await HjA(y));
-                if (S && Object.keys(S).length > 0) u = S;
-              }
-              P.push({
-                id: V,
-                version: k.version || "unknown",
-                scope: k.scope,
-                enabled: _.has(V),
-                installPath: k.installPath,
-                installedAt: k.installedAt,
-                lastUpdated: k.lastUpdated,
-                projectPath: k.projectPath,
-                mcpServers: u,
-                errors: T.length > 0 ? T : void 0,
-              });
-            }
-          }
-          if (O.available) {
-            let V = [];
-            try {
-              let [Z, N] = await Promise.all([g5(), LP1()]),
-                { marketplaces: T } = await mU(Z);
-              for (let { name: k, data: y } of T)
-                if (y)
-                  for (let u of y.plugins) {
-                    let S = pu(u.name, k);
-                    if (!jM(S))
-                      V.push({
-                        pluginId: S,
-                        name: u.name,
-                        description: u.description,
-                        marketplaceName: k,
-                        version: u.version,
-                        source: u.source,
-                        installCount: N?.get(S),
-                      });
-                  }
-            } catch {}
-            console.log(g1({ installed: P, available: V }, null, 2));
-          } else console.log(g1(P, null, 2));
-          process.exit(0);
-        }
-        if (J.length === 0)
-          (console.log(
-            "No plugins installed. Use `claude plugin install` to install a plugin.",
-          ),
-            process.exit(0));
-        let { errors: X } = await uY();
-        console.log(`Installed plugins:
-`);
-        for (let D of J.sort()) {
-          let j = $.plugins[D];
-          if (!j || j.length === 0) continue;
-          let M = D.split("@")[0],
-            W = X.filter(
-              (G) => G.source === D || ("plugin" in G && G.plugin === M),
-            );
-          for (let G of j) {
-            let P = _.has(D),
-              V =
-                W.length > 0
-                  ? `${n1.cross} failed to load`
-                  : P
-                    ? `${n1.tick} enabled`
-                    : `${n1.cross} disabled`,
-              Z = G.version || "unknown",
-              N = G.scope;
-            (console.log(`  ${n1.pointer} ${D}`),
-              console.log(`    Version: ${Z}`),
-              console.log(`    Scope: ${N}`),
-              console.log(`    Status: ${V}`));
-            for (let T of W) console.log(`    Error: ${rP(T)}`);
-            console.log("");
-          }
-        }
-        process.exit(0);
+        let { pluginListHandler: H } = await Promise.resolve().then(
+          () => ($y(), Hy),
+        );
+        await H(w);
       }));
-  let w = z
-    .command("marketplace")
+  let z = Y.command("marketplace")
     .description("Manage Claude Code marketplaces")
     .helpOption("-h, --help", "Display help for command")
     .configureHelp(A());
-  (w
-    .command("add <source>")
-    .description("Add a marketplace from a URL, path, or GitHub repo")
-    .addOption(new D5("--cowork", "Use cowork_plugins directory").hideHelp())
-    .helpOption("-h, --help", "Display help for command")
-    .action(async (O, $) => {
-      if ($.cowork) QN(!0);
-      try {
-        let _ = Of6(O);
-        if (!_)
-          (console.error(
-            `${n1.cross} Invalid marketplace source format. Try: owner/repo, https://..., or ./path`,
-          ),
-            process.exit(1));
-        if ("error" in _)
-          (console.error(`${n1.cross} ${_.error}`), process.exit(1));
-        let J = _;
-        console.log("Adding marketplace...");
-        let { name: X } = await mv(J, (j) => {
-          console.log(j);
-        });
-        iw();
-        let D = J.source;
-        if (J.source === "github") D = J.repo;
-        (c("tengu_marketplace_added", { source_type: D }),
-          console.log(`${n1.tick} Successfully added marketplace: ${X}`),
-          process.exit(0));
-      } catch (_) {
-        Y(_, "add marketplace");
-      }
-    }),
+  return (
+    z
+      .command("add <source>")
+      .description("Add a marketplace from a URL, path, or GitHub repo")
+      .addOption(new W5("--cowork", "Use cowork_plugins directory").hideHelp())
+      .helpOption("-h, --help", "Display help for command")
+      .action(async (w, H) => {
+        let { marketplaceAddHandler: $ } = await Promise.resolve().then(
+          () => ($y(), Hy),
+        );
+        await $(w, H);
+      }),
     w
       .command("list")
       .description("List all configured marketplaces")
@@ -2065,52 +1719,10 @@
       .addOption(new D5("--cowork", "Use cowork_plugins directory").hideHelp())
       .helpOption("-h, --help", "Display help for command")
       .action(async (O) => {
-        if (O.cowork) QN(!0);
-        try {
-          let $ = await g5(),
-            _ = Object.keys($);
-          if (O.json) {
-            let J = _.sort().map((X) => {
-              let D = $[X],
-                j = D?.source;
-              return {
-                name: X,
-                source: j?.source,
-                ...(j?.source === "github" && { repo: j.repo }),
-                ...(j?.source === "git" && { url: j.url }),
-                ...(j?.source === "url" && { url: j.url }),
-                ...(j?.source === "directory" && { path: j.path }),
-                ...(j?.source === "file" && { path: j.path }),
-                installLocation: D?.installLocation,
-              };
-            });
-            (console.log(g1(J, null, 2)), process.exit(0));
-          }
-          if (_.length === 0)
-            (console.log("No marketplaces configured"), process.exit(0));
-          (console.log(`Configured marketplaces:
-`),
-            _.forEach((J) => {
-              let X = $[J];
-              if ((console.log(`  ${n1.pointer} ${J}`), X?.source)) {
-                let D = X.source;
-                if (D.source === "github")
-                  console.log(`    Source: GitHub (${D.repo})`);
-                else if (D.source === "git")
-                  console.log(`    Source: Git (${D.url})`);
-                else if (D.source === "url")
-                  console.log(`    Source: URL (${D.url})`);
-                else if (D.source === "directory")
-                  console.log(`    Source: Directory (${D.path})`);
-                else if (D.source === "file")
-                  console.log(`    Source: File (${D.path})`);
-              }
-              console.log("");
-            }),
-            process.exit(0));
-        } catch ($) {
-          Y($, "list marketplaces");
-        }
+        let { marketplaceListHandler: H } = await Promise.resolve().then(
+          () => ($y(), Hy),
+        );
+        await H(w);
       }),
     w
       .command("remove <name>")
@@ -2119,16 +1731,10 @@
       .addOption(new D5("--cowork", "Use cowork_plugins directory").hideHelp())
       .helpOption("-h, --help", "Display help for command")
       .action(async (O, $) => {
-        if ($.cowork) QN(!0);
-        try {
-          (await KP6(O),
-            iw(),
-            c("tengu_marketplace_removed", { marketplace_name: O }),
-            console.log(`${n1.tick} Successfully removed marketplace: ${O}`),
-            process.exit(0));
-        } catch (_) {
-          Y(_, "remove marketplace");
-        }
+        let { marketplaceRemoveHandler: $ } = await Promise.resolve().then(
+          () => ($y(), Hy),
+        );
+        await $(w, H);
       }),
     w
       .command("update [name]")
@@ -2138,37 +1744,12 @@
       .addOption(new D5("--cowork", "Use cowork_plugins directory").hideHelp())
       .helpOption("-h, --help", "Display help for command")
       .action(async (O, $) => {
-        if ($.cowork) QN(!0);
-        try {
-          if (O)
-            (console.log(`Updating marketplace: ${O}...`),
-              await Nt(O, (_) => {
-                console.log(_);
-              }),
-              iw(),
-              c("tengu_marketplace_updated", { marketplace_name: O }),
-              console.log(`${n1.tick} Successfully updated marketplace: ${O}`),
-              process.exit(0));
-          else {
-            let _ = await g5(),
-              J = Object.keys(_);
-            if (J.length === 0)
-              (console.log("No marketplaces configured"), process.exit(0));
-            (console.log(`Updating ${J.length} marketplace(s)...`),
-              await co4(),
-              iw(),
-              c("tengu_marketplace_updated_all", { count: J.length }),
-              console.log(
-                `${n1.tick} Successfully updated ${J.length} marketplace(s)`,
-              ),
-              process.exit(0));
-          }
-        } catch (_) {
-          Y(_, "update marketplace(s)");
-        }
+        let { marketplaceUpdateHandler: $ } = await Promise.resolve().then(
+          () => ($y(), Hy),
+        );
+        await $(w, H);
       }),
-    z
-      .command("install <plugin>")
+    Y.command("install <plugin>")
       .alias("i")
       .description(
         "Install a plugin from available marketplaces (use plugin@marketplace for specific marketplace)",
@@ -2181,21 +1762,12 @@
       .addOption(new D5("--cowork", "Use cowork_plugins directory").hideHelp())
       .helpOption("-h, --help", "Display help for command")
       .action(async (O, $) => {
-        if ($.cowork) QN(!0);
-        let _ = $.scope || "user";
-        if ($.cowork && _ !== "user")
-          (console.error("--cowork can only be used with user scope"),
-            process.exit(1));
-        if (!SZ.includes(_))
-          (console.error(
-            `Invalid scope: ${_}. Must be one of: ${SZ.join(", ")}.`,
-          ),
-            process.exit(1));
-        (c("tengu_plugin_install_command", { plugin: O, scope: _ }),
-          await qNq(O, _));
+        let { pluginInstallHandler: $ } = await Promise.resolve().then(
+          () => ($y(), Hy),
+        );
+        await $(w, H);
       }),
-    z
-      .command("uninstall <plugin>")
+    Y.command("uninstall <plugin>")
       .alias("remove")
       .alias("rm")
       .description("Uninstall an installed plugin")
@@ -2207,21 +1779,12 @@
       .addOption(new D5("--cowork", "Use cowork_plugins directory").hideHelp())
       .helpOption("-h, --help", "Display help for command")
       .action(async (O, $) => {
-        if ($.cowork) QN(!0);
-        let _ = $.scope || "user";
-        if ($.cowork && _ !== "user")
-          (console.error("--cowork can only be used with user scope"),
-            process.exit(1));
-        if (!SZ.includes(_))
-          (console.error(
-            `Invalid scope: ${_}. Must be one of: ${SZ.join(", ")}.`,
-          ),
-            process.exit(1));
-        (c("tengu_plugin_uninstall_command", { plugin: O, scope: _ }),
-          await KNq(O, _));
+        let { pluginUninstallHandler: $ } = await Promise.resolve().then(
+          () => ($y(), Hy),
+        );
+        await $(w, H);
       }),
-    z
-      .command("enable <plugin>")
+    Y.command("enable <plugin>")
       .description("Enable a disabled plugin")
       .option(
         "-s, --scope <scope>",
@@ -2230,24 +1793,12 @@
       .addOption(new D5("--cowork", "Use cowork_plugins directory").hideHelp())
       .helpOption("-h, --help", "Display help for command")
       .action(async (O, $) => {
-        if ($.cowork) QN(!0);
-        let _ = "user";
-        if ($.scope) {
-          if (!SZ.includes($.scope))
-            (process.stderr
-              .write(`Invalid scope "${$.scope}". Valid scopes: ${SZ.join(", ")}
-`),
-              process.exit(1));
-          _ = $.scope;
-        }
-        if ($.cowork && _ !== "user")
-          (console.error("--cowork can only be used with user scope"),
-            process.exit(1));
-        (c("tengu_plugin_enable_command", { plugin: O, scope: _ }),
-          await YNq(O, _));
+        let { pluginEnableHandler: $ } = await Promise.resolve().then(
+          () => ($y(), Hy),
+        );
+        await $(w, H);
       }),
-    z
-      .command("disable [plugin]")
+    Y.command("disable [plugin]")
       .description("Disable an enabled plugin")
       .option("-a, --all", "Disable all enabled plugins")
       .option(
@@ -2257,41 +1808,12 @@
       .addOption(new D5("--cowork", "Use cowork_plugins directory").hideHelp())
       .helpOption("-h, --help", "Display help for command")
       .action(async (O, $) => {
-        if ($.all && O)
-          (process.stderr.write(`Cannot use --all with a specific plugin
-`),
-            process.exit(1));
-        if (!$.all && !O)
-          (process.stderr
-            .write(`Please specify a plugin name or use --all to disable all plugins
-`),
-            process.exit(1));
-        if ($.cowork) QN(!0);
-        if ($.all) {
-          if ($.scope)
-            (process.stderr.write(`Cannot use --scope with --all
-`),
-              process.exit(1));
-          (c("tengu_plugin_disable_command", { plugin: "--all" }), await wNq());
-          return;
-        }
-        let _ = "user";
-        if ($.scope) {
-          if (!SZ.includes($.scope))
-            (process.stderr
-              .write(`Invalid scope "${$.scope}". Valid scopes: ${SZ.join(", ")}
-`),
-              process.exit(1));
-          _ = $.scope;
-        }
-        if ($.cowork && _ !== "user")
-          (console.error("--cowork can only be used with user scope"),
-            process.exit(1));
-        (c("tengu_plugin_disable_command", { plugin: O, scope: _ }),
-          await zNq(O, _));
+        let { pluginDisableHandler: $ } = await Promise.resolve().then(
+          () => ($y(), Hy),
+        );
+        await $(w, H);
       }),
-    z
-      .command("update <plugin>")
+    Y.command("update <plugin>")
       .description(
         "Update a plugin to the latest version (restart required to apply)",
       )
@@ -2302,20 +1824,9 @@
       .addOption(new D5("--cowork", "Use cowork_plugins directory").hideHelp())
       .helpOption("-h, --help", "Display help for command")
       .action(async (O, $) => {
-        if ($.cowork) QN(!0);
-        c("tengu_plugin_update_command", {});
-        let _ = "user";
-        if ($.scope) {
-          if (!CU1.includes($.scope))
-            (process.stderr
-              .write(`Invalid scope "${$.scope}". Valid scopes: ${CU1.join(", ")}
-`),
-              process.exit(1));
-          _ = $.scope;
-        }
-        if ($.cowork && _ !== "user")
-          (console.error("--cowork can only be used with user scope"),
-            process.exit(1));
+        let { pluginUpdateHandler: $ } = await Promise.resolve().then(
+          () => ($y(), Hy),
+        );
         await HNq(O, _);
       }),
     q
@@ -2325,87 +1836,30 @@
       )
       .helpOption("-h, --help", "Display help for command")
       .action(async () => {
-        if ((c("tengu_setup_token_command", {}), await o41(), !lf()))
-          (process.stderr.write(
-            Y6.yellow(`Warning: You already have authentication configured via environment variable or API key helper.
-`),
-          ),
-            process.stderr.write(
-              Y6.yellow(`The setup-token command will create a new OAuth token which you can use instead.
-`),
-            ));
-        (await new Promise(async (O) => {
-          let { unmount: $ } = await O9(
-            MK.default.createElement(
-              YY,
-              { onChangeAppState: xm },
-              MK.default.createElement(
-                I,
-                { flexDirection: "column", gap: 1 },
-                MK.default.createElement(FT6, null),
-                MK.default.createElement(Is, {
-                  onDone: () => {
-                    ($(), O());
-                  },
-                  mode: "setup-token",
-                  startingMessage:
-                    "This will guide you through long-lived (1-year) auth token setup for your Claude account. Claude subscription required.",
-                }),
-              ),
-            ),
-          );
-        }),
-          process.exit(0));
-      }));
-  function H(O) {
-    let $ = A1(2),
-      { onDone: _ } = O;
-    _T6();
-    let J;
-    if ($[0] !== _)
-      ((J = MK.default.createElement(rZ6, { onDone: _ })),
-        ($[0] = _),
-        ($[1] = J));
-    else J = $[1];
-    return J;
-  }
-  return (
+        let { setupTokenHandler: w } = await Promise.resolve().then(
+          () => (Dv6(), Xv6),
+        );
+        await w();
+      }),
     q
       .command("doctor")
       .description("Check the health of your Claude Code auto-updater")
       .helpOption("-h, --help", "Display help for command")
       .action(async () => {
-        (c("tengu_doctor_command", {}),
-          await new Promise(async (O) => {
-            let { unmount: $ } = await O9(
-              MK.default.createElement(
-                YY,
-                null,
-                MK.default.createElement(
-                  x2,
-                  null,
-                  MK.default.createElement(
-                    Af6,
-                    { dynamicMcpConfig: void 0, isStrictMcpConfig: !1 },
-                    MK.default.createElement(H, {
-                      onDone: () => {
-                        ($(), O());
-                      },
-                    }),
-                  ),
-                ),
-              ),
-              Uw(!1),
-            );
-          }),
-          process.exit(0));
+        let { doctorHandler: w } = await Promise.resolve().then(
+          () => (Dv6(), Xv6),
+        );
+        await w();
       }),
     q
       .command("update")
       .alias("upgrade")
       .description("Check for updates and install if available")
       .helpOption("-h, --help", "Display help for command")
-      .action(VTq),
+      .action(async () => {
+        let { update: w } = await Promise.resolve().then(() => (sEq(), aEq));
+        await w();
+      }),
     q
       .command("install [target]")
       .description(
@@ -2414,19 +1868,10 @@
       .option("--force", "Force installation even if already installed")
       .helpOption("-h, --help", "Display help for command")
       .action(async (O, $) => {
-        (await nT6(mFA(), "default", !1, !1, void 0, !1),
-          await new Promise((_) => {
-            let J = [];
-            if (O) J.push(O);
-            if ($.force) J.push("--force");
-            ETq.call(
-              (X) => {
-                (_(), process.exit(X.includes("failed") ? 1 : 0));
-              },
-              {},
-              J,
-            );
-          }));
+        let { installHandler: $ } = await Promise.resolve().then(
+          () => (Dv6(), Xv6),
+        );
+        await $(w, H);
       }),
     Vq("run_before_parse"),
     await q.parseAsync(process.argv),

@@@ variable 'B7q' (was 'F8q') — structural (52.0%)
--- pretty-v2.1.32.js:469353
+++ pretty-v2.1.33.js:469411
@@ -39,18 +39,4 @@
       selectedApiKeyOption: "new",
       authType: "api_key",
     }));
-  ((GiY = {
-    type: "local-jsx",
-    name: "install-github-app",
-    description: "Set up Claude GitHub Actions for a repository",
-    isEnabled: () => !process.env.DISABLE_INSTALL_GITHUB_APP_COMMAND && !XC(),
-    isHidden: !1,
-    async call(A) {
-      return (B4("github-app"), MO.default.createElement(WiY, { onDone: A }));
-    },
-    userFacingName() {
-      return "install-github-app";
-    },
-  }),
-    (m8q = GiY));
 });

@@@ variable 'g8q' (was 'nAq') — structural (50.8%)
--- pretty-v2.1.32.js:466333
+++ pretty-v2.1.33.js:466358
@@ -1,7 +1,5 @@
 var nAq = v(() => {
   en();
-  lAq();
-  Dm();
   ((wiY = {
     name: "keybindings",
     description: "Open or create your keybindings configuration file",
@@ -9,8 +7,8 @@
     isHidden: !1,
     supportsNonInteractive: !1,
     type: "local",
+    load: () => Promise.resolve().then(() => (U8q(), Q8q)),
     userFacingName: () => "keybindings",
-    call: ziY,
   }),
     (iAq = wiY));
 });

@@@ variable 'xb1' (was '_j1') — structural (50.7%)
--- pretty-v2.1.32.js:297297
+++ pretty-v2.1.33.js:259347
@@ -21,10 +21,9 @@
       OJ,
       P0,
       XM,
-      BV,
       ...[],
       wB,
     ])),
     (O94 = new Set([dS, eq1, AK1, aL])),
-    (U$6 = new Set([BV, wB, dS, eq1, AK1, aL, OK])));
+    (m$6 = new Set([aS, yq1, $B, rS, Cq1, Sq1, cL, XK])));
 });

@@@ variable 'w2q' (was 'hYq') — structural (50.6%)
--- pretty-v2.1.32.js:501264
+++ pretty-v2.1.33.js:501409
@@ -1,19 +1,15 @@
 var hYq = v(() => {
-  YIA();
-  ((wbA = a($1(), 1)),
-    (zAz = {
-      type: "local-jsx",
-      name: "plugin",
-      aliases: ["plugins", "marketplace"],
-      description: "Manage Claude Code plugins",
-      isEnabled: () => !0,
-      isHidden: !1,
-      async call(A, q, K) {
-        return wbA.createElement(x7q, { onComplete: A, args: K });
-      },
-      userFacingName() {
-        return "plugin";
-      },
-    }),
+  ((h7z = {
+    type: "local-jsx",
+    name: "plugin",
+    aliases: ["plugins", "marketplace"],
+    description: "Manage Claude Code plugins",
+    isEnabled: () => !0,
+    isHidden: !1,
+    load: () => Promise.resolve().then(() => (Y2q(), K2q)),
+    userFacingName() {
+      return "plugin";
+    },
+  }),
     (SYq = zAz));
 });

@@@ variable 'G9q' (was 'Y5q') — structural (49.4%)
--- pretty-v2.1.32.js:491567
+++ pretty-v2.1.33.js:491678
@@ -1,23 +1,15 @@
 var Y5q = v(() => {
-  RxA();
-  ((yxA = a($1(), 1)),
-    (K1z = {
-      type: "local-jsx",
-      name: "tasks",
-      aliases: ["bashes"],
-      description: "List and manage background tasks",
-      isEnabled: () => !0,
-      isHidden: !1,
-      async call(A, q) {
-        return yxA.createElement(tf6, {
-          toolUseContext: q,
-          onDone: A,
-          onForegroundTask: q.onForegroundTask,
-        });
-      },
-      userFacingName() {
-        return "tasks";
-      },
-    }),
+  ((NAz = {
+    type: "local-jsx",
+    name: "tasks",
+    aliases: ["bashes"],
+    description: "List and manage background tasks",
+    isEnabled: () => !0,
+    isHidden: !1,
+    load: () => Promise.resolve().then(() => (j9q(), M9q)),
+    userFacingName() {
+      return "tasks";
+    },
+  }),
     (K5q = K1z));
 });

@@@ variable '_2q' (was 'xYq') — structural (48.9%)
--- pretty-v2.1.32.js:501284
+++ pretty-v2.1.33.js:501434
@@ -1,5 +1,4 @@
 var xYq = v(() => {
-  vz();
   ((wAz = {
     description: "Restore the code and/or conversation to a previous point",
     name: "rewind",
@@ -10,10 +9,7 @@
     type: "local",
     isHidden: !1,
     supportsNonInteractive: !1,
-    async call(A, q) {
-      if ((B4("rewind"), q.openMessageSelector)) q.openMessageSelector();
-      return { type: "skip" };
-    },
+    load: () => Promise.resolve().then(() => ($2q(), H2q)),
   }),
     (IYq = wAz));
 });

@@@ class '_P6' (was 'WP6') — structural (48.2%)
--- pretty-v2.1.32.js:443840
+++ pretty-v2.1.33.js:441401
@@ -2,50 +2,106 @@
   ws;
   started = !1;
   opened;
+  isBun = typeof Bun < "u";
   constructor(A) {
     this.ws = A;
-    ((this.opened = new Promise((q, K) => {
-      if (this.ws.readyState === FP.OPEN) q();
-      else
-        (this.ws.on("open", () => {
-          q();
-        }),
-          this.ws.on("error", (Y) => {
-            (W8("error", "mcp_websocket_connect_fail"), K(Y));
-          }));
-    })),
-      this.ws.on("message", this.onMessageHandler),
-      this.ws.on("error", this.onErrorHandler),
-      this.ws.on("close", this.onCloseHandler));
+    if (
+      ((this.opened = new Promise((q, K) => {
+        if (this.ws.readyState === OP6) q();
+        else if (this.isBun) {
+          let Y = this.ws,
+            z = () => {
+              (Y.removeEventListener("open", z),
+                Y.removeEventListener("error", w),
+                q());
+            },
+            w = (H) => {
+              (Y.removeEventListener("open", z),
+                Y.removeEventListener("error", w),
+                O8("error", "mcp_websocket_connect_fail"),
+                K(H));
+            };
+          (Y.addEventListener("open", z), Y.addEventListener("error", w));
+        } else {
+          let Y = this.ws;
+          (Y.on("open", () => {
+            q();
+          }),
+            Y.on("error", (z) => {
+              (O8("error", "mcp_websocket_connect_fail"), K(z));
+            }));
+        }
+      })),
+      this.isBun)
+    ) {
+      let q = this.ws;
+      (q.addEventListener("message", this.onBunMessage),
+        q.addEventListener("error", this.onBunError),
+        q.addEventListener("close", this.onBunClose));
+    } else {
+      let q = this.ws;
+      (q.on("message", this.onNodeMessage),
+        q.on("error", this.onNodeError),
+        q.on("close", this.onNodeClose));
+    }
   }
   onclose;
   onerror;
   onmessage;
-  onMessageHandler = (A) => {
+  onBunMessage = (A) => {
+    try {
+      let q = typeof A.data === "string" ? A.data : String(A.data),
+        K = MA(q),
+        Y = LS.parse(K);
+      this.onmessage?.(Y);
+    } catch (q) {
+      this.handleError(q);
+    }
+  };
+  onBunError = () => {
+    this.handleError(Error("WebSocket error"));
+  };
+  onBunClose = () => {
+    this.handleCloseCleanup();
+  };
+  onNodeMessage = (A) => {
     try {
       let q = JA(A.toString("utf-8")),
         K = uu.parse(q);
       this.onmessage?.(K);
     } catch (q) {
-      this.onErrorHandler(q);
+      this.handleError(q);
     }
   };
-  onErrorHandler = (A) => {
+  onNodeError = (A) => {
+    this.handleError(A);
+  };
+  onNodeClose = () => {
+    this.handleCloseCleanup();
+  };
+  handleError(A) {
     (W8("error", "mcp_websocket_message_fail"),
       this.onerror?.(
         A instanceof Error ? A : Error("Failed to process message"),
       ));
-  };
-  onCloseHandler = () => {
-    (this.onclose?.(),
-      this.ws.off("message", this.onMessageHandler),
-      this.ws.off("error", this.onErrorHandler),
-      this.ws.off("close", this.onCloseHandler));
-  };
+  }
+  handleCloseCleanup() {
+    if ((this.onclose?.(), this.isBun)) {
+      let A = this.ws;
+      (A.removeEventListener("message", this.onBunMessage),
+        A.removeEventListener("error", this.onBunError),
+        A.removeEventListener("close", this.onBunClose));
+    } else {
+      let A = this.ws;
+      (A.off("message", this.onNodeMessage),
+        A.off("error", this.onNodeError),
+        A.off("close", this.onNodeClose));
+    }
+  }
   async start() {
     if (this.started)
       throw Error("Start can only be called once per transport.");
-    if ((await this.opened, this.ws.readyState !== FP.OPEN))
+    if ((await this.opened, this.ws.readyState !== OP6))
       throw (
         W8("error", "mcp_websocket_start_not_opened"),
         Error("WebSocket is not open. Cannot start transport.")
@@ -53,26 +109,28 @@
     this.started = !0;
   }
   async close() {
-    if (this.ws.readyState === FP.OPEN || this.ws.readyState === FP.CONNECTING)
+    if (this.ws.readyState === OP6 || this.ws.readyState === XFY)
       this.ws.close();
-    this.onCloseHandler();
+    this.handleCloseCleanup();
   }
   async send(A) {
-    if (this.ws.readyState !== FP.OPEN)
+    if (this.ws.readyState !== OP6)
       throw (
         W8("error", "mcp_websocket_send_not_opened"),
         Error("WebSocket is not open. Cannot send message.")
       );
     let q = g1(A);
     try {
-      await new Promise((K, Y) => {
-        this.ws.send(q, (z) => {
-          if (z) Y(z);
-          else K();
+      if (this.isBun) this.ws.send(q);
+      else
+        await new Promise((K, Y) => {
+          this.ws.send(q, (z) => {
+            if (z) Y(z);
+            else K();
+          });
         });
-      });
     } catch (K) {
-      throw (this.onErrorHandler(K), K);
+      throw (this.handleError(K), K);
     }
   }
 }

@@@ function 'fXq' (was 'wJq') — structural (48.0%)
--- pretty-v2.1.32.js:536304
+++ pretty-v2.1.33.js:534711
@@ -1,9 +1,10 @@
 function wJq(A) {
-  let q = A1(7),
-    { tokenUsage: K } = A,
+  let q = q1(8),
+    { tokenUsage: K, model: Y } = A,
     Y;
-  if (q[0] !== K) ((Y = jd(K)), (q[0] = K), (q[1] = Y));
-  else Y = q[1];
+  if (q[0] !== Y || q[1] !== K)
+    ((z = Md(K, Y)), (q[0] = Y), (q[1] = K), (q[2] = z));
+  else z = q[2];
   let {
       percentLeft: z,
       isAboveWarningThreshold: w,
@@ -12,17 +13,17 @@
     O = xLA();
   if (!w || O) return null;
   let $;
-  if (q[2] === Symbol.for("react.memo_cache_sentinel"))
-    (($ = Md()), (q[2] = $));
-  else $ = q[2];
-  let _ = $,
-    J;
   if (q[3] === Symbol.for("react.memo_cache_sentinel"))
-    ((J = PK1("warning")), (q[3] = J));
+    ((_ = jd()), (q[3] = _));
   else J = q[3];
   let X = J,
     D;
-  if (q[4] !== H || q[5] !== z)
+  if (q[4] === Symbol.for("react.memo_cache_sentinel"))
+    ((X = AK1("warning")), (q[4] = X));
+  else X = q[4];
+  let D = X,
+    M;
+  if (q[5] !== $ || q[6] !== w)
     ((D = v91.createElement(
       I,
       { flexDirection: "row" },
@@ -42,9 +43,9 @@
               : `Context low (${z}% remaining) · Run /compact to compact & continue`,
           ),
     )),
-      (q[4] = H),
       (q[5] = z),
-      (q[6] = D));
-  else D = q[6];
+      (q[6] = w),
+      (q[7] = M));
+  else M = q[7];
   return D;
 }

@@@ variable 'm9q' (was 'IxA') — structural (47.1%)
--- pretty-v2.1.32.js:492453
+++ pretty-v2.1.33.js:492586
@@ -1,32 +1,12 @@
 var IxA = v(() => {
   d1();
-  g4();
-  u1();
-  hq();
-  d_1();
-  u3();
-  Rq();
-  k5();
-  dO();
-  MM();
-  RP1();
-  wJ();
-  CP1();
-  kR();
-  Ez();
-  _6();
-  k6();
-  ef6();
-  ((t3 = a($1(), 1)), (mR = a($1(), 1)));
   ((E1z = {
     type: "local-jsx",
     name: "think-back",
     description: "Your 2025 Claude Code Year in Review",
     isEnabled: () => sY("tengu_thinkback"),
     isHidden: !1,
-    async call(A) {
-      return t3.createElement(v1z, { onDone: A });
-    },
+    load: () => Promise.resolve().then(() => (AbA(), u9q)),
     userFacingName() {
       return "think-back";
     },

@@@ variable 'e2q' (was 'Tzq') — structural (46.6%)
--- pretty-v2.1.32.js:505021
+++ pretty-v2.1.33.js:504997
@@ -1,26 +1,13 @@
 var Tzq = v(() => {
   d1();
-  u1();
-  $91();
-  ah();
-  FA();
-  a6();
-  hq();
-  k5();
-  Q8();
-  D7();
-  Z5();
-  YG();
-  BA();
-  ((pY = a($1(), 1)), (Vp1 = a($1(), 1)));
   ((sAz = {
     name: "chrome",
     description: "Claude in Chrome (Beta) settings",
     isEnabled: () => !X4(),
     isHidden: !1,
     type: "local-jsx",
+    load: () => Promise.resolve().then(() => (s2q(), a2q)),
     userFacingName: () => "chrome",
-    call: aAz,
   }),
     (Nzq = sAz));
 });

@@@ variable 'r5q' (was 'm3q') — structural (45.8%)
--- pretty-v2.1.32.js:489376
+++ pretty-v2.1.33.js:489513
@@ -1,21 +1,14 @@
 var m3q = v(() => {
-  u3q();
-  ((vxA = a($1(), 1)),
-    (geY = {
-      type: "local-jsx",
-      name: "skills",
-      description: "List available skills",
-      isEnabled: () => !0,
-      isHidden: !1,
-      async call(A, q) {
-        return vxA.createElement(b3q, {
-          onExit: A,
-          commands: q.options.commands,
-        });
-      },
-      userFacingName() {
-        return "skills";
-      },
-    }),
+  ((YAz = {
+    type: "local-jsx",
+    name: "skills",
+    description: "List available skills",
+    isEnabled: () => !0,
+    isHidden: !1,
+    load: () => Promise.resolve().then(() => (i5q(), l5q)),
+    userFacingName() {
+      return "skills";
+    },
+  }),
     (B3q = geY));
 });

@@@ variable 't5q' (was 'Q3q') — structural (45.8%)
--- pretty-v2.1.32.js:489398
+++ pretty-v2.1.33.js:489542
@@ -1,23 +1,15 @@
 var Q3q = v(() => {
-  gZ6();
-  ((ExA = a($1(), 1)),
-    (UeY = {
-      type: "local-jsx",
-      name: "status",
-      description:
-        "Show Claude Code status including version, model, account, API connectivity, and tool statuses",
-      isEnabled: () => !0,
-      isHidden: !1,
-      async call(A, q) {
-        return ExA.createElement(WP1, {
-          onClose: A,
-          context: q,
-          defaultTab: "Status",
-        });
-      },
-      userFacingName() {
-        return "status";
-      },
-    }),
+  ((wAz = {
+    type: "local-jsx",
+    name: "status",
+    description:
+      "Show Claude Code status including version, model, account, API connectivity, and tool statuses",
+    isEnabled: () => !0,
+    isHidden: !1,
+    load: () => Promise.resolve().then(() => (a5q(), o5q)),
+    userFacingName() {
+      return "status";
+    },
+  }),
     (F3q = UeY));
 });

@@@ variable 'iKq' (was 'pqq') — structural (43.6%)
--- pretty-v2.1.32.js:483142
+++ pretty-v2.1.33.js:483224
@@ -1,18 +1,4 @@
 var pqq = v(() => {
-  d1();
-  u1();
-  r8();
-  sIA();
-  ((EJ = a($1(), 1)),
-    (pU1 = a($1(), 1)),
-    (tIA = {
-      ios: {
-        url: "https://apps.apple.com/app/claude-by-anthropic/id6473753684",
-      },
-      android: {
-        url: "https://play.google.com/store/apps/details?id=com.anthropic.claude",
-      },
-    }));
   ((rsY = {
     type: "local-jsx",
     name: "mobile",
@@ -20,9 +6,7 @@
     description: "Show QR code to download the Claude mobile app",
     isEnabled: () => !0,
     isHidden: !1,
-    async call(A) {
-      return EJ.createElement(dsY, { onDone: A });
-    },
+    load: () => Promise.resolve().then(() => (lKq(), cKq)),
     userFacingName() {
       return "mobile";
     },

@@@ variable 'q2q' (was 'CYq') — structural (42.9%)
--- pretty-v2.1.32.js:501242
+++ pretty-v2.1.33.js:501384
@@ -1,21 +1,14 @@
 var CYq = v(() => {
-  RYq();
-  E0();
-  ((zbA = a($1(), 1)),
-    (YAz = {
-      type: "local-jsx",
-      name: "agents",
-      description: "Manage agent configurations",
-      isEnabled: () => !0,
-      isHidden: !1,
-      async call(A, q) {
-        let Y = (await q.getAppState()).toolPermissionContext,
-          z = LX(Y);
-        return zbA.createElement(LYq, { tools: z, onExit: A });
-      },
-      userFacingName() {
-        return "agents";
-      },
-    }),
+  ((C7z = {
+    type: "local-jsx",
+    name: "agents",
+    description: "Manage agent configurations",
+    isEnabled: () => !0,
+    isHidden: !1,
+    load: () => Promise.resolve().then(() => (ezq(), tzq)),
+    userFacingName() {
+      return "agents";
+    },
+  }),
     (yYq = YAz));
 });

@@@ variable 'N_1' (was 'NX1') — structural (42.8%)
--- pretty-v2.1.32.js:231617
+++ pretty-v2.1.33.js:151508
@@ -49,11 +49,11 @@
   );
   i3(
     "PRERELEASEIDENTIFIER",
-    `(?:${C4[S4.NUMERICIDENTIFIER]}|${C4[S4.NONNUMERICIDENTIFIER]})`,
+    `(?:${v4[E4.NONNUMERICIDENTIFIER]}|${v4[E4.NUMERICIDENTIFIER]})`,
   );
   i3(
     "PRERELEASEIDENTIFIERLOOSE",
-    `(?:${C4[S4.NUMERICIDENTIFIERLOOSE]}|${C4[S4.NONNUMERICIDENTIFIER]})`,
+    `(?:${v4[E4.NONNUMERICIDENTIFIER]}|${v4[E4.NUMERICIDENTIFIERLOOSE]})`,
   );
   i3(
     "PRERELEASE",

@@@ variable 'p8q' (was 'vI4') — structural (41.9%)
--- pretty-v2.1.32.js:380100
+++ pretty-v2.1.33.js:466372
@@ -1,25 +1,13 @@
-  vI4 = () => ({
-    type: "local-jsx",
-    name: "login",
-    description: Os8()
-      ? "Switch Anthropic accounts"
-      : "Sign in with your Anthropic account",
-    isEnabled: () => !process.env.DISABLE_LOGIN_COMMAND,
-    isHidden: !1,
-    async call(A, q) {
-      return JG.createElement(vF1, {
-        onDone: async (K) => {
-          if ((q.onChangeAPIKey(), q.setMessages(EI4), K))
-            (Hz1(),
-              TI4(mGY()),
-              h06(),
-              oz6(),
-              q.setAppState((Y) => ({ ...Y, authVersion: Y.authVersion + 1 })));
-          A(K ? "Login successful" : "Login interrupted");
-        },
-      });
-    },
-    userFacingName() {
-      return "login";
-    },
-  });
+var p8q = () => ({
+  type: "local-jsx",
+  name: "login",
+  description: Ud8()
+    ? "Switch Anthropic accounts"
+    : "Sign in with your Anthropic account",
+  isEnabled: () => !process.env.DISABLE_LOGIN_COMMAND,
+  isHidden: !1,
+  load: () => Promise.resolve().then(() => (LD6(), nC4)),
+  userFacingName() {
+    return "login";
+  },
+});

@@@ function 'EZ5' (was 'Hp5') — structural (41.8%)
--- pretty-v2.1.32.js:186288
+++ pretty-v2.1.33.js:150460
@@ -1,51 +1,37 @@
 function Hp5(A) {
   let q = new Map(),
     K = null,
+    Y = A,
     Y = 0,
     z = 0;
   function w() {
-    return s81();
-  }
-  function H() {
-    if (w() === "blurred") z += A;
-    else z = Date.now() - Y;
-    for (let { onChange: _ } of q.values()) _();
+    w = Date.now() - z;
+    for (let O of q.keys()) O();
   }
   function O() {
-    if ([...q.values()].some((J) => J.isVisible)) {
+    if ([...q.values()].some(Boolean)) {
       if (K) (clearInterval(K), (K = null));
       if (Y === 0) Y = Date.now();
-      let J = w() === "blurred" ? A * wp5 : A;
       K = setInterval(H, J);
     } else if (K) (clearInterval(K), (K = null));
   }
-  let $ = w();
-  return (
-    t81(() => {
-      let _ = $,
-        J = w();
-      if ((($ = J), _ === J)) return;
-      if (_ === "blurred" && z > 0) Y = Date.now() - z;
-      if ((O(), _ === "blurred" && K)) H();
-    }),
-    {
-      subscribe(_, J, X) {
-        return (
-          q.set(_, { isVisible: J, onChange: X }),
-          O(),
-          () => {
-            (q.delete(_), O());
-          }
-        );
-      },
-      setVisibility(_, J) {
-        let X = q.get(_);
-        if (X) ((X.isVisible = J), O());
-      },
-      getTime() {
-        if (Y === 0) Y = Date.now();
-        return z || Date.now() - Y;
-      },
-    }
-  );
+  return {
+    subscribe(O, _) {
+      return (
+        q.set(O, _),
+        $(),
+        () => {
+          (q.delete(O), $());
+        }
+      );
+    },
+    now() {
+      if (z === 0) z = Date.now();
+      return w || Date.now() - z;
+    },
+    setTickInterval(O) {
+      if (O === Y) return;
+      ((Y = O), $());
+    },
+  };
 }

@@@ variable 'N9q' (was 'H5q') — structural (41.3%)
--- pretty-v2.1.32.js:491643
+++ pretty-v2.1.33.js:491762
@@ -1,21 +1,11 @@
 var H5q = v(() => {
-  d1();
-  zB();
-  a6();
-  u1();
-  WU1();
-  Mm1();
-  Fd = a($1(), 1);
   ((z1z = {
     type: "local-jsx",
     name: "todos",
     description: "List current todo items",
     isEnabled: () => !0,
     isHidden: !1,
-    async call(A) {
-      let q = await GP1(Fd.default.createElement(Y1z, null));
-      return (A(q), null);
-    },
+    load: () => Promise.resolve().then(() => (f9q(), Z9q)),
     userFacingName() {
       return "todos";
     },

@@@ function 'WMz' (was 'hW7') — structural (41.1%)
--- pretty-v2.1.32.js:186339
+++ pretty-v2.1.33.js:567109
@@ -1,13 +1,16 @@
 function hW7(A) {
-  let q = A1(3),
-    { children: K } = A,
-    [Y] = n_1.useState(Op5),
-    z;
-  if (q[0] !== K || q[1] !== Y)
-    ((z = n_1.default.createElement(qC1.Provider, { value: Y }, K)),
+  let q = q1(2),
+    { onDone: K } = A;
+  ET6();
+  let Y;
+  if (q[0] !== K)
+    ((Y = WE.default.createElement(
+      WE.default.Suspense,
+      { fallback: null },
+      WE.default.createElement(jMz, { onDone: K }),
+    )),
       (q[0] = K),
-      (q[1] = Y),
-      (q[2] = z));
-  else z = q[2];
+      (q[1] = Y));
+  else Y = q[1];
   return z;
 }

@@@ variable 'XYq' (was 'n5q') — structural (40.5%)
--- pretty-v2.1.32.js:494187
+++ pretty-v2.1.33.js:494309
@@ -1,36 +1,18 @@
 var n5q = v(() => {
   l5q();
-  FA();
-  F6();
-  rt();
-  ((mxA = a($1(), 1)),
-    (i5q = {
-      type: "local-jsx",
-      name: "passes",
-      get description() {
-        if (nt())
-          return "Share a free week of Claude Code with friends and earn extra usage";
-        return "Share a free week of Claude Code with friends";
-      },
-      isEnabled: () => !0,
-      isHidden: !1,
-      async call(A) {
-        let K = !M6().hasVisitedPasses;
-        if (K) {
-          let Y = pf6();
-          OA((z) => ({
-            ...z,
-            hasVisitedPasses: !0,
-            passesLastSeenRemaining: Y ?? z.passesLastSeenRemaining,
-          }));
-        }
-        return (
-          c("tengu_guest_passes_visited", { is_first_visit: K }),
-          mxA.createElement(c5q, { onDone: A })
-        );
-      },
-      userFacingName() {
-        return "passes";
-      },
-    }));
+  JYq = {
+    type: "local-jsx",
+    name: "passes",
+    get description() {
+      if (dt())
+        return "Share a free week of Claude Code with friends and earn extra usage";
+      return "Share a free week of Claude Code with friends";
+    },
+    isEnabled: () => !0,
+    isHidden: !1,
+    load: () => Promise.resolve().then(() => (_Yq(), OYq)),
+    userFacingName() {
+      return "passes";
+    },
+  };
 });

@@@ function 'MXY' — structural (25.9%)
--- pretty-v2.1.32.js:358368
+++ pretty-v2.1.33.js:355670
@@ -1,4 +1,6 @@
-function MXY() {
-  let A = process.env.HOME || process.env.USERPROFILE || ".";
-  return gE4(A, ".claude", "teams");
+function MXY(A, q) {
+  Q5(A, q, (K) => {
+    if (K.status !== "running" || K.awaitingPlanApproval) return K;
+    return { ...K, awaitingPlanApproval: !0 };
+  });
 }
