---
id: msg-warning-186461
name: Warning Message
category: message
subcategory: warning
source_line: 186461
---

;
});
import { resolve as RnQ } from "path";
function vCA(A) {
  let Q = A.match(/^([^(]+)\(([^)]+)\)$/);
  if (!Q) return { toolName: A };
  let B = Q[1],
    G = Q[2];
  if (!B || !G) return { toolName: A };
  return { toolName: B, ruleContent: G };
}
function fA6(A) {
  return A.match(/^(.+):\*$/)?.[1] ?? null;
}
function nx1(A) {
  let Q = A.permissions || {},
    B = [],
    G = [];
  for (let V of A.sandbox?.network?.allowedDomains || []) B.push(V);
  for (let V of Q.allow || []) {
    let E = vCA(V);
    if (E.toolName === mW && E.ruleContent?.startsWith("domain:"))
      B.push(E.ruleContent.substring(7));
  }
  for (let V of Q.deny || []) {
    let E = vCA(V);
    if (E.toolName === mW && E.ruleContent?.startsWith("domain:"))
      G.push(E.ruleContent.substring(7));
  }
  let Z = ["."],
    Y = [],
    J = [],
    I = wL.map((V) => xF(V)).filter((V) => V !== void 0);
  Y.push(...I);
  let X = _BA(),
    W = dQ();
  if (X !== W)
    (Y.push(RnQ(X, ".claude", "settings.json")),
      Y.push(RnQ(X, ".claude", "settings.local.json")));
  for (let V of Q.allow || []) {
    let E = vCA(V);
    if (E.toolName === a6 && E.ruleContent) Z.push(E.ruleContent);
  }
  for (let V of Q.deny || []) {
    let E = vCA(V);
    if (E.toolName === a6 && E.ruleContent) Y.push(E.ruleContent);
    if (E.toolName === V5 && E.ruleContent) J.push(E.ruleContent);
  }
  let K = A.sandbox?.ripgrep
    ? A.sandbox.ripgrep
    : (() => {
        let { rgPath: V, rgArgs: E } = j2A();
        return { command: V, args: E };
      })();
  return {
    network: {
      allowedDomains: B,
      deniedDomains: G,
      allowUnixSockets: A.sandbox?.network?.allowUnixSockets,
      allowAllUnixSockets: A.sandbox?.network?.allowAllUnixSockets,
      allowLocalBinding: A.sandbox?.network?.allowLocalBinding,
      httpProxyPort: A.sandbox?.network?.httpProxyPort,
      socksProxyPort: A.sandbox?.network?.socksProxyPort,
    },
    filesystem: { denyRead: J, allowWrite: Z, denyWrite: Y },
    ignoreViolations: A.sandbox?.ignoreViolations,
    enableWeakerNestedSandbox: A.sandbox?.enableWeakerNestedSandbox,
    ripgrep: K,
  };
}
function bA6() {
  try {
    let A = CQ();
    return _nQ(A);
  } catch (A) {
    return (f(
