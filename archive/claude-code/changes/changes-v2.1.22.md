--- archive/claude-code/pretty/pretty-v2.1.21.js
+++ archive/claude-code/pretty/pretty-v2.1.22.js
Structural similarity: 99.9%
Matched: 14314/14329 vs 14329
Changes: 15 added, 15 removed, 371 structural, 39 string-only (13904 unchanged)

Filtered: 57 version bumps, 353 reformatting-only changes

=== Import Style Changes ===

"child_process":
  - import NYY from "child_process";
  - import TYY from "child_process";
  + import { execFile as JWq, spawn as OWq, spawnSync as XWq } from "child_process";
  + import { spawn as Ez5, spawnSync as kz5 } from "child_process";

"crypto":
  - import _4Y from "crypto";
  - import Z4Y from "crypto";
  + import { randomBytes as po2, randomUUID as do2 } from "crypto";
  + import { randomBytes as sKz, timingSafeEqual as tKz } from "crypto";

"https":
  - import O17 from "https";
  + import { Agent as xn3 } from "https";

"node:child_process":
  - import UR1 from "node:child_process";
  - import xK7 from "node:child_process";
  + import { execFile as s9Y, execFileSync as vFw } from "node:child_process";
  + import { execFileSync as DR2, spawn as jR2 } from "node:child_process";

"node:fs":
  - import g9Y from "node:fs";
  - import U9Y from "node:fs";
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
  - import Q9Y from "node:os";
  + import { homedir as BKz } from "node:os";

"node:path":
  - import bK7 from "node:path";
  + import {
  +   join as GX,
  +   dirname as id,
  +   resolve as Wm,
  +   delimiter as zb2,
  +   basename as wb2,
  + } from "node:path";

"node:process":
  - import dvK from "node:process";
  + import { cwd as v04 } from "node:process";

"node:util":
  - import ce9 from "node:util";
  + import { isDeepStrictEqual as ZgK } from "node:util";

"path":
  - import D9Y from "path";
  + import { dirname as KKz, join as hFK } from "path";

"stream":
  - import hzA from "stream";
  + import { PassThrough as kKz } from "stream";
