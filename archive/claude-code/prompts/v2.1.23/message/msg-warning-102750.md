---
id: msg-warning-102750
name: Warning Message
category: message
subcategory: warning
source_line: 102750
---

;
});
import { resolve as uc1, join as DO5 } from "path";
import { statSync as jO5, readFileSync as MO5 } from "fs";
function KCA(A) {
  let K = A.match(/^([^(]+)\(([^)]+)\)$/);
  if (!K) return { toolName: A };
  let q = K[1],
    Y = K[2];
  if (!q || !Y) return { toolName: A };
  return { toolName: q, ruleContent: Y };
}
function PO5(A) {
  return A.match(/^(.+):\*$/)?.[1] ?? null;
}
function xc1(A, K) {
  if (A.startsWith("//")) return A.slice(1);
  if (A.startsWith("/") && !A.startsWith("//")) {
    let q = nJA(K);
    return uc1(q, A.slice(1));
  }
  return A;
}
function Bc1(A) {
  let K = A.permissions || {},
    q = [],
    Y = [];
  for (let G of A.sandbox?.network?.allowedDomains || []) q.push(G);
  for (let G of K.allow || []) {
    let Z = KCA(G);
    if (Z.toolName === wO && Z.ruleContent?.startsWith("domain:"))
      q.push(Z.ruleContent.substring(7));
  }
  for (let G of K.deny || []) {
    let Z = KCA(G);
    if (Z.toolName === wO && Z.ruleContent?.startsWith("domain:"))
      Y.push(Z.ruleContent.substring(7));
  }
  let z = ["."],
    w = [],
    H = [],
    J = XV.map((G) => pO(G)).filter((G) => G !== void 0);
  w.push(...J);
  let O = bg(),
    X = V8();
  if (O !== X)
    (w.push(uc1(O, ".claude", "settings.json")),
      w.push(uc1(O, ".claude", "settings.local.json")));
  let $ = DO5(O, ".git");
  try {
    if (jO5($).isFile()) {
      let W = MO5($, { encoding: "utf8" }).match(/^gitdir:\s*(.+)$/m);
      if (W?.[1]) {
        let D = W[1].trim(),
          j = D.indexOf(".git");
        if (j > 0) {
          let M = D.substring(0, j - 1);
          if (M !== O) z.push(M);
        }
      }
    }
  } catch {}
  for (let G of XV) {
    let Z = E4(G);
    if (!Z?.permissions) continue;
    for (let W of Z.permissions.allow || []) {
      let D = KCA(W);
      if (D.toolName === m5 && D.ruleContent) z.push(xc1(D.ruleContent, G));
    }
    for (let W of Z.permissions.deny || []) {
      let D = KCA(W);
      if (D.toolName === m5 && D.ruleContent) w.push(xc1(D.ruleContent, G));
      if (D.toolName === eq && D.ruleContent) H.push(xc1(D.ruleContent, G));
    }
  }
  let _ = A.sandbox?.ripgrep
    ? A.sandbox.ripgrep
    : (() => {
        let { rgPath: G, rgArgs: Z } = UwA();
        return { command: G, args: Z };
      })();
  return {
    network: {
      allowedDomains: q,
      deniedDomains: Y,
      allowUnixSockets: A.sandbox?.network?.allowUnixSockets,
      allowAllUnixSockets: A.sandbox?.network?.allowAllUnixSockets,
      allowLocalBinding: A.sandbox?.network?.allowLocalBinding,
      httpProxyPort: A.sandbox?.network?.httpProxyPort,
      socksProxyPort: A.sandbox?.network?.socksProxyPort,
    },
    filesystem: { denyRead: H, allowWrite: z, denyWrite: w },
    ignoreViolations: A.sandbox?.ignoreViolations,
    enableWeakerNestedSandbox: A.sandbox?.enableWeakerNestedSandbox,
    ripgrep: _,
  };
}
function yx8() {
  try {
    let A = J8();
    return Rx8(A);
  } catch (A) {
    return (h(
