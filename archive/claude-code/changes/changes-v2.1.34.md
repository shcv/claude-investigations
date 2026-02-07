--- archive/claude-code/pretty/pretty-v2.1.33.js
+++ archive/claude-code/pretty/pretty-v2.1.34.js
Structural similarity: 99.9%
Matched: 14792/14809 vs 14810
Changes: 18 added, 17 removed, 492 structural, 37 string-only (14263 unchanged)

Filtered: 56 version bumps, 462 reformatting-only changes

=== Import Style Changes ===

"child_process":
  - import ft5 from "child_process";
  - import Vt5 from "child_process";
  + import { execFile as Q9K, spawn as U9K, spawnSync as g9K } from "child_process";
  + import { spawn as CD5, spawnSync as SD5 } from "child_process";

"crypto":
  - import _l5 from "crypto";
  - import Jl5 from "crypto";
  + import { randomBytes as J9z, randomUUID as X9z } from "crypto";
  + import { randomBytes as f0z, timingSafeEqual as V0z } from "crypto";

"https":
  - import i07 from "https";
  + import { Agent as yK5 } from "https";

"node:child_process":
  - import wh6 from "node:child_process";
  - import ZP7 from "node:child_process";
  + import { execFile as as5, execFileSync as pF2 } from "node:child_process";
  + import { execFileSync as OxY, spawn as _xY } from "node:child_process";

"node:fs":
  - import Bs5 from "node:fs";
  - import Qs5 from "node:fs";
  + import {
  +   existsSync as dQ1,
  +   statSync as oIY,
  +   mkdirSync as aIY,
  +   realpathSync as sIY,
  + } from "node:fs";
  + import {
  +   constants as zxY,
  +   readFileSync as wxY,
  +   existsSync as HxY,
  +   unlinkSync as $xY,
  + } from "node:fs";

"node:os":
  - import Fs5 from "node:os";
  + import { homedir as $Mz } from "node:os";

"node:path":
  - import PP7 from "node:path";
  + import {
  +   join as vJ,
  +   dirname as Sd,
  +   resolve as jm,
  +   delimiter as cdY,
  +   basename as ldY,
  + } from "node:path";

"node:process":
  - import q_q from "node:process";
  + import { cwd as F67 } from "node:process";

"node:util":
  - import pU5 from "node:util";
  + import { isDeepStrictEqual as E8q } from "node:util";

"stream":
  - import xz1 from "stream";
  + import { PassThrough as sXz } from "stream";

=== Removed ===

--- Removed Nb1 (pretty-v2.1.33.js:254829-254860)
- var Nb1 = v(() => {
-   m$();
-   M6();
-   L6();
-   m$();
-   Li1();
-   Dz();
-   gXA = KA(async (A) => {
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
- - If you see a <${_P}> tag in the current conversation turn, the skill has ALREADY been loaded - follow the instructions directly instead of calling this tool again
- `;
-   });
- });

--- Removed Oa (pretty-v2.1.33.js:259226-259245)
- var Oa = v(() => {
-   F4();
-   I$6();
-   B6();
-   yA();
-   ((LQ7 = `Search for or select deferred tools to make them available for use.
- 
- **MANDATORY PREREQUISITE - THIS IS A HARD REQUIREMENT**
- 
- You MUST use this tool to load deferred tools BEFORE calling them directly.
- 
- This is a BLOCKING REQUIREMENT - deferred tools listed below are NOT available until you load them using this tool. Both query modes (keyword search and direct selection) load the returned tools — once a tool appears in the results, it is immediately available to call.${RQ7}`),
-     (If9 = `Search for or select deferred tools to make them available for use.
- 
- **MANDATORY PREREQUISITE - THIS IS A HARD REQUIREMENT**
- 
- You MUST use this tool to load deferred tools BEFORE calling them directly.
- 
- This is a BLOCKING REQUIREMENT - deferred tools are NOT available until you load them using this tool. Look for <available-deferred-tools> messages in the conversation for the list of tools you can discover. Both query modes (keyword search and direct selection) load the returned tools — once a tool appears in the results, it is immediately available to call.${RQ7}`));
- });

--- Removed Kx4 (pretty-v2.1.33.js:387528-387534)
- function Kx4() {
-   if (aj1)
-     ((ys = aj1), h(`[TeammateModeSnapshot] Captured from CLI override: ${ys}`));
-   else
-     ((ys = j6().teammateMode ?? "auto"),
-       h(`[TeammateModeSnapshot] Captured from config: ${ys}`));
- }

=== Added ===

+++ Added kb1 (pretty-v2.1.34.js:256188-256219)
+ var kb1 = v(() => {
+   m$();
+   M6();
+   L6();
+   m$();
+   Ri1();
+   Dz();
+   A0A = KA(async (A) => {
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
+ - If you see a <${JP}> tag in the current conversation turn, the skill has ALREADY been loaded - follow the instructions directly instead of calling this tool again
+ `;
+   });
+ });

+++ Added Xa (pretty-v2.1.34.js:260600-260619)
+ var Xa = v(() => {
+   x4();
+   i$6();
+   B6();
+   yA();
+   ((KU7 = `Search for or select deferred tools to make them available for use.
+ 
+ **MANDATORY PREREQUISITE - THIS IS A HARD REQUIREMENT**
+ 
+ You MUST use this tool to load deferred tools BEFORE calling them directly.
+ 
+ This is a BLOCKING REQUIREMENT - deferred tools listed below are NOT available until you load them using this tool. Both query modes (keyword search and direct selection) load the returned tools — once a tool appears in the results, it is immediately available to call.${YU7}`),
+     (ef9 = `Search for or select deferred tools to make them available for use.
+ 
+ **MANDATORY PREREQUISITE - THIS IS A HARD REQUIREMENT**
+ 
+ You MUST use this tool to load deferred tools BEFORE calling them directly.
+ 
+ This is a BLOCKING REQUIREMENT - deferred tools are NOT available until you load them using this tool. Look for <available-deferred-tools> messages in the conversation for the list of tools you can discover. Both query modes (keyword search and direct selection) load the returned tools — once a tool appears in the results, it is immediately available to call.${YU7}`));
+ });

+++ Added XI4 (pretty-v2.1.34.js:382063-382069)
+ function XI4() {
+   if (tj1)
+     ((vs = tj1), h(`[TeammateModeSnapshot] Captured from CLI override: ${vs}`));
+   else
+     ((vs = j6().teammateMode ?? "auto"),
+       h(`[TeammateModeSnapshot] Captured from config: ${vs}`));
+ }

+++ Added iEq (pretty-v2.1.34.js:566127-566133)
+ var iEq = v(() => {
+   Ww();
+   L6();
+   V61();
+   E3();
+   K8();
+ });

=== Structural Changes ===

@@@ variable 'zH' — structural (98.0%)
--- pretty-v2.1.33.js:63168
+++ pretty-v2.1.34.js:63160
@@ -230,8 +230,7 @@
       if (A.signer) $ = qi.normalizeProvider(A.signer);
       else if (A.regionInfoProvider)
         $ = () =>
-          qi
-            .normalizeProvider(A.region)()
+          Ki.normalizeProvider(A.region)()
             .then(async (_) => [
               (await A.regionInfoProvider(_, {
                 useFipsEndpoint: await A.useFipsEndpoint(),

@@@ function 'x91' (was 'h91') — structural (96.4%)
--- pretty-v2.1.33.js:553656
+++ pretty-v2.1.34.js:553667
@@ -1217,8 +1217,13 @@
     },
     [lG, o],
   );
-  if (p8()) ljq({ isLoading: B7, focusedInputDialog: u_, onSubmitMessage: kA });
-  (Sjq({ isLoading: B7, onSubmitMessage: kA }),
+  (ijq({
+    enabled: p8(),
+    isLoading: B7,
+    focusedInputDialog: u_,
+    onSubmitMessage: kA,
+  }),
+    hjq({ isLoading: B7, onSubmitMessage: kA }),
     cA.useEffect(() => {
       return (
         BZ1(),

@@@ variable 'Ot7' (was '_t7') — structural (95.6%)
--- pretty-v2.1.33.js:292119
+++ pretty-v2.1.34.js:292066
@@ -273,8 +273,7 @@
       },
       w = { match: bw(/\./, MZ(...yMA)), relevance: 0 },
       H = yMA.filter((A1) => typeof A1 === "string").concat(["_|0"]),
-      $ = yMA
-        .filter((A1) => typeof A1 !== "string")
+      $ = CMA.filter((A1) => typeof A1 !== "string")
         .concat(LC9)
         .map(hMA),
       O = { variants: [{ className: "keyword", match: MZ(...$, ...RMA) }] },

@@@ function 'b3z' (was 'x3z') — structural (90.3%)
--- pretty-v2.1.33.js:514506
+++ pretty-v2.1.34.js:514497
@@ -14,7 +14,8 @@
       !(
         A.name === f4 &&
         F8.isSandboxingEnabled() &&
-        F8.isAutoAllowBashIfSandboxedEnabled()
+        I8.isAutoAllowBashIfSandboxedEnabled() &&
+        td(q)
       )
     )
       return {

@@@ function 'r$6' (was 'b$6') — structural (89.3%)
--- pretty-v2.1.33.js:259115
+++ pretty-v2.1.34.js:260491
@@ -17,12 +17,10 @@
     : q.map((Y) => Y.name).join(`
 `);
   if ($a !== void 0 && K !== $a) {
-    let Y = $a
-        .split(
-          `
+    let Y = Ja.split(
+        `
 `,
-        )
-        .filter(Boolean).length,
+      ).filter(Boolean).length,
       z = K.split(
         `
 `,

@@@ variable 'pB' (was 'ip') — structural (87.9%)
--- pretty-v2.1.33.js:386587
+++ pretty-v2.1.34.js:514255
@@ -18,6 +18,7 @@
   B6();
   I6();
   rf();
+  rf();
   OZY = new Set([
     "GOEXPERIMENT",
     "GOOS",

@@@ function 'jOq' (was 'MOq') — structural (80.5%)
--- pretty-v2.1.33.js:520599
+++ pretty-v2.1.34.js:520598
@@ -10,6 +10,7 @@
     ...(A.accountUuid && { accountUUID: A.accountUuid }),
     ...(A.userType && { userType: A.userType }),
     ...(A.subscriptionType && { subscriptionType: A.subscriptionType }),
+    ...(A.rateLimitTier && { rateLimitTier: A.rateLimitTier }),
     ...(A.firstTokenTime && { firstTokenTime: A.firstTokenTime }),
     ...(q && { email: q }),
     ...(A.appVersion && { appVersion: A.appVersion }),

@@@ variable 'zJ' (was '$J') — structural (75.8%)
--- pretty-v2.1.33.js:514668
+++ pretty-v2.1.34.js:514660
@@ -17,5 +17,6 @@
   V8();
   B6();
   b$();
+  b$();
   CuA = [...Pf, "cliArg", "command", "session"];
 });

@@@ variable 'EJq' (was 'vJq') — structural (72.4%)
--- pretty-v2.1.33.js:529208
+++ pretty-v2.1.34.js:529210
@@ -21,5 +21,6 @@
   Q06();
   U06();
   NJq();
+  TJq();
   ((gO = s(J1(), 1)), (L_ = s(J1(), 1)));
 });

@@@ variable 'v81' (was 'N81') — structural (60.6%)
--- pretty-v2.1.33.js:520533
+++ pretty-v2.1.34.js:520526
@@ -9,9 +9,14 @@
     let q = Ah(),
       K = j6(),
       Y,
+      z,
       z;
     if (A) {
-      if (((Y = JK() ?? void 0), Y && K.claudeCodeFirstTokenDate)) {
+      if (
+        ((Y = JK() ?? void 0),
+        (z = si() ?? void 0),
+        Y && K.claudeCodeFirstTokenDate)
+      ) {
         let O = new Date(K.claudeCodeFirstTokenDate).getTime();
         if (!isNaN(O)) z = O;
       }
@@ -28,15 +33,16 @@
           "report the issue at https://github.com/anthropics/claude-code/issues",
         PACKAGE_URL: "@anthropic-ai/claude-code",
         README_URL: "https://code.claude.com/docs/en/overview",
-        VERSION: "2.1.33",
+        VERSION: "2.1.34",
         FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
-        BUILD_TIME: "2026-02-06T00:14:56Z",
+        BUILD_TIME: "2026-02-06T06:36:54Z",
       }.VERSION,
       platform: SA.platform,
       organizationUuid: H,
       accountUuid: $,
       userType: "external",
       subscriptionType: Y,
+      rateLimitTier: z,
       firstTokenTime: z,
       ...(process.env.GITHUB_ACTIONS === "true" && {
         githubActionsMetadata: {

@@@ function 'ijq' (was 'ljq') — structural (51.6%)
--- pretty-v2.1.33.js:547953
+++ pretty-v2.1.34.js:547956
@@ -1,4 +1,9 @@
-function ljq({ isLoading: A, focusedInputDialog: q, onSubmitMessage: K }) {
+function ijq({
+  enabled: A,
+  isLoading: q,
+  focusedInputDialog: K,
+  onSubmitMessage: Y,
+}) {
   let Y = K,
     z = G_(),
     w = b7(),
@@ -6,6 +11,7 @@
     $ = rb(),
     O = ve.useRef(A),
     _ = ve.useCallback(() => {
+      if (!A) return;
       let D = z.getState(),
         M = kT6(D);
       if (!M) return;
@@ -399,8 +405,9 @@
           (h("[InboxPoller] Submission rejected, queuing for later delivery"),
             S());
       } else (h("[InboxPoller] Session busy, queuing for later delivery"), S());
-    }, [A, q, Y, w, $, z]);
+    }, [A, q, K, z, H, O, w]);
   ve.useEffect(() => {
+    if (!A) return;
     let D = O.current;
     if (((O.current = A), A || q)) return;
     let M = z.getState();
@@ -438,12 +445,13 @@
         inbox: { messages: k.inbox.messages.filter((y) => !T.has(y.id)) },
       }));
     } else h("[InboxPoller] Submission rejected, keeping messages queued");
-  }, [A, q, Y, w, H, z]);
-  let J = !!kT6(z.getState());
+  }, [A, q, K, z, H, $, w]);
+  let X = A && !!LT6(w.getState());
   DX(_, J ? __z : null);
   let X = ve.useRef(!1);
   ve.useEffect(() => {
+    if (!A) return;
     if (X.current) return;
     if (kT6(z.getState())) ((X.current = !0), _());
-  }, [_, z]);
+  }, [A, J, w]);
 }
