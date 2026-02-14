---
id: msg-warning-247335
name: Warning Message
category: message
subcategory: warning
source_line: 247335
---

);
  }
}
var V6Y = "tracingPolicy";
var CA7 = k(() => {
  A06();
  rO6();
  uw1();
  Po();
  dw1();
  Fw1();
});
function cw1(A) {
  if (A instanceof AbortSignal) return { abortSignal: A };
  if (A.aborted) return { abortSignal: AbortSignal.abort(A.reason) };
  let K = new AbortController(),
    q = !0;
  function Y() {
    if (q) (A.removeEventListener("abort", z), (q = !1));
  }
  function z() {
    (K.abort(A.reason), Y());
  }
  return (
    A.addEventListener("abort", z),
    { abortSignal: K.signal, cleanup: Y }
  );
}
function LA7() {
  return {
    name: E6Y,
    sendRequest: async (A, K) => {
      if (!A.abortSignal) return K(A);
      let { abortSignal: q, cleanup: Y } = cw1(A.abortSignal);
      A.abortSignal = q;
      try {
        return await K(A);
      } finally {
        Y === null || Y === void 0 || Y();
      }
    },
  };
}
var E6Y = "wrapAbortSignalLikePolicy";
var RA7 = () => {};
function K06(A) {
  var K;
  let q = xhA();
  if (uhA) {
    if (A.agent) q.addPolicy(ZA7(A.agent));
    if (A.tlsOptions) q.addPolicy(DA7(A.tlsOptions));
    (q.addPolicy($A7(A.proxyOptions)), q.addPolicy(zA7()));
  }
  if (
    (q.addPolicy(LA7()),
    q.addPolicy(OA7(), { beforePolicies: [tO6] }),
    q.addPolicy(le4(A.userAgentOptions)),
    q.addPolicy(
      GA7(
        (K = A.telemetryOptions) === null || K === void 0
          ? void 0
          : K.clientRequestIdHeaderName,
      ),
    ),
    q.addPolicy(qA7(), { afterPhase: "Deserialize" }),
    q.addPolicy(HA7(A.retryOptions), { phase: "Retry" }),
    q.addPolicy(
      kA7(
        Object.assign(Object.assign({}, A.userAgentOptions), A.loggingOptions),
      ),
      { afterPhase: "Retry" },
    ),
    uhA)
  )
    q.addPolicy(me4(A.redirectOptions), { afterPhase: "Retry" });
  return (q.addPolicy(ue4(A.loggingOptions), { afterPhase: "Sign" }), q);
}
var yA7 = k(() => {
  Be4();
  nO6();
  ge4();
  ie4();
  YA7();
  wA7();
  JA7();
  XA7();
  Po();
  _A7();
  WA7();
  jA7();
  CA7();
  RA7();
});
function q06() {
  let A = VO6();
  return {
    async sendRequest(K) {
      let { abortSignal: q, cleanup: Y } = K.abortSignal
        ? cw1(K.abortSignal)
        : {};
      try {
        return ((K.abortSignal = q), await A.sendRequest(K));
      } finally {
        Y === null || Y === void 0 || Y();
      }
    },
  };
}
var IA7 = k(() => {
  u_A();
});
function U7A(A) {
  return ju(A);
}
var SA7 = k(() => {
  u_A();
});
function wI(A) {
  return GO6(A);
}
var hA7 = k(() => {
  u_A();
});
function Y06(A, K = { maxRetries: pe4 }) {
  return bhA(A, Object.assign({ logger: k6Y }, K));
}
var k6Y;
var bA7 = k(() => {
  g7A();
  zI();
  k6Y = jo("core-rest-pipeline retryPolicy");
});
async function L6Y(A, K, q) {
  async function Y() {
    if (Date.now() < q)
      try {
        return await A();
      } catch (w) {
        return null;
      }
    else {
      let w = await A();
      if (w === null) throw Error("Failed to refresh access token.");
      return w;
    }
  }
  let z = await Y();
  while (z === null) (await aO6(K), (z = await Y()));
  return z;
}
function xA7(A, K) {
  let q = null,
    Y = null,
    z,
    w = Object.assign(Object.assign({}, C6Y), K),
    H = {
      get isRefreshing() {
        return q !== null;
      },
      get shouldRefresh() {
        var O;
        if (H.isRefreshing) return !1;
        if (
          (Y === null || Y === void 0 ? void 0 : Y.refreshAfterTimestamp) &&
          Y.refreshAfterTimestamp < Date.now()
        )
          return !0;
        return (
          ((O = Y === null || Y === void 0 ? void 0 : Y.expiresOnTimestamp) !==
            null && O !== void 0
            ? O
            : 0) -
            w.refreshWindowInMs <
          Date.now()
        );
      },
      get mustRefresh() {
        return (
          Y === null ||
          Y.expiresOnTimestamp - w.forcedRefreshWindowInMs < Date.now()
        );
      },
    };
  function J(O, X) {
    var $;
    if (!H.isRefreshing)
      q = L6Y(
        () => A.getToken(O, X),
        w.retryIntervalInMs,
        ($ = Y === null || Y === void 0 ? void 0 : Y.expiresOnTimestamp) !==
          null && $ !== void 0
          ? $
          : Date.now(),
      )
        .then((G) => {
          return ((q = null), (Y = G), (z = X.tenantId), Y);
        })
        .catch((G) => {
          throw ((q = null), (Y = null), (z = void 0), G);
        });
    return q;
  }
  return async (O, X) => {
    let $ = Boolean(X.claims),
      _ = z !== X.tenantId;
    if ($) Y = null;
    if (_ || $ || H.mustRefresh) return J(O, X);
    if (H.shouldRefresh) J(O, X);
    return Y;
  };
}
var C6Y;
var uA7 = k(() => {
  Po();
  C6Y = {
    forcedRefreshWindowInMs: 1000,
    retryIntervalInMs: 3000,
    refreshWindowInMs: 120000,
  };
});
async function lw1(A, K) {
  try {
    return [await K(A), void 0];
  } catch (q) {
    if (FhA(q) && q.response) return [q.response, q];
    else throw q;
  }
}
async function R6Y(A) {
  let { scopes: K, getAccessToken: q, request: Y } = A,
    z = {
      abortSignal: Y.abortSignal,
      tracingOptions: Y.tracingOptions,
      enableCae: !0,
    },
    w = await q(K, z);
  if (w) A.request.headers.set("Authorization", 
