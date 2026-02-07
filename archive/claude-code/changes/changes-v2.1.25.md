--- archive/claude-code/pretty/pretty-v2.1.23.js
+++ archive/claude-code/pretty/pretty-v2.1.25.js
Structural similarity: 99.9%
Matched: 14430/14445 vs 14445
Changes: 15 added, 15 removed, 381 structural, 36 string-only (14013 unchanged)

Filtered: 54 version bumps, 362 reformatting-only changes

=== Import Style Changes ===

"child_process":
  - import I2Y from "child_process";
  - import S2Y from "child_process";
  + import { execFile as WDq, spawn as DDq, spawnSync as jDq } from "child_process";
  + import { spawn as Sw5, spawnSync as hw5 } from "child_process";

"crypto":
  - import f7Y from "crypto";
  - import N7Y from "crypto";
  + import { randomBytes as xs2, randomUUID as us2 } from "crypto";
  + import { randomBytes as P3z, timingSafeEqual as V3z } from "crypto";

"https":
  - import H67 from "https";
  + import { Agent as Ur3 } from "https";

"node:child_process":
  - import My1 from "node:child_process";
  - import hq7 from "node:child_process";
  + import { execFile as H2Y, execFileSync as dUw } from "node:child_process";
  + import { execFileSync as Ty2, spawn as vy2 } from "node:child_process";

"node:fs":
  - import nYY from "node:fs";
  - import aYY from "node:fs";
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
  - import oYY from "node:os";
  + import { homedir as Y3z } from "node:os";

"node:path":
  - import Sq7 from "node:path";
  + import {
  +   join as fX,
  +   dirname as ed,
  +   resolve as Em,
  +   delimiter as Wx2,
  +   basename as Dx2,
  + } from "node:path";

"node:process":
  - import iEK from "node:process";
  + import { cwd as PX4 } from "node:process";

"node:util":
  - import eAY from "node:util";
  + import { isDeepStrictEqual as fFK } from "node:util";

"path":
  - import EYY from "path";
  + import { dirname as T5z, join as QQK } from "path";

"stream":
  - import izA from "stream";
  + import { PassThrough as i5z } from "stream";

=== Structural Changes ===

@@@ variable 'ok' — structural (81.7%)
--- pretty-v2.1.23.js:193152
+++ pretty-v2.1.25.js:193151
@@ -28,7 +28,7 @@
     if (z && G4("tengu_scarf_coffee", !1)) K.push(EnA);
     if (Y === "vertex" && TG9(A)) K.push(YR1);
     if (Y === "foundry") K.push(YR1);
-    if (Y === "firstParty") K.push(gn6);
+    if (z) K.push(Fn6);
     if (process.env.ANTHROPIC_BETAS && !q)
       K.push(
         ...process.env.ANTHROPIC_BETAS.split(",")
