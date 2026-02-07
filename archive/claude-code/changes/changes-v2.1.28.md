--- archive/claude-code/pretty/pretty-v2.1.27.js
+++ archive/claude-code/pretty/pretty-v2.1.28.js
Structural similarity: 99.9%
Matched: 14289/14304 vs 14304
Changes: 15 added, 15 removed, 390 structural, 38 string-only (13861 unchanged)

Filtered: 56 version bumps, 367 reformatting-only changes

=== Import Style Changes ===

"child_process":
  - import _k9 from "child_process";
  - import Jk9 from "child_process";
  + import { execFile as x6K, spawn as b6K, spawnSync as u6K } from "child_process";
  + import { spawn as mI5, spawnSync as FI5 } from "child_process";

"crypto":
  - import eG9 from "crypto";
  - import AZ9 from "crypto";
  + import { randomBytes as z1z, randomUUID as w1z } from "crypto";
  + import { randomBytes as gYz, timingSafeEqual as QYz } from "crypto";

"https":
  - import Pl7 from "https";
  + import { Agent as qK5 } from "https";

"node:child_process":
  - import ev6 from "node:child_process";
  - import Ua7 from "node:child_process";
  + import { execFile as FE9, execFileSync as ne2 } from "node:child_process";
  + import { execFileSync as pIY, spawn as dIY } from "node:child_process";

"node:fs":
  - import LE9 from "node:fs";
  - import CE9 from "node:fs";
  + import {
  +   existsSync as iF1,
  +   statSync as CIY,
  +   mkdirSync as SIY,
  +   realpathSync as hIY,
  + } from "node:fs";
  + import {
  +   constants as FIY,
  +   readFileSync as gIY,
  +   existsSync as QIY,
  +   unlinkSync as UIY,
  + } from "node:fs";

"node:os":
  - import yE9 from "node:os";
  + import { homedir as kYz } from "node:os";

"node:path":
  - import Qa7 from "node:path";
  + import {
  +   join as JJ,
  +   dirname as Cp,
  +   resolve as JB,
  +   delimiter as XBY,
  +   basename as DBY,
  + } from "node:path";

"node:process":
  - import r9q from "node:process";
  + import { cwd as vD7 } from "node:process";

"node:util":
  - import Ij9 from "node:util";
  + import { isDeepStrictEqual as hPq } from "node:util";

"path":
  - import YE9 from "path";
  + import { dirname as U9z, join as lWq } from "path";

"stream":
  - import QY1 from "stream";
  + import { PassThrough as MYz } from "stream";

=== Structural Changes ===

@@@ variable 'HY8' — structural (97.3%)
--- pretty-v2.1.27.js:56762
+++ pretty-v2.1.28.js:56751
@@ -273,7 +273,8 @@
       },
       w = { match: t2(/\./, RW(...AC6)), relevance: 0 },
       H = AC6.filter((w1) => typeof w1 === "string").concat(["_|0"]),
-      O = AC6.filter((w1) => typeof w1 !== "string")
+      O = ey6
+        .filter((w1) => typeof w1 !== "string")
         .concat(UKK)
         .map(YC6),
       $ = { variants: [{ className: "keyword", match: RW(...O, ...ey6) }] },

@@@ function 'ft' — structural (87.6%)
--- pretty-v2.1.27.js:512907
+++ pretty-v2.1.28.js:512867
@@ -14,28 +14,7 @@
     let W = await W9q(A),
       G = $11(W);
     for (let Z of G)
-      if (Z.type === "saved_hook_context") {
-        let N = {
-          type: "attachment",
-          uuid: Z.uuid,
-          attachment: {
-            type: "hook_additional_context",
-            content: Z.content,
-            hookName: Z.hookName,
-            toolUseID: Z.toolUseID,
-            hookEvent: Z.hookEvent,
-          },
-          timestamp: Z.timestamp,
-          parentUuid: Z.parentUuid,
-          sessionId: Z.sessionId,
-          cwd: Z.cwd,
-          userType: Z.userType,
-          version: Z.version,
-          isSidechain: Z.isSidechain,
-          gitBranch: Z.gitBranch,
-        };
-        q.set(Z.uuid, N);
-      } else if (Wh(Z)) {
+      if (Wh(Z)) {
         if (
           Z.type === "progress" &&
           Z.data &&

@@@ class 'G9q' (was 'Z9q') — structural (85.2%)
--- pretty-v2.1.27.js:512141
+++ pretty-v2.1.28.js:512133
@@ -77,30 +77,6 @@
           _.sourceToolAssistantUUID
         )
           X = _.sourceToolAssistantUUID;
-        if (
-          _.type === "attachment" &&
-          _.attachment.type === "hook_additional_context" &&
-          mQ1() !== "ant"
-        ) {
-          let j = {
-            type: "saved_hook_context",
-            uuid: _.uuid,
-            content: _.attachment.content,
-            hookName: _.attachment.hookName,
-            toolUseID: _.attachment.toolUseID,
-            hookEvent: _.attachment.hookEvent,
-            timestamp: _.timestamp,
-            parentUuid: J ? null : X,
-            sessionId: O,
-            cwd: y6(),
-            userType: mQ1(),
-            version: M9q,
-            isSidechain: q,
-            gitBranch: H,
-          };
-          (await this.appendEntry(j), (w = _.uuid));
-          continue;
-        }
         let D = {
           parentUuid: J ? null : X,
           logicalParentUuid: J ? w : void 0,
@@ -214,14 +190,6 @@
         { mode: 384 },
       );
     else if (A.type === "attribution-snapshot")
-      Y.appendFileSync(
-        H,
-        B1(A) +
-          `
-`,
-        { mode: 384 },
-      );
-    else if (A.type === "saved_hook_context")
       Y.appendFileSync(
         H,
         B1(A) +

@@@ function 'BkA' (was 'mkA') — structural (83.7%)
--- pretty-v2.1.27.js:431827
+++ pretty-v2.1.28.js:431819
@@ -9,7 +9,7 @@
     H = await $h({
       promptMessages: [r6({ content: z })],
       cacheSafeParams: Y,
-      maxOutputTokens: 500,
+      maxOutputTokens: 16000,
       canUseTool: w,
       querySource: "prompt_suggestion",
       forkLabel: "prompt_suggestion",

@@@ function 'f9q' (was 'N9q') — structural (73.4%)
--- pretty-v2.1.27.js:513105
+++ pretty-v2.1.28.js:513044
@@ -1,9 +1,6 @@
 function N9q(A) {
   return A.filter((q) => {
-    if (q.type === "attachment" && mQ1() !== "ant") {
-      if (q.attachment.type === "hook_additional_context") return !0;
-      return !1;
-    }
+    if (q.type === "attachment" && TIA() !== "ant") return !1;
     return !0;
   }).map((q) => {
     if (
