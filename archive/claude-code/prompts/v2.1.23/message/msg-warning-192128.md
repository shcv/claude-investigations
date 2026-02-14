---
id: msg-warning-192128
name: Warning Message
category: message
subcategory: warning
source_line: 192128
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
    _truncateToLimitUtil(A, K) {
      if (A.length <= K) return A;
      return A.substring(0, K);
    }
    _isLogRecordReadonly() {
      if (this._isReadonly)
        i4A.diag.warn("Can not execute the operation on emitted log record");
      return this._isReadonly;
    }
  }
  _R4.LogRecordImpl = $R4;
});
var MR4 = v((DR4) => {
  Object.defineProperty(DR4, "__esModule", { value: !0 });
  DR4.Logger = void 0;
  var c_9 = RK(),
    l_9 = ZR4();
  class WR4 {
    instrumentationScope;
    _sharedState;
    constructor(A, K) {
      ((this.instrumentationScope = A), (this._sharedState = K));
    }
    emit(A) {
      let K = A.context || c_9.context.active(),
        q = new l_9.LogRecordImpl(
          this._sharedState,
          this.instrumentationScope,
          { context: K, ...A },
        );
      (this._sharedState.activeProcessor.onEmit(q, K), q._makeReadonly());
    }
  }
  DR4.Logger = WR4;
});
var fR4 = v((PR4) => {
  Object.defineProperty(PR4, "__esModule", { value: !0 });
  PR4.reconfigureLimits = PR4.loadDefaultConfig = void 0;
  var A$A = P9();
  function i_9() {
    return {
      forceFlushTimeoutMillis: 30000,
      logRecordLimits: {
        attributeValueLengthLimit:
          (0, A$A.getNumberFromEnv)(
            "OTEL_LOGRECORD_ATTRIBUTE_VALUE_LENGTH_LIMIT",
          ) ?? 1 / 0,
        attributeCountLimit:
          (0, A$A.getNumberFromEnv)("OTEL_LOGRECORD_ATTRIBUTE_COUNT_LIMIT") ??
          128,
      },
      includeTraceContext: !0,
    };
  }
  PR4.loadDefaultConfig = i_9;
  function n_9(A) {
    return {
      attributeCountLimit:
        A.attributeCountLimit ??
        (0, A$A.getNumberFromEnv)("OTEL_LOGRECORD_ATTRIBUTE_COUNT_LIMIT") ??
        (0, A$A.getNumberFromEnv)("OTEL_ATTRIBUTE_COUNT_LIMIT") ??
        128,
      attributeValueLengthLimit:
        A.attributeValueLengthLimit ??
        (0, A$A.getNumberFromEnv)(
          "OTEL_LOGRECORD_ATTRIBUTE_VALUE_LENGTH_LIMIT",
        ) ??
        (0, A$A.getNumberFromEnv)("OTEL_ATTRIBUTE_VALUE_LENGTH_LIMIT") ??
        1 / 0,
    };
  }
  PR4.reconfigureLimits = n_9;
});
var ER4 = v((TR4) => {
  Object.defineProperty(TR4, "__esModule", { value: !0 });
  TR4.NoopLogRecordProcessor = void 0;
  class NR4 {
    forceFlush() {
      return Promise.resolve();
    }
    onEmit(A, K) {}
    shutdown() {
      return Promise.resolve();
    }
  }
  TR4.NoopLogRecordProcessor = NR4;
});
var RR4 = v((CR4) => {
  Object.defineProperty(CR4, "__esModule", { value: !0 });
  CR4.MultiLogRecordProcessor = void 0;
  var o_9 = P9();
  class kR4 {
    processors;
    forceFlushTimeoutMillis;
    constructor(A, K) {
      ((this.processors = A), (this.forceFlushTimeoutMillis = K));
    }
    async forceFlush() {
      let A = this.forceFlushTimeoutMillis;
      await Promise.all(
        this.processors.map((K) => (0, o_9.callWithTimeout)(K.forceFlush(), A)),
      );
    }
    onEmit(A, K) {
      this.processors.forEach((q) => q.onEmit(A, K));
    }
    async shutdown() {
      await Promise.all(this.processors.map((A) => A.shutdown()));
    }
  }
  CR4.MultiLogRecordProcessor = kR4;
});
var hR4 = v((IR4) => {
  Object.defineProperty(IR4, "__esModule", { value: !0 });
  IR4.LoggerProviderSharedState = void 0;
  var a_9 = ER4(),
    s_9 = RR4();
  class yR4 {
    resource;
    forceFlushTimeoutMillis;
    logRecordLimits;
    processors;
    loggers = new Map();
    activeProcessor;
    registeredLogRecordProcessors = [];
    constructor(A, K, q, Y) {
      if (
        ((this.resource = A),
        (this.forceFlushTimeoutMillis = K),
        (this.logRecordLimits = q),
        (this.processors = Y),
        Y.length > 0)
      )
        ((this.registeredLogRecordProcessors = Y),
          (this.activeProcessor = new s_9.MultiLogRecordProcessor(
            this.registeredLogRecordProcessors,
            this.forceFlushTimeoutMillis,
          )));
      else this.activeProcessor = new a_9.NoopLogRecordProcessor();
    }
  }
  IR4.LoggerProviderSharedState = yR4;
});
var FR4 = v((BR4) => {
  Object.defineProperty(BR4, "__esModule", { value: !0 });
  BR4.LoggerProvider = BR4.DEFAULT_LOGGER_NAME = void 0;
  var _91 = RK(),
    t_9 = l56(),
    e_9 = eXA(),
    bR4 = P9(),
    AG9 = MR4(),
    xR4 = fR4(),
    KG9 = hR4();
  BR4.DEFAULT_LOGGER_NAME = "unknown";
  class uR4 {
    _shutdownOnce;
    _sharedState;
    constructor(A = {}) {
      let K = (0, bR4.merge)({}, (0, xR4.loadDefaultConfig)(), A),
        q = A.resource ?? (0, e_9.defaultResource)();
      ((this._sharedState = new KG9.LoggerProviderSharedState(
        q,
        K.forceFlushTimeoutMillis,
        (0, xR4.reconfigureLimits)(K.logRecordLimits),
        A?.processors ?? [],
      )),
        (this._shutdownOnce = new bR4.BindOnceFuture(this._shutdown, this)));
    }
    getLogger(A, K, q) {
      if (this._shutdownOnce.isCalled)
        return (
          _91.diag.warn("A shutdown LoggerProvider cannot provide a Logger"),
          t_9.NOOP_LOGGER
        );
      if (!A)
        _91.diag.warn("Logger requested without instrumentation scope name.");
      let Y = A || BR4.DEFAULT_LOGGER_NAME,
        z = 
