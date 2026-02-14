---
id: msg-warning-412525
name: Warning Message
category: message
subcategory: warning
source_line: 412525
---

);
      return;
    }
  }
  function vW2() {
    let { request: A } = br8;
    if (cr8(A)) return A.__sentry_original__;
    return A;
  }
  function cr8(A) {
    return "__sentry_original__" in A;
  }
  kW2.Spotlight = ur8;
  kW2.getNativeHttpRequest = vW2;
  kW2.spotlightIntegration = yW2;
});
var E31 = w((fW2) => {
  var { _optionalChain: V31 } = XQ();
  Object.defineProperty(fW2, "__esModule", { value: !0 });
  var CW = l4(),
    z0A = XQ(),
    nr8 = D0A();
  fW2.ChannelName = void 0;
  (function (A) {
    A.RequestCreate = "undici:request:create";
    let B = "undici:request:headers";
    A.RequestEnd = B;
    let G = "undici:request:error";
    A.RequestError = G;
  })(fW2.ChannelName || (fW2.ChannelName = {}));
  var ar8 = (A) => {
      return new eU(A);
    },
    or8 = CW.defineIntegration(ar8);
  class eU {
    static __initStatic() {
      this.id = "Undici";
    }
    __init() {
      this.name = eU.id;
    }
    __init2() {
      this._createSpanUrlMap = new z0A.LRUMap(100);
    }
    __init3() {
      this._headersUrlMap = new z0A.LRUMap(100);
    }
    constructor(A = {}) {
      (eU.prototype.__init.call(this),
        eU.prototype.__init2.call(this),
        eU.prototype.__init3.call(this),
        eU.prototype.__init4.call(this),
        eU.prototype.__init5.call(this),
        eU.prototype.__init6.call(this),
        (this._options = {
          breadcrumbs: A.breadcrumbs === void 0 ? !0 : A.breadcrumbs,
          tracing: A.tracing,
          shouldCreateSpanForRequest: A.shouldCreateSpanForRequest,
        }));
    }
    setupOnce(A) {
      if (nr8.NODE_VERSION.major < 16) return;
      let Q;
      try {
        Q = qA("diagnostics_channel");
      } catch (B) {}
      if (!Q || !Q.subscribe) return;
      (Q.subscribe(fW2.ChannelName.RequestCreate, this._onRequestCreate),
        Q.subscribe(fW2.ChannelName.RequestEnd, this._onRequestEnd),
        Q.subscribe(fW2.ChannelName.RequestError, this._onRequestError));
    }
    _shouldCreateSpan(A) {
      if (
        this._options.tracing === !1 ||
        (this._options.tracing === void 0 && !CW.hasTracingEnabled())
      )
        return !1;
      if (this._options.shouldCreateSpanForRequest === void 0) return !0;
      let Q = this._createSpanUrlMap.get(A);
      if (Q !== void 0) return Q;
      let B = this._options.shouldCreateSpanForRequest(A);
      return (this._createSpanUrlMap.set(A, B), B);
    }
    __init4() {
      this._onRequestCreate = (A) => {
        if (
          !V31([
            CW.getClient,
            "call",
            (K) => K(),
            "optionalAccess",
            (K) => K.getIntegration,
            "call",
            (K) => K(eU),
          ])
        )
          return;
        let { request: Q } = A,
          B = Q.origin ? Q.origin.toString() + Q.path : Q.path,
          G = CW.getClient();
        if (!G) return;
        if (CW.isSentryRequestUrl(B, G) || Q.__sentry_span__ !== void 0) return;
        let Z = G.getOptions(),
          Y = CW.getCurrentScope(),
          J = CW.getIsolationScope(),
          I = CW.getActiveSpan(),
          X = this._shouldCreateSpan(B) ? sr8(I, Q, B) : void 0;
        if (X) Q.__sentry_span__ = X;
        if (
          ((K) => {
            if (Z.tracePropagationTargets === void 0) return !0;
            let V = this._headersUrlMap.get(K);
            if (V !== void 0) return V;
            let E = z0A.stringMatchesSomePattern(K, Z.tracePropagationTargets);
            return (this._headersUrlMap.set(K, E), E);
          })(B)
        ) {
          let {
              traceId: K,
              spanId: V,
              sampled: E,
              dsc: D,
            } = { ...J.getPropagationContext(), ...Y.getPropagationContext() },
            H = X
              ? CW.spanToTraceHeader(X)
              : z0A.generateSentryTraceHeader(K, V, E),
            F = z0A.dynamicSamplingContextToSentryBaggageHeader(
              D ||
                (X
                  ? CW.getDynamicSamplingContextFromSpan(X)
                  : CW.getDynamicSamplingContextFromClient(K, G, Y)),
            );
          rr8(Q, H, F);
        }
      };
    }
    __init5() {
      this._onRequestEnd = (A) => {
        if (
          !V31([
            CW.getClient,
            "call",
            (Y) => Y(),
            "optionalAccess",
            (Y) => Y.getIntegration,
            "call",
            (Y) => Y(eU),
          ])
        )
          return;
        let { request: Q, response: B } = A,
          G = Q.origin ? Q.origin.toString() + Q.path : Q.path;
        if (CW.isSentryRequestUrl(G, CW.getClient())) return;
        let Z = Q.__sentry_span__;
        if (Z) (CW.setHttpStatus(Z, B.statusCode), Z.end());
        if (this._options.breadcrumbs)
          CW.addBreadcrumb(
            {
              category: "http",
              data: { method: Q.method, status_code: B.statusCode, url: G },
              type: "http",
            },
            { event: "response", request: Q, response: B },
          );
      };
    }
    __init6() {
      this._onRequestError = (A) => {
        if (
          !V31([
            CW.getClient,
            "call",
            (Z) => Z(),
            "optionalAccess",
            (Z) => Z.getIntegration,
            "call",
            (Z) => Z(eU),
          ])
        )
          return;
        let { request: Q } = A,
          B = Q.origin ? Q.origin.toString() + Q.path : Q.path;
        if (CW.isSentryRequestUrl(B, CW.getClient())) return;
        let G = Q.__sentry_span__;
        if (G) (G.setStatus("internal_error"), G.end());
        if (this._options.breadcrumbs)
          CW.addBreadcrumb(
            {
              category: "http",
              data: { method: Q.method, url: B },
              level: "error",
              type: "http",
            },
            { event: "error", request: Q },
          );
      };
    }
  }
  eU.__initStatic();
  function rr8(A, Q, B) {
    let G;
    if (Array.isArray(A.headers))
      G = A.headers.some((Z) => Z === "sentry-trace");
    else
      G = A.headers
        .split(
          
