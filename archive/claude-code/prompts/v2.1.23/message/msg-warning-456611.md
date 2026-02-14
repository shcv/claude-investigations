---
id: msg-warning-456611
name: Warning Message
category: message
subcategory: warning
source_line: 456611
---

,
        { level: "warn" },
      );
    }
  for await (let z of cx6(A, void 0, void 0, K)) {
    if (z.message) q.push(z.message);
    if (z.additionalContexts && z.additionalContexts.length > 0)
      Y.push(...z.additionalContexts);
  }
  if (Y.length > 0) {
    let z = PK({
      type: "hook_additional_context",
      content: Y,
      hookName: "Setup",
      toolUseID: "Setup",
      hookEvent: "Setup",
    });
    q.push(z);
  }
  return q;
}
var Ye = k(() => {
  JP();
  wpA();
  C1();
  Z1();
  sD();
  aqA();
  q6();
});
import { randomUUID as sHK } from "crypto";
function mC2(A) {
  if (A.type !== "attachment") return A;
  let K = A.attachment;
  if (K.type === "new_file")
    return { ...A, attachment: { ...K, type: "file" } };
  if (K.type === "new_directory")
    return { ...A, attachment: { ...K, type: "directory" } };
  return A;
}
function HpA(A) {
  try {
    let K = A.map(mC2),
      q = LV1(K),
      Y = RV1(q);
    if (Y[Y.length - 1]?.type === "user") Y.push(WL({ content: aKA }));
    return Y;
  } catch (K) {
    throw (KA(K), K);
  }
}
function gC2(A) {
  for (let K of A) {
    if (K.type !== "attachment") continue;
    if (K.attachment.type !== "invoked_skills") continue;
    for (let q of K.attachment.skills)
      if (q.name && q.path && q.content) UnA(q.name, q.path, q.content);
  }
}
async function ze(A, K) {
  try {
    let q = null,
      Y = null,
      z;
    if (A === void 0) q = await tHK(0);
    else if (K) {
      Y = [];
      for (let H of await S1A(K)) {
        if (H.type === "assistant" || H.type === "user") {
          let J = FC2(H);
          if (J) Y.push(J);
        }
        z = H.session_id;
      }
    } else if (typeof A === "string") ((q = await ax6(A)), (z = A));
    else q = A;
    if (!q && !Y) return null;
    if (q) {
      if (NL(q)) q = await sS(q);
      if (!z) z = ZH(q);
      if ((jO1(q), z)) MO1(q, rD(z));
      (rG1(q), (Y = q.messages));
    }
    (gC2(Y), (Y = HpA(Y)));
    let w = await fj("resume", z);
    return (
      Y.push(...w),
      {
        messages: Y,
        fileHistorySnapshots: q?.fileHistorySnapshots,
        attributionSnapshots: q?.attributionSnapshots,
        sessionId: z,
        agentName: q?.agentName,
        agentColor: q?.agentColor,
        customTitle: q?.customTitle,
        tag: q?.tag,
        fullPath: q?.fullPath,
      }
    );
  } catch (q) {
    throw (KA(q), q);
  }
}
function FC2(A) {
  if (A.type === "assistant")
    return {
      type: A.type,
      message: A.message,
      uuid: sHK(),
      timestamp: new Date().toISOString(),
      requestId: void 0,
    };
  else if (A.type === "user")
    return {
      type: A.type,
      message: A.message,
      uuid: sHK(),
      timestamp: new Date().toISOString(),
    };
  return;
}
var JPA = k(() => {
  C1();
  UK();
  $8();
  xu();
  NG();
  Xw();
  Ye();
  AP();
  q6();
});
function eHK({ onStashAndContinue: A, onCancel: K }) {
  let [q, Y] = Z9A.useState(null),
    z = q !== null ? [...q.tracked, ...q.untracked] : [],
    [w, H] = Z9A.useState(!0),
    [J, O] = Z9A.useState(!1),
    [X, $] = Z9A.useState(null);
  Z9A.useEffect(() => {
    (async () => {
      try {
        let D = await hy1();
        Y(D);
      } catch (D) {
        let j = D instanceof Error ? D.message : String(D);
        (h(
