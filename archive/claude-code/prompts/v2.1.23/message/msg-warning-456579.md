---
id: msg-warning-456579
name: Warning Message
category: message
subcategory: warning
source_line: 456579
---

,
        { level: "warn" },
      );
    }
  let H = q ?? pnA();
  for await (let J of dx6(A, K, H, Y)) {
    if (J.message) z.push(J.message);
    if (J.additionalContexts && J.additionalContexts.length > 0)
      w.push(...J.additionalContexts);
  }
  if (w.length > 0) {
    let J = PK({
      type: "hook_additional_context",
      content: w,
      hookName: "SessionStart",
      toolUseID: "SessionStart",
      hookEvent: "SessionStart",
    });
    z.push(J);
  }
  return z;
}
async function sf1(A, K) {
  let q = [],
    Y = [];
  if (Ip()) h("Skipping plugin hooks - allowManagedHooksOnly is enabled");
  else
    try {
      await Qd();
    } catch (z) {
      let w = z instanceof Error ? z.message : String(z);
      h(
        
