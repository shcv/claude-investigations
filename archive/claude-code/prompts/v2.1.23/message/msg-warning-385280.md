---
id: msg-warning-385280
name: Warning Message
category: message
subcategory: warning
source_line: 385280
---

),
          A
        );
      if (typeof A === "string") return this._truncateToLimitUtil(A, K);
      if (Array.isArray(A))
        return A.map((q) =>
          typeof q === "string" ? this._truncateToLimitUtil(q, K) : q,
        );
      return A;
    }
  }
  do7.SpanImpl = po7;
});
var gFA = v((io7) => {
  Object.defineProperty(io7, "__esModule", { value: !0 });
  io7.SamplingDecision = void 0;
  var t02;
  (function (A) {
    ((A[(A.NOT_RECORD = 0)] = "NOT_RECORD"),
      (A[(A.RECORD = 1)] = "RECORD"),
      (A[(A.RECORD_AND_SAMPLED = 2)] = "RECORD_AND_SAMPLED"));
  })((t02 = io7.SamplingDecision || (io7.SamplingDecision = {})));
});
var aj1 = v((ro7) => {
  Object.defineProperty(ro7, "__esModule", { value: !0 });
  ro7.AlwaysOffSampler = void 0;
  var e02 = gFA();
  class no7 {
    shouldSample() {
      return { decision: e02.SamplingDecision.NOT_RECORD };
    }
    toString() {
      return "AlwaysOffSampler";
    }
  }
  ro7.AlwaysOffSampler = no7;
});
var sj1 = v((so7) => {
  Object.defineProperty(so7, "__esModule", { value: !0 });
  so7.AlwaysOnSampler = void 0;
  var AX2 = gFA();
  class ao7 {
    shouldSample() {
      return { decision: AX2.SamplingDecision.RECORD_AND_SAMPLED };
    }
    toString() {
      return "AlwaysOnSampler";
    }
  }
  so7.AlwaysOnSampler = ao7;
});
var TL6 = v((Ka7) => {
  Object.defineProperty(Ka7, "__esModule", { value: !0 });
  Ka7.ParentBasedSampler = void 0;
  var tj1 = RK(),
    KX2 = P9(),
    eo7 = aj1(),
    NL6 = sj1();
  class Aa7 {
    _root;
    _remoteParentSampled;
    _remoteParentNotSampled;
    _localParentSampled;
    _localParentNotSampled;
    constructor(A) {
      if (((this._root = A.root), !this._root))
        ((0, KX2.globalErrorHandler)(
          Error("ParentBasedSampler must have a root sampler configured"),
        ),
          (this._root = new NL6.AlwaysOnSampler()));
      ((this._remoteParentSampled =
        A.remoteParentSampled ?? new NL6.AlwaysOnSampler()),
        (this._remoteParentNotSampled =
          A.remoteParentNotSampled ?? new eo7.AlwaysOffSampler()),
        (this._localParentSampled =
          A.localParentSampled ?? new NL6.AlwaysOnSampler()),
        (this._localParentNotSampled =
          A.localParentNotSampled ?? new eo7.AlwaysOffSampler()));
    }
    shouldSample(A, K, q, Y, z, w) {
      let H = tj1.trace.getSpanContext(A);
      if (!H || !(0, tj1.isSpanContextValid)(H))
        return this._root.shouldSample(A, K, q, Y, z, w);
      if (H.isRemote) {
        if (H.traceFlags & tj1.TraceFlags.SAMPLED)
          return this._remoteParentSampled.shouldSample(A, K, q, Y, z, w);
        return this._remoteParentNotSampled.shouldSample(A, K, q, Y, z, w);
      }
      if (H.traceFlags & tj1.TraceFlags.SAMPLED)
        return this._localParentSampled.shouldSample(A, K, q, Y, z, w);
      return this._localParentNotSampled.shouldSample(A, K, q, Y, z, w);
    }
    toString() {
      return 
