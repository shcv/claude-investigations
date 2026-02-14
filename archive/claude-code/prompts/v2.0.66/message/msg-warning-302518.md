---
id: msg-warning-302518
name: Warning Message
category: message
subcategory: warning
source_line: 302518
---

,
        { level: "warn" },
      );
    }
  for await (let Z of ra1(A, Q)) {
    if (Z.message) B.push(Z.message);
    if (Z.additionalContexts && Z.additionalContexts.length > 0)
      G.push(...Z.additionalContexts);
  }
  if (G.length > 0) {
    let Z = o9({
      type: "hook_additional_context",
      content: G,
      hookName: "SessionStart",
      toolUseID: "SessionStart",
      hookEvent: "SessionStart",
    });
    B.push(Z);
  }
  return B;
}
var uAA = q(() => {
  aw();
  $qA();
  g1();
  Q0();
  OM();
  CZA();
});
import { randomUUID as X_B } from "crypto";
function vi6(A) {
  if (A.type !== "attachment") return A;
  let Q = A.attachment;
  if (Q.type === "new_file")
    return { ...A, attachment: { ...Q, type: "file" } };
  if (Q.type === "new_directory")
    return { ...A, attachment: { ...Q, type: "directory" } };
  return A;
}
function wqA(A) {
  try {
    let Q = A.map(vi6),
      B = K_B(Q);
    if (B[B.length - 1]?.type === "user") B.push(aE({ content: jAA }));
    return B;
  } catch (Q) {
    throw (r(Q), Q);
  }
}
async function W_B(A, Q) {
  try {
    let B = await FQ.get(A, { headers: Q, timeout: 30000 });
    if (!B.data || !Array.isArray(B.data.log))
      throw Error("Invalid response format: missing or invalid log array");
    return B.data;
  } catch (B) {
    if (FQ.isAxiosError(B)) {
      let G = B.response
        ? 
