---
id: msg-warning-537276
name: Warning Message
category: message
subcategory: warning
source_line: 537276
---

, {
          level: "warn",
        });
    } catch {}
  }),
    process.on("warning", tE1));
}
var gkK,
  De2,
  tE1 = null;
var QkK = k(() => {
  l1();
  Z1();
  B5();
  gkK = new Map();
  De2 = [
    /MaxListenersExceededWarning.*AbortSignal/,
    /MaxListenersExceededWarning.*EventTarget/,
  ];
});
function UkK() {}
function pkK() {
  let A = J8() || {},
    K = M1().env || {},
    q = A.env || {};
  for (let [Y, z] of Object.entries(K))
    if (_3A.has(Y.toUpperCase())) process.env[Y] = z;
  for (let [Y, z] of Object.entries(q))
    if (_3A.has(Y.toUpperCase())) process.env[Y] = z;
  UkK();
}
function qAA() {
  let A = J8() || {};
  (Object.assign(process.env, M1().env),
    Object.assign(process.env, A.env),
    UkK());
}
var xcA = k(() => {
  i6();
  I8();
  $M1();
});
function Me2(A) {
  let K = s(19),
    { filePath: q, errorDescription: Y, onExit: z, onReset: w } = A,
    H;
  if (K[0] !== z || K[1] !== w)
    ((H = (D) => {
      if (D === "exit") z();
      else w();
    }),
      (K[0] = z),
      (K[1] = w),
      (K[2] = H));
  else H = K[2];
  let J = H,
    O;
  if (K[3] !== q)
    ((O = QL.default.createElement(
      V,
      null,
      "The configuration file at ",
      QL.default.createElement(V, { bold: !0 }, q),
      " contains invalid JSON.",
    )),
      (K[3] = q),
      (K[4] = O));
  else O = K[4];
  let X;
  if (K[5] !== Y)
    ((X = QL.default.createElement(V, null, Y)), (K[5] = Y), (K[6] = X));
  else X = K[6];
  let $;
  if (K[7] !== O || K[8] !== X)
    (($ = QL.default.createElement(
      S,
      { flexDirection: "column", gap: 1 },
      O,
      X,
    )),
      (K[7] = O),
      (K[8] = X),
      (K[9] = $));
  else $ = K[9];
  let _;
  if (K[10] === Symbol.for("react.memo_cache_sentinel"))
    ((_ = QL.default.createElement(V, { bold: !0 }, "Choose an option:")),
      (K[10] = _));
  else _ = K[10];
  let G;
  if (K[11] === Symbol.for("react.memo_cache_sentinel"))
    ((G = [
      { label: "Exit and fix manually", value: "exit" },
      { label: "Reset with default configuration", value: "reset" },
    ]),
      (K[11] = G));
  else G = K[11];
  let Z;
  if (K[12] !== J || K[13] !== z)
    ((Z = QL.default.createElement(
      S,
      { flexDirection: "column" },
      _,
      QL.default.createElement(E6, { options: G, onChange: J, onCancel: z }),
    )),
      (K[12] = J),
      (K[13] = z),
      (K[14] = Z));
  else Z = K[14];
  let W;
  if (K[15] !== z || K[16] !== $ || K[17] !== Z)
    ((W = QL.default.createElement(
      L4,
      { title: "Configuration Error", color: "error", onCancel: z },
      $,
      Z,
    )),
      (K[15] = z),
      (K[16] = $),
      (K[17] = Z),
      (K[18] = W));
  else W = K[18];
  return W;
}
async function dkK({ error: A }) {
  let K = { ...Iw(!1), theme: Pe2 };
  await new Promise(async (q) => {
    let { unmount: Y } = await M9(
      QL.default.createElement(
        $Y,
        null,
        QL.default.createElement(
          Ez,
          null,
          QL.default.createElement(Me2, {
            filePath: A.filePath,
            errorDescription: A.message,
            onExit: () => {
              (Y(), q(), process.exit(1));
            },
            onReset: () => {
              (x8(A.filePath, UA(A.defaultConfig, null, 2), {
                flush: !1,
                encoding: "utf8",
              }),
                Y(),
                q(),
                process.exit(0));
            },
          }),
        ),
      ),
      K,
    );
  });
}
var QL,
  Pe2 = "dark";
var ckK = k(() => {
  cA();
  mA();
  q9();
  mA();
  b1();
  A4();
  cB();
  b1();
  dB();
  t3();
  QL = o($A(), 1);
});
import * as ucA from "path";
async function Ne2() {
  if (oU6 || sU6) return;
  if (((oU6 = !0), !lkK))
    ((lkK = !0),
      EC7(() => {
        (rQ6(), gVA.forEach((K) => K()));
      }));
  let A = await ve2();
  if (A.length === 0) return;
  (h(
