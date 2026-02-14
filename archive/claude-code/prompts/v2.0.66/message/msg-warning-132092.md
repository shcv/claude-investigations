---
id: msg-warning-132092
name: Warning Message
category: message
subcategory: warning
source_line: 132092
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
    _truncateToLimitUtil(A, Q) {
      if (A.length <= Q) return A;
      return A.substring(0, Q);
    }
    _isLogRecordReadonly() {
      if (this._isReadonly)
        sr.diag.warn("Can not execute the operation on emitted log record");
      return this._isReadonly;
    }
  }
  nxQ.LogRecordImpl = ixQ;
});
var exQ = w((sxQ) => {
  Object.defineProperty(sxQ, "__esModule", { value: !0 });
  sxQ.Logger = void 0;
  var vh3 = N9(),
    kh3 = oxQ();
  class rxQ {
    instrumentationScope;
    _sharedState;
    constructor(A, Q) {
      ((this.instrumentationScope = A), (this._sharedState = Q));
    }
    emit(A) {
      let Q = A.context || vh3.context.active(),
        B = new kh3.LogRecordImpl(
          this._sharedState,
          this.instrumentationScope,
          { context: Q, ...A },
        );
      (this._sharedState.activeProcessor.onEmit(B, Q), B._makeReadonly());
    }
  }
  sxQ.Logger = rxQ;
});
var ByQ = w((AyQ) => {
  Object.defineProperty(AyQ, "__esModule", { value: !0 });
  AyQ.reconfigureLimits = AyQ.loadDefaultConfig = void 0;
  var a3A = X8();
  function fh3() {
    return {
      forceFlushTimeoutMillis: 30000,
      logRecordLimits: {
        attributeValueLengthLimit:
          (0, a3A.getNumberFromEnv)(
            "OTEL_LOGRECORD_ATTRIBUTE_VALUE_LENGTH_LIMIT",
          ) ?? 1 / 0,
        attributeCountLimit:
          (0, a3A.getNumberFromEnv)("OTEL_LOGRECORD_ATTRIBUTE_COUNT_LIMIT") ??
          128,
      },
      includeTraceContext: !0,
    };
  }
  AyQ.loadDefaultConfig = fh3;
  function bh3(A) {
    return {
      attributeCountLimit:
        A.attributeCountLimit ??
        (0, a3A.getNumberFromEnv)("OTEL_LOGRECORD_ATTRIBUTE_COUNT_LIMIT") ??
        (0, a3A.getNumberFromEnv)("OTEL_ATTRIBUTE_COUNT_LIMIT") ??
        128,
      attributeValueLengthLimit:
        A.attributeValueLengthLimit ??
        (0, a3A.getNumberFromEnv)(
          "OTEL_LOGRECORD_ATTRIBUTE_VALUE_LENGTH_LIMIT",
        ) ??
        (0, a3A.getNumberFromEnv)("OTEL_ATTRIBUTE_VALUE_LENGTH_LIMIT") ??
        1 / 0,
    };
  }
  AyQ.reconfigureLimits = bh3;
});
var zT1 = w((ZyQ) => {
  Object.defineProperty(ZyQ, "__esModule", { value: !0 });
  ZyQ.NoopLogRecordProcessor = void 0;
  class GyQ {
    forceFlush() {
      return Promise.resolve();
    }
    onEmit(A, Q) {}
    shutdown() {
      return Promise.resolve();
    }
  }
  ZyQ.NoopLogRecordProcessor = GyQ;
});
var WyQ = w((IyQ) => {
  Object.defineProperty(IyQ, "__esModule", { value: !0 });
  IyQ.MultiLogRecordProcessor = void 0;
  var gh3 = X8();
  class JyQ {
    processors;
    forceFlushTimeoutMillis;
    constructor(A, Q) {
      ((this.processors = A), (this.forceFlushTimeoutMillis = Q));
    }
    async forceFlush() {
      let A = this.forceFlushTimeoutMillis;
      await Promise.all(
        this.processors.map((Q) => (0, gh3.callWithTimeout)(Q.forceFlush(), A)),
      );
    }
    onEmit(A, Q) {
      this.processors.forEach((B) => B.onEmit(A, Q));
    }
    async shutdown() {
      await Promise.all(this.processors.map((A) => A.shutdown()));
    }
  }
  IyQ.MultiLogRecordProcessor = JyQ;
});
var DyQ = w((VyQ) => {
  Object.defineProperty(VyQ, "__esModule", { value: !0 });
  VyQ.LoggerProviderSharedState = void 0;
  var uh3 = zT1(),
    mh3 = WyQ();
  class KyQ {
    resource;
    forceFlushTimeoutMillis;
    logRecordLimits;
    processors;
    loggers = new Map();
    activeProcessor;
    registeredLogRecordProcessors = [];
    constructor(A, Q, B, G) {
      if (
        ((this.resource = A),
        (this.forceFlushTimeoutMillis = Q),
        (this.logRecordLimits = B),
        (this.processors = G),
        G.length > 0)
      )
        ((this.registeredLogRecordProcessors = G),
          (this.activeProcessor = new mh3.MultiLogRecordProcessor(
            this.registeredLogRecordProcessors,
            this.forceFlushTimeoutMillis,
          )));
      else this.activeProcessor = new uh3.NoopLogRecordProcessor();
    }
  }
  VyQ.LoggerProviderSharedState = KyQ;
});
var wyQ = w((zyQ) => {
  Object.defineProperty(zyQ, "__esModule", { value: !0 });
  zyQ.LoggerProvider = zyQ.DEFAULT_LOGGER_NAME = void 0;
  var _uA = N9(),
    dh3 = m_1(),
    ch3 = n3A(),
    HyQ = X8(),
    ph3 = exQ(),
    FyQ = ByQ(),
    lh3 = DyQ();
  zyQ.DEFAULT_LOGGER_NAME = "unknown";
  class CyQ {
    _shutdownOnce;
    _sharedState;
    constructor(A = {}) {
      let Q = (0, HyQ.merge)({}, (0, FyQ.loadDefaultConfig)(), A),
        B = A.resource ?? (0, ch3.defaultResource)();
      ((this._sharedState = new lh3.LoggerProviderSharedState(
        B,
        Q.forceFlushTimeoutMillis,
        (0, FyQ.reconfigureLimits)(Q.logRecordLimits),
        A?.processors ?? [],
      )),
        (this._shutdownOnce = new HyQ.BindOnceFuture(this._shutdown, this)));
    }
    getLogger(A, Q, B) {
      if (this._shutdownOnce.isCalled)
        return (
          _uA.diag.warn("A shutdown LoggerProvider cannot provide a Logger"),
          dh3.NOOP_LOGGER
        );
      if (!A)
        _uA.diag.warn("Logger requested without instrumentation scope name.");
      let G = A || zyQ.DEFAULT_LOGGER_NAME,
        Z = 
