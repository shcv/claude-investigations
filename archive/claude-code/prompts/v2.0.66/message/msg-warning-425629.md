---
id: msg-warning-425629
name: Warning Message
category: message
subcategory: warning
source_line: 425629
---

);
        });
      (await Promise.all(B), this.emit("deregister", A));
    }
  }
  Mz2.Analytics = Lz2;
});
var Rz2 = w((X_A) => {
  Object.defineProperty(X_A, "__esModule", { value: !0 });
  X_A.FetchHTTPClient = X_A.Context = X_A.Analytics = void 0;
  var K35 = h80();
  Object.defineProperty(X_A, "Analytics", {
    enumerable: !0,
    get: function () {
      return K35.Analytics;
    },
  });
  var V35 = Q61();
  Object.defineProperty(X_A, "Context", {
    enumerable: !0,
    get: function () {
      return V35.Context;
    },
  });
  var E35 = b80();
  Object.defineProperty(X_A, "FetchHTTPClient", {
    enumerable: !0,
    get: function () {
      return E35.FetchHTTPClient;
    },
  });
  var D35 = h80();
  X_A.default = D35.Analytics;
});
function z35() {
  let A = ["test", "dev"].includes("production") ? "development" : "production";
  return C35[A];
}
async function U35() {
  if (iX()) return !1;
  return !0;
}
async function g80(A, Q) {
  let B = await Tz2();
  if (!B) return;
  try {
    let G = m80(),
      Z = S8(),
      Y = await hd({ model: Q.model }),
      J = ffQ(Y, Q),
      I = { anonymousId: G, event: A, properties: J };
    if (Z) {
      let X = Fn(!0);
      ((I.userId = X.userID),
        (I.properties.accountUuid = Z.accountUuid),
        (I.properties.organizationUuid = Z.organizationUuid));
    }
    B.track(I);
  } catch (G) {
    r(G instanceof Error ? G : Error(String(G)));
  }
}
async function jz2(A) {
  let Q = await Tz2();
  if (!Q) return;
  try {
    let B = m80(),
      G = S8(),
      Z = { anonymousId: B, traits: A };
    if (G) {
      let Y = Fn(!0);
      Z.userId = Y.userID;
    }
    Q.identify(Z);
  } catch (B) {
    r(B instanceof Error ? B : Error(String(B)));
  }
}
var _z2,
  C35,
  B61 = null,
  Tz2;
var u80 = q(() => {
  p2();
  tk();
  vQ();
  g1();
  V2();
  D6A();
  br();
  ((_z2 = o(Rz2(), 1)),
    (C35 = {
      production: "LKJN8LsLERHEOXkw487o7qCTFOrGPimI",
      development: "b64sf1kxwDGe1PiSAlv5ixuH0f509RKK",
    }));
  Tz2 = Z0(async () => {
    if (!(await U35())) return null;
    try {
      return (
        (B61 = new _z2.Analytics({ writeKey: z35() })),
        process.on("beforeExit", async () => {
          await B61?.closeAndFlush();
        }),
        process.on("exit", () => {
          B61?.closeAndFlush();
        }),
        B61
      );
    } catch (Q) {
      return (r(Q instanceof Error ? Q : Error(String(Q))), null);
    }
  });
});
function $35() {
  let A = S8();
  if (!A) return {};
  return {
    email: A.emailAddress,
    account_uuid: A.accountUuid,
    organization_uuid: A.organizationUuid,
  };
}
function W_A(A) {
  let Q = En(),
    B = jQ(() => A.onDone(!1, Q));
  return (
    f1((G, Z) => {
      if (Z.escape) A.onDone(!1, Q);
    }),
    hH.createElement(
      j,
      { flexDirection: "column", marginTop: 1 },
      hH.createElement(Wi, {
        onDone: () => A.onDone(!0, Q),
        startingMessage: A.startingMessage,
      }),
      hH.createElement(
        j,
        { marginLeft: 1 },
        hH.createElement(
          z,
          { dimColor: !0 },
          B.pending
            ? hH.createElement(
                hH.Fragment,
                null,
                "Press ",
                B.keyName,
                " again to exit",
              )
            : "",
        ),
      ),
    )
  );
}
var hH,
  Pz2 = () => ({
    type: "local-jsx",
    name: "login",
    description: eFQ()
      ? "Switch Anthropic accounts"
      : "Sign in with your Anthropic account",
    isEnabled: () => !process.env.DISABLE_LOGIN_COMMAND,
    isHidden: !1,
    async call(A, Q) {
      return hH.createElement(W_A, {
        onDone: async (B) => {
          if ((Q.onChangeAPIKey(), B)) (wWA(), t1A(), jz2($35()), _iB());
          A(B ? "Login successful" : "Login interrupted");
        },
      });
    },
    userFacingName() {
      return "login";
    },
  });
var G61 = q(() => {
  JMA();
  a9();
  hA();
  V2();
  rRA();
  z4();
  u0();
  u80();
  V2();
  MYA();
  hH = o(KA(), 1);
});
async function Sz2(A) {
  let { accessToken: Q, orgUUID: B } = await Ex(),
    G = { ...oW(Q), "x-organization-uuid": B },
    Z = 
