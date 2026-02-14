---
id: msg-warning-533014
name: Warning Message
category: message
subcategory: warning
source_line: 533014
---

,
        );
      w[X] = O.name;
    }
    let H = {
        clients: A.map(_s2),
        configs: z,
        tools: Y,
        resources: q,
        normalizedNames: w,
      },
      J = gE1();
    await Os2(J, UA(H, null, 2));
  } catch {}
}
var xVA = k(() => {
  q6();
  R2();
  IG();
  b1();
});
import { join as dv, posix as se, sep as FL } from "path";
import { homedir as Zs2, tmpdir as Ws2 } from "os";
function XN(A) {
  return A.toLowerCase();
}
function CEK(A, K) {
  if (o6() === "windows") {
    let q = Kb(A),
      Y = Kb(K);
    return se.relative(q, Y);
  }
  return se.relative(A, K);
}
function $A1(A) {
  if (o6() === "windows") return Kb(A);
  return A;
}
function Ms2() {
  return XV.map((A) => pO(A)).filter((A) => A !== void 0);
}
function Vf6(A) {
  let K = x7(A),
    q = XN(K);
  if (
    q.endsWith("/.claude/settings.json") ||
    q.endsWith("/.claude/settings.local.json")
  )
    return !0;
  return Ms2().some((Y) => XN(Y) === q);
}
function Ps2(A) {
  if (Vf6(A)) return !0;
  let K = dv(V8(), ".claude", "commands"),
    q = dv(V8(), ".claude", "agents"),
    Y = dv(V8(), ".claude", "skills");
  return HU(A, K) || HU(A, q) || HU(A, Y);
}
function Vs2(A) {
  if (!Wc()) return !1;
  let K = x7(A);
  return HU(K, Wc());
}
function LEK(A) {
  let K = dv(tZ(), QxA());
  return A.startsWith(K) && A.endsWith(".md");
}
function _E1() {
  return dv(yJ(x1()), d1(), "session-memory") + FL;
}
function M9A() {
  return dv(_E1(), "summary.md");
}
function fs2(A) {
  return A.startsWith(_E1());
}
function Ns2(A) {
  let K = yJ(x1());
  return A === K || A.startsWith(K + FL);
}
function CVA() {
  return aY("tengu_scratch");
}
function xu6() {
  if (o6() === "windows") return "claude";
  return 
