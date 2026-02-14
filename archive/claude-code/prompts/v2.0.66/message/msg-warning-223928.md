---
id: msg-warning-223928
name: Warning Message
category: message
subcategory: warning
source_line: 223928
---

);
  }
}
var pV6 = "tracingPolicy";
var B5B = q(() => {
  nh1();
  mh1();
  HnA();
  sc();
  qnA();
  UnA();
});
function LnA(A) {
  if (A instanceof AbortSignal) return { abortSignal: A };
  if (A.aborted) return { abortSignal: AbortSignal.abort(A.reason) };
  let Q = new AbortController(),
    B = !0;
  function G() {
    if (B) (A.removeEventListener("abort", Z), (B = !1));
  }
  function Z() {
    (Q.abort(A.reason), G());
  }
  return (
    A.addEventListener("abort", Z),
    { abortSignal: Q.signal, cleanup: G }
  );
}
function G5B() {
  return {
    name: oV6,
    sendRequest: async (A, Q) => {
      if (!A.abortSignal) return Q(A);
      let { abortSignal: B, cleanup: G } = LnA(A.abortSignal);
      A.abortSignal = B;
      try {
        return await Q(A);
      } finally {
        G === null || G === void 0 || G();
      }
    },
  };
}
var oV6 = "wrapAbortSignalLikePolicy";
var Z5B = () => {};
function ah1(A) {
  var Q;
  let B = EUA();
  if (DUA) {
    if (A.agent) B.addPolicy(c8B(A.agent));
    if (A.tlsOptions) B.addPolicy(l8B(A.tlsOptions));
    (B.addPolicy(u8B(A.proxyOptions)), B.addPolicy(v8B()));
  }
  if (
    (B.addPolicy(G5B()),
    B.addPolicy(h8B(), { beforePolicies: [lh1] }),
    B.addPolicy(N8B(A.userAgentOptions)),
    B.addPolicy(
      d8B(
        (Q = A.telemetryOptions) === null || Q === void 0
          ? void 0
          : Q.clientRequestIdHeaderName,
      ),
    ),
    B.addPolicy(x8B(), { afterPhase: "Deserialize" }),
    B.addPolicy(f8B(A.retryOptions), { phase: "Retry" }),
    B.addPolicy(
      Q5B(
        Object.assign(Object.assign({}, A.userAgentOptions), A.loggingOptions),
      ),
      { afterPhase: "Retry" },
    ),
    DUA)
  )
    B.addPolicy(D8B(A.redirectOptions), { afterPhase: "Retry" });
  return (B.addPolicy(V8B(A.loggingOptions), { afterPhase: "Sign" }), B);
}
var Y5B = q(() => {
  E8B();
  uh1();
  H8B();
  q8B();
  y8B();
  k8B();
  b8B();
  g8B();
  sc();
  m8B();
  p8B();
  i8B();
  B5B();
  Z5B();
});
function oh1() {
  let A = Eh1();
  return {
    async sendRequest(Q) {
      let { abortSignal: B, cleanup: G } = Q.abortSignal
        ? LnA(Q.abortSignal)
        : {};
      try {
        return ((Q.abortSignal = B), await A.sendRequest(Q));
      } finally {
        G === null || G === void 0 || G();
      }
    },
  };
}
var J5B = q(() => {
  x5A();
});
function Lt(A) {
  return kS(A);
}
var I5B = q(() => {
  x5A();
});
function D_(A) {
  return Yh1(A);
}
var X5B = q(() => {
  x5A();
});
function rh1(A, Q = { maxRetries: U8B }) {
  return VUA(A, Object.assign({ logger: rV6 }, Q));
}
var rV6;
var W5B = q(() => {
  wt();
  E_();
  rV6 = oc("core-rest-pipeline retryPolicy");
});
async function tV6(A, Q, B) {
  async function G() {
    if (Date.now() < B)
      try {
        return await A();
      } catch (Y) {
        return null;
      }
    else {
      let Y = await A();
      if (Y === null) throw Error("Failed to refresh access token.");
      return Y;
    }
  }
  let Z = await G();
  while (Z === null) (await ch1(Q), (Z = await G()));
  return Z;
}
function K5B(A, Q) {
  let B = null,
    G = null,
    Z,
    Y = Object.assign(Object.assign({}, sV6), Q),
    J = {
      get isRefreshing() {
        return B !== null;
      },
      get shouldRefresh() {
        var X;
        if (J.isRefreshing) return !1;
        if (
          (G === null || G === void 0 ? void 0 : G.refreshAfterTimestamp) &&
          G.refreshAfterTimestamp < Date.now()
        )
          return !0;
        return (
          ((X = G === null || G === void 0 ? void 0 : G.expiresOnTimestamp) !==
            null && X !== void 0
            ? X
            : 0) -
            Y.refreshWindowInMs <
          Date.now()
        );
      },
      get mustRefresh() {
        return (
          G === null ||
          G.expiresOnTimestamp - Y.forcedRefreshWindowInMs < Date.now()
        );
      },
    };
  function I(X, W) {
    var K;
    if (!J.isRefreshing)
      B = tV6(
        () => A.getToken(X, W),
        Y.retryIntervalInMs,
        (K = G === null || G === void 0 ? void 0 : G.expiresOnTimestamp) !==
          null && K !== void 0
          ? K
          : Date.now(),
      )
        .then((E) => {
          return ((B = null), (G = E), (Z = W.tenantId), G);
        })
        .catch((E) => {
          throw ((B = null), (G = null), (Z = void 0), E);
        });
    return B;
  }
  return async (X, W) => {
    let K = Boolean(W.claims),
      V = Z !== W.tenantId;
    if (K) G = null;
    if (V || K || J.mustRefresh) return I(X, W);
    if (J.shouldRefresh) I(X, W);
    return G;
  };
}
var sV6;
var V5B = q(() => {
  sc();
  sV6 = {
    forcedRefreshWindowInMs: 1000,
    retryIntervalInMs: 3000,
    refreshWindowInMs: 120000,
  };
});
async function MnA(A, Q) {
  try {
    return [await Q(A), void 0];
  } catch (B) {
    if (zUA(B) && B.response) return [B.response, B];
    else throw B;
  }
}
async function eV6(A) {
  let { scopes: Q, getAccessToken: B, request: G } = A,
    Z = {
      abortSignal: G.abortSignal,
      tracingOptions: G.tracingOptions,
      enableCae: !0,
    },
    Y = await B(Q, Z);
  if (Y) A.request.headers.set("Authorization", 
