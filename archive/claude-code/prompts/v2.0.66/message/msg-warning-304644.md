---
id: msg-warning-304644
name: Warning Message
category: message
subcategory: warning
source_line: 304644
---

),
        OTB.DROP_AGGREGATION
      );
    }
    createAggregator(A) {
      return this._resolve(A).createAggregator(A);
    }
  }
  OTB.DefaultAggregation = Eo1;
  OTB.DROP_AGGREGATION = new DA1();
  OTB.SUM_AGGREGATION = new TqA();
  OTB.LAST_VALUE_AGGREGATION = new HA1();
  OTB.HISTOGRAM_AGGREGATION = new FA1();
  OTB.EXPONENTIAL_HISTOGRAM_AGGREGATION = new Vo1();
  OTB.DEFAULT_AGGREGATION = new Eo1();
});
var jqA = w((yTB) => {
  Object.defineProperty(yTB, "__esModule", { value: !0 });
  yTB.toAggregation = yTB.AggregationType = void 0;
  var pAA = STB(),
    lAA;
  (function (A) {
    ((A[(A.DEFAULT = 0)] = "DEFAULT"),
      (A[(A.DROP = 1)] = "DROP"),
      (A[(A.SUM = 2)] = "SUM"),
      (A[(A.LAST_VALUE = 3)] = "LAST_VALUE"),
      (A[(A.EXPLICIT_BUCKET_HISTOGRAM = 4)] = "EXPLICIT_BUCKET_HISTOGRAM"),
      (A[(A.EXPONENTIAL_HISTOGRAM = 5)] = "EXPONENTIAL_HISTOGRAM"));
  })((lAA = yTB.AggregationType || (yTB.AggregationType = {})));
  function Ba6(A) {
    switch (A.type) {
      case lAA.DEFAULT:
        return pAA.DEFAULT_AGGREGATION;
      case lAA.DROP:
        return pAA.DROP_AGGREGATION;
      case lAA.SUM:
        return pAA.SUM_AGGREGATION;
      case lAA.LAST_VALUE:
        return pAA.LAST_VALUE_AGGREGATION;
      case lAA.EXPONENTIAL_HISTOGRAM: {
        let Q = A;
        return new pAA.ExponentialHistogramAggregation(
          Q.options?.maxSize,
          Q.options?.recordMinMax,
        );
      }
      case lAA.EXPLICIT_BUCKET_HISTOGRAM: {
        let Q = A;
        if (Q.options == null) return pAA.HISTOGRAM_AGGREGATION;
        else
          return new pAA.ExplicitBucketHistogramAggregation(
            Q.options?.boundaries,
            Q.options?.recordMinMax,
          );
      }
      default:
        throw Error("Unsupported Aggregation");
    }
  }
  yTB.toAggregation = Ba6;
});
var Do1 = w((kTB) => {
  Object.defineProperty(kTB, "__esModule", { value: !0 });
  kTB.DEFAULT_AGGREGATION_TEMPORALITY_SELECTOR =
    kTB.DEFAULT_AGGREGATION_SELECTOR = void 0;
  var Ga6 = XA1(),
    Za6 = jqA(),
    Ya6 = (A) => {
      return { type: Za6.AggregationType.DEFAULT };
    };
  kTB.DEFAULT_AGGREGATION_SELECTOR = Ya6;
  var Ja6 = (A) => Ga6.AggregationTemporality.CUMULATIVE;
  kTB.DEFAULT_AGGREGATION_TEMPORALITY_SELECTOR = Ja6;
});
var Ho1 = w((uTB) => {
  Object.defineProperty(uTB, "__esModule", { value: !0 });
  uTB.MetricReader = void 0;
  var bTB = N9(),
    CA1 = r_(),
    hTB = Do1();
  class gTB {
    _shutdown = !1;
    _metricProducers;
    _sdkMetricProducer;
    _aggregationTemporalitySelector;
    _aggregationSelector;
    _cardinalitySelector;
    constructor(A) {
      ((this._aggregationSelector =
        A?.aggregationSelector ?? hTB.DEFAULT_AGGREGATION_SELECTOR),
        (this._aggregationTemporalitySelector =
          A?.aggregationTemporalitySelector ??
          hTB.DEFAULT_AGGREGATION_TEMPORALITY_SELECTOR),
        (this._metricProducers = A?.metricProducers ?? []),
        (this._cardinalitySelector = A?.cardinalitySelector));
    }
    setMetricProducer(A) {
      if (this._sdkMetricProducer)
        throw Error("MetricReader can not be bound to a MeterProvider again.");
      ((this._sdkMetricProducer = A), this.onInitialized());
    }
    selectAggregation(A) {
      return this._aggregationSelector(A);
    }
    selectAggregationTemporality(A) {
      return this._aggregationTemporalitySelector(A);
    }
    selectCardinalityLimit(A) {
      return this._cardinalitySelector ? this._cardinalitySelector(A) : 2000;
    }
    onInitialized() {}
    async collect(A) {
      if (this._sdkMetricProducer === void 0)
        throw Error("MetricReader is not bound to a MetricProducer");
      if (this._shutdown) throw Error("MetricReader is shutdown");
      let [Q, ...B] = await Promise.all([
          this._sdkMetricProducer.collect({ timeoutMillis: A?.timeoutMillis }),
          ...this._metricProducers.map((J) =>
            J.collect({ timeoutMillis: A?.timeoutMillis }),
          ),
        ]),
        G = Q.errors.concat((0, CA1.FlatMap)(B, (J) => J.errors)),
        Z = Q.resourceMetrics.resource,
        Y = Q.resourceMetrics.scopeMetrics.concat(
          (0, CA1.FlatMap)(B, (J) => J.resourceMetrics.scopeMetrics),
        );
      return { resourceMetrics: { resource: Z, scopeMetrics: Y }, errors: G };
    }
    async shutdown(A) {
      if (this._shutdown) {
        bTB.diag.error("Cannot call shutdown twice.");
        return;
      }
      if (A?.timeoutMillis == null) await this.onShutdown();
      else await (0, CA1.callWithTimeout)(this.onShutdown(), A.timeoutMillis);
      this._shutdown = !0;
    }
    async forceFlush(A) {
      if (this._shutdown) {
        bTB.diag.warn("Cannot forceFlush on already shutdown MetricReader.");
        return;
      }
      if (A?.timeoutMillis == null) {
        await this.onForceFlush();
        return;
      }
      await (0, CA1.callWithTimeout)(this.onForceFlush(), A.timeoutMillis);
    }
  }
  uTB.MetricReader = gTB;
});
var iTB = w((pTB) => {
  Object.defineProperty(pTB, "__esModule", { value: !0 });
  pTB.PeriodicExportingMetricReader = void 0;
  var Fo1 = N9(),
    PqA = X8(),
    Xa6 = Ho1(),
    dTB = r_();
  class cTB extends Xa6.MetricReader {
    _interval;
    _exporter;
    _exportInterval;
    _exportTimeout;
    constructor(A) {
      super({
        aggregationSelector: A.exporter.selectAggregation?.bind(A.exporter),
        aggregationTemporalitySelector:
          A.exporter.selectAggregationTemporality?.bind(A.exporter),
        metricProducers: A.metricProducers,
      });
      if (A.exportIntervalMillis !== void 0 && A.exportIntervalMillis <= 0)
        throw Error("exportIntervalMillis must be greater than 0");
      if (A.exportTimeoutMillis !== void 0 && A.exportTimeoutMillis <= 0)
        throw Error("exportTimeoutMillis must be greater than 0");
      if (
        A.exportTimeoutMillis !== void 0 &&
        A.exportIntervalMillis !== void 0 &&
        A.exportIntervalMillis < A.exportTimeoutMillis
      )
        throw Error(
          "exportIntervalMillis must be greater than or equal to exportTimeoutMillis",
        );
      ((this._exportInterval = A.exportIntervalMillis ?? 60000),
        (this._exportTimeout = A.exportTimeoutMillis ?? 30000),
        (this._exporter = A.exporter));
    }
    async _runOnce() {
      try {
        await (0, dTB.callWithTimeout)(this._doRun(), this._exportTimeout);
      } catch (A) {
        if (A instanceof dTB.TimeoutError) {
          Fo1.diag.error(
            "Export took longer than %s milliseconds and timed out.",
            this._exportTimeout,
          );
          return;
        }
        (0, PqA.globalErrorHandler)(A);
      }
    }
    async _doRun() {
      let { resourceMetrics: A, errors: Q } = await this.collect({
        timeoutMillis: this._exportTimeout,
      });
      if (Q.length > 0)
        Fo1.diag.error(
          "PeriodicExportingMetricReader: metrics collection errors",
          ...Q,
        );
      if (A.resource.asyncAttributesPending)
        try {
          await A.resource.waitForAsyncAttributes?.();
        } catch (G) {
          (Fo1.diag.debug(
            "Error while resolving async portion of resource: ",
            G,
          ),
            (0, PqA.globalErrorHandler)(G));
        }
      if (A.scopeMetrics.length === 0) return;
      let B = await PqA.internal._export(this._exporter, A);
      if (B.code !== PqA.ExportResultCode.SUCCESS)
        throw Error(
          
