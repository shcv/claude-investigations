---
id: msg-warning-401082
name: Warning Message
category: message
subcategory: warning
source_line: 401082
---

);
        });
      (await Promise.all(q), this.emit("deregister", A));
    }
  }
  s8K.Analytics = a8K;
});
var e8K = v((GQA) => {
  Object.defineProperty(GQA, "__esModule", { value: !0 });
  GQA.FetchHTTPClient = GQA.Context = GQA.Analytics = void 0;
  var nW2 = vy6();
  Object.defineProperty(GQA, "Analytics", {
    enumerable: !0,
    get: function () {
      return nW2.Analytics;
    },
  });
  var rW2 = tM1();
  Object.defineProperty(GQA, "Context", {
    enumerable: !0,
    get: function () {
      return rW2.Context;
    },
  });
  var oW2 = Ty6();
  Object.defineProperty(GQA, "FetchHTTPClient", {
    enumerable: !0,
    get: function () {
      return oW2.FetchHTTPClient;
    },
  });
  var aW2 = vy6();
  GQA.default = aW2.Analytics;
});
function AD2() {
  return eW2.production;
}
async function KD2() {
  if (K$()) return !1;
  return !0;
}
async function Ey6(A, K) {
  let q = await K4K();
  if (!q) return;
  try {
    let Y = Cy6(),
      z = $5(),
      w = await yr({ model: K.model }),
      H = Cy4(w, K),
      J = { anonymousId: Y, event: A, properties: H };
    if (z) {
      let O = rs(!0);
      ((J.userId = O.userID),
        (J.properties.accountUuid = z.accountUuid),
        (J.properties.organizationUuid = z.organizationUuid));
    }
    q.track(J);
  } catch (Y) {
    KA(Y instanceof Error ? Y : Error(String(Y)));
  }
}
async function q4K(A) {
  let K = await K4K();
  if (!K) return;
  try {
    let q = Cy6(),
      Y = $5(),
      z = { anonymousId: q, traits: A };
    if (Y) {
      let w = rs(!0);
      z.userId = w.userID;
    }
    K.identify(z);
  } catch (q) {
    KA(q instanceof Error ? q : Error(String(q)));
  }
}
var A4K,
  eW2,
  eM1 = null,
  K4K;
var ky6 = k(() => {
  p7();
  kx();
  i6();
  C1();
  x4();
  sO();
  BQ();
  ((A4K = o(e8K(), 1)),
    (eW2 = {
      production: "LKJN8LsLERHEOXkw487o7qCTFOrGPimI",
      development: "b64sf1kxwDGe1PiSAlv5ixuH0f509RKK",
    }));
  K4K = z6(async () => {
    if (!(await KD2())) return null;
    try {
      return (
        (eM1 = new A4K.Analytics({ writeKey: AD2() })),
        process.on("beforeExit", async () => {
          await eM1?.closeAndFlush();
        }),
        process.on("exit", () => {
          eM1?.closeAndFlush();
        }),
        eM1
      );
    } catch (K) {
      return (KA(K instanceof Error ? K : Error(String(K))), null);
    }
  });
});
function qD2() {
  let A = $5();
  if (!A) return {};
  return {
    email: A.emailAddress,
    account_uuid: A.accountUuid,
    organization_uuid: A.organizationUuid,
  };
}
function ZQA(A) {
  let K = s(21),
    q = Rt(),
    Y;
  if (K[0] !== q || K[1] !== A)
    ((Y = () => A.onDone(!1, q)), (K[0] = q), (K[1] = A), (K[2] = Y));
  else Y = K[2];
  let z = n8(Y),
    w;
  if (K[3] !== q || K[4] !== A)
    ((w = () => A.onDone(!1, q)), (K[3] = q), (K[4] = A), (K[5] = w));
  else w = K[5];
  let H;
  if (K[6] === Symbol.for("react.memo_cache_sentinel"))
    ((H = { context: "Confirmation" }), (K[6] = H));
  else H = K[6];
  J6("confirm:no", w, H);
  let J;
  if (K[7] !== q || K[8] !== A)
    ((J = () => A.onDone(!0, q)), (K[7] = q), (K[8] = A), (K[9] = J));
  else J = K[9];
  let O;
  if (K[10] !== A.startingMessage || K[11] !== J)
    ((O = Dj.createElement(Lt, {
      onDone: J,
      startingMessage: A.startingMessage,
    })),
      (K[10] = A.startingMessage),
      (K[11] = J),
      (K[12] = O));
  else O = K[12];
  let X;
  if (K[13] !== z.keyName || K[14] !== z.pending)
    ((X = z.pending
      ? Dj.createElement(
          Dj.Fragment,
          null,
          "Press ",
          z.keyName,
          " again to exit",
        )
      : ""),
      (K[13] = z.keyName),
      (K[14] = z.pending),
      (K[15] = X));
  else X = K[15];
  let $;
  if (K[16] !== X)
    (($ = Dj.createElement(
      S,
      { marginLeft: 1 },
      Dj.createElement(V, { dimColor: !0 }, X),
    )),
      (K[16] = X),
      (K[17] = $));
  else $ = K[17];
  let _;
  if (K[18] !== O || K[19] !== $)
    ((_ = Dj.createElement(S, { flexDirection: "column", marginTop: 1 }, O, $)),
      (K[18] = O),
      (K[19] = $),
      (K[20] = _));
  else _ = K[20];
  return _;
}
var Dj,
  Y4K = () => ({
    type: "local-jsx",
    name: "login",
    description: z4K()
      ? "Switch Anthropic accounts"
      : "Sign in with your Anthropic account",
    isEnabled: () => !process.env.DISABLE_LOGIN_COMMAND,
    isHidden: !1,
    async call(A, K) {
      return Dj.createElement(ZQA, {
        onDone: async (q) => {
          if ((K.onChangeAPIKey(), q))
            (yNA(),
              u5A(),
              q4K(qD2()),
              Gt7(),
              ft7(),
              K.setAppState((Y) => ({ ...Y, authVersion: Y.authVersion + 1 })));
          A(q ? "Login successful" : "Login interrupted");
        },
      });
    },
    userFacingName() {
      return "login";
    },
  });
var AP1 = k(() => {
  cA();
  XQA();
  Iq();
  mA();
  x4();
  C8();
  $QA();
  ns();
  q6();
  ky6();
  x4();
  ujA();
  CS();
  Dj = o($A(), 1);
});
async function yS() {
  let A = x1();
  if (WQA.has(A)) return WQA.get(A) ?? null;
  try {
    let K = await RrA();
    if ((h(
