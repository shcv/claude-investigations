--- archive/claude-code/pretty/pretty-v2.1.28.js
+++ archive/claude-code/pretty/pretty-v2.1.29.js
Structural similarity: 99.9%
Matched: 14289/14304 vs 14304
Changes: 15 added, 15 removed, 372 structural, 38 string-only (13879 unchanged)

Filtered: 56 version bumps, 354 reformatting-only changes

=== Import Style Changes ===

"child_process":
  - import $k9 from "child_process";
  - import _k9 from "child_process";
  + import { execFile as x6K, spawn as b6K, spawnSync as u6K } from "child_process";
  + import { spawn as mI5, spawnSync as FI5 } from "child_process";

"crypto":
  - import tG9 from "crypto";
  - import eG9 from "crypto";
  + import { randomBytes as z1z, randomUUID as w1z } from "crypto";
  + import { randomBytes as gYz, timingSafeEqual as QYz } from "crypto";

"https":
  - import Pl7 from "https";
  + import { Agent as qK5 } from "https";

"node:child_process":
  - import tv6 from "node:child_process";
  - import Ua7 from "node:child_process";
  + import { execFile as FE9, execFileSync as ne2 } from "node:child_process";
  + import { execFileSync as pIY, spawn as dIY } from "node:child_process";

"node:fs":
  - import kE9 from "node:fs";
  - import yE9 from "node:fs";
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
  - import RE9 from "node:os";
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
  - import n9q from "node:process";
  + import { cwd as vD7 } from "node:process";

"node:util":
  - import hj9 from "node:util";
  + import { isDeepStrictEqual as hPq } from "node:util";

"path":
  - import KE9 from "path";
  + import { dirname as U9z, join as lWq } from "path";

"stream":
  - import QY1 from "stream";
  + import { PassThrough as MYz } from "stream";
