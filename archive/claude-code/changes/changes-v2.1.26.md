--- archive/claude-code/pretty/pretty-v2.1.25.js
+++ archive/claude-code/pretty/pretty-v2.1.26.js
Structural similarity: 99.2%
Matched: 14327/14445 vs 14417
Changes: 90 added, 118 removed, 575 structural, 35 string-only (13717 unchanged)

Filtered: 51 version bumps, 422 reformatting-only changes

=== Import Style Changes ===

"child_process":
  - import I2Y from "child_process";
  - import S2Y from "child_process";
  + import { execFile as w_5, spawn as H_5, spawnSync as J_5 } from "child_process";
  + import { spawn as T9q, spawnSync as v9q } from "child_process";

"crypto":
  - import f7Y from "crypto";
  - import N7Y from "crypto";
  + import { randomBytes as q6z, timingSafeEqual as Y6z } from "crypto";

"https":
  - import J67 from "https";
  + import { Agent as hc3 } from "https";

"node:child_process":
  - import My1 from "node:child_process";
  - import bq7 from "node:child_process";
  + import { execFile as t5Y, execFileSync as gxw } from "node:child_process";
  + import { execFileSync as iN2, spawn as nN2 } from "node:child_process";

"node:fs":
  - import nYY from "node:fs";
  - import aYY from "node:fs";
  + import {
  +   existsSync as hUA,
  +   statSync as bN2,
  +   mkdirSync as xN2,
  +   realpathSync as uN2,
  + } from "node:fs";
  + import {
  +   constants as pN2,
  +   readFileSync as dN2,
  +   existsSync as cN2,
  +   unlinkSync as lN2,
  + } from "node:fs";

"node:os":
  - import oYY from "node:os";
  + import { homedir as U1z } from "node:os";

"node:path":
  - import hq7 from "node:path";
  + import {
  +   join as PX,
  +   dirname as cd,
  +   resolve as Pm,
  +   delimiter as FC2,
  +   basename as QC2,
  + } from "node:path";

"node:process":
  - import nEK from "node:process";
  + import { cwd as WO4 } from "node:process";

"node:util":
  - import eAY from "node:util";
  + import { isDeepStrictEqual as OuK } from "node:util";

"path":
  - import EYY from "path";
  + import { posix as qBK, win32 as YBK } from "path";
  + import { dirname as Y1z, join as yBK } from "path";

"stream":
  - import izA from "stream";
  + import { PassThrough as I1z } from "stream";

=== Removed ===

--- Removed CnA (pretty-v2.1.25.js:1847-1850)
- function CnA(A) {
-   let K = A.toLowerCase();
-   return BrK;
- }

--- Removed TW8 (pretty-v2.1.25.js:61991-61991)
-   TW8 = "client-RRNS7R65EAtReO5XA4xDC3eU6ZdJQi6lLEP6b5j32Me",

--- Removed XO5 (pretty-v2.1.25.js:102557-102570)
- function XO5() {
-   let A = BA();
-   return XV.map((K) => {
-     if (K === "flagSettings") return;
-     let q = pO(K);
-     if (!q) return;
-     try {
-       if (!A.statSync(q).isFile()) return;
-     } catch {
-       return;
-     }
-     return r11.dirname(q);
-   }).filter((K) => K !== void 0);
- }

--- Removed qJ4 (pretty-v2.1.25.js:160568-160752)
- var qJ4 = k(() => {
-   AJ4 = `Use this tool to create and manage a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user.
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
- * Uses the ${m5} tool to add a comment to the calculateTotal function *
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

--- Removed EXA (pretty-v2.1.25.js:176648-176654)
- var EXA = k(() => {
-   AK6();
-   EK6();
-   O4A();
-   ((g04 = new RegExp(`^${wr}\\]8${Jr}${Jr}([^${Hr}]*)${Hr}$`)),
-     (F04 = `${wr}]8${Jr}`));
- });

--- Removed cK (pretty-v2.1.25.js:181917-181931)
- function cK(A, K, q) {
-   let Y = mk(),
-     z = Y?.getDisplayText(A, K);
-   if (z === void 0)
-     return (
-       n("tengu_keybinding_fallback_used", {
-         action: A,
-         context: K,
-         fallback: q,
-         reason: Y ? "action_not_found" : "no_context",
-       }),
-       q
-     );
-   return z;
- }

--- Removed t69 (pretty-v2.1.25.js:183729-183741)
- function t69(A, K) {
-   let { hyperlink: q, ...Y } = A.props,
-     z = Object.keys(Y).length > 0;
-   if (q)
-     return z
-       ? Qk.default.createElement(
-           X7,
-           { key: K, url: q },
-           Qk.default.createElement(NG4, { ...Y }, A.text),
-         )
-       : Qk.default.createElement(X7, { key: K, url: q }, A.text);
-   return z ? Qk.default.createElement(NG4, { key: K, ...Y }, A.text) : A.text;
- }

--- Removed Cy4 (pretty-v2.1.25.js:193342-193352)
- function Cy4(A, K = {}) {
-   let q = {};
-   for (let [Y, z] of Object.entries(K)) if (z !== void 0) q[Y] = String(z);
-   for (let [Y, z] of Object.entries(A)) {
-     if (z === void 0) continue;
-     if (Y === "envContext") q.env = UA(z);
-     else if (Y === "processMetrics") q.process = UA(z);
-     else q[Y] = String(z);
-   }
-   return q;
- }

--- Removed aD7 (pretty-v2.1.25.js:309768-309793)
- function aD7(A, K, q, Y, z) {
-   var w = [],
-     H;
-   while (K)
-     (w.push(K), (H = K.previousComponent), delete K.previousComponent, (K = H));
-   w.reverse();
-   var J = 0,
-     O = w.length,
-     X = 0,
-     $ = 0;
-   for (; J < O; J++) {
-     var _ = w[J];
-     if (!_.removed) {
-       if (!_.added && z) {
-         var G = q.slice(X, X + _.count);
-         ((G = G.map(function (Z, W) {
-           var D = Y[$ + W];
-           return D.length > Z.length ? D : Z;
-         })),
-           (_.value = A.join(G)));
-       } else _.value = A.join(q.slice(X, X + _.count));
-       if (((X += _.count), !_.added)) $ += _.count;
-     } else ((_.value = A.join(Y.slice($, $ + _.count))), ($ += _.count));
-   }
-   return w;
- }

--- Removed Aj7 (pretty-v2.1.25.js:309856-309898)
- function Aj7(A, K, q, Y) {
-   if (K && q) {
-     var z = K.value.match(/^\s*/)[0],
-       w = K.value.match(/\s*$/)[0],
-       H = q.value.match(/^\s*/)[0],
-       J = q.value.match(/\s*$/)[0];
-     if (A) {
-       var O = sD7(z, H);
-       ((A.value = pM6(A.value, H, O)),
-         (K.value = sBA(K.value, O)),
-         (q.value = sBA(q.value, O)));
-     }
-     if (Y) {
-       var X = tD7(w, J);
-       ((Y.value = UM6(Y.value, J, X)),
-         (K.value = J_1(K.value, X)),
-         (q.value = J_1(q.value, X)));
-     }
-   } else if (q) {
-     if (A) q.value = q.value.replace(/^\s*/, "");
-     if (Y) Y.value = Y.value.replace(/^\s*/, "");
-   } else if (A && Y) {
-     var $ = Y.value.match(/^\s*/)[0],
-       _ = K.value.match(/^\s*/)[0],
-       G = K.value.match(/\s*$/)[0],
-       Z = sD7($, _);
-     K.value = sBA(K.value, Z);
-     var W = tD7(sBA($, Z), G);
-     ((K.value = J_1(K.value, W)),
-       (Y.value = UM6(Y.value, $, W)),
-       (A.value = pM6(A.value, $, $.slice(0, $.length - W.length))));
-   } else if (Y) {
-     var D = Y.value.match(/^\s*/)[0],
-       j = K.value.match(/\s*$/)[0],
-       M = eD7(j, D);
-     K.value = J_1(K.value, M);
-   } else if (A) {
-     var P = A.value.match(/\s*$/)[0],
-       f = K.value.match(/^\s*/)[0],
-       N = eD7(P, f);
-     K.value = sBA(K.value, N);
-   }
- }

--- Removed Kj7 (pretty-v2.1.25.js:309905-309916)
- function Kj7(A, K) {
-   var q = Object.keys(A);
-   if (Object.getOwnPropertySymbols) {
-     var Y = Object.getOwnPropertySymbols(A);
-     (K &&
-       (Y = Y.filter(function (z) {
-         return Object.getOwnPropertyDescriptor(A, z).enumerable;
-       })),
-       q.push.apply(q, Y));
-   }
-   return q;
- }

--- Removed qj7 (pretty-v2.1.25.js:309917-309931)
- function qj7(A) {
-   for (var K = 1; K < arguments.length; K++) {
-     var q = arguments[K] != null ? arguments[K] : {};
-     K % 2
-       ? Kj7(Object(q), !0).forEach(function (Y) {
-           DRY(A, Y, q[Y]);
-         })
-       : Object.getOwnPropertyDescriptors
-         ? Object.defineProperties(A, Object.getOwnPropertyDescriptors(q))
-         : Kj7(Object(q)).forEach(function (Y) {
-             Object.defineProperty(A, Y, Object.getOwnPropertyDescriptor(q, Y));
-           });
-   }
-   return A;
- }

--- Removed ZRY (pretty-v2.1.25.js:309932-309941)
- function ZRY(A, K) {
-   if (typeof A != "object" || !A) return A;
-   var q = A[Symbol.toPrimitive];
-   if (q !== void 0) {
-     var Y = q.call(A, K || "default");
-     if (typeof Y != "object") return Y;
-     throw TypeError("@@toPrimitive must return a primitive value.");
-   }
-   return (K === "string" ? String : Number)(A);
- }

--- Removed WRY (pretty-v2.1.25.js:309942-309945)
- function WRY(A) {
-   var K = ZRY(A, "string");
-   return typeof K == "symbol" ? K : K + "";
- }

--- Removed dM6 (pretty-v2.1.25.js:309946-309963)
- function dM6(A) {
-   return (
-     (dM6 =
-       typeof Symbol == "function" && typeof Symbol.iterator == "symbol"
-         ? function (K) {
-             return typeof K;
-           }
-         : function (K) {
-             return K &&
-               typeof Symbol == "function" &&
-               K.constructor === Symbol &&
-               K !== Symbol.prototype
-               ? "symbol"
-               : typeof K;
-           }),
-     dM6(A)
-   );
- }

--- Removed DRY (pretty-v2.1.25.js:309964-309974)
- function DRY(A, K, q) {
-   if (((K = WRY(K)), K in A))
-     Object.defineProperty(A, K, {
-       value: q,
-       enumerable: !0,
-       configurable: !0,
-       writable: !0,
-     });
-   else A[K] = q;
-   return A;
- }

--- Removed QM6 (pretty-v2.1.25.js:309975-309977)
- function QM6(A) {
-   return jRY(A) || MRY(A) || PRY(A) || VRY();
- }

--- Removed MRY (pretty-v2.1.25.js:309981-309987)
- function MRY(A) {
-   if (
-     (typeof Symbol < "u" && A[Symbol.iterator] != null) ||
-     A["@@iterator"] != null
-   )
-     return Array.from(A);
- }

--- Removed PRY (pretty-v2.1.25.js:309988-309996)
- function PRY(A, K) {
-   if (!A) return;
-   if (typeof A === "string") return cM6(A, K);
-   var q = Object.prototype.toString.call(A).slice(8, -1);
-   if (q === "Object" && A.constructor) q = A.constructor.name;
-   if (q === "Map" || q === "Set") return Array.from(A);
-   if (q === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(q))
-     return cM6(A, K);
- }

--- Removed cM6 (pretty-v2.1.25.js:309997-310001)
- function cM6(A, K) {
-   if (K == null || K > A.length) K = A.length;
-   for (var q = 0, Y = Array(K); q < K; q++) Y[q] = A[q];
-   return Y;
- }

--- Removed VRY (pretty-v2.1.25.js:310002-310005)
- function VRY() {
-   throw TypeError(`Invalid attempt to spread non-iterable instance.
- In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`);
- }

--- Removed O_1 (pretty-v2.1.25.js:310154-310155)
-   O_1 =
-     "a-zA-Z0-9_\\u{C0}-\\u{FF}\\u{D8}-\\u{F6}\\u{F8}-\\u{2C6}\\u{2C8}-\\u{2D7}\\u{2DE}-\\u{2FF}\\u{1E00}-\\u{1EFF}",

--- Removed AmA (pretty-v2.1.25.js:310164-310462)
- var AmA = k(() => {
-   dI.prototype = {
-     diff: function (K, q) {
-       var Y,
-         z = arguments.length > 2 && arguments[2] !== void 0 ? arguments[2] : {},
-         w = z.callback;
-       if (typeof z === "function") ((w = z), (z = {}));
-       var H = this;
-       function J(N) {
-         if (((N = H.postProcess(N, z)), w))
-           return (
-             setTimeout(function () {
-               w(N);
-             }, 0),
-             !0
-           );
-         else return N;
-       }
-       ((K = this.castInput(K, z)),
-         (q = this.castInput(q, z)),
-         (K = this.removeEmpty(this.tokenize(K, z))),
-         (q = this.removeEmpty(this.tokenize(q, z))));
-       var O = q.length,
-         X = K.length,
-         $ = 1,
-         _ = O + X;
-       if (z.maxEditLength != null) _ = Math.min(_, z.maxEditLength);
-       var G = (Y = z.timeout) !== null && Y !== void 0 ? Y : 1 / 0,
-         Z = Date.now() + G,
-         W = [{ oldPos: -1, lastComponent: void 0 }],
-         D = this.extractCommon(W[0], q, K, 0, z);
-       if (W[0].oldPos + 1 >= X && D + 1 >= O)
-         return J(aD7(H, W[0].lastComponent, q, K, H.useLongestToken));
-       var j = -1 / 0,
-         M = 1 / 0;
-       function P() {
-         for (var N = Math.max(j, -$); N <= Math.min(M, $); N += 2) {
-           var T = void 0,
-             C = W[N - 1],
-             R = W[N + 1];
-           if (C) W[N - 1] = void 0;
-           var x = !1;
-           if (R) {
-             var y = R.oldPos - N;
-             x = R && 0 <= y && y < O;
-           }
-           var B = C && C.oldPos + 1 < X;
-           if (!x && !B) {
-             W[N] = void 0;
-             continue;
-           }
-           if (!B || (x && C.oldPos < R.oldPos))
-             T = H.addToPath(R, !0, !1, 0, z);
-           else T = H.addToPath(C, !1, !0, 1, z);
-           if (
-             ((D = H.extractCommon(T, q, K, N, z)),
-             T.oldPos + 1 >= X && D + 1 >= O)
-           )
-             return J(aD7(H, T.lastComponent, q, K, H.useLongestToken));
-           else {
-             if (((W[N] = T), T.oldPos + 1 >= X)) M = Math.min(M, N - 1);
-             if (D + 1 >= O) j = Math.max(j, N + 1);
-           }
-         }
-         $++;
-       }
-       if (w)
-         (function N() {
-           setTimeout(function () {
-             if ($ > _ || Date.now() > Z) return w();
-             if (!P()) N();
-           }, 0);
-         })();
-       else
-         while ($ <= _ && Date.now() <= Z) {
-           var f = P();
-           if (f) return f;
-         }
-     },
-     addToPath: function (K, q, Y, z, w) {
-       var H = K.lastComponent;
-       if (H && !w.oneChangePerToken && H.added === q && H.removed === Y)
-         return {
-           oldPos: K.oldPos + z,
-           lastComponent: {
-             count: H.count + 1,
-             added: q,
-             removed: Y,
-             previousComponent: H.previousComponent,
-           },
-         };
-       else
-         return {
-           oldPos: K.oldPos + z,
-           lastComponent: {
-             count: 1,
-             added: q,
-             removed: Y,
-             previousComponent: H,
-           },
-         };
-     },
-     extractCommon: function (K, q, Y, z, w) {
-       var H = q.length,
-         J = Y.length,
-         O = K.oldPos,
-         X = O - z,
-         $ = 0;
-       while (X + 1 < H && O + 1 < J && this.equals(Y[O + 1], q[X + 1], w))
-         if ((X++, O++, $++, w.oneChangePerToken))
-           K.lastComponent = {
-             count: 1,
-             previousComponent: K.lastComponent,
-             added: !1,
-             removed: !1,
-           };
-       if ($ && !w.oneChangePerToken)
-         K.lastComponent = {
-           count: $,
-           previousComponent: K.lastComponent,
-           added: !1,
-           removed: !1,
-         };
-       return ((K.oldPos = O), X);
-     },
-     equals: function (K, q, Y) {
-       if (Y.comparator) return Y.comparator(K, q);
-       else
-         return K === q || (Y.ignoreCase && K.toLowerCase() === q.toLowerCase());
-     },
-     removeEmpty: function (K) {
-       var q = [];
-       for (var Y = 0; Y < K.length; Y++) if (K[Y]) q.push(K[Y]);
-       return q;
-     },
-     castInput: function (K) {
-       return K;
-     },
-     tokenize: function (K) {
-       return Array.from(K);
-     },
-     join: function (K) {
-       return K.join("");
-     },
-     postProcess: function (K) {
-       return K;
-     },
-   };
-   A2H = new dI();
-   (($RY = new RegExp("[".concat(O_1, "]+|\\s+|[^").concat(O_1, "]"), "ug")),
-     ($_1 = new dI()));
-   $_1.equals = function (A, K, q) {
-     if (q.ignoreCase) ((A = A.toLowerCase()), (K = K.toLowerCase()));
-     return A.trim() === K.trim();
-   };
-   $_1.tokenize = function (A) {
-     var K = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : {},
-       q;
-     if (K.intlSegmenter) {
-       if (K.intlSegmenter.resolvedOptions().granularity != "word")
-         throw Error('The segmenter passed must have a granularity of "word"');
-       q = Array.from(K.intlSegmenter.segment(A), function (w) {
-         return w.segment;
-       });
-     } else q = A.match($RY) || [];
-     var Y = [],
-       z = null;
-     return (
-       q.forEach(function (w) {
-         if (/\s/.test(w))
-           if (z == null) Y.push(w);
-           else Y.push(Y.pop() + w);
-         else if (/\s/.test(z))
-           if (Y[Y.length - 1] == z) Y.push(Y.pop() + w);
-           else Y.push(z + w);
-         else Y.push(w);
-         z = w;
-       }),
-       Y
-     );
-   };
-   $_1.join = function (A) {
-     return A.map(function (K, q) {
-       if (q == 0) return K;
-       else return K.replace(/^\s+/, "");
-     }).join("");
-   };
-   $_1.postProcess = function (A, K) {
-     if (!A || K.oneChangePerToken) return A;
-     var q = null,
-       Y = null,
-       z = null;
-     if (
-       (A.forEach(function (w) {
-         if (w.added) Y = w;
-         else if (w.removed) z = w;
-         else {
-           if (Y || z) Aj7(q, z, Y, w);
-           ((q = w), (Y = null), (z = null));
-         }
-       }),
-       Y || z)
-     )
-       Aj7(q, z, Y, null);
-     return A;
-   };
-   Yj7 = new dI();
-   Yj7.tokenize = function (A) {
-     var K = new RegExp(
-       "(\\r?\\n)|[".concat(O_1, "]+|[^\\S\\n\\r]+|[^").concat(O_1, "]"),
-       "ug",
-     );
-     return A.match(K) || [];
-   };
-   __1 = new dI();
-   __1.tokenize = function (A, K) {
-     if (K.stripTrailingCr)
-       A = A.replace(
-         /\r\n/g,
-         `
- `,
-       );
-     var q = [],
-       Y = A.split(/(\n|\r\n)/);
-     if (!Y[Y.length - 1]) Y.pop();
-     for (var z = 0; z < Y.length; z++) {
-       var w = Y[z];
-       if (z % 2 && !K.newlineIsToken) q[q.length - 1] += w;
-       else q.push(w);
-     }
-     return q;
-   };
-   __1.equals = function (A, K, q) {
-     if (q.ignoreWhitespace) {
-       if (
-         !q.newlineIsToken ||
-         !A.includes(`
- `)
-       )
-         A = A.trim();
-       if (
-         !q.newlineIsToken ||
-         !K.includes(`
- `)
-       )
-         K = K.trim();
-     } else if (q.ignoreNewlineAtEof && !q.newlineIsToken) {
-       if (
-         A.endsWith(`
- `)
-       )
-         A = A.slice(0, -1);
-       if (
-         K.endsWith(`
- `)
-       )
-         K = K.slice(0, -1);
-     }
-     return dI.prototype.equals.call(this, A, K, q);
-   };
-   _RY = new dI();
-   _RY.tokenize = function (A) {
-     return A.split(/(\S.+?[.!?])(?=\s+|$)/);
-   };
-   GRY = new dI();
-   GRY.tokenize = function (A) {
-     return A.split(/([{}:;,]|\s+)/);
-   };
-   tBA = new dI();
-   tBA.useLongestToken = !0;
-   tBA.tokenize = __1.tokenize;
-   tBA.castInput = function (A, K) {
-     var { undefinedReplacement: q, stringifyReplacer: Y } = K,
-       z =
-         Y === void 0
-           ? function (w, H) {
-               return typeof H > "u" ? q : H;
-             }
-           : Y;
-     return typeof A === "string"
-       ? A
-       : JSON.stringify(lM6(A, null, null, z), z, "  ");
-   };
-   tBA.equals = function (A, K, q) {
-     return dI.prototype.equals.call(
-       tBA,
-       A.replace(/,([\r\n])/g, "$1"),
-       K.replace(/,([\r\n])/g, "$1"),
-       q,
-     );
-   };
-   iM6 = new dI();
-   iM6.tokenize = function (A) {
-     return A.slice();
-   };
-   iM6.join = iM6.removeEmpty = function (A) {
-     return A;
-   };
- });

--- Removed zmA (pretty-v2.1.25.js:310843-310874)
- var zmA = k(() => {
-   X0();
-   Z1();
-   C1();
-   X0();
-   maA();
-   wz();
-   aM6 = z6(async (A) => {
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
- - If you see a <${hN}> tag in the current conversation turn, the skill has ALREADY been loaded - follow the instructions directly instead of calling this tool again
- `;
-   });
- });

--- Removed gdY (pretty-v2.1.25.js:334183-334190)
- function gdY(A) {
-   try {
-     let K = mdY(A, { bigint: !0 });
-     return `${K.dev}:${K.ino}`;
-   } catch {
-     return null;
-   }
- }

--- Removed qW1 (pretty-v2.1.25.js:340640-340712)
- function qW1(A) {
-   let K = s(25),
-     { hookEvent: q, messages: Y, toolUseID: z, verbose: w } = A,
-     H;
-   if (K[0] !== q || K[1] !== Y || K[2] !== z)
-     ((H = HI7(Y, z, q)), (K[0] = q), (K[1] = Y), (K[2] = z), (K[3] = H));
-   else H = K[3];
-   let J = H,
-     O;
-   if (K[4] !== q || K[5] !== Y || K[6] !== z)
-     ((O = JI7(Y, z, q)), (K[4] = q), (K[5] = Y), (K[6] = z), (K[7] = O));
-   else O = K[7];
-   let X = O;
-   if (X === J) return null;
-   let $;
-   if (K[8] === Symbol.for("react.memo_cache_sentinel"))
-     (($ = XX.createElement(V, { dimColor: !0 }, "Running ")), (K[8] = $));
-   else $ = K[8];
-   let _;
-   if (K[9] !== q)
-     ((_ = XX.createElement(V, { dimColor: !0, bold: !0 }, q)),
-       (K[9] = q),
-       (K[10] = _));
-   else _ = K[10];
-   let G;
-   if (K[11] !== J || K[12] !== X)
-     ((G =
-       J === 1
-         ? XX.createElement(V, { dimColor: !0 }, " hook…")
-         : XX.createElement(
-             V,
-             { dimColor: !0 },
-             " ",
-             "hooks… (",
-             X,
-             "/",
-             J,
-             " done)",
-           )),
-       (K[11] = J),
-       (K[12] = X),
-       (K[13] = G));
-   else G = K[13];
-   let Z;
-   if (K[14] !== _ || K[15] !== G)
-     ((Z = XX.createElement(S, { flexDirection: "row" }, $, _, G)),
-       (K[14] = _),
-       (K[15] = G),
-       (K[16] = Z));
-   else Z = K[16];
-   let W;
-   if (K[17] !== q || K[18] !== Y || K[19] !== z || K[20] !== w)
-     ((W =
-       w && XX.createElement(foY, { messages: Y, toolUseID: z, hookEvent: q })),
-       (K[17] = q),
-       (K[18] = Y),
-       (K[19] = z),
-       (K[20] = w),
-       (K[21] = W));
-   else W = K[21];
-   let D;
-   if (K[22] !== Z || K[23] !== W)
-     ((D = XX.createElement(
-       k6,
-       null,
-       XX.createElement(S, { flexDirection: "column" }, Z, W),
-     )),
-       (K[22] = Z),
-       (K[23] = W),
-       (K[24] = D));
-   else D = K[24];
-   return D;
- }

--- Removed foY (pretty-v2.1.25.js:340713-340755)
- function foY(A) {
-   let K = s(15),
-     { messages: q, toolUseID: Y, hookEvent: z } = A,
-     w,
-     H,
-     J,
-     O;
-   if (K[0] !== z || K[1] !== q || K[2] !== Y) {
-     let $;
-     if (K[7] !== z || K[8] !== Y)
-       (($ = (G) =>
-         G.type === "progress" &&
-         G.data.type === "hook_progress" &&
-         G.data.hookEvent === z &&
-         G.parentToolUseID === Y),
-         (K[7] = z),
-         (K[8] = Y),
-         (K[9] = $));
-     else $ = K[9];
-     let _ = q.filter($);
-     ((w = S),
-       (H = "column"),
-       (J = 2),
-       (O = _.map(NoY)),
-       (K[0] = z),
-       (K[1] = q),
-       (K[2] = Y),
-       (K[3] = w),
-       (K[4] = H),
-       (K[5] = J),
-       (K[6] = O));
-   } else ((w = K[3]), (H = K[4]), (J = K[5]), (O = K[6]));
-   let X;
-   if (K[10] !== w || K[11] !== H || K[12] !== J || K[13] !== O)
-     ((X = XX.createElement(w, { flexDirection: H, marginLeft: J }, O)),
-       (K[10] = w),
-       (K[11] = H),
-       (K[12] = J),
-       (K[13] = O),
-       (K[14] = X));
-   else X = K[14];
-   return X;
- }

--- Removed NoY (pretty-v2.1.25.js:340756-340765)
- function NoY(A) {
-   return XX.createElement(
-     V,
-     { dimColor: !0, key: A.uuid },
-     "· ",
-     A.data.hookName,
-     ": ",
-     A.data.command,
-   );
- }

--- Removed Xj (pretty-v2.1.25.js:341726-341753)
- var Xj = v((uI7) => {
-   Object.defineProperty(uI7, "__esModule", { value: !0 });
-   uI7.Log = uI7.LogLevel = void 0;
-   var hoY = " DEBUG ",
-     boY = "  INFO ",
-     xoY = "  WARN ",
-     uoY = " ERROR ";
-   function XW1(A) {
-     return (A.unshift("[Statsig]"), A);
-   }
-   uI7.LogLevel = { None: 0, Error: 1, Warn: 2, Info: 3, Debug: 4 };
-   class R5A {
-     static info(...A) {
-       if (R5A.level >= uI7.LogLevel.Info) console.info(boY, ...XW1(A));
-     }
-     static debug(...A) {
-       if (R5A.level >= uI7.LogLevel.Debug) console.debug(hoY, ...XW1(A));
-     }
-     static warn(...A) {
-       if (R5A.level >= uI7.LogLevel.Warn) console.warn(xoY, ...XW1(A));
-     }
-     static error(...A) {
-       if (R5A.level >= uI7.LogLevel.Error) console.error(uoY, ...XW1(A));
-     }
-   }
-   uI7.Log = R5A;
-   R5A.level = uI7.LogLevel.Warn;
- });

--- Removed y5A (pretty-v2.1.25.js:341754-341794)
- var y5A = v((QI7) => {
-   var CT6, LT6, RT6;
-   Object.defineProperty(QI7, "__esModule", { value: !0 });
-   QI7._getInstance = QI7._getStatsigGlobalFlag = QI7._getStatsigGlobal = void 0;
-   var BoY = Xj(),
-     moY = () => {
-       return __STATSIG__ ? __STATSIG__ : $W1;
-     };
-   QI7._getStatsigGlobal = moY;
-   var goY = (A) => {
-     return QI7._getStatsigGlobal()[A];
-   };
-   QI7._getStatsigGlobalFlag = goY;
-   var FoY = (A) => {
-     let K = QI7._getStatsigGlobal();
-     if (!A) {
-       if (K.instances && Object.keys(K.instances).length > 1)
-         BoY.Log.warn(
-           "Call made to Statsig global instance without an SDK key but there is more than one client instance. If you are using mulitple clients, please specify the SDK key.",
-         );
-       return K.firstInstance;
-     }
-     return K.instances && K.instances[A];
-   };
-   QI7._getInstance = FoY;
-   var vDA = "__STATSIG__",
-     mI7 = typeof window < "u" ? window : {},
-     gI7 = typeof global < "u" ? global : {},
-     FI7 = typeof globalThis < "u" ? globalThis : {},
-     $W1 =
-       (RT6 =
-         (LT6 = (CT6 = mI7[vDA]) !== null && CT6 !== void 0 ? CT6 : gI7[vDA]) !==
-           null && LT6 !== void 0
-           ? LT6
-           : FI7[vDA]) !== null && RT6 !== void 0
-         ? RT6
-         : { instance: QI7._getInstance };
-   mI7[vDA] = $W1;
-   gI7[vDA] = $W1;
-   FI7[vDA] = $W1;
- });

--- Removed GW1 (pretty-v2.1.25.js:341795-341900)
- var GW1 = v((UI7) => {
-   Object.defineProperty(UI7, "__esModule", { value: !0 });
-   UI7.Diagnostics = void 0;
-   var _W1 = new Map(),
-     ST6 = "start",
-     hT6 = "end",
-     UoY = "statsig::diagnostics";
-   UI7.Diagnostics = {
-     _getMarkers: (A) => {
-       return _W1.get(A);
-     },
-     _markInitOverallStart: (A) => {
-       kDA(A, EDA({}, ST6, "overall"));
-     },
-     _markInitOverallEnd: (A, K, q) => {
-       kDA(
-         A,
-         EDA(
-           {
-             success: K,
-             error: K
-               ? void 0
-               : { name: "InitializeError", message: "Failed to initialize" },
-             evaluationDetails: q,
-           },
-           hT6,
-           "overall",
-         ),
-       );
-     },
-     _markInitNetworkReqStart: (A, K) => {
-       kDA(A, EDA(K, ST6, "initialize", "network_request"));
-     },
-     _markInitNetworkReqEnd: (A, K) => {
-       kDA(A, EDA(K, hT6, "initialize", "network_request"));
-     },
-     _markInitProcessStart: (A) => {
-       kDA(A, EDA({}, ST6, "initialize", "process"));
-     },
-     _markInitProcessEnd: (A, K) => {
-       kDA(A, EDA(K, hT6, "initialize", "process"));
-     },
-     _clearMarkers: (A) => {
-       _W1.delete(A);
-     },
-     _formatError(A) {
-       if (!(A && typeof A === "object")) return;
-       return {
-         code: bT6(A, "code"),
-         name: bT6(A, "name"),
-         message: bT6(A, "message"),
-       };
-     },
-     _getDiagnosticsData(A, K, q, Y) {
-       var z;
-       return {
-         success: (A === null || A === void 0 ? void 0 : A.ok) === !0,
-         statusCode: A === null || A === void 0 ? void 0 : A.status,
-         sdkRegion:
-           (z = A === null || A === void 0 ? void 0 : A.headers) === null ||
-           z === void 0
-             ? void 0
-             : z.get("x-statsig-region"),
-         isDelta: q.includes('"is_delta":true') === !0 ? !0 : void 0,
-         attempt: K,
-         error: UI7.Diagnostics._formatError(Y),
-       };
-     },
-     _enqueueDiagnosticsEvent(A, K, q, Y) {
-       let z = UI7.Diagnostics._getMarkers(q);
-       if (z == null || z.length <= 0) return -1;
-       let w = z[z.length - 1].timestamp - z[0].timestamp;
-       UI7.Diagnostics._clearMarkers(q);
-       let H = poY(A, {
-         context: "initialize",
-         markers: z.slice(),
-         statsigOptions: Y,
-       });
-       return (K.enqueue(H), w);
-     },
-   };
-   function EDA(A, K, q, Y) {
-     return Object.assign(
-       { key: q, action: K, step: Y, timestamp: Date.now() },
-       A,
-     );
-   }
-   function poY(A, K) {
-     return {
-       eventName: UoY,
-       user: A,
-       value: null,
-       metadata: K,
-       time: Date.now(),
-     };
-   }
-   function kDA(A, K) {
-     var q;
-     let Y = (q = _W1.get(A)) !== null && q !== void 0 ? q : [];
-     (Y.push(K), _W1.set(A, Y));
-   }
-   function bT6(A, K) {
-     if (K in A) return A[K];
-     return;
-   }
- });

--- Removed ZW1 (pretty-v2.1.25.js:341901-341913)
- var ZW1 = v((pI7) => {
-   Object.defineProperty(pI7, "__esModule", { value: !0 });
-   pI7._isTypeMatch = pI7._typeOf = void 0;
-   function doY(A) {
-     return Array.isArray(A) ? "array" : typeof A;
-   }
-   pI7._typeOf = doY;
-   function coY(A, K) {
-     let q = (Y) => (Array.isArray(Y) ? "array" : typeof Y);
-     return q(A) === q(K);
-   }
-   pI7._isTypeMatch = coY;
- });

--- Removed CDA (pretty-v2.1.25.js:341914-341948)
- var CDA = v((cI7) => {
-   Object.defineProperty(cI7, "__esModule", { value: !0 });
-   cI7._getSortedObject = cI7._DJB2Object = cI7._DJB2 = void 0;
-   var ioY = ZW1(),
-     noY = (A) => {
-       let K = 0;
-       for (let q = 0; q < A.length; q++) {
-         let Y = A.charCodeAt(q);
-         ((K = (K << 5) - K + Y), (K = K & K));
-       }
-       return String(K >>> 0);
-     };
-   cI7._DJB2 = noY;
-   var roY = (A, K) => {
-     return cI7._DJB2(JSON.stringify(cI7._getSortedObject(A, K)));
-   };
-   cI7._DJB2Object = roY;
-   var ooY = (A, K) => {
-     if (A == null) return null;
-     let q = Object.keys(A).sort(),
-       Y = {};
-     return (
-       q.forEach((z) => {
-         let w = A[z];
-         if (K === 0 || (0, ioY._typeOf)(w) !== "object") {
-           Y[z] = w;
-           return;
-         }
-         Y[z] = cI7._getSortedObject(w, K != null ? K - 1 : K);
-       }),
-       Y
-     );
-   };
-   cI7._getSortedObject = ooY;
- });

--- Removed jgA (pretty-v2.1.25.js:341949-341973)
- var jgA = v((rI7) => {
-   Object.defineProperty(rI7, "__esModule", { value: !0 });
-   rI7._getStorageKey = rI7._getUserStorageKey = void 0;
-   var iI7 = CDA();
-   function nI7(A, K, q) {
-     var Y;
-     if (q) return q(A, K);
-     let z = K && K.customIDs ? K.customIDs : {},
-       w = [
-         `uid:${(Y = K === null || K === void 0 ? void 0 : K.userID) !== null && Y !== void 0 ? Y : ""}`,
-         `cids:${Object.keys(z)
-           .sort((H, J) => H.localeCompare(J))
-           .map((H) => `${H}-${z[H]}`)
-           .join(",")}`,
-         `k:${A}`,
-       ];
-     return (0, iI7._DJB2)(w.join("|"));
-   }
-   rI7._getUserStorageKey = nI7;
-   function soY(A, K, q) {
-     if (K) return nI7(A, K, q);
-     return (0, iI7._DJB2)(`k:${A}`);
-   }
-   rI7._getStorageKey = soY;
- });

--- Removed MgA (pretty-v2.1.25.js:341974-341997)
- var MgA = v((aI7) => {
-   Object.defineProperty(aI7, "__esModule", { value: !0 });
-   aI7.NetworkParam = aI7.NetworkDefault = aI7.Endpoint = void 0;
-   aI7.Endpoint = {
-     _initialize: "initialize",
-     _rgstr: "rgstr",
-     _download_config_specs: "download_config_specs",
-   };
-   aI7.NetworkDefault = {
-     [aI7.Endpoint._rgstr]: "https://prodregistryv2.org/v1",
-     [aI7.Endpoint._initialize]: "https://featureassets.org/v1",
-     [aI7.Endpoint._download_config_specs]: "https://api.statsigcdn.com/v1",
-   };
-   aI7.NetworkParam = {
-     EventCount: "ec",
-     SdkKey: "k",
-     SdkType: "st",
-     SdkVersion: "sv",
-     Time: "t",
-     SessionID: "sid",
-     StatsigEncoded: "se",
-     IsGzipped: "gz",
-   };
- });

--- Removed I5A (pretty-v2.1.25.js:341998-342058)
- var I5A = v((tI7) => {
-   Object.defineProperty(tI7, "__esModule", { value: !0 });
-   tI7._getCurrentPageUrlSafe =
-     tI7._addDocumentEventListenerSafe =
-     tI7._addWindowEventListenerSafe =
-     tI7._isServerEnv =
-     tI7._getDocumentSafe =
-     tI7._getWindowSafe =
-       void 0;
-   var AaY = () => {
-     return typeof window < "u" ? window : null;
-   };
-   tI7._getWindowSafe = AaY;
-   var KaY = () => {
-     var A;
-     let K = tI7._getWindowSafe();
-     return (A = K === null || K === void 0 ? void 0 : K.document) !== null &&
-       A !== void 0
-       ? A
-       : null;
-   };
-   tI7._getDocumentSafe = KaY;
-   var qaY = () => {
-     if (tI7._getDocumentSafe() !== null) return !1;
-     let A =
-       typeof process < "u" &&
-       process.versions != null &&
-       process.versions.node != null;
-     return typeof EdgeRuntime === "string" || A;
-   };
-   tI7._isServerEnv = qaY;
-   var YaY = (A, K) => {
-     let q = tI7._getWindowSafe();
-     if (
-       typeof (q === null || q === void 0 ? void 0 : q.addEventListener) ===
-       "function"
-     )
-       q.addEventListener(A, K);
-   };
-   tI7._addWindowEventListenerSafe = YaY;
-   var zaY = (A, K) => {
-     let q = tI7._getDocumentSafe();
-     if (
-       typeof (q === null || q === void 0 ? void 0 : q.addEventListener) ===
-       "function"
-     )
-       q.addEventListener(A, K);
-   };
-   tI7._addDocumentEventListenerSafe = zaY;
-   var waY = () => {
-     var A;
-     try {
-       return (A = tI7._getWindowSafe()) === null || A === void 0
-         ? void 0
-         : A.location.href.split(/[?#]/)[0];
-     } catch (K) {
-       return;
-     }
-   };
-   tI7._getCurrentPageUrlSafe = waY;
- });

--- Removed BT6 (pretty-v2.1.25.js:342059-342188)
- var BT6 = v((YS7) => {
-   Object.defineProperty(YS7, "__esModule", { value: !0 });
-   YS7._createLayerParameterExposure =
-     YS7._createConfigExposure =
-     YS7._mapExposures =
-     YS7._createGateExposure =
-     YS7._isExposureEvent =
-       void 0;
-   var AS7 = "statsig::config_exposure",
-     KS7 = "statsig::gate_exposure",
-     qS7 = "statsig::layer_exposure",
-     uT6 = (A, K, q, Y, z) => {
-       if (q.bootstrapMetadata) Y.bootstrapMetadata = q.bootstrapMetadata;
-       return {
-         eventName: A,
-         user: K,
-         value: null,
-         metadata: ZaY(q, Y),
-         secondaryExposures: z,
-         time: Date.now(),
-       };
-     },
-     XaY = ({ eventName: A }) => {
-       return A === KS7 || A === AS7 || A === qS7;
-     };
-   YS7._isExposureEvent = XaY;
-   var $aY = (A, K, q) => {
-     var Y, z, w;
-     let H = { gate: K.name, gateValue: String(K.value), ruleID: K.ruleID };
-     if (
-       ((Y = K.__evaluation) === null || Y === void 0 ? void 0 : Y.version) !=
-       null
-     )
-       H.configVersion = K.__evaluation.version;
-     return uT6(
-       KS7,
-       A,
-       K.details,
-       H,
-       MW1(
-         (w =
-           (z = K.__evaluation) === null || z === void 0
-             ? void 0
-             : z.secondary_exposures) !== null && w !== void 0
-           ? w
-           : [],
-         q,
-       ),
-     );
-   };
-   YS7._createGateExposure = $aY;
-   function MW1(A, K) {
-     return A.map((q) => {
-       if (typeof q === "string")
-         return (K !== null && K !== void 0 ? K : {})[q];
-       return q;
-     }).filter((q) => q != null);
-   }
-   YS7._mapExposures = MW1;
-   var _aY = (A, K, q) => {
-     var Y, z, w, H;
-     let J = { config: K.name, ruleID: K.ruleID };
-     if (
-       ((Y = K.__evaluation) === null || Y === void 0 ? void 0 : Y.version) !=
-       null
-     )
-       J.configVersion = K.__evaluation.version;
-     if (
-       ((z = K.__evaluation) === null || z === void 0 ? void 0 : z.passed) !=
-       null
-     )
-       J.rulePassed = String(K.__evaluation.passed);
-     return uT6(
-       AS7,
-       A,
-       K.details,
-       J,
-       MW1(
-         (H =
-           (w = K.__evaluation) === null || w === void 0
-             ? void 0
-             : w.secondary_exposures) !== null && H !== void 0
-           ? H
-           : [],
-         q,
-       ),
-     );
-   };
-   YS7._createConfigExposure = _aY;
-   var GaY = (A, K, q, Y) => {
-     var z, w, H, J;
-     let O = K.__evaluation,
-       X =
-         ((z = O === null || O === void 0 ? void 0 : O.explicit_parameters) ===
-           null || z === void 0
-           ? void 0
-           : z.includes(q)) === !0,
-       $ = "",
-       _ =
-         (w =
-           O === null || O === void 0
-             ? void 0
-             : O.undelegated_secondary_exposures) !== null && w !== void 0
-           ? w
-           : [];
-     if (X)
-       (($ =
-         (H = O.allocated_experiment_name) !== null && H !== void 0 ? H : ""),
-         (_ = O.secondary_exposures));
-     let G = {
-       config: K.name,
-       parameterName: q,
-       ruleID: K.ruleID,
-       allocatedExperiment: $,
-       isExplicitParameter: String(X),
-     };
-     if (
-       ((J = K.__evaluation) === null || J === void 0 ? void 0 : J.version) !=
-       null
-     )
-       G.configVersion = K.__evaluation.version;
-     return uT6(qS7, A, K.details, G, MW1(_, Y));
-   };
-   YS7._createLayerParameterExposure = GaY;
-   var ZaY = (A, K) => {
-     if (((K.reason = A.reason), A.lcut)) K.lcut = String(A.lcut);
-     if (A.receivedAt) K.receivedAt = String(A.receivedAt);
-     return K;
-   };
- });

--- Removed rp (pretty-v2.1.25.js:342189-342260)
- var rp = v((wS7) => {
-   Object.defineProperty(wS7, "__esModule", { value: !0 });
-   wS7._setObjectInStorage = wS7._getObjectFromStorage = wS7.Storage = void 0;
-   var PaY = Xj(),
-     VaY = I5A(),
-     PgA = {},
-     gT6 = {
-       isReady: () => !0,
-       isReadyResolver: () => null,
-       getProviderName: () => "InMemory",
-       getItem: (A) => (PgA[A] ? PgA[A] : null),
-       setItem: (A, K) => {
-         PgA[A] = K;
-       },
-       removeItem: (A) => {
-         delete PgA[A];
-       },
-       getAllKeys: () => Object.keys(PgA),
-     },
-     PW1 = null;
-   try {
-     let A = (0, VaY._getWindowSafe)();
-     if (A && A.localStorage && typeof A.localStorage.getItem === "function")
-       PW1 = {
-         isReady: () => !0,
-         isReadyResolver: () => null,
-         getProviderName: () => "LocalStorage",
-         getItem: (K) => A.localStorage.getItem(K),
-         setItem: (K, q) => A.localStorage.setItem(K, q),
-         removeItem: (K) => A.localStorage.removeItem(K),
-         getAllKeys: () => Object.keys(A.localStorage),
-       };
-   } catch (A) {
-     PaY.Log.warn("Failed to setup localStorageProvider.");
-   }
-   var mT6 = PW1 !== null && PW1 !== void 0 ? PW1 : gT6,
-     NB = mT6;
-   function faY(A) {
-     try {
-       return A();
-     } catch (K) {
-       if (K instanceof Error && K.name === "SecurityError")
-         return (wS7.Storage._setProvider(gT6), null);
-       throw K;
-     }
-   }
-   wS7.Storage = {
-     isReady: () => NB.isReady(),
-     isReadyResolver: () => NB.isReadyResolver(),
-     getProviderName: () => NB.getProviderName(),
-     getItem: (A) => faY(() => NB.getItem(A)),
-     setItem: (A, K) => NB.setItem(A, K),
-     removeItem: (A) => NB.removeItem(A),
-     getAllKeys: () => NB.getAllKeys(),
-     _setProvider: (A) => {
-       ((mT6 = A), (NB = A));
-     },
-     _setDisabled: (A) => {
-       if (A) NB = gT6;
-       else NB = mT6;
-     },
-   };
-   function NaY(A) {
-     let K = wS7.Storage.getItem(A);
-     return JSON.parse(K !== null && K !== void 0 ? K : "null");
-   }
-   wS7._getObjectFromStorage = NaY;
-   function TaY(A, K) {
-     wS7.Storage.setItem(A, JSON.stringify(K));
-   }
-   wS7._setObjectInStorage = TaY;
- });

--- Removed FT6 (pretty-v2.1.25.js:342261-342293)
- var FT6 = v((OS7) => {
-   Object.defineProperty(OS7, "__esModule", { value: !0 });
-   OS7.UrlConfiguration = void 0;
-   var fW1 = MgA(),
-     EaY = {
-       [fW1.Endpoint._initialize]: "i",
-       [fW1.Endpoint._rgstr]: "e",
-       [fW1.Endpoint._download_config_specs]: "d",
-     };
-   class JS7 {
-     constructor(A, K, q, Y) {
-       if (
-         ((this.customUrl = null),
-         (this.fallbackUrls = null),
-         (this.endpoint = A),
-         (this.endpointDnsKey = EaY[A]),
-         K)
-       )
-         this.customUrl = K;
-       if (!K && q) this.customUrl = q.endsWith("/") ? `${q}${A}` : `${q}/${A}`;
-       if (Y) this.fallbackUrls = Y;
-       let z = fW1.NetworkDefault[A];
-       this.defaultUrl = `${z}/${A}`;
-     }
-     getUrl() {
-       var A;
-       return (A = this.customUrl) !== null && A !== void 0
-         ? A
-         : this.defaultUrl;
-     }
-   }
-   OS7.UrlConfiguration = JS7;
- });

--- Removed vW1 (pretty-v2.1.25.js:342294-342336)
- var vW1 = v((_S7) => {
-   Object.defineProperty(_S7, "__esModule", { value: !0 });
-   _S7._notifyVisibilityChanged =
-     _S7._subscribeToVisiblityChanged =
-     _S7._isUnloading =
-     _S7._isCurrentlyVisible =
-       void 0;
-   var NW1 = I5A(),
-     TW1 = "foreground",
-     UT6 = "background",
-     $S7 = [],
-     QT6 = TW1,
-     pT6 = !1,
-     kaY = () => {
-       return QT6 === TW1;
-     };
-   _S7._isCurrentlyVisible = kaY;
-   var CaY = () => pT6;
-   _S7._isUnloading = CaY;
-   var LaY = (A) => {
-     $S7.unshift(A);
-   };
-   _S7._subscribeToVisiblityChanged = LaY;
-   var RaY = (A) => {
-     if (A === QT6) return;
-     ((QT6 = A), $S7.forEach((K) => K(A)));
-   };
-   _S7._notifyVisibilityChanged = RaY;
-   (0, NW1._addWindowEventListenerSafe)("focus", () => {
-     ((pT6 = !1), _S7._notifyVisibilityChanged(TW1));
-   });
-   (0, NW1._addWindowEventListenerSafe)("blur", () =>
-     _S7._notifyVisibilityChanged(UT6),
-   );
-   (0, NW1._addWindowEventListenerSafe)("beforeunload", () => {
-     ((pT6 = !0), _S7._notifyVisibilityChanged(UT6));
-   });
-   (0, NW1._addDocumentEventListenerSafe)("visibilitychange", () => {
-     _S7._notifyVisibilityChanged(
-       document.visibilityState === "visible" ? TW1 : UT6,
-     );
-   });
- });

--- Removed cT6 (pretty-v2.1.25.js:342337-342637)
- var cT6 = v((IDA) => {
-   var RDA =
-     (IDA && IDA.__awaiter) ||
-     function (A, K, q, Y) {
-       function z(w) {
-         return w instanceof q
-           ? w
-           : new q(function (H) {
-               H(w);
-             });
-       }
-       return new (q || (q = Promise))(function (w, H) {
-         function J($) {
-           try {
-             X(Y.next($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function O($) {
-           try {
-             X(Y.throw($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function X($) {
-           $.done ? w($.value) : z($.value).then(J, O);
-         }
-         X((Y = Y.apply(A, K || [])).next());
-       });
-     };
-   Object.defineProperty(IDA, "__esModule", { value: !0 });
-   IDA.EventLogger = void 0;
-   var haY = jgA(),
-     baY = CDA(),
-     VgA = Xj(),
-     GS7 = MgA(),
-     dT6 = I5A(),
-     xaY = BT6(),
-     yDA = rp(),
-     uaY = FT6(),
-     ZS7 = vW1(),
-     BaY = 100,
-     maY = 1e4,
-     gaY = 1000,
-     FaY = 600000,
-     QaY = 500,
-     WS7 = 200,
-     fgA = {},
-     EW1 = { Startup: "startup", GainedFocus: "gained_focus" };
-   class S5A {
-     static _safeFlushAndForget(A) {
-       var K;
-       (K = fgA[A]) === null || K === void 0 || K.flush().catch(() => {});
-     }
-     static _safeRetryFailedLogs(A) {
-       var K;
-       (K = fgA[A]) === null ||
-         K === void 0 ||
-         K._retryFailedLogs(EW1.GainedFocus);
-     }
-     constructor(A, K, q, Y) {
-       var z;
-       ((this._sdkKey = A),
-         (this._emitter = K),
-         (this._network = q),
-         (this._options = Y),
-         (this._queue = []),
-         (this._lastExposureTimeMap = {}),
-         (this._nonExposedChecks = {}),
-         (this._hasRunQuickFlush = !1),
-         (this._creationTime = Date.now()),
-         (this._isLoggingDisabled =
-           (Y === null || Y === void 0 ? void 0 : Y.disableLogging) === !0),
-         (this._maxQueueSize =
-           (z = Y === null || Y === void 0 ? void 0 : Y.loggingBufferMaxSize) !==
-             null && z !== void 0
-             ? z
-             : BaY));
-       let w = Y === null || Y === void 0 ? void 0 : Y.networkConfig;
-       this._logEventUrlConfig = new uaY.UrlConfiguration(
-         GS7.Endpoint._rgstr,
-         w === null || w === void 0 ? void 0 : w.logEventUrl,
-         w === null || w === void 0 ? void 0 : w.api,
-         w === null || w === void 0 ? void 0 : w.logEventFallbackUrls,
-       );
-     }
-     setLoggingDisabled(A) {
-       this._isLoggingDisabled = A;
-     }
-     enqueue(A) {
-       if (!this._shouldLogEvent(A)) return;
-       if (
-         (this._normalizeAndAppendEvent(A),
-         this._quickFlushIfNeeded(),
-         this._queue.length > this._maxQueueSize)
-       )
-         S5A._safeFlushAndForget(this._sdkKey);
-     }
-     incrementNonExposureCount(A) {
-       var K;
-       let q = (K = this._nonExposedChecks[A]) !== null && K !== void 0 ? K : 0;
-       this._nonExposedChecks[A] = q + 1;
-     }
-     reset() {
-       this._lastExposureTimeMap = {};
-     }
-     start() {
-       if ((0, dT6._isServerEnv)()) return;
-       ((fgA[this._sdkKey] = this),
-         (0, ZS7._subscribeToVisiblityChanged)((A) => {
-           if (A === "background") S5A._safeFlushAndForget(this._sdkKey);
-           else if (A === "foreground") S5A._safeRetryFailedLogs(this._sdkKey);
-         }),
-         this._retryFailedLogs(EW1.Startup),
-         this._startBackgroundFlushInterval());
-     }
-     stop() {
-       return RDA(this, void 0, void 0, function* () {
-         if (this._flushIntervalId)
-           (clearInterval(this._flushIntervalId),
-             (this._flushIntervalId = null));
-         (delete fgA[this._sdkKey], yield this.flush());
-       });
-     }
-     flush() {
-       return RDA(this, void 0, void 0, function* () {
-         if ((this._appendAndResetNonExposedChecks(), this._queue.length === 0))
-           return;
-         let A = this._queue;
-         ((this._queue = []), yield this._sendEvents(A));
-       });
-     }
-     _quickFlushIfNeeded() {
-       if (this._hasRunQuickFlush) return;
-       if (
-         ((this._hasRunQuickFlush = !0), Date.now() - this._creationTime > WS7)
-       )
-         return;
-       setTimeout(() => S5A._safeFlushAndForget(this._sdkKey), WS7);
-     }
-     _shouldLogEvent(A) {
-       if ((0, dT6._isServerEnv)()) return !1;
-       if (!(0, xaY._isExposureEvent)(A)) return !0;
-       let K = A.user ? A.user : { statsigEnvironment: void 0 },
-         q = (0, haY._getUserStorageKey)(this._sdkKey, K),
-         Y = A.metadata ? A.metadata : {},
-         z = [
-           A.eventName,
-           q,
-           Y.gate,
-           Y.config,
-           Y.ruleID,
-           Y.allocatedExperiment,
-           Y.parameterName,
-           String(Y.isExplicitParameter),
-           Y.reason,
-         ].join("|"),
-         w = this._lastExposureTimeMap[z],
-         H = Date.now();
-       if (w && H - w < FaY) return !1;
-       if (Object.keys(this._lastExposureTimeMap).length > gaY)
-         this._lastExposureTimeMap = {};
-       return ((this._lastExposureTimeMap[z] = H), !0);
-     }
-     _sendEvents(A) {
-       var K, q;
-       return RDA(this, void 0, void 0, function* () {
-         if (this._isLoggingDisabled)
-           return (this._saveFailedLogsToStorage(A), !1);
-         try {
-           let z =
-             (0, ZS7._isUnloading)() &&
-             this._network.isBeaconSupported() &&
-             ((q =
-               (K = this._options) === null || K === void 0
-                 ? void 0
-                 : K.networkConfig) === null || q === void 0
-               ? void 0
-               : q.networkOverrideFunc) == null;
-           if (
-             (this._emitter({ name: "pre_logs_flushed", events: A }),
-             (z
-               ? yield this._sendEventsViaBeacon(A)
-               : yield this._sendEventsViaPost(A)
-             ).success)
-           )
-             return (this._emitter({ name: "logs_flushed", events: A }), !0);
-           else
-             return (
-               VgA.Log.warn("Failed to flush events."),
-               this._saveFailedLogsToStorage(A),
-               !1
-             );
-         } catch (Y) {
-           return (VgA.Log.warn("Failed to flush events."), !1);
-         }
-       });
-     }
-     _sendEventsViaPost(A) {
-       var K;
-       return RDA(this, void 0, void 0, function* () {
-         let q = yield this._network.post(this._getRequestData(A)),
-           Y =
-             (K = q === null || q === void 0 ? void 0 : q.code) !== null &&
-             K !== void 0
-               ? K
-               : -1;
-         return { success: Y >= 200 && Y < 300 };
-       });
-     }
-     _sendEventsViaBeacon(A) {
-       return RDA(this, void 0, void 0, function* () {
-         return { success: yield this._network.beacon(this._getRequestData(A)) };
-       });
-     }
-     _getRequestData(A) {
-       return {
-         sdkKey: this._sdkKey,
-         data: { events: A },
-         urlConfig: this._logEventUrlConfig,
-         retries: 3,
-         isCompressable: !0,
-         params: { [GS7.NetworkParam.EventCount]: String(A.length) },
-       };
-     }
-     _saveFailedLogsToStorage(A) {
-       while (A.length > QaY) A.shift();
-       let K = this._getStorageKey();
-       try {
-         (0, yDA._setObjectInStorage)(K, A);
-       } catch (q) {
-         VgA.Log.warn("Unable to save failed logs to storage");
-       }
-     }
-     _retryFailedLogs(A) {
-       let K = this._getStorageKey();
-       (() =>
-         RDA(this, void 0, void 0, function* () {
-           if (!yDA.Storage.isReady()) yield yDA.Storage.isReadyResolver();
-           let q = (0, yDA._getObjectFromStorage)(K);
-           if (!q) return;
-           if (A === EW1.Startup) yDA.Storage.removeItem(K);
-           if ((yield this._sendEvents(q)) && A === EW1.GainedFocus)
-             yDA.Storage.removeItem(K);
-         }))().catch(() => {
-         VgA.Log.warn("Failed to flush stored logs");
-       });
-     }
-     _getStorageKey() {
-       return `statsig.failed_logs.${(0, baY._DJB2)(this._sdkKey)}`;
-     }
-     _normalizeAndAppendEvent(A) {
-       if (A.user)
-         ((A.user = Object.assign({}, A.user)), delete A.user.privateAttributes);
-       let K = {},
-         q = this._getCurrentPageUrl();
-       if (q) K.statsigMetadata = { currentPage: q };
-       let Y = Object.assign(Object.assign({}, A), K);
-       (VgA.Log.debug("Enqueued Event:", Y), this._queue.push(Y));
-     }
-     _appendAndResetNonExposedChecks() {
-       if (Object.keys(this._nonExposedChecks).length === 0) return;
-       (this._normalizeAndAppendEvent({
-         eventName: "statsig::non_exposed_checks",
-         user: null,
-         time: Date.now(),
-         metadata: { checks: Object.assign({}, this._nonExposedChecks) },
-       }),
-         (this._nonExposedChecks = {}));
-     }
-     _getCurrentPageUrl() {
-       var A;
-       if (
-         ((A = this._options) === null || A === void 0
-           ? void 0
-           : A.includeCurrentPageUrlWithEvents) === !1
-       )
-         return;
-       return (0, dT6._getCurrentPageUrlSafe)();
-     }
-     _startBackgroundFlushInterval() {
-       var A, K;
-       let q =
-           (K =
-             (A = this._options) === null || A === void 0
-               ? void 0
-               : A.loggingIntervalMs) !== null && K !== void 0
-             ? K
-             : maY,
-         Y = setInterval(() => {
-           let z = fgA[this._sdkKey];
-           if (!z || z._flushIntervalId !== Y) clearInterval(Y);
-           else S5A._safeFlushAndForget(this._sdkKey);
-         }, q);
-       this._flushIntervalId = Y;
-     }
-   }
-   IDA.EventLogger = S5A;
- });

--- Removed NgA (pretty-v2.1.25.js:342638-342649)
- var NgA = v((DS7) => {
-   Object.defineProperty(DS7, "__esModule", { value: !0 });
-   DS7.StatsigMetadataProvider = DS7.SDK_VERSION = void 0;
-   DS7.SDK_VERSION = "3.12.1";
-   var lT6 = { sdkVersion: DS7.SDK_VERSION, sdkType: "js-mono" };
-   DS7.StatsigMetadataProvider = {
-     get: () => lT6,
-     add: (A) => {
-       lT6 = Object.assign(Object.assign({}, lT6), A);
-     },
-   };
- });

--- Removed kW1 (pretty-v2.1.25.js:342653-342676)
- var kW1 = v((fS7) => {
-   Object.defineProperty(fS7, "__esModule", { value: !0 });
-   fS7.getUUID = void 0;
-   function UaY() {
-     if (typeof crypto < "u" && typeof crypto.randomUUID === "function")
-       return crypto.randomUUID();
-     let A = new Date().getTime(),
-       K =
-         (typeof performance < "u" &&
-           performance.now &&
-           performance.now() * 1000) ||
-         0;
-     return `xxxxxxxx-xxxx-4xxx-${"89ab"[Math.floor(Math.random() * 4)]}xxx-xxxxxxxxxxxx`.replace(
-       /[xy]/g,
-       (Y) => {
-         let z = Math.random() * 16;
-         if (A > 0) ((z = (A + z) % 16 | 0), (A = Math.floor(A / 16)));
-         else ((z = (K + z) % 16 | 0), (K = Math.floor(K / 16)));
-         return (Y === "x" ? z : (z & 7) | 8).toString(16);
-       },
-     );
-   }
-   fS7.getUUID = UaY;
- });

--- Removed LW1 (pretty-v2.1.25.js:342677-342713)
- var LW1 = v((kS7) => {
-   Object.defineProperty(kS7, "__esModule", { value: !0 });
-   kS7.StableID = void 0;
-   var paY = jgA(),
-     daY = Xj(),
-     vS7 = rp(),
-     caY = kW1(),
-     CW1 = {};
-   kS7.StableID = {
-     get: (A) => {
-       if (CW1[A] == null) {
-         let K = laY(A);
-         if (K == null) ((K = (0, caY.getUUID)()), TS7(K, A));
-         CW1[A] = K;
-       }
-       return CW1[A];
-     },
-     setOverride: (A, K) => {
-       ((CW1[K] = A), TS7(A, K));
-     },
-   };
-   function ES7(A) {
-     return `statsig.stable_id.${(0, paY._getStorageKey)(A)}`;
-   }
-   function TS7(A, K) {
-     let q = ES7(K);
-     try {
-       (0, vS7._setObjectInStorage)(q, A);
-     } catch (Y) {
-       daY.Log.warn("Failed to save StableID");
-     }
-   }
-   function laY(A) {
-     let K = ES7(A);
-     return (0, vS7._getObjectFromStorage)(K);
-   }
- });

--- Removed iT6 (pretty-v2.1.25.js:342714-342738)
- var iT6 = v((LS7) => {
-   Object.defineProperty(LS7, "__esModule", { value: !0 });
-   LS7._getFullUserHash = LS7._normalizeUser = void 0;
-   var iaY = CDA(),
-     naY = Xj();
-   function raY(A, K, q) {
-     try {
-       let Y = JSON.parse(JSON.stringify(A));
-       if (K != null && K.environment != null)
-         Y.statsigEnvironment = K.environment;
-       else if (q != null) Y.statsigEnvironment = { tier: q };
-       return Y;
-     } catch (Y) {
-       return (
-         naY.Log.error("Failed to JSON.stringify user"),
-         { statsigEnvironment: void 0 }
-       );
-     }
-   }
-   LS7._normalizeUser = raY;
-   function oaY(A) {
-     return A ? (0, iaY._DJB2Object)(A) : null;
-   }
-   LS7._getFullUserHash = oaY;
- });

--- Removed nT6 (pretty-v2.1.25.js:342739-342751)
- var nT6 = v((yS7) => {
-   Object.defineProperty(yS7, "__esModule", { value: !0 });
-   yS7._typedJsonParse = void 0;
-   var saY = Xj();
-   function taY(A, K, q) {
-     try {
-       let Y = JSON.parse(A);
-       if (Y && typeof Y === "object" && K in Y) return Y;
-     } catch (Y) {}
-     return (saY.Log.error(`Failed to parse ${q}`), null);
-   }
-   yS7._typedJsonParse = taY;
- });

--- Removed BS7 (pretty-v2.1.25.js:342752-342960)
- var BS7 = v((cs) => {
-   var rT6 =
-     (cs && cs.__awaiter) ||
-     function (A, K, q, Y) {
-       function z(w) {
-         return w instanceof q
-           ? w
-           : new q(function (H) {
-               H(w);
-             });
-       }
-       return new (q || (q = Promise))(function (w, H) {
-         function J($) {
-           try {
-             X(Y.next($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function O($) {
-           try {
-             X(Y.throw($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function X($) {
-           $.done ? w($.value) : z($.value).then(J, O);
-         }
-         X((Y = Y.apply(A, K || [])).next());
-       });
-     };
-   Object.defineProperty(cs, "__esModule", { value: !0 });
-   cs._makeDataAdapterResult = cs.DataAdapterCore = void 0;
-   var RW1 = Xj(),
-     eaY = LW1(),
-     yW1 = iT6(),
-     ds = rp(),
-     SS7 = nT6(),
-     hS7 = 10;
-   class bS7 {
-     constructor(A, K) {
-       ((this._adapterName = A),
-         (this._cacheSuffix = K),
-         (this._options = null),
-         (this._sdkKey = null),
-         (this._lastModifiedStoreKey = `statsig.last_modified_time.${K}`),
-         (this._inMemoryCache = new xS7()));
-     }
-     attach(A, K) {
-       ((this._sdkKey = A), (this._options = K));
-     }
-     getDataSync(A) {
-       let K = A && (0, yW1._normalizeUser)(A, this._options),
-         q = this._getCacheKey(K),
-         Y = this._inMemoryCache.get(q, K);
-       if (Y) return Y;
-       let z = this._loadFromCache(q);
-       if (z)
-         return (this._inMemoryCache.add(q, z), this._inMemoryCache.get(q, K));
-       return null;
-     }
-     setData(A, K) {
-       let q = K && (0, yW1._normalizeUser)(K, this._options),
-         Y = this._getCacheKey(q);
-       this._inMemoryCache.add(Y, IW1("Bootstrap", A, null, q));
-     }
-     _getDataAsyncImpl(A, K, q) {
-       return rT6(this, void 0, void 0, function* () {
-         if (!ds.Storage.isReady()) yield ds.Storage.isReadyResolver();
-         let Y = A !== null && A !== void 0 ? A : this.getDataSync(K),
-           z = [this._fetchAndPrepFromNetwork(Y, K, q)];
-         if (q === null || q === void 0 ? void 0 : q.timeoutMs)
-           z.push(
-             new Promise((w) => setTimeout(w, q.timeoutMs)).then(() => {
-               return (RW1.Log.debug("Fetching latest value timed out"), null);
-             }),
-           );
-         return yield Promise.race(z);
-       });
-     }
-     _prefetchDataImpl(A, K) {
-       return rT6(this, void 0, void 0, function* () {
-         let q = A && (0, yW1._normalizeUser)(A, this._options),
-           Y = this._getCacheKey(q),
-           z = yield this._getDataAsyncImpl(null, q, K);
-         if (z)
-           this._inMemoryCache.add(
-             Y,
-             Object.assign(Object.assign({}, z), { source: "Prefetch" }),
-           );
-       });
-     }
-     _fetchAndPrepFromNetwork(A, K, q) {
-       var Y;
-       return rT6(this, void 0, void 0, function* () {
-         let z =
-             (Y = A === null || A === void 0 ? void 0 : A.data) !== null &&
-             Y !== void 0
-               ? Y
-               : null,
-           w = A != null && this._isCachedResultValidFor204(A, K),
-           H = yield this._fetchFromNetwork(z, K, q, w);
-         if (!H)
-           return (RW1.Log.debug("No response returned for latest value"), null);
-         let J = (0, SS7._typedJsonParse)(H, "has_updates", "Response"),
-           O = this._getSdkKey(),
-           X = eaY.StableID.get(O),
-           $ = null;
-         if ((J === null || J === void 0 ? void 0 : J.has_updates) === !0)
-           $ = IW1("Network", H, X, K);
-         else if (
-           z &&
-           (J === null || J === void 0 ? void 0 : J.has_updates) === !1
-         )
-           $ = IW1("NetworkNotModified", z, X, K);
-         else return null;
-         let _ = this._getCacheKey(K);
-         return (this._inMemoryCache.add(_, $), this._writeToCache(_, $), $);
-       });
-     }
-     _getSdkKey() {
-       if (this._sdkKey != null) return this._sdkKey;
-       return (
-         RW1.Log.error(`${this._adapterName} is not attached to a Client`),
-         ""
-       );
-     }
-     _loadFromCache(A) {
-       var K;
-       let q =
-         (K = ds.Storage.getItem) === null || K === void 0
-           ? void 0
-           : K.call(ds.Storage, A);
-       if (q == null) return null;
-       let Y = (0, SS7._typedJsonParse)(q, "source", "Cached Result");
-       return Y
-         ? Object.assign(Object.assign({}, Y), { source: "Cache" })
-         : null;
-     }
-     _writeToCache(A, K) {
-       (ds.Storage.setItem(A, JSON.stringify(K)),
-         this._runLocalStorageCacheEviction(A));
-     }
-     _runLocalStorageCacheEviction(A) {
-       var K;
-       let q =
-         (K = (0, ds._getObjectFromStorage)(this._lastModifiedStoreKey)) !==
-           null && K !== void 0
-           ? K
-           : {};
-       q[A] = Date.now();
-       let Y = uS7(q, hS7);
-       if (Y) (delete q[Y], ds.Storage.removeItem(Y));
-       (0, ds._setObjectInStorage)(this._lastModifiedStoreKey, q);
-     }
-   }
-   cs.DataAdapterCore = bS7;
-   function IW1(A, K, q, Y) {
-     return {
-       source: A,
-       data: K,
-       receivedAt: Date.now(),
-       stableID: q,
-       fullUserHash: (0, yW1._getFullUserHash)(Y),
-     };
-   }
-   cs._makeDataAdapterResult = IW1;
-   class xS7 {
-     constructor() {
-       this._data = {};
-     }
-     get(A, K) {
-       var q;
-       let Y = this._data[A],
-         z = Y === null || Y === void 0 ? void 0 : Y.stableID,
-         w =
-           (q = K === null || K === void 0 ? void 0 : K.customIDs) === null ||
-           q === void 0
-             ? void 0
-             : q.stableID;
-       if (w && z && w !== z)
-         return (
-           RW1.Log.warn("'StatsigUser.customIDs.stableID' mismatch"),
-           null
-         );
-       return Y;
-     }
-     add(A, K) {
-       let q = uS7(this._data, hS7 - 1);
-       if (q) delete this._data[q];
-       this._data[A] = K;
-     }
-     merge(A) {
-       this._data = Object.assign(Object.assign({}, this._data), A);
-     }
-   }
-   function uS7(A, K) {
-     let q = Object.keys(A);
-     if (q.length <= K) return null;
-     return q.reduce((Y, z) => {
-       let w = A[Y],
-         H = A[z];
-       if (typeof w === "object" && typeof H === "object")
-         return H.receivedAt < w.receivedAt ? z : Y;
-       return H < w ? z : Y;
-     });
-   }
- });

--- Removed SW1 (pretty-v2.1.25.js:342964-342984)
- var SW1 = v((QS7) => {
-   Object.defineProperty(QS7, "__esModule", { value: !0 });
-   QS7.SDKType = void 0;
-   var FS7 = {},
-     SDA;
-   QS7.SDKType = {
-     _get: (A) => {
-       var K;
-       return (
-         ((K = FS7[A]) !== null && K !== void 0 ? K : "js-mono") +
-         (SDA !== null && SDA !== void 0 ? SDA : "")
-       );
-     },
-     _setClientType(A, K) {
-       FS7[A] = K;
-     },
-     _setBindingType(A) {
-       if (!SDA || SDA === "-react") SDA = "-" + A;
-     },
-   };
- });

--- Removed oT6 (pretty-v2.1.25.js:342985-343160)
- var oT6 = v((op) => {
-   var AsY =
-     (op && op.__awaiter) ||
-     function (A, K, q, Y) {
-       function z(w) {
-         return w instanceof q
-           ? w
-           : new q(function (H) {
-               H(w);
-             });
-       }
-       return new (q || (q = Promise))(function (w, H) {
-         function J($) {
-           try {
-             X(Y.next($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function O($) {
-           try {
-             X(Y.throw($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function X($) {
-           $.done ? w($.value) : z($.value).then(J, O);
-         }
-         X((Y = Y.apply(A, K || [])).next());
-       });
-     };
-   Object.defineProperty(op, "__esModule", { value: !0 });
-   op.ErrorBoundary = op.EXCEPTION_ENDPOINT = void 0;
-   var KsY = Xj(),
-     qsY = SW1(),
-     YsY = NgA();
-   op.EXCEPTION_ENDPOINT = "https://statsigapi.net/v1/sdk_exception";
-   var dS7 = "[Statsig] UnknownError";
-   class cS7 {
-     constructor(A, K, q, Y) {
-       ((this._sdkKey = A),
-         (this._options = K),
-         (this._emitter = q),
-         (this._lastSeenError = Y),
-         (this._seen = new Set()));
-     }
-     wrap(A) {
-       try {
-         let K = A;
-         wsY(K).forEach((q) => {
-           let Y = K[q];
-           if ("$EB" in Y) return;
-           ((K[q] = (...z) => {
-             return this._capture(q, () => Y.apply(A, z));
-           }),
-             (K[q].$EB = !0));
-         });
-       } catch (K) {
-         this._onError("eb:wrap", K);
-       }
-     }
-     logError(A, K) {
-       this._onError(A, K);
-     }
-     getLastSeenErrorAndReset() {
-       let A = this._lastSeenError;
-       return (
-         (this._lastSeenError = void 0),
-         A !== null && A !== void 0 ? A : null
-       );
-     }
-     attachErrorIfNoneExists(A) {
-       if (this._lastSeenError) return;
-       this._lastSeenError = pS7(A);
-     }
-     _capture(A, K) {
-       try {
-         let q = K();
-         if (q && q instanceof Promise)
-           return q.catch((Y) => this._onError(A, Y));
-         return q;
-       } catch (q) {
-         return (this._onError(A, q), null);
-       }
-     }
-     _onError(A, K) {
-       try {
-         (KsY.Log.warn(`Caught error in ${A}`, { error: K }),
-           (() =>
-             AsY(this, void 0, void 0, function* () {
-               var Y, z, w, H, J, O, X;
-               let $ = K ? K : Error(dS7),
-                 _ = $ instanceof Error,
-                 G = _ ? $.name : "No Name",
-                 Z = pS7($);
-               if (((this._lastSeenError = Z), this._seen.has(G))) return;
-               if (
-                 (this._seen.add(G),
-                 (z =
-                   (Y = this._options) === null || Y === void 0
-                     ? void 0
-                     : Y.networkConfig) === null || z === void 0
-                   ? void 0
-                   : z.preventAllNetworkTraffic)
-               ) {
-                 (w = this._emitter) === null ||
-                   w === void 0 ||
-                   w.call(this, { name: "error", error: K, tag: A });
-                 return;
-               }
-               let W = qsY.SDKType._get(this._sdkKey),
-                 D = YsY.StatsigMetadataProvider.get(),
-                 j = _ ? $.stack : zsY($),
-                 M = JSON.stringify(
-                   Object.assign(
-                     { tag: A, exception: G, info: j },
-                     Object.assign(Object.assign({}, D), { sdkType: W }),
-                   ),
-                 );
-               (yield (
-                 (O =
-                   (J =
-                     (H = this._options) === null || H === void 0
-                       ? void 0
-                       : H.networkConfig) === null || J === void 0
-                     ? void 0
-                     : J.networkOverrideFunc) !== null && O !== void 0
-                   ? O
-                   : fetch
-               )(op.EXCEPTION_ENDPOINT, {
-                 method: "POST",
-                 headers: {
-                   "STATSIG-API-KEY": this._sdkKey,
-                   "STATSIG-SDK-TYPE": String(W),
-                   "STATSIG-SDK-VERSION": String(D.sdkVersion),
-                   "Content-Type": "application/json",
-                 },
-                 body: M,
-               }),
-                 (X = this._emitter) === null ||
-                   X === void 0 ||
-                   X.call(this, { name: "error", error: K, tag: A }));
-             }))()
-             .then(() => {})
-             .catch(() => {}));
-       } catch (q) {}
-     }
-   }
-   op.ErrorBoundary = cS7;
-   function pS7(A) {
-     if (A instanceof Error) return A;
-     else if (typeof A === "string") return Error(A);
-     else return Error("An unknown error occurred.");
-   }
-   function zsY(A) {
-     try {
-       return JSON.stringify(A);
-     } catch (K) {
-       return dS7;
-     }
-   }
-   function wsY(A) {
-     let K = new Set(),
-       q = Object.getPrototypeOf(A);
-     while (q && q !== Object.prototype)
-       (Object.getOwnPropertyNames(q)
-         .filter(
-           (Y) =>
-             typeof (q === null || q === void 0 ? void 0 : q[Y]) === "function",
-         )
-         .forEach((Y) => K.add(Y)),
-         (q = Object.getPrototypeOf(q)));
-     return Array.from(K);
-   }
- });

--- Removed aS7 (pretty-v2.1.25.js:343167-343169)
- var aS7 = v((oS7) => {
-   Object.defineProperty(oS7, "__esModule", { value: !0 });
- });

--- Removed aT6 (pretty-v2.1.25.js:343170-343193)
- var aT6 = v((sS7) => {
-   Object.defineProperty(sS7, "__esModule", { value: !0 });
-   sS7.createMemoKey = sS7.MemoPrefix = void 0;
-   sS7.MemoPrefix = {
-     _gate: "g",
-     _dynamicConfig: "c",
-     _experiment: "e",
-     _layer: "l",
-     _paramStore: "p",
-   };
-   var HsY = new Set([]),
-     JsY = new Set(["userPersistedValues"]);
-   function OsY(A, K, q) {
-     let Y = `${A}|${K}`;
-     if (!q) return Y;
-     for (let z of Object.keys(q)) {
-       if (JsY.has(z)) return;
-       if (HsY.has(z)) Y += `|${z}=true`;
-       else Y += `|${z}=${q[z]}`;
-     }
-     return Y;
-   }
-   sS7.createMemoKey = OsY;
- });

--- Removed eS7 (pretty-v2.1.25.js:343194-343270)
- var eS7 = v((hDA) => {
-   var $sY =
-     (hDA && hDA.__awaiter) ||
-     function (A, K, q, Y) {
-       function z(w) {
-         return w instanceof q
-           ? w
-           : new q(function (H) {
-               H(w);
-             });
-       }
-       return new (q || (q = Promise))(function (w, H) {
-         function J($) {
-           try {
-             X(Y.next($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function O($) {
-           try {
-             X(Y.throw($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function X($) {
-           $.done ? w($.value) : z($.value).then(J, O);
-         }
-         X((Y = Y.apply(A, K || [])).next());
-       });
-     };
-   Object.defineProperty(hDA, "__esModule", { value: !0 });
-   hDA._fetchTxtRecords = void 0;
-   var _sY = new Uint8Array([
-       0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 13, 102, 101, 97, 116, 117, 114, 101,
-       97, 115, 115, 101, 116, 115, 3, 111, 114, 103, 0, 0, 16, 0, 1,
-     ]),
-     GsY = "https://cloudflare-dns.com/dns-query",
-     ZsY = ["i", "e", "d"],
-     WsY = 200;
-   function DsY(A) {
-     return $sY(this, void 0, void 0, function* () {
-       let K = yield A(GsY, {
-         method: "POST",
-         headers: {
-           "Content-Type": "application/dns-message",
-           Accept: "application/dns-message",
-         },
-         body: _sY,
-       });
-       if (!K.ok) {
-         let z = Error("Failed to fetch TXT records from DNS");
-         throw ((z.name = "DnsTxtFetchError"), z);
-       }
-       let q = yield K.arrayBuffer(),
-         Y = new Uint8Array(q);
-       return jsY(Y);
-     });
-   }
-   hDA._fetchTxtRecords = DsY;
-   function jsY(A) {
-     let K = A.findIndex(
-       (Y, z) =>
-         z < WsY &&
-         String.fromCharCode(Y) === "=" &&
-         ZsY.includes(String.fromCharCode(A[z - 1])),
-     );
-     if (K === -1) {
-       let Y = Error("Failed to parse TXT records from DNS");
-       throw ((Y.name = "DnsTxtParseError"), Y);
-     }
-     let q = "";
-     for (let Y = K - 1; Y < A.length; Y++) q += String.fromCharCode(A[Y]);
-     return q.split(",");
-   }
- });

--- Removed Hh7 (pretty-v2.1.25.js:343271-343501)
- var Hh7 = v((ls) => {
-   var Ah7 =
-     (ls && ls.__awaiter) ||
-     function (A, K, q, Y) {
-       function z(w) {
-         return w instanceof q
-           ? w
-           : new q(function (H) {
-               H(w);
-             });
-       }
-       return new (q || (q = Promise))(function (w, H) {
-         function J($) {
-           try {
-             X(Y.next($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function O($) {
-           try {
-             X(Y.throw($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function X($) {
-           $.done ? w($.value) : z($.value).then(J, O);
-         }
-         X((Y = Y.apply(A, K || [])).next());
-       });
-     };
-   Object.defineProperty(ls, "__esModule", { value: !0 });
-   ls._isDomainFailure = ls.NetworkFallbackResolver = void 0;
-   var MsY = eS7(),
-     PsY = CDA(),
-     VsY = Xj(),
-     tT6 = rp(),
-     Kh7 = 604800000,
-     fsY = 14400000;
-   class Yh7 {
-     constructor(A) {
-       var K;
-       ((this._fallbackInfo = null),
-         (this._errorBoundary = null),
-         (this._dnsQueryCooldowns = {}),
-         (this._networkOverrideFunc =
-           (K = A.networkConfig) === null || K === void 0
-             ? void 0
-             : K.networkOverrideFunc));
-     }
-     setErrorBoundary(A) {
-       this._errorBoundary = A;
-     }
-     tryBumpExpiryTime(A, K) {
-       var q;
-       let Y =
-         (q = this._fallbackInfo) === null || q === void 0
-           ? void 0
-           : q[K.endpoint];
-       if (!Y) return;
-       ((Y.expiryTime = Date.now() + Kh7),
-         sT6(
-           A,
-           Object.assign(Object.assign({}, this._fallbackInfo), {
-             [K.endpoint]: Y,
-           }),
-         ));
-     }
-     getActiveFallbackUrl(A, K) {
-       var q, Y;
-       let z = this._fallbackInfo;
-       if (z == null)
-         ((z = (q = NsY(A)) !== null && q !== void 0 ? q : {}),
-           (this._fallbackInfo = z));
-       let w = z[K.endpoint];
-       if (
-         !w ||
-         Date.now() > ((Y = w.expiryTime) !== null && Y !== void 0 ? Y : 0)
-       )
-         return (
-           delete z[K.endpoint],
-           (this._fallbackInfo = z),
-           sT6(A, this._fallbackInfo),
-           null
-         );
-       if (w.url) return w.url;
-       return null;
-     }
-     getFallbackFromProvided(A) {
-       let K = qh7(A);
-       if (K) return A.replace(K, "");
-       return null;
-     }
-     tryFetchUpdatedFallbackInfo(A, K, q, Y) {
-       var z, w;
-       return Ah7(this, void 0, void 0, function* () {
-         try {
-           if (!zh7(q, Y)) return !1;
-           let J =
-               K.customUrl == null && K.fallbackUrls == null
-                 ? yield this._tryFetchFallbackUrlsFromNetwork(K)
-                 : K.fallbackUrls,
-             O = this._pickNewFallbackUrl(
-               (z = this._fallbackInfo) === null || z === void 0
-                 ? void 0
-                 : z[K.endpoint],
-               J,
-             );
-           if (!O) return !1;
-           return (this._updateFallbackInfoWithNewUrl(A, K.endpoint, O), !0);
-         } catch (H) {
-           return (
-             (w = this._errorBoundary) === null ||
-               w === void 0 ||
-               w.logError("tryFetchUpdatedFallbackInfo", H),
-             !1
-           );
-         }
-       });
-     }
-     _updateFallbackInfoWithNewUrl(A, K, q) {
-       var Y, z, w;
-       let H = { url: q, expiryTime: Date.now() + Kh7, previous: [] },
-         J = (Y = this._fallbackInfo) === null || Y === void 0 ? void 0 : Y[K];
-       if (J) H.previous.push(...J.previous);
-       if (H.previous.length > 10) H.previous = [];
-       let O =
-         (w =
-           (z = this._fallbackInfo) === null || z === void 0 ? void 0 : z[K]) ===
-           null || w === void 0
-           ? void 0
-           : w.url;
-       if (O != null) H.previous.push(O);
-       ((this._fallbackInfo = Object.assign(
-         Object.assign({}, this._fallbackInfo),
-         { [K]: H },
-       )),
-         sT6(A, this._fallbackInfo));
-     }
-     _tryFetchFallbackUrlsFromNetwork(A) {
-       var K;
-       return Ah7(this, void 0, void 0, function* () {
-         let q = this._dnsQueryCooldowns[A.endpoint];
-         if (q && Date.now() < q) return null;
-         this._dnsQueryCooldowns[A.endpoint] = Date.now() + fsY;
-         let Y = [],
-           z = yield (0, MsY._fetchTxtRecords)(
-             (K = this._networkOverrideFunc) !== null && K !== void 0
-               ? K
-               : fetch,
-           ),
-           w = qh7(A.defaultUrl);
-         for (let H of z) {
-           if (!H.startsWith(A.endpointDnsKey + "=")) continue;
-           let J = H.split("=");
-           if (J.length > 1) {
-             let O = J[1];
-             if (O.endsWith("/")) O = O.slice(0, -1);
-             Y.push(`https://${O}${w}`);
-           }
-         }
-         return Y;
-       });
-     }
-     _pickNewFallbackUrl(A, K) {
-       var q;
-       if (K == null) return null;
-       let Y = new Set(
-           (q = A === null || A === void 0 ? void 0 : A.previous) !== null &&
-           q !== void 0
-             ? q
-             : [],
-         ),
-         z = A === null || A === void 0 ? void 0 : A.url,
-         w = null;
-       for (let H of K) {
-         let J = H.endsWith("/") ? H.slice(0, -1) : H;
-         if (!Y.has(H) && J !== z) {
-           w = J;
-           break;
-         }
-       }
-       return w;
-     }
-   }
-   ls.NetworkFallbackResolver = Yh7;
-   function zh7(A, K) {
-     var q;
-     let Y =
-       (q = A === null || A === void 0 ? void 0 : A.toLowerCase()) !== null &&
-       q !== void 0
-         ? q
-         : "";
-     return (
-       K ||
-       Y.includes("uncaught exception") ||
-       Y.includes("failed to fetch") ||
-       Y.includes("networkerror when attempting to fetch resource")
-     );
-   }
-   ls._isDomainFailure = zh7;
-   function wh7(A) {
-     return `statsig.network_fallback.${(0, PsY._DJB2)(A)}`;
-   }
-   function sT6(A, K) {
-     let q = wh7(A);
-     if (!K || Object.keys(K).length === 0) {
-       tT6.Storage.removeItem(q);
-       return;
-     }
-     tT6.Storage.setItem(q, JSON.stringify(K));
-   }
-   function NsY(A) {
-     let K = wh7(A),
-       q = tT6.Storage.getItem(K);
-     if (!q) return null;
-     try {
-       return JSON.parse(q);
-     } catch (Y) {
-       return (VsY.Log.error("Failed to parse FallbackInfo"), null);
-     }
-   }
-   function qh7(A) {
-     try {
-       return new URL(A).pathname;
-     } catch (K) {
-       return null;
-     }
-   }
- });

--- Removed eT6 (pretty-v2.1.25.js:343502-343518)
- var eT6 = v((Oh7) => {
-   Object.defineProperty(Oh7, "__esModule", { value: !0 });
-   Oh7.SDKFlags = void 0;
-   var Jh7 = {};
-   Oh7.SDKFlags = {
-     setFlags: (A, K) => {
-       Jh7[A] = K;
-     },
-     get: (A, K) => {
-       var q, Y;
-       return (Y = (q = Jh7[A]) === null || q === void 0 ? void 0 : q[K]) !==
-         null && Y !== void 0
-         ? Y
-         : !1;
-     },
-   };
- });

--- Removed bW1 (pretty-v2.1.25.js:343519-343601)
- var bW1 = v((jh7) => {
-   Object.defineProperty(jh7, "__esModule", { value: !0 });
-   jh7.StatsigSession = jh7.SessionID = void 0;
-   var TsY = jgA(),
-     vsY = Xj(),
-     _h7 = rp(),
-     Gh7 = kW1(),
-     Zh7 = 1800000,
-     Wh7 = 14400000,
-     hW1 = {};
-   jh7.SessionID = {
-     get: (A) => {
-       return jh7.StatsigSession.get(A).data.sessionID;
-     },
-   };
-   jh7.StatsigSession = {
-     get: (A) => {
-       if (hW1[A] == null) hW1[A] = EsY(A);
-       let K = hW1[A];
-       return CsY(K);
-     },
-     overrideInitialSessionID: (A, K) => {
-       hW1[K] = ksY(A, K);
-     },
-   };
-   function EsY(A) {
-     let K = IsY(A),
-       q = Date.now();
-     if (!K) K = { sessionID: (0, Gh7.getUUID)(), startTime: q, lastUpdate: q };
-     return { data: K, sdkKey: A };
-   }
-   function ksY(A, K) {
-     let q = Date.now();
-     return { data: { sessionID: A, startTime: q, lastUpdate: q }, sdkKey: K };
-   }
-   function CsY(A) {
-     let K = Date.now(),
-       q = A.data;
-     if (LsY(q) || RsY(q))
-       ((q.sessionID = (0, Gh7.getUUID)()), (q.startTime = K));
-     ((q.lastUpdate = K),
-       ysY(q, A.sdkKey),
-       clearTimeout(A.idleTimeoutID),
-       clearTimeout(A.ageTimeoutID));
-     let Y = K - q.startTime,
-       z = A.sdkKey;
-     return (
-       (A.idleTimeoutID = $h7(z, Zh7)),
-       (A.ageTimeoutID = $h7(z, Wh7 - Y)),
-       A
-     );
-   }
-   function $h7(A, K) {
-     return setTimeout(() => {
-       let q =
-         __STATSIG__ === null || __STATSIG__ === void 0
-           ? void 0
-           : __STATSIG__.instance(A);
-       if (q) q.$emt({ name: "session_expired" });
-     }, K);
-   }
-   function LsY({ lastUpdate: A }) {
-     return Date.now() - A > Zh7;
-   }
-   function RsY({ startTime: A }) {
-     return Date.now() - A > Wh7;
-   }
-   function Dh7(A) {
-     return `statsig.session_id.${(0, TsY._getStorageKey)(A)}`;
-   }
-   function ysY(A, K) {
-     let q = Dh7(K);
-     try {
-       (0, _h7._setObjectInStorage)(q, A);
-     } catch (Y) {
-       vsY.Log.warn("Failed to save SessionID");
-     }
-   }
-   function IsY(A) {
-     let K = Dh7(A);
-     return (0, _h7._getObjectFromStorage)(K);
-   }
- });

--- Removed Kv6 (pretty-v2.1.25.js:343602-343606)
- var Kv6 = v((Mh7) => {
-   Object.defineProperty(Mh7, "__esModule", { value: !0 });
-   Mh7.ErrorTag = void 0;
-   Mh7.ErrorTag = { NetworkError: "NetworkError" };
- });

--- Removed Lh7 (pretty-v2.1.25.js:343607-344006)
- var Lh7 = v((xDA) => {
-   var bDA =
-     (xDA && xDA.__awaiter) ||
-     function (A, K, q, Y) {
-       function z(w) {
-         return w instanceof q
-           ? w
-           : new q(function (H) {
-               H(w);
-             });
-       }
-       return new (q || (q = Promise))(function (w, H) {
-         function J($) {
-           try {
-             X(Y.next($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function O($) {
-           try {
-             X(Y.throw($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function X($) {
-           $.done ? w($.value) : z($.value).then(J, O);
-         }
-         X((Y = Y.apply(A, K || [])).next());
-       });
-     };
-   Object.defineProperty(xDA, "__esModule", { value: !0 });
-   xDA.NetworkCore = void 0;
-   y5A();
-   var Vh7 = y5A(),
-     qv6 = GW1(),
-     h5A = Xj(),
-     _S = MgA(),
-     hsY = Hh7(),
-     bsY = eT6(),
-     Th7 = SW1(),
-     xsY = I5A(),
-     vh7 = bW1(),
-     usY = LW1(),
-     BsY = Kv6(),
-     Eh7 = NgA(),
-     msY = vW1(),
-     gsY = 1e4,
-     FsY = 500,
-     QsY = 30000,
-     UsY = 1000,
-     kh7 = 50,
-     psY = kh7 / UsY,
-     dsY = new Set([408, 500, 502, 503, 504, 522, 524, 599]);
-   class Ch7 {
-     constructor(A, K) {
-       if (
-         ((this._emitter = K),
-         (this._errorBoundary = null),
-         (this._timeout = gsY),
-         (this._netConfig = {}),
-         (this._options = {}),
-         (this._leakyBucket = {}),
-         (this._lastUsedInitUrl = null),
-         A)
-       )
-         this._options = A;
-       if (this._options.networkConfig)
-         this._netConfig = this._options.networkConfig;
-       if (this._netConfig.networkTimeoutMs)
-         this._timeout = this._netConfig.networkTimeoutMs;
-       this._fallbackResolver = new hsY.NetworkFallbackResolver(this._options);
-     }
-     setErrorBoundary(A) {
-       ((this._errorBoundary = A),
-         this._errorBoundary.wrap(this),
-         this._errorBoundary.wrap(this._fallbackResolver),
-         this._fallbackResolver.setErrorBoundary(A));
-     }
-     isBeaconSupported() {
-       return (
-         typeof navigator < "u" && typeof navigator.sendBeacon === "function"
-       );
-     }
-     getLastUsedInitUrlAndReset() {
-       let A = this._lastUsedInitUrl;
-       return ((this._lastUsedInitUrl = null), A);
-     }
-     beacon(A) {
-       return bDA(this, void 0, void 0, function* () {
-         if (!fh7(A)) return !1;
-         let K = this._getInternalRequestArgs("POST", A);
-         yield this._tryToCompressBody(K);
-         let q = yield this._getPopulatedURL(K),
-           Y = navigator;
-         return Y.sendBeacon.bind(Y)(q, K.body);
-       });
-     }
-     post(A) {
-       return bDA(this, void 0, void 0, function* () {
-         let K = this._getInternalRequestArgs("POST", A);
-         return (
-           this._tryEncodeBody(K),
-           yield this._tryToCompressBody(K),
-           this._sendRequest(K)
-         );
-       });
-     }
-     get(A) {
-       let K = this._getInternalRequestArgs("GET", A);
-       return this._sendRequest(K);
-     }
-     _sendRequest(A) {
-       var K, q, Y, z;
-       return bDA(this, void 0, void 0, function* () {
-         if (!fh7(A)) return null;
-         if (this._netConfig.preventAllNetworkTraffic) return null;
-         let { method: w, body: H, retries: J, attempt: O } = A,
-           X = A.urlConfig.endpoint;
-         if (this._isRateLimited(X))
-           return (
-             h5A.Log.warn(
-               `Request to ${X} was blocked because you are making requests too frequently.`,
-             ),
-             null
-           );
-         let $ = O !== null && O !== void 0 ? O : 1,
-           _ = typeof AbortController < "u" ? new AbortController() : null,
-           G = setTimeout(() => {
-             _ === null ||
-               _ === void 0 ||
-               _.abort(`Timeout of ${this._timeout}ms expired.`);
-           }, this._timeout),
-           Z = yield this._getPopulatedURL(A),
-           W = null,
-           D = (0, msY._isUnloading)();
-         try {
-           let j = {
-             method: w,
-             body: H,
-             headers: Object.assign({}, A.headers),
-             signal: _ === null || _ === void 0 ? void 0 : _.signal,
-             priority: A.priority,
-             keepalive: D,
-           };
-           nsY(A, $);
-           let M = this._leakyBucket[X];
-           if (M) ((M.lastRequestTime = Date.now()), (this._leakyBucket[X] = M));
-           if (
-             ((W = yield (
-               (K = this._netConfig.networkOverrideFunc) !== null && K !== void 0
-                 ? K
-                 : fetch
-             )(Z, j)),
-             clearTimeout(G),
-             !W.ok)
-           ) {
-             let N = yield W.text().catch(() => "No Text"),
-               T = Error(`NetworkError: ${Z} ${N}`);
-             throw ((T.name = "NetworkError"), T);
-           }
-           let f = yield W.text();
-           return (
-             Nh7(A, W, $, f),
-             this._fallbackResolver.tryBumpExpiryTime(A.sdkKey, A.urlConfig),
-             { body: f, code: W.status }
-           );
-         } catch (j) {
-           let M = lsY(_, j),
-             P = isY(_);
-           if (
-             (Nh7(A, W, $, "", j),
-             yield this._fallbackResolver.tryFetchUpdatedFallbackInfo(
-               A.sdkKey,
-               A.urlConfig,
-               M,
-               P,
-             ))
-           )
-             A.fallbackUrl = this._fallbackResolver.getActiveFallbackUrl(
-               A.sdkKey,
-               A.urlConfig,
-             );
-           if (
-             !J ||
-             $ > J ||
-             !dsY.has(
-               (q = W === null || W === void 0 ? void 0 : W.status) !== null &&
-                 q !== void 0
-                 ? q
-                 : 500,
-             )
-           ) {
-             (Y = this._emitter) === null ||
-               Y === void 0 ||
-               Y.call(this, {
-                 name: "error",
-                 error: j,
-                 tag: BsY.ErrorTag.NetworkError,
-                 requestArgs: A,
-               });
-             let N = `A networking error occurred during ${w} request to ${Z}.`;
-             return (
-               h5A.Log.error(N, M, j),
-               (z = this._errorBoundary) === null ||
-                 z === void 0 ||
-                 z.attachErrorIfNoneExists(N),
-               null
-             );
-           }
-           return (
-             yield rsY($),
-             this._sendRequest(
-               Object.assign(Object.assign({}, A), {
-                 retries: J,
-                 attempt: $ + 1,
-               }),
-             )
-           );
-         }
-       });
-     }
-     _isRateLimited(A) {
-       var K;
-       let q = Date.now(),
-         Y =
-           (K = this._leakyBucket[A]) !== null && K !== void 0
-             ? K
-             : { count: 0, lastRequestTime: q },
-         z = q - Y.lastRequestTime,
-         w = Math.floor(z * psY);
-       if (((Y.count = Math.max(0, Y.count - w)), Y.count >= kh7)) return !0;
-       return (
-         (Y.count += 1),
-         (Y.lastRequestTime = q),
-         (this._leakyBucket[A] = Y),
-         !1
-       );
-     }
-     _getPopulatedURL(A) {
-       var K;
-       return bDA(this, void 0, void 0, function* () {
-         let q =
-           (K = A.fallbackUrl) !== null && K !== void 0
-             ? K
-             : A.urlConfig.getUrl();
-         if (
-           A.urlConfig.endpoint === _S.Endpoint._initialize ||
-           A.urlConfig.endpoint === _S.Endpoint._download_config_specs
-         )
-           this._lastUsedInitUrl = q;
-         let Y = Object.assign(
-             {
-               [_S.NetworkParam.SdkKey]: A.sdkKey,
-               [_S.NetworkParam.SdkType]: Th7.SDKType._get(A.sdkKey),
-               [_S.NetworkParam.SdkVersion]: Eh7.SDK_VERSION,
-               [_S.NetworkParam.Time]: String(Date.now()),
-               [_S.NetworkParam.SessionID]: vh7.SessionID.get(A.sdkKey),
-             },
-             A.params,
-           ),
-           z = Object.keys(Y)
-             .map((w) => {
-               return `${encodeURIComponent(w)}=${encodeURIComponent(Y[w])}`;
-             })
-             .join("&");
-         return `${q}${z ? `?${z}` : ""}`;
-       });
-     }
-     _tryEncodeBody(A) {
-       var K;
-       let q = (0, xsY._getWindowSafe)(),
-         Y = A.body;
-       if (
-         !A.isStatsigEncodable ||
-         this._options.disableStatsigEncoding ||
-         typeof Y !== "string" ||
-         (0, Vh7._getStatsigGlobalFlag)("no-encode") != null ||
-         !(q === null || q === void 0 ? void 0 : q.btoa)
-       )
-         return;
-       try {
-         ((A.body = q.btoa(Y).split("").reverse().join("")),
-           (A.params = Object.assign(
-             Object.assign({}, (K = A.params) !== null && K !== void 0 ? K : {}),
-             { [_S.NetworkParam.StatsigEncoded]: "1" },
-           )));
-       } catch (z) {
-         h5A.Log.warn(`Request encoding failed for ${A.urlConfig.getUrl()}`, z);
-       }
-     }
-     _tryToCompressBody(A) {
-       var K;
-       return bDA(this, void 0, void 0, function* () {
-         let q = A.body;
-         if (
-           !A.isCompressable ||
-           this._options.disableCompression ||
-           typeof q !== "string" ||
-           bsY.SDKFlags.get(A.sdkKey, "enable_log_event_compression") !== !0 ||
-           (0, Vh7._getStatsigGlobalFlag)("no-compress") != null ||
-           typeof CompressionStream > "u" ||
-           typeof TextEncoder > "u"
-         )
-           return;
-         try {
-           let Y = new TextEncoder().encode(q),
-             z = new CompressionStream("gzip"),
-             w = z.writable.getWriter();
-           (w.write(Y).catch(h5A.Log.error), w.close().catch(h5A.Log.error));
-           let H = z.readable.getReader(),
-             J = [],
-             O;
-           while (!(O = yield H.read()).done) J.push(O.value);
-           let X = J.reduce((G, Z) => G + Z.length, 0),
-             $ = new Uint8Array(X),
-             _ = 0;
-           for (let G of J) ($.set(G, _), (_ += G.length));
-           ((A.body = $),
-             (A.params = Object.assign(
-               Object.assign(
-                 {},
-                 (K = A.params) !== null && K !== void 0 ? K : {},
-               ),
-               { [_S.NetworkParam.IsGzipped]: "1" },
-             )));
-         } catch (Y) {
-           h5A.Log.warn(
-             `Request compression failed for ${A.urlConfig.getUrl()}`,
-             Y,
-           );
-         }
-       });
-     }
-     _getInternalRequestArgs(A, K) {
-       let q = this._fallbackResolver.getActiveFallbackUrl(
-           K.sdkKey,
-           K.urlConfig,
-         ),
-         Y = Object.assign(Object.assign({}, K), { method: A, fallbackUrl: q });
-       if ("data" in K) csY(Y, K.data);
-       return Y;
-     }
-   }
-   xDA.NetworkCore = Ch7;
-   var fh7 = (A) => {
-       if (!A.sdkKey)
-         return (h5A.Log.warn("Unable to make request without an SDK key"), !1);
-       return !0;
-     },
-     csY = (A, K) => {
-       let { sdkKey: q, fallbackUrl: Y } = A,
-         z = usY.StableID.get(q),
-         w = vh7.SessionID.get(q),
-         H = Th7.SDKType._get(q);
-       A.body = JSON.stringify(
-         Object.assign(Object.assign({}, K), {
-           statsigMetadata: Object.assign(
-             Object.assign({}, Eh7.StatsigMetadataProvider.get()),
-             { stableID: z, sessionID: w, sdkType: H, fallbackUrl: Y },
-           ),
-         }),
-       );
-     };
-   function lsY(A, K) {
-     if (
-       (A === null || A === void 0 ? void 0 : A.signal.aborted) &&
-       typeof A.signal.reason === "string"
-     )
-       return A.signal.reason;
-     if (typeof K === "string") return K;
-     if (K instanceof Error) return `${K.name}: ${K.message}`;
-     return "Unknown Error";
-   }
-   function isY(A) {
-     return (
-       ((A === null || A === void 0 ? void 0 : A.signal.aborted) &&
-         typeof A.signal.reason === "string" &&
-         A.signal.reason.includes("Timeout")) ||
-       !1
-     );
-   }
-   function nsY(A, K) {
-     if (A.urlConfig.endpoint !== _S.Endpoint._initialize) return;
-     qv6.Diagnostics._markInitNetworkReqStart(A.sdkKey, { attempt: K });
-   }
-   function Nh7(A, K, q, Y, z) {
-     if (A.urlConfig.endpoint !== _S.Endpoint._initialize) return;
-     qv6.Diagnostics._markInitNetworkReqEnd(
-       A.sdkKey,
-       qv6.Diagnostics._getDiagnosticsData(K, q, Y, z),
-     );
-   }
-   function rsY(A) {
-     return bDA(this, void 0, void 0, function* () {
-       yield new Promise((K) => setTimeout(K, Math.min(FsY * (A * A), QsY)));
-     });
-   }
- });

--- Removed yh7 (pretty-v2.1.25.js:344007-344009)
- var yh7 = v((Rh7) => {
-   Object.defineProperty(Rh7, "__esModule", { value: !0 });
- });

--- Removed Sh7 (pretty-v2.1.25.js:344010-344012)
- var Sh7 = v((Ih7) => {
-   Object.defineProperty(Ih7, "__esModule", { value: !0 });
- });

--- Removed bh7 (pretty-v2.1.25.js:344013-344182)
- var bh7 = v((uDA) => {
-   var osY =
-     (uDA && uDA.__awaiter) ||
-     function (A, K, q, Y) {
-       function z(w) {
-         return w instanceof q
-           ? w
-           : new q(function (H) {
-               H(w);
-             });
-       }
-       return new (q || (q = Promise))(function (w, H) {
-         function J($) {
-           try {
-             X(Y.next($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function O($) {
-           try {
-             X(Y.throw($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function X($) {
-           $.done ? w($.value) : z($.value).then(J, O);
-         }
-         X((Y = Y.apply(A, K || [])).next());
-       });
-     };
-   Object.defineProperty(uDA, "__esModule", { value: !0 });
-   uDA.StatsigClientBase = void 0;
-   y5A();
-   var asY = y5A(),
-     ssY = oT6(),
-     tsY = cT6(),
-     Yv6 = Xj(),
-     esY = aT6(),
-     AtY = I5A(),
-     KtY = bW1(),
-     xW1 = rp(),
-     qtY = 3000;
-   class hh7 {
-     constructor(A, K, q, Y) {
-       var z;
-       ((this.loadingStatus = "Uninitialized"),
-         (this._initializePromise = null),
-         (this._listeners = {}));
-       let w = this.$emt.bind(this);
-       ((Y === null || Y === void 0 ? void 0 : Y.logLevel) != null &&
-         (Yv6.Log.level = Y.logLevel),
-         (Y === null || Y === void 0 ? void 0 : Y.disableStorage) &&
-           xW1.Storage._setDisabled(!0),
-         (Y === null || Y === void 0 ? void 0 : Y.initialSessionID) &&
-           KtY.StatsigSession.overrideInitialSessionID(Y.initialSessionID, A),
-         (Y === null || Y === void 0 ? void 0 : Y.storageProvider) &&
-           xW1.Storage._setProvider(Y.storageProvider),
-         (this._sdkKey = A),
-         (this._options = Y !== null && Y !== void 0 ? Y : {}),
-         (this._memoCache = {}),
-         (this.overrideAdapter =
-           (z = Y === null || Y === void 0 ? void 0 : Y.overrideAdapter) !==
-             null && z !== void 0
-             ? z
-             : null),
-         (this._logger = new tsY.EventLogger(A, w, q, Y)),
-         (this._errorBoundary = new ssY.ErrorBoundary(A, Y, w)),
-         this._errorBoundary.wrap(this),
-         this._errorBoundary.wrap(K),
-         this._errorBoundary.wrap(this._logger),
-         q.setErrorBoundary(this._errorBoundary),
-         (this.dataAdapter = K),
-         this.dataAdapter.attach(A, Y),
-         (this.storageProvider = xW1.Storage),
-         this._primeReadyRipcord(),
-         YtY(A, this));
-     }
-     updateRuntimeOptions(A) {
-       if (A.disableLogging != null)
-         ((this._options.disableLogging = A.disableLogging),
-           this._logger.setLoggingDisabled(A.disableLogging));
-       if (A.disableStorage != null)
-         ((this._options.disableStorage = A.disableStorage),
-           xW1.Storage._setDisabled(A.disableStorage));
-     }
-     flush() {
-       return this._logger.flush();
-     }
-     shutdown() {
-       return osY(this, void 0, void 0, function* () {
-         (this.$emt({ name: "pre_shutdown" }),
-           this._setStatus("Uninitialized", null),
-           (this._initializePromise = null),
-           yield this._logger.stop());
-       });
-     }
-     on(A, K) {
-       if (!this._listeners[A]) this._listeners[A] = [];
-       this._listeners[A].push(K);
-     }
-     off(A, K) {
-       if (this._listeners[A]) {
-         let q = this._listeners[A].indexOf(K);
-         if (q !== -1) this._listeners[A].splice(q, 1);
-       }
-     }
-     $on(A, K) {
-       ((K.__isInternal = !0), this.on(A, K));
-     }
-     $emt(A) {
-       var K;
-       let q = (Y) => {
-         try {
-           Y(A);
-         } catch (z) {
-           if (Y.__isInternal === !0) {
-             this._errorBoundary.logError(`__emit:${A.name}`, z);
-             return;
-           }
-           Yv6.Log.error(
-             "An error occurred in a StatsigClientEvent listener. This is not an issue with Statsig.",
-             A,
-           );
-         }
-       };
-       if (this._listeners[A.name]) this._listeners[A.name].forEach((Y) => q(Y));
-       (K = this._listeners["*"]) === null || K === void 0 || K.forEach(q);
-     }
-     _setStatus(A, K) {
-       ((this.loadingStatus = A),
-         (this._memoCache = {}),
-         this.$emt({ name: "values_updated", status: A, values: K }));
-     }
-     _enqueueExposure(A, K, q) {
-       if ((q === null || q === void 0 ? void 0 : q.disableExposureLog) === !0) {
-         this._logger.incrementNonExposureCount(A);
-         return;
-       }
-       this._logger.enqueue(K);
-     }
-     _memoize(A, K) {
-       return (q, Y) => {
-         if (this._options.disableEvaluationMemoization) return K(q, Y);
-         let z = (0, esY.createMemoKey)(A, q, Y);
-         if (!z) return K(q, Y);
-         if (!(z in this._memoCache)) {
-           if (Object.keys(this._memoCache).length >= qtY) this._memoCache = {};
-           this._memoCache[z] = K(q, Y);
-         }
-         return this._memoCache[z];
-       };
-     }
-   }
-   uDA.StatsigClientBase = hh7;
-   function YtY(A, K) {
-     var q;
-     if ((0, AtY._isServerEnv)()) return;
-     let Y = (0, asY._getStatsigGlobal)(),
-       z = (q = Y.instances) !== null && q !== void 0 ? q : {},
-       w = K;
-     if (z[A] != null)
-       Yv6.Log.warn(
-         "Creating multiple Statsig clients with the same SDK key can lead to unexpected behavior. Multi-instance support requires different SDK keys.",
-       );
-     if (((z[A] = w), !Y.firstInstance)) Y.firstInstance = w;
-     ((Y.instances = z), (__STATSIG__ = Y));
-   }
- });

--- Removed Bh7 (pretty-v2.1.25.js:344183-344187)
- var Bh7 = v((xh7) => {
-   Object.defineProperty(xh7, "__esModule", { value: !0 });
-   xh7.DataAdapterCachePrefix = void 0;
-   xh7.DataAdapterCachePrefix = "statsig.cached";
- });

--- Removed gh7 (pretty-v2.1.25.js:344188-344190)
- var gh7 = v((mh7) => {
-   Object.defineProperty(mh7, "__esModule", { value: !0 });
- });

--- Removed Qh7 (pretty-v2.1.25.js:344191-344193)
- var Qh7 = v((Fh7) => {
-   Object.defineProperty(Fh7, "__esModule", { value: !0 });
- });

--- Removed ch7 (pretty-v2.1.25.js:344194-344291)
- var ch7 = v((ph7) => {
-   Object.defineProperty(ph7, "__esModule", { value: !0 });
-   ph7._makeTypedGet =
-     ph7._mergeOverride =
-     ph7._makeLayer =
-     ph7._makeExperiment =
-     ph7._makeDynamicConfig =
-     ph7._makeFeatureGate =
-       void 0;
-   var ztY = Xj(),
-     wtY = ZW1(),
-     HtY = "default";
-   function zv6(A, K, q, Y) {
-     var z;
-     return {
-       name: A,
-       details: K,
-       ruleID:
-         (z = q === null || q === void 0 ? void 0 : q.rule_id) !== null &&
-         z !== void 0
-           ? z
-           : HtY,
-       __evaluation: q,
-       value: Y,
-     };
-   }
-   function JtY(A, K, q) {
-     return zv6(A, K, q, (q === null || q === void 0 ? void 0 : q.value) === !0);
-   }
-   ph7._makeFeatureGate = JtY;
-   function Uh7(A, K, q) {
-     var Y;
-     let z =
-       (Y = q === null || q === void 0 ? void 0 : q.value) !== null &&
-       Y !== void 0
-         ? Y
-         : {};
-     return Object.assign(Object.assign({}, zv6(A, K, q, z)), {
-       get: uW1(A, q === null || q === void 0 ? void 0 : q.value),
-     });
-   }
-   ph7._makeDynamicConfig = Uh7;
-   function OtY(A, K, q) {
-     var Y;
-     let z = Uh7(A, K, q);
-     return Object.assign(Object.assign({}, z), {
-       groupName:
-         (Y = q === null || q === void 0 ? void 0 : q.group_name) !== null &&
-         Y !== void 0
-           ? Y
-           : null,
-     });
-   }
-   ph7._makeExperiment = OtY;
-   function XtY(A, K, q, Y) {
-     var z, w;
-     return Object.assign(Object.assign({}, zv6(A, K, q, void 0)), {
-       get: uW1(A, q === null || q === void 0 ? void 0 : q.value, Y),
-       groupName:
-         (z = q === null || q === void 0 ? void 0 : q.group_name) !== null &&
-         z !== void 0
-           ? z
-           : null,
-       __value:
-         (w = q === null || q === void 0 ? void 0 : q.value) !== null &&
-         w !== void 0
-           ? w
-           : {},
-     });
-   }
-   ph7._makeLayer = XtY;
-   function $tY(A, K, q, Y) {
-     return Object.assign(Object.assign(Object.assign({}, A), K), {
-       get: uW1(A.name, q, Y),
-     });
-   }
-   ph7._mergeOverride = $tY;
-   function uW1(A, K, q) {
-     return (Y, z) => {
-       var w;
-       let H =
-         (w = K === null || K === void 0 ? void 0 : K[Y]) !== null &&
-         w !== void 0
-           ? w
-           : null;
-       if (H == null) return z !== null && z !== void 0 ? z : null;
-       if (z != null && !(0, wtY._isTypeMatch)(H, z))
-         return (
-           ztY.Log.warn(
-             `Parameter type mismatch. '${A}.${Y}' was found to be type '${typeof H}' but fallback/return type is '${typeof z}'. See https://docs.statsig.com/client/javascript-sdk/#typed-getters`,
-           ),
-           z !== null && z !== void 0 ? z : null
-         );
-       return (q === null || q === void 0 || q(Y), H);
-     };
-   }
-   ph7._makeTypedGet = uW1;
- });

--- Removed ih7 (pretty-v2.1.25.js:344292-344294)
- var ih7 = v((lh7) => {
-   Object.defineProperty(lh7, "__esModule", { value: !0 });
- });

--- Removed oh7 (pretty-v2.1.25.js:344295-344313)
- var oh7 = v((nh7) => {
-   Object.defineProperty(nh7, "__esModule", { value: !0 });
-   nh7.UPDATE_DETAIL_ERROR_MESSAGES = nh7.createUpdateDetails = void 0;
-   var jtY = (A, K, q, Y, z, w) => {
-     return {
-       duration: q,
-       source: K,
-       success: A,
-       error: Y,
-       sourceUrl: z,
-       warnings: w,
-     };
-   };
-   nh7.createUpdateDetails = jtY;
-   nh7.UPDATE_DETAIL_ERROR_MESSAGES = {
-     NO_NETWORK_DATA:
-       "No data was returned from the network. This may be due to a network timeout if a timeout value was specified in the options or ad blocker error.",
-   };
- });

--- Removed is (pretty-v2.1.25.js:344314-344422)
- var is = v((eK) => {
-   var PtY =
-       (eK && eK.__createBinding) ||
-       (Object.create
-         ? function (A, K, q, Y) {
-             if (Y === void 0) Y = q;
-             var z = Object.getOwnPropertyDescriptor(K, q);
-             if (
-               !z ||
-               ("get" in z ? !K.__esModule : z.writable || z.configurable)
-             )
-               z = {
-                 enumerable: !0,
-                 get: function () {
-                   return K[q];
-                 },
-               };
-             Object.defineProperty(A, Y, z);
-           }
-         : function (A, K, q, Y) {
-             if (Y === void 0) Y = q;
-             A[Y] = K[q];
-           }),
-     A9 =
-       (eK && eK.__exportStar) ||
-       function (A, K) {
-         for (var q in A)
-           if (q !== "default" && !Object.prototype.hasOwnProperty.call(K, q))
-             PtY(K, A, q);
-       };
-   Object.defineProperty(eK, "__esModule", { value: !0 });
-   eK.Storage = eK.Log = eK.EventLogger = eK.Diagnostics = void 0;
-   y5A();
-   var VtY = GW1();
-   Object.defineProperty(eK, "Diagnostics", {
-     enumerable: !0,
-     get: function () {
-       return VtY.Diagnostics;
-     },
-   });
-   var ftY = cT6();
-   Object.defineProperty(eK, "EventLogger", {
-     enumerable: !0,
-     get: function () {
-       return ftY.EventLogger;
-     },
-   });
-   var ah7 = Xj();
-   Object.defineProperty(eK, "Log", {
-     enumerable: !0,
-     get: function () {
-       return ah7.Log;
-     },
-   });
-   var NtY = NgA(),
-     TtY = rp();
-   Object.defineProperty(eK, "Storage", {
-     enumerable: !0,
-     get: function () {
-       return TtY.Storage;
-     },
-   });
-   A9(y5A(), eK);
-   A9(jgA(), eK);
-   A9(VS7(), eK);
-   A9(BS7(), eK);
-   A9(GW1(), eK);
-   A9(gS7(), eK);
-   A9(oT6(), eK);
-   A9(iS7(), eK);
-   A9(rS7(), eK);
-   A9(CDA(), eK);
-   A9(aS7(), eK);
-   A9(Xj(), eK);
-   A9(aT6(), eK);
-   A9(MgA(), eK);
-   A9(Lh7(), eK);
-   A9(yh7(), eK);
-   A9(Sh7(), eK);
-   A9(I5A(), eK);
-   A9(SW1(), eK);
-   A9(bW1(), eK);
-   A9(LW1(), eK);
-   A9(bh7(), eK);
-   A9(Kv6(), eK);
-   A9(Bh7(), eK);
-   A9(BT6(), eK);
-   A9(NgA(), eK);
-   A9(gh7(), eK);
-   A9(Qh7(), eK);
-   A9(ch7(), eK);
-   A9(ih7(), eK);
-   A9(iT6(), eK);
-   A9(rp(), eK);
-   A9(nT6(), eK);
-   A9(ZW1(), eK);
-   A9(FT6(), eK);
-   A9(kW1(), eK);
-   A9(vW1(), eK);
-   A9(oh7(), eK);
-   A9(eT6(), eK);
-   __STATSIG__ = Object.assign(
-     Object.assign(
-       {},
-       __STATSIG__ !== null && __STATSIG__ !== void 0 ? __STATSIG__ : {},
-     ),
-     { Log: ah7.Log, SDK_VERSION: NtY.SDK_VERSION },
-   );
- });

--- Removed eh7 (pretty-v2.1.25.js:344423-344587)
- var eh7 = v((th7) => {
-   Object.defineProperty(th7, "__esModule", { value: !0 });
-   var b5A = is();
-   class sh7 {
-     constructor(A) {
-       ((this._sdkKey = A),
-         (this._rawValues = null),
-         (this._values = null),
-         (this._source = "Uninitialized"),
-         (this._lcut = 0),
-         (this._receivedAt = 0),
-         (this._bootstrapMetadata = null),
-         (this._warnings = new Set()));
-     }
-     reset() {
-       ((this._values = null),
-         (this._rawValues = null),
-         (this._source = "Loading"),
-         (this._lcut = 0),
-         (this._receivedAt = 0),
-         (this._bootstrapMetadata = null));
-     }
-     finalize() {
-       if (this._values) return;
-       this._source = "NoValues";
-     }
-     getValues() {
-       return this._rawValues
-         ? (0, b5A._typedJsonParse)(
-             this._rawValues,
-             "has_updates",
-             "EvaluationStoreValues",
-           )
-         : null;
-     }
-     setValues(A, K) {
-       var q;
-       if (!A) return !1;
-       let Y = (0, b5A._typedJsonParse)(
-         A.data,
-         "has_updates",
-         "EvaluationResponse",
-       );
-       if (Y == null) return !1;
-       if (
-         ((this._source = A.source),
-         (Y === null || Y === void 0 ? void 0 : Y.has_updates) !== !0)
-       )
-         return !0;
-       if (
-         ((this._rawValues = A.data),
-         (this._lcut = Y.time),
-         (this._receivedAt = A.receivedAt),
-         (this._values = Y),
-         (this._bootstrapMetadata = this._extractBootstrapMetadata(A.source, Y)),
-         A.source && Y.user)
-       )
-         this._setWarningState(K, Y);
-       return (
-         b5A.SDKFlags.setFlags(
-           this._sdkKey,
-           (q = Y.sdk_flags) !== null && q !== void 0 ? q : {},
-         ),
-         !0
-       );
-     }
-     getWarnings() {
-       if (this._warnings.size === 0) return;
-       return Array.from(this._warnings);
-     }
-     getGate(A) {
-       var K;
-       return this._getDetailedStoreResult(
-         (K = this._values) === null || K === void 0 ? void 0 : K.feature_gates,
-         A,
-       );
-     }
-     getConfig(A) {
-       var K;
-       return this._getDetailedStoreResult(
-         (K = this._values) === null || K === void 0
-           ? void 0
-           : K.dynamic_configs,
-         A,
-       );
-     }
-     getLayer(A) {
-       var K;
-       return this._getDetailedStoreResult(
-         (K = this._values) === null || K === void 0 ? void 0 : K.layer_configs,
-         A,
-       );
-     }
-     getParamStore(A) {
-       var K;
-       return this._getDetailedStoreResult(
-         (K = this._values) === null || K === void 0 ? void 0 : K.param_stores,
-         A,
-       );
-     }
-     getSource() {
-       return this._source;
-     }
-     getExposureMapping() {
-       var A;
-       return (A = this._values) === null || A === void 0 ? void 0 : A.exposures;
-     }
-     _extractBootstrapMetadata(A, K) {
-       if (A !== "Bootstrap") return null;
-       let q = {};
-       if (K.user) q.user = K.user;
-       if (K.sdkInfo) q.generatorSDKInfo = K.sdkInfo;
-       return ((q.lcut = K.time), q);
-     }
-     _getDetailedStoreResult(A, K) {
-       let q = null;
-       if (A) q = A[K] ? A[K] : A[(0, b5A._DJB2)(K)];
-       return { result: q, details: this._getDetails(q == null) };
-     }
-     _setWarningState(A, K) {
-       var q;
-       let Y = b5A.StableID.get(this._sdkKey);
-       if (
-         ((q = A.customIDs) === null || q === void 0 ? void 0 : q.stableID) !== Y
-       ) {
-         this._warnings.add("StableIDMismatch");
-         return;
-       }
-       if ("user" in K) {
-         let z = K.user;
-         if ((0, b5A._getFullUserHash)(A) !== (0, b5A._getFullUserHash)(z))
-           this._warnings.add("PartialUserMatch");
-       }
-     }
-     getCurrentSourceDetails() {
-       if (this._source === "Uninitialized" || this._source === "NoValues")
-         return { reason: this._source };
-       let A = {
-         reason: this._source,
-         lcut: this._lcut,
-         receivedAt: this._receivedAt,
-       };
-       if (this._warnings.size > 0) A.warnings = Array.from(this._warnings);
-       return A;
-     }
-     _getDetails(A) {
-       var K, q;
-       let Y = this.getCurrentSourceDetails(),
-         z = Y.reason,
-         w = (K = Y.warnings) !== null && K !== void 0 ? K : [];
-       if (this._source === "Bootstrap" && w.length > 0) z = z + w[0];
-       if (z !== "Uninitialized" && z !== "NoValues")
-         z = `${z}:${A ? "Unrecognized" : "Recognized"}`;
-       let H =
-         this._source === "Bootstrap"
-           ? (q = this._bootstrapMetadata) !== null && q !== void 0
-             ? q
-             : void 0
-           : void 0;
-       if (H) Y.bootstrapMetadata = H;
-       return Object.assign(Object.assign({}, Y), { reason: z });
-     }
-   }
-   th7.default = sh7;
- });

--- Removed Yb7 (pretty-v2.1.25.js:344588-344651)
- var Yb7 = v((Kb7) => {
-   Object.defineProperty(Kb7, "__esModule", { value: !0 });
-   Kb7._resolveDeltasResponse = void 0;
-   var Ab7 = is(),
-     EtY = 2;
-   function ktY(A, K) {
-     let q = (0, Ab7._typedJsonParse)(K, "checksum", "DeltasEvaluationResponse");
-     if (!q) return { hadBadDeltaChecksum: !0 };
-     let Y = CtY(A, q),
-       z = LtY(Y),
-       w = (0, Ab7._DJB2Object)(
-         {
-           feature_gates: z.feature_gates,
-           dynamic_configs: z.dynamic_configs,
-           layer_configs: z.layer_configs,
-         },
-         EtY,
-       );
-     if (w !== q.checksumV2)
-       return {
-         hadBadDeltaChecksum: !0,
-         badChecksum: w,
-         badMergedConfigs: z,
-         badFullResponse: q.deltas_full_response,
-       };
-     return JSON.stringify(z);
-   }
-   Kb7._resolveDeltasResponse = ktY;
-   function CtY(A, K) {
-     return Object.assign(Object.assign(Object.assign({}, A), K), {
-       feature_gates: Object.assign(
-         Object.assign({}, A.feature_gates),
-         K.feature_gates,
-       ),
-       layer_configs: Object.assign(
-         Object.assign({}, A.layer_configs),
-         K.layer_configs,
-       ),
-       dynamic_configs: Object.assign(
-         Object.assign({}, A.dynamic_configs),
-         K.dynamic_configs,
-       ),
-     });
-   }
-   function LtY(A) {
-     let K = A;
-     return (
-       wv6(A.deleted_gates, K.feature_gates),
-       delete K.deleted_gates,
-       wv6(A.deleted_configs, K.dynamic_configs),
-       delete K.deleted_configs,
-       wv6(A.deleted_layers, K.layer_configs),
-       delete K.deleted_layers,
-       K
-     );
-   }
-   function wv6(A, K) {
-     A === null ||
-       A === void 0 ||
-       A.forEach((q) => {
-         delete K[q];
-       });
-   }
- });

--- Removed Hv6 (pretty-v2.1.25.js:344652-344760)
- var Hv6 = v((TgA) => {
-   var zb7 =
-     (TgA && TgA.__awaiter) ||
-     function (A, K, q, Y) {
-       function z(w) {
-         return w instanceof q
-           ? w
-           : new q(function (H) {
-               H(w);
-             });
-       }
-       return new (q || (q = Promise))(function (w, H) {
-         function J($) {
-           try {
-             X(Y.next($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function O($) {
-           try {
-             X(Y.throw($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function X($) {
-           $.done ? w($.value) : z($.value).then(J, O);
-         }
-         X((Y = Y.apply(A, K || [])).next());
-       });
-     };
-   Object.defineProperty(TgA, "__esModule", { value: !0 });
-   var BW1 = is(),
-     RtY = Yb7();
-   class wb7 extends BW1.NetworkCore {
-     constructor(A, K) {
-       super(A, K);
-       let q = A === null || A === void 0 ? void 0 : A.networkConfig;
-       this._initializeUrlConfig = new BW1.UrlConfiguration(
-         BW1.Endpoint._initialize,
-         q === null || q === void 0 ? void 0 : q.initializeUrl,
-         q === null || q === void 0 ? void 0 : q.api,
-         q === null || q === void 0 ? void 0 : q.initializeFallbackUrls,
-       );
-     }
-     fetchEvaluations(A, K, q, Y, z) {
-       return zb7(this, void 0, void 0, function* () {
-         let w = K
-             ? (0, BW1._typedJsonParse)(K, "has_updates", "InitializeResponse")
-             : null,
-           H = {
-             user: Y,
-             hash: "djb2",
-             deltasResponseRequested: !1,
-             full_checksum: null,
-           };
-         if (w === null || w === void 0 ? void 0 : w.has_updates)
-           H = Object.assign(Object.assign({}, H), {
-             sinceTime: z ? w.time : 0,
-             previousDerivedFields:
-               "derived_fields" in w && z ? w.derived_fields : {},
-             deltasResponseRequested: !0,
-             full_checksum: w.full_checksum,
-           });
-         return this._fetchEvaluations(A, w, H, q);
-       });
-     }
-     _fetchEvaluations(A, K, q, Y) {
-       var z, w;
-       return zb7(this, void 0, void 0, function* () {
-         let H = yield this.post({
-           sdkKey: A,
-           urlConfig: this._initializeUrlConfig,
-           data: q,
-           retries: 2,
-           isStatsigEncodable: !0,
-           priority: Y,
-         });
-         if ((H === null || H === void 0 ? void 0 : H.code) === 204)
-           return '{"has_updates": false}';
-         if ((H === null || H === void 0 ? void 0 : H.code) !== 200)
-           return (z = H === null || H === void 0 ? void 0 : H.body) !== null &&
-             z !== void 0
-             ? z
-             : null;
-         if (
-           (K === null || K === void 0 ? void 0 : K.has_updates) !== !0 ||
-           ((w = H.body) === null || w === void 0
-             ? void 0
-             : w.includes('"is_delta":true')) !== !0 ||
-           q.deltasResponseRequested !== !0
-         )
-           return H.body;
-         let J = (0, RtY._resolveDeltasResponse)(K, H.body);
-         if (typeof J === "string") return J;
-         return this._fetchEvaluations(
-           A,
-           K,
-           Object.assign(Object.assign(Object.assign({}, q), J), {
-             deltasResponseRequested: !1,
-           }),
-           Y,
-         );
-       });
-     }
-   }
-   TgA.default = wb7;
- });

--- Removed Xb7 (pretty-v2.1.25.js:344761-344821)
- var Xb7 = v((Jb7) => {
-   Object.defineProperty(Jb7, "__esModule", { value: !0 });
-   Jb7._makeParamStoreGetter = void 0;
-   var Hb7 = is(),
-     mW1 = { disableExposureLog: !0 };
-   function gW1(A) {
-     return A == null || A.disableExposureLog === !1;
-   }
-   function Jv6(A, K) {
-     return K != null && !(0, Hb7._isTypeMatch)(A, K);
-   }
-   function ytY(A, K) {
-     return A.value;
-   }
-   function ItY(A, K, q) {
-     if (A.getFeatureGate(K.gate_name, gW1(q) ? void 0 : mW1).value)
-       return K.pass_value;
-     return K.fail_value;
-   }
-   function StY(A, K, q, Y) {
-     let w = A.getDynamicConfig(K.config_name, mW1).get(K.param_name);
-     if (Jv6(w, q)) return q;
-     if (gW1(Y)) A.getDynamicConfig(K.config_name);
-     return w;
-   }
-   function htY(A, K, q, Y) {
-     let w = A.getExperiment(K.experiment_name, mW1).get(K.param_name);
-     if (Jv6(w, q)) return q;
-     if (gW1(Y)) A.getExperiment(K.experiment_name);
-     return w;
-   }
-   function btY(A, K, q, Y) {
-     let w = A.getLayer(K.layer_name, mW1).get(K.param_name);
-     if (Jv6(w, q)) return q;
-     if (gW1(Y)) A.getLayer(K.layer_name).get(K.param_name);
-     return w;
-   }
-   function xtY(A, K, q) {
-     return (Y, z) => {
-       if (K == null) return z;
-       let w = K[Y];
-       if (w == null || (z != null && (0, Hb7._typeOf)(z) !== w.param_type))
-         return z;
-       switch (w.ref_type) {
-         case "static":
-           return ytY(w, q);
-         case "gate":
-           return ItY(A, w, q);
-         case "dynamic_config":
-           return StY(A, w, z, q);
-         case "experiment":
-           return htY(A, w, z, q);
-         case "layer":
-           return btY(A, w, z, q);
-         default:
-           return z;
-       }
-     };
-   }
-   Jb7._makeParamStoreGetter = xtY;
- });

--- Removed _b7 (pretty-v2.1.25.js:344822-344922)
- var _b7 = v((BDA) => {
-   var utY =
-     (BDA && BDA.__awaiter) ||
-     function (A, K, q, Y) {
-       function z(w) {
-         return w instanceof q
-           ? w
-           : new q(function (H) {
-               H(w);
-             });
-       }
-       return new (q || (q = Promise))(function (w, H) {
-         function J($) {
-           try {
-             X(Y.next($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function O($) {
-           try {
-             X(Y.throw($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function X($) {
-           $.done ? w($.value) : z($.value).then(J, O);
-         }
-         X((Y = Y.apply(A, K || [])).next());
-       });
-     };
-   Object.defineProperty(BDA, "__esModule", { value: !0 });
-   BDA.StatsigEvaluationsDataAdapter = void 0;
-   var x5A = is(),
-     BtY = Hv6();
-   class $b7 extends x5A.DataAdapterCore {
-     constructor() {
-       super("EvaluationsDataAdapter", "evaluations");
-       ((this._network = null), (this._options = null));
-     }
-     attach(A, K) {
-       (super.attach(A, K),
-         (this._network = new BtY.default(K !== null && K !== void 0 ? K : {})));
-     }
-     getDataAsync(A, K, q) {
-       return this._getDataAsyncImpl(
-         A,
-         (0, x5A._normalizeUser)(K, this._options),
-         q,
-       );
-     }
-     prefetchData(A, K) {
-       return this._prefetchDataImpl(A, K);
-     }
-     setData(A) {
-       let K = (0, x5A._typedJsonParse)(A, "has_updates", "data");
-       if (K && "user" in K) super.setData(A, K.user);
-       else
-         x5A.Log.error(
-           "StatsigUser not found. You may be using an older server SDK version. Please upgrade your SDK or use setDataLegacy.",
-         );
-     }
-     setDataLegacy(A, K) {
-       super.setData(A, K);
-     }
-     _fetchFromNetwork(A, K, q, Y) {
-       var z;
-       return utY(this, void 0, void 0, function* () {
-         let w = yield (z = this._network) === null || z === void 0
-           ? void 0
-           : z.fetchEvaluations(
-               this._getSdkKey(),
-               A,
-               q === null || q === void 0 ? void 0 : q.priority,
-               K,
-               Y,
-             );
-         return w !== null && w !== void 0 ? w : null;
-       });
-     }
-     _getCacheKey(A) {
-       var K;
-       let q = (0, x5A._getStorageKey)(
-         this._getSdkKey(),
-         A,
-         (K = this._options) === null || K === void 0
-           ? void 0
-           : K.customUserCacheKeyFunc,
-       );
-       return `${x5A.DataAdapterCachePrefix}.${this._cacheSuffix}.${q}`;
-     }
-     _isCachedResultValidFor204(A, K) {
-       return (
-         A.fullUserHash != null &&
-         A.fullUserHash === (0, x5A._getFullUserHash)(K)
-       );
-     }
-   }
-   BDA.StatsigEvaluationsDataAdapter = $b7;
- });

--- Removed Zb7 (pretty-v2.1.25.js:344923-345340)
- var Zb7 = v((vgA) => {
-   var Ov6 =
-     (vgA && vgA.__awaiter) ||
-     function (A, K, q, Y) {
-       function z(w) {
-         return w instanceof q
-           ? w
-           : new q(function (H) {
-               H(w);
-             });
-       }
-       return new (q || (q = Promise))(function (w, H) {
-         function J($) {
-           try {
-             X(Y.next($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function O($) {
-           try {
-             X(Y.throw($));
-           } catch (_) {
-             H(_);
-           }
-         }
-         function X($) {
-           $.done ? w($.value) : z($.value).then(J, O);
-         }
-         X((Y = Y.apply(A, K || [])).next());
-       });
-     };
-   Object.defineProperty(vgA, "__esModule", { value: !0 });
-   var V9 = is(),
-     mtY = eh7(),
-     gtY = Hv6(),
-     Gb7 = Xb7(),
-     FtY = _b7();
-   class FW1 extends V9.StatsigClientBase {
-     static instance(A) {
-       let K = (0, V9._getStatsigGlobal)().instance(A);
-       if (K instanceof FW1) return K;
-       return (
-         V9.Log.warn(
-           (0, V9._isServerEnv)()
-             ? "StatsigClient.instance is not supported in server environments"
-             : "Unable to find StatsigClient instance",
-         ),
-         new FW1(A !== null && A !== void 0 ? A : "", {})
-       );
-     }
-     constructor(A, K, q = null) {
-       var Y, z;
-       V9.SDKType._setClientType(A, "javascript-client");
-       let w = new gtY.default(q, (J) => {
-         this.$emt(J);
-       });
-       super(
-         A,
-         (Y = q === null || q === void 0 ? void 0 : q.dataAdapter) !== null &&
-           Y !== void 0
-           ? Y
-           : new FtY.StatsigEvaluationsDataAdapter(),
-         w,
-         q,
-       );
-       ((this.getFeatureGate = this._memoize(
-         V9.MemoPrefix._gate,
-         this._getFeatureGateImpl.bind(this),
-       )),
-         (this.getDynamicConfig = this._memoize(
-           V9.MemoPrefix._dynamicConfig,
-           this._getDynamicConfigImpl.bind(this),
-         )),
-         (this.getExperiment = this._memoize(
-           V9.MemoPrefix._experiment,
-           this._getExperimentImpl.bind(this),
-         )),
-         (this.getLayer = this._memoize(
-           V9.MemoPrefix._layer,
-           this._getLayerImpl.bind(this),
-         )),
-         (this.getParameterStore = this._memoize(
-           V9.MemoPrefix._paramStore,
-           this._getParameterStoreImpl.bind(this),
-         )),
-         (this._store = new mtY.default(A)),
-         (this._network = w),
-         (this._user = this._configureUser(K, q)));
-       let H =
-         (z = q === null || q === void 0 ? void 0 : q.plugins) !== null &&
-         z !== void 0
-           ? z
-           : [];
-       for (let J of H) J.bind(this);
-     }
-     initializeSync(A) {
-       var K;
-       if (this.loadingStatus !== "Uninitialized")
-         return (0, V9.createUpdateDetails)(
-           !0,
-           this._store.getSource(),
-           -1,
-           null,
-           null,
-           [
-             "MultipleInitializations",
-             ...((K = this._store.getWarnings()) !== null && K !== void 0
-               ? K
-               : []),
-           ],
-         );
-       return (this._logger.start(), this.updateUserSync(this._user, A));
-     }
-     initializeAsync(A) {
-       return Ov6(this, void 0, void 0, function* () {
-         if (this._initializePromise) return this._initializePromise;
-         return (
-           (this._initializePromise = this._initializeAsyncImpl(A)),
-           this._initializePromise
-         );
-       });
-     }
-     updateUserSync(A, K) {
-       var q;
-       let Y = performance.now(),
-         z = [
-           ...((q = this._store.getWarnings()) !== null && q !== void 0
-             ? q
-             : []),
-         ];
-       this._resetForUser(A);
-       let w = this.dataAdapter.getDataSync(this._user);
-       if (w == null) z.push("NoCachedValues");
-       (this._store.setValues(w, this._user), this._finalizeUpdate(w));
-       let H =
-         K === null || K === void 0 ? void 0 : K.disableBackgroundCacheRefresh;
-       if (
-         H === !0 ||
-         (H == null &&
-           (w === null || w === void 0 ? void 0 : w.source) === "Bootstrap")
-       )
-         return (0, V9.createUpdateDetails)(
-           !0,
-           this._store.getSource(),
-           performance.now() - Y,
-           this._errorBoundary.getLastSeenErrorAndReset(),
-           this._network.getLastUsedInitUrlAndReset(),
-           z,
-         );
-       return (
-         this._runPostUpdate(w !== null && w !== void 0 ? w : null, this._user),
-         (0, V9.createUpdateDetails)(
-           !0,
-           this._store.getSource(),
-           performance.now() - Y,
-           this._errorBoundary.getLastSeenErrorAndReset(),
-           this._network.getLastUsedInitUrlAndReset(),
-           z,
-         )
-       );
-     }
-     updateUserAsync(A, K) {
-       return Ov6(this, void 0, void 0, function* () {
-         this._resetForUser(A);
-         let q = this._user;
-         V9.Diagnostics._markInitOverallStart(this._sdkKey);
-         let Y = this.dataAdapter.getDataSync(q);
-         if (
-           (this._store.setValues(Y, this._user),
-           this._setStatus("Loading", Y),
-           (Y = yield this.dataAdapter.getDataAsync(Y, q, K)),
-           q !== this._user)
-         )
-           return (0, V9.createUpdateDetails)(
-             !1,
-             this._store.getSource(),
-             -1,
-             Error("User changed during update"),
-             this._network.getLastUsedInitUrlAndReset(),
-           );
-         let z = !1;
-         if (Y != null)
-           (V9.Diagnostics._markInitProcessStart(this._sdkKey),
-             (z = this._store.setValues(Y, this._user)),
-             V9.Diagnostics._markInitProcessEnd(this._sdkKey, { success: z }));
-         if ((this._finalizeUpdate(Y), !z))
-           (this._errorBoundary.attachErrorIfNoneExists(
-             V9.UPDATE_DETAIL_ERROR_MESSAGES.NO_NETWORK_DATA,
-           ),
-             this.$emt({ name: "initialization_failure" }));
-         V9.Diagnostics._markInitOverallEnd(
-           this._sdkKey,
-           z,
-           this._store.getCurrentSourceDetails(),
-         );
-         let w = V9.Diagnostics._enqueueDiagnosticsEvent(
-           this._user,
-           this._logger,
-           this._sdkKey,
-           this._options,
-         );
-         return (0, V9.createUpdateDetails)(
-           z,
-           this._store.getSource(),
-           w,
-           this._errorBoundary.getLastSeenErrorAndReset(),
-           this._network.getLastUsedInitUrlAndReset(),
-           this._store.getWarnings(),
-         );
-       });
-     }
-     getContext() {
-       return {
-         sdkKey: this._sdkKey,
-         options: this._options,
-         values: this._store.getValues(),
-         user: JSON.parse(JSON.stringify(this._user)),
-         errorBoundary: this._errorBoundary,
-         session: V9.StatsigSession.get(this._sdkKey),
-         stableID: V9.StableID.get(this._sdkKey),
-       };
-     }
-     checkGate(A, K) {
-       return this.getFeatureGate(A, K).value;
-     }
-     logEvent(A, K, q) {
-       let Y =
-         typeof A === "string" ? { eventName: A, value: K, metadata: q } : A;
-       this._logger.enqueue(
-         Object.assign(Object.assign({}, Y), {
-           user: this._user,
-           time: Date.now(),
-         }),
-       );
-     }
-     _primeReadyRipcord() {
-       this.$on("error", () => {
-         this.loadingStatus === "Loading" && this._finalizeUpdate(null);
-       });
-     }
-     _initializeAsyncImpl(A) {
-       return Ov6(this, void 0, void 0, function* () {
-         if (!V9.Storage.isReady()) yield V9.Storage.isReadyResolver();
-         return (this._logger.start(), this.updateUserAsync(this._user, A));
-       });
-     }
-     _finalizeUpdate(A) {
-       (this._store.finalize(), this._setStatus("Ready", A));
-     }
-     _runPostUpdate(A, K) {
-       this.dataAdapter.getDataAsync(A, K, { priority: "low" }).catch((q) => {
-         V9.Log.error("An error occurred after update.", q);
-       });
-     }
-     _resetForUser(A) {
-       (this._logger.reset(),
-         this._store.reset(),
-         (this._user = this._configureUser(A, this._options)));
-     }
-     _configureUser(A, K) {
-       var q;
-       let Y = (0, V9._normalizeUser)(A, K),
-         z = (q = Y.customIDs) === null || q === void 0 ? void 0 : q.stableID;
-       if (z) V9.StableID.setOverride(z, this._sdkKey);
-       return Y;
-     }
-     _getFeatureGateImpl(A, K) {
-       var q, Y;
-       let { result: z, details: w } = this._store.getGate(A),
-         H = (0, V9._makeFeatureGate)(A, w, z),
-         J =
-           (Y =
-             (q = this.overrideAdapter) === null || q === void 0
-               ? void 0
-               : q.getGateOverride) === null || Y === void 0
-             ? void 0
-             : Y.call(q, H, this._user, K),
-         O = J !== null && J !== void 0 ? J : H;
-       return (
-         this._enqueueExposure(
-           A,
-           (0, V9._createGateExposure)(
-             this._user,
-             O,
-             this._store.getExposureMapping(),
-           ),
-           K,
-         ),
-         this.$emt({ name: "gate_evaluation", gate: O }),
-         O
-       );
-     }
-     _getDynamicConfigImpl(A, K) {
-       var q, Y;
-       let { result: z, details: w } = this._store.getConfig(A),
-         H = (0, V9._makeDynamicConfig)(A, w, z),
-         J =
-           (Y =
-             (q = this.overrideAdapter) === null || q === void 0
-               ? void 0
-               : q.getDynamicConfigOverride) === null || Y === void 0
-             ? void 0
-             : Y.call(q, H, this._user, K),
-         O = J !== null && J !== void 0 ? J : H;
-       return (
-         this._enqueueExposure(
-           A,
-           (0, V9._createConfigExposure)(
-             this._user,
-             O,
-             this._store.getExposureMapping(),
-           ),
-           K,
-         ),
-         this.$emt({ name: "dynamic_config_evaluation", dynamicConfig: O }),
-         O
-       );
-     }
-     _getExperimentImpl(A, K) {
-       var q, Y, z, w;
-       let { result: H, details: J } = this._store.getConfig(A),
-         O = (0, V9._makeExperiment)(A, J, H);
-       if (O.__evaluation != null)
-         O.__evaluation.secondary_exposures = (0, V9._mapExposures)(
-           (Y =
-             (q = O.__evaluation) === null || q === void 0
-               ? void 0
-               : q.secondary_exposures) !== null && Y !== void 0
-             ? Y
-             : [],
-           this._store.getExposureMapping(),
-         );
-       let X =
-           (w =
-             (z = this.overrideAdapter) === null || z === void 0
-               ? void 0
-               : z.getExperimentOverride) === null || w === void 0
-             ? void 0
-             : w.call(z, O, this._user, K),
-         $ = X !== null && X !== void 0 ? X : O;
-       return (
-         this._enqueueExposure(
-           A,
-           (0, V9._createConfigExposure)(
-             this._user,
-             $,
-             this._store.getExposureMapping(),
-           ),
-           K,
-         ),
-         this.$emt({ name: "experiment_evaluation", experiment: $ }),
-         $
-       );
-     }
-     _getLayerImpl(A, K) {
-       var q, Y, z;
-       let { result: w, details: H } = this._store.getLayer(A),
-         J = (0, V9._makeLayer)(A, H, w),
-         O =
-           (Y =
-             (q = this.overrideAdapter) === null || q === void 0
-               ? void 0
-               : q.getLayerOverride) === null || Y === void 0
-             ? void 0
-             : Y.call(q, J, this._user, K);
-       if (K === null || K === void 0 ? void 0 : K.disableExposureLog)
-         this._logger.incrementNonExposureCount(A);
-       let X = (0, V9._mergeOverride)(
-         J,
-         O,
-         (z = O === null || O === void 0 ? void 0 : O.__value) !== null &&
-           z !== void 0
-           ? z
-           : J.__value,
-         ($) => {
-           if (K === null || K === void 0 ? void 0 : K.disableExposureLog)
-             return;
-           this._enqueueExposure(
-             A,
-             (0, V9._createLayerParameterExposure)(
-               this._user,
-               X,
-               $,
-               this._store.getExposureMapping(),
-             ),
-             K,
-           );
-         },
-       );
-       return (this.$emt({ name: "layer_evaluation", layer: X }), X);
-     }
-     _getParameterStoreImpl(A, K) {
-       var q, Y;
-       let { result: z, details: w } = this._store.getParamStore(A);
-       this._logger.incrementNonExposureCount(A);
-       let H = {
-           name: A,
-           details: w,
-           __configuration: z,
-           get: (0, Gb7._makeParamStoreGetter)(this, z, K),
-         },
-         J =
-           (Y =
-             (q = this.overrideAdapter) === null || q === void 0
-               ? void 0
-               : q.getParamStoreOverride) === null || Y === void 0
-             ? void 0
-             : Y.call(q, H, K);
-       if (J != null)
-         ((H.__configuration = J.config),
-           (H.details = J.details),
-           (H.get = (0, Gb7._makeParamStoreGetter)(this, J.config, K)));
-       return H;
-     }
-   }
-   vgA.default = FW1;
- });

--- Removed Db7 (pretty-v2.1.25.js:345341-345384)
- var Db7 = v((TB) => {
-   var QtY =
-       (TB && TB.__createBinding) ||
-       (Object.create
-         ? function (A, K, q, Y) {
-             if (Y === void 0) Y = q;
-             var z = Object.getOwnPropertyDescriptor(K, q);
-             if (
-               !z ||
-               ("get" in z ? !K.__esModule : z.writable || z.configurable)
-             )
-               z = {
-                 enumerable: !0,
-                 get: function () {
-                   return K[q];
-                 },
-               };
-             Object.defineProperty(A, Y, z);
-           }
-         : function (A, K, q, Y) {
-             if (Y === void 0) Y = q;
-             A[Y] = K[q];
-           }),
-     UtY =
-       (TB && TB.__exportStar) ||
-       function (A, K) {
-         for (var q in A)
-           if (q !== "default" && !Object.prototype.hasOwnProperty.call(K, q))
-             QtY(K, A, q);
-       };
-   Object.defineProperty(TB, "__esModule", { value: !0 });
-   TB.StatsigClient = void 0;
-   var Wb7 = Zb7();
-   TB.StatsigClient = Wb7.default;
-   UtY(is(), TB);
-   __STATSIG__ = Object.assign(
-     Object.assign(
-       {},
-       __STATSIG__ !== null && __STATSIG__ !== void 0 ? __STATSIG__ : {},
-     ),
-     { StatsigClient: Wb7.default },
-   );
-   TB.default = __STATSIG__;
- });

--- Removed jb7 (pretty-v2.1.25.js:345386-345416)
- var jb7 = k(() => {
-   ((ptY = {
-     visibilityState: "visible",
-     documentElement: { lang: "en" },
-     addEventListener: (A, K) => {},
-   }),
-     (dtY = {
-       document: ptY,
-       location: { href: "node://localhost", pathname: "/" },
-       addEventListener: (A, K) => {
-         if (A === "beforeunload")
-           process.on("exit", () => {
-             if (typeof K === "function") K({});
-             else K.handleEvent({});
-           });
-       },
-       focus: () => {},
-       innerHeight: 768,
-       innerWidth: 1024,
-     }),
-     (ctY = {
-       sendBeacon: (A, K) => {
-         return !0;
-       },
-       userAgent:
-         "Mozilla/5.0 (Node.js) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0",
-       language: "en-US",
-     }));
-   if (typeof window > "u") global.window = dtY;
-   if (typeof navigator > "u") global.navigator = ctY;
- });

--- Removed mDA (pretty-v2.1.25.js:345426-345428)
- function mDA() {
-   return EgA.join(w8(), "statsig");
- }

--- Removed Xv6 (pretty-v2.1.25.js:345429-345477)
- class Xv6 {
-   cache = new Map();
-   ready = !1;
-   constructor() {
-     try {
-       if (!Mb7(mDA())) ltY(mDA(), { recursive: !0 });
-       let A = itY(mDA());
-       for (let K of A) {
-         let q = decodeURIComponent(K),
-           Y = ntY(EgA.join(mDA(), K), "utf8");
-         this.cache.set(q, Y);
-       }
-       this.ready = !0;
-     } catch (A) {
-       (KA(A), (this.ready = !0));
-     }
-   }
-   isReady() {
-     return this.ready;
-   }
-   isReadyResolver() {
-     return this.ready ? Promise.resolve() : null;
-   }
-   getProviderName() {
-     return "FileSystemStorageProvider";
-   }
-   getItem(A) {
-     return this.cache.get(A) ?? null;
-   }
-   setItem(A, K) {
-     this.cache.set(A, K);
-     let q = encodeURIComponent(A);
-     otY(EgA.join(mDA(), q), K, "utf8").catch((Y) => KA(Y));
-   }
-   removeItem(A) {
-     this.cache.delete(A);
-     let K = encodeURIComponent(A),
-       q = EgA.join(mDA(), K);
-     if (!Mb7(q)) return;
-     try {
-       rtY(q);
-     } catch (Y) {
-       KA(Y);
-     }
-   }
-   getAllKeys() {
-     return Array.from(this.cache.keys());
-   }
- }

--- Removed ttY (pretty-v2.1.25.js:345483-345516)
- function ttY(A) {
-   let K = rs(!0),
-     q = {
-       networkConfig: {
-         api: "https://statsig.anthropic.com/v1/",
-         networkTimeoutMs: 30000,
-       },
-       environment: { tier: "production" },
-       includeCurrentPageUrlWithEvents: !1,
-       logLevel: QW1.LogLevel.None,
-       storageProvider: new Xv6(),
-       customUserCacheKeyFunc: (w, H) => {
-         return atY("sha1")
-           .update(w)
-           .update(H.userID || "")
-           .digest("hex")
-           .slice(0, 10);
-       },
-     },
-     Y = new QW1.StatsigClient(A, K, q);
-   Y.on("error", () => {
-     A8.head("https://api.anthropic.com/api/hello").catch(() => {});
-   });
-   let z = Y.initializeAsync();
-   return (
-     process.on("beforeExit", async () => {
-       await Y.flush();
-     }),
-     process.on("exit", () => {
-       Y.flush();
-     }),
-     { client: Y, initialized: z }
-   );
- }

--- Removed fb7 (pretty-v2.1.25.js:345517-345519)
- function fb7() {
-   (Vb7.cache?.clear?.(), ap.cache?.clear?.());
- }

--- Removed u5A (pretty-v2.1.25.js:345520-345529)
- async function u5A() {
-   if (K$()) return;
-   try {
-     let A = rs(!0),
-       K = await ap();
-     if (K) await K.updateUserAsync(A);
-   } catch (A) {
-     KA(A instanceof Error ? A : Error(`Statsig: Force refresh failed: ${A}`));
-   }
- }

--- Removed Nb7 (pretty-v2.1.25.js:345530-345538)
- function Nb7() {
-   if (K$()) return;
-   let A = setInterval(() => {
-     u5A();
-   }, stY);
-   process.on("beforeExit", () => {
-     clearInterval(A);
-   });
- }

--- Removed $v6 (pretty-v2.1.25.js:345539-345548)
- async function $v6(A, K) {
-   if (K$()) return;
-   try {
-     let [q, Y] = await Promise.all([ap(), yr({ model: K.model })]);
-     if (!q) return;
-     let z = Cy4(Y, K),
-       w = { eventName: A, metadata: z };
-     (q.logEvent(w), await q.flush());
-   } catch (q) {}
- }

--- Removed Tb7 (pretty-v2.1.25.js:345549-345551)
- function Tb7(A, K) {
-   $v6(A, K);
- }

--- Removed ns (pretty-v2.1.25.js:345556-345578)
- var ns = k(() => {
-   p7();
-   n3();
-   jb7();
-   Pb7();
-   YsA();
-   kx();
-   Z1();
-   C1();
-   sO();
-   BQ();
-   b1();
-   QW1 = o(Db7(), 1);
-   ((Vb7 = z6(() => {
-     if (K$()) return null;
-     return ttY(TW8);
-   })),
-     (ap = z6(async () => {
-       let A = Vb7();
-       if (!A) return null;
-       return (await A.initialized, A.client);
-     })));
- });

--- Removed N1K (pretty-v2.1.25.js:398935-398937)
- var N1K = v((f1K) => {
-   Object.defineProperty(f1K, "__esModule", { value: !0 });
- });

--- Removed v1K (pretty-v2.1.25.js:398938-398940)
- var v1K = v((T1K) => {
-   Object.defineProperty(T1K, "__esModule", { value: !0 });
- });

--- Removed tR6 (pretty-v2.1.25.js:398941-398943)
- var tR6 = v((E1K) => {
-   Object.defineProperty(E1K, "__esModule", { value: !0 });
- });

--- Removed x6K (pretty-v2.1.25.js:400235-400237)
- var x6K = v((b6K) => {
-   Object.defineProperty(b6K, "__esModule", { value: !0 });
- });

--- Removed QqK (pretty-v2.1.25.js:424184-424190)
- function QqK() {
-   if (kMA)
-     ((lt = kMA), h(`[TeammateModeSnapshot] Captured from CLI override: ${lt}`));
-   else
-     ((lt = M1().teammateMode ?? "auto"),
-       h(`[TeammateModeSnapshot] Captured from config: ${lt}`));
- }

--- Removed xzK (pretty-v2.1.25.js:447440-447593)
- var xzK = k(() => {
-   ((eE2 = `Use this tool proactively when you're about to start a non-trivial implementation task. Getting user sign-off on your approach before writing code prevents wasted effort and ensures alignment. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
-    - If you would use ${bJ} to clarify the approach, use EnterPlanMode instead
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
- 5. Use ${bJ} if you need to clarify approaches
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
-     (P6J = `Use this tool when a task has genuine ambiguity about the right approach and getting user input before coding would prevent significant rework. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
- When in doubt, prefer starting work and using ${bJ} for specific questions over entering a full planning phase.
- 
- ## What Happens in Plan Mode
- 
- In plan mode, you'll:
- 1. Explore the codebase using Glob, Grep, and Read tools
- 2. Understand existing patterns and architecture
- 3. Design an implementation approach
- 4. Present your plan to the user for approval
- 5. Use ${bJ} if you need to clarify approaches
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

--- Removed vC2 (pretty-v2.1.25.js:454068-454097)
-   vC2 = `[SUGGESTION MODE: Suggest what the user might naturally type next into Claude Code.]
- 
- FIRST: Look at the user's recent messages and original request.
- 
- Your job is to predict what THEY would type - not what you think they should do.
- 
- THE TEST: Would they think "I was just about to type that"?
- 
- EXAMPLES:
- User asked "fix the bug and run tests", bug is fixed → "run the tests"
- After code written → "try it out"
- Claude offers options → suggest the one the user would likely pick, based on conversation
- Claude asks to continue → "yes" or "go ahead"
- Task complete, obvious follow-up → "commit this" or "push it"
- After error or misunderstanding → silence (let them assess/correct)
- 
- Be specific: "run the tests" beats "continue".
- 
- NEVER SUGGEST:
- - Evaluative ("looks good", "thanks")
- - Questions ("what about...?")
- - Claude-voice ("Let me...", "I'll...", "Here's...")
- - New ideas they didn't ask about
- - Multiple sentences
- 
- Stay silent if the next step isn't obvious from what the user said.
- 
- Format: 2-8 words, match the user's style. Or nothing.
- 
- Reply with ONLY the suggestion, no quotes or explanation.`,

--- Removed EC2 (pretty-v2.1.25.js:454098-454111)
-   EC2 = `[SUGGESTION MODE]
- 
- TASK: Find a stated next step in the user's messages. Return it, or nothing.
- 
- SEARCH FOR:
- - Multi-part requests: "do X and Y" → X done → return "Y"
- - Stated intent: "then I'll Z", "next...", "after that..." → return "Z"
- - Answer to Claude's question → return "yes" / "go ahead" / obvious choice
- 
- NOTHING FOUND → return nothing.
- This is correct most of the time. Only return text you can trace to the user's stated plan.
- 
- 2-8 words. User's phrasing. Never evaluate, never Claude-voice.
- Output ONLY the suggestion, or nothing.`,

--- Removed $c (pretty-v2.1.25.js:523245-523247)
- async function $c() {
-   return (await bn2()).isInstalled;
- }

--- Removed rs (pretty-v2.1.25.js:532588-532615)
- function rs(A) {
-   let K = Ir(A);
-   return {
-     customIDs: {
-       sessionId: K.sessionId,
-       organizationUUID: K.organizationUuid,
-       accountUUID: K.accountUuid,
-     },
-     userID: K.deviceId,
-     appVersion: K.appVersion,
-     email: K.email,
-     custom: {
-       userType: K.userType,
-       organizationUuid: K.organizationUuid,
-       accountUuid: K.accountUuid,
-       subscriptionType: K.subscriptionType ?? "",
-       firstTokenTime: K.firstTokenTime ?? 0,
-       ...(K.githubActionsMetadata && {
-         githubActor: K.githubActionsMetadata.actor,
-         githubActorId: K.githubActionsMetadata.actorId,
-         githubRepository: K.githubActionsMetadata.repository,
-         githubRepositoryId: K.githubActionsMetadata.repositoryId,
-         githubRepositoryOwner: K.githubActionsMetadata.repositoryOwner,
-         githubRepositoryOwnerId: K.githubActionsMetadata.repositoryOwnerId,
-       }),
-     },
-   };
- }

--- Removed zs2 (pretty-v2.1.25.js:532846-532846)
-   zs2 = 21600000,

--- Removed v1z (pretty-v2.1.25.js:543752-543752)
-   v1z = 1,

--- Removed ehK (pretty-v2.1.25.js:563446-563454)
- function ehK(A, K) {
-   let q = s(3);
-   YC1.useRef(void 0);
-   let Y;
-   if (q[0] !== A || q[1] !== K)
-     ((Y = [A, K]), (q[0] = A), (q[1] = K), (q[2] = Y));
-   else Y = q[2];
-   YC1.useEffect(a7z, Y);
- }

--- Removed _qz (pretty-v2.1.25.js:566820-566826)
- function _qz(A) {
-   try {
-     return G6(A)?.type === "idle_notification";
-   } catch {
-     return !1;
-   }
- }

--- Removed Gqz (pretty-v2.1.25.js:566827-566831)
- function Gqz(A) {
-   let K = new Map();
-   for (let q of A) if (!K.has(q.from)) K.set(q.from, q.color);
-   return [...K.entries()].map(([q, Y]) => ({ name: q, color: Y }));
- }

--- Removed UgK (pretty-v2.1.25.js:566832-566876)
- function UgK() {
-   let A = F1(($) => $.inbox),
-     K = F1(($) => $.viewSelectionMode),
-     { addNotification: q, removeNotification: Y } = mK(),
-     z = $fA.useRef(0),
-     H =
-       hZ() || K === "viewing-agent"
-         ? []
-         : A.messages.filter(($) => $.status === "pending" && !_qz($.text)),
-     J = H.length,
-     O = H.map(($) => $.from)
-       .sort()
-       .join(","),
-     X = $fA.useMemo(() => Gqz(H), [O]);
-   $fA.useEffect(() => {
-     if (J === 0) {
-       if (z.current > 0) Y(ad6);
-       z.current = J;
-       return;
-     }
-     (q({
-       key: ad6,
-       jsx: yc.createElement(
-         V,
-         { dimColor: !0 },
-         "Incoming ",
-         J === 1 ? "message" : "messages",
-         " from",
-         " ",
-         X.map(({ name: $, color: _ }, G) =>
-           yc.createElement(
-             yc.Fragment,
-             { key: $ },
-             yc.createElement(V, { bold: !0, color: Pv(_) }, "@", $),
-             G < X.length - 1 && ", ",
-           ),
-         ),
-       ),
-       priority: "immediate",
-       invalidates: [ad6],
-       timeoutMs: 60000,
-     }),
-       (z.current = J));
-   }, [J, X, q, Y]);
- }

--- Removed ad6 (pretty-v2.1.25.js:566879-566879)
-   ad6 = "teammate-inbox";

--- Removed rEK (pretty-v2.1.25.js:581558-581582)
- async function rEK() {
-   let A = new oEK(),
-     K = {
-       serverName: "Claude in Chrome",
-       logger: A,
-       socketPath: ZX1(),
-       getSocketPaths: IJ7,
-       clientTypeId: "claude-code",
-       onAuthenticationError: () => {
-         A.warn(
-           "Authentication error occurred. Please ensure you are logged into the Claude browser extension.",
-         );
-       },
-       onToolCallDisconnected: () => {
-         return `Browser extension is not connected. Please ensure the Claude browser extension is installed and running (${ms2}). If this is your first time connecting to Chrome, you may need to restart Chrome for the installation to take effect. If you continue to experience issues, please report a bug: ${gs2}`;
-       },
-     },
-     q = VQ6(K),
-     Y = new LcA();
-   (process.stdin.on("end", () => process.exit(0)),
-     process.stdin.on("error", () => process.exit(0)),
-     h("[Claude in Chrome] Starting MCP server"),
-     await q.connect(Y),
-     h("[Claude in Chrome] MCP server started"));
- }

--- Removed import@581604 (pretty-v2.1.25.js:581605-581614)
- import {
-   existsSync as Us2,
-   unlinkSync as LU6,
-   chmodSync as aEK,
-   statSync as ps2,
-   mkdirSync as ds2,
-   readdirSync as sEK,
-   rmdirSync as cs2,
-   appendFileSync as ls2,
- } from "fs";

=== Added ===

+++ Added QnA (pretty-v2.1.26.js:5493-5495)
+ function QnA(A) {
+   return A.replace(RrK, "").trim() || A;
+ }

+++ Added zR1 (pretty-v2.1.26.js:5497-5503)
+ var zR1 = E(() => {
+   ((LrK = ["ide_opened_file", "ide_selection"]),
+     (RrK = new RegExp(
+       LrK.map((A) => `<${A}(?:\\s[^>]*)?>([\\s\\S]*?)<\\/${A}>\\n?`).join("|"),
+       "g",
+     )));
+ });

+++ Added Azq (pretty-v2.1.26.js:102569-102590)
+ function Azq() {
+   let A = BA(),
+     K = new Map(),
+     q = new Set();
+   for (let z of OV) {
+     if (z === "flagSettings") continue;
+     let w = gO(z);
+     if (!w) continue;
+     let H = X11.dirname(w);
+     if (!K.has(H)) K.set(H, new Set());
+     K.get(H).add(w);
+     try {
+       if (A.statSync(w).isFile()) q.add(H);
+     } catch {}
+   }
+   let Y = new Set();
+   for (let z of q) {
+     let w = K.get(z);
+     if (w) for (let H of w) Y.add(H);
+   }
+   return { dirs: [...q], settingsFiles: Y };
+ }

+++ Added ez4 (pretty-v2.1.26.js:160592-160776)
+ var ez4 = E(() => {
+   sz4 = `Use this tool to create and manage a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user.
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
+ * Uses the ${Dq} tool to add a comment to the calculateTotal function *
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

+++ Added YXA (pretty-v2.1.26.js:176672-176678)
+ var YXA = E(() => {
+   g46();
+   O76();
+   n8A();
+   ((uJ4 = new RegExp(`^${an}\\]8${tn}${tn}([^${sn}]*)${sn}$`)),
+     (GyA = `${an}]8${tn}`));
+ });

+++ Added cK (pretty-v2.1.26.js:181949-181968)
+ function cK(A, K, q) {
+   let Y = uk(),
+     z = Y?.getDisplayText(A, K),
+     w = z === void 0,
+     H = Y ? "action_not_found" : "no_context",
+     J = Iq1.useRef(!1);
+   return (
+     Iq1.useEffect(() => {
+       if (w && !J.current)
+         ((J.current = !0),
+           n("tengu_keybinding_fallback_used", {
+             action: A,
+             context: K,
+             fallback: q,
+             reason: H,
+           }));
+     }, [w, A, K, q, H]),
+     w ? q : z
+   );
+ }

+++ Added Mz (pretty-v2.1.26.js:181987-181994)
+ var Mz = E(() => {
+   kQ();
+   Jr();
+   kq1();
+   l1();
+   Iq1 = r(XA(), 1);
+   iX4 = new Set();
+ });

+++ Added Zb4 (pretty-v2.1.26.js:209572-209574)
+ function Zb4() {
+   return M$A === !0;
+ }

+++ Added ib4 (pretty-v2.1.26.js:212192-212194)
+ function ib4() {
+   return "memory";
+ }

+++ Added DE9 (pretty-v2.1.26.js:212195-212197)
+ function DE9() {
+   return "MEMORY.md";
+ }

+++ Added nb4 (pretty-v2.1.26.js:212198-212200)
+ function nb4() {
+   return ch(c$()) ?? c$();
+ }

+++ Added X7A (pretty-v2.1.26.js:212201-212203)
+ function X7A() {
+   return "";
+ }

+++ Added jE9 (pretty-v2.1.26.js:212204-212206)
+ function jE9() {
+   return lb4(Zw(nb4()), ib4()) + WE9;
+ }

+++ Added rb4 (pretty-v2.1.26.js:212207-212209)
+ function rb4() {
+   return lb4(Zw(nb4()), ib4(), DE9());
+ }

+++ Added j3Y (pretty-v2.1.26.js:266271-266273)
+ function j3Y(A) {
+   return A.includes("haiku");
+ }

+++ Added e_7 (pretty-v2.1.26.js:303797-303799)
+ function e_7(A) {
+   ((t_7 = !0), $BA(A));
+ }

+++ Added RG (pretty-v2.1.26.js:309858-310031)
+ class RG {
+   diff(A, K, q = {}) {
+     let Y;
+     if (typeof q === "function") ((Y = q), (q = {}));
+     else if ("callback" in q) Y = q.callback;
+     let z = this.castInput(A, q),
+       w = this.castInput(K, q),
+       H = this.removeEmpty(this.tokenize(z, q)),
+       J = this.removeEmpty(this.tokenize(w, q));
+     return this.diffWithOptionsObj(H, J, q, Y);
+   }
+   diffWithOptionsObj(A, K, q, Y) {
+     var z;
+     let w = (M) => {
+         if (((M = this.postProcess(M, q)), Y)) {
+           setTimeout(function () {
+             Y(M);
+           }, 0);
+           return;
+         } else return M;
+       },
+       H = K.length,
+       J = A.length,
+       O = 1,
+       X = H + J;
+     if (q.maxEditLength != null) X = Math.min(X, q.maxEditLength);
+     let $ = (z = q.timeout) !== null && z !== void 0 ? z : 1 / 0,
+       _ = Date.now() + $,
+       G = [{ oldPos: -1, lastComponent: void 0 }],
+       Z = this.extractCommon(G[0], K, A, 0, q);
+     if (G[0].oldPos + 1 >= J && Z + 1 >= H)
+       return w(this.buildValues(G[0].lastComponent, K, A));
+     let W = -1 / 0,
+       D = 1 / 0,
+       j = () => {
+         for (let M = Math.max(W, -O); M <= Math.min(D, O); M += 2) {
+           let P,
+             f = G[M - 1],
+             N = G[M + 1];
+           if (f) G[M - 1] = void 0;
+           let T = !1;
+           if (N) {
+             let R = N.oldPos - M;
+             T = N && 0 <= R && R < H;
+           }
+           let C = f && f.oldPos + 1 < J;
+           if (!T && !C) {
+             G[M] = void 0;
+             continue;
+           }
+           if (!C || (T && f.oldPos < N.oldPos))
+             P = this.addToPath(N, !0, !1, 0, q);
+           else P = this.addToPath(f, !1, !0, 1, q);
+           if (
+             ((Z = this.extractCommon(P, K, A, M, q)),
+             P.oldPos + 1 >= J && Z + 1 >= H)
+           )
+             return w(this.buildValues(P.lastComponent, K, A)) || !0;
+           else {
+             if (((G[M] = P), P.oldPos + 1 >= J)) D = Math.min(D, M - 1);
+             if (Z + 1 >= H) W = Math.max(W, M + 1);
+           }
+         }
+         O++;
+       };
+     if (Y)
+       (function M() {
+         setTimeout(function () {
+           if (O > X || Date.now() > _) return Y(void 0);
+           if (!j()) M();
+         }, 0);
+       })();
+     else
+       while (O <= X && Date.now() <= _) {
+         let M = j();
+         if (M) return M;
+       }
+   }
+   addToPath(A, K, q, Y, z) {
+     let w = A.lastComponent;
+     if (w && !z.oneChangePerToken && w.added === K && w.removed === q)
+       return {
+         oldPos: A.oldPos + Y,
+         lastComponent: {
+           count: w.count + 1,
+           added: K,
+           removed: q,
+           previousComponent: w.previousComponent,
+         },
+       };
+     else
+       return {
+         oldPos: A.oldPos + Y,
+         lastComponent: { count: 1, added: K, removed: q, previousComponent: w },
+       };
+   }
+   extractCommon(A, K, q, Y, z) {
+     let w = K.length,
+       H = q.length,
+       J = A.oldPos,
+       O = J - Y,
+       X = 0;
+     while (O + 1 < w && J + 1 < H && this.equals(q[J + 1], K[O + 1], z))
+       if ((O++, J++, X++, z.oneChangePerToken))
+         A.lastComponent = {
+           count: 1,
+           previousComponent: A.lastComponent,
+           added: !1,
+           removed: !1,
+         };
+     if (X && !z.oneChangePerToken)
+       A.lastComponent = {
+         count: X,
+         previousComponent: A.lastComponent,
+         added: !1,
+         removed: !1,
+       };
+     return ((A.oldPos = J), O);
+   }
+   equals(A, K, q) {
+     if (q.comparator) return q.comparator(A, K);
+     else
+       return A === K || (!!q.ignoreCase && A.toLowerCase() === K.toLowerCase());
+   }
+   removeEmpty(A) {
+     let K = [];
+     for (let q = 0; q < A.length; q++) if (A[q]) K.push(A[q]);
+     return K;
+   }
+   castInput(A, K) {
+     return A;
+   }
+   tokenize(A, K) {
+     return Array.from(A);
+   }
+   join(A) {
+     return A.join("");
+   }
+   postProcess(A, K) {
+     return A;
+   }
+   get useLongestToken() {
+     return !1;
+   }
+   buildValues(A, K, q) {
+     let Y = [],
+       z;
+     while (A)
+       (Y.push(A),
+         (z = A.previousComponent),
+         delete A.previousComponent,
+         (A = z));
+     Y.reverse();
+     let w = Y.length,
+       H = 0,
+       J = 0,
+       O = 0;
+     for (; H < w; H++) {
+       let X = Y[H];
+       if (!X.removed) {
+         if (!X.added && this.useLongestToken) {
+           let $ = K.slice(J, J + X.count);
+           (($ = $.map(function (_, G) {
+             let Z = q[O + G];
+             return Z.length > _.length ? Z : _;
+           })),
+             (X.value = this.join($)));
+         } else X.value = this.join(K.slice(J, J + X.count));
+         if (((J += X.count), !X.added)) O += X.count;
+       } else ((X.value = this.join(q.slice(O, O + X.count))), (O += X.count));
+     }
+     return Y;
+   }
+ }

+++ Added zW7 (pretty-v2.1.26.js:310033-310036)
+ var zW7 = E(() => {
+   YW7 = class YW7 extends RG {};
+   YEY = new YW7();
+ });

+++ Added UZA (pretty-v2.1.26.js:310095-310099)
+ function UZA(A) {
+   let K;
+   for (K = A.length - 1; K >= 0; K--) if (!A[K].match(/\s/)) break;
+   return A.substring(K + 1);
+ }

+++ Added jp (pretty-v2.1.26.js:310100-310103)
+ function jp(A) {
+   let K = A.match(/^\s*/);
+   return K ? K[0] : "";
+ }

+++ Added wW7 (pretty-v2.1.26.js:310104-310152)
+ function wW7(A, K, q, Y) {
+   if (K && q) {
+     let z = jp(K.value),
+       w = UZA(K.value),
+       H = jp(q.value),
+       J = UZA(q.value);
+     if (A) {
+       let O = Tj6(z, H);
+       ((A.value = E$1(A.value, H, O)),
+         (K.value = QZA(K.value, O)),
+         (q.value = QZA(q.value, O)));
+     }
+     if (Y) {
+       let O = vj6(w, J);
+       ((Y.value = v$1(Y.value, J, O)),
+         (K.value = vBA(K.value, O)),
+         (q.value = vBA(q.value, O)));
+     }
+   } else if (q) {
+     if (A) {
+       let z = jp(q.value);
+       q.value = q.value.substring(z.length);
+     }
+     if (Y) {
+       let z = jp(Y.value);
+       Y.value = Y.value.substring(z.length);
+     }
+   } else if (A && Y) {
+     let z = jp(Y.value),
+       w = jp(K.value),
+       H = UZA(K.value),
+       J = Tj6(z, w);
+     K.value = QZA(K.value, J);
+     let O = vj6(QZA(z, J), H);
+     ((K.value = vBA(K.value, O)),
+       (Y.value = v$1(Y.value, z, O)),
+       (A.value = E$1(A.value, z, z.slice(0, z.length - O.length))));
+   } else if (Y) {
+     let z = jp(Y.value),
+       w = UZA(K.value),
+       H = Ej6(w, z);
+     K.value = vBA(K.value, H);
+   } else if (A) {
+     let z = UZA(A.value),
+       w = jp(K.value),
+       H = Ej6(z, w);
+     K.value = QZA(K.value, H);
+   }
+ }

+++ Added k$1 (pretty-v2.1.26.js:310156-310157)
+ var k$1 =
+     "a-zA-Z0-9_\\u{AD}\\u{C0}-\\u{D6}\\u{D8}-\\u{F6}\\u{F8}-\\u{2C6}\\u{2C8}-\\u{2D7}\\u{2DE}-\\u{2FF}\\u{1E00}-\\u{1EFF}",

+++ Added XW7 (pretty-v2.1.26.js:310163-310234)
+ var XW7 = E(() => {
+   wEY = new RegExp(`[${k$1}]+|\\s+|[^${k$1}]`, "ug");
+   HW7 = class HW7 extends RG {
+     equals(A, K, q) {
+       if (q.ignoreCase) ((A = A.toLowerCase()), (K = K.toLowerCase()));
+       return A.trim() === K.trim();
+     }
+     tokenize(A, K = {}) {
+       let q;
+       if (K.intlSegmenter) {
+         let w = K.intlSegmenter;
+         if (w.resolvedOptions().granularity != "word")
+           throw Error('The segmenter passed must have a granularity of "word"');
+         q = [];
+         for (let H of Array.from(w.segment(A))) {
+           let J = H.segment;
+           if (q.length && /\s/.test(q[q.length - 1]) && /\s/.test(J))
+             q[q.length - 1] += J;
+           else q.push(J);
+         }
+       } else q = A.match(wEY) || [];
+       let Y = [],
+         z = null;
+       return (
+         q.forEach((w) => {
+           if (/\s/.test(w))
+             if (z == null) Y.push(w);
+             else Y.push(Y.pop() + w);
+           else if (z != null && /\s/.test(z))
+             if (Y[Y.length - 1] == z) Y.push(Y.pop() + w);
+             else Y.push(z + w);
+           else Y.push(w);
+           z = w;
+         }),
+         Y
+       );
+     }
+     join(A) {
+       return A.map((K, q) => {
+         if (q == 0) return K;
+         else return K.replace(/^\s+/, "");
+       }).join("");
+     }
+     postProcess(A, K) {
+       if (!A || K.oneChangePerToken) return A;
+       let q = null,
+         Y = null,
+         z = null;
+       if (
+         (A.forEach((w) => {
+           if (w.added) Y = w;
+           else if (w.removed) z = w;
+           else {
+             if (Y || z) wW7(q, z, Y, w);
+             ((q = w), (Y = null), (z = null));
+           }
+         }),
+         Y || z)
+       )
+         wW7(q, z, Y, null);
+       return A;
+     }
+   };
+   HEY = new HW7();
+   JW7 = class JW7 extends RG {
+     tokenize(A) {
+       let K = new RegExp(`(\\r?\\n)|[${k$1}]+|[^\\S\\n\\r]+|[^${k$1}]`, "ug");
+       return A.match(K) || [];
+     }
+   };
+   OW7 = new JW7();
+ });

+++ Added Cj6 (pretty-v2.1.26.js:310238-310254)
+ function Cj6(A, K) {
+   if (K.stripTrailingCr)
+     A = A.replace(
+       /\r\n/g,
+       `
+ `,
+     );
+   let q = [],
+     Y = A.split(/(\n|\r\n)/);
+   if (!Y[Y.length - 1]) Y.pop();
+   for (let z = 0; z < Y.length; z++) {
+     let w = Y[z];
+     if (z % 2 && !K.newlineIsToken) q[q.length - 1] += w;
+     else q.push(w);
+   }
+   return q;
+ }

+++ Added C$1 (pretty-v2.1.26.js:310256-310292)
+ var C$1 = E(() => {
+   $W7 = class $W7 extends RG {
+     constructor() {
+       super(...arguments);
+       this.tokenize = Cj6;
+     }
+     equals(A, K, q) {
+       if (q.ignoreWhitespace) {
+         if (
+           !q.newlineIsToken ||
+           !A.includes(`
+ `)
+         )
+           A = A.trim();
+         if (
+           !q.newlineIsToken ||
+           !K.includes(`
+ `)
+         )
+           K = K.trim();
+       } else if (q.ignoreNewlineAtEof && !q.newlineIsToken) {
+         if (
+           A.endsWith(`
+ `)
+         )
+           A = A.slice(0, -1);
+         if (
+           K.endsWith(`
+ `)
+         )
+           K = K.slice(0, -1);
+       }
+       return super.equals(A, K, q);
+     }
+   };
+   _W7 = new $W7();
+ });

+++ Added JEY (pretty-v2.1.26.js:310293-310295)
+ function JEY(A) {
+   return A == "." || A == "!" || A == "?";
+ }

+++ Added ZW7 (pretty-v2.1.26.js:310297-310321)
+ var ZW7 = E(() => {
+   GW7 = class GW7 extends RG {
+     tokenize(A) {
+       var K;
+       let q = [],
+         Y = 0;
+       for (let z = 0; z < A.length; z++) {
+         if (z == A.length - 1) {
+           q.push(A.slice(Y));
+           break;
+         }
+         if (JEY(A[z]) && A[z + 1].match(/\s/)) {
+           (q.push(A.slice(Y, z + 1)), (z = Y = z + 1));
+           while (
+             (K = A[z + 1]) === null || K === void 0 ? void 0 : K.match(/\s/)
+           )
+             z++;
+           (q.push(A.slice(Y, z + 1)), (Y = z + 1));
+         }
+       }
+       return q;
+     }
+   };
+   OEY = new GW7();
+ });

+++ Added DW7 (pretty-v2.1.26.js:310323-310330)
+ var DW7 = E(() => {
+   WW7 = class WW7 extends RG {
+     tokenize(A) {
+       return A.split(/([{}:;,]|\s+)/);
+     }
+   };
+   XEY = new WW7();
+ });

+++ Added MW7 (pretty-v2.1.26.js:310355-310383)
+ var MW7 = E(() => {
+   C$1();
+   jW7 = class jW7 extends RG {
+     constructor() {
+       super(...arguments);
+       this.tokenize = Cj6;
+     }
+     get useLongestToken() {
+       return !0;
+     }
+     castInput(A, K) {
+       let {
+         undefinedReplacement: q,
+         stringifyReplacer: Y = (z, w) => (typeof w > "u" ? q : w),
+       } = K;
+       return typeof A === "string"
+         ? A
+         : JSON.stringify(L$1(A, null, null, Y), null, "  ");
+     }
+     equals(A, K, q) {
+       return super.equals(
+         A.replace(/,([\r\n])/g, "$1"),
+         K.replace(/,([\r\n])/g, "$1"),
+         q,
+       );
+     }
+   };
+   $EY = new jW7();
+ });

+++ Added VW7 (pretty-v2.1.26.js:310385-310398)
+ var VW7 = E(() => {
+   PW7 = class PW7 extends RG {
+     tokenize(A) {
+       return A.slice();
+     }
+     join(A) {
+       return A;
+     }
+     removeEmpty(A) {
+       return A;
+     }
+   };
+   _EY = new PW7();
+ });

+++ Added RBA (pretty-v2.1.26.js:310899-310930)
+ var RBA = E(() => {
+   w0();
+   G1();
+   C1();
+   w0();
+   eoA();
+   Yz();
+   Ij6 = J6(async (A) => {
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
+ - If you see a <${IN}> tag in the current conversation turn, the skill has ALREADY been loaded - follow the instructions directly instead of calling this tool again
+ `;
+   });
+ });

+++ Added SFY (pretty-v2.1.26.js:334244-334250)
+ function SFY(A) {
+   try {
+     return IFY(A);
+   } catch {
+     return null;
+   }
+ }

+++ Added VZ1 (pretty-v2.1.26.js:340709-340741)
+ function VZ1(A) {
+   let K = s(8),
+     { hookEvent: q, messages: Y, toolUseID: z } = A,
+     w = vR7(Y, z, q);
+   if (ER7(Y, z, q) === w) return null;
+   let J;
+   if (K[0] === Symbol.for("react.memo_cache_sentinel"))
+     ((J = XS.createElement(V, { dimColor: !0 }, "Running ")), (K[0] = J));
+   else J = K[0];
+   let O;
+   if (K[1] !== q)
+     ((O = XS.createElement(V, { dimColor: !0, bold: !0 }, q)),
+       (K[1] = q),
+       (K[2] = O));
+   else O = K[2];
+   let X = w === 1 ? " hook…" : " hooks…",
+     $;
+   if (K[3] !== X)
+     (($ = XS.createElement(V, { dimColor: !0 }, X)), (K[3] = X), (K[4] = $));
+   else $ = K[4];
+   let _;
+   if (K[5] !== O || K[6] !== $)
+     ((_ = XS.createElement(
+       C6,
+       null,
+       XS.createElement(S, { flexDirection: "row" }, J, O, $),
+     )),
+       (K[5] = O),
+       (K[6] = $),
+       (K[7] = _));
+   else _ = K[7];
+   return _;
+ }

+++ Added D8K (pretty-v2.1.26.js:420203-420209)
+ function D8K() {
+   if (ajA)
+     ((It = ajA), h(`[TeammateModeSnapshot] Captured from CLI override: ${It}`));
+   else
+     ((It = M1().teammateMode ?? "auto"),
+       h(`[TeammateModeSnapshot] Captured from config: ${It}`));
+ }

+++ Added X3K (pretty-v2.1.26.js:443472-443625)
+ var X3K = E(() => {
+   ((TM2 = `Use this tool proactively when you're about to start a non-trivial implementation task. Getting user sign-off on your approach before writing code prevents wasted effort and ensures alignment. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
+    - If you would use ${IJ} to clarify the approach, use EnterPlanMode instead
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
+ 5. Use ${IJ} if you need to clarify approaches
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
+     (WoH = `Use this tool when a task has genuine ambiguity about the right approach and getting user input before coding would prevent significant rework. This tool transitions you into plan mode where you can explore the codebase and design an implementation approach for user approval.
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
+ When in doubt, prefer starting work and using ${IJ} for specific questions over entering a full planning phase.
+ 
+ ## What Happens in Plan Mode
+ 
+ In plan mode, you'll:
+ 1. Explore the codebase using Glob, Grep, and Read tools
+ 2. Understand existing patterns and architecture
+ 3. Design an implementation approach
+ 4. Present your plan to the user for approval
+ 5. Use ${IJ} if you need to clarify approaches
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

+++ Added nP2 (pretty-v2.1.26.js:450139-450168)
+   nP2 = `[SUGGESTION MODE: Suggest what the user might naturally type next into Claude Code.]
+ 
+ FIRST: Look at the user's recent messages and original request.
+ 
+ Your job is to predict what THEY would type - not what you think they should do.
+ 
+ THE TEST: Would they think "I was just about to type that"?
+ 
+ EXAMPLES:
+ User asked "fix the bug and run tests", bug is fixed → "run the tests"
+ After code written → "try it out"
+ Claude offers options → suggest the one the user would likely pick, based on conversation
+ Claude asks to continue → "yes" or "go ahead"
+ Task complete, obvious follow-up → "commit this" or "push it"
+ After error or misunderstanding → silence (let them assess/correct)
+ 
+ Be specific: "run the tests" beats "continue".
+ 
+ NEVER SUGGEST:
+ - Evaluative ("looks good", "thanks")
+ - Questions ("what about...?")
+ - Claude-voice ("Let me...", "I'll...", "Here's...")
+ - New ideas they didn't ask about
+ - Multiple sentences
+ 
+ Stay silent if the next step isn't obvious from what the user said.
+ 
+ Format: 2-12 words, match the user's style. Or nothing.
+ 
+ Reply with ONLY the suggestion, no quotes or explanation.`,

+++ Added rP2 (pretty-v2.1.26.js:450169-450182)
+   rP2 = `[SUGGESTION MODE]
+ 
+ TASK: Find a stated next step in the user's messages. Return it, or nothing.
+ 
+ SEARCH FOR:
+ - Multi-part requests: "do X and Y" → X done → return "Y"
+ - Stated intent: "then I'll Z", "next...", "after that..." → return "Z"
+ - Answer to Claude's question → return "yes" / "go ahead" / obvious choice
+ 
+ NOTHING FOUND → return nothing.
+ This is correct most of the time. Only return text you can trace to the user's stated plan.
+ 
+ 2-12 words. User's phrasing. Never evaluate, never Claude-voice.
+ Output ONLY the suggestion, or nothing.`,

+++ Added z$K (pretty-v2.1.26.js:490959-490981)
+ async function z$K() {
+   let A = v9A();
+   if (A.size === 0)
+     return { success: !0, message: "No enabled plugins to disable" };
+   let K = [],
+     q = [];
+   for (let [Y] of A) {
+     let z = await qB6(Y, !1);
+     if (z.success) K.push(Y);
+     else q.push(`${Y}: ${z.message}`);
+   }
+   if (q.length > 0)
+     return {
+       success: !1,
+       message: `Disabled ${K.length} plugin${K.length === 1 ? "" : "s"}, ${q.length} failed:
+ ${q.join(`
+ `)}`,
+     };
+   return {
+     success: !0,
+     message: `Disabled ${K.length} plugin${K.length === 1 ? "" : "s"}`,
+   };
+ }

+++ Added Gg6 (pretty-v2.1.26.js:517673-517967)
+ class Gg6 {
+   ws = null;
+   connected = !1;
+   authenticated = !1;
+   connecting = !1;
+   reconnectTimer = null;
+   reconnectAttempts = 0;
+   pendingCalls = new Map();
+   notificationHandler = null;
+   context;
+   permissionMode = "ask";
+   allowedDomains;
+   tabsContextCollectionTimeoutMs = 2000;
+   toolCallTimeoutMs = 120000;
+   constructor(A) {
+     if (((this.context = A), A.initialPermissionMode))
+       this.permissionMode = A.initialPermissionMode;
+   }
+   async ensureConnected() {
+     let { logger: A, serverName: K } = this.context;
+     if (
+       (A.info(
+         `[${K}] ensureConnected called, connected=${this.connected}, authenticated=${this.authenticated}, wsState=${this.ws?.readyState}`,
+       ),
+       this.connected && this.authenticated && this.ws?.readyState === bM.OPEN)
+     )
+       return (A.info(`[${K}] Already connected and authenticated`), !0);
+     if (!this.connecting)
+       (A.info(`[${K}] Not connecting, starting connection...`),
+         await this.connect());
+     else A.info(`[${K}] Already connecting, waiting...`);
+     return new Promise((q) => {
+       let Y = setTimeout(() => {
+           (A.info(
+             `[${K}] Connection timeout, connected=${this.connected}, authenticated=${this.authenticated}`,
+           ),
+             q(!1));
+         }, 1e4),
+         z = () => {
+           if (this.connected && this.authenticated)
+             (A.info(`[${K}] Connection successful`), clearTimeout(Y), q(!0));
+           else if (!this.connecting)
+             (A.info(`[${K}] No longer connecting, giving up`),
+               clearTimeout(Y),
+               q(!1));
+           else setTimeout(z, 200);
+         };
+       z();
+     });
+   }
+   async callTool(A, K) {
+     let { logger: q, serverName: Y } = this.context;
+     if (!this.ws || this.ws.readyState !== bM.OPEN)
+       throw Error(`[${Y}] Bridge not connected`);
+     let z = crypto.randomUUID(),
+       w = A === "tabs_context_mcp";
+     return new Promise((H, J) => {
+       let O = setTimeout(
+         () => {
+           let $ = this.pendingCalls.get(z);
+           if ($)
+             if ((this.pendingCalls.delete(z), w && $.results.length > 0))
+               H(this.mergeTabsResults($.results));
+             else J(Error(`[${Y}] Tool call timed out: ${A}`));
+         },
+         w ? this.tabsContextCollectionTimeoutMs : this.toolCallTimeoutMs,
+       );
+       this.pendingCalls.set(z, {
+         resolve: H,
+         reject: J,
+         timer: O,
+         results: [],
+         isTabsContext: w,
+       });
+       let X = {
+         type: "tool_call",
+         tool_use_id: z,
+         client_type: this.context.clientTypeId,
+         tool: A,
+         args: K,
+         permission_mode: this.permissionMode,
+       };
+       if (this.allowedDomains?.length) X.allowed_domains = this.allowedDomains;
+       (q.debug(`[${Y}] Sending tool_call: ${A} (${z.slice(0, 8)})`),
+         this.ws.send(JSON.stringify(X)));
+     });
+   }
+   isConnected() {
+     return (
+       this.connected && this.authenticated && this.ws?.readyState === bM.OPEN
+     );
+   }
+   disconnect() {
+     this.cleanup();
+   }
+   setNotificationHandler(A) {
+     this.notificationHandler = A;
+   }
+   async setPermissionMode(A, K) {
+     ((this.permissionMode = A), (this.allowedDomains = K));
+   }
+   async connect() {
+     let { logger: A, serverName: K, bridgeConfig: q } = this.context;
+     if (!q) {
+       A.error(`[${K}] No bridge config provided`);
+       return;
+     }
+     if (this.connecting) return;
+     ((this.connecting = !0), (this.authenticated = !1), this.closeSocket());
+     let Y, z;
+     if (q.devUserId) Y = q.devUserId;
+     else {
+       let H = await q.getUserId();
+       if (!H) {
+         (A.error(`[${K}] No user ID available`),
+           (this.connecting = !1),
+           this.context.onAuthenticationError?.());
+         return;
+       }
+       if (((Y = H), (z = await q.getOAuthToken()), !z)) {
+         (A.error(`[${K}] No OAuth token available`),
+           (this.connecting = !1),
+           this.context.onAuthenticationError?.());
+         return;
+       }
+     }
+     let w = `${q.url}/chrome/${Y}`;
+     A.info(`[${K}] Connecting to bridge: ${w}`);
+     try {
+       this.ws = new bM(w);
+     } catch (H) {
+       ((this.connecting = !1),
+         A.error(`[${K}] Failed to create WebSocket:`, H),
+         this.scheduleReconnect());
+       return;
+     }
+     (this.ws.on("open", () => {
+       A.info(`[${K}] WebSocket connected, sending connect`);
+       let H = { type: "connect", client_type: this.context.clientTypeId };
+       if (q.devUserId) H.dev_user_id = q.devUserId;
+       else H.oauth_token = z;
+       this.ws?.send(JSON.stringify(H));
+     }),
+       this.ws.on("message", (H) => {
+         try {
+           let J = JSON.parse(H.toString());
+           (A.debug(`[${K}] Bridge received: ${JSON.stringify(J)}`),
+             this.handleMessage(J));
+         } catch (J) {
+           A.error(`[${K}] Failed to parse message:`, J);
+         }
+       }),
+       this.ws.on("close", (H) => {
+         (A.info(`[${K}] Bridge connection closed (code: ${H})`),
+           (this.connected = !1),
+           (this.authenticated = !1),
+           (this.connecting = !1),
+           this.scheduleReconnect());
+       }),
+       this.ws.on("error", (H) => {
+         (A.error(`[${K}] Bridge WebSocket error: ${H.message}`),
+           (this.connected = !1),
+           (this.authenticated = !1),
+           (this.connecting = !1));
+       }));
+   }
+   handleMessage(A) {
+     let { logger: K, serverName: q } = this.context;
+     switch (A.type) {
+       case "paired":
+         (K.info(`[${q}] Paired with Chrome extension`),
+           (this.connected = !0),
+           (this.authenticated = !0),
+           (this.connecting = !1),
+           (this.reconnectAttempts = 0));
+         break;
+       case "waiting":
+         (K.info(`[${q}] Waiting for Chrome extension to connect`),
+           (this.connected = !0),
+           (this.authenticated = !0),
+           (this.connecting = !1),
+           (this.reconnectAttempts = 0));
+         break;
+       case "peer_connected":
+         K.info(`[${q}] Chrome extension connected`);
+         break;
+       case "peer_disconnected":
+         K.info(`[${q}] Chrome extension disconnected`);
+         break;
+       case "ping":
+         this.ws?.send(JSON.stringify({ type: "pong" }));
+         break;
+       case "pong":
+         break;
+       case "tool_result":
+         this.handleToolResult(A);
+         break;
+       case "notification":
+         if (this.notificationHandler)
+           this.notificationHandler({ method: A.method, params: A.params });
+         break;
+       case "error":
+         K.error(`[${q}] Bridge error: ${A.error}`);
+         break;
+       default:
+         K.debug(`[${q}] Unknown bridge message type: ${A.type}`);
+     }
+   }
+   handleToolResult(A) {
+     let K = A.tool_use_id;
+     if (!K) return;
+     let q = this.pendingCalls.get(K);
+     if (!q) return;
+     let Y = this.normalizeBridgeResponse(A);
+     if (q.isTabsContext) q.results.push(Y);
+     else (clearTimeout(q.timer), this.pendingCalls.delete(K), q.resolve(Y));
+   }
+   normalizeBridgeResponse(A) {
+     if (A.result || A.error) return A;
+     if (A.content) {
+       if (A.is_error) return { error: { content: A.content } };
+       return { result: { content: A.content } };
+     }
+     return A;
+   }
+   mergeTabsResults(A) {
+     let K = [];
+     for (let q of A) {
+       let w = q.result?.content;
+       if (!w || !Array.isArray(w)) continue;
+       for (let H of w)
+         if (H.type === "text" && H.text)
+           try {
+             let J = JSON.parse(H.text);
+             if (Array.isArray(J)) K.push(...J);
+             else if (J?.availableTabs && Array.isArray(J.availableTabs))
+               K.push(...J.availableTabs);
+           } catch {}
+     }
+     if (K.length > 0) {
+       let q = K.map((Y) => {
+         let z = Y;
+         return `  • tabId ${z.tabId}: "${z.title}" (${z.url})`;
+       }).join(`
+ `);
+       return {
+         result: {
+           content: [
+             { type: "text", text: JSON.stringify({ availableTabs: K }) },
+             {
+               type: "text",
+               text: `
+ 
+ Tab Context:
+ - Available tabs:
+ ${q}`,
+             },
+           ],
+         },
+       };
+     }
+     return A[0];
+   }
+   scheduleReconnect() {
+     let { logger: A, serverName: K } = this.context;
+     if (this.reconnectTimer) return;
+     if ((this.reconnectAttempts++, this.reconnectAttempts > 100)) {
+       (A.info(`[${K}] Giving up bridge reconnection after 100 attempts`),
+         (this.reconnectAttempts = 0));
+       return;
+     }
+     let q = Math.min(2000 * Math.pow(1.5, this.reconnectAttempts - 1), 30000);
+     if (this.reconnectAttempts <= 10 || this.reconnectAttempts % 10 === 0)
+       A.info(
+         `[${K}] Bridge reconnecting in ${Math.round(q)}ms (attempt ${this.reconnectAttempts})`,
+       );
+     this.reconnectTimer = setTimeout(() => {
+       ((this.reconnectTimer = null), this.connect());
+     }, q);
+   }
+   closeSocket() {
+     if (this.ws)
+       (this.ws.removeAllListeners(), this.ws.close(), (this.ws = null));
+     ((this.connected = !1), (this.authenticated = !1));
+   }
+   cleanup() {
+     if (this.reconnectTimer)
+       (clearTimeout(this.reconnectTimer), (this.reconnectTimer = null));
+     for (let [A, K] of this.pendingCalls)
+       (clearTimeout(K.timer),
+         K.reject(Error("Bridge client disconnected")),
+         this.pendingCalls.delete(A));
+     (this.closeSocket(), (this.reconnectAttempts = 0));
+   }
+ }

+++ Added kMK (pretty-v2.1.26.js:519445-519447)
+ function kMK(A) {
+   return new EMK(A);
+ }

+++ Added oF2 (pretty-v2.1.26.js:519519-519525)
+ async function oF2(A, K) {
+   let q = ["ask", "skip_all_permission_checks", "follow_a_plan"],
+     Y = K.mode,
+     z = Y && q.includes(Y) ? Y : "ask";
+   if (A.setPermissionMode) await A.setPermissionMode(z, K.allowed_domains);
+   return { content: [{ type: "text", text: `Permission mode set to: ${z}` }] };
+ }

+++ Added eF2 (pretty-v2.1.26.js:519728-519730)
+ function eF2() {
+   return [tF2];
+ }

+++ Added BMK (pretty-v2.1.26.js:519770-519772)
+ async function BMK(A, K) {
+   return (await uMK(A, K)).isInstalled;
+ }

+++ Added tF2 (pretty-v2.1.26.js:519773-519773)
+ var tF2 = "fcoeoabgfenejglbffodgkkbkcdhcgfn";

+++ Added qc (pretty-v2.1.26.js:519952-519962)
+ async function qc() {
+   let A = Sw7();
+   if (A.length === 0)
+     return (
+       h(
+         `[Claude in Chrome] Unsupported platform for extension detection: ${o6()}`,
+       ),
+       !1
+     );
+   return BMK(A, h);
+ }

+++ Added Tp2 (pretty-v2.1.26.js:525143-525145)
+ function Tp2() {
+   return null;
+ }

+++ Added od2 (pretty-v2.1.26.js:529763-529765)
+ function od2(A) {
+   return A.startsWith(aT1());
+ }

+++ Added jTK (pretty-v2.1.26.js:536627-536627)
+   jTK = !1;

+++ Added do2 (pretty-v2.1.26.js:549253-549255)
+ function do2(A) {
+   return A;
+ }

+++ Added lo2 (pretty-v2.1.26.js:549591-549593)
+ function lo2(A, K) {
+   return { ...A, idx: K };
+ }

+++ Added io2 (pretty-v2.1.26.js:549594-549597)
+ function io2(A, K) {
+   if (A.isIdle !== K.isIdle) return A.isIdle ? 1 : -1;
+   return 0;
+ }

+++ Added ja2 (pretty-v2.1.26.js:550464-550464)
+   ja2 = (A) => () => {},

+++ Added LkK (pretty-v2.1.26.js:550465-550465)
+   LkK = () => !1;

+++ Added TCK (pretty-v2.1.26.js:553104-553104)
+   TCK = 2,

+++ Added Es2 (pretty-v2.1.26.js:555209-555209)
+   Es2 = (A) => () => {},

+++ Added iCK (pretty-v2.1.26.js:555210-555210)
+   iCK = () => !1,

+++ Added Ls2 (pretty-v2.1.26.js:555451-555451)
+ var Ls2 = 2000,

+++ Added pRK (pretty-v2.1.26.js:560215-560244)
+ function pRK(A, K, q) {
+   let Y = s(7);
+   vcA.useRef(void 0);
+   let z;
+   if (Y[0] !== A || Y[1] !== K)
+     ((z = [A, K]), (Y[0] = A), (Y[1] = K), (Y[2] = z));
+   else z = Y[2];
+   vcA.useEffect(bt2, z);
+   let w, H;
+   if (Y[3] !== A || Y[4] !== q)
+     ((w = () => {
+       let J = A.find(ht2);
+       if (!J) return;
+       FI(
+         "set_permission_mode",
+         {
+           mode:
+             q === "bypassPermissions" ? "skip_all_permission_checks" : "ask",
+         },
+         J,
+       );
+     }),
+       (H = [A, q]),
+       (Y[3] = A),
+       (Y[4] = q),
+       (Y[5] = w),
+       (Y[6] = H));
+   else ((w = Y[5]), (H = Y[6]));
+   vcA.useEffect(w, H);
+ }

+++ Added ht2 (pretty-v2.1.26.js:560245-560247)
+ function ht2(A) {
+   return A.type === "connected" && A.name === SC;
+ }

+++ Added tbK (pretty-v2.1.26.js:562380-562380)
+ var tbK = () => {};

+++ Added YAz (pretty-v2.1.26.js:565807-565807)
+   YAz = () => {},

+++ Added $BK (pretty-v2.1.26.js:569144-569154)
+ async function $BK() {
+   try {
+     let A = await z$K();
+     if (!A.success) throw Error(A.message);
+     (console.log(`${eA.tick} ${A.message}`),
+       n("tengu_plugin_disabled_all_cli", {}),
+       process.exit(0));
+   } catch (A) {
+     FVA(A, "disable all plugins");
+   }
+ }

+++ Added Tc (pretty-v2.1.26.js:569574-569574)
+   Tc = null,

+++ Added Zk1 (pretty-v2.1.26.js:569575-569575)
+   Zk1 = null,

+++ Added R1z (pretty-v2.1.26.js:570914-570920)
+ function R1z(A) {
+   let K = A.protocol === "wss:" ? "https:" : "http:",
+     q = A.pathname;
+   if (((q = q.replace("/ws/", "/session/")), !q.endsWith("/events")))
+     q = q.endsWith("/") ? q + "events" : q + "/events";
+   return `${K}//${A.host}${q}${A.search}`;
+ }

+++ Added gcA (pretty-v2.1.26.js:570921-570921)
+ var gcA = 10,

+++ Added C1z (pretty-v2.1.26.js:570922-570922)
+   C1z = 500,

+++ Added L1z (pretty-v2.1.26.js:570923-570923)
+   L1z = 8000,

+++ Added YmK (pretty-v2.1.26.js:570925-570987)
+ var YmK = E(() => {
+   r3();
+   fp6();
+   G1();
+   Bj();
+   Ja();
+   Np6 = class Np6 extends mcA {
+     postUrl;
+     constructor(A, K = {}, q) {
+       super(A, K, q);
+       ((this.postUrl = R1z(A)),
+         h(`HybridTransport: POST URL = ${this.postUrl}`),
+         M8("info", "cli_hybrid_transport_initialized"));
+     }
+     async write(A) {
+       let K = $f();
+       if (!K) {
+         (h("HybridTransport: No session token available for POST"),
+           M8("warn", "cli_hybrid_post_no_token"));
+         return;
+       }
+       let q = {
+         Authorization: `Bearer ${K}`,
+         "Content-Type": "application/json",
+       };
+       for (let Y = 1; Y <= gcA; Y++) {
+         try {
+           let w = await K8.post(
+             this.postUrl,
+             { events: [A] },
+             { headers: q, validateStatus: () => !0 },
+           );
+           if (w.status === 200 || w.status === 201) {
+             h(`HybridTransport: POST success type=${A.type}`);
+             return;
+           }
+           if (w.status >= 400 && w.status < 500 && w.status !== 429) {
+             (h(
+               `HybridTransport: POST returned ${w.status} (client error), not retrying`,
+             ),
+               M8("warn", "cli_hybrid_post_client_error", { status: w.status }));
+             return;
+           }
+           (h(`HybridTransport: POST returned ${w.status}, attempt ${Y}/${gcA}`),
+             M8("warn", "cli_hybrid_post_retryable_error", {
+               status: w.status,
+               attempt: Y,
+             }));
+         } catch (w) {
+           (h(`HybridTransport: POST error: ${w.message}, attempt ${Y}/${gcA}`),
+             M8("warn", "cli_hybrid_post_network_error", { attempt: Y }));
+         }
+         if (Y === gcA) {
+           (h(`HybridTransport: POST failed after ${gcA} attempts, continuing`),
+             M8("warn", "cli_hybrid_post_retries_exhausted"));
+           return;
+         }
+         let z = Math.min(C1z * Math.pow(2, Y - 1), L1z);
+         await new Promise((w) => setTimeout(w, z));
+       }
+     }
+   };
+ });

+++ Added $mK (pretty-v2.1.26.js:571624-571626)
+ var $mK = E(() => {
+   G1();
+ });

+++ Added jmK (pretty-v2.1.26.js:571691-571693)
+ var jmK = E(() => {
+   HS();
+ });

+++ Added amK (pretty-v2.1.26.js:574961-574967)
+ var amK = E(() => {
+   cM();
+   $$();
+   i6();
+   b1();
+   l1();
+ });

+++ Added Wc2 (pretty-v2.1.26.js:578427-578429)
+ function Wc2() {
+   return;
+ }

+++ Added Dc2 (pretty-v2.1.26.js:578430-578432)
+ function Dc2() {
+   return j1(process.env.USE_LOCAL_OAUTH) || j1(process.env.LOCAL_BRIDGE);
+ }

+++ Added SfK (pretty-v2.1.26.js:578433-578475)
+ async function SfK() {
+   HVA();
+   let A = new hfK(),
+     K = Wc2();
+   A.info(`Bridge URL: ${K ?? "none (using native socket)"}`);
+   let q = {
+       serverName: "Claude in Chrome",
+       logger: A,
+       socketPath: I01(),
+       getSocketPaths: uw7,
+       clientTypeId: "claude-code",
+       onAuthenticationError: () => {
+         A.warn(
+           "Authentication error occurred. Please ensure you are logged into the Claude browser extension.",
+         );
+       },
+       onToolCallDisconnected: () => {
+         return `Browser extension is not connected. Please ensure the Claude browser extension is installed and running (${Gc2}). If this is your first time connecting to Chrome, you may need to restart Chrome for the installation to take effect. If you continue to experience issues, please report a bug: ${Zc2}`;
+       },
+       ...(K && {
+         bridgeConfig: {
+           url: K,
+           getUserId: async () => {
+             return M1().oauthAccount?.accountUuid;
+           },
+           getOAuthToken: async () => {
+             return jK()?.accessToken ?? "";
+           },
+           ...(Dc2() && { devUserId: "dev_user_local" }),
+         },
+       }),
+       ...(process.env.CLAUDE_CHROME_PERMISSION_MODE && {
+         initialPermissionMode: process.env.CLAUDE_CHROME_PERMISSION_MODE,
+       }),
+     },
+     Y = Pg6(q),
+     z = new UdA();
+   (process.stdin.on("end", () => process.exit(0)),
+     process.stdin.on("error", () => process.exit(0)),
+     h("[Claude in Chrome] Starting MCP server"),
+     await Y.connect(z),
+     h("[Claude in Chrome] MCP server started"));
+ }

=== Structural Changes ===

@@@ class 'vMK' (was 'lNK') — structural (99.0%)
--- pretty-v2.1.25.js:522370
+++ pretty-v2.1.26.js:519007
@@ -193,6 +193,7 @@
       );
     }
   }
+  async setPermissionMode(A, K) {}
   isConnected() {
     return this.connected;
   }

@@@ variable 'xZ' (was 'gZ') — structural (97.6%)
--- pretty-v2.1.25.js:212388
+++ pretty-v2.1.26.js:212472
@@ -13,6 +13,7 @@
   hD();
   Z1();
   dj();
+  Ur();
   ((cu4 = o(CSA(), 1)),
     (IR9 = new Set([
       ".md",

@@@ variable 'ZNK' (was 'IkK') — structural (97.2%)
--- pretty-v2.1.25.js:536641
+++ pretty-v2.1.26.js:533335
@@ -18,7 +18,6 @@
   G_();
   IG();
   IcA();
-  b1();
   ScA = class ScA extends Error {
     constructor(A) {
       super(A);

@@@ class 'EMK' (was 'iNK') — structural (96.8%)
--- pretty-v2.1.25.js:522645
+++ pretty-v2.1.26.js:519283
@@ -38,6 +38,10 @@
       );
     return Y[0].callTool(A, K);
   }
+  async setPermissionMode(A, K) {
+    let q = this.getConnectedClients();
+    await Promise.all(q.map((Y) => Y.setPermissionMode(A, K)));
+  }
   isConnected() {
     return this.getConnectedClients().length > 0;
   }

@@@ variable 'w0' (was 'X0') — structural (96.3%)
--- pretty-v2.1.25.js:528053
+++ pretty-v2.1.26.js:524743
@@ -91,6 +91,7 @@
   NvK();
   TvK();
   GJ();
+  $J();
   ((rQ6 = z6(() => [
     w$K,
     VNK,

@@@ function 'dU2' (was 'Do2') — structural (96.0%)
--- pretty-v2.1.25.js:527163
+++ pretty-v2.1.26.js:523852
@@ -154,6 +154,7 @@
         ),
       ),
     ),
+    !1,
     $ &&
       G8.default.createElement(
         G8.default.Fragment,

@@@ function 'HU2' (was 'hr2') — structural (95.7%)
--- pretty-v2.1.25.js:525671
+++ pretty-v2.1.26.js:522356
@@ -78,7 +78,8 @@
         ? Math.ceil(
             (new Date(Z).getTime() - new Date(G).getTime()) / 86400000,
           ) + 1
-        : 0;
+        : 0,
+    M = A.totalSpeculationTimeSavedMs + (K?.totalSpeculationTimeSavedMs || 0);
   return {
     totalSessions: X,
     totalMessages: $,
@@ -93,5 +94,6 @@
     lastSessionDate: Z,
     peakActivityDay: W,
     peakActivityHour: D,
+    totalSpeculationTimeSavedMs: M,
   };
 }

@@@ function 'TmK' (was 'bUK') — structural (95.5%)
--- pretty-v2.1.25.js:574930
+++ pretty-v2.1.26.js:571756
@@ -29,6 +29,8 @@
       Y5(1));
     return;
   }
+  if (J.thinking === "disabled") J.maxThinkingTokens = 0;
+  else if (J.thinking === "adaptive") J.maxThinkingTokens = void 0;
   let O = e5z(A, J);
   if (J.outputFormat === "stream-json" && J.verbose)
     vP7((N) => {

@@@ function 'ks2' (was 'd4z') — structural (94.6%)
--- pretty-v2.1.25.js:557264
+++ pretty-v2.1.26.js:553995
@@ -323,7 +323,11 @@
     )
       T7(0);
   }
-  let Z6 = !1;
+  let G6 = nCK.useSyncExternalStore(
+    lCK?.subscribeToLoopModeChanges ?? Es2,
+    lCK?.isLoopModeActive ?? iCK,
+    iCK,
+  );
   function Z8() {
     if (b3.length > 1) return;
     if (!EY) return;
@@ -467,11 +471,7 @@
             return;
           }
         }
-        await qA(j1, {
-          setCursorOffset: VA,
-          clearBuffer: ZA,
-          resetHistory: dA,
-        });
+        await e(P1, { setCursorOffset: VA, clearBuffer: DA, resetHistory: cA });
       },
       [
         iA,
@@ -1129,6 +1129,7 @@
               viewingAgentColor: A6,
             }),
             F4.createElement(S, { flexGrow: 1, flexShrink: 1 }, v2),
+            null,
           ),
           F4.createElement(V, { color: x3.bgColor }, "─".repeat(S0)),
         )
@@ -1153,6 +1154,7 @@
             viewingAgentColor: A6,
           }),
           F4.createElement(S, { flexGrow: 1, flexShrink: 1 }, v2),
+          null,
         ),
     F4.createElement(oyK, {
       apiKeyStatus: z,

@@@ variable '$a1' (was 'Cs1') — structural (94.6%)
--- pretty-v2.1.25.js:130124
+++ pretty-v2.1.26.js:130144
@@ -14,7 +14,10 @@
             q?.debug(
               "@aws-sdk/credential-provider-ini - credential_source is EcsContainer",
             ),
-            async () => VLA.chain(w(z ?? {}), H(z))().then(Es1)
+            async () =>
+              iCA
+                .chain(w(z ?? {}), H(z))()
+                .then(Oa1)
           );
         },
         Ec2InstanceMetadata: async (z) => {

@@@ function 'RTK' (was 'lCK') — structural (94.5%)
--- pretty-v2.1.25.js:540580
+++ pretty-v2.1.26.js:537273
@@ -43,11 +43,12 @@
     M = Symbol.for("react.early_return_sentinel");
     A: {
       let N =
-        typeof O === "string"
-          ? O.trim()
-          : X && iCK(X)
-            ? X.text.trim()
-            : "(no prompt)";
+          typeof O === "string"
+            ? O.trim()
+            : X && yTK(X)
+              ? X.text.trim()
+              : "(no prompt)",
+        T = QnA(N);
       if (YP1(N)) {
         let T;
         if (K[17] !== Y || K[18] !== z)

@@@ function 'lwK' (was 'jXK') — structural (94.4%)
--- pretty-v2.1.25.js:470387
+++ pretty-v2.1.26.js:466486
@@ -7,11 +7,11 @@
     z = aY("tengu_disable_bypass_permissions_mode"),
     w = Y.permissions?.disableBypassPermissionsMode === "disable",
     H = z || w,
-    J = [];
+    J = [],
+    O;
   if (K) J.push("bypassPermissions");
   if (A) J.push(FR(A));
   if (Y.permissions?.defaultMode) J.push(Y.permissions.defaultMode);
-  let O;
   for (let X of J) {
     if (X === "bypassPermissions" && H) {
       if (z)

@@@ function 'OU2' (was 'xr2') — structural (93.8%)
--- pretty-v2.1.25.js:525805
+++ pretty-v2.1.26.js:522492
@@ -44,5 +44,6 @@
     lastSessionDate: H,
     peakActivityDay: J,
     peakActivityHour: X,
+    totalSpeculationTimeSavedMs: A.totalSpeculationTimeSavedMs,
   };
 }

@@@ variable 'UU' (was 'rU') — structural (93.6%)
--- pretty-v2.1.25.js:531167
+++ pretty-v2.1.26.js:527865
@@ -137,9 +137,9 @@
         .describe(
           "Number of days to retain chat transcripts (0 to disable cleanup)",
         ),
-      env: ma2
-        .optional()
-        .describe("Environment variables to set for Claude Code sessions"),
+      env: Gd2.optional().describe(
+        "Environment variables to set for Claude Code sessions",
+      ),
       attribution: U.object({
         commit: U.string()
           .optional()
@@ -161,9 +161,9 @@
         .describe(
           "Deprecated: Use attribution instead. Whether to include Claude's co-authored by attribution in commits and PRs (defaults to true)",
         ),
-      permissions: ga2
-        .optional()
-        .describe("Tool usage permissions configuration"),
+      permissions: Zd2.optional().describe(
+        "Tool usage permissions configuration",
+      ),
       model: U.string()
         .optional()
         .describe("Override the default model used by Claude Code"),
@@ -283,11 +283,17 @@
       syntaxHighlightingDisabled: U.boolean()
         .optional()
         .describe("Whether to disable syntax highlighting in diffs"),
+      terminalTitleFromRename: U.boolean()
+        .optional()
+        .describe(
+          "When true, terminal tab title is set from /rename and not auto-updated based on the conversation topic",
+        ),
       alwaysThinkingEnabled: U.boolean()
         .optional()
         .describe(
           "When false, thinking is disabled. When absent or true, thinking is enabled automatically for supported models.",
         ),
+      ...{},
       promptSuggestionEnabled: U.boolean()
         .optional()
         .describe(

@@@ function 'EdA' (was '$cA') — structural (93.5%)
--- pretty-v2.1.25.js:525402
+++ pretty-v2.1.26.js:522081
@@ -61,5 +61,7 @@
     longestSession: X,
     firstSessionDate: $,
     hourCounts: H,
+    totalSpeculationTimeSavedMs:
+      A.totalSpeculationTimeSavedMs + K.totalSpeculationTimeSavedMs,
   };
 }

@@@ function 'uh6' (was 'Qx6') — structural (93.4%)
--- pretty-v2.1.25.js:455417
+++ pretty-v2.1.26.js:451494
@@ -27,6 +27,9 @@
       case "SubagentStart":
         H = Y.agent_type;
         break;
+      case "SubagentStop":
+        H = Y.agent_type;
+        break;
       default:
         break;
     }

@@@ function 'wP2' (was 'Bk2') — structural (93.0%)
--- pretty-v2.1.25.js:450537
+++ pretty-v2.1.26.js:446569
@@ -217,6 +217,13 @@
       }),
     };
   }
+  if (vL4()) {
+    let R = EL4(A.name);
+    if (R)
+      ((N.mcp_server_name = R.serverName), (N.mcp_tool_name = R.mcpToolName));
+    let x = kL4(A.name, W);
+    if (x) N.skill_name = x;
+  }
   let T = Y.toolDecisions?.get(K);
   (bP6(T?.decision || "unknown", T?.source || "unknown"), MP7());
   let C = Date.now();
@@ -291,10 +298,7 @@
       ...(J ? { requestId: J } : {}),
     }),
       b57(A.name));
-    let F = aT(A) ? YM6(A.name) : null,
-      Q = b36(),
-      u = Q ? x36(A.name) : void 0,
-      d = Q ? u36(A.name, W) : void 0;
+    let F = lT(A) ? FD6(A.name) : null;
     uG("tool_result", {
       tool_name: jK(A.name),
       success: "true",
@@ -303,10 +307,6 @@
       tool_result_size_bytes: String(B),
       ...(T && { decision_source: T.source, decision_type: T.decision }),
       ...(F ? { mcp_server_scope: F } : {}),
-      ...(u
-        ? { mcp_server_name: u.serverName, mcp_tool_name: u.mcpToolName }
-        : {}),
-      ...(d ? { skill_name: d } : {}),
     });
     let r = R.data,
       c = [],
@@ -385,10 +385,7 @@
         ...(X ? { mcpServerBaseUrl: X } : {}),
         ...(J ? { requestId: J } : {}),
       });
-      let F = aT(A) ? YM6(A.name) : null,
-        Q = b36(),
-        u = Q ? x36(A.name) : void 0,
-        d = Q ? u36(A.name, W) : void 0;
+      let F = lT(A) ? FD6(A.name) : null;
       uG("tool_result", {
         tool_name: jK(A.name),
         use_id: K,
@@ -398,10 +395,6 @@
         ...(Object.keys(N).length > 0 && { tool_parameters: UA(N) }),
         ...(T && { decision_source: T.source, decision_type: T.decision }),
         ...(F ? { mcp_server_scope: F } : {}),
-        ...(u
-          ? { mcp_server_name: u.serverName, mcp_tool_name: u.mcpToolName }
-          : {}),
-        ...(d ? { skill_name: d } : {}),
       });
     }
     let y = KPA(R),

@@@ function 'wJ1' (was 'pJ1') — structural (92.9%)
--- pretty-v2.1.25.js:528736
+++ pretty-v2.1.26.js:525436
@@ -1,7 +1,6 @@
 function pJ1(A) {
-  let K = {};
-  process.env.CLAUDE_CODE_ENTRYPOINT;
-  let q = process.env.CLAUDE_CODE_EXTRA_BODY,
+  let K = {},
+    q = process.env.CLAUDE_CODE_EXTRA_BODY,
     Y = {};
   if (q)
     try {

@@@ class 'n51' (was 'S51') — structural (92.7%)
--- pretty-v2.1.25.js:176655
+++ pretty-v2.1.26.js:176679
@@ -155,7 +155,13 @@
             }
             W[j] = P;
             let C = Q04(P.styles),
-              R = C ? U04(P.styles) : P.styles;
+              x =
+                C !== null ||
+                P.styles.some(
+                  (y) => y.code.length >= GyA.length && y.code.startsWith(GyA),
+                )
+                  ? mJ4(P.styles)
+                  : P.styles;
             if (
               (I51(K, j, X + G, {
                 char: P.value,

@@@ variable 'l6' (was 'i6') — structural (92.5%)
--- pretty-v2.1.25.js:534378
+++ pretty-v2.1.26.js:531075
@@ -21,6 +21,7 @@
   B7();
   b1();
   tb6();
+  nS6();
   ((UEK = o(Yb(), 1)),
     (CcA = {
       allowedTools: [],

@@@ variable 'HPK' (was 'ETK') — structural (92.5%)
--- pretty-v2.1.25.js:524233
+++ pretty-v2.1.26.js:520910
@@ -9,6 +9,7 @@
   u5();
   x4();
   wz();
+  ZPA();
   Xh = o($A(), 1);
   vTK = {
     type: "local-jsx",

@@@ function 'vOK' (was 'n_K') — structural (92.4%)
--- pretty-v2.1.25.js:479171
+++ pretty-v2.1.26.js:475274
@@ -33,6 +33,7 @@
     c = p4(),
     [YA, e] = DP.useState({}),
     qA = o1.useRef(d),
+    JA = o1.useRef(d),
     [HA, _A] = DP.useState(!1),
     [a, JA] = DP.useState(null),
     {
@@ -107,6 +108,7 @@
             n("tengu_thinking_toggled", { enabled: fA }));
         },
       },
+      ...[],
       {
         id: "promptSuggestionEnabled",
         label: "Prompt suggestions",
@@ -561,13 +563,15 @@
       fA.push(
         `Set auto-update channel to ${O1.bold(Z?.autoUpdatesChannel ?? "latest")}`,
       );
+    if (Q !== e.current && !("model" in qA))
+      fA.push(`Set model to ${O1.bold(kk(Q))}`);
     if (fA.length > 0)
       A(
         fA.join(`
 `),
       );
     else A("Config dialog dismissed", { display: "system" });
-  }, [a, YA, O, j, f, Z?.autoUpdatesChannel, A]);
+  }, [_A, qA, O, Q, j, f, Z?.autoUpdatesChannel, void 0, A]);
   J6("confirm:no", vA, { context: "Settings", isActive: a === null });
   let RA = DP.useCallback(() => {
     let fA = VA[C];
@@ -910,10 +914,10 @@
                           PACKAGE_URL: "@anthropic-ai/claude-code",
                           README_URL:
                             "https://code.claude.com/docs/en/overview",
-                          VERSION: "2.1.25",
+                          VERSION: "2.1.26",
                           FEEDBACK_CHANNEL:
                             "https://github.com/anthropics/claude-code/issues",
-                          BUILD_TIME: "2026-01-29T20:32:59Z",
+                          BUILD_TIME: "2026-01-30T02:12:23Z",
                         }.VERSION,
                         onChoice: (fA) => {
                           if ((JA(null), q(!1), fA === "cancel")) return;
@@ -925,10 +929,10 @@
                               PACKAGE_URL: "@anthropic-ai/claude-code",
                               README_URL:
                                 "https://code.claude.com/docs/en/overview",
-                              VERSION: "2.1.25",
+                              VERSION: "2.1.26",
                               FEEDBACK_CHANNEL:
                                 "https://github.com/anthropics/claude-code/issues",
-                              BUILD_TIME: "2026-01-29T20:32:59Z",
+                              BUILD_TIME: "2026-01-30T02:12:23Z",
                             }.VERSION;
                           (v4("userSettings", LA),
                             W((SA) => ({ ...SA, ...LA })),

@@@ class 'IwK' (was 'KXK') — structural (92.2%)
--- pretty-v2.1.25.js:469042
+++ pretty-v2.1.26.js:465131
@@ -189,6 +189,14 @@
 `,
         { mode: 384 },
       );
+    else if (A.type === "speculation-accept")
+      Y.appendFileSync(
+        H,
+        FA(A) +
+          `
+`,
+        { mode: 384 },
+      );
     else {
       let J = await PB6(K);
       if (A.type === "queue-operation")

@@@ function 'rFA' (was 'xQA') — structural (91.9%)
--- pretty-v2.1.25.js:413129
+++ pretty-v2.1.26.js:409147
@@ -40,6 +40,7 @@
     options: K?.options ?? A.options,
     messages: K?.messages ?? A.messages,
     agentId: K?.agentId ?? HL(),
+    agentType: K?.agentType,
     queryTracking: {
       chainId: Wj2(),
       depth: (A.queryTracking?.depth ?? -1) + 1,

@@@ function 'hkK' (was 'iyK') — structural (91.9%)
--- pretty-v2.1.25.js:553801
+++ pretty-v2.1.26.js:550532
@@ -75,6 +75,6 @@
   return tcA.createElement(
     S,
     { paddingX: $, gap: 2 },
-    z && tcA.createElement(V, { dimColor: !0 }, z),
+    z && zYA.createElement(V, { dimColor: !0 }, zYA.createElement(T3, null, z)),
   );
 }

@@@ function 'Od2' (was 'ba2') — structural (91.4%)
--- pretty-v2.1.25.js:530724
+++ pretty-v2.1.26.js:527420
@@ -1,6 +1,5 @@
 async function ba2(A, K, q, Y) {
   if (q.abortController.signal.aborted) throw new y2();
-  process.env.CLAUDE_CODE_ENTRYPOINT;
   let z = await q.getAppState(),
     w = TS6(z.toolPermissionContext, A);
   if (w)

@@@ function 'vT' (was 'CT') — structural (91.3%)
--- pretty-v2.1.25.js:183068
+++ pretty-v2.1.26.js:183110
@@ -2,6 +2,8 @@
   if (_G4.default.stdout) return !0;
   let A = process.env.TERM_PROGRAM;
   if (A && Q69.includes(A)) return !0;
+  let K = process.env.LC_TERMINAL;
+  if (K && O$4.includes(K)) return !0;
   if (process.env.TERM?.includes("kitty")) return !0;
   return !1;
 }

@@@ function 'HM1' (was 'NP1') — structural (90.8%)
--- pretty-v2.1.25.js:409899
+++ pretty-v2.1.26.js:406016
@@ -58,7 +58,7 @@
     ((P = S3A.default.createElement(
       S,
       { paddingLeft: 2 },
-      S3A.default.createElement(PO, null, J),
+      X3A.default.createElement(DO, { dimColor: !0 }, J),
     )),
       (K[11] = J),
       (K[12] = P));

@@@ variable 'Mp6' (was 'Pc6') — structural (90.8%)
--- pretty-v2.1.25.js:573624
+++ pretty-v2.1.26.js:570379
@@ -2,6 +2,7 @@
   z7();
   uP6();
   LH();
+  G1();
   ((C50 = f7.object({
     tool_name: f7
       .string()

@@@ function 'zy6' (was 'XS6') — structural (90.5%)
--- pretty-v2.1.25.js:533547
+++ pretty-v2.1.26.js:530232
@@ -65,6 +65,15 @@
         reason: "Agent memory files are allowed for reading",
       },
     };
+  if (U96(A))
+    return {
+      behavior: "allow",
+      updatedInput: K,
+      decisionReason: {
+        type: "other",
+        reason: `${X7A()} files are allowed for reading`,
+      },
+    };
   let w = dv(w8(), "tasks") + FL;
   if (A === w.slice(0, -1) || A.startsWith(w))
     return {

@@@ variable 'Kj1' (was 'jM1') — structural (90.2%)
--- pretty-v2.1.25.js:388865
+++ pretty-v2.1.26.js:384987
@@ -11,7 +11,6 @@
   rL6();
   ujA();
   CS();
-  B7();
   $R6 = o($A(), 1);
   vt7 = {
     type: "local-jsx",

@@@ function 'ZYA' (was 'bYA') — structural (89.9%)
--- pretty-v2.1.25.js:567489
+++ pretty-v2.1.26.js:564216
@@ -113,7 +113,7 @@
   (q8.useEffect(() => {
     mgK(yA);
   }, [yA]),
-    ehK(B1, yA),
+    pRK(F1, LA, C.mode),
     QSK(yA, Y));
   let T1 = $E1(z1, x.tools, C),
     K6 = q8.useMemo(() => {
@@ -620,8 +620,9 @@
         }
         let d3 = HJ(W1, F6, r6, f4, SK, h7);
         W5("query_context_loading_start");
-        let [, x5, Hw, YR] = await Promise.all([
+        let [, , bq, zw, KR] = await Promise.all([
           bd6(C, yA),
+          void 0,
           sf(K6, h7, Array.from(C.additionalWorkingDirectories.keys()), B1),
           AX(),
           e0(),

@@@ function 'f9A' (was 'p9A') — structural (89.4%)
--- pretty-v2.1.25.js:489880
+++ pretty-v2.1.26.js:485990
@@ -255,6 +255,179 @@
       { flexDirection: "column", gap: 1, padding: 1 },
       u4.default.createElement(
         V,
+        { color: "claude" },
+        "Authenticating with ",
+        A.name,
+        "…",
+      ),
+      e6.default.createElement(
+        S,
+        null,
+        e6.default.createElement(u7, null),
+        e6.default.createElement(
+          V,
+          null,
+          " A browser window will open for authentication",
+        ),
+      ),
+      C &&
+        e6.default.createElement(
+          S,
+          { flexDirection: "column" },
+          e6.default.createElement(
+            S,
+            null,
+            e6.default.createElement(
+              V,
+              { dimColor: !0 },
+              "If your browser doesn't open automatically, copy this URL manually",
+              " ",
+            ),
+            u
+              ? e6.default.createElement(V, { color: "success" }, "(Copied!)")
+              : e6.default.createElement(
+                  V,
+                  { dimColor: !0 },
+                  e6.default.createElement(D6, {
+                    shortcut: "c",
+                    action: "copy",
+                    parens: !0,
+                  }),
+                ),
+          ),
+          e6.default.createElement(q7, { url: C }),
+        ),
+      e6.default.createElement(
+        S,
+        { marginLeft: 3, flexDirection: "column" },
+        e6.default.createElement(
+          V,
+          { color: "permission" },
+          "Press ",
+          e6.default.createElement(V, { bold: !0 }, "Enter"),
+          " after authenticating in your browser.",
+        ),
+        e6.default.createElement(
+          V,
+          { dimColor: !0, italic: !0 },
+          e6.default.createElement(B6, {
+            action: "confirm:no",
+            context: "Confirmation",
+            fallback: "Esc",
+            description: "back",
+          }),
+        ),
+      ),
+    );
+  if (x)
+    return e6.default.createElement(
+      S,
+      { flexDirection: "column", gap: 1, padding: 1 },
+      e6.default.createElement(
+        V,
+        { color: "claude" },
+        "Clear authentication for ",
+        A.name,
+      ),
+      F
+        ? e6.default.createElement(
+            e6.default.Fragment,
+            null,
+            e6.default.createElement(
+              V,
+              null,
+              'Find the MCP server in the browser and click "Disconnect".',
+            ),
+            B &&
+              e6.default.createElement(
+                S,
+                { flexDirection: "column" },
+                e6.default.createElement(
+                  S,
+                  null,
+                  e6.default.createElement(
+                    V,
+                    { dimColor: !0 },
+                    "If your browser didn't open automatically, copy this URL manually",
+                    " ",
+                  ),
+                  u
+                    ? e6.default.createElement(
+                        V,
+                        { color: "success" },
+                        "(Copied!)",
+                      )
+                    : e6.default.createElement(
+                        V,
+                        { dimColor: !0 },
+                        e6.default.createElement(D6, {
+                          shortcut: "c",
+                          action: "copy",
+                          parens: !0,
+                        }),
+                      ),
+                ),
+                e6.default.createElement(q7, { url: B }),
+              ),
+            e6.default.createElement(
+              S,
+              { marginLeft: 3, flexDirection: "column" },
+              e6.default.createElement(
+                V,
+                { color: "permission" },
+                "Press ",
+                e6.default.createElement(V, { bold: !0 }, "Enter"),
+                " when done.",
+              ),
+              e6.default.createElement(
+                V,
+                { dimColor: !0, italic: !0 },
+                e6.default.createElement(B6, {
+                  action: "confirm:no",
+                  context: "Confirmation",
+                  fallback: "Esc",
+                  description: "back",
+                }),
+              ),
+            ),
+          )
+        : e6.default.createElement(
+            e6.default.Fragment,
+            null,
+            e6.default.createElement(
+              V,
+              null,
+              'This will open claude.ai in the browser. Find the MCP server in the list and click "Disconnect".',
+            ),
+            e6.default.createElement(
+              S,
+              { marginLeft: 3, flexDirection: "column" },
+              e6.default.createElement(
+                V,
+                { color: "permission" },
+                "Press ",
+                e6.default.createElement(V, { bold: !0 }, "Enter"),
+                " to open the browser.",
+              ),
+              e6.default.createElement(
+                V,
+                { dimColor: !0, italic: !0 },
+                e6.default.createElement(B6, {
+                  action: "confirm:no",
+                  context: "Confirmation",
+                  fallback: "Esc",
+                  description: "back",
+                }),
+              ),
+            ),
+          ),
+    );
+  if (j)
+    return e6.default.createElement(
+      S,
+      { flexDirection: "column", gap: 1, padding: 1 },
+      e6.default.createElement(
+        V,
         { color: "text" },
         "Connecting to ",
         u4.default.createElement(V, { bold: !0 }, A.name),
@@ -281,10 +454,17 @@
     yA.push({ label: "Enable", value: "toggle-enabled" });
   if (A.client.type === "connected" && K > 0)
     yA.push({ label: "View tools", value: "tools" });
-  if (r)
-    (yA.push({ label: "Re-authenticate", value: "reauth" }),
-      yA.push({ label: "Clear authentication", value: "clear-auth" }));
-  if (!r) yA.push({ label: "Authenticate", value: "auth" });
+  if (A.config.type === "claudeai-proxy") {
+    if (A.client.type === "connected")
+      LA.push({ label: "Clear authentication", value: "claudeai-clear-auth" });
+    else if (A.client.type !== "disabled")
+      LA.push({ label: "Authenticate", value: "claudeai-auth" });
+  } else {
+    if (o)
+      (LA.push({ label: "Re-authenticate", value: "reauth" }),
+        LA.push({ label: "Clear authentication", value: "clear-auth" }));
+    if (!o) LA.push({ label: "Authenticate", value: "auth" });
+  }
   if (A.client.type !== "disabled") {
     if (A.client.type !== "needs-auth")
       yA.push({ label: "Reconnect", value: "reconnectMcpServer" });

@@@ function 'YG7' (was 'aZ7') — structural (89.3%)
--- pretty-v2.1.25.js:303728
+++ pretty-v2.1.26.js:303817
@@ -1,5 +1,6 @@
 async function aZ7(A) {
   if (P1(process.env.CLAUDE_CODE_DISABLE_TERMINAL_TITLE)) return;
+  if (t_7) return;
   if (A.startsWith(`<${kzA}>`)) return;
   try {
     let q = (

@@@ variable 'SG' (was 'xG') — structural (89.1%)
--- pretty-v2.1.25.js:463517
+++ pretty-v2.1.26.js:459606
@@ -338,7 +338,7 @@
       }
       let P = $.toString(),
         f = _.toString();
-      if (G4("tengu_bash_haiku_prefetch", !0)) {
+      {
         let r = e7();
         IOK(A.command, P, r.signal, K.options.isNonInteractiveSession)
           .then(async (c) => {

@@@ variable 'dRK' (was 'AbK') — structural (89.0%)
--- pretty-v2.1.25.js:563457
+++ pretty-v2.1.26.js:560250
@@ -1,6 +1,8 @@
 var AbK = k(() => {
   cA();
   z7();
+  EI();
+  iM();
   ((YC1 = o($A(), 1)),
     (PFO = U.object({
       method: U.literal("notifications/message"),

@@@ function 'ZJ1' (was 'aJ1') — structural (88.9%)
--- pretty-v2.1.25.js:265613
+++ pretty-v2.1.26.js:265696
@@ -16,12 +16,10 @@
     : K.map((Y) => Y.name).join(`
 `);
   if (oo !== void 0 && q !== oo) {
-    let Y = oo
-        .split(
-          `
+    let Y = Fo.split(
+        `
 `,
-        )
-        .filter(Boolean).length,
+      ).filter(Boolean).length,
       z = q
         .split(
           `

@@@ variable 'j_' (was 'V_') — structural (88.9%)
--- pretty-v2.1.25.js:530861
+++ pretty-v2.1.26.js:527556
@@ -1,5 +1,9 @@
   V_ = async (A, K, q, Y, z) => {
     let w = await ba2(A, K, q, Y);
+    if (w.behavior === "allow") {
+      let H = await q.getAppState();
+      return w;
+    }
     if (w.behavior === "ask") {
       let H = await q.getAppState();
       if (H.toolPermissionContext.mode === "dontAsk")

@@@ function 'T0K' (was 'iGK') — structural (88.5%)
--- pretty-v2.1.25.js:484241
+++ pretty-v2.1.26.js:480349
@@ -29,7 +29,8 @@
       if (x.type === "User" && !x.isNested) u = "Saved in ~/.claude/CLAUDE.md";
       else if (x.type === "Project" && !x.isNested && x.path === O)
         u = `${d ? "Checked in at" : "Saved in"} ./CLAUDE.md`;
-      else if ((x.type, x.parent)) u = "@-imported";
+      else if ((x.type, x.type === "AutoMem")) u = `${X7A()} entrypoint`;
+      else if (x.parent) u = "@-imported";
       else if (x.isNested) u = "dynamically loaded";
       else u = "";
       return { label: Q, value: x.path, description: u };

@@@ function 'EvK' (was 'ULK') — structural (88.4%)
--- pretty-v2.1.25.js:545940
+++ pretty-v2.1.26.js:542635
@@ -286,11 +286,9 @@
             onCancel: () => N("default"),
           }),
         ),
-        e
-          .filter((qA) => qA.url)
-          .map((qA, HA) =>
-            a5.default.createElement(V, { key: HA, dimColor: !0 }, qA.url),
-          ),
+        YA.filter((e) => e.url).map((e, JA) =>
+          oq.default.createElement(V, { key: JA, dimColor: !0 }, e.url),
+        ),
         a5.default.createElement(V, { dimColor: !0 }, "← to go back"),
       ),
     );
@@ -443,7 +441,7 @@
           a5.default.createElement(
             V,
             { dimColor: !0 },
-            "Would you like to proceed?",
+            "Claude has written up a plan and is ready to execute. Would you like to proceed?",
           ),
           a5.default.createElement(
             S,

@@@ function 'SE1' (was 'nk1') — structural (88.3%)
--- pretty-v2.1.25.js:561224
+++ pretty-v2.1.26.js:557979
@@ -40,7 +40,9 @@
         (e) =>
           e.immediate &&
           e.isEnabled() &&
-          (e.name === r || e.aliases?.includes(r) || e.userFacingName() === r),
+          (YA.name === o ||
+            YA.aliases?.includes(o) ||
+            YA.userFacingName() === o),
       );
     if (YA && YA.type === "local-jsx") {
       (H(""), R(0), x());

@@@ function '_p6' (was 'Gc6') — structural (87.6%)
--- pretty-v2.1.25.js:572763
+++ pretty-v2.1.26.js:569515
@@ -25,7 +25,8 @@
     let J = H,
       X = {
         ddsource: "nodejs",
-        ddtags: W5z.filter(($) => J[$] !== void 0 && J[$] !== null)
+        ddtags: oAz
+          .filter(($) => J[$] !== void 0 && J[$] !== null)
           .map(($) => `${IQK($)}:${J[$]}`)
           .join(","),
         message: A,

@@@ variable 'Uv1' (was 'Yk1') — structural (87.5%)
--- pretty-v2.1.25.js:540805
+++ pretty-v2.1.26.js:537499
@@ -13,6 +13,7 @@
   uK();
   j$();
   wz();
+  Yz();
   ((h6 = o($A(), 1)), (CX = o($A(), 1)));
   ((bAz = [
     { value: "both", label: "Restore code and conversation" },

@@@ function 'mG1' (was 'fZ1') — structural (87.3%)
--- pretty-v2.1.25.js:334284
+++ pretty-v2.1.26.js:334344
@@ -53,7 +53,9 @@
         KA(H instanceof Error ? H : Error(String(H)));
       }
   } catch (z) {
-    KA(z instanceof Error ? z : Error(String(z)));
+    let w = z.code;
+    if (w !== "ENOENT" && w !== "EACCES" && w !== "EPERM")
+      KA(z instanceof Error ? z : Error(String(z)));
   }
   return Y;
 }

@@@ function 'aPA' (was 'kVA') — structural (87.2%)
--- pretty-v2.1.25.js:525494
+++ pretty-v2.1.26.js:522175
@@ -6,6 +6,7 @@
     J = [],
     O = new Map(),
     X = 0,
+    $ = 0,
     $ = {},
     _ = void 0,
     G = new Set(),
@@ -44,7 +45,9 @@
       }
       let T = Sr2(M, ".jsonl"),
         C = [];
-      for (let r of P) if (Pm(r)) C.push(r);
+      for (let c of f)
+        if (Gm(c)) R.push(c);
+        else if (c.type === "speculation-accept") $ += c.timeSavedMs;
       if (C.length === 0) continue;
       let R = C.filter((r) => !r.isSidechain);
       if (R.length === 0) continue;
@@ -122,6 +125,7 @@
     sessionStats: J,
     hourCounts: Object.fromEntries(O),
     totalMessages: X,
+    totalSpeculationTimeSavedMs: $,
     ...{},
   };
 }

@@@ function 'Yy6' (was 'OS6') — structural (87.2%)
--- pretty-v2.1.25.js:533497
+++ pretty-v2.1.26.js:530173
@@ -26,6 +26,15 @@
         reason: "Agent memory files are allowed for writing",
       },
     };
+  if (U96(A))
+    return {
+      behavior: "allow",
+      updatedInput: K,
+      decisionReason: {
+        type: "other",
+        reason: `${X7A()} files are allowed for writing`,
+      },
+    };
   let q = dv(w8(), "teams") + FL;
   if (A === q.slice(0, -1) || A.startsWith(q))
     return {

@@@ variable 'RMK' (was 'aNK') — structural (87.0%)
--- pretty-v2.1.25.js:522896
+++ pretty-v2.1.26.js:519545
@@ -1,4 +1,5 @@
 var aNK = async (A, K, q, Y) => {
+  if (q === "set_permission_mode") return oF2(K, Y);
   try {
     let z = await K.ensureConnected();
     if (

@@@ variable 'z7A' (was 'V7A') — structural (86.1%)
--- pretty-v2.1.25.js:209540
+++ pretty-v2.1.26.js:209595
@@ -6,7 +6,7 @@
   Gu4();
   CK();
   K7();
-  ((NL9 = [
+  $v9 = [
     "github.com:anthropics/claude-cli-internal",
     "github.com/anthropics/claude-cli-internal",
     "github.com:anthropics/anthropic",
@@ -19,16 +19,16 @@
     "github.com/anthropics/hex-export",
     "github.com:anthropics/feedback-v2",
     "github.com/anthropics/feedback-v2",
-  ]),
-    (TL9 = vx(async () => {
-      if (vSA !== null) return vSA;
-      let A = V8(),
-        K = await A7("git", ["remote", "get-url", "origin"], {
-          cwd: A,
-          timeout: 5000,
-        });
-      if (K.code !== 0) return ((vSA = !1), !1);
-      let q = K.stdout.trim();
-      return ((vSA = NL9.some((Y) => q.includes(Y))), vSA);
-    })));
+  ];
+  _v9 = Ex(async () => {
+    if (M$A !== null) return M$A;
+    let A = N8(),
+      K = await A7("git", ["remote", "get-url", "origin"], {
+        cwd: A,
+        timeout: 5000,
+      });
+    if (K.code !== 0) return ((M$A = !1), !1);
+    let q = K.stdout.trim();
+    return ((M$A = $v9.some((Y) => q.includes(Y))), M$A);
+  });
 });

@@@ variable 'Jz' (was 'Xz') — structural (86.0%)
--- pretty-v2.1.25.js:533637
+++ pretty-v2.1.26.js:530331
@@ -19,6 +19,7 @@
   Pa();
   xxA();
   l6();
+  i6();
   ((CEK = o(CSA(), 1)),
     (Ds2 = [
       ".gitconfig",

@@@ variable 'KK' (was 'B7') — structural (85.8%)
--- pretty-v2.1.25.js:532849
+++ pretty-v2.1.26.js:529525
@@ -23,7 +23,7 @@
       clientKey: vW8,
       attributes: A,
       remoteEval: !0,
-      cacheKeyAttributes: ["id"],
+      cacheKeyAttributes: ["id", "organizationUUID"],
       ...(Y.error ? {} : { apiHostRequestHeaders: Y.headers }),
       ...{},
     });

@@@ function 'svK' (was 'WRK') — structural (84.9%)
--- pretty-v2.1.25.js:549168
+++ pretty-v2.1.26.js:545865
@@ -22,10 +22,10 @@
               "report the issue at https://github.com/anthropics/claude-code/issues",
             PACKAGE_URL: "@anthropic-ai/claude-code",
             README_URL: "https://code.claude.com/docs/en/overview",
-            VERSION: "2.1.25",
+            VERSION: "2.1.26",
             FEEDBACK_CHANNEL:
               "https://github.com/anthropics/claude-code/issues",
-            BUILD_TIME: "2026-01-29T20:32:59Z",
+            BUILD_TIME: "2026-01-30T02:12:23Z",
           }.VERSION,
           D = Date.now() - G;
         if (Z.lockFailed) {
@@ -33,8 +33,7 @@
           return;
         }
         if ((J({ current: W, latest: Z.latestVersion }), Z.wasUpdated))
-          (u5A(),
-            n("tengu_native_auto_updater_success", { latency_ms: D }),
+          (n("tengu_native_auto_updater_success", { latency_ms: D }),
             q({ version: Z.latestVersion, status: "success" }));
         else n("tengu_native_auto_updater_up_to_date", { latency_ms: D });
       } catch (Z) {

@@@ function 'ZRK' (was 'EhK') — structural (84.7%)
--- pretty-v2.1.25.js:561863
+++ pretty-v2.1.26.js:558620
@@ -176,6 +176,12 @@
         for (let b of M) {
           let F = JP1(b.text);
           if (!F) continue;
+          if (!F.hostPattern?.host) {
+            h(
+              "[InboxPoller] Invalid sandbox permission request: missing hostPattern.host",
+            );
+            continue;
+          }
           B.push({
             requestId: F.requestId,
             workerId: F.workerId,
@@ -227,6 +233,12 @@
             );
             continue;
           }
+          if (!b.permissionUpdate?.rules || !b.permissionUpdate?.behavior) {
+            h(
+              "[InboxPoller] Invalid team permission update: missing permissionUpdate.rules or permissionUpdate.behavior",
+            );
+            continue;
+          }
           (h(
             `[InboxPoller] Applying team permission update: ${b.toolName} allowed in ${b.directoryPath}`,
           ),

@@@ function 'K1z' (was 'f5z') — structural (84.3%)
--- pretty-v2.1.25.js:572902
+++ pretty-v2.1.26.js:569655
@@ -2,7 +2,7 @@
   let q = c36(A);
   if (q === 0) return;
   let Y = q !== null ? { ...K, sample_rate: q } : K;
-  if ((Tb7(A, Y), xQK())) ky6(A, Y);
   if (uQK()) Gc6(A, Y);
+  if (EBK()) _p6(A, Y);
   i36(A, Y);
 }

@@@ function 'qu' — structural (83.3%)
--- pretty-v2.1.25.js:534344
+++ pretty-v2.1.26.js:531039
@@ -12,5 +12,7 @@
       return Um(yT(), "CLAUDE.md");
     case "ExperimentalUltraClaudeMd":
       return Um(w8(), "ULTRACLAUDE.md");
+    case "AutoMem":
+      return rb4();
   }
 }

@@@ function 'BUA' (was 'TpA') — structural (83.2%)
--- pretty-v2.1.25.js:464107
+++ pretty-v2.1.26.js:460196
@@ -20,7 +20,8 @@
       N;
     if (H.isSkillMode) N = f === void 0 ? !1 : P1(f);
     else N = P1(f);
-    let T = H.isSkillMode ? !0 : !1;
+    let T = J["user-invocable"],
+      R = !(H.isSkillMode ? (T === void 0 || T === null ? !0 : j1(T)) : !0);
     return {
       type: "prompt",
       name: A,

@@@ variable 'HZ1' (was 'dZ1') — structural (83.0%)
--- pretty-v2.1.25.js:426409
+++ pretty-v2.1.26.js:422428
@@ -71,11 +71,9 @@
         .describe(
           "Team name for spawning. Uses current team context if omitted.",
         ),
-      mode: pR8
-        .optional()
-        .describe(
-          'Permission mode for spawned teammate (e.g., "plan" to require plan approval).',
-        ),
+      mode: QC8.optional().describe(
+        'Permission mode for spawned teammate (e.g., "plan" to require plan approval).',
+      ),
     })),
     (N5K = RV2.merge(yV2)),
     ($I6 = EV1 ? N5K.omit({ run_in_background: !0 }) : N5K),
@@ -201,7 +199,8 @@
           }
         if (!B_6(N, r)) {
           let c = N.requiredMcpServers.filter(
-            (YA) => !r.some((e) => e.toLowerCase().includes(YA.toLowerCase())),
+            (qA) =>
+              !o.some((YA) => YA.toLowerCase().includes(qA.toLowerCase())),
           );
           throw Error(
             `Agent '${K}' requires MCP servers matching: ${c.join(", ")}. MCP servers with tools: ${r.length > 0 ? r.join(", ") : "none"}. Use /mcp to configure and authenticate the required MCP servers.`,
@@ -403,7 +402,21 @@
                           LA = fA.content
                             .filter((SA) => SA.type === "text")
                             .map((SA) => SA.text).join(`
-`);
+`),
+                          RA = await $.getAppState(),
+                          hA = await classifyHandoffIfNeeded({
+                            agentMessages: qA,
+                            toolPermissionContext: RA.toolPermissionContext,
+                            abortSignal: $A.abortController.signal,
+                            isNonInteractiveSession:
+                              $.options.isNonInteractiveSession,
+                            subagentType: K,
+                            totalToolUseCount: xA.totalToolUseCount,
+                          });
+                        if (hA)
+                          fA = `${hA}
+
+${fA}`;
                         (HP6(fA, $.setAppState),
                           rqA(VA, q, "completed", void 0, $.setAppState, LA));
                       } catch (vA) {

@@@ function 'Hx6' (was '_B6') — structural (83.0%)
--- pretty-v2.1.25.js:469402
+++ pretty-v2.1.26.js:465499
@@ -17,9 +17,7 @@
         if (!J || J.trim() === "") continue;
       }
     }
-    if (Y.match(/^<local-command-stdout>/)) continue;
-    if (Y.match(/^<session-start-hook>/)) continue;
-    if (Y.startsWith(`<${El}>`)) continue;
+    if (wE2.test(Y)) continue;
     let w = l7(Y, "bash-input");
     if (w) return `! ${w}`;
     return Y;

@@@ variable 'iDK' (was 'WfK') — structural (82.5%)
--- pretty-v2.1.25.js:515062
+++ pretty-v2.1.26.js:511390
@@ -78,9 +78,11 @@
       SubagentStop: {
         summary:
           "Right before a subagent (Task tool call) concludes its response",
-        description: `Exit code 0 - stdout/stderr not shown
+        description: `Input to command is JSON with agent_id, agent_type, and agent_transcript_path.
+Exit code 0 - stdout/stderr not shown
 Exit code 2 - show stderr to subagent and continue having it run
 Other exit codes - show stderr to user only`,
+        matcherMetadata: { fieldToMatch: "agent_type", values: [] },
       },
       PreCompact: {
         summary: "Before conversation compaction",

@@@ variable 'wgK' (was 'jpK') — structural (82.2%)
--- pretty-v2.1.25.js:581358
+++ pretty-v2.1.26.js:578225
@@ -179,7 +179,6 @@
   OpK();
   IG();
   IcA();
-  dj();
   qq = o($A(), 1);
   wK("main_tsx_entry");
   wK("main_tsx_imports_loaded");

@@@ function 'of' (was 'sf') — structural (82.0%)
--- pretty-v2.1.25.js:528460
+++ pretty-v2.1.26.js:525160
@@ -24,6 +24,7 @@
     ...(G4("tengu_system_prompt_global_cache", !1) ? [UUA] : []),
     no2(),
     ro2(),
+    Tp2(),
     J,
     oo2(O.language),
     ao2(H),

@@@ function 'xNK' (was 'skK') — structural (81.8%)
--- pretty-v2.1.25.js:537680
+++ pretty-v2.1.26.js:534373
@@ -15,9 +15,9 @@
         "report the issue at https://github.com/anthropics/claude-code/issues",
       PACKAGE_URL: "@anthropic-ai/claude-code",
       README_URL: "https://code.claude.com/docs/en/overview",
-      VERSION: "2.1.25",
+      VERSION: "2.1.26",
       FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-      BUILD_TIME: "2026-01-29T20:32:59Z",
+      BUILD_TIME: "2026-01-30T02:12:23Z",
     }.VERSION,
     integrations: [
       new YAA.Integrations.OnUncaughtException({
@@ -32,8 +32,8 @@
     beforeSend(K) {
       try {
         let q = rs();
-        if (q.userID) {
-          let Y = Ce2("sha256").update(q.userID).digest("hex");
+        if (q.deviceId) {
+          let Y = Yi2("sha256").update(q.deviceId).digest("hex");
           K.user = { id: Y };
         }
       } catch {}

@@@ variable 'C1' — structural (81.0%)
--- pretty-v2.1.25.js:5589
+++ pretty-v2.1.26.js:5598
@@ -6,6 +6,7 @@
   l6();
   b1();
   wz();
+  zR1();
   krA = [];
   RzA = [];
   b$z = z6(() => {

@@@ function 'jYA' (was 'BYA') — structural (80.8%)
--- pretty-v2.1.25.js:578813
+++ pretty-v2.1.26.js:575666
@@ -9,10 +9,5 @@
   )
     ZEK();
   let A = e7();
-  (setTimeout(() => A.abort(), 3000),
-    _aA(x1(), A.signal, []),
-    skK(),
-    ap(),
-    Nb7(),
-    BQK());
+  (setTimeout(() => A.abort(), 3000), LoA(x1(), A.signal, []), xNK(), kBK());
 }

@@@ function 'S1z' (was 'n5z') — structural (80.5%)
--- pretty-v2.1.25.js:575140
+++ pretty-v2.1.26.js:571968
@@ -3,7 +3,32 @@
     G = !1,
     Z = !1,
     W,
-    D = new rUA();
+    D = new OUA(),
+    j = (YA) => {
+      O((e) => {
+        let JA = YA(e),
+          OA = e.toolPermissionContext.mode,
+          a = JA.toolPermissionContext.mode;
+        if (
+          OA !== a &&
+          (a === "default" ||
+            a === "acceptEdits" ||
+            a === "bypassPermissions" ||
+            a === "plan" ||
+            a === "delegate" ||
+            a === "dontAsk")
+        )
+          D.enqueue({
+            type: "system",
+            subtype: "status",
+            status: null,
+            permissionMode: a,
+            uuid: ov(),
+            session_id: d1(),
+          });
+        return JA;
+      });
+    };
   if ($.enableAuthStatus)
     YN.getInstance().subscribe((e) => {
       D.enqueue({

@@@ variable 'mLK' (was 'rSK') — structural (80.5%)
--- pretty-v2.1.25.js:560560
+++ pretty-v2.1.26.js:557314
@@ -19,6 +19,7 @@
   t9();
   _MA();
   dQA();
+  YQA();
   ((iSK = o($A(), 1)), (M7z = ["Edit", "Write", "NotebookEdit"]));
   nSK = V7z;
 });

@@@ function 'CX4' (was 'I_4') — structural (80.4%)
--- pretty-v2.1.25.js:180613
+++ pretty-v2.1.26.js:180643
@@ -4,6 +4,7 @@
   if (
     A === "iTerm.app" ||
     A === "WezTerm" ||
+    A === "WarpTerminal" ||
     A === "ghostty" ||
     A === "contour" ||
     A === "vscode" ||
@@ -14,6 +15,7 @@
   if (K === "xterm-ghostty") return !0;
   if (K?.startsWith("foot")) return !0;
   if (K?.includes("alacritty")) return !0;
+  if (process.env.ZED_TERM) return !0;
   if (process.env.WT_SESSION) return !0;
   let q = process.env.VTE_VERSION;
   if (q) {

@@@ function 'SvK' (was 'rLK') — structural (80.3%)
--- pretty-v2.1.25.js:547245
+++ pretty-v2.1.26.js:543938
@@ -1,5 +1,5 @@
 function rLK(A) {
-  let K = s(90),
+  let K = s(92),
     {
       question: q,
       questions: Y,
@@ -223,7 +223,9 @@
             defaultValue: H[q.question]?.selectedValue,
             onChange: (LA) => {
               X(e, { selectedValue: LA }, !0);
-              let SA = LA.includes("__other__") ? H[e]?.textInputValue : void 0,
+              let hA = RA.includes("__other__")
+                  ? H[YA]?.textInputValue
+                  : void 0,
                 xA = LA.filter(j6z).concat(SA ? [SA] : []);
               $(e, xA, void 0, !1);
             },
@@ -284,26 +286,28 @@
       (K[61] = yA));
   else yA = K[61];
   let AA = P && N === 0 ? "suggestion" : void 0,
+    wA = JA.length + 1,
     wA;
-  if (K[62] !== AA)
-    ((wA = pY.default.createElement(V, { color: AA }, "Chat about this")),
+  if (K[62] !== AA || K[63] !== wA)
+    ((GA = FY.default.createElement(V, { color: AA }, wA, ". Chat about this")),
       (K[62] = AA),
-      (K[63] = wA));
-  else wA = K[63];
+      (K[63] = wA),
+      (K[64] = GA));
+  else GA = K[64];
   let GA;
-  if (K[64] !== yA || K[65] !== wA)
+  if (K[65] !== LA || K[66] !== GA)
     ((GA = pY.default.createElement(
       S,
       { flexDirection: "row", gap: 1 },
       yA,
       wA,
     )),
-      (K[64] = yA),
       (K[65] = wA),
-      (K[66] = GA));
-  else GA = K[66];
+      (K[66] = GA),
+      (K[67] = HA));
+  else HA = K[67];
   let OA;
-  if (K[67] !== N || K[68] !== P || K[69] !== M)
+  if (K[68] !== N || K[69] !== P || K[70] !== M || K[71] !== JA.length)
     ((OA =
       M &&
       pY.default.createElement(
@@ -315,23 +319,25 @@
         pY.default.createElement(
           V,
           { color: P && N === 1 ? "suggestion" : void 0 },
-          "Skip interview and plan immediately",
+          JA.length + 2,
+          ". Skip interview and plan immediately",
         ),
       )),
-      (K[67] = N),
       (K[68] = P),
       (K[69] = M),
-      (K[70] = OA));
-  else OA = K[70];
+      (K[70] = M),
+      (K[71] = JA.length),
+      (K[72] = t));
+  else t = K[72];
   let t;
-  if (K[71] !== GA || K[72] !== OA)
+  if (K[73] !== HA || K[74] !== t)
     ((t = pY.default.createElement(S, { flexDirection: "column" }, hA, GA, OA)),
-      (K[71] = GA),
-      (K[72] = OA),
-      (K[73] = t));
-  else t = K[73];
+      (K[73] = HA),
+      (K[74] = t),
+      (K[75] = $A));
+  else $A = K[75];
   let XA;
-  if (K[74] !== Y.length)
+  if (K[76] !== Y.length)
     ((XA =
       Y.length === 1
         ? pY.default.createElement(
@@ -343,11 +349,11 @@
             " to navigate",
           )
         : "Tab/Arrow keys to navigate"),
-      (K[74] = Y.length),
-      (K[75] = XA));
-  else XA = K[75];
+      (K[76] = Y.length),
+      (K[77] = VA));
+  else VA = K[77];
   let VA;
-  if (K[76] !== C)
+  if (K[78] !== C)
     ((VA =
       C &&
       y &&
@@ -357,11 +363,11 @@
         " · ctrl+g to edit in ",
         y,
       )),
-      (K[76] = C),
-      (K[77] = VA));
-  else VA = K[77];
+      (K[78] = C),
+      (K[79] = vA));
+  else vA = K[79];
   let vA;
-  if (K[78] !== XA || K[79] !== VA)
+  if (K[80] !== VA || K[81] !== vA)
     ((vA = pY.default.createElement(
       S,
       { marginTop: 1 },
@@ -376,17 +382,17 @@
         "· Esc to cancel",
       ),
     )),
-      (K[78] = XA),
-      (K[79] = VA),
-      (K[80] = vA));
-  else vA = K[80];
+      (K[80] = VA),
+      (K[81] = vA),
+      (K[82] = yA));
+  else yA = K[82];
   let RA;
   if (
-    K[81] !== JA ||
-    K[82] !== jA ||
     K[83] !== MA ||
     K[84] !== t ||
-    K[85] !== vA
+    K[85] !== ZA ||
+    K[86] !== $A ||
+    K[87] !== yA
   )
     ((RA = pY.default.createElement(
       S,
@@ -397,15 +403,15 @@
       t,
       vA,
     )),
-      (K[81] = JA),
-      (K[82] = jA),
       (K[83] = MA),
       (K[84] = t),
       (K[85] = vA),
-      (K[86] = RA));
-  else RA = K[86];
+      (K[86] = $A),
+      (K[87] = yA),
+      (K[88] = xA));
+  else xA = K[88];
   let fA;
-  if (K[87] !== RA || K[88] !== _A)
+  if (K[89] !== xA || K[90] !== OA)
     ((fA = pY.default.createElement(
       S,
       { flexDirection: "column", marginTop: 0 },
@@ -413,9 +419,9 @@
       a,
       RA,
     )),
-      (K[87] = RA),
-      (K[88] = _A),
-      (K[89] = fA));
-  else fA = K[89];
+      (K[89] = xA),
+      (K[90] = OA),
+      (K[91] = fA));
+  else fA = K[91];
   return fA;
 }

@@@ function 'rvK' (was '_RK') — structural (79.2%)
--- pretty-v2.1.25.js:548956
+++ pretty-v2.1.26.js:545655
@@ -15,9 +15,9 @@
             "report the issue at https://github.com/anthropics/claude-code/issues",
           PACKAGE_URL: "@anthropic-ai/claude-code",
           README_URL: "https://code.claude.com/docs/en/overview",
-          VERSION: "2.1.25",
+          VERSION: "2.1.26",
           FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-          BUILD_TIME: "2026-01-29T20:32:59Z",
+          BUILD_TIME: "2026-01-30T02:12:23Z",
         }.VERSION,
         _ = yq()?.autoUpdatesChannel ?? "latest",
         G = await l3A(_),
@@ -60,14 +60,13 @@
           else M = await jMA();
         }
         if ((K(!1), M === "success"))
-          (u5A(),
-            n("tengu_auto_updater_success", {
-              fromVersion: $,
-              toVersion: G,
-              durationMs: Date.now() - W,
-              wasMigrated: P === "local",
-              installationType: j,
-            }));
+          n("tengu_auto_updater_success", {
+            fromVersion: $,
+            toVersion: G,
+            durationMs: Date.now() - W,
+            wasMigrated: P === "local",
+            installationType: j,
+          });
         else
           n("tengu_auto_updater_fail", {
             fromVersion: $,
@@ -145,10 +144,10 @@
                   "report the issue at https://github.com/anthropics/claude-code/issues",
                 PACKAGE_URL: "@anthropic-ai/claude-code",
                 README_URL: "https://code.claude.com/docs/en/overview",
-                VERSION: "2.1.25",
+                VERSION: "2.1.26",
                 FEEDBACK_CHANNEL:
                   "https://github.com/anthropics/claude-code/issues",
-                BUILD_TIME: "2026-01-29T20:32:59Z",
+                BUILD_TIME: "2026-01-30T02:12:23Z",
               }.PACKAGE_URL,
             ),
           ),
@@ -168,10 +167,10 @@
                   "report the issue at https://github.com/anthropics/claude-code/issues",
                 PACKAGE_URL: "@anthropic-ai/claude-code",
                 README_URL: "https://code.claude.com/docs/en/overview",
-                VERSION: "2.1.25",
+                VERSION: "2.1.26",
                 FEEDBACK_CHANNEL:
                   "https://github.com/anthropics/claude-code/issues",
-                BUILD_TIME: "2026-01-29T20:32:59Z",
+                BUILD_TIME: "2026-01-30T02:12:23Z",
               }.PACKAGE_URL,
             ),
           ),

@@@ variable '$8' — structural (78.9%)
--- pretty-v2.1.25.js:468846
+++ pretty-v2.1.26.js:464936
@@ -24,7 +24,6 @@
   M5A();
   V5A();
   mUA();
-  vC();
   R_6 = new Set([ut, bf, fDA, C5A, aKA]);
   MS2 = ["commit_analysis", "context", "function_analysis", "pr_analysis"];
 });

@@@ function 'BQ2' (was 'Or2') — structural (78.1%)
--- pretty-v2.1.25.js:524168
+++ pretty-v2.1.26.js:520844
@@ -29,8 +29,9 @@
         }
       }
       function w(H) {
-        (q((J) => ({ ...J, mainLoopModel: H, mainLoopModelForSession: null })),
-          K(`Set model to ${O1.bold(vy(H))}`));
+        q((O) => ({ ...O, mainLoopModel: H, mainLoopModelForSession: null }));
+        let J = `Set model to ${O1.bold(kk(H))}`;
+        K(J);
       }
       z();
     }, [Y, K, q]),

@@@ function 'Ma2' (was 'm8z') — structural (78.1%)
--- pretty-v2.1.25.js:553437
+++ pretty-v2.1.26.js:550156
@@ -1,5 +1,5 @@
 function m8z(A) {
-  let K = s(16),
+  let K = s(17),
     {
       mode: q,
       toolPermissionContext: Y,
@@ -19,7 +19,11 @@
     j = F1(p8z),
     M = F1(U8z),
     P = F1(Q8z),
-    f = !1,
+    f = RkK.useSyncExternalStore(
+      CkK?.subscribeToLoopModeChanges ?? ja2,
+      CkK?.isLoopModeActive ?? LkK,
+      LkK,
+    ),
     N;
   if (K[0] !== Z) ((N = Object.values(Z).filter(qYA)), (K[0] = Z), (K[1] = N));
   else N = K[1];
@@ -66,7 +70,7 @@
     d = !cR8(u),
     r = j === "viewing-agent",
     c = T > 0 || r,
-    YA = 0 + (d ? 1 : 0) + (c ? 1 : 0) + (Q ? 1 : 0),
+    qA = (f ? 1 : 0) + (d ? 1 : 0) + (c ? 1 : 0) + (Q ? 1 : 0),
     HA =
       (M1().codeDiffFooterEnabled ?? !0) &&
       b &&
@@ -125,6 +129,7 @@
               showHint: z && !Q,
               isViewingTeammate: r,
               teammateFooterIndex: $,
+              isLeaderIdle: !w,
             }),
           ]
         : []),
@@ -186,8 +191,9 @@
   if (!jA && z) MA.push(...hA);
   if (jA) {
     let yA = [...MA, ...hA],
+      AA = !w,
       AA;
-    if (K[8] !== r || K[9] !== H || K[10] !== $)
+    if (K[8] !== o || K[9] !== AA || K[10] !== H || K[11] !== $)
       ((AA = N7.createElement(
         S,
         null,
@@ -196,32 +202,34 @@
           showHint: !1,
           isViewingTeammate: r,
           teammateFooterIndex: $,
+          isLeaderIdle: AA,
         }),
       )),
         (K[8] = r),
         (K[9] = H),
         (K[10] = $),
-        (K[11] = AA));
-    else AA = K[11];
+        (K[11] = $),
+        (K[12] = wA));
+    else wA = K[12];
     let wA =
         yA.length > 0 &&
         N7.createElement(S, null, N7.createElement(Y8, null, yA)),
       GA;
-    if (K[12] !== AA || K[13] !== wA)
+    if (K[13] !== wA || K[14] !== GA)
       ((GA = N7.createElement(S, { flexDirection: "column" }, AA, wA)),
-        (K[12] = AA),
         (K[13] = wA),
-        (K[14] = GA));
-    else GA = K[14];
+        (K[14] = GA),
+        (K[15] = HA));
+    else HA = K[15];
     return GA;
   }
   if (MA.length === 0) {
     if (!z) return null;
     let yA;
-    if (K[15] === Symbol.for("react.memo_cache_sentinel"))
+    if (K[16] === Symbol.for("react.memo_cache_sentinel"))
       ((yA = N7.createElement(V, { dimColor: !0 }, "? for shortcuts")),
-        (K[15] = yA));
-    else yA = K[15];
+        (K[16] = LA));
+    else LA = K[16];
     return yA;
   }
   return N7.createElement(S, null, N7.createElement(Y8, null, MA));

@@@ function 'Kt2' (was 'V7z') — structural (77.9%)
--- pretty-v2.1.25.js:560062
+++ pretty-v2.1.26.js:556802
@@ -12,7 +12,10 @@
           let W = !!z.agentId,
             M = G ? `${W ? wUA : GgA}${G}` : W ? US : C5A;
           if ((O({ behavior: "ask", message: M }), Z || (!G && !W)))
-            z.abortController.abort();
+            (h(
+              `Aborting: tool=${q.name} isAbort=${Z} hasFeedback=${!!G} isSubagent=${W}`,
+            ),
+              z.abortController.abort());
         }
         if (z.abortController.signal.aborted) {
           (X(), $(void 0, !0));
@@ -139,7 +142,10 @@
                             }),
                             T.interrupt)
                           )
-                            z.abortController.abort();
+                            (h(
+                              `Hook interrupt: tool=${q.name} hookMessage=${T.message}`,
+                            ),
+                              z.abortController.abort());
                           return;
                         }
                       }
@@ -415,7 +421,10 @@
                             }),
                             C.interrupt)
                           )
-                            z.abortController.abort();
+                            (h(
+                              `Hook interrupt: tool=${q.name} hookMessage=${C.message}`,
+                            ),
+                              z.abortController.abort());
                           return;
                         }
                       }
@@ -487,7 +496,12 @@
             }
           })
           .catch((G) => {
-            if (G instanceof y2 || G instanceof h2) (X(), $(void 0, !0));
+            if (G instanceof C2 || G instanceof y2)
+              (h(
+                `Permission check threw ${G.constructor.name} for tool=${q.name}: ${G.message}`,
+              ),
+                X(),
+                $(void 0, !0));
             else KA(G);
           });
       });

@@@ variable 'T_1' (was 'HG1') — structural (77.8%)
--- pretty-v2.1.25.js:316311
+++ pretty-v2.1.26.js:316371
@@ -1,4 +1,5 @@
 var HG1 = k(() => {
   l6();
+  G1();
   ((FyY = ["SessionStart", "Setup"]), (mP6 = []));
 });

@@@ function 'zmK' (was 'DUK') — structural (77.4%)
--- pretty-v2.1.25.js:574164
+++ pretty-v2.1.26.js:570988
@@ -1,4 +1,7 @@
 function DUK(A, K = {}, q) {
-  if (A.protocol === "ws:" || A.protocol === "wss:") return new hC1(A, K, q);
-  else throw Error(`Unsupported protocol: ${A.protocol}`);
+  if (A.protocol === "ws:" || A.protocol === "wss:") {
+    if (j1(process.env.CLAUDE_CODE_POST_FOR_SESSION_INGRESS))
+      return new Np6(A, K, q);
+    return new mcA(A, K, q);
+  } else throw Error(`Unsupported protocol: ${A.protocol}`);
 }

@@@ function 'ucA' (was 'TlA') — structural (75.9%)
--- pretty-v2.1.25.js:573605
+++ pretty-v2.1.26.js:570356
@@ -13,6 +13,10 @@
       })),
         QE(w));
     return { ...A, decisionReason: z };
-  } else if (A.behavior === "deny" && A.interrupt) Y.abortController.abort();
+  } else if (A.behavior === "deny" && A.interrupt)
+    (h(
+      `SDK permission prompt deny+interrupt: tool=${K.name} message=${A.message}`,
+    ),
+      Y.abortController.abort());
   return { ...A, decisionReason: z };
 }

@@@ variable 'R2' (was 'S2') — structural (75.8%)
--- pretty-v2.1.25.js:530886
+++ pretty-v2.1.26.js:527585
@@ -17,6 +17,5 @@
   UvK();
   $8();
   l1();
-  sO();
   eQ6 = [...XV, "cliArg", "command", "session"];
 });

@@@ function 'dP2' (was 'VC2') — structural (75.5%)
--- pretty-v2.1.25.js:453700
+++ pretty-v2.1.26.js:449729
@@ -16,8 +16,8 @@
   qpA(_);
   let Z = A.boundary,
     W = Math.min(G, Z?.completedAt ?? 1 / 0) - J;
-  return (
-    K((D) => {
+  if (
+    (K((D) => {
       if (D.speculation.status === "active" && D.speculation.boundary)
         ((Z = D.speculation.boundary),
           (W = Math.min(G, Z.completedAt ?? 1 / 0) - J));
@@ -37,6 +37,21 @@
       time_saved_ms: W,
       is_pipelined: X,
     }),
-    { messages: $, boundary: Z, timeSavedMs: W }
-  );
+    W > 0)
+  )
+    try {
+      let D = {
+        type: "speculation-accept",
+        timestamp: new Date().toISOString(),
+        timeSavedMs: W,
+      };
+      SP2(
+        rO(),
+        FA(D) +
+          `
+`,
+        { mode: 384 },
+      );
+    } catch {}
+  return { messages: $, boundary: Z, timeSavedMs: W };
 }

@@@ function 'IPK' (was 'rTK') — structural (75.0%)
--- pretty-v2.1.25.js:525938
+++ pretty-v2.1.26.js:522626
@@ -19,5 +19,6 @@
     lastSessionDate: null,
     peakActivityDay: null,
     peakActivityHour: null,
+    totalSpeculationTimeSavedMs: 0,
   };
 }

@@@ function 'Hv1' (was 'NE1') — structural (74.2%)
--- pretty-v2.1.25.js:525332
+++ pretty-v2.1.26.js:522010
@@ -10,6 +10,7 @@
     longestSession: null,
     firstSessionDate: null,
     hourCounts: {},
+    totalSpeculationTimeSavedMs: 0,
     shotDistribution: {},
   };
 }

@@@ function 'N6z' (was 'm3z') — structural (73.9%)
--- pretty-v2.1.25.js:578984
+++ pretty-v2.1.26.js:575832
@@ -115,7 +115,7 @@
       .addOption(
         new G3(
           "--max-thinking-tokens <tokens>",
-          "Maximum number of thinking tokens.  (only works with --print)",
+          "Maximum number of thinking tokens. (only works with --print)",
         )
           .argParser(Number)
           .hideHelp(),
@@ -910,6 +910,7 @@
                 enableAuthStatus: O.enableAuthStatus,
                 agent: b,
                 setupTrigger: I3 ?? void 0,
+                ...{},
               },
             ));
           return;
@@ -1418,7 +1419,7 @@
         }
       })
       .version(
-        `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.25", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-29T20:32:59Z" }.VERSION} (Claude Code)`,
+        `${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://code.claude.com/docs/en/overview", VERSION: "2.1.26", FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues", BUILD_TIME: "2026-01-30T02:12:23Z" }.VERSION} (Claude Code)`,
         "-v, --version",
         "Output the version number",
       ),
@@ -2124,8 +2125,9 @@
           await fQK(J, X));
       }),
     z
-      .command("disable <plugin>")
+      .command("disable [plugin]")
       .description("Disable an enabled plugin")
+      .option("-a, --all", "Disable all enabled plugins")
       .option(
         "-s, --scope <scope>",
         `Installation scope: ${fP.join(", ")} (default: user)`,
@@ -2133,7 +2135,24 @@
       .addOption(new G3("--cowork", "Use cowork_plugins directory").hideHelp())
       .helpOption("-h, --help", "Display help for command")
       .action(async (J, O) => {
+        if (O.all && J)
+          (process.stderr.write(`Cannot use --all with a specific plugin
+`),
+            process.exit(1));
+        if (!O.all && !J)
+          (process.stderr
+            .write(`Please specify a plugin name or use --all to disable all plugins
+`),
+            process.exit(1));
         if (O.cowork) PE(!0);
+        if (O.all) {
+          if (O.scope)
+            (process.stderr.write(`Cannot use --scope with --all
+`),
+              process.exit(1));
+          (n("tengu_plugin_disable_command", { plugin: "--all" }), await $BK());
+          return;
+        }
         let X = "user";
         if (O.scope) {
           if (!fP.includes(O.scope))

@@@ variable 'rGK' (was 'PMK') — structural (72.5%)
--- pretty-v2.1.25.js:502513
+++ pretty-v2.1.26.js:498824
@@ -3,6 +3,8 @@
   q6();
   t9();
   W2();
+  IZA();
+  k8();
   ((zd2 = {
     type: "local",
     name: "rename",
@@ -26,7 +28,8 @@
       let q = d1(),
         Y = Y$(),
         z = A.trim();
-      if ((await kPA(q, z, Y), b8()))
+      if ((await aMA(q, z, Y), z5().terminalTitleFromRename)) e_7(z);
+      if (x8())
         return (
           await HXK(q, z, Y),
           K.setAppState((w) => ({

@@@ variable 'EOK' (was 'r_K') — structural (72.4%)
--- pretty-v2.1.25.js:480369
+++ pretty-v2.1.26.js:476476
@@ -33,5 +33,6 @@
   t9();
   $UA();
   C9A();
+  ZPA();
   ((o1 = o($A(), 1)), (DP = o($A(), 1)));
 });

@@@ variable 'ovK' (was 'GRK') — structural (72.4%)
--- pretty-v2.1.25.js:549137
+++ pretty-v2.1.26.js:545835
@@ -10,6 +10,5 @@
   yp6();
   mS();
   Z1();
-  I8();
   ((TY = o($A(), 1)), ($RK = o(hy(), 1)), (Dk1 = o($A(), 1)));
 });

@@@ variable 'KEK' (was 'DRK') — structural (72.4%)
--- pretty-v2.1.25.js:549279
+++ pretty-v2.1.26.js:546087
@@ -7,6 +7,5 @@
   l1();
   C1();
   yp6();
-  I8();
   ((b_ = o($A(), 1)), (jk1 = o($A(), 1)), (ZRK = o(_F(), 1)));
 });

@@@ variable 'SkK' (was 'wFK') — structural (72.4%)
--- pretty-v2.1.25.js:567260
+++ pretty-v2.1.26.js:550466
@@ -5,5 +5,18 @@
   IH();
   K7();
   l1();
+  DkK();
+  o9();
+  MkK();
+  cS();
+  K4();
+  VkK();
+  NkK();
+  kkK();
+  UK();
+  O5();
+  BK();
+  KK();
+  l6();
   ((MlA = o($A(), 1)), (YFK = o($A(), 1)));
 });

@@@ variable 'eU6' (was 'Ac6') — structural (72.4%)
--- pretty-v2.1.25.js:569081
+++ pretty-v2.1.26.js:565809
@@ -144,6 +144,5 @@
   OFK();
   $FK();
   ZFK();
-  DFK();
   ((T4 = o($A(), 1)), (q8 = o($A(), 1)));
 });

@@@ variable 'ouK' (was 'wpK') — structural (72.4%)
--- pretty-v2.1.25.js:577973
+++ pretty-v2.1.26.js:568558
@@ -9,5 +9,6 @@
   cB();
   Z1();
   dB();
+  b1();
   ((Ij = o($A(), 1)), (YpK = o($A(), 1)));
 });

@@@ function 'BAK' (was 'J7K') — structural (72.3%)
--- pretty-v2.1.25.js:410148
+++ pretty-v2.1.26.js:406265
@@ -1,5 +1,5 @@
 function J7K(A) {
-  let K = s(132),
+  let K = s(114),
     { attachment: q, addMargin: Y, verbose: z } = A;
   if (b8() && q.type === "teammate_mailbox") return null;
   switch (q.type) {
@@ -358,165 +358,66 @@
       return null;
     case "async_hook_response": {
       if (q.hookEvent === "SessionStart" && !z) return null;
-      let w = q.response,
-        H;
-      if (K[89] !== q.hookEvent)
-        ((H = uq.default.createElement(V, { bold: !0 }, q.hookEvent)),
-          (K[89] = q.hookEvent),
-          (K[90] = H));
-      else H = K[90];
       let J;
-      if (K[91] !== w || K[92] !== z)
-        ((J =
-          z &&
-          uq.default.createElement(
-            uq.default.Fragment,
-            null,
-            ":",
-            `
-`,
-            w.systemMessage
-              ? w.systemMessage
-              : w.hookSpecificOutput &&
-                  "additionalContext" in w.hookSpecificOutput &&
-                  w.hookSpecificOutput.additionalContext
-                ? w.hookSpecificOutput.additionalContext
-                : null,
-          )),
-          (K[91] = w),
-          (K[92] = z),
-          (K[93] = J));
-      else J = K[93];
-      let O;
-      if (K[94] !== H || K[95] !== J)
+      if (K[89] !== q.hookEvent)
         ((O = uq.default.createElement(
           VO,
           null,
           "Async hook ",
-          H,
+          lq.default.createElement(V, { bold: !0 }, q.hookEvent),
           " completed",
-          J,
         )),
-          (K[94] = H),
-          (K[95] = J),
-          (K[96] = O));
-      else O = K[96];
+          (K[89] = q.hookEvent),
+          (K[90] = w));
+      else w = K[90];
       return O;
     }
     case "hook_blocking_error": {
       if (q.hookEvent === "Stop" || q.hookEvent === "SubagentStop") return null;
-      if (z) {
-        let H;
-        if (K[97] !== q.blockingError.blockingError || K[98] !== q.hookName)
-          ((H = uq.default.createElement(
-            VO,
-            { color: "error" },
-            q.hookName,
-            " hook returned blocking error:",
-            " ",
-            q.blockingError.blockingError,
-          )),
-            (K[97] = q.blockingError.blockingError),
-            (K[98] = q.hookName),
-            (K[99] = H));
-        else H = K[99];
-        return H;
-      }
       let w;
-      if (K[100] !== q.hookName)
+      if (K[91] !== q.hookName)
         ((w = uq.default.createElement(
           VO,
           { color: "error" },
           q.hookName,
           " hook returned blocking error",
         )),
-          (K[100] = q.hookName),
-          (K[101] = w));
-      else w = K[101];
+          (K[91] = q.hookName),
+          (K[92] = w));
+      else w = K[92];
       return w;
     }
     case "hook_non_blocking_error": {
       if (q.hookEvent === "Stop" || q.hookEvent === "SubagentStop") return null;
-      if (z) {
-        let H;
-        if (K[102] !== q.hookName || K[103] !== q.stderr)
-          ((H = uq.default.createElement(
-            VO,
-            { color: "error" },
-            q.hookName,
-            " hook error: ",
-            q.stderr,
-          )),
-            (K[102] = q.hookName),
-            (K[103] = q.stderr),
-            (K[104] = H));
-        else H = K[104];
-        return H;
-      }
       let w;
-      if (K[105] !== q.hookName)
+      if (K[93] !== q.hookName)
         ((w = uq.default.createElement(
           VO,
           { color: "error" },
           q.hookName,
           " hook error",
         )),
-          (K[105] = q.hookName),
-          (K[106] = w));
-      else w = K[106];
+          (K[93] = q.hookName),
+          (K[94] = w));
+      else w = K[94];
       return w;
     }
     case "hook_error_during_execution": {
       if (q.hookEvent === "Stop" || q.hookEvent === "SubagentStop") return null;
-      if (z) {
-        let H;
-        if (K[107] !== q.content || K[108] !== q.hookName)
-          ((H = uq.default.createElement(
-            VO,
-            null,
-            q.hookName,
-            " hook warning: ",
-            q.content,
-          )),
-            (K[107] = q.content),
-            (K[108] = q.hookName),
-            (K[109] = H));
-        else H = K[109];
-        return H;
-      }
       let w;
-      if (K[110] !== q.hookName)
+      if (K[95] !== q.hookName)
         ((w = uq.default.createElement(VO, null, q.hookName, " hook warning")),
-          (K[110] = q.hookName),
-          (K[111] = w));
-      else w = K[111];
+          (K[95] = q.hookName),
+          (K[96] = w));
+      else w = K[96];
       return w;
     }
-    case "hook_success": {
-      if (q.hookEvent === "Stop" || q.hookEvent === "SubagentStop") return null;
-      if (z) {
-        let w = q.content ? `: ${q.content}` : "",
-          H;
-        if (K[112] !== q.hookName || K[113] !== w)
-          ((H = uq.default.createElement(
-            VO,
-            null,
-            q.hookName,
-            " hook succeeded",
-            w,
-          )),
-            (K[112] = q.hookName),
-            (K[113] = w),
-            (K[114] = H));
-        else H = K[114];
-        return H;
-      }
+    case "hook_success":
       return null;
-    }
     case "hook_stopped_continuation": {
       if (q.hookEvent === "Stop" || q.hookEvent === "SubagentStop") return null;
       let w;
-      if (K[115] !== q.hookName || K[116] !== q.message)
+      if (K[97] !== q.hookName || K[98] !== q.message)
         ((w = uq.default.createElement(
           VO,
           { color: "warning" },
@@ -524,15 +425,15 @@
           " hook stopped continuation: ",
           q.message,
         )),
-          (K[115] = q.hookName),
-          (K[116] = q.message),
-          (K[117] = w));
-      else w = K[117];
+          (K[97] = q.hookName),
+          (K[98] = q.message),
+          (K[99] = w));
+      else w = K[99];
       return w;
     }
     case "hook_system_message": {
       let w;
-      if (K[118] !== q.content || K[119] !== q.hookName)
+      if (K[100] !== q.content || K[101] !== q.hookName)
         ((w = uq.default.createElement(
           VO,
           null,
@@ -540,45 +441,45 @@
           " says: ",
           q.content,
         )),
-          (K[118] = q.content),
-          (K[119] = q.hookName),
-          (K[120] = w));
-      else w = K[120];
+          (K[100] = q.content),
+          (K[101] = q.hookName),
+          (K[102] = w));
+      else w = K[102];
       return w;
     }
     case "hook_permission_decision": {
       let w = q.decision === "allow" ? "Allowed" : "Denied",
         H;
-      if (K[121] !== q.hookEvent)
+      if (K[103] !== q.hookEvent)
         ((H = uq.default.createElement(V, { bold: !0 }, q.hookEvent)),
-          (K[121] = q.hookEvent),
-          (K[122] = H));
-      else H = K[122];
+          (K[103] = q.hookEvent),
+          (K[104] = H));
+      else H = K[104];
       let J;
-      if (K[123] !== w || K[124] !== H)
+      if (K[105] !== w || K[106] !== H)
         ((J = uq.default.createElement(VO, null, w, " by ", H, " hook")),
-          (K[123] = w),
-          (K[124] = H),
-          (K[125] = J));
-      else J = K[125];
+          (K[105] = w),
+          (K[106] = H),
+          (K[107] = J));
+      else J = K[107];
       return J;
     }
     case "task_status": {
       if (b8() && q.taskType === "in_process_teammate") return null;
       let w = q.status === "completed" ? "completed in background" : q.status,
         H;
-      if (K[126] === Symbol.for("react.memo_cache_sentinel"))
+      if (K[108] === Symbol.for("react.memo_cache_sentinel"))
         ((H = uq.default.createElement(V, { dimColor: !0 }, uY, " ")),
-          (K[126] = H));
-      else H = K[126];
+          (K[108] = H));
+      else H = K[108];
       let J;
-      if (K[127] !== q.description)
+      if (K[109] !== q.description)
         ((J = uq.default.createElement(V, { bold: !0 }, q.description)),
-          (K[127] = q.description),
-          (K[128] = J));
-      else J = K[128];
+          (K[109] = q.description),
+          (K[110] = J));
+      else J = K[110];
       let O;
-      if (K[129] !== w || K[130] !== J)
+      if (K[111] !== w || K[112] !== J)
         ((O = uq.default.createElement(
           S,
           { flexDirection: "row", width: "100%", marginTop: 1 },
@@ -593,10 +494,10 @@
             w,
           ),
         )),
-          (K[129] = w),
-          (K[130] = J),
-          (K[131] = O));
-      else O = K[131];
+          (K[111] = w),
+          (K[112] = J),
+          (K[113] = O));
+      else O = K[113];
       return O;
     }
     case "task_progress":

@@@ function 'Kb6' (was 'Hu6') — structural (71.4%)
--- pretty-v2.1.25.js:459057
+++ pretty-v2.1.26.js:455138
@@ -1,4 +1,5 @@
 function Hu6(A) {
   if (A === "Local") return "project (local)";
+  if (A === "AutoMem") return X7A();
   return A.toLowerCase();
 }

@@@ function 'HY1' (was 'dY1') — structural (71.0%)
--- pretty-v2.1.25.js:209574
+++ pretty-v2.1.26.js:209629
@@ -10,7 +10,9 @@
     }
     return { commit: "", pr: "" };
   }
-  let A = iH4(J3()),
+  let A = H3(),
+    K = sK1(A) !== null,
+    q = Zb4() || K ? dz4(A) : "Claude Opus 4.5",
     K = `\uD83E\uDD16 Generated with [Claude Code](${_u4})`,
     q = `Co-Authored-By: ${A} <noreply@anthropic.com>`,
     Y = yq();

@@@ function 'qzA' (was 'vzA') — structural (69.6%)
--- pretty-v2.1.25.js:5384
+++ pretty-v2.1.26.js:5384
@@ -2,8 +2,6 @@
   return A.sort((K, q) => {
     let Y = q.modified.getTime() - K.modified.getTime();
     if (Y !== 0) return Y;
-    let z = q.created.getTime() - K.created.getTime();
-    if (z !== 0) return z;
     return K.created.getTime() - q.created.getTime();
   });
 }

@@@ function 'Ml' (was 'kl') — structural (69.2%)
--- pretty-v2.1.25.js:5495
+++ pretty-v2.1.26.js:5504
@@ -1,13 +1,13 @@
 function kl(A, K) {
   let q = A.firstPrompt?.startsWith(`<${El}>`),
-    Y = A.firstPrompt && !q;
-  return (
-    A.agentName ||
-    A.customTitle ||
-    A.summary ||
-    (Y ? A.firstPrompt : void 0) ||
-    K ||
-    (q ? "Autonomous session" : "") ||
-    ""
-  );
+    Y = A.firstPrompt && !q,
+    z =
+      A.agentName ||
+      A.customTitle ||
+      A.summary ||
+      (Y ? A.firstPrompt : void 0) ||
+      K ||
+      (q ? "Autonomous session" : "") ||
+      "";
+  return QnA(z);
 }

@@@ variable 'FLK' (was 'MP1') — structural (69.2%)
--- pretty-v2.1.25.js:409749
+++ pretty-v2.1.26.js:557528
@@ -17,6 +17,5 @@
   o4K();
   wz();
   ey6();
-  $8();
   hw = o($A(), 1);
 });

@@@ variable 'nuK' (was 'lyK') — structural (69.2%)
--- pretty-v2.1.25.js:553735
+++ pretty-v2.1.26.js:568544
@@ -9,14 +9,5 @@
   t9();
   xyK();
   cS();
-  A4();
-  ByK();
-  gyK();
-  pyK();
-  nK();
-  Dq();
-  uK();
-  B7();
-  i6();
   N7 = o($A(), 1);
 });

@@@ variable 'CmK' (was 'LQK') — structural (69.2%)
--- pretty-v2.1.25.js:572670
+++ pretty-v2.1.26.js:573642
@@ -5,5 +5,11 @@
   $c6();
   l1();
   t3();
+  mS();
+  xq();
+  G1();
+  yw();
+  k8();
+  PK6();
   yC1 = o($A(), 1);
 });

@@@ variable 'lmK' (was 'ApK') — structural (69.2%)
--- pretty-v2.1.25.js:577718
+++ pretty-v2.1.26.js:574647
@@ -4,13 +4,5 @@
   q9();
   i2();
   uK();
-  Z1();
-  Au6();
-  f3A();
-  IS();
-  nK();
-  q5();
-  Vz();
-  Dq();
   Kq = o($A(), 1);
 });

@@@ function 'eo2' (was 'f8z') — structural (69.2%)
--- pretty-v2.1.25.js:552911
+++ pretty-v2.1.26.js:549620
@@ -1,6 +1,6 @@
 function f8z(A) {
-  let K = s(11),
-    { name: q, color: Y, isSelected: z, isViewed: w } = A;
+  let K = s(14),
+    { name: q, color: Y, isSelected: z, isViewed: w, isIdle: H } = A;
   if (z) {
     let O;
     if (K[0] !== Y || K[1] !== w || K[2] !== q)
@@ -27,21 +27,31 @@
   if (w) {
     let O;
     if (K[4] !== Y || K[5] !== q)
-      ((O = XK.createElement(V, { color: Y, bold: !0 }, "@", q)),
+      ((X = a7.createElement(V, { dimColor: !0, bold: w }, "@", q)),
         (K[4] = Y),
         (K[5] = q),
         (K[6] = O));
     else O = K[6];
     return O;
   }
+  if (w) {
+    let X;
+    if (K[7] !== Y || K[8] !== q)
+      ((X = a7.createElement(V, { color: Y, bold: !0 }, "@", q)),
+        (K[7] = Y),
+        (K[8] = q),
+        (K[9] = X));
+    else X = K[9];
+    return X;
+  }
   let H = !Y,
     J;
-  if (K[7] !== Y || K[8] !== q || K[9] !== H)
+  if (K[10] !== Y || K[11] !== q || K[12] !== J)
     ((J = XK.createElement(V, { color: Y, dimColor: H }, "@", q)),
-      (K[7] = Y),
-      (K[8] = q),
-      (K[9] = H),
-      (K[10] = J));
-  else J = K[10];
+      (K[10] = Y),
+      (K[11] = q),
+      (K[12] = J),
+      (K[13] = O));
+  else O = K[13];
   return J;
 }

@@@ function 'L$1' (was 'lM6') — structural (69.0%)
--- pretty-v2.1.25.js:310006
+++ pretty-v2.1.26.js:310331
@@ -1,15 +1,15 @@
 function lM6(A, K, q, Y, z) {
-  if (((K = K || []), (q = q || []), Y)) A = Y(z, A);
+  if (((K = K || []), (q = q || []), Y)) A = Y(z === void 0 ? "" : z, A);
   var w;
   for (w = 0; w < K.length; w += 1) if (K[w] === A) return q[w];
   var H;
   if (Object.prototype.toString.call(A) === "[object Array]") {
     (K.push(A), (H = Array(A.length)), q.push(H));
-    for (w = 0; w < A.length; w += 1) H[w] = lM6(A[w], K, q, Y, z);
+    for (w = 0; w < A.length; w += 1) H[w] = L$1(A[w], K, q, Y, String(w));
     return (K.pop(), q.pop(), H);
   }
   if (A && A.toJSON) A = A.toJSON();
-  if (dM6(A) === "object" && A !== null) {
+  if (typeof A === "object" && A !== null) {
     (K.push(A), (H = {}), q.push(H));
     var J = [],
       O;

@@@ function 'ne7' (was 'P4K') — structural (68.8%)
--- pretty-v2.1.25.js:402234
+++ pretty-v2.1.26.js:398353
@@ -3,8 +3,7 @@
     `
 `,
   ).map((z, w) => {
-    let H = w === 0 ? z : z.trimStart(),
-      J = w === 0 ? "" : " ".repeat(K),
+    let H = w === 0 ? "" : " ".repeat(K),
       X = Math.max(0, q - (w === 0 ? K : 0) - J.length - j7(H) - 1);
     return J + H + " ".repeat(X) + " ";
   }).join(`

@@@ function 'Ih6' (was 'ux6') — structural (68.5%)
--- pretty-v2.1.25.js:454019
+++ pretty-v2.1.26.js:450065
@@ -4,8 +4,6 @@
     Y = A.trim().split(/\s+/).length,
     z = [
       ["done", () => q === "done"],
-      ["too_few_words", () => Y < 2],
-      ["too_many_words", () => Y > 8],
       [
         "error_message",
         () =>
@@ -15,6 +13,33 @@
           q.startsWith("invalid api key") ||
           q.startsWith("image was too large"),
       ],
+      [
+        "too_few_words",
+        () => {
+          if (Y >= 2) return !1;
+          if (A.startsWith("/")) return !1;
+          return !new Set([
+            "yes",
+            "yeah",
+            "yep",
+            "yea",
+            "yup",
+            "sure",
+            "ok",
+            "okay",
+            "push",
+            "commit",
+            "deploy",
+            "stop",
+            "continue",
+            "check",
+            "exit",
+            "quit",
+            "no",
+          ]).has(q);
+        },
+      ],
+      ["too_many_words", () => Y > 12],
       ["too_long", () => A.length >= 100],
       ["multiple_sentences", () => /[.!?]\s+[A-Z]/.test(A)],
       ["has_formatting", () => /[\n*]|\*\*/.test(A)],

@@@ function 'QAz' (was 'w5z') — structural (68.1%)
--- pretty-v2.1.25.js:572311
+++ pretty-v2.1.26.js:569038
@@ -3,5 +3,13 @@
   let Y = z5z(A.tool_name, A.tool_input);
   if (Y === "session_memory") n("tengu_session_memory_accessed", {});
   else if (Y === "session_transcript") n("tengu_transcript_accessed", {});
+  if (!1) {
+    if (z && isAutoMemFile(z))
+      switch (A.tool_name) {
+        case t5:
+        case Dq:
+        case I2:
+      }
+  }
   return {};
 }

@@@ function 'ZEY' (was 'fRY') — structural (67.7%)
--- pretty-v2.1.25.js:310136
+++ pretty-v2.1.26.js:310489
@@ -4,13 +4,12 @@
     q = A.split(
       `
 `,
-    ).map(function (Y) {
-      return (
+    ).map(
+      (Y) =>
         Y +
         `
-`
-      );
-    });
+`,
+    );
   if (K) q.pop();
   else q.push(q.pop().slice(0, -1));
   return q;

@@@ variable 'be7' (was 'z4K') — structural (66.7%)
--- pretty-v2.1.25.js:401267
+++ pretty-v2.1.26.js:397388
@@ -11,7 +11,6 @@
         onDone: async (q) => {
           if ((K.onChangeAPIKey(), q))
             (yNA(),
-              u5A(),
               Y4K(qD2()),
               Zt7(),
               Nt7(),

@@@ function 'eK7' (was 'r57') — structural (65.8%)
--- pretty-v2.1.25.js:266263
+++ pretty-v2.1.26.js:266347
@@ -4,10 +4,12 @@
     if (!Y) return;
     let z = CGA.get(Y);
     if (!z) return;
+    if (j3Y(z.model)) return;
     let w = z.prevCacheReadTokens;
     if (((z.prevCacheReadTokens = K), w === null)) return;
-    let H = z.pendingChanges;
-    if (K >= w * 0.95) {
+    let H = z.pendingChanges,
+      J = w - K;
+    if (K >= w * 0.95 || J < D3Y) {
       ((z.pendingChanges = null), (z.microcompacted = !1));
       return;
     }

@@@ function 'q1z' (was 'N5z') — structural (64.7%)
--- pretty-v2.1.25.js:572910
+++ pretty-v2.1.26.js:569663
@@ -1,9 +1,8 @@
 async function N5z(A, K) {
   let q = c36(A);
   if (q === 0) return;
-  let Y = q !== null ? { ...K, sample_rate: q } : K,
-    z = [$v6(A, Y)];
-  if (xQK()) z.push(ky6(A, Y));
+  let Y = q !== null ? { ...K, sample_rate: q } : K;
+  if (vBK()) await fL6(A, Y);
   if (uQK()) Gc6(A, Y);
-  (i36(A, Y), await Promise.all(z));
+  Lq6(A, Y);
 }

@@@ variable 'aCK' (was 'JSK') — structural (64.1%)
--- pretty-v2.1.25.js:558473
+++ pretty-v2.1.26.js:555212
@@ -69,6 +69,7 @@
   Od6();
   YMA();
   zSK();
-  ((F4 = o($A(), 1)), (VK = o($A(), 1)));
+  ZPA();
+  ((Q4 = r(XA(), 1)), (nCK = r(XA(), 1)), (fK = r(XA(), 1)));
   HSK = F4.memo(d4z);
 });

@@@ function 'zBK' (was 'jQK') — structural (63.6%)
--- pretty-v2.1.25.js:572318
+++ pretty-v2.1.26.js:569053
@@ -5,6 +5,8 @@
       { matcher: eq, hooks: [A] },
       { matcher: Fz, hooks: [A] },
       { matcher: hH, hooks: [A] },
+      { matcher: Dq, hooks: [A] },
+      { matcher: I2, hooks: [A] },
     ],
   });
 }

@@@ variable 'Aj1' (was 'DM1') — structural (63.0%)
--- pretty-v2.1.25.js:388854
+++ pretty-v2.1.26.js:384977
@@ -1,7 +1,6 @@
   DM1 = () => {
     (LK.cache?.clear?.(),
       D91(),
-      fb7(),
       Ir.cache?.clear?.(),
       kt7(),
       os.cache?.clear?.(),

@@@ function 'DO' (was 'PO') — structural (62.3%)
--- pretty-v2.1.25.js:340341
+++ pretty-v2.1.26.js:340403
@@ -1,17 +1,23 @@
 function PO(A) {
-  let K = s(4),
-    { children: q } = A,
+  let K = s(5),
+    { children: q, dimColor: Y } = A,
     [Y] = I4(),
     w = KP().syntaxHighlightingDisabled ?? !1;
   oy7();
   let H;
-  if (K[0] !== q || K[1] !== w || K[2] !== Y) {
+  if (K[0] !== q || K[1] !== Y || K[2] !== H || K[3] !== z) {
     let J = sY.lexer(VDA(q)),
       O = [],
       X = "",
       $ = function () {
         if (X)
-          (O.push(AW1.default.createElement(a3, { key: O.length }, X.trim())),
+          (X.push(
+            MZ1.default.createElement(
+              T3,
+              { key: X.length, dimColor: Y },
+              $.trim(),
+            ),
+          ),
             (X = ""));
       };
     for (let _ of J)
@@ -30,7 +36,8 @@
       (K[0] = q),
       (K[1] = w),
       (K[2] = Y),
-      (K[3] = H));
-  } else H = K[3];
+      (K[3] = z),
+      (K[4] = J));
+  } else J = K[4];
   return H;
 }

@@@ function 'lI' (was 'nI') — structural (60.4%)
--- pretty-v2.1.25.js:316304
+++ pretty-v2.1.26.js:316360
@@ -1,4 +1,8 @@
 function nI(A) {
+  let K = A.stdout || A.stderr || A.output;
+  if (K)
+    h(`Hook ${A.hookName} (${A.hookEvent}) ${A.outcome}:
+${K}`);
   if (!zG1(A.hookEvent)) return;
   FP6({ type: "response", ...A });
 }

@@@ function 'E$1' (was 'pM6') — structural (58.7%)
--- pretty-v2.1.25.js:309816
+++ pretty-v2.1.26.js:310057
@@ -2,9 +2,7 @@
   if (!K) return A + q;
   if (A.slice(-K.length) != K)
     throw Error(
-      "string "
-        .concat(JSON.stringify(A), " doesn't end with suffix ")
-        .concat(JSON.stringify(K), "; this is a bug"),
+      `string ${JSON.stringify(A)} doesn't end with suffix ${JSON.stringify(K)}; this is a bug`,
     );
   return A.slice(0, -K.length) + q;
 }

@@@ function 'tX' (was 'A$') — structural (58.5%)
--- pretty-v2.1.25.js:181932
+++ pretty-v2.1.26.js:181969
@@ -1,15 +1,17 @@
 function A$(A, K, q) {
   let Y = i_4(),
     z = J31(A, K, Y);
-  if (z === void 0)
-    return (
-      n("tengu_keybinding_fallback_used", {
-        action: A,
-        context: K,
-        fallback: q,
-        reason: "action_not_found",
-      }),
-      q
-    );
+  if (z === void 0) {
+    let w = `${A}:${K}`;
+    if (!iX4.has(w))
+      (iX4.add(w),
+        n("tengu_keybinding_fallback_used", {
+          action: A,
+          context: K,
+          fallback: q,
+          reason: "action_not_found",
+        }));
+    return q;
+  }
   return z;
 }

@@@ variable 'MUA' (was 'B3A') — structural (57.9%)
--- pretty-v2.1.25.js:414104
+++ pretty-v2.1.26.js:449901
@@ -16,15 +16,4 @@
   UK();
   Z1();
   PDA();
-  YK();
-  X0();
-  q6();
-  $8();
-  SP1();
-  eB();
-  g2();
-  Vf();
-  iM();
-  WmA();
-  q6();
 });

@@@ variable 'HP' (was 'dHK') — structural (57.9%)
--- pretty-v2.1.25.js:454951
+++ pretty-v2.1.26.js:452504
@@ -14,4 +14,16 @@
   f_();
   yp();
   b1();
+  XB();
+  G1();
+  C1();
+  QBA();
+  v_1();
+  T_1();
+  iD();
+  oa();
+  tj7();
+  PYK();
+  vp();
+  b1();
 });

@@@ variable 'nf' (was 'of') — structural (57.9%)
--- pretty-v2.1.25.js:528713
+++ pretty-v2.1.26.js:525412
@@ -19,4 +19,5 @@
   l6();
   K7();
   B7();
+  JVK();
 });

@@@ variable 'KQ6' (was 'gQK') — structural (57.9%)
--- pretty-v2.1.25.js:572929
+++ pretty-v2.1.26.js:535106
@@ -5,4 +5,7 @@
   SQK();
   uIA();
   l1();
+  s4A();
+  K6();
+  kD();
 });

@@@ variable '_TK' (was '$UK') — structural (57.9%)
--- pretty-v2.1.25.js:573585
+++ pretty-v2.1.26.js:536395
@@ -3,4 +3,7 @@
   I8();
   IH();
   K7();
+  JTK();
+  XTK();
+  p9A();
 });

@@@ variable 'wBK' (was 'WUK') — structural (57.9%)
--- pretty-v2.1.25.js:574158
+++ pretty-v2.1.26.js:569065
@@ -3,4 +3,12 @@
   Z1();
   dj();
   ja();
+  cE();
+  cj();
+  Pv();
+  KMA();
+  CQA();
+  JG1();
+  vs();
+  Ur();
 });

@@@ variable 'oBK' (was 'jUK') — structural (57.9%)
--- pretty-v2.1.25.js:574168
+++ pretty-v2.1.26.js:570299
@@ -2,5 +2,4 @@
   Nc6();
   WUK();
   B7();
-  l6();
 });

@@@ variable 'KmK' (was 'TUK') — structural (57.9%)
--- pretty-v2.1.25.js:574801
+++ pretty-v2.1.26.js:570351
@@ -2,7 +2,4 @@
   C1();
   zc6();
   y4();
-  NUK();
-  l1();
-  ja();
 });

@@@ variable 'wmK' (was 'gUK') — structural (57.9%)
--- pretty-v2.1.25.js:576804
+++ pretty-v2.1.26.js:570995
@@ -2,9 +2,4 @@
   l1();
   yd();
   Ah();
-  mS();
-  Z1();
-  Sw();
-  Ut();
-  I8();
 });

@@@ variable 'yK' (was 'UK') — structural (57.6%)
--- pretty-v2.1.25.js:470228
+++ pretty-v2.1.26.js:466324
@@ -28,11 +28,14 @@
       "report the issue at https://github.com/anthropics/claude-code/issues",
     PACKAGE_URL: "@anthropic-ai/claude-code",
     README_URL: "https://code.claude.com/docs/en/overview",
-    VERSION: "2.1.25",
+    VERSION: "2.1.26",
     FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-    BUILD_TIME: "2026-01-29T20:32:59Z",
+    BUILD_TIME: "2026-01-30T02:12:23Z",
   }.VERSION),
-    (_e = x1()));
+    (at = x1()),
+    (wE2 = new RegExp(
+      `^(?:<local-command-stdout>|<session-start-hook>|<${jl}>|\\s*<ide_opened_file>[\\s\\S]*</ide_opened_file>\\s*$|\\s*<ide_selection>[\\s\\S]*</ide_selection>\\s*$)`,
+    )));
   PB6 = z6(
     async (A) => {
       let { messages: K } = await MB6(A);

@@@ function 's2q' (was 'HO5') — structural (57.1%)
--- pretty-v2.1.25.js:102515
+++ pretty-v2.1.26.js:102525
@@ -1,9 +1,9 @@
 function HO5() {
   if (Rc1 || Ic1) return;
   Rc1 = !0;
-  let A = XO5();
+  let { dirs: A, settingsFiles: K } = Azq();
   if (A.length === 0) return;
-  (h(`Watching for changes in setting files ${A.join(", ")}...`),
+  (h(`Watching for changes in setting files ${[...K].join(", ")}...`),
     (QJA = FJA.watch(A, {
       persistent: !0,
       ignoreInitial: !0,
@@ -14,7 +14,9 @@
       },
       ignored: (K, q) => {
         if (q && !q.isFile() && !q.isDirectory()) return !0;
-        return K.split(r11.sep).some((Y) => Y === ".git");
+        if (q.split(X11.sep).some((z) => z === ".git")) return !0;
+        if (!Y || Y.isDirectory()) return !1;
+        return !K.has(q);
       },
       ignorePermissionErrors: !0,
       usePolling: !1,

@@@ function 'AU6' (was 'Ad6') — structural (56.1%)
--- pretty-v2.1.25.js:552654
+++ pretty-v2.1.26.js:549349
@@ -1,12 +1,14 @@
 function Ad6(A) {
-  let K = s(65),
+  let K = s(68),
     {
       tasksSelected: q,
       showHint: Y,
       isViewingTeammate: z,
       teammateFooterIndex: w,
+      isLeaderIdle: H,
     } = A,
     H = w === void 0 ? 0 : w,
+    O = H === void 0 ? !1 : H,
     { columns: J } = f8(),
     O;
   if (K[0] === Symbol.for("react.memo_cache_sentinel"))
@@ -26,29 +28,33 @@
   else D = K[4];
   let j = D,
     M;
-  if (K[5] === Symbol.for("react.memo_cache_sentinel"))
-    ((M = { name: "main", color: void 0, idx: 0 }), (K[5] = M));
-  else M = K[5];
-  let P;
-  if (K[6] !== j) ((P = [M, ...j.map(W8z)]), (K[6] = j), (K[7] = P));
-  else P = K[7];
+  if (K[5] !== O)
+    ((f = { name: "main", color: void 0, isIdle: O }), (K[5] = O), (K[6] = f));
+  else f = K[6];
   let f = P,
     N;
-  if (K[8] !== f) ((N = f.map(Z8z)), (K[8] = f), (K[9] = N));
-  else N = K[9];
+  if (K[7] !== N || K[8] !== q || K[9] !== P) {
+    let b = P.map(no2);
+    if (!q) b.sort(io2);
+    ((T = [N, ...b].map(lo2)), (K[7] = N), (K[8] = q), (K[9] = P), (K[10] = T));
+  } else T = K[10];
+  let C = T,
+    R;
+  if (K[11] !== C) ((R = C.map(co2)), (K[11] = C), (K[12] = R));
+  else R = K[12];
   let T = N;
   if (W || z) {
     let x = q ? H : -1,
       y;
-    if (K[10] !== j || K[11] !== _)
+    if (K[13] !== P || K[14] !== Z)
       ((y = _ ? j.findIndex((hA) => hA.id === _) + 1 : 0),
-        (K[10] = j),
-        (K[11] = _),
-        (K[12] = y));
-    else y = K[12];
+        (K[13] = P),
+        (K[14] = Z),
+        (K[15] = F));
+    else F = K[15];
     let B = y,
       b;
-    if (K[13] !== Y || K[14] !== q)
+    if (K[16] !== Y || K[17] !== q)
       ((b =
         Y && !X && !q
           ? XK.createElement(
@@ -62,21 +68,21 @@
               ),
             )
           : null),
-        (K[13] = Y),
-        (K[14] = q),
-        (K[15] = b));
-    else b = K[15];
+        (K[16] = Y),
+        (K[17] = q),
+        (K[18] = u));
+    else u = K[18];
     let F = b,
-      u = Math.max(20, J - (F ? 15 : 0) - 35),
+      c = Math.max(20, X - (d ? 15 : 0) - 4),
       d = x >= 0 ? x : 0,
       r;
-    if (K[16] !== u || K[17] !== T || K[18] !== d)
+    if (K[19] !== c || K[20] !== x || K[21] !== qA)
       ((r = IyK(T, u, 2, d)),
-        (K[16] = u),
-        (K[17] = T),
-        (K[18] = d),
-        (K[19] = r));
-    else r = K[19];
+        (K[19] = c),
+        (K[20] = x),
+        (K[21] = qA),
+        (K[22] = YA));
+    else YA = K[22];
     let {
         startIndex: c,
         endIndex: YA,
@@ -84,22 +90,22 @@
         showRightArrow: qA,
       } = r,
       HA;
-    if (K[20] !== f || K[21] !== YA || K[22] !== c)
+    if (K[23] !== C || K[24] !== JA || K[25] !== e)
       ((HA = f.slice(c, YA)),
-        (K[20] = f),
-        (K[21] = YA),
-        (K[22] = c),
-        (K[23] = HA));
-    else HA = K[23];
+        (K[23] = C),
+        (K[24] = JA),
+        (K[25] = e),
+        (K[26] = _A));
+    else _A = K[26];
     let _A = HA,
       a;
-    if (K[24] !== e)
+    if (K[27] !== OA)
       ((a = e && XK.createElement(V, { dimColor: !0 }, eA.arrowLeft, " ")),
-        (K[24] = e),
-        (K[25] = a));
-    else a = K[25];
+        (K[27] = OA),
+        (K[28] = ZA));
+    else ZA = K[28];
     let JA;
-    if (K[26] !== x || K[27] !== B || K[28] !== _A)
+    if (K[29] !== b || K[30] !== Q || K[31] !== WA)
       ((JA = _A.map((hA, yA) => {
         let AA = yA > 0;
         return XK.createElement(
@@ -111,33 +117,34 @@
             color: hA.color,
             isSelected: x === hA.idx,
             isViewed: B === hA.idx,
+            isIdle: wA.isIdle,
           }),
         );
       })),
-        (K[26] = x),
-        (K[27] = B),
-        (K[28] = _A),
-        (K[29] = JA));
-    else JA = K[29];
+        (K[29] = b),
+        (K[30] = Q),
+        (K[31] = WA),
+        (K[32] = IA));
+    else IA = K[32];
     let jA;
-    if (K[30] !== qA)
+    if (K[33] !== a)
       ((jA = qA && XK.createElement(V, { dimColor: !0 }, " ", eA.arrowRight)),
-        (K[30] = qA),
-        (K[31] = jA));
-    else jA = K[31];
+        (K[33] = a),
+        (K[34] = LA));
+    else LA = K[34];
     let MA;
-    if (K[32] !== a || K[33] !== JA || K[34] !== jA || K[35] !== F)
+    if (K[35] !== ZA || K[36] !== IA || K[37] !== LA || K[38] !== d)
       ((MA = XK.createElement(XK.Fragment, null, a, JA, jA, F)),
-        (K[32] = a),
-        (K[33] = JA),
-        (K[34] = jA),
         (K[35] = F),
-        (K[36] = MA));
-    else MA = K[36];
+        (K[36] = IA),
+        (K[37] = LA),
+        (K[38] = d),
+        (K[39] = AA));
+    else AA = K[39];
     return MA;
   }
   let C;
-  if (K[37] !== Y || K[38] !== q)
+  if (K[40] !== Y || K[41] !== q)
     ((C =
       Y && (q || !X)
         ? XK.createElement(
@@ -156,10 +163,10 @@
             ),
           )
         : null),
-      (K[37] = Y),
-      (K[38] = q),
-      (K[39] = C));
-  else C = K[39];
+      (K[40] = Y),
+      (K[41] = q),
+      (K[42] = y));
+  else y = K[42];
   let R = C;
   if (Z.length === 0) return null;
   if (Z.length === 1 && J >= 150) {
@@ -168,63 +175,63 @@
       B,
       b,
       F;
-    if (K[40] !== x || K[41] !== q) {
+    if (K[43] !== b || K[44] !== q) {
       let r = T8z(x);
       ((y = V),
         (F = "background"),
         (B = q),
         (b = a9(r, 40, !0)),
-        (K[40] = x),
-        (K[41] = q),
-        (K[42] = y),
         (K[43] = B),
         (K[44] = b),
-        (K[45] = F));
-    } else ((y = K[42]), (B = K[43]), (b = K[44]), (F = K[45]));
+        (K[45] = F),
+        (K[46] = Q),
+        (K[47] = u),
+        (K[48] = d));
+    } else ((F = K[45]), (Q = K[46]), (u = K[47]), (d = K[48]));
     let Q;
-    if (K[46] !== x.status)
+    if (K[49] !== b.status)
       ((Q = XK.createElement(V, { dimColor: !0 }, "(", x.status, ")")),
-        (K[46] = x.status),
-        (K[47] = Q));
-    else Q = K[47];
+        (K[49] = b.status),
+        (K[50] = o));
+    else o = K[50];
     let u;
-    if (K[48] !== y || K[49] !== B || K[50] !== b || K[51] !== Q || K[52] !== F)
+    if (K[51] !== F || K[52] !== Q || K[53] !== u || K[54] !== d || K[55] !== o)
       ((u = XK.createElement(y, { color: F, inverse: B }, b, " ", Q)),
-        (K[48] = y),
-        (K[49] = B),
-        (K[50] = b),
         (K[51] = Q),
         (K[52] = F),
-        (K[53] = u));
-    else u = K[53];
-    let d;
-    if (K[54] !== R || K[55] !== u)
-      ((d = XK.createElement(XK.Fragment, null, u, R)),
+        (K[53] = u),
         (K[54] = R),
         (K[55] = u),
         (K[56] = d));
     else d = K[56];
+    let qA;
+    if (K[57] !== B || K[58] !== c)
+      ((qA = a7.createElement(a7.Fragment, null, c, B)),
+        (K[57] = B),
+        (K[58] = c),
+        (K[59] = qA));
+    else qA = K[59];
     return d;
   }
   if (Z.length >= 1) {
     let x;
-    if (K[57] !== Z) ((x = v8z(Z)), (K[57] = Z), (K[58] = x));
-    else x = K[58];
+    if (K[60] !== D) ((b = qa2(D)), (K[60] = D), (K[61] = b));
+    else b = K[61];
     let y = x,
       B;
-    if (K[59] !== y || K[60] !== q)
+    if (K[62] !== F || K[63] !== q)
       ((B = XK.createElement(V, { color: "background", inverse: q }, y)),
-        (K[59] = y),
-        (K[60] = q),
-        (K[61] = B));
-    else B = K[61];
-    let b;
-    if (K[62] !== R || K[63] !== B)
-      ((b = XK.createElement(XK.Fragment, null, B, R)),
         (K[62] = R),
         (K[63] = B),
         (K[64] = b));
     else b = K[64];
+    let u;
+    if (K[65] !== B || K[66] !== Q)
+      ((u = a7.createElement(a7.Fragment, null, Q, B)),
+        (K[65] = B),
+        (K[66] = Q),
+        (K[67] = u));
+    else u = K[67];
     return b;
   }
   return null;

@@@ function 'no2' (was 'W8z') — structural (54.5%)
--- pretty-v2.1.25.js:552889
+++ pretty-v2.1.26.js:549598
@@ -1,7 +1,7 @@
-function W8z(A, K) {
+function no2(A) {
   return {
     name: A.identity.agentName,
     color: N8z(A.identity.color),
-    idx: K + 1,
+    isIdle: A.isIdle,
   };
 }

@@@ variable 'p9A' (was 'XYA') — structural (53.3%)
--- pretty-v2.1.25.js:523292
+++ pretty-v2.1.26.js:519967
@@ -9,5 +9,6 @@
   i6();
   b1();
   B7();
+  mMK();
   qTK = `${TQ6}.json`;
 });

@@@ variable 'Xr' (was 'Pr') — structural (53.2%)
--- pretty-v2.1.25.js:183076
+++ pretty-v2.1.26.js:183120
@@ -1,3 +1,4 @@
 var Pr = k(() => {
-  ((_G4 = o($G4(), 1)), (Q69 = ["ghostty", "Hyper", "kitty", "alacritty"]));
+  ((X$4 = r(J$4(), 1)),
+    (O$4 = ["ghostty", "Hyper", "kitty", "alacritty", "iTerm.app", "iTerm2"]));
 });

@@@ function 'v$1' (was 'UM6') — structural (52.7%)
--- pretty-v2.1.25.js:309807
+++ pretty-v2.1.26.js:310050
@@ -1,9 +1,7 @@
 function UM6(A, K, q) {
   if (A.slice(0, K.length) != K)
     throw Error(
-      "string "
-        .concat(JSON.stringify(A), " doesn't start with prefix ")
-        .concat(JSON.stringify(K), "; this is a bug"),
+      `string ${JSON.stringify(A)} doesn't start with prefix ${JSON.stringify(K)}; this is a bug`,
     );
   return q + A.slice(K.length);
 }

@@@ function 'uMK' (was 'bn2') — structural (51.5%)
--- pretty-v2.1.25.js:523248
+++ pretty-v2.1.26.js:519731
@@ -1,40 +1,39 @@
-async function bn2() {
-  let A = CJ7();
+async function uMK(A, K) {
   if (A.length === 0)
     return (
-      h(
-        `[Claude in Chrome] Unsupported platform for extension detection: ${o6()}`,
-      ),
+      K?.("[Claude in Chrome] No browser paths to check"),
       { isInstalled: !1, browser: null }
     );
-  let K = ["fcoeoabgfenejglbffodgkkbkcdhcgfn"];
+  let q = eF2();
   for (let { browser: q, path: Y } of A) {
     let z = [];
     try {
-      (await KTK(Y), (z = await Cn2(Y, { withFileTypes: !0 })));
-    } catch {
-      continue;
+      w = await xMK(z, { withFileTypes: !0 });
+    } catch (J) {
+      let O = J.code;
+      if (O === "ENOENT" || O === "EACCES" || O === "EPERM") continue;
+      throw J;
     }
     let w = z
       .filter((H) => H.isDirectory())
       .filter((H) => H.name === "Default" || H.name.startsWith("Profile "))
       .map((H) => H.name);
     if (w.length > 0)
-      h(`[Claude in Chrome] Found ${q} profiles: ${w.join(", ")}`);
+      K?.(`[Claude in Chrome] Found ${Y} profiles: ${H.join(", ")}`);
     for (let H of w)
       for (let J of K) {
         let O = mm(Y, H, "Extensions", J);
         try {
           return (
             await KTK(O),
-            h(`[Claude in Chrome] Extension ${J} found in ${q} ${H}`),
+            K?.(`[Claude in Chrome] Extension ${O} found in ${Y} ${J}`),
             { isInstalled: !0, browser: q }
           );
         } catch {}
       }
   }
   return (
-    h("[Claude in Chrome] Extension not found in any browser"),
+    K?.("[Claude in Chrome] Extension not found in any browser"),
     { isInstalled: !1, browser: null }
   );
 }

@@@ function 'dZA' (was 'eBA') — structural (51.5%)
--- pretty-v2.1.25.js:310029
+++ pretty-v2.1.26.js:310400
@@ -1,28 +1,26 @@
 function eBA(A, K, q, Y, z, w, H) {
+  let J;
   if (!H) H = {};
-  if (typeof H === "function") H = { callback: H };
+  else if (typeof H === "function") J = { callback: H };
+  else J = H;
   if (typeof H.context > "u") H.context = 4;
+  let O = J.context;
   if (H.newlineIsToken)
     throw Error(
       "newlineIsToken may not be used with patch-generation functions, only with diffing functions",
     );
   if (!H.callback) return X(X_1(q, Y, H));
   else {
-    var J = H,
-      O = J.callback;
+    let { callback: $ } = J;
     X_1(
       q,
       Y,
-      qj7(
-        qj7({}, H),
-        {},
-        {
-          callback: function (_) {
-            var G = X(_);
-            O(G);
-          },
+      Object.assign(Object.assign({}, J), {
+        callback: (_) => {
+          let G = X(_);
+          $(G);
         },
-      ),
+      }),
     );
   }
   function X($) {
@@ -38,56 +36,41 @@
       W = 0,
       D = [],
       j = 1,
-      M = 1,
-      P = function () {
-        var y = $[f],
-          B = y.lines || fRY(y.value);
-        if (((y.lines = B), y.added || y.removed)) {
-          var b;
-          if (!Z) {
-            var F = $[f - 1];
-            if (((Z = j), (W = M), F))
-              ((D = H.context > 0 ? _(F.lines.slice(-H.context)) : []),
-                (Z -= D.length),
-                (W -= D.length));
+      M = 1;
+    for (let P = 0; P < $.length; P++) {
+      let f = $[P],
+        N = f.lines || ZEY(f.value);
+      if (((f.lines = N), f.added || f.removed)) {
+        if (!Z) {
+          let T = $[P - 1];
+          if (((Z = j), (W = M), T))
+            ((D = O > 0 ? _(T.lines.slice(-O)) : []),
+              (Z -= D.length),
+              (W -= D.length));
+        }
+        for (let T of N) D.push((f.added ? "+" : "-") + T);
+        if (f.added) M += N.length;
+        else j += N.length;
+      } else {
+        if (Z)
+          if (N.length <= O * 2 && P < $.length - 2)
+            for (let T of _(N)) D.push(T);
+          else {
+            let T = Math.min(N.length, O);
+            for (let R of _(N.slice(0, T))) D.push(R);
+            let C = {
+              oldStart: Z,
+              oldLines: j - Z + T,
+              newStart: W,
+              newLines: M - W + T,
+              lines: D,
+            };
+            (G.push(C), (Z = 0), (W = 0), (D = []));
           }
-          if (
-            ((b = D).push.apply(
-              b,
-              QM6(
-                B.map(function (c) {
-                  return (y.added ? "+" : "-") + c;
-                }),
-              ),
-            ),
-            y.added)
-          )
-            M += B.length;
-          else j += B.length;
-        } else {
-          if (Z)
-            if (B.length <= H.context * 2 && f < $.length - 2) {
-              var Q;
-              (Q = D).push.apply(Q, QM6(_(B)));
-            } else {
-              var u,
-                d = Math.min(B.length, H.context);
-              (u = D).push.apply(u, QM6(_(B.slice(0, d))));
-              var r = {
-                oldStart: Z,
-                oldLines: j - Z + d,
-                newStart: W,
-                newLines: M - W + d,
-                lines: D,
-              };
-              (G.push(r), (Z = 0), (W = 0), (D = []));
-            }
-          ((j += B.length), (M += B.length));
-        }
-      };
-    for (var f = 0; f < $.length; f++) P();
-    for (var N = 0, T = G; N < T.length; N++) {
-      var C = T[N];
+        ((j += N.length), (M += N.length));
+      }
+    }
+    for (let P of G)
       for (var R = 0; R < C.lines.length; R++)
         if (
           C.lines[R].endsWith(`
@@ -95,7 +78,6 @@
         )
           C.lines[R] = C.lines[R].slice(0, -1);
         else (C.lines.splice(R + 1, 0, "\\ No newline at end of file"), R++);
-    }
     return {
       oldFileName: A,
       newFileName: K,

@@@ variable 'qb6' (was 'Ju6') — structural (51.4%)
--- pretty-v2.1.25.js:459062
+++ pretty-v2.1.26.js:455144
@@ -1,3 +1,11 @@
 var Ju6 = k(() => {
-  kJK = ["User", "Project", "Local", "Managed", "ExperimentalUltraClaudeMd"];
+  Ur();
+  A2K = [
+    "User",
+    "Project",
+    "Local",
+    "Managed",
+    "ExperimentalUltraClaudeMd",
+    "AutoMem",
+  ];
 });

@@@ function 'IMK' (was 'jRY') — structural (50.0%)
--- pretty-v2.1.25.js:309978
+++ pretty-v2.1.26.js:519577
@@ -1,3 +1,3 @@
 function jRY(A) {
-  if (Array.isArray(A)) return cM6(A);
+  return A.bridgeConfig ? Zg6(A) : A.getSocketPaths ? kMK(A) : sT1(A);
 }

@@@ function 'Pg6' (was 'VQ6') — structural (48.3%)
--- pretty-v2.1.25.js:522927
+++ pretty-v2.1.26.js:519580
@@ -1,6 +1,6 @@
-function VQ6(A) {
+function Pg6(A, K) {
   let { serverName: K, logger: q } = A,
-    Y = A.getSocketPaths ? nNK(A) : GE1(A),
+    z = K ?? IMK(A),
     z = new HcA(
       { name: K, version: "1.0.0" },
       { capabilities: { tools: {}, logging: {} } },
@@ -13,7 +13,7 @@
     z.setRequestHandler(HqA, async (w) => {
       return (
         q.info(`[${K}] Executing tool: ${w.params.name}`),
-        await aNK(A, Y, w.params.name, w.params.arguments || {})
+        RMK(A, z, H.params.name, H.params.arguments || {})
       );
     }),
     Y.setNotificationHandler((w) => {

@@@ function 'Ll2' (was 'at2') — structural (46.2%)
--- pretty-v2.1.25.js:536625
+++ pretty-v2.1.26.js:533323
@@ -1,12 +1,8 @@
 async function at2(A) {
-  if ((pE1(), !Rj())) ap();
+  HVA();
   try {
-    if ((await KAA.parseAsync(A, { from: "user" }), !Rj()))
-      await (await ap())?.flush();
-    return 0;
+    return (await Qe.parseAsync(A, { from: "user" }), 0);
   } catch (K) {
-    if ((console.error(O1.red("Error:"), K), !Rj()))
-      await (await ap())?.flush();
-    return 1;
+    return (console.error(O1.red("Error:"), K), 1);
   }
 }

@@@ variable 'f$4' (was 'TG4') — structural (44.2%)
--- pretty-v2.1.25.js:183743
+++ pretty-v2.1.26.js:183775
@@ -5,19 +5,23 @@
   VG4();
   ((Qk = o($A(), 1)),
     (a3 = Qk.default.memo(function (K) {
-      let q = s(9),
-        { children: Y } = K;
+      let q = s(12),
+        { children: Y, dimColor: z } = K;
       if (typeof Y !== "string") {
-        let O = String(Y),
-          X;
-        if (q[0] !== O)
-          ((X = Qk.default.createElement($G, null, O)), (q[0] = O), (q[1] = X));
-        else X = q[1];
+        let X;
+        if (q[0] !== Y || q[1] !== z)
+          ((X = z
+            ? wM.default.createElement(n0, { dim: !0 }, String(Y))
+            : wM.default.createElement(n0, null, String(Y))),
+            (q[0] = Y),
+            (q[1] = z),
+            (q[2] = X));
+        else X = q[2];
         return X;
       }
       if (Y === "") return null;
-      let z, w, H;
-      if (q[2] !== Y) {
+      let w, H;
+      if (q[3] !== Y || q[4] !== z) {
         H = Symbol.for("react.early_return_sentinel");
         A: {
           let O = r69(Y);
@@ -26,21 +30,47 @@
             break A;
           }
           if (O.length === 1 && Object.keys(O[0].props).length === 0) {
-            H = Qk.default.createElement($G, null, O[0].text);
+            H = z
+              ? wM.default.createElement(n0, { dim: !0 }, X[0].text)
+              : wM.default.createElement(n0, null, X[0].text);
             break A;
           }
-          ((z = $G), (w = O.map(t69)));
+          let $;
+          if (q[7] !== z)
+            (($ = (_, G) => {
+              let { hyperlink: Z, ...W } = _.props;
+              if (z) W.dim = !0;
+              let D = Object.keys(W).length > 0;
+              if (Z)
+                return D
+                  ? wM.default.createElement(
+                      q7,
+                      { key: G, url: Z },
+                      wM.default.createElement(V$4, { ...W }, _.text),
+                    )
+                  : wM.default.createElement(q7, { key: G, url: Z }, _.text);
+              return D
+                ? wM.default.createElement(V$4, { key: G, ...W }, _.text)
+                : _.text;
+            }),
+              (q[7] = z),
+              (q[8] = $));
+          else $ = q[8];
+          w = X.map($);
         }
-        ((q[2] = Y), (q[3] = z), (q[4] = w), (q[5] = H));
-      } else ((z = q[3]), (w = q[4]), (H = q[5]));
+        ((q[3] = Y), (q[4] = z), (q[5] = w), (q[6] = H));
+      } else ((w = q[5]), (H = q[6]));
       if (H !== Symbol.for("react.early_return_sentinel")) return H;
-      let J;
-      if (q[6] !== z || q[7] !== w)
-        ((J = Qk.default.createElement(z, null, w)),
-          (q[6] = z),
-          (q[7] = w),
-          (q[8] = J));
-      else J = q[8];
+      let J = w,
+        O;
+      if (q[9] !== J || q[10] !== z)
+        ((O = z
+          ? wM.default.createElement(n0, { dim: !0 }, J)
+          : wM.default.createElement(n0, null, J)),
+          (q[9] = J),
+          (q[10] = z),
+          (q[11] = O));
+      else O = q[11];
       return J;
     })));
   a69 = {

@@@ function 'Tg6' (was 'vQ6') — structural (42.5%)
--- pretty-v2.1.25.js:523097
+++ pretty-v2.1.26.js:519799
@@ -1,6 +1,9 @@
 function vQ6() {
   let A = n9(),
-    K = OYA.map((q) => `mcp__claude-in-chrome__${q.name}`);
+    K = U9A.map((z) => `mcp__claude-in-chrome__${z.name}`),
+    q = {};
+  if (Xl()) q.CLAUDE_CHROME_PERMISSION_MODE = "skip_all_permission_checks";
+  let Y = Object.keys(q).length > 0;
   if (A) {
     let q = `"${process.execPath}" --chrome-native-host`;
     return (
@@ -12,6 +15,7 @@
             command: process.execPath,
             args: ["--claude-in-chrome-mcp"],
             scope: "dynamic",
+            ...(Y && { env: q }),
           },
         },
         allowedTools: K,
@@ -33,6 +37,7 @@
             command: process.execPath,
             args: [`${z}`, "--claude-in-chrome-mcp"],
             scope: "dynamic",
+            ...(Y && { env: q }),
           },
         },
         allowedTools: K,

=== String Changes ===

@@@ variable 'Vs' (was 'ys') — string-only
--- pretty-v2.1.25.js:334512
+++ pretty-v2.1.26.js:334574
@@ -43,14 +43,14 @@
       let D = X.get(W);
       if (D !== void 0) {
         h(
-          `Skipping duplicate skill '${G.name}' from ${G.source} (same inode already loaded from ${D})`,
+          `Skipping duplicate skill '${G.name}' from ${G.source} (same file already loaded from ${D})`,
         );
         continue;
       }
       (X.set(W, G.source), $.push(G));
     }
     let _ = O.length - $.length;
-    if (_ > 0) h(`Deduplicated ${_} skills (same inode)`);
+    if (_ > 0) h(`Deduplicated ${_} skills (same file)`);
     return (
       h(
         `Loaded ${$.length} unique skills (managed: ${z.length}, user: ${w.length}, project: ${H.flat().length}, legacy commands: ${J.length})`,
