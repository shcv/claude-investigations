---
id: msg-warning-74954
name: Warning Message
category: message
subcategory: warning
source_line: 74954
---

);
      return;
    }
  }
  function DE8() {
    let { request: A } = feq;
    if (Ceq(A)) return A.__sentry_original__;
    return A;
  }
  function Ceq(A) {
    return "__sentry_original__" in A;
  }
  jE8.Spotlight = veq;
  jE8.getNativeHttpRequest = DE8;
  jE8.spotlightIntegration = WE8;
});
var otA = v((ME8) => {
  var { _optionalChain: rtA } = H8();
  Object.defineProperty(ME8, "__esModule", { value: !0 });
  var QX = sq(),
    O6A = H8(),
    Ieq = z6A();
  ME8.ChannelName = void 0;
  (function (A) {
    A.RequestCreate = "undici:request:create";
    let q = "undici:request:headers";
    A.RequestEnd = q;
    let Y = "undici:request:error";
    A.RequestError = Y;
  })(ME8.ChannelName || (ME8.ChannelName = {}));
  var Seq = (A) => {
      return new JV(A);
    },
    heq = QX.defineIntegration(Seq);
  class JV {
    static __initStatic() {
      this.id = "Undici";
    }
    __init() {
      this.name = JV.id;
    }
    __init2() {
      this._createSpanUrlMap = new O6A.LRUMap(100);
    }
    __init3() {
      this._headersUrlMap = new O6A.LRUMap(100);
    }
    constructor(A = {}) {
      (JV.prototype.__init.call(this),
        JV.prototype.__init2.call(this),
        JV.prototype.__init3.call(this),
        JV.prototype.__init4.call(this),
        JV.prototype.__init5.call(this),
        JV.prototype.__init6.call(this),
        (this._options = {
          breadcrumbs: A.breadcrumbs === void 0 ? !0 : A.breadcrumbs,
          tracing: A.tracing,
          shouldCreateSpanForRequest: A.shouldCreateSpanForRequest,
        }));
    }
    setupOnce(A) {
      if (Ieq.NODE_VERSION.major < 16) return;
      let K;
      try {
        K = CA("diagnostics_channel");
      } catch (q) {}
      if (!K || !K.subscribe) return;
      (K.subscribe(ME8.ChannelName.RequestCreate, this._onRequestCreate),
        K.subscribe(ME8.ChannelName.RequestEnd, this._onRequestEnd),
        K.subscribe(ME8.ChannelName.RequestError, this._onRequestError));
    }
    _shouldCreateSpan(A) {
      if (
        this._options.tracing === !1 ||
        (this._options.tracing === void 0 && !QX.hasTracingEnabled())
      )
        return !1;
      if (this._options.shouldCreateSpanForRequest === void 0) return !0;
      let K = this._createSpanUrlMap.get(A);
      if (K !== void 0) return K;
      let q = this._options.shouldCreateSpanForRequest(A);
      return (this._createSpanUrlMap.set(A, q), q);
    }
    __init4() {
      this._onRequestCreate = (A) => {
        if (
          !rtA([
            QX.getClient,
            "call",
            ($) => $(),
            "optionalAccess",
            ($) => $.getIntegration,
            "call",
            ($) => $(JV),
          ])
        )
          return;
        let { request: K } = A,
          q = K.origin ? K.origin.toString() + K.path : K.path,
          Y = QX.getClient();
        if (!Y) return;
        if (QX.isSentryRequestUrl(q, Y) || K.__sentry_span__ !== void 0) return;
        let z = Y.getOptions(),
          w = QX.getCurrentScope(),
          H = QX.getIsolationScope(),
          J = QX.getActiveSpan(),
          O = this._shouldCreateSpan(q) ? xeq(J, K, q) : void 0;
        if (O) K.__sentry_span__ = O;
        if (
          (($) => {
            if (z.tracePropagationTargets === void 0) return !0;
            let _ = this._headersUrlMap.get($);
            if (_ !== void 0) return _;
            let G = O6A.stringMatchesSomePattern($, z.tracePropagationTargets);
            return (this._headersUrlMap.set($, G), G);
          })(q)
        ) {
          let {
              traceId: $,
              spanId: _,
              sampled: G,
              dsc: Z,
            } = { ...H.getPropagationContext(), ...w.getPropagationContext() },
            W = O
              ? QX.spanToTraceHeader(O)
              : O6A.generateSentryTraceHeader($, _, G),
            D = O6A.dynamicSamplingContextToSentryBaggageHeader(
              Z ||
                (O
                  ? QX.getDynamicSamplingContextFromSpan(O)
                  : QX.getDynamicSamplingContextFromClient($, Y, w)),
            );
          beq(K, W, D);
        }
      };
    }
    __init5() {
      this._onRequestEnd = (A) => {
        if (
          !rtA([
            QX.getClient,
            "call",
            (w) => w(),
            "optionalAccess",
            (w) => w.getIntegration,
            "call",
            (w) => w(JV),
          ])
        )
          return;
        let { request: K, response: q } = A,
          Y = K.origin ? K.origin.toString() + K.path : K.path;
        if (QX.isSentryRequestUrl(Y, QX.getClient())) return;
        let z = K.__sentry_span__;
        if (z) (QX.setHttpStatus(z, q.statusCode), z.end());
        if (this._options.breadcrumbs)
          QX.addBreadcrumb(
            {
              category: "http",
              data: { method: K.method, status_code: q.statusCode, url: Y },
              type: "http",
            },
            { event: "response", request: K, response: q },
          );
      };
    }
    __init6() {
      this._onRequestError = (A) => {
        if (
          !rtA([
            QX.getClient,
            "call",
            (z) => z(),
            "optionalAccess",
            (z) => z.getIntegration,
            "call",
            (z) => z(JV),
          ])
        )
          return;
        let { request: K } = A,
          q = K.origin ? K.origin.toString() + K.path : K.path;
        if (QX.isSentryRequestUrl(q, QX.getClient())) return;
        let Y = K.__sentry_span__;
        if (Y) (Y.setStatus("internal_error"), Y.end());
        if (this._options.breadcrumbs)
          QX.addBreadcrumb(
            {
              category: "http",
              data: { method: K.method, url: q },
              level: "error",
              type: "http",
            },
            { event: "error", request: K },
          );
      };
    }
  }
  JV.__initStatic();
  function beq(A, K, q) {
    let Y;
    if (Array.isArray(A.headers))
      Y = A.headers.some((z) => z === "sentry-trace");
    else
      Y = A.headers
        .split(
          
