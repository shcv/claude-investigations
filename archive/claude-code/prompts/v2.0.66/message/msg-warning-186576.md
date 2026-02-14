---
id: msg-warning-186576
name: Warning Message
category: message
subcategory: warning
source_line: 186576
---

), []);
  }
}
function mA6() {
  let A = ["flagSettings", "policySettings"];
  for (let Q of A) {
    let B = uB(Q);
    if (
      B?.sandbox?.enabled !== void 0 ||
      B?.sandbox?.autoAllowBashIfSandboxed !== void 0 ||
      B?.sandbox?.allowUnsandboxedCommands !== void 0
    )
      return !0;
  }
  return !1;
}
async function dA6(A) {
  let Q = uB("localSettings");
  X2("localSettings", {
    sandbox: {
      ...Q?.sandbox,
      ...(A.enabled !== void 0 && { enabled: A.enabled }),
      ...(A.autoAllowBashIfSandboxed !== void 0 && {
        autoAllowBashIfSandboxed: A.autoAllowBashIfSandboxed,
      }),
      ...(A.allowUnsandboxedCommands !== void 0 && {
        allowUnsandboxedCommands: A.allowUnsandboxedCommands,
      }),
    },
  });
}
function cA6() {
  return CQ()?.sandbox?.excludedCommands ?? [];
}
async function pA6(A, Q, B, G) {
  if (DpA())
    if ($c) await $c;
    else throw Error("Sandbox failed to initialize. ");
  return dY.wrapWithSandbox(A, Q, B, G);
}
async function lA6(A) {
  if ($c) return $c;
  if (!DpA()) return;
  let Q = CQ(),
    B = nx1(Q);
  return (
    ($c = (async () => {
      try {
        (await dY.initialize(B, A),
          (ax1 = SF.subscribe(() => {
            let G = CQ(),
              Z = nx1(G);
            (dY.updateConfig(Z),
              f("Sandbox configuration updated from settings change"));
          })));
      } catch (G) {
        (($c = void 0),
          f(
            
