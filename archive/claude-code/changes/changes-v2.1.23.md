--- archive/claude-code/pretty/pretty-v2.1.22.js
+++ archive/claude-code/pretty/pretty-v2.1.23.js
Structural similarity: 98.7%
Matched: 14260/14329 vs 14445
Changes: 185 added, 69 removed, 748 structural, 35 string-only (13477 unchanged)

Filtered: 50 version bumps, 501 reformatting-only changes

=== Import Style Changes ===

"child_process":
  - import NYY from "child_process";
  - import TYY from "child_process";
  + import { execFile as ZDq, spawn as WDq, spawnSync as DDq } from "child_process";
  + import { spawn as Iw5, spawnSync as Sw5 } from "child_process";

"crypto":
  - import _4Y from "crypto";
  - import Z4Y from "crypto";
  + import { randomBytes as xs2, randomUUID as us2 } from "crypto";
  + import { randomBytes as P3z, timingSafeEqual as V3z } from "crypto";

"https":
  - import O17 from "https";
  + import { Agent as Qr3 } from "https";

"node:child_process":
  - import UR1 from "node:child_process";
  - import xK7 from "node:child_process";
  + import { execFile as H2Y, execFileSync as dUw } from "node:child_process";
  + import { execFileSync as Ty2, spawn as vy2 } from "node:child_process";

"node:fs":
  - import g9Y from "node:fs";
  - import U9Y from "node:fs";
  + import {
  +   existsSync as PpA,
  +   statSync as Xy2,
  +   mkdirSync as $y2,
  +   realpathSync as _y2,
  + } from "node:fs";
  + import {
  +   constants as Py2,
  +   readFileSync as Vy2,
  +   existsSync as fy2,
  +   unlinkSync as Ny2,
  + } from "node:fs";

"node:os":
  - import Q9Y from "node:os";
  + import { homedir as Y3z } from "node:os";

"node:path":
  - import bK7 from "node:path";
  + import {
  +   join as fX,
  +   dirname as ed,
  +   resolve as Em,
  +   delimiter as Wx2,
  +   basename as Dx2,
  + } from "node:path";

"node:process":
  - import dvK from "node:process";
  + import { cwd as MX4 } from "node:process";

"node:util":
  - import ce9 from "node:util";
  + import { isDeepStrictEqual as VFK } from "node:util";

"path":
  - import D9Y from "path";
  + import { dirname as T5z, join as FQK } from "path";

"stream":
  - import hzA from "stream";
  + import { PassThrough as i5z } from "stream";

=== Removed ===

--- Removed U8A (pretty-v2.1.22.js:157706-157711)
- function U8A() {
-   let A = Bn(),
-     K = t86();
-   if (A) return { dispatcher: Ww4(A) };
-   return K;
- }

--- Removed JH4 (pretty-v2.1.22.js:160522-160706)
- var JH4 = C(() => {
-   wH4 = `Use this tool to create and manage a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user.
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
- * Uses the ${l5} tool to add a comment to the calculateTotal function *
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

--- Removed mO4 (pretty-v2.1.22.js:176288-176294)
- function mO4(A, K) {
-   if (!K) return 0;
-   let q = A.hyperlinkMap.get(K);
-   if (q === void 0)
-     ((q = A.hyperlinks.length), A.hyperlinks.push(K), A.hyperlinkMap.set(K, q));
-   return q;
- }

--- Removed gO4 (pretty-v2.1.22.js:176295-176297)
- function gO4(A, K) {
-   return K === 0 ? void 0 : A.hyperlinks[K];
- }

--- Removed $s3 (pretty-v2.1.22.js:176366-176375)
- function $s3(A, K) {
-   let q = A.chars[K],
-     Y = A.styleIds[K];
-   return {
-     char: A.charStrings[q] ?? " ",
-     styleId: Y === fQ ? A.emptyStyleId : Y,
-     width: A.widths[K],
-     hyperlink: gO4(A, A.hyperlinkIds[K]),
-   };
- }

--- Removed J51 (pretty-v2.1.22.js:176376-176383)
- function J51(A, K, q) {
-   let Y = A.chars[K],
-     z = A.styleIds[K];
-   ((q.char = A.charStrings[Y] ?? " "),
-     (q.styleId = z === fQ ? A.emptyStyleId : z),
-     (q.width = A.widths[K]),
-     (q.hyperlink = gO4(A, A.hyperlinkIds[K])));
- }

--- Removed QO4 (pretty-v2.1.22.js:176440-176454)
- function QO4(A, K) {
-   if (K.length === 1) {
-     let z = K.charCodeAt(0);
-     if (z < 128) {
-       let w = A.charAscii[z];
-       if (w !== -1) return w;
-       let H = A.charStrings.length;
-       return (A.charStrings.push(K), (A.charAscii[z] = H), H);
-     }
-   }
-   let q = A.charStringMap.get(K);
-   if (q !== void 0) return q;
-   let Y = A.charStrings.length;
-   return (A.charStrings.push(K), A.charStringMap.set(K, Y), Y);
- }

--- Removed UO4 (pretty-v2.1.22.js:176455-176489)
- function UO4(A, K, q, Y) {
-   if (q < 0 || Y < 0 || q >= A.width || Y >= A.height) return;
-   if (q >= K.width || Y >= K.height) return;
-   let z = Y * K.width + q,
-     w = Y * A.width + q,
-     H = K.charStrings[K.chars[z]];
-   A.chars[w] = QO4(A, H);
-   let J = K.styleIds[z];
-   ((A.styleIds[w] = J === fQ ? A.emptyStyleId : J),
-     (A.widths[w] = K.widths[z]));
-   let O = K.hyperlinkIds[z];
-   if (O === 0) A.hyperlinkIds[w] = 0;
-   else A.hyperlinkIds[w] = mO4(A, K.hyperlinks[O]);
-   let X = A.damage;
-   if (X) {
-     let $ = X.x + X.width,
-       _ = X.y + X.height;
-     if (q < X.x) ((X.width += X.x - q), (X.x = q));
-     else if (q >= $) X.width = q - X.x + 1;
-     if (Y < X.y) ((X.height += X.y - Y), (X.y = Y));
-     else if (Y >= _) X.height = Y - X.y + 1;
-   } else A.damage = { x: q, y: Y, width: 1, height: 1 };
-   if (K.widths[z] === 1) {
-     let $ = q + 1;
-     if ($ < A.width) {
-       let _ = Y * A.width + $;
-       ((A.chars[_] = O51),
-         (A.styleIds[_] = A.emptyStyleId),
-         (A.widths[_] = 2),
-         (A.hyperlinkIds[_] = 0));
-       let Z = A.damage;
-       if (Z && $ >= Z.x + Z.width) Z.width = $ - Z.x + 1;
-     }
-   }
- }

--- Removed fQ (pretty-v2.1.22.js:176587-176587)
-   fQ = 65535,

--- Removed OXA (pretty-v2.1.22.js:176590-176596)
- var OXA = C(() => {
-   C76();
-   a76();
-   t8A();
-   ((dO4 = new RegExp(`^${tn}\\]8${Ar}${Ar}([^${en}]*)${en}$`)),
-     (cO4 = `${tn}]8${Ar}`));
- });

--- Removed F04 (pretty-v2.1.22.js:178608-178613)
- function F04() {
-   if (!m04) return Promise.resolve();
-   return new Promise((A) => {
-     PK6.add(A);
-   });
- }

--- Removed i31 (pretty-v2.1.22.js:192821-192833)
- function i31(A) {
-   try {
-     let K = String(A),
-       q =
-         process.platform === "win32"
-           ? `powershell.exe -NoProfile -Command "(Get-CimInstance Win32_Process -Filter \\"ProcessId=${K}\\").ParentProcessId"`
-           : `ps -o ppid= -p ${K}`,
-       Y = GG(q, { timeout: 1000 });
-     return Y ? Y.trim() : null;
-   } catch {
-     return null;
-   }
- }

--- Removed A36 (pretty-v2.1.22.js:192964-192971)
- function A36(A) {
-   return (
-     A.includes("claude-sonnet-4-5") ||
-     A.includes("claude-opus-4-1") ||
-     A.includes("claude-opus-4-5") ||
-     A.includes("claude-haiku-4-5")
-   );
- }

--- Removed UCY (pretty-v2.1.22.js:308431-308448)
- function UCY(A) {
-   if (!yW7(A)) return !1;
-   if (!W$()) return !0;
-   try {
-     let K = process.ppid;
-     for (let q = 0; q < 10; q++) {
-       if (K === A) return !0;
-       if (K === 0 || K === 1) break;
-       let Y = i31(K),
-         z = Y ? parseInt(Y) : null;
-       if (!z || z === K) break;
-       K = z;
-     }
-     return !1;
-   } catch (K) {
-     return !1;
-   }
- }

--- Removed QW7 (pretty-v2.1.22.js:309204-309208)
- function QW7(A, K) {
-   let q = cM(A);
-   if (q?.messages) return q.messages;
-   return K;
- }

--- Removed HV6 (pretty-v2.1.22.js:318996-318998)
- function HV6(A) {
-   return A.toLowerCase().includes("opus-4-5") || !1 || !1 || !1;
- }

--- Removed UV7 (pretty-v2.1.22.js:319002-319010)
- function UV7(A) {
-   if (typeof A === "string" && A !== "unset") return A;
-   if (typeof A === "number") {
-     if (A <= 30) return "low";
-     if (A <= 60) return "medium";
-     return "high";
-   }
-   return "medium";
- }

--- Removed UN6 (pretty-v2.1.22.js:340302-340304)
- var UN6 = C(() => {
-   oR7 = new Map();
- });

--- Removed Ls7 (pretty-v2.1.22.js:389568-390013)
- function Ls7(A) {
-   let K = s(90),
-     {
-       mode: q,
-       elapsedTimeMs: Y,
-       spinnerTip: z,
-       currentResponseLength: w,
-       overrideColor: H,
-       overrideShimmerColor: J,
-       overrideMessage: O,
-       spinnerSuffix: X,
-       verbose: $,
-       todos: _,
-       hasActiveTools: Z,
-     } = A,
-     G = Z === void 0 ? !1 : Z,
-     [W, D] = Gv.useState(0),
-     [j, M] = Gv.useState(0),
-     [P] = V6(),
-     { isConnected: V } = hL6(),
-     { columns: N } = M8(),
-     T = dj1(),
-     [E, R] = Gv.useState(null),
-     b = Gv.useRef(null),
-     S,
-     B;
-   if (K[0] !== q)
-     ((S = () => {
-       let u7 = null,
-         H3 = null;
-       if (q === "thinking") {
-         if (b.current === null) ((b.current = Date.now()), R("thinking"));
-       } else if (b.current !== null) {
-         let N9 = Date.now() - b.current,
-           U5 = Date.now() - b.current,
-           p9 = Math.max(0, 2000 - U5);
-         b.current = null;
-         let y5 = () => {
-           (R(N9), (H3 = setTimeout(() => R(null), 2000)));
-         };
-         if (p9 > 0) u7 = setTimeout(y5, p9);
-         else y5();
-       }
-       return () => {
-         if (u7) clearTimeout(u7);
-         if (H3) clearTimeout(H3);
-       };
-     }),
-       (B = [q]),
-       (K[0] = q),
-       (K[1] = S),
-       (K[2] = B));
-   else ((S = K[1]), (B = K[2]));
-   Gv.useEffect(S, B);
-   let x;
-   if (K[3] !== T || K[4] !== _)
-     ((x = AH() ? T?.find(Y$2) : _?.find(q$2)),
-       (K[3] = T),
-       (K[4] = _),
-       (K[5] = x));
-   else x = K[5];
-   let F = x,
-     Q;
-   if (K[6] !== T || K[7] !== _)
-     ((Q = AH() ? H$2(T) : _?.find(K$2)), (K[6] = T), (K[7] = _), (K[8] = Q));
-   else Q = K[8];
-   let u = Q,
-     [d] = Gv.useState(A$2),
-     o = (O ?? F?.activeForm ?? d) + "…",
-     { isStalled: l, stalledIntensity: e } = dL6(w, G),
-     wA = wd(q, o, V, l),
-     HA = pL6(q),
-     OA = Gv.useRef(w),
-     WA,
-     a;
-   if (K[9] !== q)
-     ((WA = () => {
-       let u7 = "spinner-" + q;
-       return (
-         PFA.startCLIActivity(u7),
-         () => {
-           PFA.endCLIActivity(u7);
-         }
-       );
-     }),
-       (a = [q]),
-       (K[9] = q),
-       (K[10] = WA),
-       (K[11] = a));
-   else ((WA = K[10]), (a = K[11]));
-   Gv.useEffect(WA, a);
-   let _A, jA;
-   if (K[12] !== w)
-     ((_A = () => {
-       OA.current = w;
-     }),
-       (jA = [w]),
-       (K[12] = w),
-       (K[13] = _A),
-       (K[14] = jA));
-   else ((_A = K[13]), (jA = K[14]));
-   Gv.useEffect(_A, jA);
-   let PA;
-   if (K[15] !== V)
-     ((PA = () => {
-       if (!V) {
-         D(4);
-         return;
-       }
-       D(eX2);
-     }),
-       (K[15] = V),
-       (K[16] = PA));
-   else PA = K[16];
-   JY(PA, 120);
-   let SA;
-   if (K[17] === Symbol.for("react.memo_cache_sentinel"))
-     ((SA = () => {
-       M((u7) => {
-         let H3 = OA.current - u7;
-         if (H3 <= 0) return u7;
-         let N9;
-         if (H3 < 70) N9 = 1;
-         else if (H3 < 200) N9 = Math.max(2, Math.ceil(H3 * 0.08));
-         else N9 = 18;
-         return Math.min(u7 + N9, OA.current);
-       });
-     }),
-       (K[17] = SA));
-   else SA = K[17];
-   JY(SA, 10);
-   let mA = x7(o) + 2,
-     qA;
-   if (K[18] !== E)
-     ((qA =
-       E === "thinking"
-         ? "thinking"
-         : typeof E === "number"
-           ? `thought for ${Math.max(1, Math.round(E / 1000))}s`
-           : null),
-       (K[18] = E),
-       (K[19] = qA));
-   else qA = K[19];
-   let YA = qA,
-     JA;
-   if (K[20] !== YA) ((JA = YA ? x7(YA) : 0), (K[20] = YA), (K[21] = JA));
-   else JA = K[21];
-   let AA = JA,
-     t,
-     ZA;
-   if (K[22] !== Y)
-     ((ZA = fJ(Y)), (t = x7(ZA)), (K[22] = Y), (K[23] = t), (K[24] = ZA));
-   else ((t = K[23]), (ZA = K[24]));
-   let kA = t,
-     XA = BK("chat:cancel", "Chat", "esc"),
-     LA;
-   if (K[25] !== XA) ((LA = XA.toLowerCase()), (K[25] = XA), (K[26] = LA));
-   else LA = K[26];
-   let VA = LA,
-     EA = x7(`${VA} to interrupt`),
-     CA;
-   if (K[27] !== j) ((CA = i5(Math.round(j / 4))), (K[27] = j), (K[28] = CA));
-   else CA = K[28];
-   let dA = CA,
-     z1 = `${q1.arrowDown} ${dA} tokens`,
-     oA = x7(z1),
-     V1 = T && T.length > 0 ? "tasks" : "todos",
-     y1 = BK("app:toggleTodos", "Global", "ctrl+t"),
-     p1 = `${P.showExpandedTodos ? "hide" : "show"} ${V1}`,
-     S6 = x7(`${y1} to ${p1}`),
-     B6 = x7(" · "),
-     J1 = E !== null,
-     $1 = $ || Y > ks7,
-     C1 = $ || Y > ks7,
-     P1 = (T && T.length > 0) || (_ && _.length > 0),
-     z6 = N - mA - 5,
-     J6 = J1 && z6 > AA,
-     TA = J6 ? AA + B6 : 0,
-     fA = $1 && z6 > TA + kA,
-     cA = TA + (fA ? kA + B6 : 0),
-     w1 = z6 > cA + EA,
-     iA = cA + (w1 ? EA + B6 : 0),
-     sA = C1 && z6 > iA + oA,
-     f1 = iA + (sA ? oA + B6 : 0),
-     T1 = P1 && z6 > f1 + S6,
-     d1;
-   if (K[29] !== VA || K[30] !== w1)
-     ((d1 = w1
-       ? [
-           d4.createElement(
-             f,
-             { dimColor: !0, key: "esc" },
-             d4.createElement(G6, {
-               shortcut: VA,
-               action: "interrupt",
-               bold: !0,
-             }),
-           ),
-         ]
-       : []),
-       (K[29] = VA),
-       (K[30] = w1),
-       (K[31] = d1));
-   else d1 = K[31];
-   let y6;
-   if (K[32] !== X)
-     ((y6 = X ? [d4.createElement(f, { dimColor: !0, key: "suffix" }, X)] : []),
-       (K[32] = X),
-       (K[33] = y6));
-   else y6 = K[33];
-   let Q8;
-   if (K[34] !== T1 || K[35] !== p1 || K[36] !== y1)
-     ((Q8 = T1
-       ? [
-           d4.createElement(
-             f,
-             { dimColor: !0, key: "todo" },
-             d4.createElement(G6, { shortcut: y1, action: p1, bold: !0 }),
-           ),
-         ]
-       : []),
-       (K[34] = T1),
-       (K[35] = p1),
-       (K[36] = y1),
-       (K[37] = Q8));
-   else Q8 = K[37];
-   let q8;
-   if (K[38] !== fA || K[39] !== ZA)
-     ((q8 = fA
-       ? [d4.createElement(f, { dimColor: !0, key: "elapsedTime" }, ZA)]
-       : []),
-       (K[38] = fA),
-       (K[39] = ZA),
-       (K[40] = q8));
-   else q8 = K[40];
-   let F4;
-   if (K[41] !== q || K[42] !== sA || K[43] !== dA)
-     ((F4 = sA
-       ? [
-           d4.createElement(
-             I,
-             { flexDirection: "row", key: "tokens" },
-             d4.createElement(z$2, { mode: q, key: "spinnerMode" }),
-             d4.createElement(f, { dimColor: !0 }, dA, " tokens"),
-           ),
-         ]
-       : []),
-       (K[41] = q),
-       (K[42] = sA),
-       (K[43] = dA),
-       (K[44] = F4));
-   else F4 = K[44];
-   let P4;
-   if (K[45] !== J6 || K[46] !== E || K[47] !== YA)
-     ((P4 =
-       J6 && YA
-         ? [
-             E === "thinking"
-               ? d4.createElement(Ts7, { key: "thinking", text: YA })
-               : d4.createElement(f, { dimColor: !0, key: "thinking" }, YA),
-           ]
-         : []),
-       (K[45] = J6),
-       (K[46] = E),
-       (K[47] = YA),
-       (K[48] = P4));
-   else P4 = K[48];
-   let T8;
-   if (
-     K[49] !== V ||
-     K[50] !== d1 ||
-     K[51] !== y6 ||
-     K[52] !== Q8 ||
-     K[53] !== q8 ||
-     K[54] !== F4 ||
-     K[55] !== P4
-   ) {
-     if (((T8 = [...d1, ...y6, ...Q8, ...q8, ...F4, ...P4]), V === !1)) {
-       let u7;
-       if (K[57] === Symbol.for("react.memo_cache_sentinel"))
-         ((u7 = d4.createElement(
-           I,
-           { key: "offline" },
-           d4.createElement(f, { color: "error", bold: !0 }, "offline"),
-         )),
-           (K[57] = u7));
-       else u7 = K[57];
-       T8.push(u7);
-     }
-     ((K[49] = V),
-       (K[50] = d1),
-       (K[51] = y6),
-       (K[52] = Q8),
-       (K[53] = q8),
-       (K[54] = F4),
-       (K[55] = P4),
-       (K[56] = T8));
-   } else T8 = K[56];
-   let c4 = H ?? (V === !1 ? "inactive" : "claude"),
-     k4 = J ?? "claudeShimmer",
-     wq;
-   if (K[58] !== T8)
-     ((wq =
-       T8.length > 0
-         ? d4.createElement(
-             d4.Fragment,
-             null,
-             d4.createElement(f, { dimColor: !0 }, "("),
-             d4.createElement(w8, null, T8),
-             d4.createElement(f, { dimColor: !0 }, ")"),
-           )
-         : null),
-       (K[58] = T8),
-       (K[59] = wq));
-   else wq = K[59];
-   let Hq = wq,
-     l8 = H ? 0 : e,
-     d8;
-   if (K[60] !== W || K[61] !== V || K[62] !== c4 || K[63] !== l8)
-     ((d8 = d4.createElement(TFA, {
-       frame: W,
-       messageColor: c4,
-       stalledIntensity: l8,
-       isConnected: V,
-     })),
-       (K[60] = W),
-       (K[61] = V),
-       (K[62] = c4),
-       (K[63] = l8),
-       (K[64] = d8));
-   else d8 = K[64];
-   let Bq = H ? 0 : e,
-     Jq;
-   if (
-     K[65] !== HA ||
-     K[66] !== wA ||
-     K[67] !== V ||
-     K[68] !== o ||
-     K[69] !== c4 ||
-     K[70] !== q ||
-     K[71] !== k4 ||
-     K[72] !== Bq
-   )
-     ((Jq = d4.createElement(QL6, {
-       message: o,
-       mode: q,
-       isConnected: V,
-       messageColor: c4,
-       glimmerIndex: wA,
-       flashOpacity: HA,
-       shimmerColor: k4,
-       stalledIntensity: Bq,
-     })),
-       (K[65] = HA),
-       (K[66] = wA),
-       (K[67] = V),
-       (K[68] = o),
-       (K[69] = c4),
-       (K[70] = q),
-       (K[71] = k4),
-       (K[72] = Bq),
-       (K[73] = Jq));
-   else Jq = K[73];
-   let mq;
-   if (K[74] !== P.viewingAgentTaskId)
-     ((mq =
-       P.viewingAgentTaskId &&
-       d4.createElement(f, { dimColor: !0 }, " [leader]")),
-       (K[74] = P.viewingAgentTaskId),
-       (K[75] = mq));
-   else mq = K[75];
-   let w3;
-   if (K[76] !== Hq || K[77] !== d8 || K[78] !== Jq || K[79] !== mq)
-     ((w3 = d4.createElement(
-       I,
-       { flexDirection: "row", flexWrap: "wrap", marginTop: 1, width: "100%" },
-       d8,
-       Jq,
-       Hq,
-       mq,
-     )),
-       (K[76] = Hq),
-       (K[77] = d8),
-       (K[78] = Jq),
-       (K[79] = mq),
-       (K[80] = w3));
-   else w3 = K[80];
-   let KY;
-   if (
-     K[81] !== P.showExpandedTodos ||
-     K[82] !== u ||
-     K[83] !== z ||
-     K[84] !== T ||
-     K[85] !== _
-   )
-     ((KY =
-       P.showExpandedTodos && T && T.length > 0
-         ? d4.createElement(
-             I,
-             { width: "100%", flexDirection: "column" },
-             d4.createElement(E6, null, d4.createElement(Uj1, { tasks: T })),
-           )
-         : P.showExpandedTodos && _ && _.length > 0
-           ? d4.createElement(
-               I,
-               { width: "100%", flexDirection: "column" },
-               d4.createElement(E6, null, d4.createElement(Zt, { todos: _ })),
-             )
-           : u || z
-             ? d4.createElement(
-                 I,
-                 { width: "100%" },
-                 d4.createElement(
-                   E6,
-                   null,
-                   d4.createElement(
-                     f,
-                     { dimColor: !0 },
-                     u
-                       ? `Next: ${"subject" in u ? u.subject : u.content}`
-                       : `Tip: ${z}`,
-                   ),
-                 ),
-               )
-             : null),
-       (K[81] = P.showExpandedTodos),
-       (K[82] = u),
-       (K[83] = z),
-       (K[84] = T),
-       (K[85] = _),
-       (K[86] = KY));
-   else KY = K[86];
-   let t4;
-   if (K[87] !== w3 || K[88] !== KY)
-     ((t4 = d4.createElement(
-       I,
-       { flexDirection: "column", width: "100%", alignItems: "flex-start" },
-       w3,
-       KY,
-     )),
-       (K[87] = w3),
-       (K[88] = KY),
-       (K[89] = t4));
-   else t4 = K[89];
-   return t4;
- }

--- Removed E8K (pretty-v2.1.22.js:408506-408515)
- function E8K(A) {
-   let K = Ct(A);
-   if (K)
-     return `[Shutdown Request from ${K.from}]${K.reason ? ` ${K.reason}` : ""}`;
-   let q = vS(A);
-   if (q) return `[Shutdown Approved] ${q.from} is now exiting`;
-   let Y = SM1(A);
-   if (Y) return `[Shutdown Rejected] ${Y.from}: ${Y.reason}`;
-   return null;
- }

--- Removed C8K (pretty-v2.1.22.js:408689-408700)
- function C8K(A) {
-   let K = gM1(A);
-   if (K) {
-     let z = K.capabilities ? ` - ${K.capabilities}` : "";
-     return `[Join Request] ${K.proposedName} wants to join${z}`;
-   }
-   let q = gjA(A);
-   if (q) return `[Join Approved] You are now ${q.agentName} in ${q.teamName}`;
-   let Y = FjA(A);
-   if (Y) return `[Join Rejected] ${Y.reason || "Request was rejected"}`;
-   return null;
- }

--- Removed R8K (pretty-v2.1.22.js:408782-408786)
- function R8K(A) {
-   let K = hM1(A);
-   if (K) return `[Task Assigned] #${K.taskId} - ${K.subject}`;
-   return null;
- }

--- Removed MW2 (pretty-v2.1.22.js:408995-409004)
- function MW2(A) {
-   let K = IM1(A);
-   if (K) return `[Plan Approval Request from ${K.from}]`;
-   let q = mjA(A);
-   if (q)
-     if (q.approved)
-       return "[Plan Approved] You can now proceed with implementation";
-     else return `[Plan Rejected] ${q.feedback || "Please revise your plan"}`;
-   return null;
- }

--- Removed PW2 (pretty-v2.1.22.js:409005-409011)
- function PW2(A) {
-   if (A.completedTaskId) {
-     let K = A.completedStatus || "completed";
-     return `Agent idle · Task ${A.completedTaskId} ${K}`;
-   }
-   return "Agent idle";
- }

--- Removed I8K (pretty-v2.1.22.js:409012-409028)
- function I8K(A) {
-   let K = MW2(A);
-   if (K) return K;
-   let q = E8K(A);
-   if (q) return q;
-   let Y = C8K(A);
-   if (Y) return Y;
-   let z = Ky6(A);
-   if (z) return PW2(z);
-   let w = R8K(A);
-   if (w) return w;
-   try {
-     let H = X6(A);
-     if (H?.type === "teammate_terminated" && H.message) return H.message;
-   } catch {}
-   return A;
- }

--- Removed u8K (pretty-v2.1.22.js:409290-409316)
- function u8K(A) {
-   let K = s(7),
-     { addMargin: q, time: Y } = A,
-     z;
-   if (K[0] !== Y) ((z = vW2(Y)), (K[0] = Y), (K[1] = z));
-   else z = K[1];
-   let w = z,
-     H = q ? 1 : 0,
-     J;
-   if (K[2] !== w)
-     ((J = qQA.createElement(f, { dimColor: !0 }, "↻ ", w)),
-       (K[2] = w),
-       (K[3] = J));
-   else J = K[3];
-   let O;
-   if (K[4] !== H || K[5] !== J)
-     ((O = qQA.createElement(
-       I,
-       { flexDirection: "column", marginTop: H, width: "100%" },
-       J,
-     )),
-       (K[4] = H),
-       (K[5] = J),
-       (K[6] = O));
-   else O = K[6];
-   return O;
- }

--- Removed vW2 (pretty-v2.1.22.js:409317-409325)
- function vW2(A) {
-   let K = new Date(A);
-   if (isNaN(K.getTime())) return A;
-   return K.toLocaleTimeString("en-US", {
-     hour: "2-digit",
-     minute: "2-digit",
-     hour12: !0,
-   });
- }

--- Removed kS (pretty-v2.1.22.js:412893-412964)
- async function kS({
-   promptMessages: A,
-   cacheSafeParams: K,
-   canUseTool: q,
-   querySource: Y,
-   forkLabel: z,
-   overrides: w,
-   maxOutputTokens: H,
-   maxTurns: J,
-   onMessage: O,
- }) {
-   let X = Date.now(),
-     $ = [],
-     _ = { ...Nv },
-     {
-       systemPrompt: Z,
-       userContext: G,
-       systemContext: W,
-       toolUseContext: D,
-       forkContextMessages: j,
-     } = K,
-     M = JQA(D, w),
-     P = [...Iy6(j), ...A];
-   for await (let N of Uf({
-     messages: P,
-     systemPrompt: Z,
-     userContext: G,
-     systemContext: W,
-     canUseTool: q,
-     toolUseContext: M,
-     querySource: Y,
-     maxOutputTokensOverride: H,
-     maxTurns: J,
-   })) {
-     if (N.type === "stream_event" || N.type === "stream_request_start")
-       continue;
-     if (N.type === "assistant") {
-       let E = N.message.usage;
-       if (E)
-         _ = tM1(_, {
-           input_tokens: E.input_tokens ?? 0,
-           cache_creation_input_tokens: E.cache_creation_input_tokens ?? 0,
-           cache_read_input_tokens: E.cache_read_input_tokens ?? 0,
-           output_tokens: E.output_tokens ?? 0,
-           server_tool_use: {
-             web_search_requests: E.server_tool_use?.web_search_requests ?? 0,
-             web_fetch_requests: E.server_tool_use?.web_fetch_requests ?? 0,
-           },
-           service_tier: E.service_tier ?? "standard",
-           cache_creation: {
-             ephemeral_1h_input_tokens:
-               E.cache_creation?.ephemeral_1h_input_tokens ?? 0,
-             ephemeral_5m_input_tokens:
-               E.cache_creation?.ephemeral_5m_input_tokens ?? 0,
-           },
-         });
-     }
-     ($.push(N), O?.(N));
-   }
-   let V = Date.now() - X;
-   return (
-     JD2({
-       forkLabel: z,
-       querySource: Y,
-       durationMs: V,
-       messageCount: $.length,
-       totalUsage: _,
-       queryTracking: D.queryTracking,
-     }),
-     { messages: $, totalUsage: _ }
-   );
- }

--- Removed wP1 (pretty-v2.1.22.js:414114-414134)
- function wP1({ onBackground: A } = {}) {
-   let [K, q] = V6(),
-     Y = QY.useRef(K);
-   Y.current = K;
-   let z = QY.useCallback(() => {
-     (J_1(() => Y.current, q), A?.());
-   }, [q, A]);
-   A6("task:background", z, { context: "Task" });
-   let w = BK("task:background", "Task", "ctrl+b"),
-     H = Q6.terminal === "tmux" && w === "ctrl+b" ? "ctrl+b ctrl+b (twice)" : w;
-   if (j1(process.env.CLAUDE_CODE_DISABLE_BACKGROUND_TASKS)) return null;
-   return QY.createElement(
-     I,
-     { paddingLeft: 5 },
-     QY.createElement(
-       f,
-       { dimColor: !0 },
-       QY.createElement(G6, { shortcut: H, action: "run in background" }),
-     ),
-   );
- }

--- Removed S4K (pretty-v2.1.22.js:414166-414176)
- function S4K(A) {
-   let { timeout: K } = A;
-   if (!K) return null;
-   let q = ljA();
-   if (K === q) return null;
-   return QY.createElement(
-     I,
-     { flexWrap: "nowrap", marginLeft: 1 },
-     QY.createElement(f, { dimColor: !0 }, "timeout: ", fJ(K)),
-   );
- }

--- Removed u4K (pretty-v2.1.22.js:414207-414209)
- function u4K(A, K, { verbose: q, theme: Y, tools: z, style: w }) {
-   return QY.createElement(W3A, { content: A, verbose: q });
- }

--- Removed RKK (pretty-v2.1.22.js:423864-423870)
- function RKK() {
-   if (XMA)
-     ((mt = XMA), h(`[TeammateModeSnapshot] Captured from CLI override: ${mt}`));
-   else
-     ((mt = D1().teammateMode ?? "auto"),
-       h(`[TeammateModeSnapshot] Captured from config: ${mt}`));
- }

--- Removed pQA (pretty-v2.1.22.js:426684-426741)
- var pQA = C(() => {
-   OX();
-   W1();
-   v1();
-   OX();
-   VaA();
-   _z();
-   l7();
-   i1();
-   fS6 = a1(async (A) => {
-     let K = await LS(A),
-       q = V4("tengu_kv7_prompt_sort", !1)
-         ? [...K].sort((H, J) => H.name.localeCompare(J.name))
-         : K,
-       Y = q.map((H) => H.userFacingName()).join(", ");
-     h(`Skills and commands included in Skill tool: ${Y}`);
-     let z = IP2(q),
-       w = `Execute a skill within the main conversation
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
- - If you see a <${mj}> tag in the current conversation turn (e.g., <${mj}>/commit</${mj}>), the skill has ALREADY been loaded and its instructions follow in the next message. Do NOT call this tool - just follow the skill instructions directly.
- 
- Available skills:
- ${z}
- `;
-     if (QQA !== void 0 && w !== QQA)
-       n("tengu_tool_prompt_changed", {
-         tool: "SkillTool",
-         previousLength: QQA.length,
-         newLength: w.length,
-         previousCommandCount: (QQA.match(/^- /gm) ?? []).length,
-         newCommandCount: (w.match(/^- /gm) ?? []).length,
-       });
-     return ((QQA = w), w);
-   });
- });

--- Removed y2K (pretty-v2.1.22.js:447299-447452)
- var y2K = C(() => {
-   ((rv2 = `Use this tool proactively when you're about to start a non-trivial implementation task. Getting user sign-off on your approach before writing code prevents wasted effort and ensures alignment. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
-    - If you would use ${gJ} to clarify the approach, use EnterPlanMode instead
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
- 5. Use ${gJ} if you need to clarify approaches
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
-     (ttH = `Use this tool when a task has genuine ambiguity about the right approach and getting user input before coding would prevent significant rework. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
- When in doubt, prefer starting work and using ${gJ} for specific questions over entering a full planning phase.
- 
- ## What Happens in Plan Mode
- 
- In plan mode, you'll:
- 1. Explore the codebase using Glob, Grep, and Read tools
- 2. Understand existing patterns and architecture
- 3. Design an implementation approach
- 4. Present your plan to the user for approval
- 5. Use ${gJ} if you need to clarify approaches
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

--- Removed Tb6 (pretty-v2.1.22.js:449472-449490)
- function Tb6(A, K) {
-   let Y,
-     z,
-     w = [];
-   for (let O of A) {
-     if (!O) continue;
-     if (O.startsWith("x-anthropic-billing-header")) Y = O;
-     else if (YH4.has(O)) z = O;
-     else w.push(O);
-   }
-   let H = [];
-   if (Y) H.push({ text: Y, cacheScope: null });
-   if (z) H.push({ text: z, cacheScope: "org" });
-   let J = w.join(`
- 
- `);
-   if (J) H.push({ text: J, cacheScope: "org" });
-   return H;
- }

--- Removed pI2 (pretty-v2.1.22.js:470072-470079)
- function pI2(A, K) {
-   if (A === K) return !0;
-   let q = Object.keys(A),
-     Y = Object.keys(K);
-   if (q.length !== Y.length) return !1;
-   for (let z of q) if (A[z] !== K[z]) return !1;
-   return !0;
- }

--- Removed ZY (pretty-v2.1.22.js:470142-470207)
- function ZY({ children: A, initialState: K, onChangeAppState: q }) {
-   if (I$.useContext(k0K))
-     throw Error(
-       "AppStateProvider can not be nested within another AppStateProvider",
-     );
-   let [z, w] = I$.useState({ currentState: K ?? $PA(), previousState: null }),
-     H = I$.useCallback(
-       (O) => {
-         w((X) => {
-           let { currentState: $ } = X,
-             _ = O($);
-           if (pI2(_, $)) return X;
-           let Z = { currentState: _, previousState: $ };
-           return (
-             q?.({ newState: Z.currentState, oldState: Z.previousState }),
-             Z
-           );
-         });
-       },
-       [q],
-     ),
-     J = I$.useMemo(() => {
-       let O = [z.currentState, H];
-       return ((O.__IS_INITIALIZED__ = !0), O);
-     }, [z.currentState, H]);
-   return (
-     I$.useEffect(() => {
-       let { toolPermissionContext: O } = z.currentState;
-       if (O.isBypassPermissionsModeAvailable && $pA())
-         (h(
-           "Disabling bypass permissions mode on mount (remote settings loaded before mount)",
-         ),
-           H((X) => ({
-             ...X,
-             toolPermissionContext: _pA(X.toolPermissionContext),
-           })));
-     }, []),
-     I$.useEffect(() => {
-       on6(z.currentState.queuedCommands.length);
-     }, [z.currentState.queuedCommands]),
-     yXA(
-       I$.useCallback(
-         (O, X) => {
-           h(`Settings changed from ${O}, updating AppState`);
-           let $ = deA();
-           (QqA(),
-             H((_) => {
-               let Z = C0K(_.toolPermissionContext, $);
-               if (Z.isBypassPermissionsModeAvailable && $pA()) Z = _pA(Z);
-               return { ..._, settings: X, toolPermissionContext: Z };
-             }));
-         },
-         [H],
-       ),
-     ),
-     I$.default.createElement(
-       k0K.Provider,
-       { value: !0 },
-       I$.default.createElement(
-         Uu6.Provider,
-         { value: J },
-         I$.default.createElement(v0K, null, A),
-       ),
-     )
-   );
- }

--- Removed Xy7 (pretty-v2.1.22.js:470216-470220)
- function Xy7() {
-   let A = I$.useContext(Uu6);
-   if (!A.__IS_INITIALIZED__) return null;
-   return A;
- }

--- Removed fT1 (pretty-v2.1.22.js:482565-483015)
- function fT1({ onDone: A }) {
-   let [K] = V6();
-   r8();
-   let q = K.agentDefinitions,
-     Y = iS.useMemo(() => {
-       return K?.mcp?.tools || [];
-     }, [K?.mcp?.tools]),
-     [z, w] = iS.useState(null),
-     [H, J] = iS.useState(null),
-     [O, X] = iS.useState(null),
-     [$, _] = iS.useState(null),
-     Z = jT1(),
-     G = iS.useMemo(
-       () =>
-         ut().then((P) => {
-           return (P.installationType === "native" ? F7K : g7K)().catch(() => ({
-             latest: null,
-             stable: null,
-           }));
-         }),
-       [],
-     ),
-     W = oq()?.autoUpdatesChannel ?? "latest",
-     D = Z.filter((P) => P.mcpErrorMetadata === void 0),
-     j = iS.useMemo(() => E_K(), []);
-   iS.useEffect(() => {
-     (ut().then(w),
-       (async () => {
-         let P = xA(),
-           V = tB6(H8(), "agents"),
-           N = tB6(f8(), ".claude", "agents"),
-           { activeAgents: T, allAgents: E, failedFiles: R } = q,
-           b = {
-             activeAgents: T.map((B) => ({
-               agentType: B.agentType,
-               source: B.source,
-             })),
-             userAgentsDir: V,
-             projectAgentsDir: N,
-             userDirExists: P.existsSync(V),
-             projectDirExists: P.existsSync(N),
-             failedFiles: R,
-           };
-         J(b);
-         let S = await C_K(
-           Y,
-           { activeAgents: T, allAgents: E, failedFiles: R },
-           async () => K.toolPermissionContext,
-         );
-         if ((X(S), V9A())) {
-           let B = tB6(sN1(), "claude", "locks"),
-             x = KT1(B),
-             F = yB6(B);
-           _({ enabled: !0, locks: F, locksDir: B, staleLocksCleaned: x });
-         } else
-           _({ enabled: !1, locks: [], locksDir: "", staleLocksCleaned: 0 });
-       })());
-   }, [K.toolPermissionContext, Y, q]);
-   let M = p8.useCallback(() => {
-     A("Claude Code diagnostics dismissed", { display: "system" });
-   }, [A]);
-   if (
-     (O7({ "confirm:yes": M, "confirm:no": M }, { context: "Confirmation" }), !z)
-   )
-     return p8.default.createElement(
-       I,
-       { paddingX: 1, paddingTop: 1 },
-       p8.default.createElement(
-         f,
-         { dimColor: !0 },
-         "Checking installation status…",
-       ),
-     );
-   return p8.default.createElement(
-     I,
-     { flexDirection: "column", gap: 1, paddingX: 1, paddingTop: 1 },
-     p8.default.createElement(
-       I,
-       { flexDirection: "column" },
-       p8.default.createElement(f, { bold: !0 }, "Diagnostics"),
-       p8.default.createElement(
-         f,
-         null,
-         "└ Currently running: ",
-         z.installationType,
-         " (",
-         z.version,
-         ")",
-       ),
-       z.packageManager &&
-         p8.default.createElement(
-           f,
-           null,
-           "└ Package manager: ",
-           z.packageManager,
-         ),
-       p8.default.createElement(f, null, "└ Path: ", z.installationPath),
-       p8.default.createElement(f, null, "└ Invoked: ", z.invokedBinary),
-       p8.default.createElement(
-         f,
-         null,
-         "└ Config install method: ",
-         z.configInstallMethod,
-       ),
-       p8.default.createElement(
-         f,
-         null,
-         "└ Search: ",
-         z.ripgrepStatus.working ? "OK" : "Not working",
-         " (",
-         z.ripgrepStatus.mode === "builtin"
-           ? i9()
-             ? "bundled"
-             : "vendor"
-           : z.ripgrepStatus.systemPath || "system",
-         ")",
-       ),
-       z.recommendation &&
-         p8.default.createElement(
-           p8.default.Fragment,
-           null,
-           p8.default.createElement(f, null),
-           p8.default.createElement(
-             f,
-             { color: "warning" },
-             "Recommendation: ",
-             z.recommendation.split(`
- `)[0],
-           ),
-           p8.default.createElement(
-             f,
-             { dimColor: !0 },
-             z.recommendation.split(`
- `)[1],
-           ),
-         ),
-       z.multipleInstallations.length > 1 &&
-         p8.default.createElement(
-           p8.default.Fragment,
-           null,
-           p8.default.createElement(f, null),
-           p8.default.createElement(
-             f,
-             { color: "warning" },
-             "Warning: Multiple installations found",
-           ),
-           z.multipleInstallations.map((P, V) =>
-             p8.default.createElement(
-               f,
-               { key: V },
-               "└ ",
-               P.type,
-               " at ",
-               P.path,
-             ),
-           ),
-         ),
-       z.warnings.length > 0 &&
-         p8.default.createElement(
-           p8.default.Fragment,
-           null,
-           p8.default.createElement(f, null),
-           z.warnings.map((P, V) =>
-             p8.default.createElement(
-               I,
-               { key: V, flexDirection: "column" },
-               p8.default.createElement(
-                 f,
-                 { color: "warning" },
-                 "Warning: ",
-                 P.issue,
-               ),
-               p8.default.createElement(f, null, "Fix: ", P.fix),
-             ),
-           ),
-         ),
-       D.length > 0 &&
-         p8.default.createElement(
-           I,
-           { flexDirection: "column", marginTop: 1, marginBottom: 1 },
-           p8.default.createElement(f, { bold: !0 }, "Invalid Settings"),
-           p8.default.createElement(MT1, { errors: D }),
-         ),
-     ),
-     p8.default.createElement(
-       I,
-       { flexDirection: "column" },
-       p8.default.createElement(f, { bold: !0 }, "Updates"),
-       p8.default.createElement(
-         f,
-         null,
-         "└ Auto-updates:",
-         " ",
-         z.packageManager ? "Managed by package manager" : z.autoUpdates,
-       ),
-       z.hasUpdatePermissions !== null &&
-         p8.default.createElement(
-           f,
-           null,
-           "└ Update permissions:",
-           " ",
-           z.hasUpdatePermissions ? "Yes" : "No (requires sudo)",
-         ),
-       p8.default.createElement(f, null, "└ Auto-update channel: ", W),
-       p8.default.createElement(
-         p8.Suspense,
-         { fallback: null },
-         p8.default.createElement(sx2, { promise: G }),
-       ),
-     ),
-     p8.default.createElement(R_K, null),
-     p8.default.createElement(VT1, null),
-     p8.default.createElement(T_K, null),
-     j.length > 0 &&
-       p8.default.createElement(
-         I,
-         { flexDirection: "column" },
-         p8.default.createElement(f, { bold: !0 }, "Environment Variables"),
-         j.map((P, V) =>
-           p8.default.createElement(
-             f,
-             { key: V },
-             "└ ",
-             P.name,
-             ":",
-             " ",
-             p8.default.createElement(
-               f,
-               { color: P.status === "capped" ? "warning" : "error" },
-               P.message,
-             ),
-           ),
-         ),
-       ),
-     $?.enabled &&
-       p8.default.createElement(
-         I,
-         { flexDirection: "column" },
-         p8.default.createElement(f, { bold: !0 }, "Version Locks"),
-         $.staleLocksCleaned > 0 &&
-           p8.default.createElement(
-             f,
-             { dimColor: !0 },
-             "└ Cleaned ",
-             $.staleLocksCleaned,
-             " stale lock(s)",
-           ),
-         $.locks.length === 0
-           ? p8.default.createElement(
-               f,
-               { dimColor: !0 },
-               "└ No active version locks",
-             )
-           : $.locks.map((P, V) =>
-               p8.default.createElement(
-                 f,
-                 { key: V },
-                 "└ ",
-                 P.version,
-                 ": PID ",
-                 P.pid,
-                 " ",
-                 P.isProcessRunning
-                   ? p8.default.createElement(f, null, "(running)")
-                   : p8.default.createElement(
-                       f,
-                       { color: "warning" },
-                       "(stale)",
-                     ),
-               ),
-             ),
-       ),
-     H?.failedFiles &&
-       H.failedFiles.length > 0 &&
-       p8.default.createElement(
-         I,
-         { flexDirection: "column" },
-         p8.default.createElement(
-           f,
-           { bold: !0, color: "error" },
-           "Agent Parse Errors",
-         ),
-         p8.default.createElement(
-           f,
-           { color: "error" },
-           "└ Failed to parse ",
-           H.failedFiles.length,
-           " agent file(s):",
-         ),
-         H.failedFiles.map((P, V) =>
-           p8.default.createElement(
-             f,
-             { key: V, dimColor: !0 },
-             "  ",
-             "└ ",
-             P.path,
-             ": ",
-             P.error,
-           ),
-         ),
-       ),
-     K.plugins.errors.length > 0 &&
-       p8.default.createElement(
-         I,
-         { flexDirection: "column" },
-         p8.default.createElement(
-           f,
-           { bold: !0, color: "error" },
-           "Plugin Errors",
-         ),
-         p8.default.createElement(
-           f,
-           { color: "error" },
-           "└ ",
-           K.plugins.errors.length,
-           " plugin error(s) detected:",
-         ),
-         K.plugins.errors.map((P, V) =>
-           p8.default.createElement(
-             f,
-             { key: V, dimColor: !0 },
-             "  ",
-             "└ ",
-             P.source || "unknown",
-             "plugin" in P && P.plugin ? ` [${P.plugin}]` : "",
-             ":",
-             " ",
-             JM(P),
-           ),
-         ),
-       ),
-     O?.unreachableRulesWarning &&
-       p8.default.createElement(
-         I,
-         { flexDirection: "column" },
-         p8.default.createElement(
-           f,
-           { bold: !0, color: "warning" },
-           "Unreachable Permission Rules",
-         ),
-         p8.default.createElement(
-           f,
-           null,
-           "└",
-           " ",
-           p8.default.createElement(
-             f,
-             { color: "warning" },
-             q1.warning,
-             " ",
-             O.unreachableRulesWarning.message,
-           ),
-         ),
-         O.unreachableRulesWarning.details.map((P, V) =>
-           p8.default.createElement(f, { key: V, dimColor: !0 }, "  ", "└ ", P),
-         ),
-       ),
-     O &&
-       (O.claudeMdWarning || O.agentWarning || O.mcpWarning) &&
-       p8.default.createElement(
-         I,
-         { flexDirection: "column" },
-         p8.default.createElement(f, { bold: !0 }, "Context Usage Warnings"),
-         O.claudeMdWarning &&
-           p8.default.createElement(
-             p8.default.Fragment,
-             null,
-             p8.default.createElement(
-               f,
-               null,
-               "└",
-               " ",
-               p8.default.createElement(
-                 f,
-                 { color: "warning" },
-                 q1.warning,
-                 " ",
-                 O.claudeMdWarning.message,
-               ),
-             ),
-             p8.default.createElement(f, null, "  ", "└ Files:"),
-             O.claudeMdWarning.details.map((P, V) =>
-               p8.default.createElement(
-                 f,
-                 { key: V, dimColor: !0 },
-                 "    ",
-                 "└ ",
-                 P,
-               ),
-             ),
-           ),
-         O.agentWarning &&
-           p8.default.createElement(
-             p8.default.Fragment,
-             null,
-             p8.default.createElement(
-               f,
-               null,
-               "└",
-               " ",
-               p8.default.createElement(
-                 f,
-                 { color: "warning" },
-                 q1.warning,
-                 " ",
-                 O.agentWarning.message,
-               ),
-             ),
-             p8.default.createElement(f, null, "  ", "└ Top contributors:"),
-             O.agentWarning.details.map((P, V) =>
-               p8.default.createElement(
-                 f,
-                 { key: V, dimColor: !0 },
-                 "    ",
-                 "└ ",
-                 P,
-               ),
-             ),
-           ),
-         O.mcpWarning &&
-           p8.default.createElement(
-             p8.default.Fragment,
-             null,
-             p8.default.createElement(
-               f,
-               null,
-               "└",
-               " ",
-               p8.default.createElement(
-                 f,
-                 { color: "warning" },
-                 q1.warning,
-                 " ",
-                 O.mcpWarning.message,
-               ),
-             ),
-             p8.default.createElement(f, null, "  ", "└ MCP servers:"),
-             O.mcpWarning.details.map((P, V) =>
-               p8.default.createElement(
-                 f,
-                 { key: V, dimColor: !0 },
-                 "    ",
-                 "└ ",
-                 P,
-               ),
-             ),
-           ),
-       ),
-     p8.default.createElement(I, null, p8.default.createElement(LPA, null)),
-   );
- }

--- Removed NTK (pretty-v2.1.22.js:527657-527658)
- var NTK =
-     "IMPORTANT: Assist with defensive security tasks only. Refuse to create, modify, or improve code that may be used maliciously. Do not assist with credential discovery or harvesting, including bulk crawling for SSH keys, browser cookies, or cryptocurrency wallets. Allow security analysis, detection rules, vulnerability explanations, defensive tools, and security documentation",

--- Removed OP1 (pretty-v2.1.22.js:531295-531298)
- function OP1() {
-   let A = sq();
-   return A === "max" || A === "enterprise" || A === "team" || A === null;
- }

--- Removed Wt2 (pretty-v2.1.22.js:537560-537647)
- var Wt2 = `## Settings File Locations
- 
- Choose the appropriate file based on scope:
- 
- | File | Scope | Git | Use For |
- |------|-------|-----|---------|
- | \`~/.claude/settings.json\` | Global | N/A | Personal preferences for all projects |
- | \`.claude/settings.json\` | Project | Commit | Team-wide hooks, permissions, plugins |
- | \`.claude/settings.local.json\` | Project | Gitignore | Personal overrides for this project |
- 
- Settings load in order: user → project → local (later overrides earlier).
- 
- ## Settings Schema Reference
- 
- ### Permissions
- \`\`\`json
- {
-   "permissions": {
-     "allow": ["Bash(npm:*)", "Edit(.claude)", "Read"],
-     "deny": ["Bash(rm -rf:*)"],
-     "ask": ["Write(/etc/*)"],
-     "defaultMode": "default" | "plan" | "acceptEdits" | "dontAsk",
-     "additionalDirectories": ["/extra/dir"]
-   }
- }
- \`\`\`
- 
- **Permission Rule Syntax:**
- - Exact match: \`"Bash(npm run test)"\`
- - Prefix wildcard: \`"Bash(git:*)"\` - matches \`git status\`, \`git commit\`, etc.
- - Tool only: \`"Read"\` - allows all Read operations
- 
- ### Environment Variables
- \`\`\`json
- {
-   "env": {
-     "DEBUG": "true",
-     "MY_API_KEY": "value"
-   }
- }
- \`\`\`
- 
- ### Model & Agent
- \`\`\`json
- {
-   "model": "sonnet",  // or "opus", "haiku", full model ID
-   "agent": "agent-name",
-   "alwaysThinkingEnabled": true
- }
- \`\`\`
- 
- ### Attribution (Commits & PRs)
- \`\`\`json
- {
-   "attribution": {
-     "commit": "Custom commit trailer text",
-     "pr": "Custom PR description text"
-   }
- }
- \`\`\`
- Set \`commit\` or \`pr\` to empty string \`""\` to hide that attribution.
- 
- ### MCP Server Management
- \`\`\`json
- {
-   "enableAllProjectMcpServers": true,
-   "enabledMcpjsonServers": ["server1", "server2"],
-   "disabledMcpjsonServers": ["blocked-server"]
- }
- \`\`\`
- 
- ### Plugins
- \`\`\`json
- {
-   "enabledPlugins": {
-     "formatter@anthropic-tools": true
-   }
- }
- \`\`\`
- Plugin syntax: \`plugin-name@source\` where source is \`claude-code-marketplace\`, \`claude-plugins-official\`, or \`builtin\`.
- 
- ### Other Settings
- - \`language\`: Preferred response language (e.g., "japanese")
- - \`cleanupPeriodDays\`: Days to keep transcripts (0 = forever)
- - \`respectGitignore\`: Whether to respect .gitignore (default: true)
- - \`spinnerTipsEnabled\`: Show tips in spinner
- - \`syntaxHighlightingDisabled\`: Disable diff highlighting
- `,

--- Removed ykK (pretty-v2.1.22.js:538857-538857)
-   ykK = !1;

--- Removed QU6 (pretty-v2.1.22.js:545463-545493)
- var QU6 = C(() => {
-   BA();
-   y9();
-   W9();
-   Xv();
-   KL();
-   se();
-   A4();
-   Jw();
-   uE1();
-   i1();
-   l4();
-   Vm();
-   nH();
-   PZ();
-   OK();
-   s1();
-   UK();
-   j8();
-   l_();
-   L4();
-   PS();
-   uMA();
-   xd();
-   Ow();
-   t2();
-   pD();
-   gU6();
-   YpA();
-   ((F5 = r($A(), 1)), (zJ = r($A(), 1)), (FU6 = [2, 3, 4, 6, 8]));
- });

--- Removed CRK (pretty-v2.1.22.js:551559-551689)
- function CRK(A) {
-   let K = s(36),
-     { tasksSelected: q, showHint: Y, isViewingTeammate: z } = A,
-     { columns: w } = M8(),
-     H;
-   if (K[0] === Symbol.for("react.memo_cache_sentinel"))
-     ((H = D1()), (K[0] = H));
-   else H = K[0];
-   let J = H.hasSeenTasksHint,
-     [O] = V6(),
-     { tasks: X } = O,
-     $;
-   if (K[1] !== Y || K[2] !== q)
-     (($ =
-       Y && (q || !J)
-         ? CY.createElement(
-             CY.Fragment,
-             null,
-             CY.createElement(f, { dimColor: !0 }, " · "),
-             CY.createElement(
-               f,
-               { dimColor: !0 },
-               q
-                 ? CY.createElement(G6, {
-                     shortcut: "Enter",
-                     action: "view tasks",
-                   })
-                 : CY.createElement(G6, { shortcut: "↓", action: "view" }),
-             ),
-           )
-         : null),
-       (K[1] = Y),
-       (K[2] = q),
-       (K[3] = $));
-   else $ = K[3];
-   let _ = $,
-     Z;
-   if (K[4] !== X)
-     ((Z = Object.values(X ?? {}).filter(p9A)), (K[4] = X), (K[5] = Z));
-   else Z = K[5];
-   let G = Z;
-   if (G.length === 0) {
-     if (z) {
-       let W;
-       if (K[6] !== q)
-         ((W = CY.createElement(
-           f,
-           { color: "background", inverse: q },
-           "1 team",
-         )),
-           (K[6] = q),
-           (K[7] = W));
-       else W = K[7];
-       let D;
-       if (K[8] !== _ || K[9] !== W)
-         ((D = CY.createElement(CY.Fragment, null, W, _)),
-           (K[8] = _),
-           (K[9] = W),
-           (K[10] = D));
-       else D = K[10];
-       return D;
-     }
-     return null;
-   }
-   if (G.length === 1 && w >= 150) {
-     let W = G[0],
-       D,
-       j,
-       M,
-       P;
-     if (K[11] !== W || K[12] !== q) {
-       let E = j1z(W);
-       ((D = f),
-         (j = "background"),
-         (M = q),
-         (P = a9(E, 40, !0)),
-         (K[11] = W),
-         (K[12] = q),
-         (K[13] = D),
-         (K[14] = j),
-         (K[15] = M),
-         (K[16] = P));
-     } else ((D = K[13]), (j = K[14]), (M = K[15]), (P = K[16]));
-     let V;
-     if (K[17] !== W.status)
-       ((V = CY.createElement(f, { dimColor: !0 }, "(", W.status, ")")),
-         (K[17] = W.status),
-         (K[18] = V));
-     else V = K[18];
-     let N;
-     if (K[19] !== D || K[20] !== j || K[21] !== M || K[22] !== P || K[23] !== V)
-       ((N = CY.createElement(D, { color: j, inverse: M }, P, " ", V)),
-         (K[19] = D),
-         (K[20] = j),
-         (K[21] = M),
-         (K[22] = P),
-         (K[23] = V),
-         (K[24] = N));
-     else N = K[24];
-     let T;
-     if (K[25] !== _ || K[26] !== N)
-       ((T = CY.createElement(CY.Fragment, null, N, _)),
-         (K[25] = _),
-         (K[26] = N),
-         (K[27] = T));
-     else T = K[27];
-     return T;
-   }
-   if (G.length >= 1) {
-     let W;
-     if (K[28] !== G) ((W = M1z(G)), (K[28] = G), (K[29] = W));
-     else W = K[29];
-     let D = W,
-       j;
-     if (K[30] !== D || K[31] !== q)
-       ((j = CY.createElement(f, { color: "background", inverse: q }, D)),
-         (K[30] = D),
-         (K[31] = q),
-         (K[32] = j));
-     else j = K[32];
-     let M;
-     if (K[33] !== _ || K[34] !== j)
-       ((M = CY.createElement(CY.Fragment, null, j, _)),
-         (K[33] = _),
-         (K[34] = j),
-         (K[35] = M));
-     else M = K[35];
-     return M;
-   }
-   return null;
- }

--- Removed I1z (pretty-v2.1.22.js:552146-552415)
- function I1z(A) {
-   let K = s(56),
-     {
-       mode: q,
-       toolPermissionContext: Y,
-       showHint: z,
-       tasksSelected: w,
-       teamsSelected: H,
-       diffSelected: J,
-       loopSelected: O,
-     } = A,
-     { columns: X } = M8(),
-     $ = BK("chat:cycleMode", "Chat", "shift+tab"),
-     [_] = V6(),
-     { tasks: Z, teamContext: G, remoteSessionUrl: W, viewSelectionMode: D } = _,
-     j;
-   if (K[0] === Symbol.for("react.memo_cache_sentinel")) ((j = !1), (K[0] = j));
-   else j = K[0];
-   let M = j,
-     P;
-   if (K[1] !== Z) ((P = Object.values(Z).filter(p9A)), (K[1] = Z), (K[2] = P));
-   else P = K[2];
-   let V = P.length,
-     N = hRK(),
-     T;
-   if (K[3] !== N?.stats)
-     ((T = V4("tengu_code_diff_cli", !1) ? (N?.stats ?? null) : null),
-       (K[3] = N?.stats),
-       (K[4] = T));
-   else T = K[4];
-   let E = T,
-     R = _.prStatus,
-     b;
-   if (K[5] !== G)
-     ((b =
-       D8() &&
-       !qm() &&
-       G !== void 0 &&
-       Object.values(G.teammates).filter(S1z).length > 0),
-       (K[5] = G),
-       (K[6] = b));
-   else b = K[6];
-   let S = b;
-   if (q === "bash") {
-     let t;
-     if (K[7] === Symbol.for("react.memo_cache_sentinel"))
-       ((t = jq.createElement(f, { color: "bashBorder" }, "! for bash mode")),
-         (K[7] = t));
-     else t = K[7];
-     return t;
-   }
-   if (q === "background") {
-     let t;
-     if (K[8] === Symbol.for("react.memo_cache_sentinel"))
-       ((t = jq.createElement(f, { color: "background" }, "& to background")),
-         (K[8] = t));
-     else t = K[8];
-     return t;
-   }
-   let B = Y?.mode,
-     x;
-   if (K[9] !== B) ((x = aL8(B)), (K[9] = B), (K[10] = x));
-   else x = K[10];
-   let F = !x,
-     Q = D === "viewing-agent",
-     u = V > 0 || Q,
-     d = (M ? 1 : 0) + (F ? 1 : 0) + (u ? 1 : 0) + (S ? 1 : 0),
-     o;
-   if (K[11] === Symbol.for("react.memo_cache_sentinel"))
-     ((o = D1()), (K[11] = o));
-   else o = K[11];
-   let wA =
-       (o.codeDiffFooterEnabled ?? !0) &&
-       E &&
-       E.filesCount > 0 &&
-       d < 2 &&
-       (d === 0 || X >= 100),
-     HA;
-   if (K[12] !== X || K[13] !== R || K[14] !== d)
-     ((HA =
-       FRK() &&
-       R.number !== null &&
-       R.reviewState !== null &&
-       R.url !== null &&
-       d < 2 &&
-       (d === 0 || X >= 100)),
-       (K[12] = X),
-       (K[13] = R),
-       (K[14] = d),
-       (K[15] = HA));
-   else HA = K[15];
-   let OA = HA,
-     WA = d < 2,
-     a;
-   if (K[16] !== W)
-     ((a = W
-       ? [
-           jq.createElement(
-             f,
-             { color: "ide", key: "remote" },
-             q1.circleDouble,
-             " remote",
-           ),
-         ]
-       : []),
-       (K[16] = W),
-       (K[17] = a));
-   else a = K[17];
-   let _A;
-   if (K[18] !== B || K[19] !== F || K[20] !== $ || K[21] !== WA)
-     ((_A =
-       B && F
-         ? [
-             jq.createElement(
-               f,
-               { color: qD(B), key: "mode" },
-               TEA(B),
-               " ",
-               XF(B).toLowerCase(),
-               " on",
-               WA &&
-                 jq.createElement(
-                   f,
-                   { dimColor: !0 },
-                   " ",
-                   jq.createElement(G6, {
-                     shortcut: $,
-                     action: "cycle",
-                     parens: !0,
-                   }),
-                 ),
-             ),
-           ]
-         : []),
-       (K[18] = B),
-       (K[19] = F),
-       (K[20] = $),
-       (K[21] = WA),
-       (K[22] = _A));
-   else _A = K[22];
-   let jA;
-   if (K[23] !== O || K[24] !== z)
-     ((jA = []), (K[23] = O), (K[24] = z), (K[25] = jA));
-   else jA = K[25];
-   let PA;
-   if (K[26] !== u || K[27] !== S || K[28] !== Q || K[29] !== z || K[30] !== w)
-     ((PA = u
-       ? [
-           jq.createElement(CRK, {
-             key: "tasks",
-             tasksSelected: w,
-             showHint: z && !S,
-             isViewingTeammate: Q,
-           }),
-         ]
-       : []),
-       (K[26] = u),
-       (K[27] = S),
-       (K[28] = Q),
-       (K[29] = z),
-       (K[30] = w),
-       (K[31] = PA));
-   else PA = K[31];
-   let SA;
-   if (K[32] !== u || K[33] !== S || K[34] !== z || K[35] !== H)
-     ((SA =
-       D8() && S
-         ? [
-             jq.createElement(RRK, {
-               key: "teams",
-               teamsSelected: H,
-               showHint: z && !u,
-             }),
-           ]
-         : []),
-       (K[32] = u),
-       (K[33] = S),
-       (K[34] = z),
-       (K[35] = H),
-       (K[36] = SA));
-   else SA = K[36];
-   let mA;
-   if (K[37] !== E || K[38] !== J || K[39] !== wA || K[40] !== z)
-     ((mA = wA
-       ? [
-           jq.createElement(
-             f,
-             {
-               key: "code-changes",
-               dimColor: !J,
-               inverse: J,
-               color: J ? "background" : void 0,
-             },
-             E.filesCount,
-             " ",
-             E.filesCount === 1 ? "file" : "files",
-             " ",
-             jq.createElement(f, { color: "diffAddedWord" }, "+", E.linesAdded),
-             " ",
-             jq.createElement(
-               f,
-               { color: "diffRemovedWord" },
-               "-",
-               E.linesRemoved,
-             ),
-             J && z && jq.createElement(f, { dimColor: !0 }, " · Enter to view"),
-           ),
-         ]
-       : []),
-       (K[37] = E),
-       (K[38] = J),
-       (K[39] = wA),
-       (K[40] = z),
-       (K[41] = mA));
-   else mA = K[41];
-   let qA;
-   if (K[42] !== R || K[43] !== OA)
-     ((qA = OA
-       ? [
-           jq.createElement(
-             f,
-             { key: "pr-status", dimColor: !0 },
-             jq.createElement(f, { color: h1z(R.reviewState) }, "PR"),
-             " ",
-             jq.createElement(G7, { url: R.url }, "#", R.number),
-           ),
-         ]
-       : []),
-       (K[42] = R),
-       (K[43] = OA),
-       (K[44] = qA));
-   else qA = K[44];
-   let YA;
-   if (
-     K[45] !== jA ||
-     K[46] !== PA ||
-     K[47] !== SA ||
-     K[48] !== mA ||
-     K[49] !== qA ||
-     K[50] !== a ||
-     K[51] !== _A
-   )
-     ((YA = [...a, ..._A, ...jA, ...PA, ...SA, ...mA, ...qA]),
-       (K[45] = jA),
-       (K[46] = PA),
-       (K[47] = SA),
-       (K[48] = mA),
-       (K[49] = qA),
-       (K[50] = a),
-       (K[51] = _A),
-       (K[52] = YA));
-   else YA = K[52];
-   let JA = YA;
-   if (JA.length) {
-     let t;
-     if (K[53] !== JA)
-       ((t = jq.createElement(I, null, jq.createElement(w8, null, JA))),
-         (K[53] = JA),
-         (K[54] = t));
-     else t = K[54];
-     return t;
-   }
-   if (!z) return null;
-   let AA;
-   if (K[55] === Symbol.for("react.memo_cache_sentinel"))
-     ((AA = jq.createElement(f, { dimColor: !0 }, "? for shortcuts")),
-       (K[55] = AA));
-   else AA = K[55];
-   return AA;
- }

--- Removed E6z (pretty-v2.1.22.js:555164-555183)
- function E6z(A, K, q) {
-   let Y = A.split(`
- `),
-     z = 0,
-     w = [];
-   for (let H of Y) {
-     let J = Math.max(1, Math.ceil(H.length / q));
-     if (z + J > K) {
-       let O = K - z;
-       if (O > 0) {
-         let X = O * q;
-         w.push(H.slice(0, X) + "...");
-       }
-       break;
-     }
-     (w.push(H), (z += J));
-   }
-   return w.join(`
- `);
- }

--- Removed ByK (pretty-v2.1.22.js:555184-555298)
- function ByK() {
-   let A = s(26),
-     { columns: K } = M8(),
-     [q] = V6(),
-     { inbox: Y } = q;
-   if (IG()) return null;
-   if (IqA(q)) return null;
-   let z = Y.messages,
-     w,
-     H,
-     J,
-     O,
-     X,
-     $,
-     _,
-     Z,
-     G;
-   if (A[0] !== K || A[1] !== Y.messages) {
-     G = Symbol.for("react.early_return_sentinel");
-     A: {
-       let j = z.filter(k6z);
-       if (j.length === 0) {
-         G = null;
-         break A;
-       }
-       let M = j.slice(0, v6z);
-       H = j.length - M.length;
-       let P = Math.max(20, K - 4 - 2 - 4);
-       ((w = I), (J = 1), (O = 2), (X = "column"), ($ = K - 4));
-       let V = j.length === 1 ? "message" : "messages";
-       if (A[11] !== V)
-         ((_ = Hh.createElement(
-           f,
-           { dimColor: !0 },
-           "Queued teammate ",
-           V,
-           ":",
-         )),
-           (A[11] = V),
-           (A[12] = _));
-       else _ = A[12];
-       let N;
-       if (A[13] !== P)
-         ((N = (T, E) =>
-           Hh.createElement(
-             f,
-             { key: E, color: Pv(T.color), wrap: "wrap" },
-             "● ",
-             Hh.createElement(f, { bold: !0 }, "@", T.from, ":"),
-             " ",
-             E6z(I8K(T.text), T6z, P),
-           )),
-           (A[13] = P),
-           (A[14] = N));
-       else N = A[14];
-       Z = M.map(N);
-     }
-     ((A[0] = K),
-       (A[1] = Y.messages),
-       (A[2] = w),
-       (A[3] = H),
-       (A[4] = J),
-       (A[5] = O),
-       (A[6] = X),
-       (A[7] = $),
-       (A[8] = _),
-       (A[9] = Z),
-       (A[10] = G));
-   } else
-     ((w = A[2]),
-       (H = A[3]),
-       (J = A[4]),
-       (O = A[5]),
-       (X = A[6]),
-       ($ = A[7]),
-       (_ = A[8]),
-       (Z = A[9]),
-       (G = A[10]));
-   if (G !== Symbol.for("react.early_return_sentinel")) return G;
-   let W;
-   if (A[15] !== H)
-     ((W = H > 0 && Hh.createElement(f, { dimColor: !0 }, "(...", H, " more)")),
-       (A[15] = H),
-       (A[16] = W));
-   else W = A[16];
-   let D;
-   if (
-     A[17] !== w ||
-     A[18] !== J ||
-     A[19] !== O ||
-     A[20] !== X ||
-     A[21] !== $ ||
-     A[22] !== _ ||
-     A[23] !== Z ||
-     A[24] !== W
-   )
-     ((D = Hh.createElement(
-       w,
-       { marginTop: J, paddingLeft: O, flexDirection: X, width: $ },
-       _,
-       Z,
-       W,
-     )),
-       (A[17] = w),
-       (A[18] = J),
-       (A[19] = O),
-       (A[20] = X),
-       (A[21] = $),
-       (A[22] = _),
-       (A[23] = Z),
-       (A[24] = W),
-       (A[25] = D));
-   else D = A[25];
-   return D;
- }

--- Removed k6z (pretty-v2.1.22.js:555299-555301)
- function k6z(A) {
-   return A.status === "pending" && !N6z(A.text);
- }

--- Removed AIK (pretty-v2.1.22.js:555986-556030)
- function AIK({
-   suggestion: A,
-   isSpeculating: K,
-   timeSavedMs: q,
-   availableWidth: Y,
- }) {
-   let z = (X) => (A.length > X ? A.slice(0, Math.max(0, X)) : A);
-   if (K) {
-     let X = z(Y);
-     return wG.createElement(SN1, {
-       text: X,
-       highlights: [
-         {
-           start: 0,
-           end: X.length,
-           style: {
-             type: "shimmer",
-             baseColor: "inactive",
-             shimmerColor: "subtle",
-           },
-           priority: 0,
-         },
-       ],
-     });
-   }
-   let w =
-       q !== null && q >= y6z
-         ? `${q1.play}${q1.play} ${Math.round(q / 1000)}s`
-         : null,
-     H = w ? x7(w) + 2 : 0,
-     J = z(Y - H),
-     O = Math.max(0, Y - x7(J) - H);
-   return wG.createElement(
-     wG.Fragment,
-     null,
-     wG.createElement(f, { dimColor: !0 }, J),
-     w &&
-       wG.createElement(
-         wG.Fragment,
-         null,
-         wG.createElement(f, null, " ".repeat(O)),
-         wG.createElement(f, { dimColor: !0 }, w),
-       ),
-   );
- }

--- Removed CSK (pretty-v2.1.22.js:560767-560791)
- function CSK({ onBackgroundSession: A, isLoading: K }) {
-   let [q, Y] = V6(),
-     z = pVA.useRef(q);
-   z.current = q;
-   let [w, H] = pVA.useState(!1),
-     J = Ey(H, A, () => {}),
-     O = pVA.useCallback(() => {
-       if (j1(process.env.CLAUDE_CODE_DISABLE_BACKGROUND_TASKS)) return;
-       let _ = z.current;
-       if (QD7(_)) J_1(() => z.current, Y);
-     }, [Y, K, J]);
-   A6("task:background", O, { context: "Task" });
-   let X = BK("task:background", "Task", "ctrl+b"),
-     $ = Q6.terminal === "tmux" && X === "ctrl+b" ? "ctrl+b ctrl+b" : X;
-   if (!K || !w) return null;
-   return WYA.createElement(
-     I,
-     { paddingLeft: 2 },
-     WYA.createElement(
-       f,
-       { dimColor: !0 },
-       WYA.createElement(G6, { shortcut: $, action: "background" }),
-     ),
-   );
- }

--- Removed l7z (pretty-v2.1.22.js:571106-571106)
-   l7z = 5000,

--- Removed JUK (pretty-v2.1.22.js:576705-576705)
- var JUK = {};

--- Removed zUK (pretty-v2.1.22.js:579635-579635)
-   zUK = () => (gQA(), Vh(yKK));

=== Added ===

+++ Added zR1 (pretty-v2.1.23.js:1800-1800)
+   zR1 = "effort-2025-11-24",

+++ Added gn6 (pretty-v2.1.23.js:1801-1801)
+   gn6 = "prompt-caching-scope-2026-01-05",

+++ Added gr6 (pretty-v2.1.23.js:2394-2396)
+ function gr6() {
+   f6.promptCacheBreaks = [];
+ }

+++ Added s8A (pretty-v2.1.23.js:157730-157738)
+ function s8A() {
+   let A = dn(),
+     K = L46();
+   if (A) {
+     if (typeof Bun < "u") return { proxy: A, ...K };
+     return { dispatcher: JH4(A) };
+   }
+   return K;
+ }

+++ Added DH4 (pretty-v2.1.23.js:157998-158005)
+ async function DH4() {
+   if (INA() !== null) return;
+   if (c7() !== "bedrock") {
+     bnA(wyA(c7()));
+     return;
+   }
+   await WH4();
+ }

+++ Added KJ4 (pretty-v2.1.23.js:160569-160753)
+ var KJ4 = k(() => {
+   eH4 = `Use this tool to create and manage a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user.
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
+ * Uses the ${m5} tool to add a comment to the calculateTotal function *
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

+++ Added C51 (pretty-v2.1.23.js:176310-176335)
+ class C51 {
+   strings = [" ", ""];
+   stringMap = new Map([
+     [" ", 0],
+     ["", 1],
+   ]);
+   ascii = Zt3();
+   intern(A) {
+     if (A.length === 1) {
+       let Y = A.charCodeAt(0);
+       if (Y < 128) {
+         let z = this.ascii[Y];
+         if (z !== -1) return z;
+         let w = this.strings.length;
+         return (this.strings.push(A), (this.ascii[Y] = w), w);
+       }
+     }
+     let K = this.stringMap.get(A);
+     if (K !== void 0) return K;
+     let q = this.strings.length;
+     return (this.strings.push(A), this.stringMap.set(A, q), q);
+   }
+   get(A) {
+     return this.strings[A] ?? " ";
+   }
+ }

+++ Added L51 (pretty-v2.1.23.js:176336-176351)
+ class L51 {
+   strings = [""];
+   stringMap = new Map();
+   intern(A) {
+     if (!A) return 0;
+     let K = this.stringMap.get(A);
+     if (K === void 0)
+       ((K = this.strings.length),
+         this.strings.push(A),
+         this.stringMap.set(A, K));
+     return K;
+   }
+   get(A) {
+     return A === 0 ? void 0 : this.strings[A];
+   }
+ }

+++ Added vXA (pretty-v2.1.23.js:176376-176378)
+ function vXA(A, K, q) {
+   return (A << R51) | (K << y51) | q;
+ }

+++ Added Dt3 (pretty-v2.1.23.js:176386-176388)
+ function Dt3(A, K) {
+   return A.hyperlinkPool.intern(K);
+ }

+++ Added x04 (pretty-v2.1.23.js:176430-176449)
+ function x04(A, K, q) {
+   let { charPool: Y, hyperlinkPool: z } = A;
+   if (Y === K && z === q) return;
+   let w = A.width * A.height,
+     H = A.cells;
+   for (let J = 0; J < w << 1; J += 2) {
+     let O = H[J];
+     H[J] = K.intern(Y.get(O));
+     let X = H[J + 1],
+       $ = (X >>> y51) & LK6;
+     if ($ !== 0) {
+       let _ = z.get($),
+         G = q.intern(_),
+         Z = X >>> R51,
+         W = X & j4A;
+       H[J + 1] = vXA(Z, G, W);
+     }
+   }
+   ((A.charPool = K), (A.hyperlinkPool = q));
+ }

+++ Added jt3 (pretty-v2.1.23.js:176454-176464)
+ function jt3(A, K) {
+   let q = K << 1,
+     Y = A.cells[q + 1],
+     z = (Y >>> y51) & LK6;
+   return {
+     char: A.charPool.get(A.cells[q]),
+     styleId: Y >>> R51,
+     width: Y & j4A,
+     hyperlink: z === 0 ? void 0 : A.hyperlinkPool.get(z),
+   };
+ }

+++ Added k51 (pretty-v2.1.23.js:176465-176473)
+ function k51(A, K, q) {
+   let Y = K << 1,
+     z = A.cells[Y + 1];
+   ((q.char = A.charPool.get(A.cells[Y])),
+     (q.styleId = z >>> R51),
+     (q.width = z & j4A));
+   let w = (z >>> y51) & LK6;
+   q.hyperlink = w === 0 ? void 0 : A.hyperlinkPool.get(w);
+ }

+++ Added Mt3 (pretty-v2.1.23.js:176519-176521)
+ function Mt3(A, K) {
+   return A.charPool.intern(K);
+ }

+++ Added u04 (pretty-v2.1.23.js:176522-176552)
+ function u04(A, K, q, Y, z, w) {
+   if (q >= z || Y >= w) return;
+   let H = z - q,
+     J = K.width << 1,
+     O = A.width << 1,
+     X = H << 1,
+     $ = K.cells,
+     _ = A.cells;
+   if (q === 0 && z === K.width && K.width === A.width) {
+     let Z = Y * J,
+       W = (w - Y) * J;
+     _.set($.subarray(Z, Z + W), Z);
+   } else {
+     let Z = Y * J + (q << 1),
+       W = Y * O + (q << 1);
+     for (let D = Y; D < w; D++)
+       (_.set($.subarray(Z, Z + X), W), (Z += J), (W += O));
+   }
+   let G = { x: q, y: Y, width: H, height: w - Y };
+   if (A.damage) A.damage = SyA(A.damage, G);
+   else A.damage = G;
+   if (z < A.width) {
+     let Z = (Y * K.width + (z - 1)) << 1,
+       W = (Y * A.width + z) << 1;
+     for (let D = Y; D < w; D++) {
+       if (($[Z + 1] & j4A) === 1)
+         ((_[W] = I04), (_[W + 1] = vXA(A.emptyStyleId, 0, 2)));
+       ((Z += J), (W += O));
+     }
+   }
+ }

+++ Added R51 (pretty-v2.1.23.js:176642-176642)
+   R51 = 17,

+++ Added LK6 (pretty-v2.1.23.js:176644-176644)
+   LK6 = 32767,

+++ Added S04 (pretty-v2.1.23.js:176646-176646)
+   S04 = 0n,

+++ Added EXA (pretty-v2.1.23.js:176649-176655)
+ var EXA = k(() => {
+   AK6();
+   EK6();
+   O4A();
+   ((m04 = new RegExp(`^${wr}\\]8${Jr}${Jr}([^${Hr}]*)${Hr}$`)),
+     (g04 = `${wr}]8${Jr}`));
+ });

+++ Added Dy4 (pretty-v2.1.23.js:192920-192956)
+ async function Dy4(A, K = 10) {
+   if (process.platform === "win32") {
+     let z = `
+       $pid = ${String(A)}
+       $ancestors = @()
+       for ($i = 0; $i -lt ${K}; $i++) {
+         $proc = Get-CimInstance Win32_Process -Filter "ProcessId=$pid" -ErrorAction SilentlyContinue
+         if (-not $proc -or -not $proc.ParentProcessId -or $proc.ParentProcessId -eq 0) { break }
+         $pid = $proc.ParentProcessId
+         $ancestors += $pid
+       }
+       $ancestors -join ','
+     `.trim(),
+       w = await A7("powershell.exe", ["-NoProfile", "-Command", z], {
+         timeout: 3000,
+       });
+     if (w.code !== 0 || !w.stdout?.trim()) return [];
+     return w.stdout
+       .trim()
+       .split(",")
+       .filter(Boolean)
+       .map((H) => parseInt(H, 10))
+       .filter((H) => !isNaN(H));
+   }
+   let q = `pid=${String(A)}; for i in $(seq 1 ${K}); do ppid=$(ps -o ppid= -p $pid 2>/dev/null | tr -d ' '); if [ -z "$ppid" ] || [ "$ppid" = "0" ] || [ "$ppid" = "1" ]; then break; fi; echo $ppid; pid=$ppid; done`,
+     Y = await A7("sh", ["-c", q], { timeout: 3000 });
+   if (Y.code !== 0 || !Y.stdout?.trim()) return [];
+   return Y.stdout
+     .trim()
+     .split(
+       `
+ `,
+     )
+     .filter(Boolean)
+     .map((z) => parseInt(z, 10))
+     .filter((z) => !isNaN(z));
+ }

+++ Added My4 (pretty-v2.1.23.js:192970-192994)
+ async function My4(A, K = 10) {
+   if (process.platform === "win32") {
+     let z = `
+       $currentPid = ${String(A)}
+       $commands = @()
+       for ($i = 0; $i -lt ${K}; $i++) {
+         $proc = Get-CimInstance Win32_Process -Filter "ProcessId=$currentPid" -ErrorAction SilentlyContinue
+         if (-not $proc) { break }
+         if ($proc.CommandLine) { $commands += $proc.CommandLine }
+         if (-not $proc.ParentProcessId -or $proc.ParentProcessId -eq 0) { break }
+         $currentPid = $proc.ParentProcessId
+       }
+       $commands -join [char]0
+     `.trim(),
+       w = await A7("powershell.exe", ["-NoProfile", "-Command", z], {
+         timeout: 3000,
+       });
+     if (w.code !== 0 || !w.stdout?.trim()) return [];
+     return w.stdout.split("\x00").filter(Boolean);
+   }
+   let q = `currentpid=${String(A)}; for i in $(seq 1 ${K}); do cmd=$(ps -o command= -p $currentpid 2>/dev/null); if [ -n "$cmd" ]; then printf '%s\\0' "$cmd"; fi; ppid=$(ps -o ppid= -p $currentpid 2>/dev/null | tr -d ' '); if [ -z "$ppid" ] || [ "$ppid" = "0" ] || [ "$ppid" = "1" ]; then break; fi; currentpid=$ppid; done`,
+     Y = await A7("sh", ["-c", q], { timeout: 3000 });
+   if (Y.code !== 0 || !Y.stdout?.trim()) return [];
+   return Y.stdout.split("\x00").filter(Boolean);
+ }

+++ Added Py4 (pretty-v2.1.23.js:192998-193009)
+ async function Py4() {
+   if (r4A !== void 0) return r4A;
+   if (process.platform === "darwin") return ((r4A = null), null);
+   try {
+     let A = await My4(process.pid, 10);
+     for (let K of A) {
+       let q = K.toLowerCase();
+       for (let Y of Eb1) if (q.includes(Y)) return ((r4A = Y), Y);
+     }
+   } catch {}
+   return ((r4A = null), null);
+ }

+++ Added VG9 (pretty-v2.1.23.js:193016-193024)
+ function VG9() {
+   if (process.env.TERMINAL_EMULATOR === "JetBrains-JediTerm") {
+     if (m6.platform !== "darwin") {
+       if (r4A !== void 0) return r4A || "pycharm";
+       return "pycharm";
+     }
+   }
+   return m6.terminal;
+ }

+++ Added R36 (pretty-v2.1.23.js:193025-193027)
+ async function R36() {
+   if (process.env.TERMINAL_EMULATOR === "JetBrains-JediTerm") await Py4();
+ }

+++ Added y36 (pretty-v2.1.23.js:193121-193130)
+ function y36(A) {
+   let K = c7();
+   if (K !== "firstParty" && K !== "foundry") return !1;
+   return (
+     A.includes("claude-sonnet-4-5") ||
+     A.includes("claude-opus-4-1") ||
+     A.includes("claude-opus-4-5") ||
+     A.includes("claude-haiku-4-5")
+   );
+ }

+++ Added b8 (pretty-v2.1.23.js:193200-193209)
+ function b8() {
+   if (J2(process.env.CLAUDE_CODE_AGENT_SWARMS)) return !1;
+   if (!G4("tengu_brass_pebble", !1)) return !1;
+   if (j91()) return !0;
+   if (ak()) return !0;
+   let A = Uq();
+   if (A === "max" || A === "team") return $5()?.hasExtraUsageEnabled === !0;
+   if (A === null) return !0;
+   return !1;
+ }

+++ Added KO1 (pretty-v2.1.23.js:266192-266196)
+ function KO1(A) {
+   if (A === "compact") return "repl_main_thread";
+   for (let K of TzY) if (A.startsWith(K)) return A;
+   return null;
+ }

+++ Added c57 (pretty-v2.1.23.js:266197-266203)
+ function c57(A) {
+   return A.map((K) => {
+     if (!("cache_control" in K)) return K;
+     let { cache_control: q, ...Y } = K;
+     return Y;
+   });
+ }

+++ Added l57 (pretty-v2.1.23.js:266204-266207)
+ function l57(A) {
+   let K = Bun.hash(UA(A));
+   return typeof K === "bigint" ? Number(K & 0xffffffffn) : K;
+ }

+++ Added vzY (pretty-v2.1.23.js:266208-266212)
+ function vzY(A) {
+   let K = 0;
+   for (let q of A) K += q.text.length;
+   return K;
+ }

+++ Added i57 (pretty-v2.1.23.js:266213-266264)
+ function i57(A, K, q, Y) {
+   try {
+     let z = KO1(q);
+     if (!z) return;
+     let w = c57(A),
+       H = c57(K),
+       J = l57(w),
+       O = l57(H),
+       X = K.map((D) => ("name" in D ? D.name : "unknown")),
+       $ = vzY(A),
+       _ = CGA.get(z);
+     if (!_) {
+       CGA.set(z, {
+         systemHash: J,
+         toolsHash: O,
+         toolNames: X,
+         systemCharCount: $,
+         model: Y,
+         callCount: 1,
+         pendingChanges: null,
+         prevCacheReadTokens: null,
+         microcompacted: !1,
+       });
+       return;
+     }
+     _.callCount++;
+     let G = J !== _.systemHash,
+       Z = O !== _.toolsHash,
+       W = Y !== _.model;
+     if (G || Z || W) {
+       let D = new Set(_.toolNames),
+         j = new Set(X);
+       _.pendingChanges = {
+         systemPromptChanged: G,
+         toolSchemasChanged: Z,
+         modelChanged: W,
+         addedToolCount: X.filter((M) => !D.has(M)).length,
+         removedToolCount: _.toolNames.filter((M) => !j.has(M)).length,
+         systemCharDelta: $ - _.systemCharCount,
+         previousModel: _.model,
+         newModel: Y,
+       };
+     } else _.pendingChanges = null;
+     ((_.systemHash = J),
+       (_.toolsHash = O),
+       (_.toolNames = X),
+       (_.systemCharCount = $),
+       (_.model = Y));
+   } catch (z) {
+     KA(z instanceof Error ? z : Error(String(z)));
+   }
+ }

+++ Added n57 (pretty-v2.1.23.js:266265-266316)
+ function n57(A, K, q) {
+   try {
+     let Y = KO1(A);
+     if (!Y) return;
+     let z = CGA.get(Y);
+     if (!z) return;
+     let w = z.prevCacheReadTokens;
+     if (((z.prevCacheReadTokens = K), w === null)) return;
+     let H = z.pendingChanges;
+     if (K >= w * 0.95) {
+       ((z.pendingChanges = null), (z.microcompacted = !1));
+       return;
+     }
+     let J = [],
+       O = z.microcompacted;
+     if (O) (J.push("microcompact"), (z.microcompacted = !1));
+     if (H) {
+       if (H.modelChanged)
+         J.push(`model changed (${H.previousModel} → ${H.newModel})`);
+       if (H.systemPromptChanged) {
+         let _ = H.systemCharDelta,
+           G = _ === 0 ? "" : _ > 0 ? ` (+${_} chars)` : ` (${_} chars)`;
+         J.push(`system prompt changed${G}`);
+       }
+       if (H.toolSchemasChanged) {
+         let _ =
+           H.addedToolCount > 0 || H.removedToolCount > 0
+             ? ` (+${H.addedToolCount}/-${H.removedToolCount} tools)`
+             : " (tool prompt/schema changed, same tool set)";
+         J.push(`tools changed${_}`);
+       }
+     }
+     let $ = `[PROMPT CACHE BREAK] ${J.length > 0 ? J.join(", ") : "unknown cause"} [source=${A}, call #${z.callCount}, cache read: ${w} → ${K}, creation: ${q}]`;
+     (h($, { level: "warn" }),
+       n("tengu_prompt_cache_break", {
+         systemPromptChanged: H?.systemPromptChanged ?? !1,
+         toolSchemasChanged: H?.toolSchemasChanged ?? !1,
+         modelChanged: H?.modelChanged ?? !1,
+         microcompacted: O,
+         addedToolCount: H?.addedToolCount ?? 0,
+         removedToolCount: H?.removedToolCount ?? 0,
+         callNumber: z.callCount,
+         prevCacheReadTokens: w,
+         cacheReadTokens: K,
+         cacheCreationTokens: q,
+       }),
+       mr6($),
+       (z.pendingChanges = null));
+   } catch (Y) {
+     KA(Y instanceof Error ? Y : Error(String(Y)));
+   }
+ }

+++ Added r57 (pretty-v2.1.23.js:266317-266321)
+ function r57(A) {
+   let K = KO1(A),
+     q = K ? CGA.get(K) : void 0;
+   if (q) q.microcompacted = !0;
+ }

+++ Added o57 (pretty-v2.1.23.js:266322-266326)
+ function o57(A) {
+   let K = KO1(A),
+     q = K ? CGA.get(K) : void 0;
+   if (q) q.prevCacheReadTokens = null;
+ }

+++ Added a57 (pretty-v2.1.23.js:266327-266329)
+ function a57() {
+   CGA.clear();
+ }

+++ Added uxA (pretty-v2.1.23.js:266331-266345)
+ var uxA = k(() => {
+   Z1();
+   l1();
+   q6();
+   b1();
+   C1();
+   ((CGA = new Map()),
+     (TzY = [
+       "repl_main_thread",
+       "sdk",
+       "agent:custom",
+       "agent:default",
+       "agent:builtin",
+     ]));
+ });

+++ Added eLY (pretty-v2.1.23.js:308772-308777)
+ async function eLY(A) {
+   if (!xD7(A)) return !1;
+   if (!M$()) return !0;
+   if (process.ppid === A) return !0;
+   return (await Dy4(process.ppid, 10)).includes(A);
+ }

+++ Added zmA (pretty-v2.1.23.js:310845-310876)
+ var zmA = k(() => {
+   X0();
+   Z1();
+   C1();
+   X0();
+   maA();
+   wz();
+   oM6 = z6(async (A) => {
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
+ - If you see a <${hN}> tag in the current conversation turn, the skill has ALREADY been loaded - follow the instructions directly instead of calling this tool again
+ `;
+   });
+ });

+++ Added FP6 (pretty-v2.1.23.js:316373-316386)
+ function FP6(A, K, q) {
+   (A.stopProgressInterval(),
+     A.shellCommand?.cleanup(),
+     nI({
+       hookId: A.hookId,
+       hookName: A.hookName,
+       hookEvent: A.hookEvent,
+       output: A.output,
+       stdout: A.stdout,
+       stderr: A.stderr,
+       exitCode: K,
+       outcome: q,
+     }));
+ }

+++ Added QP6 (pretty-v2.1.23.js:316479-316490)
+ async function QP6() {
+   for (let A of oC.values())
+     if (A.shellCommand?.status === "completed") {
+       let K = await A.shellCommand.result;
+       FP6(A, K.code, K.code === 0 ? "success" : "error");
+     } else {
+       if (A.shellCommand && A.shellCommand.status !== "killed")
+         A.shellCommand.kill();
+       FP6(A, 1, "cancelled");
+     }
+   oC.clear();
+ }

+++ Added kmA (pretty-v2.1.23.js:319426-319436)
+ function kmA(A) {
+   let K = A.toLowerCase();
+   return ![
+     "3-5-haiku",
+     "haiku-4-5",
+     "3-5-sonnet",
+     "3-7-sonnet",
+     "sonnet-4",
+     "opus-4",
+   ].some((Y) => K.includes(Y));
+ }

+++ Added tf7 (pretty-v2.1.23.js:319440-319443)
+ function tf7(A) {
+   if (typeof A === "string") return A;
+   return "high";
+ }

+++ Added KP (pretty-v2.1.23.js:325190-325192)
+ function KP() {
+   return F1((A) => A.settings);
+ }

+++ Added ZI7 (pretty-v2.1.23.js:340807-340809)
+ function ZI7() {
+   for (let A of VT6) A();
+ }

+++ Added zW1 (pretty-v2.1.23.js:340813-340815)
+ function zW1(A) {
+   return;
+ }

+++ Added ToY (pretty-v2.1.23.js:340816-340818)
+ function ToY(A) {
+   return (VT6.add(A), () => VT6.delete(A));
+ }

+++ Added DI7 (pretty-v2.1.23.js:340819-340821)
+ function DI7(A) {
+   return XI7.useSyncExternalStore(ToY, () => NT6.has(A));
+ }

+++ Added wW1 (pretty-v2.1.23.js:340823-340825)
+ var wW1 = k(() => {
+   ((XI7 = o($A(), 1)), (fT6 = new Map()), (NT6 = new Set()), (VT6 = new Set()));
+ });

+++ Added Ct7 (pretty-v2.1.23.js:389111-389116)
+ function Ct7() {
+   let K = yq().spinnerVerbs;
+   if (!K) return WR6;
+   if (K.mode === "replace") return K.verbs.length > 0 ? K.verbs : WR6;
+   return [...WR6, ...K.verbs];
+ }

+++ Added dt7 (pretty-v2.1.23.js:390138-390361)
+ function dt7({
+   mode: A,
+   elapsedTimeMs: K,
+   spinnerTip: q,
+   currentResponseLength: Y,
+   overrideColor: z,
+   overrideShimmerColor: w,
+   overrideMessage: H,
+   spinnerSuffix: J,
+   verbose: O,
+   todos: X,
+   hasActiveTools: $ = !1,
+ }) {
+   let [_, G] = NW.useState(0),
+     [Z, W] = NW.useState(0),
+     D = F1((B1) => B1.tasks),
+     j = F1((B1) => B1.viewingAgentTaskId),
+     M = F1((B1) => B1.showExpandedTodos),
+     { isConnected: P } = GR6(),
+     { columns: f } = f8(),
+     N = NM1(),
+     [T, C] = NW.useState(null),
+     R = NW.useRef(null);
+   NW.useEffect(() => {
+     let B1 = null,
+       C6 = null;
+     if (A === "thinking") {
+       if (R.current === null) ((R.current = Date.now()), C("thinking"));
+     } else if (R.current !== null) {
+       let w1 = Date.now() - R.current,
+         $1 = Date.now() - R.current,
+         N1 = Math.max(0, 2000 - $1);
+       R.current = null;
+       let A6 = () => {
+         (C(w1), (C6 = setTimeout(() => C(null), 2000)));
+       };
+       if (N1 > 0) B1 = setTimeout(A6, N1);
+       else A6();
+     }
+     return () => {
+       if (B1) clearTimeout(B1);
+       if (C6) clearTimeout(C6);
+     };
+   }, [A]);
+   let x = ew()
+       ? N?.find((B1) => B1.status !== "pending" && B1.status !== "completed")
+       : X?.find((B1) => B1.status === "in_progress"),
+     y = ew() ? P_2(N) : X?.find((B1) => B1.status === "pending"),
+     [B] = NW.useState(() => rg(Ct7())),
+     b = (H ?? x?.activeForm ?? B) + "…",
+     { isStalled: F, stalledIntensity: Q } = ER6(Y, $),
+     u = LS(A, b, P, F),
+     d = vR6(A),
+     r = NW.useRef(Y);
+   (NW.useEffect(() => {
+     let B1 = "spinner-" + A;
+     return (
+       cFA.startCLIActivity(B1),
+       () => {
+         cFA.endCLIActivity(B1);
+       }
+     );
+   }, [A]),
+     NW.useEffect(() => {
+       r.current = Y;
+     }, [Y]),
+     s9(() => {
+       if (!P) {
+         G(4);
+         return;
+       }
+       G((B1) => B1 + 1);
+     }, 120),
+     s9(() => {
+       W((B1) => {
+         let C6 = r.current - B1;
+         if (C6 <= 0) return B1;
+         let w1;
+         if (C6 < 70) w1 = 1;
+         else if (C6 < 200) w1 = Math.max(2, Math.ceil(C6 * 0.08));
+         else w1 = 18;
+         return Math.min(B1 + w1, r.current);
+       });
+     }, 10));
+   let c = j7(b) + 2,
+     YA =
+       T === "thinking"
+         ? "thinking"
+         : typeof T === "number"
+           ? `thought for ${Math.max(1, Math.round(T / 1000))}s`
+           : null,
+     e = YA ? j7(YA) : 0,
+     qA = Math.round(Z / 4),
+     HA = 0,
+     _A = !1;
+   for (let B1 of Object.values(D))
+     if (W_(B1) && B1.status === "running") {
+       if (((_A = !0), B1.progress?.tokenCount)) HA += B1.progress.tokenCount;
+     }
+   let a = NW.useRef(Date.now() - K);
+   NW.useEffect(() => {
+     let B1 = Date.now() - K;
+     if (!_A || B1 < a.current) a.current = B1;
+   }, [K, _A]);
+   let [JA, jA] = NW.useState(K);
+   s9(() => jA(Date.now() - a.current), _A ? 100 : null);
+   let MA = NW.useRef(_A);
+   if (MA.current && !_A) ((a.current = Date.now() - K), jA(K));
+   MA.current = _A;
+   let hA = _A ? Math.max(K, JA) : K,
+     yA = $O(hA),
+     AA = j7(yA),
+     wA = qA + HA,
+     GA = g5(wA),
+     OA = _A ? `${GA} tokens` : `${eA.arrowDown} ${GA} tokens`,
+     t = j7(OA),
+     XA = j7(" · "),
+     VA = T !== null,
+     vA = O || _A || hA > D_2,
+     RA = f - c - 5,
+     fA = VA && RA > e,
+     LA = fA ? e + XA : 0,
+     SA = vA && RA > LA + AA,
+     xA = LA + (SA ? AA + XA : 0),
+     iA = vA && RA > xA + t,
+     lA = [
+       ...(J ? [P7.createElement(V, { dimColor: !0, key: "suffix" }, J)] : []),
+       ...(SA
+         ? [P7.createElement(V, { dimColor: !0, key: "elapsedTime" }, yA)]
+         : []),
+       ...(iA
+         ? [
+             P7.createElement(
+               S,
+               { flexDirection: "row", key: "tokens" },
+               !_A && P7.createElement(j_2, { mode: A }),
+               P7.createElement(V, { dimColor: !0 }, GA, " tokens"),
+             ),
+           ]
+         : []),
+       ...(fA && YA
+         ? [
+             T === "thinking"
+               ? P7.createElement(Ft7, { key: "thinking", text: YA })
+               : P7.createElement(V, { dimColor: !0, key: "thinking" }, YA),
+           ]
+         : []),
+     ];
+   if (P === !1)
+     lA.push(
+       P7.createElement(
+         S,
+         { key: "offline" },
+         P7.createElement(V, { color: "error", bold: !0 }, "offline"),
+       ),
+     );
+   let v1 = z ?? (P === !1 ? "inactive" : "claude"),
+     I1 = w ?? "claudeShimmer",
+     Q1 =
+       lA.length > 0
+         ? P7.createElement(
+             P7.Fragment,
+             null,
+             P7.createElement(V, { dimColor: !0 }, "("),
+             P7.createElement(Y8, null, lA),
+             P7.createElement(V, { dimColor: !0 }, ")"),
+           )
+         : null;
+   return P7.createElement(
+     S,
+     { flexDirection: "column", width: "100%", alignItems: "flex-start" },
+     P7.createElement(
+       S,
+       { flexDirection: "row", flexWrap: "wrap", marginTop: 1, width: "100%" },
+       P7.createElement(rFA, {
+         frame: _,
+         messageColor: v1,
+         stalledIntensity: z ? 0 : Q,
+         isConnected: P,
+       }),
+       P7.createElement(NR6, {
+         message: b,
+         mode: A,
+         isConnected: P,
+         messageColor: v1,
+         glimmerIndex: u,
+         flashOpacity: d,
+         shimmerColor: I1,
+         stalledIntensity: z ? 0 : Q,
+       }),
+       Q1,
+       j && P7.createElement(V, { dimColor: !0 }, " [leader]"),
+     ),
+     M && N && N.length > 0
+       ? P7.createElement(
+           S,
+           { width: "100%", flexDirection: "column" },
+           P7.createElement(k6, null, P7.createElement(VM1, { tasks: N })),
+         )
+       : M && X && X.length > 0
+         ? P7.createElement(
+             S,
+             { width: "100%", flexDirection: "column" },
+             P7.createElement(k6, null, P7.createElement(Nt, { todos: X })),
+           )
+         : y || q
+           ? P7.createElement(
+               S,
+               { width: "100%" },
+               P7.createElement(
+                 k6,
+                 null,
+                 P7.createElement(
+                   V,
+                   { dimColor: !0 },
+                   y
+                     ? `Next: ${"subject" in y ? y.subject : y.content}`
+                     : `Tip: ${q}`,
+                 ),
+               ),
+             )
+           : null,
+   );
+ }

+++ Added VQA (pretty-v2.1.23.js:407632-407676)
+ function VQA(A) {
+   let K = s(10),
+     { elapsedTimeSeconds: q, timeoutMs: Y } = A;
+   if (q === void 0 && !Y) return null;
+   let z;
+   if (K[0] !== Y)
+     ((z = Y ? $O(Y, { hideTrailingZeros: !0 }) : void 0),
+       (K[0] = Y),
+       (K[1] = z));
+   else z = K[1];
+   let w = z;
+   if (q === void 0) {
+     let _ = `(timeout ${w})`,
+       G;
+     if (K[2] !== _)
+       ((G = wP1.default.createElement(V, { dimColor: !0 }, _)),
+         (K[2] = _),
+         (K[3] = G));
+     else G = K[3];
+     return G;
+   }
+   let H = q * 1000,
+     J;
+   if (K[4] !== H) ((J = $O(H)), (K[4] = H), (K[5] = J));
+   else J = K[5];
+   let O = J;
+   if (w) {
+     let _ = `(${O} · timeout ${w})`,
+       G;
+     if (K[6] !== _)
+       ((G = wP1.default.createElement(V, { dimColor: !0 }, _)),
+         (K[6] = _),
+         (K[7] = G));
+     else G = K[7];
+     return G;
+   }
+   let X = `(${O})`,
+     $;
+   if (K[8] !== X)
+     (($ = wP1.default.createElement(V, { dimColor: !0 }, X)),
+       (K[8] = X),
+       (K[9] = $));
+   else $ = K[9];
+   return $;
+ }

+++ Added bS (pretty-v2.1.23.js:413183-413255)
+ async function bS({
+   promptMessages: A,
+   cacheSafeParams: K,
+   canUseTool: q,
+   querySource: Y,
+   forkLabel: z,
+   overrides: w,
+   maxOutputTokens: H,
+   maxTurns: J,
+   onMessage: O,
+ }) {
+   let X = Date.now(),
+     $ = [],
+     _ = { ...lf },
+     {
+       systemPrompt: G,
+       userContext: Z,
+       systemContext: W,
+       toolUseContext: D,
+       forkContextMessages: j,
+     } = K,
+     M = xQA(D, w),
+     P = [...ZI6(j), ...A],
+     f = HL(z);
+   await wMA(P, f).catch((C) =>
+     h(`Forked agent [${z}] failed to record initial transcript: ${C}`),
+   );
+   let N = P.length > 0 ? P[P.length - 1].uuid : null;
+   for await (let C of nf({
+     messages: P,
+     systemPrompt: G,
+     userContext: Z,
+     systemContext: W,
+     canUseTool: q,
+     toolUseContext: M,
+     querySource: Y,
+     maxOutputTokensOverride: H,
+     maxTurns: J,
+   })) {
+     if (C.type === "stream_event") {
+       if ("event" in C && C.event?.type === "message_delta" && C.event.usage) {
+         let x = g3A({ ...lf }, C.event.usage);
+         _ = LP1(_, x);
+       }
+       continue;
+     }
+     if (C.type === "stream_request_start") continue;
+     (h(`Forked agent [${z}] received message: type=${C.type}`),
+       $.push(C),
+       O?.(C));
+     let R = C;
+     if (R.type === "assistant" || R.type === "user" || R.type === "progress")
+       (await wMA([R], f, N).catch((x) =>
+         h(`Forked agent [${z}] failed to record transcript: ${x}`),
+       ),
+         (N = R.uuid));
+   }
+   h(
+     `Forked agent [${z}] finished: ${$.length} messages, types=[${$.map((C) => C.type).join(", ")}], totalUsage: input=${_.input_tokens} output=${_.output_tokens} cacheRead=${_.cache_read_input_tokens} cacheCreate=${_.cache_creation_input_tokens}`,
+   );
+   let T = Date.now() - X;
+   return (
+     jj2({
+       forkLabel: z,
+       querySource: Y,
+       durationMs: T,
+       messageCount: $.length,
+       totalUsage: _,
+       queryTracking: D.queryTracking,
+     }),
+     { messages: $, totalUsage: _ }
+   );
+ }

+++ Added xP1 (pretty-v2.1.23.js:414424-414466)
+ function xP1(A) {
+   let K = s(9),
+     q;
+   if (K[0] !== A) ((q = A === void 0 ? {} : A), (K[0] = A), (K[1] = q));
+   else q = K[1];
+   let { onBackground: Y } = q,
+     z = D0(),
+     w = p4(),
+     H;
+   if (K[2] !== Y || K[3] !== w || K[4] !== z)
+     ((H = () => {
+       (y_1(() => z.getState(), w), Y?.());
+     }),
+       (K[2] = Y),
+       (K[3] = w),
+       (K[4] = z),
+       (K[5] = H));
+   else H = K[5];
+   let J = H,
+     O;
+   if (K[6] === Symbol.for("react.memo_cache_sentinel"))
+     ((O = { context: "Task" }), (K[6] = O));
+   else O = K[6];
+   J6("task:background", J, O);
+   let X = cK("task:background", "Task", "ctrl+b"),
+     $ = m6.terminal === "tmux" && X === "ctrl+b" ? "ctrl+b ctrl+b (twice)" : X;
+   if (P1(process.env.CLAUDE_CODE_DISABLE_BACKGROUND_TASKS)) return null;
+   let _;
+   if (K[7] !== $)
+     ((_ = oH.createElement(
+       S,
+       { paddingLeft: 5 },
+       oH.createElement(
+         V,
+         { dimColor: !0 },
+         oH.createElement(M6, { shortcut: $, action: "run in background" }),
+       ),
+     )),
+       (K[7] = $),
+       (K[8] = _));
+   else _ = K[8];
+   return _;
+ }

+++ Added i7K (pretty-v2.1.23.js:414529-414532)
+ function i7K(A, K, { verbose: q, theme: Y, tools: z, style: w }) {
+   let J = K.at(-1)?.data?.timeoutMs;
+   return oH.createElement(v3A, { content: A, verbose: q, timeoutMs: J });
+ }

+++ Added qV1 (pretty-v2.1.23.js:420756-420764)
+ async function qV1(A) {
+   try {
+     return (
+       await A8.get(`${pM2}/${A}`, { timeout: 5000, responseType: "text" })
+     ).data.trim();
+   } catch (K) {
+     return (h(`Failed to fetch ${A} from GCS: ${K}`), null);
+   }
+ }

+++ Added FqK (pretty-v2.1.23.js:424186-424192)
+ function FqK() {
+   if (kMA)
+     ((lt = kMA), h(`[TeammateModeSnapshot] Captured from CLI override: ${lt}`));
+   else
+     ((lt = M1().teammateMode ?? "auto"),
+       h(`[TeammateModeSnapshot] Captured from config: ${lt}`));
+ }

+++ Added bzK (pretty-v2.1.23.js:447440-447593)
+ var bzK = k(() => {
+   ((eE2 = `Use this tool proactively when you're about to start a non-trivial implementation task. Getting user sign-off on your approach before writing code prevents wasted effort and ensures alignment. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
+    - If you would use ${bJ} to clarify the approach, use EnterPlanMode instead
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
+ 5. Use ${bJ} if you need to clarify approaches
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
+     (P6J = `Use this tool when a task has genuine ambiguity about the right approach and getting user input before coding would prevent significant rework. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
+ When in doubt, prefer starting work and using ${bJ} for specific questions over entering a full planning phase.
+ 
+ ## What Happens in Plan Mode
+ 
+ In plan mode, you'll:
+ 1. Explore the codebase using Glob, Grep, and Read tools
+ 2. Understand existing patterns and architecture
+ 3. Design an implementation approach
+ 4. Present your plan to the user for approval
+ 5. Use ${bJ} if you need to clarify approaches
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

+++ Added kV1 (pretty-v2.1.23.js:449461-449469)
+ function kV1(A, K) {
+   let q = I$(A);
+   if (sH()) return q;
+   let Y = Lf1(K, A),
+     z = Jb([...q, ...Y], "name");
+   if (A.mode === "coordinator") return z.filter((w) => oZ1.has(w.name));
+   if (A.mode === "delegate") return z.filter((w) => rZ1.has(w.name));
+   return z;
+ }

+++ Added f_ (pretty-v2.1.23.js:449492-449532)
+ var f_ = k(() => {
+   dZ1();
+   SV1();
+   xG();
+   M5A();
+   Ev();
+   V5A();
+   GUA();
+   WUA();
+   rMA();
+   Bb6();
+   Fb6();
+   Ub6();
+   XXA();
+   mUA();
+   YzK();
+   IMA();
+   Tf1();
+   SzK();
+   h$1();
+   b$1();
+   o_6();
+   rb6();
+   czK();
+   AwK();
+   XwK();
+   PwK();
+   RwK();
+   owA();
+   IG();
+   vC();
+   VJ();
+   kp();
+   aZ1();
+   aZ1();
+   S2();
+   l6();
+   t9();
+   AP6();
+   Ck2 = ["default"];
+ });

+++ Added qx6 (pretty-v2.1.23.js:449578-449660)
+ function qx6(A, K) {
+   let q =
+     c7() === "firstParty" &&
+     (P1(process.env.CLAUDE_CODE_FORCE_GLOBAL_CACHE) ||
+       G4("tengu_system_prompt_global_cache", !1));
+   if (q && K?.skipGlobalCacheForSystemPrompt) {
+     n("tengu_sysprompt_using_tool_based_cache", { promptBlockCount: A.length });
+     let O,
+       X,
+       $ = [];
+     for (let Z of A) {
+       if (!Z) continue;
+       if (Z === UUA) continue;
+       if (Z.startsWith("x-anthropic-billing-header")) O = Z;
+       else if (gq1.has(Z)) X = Z;
+       else $.push(Z);
+     }
+     let _ = [];
+     if (O) _.push({ text: O, cacheScope: null });
+     if (X) _.push({ text: X, cacheScope: null });
+     let G = $.join(`
+ 
+ `);
+     if (G) _.push({ text: G, cacheScope: null });
+     return _;
+   }
+   if (q) {
+     let O = A.findIndex((X) => X === UUA);
+     if (O !== -1) {
+       let X,
+         $,
+         _ = [],
+         G = [];
+       for (let j = 0; j < A.length; j++) {
+         let M = A[j];
+         if (!M || M === UUA) continue;
+         if (M.startsWith("x-anthropic-billing-header")) X = M;
+         else if (gq1.has(M)) $ = M;
+         else if (j < O) _.push(M);
+         else G.push(M);
+       }
+       let Z = [];
+       if (X) Z.push({ text: X, cacheScope: null });
+       if ($) Z.push({ text: $, cacheScope: null });
+       let W = _.join(`
+ 
+ `);
+       if (W) Z.push({ text: W, cacheScope: "global" });
+       let D = G.join(`
+ 
+ `);
+       if (D) Z.push({ text: D, cacheScope: null });
+       return (
+         n("tengu_sysprompt_boundary_found", {
+           blockCount: Z.length,
+           staticBlockLength: W.length,
+           dynamicBlockLength: D.length,
+         }),
+         Z
+       );
+     } else
+       n("tengu_sysprompt_missing_boundary_marker", {
+         promptBlockCount: A.length,
+       });
+   }
+   let Y,
+     z,
+     w = [];
+   for (let O of A) {
+     if (!O) continue;
+     if (O.startsWith("x-anthropic-billing-header")) Y = O;
+     else if (gq1.has(O)) z = O;
+     else w.push(O);
+   }
+   let H = [];
+   if (Y) H.push({ text: Y, cacheScope: null });
+   if (z) H.push({ text: z, cacheScope: "org" });
+   let J = w.join(`
+ 
+ `);
+   if (J) H.push({ text: J, cacheScope: "org" });
+   return H;
+ }

+++ Added WC2 (pretty-v2.1.23.js:453366-453377)
+ function WC2(A) {
+   if (!A) return;
+   switch (A.type) {
+     case "bash":
+       return "Bash";
+     case "edit":
+     case "denied_tool":
+       return A.toolName;
+     case "complete":
+       return;
+   }
+ }

+++ Added DC2 (pretty-v2.1.23.js:453378-453390)
+ function DC2(A) {
+   if (!A) return;
+   switch (A.type) {
+     case "bash":
+       return A.command.slice(0, 200);
+     case "edit":
+       return A.filePath;
+     case "denied_tool":
+       return A.detail;
+     case "complete":
+       return;
+   }
+ }

+++ Added PC2 (pretty-v2.1.23.js:453445-453470)
+ async function PC2(A, K, q, Y, z) {
+   try {
+     let w = await A.toolUseContext.getAppState(),
+       H = hx6(w);
+     if (H) {
+       rS(`pipeline_${H}`);
+       return;
+     }
+     let J = { ...A, messages: [...A.messages, t1({ content: K }), ...q] },
+       O = L1A(z);
+     if (O.signal.aborted) return;
+     let X = if1(),
+       { suggestion: $, generationRequestId: _ } = await bx6(J, O, X);
+     if (O.signal.aborted) return;
+     if (xx6($, X)) return;
+     (h(`[Speculation] Pipelined suggestion: "${$.slice(0, 50)}..."`),
+       YPA(Y, () => ({
+         pipelinedSuggestion: { text: $, promptId: X, generationRequestId: _ },
+       })));
+   } catch (w) {
+     if (w instanceof Error && w.name === "AbortError") return;
+     h(
+       `[Speculation] Pipelined suggestion failed: ${w instanceof Error ? w.message : String(w)}`,
+     );
+   }
+ }

+++ Added hx6 (pretty-v2.1.23.js:453922-453930)
+ function hx6(A) {
+   if (!A.promptSuggestionEnabled) return "disabled";
+   if (A.pendingWorkerRequest || A.pendingSandboxRequest)
+     return "pending_permission";
+   if (A.elicitation.queue.length > 0) return "elicitation_active";
+   if (A.toolPermissionContext.mode === "plan") return "plan_mode";
+   if (zf.status !== "allowed") return "rate_limit";
+   return null;
+ }

+++ Added He (pretty-v2.1.23.js:458582-458584)
+ function He() {
+   JpA.clear();
+ }

+++ Added RL2 (pretty-v2.1.23.js:458585-458604)
+ async function RL2(A) {
+   let K = sW(),
+     Y = (await lC(K)).filter((H) => !JpA.has(H.name));
+   if (Y.length === 0) return [];
+   let z = JpA.size === 0;
+   for (let H of Y) JpA.add(H.name);
+   return (
+     h(
+       `Sending ${Y.length} skills via attachment (${z ? "initial" : "dynamic"}, ${JpA.size} total sent)`,
+     ),
+     [
+       {
+         type: "skill_listing",
+         content: Wj7(Y),
+         skillCount: Y.length,
+         isInitial: z,
+       },
+     ]
+   );
+ }

+++ Added CS2 (pretty-v2.1.23.js:468677-468702)
+ function CS2(A) {
+   if (A.length === 0) return A;
+   let K = !1,
+     q = A.map((Y, z) => {
+       if (Y.type !== "assistant") return Y;
+       if (z === A.length - 1) return Y;
+       let w = Y.message.content;
+       if (Array.isArray(w) && w.length === 0)
+         return (
+           (K = !0),
+           n("tengu_fixed_empty_assistant_content", {
+             messageUUID: Y.uuid,
+             messageIndex: z,
+           }),
+           {
+             ...Y,
+             message: {
+               ...Y.message,
+               content: [{ type: "text", text: wf, citations: [] }],
+             },
+           }
+         );
+       return Y;
+     });
+   return K ? q : A;
+ }

+++ Added AT1 (pretty-v2.1.23.js:470626-470642)
+ function AT1(A, K) {
+   let q = A,
+     Y = new Set();
+   return {
+     getState: () => q,
+     setState: (z) => {
+       let w = q,
+         H = z(w);
+       if (Object.is(H, w)) return;
+       ((q = H), K?.({ newState: H, oldState: w }));
+       for (let J of Y) J();
+     },
+     subscribe: (z) => {
+       return (Y.add(z), () => Y.delete(z));
+     },
+   };
+ }

+++ Added $Y (pretty-v2.1.23.js:470705-470767)
+ function $Y(A) {
+   let K = s(13),
+     { children: q, initialState: Y, onChangeAppState: z } = A;
+   if (E_.useContext(vXK))
+     throw Error(
+       "AppStateProvider can not be nested within another AppStateProvider",
+     );
+   let H;
+   if (K[0] !== Y || K[1] !== z)
+     ((H = () => AT1(Y ?? RPA(), z)), (K[0] = Y), (K[1] = z), (K[2] = H));
+   else H = K[2];
+   let [J] = E_.useState(H),
+     O;
+   if (K[3] !== J)
+     ((O = () => {
+       let { toolPermissionContext: W } = J.getState();
+       if (W.isBypassPermissionsModeAvailable && bpA())
+         (h(
+           "Disabling bypass permissions mode on mount (remote settings loaded before mount)",
+         ),
+           J.setState(sS2));
+     }),
+       (K[3] = J),
+       (K[4] = O));
+   else O = K[4];
+   let X;
+   if (K[5] === Symbol.for("react.memo_cache_sentinel")) ((X = []), (K[5] = X));
+   else X = K[5];
+   E_.useEffect(O, X);
+   let $;
+   if (K[6] !== J)
+     (($ = (W, D) => {
+       h(`Settings changed from ${W}, updating AppState`);
+       let j = JA1();
+       (oqA(),
+         J.setState((M) => {
+           let P = EXK(M.toolPermissionContext, j);
+           if (P.isBypassPermissionsModeAvailable && bpA()) P = xpA(P);
+           return { ...M, settings: D, toolPermissionContext: P };
+         }));
+     }),
+       (K[6] = J),
+       (K[7] = $));
+   else $ = K[7];
+   let _ = E_.useEffectEvent($);
+   lXA(_);
+   let G;
+   if (K[8] !== q)
+     ((G = E_.default.createElement(NXK, null, q)), (K[8] = q), (K[9] = G));
+   else G = K[9];
+   let Z;
+   if (K[10] !== J || K[11] !== G)
+     ((Z = E_.default.createElement(
+       vXK.Provider,
+       { value: !0 },
+       E_.default.createElement(kB6.Provider, { value: J }, G),
+     )),
+       (K[10] = J),
+       (K[11] = G),
+       (K[12] = Z));
+   else Z = K[12];
+   return Z;
+ }

+++ Added sS2 (pretty-v2.1.23.js:470768-470770)
+ function sS2(A) {
+   return { ...A, toolPermissionContext: xpA(A.toolPermissionContext) };
+ }

+++ Added F1 (pretty-v2.1.23.js:470779-470799)
+ function F1(A) {
+   let K = s(3),
+     q = CB6(),
+     Y;
+   if (K[0] !== A || K[1] !== q)
+     ((Y = () => {
+       let w = q.getState(),
+         H = A(w);
+       if (w === H)
+         throw Error(
+           `Your selector in \`useAppState(${A.toString()})\` returned the original state, which is not allowed. You must instead return a property for optimised rendering.`,
+         );
+       return H;
+     }),
+       (K[0] = A),
+       (K[1] = q),
+       (K[2] = Y));
+   else Y = K[2];
+   let z = Y;
+   return E_.useSyncExternalStore(q.subscribe, z, z);
+ }

+++ Added p4 (pretty-v2.1.23.js:470800-470802)
+ function p4() {
+   return CB6().setState;
+ }

+++ Added LI7 (pretty-v2.1.23.js:470806-470817)
+ function LI7(A) {
+   let K = s(3),
+     q = E_.useContext(kB6),
+     Y;
+   if (K[0] !== A || K[1] !== q)
+     ((Y = () => (q ? A(q.getState()) : void 0)),
+       (K[0] = A),
+       (K[1] = q),
+       (K[2] = Y));
+   else Y = K[2];
+   return E_.useSyncExternalStore(q ? q.subscribe : tS2, Y);
+ }

+++ Added tS2 (pretty-v2.1.23.js:470822-470822)
+   tS2 = () => () => {};

+++ Added g_K (pretty-v2.1.23.js:478670-478674)
+ function g_K(A) {
+   if (!A) return !1;
+   if (A === gT1) return kmA(Rk());
+   return kmA(cz(A));
+ }

+++ Added F_K (pretty-v2.1.23.js:478680-478706)
+ function F_K(A) {
+   let K = s(3),
+     { effort: q } = A,
+     Y;
+   if (K[0] === Symbol.for("react.memo_cache_sentinel"))
+     ((Y = ["low", "medium", "high", "max"]), (K[0] = Y));
+   else Y = K[0];
+   let z = Y,
+     w = q ? z.indexOf(q) + 1 : 0,
+     H;
+   if (K[1] !== w)
+     ((H = EK.createElement(
+       EK.Fragment,
+       null,
+       z.map((J, O) =>
+         EK.createElement(
+           V,
+           { key: O, color: O < w ? "claude" : "subtle" },
+           "▌",
+         ),
+       ),
+     )),
+       (K[1] = w),
+       (K[2] = H));
+   else H = K[2];
+   return H;
+ }

+++ Added aT1 (pretty-v2.1.23.js:483345-483932)
+ function aT1(A) {
+   let K = s(87),
+     { onDone: q } = A,
+     Y = F1(LB2),
+     z = F1(CB2),
+     w = F1(kB2),
+     H = F1(EB2);
+   n8();
+   let J;
+   if (K[0] !== z) ((J = z || []), (K[0] = z), (K[1] = J));
+   else J = K[1];
+   let O = J,
+     [X, $] = m9A.useState(null),
+     [_, G] = m9A.useState(null),
+     [Z, W] = m9A.useState(null),
+     [D, j] = m9A.useState(null),
+     M = iT1(),
+     P;
+   if (K[2] === Symbol.for("react.memo_cache_sentinel"))
+     ((P = dt().then(TB2)), (K[2] = P));
+   else P = K[2];
+   let f = P,
+     N = yq()?.autoUpdatesChannel ?? "latest",
+     T;
+   if (K[3] !== M) ((T = M.filter(NB2)), (K[3] = M), (K[4] = T));
+   else T = K[4];
+   let C = T,
+     R;
+   if (K[5] === Symbol.for("react.memo_cache_sentinel"))
+     ((R = CGK()), (K[5] = R));
+   else R = K[5];
+   let x = R,
+     y,
+     B;
+   if (K[6] !== Y || K[7] !== w || K[8] !== O)
+     ((y = () => {
+       (dt().then($),
+         (async () => {
+           let B1 = BA(),
+             C6 = um6(w8(), "agents"),
+             w1 = um6(V8(), ".claude", "agents"),
+             { activeAgents: $1, allAgents: N1, failedFiles: A6 } = Y,
+             c1 = {
+               activeAgents: $1.map(fB2),
+               userAgentsDir: C6,
+               projectAgentsDir: w1,
+               userDirExists: B1.existsSync(C6),
+               projectDirExists: B1.existsSync(w1),
+               failedFiles: A6,
+             };
+           G(c1);
+           let w6 = await RGK(
+             O,
+             { activeAgents: $1, allAgents: N1, failedFiles: A6 },
+             async () => w,
+           );
+           if ((W(w6), h9A())) {
+             let DA = um6(kT1(), "claude", "locks"),
+               EA = yT1(DA),
+               rA = Zm6(DA);
+             j({ enabled: !0, locks: rA, locksDir: DA, staleLocksCleaned: EA });
+           } else
+             j({ enabled: !1, locks: [], locksDir: "", staleLocksCleaned: 0 });
+         })());
+     }),
+       (B = [w, O, Y]),
+       (K[6] = Y),
+       (K[7] = w),
+       (K[8] = O),
+       (K[9] = y),
+       (K[10] = B));
+   else ((y = K[9]), (B = K[10]));
+   m9A.useEffect(y, B);
+   let b;
+   if (K[11] !== q)
+     ((b = () => {
+       q("Claude Code diagnostics dismissed", { display: "system" });
+     }),
+       (K[11] = q),
+       (K[12] = b));
+   else b = K[12];
+   let F = b,
+     Q;
+   if (K[13] !== F)
+     ((Q = { "confirm:yes": F, "confirm:no": F }), (K[13] = F), (K[14] = Q));
+   else Q = K[14];
+   let u;
+   if (K[15] === Symbol.for("react.memo_cache_sentinel"))
+     ((u = { context: "Confirmation" }), (K[15] = u));
+   else u = K[15];
+   if ((s4(Q, u), !X)) {
+     let B1;
+     if (K[16] === Symbol.for("react.memo_cache_sentinel"))
+       ((B1 = l8.default.createElement(
+         S,
+         { paddingX: 1, paddingTop: 1 },
+         l8.default.createElement(
+           V,
+           { dimColor: !0 },
+           "Checking installation status…",
+         ),
+       )),
+         (K[16] = B1));
+     else B1 = K[16];
+     return B1;
+   }
+   let d;
+   if (K[17] === Symbol.for("react.memo_cache_sentinel"))
+     ((d = l8.default.createElement(V, { bold: !0 }, "Diagnostics")),
+       (K[17] = d));
+   else d = K[17];
+   let r;
+   if (K[18] !== X.installationType || K[19] !== X.version)
+     ((r = l8.default.createElement(
+       V,
+       null,
+       "└ Currently running: ",
+       X.installationType,
+       " (",
+       X.version,
+       ")",
+     )),
+       (K[18] = X.installationType),
+       (K[19] = X.version),
+       (K[20] = r));
+   else r = K[20];
+   let c;
+   if (K[21] !== X.packageManager)
+     ((c =
+       X.packageManager &&
+       l8.default.createElement(
+         V,
+         null,
+         "└ Package manager: ",
+         X.packageManager,
+       )),
+       (K[21] = X.packageManager),
+       (K[22] = c));
+   else c = K[22];
+   let YA;
+   if (K[23] !== X.installationPath)
+     ((YA = l8.default.createElement(V, null, "└ Path: ", X.installationPath)),
+       (K[23] = X.installationPath),
+       (K[24] = YA));
+   else YA = K[24];
+   let e;
+   if (K[25] !== X.invokedBinary)
+     ((e = l8.default.createElement(V, null, "└ Invoked: ", X.invokedBinary)),
+       (K[25] = X.invokedBinary),
+       (K[26] = e));
+   else e = K[26];
+   let qA;
+   if (K[27] !== X.configInstallMethod)
+     ((qA = l8.default.createElement(
+       V,
+       null,
+       "└ Config install method: ",
+       X.configInstallMethod,
+     )),
+       (K[27] = X.configInstallMethod),
+       (K[28] = qA));
+   else qA = K[28];
+   let HA = X.ripgrepStatus.working ? "OK" : "Not working",
+     _A;
+   if (K[29] !== X.ripgrepStatus.mode || K[30] !== X.ripgrepStatus.systemPath)
+     ((_A =
+       X.ripgrepStatus.mode === "builtin"
+         ? n9()
+           ? "bundled"
+           : "vendor"
+         : X.ripgrepStatus.systemPath || "system"),
+       (K[29] = X.ripgrepStatus.mode),
+       (K[30] = X.ripgrepStatus.systemPath),
+       (K[31] = _A));
+   else _A = K[31];
+   let a;
+   if (K[32] !== HA || K[33] !== _A)
+     ((a = l8.default.createElement(V, null, "└ Search: ", HA, " (", _A, ")")),
+       (K[32] = HA),
+       (K[33] = _A),
+       (K[34] = a));
+   else a = K[34];
+   let JA;
+   if (K[35] !== X.recommendation)
+     ((JA =
+       X.recommendation &&
+       l8.default.createElement(
+         l8.default.Fragment,
+         null,
+         l8.default.createElement(V, null),
+         l8.default.createElement(
+           V,
+           { color: "warning" },
+           "Recommendation: ",
+           X.recommendation.split(`
+ `)[0],
+         ),
+         l8.default.createElement(
+           V,
+           { dimColor: !0 },
+           X.recommendation.split(`
+ `)[1],
+         ),
+       )),
+       (K[35] = X.recommendation),
+       (K[36] = JA));
+   else JA = K[36];
+   let jA;
+   if (K[37] !== X.multipleInstallations)
+     ((jA =
+       X.multipleInstallations.length > 1 &&
+       l8.default.createElement(
+         l8.default.Fragment,
+         null,
+         l8.default.createElement(V, null),
+         l8.default.createElement(
+           V,
+           { color: "warning" },
+           "Warning: Multiple installations found",
+         ),
+         X.multipleInstallations.map(VB2),
+       )),
+       (K[37] = X.multipleInstallations),
+       (K[38] = jA));
+   else jA = K[38];
+   let MA;
+   if (K[39] !== X.warnings)
+     ((MA =
+       X.warnings.length > 0 &&
+       l8.default.createElement(
+         l8.default.Fragment,
+         null,
+         l8.default.createElement(V, null),
+         X.warnings.map(PB2),
+       )),
+       (K[39] = X.warnings),
+       (K[40] = MA));
+   else MA = K[40];
+   let hA;
+   if (K[41] !== C)
+     ((hA =
+       C.length > 0 &&
+       l8.default.createElement(
+         S,
+         { flexDirection: "column", marginTop: 1, marginBottom: 1 },
+         l8.default.createElement(V, { bold: !0 }, "Invalid Settings"),
+         l8.default.createElement(nT1, { errors: C }),
+       )),
+       (K[41] = C),
+       (K[42] = hA));
+   else hA = K[42];
+   let yA;
+   if (
+     K[43] !== r ||
+     K[44] !== c ||
+     K[45] !== YA ||
+     K[46] !== e ||
+     K[47] !== qA ||
+     K[48] !== a ||
+     K[49] !== JA ||
+     K[50] !== jA ||
+     K[51] !== MA ||
+     K[52] !== hA
+   )
+     ((yA = l8.default.createElement(
+       S,
+       { flexDirection: "column" },
+       d,
+       r,
+       c,
+       YA,
+       e,
+       qA,
+       a,
+       JA,
+       jA,
+       MA,
+       hA,
+     )),
+       (K[43] = r),
+       (K[44] = c),
+       (K[45] = YA),
+       (K[46] = e),
+       (K[47] = qA),
+       (K[48] = a),
+       (K[49] = JA),
+       (K[50] = jA),
+       (K[51] = MA),
+       (K[52] = hA),
+       (K[53] = yA));
+   else yA = K[53];
+   let AA;
+   if (K[54] === Symbol.for("react.memo_cache_sentinel"))
+     ((AA = l8.default.createElement(V, { bold: !0 }, "Updates")), (K[54] = AA));
+   else AA = K[54];
+   let wA = X.packageManager ? "Managed by package manager" : X.autoUpdates,
+     GA;
+   if (K[55] !== wA)
+     ((GA = l8.default.createElement(V, null, "└ Auto-updates:", " ", wA)),
+       (K[55] = wA),
+       (K[56] = GA));
+   else GA = K[56];
+   let OA;
+   if (K[57] !== X.hasUpdatePermissions)
+     ((OA =
+       X.hasUpdatePermissions !== null &&
+       l8.default.createElement(
+         V,
+         null,
+         "└ Update permissions:",
+         " ",
+         X.hasUpdatePermissions ? "Yes" : "No (requires sudo)",
+       )),
+       (K[57] = X.hasUpdatePermissions),
+       (K[58] = OA));
+   else OA = K[58];
+   let t;
+   if (K[59] === Symbol.for("react.memo_cache_sentinel"))
+     ((t = l8.default.createElement(V, null, "└ Auto-update channel: ", N)),
+       (K[59] = t));
+   else t = K[59];
+   let XA;
+   if (K[60] === Symbol.for("react.memo_cache_sentinel"))
+     ((XA = l8.default.createElement(
+       l8.Suspense,
+       { fallback: null },
+       l8.default.createElement(XB2, { promise: f }),
+     )),
+       (K[60] = XA));
+   else XA = K[60];
+   let VA;
+   if (K[61] !== GA || K[62] !== OA)
+     ((VA = l8.default.createElement(
+       S,
+       { flexDirection: "column" },
+       AA,
+       GA,
+       OA,
+       t,
+       XA,
+     )),
+       (K[61] = GA),
+       (K[62] = OA),
+       (K[63] = VA));
+   else VA = K[63];
+   let vA, RA, fA, LA;
+   if (K[64] === Symbol.for("react.memo_cache_sentinel"))
+     ((vA = l8.default.createElement(IGK, null)),
+       (RA = l8.default.createElement(oT1, null)),
+       (fA = l8.default.createElement(EGK, null)),
+       (LA =
+         x.length > 0 &&
+         l8.default.createElement(
+           S,
+           { flexDirection: "column" },
+           l8.default.createElement(V, { bold: !0 }, "Environment Variables"),
+           x.map(MB2),
+         )),
+       (K[64] = vA),
+       (K[65] = RA),
+       (K[66] = fA),
+       (K[67] = LA));
+   else ((vA = K[64]), (RA = K[65]), (fA = K[66]), (LA = K[67]));
+   let SA;
+   if (K[68] !== D)
+     ((SA =
+       D?.enabled &&
+       l8.default.createElement(
+         S,
+         { flexDirection: "column" },
+         l8.default.createElement(V, { bold: !0 }, "Version Locks"),
+         D.staleLocksCleaned > 0 &&
+           l8.default.createElement(
+             V,
+             { dimColor: !0 },
+             "└ Cleaned ",
+             D.staleLocksCleaned,
+             " stale lock(s)",
+           ),
+         D.locks.length === 0
+           ? l8.default.createElement(
+               V,
+               { dimColor: !0 },
+               "└ No active version locks",
+             )
+           : D.locks.map(jB2),
+       )),
+       (K[68] = D),
+       (K[69] = SA));
+   else SA = K[69];
+   let xA;
+   if (K[70] !== _)
+     ((xA =
+       _?.failedFiles &&
+       _.failedFiles.length > 0 &&
+       l8.default.createElement(
+         S,
+         { flexDirection: "column" },
+         l8.default.createElement(
+           V,
+           { bold: !0, color: "error" },
+           "Agent Parse Errors",
+         ),
+         l8.default.createElement(
+           V,
+           { color: "error" },
+           "└ Failed to parse ",
+           _.failedFiles.length,
+           " agent file(s):",
+         ),
+         _.failedFiles.map(DB2),
+       )),
+       (K[70] = _),
+       (K[71] = xA));
+   else xA = K[71];
+   let iA;
+   if (K[72] !== H)
+     ((iA =
+       H.length > 0 &&
+       l8.default.createElement(
+         S,
+         { flexDirection: "column" },
+         l8.default.createElement(
+           V,
+           { bold: !0, color: "error" },
+           "Plugin Errors",
+         ),
+         l8.default.createElement(
+           V,
+           { color: "error" },
+           "└ ",
+           H.length,
+           " plugin error(s) detected:",
+         ),
+         H.map(WB2),
+       )),
+       (K[72] = H),
+       (K[73] = iA));
+   else iA = K[73];
+   let lA;
+   if (K[74] !== Z)
+     ((lA =
+       Z?.unreachableRulesWarning &&
+       l8.default.createElement(
+         S,
+         { flexDirection: "column" },
+         l8.default.createElement(
+           V,
+           { bold: !0, color: "warning" },
+           "Unreachable Permission Rules",
+         ),
+         l8.default.createElement(
+           V,
+           null,
+           "└",
+           " ",
+           l8.default.createElement(
+             V,
+             { color: "warning" },
+             eA.warning,
+             " ",
+             Z.unreachableRulesWarning.message,
+           ),
+         ),
+         Z.unreachableRulesWarning.details.map(ZB2),
+       )),
+       (K[74] = Z),
+       (K[75] = lA));
+   else lA = K[75];
+   let v1;
+   if (K[76] !== Z)
+     ((v1 =
+       Z &&
+       (Z.claudeMdWarning || Z.agentWarning || Z.mcpWarning) &&
+       l8.default.createElement(
+         S,
+         { flexDirection: "column" },
+         l8.default.createElement(V, { bold: !0 }, "Context Usage Warnings"),
+         Z.claudeMdWarning &&
+           l8.default.createElement(
+             l8.default.Fragment,
+             null,
+             l8.default.createElement(
+               V,
+               null,
+               "└",
+               " ",
+               l8.default.createElement(
+                 V,
+                 { color: "warning" },
+                 eA.warning,
+                 " ",
+                 Z.claudeMdWarning.message,
+               ),
+             ),
+             l8.default.createElement(V, null, "  ", "└ Files:"),
+             Z.claudeMdWarning.details.map(GB2),
+           ),
+         Z.agentWarning &&
+           l8.default.createElement(
+             l8.default.Fragment,
+             null,
+             l8.default.createElement(
+               V,
+               null,
+               "└",
+               " ",
+               l8.default.createElement(
+                 V,
+                 { color: "warning" },
+                 eA.warning,
+                 " ",
+                 Z.agentWarning.message,
+               ),
+             ),
+             l8.default.createElement(V, null, "  ", "└ Top contributors:"),
+             Z.agentWarning.details.map(_B2),
+           ),
+         Z.mcpWarning &&
+           l8.default.createElement(
+             l8.default.Fragment,
+             null,
+             l8.default.createElement(
+               V,
+               null,
+               "└",
+               " ",
+               l8.default.createElement(
+                 V,
+                 { color: "warning" },
+                 eA.warning,
+                 " ",
+                 Z.mcpWarning.message,
+               ),
+             ),
+             l8.default.createElement(V, null, "  ", "└ MCP servers:"),
+             Z.mcpWarning.details.map($B2),
+           ),
+       )),
+       (K[76] = Z),
+       (K[77] = v1));
+   else v1 = K[77];
+   let I1;
+   if (K[78] === Symbol.for("react.memo_cache_sentinel"))
+     ((I1 = l8.default.createElement(
+       S,
+       null,
+       l8.default.createElement(lPA, null),
+     )),
+       (K[78] = I1));
+   else I1 = K[78];
+   let Q1;
+   if (
+     K[79] !== yA ||
+     K[80] !== VA ||
+     K[81] !== SA ||
+     K[82] !== xA ||
+     K[83] !== iA ||
+     K[84] !== lA ||
+     K[85] !== v1
+   )
+     ((Q1 = l8.default.createElement(
+       S,
+       { flexDirection: "column", gap: 1, paddingX: 1, paddingTop: 1 },
+       yA,
+       VA,
+       vA,
+       RA,
+       fA,
+       LA,
+       SA,
+       xA,
+       iA,
+       lA,
+       v1,
+       I1,
+     )),
+       (K[79] = yA),
+       (K[80] = VA),
+       (K[81] = SA),
+       (K[82] = xA),
+       (K[83] = iA),
+       (K[84] = lA),
+       (K[85] = v1),
+       (K[86] = Q1));
+   else Q1 = K[86];
+   return Q1;
+ }

+++ Added $B2 (pretty-v2.1.23.js:483933-483935)
+ function $B2(A, K) {
+   return l8.default.createElement(V, { key: K, dimColor: !0 }, "    ", "└ ", A);
+ }

+++ Added _B2 (pretty-v2.1.23.js:483936-483938)
+ function _B2(A, K) {
+   return l8.default.createElement(V, { key: K, dimColor: !0 }, "    ", "└ ", A);
+ }

+++ Added GB2 (pretty-v2.1.23.js:483939-483941)
+ function GB2(A, K) {
+   return l8.default.createElement(V, { key: K, dimColor: !0 }, "    ", "└ ", A);
+ }

+++ Added ZB2 (pretty-v2.1.23.js:483942-483944)
+ function ZB2(A, K) {
+   return l8.default.createElement(V, { key: K, dimColor: !0 }, "  ", "└ ", A);
+ }

+++ Added WB2 (pretty-v2.1.23.js:483945-483957)
+ function WB2(A, K) {
+   return l8.default.createElement(
+     V,
+     { key: K, dimColor: !0 },
+     "  ",
+     "└ ",
+     A.source || "unknown",
+     "plugin" in A && A.plugin ? ` [${A.plugin}]` : "",
+     ":",
+     " ",
+     _M(A),
+   );
+ }

+++ Added DB2 (pretty-v2.1.23.js:483958-483968)
+ function DB2(A, K) {
+   return l8.default.createElement(
+     V,
+     { key: K, dimColor: !0 },
+     "  ",
+     "└ ",
+     A.path,
+     ": ",
+     A.error,
+   );
+ }

+++ Added jB2 (pretty-v2.1.23.js:483969-483982)
+ function jB2(A, K) {
+   return l8.default.createElement(
+     V,
+     { key: K },
+     "└ ",
+     A.version,
+     ": PID ",
+     A.pid,
+     " ",
+     A.isProcessRunning
+       ? l8.default.createElement(V, null, "(running)")
+       : l8.default.createElement(V, { color: "warning" }, "(stale)"),
+   );
+ }

+++ Added MB2 (pretty-v2.1.23.js:483983-483997)
+ function MB2(A, K) {
+   return l8.default.createElement(
+     V,
+     { key: K },
+     "└ ",
+     A.name,
+     ":",
+     " ",
+     l8.default.createElement(
+       V,
+       { color: A.status === "capped" ? "warning" : "error" },
+       A.message,
+     ),
+   );
+ }

+++ Added PB2 (pretty-v2.1.23.js:483998-484005)
+ function PB2(A, K) {
+   return l8.default.createElement(
+     S,
+     { key: K, flexDirection: "column" },
+     l8.default.createElement(V, { color: "warning" }, "Warning: ", A.issue),
+     l8.default.createElement(V, null, "Fix: ", A.fix),
+   );
+ }

+++ Added VB2 (pretty-v2.1.23.js:484006-484008)
+ function VB2(A, K) {
+   return l8.default.createElement(V, { key: K }, "└ ", A.type, " at ", A.path);
+ }

+++ Added NB2 (pretty-v2.1.23.js:484012-484014)
+ function NB2(A) {
+   return A.mcpErrorMetadata === void 0;
+ }

+++ Added TB2 (pretty-v2.1.23.js:484015-484017)
+ function TB2(A) {
+   return (A.installationType === "native" ? aKK : oKK)().catch(vB2);
+ }

+++ Added vB2 (pretty-v2.1.23.js:484018-484020)
+ function vB2() {
+   return { latest: null, stable: null };
+ }

+++ Added EB2 (pretty-v2.1.23.js:484021-484023)
+ function EB2(A) {
+   return A.plugins.errors;
+ }

+++ Added CB2 (pretty-v2.1.23.js:484027-484029)
+ function CB2(A) {
+   return A.mcp.tools;
+ }

+++ Added xm2 (pretty-v2.1.23.js:490554-490556)
+ function xm2(A) {
+   return A.mcp.tools;
+ }

+++ Added Fm2 (pretty-v2.1.23.js:491530-491532)
+ function Fm2(A) {
+   return A.mcp.clients;
+ }

+++ Added Sg2 (pretty-v2.1.23.js:497745-497747)
+ function Sg2(A) {
+   return A.plugins.errors;
+ }

+++ Added hg2 (pretty-v2.1.23.js:497748-497750)
+ function hg2(A) {
+   return A.plugins.installationStatus;
+ }

+++ Added dg2 (pretty-v2.1.23.js:498816-498818)
+ function dg2(A) {
+   return A.mcp.clients;
+ }

+++ Added Ac2 (pretty-v2.1.23.js:505246-505248)
+ function Ac2(A) {
+   return A.contentBlock.id;
+ }

+++ Added aPK (pretty-v2.1.23.js:509461-509476)
+ var aPK = k(() => {
+   cA();
+   mA();
+   C8();
+   Iq();
+   A4();
+   lFA();
+   sdA();
+   g4();
+   f_();
+   nK();
+   Dq();
+   ty6();
+   $8();
+   ((i9 = o($A(), 1)), (lc2 = []));
+ });

+++ Added El2 (pretty-v2.1.23.js:511846-511848)
+ function El2(A) {
+   return { label: A.path, value: A.path };
+ }

+++ Added ll2 (pretty-v2.1.23.js:514358-514360)
+ function ll2(A) {
+   return A.source;
+ }

+++ Added tl2 (pretty-v2.1.23.js:516036-516038)
+ function tl2(A) {
+   return A.name;
+ }

+++ Added el2 (pretty-v2.1.23.js:516039-516041)
+ function el2(A) {
+   return A.mcp;
+ }

+++ Added mi2 (pretty-v2.1.23.js:518445-518447)
+ function mi2(A) {
+   return A.name;
+ }

+++ Added Fi2 (pretty-v2.1.23.js:518449-518451)
+ function Fi2(A) {
+   return A.name;
+ }

+++ Added Qi2 (pretty-v2.1.23.js:518452-518454)
+ function Qi2(A) {
+   return A.name;
+ }

+++ Added Ui2 (pretty-v2.1.23.js:518455-518457)
+ function Ui2(A) {
+   return A.name;
+ }

+++ Added pi2 (pretty-v2.1.23.js:518458-518460)
+ function pi2(A) {
+   return A.name;
+ }

+++ Added di2 (pretty-v2.1.23.js:518461-518463)
+ function di2(A) {
+   return A.name;
+ }

+++ Added pn2 (pretty-v2.1.23.js:523598-523600)
+ function pn2(A) {
+   return A.mcp.clients;
+ }

+++ Added Hr2 (pretty-v2.1.23.js:524162-524164)
+ function Hr2(A) {
+   return A.mainLoopModelForSession;
+ }

+++ Added Jr2 (pretty-v2.1.23.js:524165-524167)
+ function Jr2(A) {
+   return A.mainLoopModel;
+ }

+++ Added Gr2 (pretty-v2.1.23.js:524226-524228)
+ function Gr2(A) {
+   return A.mainLoopModelForSession;
+ }

+++ Added Zr2 (pretty-v2.1.23.js:524229-524231)
+ function Zr2(A) {
+   return A.mainLoopModel;
+ }

+++ Added vvK (pretty-v2.1.23.js:528706-528707)
+ var vvK =
+     "IMPORTANT: Assist with authorized security testing, defensive security, CTF challenges, and educational contexts. Refuse requests for destructive techniques, DoS attacks, mass targeting, supply chain compromise, or detection evasion for malicious purposes. Dual-use security tools (C2 frameworks, credential testing, exploit development) require clear authorization context: pentesting engagements, CTF competitions, security research, or defensive use cases.",

+++ Added UUA (pretty-v2.1.23.js:528708-528708)
+   UUA = "__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__",

+++ Added qa2 (pretty-v2.1.23.js:528788-528792)
+ function qa2(A, K, q, Y, z) {
+   if (!Xs() || !kmA(z) || "effort" in K) return;
+   if (A === void 0) Y.push(zR1);
+   else if (typeof A === "string") ((K.effort = A), Y.push(zR1));
+ }

+++ Added UvK (pretty-v2.1.23.js:530857-530859)
+ function UvK(A, K) {
+   return ("updatedInput" in A ? A.updatedInput : void 0) ?? K;
+ }

+++ Added ae (pretty-v2.1.23.js:532692-532694)
+ function ae() {
+   return xIA();
+ }

+++ Added xu6 (pretty-v2.1.23.js:533097-533100)
+ function xu6() {
+   if (o6() === "windows") return "claude";
+   return `claude-${process.getuid?.() ?? 0}`;
+ }

+++ Added HAz (pretty-v2.1.23.js:538635-538723)
+ var HAz = `## Settings File Locations
+ 
+ Choose the appropriate file based on scope:
+ 
+ | File | Scope | Git | Use For |
+ |------|-------|-----|---------|
+ | \`~/.claude/settings.json\` | Global | N/A | Personal preferences for all projects |
+ | \`.claude/settings.json\` | Project | Commit | Team-wide hooks, permissions, plugins |
+ | \`.claude/settings.local.json\` | Project | Gitignore | Personal overrides for this project |
+ 
+ Settings load in order: user → project → local (later overrides earlier).
+ 
+ ## Settings Schema Reference
+ 
+ ### Permissions
+ \`\`\`json
+ {
+   "permissions": {
+     "allow": ["Bash(npm:*)", "Edit(.claude)", "Read"],
+     "deny": ["Bash(rm -rf:*)"],
+     "ask": ["Write(/etc/*)"],
+     "defaultMode": "default" | "plan" | "acceptEdits" | "dontAsk",
+     "additionalDirectories": ["/extra/dir"]
+   }
+ }
+ \`\`\`
+ 
+ **Permission Rule Syntax:**
+ - Exact match: \`"Bash(npm run test)"\`
+ - Prefix wildcard: \`"Bash(git:*)"\` - matches \`git status\`, \`git commit\`, etc.
+ - Tool only: \`"Read"\` - allows all Read operations
+ 
+ ### Environment Variables
+ \`\`\`json
+ {
+   "env": {
+     "DEBUG": "true",
+     "MY_API_KEY": "value"
+   }
+ }
+ \`\`\`
+ 
+ ### Model & Agent
+ \`\`\`json
+ {
+   "model": "sonnet",  // or "opus", "haiku", full model ID
+   "agent": "agent-name",
+   "alwaysThinkingEnabled": true
+ }
+ \`\`\`
+ 
+ ### Attribution (Commits & PRs)
+ \`\`\`json
+ {
+   "attribution": {
+     "commit": "Custom commit trailer text",
+     "pr": "Custom PR description text"
+   }
+ }
+ \`\`\`
+ Set \`commit\` or \`pr\` to empty string \`""\` to hide that attribution.
+ 
+ ### MCP Server Management
+ \`\`\`json
+ {
+   "enableAllProjectMcpServers": true,
+   "enabledMcpjsonServers": ["server1", "server2"],
+   "disabledMcpjsonServers": ["blocked-server"]
+ }
+ \`\`\`
+ 
+ ### Plugins
+ \`\`\`json
+ {
+   "enabledPlugins": {
+     "formatter@anthropic-tools": true
+   }
+ }
+ \`\`\`
+ Plugin syntax: \`plugin-name@source\` where source is \`claude-code-marketplace\`, \`claude-plugins-official\`, or \`builtin\`.
+ 
+ ### Other Settings
+ - \`language\`: Preferred response language (e.g., "japanese")
+ - \`cleanupPeriodDays\`: Days to keep transcripts (0 = forever)
+ - \`respectGitignore\`: Whether to respect .gitignore (default: true)
+ - \`spinnerTipsEnabled\`: Show tips in spinner
+ - \`spinnerVerbs\`: Customize spinner verbs (\`{ "mode": "append" | "replace", "verbs": [...] }\`)
+ - \`syntaxHighlightingDisabled\`: Disable diff highlighting
+ `,

+++ Added j1z (pretty-v2.1.23.js:542851-542853)
+ function j1z(A) {
+   return A.toolPermissionContext;
+ }

+++ Added X6z (pretty-v2.1.23.js:546633-546635)
+ function X6z(A) {
+   return A.toolPermissionContext.mode;
+ }

+++ Added P6z (pretty-v2.1.23.js:547675-547677)
+ function P6z(A) {
+   return A.toolPermissionContext.mode;
+ }

+++ Added V6z (pretty-v2.1.23.js:548197-548199)
+ function V6z(A) {
+   return A.toolPermissionContext.mode;
+ }

+++ Added y6z (pretty-v2.1.23.js:550181-550183)
+ function y6z(A) {
+   return A.notifications;
+ }

+++ Added yyK (pretty-v2.1.23.js:552595-552648)
+ function yyK(A, K, q, Y, z = !0) {
+   let w = A.length;
+   if (w === 0)
+     return {
+       startIndex: 0,
+       endIndex: 0,
+       showLeftArrow: !1,
+       showRightArrow: !1,
+     };
+   let H = Math.max(0, Math.min(Y, w - 1));
+   if (A.reduce((Z, W) => Z + W, 0) <= K)
+     return {
+       startIndex: 0,
+       endIndex: w,
+       showLeftArrow: !1,
+       showRightArrow: !1,
+     };
+   let O = [0];
+   for (let Z = 0; Z < w; Z++) O.push(O[Z] + A[Z]);
+   function X(Z, W) {
+     let D = O[W] - O[Z];
+     if (z && Z > 0) return D - 1;
+     return D;
+   }
+   function $(Z, W) {
+     let D = K;
+     if (Z > 0) D -= q;
+     if (W < w) D -= q;
+     return D;
+   }
+   let _ = 0,
+     G = 1;
+   while (G < w && X(_, G + 1) <= $(_, G + 1)) G++;
+   if (H >= _ && H < G)
+     return {
+       startIndex: _,
+       endIndex: G,
+       showLeftArrow: _ > 0,
+       showRightArrow: G < w,
+     };
+   if (H >= G) {
+     ((G = H + 1), (_ = H));
+     while (_ > 0 && X(_ - 1, G) <= $(_ - 1, G)) _--;
+   } else {
+     ((_ = H), (G = H + 1));
+     while (G < w && X(_, G + 1) <= $(_, G + 1)) G++;
+   }
+   return {
+     startIndex: _,
+     endIndex: G,
+     showLeftArrow: _ > 0,
+     showRightArrow: G < w,
+   };
+ }

+++ Added ep6 (pretty-v2.1.23.js:552652-552882)
+ function ep6(A) {
+   let K = s(65),
+     {
+       tasksSelected: q,
+       showHint: Y,
+       isViewingTeammate: z,
+       teammateFooterIndex: w,
+     } = A,
+     H = w === void 0 ? 0 : w,
+     { columns: J } = f8(),
+     O;
+   if (K[0] === Symbol.for("react.memo_cache_sentinel"))
+     ((O = M1()), (K[0] = O));
+   else O = K[0];
+   let X = O.hasSeenTasksHint,
+     $ = F1(V8z),
+     _ = F1(P8z),
+     G;
+   if (K[1] !== $)
+     ((G = Object.values($ ?? {}).filter(qYA)), (K[1] = $), (K[2] = G));
+   else G = K[2];
+   let Z = G,
+     W = Z.length > 0 && Z.every(M8z),
+     D;
+   if (K[3] !== Z) ((D = Z.filter(j8z).sort(D8z)), (K[3] = Z), (K[4] = D));
+   else D = K[4];
+   let j = D,
+     M;
+   if (K[5] === Symbol.for("react.memo_cache_sentinel"))
+     ((M = { name: "main", color: void 0, idx: 0 }), (K[5] = M));
+   else M = K[5];
+   let P;
+   if (K[6] !== j) ((P = [M, ...j.map(W8z)]), (K[6] = j), (K[7] = P));
+   else P = K[7];
+   let f = P,
+     N;
+   if (K[8] !== f) ((N = f.map(Z8z)), (K[8] = f), (K[9] = N));
+   else N = K[9];
+   let T = N;
+   if (W || z) {
+     let x = q ? H : -1,
+       y;
+     if (K[10] !== j || K[11] !== _)
+       ((y = _ ? j.findIndex((hA) => hA.id === _) + 1 : 0),
+         (K[10] = j),
+         (K[11] = _),
+         (K[12] = y));
+     else y = K[12];
+     let B = y,
+       b;
+     if (K[13] !== Y || K[14] !== q)
+       ((b =
+         Y && !X && !q
+           ? XK.createElement(
+               XK.Fragment,
+               null,
+               XK.createElement(V, { dimColor: !0 }, " · "),
+               XK.createElement(
+                 V,
+                 { dimColor: !0 },
+                 XK.createElement(M6, { shortcut: "↓", action: "view" }),
+               ),
+             )
+           : null),
+         (K[13] = Y),
+         (K[14] = q),
+         (K[15] = b));
+     else b = K[15];
+     let F = b,
+       u = Math.max(20, J - (F ? 15 : 0) - 35),
+       d = x >= 0 ? x : 0,
+       r;
+     if (K[16] !== u || K[17] !== T || K[18] !== d)
+       ((r = yyK(T, u, 2, d)),
+         (K[16] = u),
+         (K[17] = T),
+         (K[18] = d),
+         (K[19] = r));
+     else r = K[19];
+     let {
+         startIndex: c,
+         endIndex: YA,
+         showLeftArrow: e,
+         showRightArrow: qA,
+       } = r,
+       HA;
+     if (K[20] !== f || K[21] !== YA || K[22] !== c)
+       ((HA = f.slice(c, YA)),
+         (K[20] = f),
+         (K[21] = YA),
+         (K[22] = c),
+         (K[23] = HA));
+     else HA = K[23];
+     let _A = HA,
+       a;
+     if (K[24] !== e)
+       ((a = e && XK.createElement(V, { dimColor: !0 }, eA.arrowLeft, " ")),
+         (K[24] = e),
+         (K[25] = a));
+     else a = K[25];
+     let JA;
+     if (K[26] !== x || K[27] !== B || K[28] !== _A)
+       ((JA = _A.map((hA, yA) => {
+         let AA = yA > 0;
+         return XK.createElement(
+           XK.Fragment,
+           { key: hA.name },
+           AA && XK.createElement(V, null, " "),
+           XK.createElement(f8z, {
+             name: hA.name,
+             color: hA.color,
+             isSelected: x === hA.idx,
+             isViewed: B === hA.idx,
+           }),
+         );
+       })),
+         (K[26] = x),
+         (K[27] = B),
+         (K[28] = _A),
+         (K[29] = JA));
+     else JA = K[29];
+     let jA;
+     if (K[30] !== qA)
+       ((jA = qA && XK.createElement(V, { dimColor: !0 }, " ", eA.arrowRight)),
+         (K[30] = qA),
+         (K[31] = jA));
+     else jA = K[31];
+     let MA;
+     if (K[32] !== a || K[33] !== JA || K[34] !== jA || K[35] !== F)
+       ((MA = XK.createElement(XK.Fragment, null, a, JA, jA, F)),
+         (K[32] = a),
+         (K[33] = JA),
+         (K[34] = jA),
+         (K[35] = F),
+         (K[36] = MA));
+     else MA = K[36];
+     return MA;
+   }
+   let C;
+   if (K[37] !== Y || K[38] !== q)
+     ((C =
+       Y && (q || !X)
+         ? XK.createElement(
+             XK.Fragment,
+             null,
+             XK.createElement(V, { dimColor: !0 }, " · "),
+             XK.createElement(
+               V,
+               { dimColor: !0 },
+               q
+                 ? XK.createElement(M6, {
+                     shortcut: "Enter",
+                     action: "view tasks",
+                   })
+                 : XK.createElement(M6, { shortcut: "↓", action: "view" }),
+             ),
+           )
+         : null),
+       (K[37] = Y),
+       (K[38] = q),
+       (K[39] = C));
+   else C = K[39];
+   let R = C;
+   if (Z.length === 0) return null;
+   if (Z.length === 1 && J >= 150) {
+     let x = Z[0],
+       y,
+       B,
+       b,
+       F;
+     if (K[40] !== x || K[41] !== q) {
+       let r = T8z(x);
+       ((y = V),
+         (F = "background"),
+         (B = q),
+         (b = a9(r, 40, !0)),
+         (K[40] = x),
+         (K[41] = q),
+         (K[42] = y),
+         (K[43] = B),
+         (K[44] = b),
+         (K[45] = F));
+     } else ((y = K[42]), (B = K[43]), (b = K[44]), (F = K[45]));
+     let Q;
+     if (K[46] !== x.status)
+       ((Q = XK.createElement(V, { dimColor: !0 }, "(", x.status, ")")),
+         (K[46] = x.status),
+         (K[47] = Q));
+     else Q = K[47];
+     let u;
+     if (K[48] !== y || K[49] !== B || K[50] !== b || K[51] !== Q || K[52] !== F)
+       ((u = XK.createElement(y, { color: F, inverse: B }, b, " ", Q)),
+         (K[48] = y),
+         (K[49] = B),
+         (K[50] = b),
+         (K[51] = Q),
+         (K[52] = F),
+         (K[53] = u));
+     else u = K[53];
+     let d;
+     if (K[54] !== R || K[55] !== u)
+       ((d = XK.createElement(XK.Fragment, null, u, R)),
+         (K[54] = R),
+         (K[55] = u),
+         (K[56] = d));
+     else d = K[56];
+     return d;
+   }
+   if (Z.length >= 1) {
+     let x;
+     if (K[57] !== Z) ((x = v8z(Z)), (K[57] = Z), (K[58] = x));
+     else x = K[58];
+     let y = x,
+       B;
+     if (K[59] !== y || K[60] !== q)
+       ((B = XK.createElement(V, { color: "background", inverse: q }, y)),
+         (K[59] = y),
+         (K[60] = q),
+         (K[61] = B));
+     else B = K[61];
+     let b;
+     if (K[62] !== R || K[63] !== B)
+       ((b = XK.createElement(XK.Fragment, null, B, R)),
+         (K[62] = R),
+         (K[63] = B),
+         (K[64] = b));
+     else b = K[64];
+     return b;
+   }
+   return null;
+ }

+++ Added Z8z (pretty-v2.1.23.js:552883-552886)
+ function Z8z(A, K) {
+   let q = `@${A.name}`;
+   return j7(q) + (K > 0 ? 1 : 0);
+ }

+++ Added W8z (pretty-v2.1.23.js:552887-552893)
+ function W8z(A, K) {
+   return {
+     name: A.identity.agentName,
+     color: N8z(A.identity.color),
+     idx: K + 1,
+   };
+ }

+++ Added D8z (pretty-v2.1.23.js:552894-552896)
+ function D8z(A, K) {
+   return A.identity.agentName.localeCompare(K.identity.agentName);
+ }

+++ Added P8z (pretty-v2.1.23.js:552903-552905)
+ function P8z(A) {
+   return A.viewingAgentTaskId;
+ }

+++ Added V8z (pretty-v2.1.23.js:552906-552908)
+ function V8z(A) {
+   return A.tasks;
+ }

+++ Added f8z (pretty-v2.1.23.js:552909-552955)
+ function f8z(A) {
+   let K = s(11),
+     { name: q, color: Y, isSelected: z, isViewed: w } = A;
+   if (z) {
+     let O;
+     if (K[0] !== Y || K[1] !== w || K[2] !== q)
+       ((O = Y
+         ? XK.createElement(
+             V,
+             { backgroundColor: Y, color: "inverseText", bold: w },
+             "@",
+             q,
+           )
+         : XK.createElement(
+             V,
+             { color: "background", inverse: !0, bold: w },
+             "@",
+             q,
+           )),
+         (K[0] = Y),
+         (K[1] = w),
+         (K[2] = q),
+         (K[3] = O));
+     else O = K[3];
+     return O;
+   }
+   if (w) {
+     let O;
+     if (K[4] !== Y || K[5] !== q)
+       ((O = XK.createElement(V, { color: Y, bold: !0 }, "@", q)),
+         (K[4] = Y),
+         (K[5] = q),
+         (K[6] = O));
+     else O = K[6];
+     return O;
+   }
+   let H = !Y,
+     J;
+   if (K[7] !== Y || K[8] !== q || K[9] !== H)
+     ((J = XK.createElement(V, { color: Y, dimColor: H }, "@", q)),
+       (K[7] = Y),
+       (K[8] = q),
+       (K[9] = H),
+       (K[10] = J));
+   else J = K[10];
+   return J;
+ }

+++ Added N8z (pretty-v2.1.23.js:552956-552960)
+ function N8z(A) {
+   if (!A) return;
+   if (Y0.includes(A)) return LJ[A];
+   return;
+ }

+++ Added k8z (pretty-v2.1.23.js:553064-553066)
+ function k8z(A) {
+   return A.teamContext;
+ }

+++ Added m8z (pretty-v2.1.23.js:553435-553662)
+ function m8z(A) {
+   let K = s(16),
+     {
+       mode: q,
+       toolPermissionContext: Y,
+       showHint: z,
+       isLoading: w,
+       tasksSelected: H,
+       teamsSelected: J,
+       diffSelected: O,
+       loopSelected: X,
+       teammateFooterIndex: $,
+     } = A,
+     { columns: _ } = f8(),
+     G = cK("chat:cycleMode", "Chat", "shift+tab"),
+     Z = F1(l8z),
+     W = F1(c8z),
+     D = F1(d8z),
+     j = F1(p8z),
+     M = F1(U8z),
+     P = F1(Q8z),
+     f = !1,
+     N;
+   if (K[0] !== Z) ((N = Object.values(Z).filter(qYA)), (K[0] = Z), (K[1] = N));
+   else N = K[1];
+   let T = N.length,
+     C = T > 0,
+     R = cK("chat:cancel", "Chat", "esc").toLowerCase(),
+     x = cK("app:toggleTodos", "Global", "ctrl+t"),
+     y = ByK(),
+     B;
+   if (K[2] !== y?.stats)
+     ((B = G4("tengu_code_diff_cli", !1) ? (y?.stats ?? null) : null),
+       (K[2] = y?.stats),
+       (K[3] = B));
+   else B = K[3];
+   let b = B,
+     F;
+   if (K[4] !== W)
+     ((F =
+       b8() &&
+       !Gm() &&
+       W !== void 0 &&
+       Object.values(W.teammates).filter(F8z).length > 0),
+       (K[4] = W),
+       (K[5] = F));
+   else F = K[5];
+   let Q = F;
+   if (q === "bash") {
+     let yA;
+     if (K[6] === Symbol.for("react.memo_cache_sentinel"))
+       ((yA = N7.createElement(V, { color: "bashBorder" }, "! for bash mode")),
+         (K[6] = yA));
+     else yA = K[6];
+     return yA;
+   }
+   if (q === "background") {
+     let yA;
+     if (K[7] === Symbol.for("react.memo_cache_sentinel"))
+       ((yA = N7.createElement(V, { color: "background" }, "& to background")),
+         (K[7] = yA));
+     else yA = K[7];
+     return yA;
+   }
+   let u = Y?.mode,
+     d = !dR8(u),
+     r = j === "viewing-agent",
+     c = T > 0 || r,
+     YA = 0 + (d ? 1 : 0) + (c ? 1 : 0) + (Q ? 1 : 0),
+     HA =
+       (M1().codeDiffFooterEnabled ?? !0) &&
+       b &&
+       b.filesCount > 0 &&
+       YA < 2 &&
+       (YA === 0 || _ >= 100),
+     _A =
+       dyK() &&
+       P.number !== null &&
+       P.reviewState !== null &&
+       P.url !== null &&
+       YA < 2 &&
+       (YA === 0 || _ >= 100),
+     a = YA < 2 && u !== "coordinator",
+     jA = (c && Object.values(Z).some(g8z)) || r,
+     MA = [
+       ...(D
+         ? [
+             N7.createElement(
+               V,
+               { color: "ide", key: "remote" },
+               eA.circleDouble,
+               " remote",
+             ),
+           ]
+         : []),
+       ...(u && d
+         ? [
+             N7.createElement(
+               V,
+               { color: OD(u), key: "mode" },
+               dEA(u),
+               " ",
+               fF(u).toLowerCase(),
+               " on",
+               a &&
+                 N7.createElement(
+                   V,
+                   { dimColor: !0 },
+                   " ",
+                   N7.createElement(M6, {
+                     shortcut: G,
+                     action: "cycle",
+                     parens: !0,
+                   }),
+                 ),
+             ),
+           ]
+         : []),
+       ...[],
+       ...(c && !jA
+         ? [
+             N7.createElement(ep6, {
+               key: "tasks",
+               tasksSelected: H,
+               showHint: z && !Q,
+               isViewingTeammate: r,
+               teammateFooterIndex: $,
+             }),
+           ]
+         : []),
+       ...(b8() && Q
+         ? [
+             N7.createElement(hyK, {
+               key: "teams",
+               teamsSelected: J,
+               showHint: z && !c,
+             }),
+           ]
+         : []),
+       ...(HA
+         ? [
+             N7.createElement(
+               V,
+               {
+                 key: "code-changes",
+                 dimColor: !O,
+                 inverse: O,
+                 color: O ? "background" : void 0,
+               },
+               b.filesCount,
+               " ",
+               b.filesCount === 1 ? "file" : "files",
+               " ",
+               N7.createElement(
+                 V,
+                 { color: "diffAddedWord" },
+                 "+",
+                 b.linesAdded,
+               ),
+               " ",
+               N7.createElement(
+                 V,
+                 { color: "diffRemovedWord" },
+                 "-",
+                 b.linesRemoved,
+               ),
+               O &&
+                 z &&
+                 N7.createElement(V, { dimColor: !0 }, " · Enter to view"),
+             ),
+           ]
+         : []),
+       ...(_A
+         ? [
+             N7.createElement(
+               V,
+               { key: "pr-status", dimColor: !0 },
+               N7.createElement(V, { color: n8z(P.reviewState) }, "PR"),
+               " ",
+               N7.createElement(X7, { url: P.url }, "#", P.number),
+             ),
+           ]
+         : []),
+     ],
+     hA = z ? i8z(w, R, x, C, M) : [];
+   if (!jA && z) MA.push(...hA);
+   if (jA) {
+     let yA = [...MA, ...hA],
+       AA;
+     if (K[8] !== r || K[9] !== H || K[10] !== $)
+       ((AA = N7.createElement(
+         S,
+         null,
+         N7.createElement(ep6, {
+           tasksSelected: H,
+           showHint: !1,
+           isViewingTeammate: r,
+           teammateFooterIndex: $,
+         }),
+       )),
+         (K[8] = r),
+         (K[9] = H),
+         (K[10] = $),
+         (K[11] = AA));
+     else AA = K[11];
+     let wA =
+         yA.length > 0 &&
+         N7.createElement(S, null, N7.createElement(Y8, null, yA)),
+       GA;
+     if (K[12] !== AA || K[13] !== wA)
+       ((GA = N7.createElement(S, { flexDirection: "column" }, AA, wA)),
+         (K[12] = AA),
+         (K[13] = wA),
+         (K[14] = GA));
+     else GA = K[14];
+     return GA;
+   }
+   if (MA.length === 0) {
+     if (!z) return null;
+     let yA;
+     if (K[15] === Symbol.for("react.memo_cache_sentinel"))
+       ((yA = N7.createElement(V, { dimColor: !0 }, "? for shortcuts")),
+         (K[15] = yA));
+     else yA = K[15];
+     return yA;
+   }
+   return N7.createElement(S, null, N7.createElement(Y8, null, MA));
+ }

+++ Added g8z (pretty-v2.1.23.js:553663-553665)
+ function g8z(A) {
+   return A.type === "in_process_teammate";
+ }

+++ Added Q8z (pretty-v2.1.23.js:553669-553671)
+ function Q8z(A) {
+   return A.prStatus;
+ }

+++ Added U8z (pretty-v2.1.23.js:553672-553674)
+ function U8z(A) {
+   return A.showExpandedTodos;
+ }

+++ Added p8z (pretty-v2.1.23.js:553675-553677)
+ function p8z(A) {
+   return A.viewSelectionMode;
+ }

+++ Added d8z (pretty-v2.1.23.js:553678-553680)
+ function d8z(A) {
+   return A.remoteSessionUrl;
+ }

+++ Added c8z (pretty-v2.1.23.js:553681-553683)
+ function c8z(A) {
+   return A.teamContext;
+ }

+++ Added l8z (pretty-v2.1.23.js:553684-553686)
+ function l8z(A) {
+   return A.tasks;
+ }

+++ Added i8z (pretty-v2.1.23.js:553687-553711)
+ function i8z(A, K, q, Y, z) {
+   return [
+     ...(A
+       ? [
+           N7.createElement(
+             V,
+             { dimColor: !0, key: "esc" },
+             N7.createElement(M6, { shortcut: K, action: "interrupt" }),
+           ),
+         ]
+       : []),
+     ...(Y
+       ? [
+           N7.createElement(
+             V,
+             { dimColor: !0, key: "tasks" },
+             N7.createElement(M6, {
+               shortcut: q,
+               action: z ? "hide tasks" : "show tasks",
+             }),
+           ),
+         ]
+       : []),
+   ];
+ }

+++ Added m4z (pretty-v2.1.23.js:556462-556464)
+ function m4z(A) {
+   return A.queuedCommands;
+ }

+++ Added p4z (pretty-v2.1.23.js:557151-557187)
+ function p4z(A) {
+   let K = s(8),
+     { shimmer: q, suffix: Y } = A,
+     z = LS("requesting", Od6, q, !1),
+     w;
+   if (K[0] !== z || K[1] !== q)
+     ((w = Od6.split("").map((O, X) =>
+       q
+         ? E0.createElement(Dd, {
+             key: X,
+             char: O,
+             index: X,
+             glimmerIndex: z,
+             messageColor: "inactive",
+             shimmerColor: "inactiveShimmer",
+           })
+         : E0.createElement(V, { key: X, dimColor: !0 }, O),
+     )),
+       (K[0] = z),
+       (K[1] = q),
+       (K[2] = w));
+   else w = K[2];
+   let H;
+   if (K[3] !== Y)
+     ((H = Y && E0.createElement(V, { dimColor: !0 }, Y)),
+       (K[3] = Y),
+       (K[4] = H));
+   else H = K[4];
+   let J;
+   if (K[5] !== w || K[6] !== H)
+     ((J = E0.createElement(E0.Fragment, null, w, H)),
+       (K[5] = w),
+       (K[6] = H),
+       (K[7] = J));
+   else J = K[7];
+   return J;
+ }

+++ Added qSK (pretty-v2.1.23.js:557188-557248)
+ function qSK(A) {
+   let K = s(19),
+     {
+       suggestion: q,
+       isSpeculating: Y,
+       toolUseCount: z,
+       timeSavedMs: w,
+       availableWidth: H,
+     } = A,
+     J = j7(Od6),
+     O;
+   if (K[0] !== Y || K[1] !== w || K[2] !== z)
+     ((O = Y
+       ? z > 0
+         ? ` ${z}`
+         : null
+       : w !== null && w >= U4z
+         ? ` ${Math.round(w / 1000)}s`
+         : null),
+       (K[0] = Y),
+       (K[1] = w),
+       (K[2] = z),
+       (K[3] = O));
+   else O = K[3];
+   let X = O,
+     $;
+   if (K[4] !== X) (($ = X ? j7(X) : 0), (K[4] = X), (K[5] = $));
+   else $ = K[5];
+   let _ = J + $,
+     G = H - _ - 1,
+     Z = q;
+   while (j7(Z) > G && Z.length > 0) Z = Z.slice(0, -1);
+   let W = Math.max(0, H - j7(Z) - _),
+     D;
+   if (K[6] !== Z)
+     ((D = E0.createElement(V, { dimColor: !0 }, Z)), (K[6] = Z), (K[7] = D));
+   else D = K[7];
+   let j;
+   if (K[8] !== W) ((j = " ".repeat(W)), (K[8] = W), (K[9] = j));
+   else j = K[9];
+   let M;
+   if (K[10] !== j)
+     ((M = E0.createElement(V, null, j)), (K[10] = j), (K[11] = M));
+   else M = K[11];
+   let P;
+   if (K[12] !== Y || K[13] !== X)
+     ((P = E0.createElement(p4z, { shimmer: Y, suffix: X })),
+       (K[12] = Y),
+       (K[13] = X),
+       (K[14] = P));
+   else P = K[14];
+   let f;
+   if (K[15] !== D || K[16] !== M || K[17] !== P)
+     ((f = E0.createElement(E0.Fragment, null, D, M, P)),
+       (K[15] = D),
+       (K[16] = M),
+       (K[17] = P),
+       (K[18] = f));
+   else f = K[18];
+   return f;
+ }

+++ Added YSK (pretty-v2.1.23.js:557252-557260)
+ var YSK = k(() => {
+   cA();
+   g4();
+   mA();
+   XG();
+   W3A();
+   QjA();
+   ((E0 = o($A(), 1)), (Od6 = `${eA.play}${eA.play}`));
+ });

+++ Added z7z (pretty-v2.1.23.js:559113-559120)
+ function z7z(A) {
+   return (
+     typeof A === "object" &&
+     A !== null &&
+     "type" in A &&
+     typeof A.type === "string"
+   );
+ }

+++ Added Zd6 (pretty-v2.1.23.js:559121-559207)
+ class Zd6 {
+   ws = null;
+   config;
+   callbacks;
+   constructor(A, K) {
+     ((this.config = A), (this.callbacks = K));
+   }
+   connect() {
+     let A = {};
+     if (this.config.authToken)
+       A.authorization = `Bearer ${this.config.authToken}`;
+     ((this.ws = new WebSocket(this.config.wsUrl, { headers: A })),
+       this.ws.addEventListener("open", () => {
+         this.callbacks.onConnected?.();
+       }),
+       this.ws.addEventListener("message", (K) => {
+         let Y = (typeof K.data === "string" ? K.data : "")
+           .split(
+             `
+ `,
+           )
+           .filter((z) => z.trim());
+         for (let z of Y) {
+           let w;
+           try {
+             w = G6(z);
+           } catch {
+             continue;
+           }
+           if (!z7z(w)) continue;
+           let H = w;
+           if (H.type === "control_request") {
+             if (H.request.subtype === "can_use_tool") {
+               this.callbacks.onPermissionRequest(H.request, H.request_id);
+               continue;
+             }
+           }
+           if (
+             H.type !== "control_request" &&
+             H.type !== "control_response" &&
+             H.type !== "keep_alive" &&
+             H.type !== "control_cancel_request"
+           )
+             this.callbacks.onMessage(H);
+         }
+       }),
+       this.ws.addEventListener("close", () => {
+         this.callbacks.onDisconnected?.();
+       }),
+       this.ws.addEventListener("error", () => {
+         this.callbacks.onError?.(Error("WebSocket connection error"));
+       }));
+   }
+   sendMessage(A) {
+     if (!this.ws || this.ws.readyState !== WebSocket.OPEN) return !1;
+     let K = UA({
+       type: "user",
+       message: { role: "user", content: A },
+       parent_tool_use_id: null,
+       session_id: "",
+     });
+     return (this.ws.send(K), !0);
+   }
+   respondToPermissionRequest(A, K) {
+     if (!this.ws || this.ws.readyState !== WebSocket.OPEN) return;
+     let q = UA({
+       type: "control_response",
+       response: {
+         subtype: "success",
+         request_id: A,
+         response: {
+           behavior: K.behavior,
+           ...(K.behavior === "allow"
+             ? { updatedInput: K.updatedInput }
+             : { message: K.message }),
+         },
+       },
+     });
+     this.ws.send(q);
+   }
+   disconnect() {
+     if (this.ws) (this.ws.close(), (this.ws = null));
+   }
+   isConnected() {
+     return this.ws?.readyState === WebSocket.OPEN;
+   }
+ }

+++ Added DSK (pretty-v2.1.23.js:559211-559305)
+ function DSK({ config: A, setMessages: K, setIsLoading: q }) {
+   let Y = !!A,
+     [z, w] = rL.useState({
+       isConnected: !1,
+       isLoading: !1,
+       responseTimedOut: !1,
+     }),
+     [H, J] = rL.useState(null),
+     O = rL.useRef(null),
+     X = rL.useRef(!1);
+   rL.useEffect(() => {
+     if (!A) return;
+     ((X.current = !1), h(`[useDirectConnect] Connecting to ${A.wsUrl}`));
+     let Z = new Zd6(A, {
+       onMessage: (W) => {
+         if (Fk1(W)) (w((j) => ({ ...j, isLoading: !1 })), q(!1));
+         if (W.type === "system" && W.subtype === "init") {
+           if (X.current) return;
+           X.current = !0;
+         }
+         let D = gk1(W, { convertToolResults: !0 });
+         if (D.type === "message") K((j) => [...j, D.message]);
+       },
+       onPermissionRequest: (W, D) => {
+         (h(`[useDirectConnect] Permission request for tool: ${W.tool_name}`),
+           J({ request: W, requestId: D }),
+           q(!1));
+       },
+       onConnected: () => {
+         (h("[useDirectConnect] Connected"),
+           w((W) => ({ ...W, isConnected: !0 })));
+       },
+       onDisconnected: () => {
+         (h("[useDirectConnect] Disconnected"),
+           w((W) => {
+             if (!W.isConnected)
+               process.stderr.write(`
+ Failed to connect to server at ${A.wsUrl}
+ `);
+             else
+               process.stderr.write(`
+ Server disconnected.
+ `);
+             return (Jq(1), { ...W, isConnected: !1 });
+           }),
+           q(!1));
+       },
+       onError: (W) => {
+         h(`[useDirectConnect] Error: ${W.message}`);
+       },
+     });
+     return (
+       (O.current = Z),
+       Z.connect(),
+       () => {
+         (h("[useDirectConnect] Cleanup - disconnecting"),
+           Z.disconnect(),
+           (O.current = null));
+       }
+     );
+   }, [A, K, q]);
+   let $ = rL.useCallback(
+       async (Z) => {
+         let W = O.current;
+         if (!W) return !1;
+         return (w((D) => ({ ...D, isLoading: !0 })), q(!0), W.sendMessage(Z));
+       },
+       [q],
+     ),
+     _ = rL.useCallback(
+       (Z) => {
+         let W = O.current,
+           D = H;
+         if (!W || !D) return;
+         let j = Z
+           ? { behavior: "allow", updatedInput: D.request.input }
+           : { behavior: "deny", message: "User denied permission" };
+         if ((W.respondToPermissionRequest(D.requestId, j), J(null), Z)) q(!0);
+       },
+       [H, q],
+     ),
+     G = rL.useCallback(() => {
+       (O.current?.disconnect(),
+         (O.current = null),
+         w({ isConnected: !1, isLoading: !1, responseTimedOut: !1 }));
+     }, []);
+   return {
+     isRemoteMode: Y,
+     state: z,
+     sendMessage: $,
+     pendingPermissionRequest: H,
+     respondToPermission: _,
+     disconnect: G,
+   };
+ }

+++ Added D7z (pretty-v2.1.23.js:559558-559560)
+ function D7z(A) {
+   return A.showExpandedTodos;
+ }

+++ Added NhK (pretty-v2.1.23.js:561838-561840)
+ function NhK(A) {
+   return;
+ }

+++ Added IhK (pretty-v2.1.23.js:562378-562422)
+ function IhK(A) {
+   let K = s(8),
+     { onBackgroundSession: q, isLoading: Y } = A,
+     z = p4(),
+     w = D0(),
+     [H, J] = yhK.useState(!1),
+     O = by(J, q, h7z),
+     X;
+   if (K[0] !== w || K[1] !== O || K[2] !== Y || K[3] !== z)
+     ((X = () => {
+       if (P1(process.env.CLAUDE_CODE_DISABLE_BACKGROUND_TASKS)) return;
+       let D = w.getState();
+       if (sj7(D)) y_1(() => w.getState(), z);
+     }),
+       (K[0] = w),
+       (K[1] = O),
+       (K[2] = Y),
+       (K[3] = z),
+       (K[4] = X));
+   else X = K[4];
+   let $ = X,
+     _;
+   if (K[5] === Symbol.for("react.memo_cache_sentinel"))
+     ((_ = { context: "Task" }), (K[5] = _));
+   else _ = K[5];
+   J6("task:background", $, _);
+   let G = cK("task:background", "Task", "ctrl+b"),
+     Z = m6.terminal === "tmux" && G === "ctrl+b" ? "ctrl+b ctrl+b" : G;
+   if (!Y || !H) return null;
+   let W;
+   if (K[6] !== Z)
+     ((W = yYA.createElement(
+       S,
+       { paddingLeft: 2 },
+       yYA.createElement(
+         V,
+         { dimColor: !0 },
+         yYA.createElement(M6, { shortcut: Z, action: "background" }),
+       ),
+     )),
+       (K[6] = Z),
+       (K[7] = W));
+   else W = K[7];
+   return W;
+ }

+++ Added g7z (pretty-v2.1.23.js:562826-562828)
+ function g7z(A) {
+   return A.uuid;
+ }

+++ Added DAA (pretty-v2.1.23.js:564112-564114)
+ function DAA() {
+   return wKz;
+ }

+++ Added zqz (pretty-v2.1.23.js:566374-566376)
+ function zqz(A) {
+   return A.fileHistory.trackedFiles;
+ }

+++ Added RgK (pretty-v2.1.23.js:566431-566431)
+ function RgK() {}

+++ Added Xqz (pretty-v2.1.23.js:566639-566641)
+ function Xqz(A) {
+   return A.plugins.installationStatus;
+ }

+++ Added Gqz (pretty-v2.1.23.js:566825-566829)
+ function Gqz(A) {
+   let K = new Map();
+   for (let q of A) if (!K.has(q.from)) K.set(q.from, q.color);
+   return [...K.entries()].map(([q, Y]) => ({ name: q, color: Y }));
+ }

+++ Added QgK (pretty-v2.1.23.js:566830-566874)
+ function QgK() {
+   let A = F1(($) => $.inbox),
+     K = F1(($) => $.viewSelectionMode),
+     { addNotification: q, removeNotification: Y } = mK(),
+     z = $fA.useRef(0),
+     H =
+       hZ() || K === "viewing-agent"
+         ? []
+         : A.messages.filter(($) => $.status === "pending" && !_qz($.text)),
+     J = H.length,
+     O = H.map(($) => $.from)
+       .sort()
+       .join(","),
+     X = $fA.useMemo(() => Gqz(H), [O]);
+   $fA.useEffect(() => {
+     if (J === 0) {
+       if (z.current > 0) Y(od6);
+       z.current = J;
+       return;
+     }
+     (q({
+       key: od6,
+       jsx: yc.createElement(
+         V,
+         { dimColor: !0 },
+         "Incoming ",
+         J === 1 ? "message" : "messages",
+         " from",
+         " ",
+         X.map(({ name: $, color: _ }, G) =>
+           yc.createElement(
+             yc.Fragment,
+             { key: $ },
+             yc.createElement(V, { bold: !0, color: Pv(_) }, "@", $),
+             G < X.length - 1 && ", ",
+           ),
+         ),
+       ),
+       priority: "immediate",
+       invalidates: [od6],
+       timeoutMs: 60000,
+     }),
+       (z.current = J));
+   }, [J, X, q, Y]);
+ }

+++ Added od6 (pretty-v2.1.23.js:566877-566877)
+   od6 = "teammate-inbox";

+++ Added IFK (pretty-v2.1.23.js:569831-569833)
+ function IFK(A) {
+   return A instanceof Error ? A.message : String(A);
+ }

+++ Added Iqz (pretty-v2.1.23.js:569834-569850)
+ async function Iqz(A, K) {
+   let q = "";
+   for (let Y = 1; Y <= vC1; Y++) {
+     let z = await K(Y);
+     if (z.done) return z.value;
+     if (
+       ((q = z.error || `${A} failed`),
+       xYA(`${A} attempt ${Y}/${vC1} failed: ${q}`),
+       Y < vC1)
+     ) {
+       let w = yqz * Math.pow(2, Y - 1);
+       (xYA(`Retrying ${A} in ${w}ms...`),
+         await new Promise((H) => setTimeout(H, w)));
+     }
+   }
+   throw Error(`${q} after ${vC1} attempts`);
+ }

+++ Added wUK (pretty-v2.1.23.js:573546-573550)
+ var wUK = k(() => {
+   i6();
+   I8();
+   IH();
+ });

+++ Added _UK (pretty-v2.1.23.js:573598-573602)
+ var _UK = k(() => {
+   i6();
+   I8();
+   I8();
+ });

+++ Added NUK (pretty-v2.1.23.js:574799-574806)
+ var NUK = k(() => {
+   C1();
+   Yc6();
+   y4();
+   fUK();
+   l1();
+   ja();
+ });

+++ Added CUK (pretty-v2.1.23.js:574863-574865)
+ var CUK = k(() => {
+   OS();
+ });

+++ Added HpK (pretty-v2.1.23.js:578106-578112)
+ var HpK = k(() => {
+   iM();
+   W$();
+   l6();
+   b1();
+   l1();
+ });

=== Structural Changes ===

@@@ function 'nLK' (was 'cCK') — structural (98.9%)
--- pretty-v2.1.22.js:546225
+++ pretty-v2.1.23.js:547243
@@ -17,8 +17,7 @@
       onFinishPlanInterview: D,
     } = A,
     j = J === void 0 ? !1 : J,
-    [M] = V6(),
-    P = M.toolPermissionContext.mode === "plan",
+    M = F1(P6z) === "plan",
     [V, N] = lY.useState(!1),
     [T, E] = lY.useState(0),
     [R, b] = lY.useState(!1),
@@ -224,9 +223,7 @@
             defaultValue: H[q.question]?.selectedValue,
             onChange: (CA) => {
               X(HA, { selectedValue: CA }, !0);
-              let dA = CA.includes("__other__")
-                  ? H[HA]?.textInputValue
-                  : void 0,
+              let SA = LA.includes("__other__") ? H[e]?.textInputValue : void 0,
                 z1 = CA.filter(TAz).concat(dA ? [dA] : []);
               $(HA, z1, void 0, !1);
             },

@@@ function 'UWK' (was 'FGK') — structural (98.1%)
--- pretty-v2.1.22.js:496286
+++ pretty-v2.1.23.js:497313
@@ -1,8 +1,9 @@
 function FGK(A) {
   let K = s(56),
     { onComplete: q } = A,
-    [Y, z] = V6(),
-    { installationStatus: w, errors: H } = Y.plugins;
+    Y = F1(hg2),
+    z = F1(Sg2),
+    w = p4();
   r8();
   let J;
   if (K[0] !== z)

@@@ variable 'v18' (was 'IA8') — structural (97.5%)
--- pretty-v2.1.22.js:14088
+++ pretty-v2.1.23.js:14105
@@ -362,7 +362,7 @@
         (this.message = this.cause ? K + ": " + this.cause.message : K));
     }
     return (
-      (Y.prototype = new (q || Error)()),
+      (Y.prototype = Object.create((q || Error).prototype)),
       Object.defineProperties(Y.prototype, {
         constructor: { value: Y, enumerable: !1 },
         name: { value: "Error [" + A + "]", enumerable: !1 },

@@@ function 'WLK' (was '_CK') — structural (97.2%)
--- pretty-v2.1.22.js:541623
+++ pretty-v2.1.23.js:542698
@@ -1,8 +1,7 @@
 function _CK(A) {
   let K = s(25),
     { permissionResult: q, toolName: Y } = A,
-    [z] = V6(),
-    { toolPermissionContext: w } = z,
+    z = F1(j1z),
     H = q.decisionReason,
     J = "suggestions" in q ? q.suggestions : void 0,
     O;

@@@ function 'Cc2' (was 'dp2') — structural (97.2%)
--- pretty-v2.1.22.js:506896
+++ pretty-v2.1.23.js:507929
@@ -1,8 +1,7 @@
 function dp2(A) {
   let K = s(23),
     { onDone: q } = A,
-    [Y] = V6(),
-    z = Y.remoteSessionUrl,
+    Y = F1(Ic2),
     [w, H] = fv1.useState(""),
     J,
     O;

@@@ function 'JQK' (was 'AFK') — structural (96.9%)
--- pretty-v2.1.22.js:570133
+++ pretty-v2.1.23.js:571843
@@ -15,7 +15,7 @@
   taskListId: G,
 }) {
   let { rows: W } = M8(),
-    [, D] = V6(),
+    D = p4(),
     [j, M] = Hz.default.useState([]),
     [P, V] = Hz.default.useState(!0),
     [N, T] = Hz.default.useState(!1),

@@@ class '$uA' (was 'pxA') — structural (96.3%)
--- pretty-v2.1.22.js:271868
+++ pretty-v2.1.23.js:272199
@@ -546,16 +546,22 @@
           this._cleanupTimeout(P),
           (S = this._transport) === null ||
             S === void 0 ||
-            S.send(
-              {
-                jsonrpc: "2.0",
-                method: "notifications/cancelled",
-                params: { requestId: P, reason: String(b) },
-              },
-              { relatedRequestId: Y, resumptionToken: z, onresumptiontoken: w },
-            ).catch((x) =>
-              this._onerror(Error(`Failed to send cancellation: ${x}`)),
-            ));
+            y
+              .send(
+                {
+                  jsonrpc: "2.0",
+                  method: "notifications/cancelled",
+                  params: { requestId: P, reason: String(x) },
+                },
+                {
+                  relatedRequestId: Y,
+                  resumptionToken: z,
+                  onresumptiontoken: w,
+                },
+              )
+              .catch((b) =>
+                this._onerror(Error(`Failed to send cancellation: ${b}`)),
+              ));
         let B = b instanceof DK ? b : new DK(Yq.RequestTimeout, String(b));
         X(B);
       };

@@@ function 'YIK' (was 'eRK') — structural (95.9%)
--- pretty-v2.1.22.js:552943
+++ pretty-v2.1.23.js:554258
@@ -1,6 +1,6 @@
 function eRK({ initialTeams: A, onDone: K }) {
   dC("teams-dialog");
-  let [, q] = V6(),
+  let q = p4(),
     Y = A?.[0]?.name ?? "",
     [z, w] = Bm.useState({ type: "teammateList", teamName: Y }),
     [H, J] = Bm.useState(0),
@@ -15,8 +15,7 @@
       if (z.type !== "teammateDetail") return null;
       return $.find((M) => M.name === z.memberName) ?? null;
     }, [z, $]),
-    [Z] = V6(),
-    G = Z.toolPermissionContext.isBypassPermissionsModeAvailable,
+    G = F1((j) => j.toolPermissionContext.isBypassPermissionsModeAvailable),
     W = () => {
       (w({ type: "teammateList", teamName: z.teamName }), J(0));
     },

@@@ function 'QPA' (was 'TPA') — structural (95.7%)
--- pretty-v2.1.22.js:477370
+++ pretty-v2.1.23.js:478011
@@ -26,8 +26,8 @@
   else P = K[2];
   let V = P,
     { setPreviewTheme: N, savePreview: T, cancelPreview: E } = _K6(),
-    [R, b] = V6(),
-    S = R.settings.syntaxHighlightingDisabled ?? !1;
+    R = F1(lx2) ?? !1,
+    x = p4();
   c51("ThemePicker");
   let B = BK("theme:toggleSyntaxHighlighting", "ThemePicker", "ctrl+t"),
     x;

@@@ variable 'b$8' (was 'QX8') — structural (95.6%)
--- pretty-v2.1.22.js:56538
+++ pretty-v2.1.23.js:56566
@@ -273,8 +273,7 @@
       },
       w = { match: _w(/\./, Fj(...db1)), relevance: 0 },
       H = db1.filter((YA) => typeof YA === "string").concat(["_|0"]),
-      J = db1
-        .filter((YA) => typeof YA !== "string")
+      J = Px1.filter((wA) => typeof wA !== "string")
         .concat(Wfq)
         .map(ib1),
       O = { variants: [{ className: "keyword", match: Fj(...J, ...pb1) }] },

@@@ function 'mn2' (was 'al2') — structural (95.5%)
--- pretty-v2.1.22.js:522271
+++ pretty-v2.1.23.js:523305
@@ -7,7 +7,7 @@
       isClaudeAISubscriber: w,
       isWSL: H,
     } = A,
-    [J] = V6(),
+    J = F1(pn2),
     [O, X] = mdA.useState(0),
     [$, _] = mdA.useState(z ?? !1),
     [Z, G] = mdA.useState(!1),
@@ -17,8 +17,7 @@
   else j = K[0];
   let M = j,
     P;
-  if (K[1] !== J.mcp.clients)
-    ((P = J.mcp.clients.find(Ai2)), (K[1] = J.mcp.clients), (K[2] = P));
+  if (K[1] !== J) ((P = J.find(Un2)), (K[1] = J), (K[2] = P));
   else P = K[2];
   let N = P?.type === "connected",
     T;

@@@ function 'Ly4' (was 'yR4') — structural (95.2%)
--- pretty-v2.1.22.js:193186
+++ pretty-v2.1.23.js:193358
@@ -55,6 +55,7 @@
   if (w.agentId) J.agent_id = w.agentId;
   if (w.parentSessionId) J.parent_session_id = w.parentSessionId;
   if (w.agentType) J.agent_type = w.agentType;
+  if (w.teamName) J.team_name = w.teamName;
   if (K.githubActionsMetadata) {
     let O = K.githubActionsMetadata;
     H.github_actions_metadata = {

@@@ function 'm1z' (was 'ce2') — structural (95.0%)
--- pretty-v2.1.22.js:543048
+++ pretty-v2.1.23.js:544141
@@ -9,7 +9,8 @@
   description: J,
 }) {
   let [O] = R4(),
-    [X, $] = V6(),
+    X = F1((AA) => AA.toolPermissionContext),
+    $ = p4(),
     _ = VCK({
       toolName: A.tool.name,
       toolInput: A.input,
@@ -48,10 +49,7 @@
       [],
     );
   BL(A, OA);
-  let WA = fX.useMemo(
-      () => wMA(X.toolPermissionContext),
-      [X.toolPermissionContext],
-    ),
+  let _A = LX.useMemo(() => NMA(X), [X]),
     a = fX.useMemo(
       () =>
         OCK({

@@@ variable 'Lt7' (was '$s7') — structural (94.8%)
--- pretty-v2.1.22.js:388559
+++ pretty-v2.1.23.js:389118
@@ -1,4 +1,5 @@
 var $s7 = C(() => {
+  I8();
   Xs7 = [
     "Accomplishing",
     "Actioning",

@@@ function 'HNK' (was 'zfK') — structural (94.8%)
--- pretty-v2.1.22.js:518276
+++ pretty-v2.1.23.js:519315
@@ -1,7 +1,7 @@
 function zfK({ tools: A, existingAgents: K, onComplete: q }) {
   let { wizardData: Y } = NH(),
     [z, w] = xe.useState(null),
-    [, H] = V6(),
+    H = p4(),
     J = xe.useCallback(
       async ($) => {
         if (!Y?.finalAgent) return;

@@@ function 'q0' (was 'K0') — structural (94.7%)
--- pretty-v2.1.22.js:466950
+++ pretty-v2.1.23.js:467470
@@ -2,73 +2,67 @@
   let q = new Set(K.map((w) => w.name)),
     Y = YI2(A),
     z = [];
-  return (
-    Y.filter((w) => {
-      if (w.type === "progress" || w.type === "system" || KI2(w)) return !1;
-      return !0;
-    }).forEach((w) => {
-      switch (w.type) {
-        case "user": {
-          let H = w;
-          if (!BU()) H = Pu6(w);
-          else H = zI2(w, q);
-          let J = oW(z);
-          if (J?.type === "user") {
-            z[z.indexOf(J)] = OI2(J, H);
-            return;
-          }
-          z.push(H);
+  (Y.filter((H) => {
+    if (H.type === "progress" || H.type === "system" || OS2(H)) return !1;
+    return !0;
+  }).forEach((H) => {
+    switch (H.type) {
+      case "user": {
+        let J = H;
+        if (!iU()) J = qB6(H);
+        else J = _S2(H, q);
+        let O = KD(z);
+        if (O?.type === "user") {
+          z[z.indexOf(O)] = DS2(O, J);
           return;
         }
-        case "assistant": {
-          let H = BU(),
-            J = {
-              ...w,
-              message: {
-                ...w.message,
-                content: w.message.content.map((O) => {
-                  if (O.type === "tool_use") {
-                    let X = K.find((_) => _.name === O.name),
-                      $ = X ? nzK(X, O.input) : O.input;
-                    if (H) return { ...O, input: $ };
-                    return {
-                      type: "tool_use",
-                      id: O.id,
-                      name: O.name,
-                      input: $,
-                    };
-                  }
-                  return O;
-                }),
-              },
-            };
-          for (let O = z.length - 1; O >= 0; O--) {
-            let X = z[O];
-            if (X.type !== "assistant" && !JI2(X)) break;
-            if (X.type === "assistant") {
-              if (X.message.id === J.message.id) {
-                z[O] = HI2(X, J);
-                return;
-              }
-              break;
+        z.push(J);
+        return;
+      }
+      case "assistant": {
+        let J = iU(),
+          O = {
+            ...H,
+            message: {
+              ...H.message,
+              content: H.message.content.map((X) => {
+                if (X.type === "tool_use") {
+                  let $ = K.find((G) => G.name === X.name),
+                    _ = $ ? swK($, X.input) : X.input;
+                  if (J) return { ...X, input: _ };
+                  return { type: "tool_use", id: X.id, name: X.name, input: _ };
+                }
+                return X;
+              }),
+            },
+          };
+        for (let X = z.length - 1; X >= 0; X--) {
+          let $ = z[X];
+          if ($.type !== "assistant" && !WS2($)) break;
+          if ($.type === "assistant") {
+            if ($.message.id === O.message.id) {
+              z[X] = ZS2($, O);
+              return;
             }
+            break;
           }
-          z.push(J);
-          return;
         }
-        case "attachment": {
-          let H = jI2(w.attachment),
-            J = oW(z);
-          if (J?.type === "user") {
-            z[z.indexOf(J)] = H.reduce((O, X) => wI2(O, X), J);
-            return;
-          }
-          z.push(...H);
+        z.push(O);
+        return;
+      }
+      case "attachment": {
+        let J = vS2(H.attachment),
+          O = KD(z);
+        if (O?.type === "user") {
+          z[z.indexOf(O)] = J.reduce((X, $) => GS2(X, $), O);
           return;
         }
+        z.push(...J);
+        return;
       }
-    }),
-    Y57(z),
-    PI2(z)
-  );
+    }
+  }),
+    O37(z));
+  let w = kS2(z);
+  return CS2(w);
 }

@@@ function 'em' (was 'Um') — structural (94.7%)
--- pretty-v2.1.22.js:571644
+++ pretty-v2.1.23.js:573353
@@ -26,6 +26,7 @@
   if (sH() && A.mcp !== K.mcp) {
     if ((NvK(A.mcp.clients, A.mcp.tools, A.mcp.resources), st())) VVA();
   }
+  if (A.queuedCommands !== K.queuedCommands) pr6(A.queuedCommands.length);
   if (A.settings !== K.settings)
     try {
       if ((KZ1(), qZ1(), A.settings.env !== K.settings.env)) ie();

@@@ variable 'Cs1' (was 'sa1') — structural (94.6%)
--- pretty-v2.1.22.js:130101
+++ pretty-v2.1.23.js:130125
@@ -14,10 +14,7 @@
             q?.debug(
               "@aws-sdk/credential-provider-ini - credential_source is EcsContainer",
             ),
-            async () =>
-              eCA
-                .chain(w(z ?? {}), H(z))()
-                .then(oa1)
+            async () => VLA.chain(w(z ?? {}), H(z))().then(Es1)
           );
         },
         Ec2InstanceMetadata: async (z) => {

@@@ function 'ok2' (was 'dE2') — structural (94.5%)
--- pretty-v2.1.22.js:451412
+++ pretty-v2.1.23.js:451587
@@ -11,7 +11,8 @@
   let z = q;
   if (z.length === 0) return !1;
   let w,
-    H = 0;
+    H = 0,
+    J = nk2();
   for (let [O] of Object.entries(PwK)) {
     let X = O.split(" ");
     if (z.length >= X.length) {

@@@ function 'lyK' (was 'URK') — structural (94.5%)
--- pretty-v2.1.22.js:552504
+++ pretty-v2.1.23.js:553799
@@ -1,6 +1,8 @@
 function URK({ messages: A, vimMode: K }) {
   let q = Pc.useRef(void 0),
-    [{ toolPermissionContext: Y, statusLineText: z }, w] = V6(),
+    Y = F1((_) => _.toolPermissionContext),
+    z = F1((_) => _.statusLineText),
+    w = p4(),
     H = tM(),
     J = Pc.useRef({
       messageId: null,

@@@ function 'WfK' (was 'ZVK') — structural (94.3%)
--- pretty-v2.1.22.js:514153
+++ pretty-v2.1.23.js:515189
@@ -30,8 +30,8 @@
     T = O.mode,
     E = "event" in O ? O.event : "PreToolUse",
     R = "matcher" in O ? O.matcher : null,
-    [b] = V6(),
-    { mcp: S } = b,
+    x = F1(el2),
+    y = D0(),
     B;
   if (K[3] !== S.tools || K[4] !== q)
     ((B = [...q, ...S.tools.map(Zc2)]),
@@ -42,7 +42,7 @@
   let x = B,
     F;
   if (K[6] !== b || K[7] !== x)
-    ((F = JVK(b, x)), (K[6] = b), (K[7] = x), (K[8] = F));
+    ((F = XfK(y.getState(), b)), (K[6] = y), (K[7] = b), (K[8] = F));
   else F = K[8];
   let Q = F,
     u;

@@@ function 'YLK' (was 'ACK') — structural (94.2%)
--- pretty-v2.1.22.js:540150
+++ pretty-v2.1.23.js:541226
@@ -8,8 +8,7 @@
   parseInput: H,
   operationType: J = "write",
 }) {
-  let [O] = V6(),
-    X = O.toolPermissionContext,
+  let O = F1((F) => F.toolPermissionContext),
     [$, _] = kP.useState(""),
     [Z, G] = kP.useState(""),
     [W, D] = kP.useState("yes"),

@@@ function 'rWK' (was 'iGK') — structural (94.2%)
--- pretty-v2.1.22.js:497261
+++ pretty-v2.1.23.js:498295
@@ -19,8 +19,8 @@
     [M, P] = KN.useState(null),
     [V, N] = KN.useState(null),
     [T, E] = KN.useState(!1),
-    [, R] = V6(),
     b = r8(),
+    x = n8(),
     S = w.type === "marketplace" && w.action === "add" && w.target !== void 0,
     B;
   if (K[5] !== R)

@@@ class 'S51' (was '$51') — structural (93.7%)
--- pretty-v2.1.22.js:176597
+++ pretty-v2.1.23.js:176656
@@ -52,8 +52,7 @@
           { x: X, y: $, width: _, height: Z } = O,
           G = Math.min($ + Z, this.height, J.height),
           W = Math.min(X + _, this.width, J.width);
-        for (let D = $; D < G; D++)
-          for (let j = X; j < W; j++) (UO4(K, J, j, D), q++);
+        (u04(K, J, X, $, W, Z), (q += (Z - $) * (W - X)));
       }
       if (H.type === "write") {
         let { text: J } = H,

@@@ variable 'QwK' (was 'BzK') — structural (93.6%)
--- pretty-v2.1.22.js:449098
+++ pretty-v2.1.23.js:449235
@@ -9,7 +9,6 @@
   y9();
   ZH();
   Pd();
-  h1();
   bzK = U.strictObject({
     type: U.enum(["message", "broadcast", "request", "response"]).describe(
       'Message type: "message" for DMs, "broadcast" to all teammates, "request" for protocol requests (shutdown, plan approval), "response" for protocol responses',
@@ -41,7 +40,7 @@
     },
     inputSchema: bzK,
     isEnabled() {
-      return D8() && OP1();
+      return b8();
     },
     isConcurrencySafe(A) {
       return !1;

@@@ function 'hUK' (was 'EQK') — structural (93.4%)
--- pretty-v2.1.22.js:573207
+++ pretty-v2.1.23.js:574928
@@ -133,7 +133,7 @@
     M = RKz(D, O, X.mcp.tools, j);
   if (J.permissionPromptToolName)
     W = W.filter((N) => N.name !== J.permissionPromptToolName);
-  zl6();
+  (il6(), await DH4());
   let P = [];
   for await (let N of CKz(
     O,

@@@ function 'QyK' (was 'BRK') — structural (93.0%)
--- pretty-v2.1.22.js:551983
+++ pretty-v2.1.23.js:553264
@@ -1,5 +1,5 @@
 function BRK() {
-  let [, A] = V6(),
+  let A = p4(),
     K = gVA.useRef(null),
     q = gVA.useCallback(async () => {
       let Y = await xRK();

@@@ function 'Pj2' (was 'XD2') — structural (92.7%)
--- pretty-v2.1.22.js:413027
+++ pretty-v2.1.23.js:413320
@@ -50,6 +50,7 @@
       isAsync: !1,
       querySource: "agent:custom",
       model: A.model,
+      availableTools: q.options.tools,
     })) {
       _.push(V);
       let N = e2([V]);

@@@ variable 'Fb6' (was 'zb6') — structural (92.5%)
--- pretty-v2.1.22.js:444979
+++ pretty-v2.1.23.js:445195
@@ -132,11 +132,7 @@
     },
     renderToolUseTag(A) {
       if (!A.task_id) return null;
-      return Q3.default.createElement(
-        I,
-        { flexWrap: "nowrap", marginLeft: 1 },
-        Q3.default.createElement(f, { dimColor: !0 }, A.task_id),
-      );
+      return w9.default.createElement(V, { dimColor: !0 }, " ", A.task_id);
     },
     renderToolUseProgressMessage(A) {
       let q = A[A.length - 1]?.data;

@@@ variable 'G31' (was 'l51') — structural (92.5%)
--- pretty-v2.1.22.js:181099
+++ pretty-v2.1.23.js:181153
@@ -22,6 +22,7 @@
           "ctrl+shift+o": "app:toggleTeammatePreview",
           "ctrl+r": "history:search",
           ...{},
+          ...{},
         },
       },
       {

@@@ function '_dA' (was 'ppA') — structural (92.2%)
--- pretty-v2.1.22.js:489379
+++ pretty-v2.1.23.js:490398
@@ -2,7 +2,7 @@
   let K = s(30),
     { server: q, onSelectTool: Y, onBack: z } = A,
     w = r8(),
-    [H] = V6(),
+    H = F1(xm2),
     J;
   A: {
     if (q.client.type !== "connected") {
@@ -14,11 +14,8 @@
       break A;
     }
     let P;
-    if (K[1] !== H.mcp.tools || K[2] !== q.name)
-      ((P = ru(H.mcp.tools, q.name)),
-        (K[1] = H.mcp.tools),
-        (K[2] = q.name),
-        (K[3] = P));
+    if (K[1] !== H || K[2] !== q.name)
+      ((P = YB(H, q.name)), (K[1] = H), (K[2] = q.name), (K[3] = P));
     else P = K[3];
     J = P;
   }

@@@ function 'sIK' (was 'oyK') — structural (92.1%)
--- pretty-v2.1.22.js:555709
+++ pretty-v2.1.23.js:556873
@@ -1,12 +1,13 @@
 function oyK({ inputValue: A, isAssistantResponding: K }) {
-  let [q, Y] = V6(),
+  let q = F1((D) => D.promptSuggestion),
+    Y = p4(),
     {
       text: z,
       promptId: w,
       shownAt: H,
       acceptedAt: J,
       generationRequestId: O,
-    } = q.promptSuggestion,
+    } = q,
     X = K || A.length > 0 ? null : z,
     $ = z && H > 0,
     _ = ScA.useCallback(() => {

@@@ function 'NM1' (was 'dj1') — structural (91.7%)
--- pretty-v2.1.22.js:389100
+++ pretty-v2.1.23.js:389671
@@ -1,6 +1,5 @@
 function dj1() {
-  let [A] = V6(),
-    { teamContext: K } = A,
+  let A = F1((q) => q.teamContext),
     [, q] = pj1.useState(0);
   if (
     (pj1.useEffect(() => {

@@@ function 'gV2' (was 'bP2') — structural (91.7%)
--- pretty-v2.1.22.js:426862
+++ pretty-v2.1.23.js:427084
@@ -22,6 +22,7 @@
     isAsync: !1,
     querySource: "agent:custom",
     model: A.model,
+    availableTools: Y.options.tools,
   }))
     if ((G.push(j), (j.type === "assistant" || j.type === "user") && H)) {
       let M = e2(G);

@@@ function 'o2K' (was 'pYK') — structural (91.5%)
--- pretty-v2.1.22.js:445541
+++ pretty-v2.1.23.js:445753
@@ -2,7 +2,7 @@
   let { plan: Y, filePath: z, pushToRemote: w, remoteSessionUrl: H } = A,
     J = !Y || Y.trim() === "",
     O = z ? M5(z) : "",
-    X = "awaitingLeaderApproval" in A && A.awaitingLeaderApproval;
+    X = A.awaitingLeaderApproval;
   if (J)
     return wK.createElement(
       I,

@@@ variable 'Nv' (was 'Tv') — structural (91.5%)
--- pretty-v2.1.22.js:415404
+++ pretty-v2.1.23.js:415727
@@ -15,7 +15,6 @@
   s1();
   z7();
   h1();
-  y9();
   n4K = U.strictObject({
     operation: U.enum([
       "spawnTeam",
@@ -78,7 +77,7 @@
     },
     inputSchema: n4K,
     isEnabled() {
-      return D8() && OP1();
+      return b8();
     },
     isConcurrencySafe(A) {
       return !1;

@@@ variable 'I$' (was 'L$') — structural (91.5%)
--- pretty-v2.1.22.js:449352
+++ pretty-v2.1.23.js:449479
@@ -4,6 +4,7 @@
       q = yd().filter((w) => !K.has(w.name)),
       Y = gMA(q, A);
     if (A.mode === "delegate") Y = Y.filter((w) => pzK.has(w.name));
+    if (A.mode === "coordinator") Y = Y.filter((w) => oZ1.has(w.name));
     if (j1(process.env.CLAUDE_REPL_MODE)) {
       if (Y.some((H) => H.name === A_1)) Y = Y.filter((H) => !EM6.has(H.name));
     }

@@@ variable 'VCK' (was 'jkK') — structural (91.4%)
--- pretty-v2.1.22.js:537937
+++ pretty-v2.1.23.js:539013
@@ -46,6 +46,7 @@
       "app:toggleTodos",
       "app:toggleTranscript",
       "app:toggleTeammatePreview",
+      "app:toggleTerminal",
       "history:search",
       "history:previous",
       "history:next",

@@@ function 'hyK' (was 'RRK') — structural (91.2%)
--- pretty-v2.1.22.js:551733
+++ pretty-v2.1.23.js:553008
@@ -1,8 +1,7 @@
 function RRK(A) {
   let K = s(14),
     { teamsSelected: q, showHint: Y } = A,
-    [z] = V6(),
-    { teamContext: w } = z,
+    z = F1(k8z),
     H;
   if (K[0] !== w)
     ((H = w ? Object.values(w.teammates).filter(P1z).length : 0),

@@@ function 'DW' (was 'GW') — structural (91.1%)
--- pretty-v2.1.22.js:339385
+++ pretty-v2.1.23.js:339887
@@ -146,9 +146,10 @@
         X + Aj
       );
     }
+    case "escape":
+      return A.text;
     case "def":
     case "del":
-    case "escape":
     case "html":
       return "";
   }

@@@ variable 'wb' (was 'oh') — structural (91.0%)
--- pretty-v2.1.22.js:31115
+++ pretty-v2.1.23.js:31136
@@ -39,6 +39,14 @@
         args: [],
       };
     })));
+  fz8 = class fz8 extends Error {
+    partialResults;
+    constructor(A, K) {
+      super(A);
+      this.partialResults = K;
+      this.name = "RipgrepTimeoutError";
+    }
+  };
   ioA = a1(async (A, K, q = []) => {
     if (sl.resolve(A) === sl.resolve(HWq())) return;
     try {

@@@ variable 'rU' (was 'gU') — structural (90.9%)
--- pretty-v2.1.22.js:530103
+++ pretty-v2.1.23.js:531167
@@ -272,6 +272,14 @@
       spinnerTipsEnabled: U.boolean()
         .optional()
         .describe("Whether to show tips in the spinner"),
+      spinnerVerbs: U.object({
+        mode: U.enum(["append", "replace"]),
+        verbs: U.array(U.string()),
+      })
+        .optional()
+        .describe(
+          'Customize spinner verbs. mode: "append" adds verbs to defaults, "replace" uses only your verbs.',
+        ),
       syntaxHighlightingDisabled: U.boolean()
         .optional()
         .describe("Whether to disable syntax highlighting in diffs"),

@@@ function 'Cm' (was 'jm') — structural (90.7%)
--- pretty-v2.1.22.js:476451
+++ pretty-v2.1.23.js:477069
@@ -20,5 +20,5 @@
           'Native installer: Set installMethod to "native" and disabled legacy auto-updater for protection',
         ));
   }
-  return { latestVersion: q, wasUpdated: Y.success, lockFailed: !1 };
+  return (xT1(), { latestVersion: q, wasUpdated: Y.success, lockFailed: !1 });
 }

@@@ function 'J$K' (was 'JXK') — structural (90.7%)
--- pretty-v2.1.22.js:472265
+++ pretty-v2.1.23.js:472869
@@ -3,7 +3,16 @@
       ...K.toolUseContext,
       options: { ...K.toolUseContext.options, maxThinkingTokens: 0 },
     },
-    Y = `<system-reminder>Answer this side question immediately without using any tools. Base your response only on what you already know from the conversation context.</system-reminder>
+    Y = `<system-reminder>This is a side question from the user. You must answer this question directly in a single response.
+
+CRITICAL CONSTRAINTS:
+- You have NO tools available - you cannot read files, run commands, search, or take any actions
+- This is a one-off response - there will be no follow-up turns
+- You can ONLY provide information based on what you already know from the conversation context
+- NEVER say things like "Let me try...", "I'll now...", "Let me check...", or promise to take any action
+- If you don't know the answer, say so - do not offer to look it up or investigate
+
+Simply answer the question with the information you have.</system-reminder>
 
 ${A}`,
     z = await kS({

@@@ variable 'Uf1' (was 'jf1') — structural (90.4%)
--- pretty-v2.1.22.js:451677
+++ pretty-v2.1.23.js:451853
@@ -342,6 +342,170 @@
           "--all": "none",
         },
       },
+      "git rev-parse": {
+        safeFlags: {
+          "--verify": "none",
+          "--short": "string",
+          "--abbrev-ref": "none",
+          "--symbolic": "none",
+          "--symbolic-full-name": "none",
+          "--show-toplevel": "none",
+          "--show-cdup": "none",
+          "--show-prefix": "none",
+          "--git-dir": "none",
+          "--git-common-dir": "none",
+          "--absolute-git-dir": "none",
+          "--show-superproject-working-tree": "none",
+          "--is-inside-work-tree": "none",
+          "--is-inside-git-dir": "none",
+          "--is-bare-repository": "none",
+          "--is-shallow-repository": "none",
+          "--is-shallow-update": "none",
+          "--path-prefix": "none",
+        },
+      },
+      "git rev-list": {
+        safeFlags: {
+          ...eUA,
+          ...uf1,
+          ...mf1,
+          ...kx6,
+          "--count": "none",
+          "--reverse": "none",
+          "--first-parent": "none",
+          "--ancestry-path": "none",
+          "--merges": "none",
+          "--no-merges": "none",
+          "--min-parents": "number",
+          "--max-parents": "number",
+          "--no-min-parents": "none",
+          "--no-max-parents": "none",
+          "--skip": "number",
+          "--max-age": "number",
+          "--min-age": "number",
+          "--walk-reflogs": "none",
+          "--oneline": "none",
+          "--abbrev-commit": "none",
+          "--pretty": "string",
+          "--format": "string",
+          "--abbrev": "number",
+          "--full-history": "none",
+          "--dense": "none",
+          "--sparse": "none",
+          "--source": "none",
+          "--graph": "none",
+        },
+      },
+      "git describe": {
+        safeFlags: {
+          "--tags": "none",
+          "--match": "string",
+          "--exclude": "string",
+          "--long": "none",
+          "--abbrev": "number",
+          "--always": "none",
+          "--contains": "none",
+          "--first-match": "none",
+          "--exact-match": "none",
+          "--candidates": "number",
+          "--dirty": "none",
+          "--broken": "none",
+        },
+      },
+      "git cat-file": {
+        safeFlags: {
+          "-t": "none",
+          "-s": "none",
+          "-p": "none",
+          "-e": "none",
+          "--batch-check": "none",
+          "--allow-undetermined-type": "none",
+        },
+      },
+      "git for-each-ref": {
+        safeFlags: {
+          "--format": "string",
+          "--sort": "string",
+          "--count": "number",
+          "--contains": "string",
+          "--no-contains": "string",
+          "--merged": "string",
+          "--no-merged": "string",
+          "--points-at": "string",
+        },
+      },
+      "git grep": {
+        safeFlags: {
+          "-e": "string",
+          "-E": "none",
+          "--extended-regexp": "none",
+          "-G": "none",
+          "--basic-regexp": "none",
+          "-F": "none",
+          "--fixed-strings": "none",
+          "-P": "none",
+          "--perl-regexp": "none",
+          "-i": "none",
+          "--ignore-case": "none",
+          "-v": "none",
+          "--invert-match": "none",
+          "-w": "none",
+          "--word-regexp": "none",
+          "-n": "none",
+          "--line-number": "none",
+          "-c": "none",
+          "--count": "none",
+          "-l": "none",
+          "--files-with-matches": "none",
+          "-L": "none",
+          "--files-without-match": "none",
+          "-h": "none",
+          "-H": "none",
+          "--heading": "none",
+          "--break": "none",
+          "--full-name": "none",
+          "--color": "none",
+          "--no-color": "none",
+          "-o": "none",
+          "--only-matching": "none",
+          "-A": "number",
+          "--after-context": "number",
+          "-B": "number",
+          "--before-context": "number",
+          "-C": "number",
+          "--context": "number",
+          "--and": "none",
+          "--or": "none",
+          "--not": "none",
+          "--max-depth": "number",
+          "--untracked": "none",
+          "--no-index": "none",
+          "--recurse-submodules": "none",
+          "--cached": "none",
+          "--threads": "number",
+          "-q": "none",
+          "--quiet": "none",
+        },
+      },
+      "git stash show": {
+        safeFlags: {
+          ...gf1,
+          ...ApA,
+          ...Ex6,
+          "--word-diff": "none",
+          "--word-diff-regex": "string",
+          "--diff-filter": "string",
+          "--abbrev": "number",
+        },
+      },
+      "git worktree list": {
+        safeFlags: {
+          "--porcelain": "none",
+          "-v": "none",
+          "--verbose": "none",
+          "--expire": "string",
+        },
+      },
       "git tag": {
         safeFlags: {
           "-l": "none",
@@ -1011,8 +1175,8 @@
           "--version": "none",
         },
       },
-    }),
-    (pE2 = ["echo", "printf", "wc", "grep", "head", "tail"]));
+    }));
+  rk2 = ["echo", "printf", "wc", "grep", "head", "tail"];
   ((lE2 = [
     "cal",
     "uptime",

@@@ function 'sLK' (was 'rCK') — structural (90.4%)
--- pretty-v2.1.22.js:546867
+++ pretty-v2.1.23.js:547885
@@ -4,8 +4,7 @@
     w = Jb6.safeParse(q.input),
     H = w.success ? w.data.questions || [] : [],
     J = w.success ? w.data.metadata?.source : void 0,
-    [O] = V6(),
-    X = O.toolPermissionContext.mode === "plan",
+    X = F1(V6z) === "plan",
     $;
   if (K[0] !== X) (($ = X ? SM() : void 0), (K[0] = X), (K[1] = $));
   else $ = K[1];

@@@ function '$NK' (was 'OfK') — structural (90.3%)
--- pretty-v2.1.22.js:518437
+++ pretty-v2.1.23.js:519476
@@ -1,5 +1,5 @@
 function OfK({ agent: A, tools: K, onSaved: q, onBack: Y }) {
-  let [, z] = V6(),
+  let z = p4(),
     [w, H] = SL.useState("menu"),
     [J, O] = SL.useState(0),
     [X, $] = SL.useState(null),

@@@ function 'UL' (was 'BL') — structural (90.3%)
--- pretty-v2.1.22.js:539903
+++ pretty-v2.1.23.js:540979
@@ -1,5 +1,5 @@
 function BL(A, K) {
-  let [, q] = V6();
+  let q = p4();
   rkK.useEffect(() => {
     (q((z) => ({
       ...z,

@@@ variable 'q5A' (was 'nqA') — structural (90.2%)
--- pretty-v2.1.22.js:318960
+++ pretty-v2.1.23.js:319386
@@ -11,6 +11,7 @@
   j8();
   QU();
   l6();
+  l6();
   As = class As extends Error {
     originalError;
     retryContext;

@@@ variable 'TT1' (was 'rN1') — structural (89.3%)
--- pretty-v2.1.22.js:475082
+++ pretty-v2.1.23.js:475698
@@ -10,6 +10,8 @@
   c2();
   lN1();
   PZ();
+  sD();
+  uxA();
   ((gh2 = {
     type: "local",
     name: "clear",

@@@ function 'EMA' (was 'OMA') — structural (89.2%)
--- pretty-v2.1.22.js:458735
+++ pretty-v2.1.23.js:459230
@@ -72,7 +72,7 @@
         Error(rC2)
       );
     let M = cx4(K.readFileState);
-    K.readFileState.clear();
+    (K.readFileState.clear(), He());
     let [P, V] = await Promise.all([tC2(M, K, cC2), KL2(K)]),
       N = [...P, ...V],
       T = eC2(K.agentId ?? F1());
@@ -110,16 +110,19 @@
           isVisibleInTranscriptOnly: !0,
         }),
       ];
-    return {
-      boundaryMarker: x,
-      summaryMessages: Q,
-      attachments: N,
-      hookResults: b,
-      userDisplayMessage: _,
-      preCompactTokenCount: H,
-      postCompactTokenCount: S,
-      compactionUsage: B,
-    };
+    return (
+      o57(K.options.querySource ?? "compact"),
+      {
+        boundaryMarker: b,
+        summaryMessages: Q,
+        attachments: N,
+        hookResults: x,
+        userDisplayMessage: _,
+        preCompactTokenCount: H,
+        postCompactTokenCount: y,
+        compactionUsage: B,
+      }
+    );
   } catch (H) {
     throw (oC2(H, K), H);
   } finally {

@@@ function 'aJ1' (was 'IJ1') — structural (88.9%)
--- pretty-v2.1.22.js:265438
+++ pretty-v2.1.23.js:265615
@@ -16,10 +16,12 @@
     : K.map((Y) => Y.name).join(`
 `);
   if (Qo !== void 0 && q !== Qo) {
-    let Y = Qo.split(
-        `
+    let Y = oo
+        .split(
+          `
 `,
-      ).filter(Boolean).length,
+        )
+        .filter(Boolean).length,
       z = q
         .split(
           `

@@@ function 'ULK' (was 'gCK') — structural (88.8%)
--- pretty-v2.1.22.js:545494
+++ pretty-v2.1.23.js:546509
@@ -1,7 +1,7 @@
 function gCK(A) {
   let K = s(18),
     { toolUseConfirm: q, onDone: Y, onReject: z, workerBadge: w } = A,
-    [H] = V6(),
+    H = F1(X6z),
     J;
   if (K[0] !== H || K[1] !== Y || K[2] !== z || K[3] !== q)
     ((J = function (P) {
@@ -10,7 +10,7 @@
           interviewPhaseEnabled: y$(),
           entryMethod: "tool",
         }),
-          Ih(H.toolPermissionContext.mode, "plan"),
+          Qh(H, "plan"),
           Y(),
           q.onAllow({}, [
             { type: "setMode", mode: "plan", destination: "session" },

@@@ function 'ev1' (was 'Ev1') — structural (88.4%)
--- pretty-v2.1.22.js:509047
+++ pretty-v2.1.23.js:510078
@@ -1,5 +1,7 @@
 function Ev1({ onDone: A, onForegroundTask: K, toolUseContext: q }) {
-  let [{ tasks: Y, foregroundedTaskId: z }, w] = V6(),
+  let Y = F1((F) => F.tasks),
+    z = F1((F) => F.foregroundedTaskId),
+    w = p4(),
     H = Y,
     J = uK.useRef(!1),
     [O, X] = d9A.useState(() => {
@@ -313,14 +315,6 @@
                     return uK.default.createElement(
                       uK.default.Fragment,
                       null,
-                      F.map((l) => {
-                        let e = o++;
-                        return uK.default.createElement(ydA, {
-                          key: l.id,
-                          item: l,
-                          isSelected: e === $,
-                        });
-                      }),
                       d.map(([l, e]) => {
                         let wA = e.length + F.length;
                         return uK.default.createElement(
@@ -344,6 +338,14 @@
                               isSelected: OA === $,
                             });
                           }),
+                          YA.map((qA) => {
+                            let HA = r++;
+                            return FK.default.createElement(edA, {
+                              key: qA.id,
+                              item: qA,
+                              isSelected: HA === $,
+                            });
+                          }),
                         );
                       }),
                     );

@@@ function '$dA' (was 'UpA') — structural (88.3%)
--- pretty-v2.1.22.js:488629
+++ pretty-v2.1.23.js:489647
@@ -8,7 +8,7 @@
 }) {
   let [H] = R4(),
     J = r8(),
-    [O] = V6(),
+    O = F1((M) => M.mcp),
     X = bPA(),
     $ = _e(),
     [_, Z] = pq.useState(!1),
@@ -23,7 +23,7 @@
       }
     }, [A.client.type, A.name, $, Y, z]),
     W = String(A.name).charAt(0).toUpperCase() + String(A.name).slice(1),
-    D = q$1(O.mcp.commands, A.name).length,
+    D = v$1(O.commands, A.name).length,
     j = [];
   if (A.client.type !== "disabled" && K > 0)
     j.push({ label: "View tools", value: "tools" });
@@ -141,7 +141,7 @@
           pq.default.createElement(ET1, {
             serverToolsCount: K,
             serverPromptsCount: D,
-            serverResourcesCount: O.mcp.resources[A.name]?.length || 0,
+            serverResourcesCount: O.resources[A.name]?.length || 0,
           }),
         A.client.type === "connected" &&
           K > 0 &&

@@@ function 'nk1' (was 'Mk1') — structural (88.3%)
--- pretty-v2.1.22.js:559601
+++ pretty-v2.1.23.js:561222
@@ -40,9 +40,7 @@
         (wA) =>
           wA.immediate &&
           wA.isEnabled() &&
-          (wA.name === o ||
-            wA.aliases?.includes(o) ||
-            wA.userFacingName() === o),
+          (e.name === r || e.aliases?.includes(r) || e.userFacingName() === r),
       );
     if (e && e.type === "local-jsx") {
       (H(""), R(0), b());

@@@ function 'gRK' (was 'uLK') — structural (88.1%)
--- pretty-v2.1.22.js:548909
+++ pretty-v2.1.23.js:549929
@@ -22,8 +22,7 @@
   let D = W,
     j = TLK(D),
     M = bVA(_),
-    [P] = V6(),
-    { notifications: V } = P,
+    P = F1(y6z),
     { addNotification: N, removeNotification: T } = iK(),
     E = po(),
     b =
@@ -219,7 +218,12 @@
       null,
       z3.createElement(
         I,
-        { flexDirection: "column", alignItems: "flex-end" },
+        {
+          flexDirection: "column",
+          alignItems: "flex-end",
+          flexShrink: 1,
+          overflowX: "hidden",
+        },
         e,
         wA,
         HA,

@@@ function 'gd' (was 'Sd') — structural (87.7%)
--- pretty-v2.1.22.js:459783
+++ pretty-v2.1.23.js:460298
@@ -112,7 +112,10 @@
     }),
       aMA());
     let W = HJK(Y ? "manual" : "auto", O, X, Array.from($), Array.from(Z));
-    return { messages: G, compactionInfo: { boundaryMessage: W } };
+    return (
+      r57(q?.options.querySource ?? "repl_main_thread"),
+      { messages: Z, compactionInfo: { boundaryMessage: W } }
+    );
   }
   return { messages: G };
 }

@@@ function 'mK' (was 'iK') — structural (87.7%)
--- pretty-v2.1.22.js:470239
+++ pretty-v2.1.23.js:470840
@@ -1,5 +1,6 @@
 function iK() {
-  let [A, K] = V6(),
+  let A = F1((w) => w.notifications.queue.length),
+    K = p4(),
     q = _PA.useCallback(() => {
       K((w) => {
         let H = dI2(w.notifications.queue);
@@ -112,7 +113,7 @@
     );
   return (
     _PA.useEffect(() => {
-      if (A.notifications.queue.length > 0) q();
+      if (A > 0) q();
     }, []),
     { addNotification: Y, removeNotification: z }
   );

@@@ function '_c6' (was 'vd6') — structural (87.6%)
--- pretty-v2.1.22.js:571051
+++ pretty-v2.1.23.js:572761
@@ -25,8 +25,7 @@
     let J = H,
       X = {
         ddsource: "nodejs",
-        ddtags: n7z
-          .filter(($) => J[$] !== void 0 && J[$] !== null)
+        ddtags: W5z.filter(($) => J[$] !== void 0 && J[$] !== null)
           .map(($) => `${TFK($)}:${J[$]}`)
           .join(","),
         message: A,

@@@ function 'jXK' (was 'P0K') — structural (87.3%)
--- pretty-v2.1.22.js:469906
+++ pretty-v2.1.23.js:470457
@@ -22,6 +22,9 @@
   let _ = K2("tengu_disable_bypass_permissions_mode"),
     Z = O8() || {},
     G = Z.permissions?.disableBypassPermissionsMode === "disable",
+    W = (Y === "bypassPermissions" || z) && !_ && !Z,
+    D = JA1(),
+    j = [],
     D = f0K(
       {
         mode: Y,
@@ -29,10 +32,9 @@
         alwaysAllowRules: { cliArg: H },
         alwaysDenyRules: { cliArg: J },
         alwaysAskRules: {},
-        isBypassPermissionsModeAvailable:
-          (Y === "bypassPermissions" || z) && !_ && !G,
+        isBypassPermissionsModeAvailable: W,
       },
-      deA(),
+      D,
     ),
     j = [...(Z.permissions?.additionalDirectories || []), ...w];
   for (let M of j) {
@@ -49,5 +51,5 @@
     )
       O.push(GpA(P));
   }
-  return { toolPermissionContext: D, warnings: O };
+  return { toolPermissionContext: M, warnings: O, dangerousPermissions: j };
 }

@@@ function 'UPA' (was 'vPA') — structural (87.2%)
--- pretty-v2.1.22.js:477696
+++ pretty-v2.1.23.js:478340
@@ -59,7 +59,7 @@
   else S = K[13];
   let B = S,
     x;
-  if (K[14] !== G) ((x = !1), (K[14] = G), (K[15] = x));
+  if (K[14] !== Z) ((b = Xs() && g_K(Z)), (K[14] = Z), (K[15] = b));
   else x = K[15];
   let F = x,
     Q;
@@ -89,17 +89,21 @@
   else l = K[22];
   let e;
   if (K[23] === Symbol.for("react.memo_cache_sentinel"))
-    ((e = { context: "ModelPicker", isActive: !1 }), (K[23] = e));
+    ((YA = { context: "ModelPicker", isActive: Xs() }), (K[23] = YA));
   else e = K[23];
   O7(l, e);
   let wA;
   if (K[24] !== X || K[25] !== _ || K[26] !== z)
     ((wA = function (LA) {
+      if (Xs())
+        (n("tengu_model_command_menu_effort", { effort: X }),
+          v4("userSettings", { effortLevel: X === "high" ? void 0 : X }));
       if (LA === mB6) {
         z(null, void 0);
         return;
       }
-      z(LA, void 0);
+      let fA = Xs() && _ && g_K(RA) ? X : void 0;
+      z(RA, fA);
     }),
       (K[24] = X),
       (K[25] = _),
@@ -214,7 +218,36 @@
   else YA = K[47];
   let JA;
   if (K[48] !== X || K[49] !== B || K[50] !== F)
-    ((JA = !1), (K[48] = X), (K[49] = B), (K[50] = F), (K[51] = JA));
+    ((GA =
+      Xs() &&
+      EK.createElement(
+        S,
+        { marginBottom: 1, flexDirection: "column" },
+        F
+          ? EK.createElement(
+              V,
+              { dimColor: !0 },
+              EK.createElement(F_K, { effort: X }),
+              " ",
+              ng(X),
+              " ",
+              "effort",
+              X === "high" ? " (default)" : "",
+              " ",
+              EK.createElement(V, { color: "subtle" }, "← → to adjust"),
+            )
+          : EK.createElement(
+              V,
+              { color: "subtle" },
+              EK.createElement(F_K, { effort: void 0 }),
+              " Effort not supported",
+              B ? ` for ${B}` : "",
+            ),
+      )),
+      (K[48] = X),
+      (K[49] = B),
+      (K[50] = F),
+      (K[51] = GA));
   else JA = K[51];
   let AA;
   if (K[52] !== PA || K[53] !== YA || K[54] !== JA)

@@@ function 'OL2' (was 'qC2') — structural (87.1%)
--- pretty-v2.1.22.js:457670
+++ pretty-v2.1.23.js:458132
@@ -20,6 +20,7 @@
       jH("changed_files", () => VC2(J)),
       jH("nested_memory", () => fC2(J)),
       jH("dynamic_skill", () => NC2(J)),
+      xw("skill_listing", () => RL2(J)),
       jH("ultra_claude_md", async () => ZC2(z)),
       jH("plan_mode", () => HC2(z, K)),
       jH("plan_mode_exit", () => JC2(K)),
@@ -39,8 +40,8 @@
           jH("ide_selection", async () => GC2(q, K)),
           jH("ide_opened_file", async () => DC2(q, K)),
           jH("output_style", async () => Promise.resolve(_C2())),
-          jH("diagnostics", async () => RC2()),
-          jH("lsp_diagnostics", async () => yC2()),
+          xw("diagnostics", async () => uL2(K)),
+          xw("lsp_diagnostics", async () => BL2(K)),
           jH("unified_tasks", async () => uC2(K, z)),
           jH("async_hook_responses", async () => BC2()),
           jH("token_usage", async () => Promise.resolve(FC2(z ?? []))),

@@@ function 'IVK' (was 'RPK') — structural (87.0%)
--- pretty-v2.1.22.js:511265
+++ pretty-v2.1.23.js:512298
@@ -6,8 +6,8 @@
   if (K[0] === Symbol.for("react.memo_cache_sentinel")) ((w = []), (K[0] = w));
   else w = K[0];
   let [H, J] = Ac.useState(w),
-    [O, X] = V6(),
-    { toolPermissionContext: $ } = O,
+    O = F1(hl2),
+    X = p4(),
     _ = vD(),
     [Z, G] = Ac.useState(),
     [W, D] = Ac.useState(),

@@@ variable 'WSA' (was 'DXA') — structural (86.9%)
--- pretty-v2.1.22.js:179052
+++ pretty-v2.1.23.js:203806
@@ -49,11 +49,11 @@
   );
   n5(
     "PRERELEASEIDENTIFIER",
-    `(?:${L7[R7.NONNUMERICIDENTIFIER]}|${L7[R7.NUMERICIDENTIFIER]})`,
+    `(?:${L7[R7.NUMERICIDENTIFIER]}|${L7[R7.NONNUMERICIDENTIFIER]})`,
   );
   n5(
     "PRERELEASEIDENTIFIERLOOSE",
-    `(?:${L7[R7.NONNUMERICIDENTIFIER]}|${L7[R7.NUMERICIDENTIFIERLOOSE]})`,
+    `(?:${L7[R7.NUMERICIDENTIFIERLOOSE]}|${L7[R7.NONNUMERICIDENTIFIER]})`,
   );
   n5(
     "PRERELEASE",

@@@ class 'MUK' (was '$QK') — structural (86.8%)
--- pretty-v2.1.22.js:572516
+++ pretty-v2.1.23.js:574226
@@ -195,9 +195,9 @@
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.22",
+          VERSION: "2.1.23",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-01-28T06:33:34Z",
+          BUILD_TIME: "2026-01-29T00:18:20Z",
         }.VERSION,
         output_style: AA,
         agents: N.map((oA) => oA.agentType),
@@ -410,7 +410,7 @@
             subtype: "error_max_structured_output_retries",
             duration_ms: Date.now() - b,
             duration_api_ms: DE(),
-            is_error: !1,
+            is_error: !0,
             num_turns: XA,
             session_id: F1(),
             total_cost_usd: $G(),

@@@ function 'Lb' (was 'jb') — structural (86.8%)
--- pretty-v2.1.22.js:89718
+++ pretty-v2.1.23.js:89740
@@ -29,7 +29,10 @@
       );
       let Y = (N4(A.destination)?.permissions || {})[A.behavior] || [],
         z = new Set(A.rules.map(n9)),
-        w = Y.filter((H) => !z.has(H));
+        w = Y.filter((H) => {
+          let J = I9(GV(H));
+          return !z.has(J);
+        });
       C4(A.destination, { permissions: { [A.behavior]: w } });
       break;
     }

@@@ function 'aBA' (was 'RBA') — structural (86.6%)
--- pretty-v2.1.22.js:308645
+++ pretty-v2.1.23.js:308974
@@ -8,7 +8,9 @@
     for (let H of w) {
       let J = IW7(H);
       if (!J) continue;
-      if (r6() !== "wsl" && W$() && (!J.pid || !UCY(J.pid))) continue;
+      if (o6() !== "wsl" && M$()) {
+        if (!(J.pid ? await eLY(J.pid) : !1)) continue;
+      }
       let O = !1;
       if (process.env.CLAUDE_CODE_IDE_SKIP_VALID_CHECK === "true") O = !0;
       else if (J.port === Y) O = !0;

@@@ function 'zR2' (was 'sC2') — structural (86.6%)
--- pretty-v2.1.22.js:458885
+++ pretty-v2.1.23.js:459383
@@ -18,7 +18,23 @@
           maxOutputTokens: JnA,
         }),
         $ = pf(X.messages);
-      if ($ && Xm($)) return $;
+      if ($ && Vm($))
+        return (
+          n("tengu_compact_cache_sharing_success", {
+            preCompactTokenCount: z,
+            outputTokens: X.totalUsage.output_tokens,
+            cacheReadInputTokens: X.totalUsage.cache_read_input_tokens,
+            cacheCreationInputTokens: X.totalUsage.cache_creation_input_tokens,
+            cacheHitRate:
+              X.totalUsage.cache_read_input_tokens > 0
+                ? X.totalUsage.cache_read_input_tokens /
+                  (X.totalUsage.cache_read_input_tokens +
+                    X.totalUsage.cache_creation_input_tokens +
+                    X.totalUsage.input_tokens)
+                : 0,
+          }),
+          $
+        );
       (h(
         `Compact cache sharing: no text in response, falling back. Response: ${QA($)}`,
         { level: "warn" },

@@@ variable 'xG' (was 'IZ') — structural (86.5%)
--- pretty-v2.1.22.js:463001
+++ pretty-v2.1.23.js:463517
@@ -209,7 +209,6 @@
       return await mI6(A, K);
     },
     renderToolUseMessage: I4K,
-    renderToolUseTag: S4K,
     renderToolUseRejectedMessage: h4K,
     renderToolUseProgressMessage: b4K,
     renderToolUseQueuedMessage: x4K,
@@ -303,6 +302,7 @@
                 fullOutput: wA.fullOutput,
                 elapsedTimeSeconds: wA.elapsedTimeSeconds,
                 totalLines: wA.totalLines,
+                timeoutMs: e.timeoutMs,
               },
             });
           }
@@ -327,7 +327,10 @@
             (_.clear(), _.append(qN1(HA)));
           }
         }
-        let e = I8.annotateStderrWithSandboxFailures(A.command, D.stderr || "");
+        let YA = S8.annotateStderrWithSandboxFailures(
+          A.command,
+          D.stderr || "",
+        );
         if (Z.isError) throw new vR(D.stdout, e, D.code, D.interrupted);
         W = D.interrupted;
       } finally {

@@@ function 'Ag6' (was 'Mm6') — structural (86.0%)
--- pretty-v2.1.22.js:490362
+++ pretty-v2.1.23.js:491385
@@ -2,17 +2,17 @@
   let K = s(25),
     { serverName: q, onComplete: Y } = A,
     [z] = R4(),
-    [w] = V6(),
+    w = F1(Fm2),
     H = bPA(),
     [J, O] = cpA.useState(!0),
     [X, $] = cpA.useState(null),
     _,
     Z;
-  if (K[0] !== w.mcp.clients || K[1] !== Y || K[2] !== H || K[3] !== q)
+  if (K[0] !== w || K[1] !== Y || K[2] !== H || K[3] !== q)
     ((_ = () => {
       (async function () {
         try {
-          if (!w.mcp.clients.find((M) => M.name === q)) {
+          if (!w.find((M) => M.name === q)) {
             ($(`MCP server "${q}" not found`), O(!1));
             return;
           }
@@ -46,8 +46,8 @@
         }
       })();
     }),
-      (Z = [q, H, w.mcp.clients, Y]),
-      (K[0] = w.mcp.clients),
+      (G = [q, H, w, Y]),
+      (K[0] = w),
       (K[1] = Y),
       (K[2] = H),
       (K[3] = q),

@@@ variable 'Z4A' (was 'Y4A') — structural (85.8%)
--- pretty-v2.1.22.js:175302
+++ pretty-v2.1.23.js:175349
@@ -34,6 +34,7 @@
       success: "rgb(44,122,57)",
       error: "rgb(171,43,63)",
       warning: "rgb(150,108,30)",
+      merged: "rgb(135,0,255)",
       warningShimmer: "rgb(200,158,80)",
       diffAdded: "rgb(105,219,124)",
       diffRemoved: "rgb(255,168,180)",
@@ -84,6 +85,7 @@
       success: "ansi:green",
       error: "ansi:red",
       warning: "ansi:yellow",
+      merged: "ansi:magenta",
       warningShimmer: "ansi:yellowBright",
       diffAdded: "ansi:green",
       diffRemoved: "ansi:red",
@@ -134,6 +136,7 @@
       success: "ansi:greenBright",
       error: "ansi:redBright",
       warning: "ansi:yellowBright",
+      merged: "ansi:magentaBright",
       warningShimmer: "ansi:yellowBright",
       diffAdded: "ansi:green",
       diffRemoved: "ansi:red",
@@ -184,6 +187,7 @@
       success: "rgb(0,102,153)",
       error: "rgb(204,0,0)",
       warning: "rgb(255,153,0)",
+      merged: "rgb(135,0,255)",
       warningShimmer: "rgb(255,183,50)",
       diffAdded: "rgb(153,204,255)",
       diffRemoved: "rgb(255,204,204)",
@@ -234,6 +238,7 @@
       success: "rgb(78,186,101)",
       error: "rgb(255,107,128)",
       warning: "rgb(255,193,7)",
+      merged: "rgb(175,135,255)",
       warningShimmer: "rgb(255,223,57)",
       diffAdded: "rgb(34,92,43)",
       diffRemoved: "rgb(122,41,54)",
@@ -284,6 +289,7 @@
       success: "rgb(51,153,255)",
       error: "rgb(255,102,102)",
       warning: "rgb(255,204,0)",
+      merged: "rgb(175,135,255)",
       warningShimmer: "rgb(255,234,50)",
       diffAdded: "rgb(0,68,102)",
       diffRemoved: "rgb(102,0,0)",

@@@ function 'p9A' (was 'R9A') — structural (85.8%)
--- pretty-v2.1.22.js:488862
+++ pretty-v2.1.23.js:489880
@@ -10,7 +10,8 @@
     J = r8(),
     [O, X] = b4.default.useState(!1),
     [$, _] = b4.default.useState(null),
-    [Z, G] = V6(),
+    G = F1((AA) => AA.mcp),
+    Z = p4(),
     [W, D] = b4.default.useState(null),
     [j, M] = b4.useState(!1),
     [P, V] = b4.useState(null),
@@ -104,7 +105,7 @@
       }
     }));
   let HA = String(A.name).charAt(0).toUpperCase() + String(A.name).slice(1),
-    OA = q$1(Z.mcp.commands, A.name).length,
+    HA = v$1(G.commands, A.name).length,
     WA = _e(),
     a = b4.default.useCallback(async () => {
       let qA = C7(),
@@ -382,7 +383,7 @@
           b4.default.createElement(ET1, {
             serverToolsCount: K,
             serverPromptsCount: OA,
-            serverResourcesCount: Z.mcp.resources[A.name]?.length || 0,
+            serverResourcesCount: G.resources[A.name]?.length || 0,
           }),
         A.client.type === "connected" &&
           K > 0 &&

@@@ function 'i_K' (was 'c$K') — structural (85.0%)
--- pretty-v2.1.22.js:478459
+++ pretty-v2.1.23.js:479171
@@ -26,15 +26,11 @@
     ),
     x = b,
     F = vD(),
-    [
-      {
-        mainLoopModel: Q,
-        verbose: u,
-        thinkingEnabled: d,
-        promptSuggestionEnabled: o,
-      },
-      l,
-    ] = V6(),
+    Q = F1((fA) => fA.mainLoopModel),
+    u = F1((fA) => fA.verbose),
+    d = F1((fA) => fA.thinkingEnabled),
+    r = F1((fA) => fA.promptSuggestionEnabled),
+    c = p4(),
     [e, wA] = _P.useState({}),
     HA = K6.useRef(d),
     [OA, WA] = _P.useState(!1),
@@ -608,6 +604,10 @@
           return;
       }
     if (VA.id === "autoUpdatesChannel") {
+      if (GA) {
+        (JA(6), q(!0));
+        return;
+      }
       if ((G?.autoUpdatesChannel ?? "latest") === "latest") (_A(4), q(!0));
       else
         (C4("userSettings", {
@@ -627,7 +627,7 @@
       VA.onChange(VA.options[CA]);
       return;
     }
-  }, [kA, E, G?.autoUpdatesChannel, q, z, Y]);
+  }, [GA, VA, C, Z?.autoUpdatesChannel, q, z, Y]);
   return (
     O7(
       {
@@ -841,134 +841,174 @@
                       ),
                     ),
                   )
-                : a === 4
-                  ? K6.createElement(F$K, {
-                      currentVersion: {
-                        ISSUES_EXPLAINER:
-                          "report the issue at https://github.com/anthropics/claude-code/issues",
-                        PACKAGE_URL: "@anthropic-ai/claude-code",
-                        README_URL: "https://code.claude.com/docs/en/overview",
-                        VERSION: "2.1.22",
-                        FEEDBACK_CHANNEL:
-                          "https://github.com/anthropics/claude-code/issues",
-                        BUILD_TIME: "2026-01-28T06:33:34Z",
-                      }.VERSION,
-                      onChoice: (VA) => {
-                        if ((_A(null), q(!1), VA === "cancel")) return;
-                        let EA = { autoUpdatesChannel: "stable" };
-                        if (VA === "stay")
-                          EA.minimumVersion = {
-                            ISSUES_EXPLAINER:
-                              "report the issue at https://github.com/anthropics/claude-code/issues",
-                            PACKAGE_URL: "@anthropic-ai/claude-code",
-                            README_URL:
-                              "https://code.claude.com/docs/en/overview",
-                            VERSION: "2.1.22",
-                            FEEDBACK_CHANNEL:
-                              "https://github.com/anthropics/claude-code/issues",
-                            BUILD_TIME: "2026-01-28T06:33:34Z",
-                          }.VERSION;
-                        (C4("userSettings", EA),
-                          W((CA) => ({ ...CA, ...EA })),
-                          n("tengu_autoupdate_channel_changed", {
-                            channel: "stable",
-                            minimum_version_set: VA === "stay",
-                          }));
+                : a === 6
+                  ? o1.createElement(
+                      L4,
+                      {
+                        title: "Enable Auto-Updates",
+                        onCancel: () => {
+                          (JA(null), q(!1));
+                        },
+                        hideBorder: !0,
+                        hideInputGuide: !0,
                       },
-                    })
-                  : K6.createElement(
-                      I,
-                      { flexDirection: "column", marginY: 1, gap: 1 },
-                      K6.createElement(
-                        f,
-                        null,
-                        "Configure Claude Code preferences",
-                      ),
-                      K6.createElement(dS, {
-                        query: jA,
-                        isFocused: x,
-                        isTerminalFocused: F,
-                        cursorOffset: SA,
-                        placeholder: "Search settings...",
-                      }),
-                      K6.createElement(
-                        I,
-                        { flexDirection: "column" },
-                        kA.length === 0
-                          ? K6.createElement(
+                      GA !== "config"
+                        ? o1.createElement(
+                            o1.Fragment,
+                            null,
+                            o1.createElement(
+                              V,
                               f,
-                              { dimColor: !0, italic: !0 },
-                              'No settings match "',
+                              "Auto-updates are controlled by an environment variable and cannot be changed here.",
+                            ),
+                            o1.createElement(
                               jA,
-                              '"',
-                            )
-                          : kA.map((VA, EA) => {
-                              let CA = EA === E;
-                              return K6.createElement(
-                                K6.Fragment,
-                                { key: VA.id },
-                                K6.createElement(
-                                  I,
-                                  null,
+                              { dimColor: !0 },
+                              "Unset",
+                              " ",
+                              GA?.includes("NONESSENTIAL")
+                                ? "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
+                                : "DISABLE_AUTOUPDATER",
+                              " ",
+                              "to re-enable auto-updates.",
+                            ),
+                          )
+                        : o1.createElement(E6, {
+                            options: [
+                              {
+                                label: "Enable with latest channel",
+                                value: "latest",
+                              },
+                              {
+                                label: "Enable with stable channel",
+                                value: "stable",
+                              },
+                            ],
+                            onChange: (fA) => {
+                              (JA(null),
+                                q(!1),
+                                D6((LA) => ({ ...LA, autoUpdates: !0 })),
+                                X({ ...M1(), autoUpdates: !0 }),
+                                v4("userSettings", {
+                                  autoUpdatesChannel: fA,
+                                  minimumVersion: void 0,
+                                }),
+                                W((LA) => ({
+                                  ...LA,
+                                  autoUpdatesChannel: fA,
+                                  minimumVersion: void 0,
+                                })),
+                                n("tengu_autoupdate_enabled", { channel: fA }));
+                            },
+                          }),
+                    )
+                  : a === 4
+                    ? o1.createElement(U_K, {
+                        currentVersion: {
+                          ISSUES_EXPLAINER:
+                            "report the issue at https://github.com/anthropics/claude-code/issues",
+                          PACKAGE_URL: "@anthropic-ai/claude-code",
+                          README_URL:
+                            "https://code.claude.com/docs/en/overview",
+                          VERSION: "2.1.23",
+                          FEEDBACK_CHANNEL:
+                            "https://github.com/anthropics/claude-code/issues",
+                          BUILD_TIME: "2026-01-29T00:18:20Z",
+                        }.VERSION,
+                        onChoice: (fA) => {
+                          if ((JA(null), q(!1), fA === "cancel")) return;
+                          let LA = { autoUpdatesChannel: "stable" };
+                          if (fA === "stay")
+                            LA.minimumVersion = {
+                              ISSUES_EXPLAINER:
+                                "report the issue at https://github.com/anthropics/claude-code/issues",
+                              PACKAGE_URL: "@anthropic-ai/claude-code",
+                              README_URL:
+                                "https://code.claude.com/docs/en/overview",
+                              VERSION: "2.1.23",
+                              FEEDBACK_CHANNEL:
+                                "https://github.com/anthropics/claude-code/issues",
+                              BUILD_TIME: "2026-01-29T00:18:20Z",
+                            }.VERSION;
+                          (v4("userSettings", LA),
+                            W((SA) => ({ ...SA, ...LA })),
+                            n("tengu_autoupdate_channel_changed", {
+                              channel: "stable",
+                              minimum_version_set: fA === "stay",
+                            }));
+                        },
+                      })
+                    : o1.createElement(
+                        S,
+                        { flexDirection: "column", marginY: 1, gap: 1 },
+                        o1.createElement(
+                          V,
+                          null,
+                          "Configure Claude Code preferences",
+                        ),
+                        o1.createElement(tS, {
+                          query: jA,
+                          isFocused: b,
+                          isTerminalFocused: F,
+                          cursorOffset: hA,
+                          placeholder: "Search settings...",
+                        }),
+                        o1.createElement(
+                          S,
+                          { flexDirection: "column" },
+                          VA.length === 0
+                            ? o1.createElement(
+                                V,
+                                { dimColor: !0, italic: !0 },
+                                'No settings match "',
+                                jA,
+                                '"',
+                              )
+                            : VA.map((fA, LA) => {
+                                let SA = LA === C;
+                                return o1.createElement(
+                                  o1.Fragment,
+                                  { key: fA.id },
                                   K6.createElement(
                                     I,
-                                    { width: 44 },
+                                    null,
                                     K6.createElement(
                                       f,
-                                      { color: CA ? "suggestion" : void 0 },
-                                      CA ? q1.pointer : " ",
-                                      " ",
-                                      VA.label,
+                                      { width: 44 },
+                                      o1.createElement(
+                                        V,
+                                        { color: SA ? "suggestion" : void 0 },
+                                        SA ? eA.pointer : " ",
+                                        " ",
+                                        fA.label,
+                                      ),
                                     ),
-                                  ),
-                                  K6.createElement(
-                                    I,
-                                    { key: CA ? "selected" : "unselected" },
-                                    VA.type === "boolean"
-                                      ? K6.createElement(
-                                          K6.Fragment,
-                                          null,
-                                          K6.createElement(
+                                    o1.createElement(
+                                      S,
+                                      { key: SA ? "selected" : "unselected" },
+                                      fA.type === "boolean"
+                                        ? o1.createElement(
+                                            o1.Fragment,
                                             f,
-                                            {
-                                              color: CA ? "suggestion" : void 0,
-                                            },
-                                            VA.value.toString(),
-                                          ),
-                                          OA &&
-                                            VA.id === "thinkingEnabled" &&
                                             K6.createElement(
                                               f,
-                                              { color: "warning" },
-                                              " ",
-                                              "Changing thinking mode mid-conversation will increase latency and may reduce quality.",
+                                              {
+                                                color: SA
+                                                  ? "suggestion"
+                                                  : void 0,
+                                              },
+                                              fA.value.toString(),
                                             ),
-                                        )
-                                      : VA.id === "theme"
-                                        ? K6.createElement(
-                                            f,
-                                            {
-                                              color: CA ? "suggestion" : void 0,
-                                            },
-                                            (() => {
-                                              return (
-                                                {
-                                                  dark: "Dark mode",
-                                                  light: "Light mode",
-                                                  "dark-daltonized":
-                                                    "Dark mode (colorblind-friendly)",
-                                                  "light-daltonized":
-                                                    "Light mode (colorblind-friendly)",
-                                                  "dark-ansi":
-                                                    "Dark mode (ANSI colors only)",
-                                                  "light-ansi":
-                                                    "Light mode (ANSI colors only)",
-                                                }[VA.value.toString()] ||
-                                                VA.value.toString()
-                                              );
-                                            })(),
+                                            HA &&
+                                              fA.id === "thinkingEnabled" &&
+                                              o1.createElement(
+                                                V,
+                                                { color: "warning" },
+                                                " ",
+                                                "Changing thinking mode mid-conversation will increase latency and may reduce quality.",
+                                              ),
                                           )
-                                        : VA.id === "notifChannel"
+                                        : fA.id === "theme"
                                           ? K6.createElement(
                                               f,
                                               {
@@ -977,63 +1017,24 @@
                                                   : void 0,
                                               },
                                               (() => {
-                                                switch (VA.value.toString()) {
-                                                  case "auto":
-                                                    return "Auto";
-                                                  case "iterm2":
-                                                    return K6.createElement(
-                                                      K6.Fragment,
-                                                      null,
-                                                      "iTerm2 ",
-                                                      K6.createElement(
-                                                        f,
-                                                        { dimColor: !0 },
-                                                        "(OSC 9)",
-                                                      ),
-                                                    );
-                                                  case "terminal_bell":
-                                                    return K6.createElement(
-                                                      K6.Fragment,
-                                                      null,
-                                                      "Terminal Bell ",
-                                                      K6.createElement(
-                                                        f,
-                                                        { dimColor: !0 },
-                                                        "(\\a)",
-                                                      ),
-                                                    );
-                                                  case "kitty":
-                                                    return K6.createElement(
-                                                      K6.Fragment,
-                                                      null,
-                                                      "Kitty ",
-                                                      K6.createElement(
-                                                        f,
-                                                        { dimColor: !0 },
-                                                        "(OSC 99)",
-                                                      ),
-                                                    );
-                                                  case "ghostty":
-                                                    return K6.createElement(
-                                                      K6.Fragment,
-                                                      null,
-                                                      "Ghostty ",
-                                                      K6.createElement(
-                                                        f,
-                                                        { dimColor: !0 },
-                                                        "(OSC 777)",
-                                                      ),
-                                                    );
-                                                  case "iterm2_with_bell":
-                                                    return "iTerm2 w/ Bell";
-                                                  case "notifications_disabled":
-                                                    return "Disabled";
-                                                  default:
-                                                    return VA.value.toString();
-                                                }
+                                                return (
+                                                  {
+                                                    dark: "Dark mode",
+                                                    light: "Light mode",
+                                                    "dark-daltonized":
+                                                      "Dark mode (colorblind-friendly)",
+                                                    "light-daltonized":
+                                                      "Light mode (colorblind-friendly)",
+                                                    "dark-ansi":
+                                                      "Dark mode (ANSI colors only)",
+                                                    "light-ansi":
+                                                      "Light mode (ANSI colors only)",
+                                                  }[fA.value.toString()] ||
+                                                  fA.value.toString()
+                                                );
                                               })(),
                                             )
-                                          : VA.id === "defaultPermissionMode"
+                                          : fA.id === "notifChannel"
                                             ? K6.createElement(
                                                 f,
                                                 {
@@ -1041,91 +1042,156 @@
                                                     ? "suggestion"
                                                     : void 0,
                                                 },
-                                                XF(VA.value),
+                                                (() => {
+                                                  switch (fA.value.toString()) {
+                                                    case "auto":
+                                                      return "Auto";
+                                                    case "iterm2":
+                                                      return o1.createElement(
+                                                        o1.Fragment,
+                                                        null,
+                                                        "iTerm2 ",
+                                                        o1.createElement(
+                                                          V,
+                                                          { dimColor: !0 },
+                                                          "(OSC 9)",
+                                                        ),
+                                                      );
+                                                    case "terminal_bell":
+                                                      return o1.createElement(
+                                                        o1.Fragment,
+                                                        null,
+                                                        "Terminal Bell ",
+                                                        o1.createElement(
+                                                          V,
+                                                          { dimColor: !0 },
+                                                          "(\\a)",
+                                                        ),
+                                                      );
+                                                    case "kitty":
+                                                      return o1.createElement(
+                                                        o1.Fragment,
+                                                        null,
+                                                        "Kitty ",
+                                                        o1.createElement(
+                                                          V,
+                                                          { dimColor: !0 },
+                                                          "(OSC 99)",
+                                                        ),
+                                                      );
+                                                    case "ghostty":
+                                                      return o1.createElement(
+                                                        o1.Fragment,
+                                                        null,
+                                                        "Ghostty ",
+                                                        o1.createElement(
+                                                          V,
+                                                          { dimColor: !0 },
+                                                          "(OSC 777)",
+                                                        ),
+                                                      );
+                                                    case "iterm2_with_bell":
+                                                      return "iTerm2 w/ Bell";
+                                                    case "notifications_disabled":
+                                                      return "Disabled";
+                                                    default:
+                                                      return fA.value.toString();
+                                                  }
+                                                })(),
                                               )
-                                            : VA.id === "autoUpdatesChannel" &&
-                                                JA
+                                            : fA.id === "defaultPermissionMode"
                                               ? K6.createElement(
                                                   I,
-                                                  { flexDirection: "column" },
-                                                  K6.createElement(
+                                                  {
+                                                    color: SA
+                                                      ? "suggestion"
+                                                      : void 0,
+                                                  },
+                                                  fF(fA.value),
+                                                )
+                                              : fA.id ===
+                                                    "autoUpdatesChannel" && GA
+                                                ? o1.createElement(
+                                                    S,
+                                                    { flexDirection: "column" },
+                                                    o1.createElement(
+                                                      V,
+                                                      {
+                                                        color: SA
+                                                          ? "suggestion"
+                                                          : void 0,
+                                                      },
+                                                      "disabled",
+                                                    ),
+                                                    o1.createElement(
+                                                      V,
+                                                      { dimColor: !0 },
+                                                      "(",
+                                                      GA,
+                                                      ")",
+                                                    ),
+                                                  )
+                                                : o1.createElement(
                                                     f,
                                                     {
                                                       color: CA
                                                         ? "suggestion"
                                                         : void 0,
                                                     },
-                                                    "disabled",
-                                                  ),
-                                                  K6.createElement(
-                                                    f,
-                                                    { dimColor: !0 },
-                                                    "(",
-                                                    JA,
-                                                    ")",
+                                                    fA.value.toString(),
                                                   ),
-                                                )
-                                              : K6.createElement(
-                                                  f,
-                                                  {
-                                                    color: CA
-                                                      ? "suggestion"
-                                                      : void 0,
-                                                  },
-                                                  VA.value.toString(),
-                                                ),
+                                    ),
                                   ),
-                                ),
-                              );
-                            }),
-                      ),
-                      x
-                        ? K6.createElement(
-                            f,
-                            { dimColor: !0 },
-                            K6.createElement(
-                              w8,
-                              null,
-                              K6.createElement(f, null, "Type to filter"),
-                              K6.createElement(G6, {
-                                shortcut: "Enter/↓",
-                                action: "select",
-                              }),
-                              K6.createElement(U6, {
-                                action: "confirm:no",
-                                context: "Settings",
-                                fallback: "Esc",
-                                description: "clear",
+                                );
                               }),
-                            ),
-                          )
-                        : K6.createElement(
-                            f,
-                            { dimColor: !0 },
-                            K6.createElement(
+                        ),
+                        b
+                          ? o1.createElement(
                               w8,
+                              { dimColor: !0 },
+                              o1.createElement(
+                                Y8,
+                                null,
+                                o1.createElement(V, null, "Type to filter"),
+                                o1.createElement(M6, {
+                                  shortcut: "Enter/↓",
+                                  action: "select",
+                                }),
+                                o1.createElement(Q6, {
+                                  action: "confirm:no",
+                                  context: "Settings",
+                                  fallback: "Esc",
+                                  description: "clear",
+                                }),
+                              ),
+                            )
+                          : o1.createElement(
                               null,
-                              K6.createElement(U6, {
-                                action: "select:accept",
-                                context: "Settings",
-                                fallback: "Enter/Space",
-                                description: "change",
-                              }),
-                              K6.createElement(U6, {
-                                action: "settings:search",
-                                context: "Settings",
-                                fallback: "/",
-                                description: "search",
-                              }),
-                              K6.createElement(U6, {
-                                action: "confirm:no",
-                                context: "Settings",
-                                fallback: "Esc",
-                                description: "cancel",
-                              }),
+                              { dimColor: !0 },
+                              o1.createElement(
+                                Y8,
+                                null,
+                                o1.createElement(Q6, {
+                                  action: "select:accept",
+                                  context: "Settings",
+                                  fallback: "Enter/Space",
+                                  description: "change",
+                                }),
+                                o1.createElement(Q6, {
+                                  action: "settings:search",
+                                  context: "Settings",
+                                  fallback: "/",
+                                  description: "search",
+                                }),
+                                o1.createElement(Q6, {
+                                  action: "confirm:no",
+                                  context: "Settings",
+                                  fallback: "Esc",
+                                  description: "cancel",
+                                }),
+                              ),
                             ),
-                          ),
-                    ),
+                      ),
     )
   );
 }

@@@ function 'ba2' (was 'Ur2') — structural (84.4%)
--- pretty-v2.1.22.js:529663
+++ pretty-v2.1.23.js:530724
@@ -42,14 +42,14 @@
   )
     return {
       behavior: "allow",
-      updatedInput: K,
+      updatedInput: UvK(J, K),
       decisionReason: { type: "mode", mode: z.toolPermissionContext.mode },
     };
   let X = gI6(z.toolPermissionContext, A);
   if (X)
     return {
       behavior: "allow",
-      updatedInput: K,
+      updatedInput: UvK(J, K),
       decisionReason: { type: "rule", rule: X },
     };
   let $ =

@@@ function 'grK' (was 'hnK') — structural (84.1%)
--- pretty-v2.1.22.js:1870
+++ pretty-v2.1.23.js:1872
@@ -1,6 +1,11 @@
 function hnK() {
   let A = "";
-  if (typeof process < "u" && typeof process.cwd === "function") A = SnK(InK());
+  if (
+    typeof process < "u" &&
+    typeof process.cwd === "function" &&
+    typeof Un6 === "function"
+  )
+    A = Un6(mrK());
   return {
     originalCwd: A,
     projectRoot: A,
@@ -67,9 +72,11 @@
     teleportedSessionInfo: null,
     invokedSkills: new Map(),
     slowOperations: [],
+    promptCacheBreaks: [],
     sdkBetas: void 0,
     mainThreadAgentType: void 0,
     isRemoteMode: !1,
+    directConnectServerUrl: void 0,
     additionalDirectoriesForClaudeMd: [],
     resumedTranscriptPath: null,
   };

@@@ function 'hgK' (was 'RmK') — structural (83.6%)
--- pretty-v2.1.22.js:564903
+++ pretty-v2.1.23.js:566536
@@ -1,8 +1,7 @@
 function RmK() {
   let A = s(20),
     { addNotification: K } = iK(),
-    [q] = V6(),
-    { installationStatus: Y } = q.plugins,
+    q = F1(Xqz),
     z;
   A: {
     if (!Y) {

@@@ variable 'Ke' (was 'it') — structural (83.0%)
--- pretty-v2.1.22.js:449641
+++ pretty-v2.1.23.js:449811
@@ -26,6 +26,8 @@
   CQ();
   df();
   l7();
+  of();
+  B7();
   ((EE2 = r(NR7(), 1)),
     (kE2 = {
       [VC]: ["launchSwarm", "teammateCount"],

@@@ class 'f31' (was 'e51') — structural (82.9%)
--- pretty-v2.1.22.js:182366
+++ pretty-v2.1.23.js:182421
@@ -9,6 +9,8 @@
   rootNode;
   renderer;
   stylePool;
+  charPool;
+  hyperlinkPool;
   exitPromise;
   restoreConsole;
   unsubscribeTTYHandlers;
@@ -17,6 +19,7 @@
   currentNode = null;
   frontFrame;
   backFrame;
+  lastPoolResetTime = performance.now();
   constructor(A) {
     this.options = A;
     if ((p46(this), this.options.patchConsole))
@@ -26,15 +29,21 @@
       (this.terminalColumns = A.stdout.columns || 80),
       (this.terminalRows = A.stdout.rows || 24),
       (this.stylePool = new s76()),
+      (this.charPool = new C51()),
+      (this.hyperlinkPool = new L51()),
       (this.frontFrame = MXA(
         this.terminalRows,
         this.terminalColumns,
         this.stylePool,
+        this.charPool,
+        this.hyperlinkPool,
       )),
       (this.backFrame = MXA(
         this.terminalRows,
         this.terminalColumns,
         this.stylePool,
+        this.charPool,
+        this.hyperlinkPool,
       )),
       (this.log = new YK6({
         debug: A.debug,
@@ -83,11 +92,15 @@
       this.frontFrame.viewport.height,
       this.frontFrame.viewport.width,
       this.stylePool,
+      this.charPool,
+      this.hyperlinkPool,
     )),
       (this.backFrame = MXA(
         this.backFrame.viewport.height,
         this.backFrame.viewport.width,
         this.stylePool,
+        this.charPool,
+        this.hyperlinkPool,
       )),
       this.log.reset());
   };
@@ -124,7 +137,12 @@
         terminalRows: q,
       }),
       z = this.log.render(this.frontFrame, Y);
-    ((this.backFrame = this.frontFrame), (this.frontFrame = Y));
+    if (
+      ((this.backFrame = this.frontFrame),
+      (this.frontFrame = Y),
+      A - this.lastPoolResetTime > 300000)
+    )
+      (this.resetPools(), (this.lastPoolResetTime = A));
     let w = [];
     for (let H of z)
       if (H.type === "clearTerminal")
@@ -145,6 +163,23 @@
   resume() {
     ((this.isPaused = !1), this.onRender());
   }
+  repaint() {
+    ((this.frontFrame = Dr(
+      this.frontFrame.viewport.height,
+      this.frontFrame.viewport.width,
+      this.stylePool,
+      this.charPool,
+      this.hyperlinkPool,
+    )),
+      (this.backFrame = Dr(
+        this.backFrame.viewport.height,
+        this.backFrame.viewport.width,
+        this.stylePool,
+        this.charPool,
+        this.hyperlinkPool,
+      )),
+      this.log.reset());
+  }
   stdinListeners = [];
   wasRawMode = !1;
   suspendStdin() {
@@ -234,9 +269,18 @@
           this.frontFrame.viewport.height,
           this.frontFrame.viewport.width,
           this.stylePool,
+          this.charPool,
+          this.hyperlinkPool,
         )),
         this.log.reset());
   }
+  resetPools() {
+    ((this.charPool = new C51()),
+      (this.hyperlinkPool = new L51()),
+      x04(this.frontFrame.screen, this.charPool, this.hyperlinkPool),
+      (this.backFrame.screen.charPool = this.charPool),
+      (this.backFrame.screen.hyperlinkPool = this.hyperlinkPool));
+  }
   patchConsole() {
     if (this.options.debug) return;
     return bH4((A, K) => {

@@@ variable 'ok' (was 'lk') — structural (82.7%)
--- pretty-v2.1.22.js:192993
+++ pretty-v2.1.23.js:193152
@@ -28,6 +28,7 @@
     if (z && V4("tengu_scarf_coffee", !1)) K.push(HnA);
     if (Y === "vertex" && G_9(A)) K.push(LL1);
     if (Y === "foundry") K.push(LL1);
+    if (Y === "firstParty") K.push(gn6);
     if (process.env.ANTHROPIC_BETAS && !q)
       K.push(
         ...process.env.ANTHROPIC_BETAS.split(",")

@@@ variable 'ld' (was 'gd') — structural (82.6%)
--- pretty-v2.1.22.js:461639
+++ pretty-v2.1.23.js:462157
@@ -19,6 +19,7 @@
   $_1();
   yJK();
   l6();
+  l6();
   NR2 =
     r6() === "windows" && !process.env.SHELLOPTS ? { SHELLOPTS: "igncr" } : {};
   ax6 = a1(ER2);

@@@ function 'JyK' (was 'zRK') — structural (82.4%)
--- pretty-v2.1.22.js:549866
+++ pretty-v2.1.23.js:550893
@@ -26,7 +26,9 @@
       return Math.max(...JA.map((t) => t.userFacingName().length)) + 6;
     }, [A]),
     [N, T] = gw.useState(void 0),
-    [E] = V6(),
+    C = F1((t) => t.mcp.resources),
+    R = F1((t) => t.teamContext),
+    x = F1((t) => t.promptSuggestion),
     R = bk(),
     [b, S] = gw.useState(void 0),
     B = gw.useMemo(() => {
@@ -63,7 +65,7 @@
     wA = gw.useCallback(
       async (JA, AA = !1) => {
         Q.current = JA;
-        let t = await zp6(JA, E.mcp.resources, J, AA);
+        let VA = await Qp6(t, C, J, XA);
         if (Q.current !== JA) return;
         if (t.length === 0) {
           (O(() => ({
@@ -83,7 +85,7 @@
           P(t.length > 0 ? "file" : "none"),
           T(void 0));
       },
-      [E.mcp.resources, O, P, T, J],
+      [C, O, P, T, J],
     ),
     HA = Gr(wA, 200),
     OA = gw.useCallback(
@@ -130,9 +132,9 @@
         }
         if (D8()) {
           let XA = JA.substring(0, t).match(/(^|\s)@([\w-]*)$/);
-          if (XA && E.teamContext) {
+          if (fA && R) {
             let LA = XA[2] ?? "",
-              VA = Object.values(E.teamContext.teammates ?? {})
+              SA = Object.values(R.teammates ?? {})
                 .filter((EA) => EA.name !== "team-lead")
                 .filter((EA) =>
                   EA.name.toLowerCase().startsWith(LA.toLowerCase()),
@@ -158,9 +160,9 @@
             }
           }
         }
-        let ZA = JA.substring(0, t).match(
-            /(^|\s)@([a-zA-Z0-9_\-./\\()[\]~:]*|"[^"]*"?)$/,
-          ),
+        let vA = t
+            .substring(0, VA)
+            .match(/(^|\s)@([a-zA-Z0-9_\-./\\()[\]~:]*|"[^"]*"?)$/),
           kA = t === JA.length && t > 0 && JA.length > 0 && JA[t - 1] === " ";
         if (H === "prompt" && Wc(JA) && t > 0) {
           let XA = sAz(JA);
@@ -281,7 +283,10 @@
               : XA,
           );
         if (M === "custom-title") e();
-        if (M === "agent" && o.current.some((XA) => XA.id?.startsWith("dm-"))) {
+        if (
+          M === "agent" &&
+          YA.current.some((fA) => fA.id?.startsWith("dm-"))
+        ) {
           if (!JA.substring(0, t).match(/(^|\s)@([\w-]*)$/)) e();
         }
         if (ZA && H !== "bash") {
@@ -373,7 +378,15 @@
                   oE1(t.metadata) && t.metadata.type === "directory"
                     ? "/"
                     : " ";
-              kA = LA + t.id + VA;
+              if (
+                ((RA = LA + VA.id + SA),
+                K(RA),
+                Y(RA.length),
+                ocA(VA.metadata) && VA.metadata.type === "directory")
+              )
+                (O((xA) => ({ ...xA, commandArgumentHint: void 0 })),
+                  a(RA, RA.length));
+              else qA();
             } else {
               let LA = Dc(z, w, !0) ?? Dc(z, w, !1);
               if (LA) {
@@ -466,7 +479,7 @@
           if (t) {
             let ZA = t.token.startsWith("@"),
               kA = ZA ? t.token.substring(1) : t.token;
-            AA = await zp6(kA, E.mcp.resources, J, ZA);
+            XA = await Qp6(RA, C, J, vA);
           } else AA = [];
         }
         if (AA.length > 0)
@@ -478,7 +491,7 @@
             P(JA),
             T(void 0));
       }
-    }, [X, $, z, M, A, H, K, Y, q, e, w, OA, E.mcp.resources, O, J, HA, x]),
+    }, [X, $, z, M, A, H, K, Y, q, qA, w, a, C, O, J, _A, Q]),
     a = gw.useCallback(() => {
       if ($ < 0 || X.length === 0) return;
       let JA = X[$];
@@ -530,9 +543,7 @@
             let kA = z.indexOf(" "),
               XA = z.slice(0, kA + 1),
               LA =
-                oE1(JA.metadata) && JA.metadata.type === "directory"
-                  ? "/"
-                  : " ";
+                ocA(t.metadata) && t.metadata.type === "directory" ? "/" : " ";
             ((t = XA + JA.id + LA), (ZA = t.length), K(t), Y(ZA));
           } else {
             let XA = Dc(z, w, !0) ?? Dc(z, w, !1);
@@ -583,8 +594,7 @@
     O7(mA, { context: "Autocomplete", isActive: qA && !YA }),
     e6((JA, AA, t) => {
       if (AA.rightArrow) {
-        let kA = E.promptSuggestion.text,
-          XA = E.promptSuggestion.shownAt;
+        let { text: RA, shownAt: fA } = x;
         if (kA && XA > 0 && z === "") {
           (G(), K(kA), Y(kA.length), t.stopImmediatePropagation());
           return;
@@ -592,8 +602,7 @@
       }
       if (AA.tab && !AA.shift) {
         if (X.length > 0 || x) return;
-        let kA = E.promptSuggestion.text,
-          XA = E.promptSuggestion.shownAt;
+        let { text: RA, shownAt: fA } = x;
         if (kA && XA > 0 && z === "") {
           (G(), K(kA), Y(kA.length));
           return;

@@@ variable 'i2' (was 't2') — structural (81.8%)
--- pretty-v2.1.22.js:390104
+++ pretty-v2.1.23.js:390437
@@ -18,8 +18,6 @@
   d2();
   Zq();
   fs7();
-  vs7();
-  fD();
   ((d4 = r($A(), 1)),
     (Gv = r($A(), 1)),
     (Es7 = NFA()),

@@@ function 'Q_K' (was 'g$K') — structural (81.4%)
--- pretty-v2.1.22.js:477998
+++ pretty-v2.1.23.js:478707
@@ -1,5 +1,5 @@
 function g$K(A, K) {
-  let q = ["low", "medium", "high"],
+  let q = ["low", "medium", "high", "max"],
     Y = q.indexOf(A);
   if (K === "right") return q[(Y + 1) % q.length];
   else return q[(Y - 1 + q.length) % q.length];

@@@ function 'Ne2' (was 'ys2') — structural (81.2%)
--- pretty-v2.1.22.js:536377
+++ pretty-v2.1.23.js:537448
@@ -3,7 +3,7 @@
   if (((ZU6 = !0), !pEK))
     ((pEK = !0),
       Gk7(() => {
-        (_Q6(), UQA(), NVA.forEach((K) => K()));
+        (rQ6(), gVA.forEach((K) => K()));
       }));
   let A = await Ss2();
   if (A.length === 0) return;

@@@ function 'Jv1' (was 'ST1') — structural (81.2%)
--- pretty-v2.1.22.js:490054
+++ pretty-v2.1.23.js:491073
@@ -1,8 +1,9 @@
 function ST1(A) {
   let K = s(66),
     { onComplete: q } = A,
-    [Y] = V6(),
-    z = Y.mcp.clients,
+    Y = F1(gm2),
+    z = F1(mm2),
+    w = Y.clients,
     w;
   if (K[0] === Symbol.for("react.memo_cache_sentinel"))
     ((w = { type: "list" }), (K[0] = w));
@@ -13,10 +14,8 @@
   else O = K[1];
   let [X, $] = vL.default.useState(O),
     _;
-  if (K[2] !== Y.agentDefinitions.allAgents)
-    ((_ = SZ7(Y.agentDefinitions.allAgents)),
-      (K[2] = Y.agentDefinitions.allAgents),
-      (K[3] = _));
+  if (K[2] !== z.allAgents)
+    ((G = BZ7(z.allAgents)), (K[2] = z.allAgents), (K[3] = G));
   else _ = K[3];
   let Z = _,
     G;
@@ -25,7 +24,7 @@
   let W = G,
     D,
     j;
-  if (K[6] !== Y.mcp.tools || K[7] !== W)
+  if (K[6] !== D || K[7] !== Y.tools)
     ((D = () => {
       (async function () {
         let T = await Promise.all(
@@ -38,8 +37,7 @@
             if (b || S) {
               let u = await new RqA(E.name, E.config).tokens(),
                 d = RC() !== null && E.type === "connected",
-                o =
-                  E.type === "connected" && ru(Y.mcp.tools, E.name).length > 0;
+                c = R.type === "connected" && YB(Y.tools, R.name).length > 0;
               x = Boolean(u) || d || o;
             }
             let F = { name: E.name, client: E, scope: R };
@@ -70,9 +68,9 @@
         $(T);
       })();
     }),
-      (j = [W, Y.mcp.tools]),
-      (K[6] = Y.mcp.tools),
-      (K[7] = W),
+      (M = [D, Y.tools]),
+      (K[6] = D),
+      (K[7] = Y.tools),
       (K[8] = D),
       (K[9] = j));
   else ((D = K[8]), (j = K[9]));
@@ -128,9 +126,9 @@
     }
     case "server-menu": {
       let V;
-      if (K[23] !== Y.mcp.tools || K[24] !== H.server.name)
-        ((V = ru(Y.mcp.tools, H.server.name)),
-          (K[23] = Y.mcp.tools),
+      if (K[23] !== Y.tools || K[24] !== J.server.name)
+        ((N = YB(Y.tools, J.server.name)),
+          (K[23] = Y.tools),
           (K[24] = H.server.name),
           (K[25] = V));
       else V = K[25];
@@ -237,9 +235,9 @@
     }
     case "server-tool-detail": {
       let V;
-      if (K[53] !== Y.mcp.tools || K[54] !== H.server.name)
-        ((V = ru(Y.mcp.tools, H.server.name)),
-          (K[53] = Y.mcp.tools),
+      if (K[53] !== Y.tools || K[54] !== J.server.name)
+        ((N = YB(Y.tools, J.server.name)),
+          (K[53] = Y.tools),
           (K[54] = H.server.name),
           (K[55] = V));
       else V = K[55];

@@@ variable 'okK' (was 'iEK') — structural (81.1%)
--- pretty-v2.1.22.js:536507
+++ pretty-v2.1.23.js:537578
@@ -30,6 +30,7 @@
   dz();
   W1();
   gj();
+  Rr();
   lEK = a1(() => {
     let A = Date.now();
     (E8("info", "init_started"), $K("init_function_start"));
@@ -59,6 +60,8 @@
         $K("init_after_1p_event_logging"),
         VR4(),
         $K("init_after_oauth_populate"),
+        R36(),
+        wK("init_after_jetbrains_detection"),
         VL6())
       )
         la7();

@@@ function 'wr2' (was 'Mi2') — structural (80.8%)
--- pretty-v2.1.22.js:523076
+++ pretty-v2.1.23.js:524112
@@ -1,8 +1,9 @@
 function Mi2(A) {
   let K = s(12),
     { onDone: q } = A,
-    [Y, z] = V6(),
-    { mainLoopModel: w, mainLoopModelForSession: H } = Y,
+    Y = F1(Jr2),
+    z = F1(Hr2),
+    w = p4(),
     J;
   if (K[0] !== w || K[1] !== q)
     ((J = function () {

@@@ function 'v3A' (was 'W3A') — structural (80.8%)
--- pretty-v2.1.22.js:407312
+++ pretty-v2.1.23.js:407694
@@ -1,6 +1,6 @@
 function W3A(A) {
-  let K = s(30),
-    { content: q, verbose: Y } = A,
+  let K = s(33),
+    { content: q, verbose: Y, timeoutMs: z } = A,
     {
       stdout: z,
       stderr: w,
@@ -120,22 +120,36 @@
       (K[22] = M));
   else M = K[22];
   let P;
+  if (K[23] !== z)
+    ((f =
+      z &&
+      OP.default.createElement(
+        k6,
+        null,
+        OP.default.createElement(VQA, { timeoutMs: z }),
+      )),
+      (K[23] = z),
+      (K[24] = f));
+  else f = K[24];
+  let N;
   if (
-    K[23] !== X ||
-    K[24] !== Z ||
     K[25] !== G ||
     K[26] !== W ||
     K[27] !== j ||
-    K[28] !== M
+    K[28] !== D ||
+    K[29] !== M ||
+    K[30] !== P ||
+    K[31] !== f
   )
-    ((P = Mv.default.createElement(X, { flexDirection: Z }, G, W, j, M)),
-      (K[23] = X),
-      (K[24] = Z),
+    ((N = OP.default.createElement($, { flexDirection: Z }, W, D, M, P, f)),
       (K[25] = G),
       (K[26] = W),
       (K[27] = j),
       (K[28] = M),
-      (K[29] = P));
-  else P = K[29];
+      (K[29] = M),
+      (K[30] = P),
+      (K[31] = f),
+      (K[32] = N));
+  else N = K[32];
   return P;
 }

@@@ function 'aP2' (was 'UM2') — structural (80.6%)
--- pretty-v2.1.22.js:423337
+++ pretty-v2.1.23.js:423659
@@ -120,7 +120,7 @@
               querySource: "agent:custom",
               override: { abortController: T },
               model: O,
-              shareSetAppState: !0,
+              availableTools: H.options.tools,
               allowedTools: _,
             })) {
               if (J.signal.aborted) {

@@@ function 'Ae' (was 'yd') — structural (80.5%)
--- pretty-v2.1.22.js:449301
+++ pretty-v2.1.23.js:449422
@@ -19,6 +19,7 @@
     PUA,
     ...(AH() ? [o2K, zzK, GzK, vzK] : []),
     ...(FzK ? [FzK] : []),
+    ...(dwK ? [dwK] : []),
     Zb6,
     ...(D8() ? [VE2(), fE2()] : []),
     ...(gzK ? [gzK] : []),

@@@ variable 'dZ1' (was 'fG1') — structural (80.1%)
--- pretty-v2.1.22.js:426089
+++ pretty-v2.1.23.js:426411
@@ -30,6 +30,7 @@
   P2();
   DS6();
   MT();
+  f_();
   ((PS6 = r($A(), 1)),
     (FQA = j1(process.env.CLAUDE_CODE_DISABLE_BACKGROUND_TASKS)),
     (VP2 = U.object({
@@ -70,11 +71,9 @@
         .describe(
           "Team name for spawning. Uses current team context if omitted.",
         ),
-      mode: rL8
-        .optional()
-        .describe(
-          'Permission mode for spawned teammate (e.g., "plan" to require plan approval).',
-        ),
+      mode: UR8.optional().describe(
+        'Permission mode for spawned teammate (e.g., "plan" to require plan approval).',
+      ),
     })),
     (XqK = VP2.merge(fP2)),
     (Cy6 = FQA ? XqK.omit({ run_in_background: !0 }) : XqK),
@@ -242,19 +241,28 @@
           isBuiltInAgent: BD(N),
           startTime: W,
         },
+        b = D.toolPermissionContext.mode === "coordinator",
+        F = (w === !0 || b) && !EV1,
         x = {
+          ...D.toolPermissionContext,
+          mode: N.permissionMode ?? "acceptEdits",
+        },
+        u = kV1(Q, D.mcp.tools),
+        d = {
           agentDefinition: N,
           promptMessages: E ? [...E, ...S] : S,
           toolUseContext: $,
           canUseTool: _,
           forkContextMessages: R,
-          isAsync: w === !0 && !FQA,
+          isAsync: F,
+          ...(b ? { canShowPermissionPrompts: !0 } : {}),
           querySource: $.options.querySource ?? L4K(N.agentType, BD(N)),
           model: Y,
           maxTurns: H,
           override: b ? { systemPrompt: b } : void 0,
+          availableTools: u,
         };
-      if (w === !0 && !FQA) {
+      if (F) {
         let F = z || eI(),
           Q = ID7({
             agentId: F,
@@ -477,7 +485,8 @@
     getActivityDescription(A) {
       return A?.description ?? "Running task";
     },
-    async checkPermissions(A) {
+    async checkPermissions(A, K) {
+      let q = await K.getAppState();
       return { behavior: "allow", updatedInput: A };
     },
     mapToolResultToToolResultBlockParam(A, K) {

@@@ function 'kGA' (was 'XZA') — structural (80.0%)
--- pretty-v2.1.22.js:265995
+++ pretty-v2.1.23.js:266174
@@ -4,9 +4,7 @@
   customSystemPrompt: q,
   defaultSystemPrompt: Y,
   appendSystemPrompt: z,
-  overrideSystemPrompt: w,
 }) {
-  if (w) return [w];
   let H = A
     ? BD(A)
       ? A.getSystemPrompt({ toolUseContext: { options: K.options } })

@@@ variable 'Hk1' (was 'SE1') — structural (80.0%)
--- pretty-v2.1.22.js:542073
+++ pretty-v2.1.23.js:543167
@@ -4,6 +4,7 @@
   R3();
   i1();
   A4();
+  C8();
   ((HN = r($A(), 1)),
     (ke2 = {
       accept: "tell Claude what to do next",

@@@ function 'DgK' (was '_mK') — structural (79.1%)
--- pretty-v2.1.22.js:564378
+++ pretty-v2.1.23.js:566009
@@ -1,7 +1,7 @@
 function _mK() {
   let A = s(9),
     { addNotification: K } = iK(),
-    [, q] = V6(),
+    q = p4(),
     [Y, z] = vj.useState(!0),
     w;
   if (A[0] === Symbol.for("react.memo_cache_sentinel"))

@@@ function 'vS2' (was 'jI2') — structural (79.0%)
--- pretty-v2.1.22.js:467467
+++ pretty-v2.1.23.js:467981
@@ -201,6 +201,17 @@
       ]);
     case "dynamic_skill":
       return [];
+    case "skill_listing": {
+      if (!A.content) return [];
+      return c9([
+        t1({
+          content: `The following skills are available for use with the Skill tool:
+
+${A.content}`,
+          isMeta: !0,
+        }),
+      ]);
+    }
     case "queued_command": {
       if (Array.isArray(A.prompt)) {
         let q = A.prompt.filter((w) => w.type === "text").map((w) => w.text)

@@@ function 'pyK' (was 'gRK') — structural (79.0%)
--- pretty-v2.1.22.js:552027
+++ pretty-v2.1.23.js:553308
@@ -1,15 +1,17 @@
 function gRK(A) {
-  let K = s(26),
+  let K = s(28),
     {
       exitMessage: q,
       vimMode: Y,
       mode: z,
       toolPermissionContext: w,
       suppressHint: H,
+      isLoading: J,
       tasksSelected: J,
       teamsSelected: O,
       diffSelected: X,
       loopSelected: $,
+      teammateFooterIndex: G,
       isPasting: _,
       isSearching: Z,
       historyQuery: G,
@@ -80,16 +82,20 @@
     K[17] !== T ||
     K[18] !== J ||
     K[19] !== O ||
-    K[20] !== w
+    K[20] !== G ||
+    K[21] !== X ||
+    K[22] !== w
   )
     ((E = jq.createElement(I1z, {
       mode: z,
       toolPermissionContext: w,
       showHint: T,
+      isLoading: J,
       tasksSelected: J,
       teamsSelected: O,
       diffSelected: X,
       loopSelected: $,
+      teammateFooterIndex: G,
     })),
       (K[14] = X),
       (K[15] = $),
@@ -98,10 +104,12 @@
       (K[18] = J),
       (K[19] = O),
       (K[20] = w),
-      (K[21] = E));
-  else E = K[21];
+      (K[21] = X),
+      (K[22] = w),
+      (K[23] = x));
+  else x = K[23];
   let R;
-  if (K[22] !== V || K[23] !== N || K[24] !== E)
+  if (K[24] !== T || K[25] !== C || K[26] !== x)
     ((R = jq.createElement(
       I,
       { justifyContent: "flex-start", gap: 1 },
@@ -110,10 +118,10 @@
       N,
       E,
     )),
-      (K[22] = V),
-      (K[23] = N),
       (K[24] = E),
-      (K[25] = R));
-  else R = K[25];
+      (K[25] = C),
+      (K[26] = x),
+      (K[27] = y));
+  else y = K[27];
   return R;
 }

@@@ function 'mhK' (was 'bSK') — structural (79.0%)
--- pretty-v2.1.22.js:560977
+++ pretty-v2.1.23.js:562612
@@ -1,7 +1,8 @@
 function bSK(A, K, q, Y = "session", z = !1) {
   let w = $N.useRef("unknown");
   w.current = pf(A)?.message?.id || "unknown";
-  let [H, J] = V6(),
+  let H = F1((T) => T.feedbackSurvey),
+    J = p4(),
     O = ISK("tengu_feedback_survey_config", j8z),
     X = $N.useRef(Date.now()),
     $ = $N.useRef(q),
@@ -56,20 +57,15 @@
       if (D !== "closed") return !1;
       if (K) return !1;
       if (z) return !1;
-      if (
-        process.env.CLAUDE_FORCE_DISPLAY_SURVEY &&
-        !H.feedbackSurvey.timeLastShown
-      )
+      if (process.env.CLAUDE_FORCE_DISPLAY_SURVEY && !H.timeLastShown)
         return !0;
       if (!V) return !1;
       if (j1(process.env.CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY)) return !1;
       if (sX()) return !1;
-      if (H.feedbackSurvey.timeLastShown) {
+      if (H.timeLastShown) {
         if (
-          H.feedbackSurvey.submitCountAtLastAppearance !== null &&
-          q <
-            H.feedbackSurvey.submitCountAtLastAppearance +
-              O.minUserTurnsBetweenFeedback
+          H.submitCountAtLastAppearance !== null &&
+          q < H.submitCountAtLastAppearance + O.minUserTurnsBetweenFeedback
         )
           return !1;
       } else {
@@ -88,8 +84,8 @@
       K,
       z,
       V,
-      H.feedbackSurvey.timeLastShown,
-      H.feedbackSurvey.submitCountAtLastAppearance,
+      H.timeLastShown,
+      H.submitCountAtLastAppearance,
       q,
       O.minTimeBetweenGlobalFeedbackMs,
       O.minUserTurnsBetweenFeedback,

@@@ function 'LP7' (was 'jM7') — structural (79.0%)
--- pretty-v2.1.22.js:315966
+++ pretty-v2.1.23.js:316387
@@ -69,8 +69,7 @@
         exitCode: H,
       }),
       (Y.responseAttachmentSent = !0),
-      Y.stopProgressInterval(),
-      Y.shellCommand.cleanup(),
+      FP6(Y, H, H === 0 ? "success" : "error"),
       YB.delete(Y.processId),
       Y.hookEvent === "SessionStart")
     )
@@ -78,16 +77,6 @@
         `Invalidating session env cache after SessionStart hook ${Y.processId} completed`,
       ),
         Oj7());
-    gI({
-      hookId: Y.hookId,
-      hookName: Y.hookName,
-      hookEvent: Y.hookEvent,
-      output: Y.output,
-      stdout: Y.stdout,
-      stderr: Y.stderr,
-      exitCode: H,
-      outcome: H === 0 ? "success" : "error",
-    });
   }
   for (let Y of q) YB.delete(Y);
   return (h(`Hooks: checkForNewResponses returning ${A.length} responses`), A);

@@@ variable 'E5A' (was 'D5A') — structural (78.9%)
--- pretty-v2.1.22.js:339308
+++ pretty-v2.1.23.js:339809
@@ -5,6 +5,7 @@
   j8();
   W1();
   J7();
+  z7();
   kR7 = U.object({
     status: U.literal("sub_agent_entered"),
     description: U.string(),

@@@ function 'jNK' (was 'WfK') — structural (78.9%)
--- pretty-v2.1.22.js:518844
+++ pretty-v2.1.23.js:519881
@@ -1,9 +1,12 @@
 function WfK({ tools: A, onExit: K }) {
   let [q, Y] = ue.useState({ mode: "list-agents", source: "all" }),
-    [z, w] = V6(),
-    { allAgents: H, activeAgents: J } = z.agentDefinitions,
+    z = F1((j) => j.agentDefinitions),
+    w = F1((j) => j.mcp.tools),
+    H = F1((j) => j.toolPermissionContext),
+    J = p4(),
+    { allAgents: O, activeAgents: X } = z,
     [O, X] = ue.useState([]),
-    $ = uv1(A, z.mcp.tools, z.toolPermissionContext);
+    G = $E1(A, w, H);
   r8();
   let _ = ue.useMemo(
     () => ({

@@@ function 'mWK' (was 'uGK') — structural (78.5%)
--- pretty-v2.1.22.js:494777
+++ pretty-v2.1.23.js:495803
@@ -7,7 +7,9 @@
   targetMarketplace: w,
   action: H,
 }) {
-  let [J] = V6(),
+  let J = F1((xA) => xA.mcp.clients),
+    O = F1((xA) => xA.mcp.tools),
+    X = F1((xA) => xA.plugins.errors),
     [O, X] = hz.useState(!1),
     $ = hz.useCallback(
       (EA) => {
@@ -60,9 +62,8 @@
     },
     l = hz.useMemo(() => {
       let EA = O8(),
-        CA = J.plugins.errors,
         dA = new Map();
-      for (let P1 of J.mcp.clients)
+      for (let c1 of J)
         if (P1.name.startsWith("plugin:")) {
           let z6 = P1.name.split(":");
           if (z6.length >= 3) {
@@ -129,7 +130,7 @@
         });
       }
       let S6 = [];
-      for (let P1 of J.mcp.clients) {
+      for (let c1 of J) {
         if (P1.name === "ide") continue;
         if (P1.name.startsWith("plugin:")) continue;
         S6.push({
@@ -205,7 +206,7 @@
         J1.push(...TA);
       }
       return J1;
-    }, [E, J.mcp.clients, J.plugins.errors, F]),
+    }, [x, J, X, u]),
     e = hz.useMemo(() => {
       if (!D) return l;
       let EA = D.toLowerCase();
@@ -656,7 +657,7 @@
     let EA = O8(),
       CA = `${P.plugin.name}@${P.marketplace}`,
       dA = EA?.enabledPlugins?.[CA] !== !1,
-      z1 = J.plugins.errors.filter(
+      v1 = X.filter(
         (V1) =>
           ("plugin" in V1 && V1.plugin === P.plugin.name) ||
           V1.source === CA ||
@@ -812,7 +813,7 @@
   }
   if (typeof G === "object" && G.type === "mcp-detail") {
     let EA = G.client,
-      CA = ru(J.mcp.tools, EA.name).length,
+      iA = YB(O, xA.name).length,
       dA = () => {
         W({ type: "mcp-tools", client: EA });
       },

@@@ function 'RN1' (was 'AN1') — structural (78.2%)
--- pretty-v2.1.22.js:461531
+++ pretty-v2.1.23.js:462050
@@ -7,7 +7,7 @@
       .padStart(4, "0"),
     Z = IJK.tmpdir();
   if (r6() === "windows") Z = lh(Z);
-  let G = rx6(process.env.CLAUDE_CODE_TMPDIR || "/tmp", "claude"),
+  let Z = Su6(process.env.CLAUDE_CODE_TMPDIR || "/tmp", xu6()),
     W = H ? rx6(G, `cwd-${_}`) : rx6(Z, `claude-${_}-cwd`),
     D = PJK(A),
     j = MJK(A, D);
@@ -36,8 +36,7 @@
   if (H) {
     N = await I8.wrapWithSandbox(N, X, void 0, K);
     try {
-      let b = xA();
-      if (!b.existsSync(G)) b.mkdirSync(G);
+      BA().mkdirSync(Z, { mode: 448 });
     } catch (b) {
       h(`Failed to create ${G} directory: ${b}`);
     }

@@@ function 'n5z' (was 'CKz') — structural (78.1%)
--- pretty-v2.1.22.js:573417
+++ pretty-v2.1.23.js:575138
@@ -141,6 +141,7 @@
           }
           let WA = OA.value;
           W = s7();
+          let a = void 0;
           for await (let a of _QK({
             commands: Q,
             prompt: WA,
@@ -291,7 +292,7 @@
           })()
         )
           (yZ({ mode: "prompt", value: TQK, uuid: nL() }, O), d());
-        else (u(), D.done());
+        else (await QP6(), u(), D.done());
     },
     o = function (e, wA) {
       D.enqueue({
@@ -573,7 +574,7 @@
         }),
           d());
       }
-      if (((Z = !0), !_)) (u(), D.done());
+      if (((G = !0), !_)) (await QP6(), u(), D.done());
     })(),
     D
   );

@@@ function 'Mz8' (was 'E28') — structural (77.9%)
--- pretty-v2.1.22.js:30939
+++ pretty-v2.1.23.js:30954
@@ -1,6 +1,6 @@
 function E28(A, K, q, Y, z = !1) {
   let { rgPath: w, rgArgs: H, argv0: J } = RwA(),
-    O = z || L28 ? ["-j", "1"] : [],
+    O = z ? ["-j", "1"] : [],
     X = [...H, ...O, ...A, K],
     $ = r6() === "wsl" ? 60000 : 20000,
     _ = parseInt(process.env.CLAUDE_CODE_GLOB_TIMEOUT_SECONDS || "", 10) || 0,

@@@ function 'VM1' (was 'Uj1') — structural (77.9%)
--- pretty-v2.1.22.js:388838
+++ pretty-v2.1.23.js:389398
@@ -1,5 +1,6 @@
 function Uj1({ tasks: A, isStandalone: K = !1 }) {
-  let [q] = V6(),
+  let q = F1((y) => y.teamContext),
+    Y = F1((y) => y.tasks),
     [, Y] = xK.useState(0),
     { rows: z } = M8(),
     w = z <= 10 ? 0 : Math.min(10, Math.max(3, z - 14)),
@@ -24,7 +25,6 @@
     !AH())
   )
     return null;
-  let { teamContext: O } = q;
   if (A.length === 0) return null;
   let X = {};
   if (D8() && O?.teammates) {
@@ -34,10 +34,12 @@
         if (S) X[b.name] = S;
       }
   }
-  let $ = {};
+  let $ = {},
+    _ = new Set();
   if (D8()) {
-    for (let b of Object.values(q.tasks))
+    for (let y of Object.values(Y))
       if (rT(b) && b.status === "running") {
+        (_.add(y.identity.agentName), _.add(y.identity.agentId));
         let S = b.progress?.recentActivities,
           B = (S && mqA(S)) ?? b.progress?.lastActivity?.activityDescription;
         if (B) (($[b.identity.agentName] = B), ($[b.identity.agentId] = B));
@@ -86,6 +88,7 @@
         ownerColor: b.owner ? X[b.owner] : void 0,
         openBlockers: b.blockedBy.filter((S) => W.has(S)),
         activity: b.owner ? $[b.owner] : void 0,
+        ownerActive: y.owner ? _.has(y.owner) : !1,
       }),
     ),
     w > 0 && E && xK.createElement(f, { dimColor: !0 }, E),

@@@ function 'ue2' (was 'ds2') — structural (77.8%)
--- pretty-v2.1.22.js:536787
+++ pretty-v2.1.23.js:537861
@@ -48,5 +48,6 @@
     forkContextMessages: q,
     querySource: "magic_docs",
     override: { systemPrompt: Y, userContext: z, systemContext: w },
+    availableTools: O.options.tools,
   }));
 }

@@@ function 'xT1' (was 'BB6') — structural (77.3%)
--- pretty-v2.1.22.js:476560
+++ pretty-v2.1.23.js:477178
@@ -109,26 +109,45 @@
     }
     O.sort((_, Z) => Z.mtime.getTime() - _.mtime.getTime());
     let X = O.slice(Wb2);
-    if (X.length === 0) return;
-    let $ = 0;
-    for (let _ of X)
-      try {
-        if (
-          await Db2(_.path, async () => {
-            await nd(_.path);
-          })
-        )
-          $++;
-        else h(`Skipping deletion of ${_.name} - locked by another process`);
-      } catch (Z) {
-        KA(Error(`Failed to delete version ${_.name}: ${Z}`));
-      }
-    if ($ > 0)
+    if (X.length === 0) {
       n("tengu_native_version_cleanup", {
-        deleted_count: $,
+        total_count: Y.length,
+        deleted_count: 0,
         protected_count: H.size,
-        retained_count: O.length - $,
+        retained_count: Dm6,
+        lock_failed_count: 0,
+        error_count: 0,
       });
+      return;
+    }
+    let $ = 0,
+      _ = 0,
+      G = 0;
+    (await Promise.all(
+      X.map(async (Z) => {
+        try {
+          if (
+            await Ex2(Z.path, async () => {
+              await Ac(Z.path);
+            })
+          )
+            $++;
+          else
+            (_++,
+              h(`Skipping deletion of ${Z.name} - locked by another process`));
+        } catch (W) {
+          (G++, KA(Error(`Failed to delete version ${Z.name}: ${W}`)));
+        }
+      }),
+    ),
+      n("tengu_native_version_cleanup", {
+        total_count: Y.length,
+        deleted_count: $,
+        protected_count: H.size,
+        retained_count: Dm6,
+        lock_failed_count: _,
+        error_count: G,
+      }));
   } catch (q) {
     KA(Error(`Version cleanup failed: ${q}`));
   }

@@@ variable 'G9A' (was 'e3A') — structural (77.1%)
--- pretty-v2.1.22.js:459909
+++ pretty-v2.1.23.js:460427
@@ -14,6 +14,7 @@
   WV();
   Xa();
   h1();
+  b1();
   ((LL2 = new Set([rq, E7, cz, bH, iE, HO, l5, lz])),
     (sMA = new Set()),
     (of1 = new Set()),

@@@ function 'hLY' (was 'fCY') — structural (77.1%)
--- pretty-v2.1.22.js:306211
+++ pretty-v2.1.23.js:306551
@@ -11,7 +11,8 @@
   let q = `${PCY}${K}`;
   return II.createElement(
     I,
-    { flexWrap: "nowrap", marginLeft: 1 },
+    null,
+    " ",
     II.createElement(
       G7,
       { url: q },

@@@ function 'zPK' (was 'qMK') — structural (77.0%)
--- pretty-v2.1.22.js:503331
+++ pretty-v2.1.23.js:504364
@@ -1,6 +1,6 @@
 function qMK() {
   let { columns: A } = M8(),
-    [K] = V6(),
+    K = F1((R) => R.agent),
     [q, { isVisible: Y }] = D4A(),
     z = Xv1(),
     w = Dv1.useRef(z);
@@ -12,7 +12,7 @@
       billingType: X,
       agentName: $,
     } = w.current,
-    _ = K.agent ?? $,
+    _ = K ?? $,
     Z = Gv1();
   Dv1.useEffect(() => {
     if (Z) Wv1();

@@@ function 'hhK' (was 'RSK') — structural (76.9%)
--- pretty-v2.1.22.js:560805
+++ pretty-v2.1.23.js:562438
@@ -4,11 +4,13 @@
   resetLoadingState: q,
   setAbortController: Y,
 }) {
-  let [z, w] = V6(),
+  let z = F1((G) => G.foregroundedTaskId),
+    w = F1((G) => G.tasks),
+    H = p4(),
     H = KAA.useRef(null),
     J = KAA.useRef(0),
     O = KAA.useCallback(() => {
-      if (z.foregroundedTaskId) {
+      if (z) {
         (w((_) => {
           let Z = _.foregroundedTaskId;
           if (!Z) return _;
@@ -26,17 +28,17 @@
         return;
       }
       H.current?.resolve();
-    }, [z.foregroundedTaskId, w, A, q, Y]),
+    }, [z, H, A, q, Y]),
     X = KAA.useCallback(
       (_) => {
         (H.current?.resolve(), BD7(_, w));
       },
       [w],
     ),
-    $ = z.foregroundedTaskId ? z.tasks[z.foregroundedTaskId] : void 0;
+    _ = z ? w[z] : void 0;
   return (
     KAA.useEffect(() => {
-      if (!z.foregroundedTaskId) {
+      if (!z) {
         J.current = 0;
         return;
       }
@@ -85,7 +87,7 @@
           q(),
           Y(null),
           (J.current = 0));
-    }, [z.foregroundedTaskId, $, w, A, K, q, Y]),
+    }, [z, _, H, A, K, q, Y]),
     {
       backgroundSignalRef: H,
       handleBackgroundSession: O,

@@@ function 'uL2' (was 'RC2') — structural (76.8%)
--- pretty-v2.1.22.js:458171
+++ pretty-v2.1.23.js:458657
@@ -1,4 +1,6 @@
-async function RC2() {
+async function uL2(A) {
+  if ((await A.getAppState()).toolPermissionContext.mode === "coordinator")
+    return [];
   let A = await Gp.getNewDiagnostics();
   if (A.length === 0) return [];
   return [{ type: "diagnostics", files: A, isNew: !0 }];

@@@ function 'bYA' (was 'VYA') — structural (76.5%)
--- pretty-v2.1.22.js:565783
+++ pretty-v2.1.23.js:567487
@@ -20,7 +20,7 @@
   disableSlashCommands: P = !1,
   taskListId: V,
   remoteSessionConfig: N,
-  autoTickIntervalMs: T,
+  directConnectConfig: T,
 }) {
   A8.useEffect(() => {
     return (
@@ -29,15 +29,31 @@
       () => h("[REPL:unmount] REPL unmounting")
     );
   }, [j]);
-  let [E, R] = V6(),
+  let C = F1((W1) => W1.toolPermissionContext),
+    R = F1((W1) => W1.verbose),
+    x = F1((W1) => W1.mcp),
+    y = F1((W1) => W1.plugins),
+    B = F1((W1) => W1.agentDefinitions),
+    b = F1((W1) => W1.fileHistory),
+    F = F1((W1) => W1.todos),
+    Q = F1((W1) => W1.thinkingEnabled),
+    u = F1((W1) => W1.initialMessage),
+    d = F1((W1) => W1.queuedCommands),
+    r = void 0,
+    c = !1,
+    YA = void 0,
+    e = F1((W1) => W1.spinnerTip),
+    qA = F1((W1) => W1.showExpandedTodos),
+    HA = F1((W1) => W1.pendingWorkerRequest),
+    _A = F1((W1) => W1.pendingSandboxRequest),
+    a = F1((W1) => W1.teamContext),
+    JA = F1((W1) => W1.tasks),
+    jA = F1((W1) => W1.workerSandboxPermissions),
+    MA = F1((W1) => W1.elicitation),
+    hA = F1((W1) => W1.viewingAgentTaskId),
+    yA = p4(),
+    AA = D0(),
     b = Cx(),
-    {
-      toolPermissionContext: S,
-      verbose: B,
-      mcp: x,
-      plugins: F,
-      agentDefinitions: Q,
-    } = E,
     u = Vt(),
     [d, o] = A8.useState(A);
   ZSK(iP(), o);
@@ -79,6 +95,7 @@
     ImK(),
     jT1(),
     xmK(u),
+    QgK(),
     BmK(u),
     gmK(),
     QmK(),
@@ -173,7 +190,7 @@
     }, []),
     [d8, Bq] = A8.useState([]),
     [Jq, mq] = A8.useState([]),
-    w3 = d8.length > 0 || E.pendingWorkerRequest || E.pendingSandboxRequest,
+    Y4 = n4.length > 0 || HA || _A,
     KY = k4?.isLocalJSXCommand === !0;
   (A8.useEffect(() => {
     if (w1 && !w3 && !KY) dZ7();
@@ -208,6 +225,8 @@
       [o],
     ),
     Y8 = GIK({ config: N, setMessages: u7, setIsLoading: P4, onInit: Z4 }),
+    Z8 = DSK({ config: T, setMessages: $q, setIsLoading: QK }),
+    j4 = Z8.isRemoteMode ? Z8 : Z6,
     [f7, S3] = A8.useState({}),
     [T9, H5] = A8.useState(0),
     [LY, eA] = A8.useState(0),
@@ -259,17 +278,17 @@
       resetLoadingState: c9,
       setAbortController: cA,
     }),
-    R_ = jQA(E.tasks).some((W6) => W6.status === "running"),
+    _4 = p3A(JA).some((W1) => W1.status === "running"),
     H6 =
       (!k4 || k4.showSpinner === !0) &&
       d8.length === 0 &&
       (w1 || T1 || R_) &&
-      !E.pendingWorkerRequest,
+      !HA,
     N8 =
       d8.length > 0 ||
       Jq.length > 0 ||
-      E.elicitation.queue.length > 0 ||
-      E.workerSandboxPermissions.queue.length > 0,
+      MA.queue.length > 0 ||
+      jA.queue.length > 0,
     p4 = bSK(t4, w1, T9, "session", N8),
     x4 = A8.useMemo(
       () => ({
@@ -293,7 +312,7 @@
     setShowIdeOnboarding: VA,
     setIDEInstallationState: XA,
   }),
-    zhK(z, E.fileHistory, (W6) => R((h8) => ({ ...h8, fileHistory: W6 }))));
+    ObK(z, b, (W1) => yA((F6) => ({ ...F6, fileHistory: W1 }))));
   let p5 = A8.useCallback(
       async (W6, h8, e8) => {
         n("tengu_session_resumed", { entrypoint: e8 });
@@ -329,7 +348,7 @@
         let W6 = rQ(_7A);
         return (
           W6.set(K8, {
-            content: QA(E.todos[a6] || []),
+            content: UA(F[w2] || []),
             timestamp: 0,
             offset: void 0,
             limit: void 0,
@@ -356,9 +375,8 @@
     if (Jq[0]) return "sandbox-permission";
     let W6 = !k4 || k4.shouldContinueAnimation;
     if (W6 && d8[0]) return "tool-permission";
-    if (W6 && E.workerSandboxPermissions.queue[0])
-      return "worker-sandbox-permission";
-    if (W6 && E.elicitation.queue[0]) return "elicitation";
+    if (W1 && jA.queue[0]) return "worker-sandbox-permission";
+    if (W1 && MA.queue[0]) return "elicitation";
     if (W6 && Jz) return "cost";
     if (W6 && LA) return "ide-onboarding";
     if (W6 && dA) return "lsp-recommendation";
@@ -448,8 +466,14 @@
         A5(1, "other"));
     });
   let pw = A8.useCallback(
-    (W6) => {
-      (R((h8) => ({ ...h8, toolPermissionContext: W6 })),
+    (W1, F6) => {
+      (yA((r6) => ({
+        ...r6,
+        toolPermissionContext: {
+          ...W1,
+          mode: F6?.preserveMode ? r6.toolPermissionContext.mode : W1.mode,
+        },
+      })),
         setImmediate(() => {
           Bq((h8) => {
             return (
@@ -478,12 +502,7 @@
             verbose: B,
             mainLoopModel: N7,
             maxThinkingTokens:
-              r4 ??
-              (E.thinkingEnabled === !0
-                ? bp(h8, void 0)
-                : E.thinkingEnabled === !1
-                  ? 0
-                  : void 0),
+              f4 ?? (Q === !0 ? dp(F6, void 0) : Q === !1 ? 0 : void 0),
             mcpClients: YA,
             mcpResources: x.resources,
             ideInstallationStatus: kA,
@@ -495,23 +514,19 @@
             appendSystemPrompt: G,
           },
           getAppState() {
-            return new Promise((FK) => {
-              R((l9) => {
-                return (
-                  FK(l9),
-                  {
-                    ...l9,
-                    toolPermissionContext: {
-                      ...l9.toolPermissionContext,
-                      alwaysAllowRules: {
-                        ...l9.toolPermissionContext.alwaysAllowRules,
-                        command: dq,
-                      },
-                    },
-                  }
-                );
-              });
-            });
+            return (
+              AA.setState((SK) => ({
+                ...SK,
+                toolPermissionContext: {
+                  ...SK.toolPermissionContext,
+                  alwaysAllowRules: {
+                    ...SK.toolPermissionContext.alwaysAllowRules,
+                    command: e4,
+                  },
+                },
+              })),
+              Promise.resolve(AA.getState())
+            );
           },
           setAppState: R,
           messages: W6,
@@ -577,18 +592,19 @@
         WA,
         v0,
         p5,
-        E.thinkingEnabled,
         j,
         Z,
         G,
         q7,
+        Z,
+        wJ,
       ],
     ),
     rL = A8.useCallback(
       async (W6, h8, e8, dq, r4, N7, FK) => {
-        let l9 = h8
-          .filter((Q1) => Q1.type === "user" || Q1.type === "assistant")
-          .pop();
+        let K3 = F6.filter(
+          (QW) => QW.type === "user" || QW.type === "assistant",
+        ).pop();
         if (dq) {
           Gp.handleQueryStart(YA);
           let Q1 = Mf(YA);
@@ -617,7 +633,6 @@
           customSystemPrompt: Z,
           defaultSystemPrompt: _5,
           appendSystemPrompt: G,
-          overrideSystemPrompt: null,
         });
         P5("query_query_start");
         let AE,
@@ -731,7 +746,7 @@
     ),
     Jh = A8.useRef(!1);
   A8.useEffect(() => {
-    let W6 = E.initialMessage;
+    let W1 = u;
     if (!W6 || w1 || Jh.current) return;
     Jh.current = !0;
     async function h8(e8) {
@@ -794,7 +809,7 @@
       }, 100);
     }
     h8(W6);
-  }, [E.initialMessage, w1, u7, R, h_, u, p1]);
+  }, [u, E8, $q, yA, IO, GA, K6]);
   let kj = A8.useCallback(
       async (W6, h8, e8, dq) => {
         if (!e8 && W6.trim().startsWith("/")) {
@@ -893,7 +908,7 @@
           setAbortController: cA,
           onQuery: h_,
           resetLoadingState: c9,
-          thinkingEnabled: E.thinkingEnabled,
+          thinkingEnabled: Q,
           setAppState: R,
           querySource: YP1(),
           onBeforeQuery: W,
@@ -924,13 +939,13 @@
         c9,
         H7,
         I5,
-        E.thinkingEnabled,
         R,
         W,
         S_,
         Y8,
         u7,
         qA,
+        Q1,
       ],
     ),
     dw = A8.useCallback(
@@ -980,12 +995,12 @@
     FkK(t4, t4.length === Y?.length),
     TIK(),
     A8.useEffect(() => {
-      if (E.queuedCommands.length < 1) return;
+      if (d.length < 1) return;
       D6((W6) => ({
         ...W6,
         promptQueueUseCount: (W6.promptQueueUseCount ?? 0) + 1,
       }));
-    }, [E.queuedCommands.length]));
+    }, [d.length]));
   let f4 = A8.useCallback(
       () =>
         new Promise((W6) =>
@@ -1020,7 +1035,7 @@
           setAbortController: cA,
           onQuery: h_,
           resetLoadingState: c9,
-          thinkingEnabled: E.thinkingEnabled,
+          thinkingEnabled: Q,
           setAppState: R,
           querySource: YP1(),
           onBeforeQuery: W,
@@ -1028,29 +1043,11 @@
           addNotification: qA,
         });
       },
-      [
-        w1,
-        J1,
-        P4,
-        l8,
-        EX,
-        t4,
-        u,
-        JA,
-        d1,
-        S_,
-        cA,
-        h_,
-        c9,
-        E.thinkingEnabled,
-        qA,
-        R,
-        W,
-      ],
+      [E8, D8, QK, Q8, HJ, z4, GA, C6, dY, YY, r8, IO, LY, Q, Q1, yA, W],
     );
   (YSK({
     isLoading: w1,
-    queuedCommandsLength: E.queuedCommands.length,
+    queuedCommandsLength: d.length,
     lastQueryCompletionTime: NA,
     getAppState: f4,
     setAppState: R,
@@ -1186,7 +1183,7 @@
     pm = A8.useCallback(() => {
       N9(null);
     }, []),
-    dm = E.todos[a6],
+    Mh = F[w2],
     cm = {
       screen: a,
       setScreen: _A,
@@ -1232,7 +1229,9 @@
       M4.createElement(HmK, null),
       M4.createElement(Y7z, { showAllInTranscript: SA }),
     );
-  let oL = QW7(E, t4);
+  let a1 = hA ? JA[hA] : void 0,
+    c6 = a1 && W_(a1) ? a1 : void 0,
+    I6 = c6?.messages ?? z4;
   return M4.createElement(
     Rz,
     null,
@@ -1250,15 +1249,13 @@
       M4.createElement(WSK, null),
       M4.createElement(ke, {
         messages: oL,
-        normalizedMessageHistory: IqA(E) ? [] : XG,
+        normalizedMessageHistory: c6 ? [] : KE,
         tools: p1,
         commands: J1,
         verbose: B,
         toolJSX: k4,
         toolUseConfirmQueue: d8,
-        inProgressToolUseIDs: IqA(E)
-          ? (cM(E)?.inProgressToolUseIDs ?? new Set())
-          : J5,
+        inProgressToolUseIDs: c6 ? (c6.inProgressToolUseIDs ?? new Set()) : nq,
         isMessageSelectorVisible: c1,
         conversationId: _4,
         screen: a,
@@ -1285,7 +1282,7 @@
         H6 &&
           M4.createElement(Ls7, {
             mode: $1,
-            spinnerTip: E.spinnerTip,
+            spinnerTip: e,
             currentResponseLength: LY,
             overrideMessage: uA,
             spinnerSuffix: CX,
@@ -1299,8 +1296,8 @@
         null,
         !H6 &&
           !k4?.isLocalJSXCommand &&
-          E.showExpandedTodos &&
           V1 &&
+          f1 &&
           V1.length > 0 &&
           M4.createElement(
             I,
@@ -1309,7 +1306,7 @@
           ),
         !H6 &&
           !k4?.isLocalJSXCommand &&
-          E.showExpandedTodos &&
+          qA &&
           !(V1 && V1.length > 0) &&
           M4.createElement(
             I,
@@ -1341,9 +1338,9 @@
               }
               mq((N7) => {
                 return (
-                  N7.filter((FK) => FK.hostPattern.host === r4).forEach((FK) =>
-                    FK.resolvePromise(h8),
-                  ),
+                  h7
+                    .filter((SK) => SK.hostPattern.host === f4)
+                    .forEach((SK) => SK.resolvePromise(F6)),
                   N7.filter((FK) => FK.hostPattern.host !== r4)
                 );
               });
@@ -1359,36 +1356,27 @@
             verbose: B,
             workerBadge: d8[0]?.workerBadge,
           }),
-        E.pendingWorkerRequest &&
+        HA &&
           M4.createElement(EU6, {
-            toolName: E.pendingWorkerRequest.toolName,
-            description: E.pendingWorkerRequest.description,
+            toolName: HA.toolName,
+            description: HA.description,
           }),
-        E.pendingSandboxRequest &&
+        _A &&
           M4.createElement(EU6, {
             toolName: "Network Access",
-            description: `Waiting for leader to approve network access to ${E.pendingSandboxRequest.host}`,
+            description: `Waiting for leader to approve network access to ${_A.host}`,
           }),
         RY === "worker-sandbox-permission" &&
           M4.createElement(np6, {
-            key: E.workerSandboxPermissions.queue[0].requestId,
-            hostPattern: {
-              host: E.workerSandboxPermissions.queue[0].host,
-              port: void 0,
-            },
+            key: jA.queue[0].requestId,
+            hostPattern: { host: jA.queue[0].host, port: void 0 },
             onUserResponse: (W6) => {
               let { allow: h8, persistToSettings: e8 } = W6,
-                dq = E.workerSandboxPermissions.queue[0];
+                e4 = jA.queue[0];
               if (!dq) return;
               let r4 = dq.host;
               if (
-                (w7K(
-                  dq.workerName,
-                  dq.requestId,
-                  r4,
-                  h8,
-                  E.teamContext?.teamName,
-                ),
+                (jKK(e4.workerName, e4.requestId, f4, F6, a?.teamName),
                 e8 && h8)
               ) {
                 let N7 = {
@@ -1415,10 +1403,10 @@
           }),
         RY === "elicitation" &&
           M4.createElement(qLK, {
-            serverName: E.elicitation.queue[0].serverName,
-            request: E.elicitation.queue[0].request,
+            serverName: MA.queue[0].serverName,
+            request: MA.queue[0].request,
             onResponse: (W6, h8) => {
-              let e8 = E.elicitation.queue[0];
+              let r6 = MA.queue[0];
               if (e8)
                 (R((dq) => ({
                   ...dq,
@@ -1426,7 +1414,7 @@
                 })),
                   e8.respond({ action: W6, content: h8 }));
             },
-            signal: E.elicitation.queue[0].signal,
+            signal: MA.queue[0].signal,
           }),
         RY === "cost" &&
           M4.createElement(LkK, {

@@@ variable 'HP1' (was 'LM1') — structural (76.5%)
--- pretty-v2.1.22.js:407454
+++ pretty-v2.1.23.js:407850
@@ -4,5 +4,6 @@
   SGA();
   Tq();
   mK();
+  Sy6();
   ((Mv = r($A(), 1)), (Z8K = /(?:^|\n)(Shell cwd was reset to .+)$/));
 });

@@@ function 'cVA' (was 'LVA') — structural (76.1%)
--- pretty-v2.1.22.js:541867
+++ pretty-v2.1.23.js:542944
@@ -1,5 +1,5 @@
 function LVA(A) {
-  let K = s(50),
+  let K = s(54),
     {
       options: q,
       onSelect: Y,
@@ -8,7 +8,7 @@
       toolAnalyticsContext: H,
     } = A,
     J = w === void 0 ? "Do you want to proceed?" : w,
-    [, O] = V6(),
+    O = p4(),
     [X, $] = HN.useState(""),
     [_, Z] = HN.useState(""),
     [G, W] = HN.useState(!1),
@@ -107,8 +107,7 @@
           instructions_length: qA?.length ?? 0,
           entered_feedback_mode: PA.feedbackConfig.type === "accept" ? V : T,
         };
-        if (PA.feedbackConfig.type === "accept")
-          n("tengu_accept_submitted", YA);
+        if (AA.feedbackConfig.type === "accept") n("tengu_accept_submitted", t);
         else if (PA.feedbackConfig.type === "reject")
           n("tengu_reject_submitted", YA);
       }
@@ -126,38 +125,50 @@
   else d = K[26];
   let o = d,
     l;
-  if (K[27] !== z || K[28] !== O)
+  if (K[27] !== r || K[28] !== q) {
+    c = {};
+    for (let yA of q) if (yA.keybinding) c[yA.keybinding] = () => r(yA.value);
+    ((K[27] = r), (K[28] = q), (K[29] = c));
+  } else c = K[29];
+  let YA = c,
+    e;
+  if (K[30] === Symbol.for("react.memo_cache_sentinel"))
+    ((e = { context: "Confirmation" }), (K[30] = e));
+  else e = K[30];
+  s4(YA, e);
+  let qA;
+  if (K[31] !== z || K[32] !== O)
     ((l = () => {
       (n("tengu_permission_request_escape", {}), O(Ce2), z?.());
     }),
-      (K[27] = z),
-      (K[28] = O),
-      (K[29] = l));
-  else l = K[29];
+      (K[31] = z),
+      (K[32] = O),
+      (K[33] = qA));
+  else qA = K[33];
   let e = l,
     wA;
-  if (K[30] !== J)
+  if (K[34] !== J)
     ((wA = typeof J === "string" ? HN.default.createElement(f, null, J) : J),
-      (K[30] = J),
-      (K[31] = wA));
-  else wA = K[31];
+      (K[34] = J),
+      (K[35] = _A));
+  else _A = K[35];
   let HA;
-  if (K[32] !== X || K[33] !== G || K[34] !== q || K[35] !== _ || K[36] !== D)
+  if (K[36] !== X || K[37] !== Z || K[38] !== q || K[39] !== _ || K[40] !== D)
     ((HA = (jA) => {
       let PA = q.find((SA) => SA.value === jA);
       if (PA?.feedbackConfig?.type !== "accept" && G && !X.trim()) W(!1);
       if (PA?.feedbackConfig?.type !== "reject" && D && !_.trim()) j(!1);
       P(jA);
     }),
-      (K[32] = X),
-      (K[33] = G),
-      (K[34] = q),
-      (K[35] = _),
       (K[36] = D),
-      (K[37] = HA));
-  else HA = K[37];
+      (K[37] = Z),
+      (K[38] = q),
+      (K[39] = _),
+      (K[40] = D),
+      (K[41] = a));
+  else a = K[41];
   let OA;
-  if (K[38] !== e || K[39] !== u || K[40] !== o || K[41] !== F || K[42] !== HA)
+  if (K[42] !== HA || K[43] !== u || K[44] !== r || K[45] !== F || K[46] !== a)
     ((OA = HN.default.createElement(k6, {
       options: F,
       inlineDescriptions: !0,
@@ -166,31 +177,37 @@
       onFocus: HA,
       onInputModeToggle: u,
     })),
-      (K[38] = e),
-      (K[39] = u),
-      (K[40] = o),
-      (K[41] = F),
       (K[42] = HA),
-      (K[43] = OA));
-  else OA = K[43];
+      (K[43] = u),
+      (K[44] = r),
+      (K[45] = F),
+      (K[46] = a),
+      (K[47] = JA));
+  else JA = K[47];
   let WA = B && " · Tab to amend",
     a;
-  if (K[44] !== WA)
+  if (K[48] !== jA)
     ((a = HN.default.createElement(
       I,
       { marginTop: 1 },
       HN.default.createElement(f, { dimColor: !0 }, "Esc to cancel", WA),
     )),
-      (K[44] = WA),
-      (K[45] = a));
-  else a = K[45];
-  let _A;
-  if (K[46] !== a || K[47] !== wA || K[48] !== OA)
-    ((_A = HN.default.createElement(I, { flexDirection: "column" }, wA, OA, a)),
-      (K[46] = a),
-      (K[47] = wA),
       (K[48] = OA),
       (K[49] = _A));
   else _A = K[49];
+  let hA;
+  if (K[50] !== JA || K[51] !== MA || K[52] !== _A)
+    ((hA = _N.default.createElement(
+      S,
+      { flexDirection: "column" },
+      _A,
+      JA,
+      MA,
+    )),
+      (K[50] = JA),
+      (K[51] = MA),
+      (K[52] = _A),
+      (K[53] = hA));
+  else hA = K[53];
   return _A;
 }

@@@ function 'pCK' (was 'FkK') — structural (75.4%)
--- pretty-v2.1.22.js:539008
+++ pretty-v2.1.23.js:540085
@@ -1,6 +1,5 @@
 function FkK(A, K = !1) {
-  let [q] = V6(),
-    { teamContext: Y } = q;
+  let q = F1((Y) => Y.teamContext);
   gkK.useEffect(() => {
     if (!K)
       Jm(A, {

@@@ function 'F7z' (was 'A$2') — structural (75.0%)
--- pretty-v2.1.22.js:390017
+++ pretty-v2.1.23.js:562829
@@ -1,3 +1,3 @@
-function A$2() {
+function F7z(A) {
   return mg(Xs7);
 }

@@@ variable 'sD' (was 'aT') — structural (75.0%)
--- pretty-v2.1.22.js:458514
+++ pretty-v2.1.23.js:459005
@@ -38,6 +38,9 @@
   P2();
   Tv();
   TJ();
+  W2();
+  Nv();
+  VJ();
   ((mf1 = { TURNS_SINCE_WRITE: 10, TURNS_BETWEEN_REMINDERS: 10 }),
     (vHK = {
       TURNS_BETWEEN_ATTACHMENTS: 5,
@@ -45,4 +48,5 @@
     }),
     (ek2 = { TOKEN_COOLDOWN: 5000 }),
     (KC2 = { TURNS_BETWEEN_REMINDERS: 10 }));
+  JpA = new Set();
 });

@@@ function 'ByK' (was 'hRK') — structural (74.9%)
--- pretty-v2.1.22.js:551872
+++ pretty-v2.1.23.js:553149
@@ -1,8 +1,10 @@
 function hRK() {
-  let [A, K] = V6(),
+  let A = F1((J) => J.fileHistory.trackedFiles),
+    K = F1((J) => J.gitDiff),
+    q = p4(),
     q = Mc.useRef(null),
     Y = Mc.useRef(!1),
-    z = A.fileHistory.trackedFiles.size > 0,
+    w = A.size > 0,
     w = Mc.useCallback(async () => {
       if (!V4("tengu_code_diff_cli", !1)) return;
       let H = await wk7();
@@ -46,12 +48,8 @@
     Mc.useMemo(() => {
       if (Y.current) return null;
       if (!z) return null;
-      if (!A.gitDiff.stats) return null;
-      return {
-        stats: A.gitDiff.stats,
-        perFileStats: A.gitDiff.perFileStats,
-        hunks: A.gitDiff.hunks,
-      };
-    }, [z, A.gitDiff.stats, A.gitDiff.perFileStats, A.gitDiff.hunks])
+      if (!K.stats) return null;
+      return { stats: K.stats, perFileStats: K.perFileStats, hunks: K.hunks };
+    }, [w, K.stats, K.perFileStats, K.hunks])
   );
 }

@@@ function 'RHK' (was 'IwK') — structural (74.0%)
--- pretty-v2.1.22.js:453457
+++ pretty-v2.1.23.js:453931
@@ -1,21 +1,9 @@
 async function IwK(A) {
   if (A.querySource !== "repl_main_thread") return;
-  let K = await A.toolUseContext.getAppState();
-  if (!K.promptSuggestionEnabled) return;
-  if (K.pendingWorkerRequest || K.pendingSandboxRequest) {
-    DL("pending_permission");
-    return;
-  }
-  if (K.elicitation.queue.length > 0) {
-    DL("elicitation_active");
-    return;
-  }
-  if (K.toolPermissionContext.mode === "plan") {
-    DL("plan_mode");
-    return;
-  }
-  if (Kf.status !== "allowed") {
-    DL("rate_limit");
+  let K = await A.toolUseContext.getAppState(),
+    q = hx6(K);
+  if (q) {
+    rS(q);
     return;
   }
   if (A.messages.filter((H) => H.type === "assistant").length < 2) {

@@@ function 'lf1' (was 'ff1') — structural (73.9%)
--- pretty-v2.1.22.js:453006
+++ pretty-v2.1.23.js:453346
@@ -7,6 +7,8 @@
     tools_executed: ab6(z),
     completed: w !== null,
     boundary_type: w?.type,
+    boundary_tool: WC2(w),
+    boundary_detail: DC2(w),
     ...H,
   });
 }

@@@ function 'CgK' (was 'TmK') — structural (73.7%)
--- pretty-v2.1.22.js:564640
+++ pretty-v2.1.23.js:566271
@@ -1,6 +1,6 @@
 function TmK() {
   let A = s(11),
-    [K] = V6(),
+    K = F1(zqz),
     { addNotification: q } = iK(),
     [Y, z] = dL.useState(null),
     w;
@@ -11,13 +11,12 @@
     J = dL.useRef(!1),
     O,
     X;
-  if (A[1] !== K.fileHistory.trackedFiles || A[2] !== Y)
+  if (A[1] !== Y || A[2] !== K)
     ((O = () => {
       if (Y) return;
       if (J.current) return;
       if (Un6()) return;
-      let G = K.fileHistory.trackedFiles,
-        W = [];
+      let Z = [];
       for (let j of G) if (!H.current.has(j)) (H.current.add(j), W.push(j));
       if (W.length === 0) return;
       ((J.current = !0),
@@ -48,8 +47,8 @@
           }
       }
     }),
-      (X = [K.fileHistory.trackedFiles, Y]),
-      (A[1] = K.fileHistory.trackedFiles),
+      (X = [K, Y]),
+      (A[1] = Y),
       (A[2] = Y),
       (A[3] = O),
       (A[4] = X));

@@@ function 'Dd6' (was 'yp6') — structural (73.2%)
--- pretty-v2.1.22.js:557920
+++ pretty-v2.1.23.js:559419
@@ -1,5 +1,5 @@
 function yp6(A) {
-  let K = s(28),
+  let K = s(31),
     {
       screen: q,
       setScreen: Y,
@@ -9,17 +9,19 @@
       onExitTranscript: J,
       todos: O,
     } = A,
-    [X, $] = V6(),
-    _;
-  if (K[0] !== X.showExpandedTodos || K[1] !== $ || K[2] !== O)
+    X = F1(D7z),
+    $ = p4();
+  D0();
+  let _;
+  if (K[0] !== $ || K[1] !== X || K[2] !== O)
     ((_ = () => {
       (n("tengu_toggle_todos", {
-        is_expanded: X.showExpandedTodos,
+        is_expanded: X,
         has_todos: O && O.length > 0,
       }),
         $(A8z));
     }),
-      (K[0] = X.showExpandedTodos),
+      (K[0] = $),
       (K[1] = $),
       (K[2] = O),
       (K[3] = _));
@@ -93,15 +95,24 @@
     ((E = { context: "Global" }), (K[23] = E));
   else E = K[23];
   A6("app:toggleTeammatePreview", T, E);
+  let R;
+  if (K[24] !== z) ((R = () => {}), (K[24] = z), (K[25] = R));
+  else R = K[25];
+  let x = R,
+    y;
+  if (K[26] === Symbol.for("react.memo_cache_sentinel"))
+    ((y = { context: "Global" }), (K[26] = y));
+  else y = K[26];
+  J6("app:toggleTerminal", x, y);
   let R = q === "transcript",
     b;
-  if (K[24] !== R)
-    ((b = { context: "Transcript", isActive: R }), (K[24] = R), (K[25] = b));
-  else b = K[25];
+  if (K[27] !== B)
+    ((b = { context: "Transcript", isActive: B }), (K[27] = B), (K[28] = b));
+  else b = K[28];
   A6("transcript:toggleShowAll", j, b);
   let S;
-  if (K[26] !== R)
-    ((S = { context: "Transcript", isActive: R }), (K[26] = R), (K[27] = S));
-  else S = K[27];
+  if (K[29] !== B)
+    ((F = { context: "Transcript", isActive: B }), (K[29] = B), (K[30] = F));
+  else F = K[30];
   return (A6("transcript:exit", P, S), null);
 }

@@@ function 'n8z' (was 'h1z') — structural (73.2%)
--- pretty-v2.1.22.js:552419
+++ pretty-v2.1.23.js:553712
@@ -6,6 +6,8 @@
       return "error";
     case "pending":
       return "warning";
+    case "merged":
+      return "merged";
     case "draft":
       return;
   }

@@@ function 'iCK' (was 'dkK') — structural (73.1%)
--- pretty-v2.1.22.js:539030
+++ pretty-v2.1.23.js:540106
@@ -5,7 +5,7 @@
   onRestoreCode: Y,
   onClose: z,
 }) {
-  let [w] = V6(),
+  let w = F1((e) => e.fileHistory),
     [H, J] = VX.useState(void 0),
     O = s2(),
     X = VX.useMemo(Qt2, []),
@@ -39,7 +39,7 @@
     }
     if (O) {
       j(wA);
-      let WA = $mA(w.fileHistory, wA.uuid);
+      let _A = xmA(w, e.uuid);
       P(WA);
     } else {
       (K(), N(!0));
@@ -128,7 +128,7 @@
       Promise.all(
         $.map(async (HA, OA) => {
           if (HA.uuid !== X) {
-            let WA = vZ1(w.fileHistory, HA.uuid),
+            let _A = iG1(w, qA.uuid),
               a = $.at(OA + 1),
               _A = WA
                 ? ct2(A, HA.uuid, a?.uuid !== X ? a?.uuid : void 0)
@@ -140,7 +140,7 @@
       );
     }
     wA();
-  }, [$, A, X, w.fileHistory, O]);
+  }, [$, A, X, w, O]);
   let e = O && M?.filesChanged && M.filesChanged.length > 0;
   return h6.createElement(
     I,

@@@ function 'cIK' (was 'pyK') — structural (73.0%)
--- pretty-v2.1.22.js:555351
+++ pretty-v2.1.23.js:556514
@@ -1,6 +1,7 @@
 function pyK() {
-  let [A] = V6(),
-    { teamContext: K, standaloneAgentContext: q } = A,
+  let A = F1((w) => w.teamContext),
+    K = F1((w) => w.standaloneAgentContext),
+    q = D0(),
     [Y, z] = Xk1.useState(null);
   if (
     (Xk1.useEffect(() => {
@@ -19,7 +20,7 @@
     (K?.teammates ? Object.keys(K.teammates).length : 0) > 0 &&
     K?.teamName
   ) {
-    let J = cM(A),
+    let J = OB(q.getState()),
       O =
         J?.identity.color && H$.includes(J.identity.color)
           ? q0[J.identity.color]
@@ -40,7 +41,7 @@
     }
   }
   if (D8()) {
-    let w = QyK(A),
+    let w = pIK(q.getState()),
       H = q?.color;
     if (w || H) {
       let J = H ? q0[H] : "cyan_FOR_SUBAGENTS_ONLY";

@@@ function '$IK' (was 'HyK') — structural (72.5%)
--- pretty-v2.1.22.js:553517
+++ pretty-v2.1.23.js:554831
@@ -1,5 +1,5 @@
 function HyK() {
-  let [A] = V6(),
+  let A = F1((Y) => Y.gitDiff),
     [K, q] = FVA.useState(new Map());
   return (
     FVA.useEffect(() => {
@@ -12,9 +12,9 @@
           Y = !0;
         }
       );
-    }, [A.gitDiff.lastUpdated]),
+    }, [A.lastUpdated]),
     FVA.useMemo(() => {
-      let { stats: Y, perFileStats: z } = A.gitDiff,
+      let { stats: Y, perFileStats: z } = A,
         w = [];
       for (let [H, J] of z) {
         let O = K.get(H),
@@ -36,6 +36,6 @@
         w.sort((H, J) => H.path.localeCompare(J.path)),
         { stats: Y, files: w, hunks: K }
       );
-    }, [A.gitDiff, K])
+    }, [A, K])
   );
 }

@@@ variable 'FT1' (was 'BGK') — structural (72.4%)
--- pretty-v2.1.22.js:495880
+++ pretty-v2.1.23.js:478716
@@ -13,23 +13,5 @@
   v1();
   W1();
   uG();
-  Qd();
-  FPA();
-  LGK();
-  jj6();
-  ipA();
-  h1();
-  A4();
-  yGK();
-  LT1();
-  RT1();
-  yT1();
-  IT1();
-  _$();
-  bGK();
-  Ze();
-  Zq();
-  eq();
-  C8();
   ((e1 = r($A(), 1)), (hz = r($A(), 1)));
 });

@@@ variable 'n_K' (was 'Zd6') — structural (72.4%)
--- pretty-v2.1.22.js:567387
+++ pretty-v2.1.23.js:480369
@@ -33,116 +33,5 @@
   PIK();
   df();
   xJ1();
-  tk();
-  BG();
-  PU6();
-  vk();
-  Rp6();
-  vIK();
-  ky();
-  kIK();
-  CIK();
-  LIK();
-  uB();
-  d2();
-  yIK();
-  SIK();
-  mIK();
-  QIK();
-  cIK();
-  ow();
-  QU6();
-  c6();
-  i1();
-  j8();
-  MBA();
-  _z();
-  xp();
-  ZH();
-  ASK();
-  zSK();
-  HSK();
-  UMA();
-  L3A();
-  XSK();
-  uy6();
-  LF6();
-  _SK();
-  GSK();
-  mp6();
-  sPA();
-  VFA();
-  xL6();
-  DSK();
-  Zp();
-  uL6();
-  cyA();
-  rt();
-  MSK();
-  Z_();
-  D5A();
-  FFA();
-  A4();
-  ku();
-  PZ();
-  UK();
-  dMA();
-  Mf1();
-  e3A();
-  sM();
-  O7A();
-  UK();
-  QcA();
-  NSK();
-  y9();
-  TSK();
-  nH();
-  kSK();
-  QF6();
-  rN1();
-  Pf();
-  LSK();
-  H_1();
-  ySK();
-  SqA();
-  bUA();
-  qM6();
-  bL6();
-  Gz();
-  Ze();
-  xSK();
-  BSK();
-  FSK();
-  pSK();
-  cSK();
-  nSK();
-  oSK();
-  AhK();
-  YhK();
-  hH();
-  whK();
-  HhK();
-  JmK();
-  rB6();
-  $mK();
-  ZmK();
-  vmK();
-  CmK();
-  ymK();
-  SmK();
-  bmK();
-  pM1();
-  umK();
-  mmK();
-  FmK();
-  UmK();
-  dmK();
-  imK();
-  omK();
-  tmK();
-  KgK();
-  YgK();
-  HgK();
-  JgK();
   ((M4 = r($A(), 1)), (A8 = r($A(), 1)));
 });

@@@ variable 'Tp6' (was 'VgK') — structural (72.4%)
--- pretty-v2.1.22.js:568028
+++ pretty-v2.1.23.js:546479
@@ -8,5 +8,23 @@
   mK();
   eq();
   Zq();
+  g4();
+  ym();
+  iH();
+  NG();
+  YK();
+  q6();
+  UK();
+  $8();
+  n_();
+  x4();
+  CS();
+  sMA();
+  Ud();
+  Jw();
+  i2();
+  nD();
+  Np6();
+  CpA();
   ((ev = r($A(), 1)), (ik1 = r($A(), 1)));
 });

@@@ variable 'zFK' (was 'egK') — structural (72.4%)
--- pretty-v2.1.22.js:570119
+++ pretty-v2.1.23.js:567258
@@ -5,10 +5,5 @@
   UK();
   v1();
   ZH();
-  CK();
-  Ow();
-  s1();
-  Pv1();
-  h1();
   ((S7z = r($A(), 1)), (tgK = r($A(), 1)));
 });

@@@ function 'c7K' (was 'b4K') — structural (72.1%)
--- pretty-v2.1.22.js:414180
+++ pretty-v2.1.23.js:414501
@@ -3,7 +3,7 @@
   { verbose: K, tools: q, terminalSize: Y, inProgressToolCallCount: z },
 ) {
   let w = A.at(-1);
-  if (!w || !w.data || !w.data.output)
+  if (!w || !w.data)
     return QY.createElement(
       E6,
       { height: 1 },
@@ -15,6 +15,7 @@
     output: H.output,
     elapsedTimeSeconds: H.elapsedTimeSeconds,
     totalLines: H.totalLines,
+    timeoutMs: H.timeoutMs,
     verbose: K,
   });
 }

@@@ function 'gyK' (was 'xRK') — structural (72.0%)
--- pretty-v2.1.22.js:551949
+++ pretty-v2.1.23.js:553224
@@ -4,7 +4,12 @@
   if (K === q) return null;
   let { stdout: Y, code: z } = await L6(
     "gh",
-    ["pr", "view", "--json", "number,url,reviewDecision,isDraft,headRefName"],
+    [
+      "pr",
+      "view",
+      "--json",
+      "number,url,reviewDecision,isDraft,headRefName,state",
+    ],
     { timeout: C1z, preserveOutputOnError: !1 },
   );
   if (z !== 0 || !Y.trim()) return null;
@@ -20,7 +25,8 @@
     return {
       number: w.number,
       url: w.url,
-      reviewState: L1z(w.isDraft, w.reviewDecision),
+      reviewState:
+        w.state === "MERGED" ? "merged" : x8z(w.isDraft, w.reviewDecision),
     };
   } catch {
     return null;

@@@ function 'JPK' (was 'wMK') — structural (72.0%)
--- pretty-v2.1.22.js:503439
+++ pretty-v2.1.23.js:504472
@@ -7,7 +7,7 @@
     H = I8.isSandboxingEnabled(),
     J = Gv1(),
     O = tM(),
-    [X] = V6(),
+    X = F1((JA) => JA.agent),
     $ = D1(),
     _;
   try {
@@ -32,9 +32,9 @@
           "report the issue at https://github.com/anthropics/claude-code/issues",
         PACKAGE_URL: "@anthropic-ai/claude-code",
         README_URL: "https://code.claude.com/docs/en/overview",
-        VERSION: "2.1.22",
+        VERSION: "2.1.23",
         FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-        BUILD_TIME: "2026-01-28T06:33:34Z",
+        BUILD_TIME: "2026-01-29T00:18:20Z",
       }.VERSION
     )
       return;
@@ -47,10 +47,10 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.22",
+            VERSION: "2.1.23",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-01-28T06:33:34Z",
+            BUILD_TIME: "2026-01-29T00:18:20Z",
           }.VERSION
         )
           return jA;
@@ -61,10 +61,10 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.22",
+            VERSION: "2.1.23",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-01-28T06:33:34Z",
+            BUILD_TIME: "2026-01-29T00:18:20Z",
           }.VERSION,
         };
       }),
@@ -86,7 +86,7 @@
       billingType: E,
       agentName: R,
     } = P.current,
-    b = X.agent ?? R,
+    x = X ?? R,
     S = a9(T, Bg6 - 20);
   if (!W && !w && !j1(process.env.CLAUDE_CODE_FORCE_FULL_LOGO))
     return P8.createElement(

@@@ function 'a8z' (was 'u1z') — structural (71.8%)
--- pretty-v2.1.22.js:552602
+++ pretty-v2.1.23.js:553899
@@ -1,5 +1,5 @@
 function u1z(A) {
-  let K = s(49),
+  let K = s(51),
     {
       apiKeyStatus: q,
       debug: Y,
@@ -17,10 +17,12 @@
       toolPermissionContext: D,
       helpOpen: j,
       suppressHint: M,
+      isLoading: P,
       tasksSelected: P,
       teamsSelected: V,
       diffSelected: N,
       loopSelected: T,
+      teammateFooterIndex: R,
       ideSelection: E,
       mcpClients: R,
       isPasting: b,
@@ -108,7 +110,9 @@
     K[26] !== P ||
     K[27] !== V ||
     K[28] !== D ||
-    K[29] !== w
+    K[29] !== N ||
+    K[30] !== D ||
+    K[31] !== w
   )
     ((OA = hW.createElement(gRK, {
       exitMessage: z,
@@ -116,10 +120,12 @@
       mode: H,
       toolPermissionContext: D,
       suppressHint: wA,
+      isLoading: P,
       tasksSelected: P,
       teamsSelected: V,
       diffSelected: N,
       loopSelected: T,
+      teammateFooterIndex: R,
       isPasting: d,
       isSearching: x,
       historyQuery: F,
@@ -140,19 +146,24 @@
       (K[27] = V),
       (K[28] = D),
       (K[29] = w),
-      (K[30] = OA));
-  else OA = K[30];
+      (K[30] = D),
+      (K[31] = w),
+      (K[32] = a));
+  else a = K[32];
   let WA;
-  if (K[31] !== HA || K[32] !== OA)
-    ((WA = hW.createElement(I, { flexDirection: "column" }, HA, OA)),
-      (K[31] = HA),
-      (K[32] = OA),
-      (K[33] = WA));
-  else WA = K[33];
+  if (K[33] !== _A || K[34] !== a)
+    ((JA = BW.createElement(
+      S,
+      { flexDirection: "column", flexShrink: 0 },
+      _A,
+      a,
+    )),
+      (K[33] = _A),
+      (K[34] = a),
+      (K[35] = JA));
+  else JA = K[35];
   let a;
   if (
-    K[34] !== q ||
-    K[35] !== J ||
     K[36] !== Y ||
     K[37] !== E ||
     K[38] !== O ||
@@ -161,7 +172,9 @@
     K[41] !== B ||
     K[42] !== $ ||
     K[43] !== _ ||
-    K[44] !== X
+    K[44] !== $ ||
+    K[45] !== _ ||
+    K[46] !== X
   )
     ((a = hW.createElement(uLK, {
       apiKeyStatus: q,
@@ -176,8 +189,6 @@
       mcpClients: R,
       isInputWrapped: o,
     })),
-      (K[34] = q),
-      (K[35] = J),
       (K[36] = Y),
       (K[37] = E),
       (K[38] = O),
@@ -187,19 +198,26 @@
       (K[42] = $),
       (K[43] = _),
       (K[44] = X),
-      (K[45] = a));
-  else a = K[45];
+      (K[45] = _),
+      (K[46] = X),
+      (K[47] = jA));
+  else jA = K[47];
   let _A;
-  if (K[46] !== WA || K[47] !== a)
+  if (K[48] !== JA || K[49] !== jA)
     ((_A = hW.createElement(
       I,
-      { flexDirection: "row", justifyContent: "space-between", paddingX: 2 },
+      {
+        flexDirection: "row",
+        justifyContent: "space-between",
+        paddingX: 2,
+        gap: 1,
+      },
       WA,
       a,
     )),
-      (K[46] = WA),
-      (K[47] = a),
-      (K[48] = _A));
-  else _A = K[48];
+      (K[48] = JA),
+      (K[49] = jA),
+      (K[50] = MA));
+  else MA = K[50];
   return _A;
 }

@@@ function 'cP2' (was 'uM2') — structural (71.6%)
--- pretty-v2.1.22.js:423030
+++ pretty-v2.1.23.js:423352
@@ -62,7 +62,7 @@
                   if (V) {
                     let N = await z.getAppState(),
                       T = pj(N.toolPermissionContext, j);
-                    V(T);
+                    f(T, { preserveMode: !0 });
                   }
                 }
                 let P = M?.trim();

@@@ function 'd4z' (was 'I6z') — structural (71.2%)
--- pretty-v2.1.22.js:556041
+++ pretty-v2.1.23.js:557262
@@ -49,13 +49,36 @@
     [YA, JA] = RK.useState(!1),
     [AA, t] = RK.useState({ show: !1 }),
     [ZA, kA] = RK.useState(Z.length),
-    [XA, LA] = V6(),
-    VA = cM(XA),
+    vA = D0(),
+    RA = p4(),
+    fA = F1((j1) => j1.tasks),
+    LA = F1((j1) => j1.teamContext),
+    SA = F1((j1) => j1.queuedCommands),
+    xA = F1((j1) => j1.gitDiff),
+    iA = F1((j1) => j1.promptSuggestion),
+    lA = F1((j1) => j1.speculation),
+    v1 = F1((j1) => j1.speculationSessionTimeSavedMs),
+    I1 = F1((j1) => j1.viewingAgentTaskId),
+    Q1 = F1((j1) => j1.viewSelectionMode),
+    B1 = F1((j1) => j1.mainLoopModel),
+    C6 = F1((j1) => j1.mainLoopModelForSession),
+    w1 = F1((j1) => j1.thinkingEnabled),
+    $1 = OB(vA.getState()),
     EA = VA?.identity.agentName,
     CA =
       VA?.identity.color && H$.includes(VA.identity.color)
         ? VA.identity.color
         : void 0,
+    c1 = VK.useMemo(
+      () =>
+        p3A(fA)
+          .filter((j1) => j1.status === "running")
+          .sort((j1, s6) =>
+            j1.identity.agentName.localeCompare(s6.identity.agentName),
+          ),
+      [fA],
+    ),
+    w6 = c1.length > 0 || $1 !== void 0,
     dA = RK.useMemo(() => {
       if (VA) return { ...q, mode: VA.permissionMode };
       return q;
@@ -84,6 +107,7 @@
     [S6, B6] = RK.useState(!1),
     [J1, $1] = RK.useState(!1),
     [C1, P1] = RK.useState(!1),
+    [Y7, T7] = VK.useState(0),
     [z6, J6] = RK.useState(!1),
     [TA, fA] = RK.useState(!1),
     [cA, w1] = RK.useState(!1),
@@ -106,19 +130,14 @@
     T8 = RK.useMemo(() => {
       if (!D8()) return [];
       if (qm()) return [];
-      if (!XA.teamContext) return [];
-      let H6 = Object.values(XA.teamContext.teammates).filter(
+      if (!LA) return [];
+      let j1 = Object.values(LA.teammates).filter(
         (N8) => N8.name !== "team-lead",
       ).length;
       return [
-        {
-          name: XA.teamContext.teamName,
-          memberCount: H6,
-          runningCount: 0,
-          idleCount: 0,
-        },
+        { name: LA.teamName, memberCount: j1, runningCount: 0, idleCount: 0 },
       ];
-    }, [XA.teamContext]),
+    }, [LA]),
     {
       suggestion: c4,
       markAccepted: k4,
@@ -140,9 +159,9 @@
     }, [d8, w]),
     w3 = RK.useMemo(() => {
       if (!D8()) return [];
-      if (!XA.teamContext?.teammates) return [];
+      if (!LA?.teammates) return [];
       let H6 = [],
-        N8 = XA.teamContext.teammates;
+        s6 = LA.teammates;
       if (!N8) return H6;
       let p4 = /(^|\s)@([\w-]+)/g,
         x4;
@@ -158,7 +177,7 @@
         }
       }
       return H6;
-    }, [d8, XA.teamContext]),
+    }, [Q8, LA]),
     KY = RK.useMemo(() => {
       let H6 = [];
       if (WA && V1 && !y1)
@@ -299,21 +318,23 @@
     if (WA) d9();
   }, [WA, d9]);
   function Y8(H6) {
-    (u(H6 === "tasks"), o(H6 === "diff"), P1(H6 === "loop"));
+    if (
+      (u(j1 === "tasks"), r(j1 === "diff"), D8(j1 === "loop"), j1 === "tasks")
+    )
+      T7(0);
   }
   let f7 = !1;
   function S3() {
     if (uA.length > 1) return;
     if (!F4) return;
-    if (XA.queuedCommands.some((p4) => t$1(p4.mode))) {
+    if (SA.some((_4) => f_1(_4.mode))) {
       _4();
       return;
     }
     if (d) {
       if (T8.length > 0) (B6(!0), Y8("none"));
       else if (
-        Object.values(XA.tasks).filter((x4) => x4.status === "running").length >
-        0
+        Object.values(fA).filter((t7) => t7.status === "running").length > 0
       )
         Y8("tasks");
       else if (f7) Y8("loop");
@@ -321,9 +342,7 @@
       return;
     }
     if (S6) {
-      let p4 = Object.values(XA.tasks).filter(
-        (x4) => x4.status === "running",
-      ).length;
+      let _4 = Object.values(fA).filter((t7) => t7.status === "running").length;
       if ((B6(!1), p4 > 0)) Y8("tasks");
       else if (f7) Y8("loop");
       else Y8("none");
@@ -349,13 +368,8 @@
     if (uA.length > 1) return;
     if (!P4) return;
     if (d1) return;
-    let H6 = Object.values(XA.tasks).filter(
-        (S5) => S5.status === "running",
-      ).length,
-      N8 =
-        V4("tengu_code_diff_cli", !1) &&
-        XA.gitDiff.stats &&
-        XA.gitDiff.stats.filesCount > 0;
+    let j1 = Object.values(fA).filter((C5) => C5.status === "running").length,
+      s6 = G4("tengu_code_diff_cli", !1) && xA.stats && xA.stats.filesCount > 0;
     if (C1) {
       if (H6 > 0) Y8("tasks");
       else if (T8.length > 0) (B6(!0), Y8("none"));
@@ -398,28 +412,27 @@
       async (H6, N8 = !1) => {
         if (Q || S6 || d || C1) return;
         let p4 = Object.values(T).some((K8) => K8.type === "image"),
-          x4 = XA.promptSuggestion.text;
+          t7 = iA.text;
         if ((H6.trim() === "" || H6 === x4) && x4 && !p4) {
-          if (XA.speculation.status === "active") {
+          if (lA.status === "active") {
             (k4(),
               HA(
                 x4,
                 { setCursorOffset: kA, clearBuffer: M6, resetHistory: H7 },
                 {
-                  state: XA.speculation,
-                  speculationSessionTimeSavedMs:
-                    XA.speculationSessionTimeSavedMs,
+                  state: lA,
+                  speculationSessionTimeSavedMs: v1,
                   setAppState: LA,
                 },
               ));
             return;
           }
-          if (XA.promptSuggestion.shownAt > 0) (k4(), (H6 = x4));
+          if (iA.shownAt > 0) (kY(), (j1 = t7));
         }
         if (D8()) {
           let K8 = zyK(H6);
           if (K8) {
-            let Q4 = wyK(K8.recipientName, K8.message, XA.teamContext, F3);
+            let hz = XIK(Yq.recipientName, Yq.message, LA, Q3);
             if (Q4.success) {
               (t4({
                 key: "direct-message-sent",
@@ -440,9 +453,9 @@
           H5.suggestions.length > 0 &&
           H5.suggestions.every((K8) => K8.description === "directory");
         if (H5.suggestions.length > 0 && !N8 && !p5 && !p4) return;
-        if (XA.promptSuggestion.text && XA.promptSuggestion.shownAt > 0) wq(H6);
+        if (iA.text && iA.shownAt > 0) gq(j1);
         u7("stash-hint");
-        let a6 = FW7(XA);
+        let C9 = cD7(vA.getState());
         if (D8()) {
           if (a6.type === "viewed" && OA) {
             (n("tengu_transcript_input_to_teammate", {}),
@@ -460,7 +473,27 @@
           resetHistory: H7,
         });
       },
-      [XA, Q, S6, d, C1, H5.suggestions, HA, OA, M6, H7, wq, LA, k4, T, u7],
+      [
+        iA,
+        lA,
+        v1,
+        LA,
+        vA,
+        Q,
+        f1,
+        d,
+        e8,
+        d4.suggestions,
+        qA,
+        HA,
+        ZA,
+        dA,
+        gq,
+        RA,
+        kY,
+        T,
+        z4,
+      ],
     ),
     DA = Object.values(T).some((H6) => H6.type === "image"),
     {
@@ -486,8 +519,8 @@
     }),
     S1 = W === "prompt" && uA.length === 0 && c4;
   if (S1) Hq();
-  if (XA.promptSuggestion.text && !c4 && XA.promptSuggestion.shownAt === 0)
-    (DL("timing", XA.promptSuggestion.text),
+  if (iA.text && !_9 && iA.shownAt === 0)
+    (rS("timing", iA.text),
       LA((H6) => ({
         ...H6,
         promptSuggestion: {
@@ -613,11 +646,12 @@
       if ((T1((H6) => !H6), PA)) SA(!1);
     }, [PA]),
     wJ = RK.useCallback(() => {
-      if (D8() && VA && XA.viewingAgentTaskId) {
+      if (q.mode === "coordinator") return;
+      if (b8() && $1 && I1) {
         let p4 = { ...q, mode: VA.permissionMode },
           x4 = mVA(p4, void 0);
         n("tengu_mode_cycle", { to: x4 });
-        let S5 = XA.viewingAgentTaskId;
+        let C5 = I1;
         if (
           (LA((p5) => {
             let a6 = p5.tasks[S5];
@@ -633,7 +667,7 @@
           SA(!1);
         return;
       }
-      let H6 = mVA(q, XA.teamContext);
+      let j1 = eVA(q, LA);
       if (
         (n("tengu_mode_cycle", { to: H6 }), q.mode === "plan" && H6 !== "plan")
       )
@@ -642,9 +676,18 @@
         (Fn6(!0), fnA(!0));
       if (H6 === "plan") D6((p4) => ({ ...p4, lastPlanModeUse: Date.now() }));
       if (H6 === "acceptEdits") i7("auto-accept-mode");
-      let N8 = WY(q, { type: "setMode", mode: OF(H6), destination: "session" });
-      if ((Y(N8), ly6(H6, XA.teamContext?.teamName), PA)) SA(!1);
-    }, [q, XA.teamContext, XA.viewingAgentTaskId, VA, LA, Y, PA]),
+      let s6 = VF(j1);
+      if (
+        (RA((_4) => ({
+          ..._4,
+          toolPermissionContext: { ..._4.toolPermissionContext, mode: s6 },
+        })),
+        Y({ ...q, mode: s6 }),
+        LI6(j1, LA?.teamName),
+        MA)
+      )
+        hA(!1);
+    }, [q, LA, I1, $1, RA, Y, MA]),
     Bz = RK.useCallback(() => {
       RN1().then((H6) => {
         if (H6) (i7("image-paste"), c1(H6.base64, H6.mediaType));
@@ -698,7 +741,7 @@
       () => {
         o3A(LA);
       },
-      { context: "Global", isActive: !J && XA.speculation.status === "active" },
+      { context: "Global", isActive: !J && lA.status === "active" },
     ));
   let HJ = vp6(T);
   O7(
@@ -732,25 +775,29 @@
       "footer:next": () => {
         if (C1) {
           if (
-            Object.values(XA.tasks).filter((N8) => N8.status === "running")
-              .length > 0
+            Object.values(fA).filter((s6) => s6.status === "running").length > 0
           )
             Y8("tasks");
           else if (T8.length > 0) (B6(!0), Y8("none"));
           else if (V4("tengu_code_diff_cli", !1)) Y8("diff");
         } else if (Q) {
+          if (w6) {
+            let j1 = 1 + c1.length;
+            T7((s6) => (s6 + 1) % j1);
+            return;
+          }
           if (T8.length > 0) (B6(!0), Y8("none"));
           else if (
             V4("tengu_code_diff_cli", !1) &&
-            XA.gitDiff.stats &&
-            XA.gitDiff.stats.filesCount > 0
+            xA.stats &&
+            xA.stats.filesCount > 0
           )
             Y8("diff");
         } else if (S6) {
           if (
             V4("tengu_code_diff_cli", !1) &&
-            XA.gitDiff.stats &&
-            XA.gitDiff.stats.filesCount > 0
+            xA.stats &&
+            xA.stats.filesCount > 0
           )
             (B6(!1), Y8("diff"));
         }
@@ -759,24 +806,34 @@
         if (d) {
           if (T8.length > 0) (B6(!0), Y8("none"));
           else if (
-            Object.values(XA.tasks).filter((N8) => N8.status === "running")
-              .length > 0
+            Object.values(fA).filter((s6) => s6.status === "running").length > 0
           )
             Y8("tasks");
           else if (f7) Y8("loop");
         } else if (S6) {
-          let H6 = Object.values(XA.tasks).filter(
+          let j1 = Object.values(fA).filter(
             (N8) => N8.status === "running",
           ).length;
           if ((B6(!1), H6 > 0)) Y8("tasks");
           else if (f7) Y8("loop");
         } else if (Q) {
+          if (w6) {
+            let j1 = 1 + c1.length;
+            T7((s6) => (s6 - 1 + j1) % j1);
+            return;
+          }
           if (f7) Y8("loop");
         }
       },
       "footer:openSelected": () => {
-        if (XA.viewSelectionMode === "selecting-agent") return;
-        if (Q) (B(!0), Y8("none"));
+        if (Q1 === "selecting-agent") return;
+        if (Q && w6)
+          if (Y7 === 0) bm(RA);
+          else {
+            let j1 = c1[Y7 - 1];
+            if (j1) Be(j1.id, RA);
+          }
+        else if (Q) (B(!0), E1("none"));
         else if (d && V4("tengu_code_diff_cli", !1))
           (n("tengu_code_change_view_opened", {}), F(!0), Y8("none"));
         else if (S6) ($1(!0), B6(!1));
@@ -823,7 +880,7 @@
         (D("prompt"), SA(!1));
       if (PA && Z === "" && (N8.backspace || N8.delete)) SA(!1);
       if (N8.escape) {
-        if (XA.speculation.status === "active") {
+        if (lA.status === "active") {
           o3A(LA);
           return;
         }
@@ -836,7 +893,7 @@
           return;
         }
         if (lJ) return;
-        if (XA.queuedCommands.some((x4) => t$1(x4.mode))) {
+        if (SA.some((t7) => f_1(t7.mode))) {
           _4();
           return;
         }
@@ -850,7 +907,6 @@
     x$ = S1 && c4 ? c4 : U4,
     BW = RK.useMemo(() => {
       if (!S1 || !c4) return;
-      let H6 = XA.speculation;
       if (H6.status !== "active") return;
       let N8 =
           H6.boundary !== null ? H6.boundary.completedAt - H6.startTime : null,
@@ -858,10 +914,11 @@
       return g4.createElement(AIK, {
         suggestion: c4,
         isSpeculating: H6.boundary === null,
+        toolUseCount: lA.toolUseCount,
         timeSavedMs: N8,
         availableWidth: p4,
       });
-    }, [S1, c4, XA.speculation, yP]),
+    }, [NH, _9, lA, yX]),
     OG = RK.useMemo(
       () =>
         Z.includes(`
@@ -889,14 +946,14 @@
         I,
         { flexDirection: "column", marginTop: 1 },
         g4.createElement(vPA, {
-          initial: XA.mainLoopModel,
-          sessionModel: XA.mainLoopModelForSession,
+          initial: B1,
+          sessionModel: C6,
           onSelect: IO,
           onCancel: NX,
           isStandaloneCommand: !0,
         }),
       );
-    }, [iA, XA.mainLoopModel, XA.mainLoopModelForSession, IO, NX]),
+    }, [E8, B1, C6, M8, V7]),
     X5 = RK.useCallback(
       (H6) => {
         (LA((N8) => ({ ...N8, thinkingEnabled: H6 })),
@@ -925,13 +982,13 @@
         I,
         { flexDirection: "column", marginTop: 1 },
         g4.createElement(tyK, {
-          currentValue: XA.thinkingEnabled ?? !0,
+          currentValue: w1 ?? !0,
           onSelect: X5,
           onCancel: c9,
           isMidConversation: X.some((H6) => H6.type === "assistant"),
         }),
       );
-    }, [f1, XA.thinkingEnabled, X5, c9, X.length]);
+    }, [I3, w1, G9, CY, X.length]);
   if (S)
     return g4.createElement(Ev1, {
       onDone: () => {
@@ -1033,7 +1090,6 @@
     I,
     { flexDirection: "column", marginTop: 1 },
     g4.createElement(xyK, null),
-    g4.createElement(ByK, null),
     g4.createElement(gyK, { hasStash: j !== void 0 }),
     g4.createElement(iyK, {
       pastedContents: T,
@@ -1115,10 +1171,12 @@
       toolPermissionContext: dA,
       helpOpen: PA,
       suppressHint: Z.length > 0,
+      isLoading: J,
       tasksSelected: Q,
       teamsSelected: S6,
       diffSelected: d,
       loopSelected: C1,
+      teammateFooterIndex: Y7,
       ideSelection: K,
       mcpClients: N,
       isPasting: TA,

@@@ function 'I7K' (was 'P4K') — structural (70.9%)
--- pretty-v2.1.22.js:412522
+++ pretty-v2.1.23.js:412810
@@ -6,6 +6,7 @@
   permissionMode: z,
   querySource: w,
   queryTracking: H,
+  effortValue: J,
 }) {
   n("tengu_api_query", {
     model: A,
@@ -17,6 +18,7 @@
     permissionMode: z,
     querySource: w,
     ...(H ? { queryChainId: H.chainId, queryDepth: H.depth } : {}),
+    effortValue: J,
     ...yy6(),
   });
 }

@@@ function 'bqz' (was 'Z7z') — structural (70.2%)
--- pretty-v2.1.22.js:568190
+++ pretty-v2.1.23.js:569899
@@ -18,8 +18,8 @@
       { fileId: q, path: z, success: !0, bytesWritten: w.length }
     );
   } catch (w) {
-    let H = w instanceof Error ? w.message : String(w);
-    if ((Dd6(`Failed to download file ${q}: ${H}`), w instanceof Error)) KA(w);
-    return { fileId: q, path: z, success: !1, error: H };
+    if ((qc6(`Failed to download file ${q}: ${IFK(w)}`), w instanceof Error))
+      KA(w);
+    return { fileId: q, path: z, success: !1, error: IFK(w) };
   }
 }

@@@ function 'g3z' (was 'Mqz') — structural (70.1%)
--- pretty-v2.1.22.js:579556
+++ pretty-v2.1.23.js:581274
@@ -14,6 +14,7 @@
   skipWebFetchPreflight: Z,
   githubActionInputs: G,
   dangerouslySkipPermissionsPassed: W,
+  permissionMode: D,
   modeIsBypass: D,
   allowDangerouslySkipPermissionsPassed: j,
   systemPromptFlag: M,
@@ -38,6 +39,7 @@
       skipWebFetchPreflight: Z,
       ...(G && { githubActionInputs: G }),
       dangerouslySkipPermissionsPassed: W,
+      permissionMode: D,
       modeIsBypass: D,
       allowDangerouslySkipPermissionsPassed: j,
       ...(M && { systemPromptFlag: M }),

@@@ function 'SIK' (was 'LyK') — structural (70.0%)
--- pretty-v2.1.22.js:554943
+++ pretty-v2.1.23.js:556257
@@ -1,5 +1,6 @@
 function LyK({ input: A, submitCount: K, viewingAgentName: q }) {
-  let [{ queuedCommands: Y, promptSuggestionEnabled: z }] = V6();
+  let Y = F1((H) => H.queuedCommands),
+    z = F1((H) => H.promptSuggestionEnabled);
   return CyK.useMemo(() => {
     if (A !== "") return;
     if (q)

@@@ function 'pSK' (was 'FIK') — structural (69.6%)
--- pretty-v2.1.22.js:558403
+++ pretty-v2.1.23.js:559919
@@ -1,7 +1,10 @@
 function FIK() {
-  let [A, K] = V6(),
-    q = cM(A),
-    Y = A.viewingAgentTaskId,
+  let A = p4(),
+    K = F1((O) => O.viewingAgentTaskId),
+    q = F1((O) => O.tasks),
+    Y = K ? q[K] : void 0,
+    z = Y && W_(Y) ? Y : void 0,
+    w = K,
     z = q?.status,
     w = q?.error;
   gIK.useEffect(() => {

@@@ variable 'cyK' (was 'NSK') — structural (69.2%)
--- pretty-v2.1.22.js:560672
+++ pretty-v2.1.23.js:553733
@@ -18,6 +18,5 @@
   j8();
   BS();
   Km();
-  TJ();
   fc = r($A(), 1);
 });

@@@ variable 'bhK' (was 'FmK') — structural (69.2%)
--- pretty-v2.1.22.js:565298
+++ pretty-v2.1.23.js:562536
@@ -1,7 +1,5 @@
 var FmK = C(() => {
   lA();
   Jw();
-  yS();
-  l6();
   Fk1 = r($A(), 1);
 });

@@@ variable 'MFK' (was 'Pd6') — structural (69.2%)
--- pretty-v2.1.22.js:569418
+++ pretty-v2.1.23.js:569242
@@ -1,6 +1,5 @@
 var Pd6 = C(() => {
   lA();
   BA();
-  X3();
   d6 = r($A(), 1);
 });

@@@ variable 'EQK' (was 'Nd6') — structural (69.2%)
--- pretty-v2.1.22.js:570740
+++ pretty-v2.1.23.js:572577
@@ -2,5 +2,13 @@
   lA();
   BA();
   BA();
+  I8();
+  WZ8();
+  Xc6();
+  l1();
+  nK();
+  q5();
+  Dq();
+  t3();
   fd6 = r($A(), 1);
 });

@@@ variable 'KpK' (was 'VFK') — structural (69.2%)
--- pretty-v2.1.22.js:570958
+++ pretty-v2.1.23.js:577792
@@ -4,6 +4,5 @@
   B8();
   Nd6();
   i1();
-  Z9();
   ek1 = r($A(), 1);
 });

@@@ function 'gk1' (was '$IK') — structural (68.8%)
--- pretty-v2.1.22.js:557646
+++ pretty-v2.1.23.js:558926
@@ -1,16 +1,27 @@
-function $IK(A) {
+function gk1(A, K) {
   switch (A.type) {
     case "assistant":
       return { type: "message", message: m6z(A) };
-    case "user":
-      return (
-        h("[sdkMessageAdapter] Ignoring user message (added locally)"),
-        { type: "ignored" }
-      );
+    case "user": {
+      if (K?.convertToolResults) {
+        let q = A.message?.content;
+        if (Array.isArray(q))
+          return {
+            type: "message",
+            message: t1({
+              content: q,
+              toolUseResult: A.tool_use_result,
+              uuid: A.uuid,
+            }),
+          };
+      }
+      return { type: "ignored" };
+    }
     case "stream_event":
       return { type: "stream_event", event: g6z(A) };
     case "result":
-      return { type: "message", message: F6z(A) };
+      if (A.subtype !== "success") return { type: "message", message: t4z(A) };
+      return { type: "ignored" };
     case "system":
       if (A.subtype === "init") return { type: "message", message: Q6z(A) };
       if (A.subtype === "status") {

@@@ function 'Md6' (was 'Sp6') — structural (68.8%)
--- pretty-v2.1.22.js:558111
+++ pretty-v2.1.23.js:559626
@@ -13,13 +13,17 @@
       inputMode: _,
       inputValue: Z,
     } = A,
-    [G, W] = V6(),
+    Z = D0(),
+    W = p4(),
+    D = F1((Q) => Q.queuedCommands.length),
+    j = void 0,
+    M = F1((Q) => Q.viewSelectionMode),
     D = RIK.useCallback(() => {
       if (w !== void 0 && !w.aborted) {
         (n("tengu_cancel", {}), K(() => []), q());
         return;
       }
-      if (G.queuedCommands.length > 0) {
+      if (Z.getState().queuedCommands.length > 0) {
         if (H) {
           H();
           return;
@@ -29,19 +33,18 @@
     }, [G, W, w, H, K, q]),
     j = Mj7(),
     M = w !== void 0 && !w.aborted,
-    P = G.queuedCommands.length > 0,
+    T = D > 0,
     V = !1,
     N = _ !== void 0 && _ !== "prompt" && !Z,
     T = !1,
-    E = G.viewSelectionMode === "viewing-agent",
     R =
       z !== "transcript" &&
-      !X &&
       !Y &&
       !O &&
       !$ &&
       !j &&
       !E &&
+      M !== "viewing-agent" &&
       !($e() && J === "INSERT") &&
       (M || P || !1 || T),
     b = R && !N,

@@@ function 'p89' (was 'b69') — structural (68.6%)
--- pretty-v2.1.22.js:185476
+++ pretty-v2.1.23.js:185575
@@ -1,5 +1,5 @@
 function b69(A) {
   if (iyA() === "darwin")
-    return `${S8("warning", A)("Warp requires manual configuration:")}${D5}${D5}${S8("success", A)("For Alt+T (thinking) and Alt+P (model picker):")}${D5}  Settings → Features → Enable "Left Option key is meta"${D5}${D5}${O1.dim("Note: Warp does not support custom Shift+Enter keybindings.")}${D5}${O1.dim("Use backslash (\\) + Enter for multi-line input.")}${D5}`;
-  return `${S8("warning", A)("Warp does not support custom Shift+Enter keybindings.")}${D5}${O1.dim("Use backslash (\\) + Enter for multi-line input.")}${D5}`;
+    return `${h8("warning", A)("Warp requires manual configuration:")}${_5}${_5}${h8("success", A)("For Alt+T (thinking) and Alt+P (model picker):")}${_5}  Settings → Features → Enable "Left Option key is meta"${_5}${_5}${O1.dim("Note: Warp does not support custom Shift+Enter keybindings.")}${_5}${O1.dim("Use backslash (\\\\) + Enter for multi-line input.")}${_5}`;
+  return `${h8("warning", A)("Warp does not support custom Shift+Enter keybindings.")}${_5}${O1.dim("Use backslash (\\\\) + Enter for multi-line input.")}${_5}`;
 }

@@@ function 'uUK' (was 'LQK') — structural (68.5%)
--- pretty-v2.1.22.js:574576
+++ pretty-v2.1.23.js:576301
@@ -1,6 +1,6 @@
 async function LQK() {
   (n("tengu_update_check", {}),
-    k7(`Current version: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.22", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T06:33:34Z" }.VERSION}
+    v7(`Current version: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.23", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-29T00:18:20Z" }.VERSION}
 `));
   let A = oq()?.autoUpdatesChannel ?? "latest";
   (k7(`Checking for updates to ${A} version...
@@ -92,16 +92,16 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.22",
+            VERSION: "2.1.23",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-01-28T06:33:34Z",
+            BUILD_TIME: "2026-01-29T00:18:20Z",
           }.VERSION,
           $,
           { loose: !0 },
         )
       )
-        (k7(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.22", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T06:33:34Z" }.VERSION} → ${$}
+        (v7(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.23", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-29T00:18:20Z" }.VERSION} → ${$}
 `),
           k7(`
 `),
@@ -127,16 +127,16 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.22",
+            VERSION: "2.1.23",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-01-28T06:33:34Z",
+            BUILD_TIME: "2026-01-29T00:18:20Z",
           }.VERSION,
           $,
           { loose: !0 },
         )
       )
-        (k7(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.22", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T06:33:34Z" }.VERSION} → ${$}
+        (v7(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.23", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-29T00:18:20Z" }.VERSION} → ${$}
 `),
           k7(`
 `),
@@ -162,16 +162,16 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.22",
+            VERSION: "2.1.23",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-01-28T06:33:34Z",
+            BUILD_TIME: "2026-01-29T00:18:20Z",
           }.VERSION,
           $,
           { loose: !0 },
         )
       )
-        (k7(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.22", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T06:33:34Z" }.VERSION} → ${$}
+        (v7(`Update available: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.23", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-29T00:18:20Z" }.VERSION} → ${$}
 `),
           k7(`
 `),
@@ -253,14 +253,14 @@
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.22",
+          VERSION: "2.1.23",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-01-28T06:33:34Z",
+          BUILD_TIME: "2026-01-29T00:18:20Z",
         }.VERSION
       )
         k7(
           O1.green(
-            `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.22", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T06:33:34Z" }.VERSION})`,
+            `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.23", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-29T00:18:20Z" }.VERSION})`,
           ) +
             `
 `,
@@ -268,7 +268,7 @@
       else
         (k7(
           O1.green(
-            `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.22", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T06:33:34Z" }.VERSION} to version ${X.latestVersion}`,
+            `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.23", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-29T00:18:20Z" }.VERSION} to version ${X.latestVersion}`,
           ) +
             `
 `,
@@ -291,10 +291,10 @@
   if (q.installMethod !== "native") await kpA();
   (h("update: Checking npm registry for latest version"),
     h(
-      `update: Package URL: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.22", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T06:33:34Z" }.PACKAGE_URL}`,
+      `update: Package URL: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.23", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-29T00:18:20Z" }.PACKAGE_URL}`,
     ));
   let Y = A === "stable" ? "stable" : "latest",
-    z = `npm view ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.22", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T06:33:34Z" }.PACKAGE_URL}@${Y} version`;
+    z = `npm view ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.23", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-29T00:18:20Z" }.PACKAGE_URL}@${Y} version`;
   h(`update: Running: ${z}`);
   let w = await fd(A);
   if ((h(`update: Latest version from npm: ${w || "FAILED"}`), !w)) {
@@ -322,18 +322,18 @@
           "report the issue at https://github.com/anthropics/claude-code/issues",
         PACKAGE_URL: "@anthropic-ai/claude-code",
         README_URL: "https://code.claude.com/docs/en/overview",
-        VERSION: "2.1.22",
+        VERSION: "2.1.23",
         FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-        BUILD_TIME: "2026-01-28T06:33:34Z",
+        BUILD_TIME: "2026-01-29T00:18:20Z",
       }.PACKAGE_URL &&
         !{
           ISSUES_EXPLAINER:
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.22",
+          VERSION: "2.1.23",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-01-28T06:33:34Z",
+          BUILD_TIME: "2026-01-29T00:18:20Z",
         }.PACKAGE_URL.startsWith("@anthropic"))
     )
       process.stderr.write(`  • Internal/development build not published to npm
@@ -352,9 +352,9 @@
           "report the issue at https://github.com/anthropics/claude-code/issues",
         PACKAGE_URL: "@anthropic-ai/claude-code",
         README_URL: "https://code.claude.com/docs/en/overview",
-        VERSION: "2.1.22",
+        VERSION: "2.1.23",
         FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-        BUILD_TIME: "2026-01-28T06:33:34Z",
+        BUILD_TIME: "2026-01-29T00:18:20Z",
       }.PACKAGE_URL || "@anthropic-ai/claude-code";
     (process.stderr.write(`  • Manually check: npm view ${X} version
 `),
@@ -369,20 +369,20 @@
         "report the issue at https://github.com/anthropics/claude-code/issues",
       PACKAGE_URL: "@anthropic-ai/claude-code",
       README_URL: "https://code.claude.com/docs/en/overview",
-      VERSION: "2.1.22",
+      VERSION: "2.1.23",
       FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-      BUILD_TIME: "2026-01-28T06:33:34Z",
+      BUILD_TIME: "2026-01-29T00:18:20Z",
     }.VERSION
   )
     (k7(
       O1.green(
-        `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.22", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T06:33:34Z" }.VERSION})`,
+        `Claude Code is up to date (${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.23", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-29T00:18:20Z" }.VERSION})`,
       ) +
         `
 `,
     ),
       await Eq(0));
-  (k7(`New version available: ${w} (current: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.22", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T06:33:34Z" }.VERSION})
+  (v7(`New version available: ${w} (current: ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.23", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-29T00:18:20Z" }.VERSION})
 `),
     k7(`Installing update...
 `));
@@ -429,7 +429,7 @@
     case "success":
       (k7(
         O1.green(
-          `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.22", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T06:33:34Z" }.VERSION} to version ${w}`,
+          `Successfully updated from ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.23", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-29T00:18:20Z" }.VERSION} to version ${w}`,
         ) +
           `
 `,
@@ -445,7 +445,7 @@
         (process.stderr.write(`Try manually updating with:
 `),
           process.stderr
-            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.22", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T06:33:34Z" }.PACKAGE_URL}
+            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.23", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-29T00:18:20Z" }.PACKAGE_URL}
 `));
       else
         (process.stderr.write(`Try running with sudo or fix npm permissions
@@ -464,7 +464,7 @@
         (process.stderr.write(`Try manually updating with:
 `),
           process.stderr
-            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.22", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T06:33:34Z" }.PACKAGE_URL}
+            .write(`  cd ~/.claude/local && npm update ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.23", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-29T00:18:20Z" }.PACKAGE_URL}
 `));
       else
         process.stderr

@@@ function 'CHK' (was 'LwK') — structural (68.4%)
--- pretty-v2.1.22.js:453326
+++ pretty-v2.1.23.js:453766
@@ -30,12 +30,37 @@
     let D = n3A(X, J, _7A);
     if (((H.current = v$A(H.current, D)), W)) w((M) => [...M, W]);
     let j = _?.boundary?.type === "complete";
-    return (
-      h(
+    if (
+      (h(
         `[Speculation] ${_?.boundary?.type ?? "incomplete"}, injected ${X.length} messages`,
       ),
-      { queryRequired: !j }
-    );
+      j && A.pipelinedSuggestion)
+    ) {
+      let {
+        text: M,
+        promptId: P,
+        generationRequestId: f,
+      } = A.pipelinedSuggestion;
+      (h(
+        `[Speculation] Promoting pipelined suggestion: "${M.slice(0, 50)}..."`,
+      ),
+        q((T) => ({
+          ...T,
+          promptSuggestion: {
+            text: M,
+            promptId: P,
+            shownAt: Date.now(),
+            acceptedAt: 0,
+            generationRequestId: f,
+          },
+        })));
+      let N = {
+        ...A.contextRef.current,
+        messages: [...A.contextRef.current.messages, t1({ content: Y }), ...X],
+      };
+      Sx6(M, N, q, !0);
+    }
+    return { queryRequired: !j };
   } catch (w) {
     return (
       KA(w instanceof Error ? w : Error("handleSpeculationAccept failed")),
@@ -53,6 +78,7 @@
             200,
           ),
           error_phase: "accept",
+          is_pipelined: A.isPipelined,
         },
       ),
       hUA(Vf1(A.id)),

@@@ function 'ux6' (was 'tb6') — structural (68.3%)
--- pretty-v2.1.22.js:532029
+++ pretty-v2.1.23.js:533101
@@ -4,7 +4,7 @@
     K = xA(),
     q = A;
   try {
-    if (K.existsSync(A)) q = K.realpathSync(A);
+    q = K.realpathSync(A);
   } catch {}
-  return cv(q, "claude") + xL;
+  return dv(q, xu6()) + FL;
 }

@@@ function 'Ug2' (was 'wm2') — structural (68.1%)
--- pretty-v2.1.22.js:497733
+++ pretty-v2.1.23.js:498767
@@ -1,23 +1,17 @@
 function wm2(A) {
   let K = s(7),
     { action: q, target: Y, onComplete: z } = A,
-    [w] = V6(),
+    w = F1(dg2),
     H = _e(),
     J = lT1.useRef(!1),
     O,
     X;
-  if (
-    K[0] !== q ||
-    K[1] !== w.mcp.clients ||
-    K[2] !== z ||
-    K[3] !== Y ||
-    K[4] !== H
-  )
+  if (K[0] !== q || K[1] !== w || K[2] !== z || K[3] !== Y || K[4] !== H)
     ((O = () => {
       if (J.current) return;
       J.current = !0;
       let $ = q === "enable",
-        _ = w.mcp.clients.filter(Hm2),
+        _ = w.filter(pg2),
         Z =
           Y === "all"
             ? _.filter((G) =>
@@ -39,9 +33,9 @@
           : `MCP server "${Y}" ${$ ? "enabled" : "disabled"}`,
       );
     }),
-      (X = [q, Y, w.mcp.clients, H, z]),
+      (X = [q, Y, w, H, z]),
       (K[0] = q),
-      (K[1] = w.mcp.clients),
+      (K[1] = w),
       (K[2] = z),
       (K[3] = Y),
       (K[4] = H),

@@@ function 'ak1' (was 'fk1') — structural (67.8%)
--- pretty-v2.1.22.js:559963
+++ pretty-v2.1.23.js:561582
@@ -1,5 +1,5 @@
 function fk1() {
-  let [, A] = V6(),
+  let A = p4(),
     K = Vk1.useCallback(async () => {
       try {
         let { enabled: q, disabled: Y, errors: z } = await bY(),

@@@ function 'uOK' (was 'mJK') — structural (67.3%)
--- pretty-v2.1.22.js:461971
+++ pretty-v2.1.23.js:462490
@@ -1,9 +1,5 @@
 function mJK({ file_path: A }) {
   let K = A ? zN1(A) : null;
   if (!K) return null;
-  return m5.createElement(
-    I,
-    { flexWrap: "nowrap", marginLeft: 1 },
-    m5.createElement(f, { dimColor: !0 }, K),
-  );
+  return $3.createElement(V, { dimColor: !0 }, " ", K);
 }

@@@ function 'zb' (was 'rh') — structural (67.1%)
--- pretty-v2.1.22.js:30983
+++ pretty-v2.1.23.js:30998
@@ -29,7 +29,6 @@
           (h(
             "rg EAGAIN error detected, retrying with single-threaded mode (-j 1)",
           ),
-            (L28 = !0),
             n("tengu_ripgrep_eagain_retry", {}),
             E28(
               A,
@@ -45,8 +44,6 @@
         let _ = J && J.trim().length > 0,
           Z = H.signal === "SIGTERM" || H.code === "ABORT_ERR",
           G = H.code === "ERR_CHILD_PROCESS_STDIO_MAXBUFFER",
-          W = H.code === 2,
-          D = (Z || G || W) && _,
           j = [];
         if (D) {
           if (
@@ -67,6 +64,15 @@
           H.code !== 2)
         )
           KA(H);
+        if (G && W.length === 0) {
+          z(
+            new fz8(
+              `Ripgrep search timed out after ${o6() === "wsl" ? 60 : 20} seconds. The search may have matched files but did not complete in time. Try searching a more specific path or pattern.`,
+              W,
+            ),
+          );
+          return;
+        }
         Y(j);
       };
       E28(A, K, q, (H, J, O) => {

@@@ function 'jI7' (was 'tR7') — structural (66.7%)
--- pretty-v2.1.22.js:340305
+++ pretty-v2.1.23.js:340826
@@ -1,5 +1,5 @@
 function tR7(A) {
-  let K = s(29),
+  let K = s(31),
     {
       message: q,
       messages: Y,
@@ -49,23 +49,27 @@
   else j = K[11];
   let M = j,
     P;
-  if (K[12] !== D || K[13] !== X)
-    ((P = !1), (K[12] = D), (K[13] = X), (K[14] = P));
-  else P = K[14];
-  let V;
-  if (K[15] !== M) ((V = !1), (K[15] = M), (K[16] = V));
+  if (K[12] !== z) ((P = GI7(z)), (K[12] = z), (K[13] = P));
+  else P = K[13];
+  let f = P,
+    N;
+  if (K[14] !== M || K[15] !== D)
+    ((N = !1), (K[14] = M), (K[15] = D), (K[16] = N));
   else V = K[16];
   let N;
-  if (K[17] !== G || K[18] !== P || K[19] !== V || K[20] !== $)
+  if (K[17] !== f) ((T = !1), (K[17] = f), (K[18] = T));
+  else T = K[18];
+  let C;
+  if (K[19] !== Z || K[20] !== N || K[21] !== T || K[22] !== $)
     ((N = up.createElement(I, { flexDirection: "column", width: $ }, G, P, V)),
-      (K[17] = G),
-      (K[18] = P),
       (K[19] = V),
       (K[20] = $),
-      (K[21] = N));
-  else N = K[21];
+      (K[21] = T),
+      (K[22] = $),
+      (K[23] = C));
+  else C = K[23];
   let T;
-  if (K[22] !== Y || K[23] !== z || K[24] !== X)
+  if (K[24] !== Y || K[25] !== z || K[26] !== X)
     ((T = up.createElement(
       j5A,
       null,
@@ -76,17 +80,17 @@
         verbose: X,
       }),
     )),
-      (K[22] = Y),
-      (K[23] = z),
       (K[24] = X),
-      (K[25] = T));
-  else T = K[25];
+      (K[25] = z),
+      (K[26] = X),
+      (K[27] = R));
+  else R = K[27];
   let E;
-  if (K[26] !== N || K[27] !== T)
+  if (K[28] !== C || K[29] !== R)
     ((E = up.createElement(I, { flexDirection: "column" }, N, T)),
-      (K[26] = N),
-      (K[27] = T),
-      (K[28] = E));
-  else E = K[28];
+      (K[28] = C),
+      (K[29] = R),
+      (K[30] = x));
+  else x = K[30];
   return E;
 }

@@@ function 'Rt' (was 'Vt') — structural (66.7%)
--- pretty-v2.1.22.js:398593
+++ pretty-v2.1.23.js:398924
@@ -1,5 +1,6 @@
 function Vt() {
-  let [{ mainLoopModel: A, mainLoopModelForSession: K }] = V6();
+  let A = F1((q) => q.mainLoopModel),
+    K = F1((q) => q.mainLoopModelForSession);
   return qAK.useMemo(() => {
     return jw(K ?? A ?? Mq1());
   }, [K, A]);

@@@ function 'GI7' (was '$r2') — structural (66.7%)
--- pretty-v2.1.22.js:527738
+++ pretty-v2.1.23.js:340804
@@ -1,3 +1,3 @@
-function $r2(A, K, q, Y) {
+function GI7(A) {
   return;
 }

@@@ variable 'xUK' (was 'CQK') — structural (66.7%)
--- pretty-v2.1.22.js:574507
+++ pretty-v2.1.23.js:576229
@@ -65,5 +65,8 @@
   GH();
   Tv();
   TJ();
+  _H();
+  Nv();
+  VJ();
   vQK = new Set();
 });

@@@ function 'bP1' (was 'zP1') — structural (66.6%)
--- pretty-v2.1.22.js:413849
+++ pretty-v2.1.23.js:414151
@@ -1,10 +1,11 @@
 function zP1(A) {
-  let K = s(27),
+  let K = s(28),
     {
       output: q,
       fullOutput: Y,
       elapsedTimeSeconds: z,
       totalLines: w,
+      timeoutMs: H,
       verbose: H,
     } = A,
     J;
@@ -31,20 +32,22 @@
       (K[6] = $));
   else ((X = K[5]), ($ = K[6]));
   let _ = $,
-    Z = H ? 0 : w ? Math.max(0, w - 5) : 0,
-    G;
-  if (K[7] !== z)
-    ((G = z !== void 0 ? `(${fJ(z * 1000)})` : void 0), (K[7] = z), (K[8] = G));
-  else G = K[8];
-  let W = G;
+    Z = J ? 0 : w ? Math.max(0, w - 5) : 0;
   if (!X.length) {
     let E;
-    if (K[9] !== W)
+    if (K[7] === Symbol.for("react.memo_cache_sentinel"))
+      ((T = uS.default.createElement(V, { dimColor: !0 }, "Running… ")),
+        (K[7] = T));
+    else T = K[7];
+    let C;
+    if (K[8] !== z || K[9] !== H)
       ((E = lB.default.createElement(
         E6,
         null,
-        lB.default.createElement(f, { dimColor: !0 }, "Running… ", W),
+        T,
+        uS.default.createElement(VQA, { elapsedTimeSeconds: z, timeoutMs: H }),
       )),
+        (K[8] = z),
         (K[9] = W),
         (K[10] = E));
     else E = K[10];
@@ -83,28 +86,32 @@
       (K[18] = P));
   else P = K[18];
   let V;
-  if (K[19] !== W)
-    ((V = W && lB.default.createElement(f, { dimColor: !0 }, W)),
+  if (K[19] !== z || K[20] !== H)
+    ((P = uS.default.createElement(VQA, {
+      elapsedTimeSeconds: z,
+      timeoutMs: H,
+    })),
       (K[19] = W),
-      (K[20] = V));
-  else V = K[20];
+      (K[20] = H),
+      (K[21] = P));
+  else P = K[21];
   let N;
-  if (K[21] !== P || K[22] !== V)
+  if (K[22] !== M || K[23] !== P)
     ((N = lB.default.createElement(I, { flexDirection: "row", gap: 1 }, P, V)),
-      (K[21] = P),
       (K[22] = V),
-      (K[23] = N));
-  else N = K[23];
+      (K[23] = P),
+      (K[24] = f));
+  else f = K[24];
   let T;
-  if (K[24] !== M || K[25] !== N)
+  if (K[25] !== j || K[26] !== f)
     ((T = lB.default.createElement(
       E6,
       null,
       lB.default.createElement(I, { flexDirection: "column" }, M, N),
     )),
-      (K[24] = M),
       (K[25] = N),
-      (K[26] = T));
-  else T = K[26];
+      (K[26] = f),
+      (K[27] = N));
+  else N = K[27];
   return T;
 }

@@@ variable 'mUA' (was 'DUA') — structural (66.3%)
--- pretty-v2.1.22.js:445676
+++ pretty-v2.1.23.js:445888
@@ -34,12 +34,6 @@
       remoteSessionTitle: U.string()
         .optional()
         .describe("The remote session title if pushed to remote"),
-      launchSwarm: U.boolean()
-        .optional()
-        .describe("Whether to launch a swarm to implement the plan"),
-      teammateCount: U.number()
-        .optional()
-        .describe("Number of teammates to spawn in the swarm"),
     }).passthrough()),
     (AtH = oYK.extend({
       plan: U.string()
@@ -63,12 +57,9 @@
       remoteSessionUrl: U.string()
         .optional()
         .describe("The remote session URL"),
-      launchSwarm: U.boolean()
-        .optional()
-        .describe("Whether to launch a swarm to implement the plan"),
-      teammateCount: U.number()
+      hasTaskTool: U.boolean()
         .optional()
-        .describe("Number of teammates to spawn in the swarm"),
+        .describe("Whether the Task tool is available in the current context"),
       awaitingLeaderApproval: U.boolean()
         .optional()
         .describe(
@@ -102,11 +93,11 @@
         return !1;
       },
       requiresUserInteraction() {
-        if (D8() && p2()) return !1;
+        if (m2()) return !1;
         return !0;
       },
       async checkPermissions(A) {
-        if (D8() && p2()) return { behavior: "allow", updatedInput: A };
+        if (m2()) return { behavior: "allow", updatedInput: A };
         return { behavior: "ask", message: "Exit plan mode?", updatedInput: A };
       },
       renderToolUseMessage: QYK,
@@ -118,7 +109,7 @@
         let q = !!K.agentId,
           Y = SM(K.agentId),
           z = MZ(K.agentId);
-        if (D8() && p2() && oRA()) {
+        if (m2() && jyA()) {
           if (!z)
             throw Error(
               `No plan file found at ${Y}. Please write your plan to this file before calling ExitPlanMode.`,
@@ -152,8 +143,6 @@
             },
           };
         }
-        let w = D8() ? A.launchSwarm : void 0,
-          H = D8() ? A.teammateCount : void 0;
         if (A.pushToRemote && A.remoteSessionId)
           jUA({
             session: {
@@ -163,34 +152,33 @@
             command: z || "",
             context: K,
           });
-        return (
-          K.setAppState((J) => {
-            if (J.toolPermissionContext.mode !== "plan") return J;
-            return (
-              LN(!0),
-              yh(!0),
-              {
-                ...J,
-                toolPermissionContext: WY(J.toolPermissionContext, {
-                  type: "setMode",
-                  mode: "default",
-                  destination: "session",
-                }),
-              }
-            );
-          }),
-          {
-            data: {
-              plan: z,
-              isAgent: q,
-              filePath: Y,
-              pushToRemote: A.pushToRemote,
-              remoteSessionId: A.remoteSessionId,
-              remoteSessionUrl: A.remoteSessionUrl,
-              ...(D8() ? { launchSwarm: w, teammateCount: H } : {}),
-            },
-          }
-        );
+        K.setAppState((H) => {
+          if (H.toolPermissionContext.mode !== "plan") return H;
+          return (
+            VE(!0),
+            xg(!0),
+            {
+              ...H,
+              toolPermissionContext: nY(H.toolPermissionContext, {
+                type: "setMode",
+                mode: "default",
+                destination: "session",
+              }),
+            }
+          );
+        });
+        let w = b8() && K.options.tools.some((H) => H.name === Nq);
+        return {
+          data: {
+            plan: z,
+            isAgent: q,
+            filePath: Y,
+            pushToRemote: A.pushToRemote,
+            remoteSessionId: A.remoteSessionId,
+            remoteSessionUrl: A.remoteSessionUrl,
+            hasTaskTool: w || void 0,
+          },
+        };
       },
       mapToolResultToToolResultBlockParam(
         {
@@ -200,9 +188,9 @@
           pushToRemote: Y,
           remoteSessionId: z,
           remoteSessionUrl: w,
+          hasTaskTool: H,
           awaitingLeaderApproval: H,
           requestId: J,
-          ...O
         },
         X,
       ) {
@@ -245,60 +233,18 @@
               "User has approved exiting plan mode. You can now proceed.",
             tool_use_id: X,
           };
-        if (D8()) {
-          let { launchSwarm: $, teammateCount: _ } = O;
-          if ($ && _)
-            return {
-              type: "tool_result",
-              content: `User has approved your plan AND requested a team of ${_} teammates to implement it.
-
-Please follow these steps to launch the swarm:
-
-1. **Create tasks from your plan** - Parse your plan and create tasks using TaskCreateTool for each actionable item. Each task should have a clear subject and description.
-
-2. **Create a team** - Use TeammateTool with operation: "spawnTeam" to create a new team:
-   \`\`\`json
-   {
-     "operation": "spawnTeam",
-     "team_name": "plan-implementation",
-     "description": "Team implementing the approved plan"
-   }
-   \`\`\`
-
-3. **Spawn ${_} teammates** - Use the Task tool with team_name and name to spawn each teammate:
-   \`\`\`json
-   {
-     "subagent_type": "general-purpose",
-     "name": "worker-1",
-     "prompt": "You are part of a team implementing a plan. Check your mailbox for task assignments.",
-     "description": "worker-1",
-     "team_name": "plan-implementation"
-   }
-   \`\`\`
-
-4. **Assign tasks to teammates** - Use TaskUpdate with owner to distribute work:
-   \`\`\`json
-   {
-     "taskId": "1",
-     "owner": "<teammate name from spawn>"
-   }
-   \`\`\`
-
-5. **Gather findings and post summary** - As the leader/coordinator, monitor your teammates' progress. When they complete their tasks and report back, gather their findings and synthesize a final summary for the user explaining what was accomplished, any issues encountered, and next steps if applicable.
-
-Your plan has been saved to: ${q}
-
-## Approved Plan:
-${K}`,
-              tool_use_id: X,
-            };
-        }
         return {
           type: "tool_result",
           content: `User has approved your plan. You can now start coding. Start with updating your todo list if applicable
 
 Your plan has been saved to: ${q}
-You can refer back to it if needed during implementation.
+You can refer back to it if needed during implementation.${
+            H
+              ? `
+
+If this plan can be broken down into multiple independent tasks, consider using a team of teammates (via the Task tool with team_name) to parallelize the work.`
+              : ""
+          }
 
 ## Approved Plan:
 ${K}`,

@@@ function 'QLK' (was 'mCK') — structural (65.8%)
--- pretty-v2.1.22.js:544847
+++ pretty-v2.1.23.js:545938
@@ -1,87 +1,12 @@
 function mCK({ toolUseConfirm: A, onDone: K, onReject: q, workerBadge: Y }) {
-  let [z, w] = V6(),
+  let z = F1((e) => e.toolPermissionContext),
+    w = p4(),
     { addNotification: H } = iK(),
     [J, O] = zJ.useState(""),
-    [X, $] = zJ.useState(null),
-    [_, Z] = zJ.useState(3),
     G = A.tool.name === VC,
     W = G ? void 0 : A.input.plan,
     D = G ? SM() : void 0,
     j = A.input.allowedPrompts,
-    M = Am() && j !== void 0 && j.length > 0,
-    [P, V] = zJ.useState("options"),
-    N = zJ.useMemo(() => (j ?? []).map((XA, LA) => LA), [j]),
-    [T, E] = zJ.useState(N),
-    R = zJ.useMemo(() => j?.filter((XA, LA) => T.includes(LA)), [j, T]),
-    b = zJ.useMemo(
-      () =>
-        (j ?? []).map((XA, LA) => ({
-          label: `${XA.tool}(${OKK} ${XA.prompt})`,
-          value: LA,
-        })),
-      [j],
-    ),
-    [S, B] = zJ.useState(void 0),
-    x = zJ.useCallback(() => {
-      if (M) (B(void 0), V("permissions"));
-    }, [M]),
-    F = zJ.useMemo(
-      () => [
-        ...(z.toolPermissionContext.isBypassPermissionsModeAvailable
-          ? [
-              {
-                label: "Yes, clear context and bypass permissions",
-                value: "yes-bypass-permissions",
-              },
-            ]
-          : [
-              {
-                label: "Yes, clear context and auto-accept edits (shift+tab)",
-                value: "yes-accept-edits",
-              },
-            ]),
-        ...[],
-        ...(D8()
-          ? [
-              {
-                label: `Yes, and launch swarm (${_} teammates [tab])`,
-                value: "yes-launch-swarm-accept-edits",
-              },
-              ...(z.toolPermissionContext.isBypassPermissionsModeAvailable
-                ? [
-                    {
-                      label: `Yes, and launch swarm (bypass, ${_} teammates [tab])`,
-                      value: "yes-launch-swarm-bypass",
-                    },
-                  ]
-                : []),
-            ]
-          : []),
-        {
-          label: z.toolPermissionContext.isBypassPermissionsModeAvailable
-            ? "Yes, and bypass permissions"
-            : "Yes, auto-accept edits",
-          value: "yes-accept-edits-keep-context",
-        },
-        {
-          label: "Yes, manually approve edits",
-          value: "yes-default-keep-context",
-        },
-        {
-          type: "input",
-          label: "No, keep planning",
-          value: "no",
-          placeholder: "Type here to tell Claude what to change",
-          onChange: O,
-        },
-      ],
-      [z.toolPermissionContext.isBypassPermissionsModeAvailable, _],
-    ),
-    Q = zJ.useCallback(() => {
-      let XA = F[0]?.value;
-      if (XA) B(XA);
-      V("options");
-    }, [F]),
     u = W ?? MZ(),
     d = !u || u.trim() === "",
     [o, l] = zJ.useState(() => {
@@ -132,21 +57,10 @@
             });
           if (VA.content !== null && VA.content !== o) (l(VA.content), wA(!0));
         }
-      if (LA.shift && LA.tab && P === "options") {
+      if (qA.shift && qA.tab) {
         t("yes-accept-edits");
         return;
       }
-      if (
-        P === "options" &&
-        D8() &&
-        LA.tab &&
-        (X === "yes-launch-swarm-accept-edits" ||
-          X === "yes-launch-swarm-bypass")
-      )
-        Z((VA) => {
-          let CA = (FU6.indexOf(VA) + 1) % FU6.length;
-          return FU6[CA];
-        });
     }));
   async function YA(XA) {
     OA("creating");
@@ -232,15 +146,14 @@
       JA();
       return;
     }
-    let LA = G ? {} : { plan: o },
-      VA =
+    let qA = X ? {} : { plan: D };
+    if (
+      e !== "no" &&
+      !(
         XA === "yes-accept-edits-keep-context" ||
-        XA === "yes-default-keep-context",
-      EA =
-        D8() &&
-        (XA === "yes-launch-swarm-accept-edits" ||
-          XA === "yes-launch-swarm-bypass");
-    if (XA !== "no" && !VA && !EA) {
+        e === "yes-default-keep-context"
+      )
+    ) {
       let V1 = "default";
       if (XA === "yes-bypass-permissions") V1 = "bypassPermissions";
       else if (XA === "yes-accept-edits") V1 = "acceptEdits";
@@ -277,8 +190,7 @@
       return;
     }
     let dA = {
-      "yes-accept-edits-keep-context": z.toolPermissionContext
-        .isBypassPermissionsModeAvailable
+      "yes-accept-edits-keep-context": z.isBypassPermissionsModeAvailable
         ? "bypassPermissions"
         : "acceptEdits",
       "yes-default-keep-context": "default",
@@ -294,25 +206,6 @@
         yh(!0),
         K(),
         A.onAllow(LA, IVA(dA, R)));
-      return;
-    }
-    if (
-      D8() &&
-      (XA === "yes-launch-swarm-accept-edits" ||
-        XA === "yes-launch-swarm-bypass")
-    ) {
-      let V1 =
-        XA === "yes-launch-swarm-bypass" ? "bypassPermissions" : "acceptEdits";
-      (n("tengu_plan_exit", {
-        planLengthChars: o.length,
-        outcome: XA,
-        teammateCount: _,
-        interviewPhaseEnabled: y$(),
-      }),
-        LN(!0),
-        yh(!0),
-        K(),
-        A.onAllow({ ...LA, launchSwarm: !0, teammateCount: _ }, IVA(V1, R)));
       return;
     }
     let oA = {
@@ -393,9 +286,11 @@
             onCancel: () => OA("default"),
           }),
         ),
-        XA.filter((LA) => LA.url).map((LA, VA) =>
-          F5.default.createElement(f, { key: VA, dimColor: !0 }, LA.url),
-        ),
+        e
+          .filter((qA) => qA.url)
+          .map((qA, HA) =>
+            a5.default.createElement(V, { key: HA, dimColor: !0 }, qA.url),
+          ),
         F5.default.createElement(f, { dimColor: !0 }, "← to go back"),
       ),
     );
@@ -519,7 +414,9 @@
             permissionResult: A.permissionResult,
             toolType: "tool",
           }),
-          M &&
+          $m() &&
+            G &&
+            G.length > 0 &&
             F5.default.createElement(
               I,
               { flexDirection: "column", marginBottom: 1 },
@@ -528,20 +425,19 @@
                 { bold: !0 },
                 "Requested permissions:",
               ),
-              F5.default.createElement(
-                I,
-                { marginLeft: 2 },
-                F5.default.createElement($jA, {
-                  options: b,
-                  defaultValue: N,
-                  isDisabled: P !== "permissions",
-                  onChange: E,
-                  onDownFromLastItem: Q,
-                  onUpFromFirstItem: () => {},
-                  initialFocusLast: !0,
-                  onCancel: Q,
-                  hideIndexes: !0,
-                }),
+              G.map((e, qA) =>
+                a5.default.createElement(
+                  V,
+                  { key: qA, dimColor: !0 },
+                  "  ",
+                  "· ",
+                  e.tool,
+                  "(",
+                  VqK,
+                  " ",
+                  e.prompt,
+                  ")",
+                ),
               ),
             ),
           F5.default.createElement(
@@ -553,7 +449,40 @@
             I,
             { marginTop: 1 },
             F5.default.createElement(k6, {
-              options: F,
+              options: [
+                ...(z.isBypassPermissionsModeAvailable
+                  ? [
+                      {
+                        label: "Yes, clear context and bypass permissions",
+                        value: "yes-bypass-permissions",
+                      },
+                    ]
+                  : [
+                      {
+                        label:
+                          "Yes, clear context and auto-accept edits (shift+tab)",
+                        value: "yes-accept-edits",
+                      },
+                    ]),
+                ...[],
+                {
+                  label: z.isBypassPermissionsModeAvailable
+                    ? "Yes, and bypass permissions"
+                    : "Yes, auto-accept edits",
+                  value: "yes-accept-edits-keep-context",
+                },
+                {
+                  label: "Yes, manually approve edits",
+                  value: "yes-default-keep-context",
+                },
+                {
+                  type: "input",
+                  label: "No, keep planning",
+                  value: "no",
+                  placeholder: "Type here to tell Claude what to change",
+                  onChange: O,
+                },
+              ],
               onChange: (XA) => t(XA),
               onCancel: () => {
                 (n("tengu_plan_exit", {
@@ -565,10 +494,6 @@
                   q(),
                   A.onReject());
               },
-              onFocus: $,
-              onUpFromFirstItem: x,
-              isDisabled: P !== "options",
-              defaultFocusValue: S,
             }),
           ),
         ),

@@@ function 'm3z' (was 'jqz') — structural (65.6%)
--- pretty-v2.1.22.js:577257
+++ pretty-v2.1.23.js:578982
@@ -8,7 +8,7 @@
       { compareOptions: (O, X) => J(O).localeCompare(J(X)) },
     );
   }
-  let K = new DE1().configureHelp(A());
+  let K = new cE1().configureHelp(A()).enablePositionalOptions();
   ($K("run_commander_initialized"),
     K.hook("preAction", async () => {
       $K("preAction_start");
@@ -338,8 +338,6 @@
           o = O.init ?? !1,
           l = O.initOnly ?? !1,
           e = O.maintenance ?? !1,
-          wA = !1,
-          HA,
           OA = O.disableSlashCommands || !1,
           WA = !1,
           a = WA ? (typeof WA === "string" ? WA : F46) : void 0,
@@ -609,14 +607,16 @@
               process.exit(1));
         }
         rn6(P);
-        let { toolPermissionContext: y1, warnings: p1 } = P0K({
-          allowedToolsCli: W,
-          disallowedToolsCli: D,
-          baseToolsCli: G,
-          permissionMode: VA,
-          allowDangerouslySkipPermissions: Z,
-          addDirs: P,
-        });
+        let lA = jXK({
+            allowedToolsCli: W,
+            disallowedToolsCli: D,
+            baseToolsCli: Z,
+            permissionMode: vA,
+            allowDangerouslySkipPermissions: G,
+            addDirs: P,
+          }),
+          v1 = lA.toolPermissionContext,
+          { warnings: I1, dangerousPermissions: Q1 } = lA;
         (p1.forEach((M6) => {
           console.error(M6);
         }),
@@ -787,8 +787,7 @@
           d8;
         if (st())
           ((d8 = new Qd6(wq, Hq)),
-            d8
-              .start()
+            E8.start()
               .then(({ url: M6 }) => {
                 let U4 = d8.getSecret();
                 (VVA({ url: M6, key: U4 }),
@@ -821,6 +820,7 @@
             skipWebFetchPreflight: oq().skipWebFetchPreflight,
             githubActionInputs: process.env.GITHUB_ACTION_INPUTS,
             dangerouslySkipPermissionsPassed: _ ?? !1,
+            permissionMode: vA,
             modeIsBypass: VA === "bypassPermissions",
             allowDangerouslySkipPermissionsPassed: Z,
             systemPromptFlag: kA
@@ -863,27 +863,24 @@
                     (i8.type === "prompt" && !i8.disableNonInteractive) ||
                     (i8.type === "local" && i8.supportsNonInteractive),
                 ),
-            U4 = $PA();
-          if (
-            ((U4 = {
-              ...U4,
-              mcp: { ...U4.mcp, clients: wq, commands: l8, tools: Hq },
-              toolPermissionContext: y1,
-            }),
-            y1.mode === "bypassPermissions" || Z)
-          )
-            V0K(y1);
+            W7 = RPA(),
+            Q8 = AT1(
+              {
+                ...W7,
+                mcp: { ...W7.mcp, clients: k5, commands: r8, tools: iq },
+                toolPermissionContext: v1,
+              },
+              em,
+            );
+          if (v1.mode === "bypassPermissions" || G) MXK(v1);
           if (O.sessionPersistence === !1) Bn6(!0);
           (Gn6(TR4(N)),
             NYA(),
             LE1(),
             EQK(
               $1,
-              async () => U4,
-              (i8) => {
-                let H7 = U4;
-                ((U4 = i8(U4)), Um({ newState: U4, oldState: H7 }));
-              },
+              async () => Q8.getState(),
+              Q8.setState,
               M6,
               C1,
               F4,
@@ -913,7 +910,6 @@
                 enableAuthStatus: O.enableAuthStatus,
                 agent: x,
                 setupTrigger: Jq ?? void 0,
-                ...{},
               },
             ));
           return;
@@ -1073,7 +1069,6 @@
                     mainThreadAgentDefinition: y6,
                     disableSlashCommands: OA,
                     taskListId: a,
-                    autoTickIntervalMs: HA,
                   }),
                 ),
               ),
@@ -1348,7 +1343,6 @@
                       mainThreadAgentDefinition: y6,
                       disableSlashCommands: OA,
                       taskListId: a,
-                      autoTickIntervalMs: HA,
                     }),
                   ),
                 ),
@@ -1415,7 +1409,6 @@
                   mainThreadAgentDefinition: y6,
                   disableSlashCommands: OA,
                   taskListId: a,
-                  autoTickIntervalMs: HA,
                 }),
               ),
             ),
@@ -1425,7 +1418,7 @@
         }
       })
       .version(
-        `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.22", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T06:33:34Z" }.VERSION} (Claude Code)`,
+        `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.23", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-29T00:18:20Z" }.VERSION} (Claude Code)`,
         "-v, --version",
         "Output the version number",
       ),

@@@ function 'Y5A' (was 'rqA') — structural (65.6%)
--- pretty-v2.1.22.js:319011
+++ pretty-v2.1.23.js:319444
@@ -1,16 +1,14 @@
 function rqA() {
   let A = process.env.CLAUDE_CODE_EFFORT_LEVEL;
   if (A) {
-    if (A === "unset") return;
     let Y = parseInt(A, 10);
     if (!isNaN(Y) && wV6(Y)) return Y;
-    if (["low", "medium", "high"].includes(A)) return A;
+    if (["low", "medium", "high", "max"].includes(A)) return A;
   }
   let q = O8().effortLevel;
-  if (q === "unset") return;
   if (q !== void 0) {
     if (typeof q === "number" && wV6(q)) return q;
-    if (typeof q === "string" && ["low", "medium", "high"].includes(q))
+    if (typeof q === "string" && ["low", "medium", "high", "max"].includes(q))
       return q;
   }
   return;

@@@ function 'w_2' (was 'dX2') — structural (65.4%)
--- pretty-v2.1.22.js:388979
+++ pretty-v2.1.23.js:389542
@@ -1,6 +1,12 @@
 function dX2(A) {
-  let K = s(27),
-    { task: q, ownerColor: Y, openBlockers: z, activity: w } = A,
+  let K = s(28),
+    {
+      task: q,
+      ownerColor: Y,
+      openBlockers: z,
+      activity: w,
+      ownerActive: H,
+    } = A,
     H = q.status === "completed",
     J = q.status === "in_progress",
     O = z.length > 0,
@@ -31,9 +37,10 @@
       (K[9] = D));
   else D = K[9];
   let j;
-  if (K[10] !== Y || K[11] !== q.owner)
+  if (K[10] !== H || K[11] !== Y || K[12] !== q.owner)
     ((j =
       q.owner &&
+      H &&
       xK.createElement(
         f,
         { dimColor: !0 },
@@ -42,11 +49,12 @@
         ")",
       )),
       (K[10] = Y),
-      (K[11] = q.owner),
-      (K[12] = j));
-  else j = K[12];
+      (K[11] = Y),
+      (K[12] = q.owner),
+      (K[13] = M));
+  else M = K[13];
   let M;
-  if (K[13] !== O || K[14] !== z)
+  if (K[14] !== X || K[15] !== z)
     ((M =
       O &&
       xK.createElement(
@@ -58,21 +66,21 @@
         " ",
         [...z].sort(lX2).map(cX2).join(", "),
       )),
-      (K[13] = O),
       (K[14] = z),
-      (K[15] = M));
-  else M = K[15];
+      (K[15] = z),
+      (K[16] = P));
+  else P = K[16];
   let P;
-  if (K[16] !== G || K[17] !== D || K[18] !== j || K[19] !== M)
+  if (K[17] !== W || K[18] !== j || K[19] !== M || K[20] !== P)
     ((P = xK.createElement(I, null, G, D, j, M)),
-      (K[16] = G),
       (K[17] = D),
       (K[18] = j),
       (K[19] = M),
-      (K[20] = P));
-  else P = K[20];
+      (K[20] = P),
+      (K[21] = f));
+  else f = K[21];
   let V;
-  if (K[21] !== w || K[22] !== Z)
+  if (K[22] !== w || K[23] !== Z)
     ((V =
       Z &&
       xK.createElement(
@@ -80,16 +88,16 @@
         null,
         xK.createElement(f, { dimColor: !0 }, "  ", w, q1.ellipsis),
       )),
-      (K[21] = w),
       (K[22] = Z),
-      (K[23] = V));
-  else V = K[23];
+      (K[23] = Z),
+      (K[24] = N));
+  else N = K[24];
   let N;
-  if (K[24] !== P || K[25] !== V)
+  if (K[25] !== f || K[26] !== N)
     ((N = xK.createElement(I, { flexDirection: "column" }, P, V)),
-      (K[24] = P),
       (K[25] = V),
-      (K[26] = N));
-  else N = K[26];
+      (K[26] = N),
+      (K[27] = T));
+  else T = K[27];
   return N;
 }

@@@ function '$O' (was 'fJ') — structural (64.3%)
--- pretty-v2.1.22.js:158475
+++ pretty-v2.1.23.js:158510
@@ -1,4 +1,4 @@
-function fJ(A) {
+function $O(A, K) {
   if (A < 60000) {
     if (A === 0) return "0s";
     if (A < 1) return `${(A / 1000).toFixed(1)}s`;
@@ -11,8 +11,20 @@
   if (z === 60) ((z = 0), Y++);
   if (Y === 60) ((Y = 0), q++);
   if (q === 24) ((q = 0), K++);
-  if (K > 0) return `${K}d ${q}h ${Y}m`;
-  if (q > 0) return `${q}h ${Y}m ${z}s`;
-  if (Y > 0) return `${Y}m ${z}s`;
+  let H = K?.hideTrailingZeros;
+  if (q > 0) {
+    if (H && Y === 0 && z === 0) return `${q}d`;
+    if (H && z === 0) return `${q}d ${Y}h`;
+    return `${q}d ${Y}h ${z}m`;
+  }
+  if (Y > 0) {
+    if (H && z === 0 && w === 0) return `${Y}h`;
+    if (H && w === 0) return `${Y}h ${z}m`;
+    return `${Y}h ${z}m ${w}s`;
+  }
+  if (z > 0) {
+    if (H && w === 0) return `${z}m`;
+    return `${z}m ${w}s`;
+  }
   return `${z}s`;
 }

@@@ function 'bSK' (was 'IIK') — structural (63.8%)
--- pretty-v2.1.22.js:558179
+++ pretty-v2.1.23.js:559697
@@ -1,8 +1,11 @@
 function IIK() {
-  let [A, K] = V6(),
-    q = bcA.useRef(A);
-  q.current = A;
-  let Y = $k1(A.tasks),
+  let A = F1(($) => $.tasks),
+    K = F1(($) => $.viewSelectionMode),
+    q = F1(($) => $.viewingAgentTaskId),
+    Y = F1(($) => $.selectedIPAgentIndex),
+    z = p4(),
+    w = D0(),
+    H = Qk1(A),
     z = Y.length,
     w = bcA.useRef(z);
   bcA.useEffect(() => {
@@ -19,22 +22,21 @@
   }, [z, K]);
   let H = () => {
     if (z === 0) return null;
-    let J = A.selectedIPAgentIndex,
-      O = Y[J];
+    let _ = H[Y];
     if (!O) return null;
     return { taskId: O.id, task: O };
   };
   e6((J, O) => {
-    if (O.escape && A.viewSelectionMode === "viewing-agent") {
-      let X = A.viewingAgentTaskId;
+    if (_.escape && K === "viewing-agent") {
+      let G = q;
       if (X) {
-        let $ = A.tasks[X];
+        let Z = A[G];
         if (rT($) && $.status === "running")
           $.currentWorkAbortController?.abort();
       }
       return;
     }
-    if (O.escape && A.viewSelectionMode === "selecting-agent") {
+    if (_.escape && K === "selecting-agent") {
       K((X) => ({ ...X, viewSelectionMode: "none", selectedIPAgentIndex: -1 }));
       return;
     }
@@ -68,29 +70,25 @@
       });
       return;
     }
-    if (J === "f" && A.viewSelectionMode === "selecting-agent" && z > 0) {
+    if ($ === "f" && K === "selecting-agent" && J > 0) {
       let X = H();
       if (X) KVA(X.taskId, K);
       return;
     }
-    if (O.return && A.viewSelectionMode === "selecting-agent") {
-      if (A.selectedIPAgentIndex === -1) Ce(K);
+    if (_.return && K === "selecting-agent") {
+      if (Y === -1) bm(z);
       else {
         let X = H();
         if (X) KVA(X.taskId, K);
       }
       return;
     }
-    if (
-      J === "k" &&
-      A.viewSelectionMode === "selecting-agent" &&
-      A.selectedIPAgentIndex >= 0
-    ) {
+    if ($ === "k" && K === "selecting-agent" && Y >= 0) {
       let X = H();
       if (X && X.task.status === "running")
         _P1.kill(X.taskId, {
           abortController: new AbortController(),
-          getAppState: async () => q.current,
+          getAppState: async () => w.getState(),
           setAppState: K,
         });
       return;

@@@ function 'V7z' (was 'z8z') — structural (63.4%)
--- pretty-v2.1.22.js:558542
+++ pretty-v2.1.23.js:560060
@@ -22,7 +22,11 @@
           .then(async (Z) => {
             if (Z.behavior === "allow") {
               (UIK(q, Y, z, w.message.id, H),
-                O({ ...Z, updatedInput: Y, userModified: !1 }));
+                O({
+                  ...G,
+                  updatedInput: G.updatedInput ?? Y,
+                  userModified: !1,
+                }));
               return;
             }
             let G = await z.getAppState(),
@@ -65,6 +69,93 @@
                   },
                   D = !1,
                   j = !1;
+                if (Z.toolPermissionContext.awaitAutomatedChecksBeforeDialog)
+                  try {
+                    if (q.name === G7 && G.pendingClassifierCheck) {
+                      let N = await zUA(
+                        G.pendingClassifierCheck,
+                        z.abortController.signal,
+                        z.options.isNonInteractiveSession,
+                      );
+                      if (N) {
+                        (zfA(z, H, "accept", "classifier"),
+                          wfA(q.name, "accept", "classifier"),
+                          LYA(q, Y, z, w.message.id, H, { type: "classifier" }),
+                          O({
+                            behavior: "allow",
+                            updatedInput: G.updatedInput ?? Y,
+                            userModified: !1,
+                            decisionReason: N,
+                          }));
+                        return;
+                      }
+                    }
+                    for await (let N of HPA(
+                      q.name,
+                      H,
+                      Y,
+                      z,
+                      Z.toolPermissionContext.mode,
+                      G.suggestions,
+                      z.abortController.signal,
+                    ))
+                      if (N.permissionRequestResult) {
+                        let T = N.permissionRequestResult;
+                        if (T.behavior === "allow") {
+                          let C = T.updatedInput ?? G.updatedInput ?? Y,
+                            R = T.updatedPermissions ?? [];
+                          if (R.length > 0) {
+                            QE(R);
+                            let y = await z.getAppState(),
+                              B = XD(y.toolPermissionContext, R);
+                            K(B);
+                          }
+                          let x = R.some((y) => oHA(y.destination));
+                          (LYA(q, C, z, w.message.id, H, {
+                            type: "hook",
+                            permanent: x,
+                          }),
+                            O({
+                              behavior: "allow",
+                              updatedInput: C,
+                              userModified: !1,
+                              decisionReason: {
+                                type: "hook",
+                                hookName: "PermissionRequest",
+                              },
+                            }));
+                          return;
+                        } else if (T.behavior === "deny") {
+                          if (
+                            (zlA(q, Y, z, w.message.id, H, { type: "hook" }),
+                            O({
+                              behavior: "deny",
+                              message: T.message || "Permission denied by hook",
+                              decisionReason: {
+                                type: "hook",
+                                hookName: "PermissionRequest",
+                                reason: T.message,
+                              },
+                            }),
+                            T.interrupt)
+                          )
+                            z.abortController.abort();
+                          return;
+                        }
+                      }
+                  } catch (N) {
+                    KA(
+                      N instanceof Error
+                        ? N
+                        : Error(
+                            `Automated permission check failed: ${String(N)}`,
+                          ),
+                    );
+                  }
+                if (z.abortController.signal.aborted) {
+                  (X(), $(void 0, !0));
+                  return;
+                }
                 if (
                   D8() &&
                   rjA() &&
@@ -168,95 +259,99 @@
                   }
                 let M = Date.now(),
                   P = Z.updatedInput ?? Y;
-                A((T) => [
-                  ...T,
-                  {
-                    assistantMessage: w,
-                    tool: q,
-                    description: W,
-                    input: P,
-                    toolUseContext: z,
-                    toolUseID: H,
-                    permissionResult: Z,
-                    permissionPromptStartTimeMs: M,
-                    classifierCheckInProgress: !!Z.pendingClassifierCheck,
-                    onUserInteraction() {
-                      ((j = !0), V());
-                    },
-                    onAbort() {
-                      if (D) return;
-                      ((D = !0),
-                        X(),
-                        _k1(
-                          q,
-                          Y,
-                          z,
-                          w.message.id,
-                          H,
-                          { type: "user_abort" },
-                          M,
-                        ),
-                        $(void 0, !0));
-                    },
-                    async onAllow(E, R, b) {
-                      if (D) return;
-                      ((D = !0), IR(R));
-                      let S = await z.getAppState(),
-                        B = pj(S.toolPermissionContext, R);
-                      K(B);
-                      let x = R.some((u) => kEA(u.destination));
-                      xcA(
-                        q,
-                        E,
-                        z,
-                        w.message.id,
-                        H,
-                        { type: "user", permanent: x },
-                        M,
-                      );
-                      let F = q.inputsEquivalent
-                          ? !q.inputsEquivalent(Y, E)
-                          : !1,
-                        Q = b?.trim();
-                      O({
-                        behavior: "allow",
-                        updatedInput: E,
-                        userModified: F,
-                        acceptFeedback: Q || void 0,
-                      });
-                    },
-                    onReject(E) {
-                      if (D) return;
-                      ((D = !0),
+                if (
+                  (A((N) => [
+                    ...N,
+                    {
+                      assistantMessage: w,
+                      tool: q,
+                      description: W,
+                      input: P,
+                      toolUseContext: z,
+                      toolUseID: H,
+                      permissionResult: G,
+                      permissionPromptStartTimeMs: M,
+                      classifierCheckInProgress: !!G.pendingClassifierCheck,
+                      onUserInteraction() {
+                        ((j = !0), zW1(H), f());
+                      },
+                      onAbort() {
+                        if (D) return;
+                        ((D = !0),
+                          X(),
+                          zlA(
+                            q,
+                            Y,
+                            z,
+                            w.message.id,
+                            H,
+                            { type: "user_abort" },
+                            M,
+                          ),
+                          $(void 0, !0));
+                      },
+                      async onAllow(T, C, R) {
+                        if (D) return;
+                        if (((D = !0), C.length > 0)) {
+                          QE(C);
+                          let b = await z.getAppState(),
+                            F = XD(b.toolPermissionContext, C);
+                          K(F);
+                        }
+                        let x = C.some((b) => oHA(b.destination));
                         _k1(
                           q,
                           Y,
                           z,
                           w.message.id,
                           H,
-                          { type: "user_reject", hasFeedback: !!E },
+                          { type: "user", permanent: x },
                           M,
-                        ),
-                        $(E));
-                    },
-                    async recheckPermission() {
-                      if (D) return;
-                      let E = await j_(q, Y, z, w, H);
-                      if (E.behavior === "allow")
-                        (A((R) => R.filter((b) => b.toolUseID !== H)),
-                          UIK(q, Y, z, w.message.id, H),
-                          (D = !0),
-                          O({
-                            behavior: "allow",
-                            updatedInput: E.updatedInput || Y,
-                            userModified: !1,
-                          }));
+                        );
+                        let y = q.inputsEquivalent
+                            ? !q.inputsEquivalent(Y, T)
+                            : !1,
+                          B = R?.trim();
+                        O({
+                          behavior: "allow",
+                          updatedInput: T,
+                          userModified: y,
+                          acceptFeedback: B || void 0,
+                        });
+                      },
+                      onReject(T) {
+                        if (D) return;
+                        ((D = !0),
+                          zlA(
+                            q,
+                            Y,
+                            z,
+                            w.message.id,
+                            H,
+                            { type: "user_reject", hasFeedback: !!T },
+                            M,
+                          ),
+                          $(T));
+                      },
+                      async recheckPermission() {
+                        if (D) return;
+                        let T = await V_(q, Y, z, w, H);
+                        if (T.behavior === "allow")
+                          (A((C) => C.filter((R) => R.toolUseID !== H)),
+                            cSK(q, Y, z, w.message.id, H),
+                            (D = !0),
+                            O({
+                              behavior: "allow",
+                              updatedInput: T.updatedInput ?? Y,
+                              userModified: !1,
+                            }));
+                      },
                     },
-                  },
-                ]);
-                let N = await z.getAppState();
-                if (
-                  ((async () => {
+                  ]),
+                  !Z.toolPermissionContext.awaitAutomatedChecksBeforeDialog)
+                ) {
+                  let N = await z.getAppState();
+                  (async () => {
                     for await (let T of JWA([
                       BUA(
                         q.name,
@@ -278,7 +373,7 @@
                           A((R) => R.filter((b) => b.toolUseID !== H)));
                         let E = T.permissionRequestResult;
                         if (E.behavior === "allow") {
-                          let R = E.updatedInput || Y,
+                          let R = C.updatedInput ?? G.updatedInput ?? Y,
                             b = E.updatedPermissions ?? [];
                           if (b.length > 0) {
                             IR(b);
@@ -325,60 +420,68 @@
                         }
                       }
                     }
-                  })(),
-                  Z.pendingClassifierCheck && q.name === E7)
+                  })();
+                }
+                if (
+                  G.pendingClassifierCheck &&
+                  q.name === G7 &&
+                  !Z.toolPermissionContext.awaitAutomatedChecksBeforeDialog
                 )
-                  VKK(
-                    Z.pendingClassifierCheck,
-                    z.abortController.signal,
-                    z.options.isNonInteractiveSession,
-                    {
-                      shouldContinue: () => !D && !j,
-                      onComplete: V,
-                      onAllow: (T) => {
-                        D = !0;
-                        let E =
-                          T.type === "classifier"
-                            ? (T.reason.match(
-                                /^Allowed by prompt rule: "(.+)"$/,
-                              )?.[1] ?? T.reason)
-                            : void 0;
-                        (A((b) =>
-                          b.map((S) =>
-                            S.toolUseID === H
-                              ? {
-                                  ...S,
-                                  classifierCheckInProgress: !1,
-                                  classifierAutoApproved: !0,
-                                  classifierMatchedRule: E,
-                                }
-                              : S,
+                  (WI7(H),
+                    IqK(
+                      G.pendingClassifierCheck,
+                      z.abortController.signal,
+                      z.options.isNonInteractiveSession,
+                      {
+                        shouldContinue: () => !D && !j,
+                        onComplete: () => {
+                          (zW1(H), f());
+                        },
+                        onAllow: (N) => {
+                          ((D = !0), zW1(H));
+                          let T =
+                            N.type === "classifier"
+                              ? (N.reason.match(
+                                  /^Allowed by prompt rule: "(.+)"$/,
+                                )?.[1] ?? N.reason)
+                              : void 0;
+                          (A((R) =>
+                            R.map((x) =>
+                              x.toolUseID === H
+                                ? {
+                                    ...x,
+                                    classifierCheckInProgress: !1,
+                                    classifierAutoApproved: !0,
+                                    classifierMatchedRule: T,
+                                  }
+                                : x,
+                            ),
                           ),
-                        ),
-                          xcA(
-                            q,
-                            Y,
-                            z,
-                            w.message.id,
-                            H,
-                            { type: "classifier" },
-                            M,
-                          ),
-                          O({
-                            behavior: "allow",
-                            updatedInput: Y,
-                            userModified: !1,
-                            decisionReason: T,
-                          }));
-                        let R = setTimeout(() => {
-                          A((b) => b.filter((S) => S.toolUseID !== H));
-                        }, 800);
-                        z.abortController.signal.addEventListener("abort", () =>
-                          clearTimeout(R),
-                        );
+                            LYA(
+                              q,
+                              Y,
+                              z,
+                              w.message.id,
+                              H,
+                              { type: "classifier" },
+                              M,
+                            ),
+                            O({
+                              behavior: "allow",
+                              updatedInput: Y,
+                              userModified: !1,
+                              decisionReason: N,
+                            }));
+                          let C = setTimeout(() => {
+                            A((R) => R.filter((x) => x.toolUseID !== H));
+                          }, 1000);
+                          z.abortController.signal.addEventListener(
+                            "abort",
+                            () => clearTimeout(C),
+                          );
+                        },
                       },
-                    },
-                  );
+                    ));
                 return;
               }
             }

@@@ function 'bG9' (was 'E_9') — structural (63.2%)
--- pretty-v2.1.22.js:193121
+++ pretty-v2.1.23.js:193288
@@ -1,19 +1,24 @@
 function E_9() {
   let A = kR4();
-  if (A)
-    return {
+  if (A) {
+    let J = {
       agentId: A.agentId,
       parentSessionId: A.parentSessionId,
       agentType: A.agentType,
     };
+    if (A.agentType === "teammate") J.teamName = A.teamName;
+    return J;
+  }
   let K = e$(),
     q = cn(),
+    Y = T3(),
     z = p2() ? "teammate" : K ? "standalone" : void 0;
-  if (K || z || q)
+  if (K || w || q || Y)
     return {
       ...(K ? { agentId: K } : {}),
       ...(z ? { agentType: z } : {}),
       ...(q ? { parentSessionId: q } : {}),
+      ...(Y ? { teamName: Y } : {}),
     };
   let w = An6();
   if (w) return { parentSessionId: w };

@@@ function 'JSK' (was 'wIK') — structural (63.2%)
--- pretty-v2.1.22.js:557266
+++ pretty-v2.1.23.js:558545
@@ -1,10 +1,11 @@
 function wIK({ inputValue: A, isAssistantResponding: K }) {
-  let [q, Y] = V6(),
+  let q = F1((X) => X.promptCoaching),
+    Y = p4(),
     z = !0,
     w = !0,
     H = null,
     J = ZYA.useRef(!1);
-  ZYA.useEffect(() => {}, [!0, q.promptCoaching.tip]);
+  CYA.useEffect(() => {}, [!0, q.tip]);
   let O = ZYA.useCallback(
     (X = "dismissed") => {
       return;
@@ -14,7 +15,7 @@
   return (
     ZYA.useEffect(() => {
       return;
-    }, [!0, q.promptCoaching.tip, A, K, O]),
+    }, [!0, q.tip, A, K, O]),
     { tip: null, dismissTip: () => {} }
   );
   return { tip: null, dismissTip: () => O("dismissed") };

@@@ function 'fT1' (was 'iN1') — structural (63.0%)
--- pretty-v2.1.22.js:475054
+++ pretty-v2.1.23.js:475667
@@ -4,5 +4,8 @@
     BY6.cache.clear?.(),
     c0.cache.clear?.(),
     lXK(),
+    fm(),
+    He(),
+    a57(),
     $m());
 }

@@@ function 'H7K' (was 'r8K') — structural (62.3%)
--- pretty-v2.1.22.js:409880
+++ pretty-v2.1.23.js:410150
@@ -1,5 +1,5 @@
 function r8K(A) {
-  let K = s(127),
+  let K = s(132),
     { attachment: q, addMargin: Y, verbose: z } = A;
   if (D8() && q.type === "teammate_mailbox") return null;
   switch (q.type) {
@@ -205,52 +205,70 @@
       else _ = K[50];
       return _;
     }
+    case "skill_listing": {
+      if (q.isInitial) return null;
+      let w;
+      if (K[51] !== q.skillCount)
+        ((w = uq.default.createElement(V, { bold: !0 }, q.skillCount)),
+          (K[51] = q.skillCount),
+          (K[52] = w));
+      else w = K[52];
+      let H = q.skillCount !== 1 ? "s" : "",
+        J;
+      if (K[53] !== w || K[54] !== H)
+        ((J = uq.default.createElement(VO, null, w, " skill", H, " available")),
+          (K[53] = w),
+          (K[54] = H),
+          (K[55] = J));
+      else J = K[55];
+      return J;
+    }
     case "queued_command": {
       let w;
-      if (K[51] !== q.prompt)
+      if (K[56] !== q.prompt)
         ((w = typeof q.prompt === "string" ? q.prompt : v3A(q.prompt) || ""),
-          (K[51] = q.prompt),
-          (K[52] = w));
-      else w = K[52];
+          (K[56] = q.prompt),
+          (K[57] = w));
+      else w = K[57];
       let H = w,
         J = q.imagePasteIds && q.imagePasteIds.length > 0,
         O;
-      if (K[53] !== H)
-        ((O = { text: H, type: "text" }), (K[53] = H), (K[54] = O));
-      else O = K[54];
+      if (K[58] !== H)
+        ((O = { text: H, type: "text" }), (K[58] = H), (K[59] = O));
+      else O = K[59];
       let X;
-      if (K[55] !== Y || K[56] !== O || K[57] !== z)
+      if (K[60] !== Y || K[61] !== O || K[62] !== z)
         ((X = q5.default.createElement(f3A, {
           addMargin: Y,
           param: O,
           verbose: z,
         })),
-          (K[55] = Y),
-          (K[56] = O),
-          (K[57] = z),
-          (K[58] = X));
-      else X = K[58];
+          (K[60] = Y),
+          (K[61] = O),
+          (K[62] = z),
+          (K[63] = X));
+      else X = K[63];
       let $;
-      if (K[59] !== q.imagePasteIds || K[60] !== J)
+      if (K[64] !== q.imagePasteIds || K[65] !== J)
         (($ = J && q.imagePasteIds?.map(bW2)),
-          (K[59] = q.imagePasteIds),
-          (K[60] = J),
-          (K[61] = $));
-      else $ = K[61];
+          (K[64] = q.imagePasteIds),
+          (K[65] = J),
+          (K[66] = $));
+      else $ = K[66];
       let _;
-      if (K[62] !== X || K[63] !== $)
+      if (K[67] !== X || K[68] !== $)
         ((_ = q5.default.createElement(I, { flexDirection: "column" }, X, $)),
-          (K[62] = X),
-          (K[63] = $),
-          (K[64] = _));
-      else _ = K[64];
+          (K[67] = X),
+          (K[68] = $),
+          (K[69] = _));
+      else _ = K[69];
       return _;
     }
     case "todo": {
       if (q.context === "post-compact") {
         let w = q.itemCount === 1 ? "item" : "items",
           H;
-        if (K[65] !== q.itemCount || K[66] !== w)
+        if (K[70] !== q.itemCount || K[71] !== w)
           ((H = q5.default.createElement(
             Z0,
             null,
@@ -260,21 +278,21 @@
             w,
             ")",
           )),
-            (K[65] = q.itemCount),
-            (K[66] = w),
-            (K[67] = H));
-        else H = K[67];
+            (K[70] = q.itemCount),
+            (K[71] = w),
+            (K[72] = H));
+        else H = K[72];
         return H;
       }
       return null;
     }
     case "plan_file_reference": {
       let w;
-      if (K[68] !== q.planFilePath)
-        ((w = M5(q.planFilePath)), (K[68] = q.planFilePath), (K[69] = w));
-      else w = K[69];
+      if (K[73] !== q.planFilePath)
+        ((w = Z5(q.planFilePath)), (K[73] = q.planFilePath), (K[74] = w));
+      else w = K[74];
       let H;
-      if (K[70] !== w)
+      if (K[75] !== w)
         ((H = q5.default.createElement(
           Z0,
           null,
@@ -282,45 +300,45 @@
           w,
           ")",
         )),
-          (K[70] = w),
-          (K[71] = H));
-      else H = K[71];
+          (K[75] = w),
+          (K[76] = H));
+      else H = K[76];
       return H;
     }
     case "invoked_skills": {
       if (q.skills.length === 0) return null;
       let w;
-      if (K[72] !== q.skills)
-        ((w = q.skills.map(hW2).join(", ")), (K[72] = q.skills), (K[73] = w));
-      else w = K[73];
+      if (K[77] !== q.skills)
+        ((w = q.skills.map(UD2).join(", ")), (K[77] = q.skills), (K[78] = w));
+      else w = K[78];
       let H = w,
         J;
-      if (K[74] !== H)
+      if (K[79] !== H)
         ((J = q5.default.createElement(Z0, null, "Skills restored (", H, ")")),
-          (K[74] = H),
-          (K[75] = J));
-      else J = K[75];
+          (K[79] = H),
+          (K[80] = J));
+      else J = K[80];
       return J;
     }
     case "diagnostics": {
       let w;
-      if (K[76] !== q || K[77] !== z)
+      if (K[81] !== q || K[82] !== z)
         ((w = q5.default.createElement(i8K, { attachment: q, verbose: z })),
-          (K[76] = q),
-          (K[77] = z),
-          (K[78] = w));
-      else w = K[78];
+          (K[81] = q),
+          (K[82] = z),
+          (K[83] = w));
+      else w = K[83];
       return w;
     }
     case "mcp_resource": {
       let w;
-      if (K[79] !== q.name)
+      if (K[84] !== q.name)
         ((w = q5.default.createElement(f, { bold: !0 }, q.name)),
-          (K[79] = q.name),
-          (K[80] = w));
-      else w = K[80];
+          (K[84] = q.name),
+          (K[85] = w));
+      else w = K[85];
       let H;
-      if (K[81] !== q.server || K[82] !== w)
+      if (K[86] !== q.server || K[87] !== w)
         ((H = q5.default.createElement(
           Z0,
           null,
@@ -330,10 +348,10 @@
           " ",
           q.server,
         )),
-          (K[81] = q.server),
-          (K[82] = w),
-          (K[83] = H));
-      else H = K[83];
+          (K[86] = q.server),
+          (K[87] = w),
+          (K[88] = H));
+      else H = K[88];
       return H;
     }
     case "command_permissions":
@@ -342,13 +360,13 @@
       if (q.hookEvent === "SessionStart" && !z) return null;
       let w = q.response,
         H;
-      if (K[84] !== q.hookEvent)
+      if (K[89] !== q.hookEvent)
         ((H = q5.default.createElement(f, { bold: !0 }, q.hookEvent)),
-          (K[84] = q.hookEvent),
-          (K[85] = H));
-      else H = K[85];
+          (K[89] = q.hookEvent),
+          (K[90] = H));
+      else H = K[90];
       let J;
-      if (K[86] !== w || K[87] !== z)
+      if (K[91] !== w || K[92] !== z)
         ((J =
           z &&
           q5.default.createElement(
@@ -365,12 +383,12 @@
                 ? w.hookSpecificOutput.additionalContext
                 : null,
           )),
-          (K[86] = w),
-          (K[87] = z),
-          (K[88] = J));
-      else J = K[88];
+          (K[91] = w),
+          (K[92] = z),
+          (K[93] = J));
+      else J = K[93];
       let O;
-      if (K[89] !== H || K[90] !== J)
+      if (K[94] !== H || K[95] !== J)
         ((O = q5.default.createElement(
           Z0,
           null,
@@ -379,17 +397,17 @@
           " completed",
           J,
         )),
-          (K[89] = H),
-          (K[90] = J),
-          (K[91] = O));
-      else O = K[91];
+          (K[94] = H),
+          (K[95] = J),
+          (K[96] = O));
+      else O = K[96];
       return O;
     }
     case "hook_blocking_error": {
       if (q.hookEvent === "Stop" || q.hookEvent === "SubagentStop") return null;
       if (z) {
         let H;
-        if (K[92] !== q.blockingError.blockingError || K[93] !== q.hookName)
+        if (K[97] !== q.blockingError.blockingError || K[98] !== q.hookName)
           ((H = q5.default.createElement(
             Z0,
             { color: "error" },
@@ -398,30 +416,30 @@
             " ",
             q.blockingError.blockingError,
           )),
-            (K[92] = q.blockingError.blockingError),
-            (K[93] = q.hookName),
-            (K[94] = H));
-        else H = K[94];
+            (K[97] = q.blockingError.blockingError),
+            (K[98] = q.hookName),
+            (K[99] = H));
+        else H = K[99];
         return H;
       }
       let w;
-      if (K[95] !== q.hookName)
+      if (K[100] !== q.hookName)
         ((w = q5.default.createElement(
           Z0,
           { color: "error" },
           q.hookName,
           " hook returned blocking error",
         )),
-          (K[95] = q.hookName),
-          (K[96] = w));
-      else w = K[96];
+          (K[100] = q.hookName),
+          (K[101] = w));
+      else w = K[101];
       return w;
     }
     case "hook_non_blocking_error": {
       if (q.hookEvent === "Stop" || q.hookEvent === "SubagentStop") return null;
       if (z) {
         let H;
-        if (K[97] !== q.hookName || K[98] !== q.stderr)
+        if (K[102] !== q.hookName || K[103] !== q.stderr)
           ((H = q5.default.createElement(
             Z0,
             { color: "error" },
@@ -429,30 +447,30 @@
             " hook error: ",
             q.stderr,
           )),
-            (K[97] = q.hookName),
-            (K[98] = q.stderr),
-            (K[99] = H));
-        else H = K[99];
+            (K[102] = q.hookName),
+            (K[103] = q.stderr),
+            (K[104] = H));
+        else H = K[104];
         return H;
       }
       let w;
-      if (K[100] !== q.hookName)
+      if (K[105] !== q.hookName)
         ((w = q5.default.createElement(
           Z0,
           { color: "error" },
           q.hookName,
           " hook error",
         )),
-          (K[100] = q.hookName),
-          (K[101] = w));
-      else w = K[101];
+          (K[105] = q.hookName),
+          (K[106] = w));
+      else w = K[106];
       return w;
     }
     case "hook_error_during_execution": {
       if (q.hookEvent === "Stop" || q.hookEvent === "SubagentStop") return null;
       if (z) {
         let H;
-        if (K[102] !== q.content || K[103] !== q.hookName)
+        if (K[107] !== q.content || K[108] !== q.hookName)
           ((H = q5.default.createElement(
             Z0,
             null,
@@ -460,18 +478,18 @@
             " hook warning: ",
             q.content,
           )),
-            (K[102] = q.content),
-            (K[103] = q.hookName),
-            (K[104] = H));
-        else H = K[104];
+            (K[107] = q.content),
+            (K[108] = q.hookName),
+            (K[109] = H));
+        else H = K[109];
         return H;
       }
       let w;
-      if (K[105] !== q.hookName)
+      if (K[110] !== q.hookName)
         ((w = q5.default.createElement(Z0, null, q.hookName, " hook warning")),
-          (K[105] = q.hookName),
-          (K[106] = w));
-      else w = K[106];
+          (K[110] = q.hookName),
+          (K[111] = w));
+      else w = K[111];
       return w;
     }
     case "hook_success": {
@@ -479,7 +497,7 @@
       if (z) {
         let w = q.content ? `: ${q.content}` : "",
           H;
-        if (K[107] !== q.hookName || K[108] !== w)
+        if (K[112] !== q.hookName || K[113] !== w)
           ((H = q5.default.createElement(
             Z0,
             null,
@@ -487,10 +505,10 @@
             " hook succeeded",
             w,
           )),
-            (K[107] = q.hookName),
-            (K[108] = w),
-            (K[109] = H));
-        else H = K[109];
+            (K[112] = q.hookName),
+            (K[113] = w),
+            (K[114] = H));
+        else H = K[114];
         return H;
       }
       return null;
@@ -498,7 +516,7 @@
     case "hook_stopped_continuation": {
       if (q.hookEvent === "Stop" || q.hookEvent === "SubagentStop") return null;
       let w;
-      if (K[110] !== q.hookName || K[111] !== q.message)
+      if (K[115] !== q.hookName || K[116] !== q.message)
         ((w = q5.default.createElement(
           Z0,
           { color: "warning" },
@@ -506,15 +524,15 @@
           " hook stopped continuation: ",
           q.message,
         )),
-          (K[110] = q.hookName),
-          (K[111] = q.message),
-          (K[112] = w));
-      else w = K[112];
+          (K[115] = q.hookName),
+          (K[116] = q.message),
+          (K[117] = w));
+      else w = K[117];
       return w;
     }
     case "hook_system_message": {
       let w;
-      if (K[113] !== q.content || K[114] !== q.hookName)
+      if (K[118] !== q.content || K[119] !== q.hookName)
         ((w = q5.default.createElement(
           Z0,
           null,
@@ -522,45 +540,45 @@
           " says: ",
           q.content,
         )),
-          (K[113] = q.content),
-          (K[114] = q.hookName),
-          (K[115] = w));
-      else w = K[115];
+          (K[118] = q.content),
+          (K[119] = q.hookName),
+          (K[120] = w));
+      else w = K[120];
       return w;
     }
     case "hook_permission_decision": {
       let w = q.decision === "allow" ? "Allowed" : "Denied",
         H;
-      if (K[116] !== q.hookEvent)
+      if (K[121] !== q.hookEvent)
         ((H = q5.default.createElement(f, { bold: !0 }, q.hookEvent)),
-          (K[116] = q.hookEvent),
-          (K[117] = H));
-      else H = K[117];
+          (K[121] = q.hookEvent),
+          (K[122] = H));
+      else H = K[122];
       let J;
-      if (K[118] !== w || K[119] !== H)
+      if (K[123] !== w || K[124] !== H)
         ((J = q5.default.createElement(Z0, null, w, " by ", H, " hook")),
-          (K[118] = w),
-          (K[119] = H),
-          (K[120] = J));
-      else J = K[120];
+          (K[123] = w),
+          (K[124] = H),
+          (K[125] = J));
+      else J = K[125];
       return J;
     }
     case "task_status": {
       if (D8() && q.taskType === "in_process_teammate") return null;
       let w = q.status === "completed" ? "completed in background" : q.status,
         H;
-      if (K[121] === Symbol.for("react.memo_cache_sentinel"))
+      if (K[126] === Symbol.for("react.memo_cache_sentinel"))
         ((H = q5.default.createElement(f, { dimColor: !0 }, mY, " ")),
-          (K[121] = H));
-      else H = K[121];
+          (K[126] = H));
+      else H = K[126];
       let J;
-      if (K[122] !== q.description)
+      if (K[127] !== q.description)
         ((J = q5.default.createElement(f, { bold: !0 }, q.description)),
-          (K[122] = q.description),
-          (K[123] = J));
-      else J = K[123];
+          (K[127] = q.description),
+          (K[128] = J));
+      else J = K[128];
       let O;
-      if (K[124] !== w || K[125] !== J)
+      if (K[129] !== w || K[130] !== J)
         ((O = q5.default.createElement(
           I,
           { flexDirection: "row", width: "100%", marginTop: 1 },
@@ -575,10 +593,10 @@
             w,
           ),
         )),
-          (K[124] = w),
-          (K[125] = J),
-          (K[126] = O));
-      else O = K[126];
+          (K[129] = w),
+          (K[130] = J),
+          (K[131] = O));
+      else O = K[131];
       return O;
     }
     case "task_progress":

@@@ function '$E1' (was 'uv1') — structural (62.3%)
--- pretty-v2.1.22.js:518830
+++ pretty-v2.1.23.js:519869
@@ -1,6 +1,5 @@
 function uv1(A, K, q) {
   return GfK.useMemo(() => {
-    if (sH()) return A;
     let Y = gMA(K, q);
     return el([...A, ...Y], "name");
   }, [A, K, q]);

@@@ function 'sf' (was 'lf') — structural (62.2%)
--- pretty-v2.1.22.js:527411
+++ pretty-v2.1.23.js:528460
@@ -21,7 +21,7 @@
     NTK,
     en2(X),
     Ar2(),
-    ...[],
+    ...(G4("tengu_system_prompt_global_cache", !1) ? [UUA] : []),
     Kr2(),
     qr2(),
     J,

@@@ function 'SK6' (was 'KK6') — structural (62.0%)
--- pretty-v2.1.22.js:176829
+++ pretty-v2.1.23.js:176887
@@ -9,6 +9,8 @@
       } = q,
       O = Y.screen,
       X = z.screen,
+      $ = X.charPool,
+      _ = X.hyperlinkPool,
       $ = A.yogaNode?.getComputedHeight(),
       _ = A.yogaNode?.getComputedWidth(),
       Z = $ === void 0 || !Number.isFinite($) || $ < 0,
@@ -19,7 +21,7 @@
           `Invalid yoga dimensions: width=${_}, height=${$}, childNodes=${A.childNodes.length}, terminalWidth=${H}, terminalRows=${J}`,
         );
       return {
-        screen: jyA(H, 0, K),
+        screen: gyA(H, 0, K, $, _),
         viewport: { width: H, height: J },
         cursor: { x: 0, y: 0, visible: !0 },
       };
@@ -30,7 +32,7 @@
         width: W,
         height: D,
         stylePool: K,
-        screen: X ?? jyA(W, D, K),
+        screen: X ?? gyA(j, M, K, $, _),
       });
     EO4(A, j, { skipStaticElements: !0, prevScreen: O });
     let M = j.get();

@@@ function 'PG9' (was '$_9') — structural (61.7%)
--- pretty-v2.1.22.js:192850
+++ pretty-v2.1.23.js:193010
@@ -1,6 +1,6 @@
-function $_9() {
+async function PG9() {
   if (process.env.TERMINAL_EMULATOR === "JetBrains-JediTerm") {
-    if (Q6.platform !== "darwin") return X_9() || "pycharm";
+    if (m6.platform !== "darwin") return (await Py4()) || "pycharm";
   }
   return Q6.terminal;
 }

@@@ function 'mo2' (was 'ln2') — structural (61.4%)
--- pretty-v2.1.22.js:527215
+++ pretty-v2.1.23.js:528264
@@ -2,10 +2,10 @@
   return `
 You are an interactive CLI tool that helps users ${A !== null ? 'according to your "Output Style" below, which describes how you should respond to user queries.' : "with software engineering tasks."} Use the instructions below and the tools available to you to assist the user.
 
-${NTK}.
+${vvK}
 IMPORTANT: You must NEVER generate or guess URLs for the user unless you are confident that the URLs are for helping the user with programming. You may use URLs provided by the user in their messages or local files.
 
 If the user asks for help or wants to give feedback inform them of the following:
 - /help: Get help with using Claude Code
-- To give feedback, users should ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.22", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-28T06:33:34Z" }.ISSUES_EXPLAINER}`;
+- To give feedback, users should ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.23", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-29T00:18:20Z" }.ISSUES_EXPLAINER}`;
 }

@@@ function 'kI7' (was 'Jy7') — structural (61.4%)
--- pretty-v2.1.22.js:340657
+++ pretty-v2.1.23.js:341182
@@ -1,5 +1,5 @@
 function Jy7(A) {
-  let K = s(58),
+  let K = s(65),
     {
       param: q,
       addMargin: Y,
@@ -17,54 +17,57 @@
     } = A,
     D = M8(),
     [j] = R4(),
-    P = Xy7()?.[0]?.pendingWorkerRequest;
+    M = LI7(koY),
+    P = DI7(q.id),
+    f = !1;
   if (!z)
     return (KA(Error(`Tools array is undefined for tool ${q.name}`)), null);
-  let V, N, T, E, R, b, S, B, x, F, Q;
+  let N, T, C, R, x, y, B, b, F, Q, u, d;
   if (
     K[0] !== Y ||
     K[1] !== w ||
     K[2] !== J ||
     K[3] !== G ||
     K[4] !== O ||
-    K[5] !== W ||
-    K[6] !== q.id ||
-    K[7] !== q.input ||
-    K[8] !== q.name ||
-    K[9] !== P?.toolUseId ||
-    K[10] !== $ ||
+    K[5] !== !1 ||
+    K[6] !== W ||
+    K[7] !== q.id ||
+    K[8] !== q.input ||
+    K[9] !== q.name ||
+    K[10] !== M?.toolUseId ||
     K[11] !== X ||
     K[12] !== _ ||
     K[13] !== Z ||
     K[14] !== D ||
     K[15] !== j ||
     K[16] !== z ||
-    K[17] !== H
+    K[17] !== z ||
+    K[18] !== H
   ) {
     Q = Symbol.for("react.early_return_sentinel");
     A: {
       let o;
-      if (K[29] !== q.name)
-        ((o = (mA) => mA.name === q.name), (K[29] = q.name), (K[30] = o));
-      else o = K[30];
+      if (K[31] !== q.name)
+        ((YA = (wA) => wA.name === q.name), (K[31] = q.name), (K[32] = YA));
+      else YA = K[32];
       let l = z.find(o);
       if (!l) {
         (KA(Error(`Tool ${q.name} not found`)), (Q = null));
         break A;
       }
       let e;
-      if (K[31] !== q.id || K[32] !== X)
-        ((e = X.has(q.id)), (K[31] = q.id), (K[32] = X), (K[33] = e));
-      else e = K[33];
+      if (K[33] !== q.id || K[34] !== X)
+        ((qA = X.has(q.id)), (K[33] = q.id), (K[34] = X), (K[35] = qA));
+      else qA = K[35];
       let wA = e,
         HA;
-      if (K[34] !== O || K[35] !== wA || K[36] !== q.id)
+      if (K[36] !== O || K[37] !== HA || K[38] !== q.id)
         ((HA = !O.has(q.id) && !wA),
-          (K[34] = O),
-          (K[35] = wA),
-          (K[36] = q.id),
-          (K[37] = HA));
-      else HA = K[37];
+          (K[36] = O),
+          (K[37] = HA),
+          (K[38] = q.id),
+          (K[39] = _A));
+      else _A = K[39];
       let OA = HA,
         WA = P?.toolUseId === q.id,
         a = l.inputSchema.safeParse(q.input),
@@ -90,12 +93,12 @@
         (T = "column"));
       let SA;
       if (
-        K[38] !== J ||
-        K[39] !== OA ||
         K[40] !== wA ||
-        K[41] !== q.id ||
+        K[41] !== a ||
         K[42] !== _ ||
-        K[43] !== Z
+        K[43] !== q.id ||
+        K[44] !== _ ||
+        K[45] !== G
       )
         ((SA =
           Z &&
@@ -110,66 +113,75 @@
                 isUnresolved: !wA,
                 isError: J.has(q.id),
               }))),
-          (K[38] = J),
-          (K[39] = OA),
           (K[40] = wA),
-          (K[41] = q.id),
+          (K[41] = a),
           (K[42] = _),
-          (K[43] = Z),
-          (K[44] = SA));
-      else SA = K[44];
-      ((E = WW.default.createElement(
-        I,
-        {
-          flexDirection: "row",
-          flexWrap: "nowrap",
-          minWidth: _A.length + (Z ? 2 : 0),
-        },
-        SA,
-        WW.default.createElement(
+          (K[43] = q.id),
+          (K[44] = _),
+          (K[45] = G),
+          (K[46] = AA));
+      else AA = K[46];
+      if (
+        ((x = jW.default.createElement(
+          S,
+          {
+            flexDirection: "row",
+            flexWrap: "nowrap",
+            minWidth: MA.length + (G ? 2 : 0),
+          },
           I,
-          { flexShrink: 0 },
           WW.default.createElement(
             f,
-            {
-              bold: !0,
-              wrap: "truncate-end",
-              backgroundColor: jA,
-              color: jA ? "inverseText" : void 0,
-            },
-            _A,
-          ),
-        ),
-        PA !== "" &&
-          WW.default.createElement(
-            I,
-            { flexWrap: "nowrap" },
-            WW.default.createElement(f, null, "(", PA, ")"),
+            { flexShrink: 0 },
+            jW.default.createElement(
+              V,
+              {
+                bold: !0,
+                wrap: "truncate-end",
+                backgroundColor: hA,
+                color: hA ? "inverseText" : void 0,
+              },
+              MA,
+            ),
           ),
-        a.success && l.renderToolUseTag && l.renderToolUseTag(a.data),
-      )),
-        (R =
-          !wA &&
-          !OA &&
-          (WA
-            ? WW.default.createElement(
+          yA !== "" &&
+            jW.default.createElement(
+              S,
+              { flexWrap: "nowrap" },
+              jW.default.createElement(V, null, "(", yA, ")"),
+            ),
+          jA.success && e.renderToolUseTag && e.renderToolUseTag(jA.data),
+        )),
+        K[47] !== !1 || K[48] !== a || K[49] !== HA)
+      )
+        ((y = !HA && !a && !1),
+          (K[47] = !1),
+          (K[48] = a),
+          (K[49] = HA),
+          (K[50] = y));
+      else y = K[50];
+      ((B =
+        !HA &&
+        !a &&
+        (JA
+          ? jW.default.createElement(
+              k6,
+              { height: 1 },
+              jW.default.createElement(
                 E6,
-                { height: 1 },
-                WW.default.createElement(
-                  f,
-                  { dimColor: !0 },
-                  "Waiting for permission…",
-                ),
-              )
-            : _rY(
-                l,
-                z,
-                W,
-                q.id,
-                $,
-                { verbose: H, inProgressToolCallCount: G },
-                D,
-              ))),
+                { dimColor: !0 },
+                "Waiting for permission…",
+              ),
+            )
+          : LoY(
+              e,
+              z,
+              W,
+              q.id,
+              $,
+              { verbose: H, inProgressToolCallCount: Z },
+              D,
+            ))),
         (b = !wA && OA && ZrY(l)));
     }
     ((K[0] = Y),
@@ -177,12 +189,12 @@
       (K[2] = J),
       (K[3] = G),
       (K[4] = O),
-      (K[5] = W),
-      (K[6] = q.id),
-      (K[7] = q.input),
-      (K[8] = q.name),
-      (K[9] = P?.toolUseId),
-      (K[10] = $),
+      (K[5] = !1),
+      (K[6] = W),
+      (K[7] = q.id),
+      (K[8] = q.input),
+      (K[9] = q.name),
+      (K[10] = M?.toolUseId),
       (K[11] = X),
       (K[12] = _),
       (K[13] = Z),
@@ -200,10 +212,11 @@
       (K[25] = B),
       (K[26] = x),
       (K[27] = F),
-      (K[28] = Q));
+      (K[28] = Q),
+      (K[29] = u),
+      (K[30] = d));
   } else
-    ((V = K[18]),
-      (N = K[19]),
+    ((N = K[19]),
       (T = K[20]),
       (E = K[21]),
       (R = K[22]),
@@ -212,18 +225,10 @@
       (B = K[25]),
       (x = K[26]),
       (F = K[27]),
-      (Q = K[28]));
+      (Q = K[28]),
+      (u = K[29]),
+      (d = K[30]));
   if (Q !== Symbol.for("react.early_return_sentinel")) return Q;
-  let u;
-  if (K[45] !== V || K[46] !== T || K[47] !== E || K[48] !== R || K[49] !== b)
-    ((u = WW.default.createElement(V, { flexDirection: T }, E, R, b)),
-      (K[45] = V),
-      (K[46] = T),
-      (K[47] = E),
-      (K[48] = R),
-      (K[49] = b),
-      (K[50] = u));
-  else u = K[50];
   let d;
   if (
     K[51] !== N ||
@@ -233,11 +238,7 @@
     K[55] !== x ||
     K[56] !== F
   )
-    ((d = WW.default.createElement(
-      N,
-      { flexDirection: S, justifyContent: B, marginTop: x, width: F },
-      u,
-    )),
+    ((r = jW.default.createElement(N, { flexDirection: C }, x, y, B, b)),
       (K[51] = N),
       (K[52] = u),
       (K[53] = S),
@@ -246,5 +247,27 @@
       (K[56] = F),
       (K[57] = d));
   else d = K[57];
+  let c;
+  if (
+    K[58] !== T ||
+    K[59] !== r ||
+    K[60] !== F ||
+    K[61] !== Q ||
+    K[62] !== u ||
+    K[63] !== d
+  )
+    ((c = jW.default.createElement(
+      T,
+      { flexDirection: F, justifyContent: Q, marginTop: u, width: d },
+      r,
+    )),
+      (K[58] = T),
+      (K[59] = r),
+      (K[60] = F),
+      (K[61] = Q),
+      (K[62] = u),
+      (K[63] = d),
+      (K[64] = c));
+  else c = K[64];
   return d;
 }

@@@ function 'HbK' (was 'qhK') — structural (60.9%)
--- pretty-v2.1.22.js:562289
+++ pretty-v2.1.23.js:563920
@@ -1,6 +1,6 @@
 function qhK() {
-  let [A, K] = V6(),
-    { toolPermissionContext: q } = A;
+  let A = F1((q) => q.toolPermissionContext),
+    K = p4();
   KhK.useEffect(() => {
     ip6(q, K);
   }, []);

@@@ function 'REK' (was 'kvK') — structural (60.8%)
--- pretty-v2.1.22.js:532045
+++ pretty-v2.1.23.js:533117
@@ -2,6 +2,5 @@
   if (!XVA()) throw Error("Scratchpad directory feature is not enabled");
   let A = xA(),
     K = KE1();
-  if (!A.existsSync(K)) A.mkdirSync(K);
-  return K;
+  return (A.mkdirSync(K, { mode: 448 }), K);
 }

@@@ function 'yK6' (was 'e76') — structural (60.3%)
--- pretty-v2.1.22.js:176384
+++ pretty-v2.1.23.js:176474
@@ -1,6 +1,5 @@
 function e76(A, K, q) {
   if (K < 0 || q < 0 || K >= A.width || q >= A.height) return;
-  let Y = q * A.width + K,
-    z = A.chars[Y];
-  return A.charStrings[z] ?? " ";
+  let Y = (q * A.width + K) << 1;
+  return A.charPool.get(A.cells[Y]);
 }

@@@ function 'j8z' (was 'q$2') — structural (60.0%)
--- pretty-v2.1.22.js:390023
+++ pretty-v2.1.23.js:552897
@@ -1,3 +1,3 @@
 function q$2(A) {
-  return A.status === "in_progress";
+  return A.type === "in_process_teammate";
 }

@@@ function 'M8z' (was 'nB2') — structural (60.0%)
--- pretty-v2.1.22.js:496696
+++ pretty-v2.1.23.js:552900
@@ -1,3 +1,3 @@
 function nB2(A) {
-  return A.status === "pending";
+  return A.type === "in_process_teammate";
 }

@@@ function 'O9A' (was 'o3A') — structural (59.5%)
--- pretty-v2.1.22.js:453306
+++ pretty-v2.1.23.js:453742
@@ -8,10 +8,14 @@
       boundary: w,
       suggestionLength: H,
       messagesRef: J,
+      isPipelined: O,
     } = K.speculation;
     return (
       h(`[Speculation] Aborting ${q}`),
-      ff1(q, "aborted", z, H, J.current, w, { abort_reason: "user_typed" }),
+      lf1(q, "aborted", z, H, J.current, w, {
+        abort_reason: "user_typed",
+        is_pipelined: O,
+      }),
       Y(),
       hUA(Vf1(q)),
       { ...K, speculation: a3A }

@@@ function '_T6' (was 'bN6') — structural (59.3%)
--- pretty-v2.1.22.js:339210
+++ pretty-v2.1.23.js:339713
@@ -2,10 +2,9 @@
   return A.filter((z) => {
     if (z.name.startsWith("mcp__")) return !0;
     if (z.name === VC && Y === "plan") return !0;
-    let w = tnY();
-    if (w.ALL_AGENT_DISALLOWED_TOOLS.has(z.name)) return !1;
-    if (!K && w.CUSTOM_AGENT_DISALLOWED_TOOLS.has(z.name)) return !1;
-    if (q && !w.ASYNC_AGENT_ALLOWED_TOOLS.has(z.name)) {
+    if (MDA.has(z.name)) return !1;
+    if (!K && XT6.has(z.name)) return !1;
+    if (q && !$T6.has(z.name)) {
       if (D8() && z.name === G5 && IG()) return !0;
       return !1;
     }

@@@ function 'CB6' (was 'V6') — structural (58.1%)
--- pretty-v2.1.22.js:470208
+++ pretty-v2.1.23.js:470771
@@ -1,8 +1,8 @@
 function V6() {
   let A = I$.useContext(Uu6);
-  if (!A.__IS_INITIALIZED__)
+  if (!A)
     throw ReferenceError(
-      "useAppState cannot be called outside of an <AppStateProvider />",
+      "useAppState/useSetAppState cannot be called outside of an <AppStateProvider />",
     );
   return A;
 }

@@@ variable 'Rr' (was 'm4A') — structural (58.1%)
--- pretty-v2.1.22.js:192865
+++ pretty-v2.1.23.js:193037
@@ -24,23 +24,6 @@
       } catch {
         return (h("musl detection failed, assuming glibc"), !1);
       }
-    })),
-    (X_9 = a1(() => {
-      if (process.platform === "darwin") return null;
-      try {
-        let K = process.pid.toString();
-        for (let q = 0; q < 10; q++) {
-          let Y = n31(K);
-          if (Y) {
-            let w = Y.toLowerCase();
-            for (let H of oh1) if (w.includes(H)) return H;
-          }
-          let z = i31(K);
-          if (!z || z === "0" || z === K) break;
-          K = z;
-        }
-      } catch {}
-      return null;
     })));
   gV = {
     ...Q6,
@@ -48,5 +31,7 @@
     getIsDocker: H_9,
     getIsBubblewrapSandbox: J_9,
     isMuslEnvironment: O_9,
+    getTerminalWithJetBrainsDetectionAsync: PG9,
+    initJetBrainsDetection: R36,
   };
 });

@@@ function 'gyA' (was 'jyA') — structural (57.9%)
--- pretty-v2.1.22.js:176298
+++ pretty-v2.1.23.js:176389
@@ -1,4 +1,4 @@
-function jyA(A, K, q) {
+function gyA(A, K, q, Y, z) {
   if (
     (ZO(A, "createScreen width"),
     ZO(K, "createScreen height"),
@@ -7,27 +7,16 @@
     A = Math.max(0, Math.floor(A) || 0);
   if (!Number.isInteger(K) || K < 0) K = Math.max(0, Math.floor(K) || 0);
   let Y = A * K,
-    z = new Int32Array(Y);
-  z.fill(wr);
-  let w = new Uint16Array(Y);
-  w.fill(fQ);
-  let H = new Uint8Array(Y),
-    J = new Uint16Array(Y);
+    H = new ArrayBuffer(w << 3),
+    J = new Int32Array(H),
+    O = new BigInt64Array(H);
   return {
     width: A,
     height: K,
-    chars: z,
-    styleIds: w,
-    widths: H,
-    hyperlinkIds: J,
-    charStrings: [" ", ""],
-    charStringMap: new Map([
-      [" ", wr],
-      ["", O51],
-    ]),
-    charAscii: Os3(),
-    hyperlinks: [""],
-    hyperlinkMap: new Map(),
+    cells: J,
+    cells64: O,
+    charPool: Y,
+    hyperlinkPool: z,
     emptyStyleId: q.none,
     damage: void 0,
   };

@@@ variable 'B3A' (was 'qP1') — structural (57.9%)
--- pretty-v2.1.22.js:413510
+++ pretty-v2.1.23.js:414106
@@ -25,4 +25,6 @@
   nG();
   KP1();
   Tt();
+  WmA();
+  q6();
 });

@@@ variable 'St' (was '$P1') — structural (57.9%)
--- pretty-v2.1.22.js:415682
+++ pretty-v2.1.23.js:459618
@@ -9,4 +9,27 @@
   s1();
   Tv();
   lBA();
+  vC();
+  hD();
+  a_6();
+  sD();
+  xu();
+  i6();
+  NG();
+  Oz();
+  Hu6();
+  iP();
+  dT();
+  RJK();
+  C1();
+  Z1();
+  B7();
+  q5A();
+  aU();
+  JP();
+  Ye();
+  q6();
+  UK();
+  b1();
+  eB();
 });

@@@ variable 'Pv1' (was 'Tt') — structural (57.9%)
--- pretty-v2.1.22.js:459104
+++ pretty-v2.1.23.js:497170
@@ -11,24 +11,4 @@
   PC();
   CD();
   N_6();
-  aT();
-  ku();
-  c6();
-  PZ();
-  Wz();
-  vx6();
-  lP();
-  FT();
-  IHK();
-  v1();
-  W1();
-  l7();
-  nqA();
-  QU();
-  zP();
-  rt();
-  s1();
-  UK();
-  h1();
-  dB();
 });

@@@ variable 'sz' (was 'ML') — structural (57.9%)
--- pretty-v2.1.22.js:464041
+++ pretty-v2.1.23.js:529668
@@ -9,4 +9,46 @@
   uG();
   W1();
   pQA();
+  C1();
+  $8();
+  K7();
+  IH();
+  oZ();
+  iP();
+  jI();
+  B7();
+  B7();
+  l1();
+  v_6();
+  RxA();
+  bQA();
+  zyA();
+  Xw();
+  q5A();
+  z1A();
+  ok();
+  vC();
+  ao();
+  lu();
+  W$();
+  Z1();
+  uxA();
+  Gs();
+  IWA();
+  cp();
+  iP();
+  qPA();
+  iUA();
+  q6();
+  y6A();
+  cT();
+  x4();
+  kNA();
+  K7();
+  zs();
+  Ys();
+  kq1();
+  Ck();
+  b1();
+  B7();
 });

@@@ variable 'Nd6' (was 'hr') — structural (57.9%)
--- pretty-v2.1.22.js:469981
+++ pretty-v2.1.23.js:561203
@@ -12,4 +12,5 @@
   ZH();
   Z_();
   y9();
+  YMA();
 });

@@@ variable 'mQK' (was 'Kw') — structural (57.9%)
--- pretty-v2.1.22.js:528608
+++ pretty-v2.1.23.js:572927
@@ -5,49 +5,4 @@
   L46();
   df();
   it();
-  lk();
-  c6();
-  L4();
-  l6();
-  v1();
-  j8();
-  z7();
-  jJ();
-  nG();
-  lP();
-  JI();
-  l7();
-  l7();
-  i1();
-  r$6();
-  JxA();
-  HQA();
-  gRA();
-  $w();
-  nqA();
-  rAA();
-  lk();
-  PC();
-  Uo();
-  Bu();
-  _$();
-  W1();
-  Ys();
-  ZWA();
-  xp();
-  lP();
-  UMA();
-  EUA();
-  s1();
-  V6A();
-  UT();
-  L4();
-  wNA();
-  z7();
-  aa();
-  oa();
-  Jq1();
-  vk();
-  h1();
-  l7();
 });

@@@ variable 'sQK' (was 'OQK') — structural (57.9%)
--- pretty-v2.1.22.js:572456
+++ pretty-v2.1.23.js:573393
@@ -3,4 +3,11 @@
   HQK();
   l7();
   l6();
+  xu();
+  xVA();
+  IG();
+  IcA();
+  x4();
+  C1();
+  xcA();
 });

@@@ function 'Fv1' (was 'Xv1') — structural (57.8%)
--- pretty-v2.1.22.js:502684
+++ pretty-v2.1.23.js:503715
@@ -6,11 +6,13 @@
           "report the issue at https://github.com/anthropics/claude-code/issues",
         PACKAGE_URL: "@anthropic-ai/claude-code",
         README_URL: "https://code.claude.com/docs/en/overview",
-        VERSION: "2.1.22",
+        VERSION: "2.1.23",
         FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-        BUILD_TIME: "2026-01-28T06:33:34Z",
+        BUILD_TIME: "2026-01-29T00:18:20Z",
       }.VERSION,
+    K = rn6(),
     K = process.env.DEMO_VERSION ? "/code/claude" : M5(b1()),
+    Y = K ? `${q} in ${K.replace(/^https?:\/\//, "")}` : q,
     q = Z3(),
     Y = rw4(q),
     z = O4() ? hg6() : "API Usage Billing",

@@@ variable 'A4' — structural (57.4%)
--- pretty-v2.1.22.js:470222
+++ pretty-v2.1.23.js:470823
@@ -12,6 +12,6 @@
   W1();
   s1();
   ((I$ = r($A(), 1)), (a3A = { status: "idle" }));
-  ((Uu6 = I$.default.createContext([{}, (A) => A])),
+  ((kB6 = E_.default.createContext(null)),
     (k0K = I$.default.createContext(!1)));
 });

@@@ function 'Dr' (was 'MXA') — structural (56.8%)
--- pretty-v2.1.22.js:180756
+++ pretty-v2.1.23.js:180810
@@ -1,6 +1,6 @@
-function MXA(A, K, q) {
+function Dr(A, K, q, Y, z) {
   return {
-    screen: jyA(0, 0, q),
+    screen: gyA(0, 0, q, Y, z),
     viewport: { width: K, height: A },
     cursor: { x: 0, y: 0, visible: !0 },
   };

@@@ variable 'ed6' (was 'dFK') — structural (56.7%)
--- pretty-v2.1.22.js:571603
+++ pretty-v2.1.23.js:569079
@@ -8,5 +8,142 @@
   C8();
   WT1();
   o9A();
-  dJ = r($A(), 1);
+  q6();
+  Z1();
+  b1();
+  Nv();
+  _MA();
+  _H();
+  zm();
+  dQA();
+  W2();
+  QCK();
+  zm();
+  Ys();
+  dCK();
+  Yk1();
+  aCK();
+  ARK();
+  HRK();
+  HSK();
+  OSK();
+  ZSK();
+  jSK();
+  MSK();
+  i2();
+  fSK();
+  of();
+  AO1();
+  YC();
+  gZ();
+  Kp6();
+  Ck();
+  Wd6();
+  kSK();
+  xy();
+  LSK();
+  ySK();
+  ISK();
+  cB();
+  Vz();
+  hSK();
+  xSK();
+  QSK();
+  dSK();
+  nSK();
+  LH();
+  Tp6();
+  i6();
+  l1();
+  $8();
+  FBA();
+  wz();
+  cp();
+  Sw();
+  YhK();
+  JhK();
+  XhK();
+  qPA();
+  m3A();
+  GhK();
+  MI6();
+  $Q6();
+  WhK();
+  jhK();
+  vd6();
+  DVA();
+  lFA();
+  DR6();
+  PhK();
+  jR6();
+  _IA();
+  Ye();
+  fhK();
+  f_();
+  E5A();
+  $QA();
+  A4();
+  xu();
+  NG();
+  UK();
+  JPA();
+  pf1();
+  G9A();
+  AP();
+  V7A();
+  UK();
+  OlA();
+  EhK();
+  t9();
+  khK();
+  iH();
+  RhK();
+  vQ6();
+  TT1();
+  Tf();
+  ShK();
+  R_1();
+  bhK();
+  QqA();
+  YpA();
+  SM6();
+  ZR6();
+  Jz();
+  Te();
+  ghK();
+  QhK();
+  dhK();
+  ihK();
+  rhK();
+  shK();
+  ehK();
+  zbK();
+  JbK();
+  SH();
+  XbK();
+  $bK();
+  _gK();
+  Sm6();
+  WgK();
+  jgK();
+  LgK();
+  IgK();
+  bgK();
+  ugK();
+  mgK();
+  MP1();
+  FgK();
+  UgK();
+  dgK();
+  lgK();
+  ngK();
+  ogK();
+  tgK();
+  KFK();
+  zFK();
+  JFK();
+  XFK();
+  GFK();
+  WFK();
+  ((T4 = o($A(), 1)), (q8 = o($A(), 1)));
 });

@@@ variable 'zpK' (was 'lQK') — structural (56.7%)
--- pretty-v2.1.22.js:575991
+++ pretty-v2.1.23.js:577971
@@ -9,8 +9,5 @@
   _3A();
   NS();
   mK();
-  eq();
-  d2();
-  Zq();
-  tK = r($A(), 1);
+  ((Ij = o($A(), 1)), (qpK = o($A(), 1)));
 });

@@@ function 'VC2' (was '_k2') — structural (56.6%)
--- pretty-v2.1.22.js:453266
+++ pretty-v2.1.23.js:453700
@@ -7,19 +7,20 @@
       abort: H,
       startTime: J,
       suggestionLength: O,
+      isPipelined: X,
     } = A,
     X = z.current,
     $ = Vf1(Y),
     _ = Date.now();
   if ((H(), q > 0)) Ok2($, w.current, Eg());
   hUA($);
-  let Z = null,
-    G = 0;
+  let Z = A.boundary,
+    W = Math.min(G, Z?.completedAt ?? 1 / 0) - J;
   return (
     K((W) => {
-      if (W.speculation.status === "active")
+      if (D.speculation.status === "active" && D.speculation.boundary)
         ((Z = W.speculation.boundary),
-          (G = Math.min(_, Z?.completedAt ?? 1 / 0) - J));
+          (W = Math.min(G, Z.completedAt ?? 1 / 0) - J));
       return {
         ...W,
         speculation: a3A,
@@ -34,6 +35,7 @@
     ff1(Y, "accepted", J, O, X, Z, {
       message_count: X.length,
       time_saved_ms: G,
+      is_pipelined: X,
     }),
     { messages: X, boundary: Z, timeSavedMs: G }
   );

@@@ function 'L46' (was 't86') — structural (56.5%)
--- pretty-v2.1.22.js:157589
+++ pretty-v2.1.23.js:157609
@@ -1,10 +1,14 @@
 function t86() {
   let A = Zy();
   if (!A) return {};
-  let K = { cert: A.cert, key: A.key, passphrase: A.passphrase },
-    q = new r86({ connect: K, pipelining: 1 });
+  if (typeof Bun < "u") return { tls: A };
   return (
     h("mTLS: Created undici agent with custom certificates"),
-    { dispatcher: q }
+    {
+      dispatcher: new v46({
+        connect: { cert: A.cert, key: A.key, passphrase: A.passphrase },
+        pipelining: 1,
+      }),
+    }
   );
 }

@@@ function 'r7K' (was 'm4K') — structural (55.6%)
--- pretty-v2.1.22.js:414235
+++ pretty-v2.1.23.js:414558
@@ -138,7 +138,7 @@
 - They will send you messages when they complete tasks or need help
 - These messages appear automatically as new conversation turns (like user messages)
 - If you're busy (mid-turn), messages are queued and delivered when your turn ends
-- The UI shows "Queued teammate messages" when messages are waiting
+- The UI shows a brief notification with the sender's name when messages are waiting
 
 Messages will be delivered automatically.

@@@ function 'XWK' (was 'JGK') — structural (55.5%)
--- pretty-v2.1.22.js:488175
+++ pretty-v2.1.23.js:489192
@@ -1,5 +1,9 @@
 function JGK(A, K = !1, q) {
-  let [Y, z] = V6(),
+  let Y = F1((W) => W.mcp.clients),
+    z = F1((W) => W.mcp.tools),
+    w = F1((W) => W.mcp.resources),
+    H = F1((W) => W.authVersion),
+    J = p4(),
     w = GP.useRef(new Map()),
     H = GP.useCallback(
       ({ tools: _, commands: Z, resources: G, ...W }) => {
@@ -310,7 +314,7 @@
           _ = !0;
         }
       );
-    }, [K, A, J, O, Y.authVersion, z]),
+    }, [K, A, $, _, H, J]),
     GP.useEffect(() => {
       let _ = w.current;
       return () => {
@@ -318,27 +322,24 @@
         _.clear();
       };
     }, []),
-    GP.useEffect(() => {}, [Y.mcp.clients, z]),
-    GP.useEffect(() => q?.updateClients(Y.mcp.clients), [q, Y.mcp.clients]),
-    GP.useEffect(() => q?.updateTools(Y.mcp.tools), [q, Y.mcp.tools]),
-    GP.useEffect(
-      () => q?.updateResources(Y.mcp.resources),
-      [q, Y.mcp.resources],
-    ));
+    MP.useEffect(() => {}, [Y, J]),
+    MP.useEffect(() => q?.updateClients(Y), [q, Y]),
+    MP.useEffect(() => q?.updateTools(z), [q, z]),
+    MP.useEffect(() => q?.updateResources(w), [q, w]));
   let X = GP.useCallback(
       async (_) => {
-        let Z = Y.mcp.clients.find((D) => D.name === _);
+        let D = Y.find((P) => P.name === W);
         if (!Z) throw Error(`MCP server ${_} not found`);
         let G = w.current.get(_);
         if (G) (clearTimeout(G), w.current.delete(_));
         let W = await su(_, Z.config);
         return (J(W), W);
       },
-      [Y.mcp.clients, J, z],
+      [Y, $, J],
     ),
     $ = GP.useCallback(
       async (_) => {
-        let Z = Y.mcp.clients.find((W) => W.name === _);
+        let D = Y.find((M) => M.name === W);
         if (!Z) throw Error(`MCP server ${_} not found`);
         if (Z.type !== "disabled") {
           let W = w.current.get(_);
@@ -351,7 +352,7 @@
           J(W);
         }
       },
-      [Y.mcp.clients, H, J, z],
+      [Y, X, $, J],
     );
   return { reconnectMcpServer: X, toggleMcpServer: $ };
 }

@@@ function 'u_K' (was 'u$K') — structural (55.3%)
--- pretty-v2.1.22.js:477224
+++ pretty-v2.1.23.js:477861
@@ -1,7 +1,8 @@
 function u$K(A) {
-  let K = s(21),
+  let K = s(18),
     { context: q } = A,
-    [Y] = V6(),
+    Y = F1(dx2),
+    z = F1(px2),
     z;
   if (K[0] === Symbol.for("react.memo_cache_sentinel")) ((z = []), (K[0] = z));
   else z = K[0];
@@ -10,37 +11,34 @@
   if (K[1] === Symbol.for("react.memo_cache_sentinel")) ((J = []), (K[1] = J));
   else J = K[1];
   let [O, X] = D3.useState(J),
-    $ = q.options.ideInstallationStatus,
     [_] = R4(),
+    G,
     Z;
-  if (K[2] !== Y || K[3] !== q || K[4] !== _)
+  if (K[2] !== q || K[3] !== Y || K[4] !== z || K[5] !== _)
     ((Z = () => {
       (async function () {
-        let T = [Cb2(), Lb2({ appState: Y, theme: _, context: q })],
+        let T = [
+            ux2(),
+            Bx2({ mainLoopModel: Y, mcp: z, theme: _, context: q }),
+          ],
           E = await Rb2();
         (H(T), X(E));
       })();
     }),
+      (Z = [Y, z, _, q]),
       (K[2] = Y),
       (K[3] = q),
       (K[4] = _),
-      (K[5] = Z));
-  else Z = K[5];
-  let G;
-  if (K[6] !== Y || K[7] !== q || K[8] !== $ || K[9] !== _)
-    ((G = [Y, _, $, q]),
+      (K[5] = _),
       (K[6] = Y),
-      (K[7] = q),
-      (K[8] = $),
-      (K[9] = _),
-      (K[10] = G));
-  else G = K[10];
+      (K[7] = Z));
+  else ((G = K[6]), (Z = K[7]));
   D3.useEffect(Z, G);
   let W;
-  if (K[11] !== w) ((W = w.map(Sb2)), (K[11] = w), (K[12] = W));
-  else W = K[12];
+  if (K[8] !== H) ((W = H.map(Qx2)), (K[8] = H), (K[9] = W));
+  else W = K[9];
   let D;
-  if (K[13] !== O)
+  if (K[10] !== X)
     ((D =
       O.length > 0 &&
       D3.createElement(
@@ -49,23 +47,23 @@
         D3.createElement(f, { bold: !0 }, "System Diagnostics"),
         O.map(Ib2),
       )),
-      (K[13] = O),
-      (K[14] = D));
-  else D = K[14];
+      (K[10] = X),
+      (K[11] = D));
+  else D = K[11];
   let j;
-  if (K[15] !== W || K[16] !== D)
+  if (K[12] !== W || K[13] !== D)
     ((j = D3.createElement(
       I,
       { flexDirection: "column", gap: 1, marginTop: 1 },
       W,
       D,
     )),
-      (K[15] = W),
-      (K[16] = D),
-      (K[17] = j));
-  else j = K[17];
+      (K[12] = W),
+      (K[13] = D),
+      (K[14] = j));
+  else j = K[14];
   let M;
-  if (K[18] === Symbol.for("react.memo_cache_sentinel"))
+  if (K[15] === Symbol.for("react.memo_cache_sentinel"))
     ((M = D3.createElement(
       f,
       { dimColor: !0 },
@@ -76,13 +74,13 @@
         description: "cancel",
       }),
     )),
-      (K[18] = M));
-  else M = K[18];
+      (K[15] = M));
+  else M = K[15];
   let P;
-  if (K[19] !== j)
+  if (K[16] !== j)
     ((P = D3.createElement(I, { flexDirection: "column" }, j, M)),
-      (K[19] = j),
-      (K[20] = P));
-  else P = K[20];
+      (K[16] = j),
+      (K[17] = P));
+  else P = K[17];
   return P;
 }

@@@ function 'oPK' (was 'nMK') — structural (55.1%)
--- pretty-v2.1.22.js:508083
+++ pretty-v2.1.23.js:509118
@@ -1,42 +1,38 @@
 function nMK(A) {
-  let K = s(65),
+  let K = s(64),
     { agent: q, onDone: Y, onKillAgent: z, onBack: w, onForeground: H } = A,
-    [J] = V6(),
     O;
-  if (K[0] !== q.agentId || K[1] !== J.todos)
-    ((O = J.todos[q.agentId] ?? []),
-      (K[0] = q.agentId),
-      (K[1] = J.todos),
-      (K[2] = O));
-  else O = K[2];
-  let X = O,
+  if (K[0] !== q.agentId)
+    ((J = (jA) => jA.todos[q.agentId]), (K[0] = q.agentId), (K[1] = J));
+  else J = K[1];
+  let X = F1(J) ?? lc2,
     $;
-  if (K[3] !== X) (($ = X.filter($d2)), (K[3] = X), (K[4] = $));
-  else $ = K[4];
+  if (K[2] !== X) (($ = X.filter(oc2)), (K[2] = X), (K[3] = $));
+  else $ = K[3];
   let _ = $.length,
     [Z] = R4(),
     G;
-  if (K[5] === Symbol.for("react.memo_cache_sentinel"))
-    ((G = L$(q_())), (K[5] = G));
-  else G = K[5];
+  if (K[4] === Symbol.for("react.memo_cache_sentinel"))
+    ((Z = I$(w_())), (K[4] = Z));
+  else Z = K[4];
   let W = G,
     D = tPA(q.startTime, q.status === "running"),
     j;
-  if (K[6] !== Y)
-    ((j = { "confirm:no": Y, "confirm:yes": Y }), (K[6] = Y), (K[7] = j));
+  if (K[5] !== Y)
+    ((j = { "confirm:no": Y, "confirm:yes": Y }), (K[5] = Y), (K[6] = j));
+  else j = K[6];
+  let M;
+  if (K[7] === Symbol.for("react.memo_cache_sentinel"))
+    ((M = { context: "Confirmation" }), (K[7] = M));
   else j = K[7];
-  let M;
-  if (K[8] === Symbol.for("react.memo_cache_sentinel"))
-    ((M = { context: "Confirmation" }), (K[8] = M));
-  else M = K[8];
   O7(j, M);
   let P;
   if (
-    K[9] !== q.status ||
+    K[8] !== q.status ||
+    K[9] !== w ||
     K[10] !== w ||
     K[11] !== Y ||
-    K[12] !== H ||
-    K[13] !== z
+    K[12] !== z
   )
     ((P = (jA, PA) => {
       if (jA === " ") Y();
@@ -44,19 +40,19 @@
       else if (jA === "k" && q.status === "running" && z) z();
       else if (jA === "f" && q.status === "running" && H) H();
     }),
-      (K[9] = q.status),
+      (K[8] = q.status),
+      (K[9] = w),
       (K[10] = w),
       (K[11] = Y),
       (K[12] = H),
-      (K[13] = z),
-      (K[14] = P));
-  else P = K[14];
+      (K[13] = P));
+  else P = K[13];
   e6(P);
   let V = r8(),
     N;
-  if (K[15] !== q.prompt)
-    ((N = n7(q.prompt, "plan")), (K[15] = q.prompt), (K[16] = N));
-  else N = K[16];
+  if (K[14] !== q.prompt)
+    ((N = i7(q.prompt, "plan")), (K[14] = q.prompt), (K[15] = N));
+  else N = K[15];
   let T = N,
     E = q.prompt.length > 300 ? q.prompt.substring(0, 297) + "…" : q.prompt,
     R = q.result?.totalTokens ?? q.progress?.tokenCount,
@@ -64,7 +60,7 @@
     S = q.selectedAgent?.agentType ?? "agent",
     B = q.description || "Async agent",
     x;
-  if (K[17] !== S || K[18] !== B)
+  if (K[16] !== y || K[17] !== B)
     ((x = U9.default.createElement(
       I,
       null,
@@ -77,12 +73,12 @@
         B,
       ),
     )),
+      (K[16] = y),
       (K[17] = S),
-      (K[18] = B),
-      (K[19] = x));
-  else x = K[19];
+      (K[18] = b));
+  else b = K[18];
   let F;
-  if (K[20] !== q.status)
+  if (K[19] !== q.status)
     ((F =
       q.status !== "running" &&
       U9.default.createElement(
@@ -97,11 +93,11 @@
             : "Killed",
         " · ",
       )),
-      (K[20] = q.status),
-      (K[21] = F));
-  else F = K[21];
+      (K[19] = q.status),
+      (K[20] = F));
+  else F = K[20];
   let Q;
-  if (K[22] !== R)
+  if (K[21] !== R)
     ((Q =
       R !== void 0 &&
       R > 0 &&
@@ -112,11 +108,11 @@
         i5(R),
         " tokens",
       )),
-      (K[22] = R),
-      (K[23] = Q));
-  else Q = K[23];
+      (K[21] = R),
+      (K[22] = Q));
+  else Q = K[22];
   let u;
-  if (K[24] !== b)
+  if (K[23] !== x)
     ((u =
       b !== void 0 &&
       b > 0 &&
@@ -129,26 +125,26 @@
         " ",
         b === 1 ? "tool" : "tools",
       )),
-      (K[24] = b),
-      (K[25] = u));
-  else u = K[25];
+      (K[23] = x),
+      (K[24] = u));
+  else u = K[24];
   let d;
-  if (K[26] !== D || K[27] !== Q || K[28] !== u)
+  if (K[25] !== D || K[26] !== Q || K[27] !== u)
     ((d = U9.default.createElement(f, { dimColor: !0 }, D, Q, u)),
+      (K[25] = D),
       (K[26] = D),
       (K[27] = Q),
-      (K[28] = u),
-      (K[29] = d));
-  else d = K[29];
+      (K[28] = d));
+  else d = K[28];
   let o;
-  if (K[30] !== F || K[31] !== d)
+  if (K[29] !== F || K[30] !== d)
     ((o = U9.default.createElement(I, null, F, d)),
+      (K[29] = F),
       (K[30] = F),
-      (K[31] = d),
-      (K[32] = o));
-  else o = K[32];
+      (K[31] = r));
+  else r = K[31];
   let l;
-  if (K[33] !== q.progress || K[34] !== q.status || K[35] !== Z)
+  if (K[32] !== q.progress || K[33] !== q.status || K[34] !== G)
     ((l =
       q.status === "running" &&
       q.progress?.recentActivities &&
@@ -170,13 +166,13 @@
           ),
         ),
       )),
-      (K[33] = q.progress),
-      (K[34] = q.status),
-      (K[35] = Z),
-      (K[36] = l));
-  else l = K[36];
+      (K[32] = q.progress),
+      (K[33] = q.status),
+      (K[34] = G),
+      (K[35] = c));
+  else c = K[35];
   let e;
-  if (K[37] !== _ || K[38] !== X)
+  if (K[36] !== _ || K[37] !== X)
     ((e =
       X.length > 0 &&
       U9.default.createElement(
@@ -193,12 +189,12 @@
         ),
         U9.default.createElement(Zt, { todos: X }),
       )),
+      (K[36] = _),
       (K[37] = _),
-      (K[38] = X),
-      (K[39] = e));
-  else e = K[39];
+      (K[38] = YA));
+  else YA = K[38];
   let wA;
-  if (K[40] !== E || K[41] !== T)
+  if (K[39] !== C || K[40] !== T)
     ((wA = T
       ? U9.default.createElement(
           I,
@@ -211,12 +207,12 @@
           U9.default.createElement(f, { bold: !0, dimColor: !0 }, "Prompt"),
           U9.default.createElement(f, { wrap: "wrap" }, E),
         )),
+      (K[39] = C),
       (K[40] = E),
-      (K[41] = T),
-      (K[42] = wA));
-  else wA = K[42];
+      (K[41] = e));
+  else e = K[41];
   let HA;
-  if (K[43] !== q.error || K[44] !== q.status)
+  if (K[42] !== q.error || K[43] !== q.status)
     ((HA =
       q.status === "failed" &&
       q.error &&
@@ -226,12 +222,12 @@
         U9.default.createElement(f, { bold: !0, color: "error" }, "Error"),
         U9.default.createElement(f, { color: "error", wrap: "wrap" }, q.error),
       )),
-      (K[43] = q.error),
-      (K[44] = q.status),
-      (K[45] = HA));
-  else HA = K[45];
+      (K[42] = q.error),
+      (K[43] = q.status),
+      (K[44] = qA));
+  else qA = K[44];
   let OA;
-  if (K[46] !== l || K[47] !== e || K[48] !== wA || K[49] !== HA)
+  if (K[45] !== c || K[46] !== YA || K[47] !== e || K[48] !== qA)
     ((OA = U9.default.createElement(
       I,
       { flexDirection: "column" },
@@ -240,14 +236,14 @@
       wA,
       HA,
     )),
+      (K[45] = c),
       (K[46] = l),
       (K[47] = e),
       (K[48] = wA),
-      (K[49] = HA),
-      (K[50] = OA));
-  else OA = K[50];
+      (K[49] = HA));
+  else HA = K[49];
   let WA;
-  if (K[51] !== x || K[52] !== o || K[53] !== OA)
+  if (K[50] !== b || K[51] !== r || K[52] !== HA)
     ((WA = U9.default.createElement(
       I,
       { width: "100%" },
@@ -267,19 +263,19 @@
         OA,
       ),
     )),
+      (K[50] = b),
       (K[51] = x),
       (K[52] = o),
-      (K[53] = OA),
-      (K[54] = WA));
-  else WA = K[54];
+      (K[53] = _A));
+  else _A = K[53];
   let a;
   if (
-    K[55] !== q.status ||
-    K[56] !== V.keyName ||
-    K[57] !== V.pending ||
+    K[54] !== q.status ||
+    K[55] !== f.keyName ||
+    K[56] !== f.pending ||
+    K[57] !== w ||
     K[58] !== w ||
-    K[59] !== H ||
-    K[60] !== z
+    K[59] !== z
   )
     ((a = U9.default.createElement(
       I,
@@ -319,25 +315,25 @@
             ),
           ),
     )),
-      (K[55] = q.status),
-      (K[56] = V.keyName),
-      (K[57] = V.pending),
+      (K[54] = q.status),
+      (K[55] = f.keyName),
+      (K[56] = f.pending),
+      (K[57] = w),
       (K[58] = w),
       (K[59] = H),
-      (K[60] = z),
-      (K[61] = a));
-  else a = K[61];
+      (K[60] = a));
+  else a = K[60];
   let _A;
-  if (K[62] !== WA || K[63] !== a)
+  if (K[61] !== _A || K[62] !== a)
     ((_A = U9.default.createElement(
       I,
       { width: "100%", flexDirection: "column" },
       WA,
       a,
     )),
+      (K[61] = _A),
       (K[62] = WA),
-      (K[63] = a),
-      (K[64] = _A));
-  else _A = K[64];
+      (K[63] = JA));
+  else JA = K[63];
   return _A;
 }

@@@ function 'b04' (was 'FO4') — structural (54.4%)
--- pretty-v2.1.22.js:176332
+++ pretty-v2.1.23.js:176412
@@ -7,24 +7,12 @@
     K = Math.max(0, Math.floor(K) || 0);
   if (!Number.isInteger(q) || q < 0) q = Math.max(0, Math.floor(q) || 0);
   let Y = K * q;
-  if (A.chars.length < Y)
-    ((A.chars = new Int32Array(Y)),
-      (A.styleIds = new Uint16Array(Y)),
-      (A.widths = new Uint8Array(Y)),
-      (A.hyperlinkIds = new Uint16Array(Y)));
-  (A.chars.fill(wr, 0, Y),
-    A.styleIds.fill(fQ, 0, Y),
-    A.widths.fill(0, 0, Y),
-    A.hyperlinkIds.fill(0, 0, Y),
+  if (A.cells64.length < Y) {
+    let z = new ArrayBuffer(Y << 3);
+    ((A.cells = new Int32Array(z)), (A.cells64 = new BigInt64Array(z)));
+  }
+  (A.cells64.fill(S04, 0, Y),
     (A.width = K),
     (A.height = q),
-    (A.charStrings.length = 2),
-    A.charStringMap.clear(),
-    A.charStringMap.set(" ", wr),
-    A.charStringMap.set("", O51),
-    A.charAscii.fill(-1),
-    (A.charAscii[32] = wr),
-    (A.hyperlinks.length = 1),
-    A.hyperlinkMap.clear(),
     (A.damage = void 0));
 }

@@@ function 'Bx2' (was 'Lb2') — structural (53.6%)
--- pretty-v2.1.22.js:477175
+++ pretty-v2.1.23.js:477812
@@ -1,8 +1,8 @@
-function Lb2({ appState: A, theme: K, context: q }) {
+function Bx2({ mainLoopModel: A, mcp: K, theme: q, context: Y }) {
   return [
-    { label: "Model", value: h$K(A.mainLoopModel) },
-    ...E$K(A.mcp.clients, q.options.ideInstallationStatus, K),
-    ...k$K(A.mcp.clients, K),
+    { label: "Model", value: h_K(A) },
+    ...E_K(K.clients, Y.options.ideInstallationStatus, q),
+    ...k_K(K.clients, q),
     { label: "Memory", value: D3.createElement(z$K, { context: q, flat: !0 }) },
     ...v$K(),
     ...L$K(),

@@@ function 'gIK' (was 'xyK') — structural (53.6%)
--- pretty-v2.1.22.js:555086
+++ pretty-v2.1.23.js:556401
@@ -1,31 +1,33 @@
 function xyK() {
-  let A = s(10),
-    [K] = V6(),
-    { queuedCommands: q } = K;
-  if (IqA(K)) return null;
+  let A = s(11),
+    K = F1(m4z),
+    q = D0();
+  if (lD7(q.getState())) return null;
   if (q.length === 0) return null;
-  let Y, z, w, H;
+  let Y, z, w, H, J;
   if (A[0] !== q) {
-    let O = P6z(q),
-      X = e2(O.map(f6z));
-    ((Y = I),
-      (z = 1),
-      (w = "column"),
-      (H = X.map(V6z)),
-      (A[0] = q),
-      (A[1] = Y),
-      (A[2] = z),
-      (A[3] = w),
-      (A[4] = H));
-  } else ((Y = A[1]), (z = A[2]), (w = A[3]), (H = A[4]));
+    J = Symbol.for("react.early_return_sentinel");
+    A: {
+      let X = K.filter(B4z);
+      if (X.length === 0) {
+        J = null;
+        break A;
+      }
+      let $ = b4z(X),
+        _ = n2($.map(u4z));
+      ((Y = S), (z = 1), (w = "column"), (H = _.map(x4z)));
+    }
+    ((A[0] = K), (A[1] = Y), (A[2] = z), (A[3] = w), (A[4] = H), (A[5] = J));
+  } else ((Y = A[1]), (z = A[2]), (w = A[3]), (H = A[4]), (J = A[5]));
+  if (J !== Symbol.for("react.early_return_sentinel")) return J;
   let J;
-  if (A[5] !== Y || A[6] !== z || A[7] !== w || A[8] !== H)
+  if (A[6] !== Y || A[7] !== z || A[8] !== w || A[9] !== H)
     ((J = _YA.createElement(Y, { marginTop: z, flexDirection: w }, H)),
-      (A[5] = Y),
       (A[6] = z),
       (A[7] = w),
       (A[8] = H),
-      (A[9] = J));
-  else J = A[9];
+      (A[9] = H),
+      (A[10] = O));
+  else O = A[10];
   return J;
 }

@@@ function '_r2' (was 'Ni2') — structural (52.7%)
--- pretty-v2.1.22.js:523170
+++ pretty-v2.1.23.js:524213
@@ -1,10 +1,10 @@
 function Ni2(A) {
   let { onDone: K } = A,
-    [q] = V6(),
-    { mainLoopModel: Y, mainLoopModelForSession: z } = q,
+    q = F1(Zr2),
+    Y = F1(Gr2),
     w = Y ?? Un().label,
     H = rqA(),
-    J = H !== void 0 && H !== "unset" ? ` (effort: ${H})` : "";
+    H = w !== void 0 ? ` (effort: ${w})` : "";
   if (z)
     K(`Current model: ${O1.bold(Dy(z))} (session override from plan mode)
 Base model: ${w}${J}`);

@@@ function 'Xs' (was 'D8') — structural (52.5%)
--- pretty-v2.1.22.js:193040
+++ pretty-v2.1.23.js:319423
@@ -1,4 +1,3 @@
 function D8() {
-  if (_2(process.env.CLAUDE_CODE_AGENT_SWARMS)) return !1;
-  return V4("tengu_brass_pebble", !1);
+  return G4("tengu_workout", !1) && !P1(process.env.CLAUDE_CODE_DISABLE_EFFORT);
 }

@@@ function 'fm' (was 'xw') — structural (52.4%)
--- pretty-v2.1.22.js:463951
+++ pretty-v2.1.23.js:528013
@@ -1,3 +1,3 @@
 function xw() {
-  (vy2(), $m(), UQA());
+  (rQ6(), mN1(), A0K(), vZ1());
 }

@@@ function 'B4z' (was 'Y$2') — structural (51.7%)
--- pretty-v2.1.22.js:390026
+++ pretty-v2.1.23.js:556459
@@ -1,3 +1,3 @@
 function Y$2(A) {
-  return A.status !== "pending" && A.status !== "completed";
+  return A.mode !== "task-notification";
 }

@@@ function 'Sx6' (was 'CwK') — structural (51.4%)
--- pretty-v2.1.22.js:453078
+++ pretty-v2.1.23.js:453471
@@ -1,19 +1,9 @@
-async function CwK(A, K, q) {
+async function Sx6(A, K, q, Y = !1) {
   if (!sb6()) return;
   o3A(q);
   let Y = Kk2().slice(0, 8),
     z = WwA(K.toolUseContext.abortController);
-  if (
-    (await Promise.race([
-      F04().then(() => !1),
-      new Promise((_) => {
-        if (z.signal.aborted) _(!0);
-        else z.signal.addEventListener("abort", () => _(!0), { once: !0 });
-      }),
-    ])) ||
-    z.signal.aborted
-  )
-    return;
+  if (w.signal.aborted) return;
   let H = Date.now(),
     J = { current: [] },
     O = { current: new Set() },
@@ -25,6 +15,7 @@
     h("[Speculation] Failed to create overlay directory");
     return;
   }
+  let _ = { current: K };
   (q((_) => ({
     ..._,
     speculation: {
@@ -36,6 +27,9 @@
       writtenPathsRef: O,
       boundary: null,
       suggestionLength: A.length,
+      toolUseCount: 0,
+      isPipelined: Y,
+      contextRef: _,
     },
   })),
     h(`[Speculation] Starting speculation ${Y}`));
@@ -45,7 +39,15 @@
       cacheSafeParams: k3A(K),
       canUseTool: async (Z, G) => {
         let W = ["Edit", "Write", "NotebookEdit"].includes(Z.name),
-          D = ["Read", "Glob", "Grep"].includes(Z.name);
+          j = [
+            "Read",
+            "Glob",
+            "Grep",
+            "ToolSearch",
+            "LSP",
+            "TaskGet",
+            "TaskList",
+          ].includes(Z.name);
         if (W) {
           let j = await K.toolUseContext.getAppState(),
             { mode: M, isBypassPermissionsModeAvailable: P } =
@@ -56,13 +58,15 @@
               M === "bypassPermissions" ||
               (M === "plan" && P)
             )
-          )
+          ) {
+            h(`[Speculation] Stopping at file edit: ${Z.name}`);
+            let C = "file_path" in W ? W.file_path : void 0;
             return (
-              h(`[Speculation] Stopping at file edit: ${Z.name}`),
               nb6(q, () => ({
                 boundary: {
                   type: "edit",
                   toolName: Z.name,
+                  filePath: C ?? "",
                   completedAt: Date.now(),
                 },
               })),
@@ -72,6 +76,7 @@
                 "speculation_edit_boundary",
               )
             );
+          }
         }
         if (W || D) {
           let j =
@@ -124,6 +129,15 @@
               }
             );
           }
+          if (j)
+            return {
+              behavior: "allow",
+              updatedInput: W,
+              decisionReason: {
+                type: "other",
+                reason: "speculation_read_default_cwd",
+              },
+            };
         }
         if (
           Z.name === "Bash" &&
@@ -144,9 +158,28 @@
               )
             );
         }
-        return Pf1(
-          `Tool ${Z.name} not allowed during speculation`,
-          "speculation_unknown_tool",
+        h(`[Speculation] Stopping at denied tool: ${Z.name}`);
+        let M = String(
+          ("url" in W && W.url) ||
+            ("file_path" in W && W.file_path) ||
+            ("path" in W && W.path) ||
+            ("command" in W && W.command) ||
+            "",
+        ).slice(0, 200);
+        return (
+          YPA(q, () => ({
+            boundary: {
+              type: "denied_tool",
+              toolName: Z.name,
+              detail: M,
+              completedAt: Date.now(),
+            },
+          })),
+          w.abort(),
+          df1(
+            `Tool ${Z.name} not allowed during speculation`,
+            "speculation_unknown_tool",
+          )
         );
       },
       querySource: "speculation",
@@ -156,6 +189,12 @@
       onMessage: (Z) => {
         if (Z.type === "assistant" || Z.type === "user") {
           if ((J.current.push(Z), J.current.length >= Jk2)) z.abort();
+          if (yx6(Z)) {
+            let W = Z.message.content.filter(
+              (D) => D.type === "tool_result" && !D.is_error,
+            ).length;
+            if (W > 0) YPA(q, (D) => ({ toolUseCount: D.toolUseCount + W }));
+          }
         }
       },
     });
@@ -167,7 +206,8 @@
         outputTokens: _.totalUsage.output_tokens,
       },
     })),
-      h(`[Speculation] Complete: ${ab6(J.current)} tools`));
+      h(`[Speculation] Complete: ${Rx6(J.current)} tools`),
+      PC2(_.current, A, J.current, q, w));
   } catch (_) {
     if ((z.abort(), _ instanceof Error && _.name === "AbortError")) {
       (hUA(X), ob6(q));
@@ -182,6 +222,7 @@
           200,
         ),
         error_phase: "start",
+        is_pipelined: Y,
       }),
       ob6(q));
   }

@@@ function 'HL' (was 'eI') — structural (51.2%)
--- pretty-v2.1.22.js:339150
+++ pretty-v2.1.23.js:339582
@@ -1,3 +1,4 @@
-function eI() {
-  return `a${nnY(3).toString("hex")}`;
+function HL(A) {
+  let K = OoY(3).toString("hex");
+  return A ? `a${A}-${K}` : `a${K}`;
 }

@@@ function 'Or2' (was 'Pi2') — structural (51.1%)
--- pretty-v2.1.22.js:523125
+++ pretty-v2.1.23.js:524168
@@ -1,5 +1,5 @@
 function Pi2({ args: A, onDone: K }) {
-  let [q, Y] = V6(),
+  let q = p4(),
     z = A === "default" ? null : A;
   return (
     Kh.useEffect(() => {

@@@ function 'lJK' (was 'tM') — structural (50.0%)
--- pretty-v2.1.22.js:324757
+++ pretty-v2.1.23.js:459700
@@ -1,4 +1,3 @@
 function tM() {
-  let [A] = V6();
-  return A.settings;
+  return ZPA.toolCallsBetweenUpdates;
 }

@@@ function 'aKK' (was 'F7K') — structural (50.0%)
--- pretty-v2.1.22.js:420434
+++ pretty-v2.1.23.js:420765
@@ -1,13 +1,4 @@
 async function F7K() {
-  async function A(Y) {
-    try {
-      return (
-        await t6.get(`${bj2}/${Y}`, { timeout: 5000, responseType: "text" })
-      ).data.trim();
-    } catch (z) {
-      return (h(`Failed to fetch ${Y} from GCS: ${z}`), null);
-    }
-  }
   let [K, q] = await Promise.all([A("latest"), A("stable")]);
   return { latest: K, stable: q };
 }

@@@ function 'WI7' (was 't6z') — structural (50.0%)
--- pretty-v2.1.22.js:558039
+++ pretty-v2.1.23.js:340810
@@ -1,3 +1,3 @@
 function t6z(A) {
-  return A + 1;
+  return;
 }

@@@ function 'Sqz' (was '$7z') — structural (49.5%)
--- pretty-v2.1.22.js:568138
+++ pretty-v2.1.23.js:569851
@@ -5,34 +5,30 @@
       "anthropic-version": J7z,
       "anthropic-beta": H7z,
     };
-  wAA(`Downloading file ${A} from ${Y}`);
-  for (let w = 1; w <= scA; w++) {
-    try {
-      let H = await t6.get(Y, {
-        headers: z,
-        responseType: "arraybuffer",
-        timeout: 60000,
-        validateStatus: (J) => J < 500,
-      });
-      if (H.status === 200)
-        return (
-          wAA(`Downloaded file ${A} (${H.data.length} bytes)`),
-          Buffer.from(H.data)
-        );
-      if (H.status === 404) throw Error(`File not found: ${A}`);
-      if (H.status === 401)
-        throw Error("Authentication failed: invalid or missing API key");
-      if (H.status === 403) throw Error(`Access denied to file: ${A}`);
-      wAA(`Download attempt ${w}/${scA} failed: ${H.status}`);
-    } catch (H) {
-      if (!t6.isAxiosError(H)) throw H;
-      wAA(`Network error on attempt ${w}/${scA}: ${H.message}`);
-    }
-    if (w < scA) {
-      let H = X7z * Math.pow(2, w - 1);
-      (wAA(`Retrying in ${H}ms...`),
-        await new Promise((J) => setTimeout(J, H)));
-    }
-  }
-  throw Error(`Failed to download file ${A} after ${scA} attempts`);
+  return (
+    xYA(`Downloading file ${A} from ${Y}`),
+    Iqz(`Download file ${A}`, async () => {
+      try {
+        let w = await A8.get(Y, {
+          headers: z,
+          responseType: "arraybuffer",
+          timeout: 60000,
+          validateStatus: (H) => H < 500,
+        });
+        if (w.status === 200)
+          return (
+            xYA(`Downloaded file ${A} (${w.data.length} bytes)`),
+            { done: !0, value: Buffer.from(w.data) }
+          );
+        if (w.status === 404) throw Error(`File not found: ${A}`);
+        if (w.status === 401)
+          throw Error("Authentication failed: invalid or missing API key");
+        if (w.status === 403) throw Error(`Access denied to file: ${A}`);
+        return { done: !1, error: `status ${w.status}` };
+      } catch (w) {
+        if (!A8.isAxiosError(w)) throw w;
+        return { done: !1, error: w.message };
+      }
+    })
+  );
 }

@@@ function 'IK6' (was 'AK6') — structural (49.0%)
--- pretty-v2.1.22.js:176510
+++ pretty-v2.1.23.js:176573
@@ -3,20 +3,8 @@
     z = K.width,
     w = A.height,
     H = K.height,
-    J = A.chars,
-    O = K.chars,
-    X = A.charStrings,
-    $ = K.charStrings,
-    _ = A.styleIds,
-    Z = K.styleIds,
-    G = A.widths,
-    W = K.widths,
-    D = A.hyperlinkIds,
-    j = K.hyperlinkIds,
-    M = A.hyperlinks,
-    P = K.hyperlinks,
-    V = A.emptyStyleId,
-    N = K.emptyStyleId,
+    J = A.cells,
+    O = K.cells,
     T;
   if (Y === 0 && w === 0) T = { x: 0, y: 0, width: z, height: H };
   else if (K.damage) {
@@ -31,42 +19,46 @@
     S = Math.min(T.x + T.width, R),
     B = { char: " ", styleId: 0, width: 0, hyperlink: void 0 },
     x = { char: " ", styleId: 0, width: 0, hyperlink: void 0 },
-    F = T.y * Y + T.x,
-    Q = T.y * z + T.x;
+    j = X.x,
+    M = Y << 1,
+    P = z << 1,
+    f = (X.y * Y + j) << 1,
+    N = (X.y * z + j) << 1;
   for (let u = T.y; u < b; u++) {
     let d = u < w,
       o = u < H,
-      l = d ? Math.min(S, Y) : T.x,
-      e = o ? Math.min(S, z) : T.x,
+      x = C ? Math.min(Z, Y) : j,
+      y = R ? Math.min(Z, z) : j,
       wA = Math.min(l, e),
       HA = F,
       OA = Q;
-    for (let WA = T.x; WA < wA; WA++, HA++, OA++) {
-      let a = X[J[HA]],
-        _A = $[O[OA]],
-        jA = M[D[HA]],
-        PA = P[j[OA]],
-        SA = _[HA],
-        mA = Z[OA];
+    for (let Q = j; Q < B; Q++) {
+      if (J[b] === O[F] && J[b + 1] === O[F + 1]) {
+        ((b += 2), (F += 2));
+        continue;
+      }
       if (
-        a === _A &&
-        (SA === fQ ? V : SA) === (mA === fQ ? N : mA) &&
-        G[HA] === W[OA] &&
-        jA === PA
+        (k51(A, b >>> 1, W),
+        k51(K, F >>> 1, D),
+        (b += 2),
+        (F += 2),
+        q(Q, T, W, D))
       )
-        continue;
-      if ((J51(A, HA, B), J51(K, OA, x), q(WA, u, B, x))) return !0;
+        return !0;
     }
     if (l > wA) {
-      HA = F + (wA - T.x);
-      for (let WA = wA; WA < l; WA++, HA++)
-        if ((J51(A, HA, B), q(WA, u, B, void 0))) return !0;
+      b = f + ((B - j) << 1);
+      for (let Q = B; Q < x; Q++)
+        if ((k51(A, b >>> 1, W), (b += 2), q(Q, T, W, void 0))) return !0;
     }
     if (e > wA) {
-      OA = Q + (wA - T.x);
-      for (let WA = wA; WA < e; WA++, OA++) {
-        if (Z[OA] === fQ) continue;
-        if ((J51(K, OA, x), q(WA, u, void 0, x))) return !0;
+      F = N + ((B - j) << 1);
+      for (let Q = B; Q < y; Q++) {
+        if (O[F] === 0 && O[F + 1] === 0) {
+          F += 2;
+          continue;
+        }
+        if ((k51(K, F >>> 1, D), (F += 2), q(Q, T, void 0, D))) return !0;
       }
     }
     ((F += Y), (Q += z));

@@@ function 'BL2' (was 'yC2') — structural (49.0%)
--- pretty-v2.1.22.js:458176
+++ pretty-v2.1.23.js:458664
@@ -1,4 +1,6 @@
-async function yC2() {
+async function BL2(A) {
+  if ((await A.getAppState()).toolPermissionContext.mode === "coordinator")
+    return [];
   h("LSP Diagnostics: getLSPDiagnosticAttachments called");
   try {
     let A = wT7();

@@@ function 'I51' (was 'X51') — structural (47.8%)
--- pretty-v2.1.22.js:176390
+++ pretty-v2.1.23.js:176479
@@ -1,31 +1,24 @@
 function X51(A, K, q, Y) {
   if (K < 0 || q < 0 || K >= A.width || q >= A.height) return;
-  let z = q * A.width + K,
-    w = A.widths[z];
+  let z = (q * A.width + K) << 1,
+    w = A.cells,
+    H = w[z + 1] & j4A;
   if (w === 1 && Y.width !== 1) {
     if (K + 1 < A.width) {
-      let O = z + 1;
-      if (A.widths[O] === 2)
-        ((A.chars[O] = wr),
-          (A.styleIds[O] = A.emptyStyleId),
-          (A.widths[O] = 0),
-          (A.hyperlinkIds[O] = 0));
+      let X = z + 2;
+      if ((w[X + 1] & j4A) === 2)
+        ((w[X] = kK6), (w[X + 1] = vXA(A.emptyStyleId, 0, 0)));
     }
   }
   if (w === 2 && Y.width !== 2) {
     if (K > 0) {
-      let J = z - 1;
-      if (A.widths[J] === 1)
-        ((A.chars[J] = wr),
-          (A.styleIds[J] = A.emptyStyleId),
-          (A.widths[J] = 0),
-          (A.hyperlinkIds[J] = 0));
+      let O = z - 2;
+      if ((w[O + 1] & j4A) === 1)
+        ((w[O] = kK6), (w[O + 1] = vXA(A.emptyStyleId, 0, 0)));
     }
   }
-  ((A.chars[z] = QO4(A, Y.char)),
-    (A.styleIds[z] = Y.styleId),
-    (A.widths[z] = Y.width),
-    (A.hyperlinkIds[z] = mO4(A, Y.hyperlink)));
+  ((w[z] = Mt3(A, Y.char)),
+    (w[z + 1] = vXA(Y.styleId, Dt3(A, Y.hyperlink), Y.width)));
   let H = A.damage;
   if (H) {
     let J = H.x + H.width,
@@ -38,11 +31,8 @@
   if (Y.width === 1) {
     let J = K + 1;
     if (J < A.width) {
-      let O = q * A.width + J;
-      ((A.chars[O] = O51),
-        (A.styleIds[O] = A.emptyStyleId),
-        (A.widths[O] = 2),
-        (A.hyperlinkIds[O] = 0));
+      let X = z + 2;
+      ((w[X] = I04), (w[X + 1] = vXA(A.emptyStyleId, 0, 2)));
       let X = A.damage;
       if (X && J >= X.x + X.width) X.width = J - X.x + 1;
     }

@@@ function 'vhK' (was 'fSK') — structural (45.6%)
--- pretty-v2.1.22.js:560249
+++ pretty-v2.1.23.js:561861
@@ -1,12 +1,12 @@
 function fSK({ isLoading: A, focusedInputDialog: K, onSubmitMessage: q }) {
   let Y = q,
-    [z, w] = V6(),
     H = Cx(),
+    w = p4(),
+    H = F1((G) => G.inbox.messages.length),
+    J = Bx(),
     J = fc.useRef(A),
-    O = fc.useRef(z);
-  O.current = z;
-  let X = fc.useCallback(() => {
-      let G = O.current,
+    X = _AA.useCallback(() => {
+      let G = z.getState(),
         W = Nk1(G);
       if (!W) return;
       let D = M3A(W, G.teamContext?.teamName);
@@ -371,12 +371,11 @@
           (h("[InboxPoller] Submission rejected, queuing for later delivery"),
             B());
       } else (h("[InboxPoller] Session busy, queuing for later delivery"), B());
-    }, [A, K, Y, w, H]),
-    $ = z.inbox.messages.length;
+    }, [A, K, Y, w, J, z]);
   fc.useEffect(() => {
     let G = J.current;
     if (((J.current = A), A || K)) return;
-    let W = O.current;
+    let Z = z.getState();
     if (!Nk1(W)) return;
     let j = W.inbox.messages.filter((E) => E.status === "pending"),
       M = W.inbox.messages.filter((E) => E.status === "processed");
@@ -410,12 +409,12 @@
         inbox: { messages: R.inbox.messages.filter((b) => !E.has(b.id)) },
       }));
     } else h("[InboxPoller] Submission rejected, keeping messages queued");
-  }, [A, K, Y, w, $]);
-  let _ = !!Nk1(z);
+  }, [A, K, Y, w, H, z]);
+  let $ = !!sk1(z.getState());
   JY(X, _ ? D8z : null);
   let Z = fc.useRef(!1);
   fc.useEffect(() => {
     if (Z.current) return;
-    if (Nk1(O.current)) ((Z.current = !0), X());
-  }, [X]);
+    if (sk1(z.getState())) ((_.current = !0), X());
+  }, [X, z]);
 }

@@@ variable 'aZ1' (was 'Z_') — structural (44.3%)
--- pretty-v2.1.22.js:449364
+++ pretty-v2.1.23.js:339682
@@ -5,41 +5,7 @@
   O5A();
   kv();
   $5A();
-  cQA();
-  iQA();
-  hMA();
-  Kb6();
-  zb6();
-  Hb6();
-  r0A();
-  DUA();
-  aYK();
-  WMA();
-  rV1();
-  L2K();
-  _$1();
-  Z$1();
-  f_6();
-  Gb6();
-  Q2K();
-  a2K();
-  wzK();
-  WzK();
-  EzK();
-  PC();
-  TJ();
-  ga();
-  B2();
-  l6();
-  y9();
-  dO();
-  b6A();
-  lE();
-  WV();
-  Uo();
-  kM6();
-  UzK = ["default"];
-  ((Yf1 = new Set([FWA, nZ.name, sV1, G5, gJ, pV1, ...(mzK ? [mzK] : [])])),
+  ((MDA = new Set([YDA, Yf, lZ1, Nq, bJ, JgA])),
     (NE2 = new Set([...Yf1])),
     (TE2 = new Set([
       rq,
@@ -59,5 +25,6 @@
       ...[],
       VUA,
     ])),
-    (pzK = new Set([oFA, VUA, io, Af1, Kf1, pU, G5])));
+    (rZ1 = new Set([OgA, XgA, Aa, iZ1, nZ1, tU, Nq])),
+    (oZ1 = new Set([Nq, JgA])));
 });

@@@ variable 'hXA' (was 's_A') — structural (42.8%)
--- pretty-v2.1.22.js:256760
+++ pretty-v2.1.23.js:179106
@@ -49,11 +49,11 @@
   );
   s5(
     "PRERELEASEIDENTIFIER",
-    `(?:${S7[h7.NUMERICIDENTIFIER]}|${S7[h7.NONNUMERICIDENTIFIER]})`,
+    `(?:${k7[C7.NONNUMERICIDENTIFIER]}|${k7[C7.NUMERICIDENTIFIER]})`,
   );
   s5(
     "PRERELEASEIDENTIFIERLOOSE",
-    `(?:${S7[h7.NUMERICIDENTIFIERLOOSE]}|${S7[h7.NONNUMERICIDENTIFIER]})`,
+    `(?:${k7[C7.NONNUMERICIDENTIFIER]}|${k7[C7.NUMERICIDENTIFIERLOOSE]})`,
   );
   s5(
     "PRERELEASE",

@@@ function 'I3A' (was 'f3A') — structural (42.7%)
--- pretty-v2.1.22.js:409332
+++ pretty-v2.1.23.js:409616
@@ -1,5 +1,5 @@
 function f3A(A) {
-  let K = s(38),
+  let K = s(33),
     {
       addMargin: q,
       param: Y,
@@ -16,39 +16,26 @@
         (K[1] = H),
         (K[2] = $));
     else $ = K[2];
-    return $;
-  }
-  let J;
-  if (K[3] !== Y.text) ((J = n7(Y.text, jl)), (K[3] = Y.text), (K[4] = J));
-  else J = K[4];
-  let O = J;
-  if (O) {
-    let $;
-    if (K[5] !== q || K[6] !== O)
-      (($ = Iz.createElement(u8K, { addMargin: q, time: O })),
-        (K[5] = q),
-        (K[6] = O),
-        (K[7] = $));
-    else $ = K[7];
     return $;
   }
+  if (i7(Y.text, El)) return null;
   if (Y.text.startsWith("<bash-stdout") || Y.text.startsWith("<bash-stderr")) {
     let $;
-    if (K[8] !== Y.text || K[9] !== z)
+    if (K[3] !== Y.text || K[4] !== z)
       (($ = Iz.createElement(G8K, { content: Y.text, verbose: z })),
-        (K[8] = Y.text),
-        (K[9] = z),
-        (K[10] = $));
-    else $ = K[10];
+        (K[3] = Y.text),
+        (K[4] = z),
+        (K[5] = O));
+    else O = K[5];
     return $;
   }
   if (Y.text.startsWith("<background-task-output>")) {
     let $;
-    if (K[11] !== Y.text)
+    if (K[6] !== Y.text)
       (($ = Iz.createElement(P8K, { content: Y.text })),
-        (K[11] = Y.text),
-        (K[12] = $));
-    else $ = K[12];
+        (K[6] = Y.text),
+        (K[7] = O));
+    else O = K[7];
     return $;
   }
   if (
@@ -56,92 +43,92 @@
     Y.text.startsWith("<local-command-stderr")
   ) {
     let $;
-    if (K[13] !== Y.text)
+    if (K[8] !== Y.text)
       (($ = Iz.createElement(j8K, { content: Y.text })),
-        (K[13] = Y.text),
-        (K[14] = $));
-    else $ = K[14];
+        (K[8] = Y.text),
+        (K[9] = O));
+    else O = K[9];
     return $;
   }
   if (Y.text === Lt || Y.text === Rf) {
     let $;
-    if (K[15] === Symbol.for("react.memo_cache_sentinel"))
+    if (K[10] === Symbol.for("react.memo_cache_sentinel"))
       (($ = Iz.createElement(E6, { height: 1 }, Iz.createElement(vu, null))),
-        (K[15] = $));
-    else $ = K[15];
+        (K[10] = O));
+    else O = K[10];
     return $;
   }
   if (Y.text.includes("<bash-input>")) {
     let $;
-    if (K[16] !== q || K[17] !== Y)
+    if (K[11] !== q || K[12] !== Y)
       (($ = Iz.createElement(CM1, { addMargin: q, param: Y })),
-        (K[16] = q),
-        (K[17] = Y),
-        (K[18] = $));
-    else $ = K[18];
+        (K[11] = q),
+        (K[12] = Y),
+        (K[13] = O));
+    else O = K[13];
     return $;
   }
   if (Y.text.includes("<background-task-input>")) {
     let $;
-    if (K[19] !== q || K[20] !== Y)
+    if (K[14] !== q || K[15] !== Y)
       (($ = Iz.createElement(D3A, { addMargin: q, param: Y })),
-        (K[19] = q),
-        (K[20] = Y),
-        (K[21] = $));
-    else $ = K[21];
+        (K[14] = q),
+        (K[15] = Y),
+        (K[16] = O));
+    else O = K[16];
     return $;
   }
   if (Y.text.includes(`<${nW}>`)) {
     let $;
-    if (K[22] !== q || K[23] !== Y)
+    if (K[17] !== q || K[18] !== Y)
       (($ = Iz.createElement(e6K, { addMargin: q, param: Y })),
-        (K[22] = q),
-        (K[23] = Y),
-        (K[24] = $));
-    else $ = K[24];
+        (K[17] = q),
+        (K[18] = Y),
+        (K[19] = O));
+    else O = K[19];
     return $;
   }
   if (Y.text.includes("<user-memory-input>")) {
     let $;
-    if (K[25] !== q || K[26] !== Y.text)
+    if (K[20] !== q || K[21] !== Y.text)
       (($ = Iz.createElement($8K, { addMargin: q, text: Y.text })),
-        (K[25] = q),
-        (K[26] = Y.text),
-        (K[27] = $));
-    else $ = K[27];
+        (K[20] = q),
+        (K[21] = Y.text),
+        (K[22] = O));
+    else O = K[22];
     return $;
   }
   if (D8() && Y.text.includes(`<${I0}`)) {
     let $;
-    if (K[28] !== q || K[29] !== Y)
+    if (K[23] !== q || K[24] !== Y)
       (($ = Iz.createElement(S8K, { addMargin: q, param: Y })),
-        (K[28] = q),
-        (K[29] = Y),
-        (K[30] = $));
-    else $ = K[30];
+        (K[23] = q),
+        (K[24] = Y),
+        (K[25] = O));
+    else O = K[25];
     return $;
   }
   if (Y.text.includes(`<${y0}`)) {
     let $;
-    if (K[31] !== q || K[32] !== Y)
+    if (K[26] !== q || K[27] !== Y)
       (($ = Iz.createElement(b8K, { addMargin: q, param: Y })),
-        (K[31] = q),
-        (K[32] = Y),
-        (K[33] = $));
-    else $ = K[33];
+        (K[26] = q),
+        (K[27] = Y),
+        (K[28] = O));
+    else O = K[28];
     return $;
   }
   let X;
-  if (K[34] !== q || K[35] !== Y || K[36] !== w)
+  if (K[29] !== q || K[30] !== Y || K[31] !== w)
     ((X = Iz.createElement(H8K, {
       addMargin: q,
       param: Y,
       thinkingMetadata: w,
     })),
-      (K[34] = q),
-      (K[35] = Y),
-      (K[36] = w),
-      (K[37] = X));
-  else X = K[37];
+      (K[29] = q),
+      (K[30] = Y),
+      (K[31] = w),
+      (K[32] = J));
+  else J = K[32];
   return X;
 }

@@@ function 'MhK' (was 'WSK') — structural (41.4%)
--- pretty-v2.1.22.js:560083
+++ pretty-v2.1.23.js:561702
@@ -1,69 +1,59 @@
 function WSK() {
-  let A = s(16),
-    [K] = V6(),
-    q,
-    Y,
-    z;
-  if (A[0] !== K) {
-    Y = Symbol.for("react.early_return_sentinel");
-    A: {
-      if (((z = cM(K)), !z)) {
-        Y = null;
-        break A;
-      }
-      q = Pv(z.identity.color);
-    }
-    ((A[0] = K), (A[1] = q), (A[2] = Y), (A[3] = z));
-  } else ((q = A[1]), (Y = A[2]), (z = A[3]));
-  if (Y !== Symbol.for("react.early_return_sentinel")) return Y;
+  let A = s(14),
+    K = F1(R7z);
+  if (!K) return null;
+  let q;
+  if (A[0] !== K.identity.color)
+    ((q = Pv(K.identity.color)), (A[0] = K.identity.color), (A[1] = q));
+  else q = A[1];
   let w = q,
     H;
-  if (A[4] === Symbol.for("react.memo_cache_sentinel"))
-    ((H = CP.createElement(f, null, "Viewing ")), (A[4] = H));
-  else H = A[4];
+  if (A[2] === Symbol.for("react.memo_cache_sentinel"))
+    ((z = IP.createElement(V, null, "Viewing ")), (A[2] = z));
+  else z = A[2];
   let J;
-  if (A[5] !== w || A[6] !== z.identity.agentName)
+  if (A[3] !== Y || A[4] !== K.identity.agentName)
     ((J = CP.createElement(
       f,
       { color: w, bold: !0 },
       "@",
       z.identity.agentName,
     )),
-      (A[5] = w),
-      (A[6] = z.identity.agentName),
-      (A[7] = J));
-  else J = A[7];
+      (A[3] = Y),
+      (A[4] = K.identity.agentName),
+      (A[5] = w));
+  else w = A[5];
   let O;
-  if (A[8] === Symbol.for("react.memo_cache_sentinel"))
+  if (A[6] === Symbol.for("react.memo_cache_sentinel"))
     ((O = CP.createElement(
       f,
       { dimColor: !0 },
       " · ",
       CP.createElement(G6, { shortcut: "shift+up", action: "return" }),
     )),
-      (A[8] = O));
-  else O = A[8];
+      (A[6] = H));
+  else H = A[6];
   let X;
-  if (A[9] !== J)
-    ((X = CP.createElement(I, null, H, J, O)), (A[9] = J), (A[10] = X));
-  else X = A[10];
+  if (A[7] !== w)
+    ((J = IP.createElement(S, null, z, w, H)), (A[7] = w), (A[8] = J));
+  else J = A[8];
   let $;
-  if (A[11] !== z.prompt)
+  if (A[9] !== K.prompt)
     (($ = CP.createElement(f, { dimColor: !0 }, z.prompt)),
-      (A[11] = z.prompt),
-      (A[12] = $));
-  else $ = A[12];
+      (A[9] = K.prompt),
+      (A[10] = O));
+  else O = A[10];
   let _;
-  if (A[13] !== X || A[14] !== $)
+  if (A[11] !== J || A[12] !== O)
     ((_ = CP.createElement(
       I,
       { flexDirection: "column", marginBottom: 1 },
       X,
       $,
     )),
-      (A[13] = X),
-      (A[14] = $),
-      (A[15] = _));
-  else _ = A[15];
+      (A[11] = J),
+      (A[12] = O),
+      (A[13] = X));
+  else X = A[13];
   return _;
 }

=== String Changes ===

@@@ variable 'R4A' (was 'M4A') — string-only
--- pretty-v2.1.22.js:185529
+++ pretty-v2.1.23.js:185628
@@ -52,7 +52,7 @@
         let H = `Terminal setup cannot be run from ${Y}.
 
 This command configures a convenient Shift+Enter shortcut for multi-line prompts.
-${O1.dim("Note: You can already use backslash (\\) + return to add newlines.")}
+${O1.dim("Note: You can already use backslash (\\\\) + return to add newlines.")}
 
 To set up the shortcut (optional):
 1. Exit tmux/screen temporarily
