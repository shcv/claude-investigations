---
id: msg-warning-342216
name: Warning Message
category: message
subcategory: warning
source_line: 342216
---

),
          A
        );
      if (typeof A === "string") return this._truncateToLimitUtil(A, Q);
      if (Array.isArray(A))
        return A.map((B) =>
          typeof B === "string" ? this._truncateToLimitUtil(B, Q) : B,
        );
      return A;
    }
  }
  fcB.SpanImpl = kcB;
});
var fLA = w((gcB) => {
  Object.defineProperty(gcB, "__esModule", { value: !0 });
  gcB.SamplingDecision = void 0;
  var _78;
  (function (A) {
    ((A[(A.NOT_RECORD = 0)] = "NOT_RECORD"),
      (A[(A.RECORD = 1)] = "RECORD"),
      (A[(A.RECORD_AND_SAMPLED = 2)] = "RECORD_AND_SAMPLED"));
  })((_78 = gcB.SamplingDecision || (gcB.SamplingDecision = {})));
});
var V01 = w((mcB) => {
  Object.defineProperty(mcB, "__esModule", { value: !0 });
  mcB.AlwaysOffSampler = void 0;
  var T78 = fLA();
  class ucB {
    shouldSample() {
      return { decision: T78.SamplingDecision.NOT_RECORD };
    }
    toString() {
      return "AlwaysOffSampler";
    }
  }
  mcB.AlwaysOffSampler = ucB;
});
var E01 = w((pcB) => {
  Object.defineProperty(pcB, "__esModule", { value: !0 });
  pcB.AlwaysOnSampler = void 0;
  var j78 = fLA();
  class ccB {
    shouldSample() {
      return { decision: j78.SamplingDecision.RECORD_AND_SAMPLED };
    }
    toString() {
      return "AlwaysOnSampler";
    }
  }
  pcB.AlwaysOnSampler = ccB;
});
var He1 = w((acB) => {
  Object.defineProperty(acB, "__esModule", { value: !0 });
  acB.ParentBasedSampler = void 0;
  var D01 = N9(),
    P78 = X8(),
    icB = V01(),
    De1 = E01();
  class ncB {
    _root;
    _remoteParentSampled;
    _remoteParentNotSampled;
    _localParentSampled;
    _localParentNotSampled;
    constructor(A) {
      if (((this._root = A.root), !this._root))
        ((0, P78.globalErrorHandler)(
          Error("ParentBasedSampler must have a root sampler configured"),
        ),
          (this._root = new De1.AlwaysOnSampler()));
      ((this._remoteParentSampled =
        A.remoteParentSampled ?? new De1.AlwaysOnSampler()),
        (this._remoteParentNotSampled =
          A.remoteParentNotSampled ?? new icB.AlwaysOffSampler()),
        (this._localParentSampled =
          A.localParentSampled ?? new De1.AlwaysOnSampler()),
        (this._localParentNotSampled =
          A.localParentNotSampled ?? new icB.AlwaysOffSampler()));
    }
    shouldSample(A, Q, B, G, Z, Y) {
      let J = D01.trace.getSpanContext(A);
      if (!J || !(0, D01.isSpanContextValid)(J))
        return this._root.shouldSample(A, Q, B, G, Z, Y);
      if (J.isRemote) {
        if (J.traceFlags & D01.TraceFlags.SAMPLED)
          return this._remoteParentSampled.shouldSample(A, Q, B, G, Z, Y);
        return this._remoteParentNotSampled.shouldSample(A, Q, B, G, Z, Y);
      }
      if (J.traceFlags & D01.TraceFlags.SAMPLED)
        return this._localParentSampled.shouldSample(A, Q, B, G, Z, Y);
      return this._localParentNotSampled.shouldSample(A, Q, B, G, Z, Y);
    }
    toString() {
      return 
