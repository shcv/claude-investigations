---
id: msg-warning-102900
name: Warning Message
category: message
subcategory: warning
source_line: 102900
---

), []);
  }
}
function TO5() {
  let A = ["flagSettings", "policySettings"];
  for (let K of A) {
    let q = E4(K);
    if (
      q?.sandbox?.enabled !== void 0 ||
      q?.sandbox?.autoAllowBashIfSandboxed !== void 0 ||
      q?.sandbox?.allowUnsandboxedCommands !== void 0
    )
      return !0;
  }
  return !1;
}
async function vO5(A) {
  let K = E4("localSettings");
  v4("localSettings", {
    sandbox: {
      ...K?.sandbox,
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
function EO5() {
  return J8()?.sandbox?.excludedCommands ?? [];
}
async function kO5(A, K, q, Y) {
  if (e11())
    if (li) await li;
    else throw Error("Sandbox failed to initialize. ");
  return YO.wrapWithSandbox(A, K, q, Y);
}
async function CO5(A) {
  if (li) return li;
  if (!e11()) return;
  let K = J8(),
    q = Bc1(K);
  return (
    (li = (async () => {
      try {
        (await YO.initialize(q, A),
          (mc1 = a_.subscribe(() => {
            let Y = J8(),
              z = Bc1(Y);
            (YO.updateConfig(z),
              h("Sandbox configuration updated from settings change"));
          })));
      } catch (Y) {
        ((li = void 0),
          h(
            
