---
id: msg-warning-346979
name: Warning Message
category: message
subcategory: warning
source_line: 346979
---

),
        Rx7.DROP_AGGREGATION
      );
    }
    createAggregator(A) {
      return this._resolve(A).createAggregator(A);
    }
  }
  Rx7.DefaultAggregation = Nv6;
  Rx7.DROP_AGGREGATION = new oW1();
  Rx7.SUM_AGGREGATION = new IgA();
  Rx7.LAST_VALUE_AGGREGATION = new aW1();
  Rx7.HISTOGRAM_AGGREGATION = new sW1();
  Rx7.EXPONENTIAL_HISTOGRAM_AGGREGATION = new fv6();
  Rx7.DEFAULT_AGGREGATION = new Nv6();
});
var SgA = v((Bx7) => {
  Object.defineProperty(Bx7, "__esModule", { value: !0 });
  Bx7.toAggregation = Bx7.AggregationType = void 0;
  var g5A = xx7(),
    F5A;
  (function (A) {
    ((A[(A.DEFAULT = 0)] = "DEFAULT"),
      (A[(A.DROP = 1)] = "DROP"),
      (A[(A.SUM = 2)] = "SUM"),
      (A[(A.LAST_VALUE = 3)] = "LAST_VALUE"),
      (A[(A.EXPLICIT_BUCKET_HISTOGRAM = 4)] = "EXPLICIT_BUCKET_HISTOGRAM"),
      (A[(A.EXPONENTIAL_HISTOGRAM = 5)] = "EXPONENTIAL_HISTOGRAM"));
  })((F5A = Bx7.AggregationType || (Bx7.AggregationType = {})));
  function jA2(A) {
    switch (A.type) {
      case F5A.DEFAULT:
        return g5A.DEFAULT_AGGREGATION;
      case F5A.DROP:
        return g5A.DROP_AGGREGATION;
      case F5A.SUM:
        return g5A.SUM_AGGREGATION;
      case F5A.LAST_VALUE:
        return g5A.LAST_VALUE_AGGREGATION;
      case F5A.EXPONENTIAL_HISTOGRAM: {
        let K = A;
        return new g5A.ExponentialHistogramAggregation(
          K.options?.maxSize,
          K.options?.recordMinMax,
        );
      }
      case F5A.EXPLICIT_BUCKET_HISTOGRAM: {
        let K = A;
        if (K.options == null) return g5A.HISTOGRAM_AGGREGATION;
        else
          return new g5A.ExplicitBucketHistogramAggregation(
            K.options?.boundaries,
            K.options?.recordMinMax,
          );
      }
      default:
        throw Error("Unsupported Aggregation");
    }
  }
  Bx7.toAggregation = jA2;
});
var Tv6 = v((gx7) => {
  Object.defineProperty(gx7, "__esModule", { value: !0 });
  gx7.DEFAULT_AGGREGATION_TEMPORALITY_SELECTOR =
    gx7.DEFAULT_AGGREGATION_SELECTOR = void 0;
  var MA2 = cW1(),
    PA2 = SgA(),
    VA2 = (A) => {
      return { type: PA2.AggregationType.DEFAULT };
    };
  gx7.DEFAULT_AGGREGATION_SELECTOR = VA2;
  var fA2 = (A) => MA2.AggregationTemporality.CUMULATIVE;
  gx7.DEFAULT_AGGREGATION_TEMPORALITY_SELECTOR = fA2;
});
var vv6 = v((dx7) => {
  Object.defineProperty(dx7, "__esModule", { value: !0 });
  dx7.MetricReader = void 0;
  var Qx7 = RK(),
    tW1 = GS(),
    Ux7 = Tv6();
  class px7 {
    _shutdown = !1;
    _metricProducers;
    _sdkMetricProducer;
    _aggregationTemporalitySelector;
    _aggregationSelector;
    _cardinalitySelector;
    constructor(A) {
      ((this._aggregationSelector =
        A?.aggregationSelector ?? Ux7.DEFAULT_AGGREGATION_SELECTOR),
        (this._aggregationTemporalitySelector =
          A?.aggregationTemporalitySelector ??
          Ux7.DEFAULT_AGGREGATION_TEMPORALITY_SELECTOR),
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
      let [K, ...q] = await Promise.all([
          this._sdkMetricProducer.collect({ timeoutMillis: A?.timeoutMillis }),
          ...this._metricProducers.map((H) =>
            H.collect({ timeoutMillis: A?.timeoutMillis }),
          ),
        ]),
        Y = K.errors.concat((0, tW1.FlatMap)(q, (H) => H.errors)),
        z = K.resourceMetrics.resource,
        w = K.resourceMetrics.scopeMetrics.concat(
          (0, tW1.FlatMap)(q, (H) => H.resourceMetrics.scopeMetrics),
        );
      return { resourceMetrics: { resource: z, scopeMetrics: w }, errors: Y };
    }
    async shutdown(A) {
      if (this._shutdown) {
        Qx7.diag.error("Cannot call shutdown twice.");
        return;
      }
      if (A?.timeoutMillis == null) await this.onShutdown();
      else await (0, tW1.callWithTimeout)(this.onShutdown(), A.timeoutMillis);
      this._shutdown = !0;
    }
    async forceFlush(A) {
      if (this._shutdown) {
        Qx7.diag.warn("Cannot forceFlush on already shutdown MetricReader.");
        return;
      }
      if (A?.timeoutMillis == null) {
        await this.onForceFlush();
        return;
      }
      await (0, tW1.callWithTimeout)(this.onForceFlush(), A.timeoutMillis);
    }
  }
  dx7.MetricReader = px7;
});
var ox7 = v((nx7) => {
  Object.defineProperty(nx7, "__esModule", { value: !0 });
  nx7.PeriodicExportingMetricReader = void 0;
  var Ev6 = RK(),
    eW1 = P9(),
    TA2 = vv6(),
    lx7 = GS();
  class ix7 extends TA2.MetricReader {
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
        await (0, lx7.callWithTimeout)(this._doRun(), this._exportTimeout);
      } catch (A) {
        if (A instanceof lx7.TimeoutError) {
          Ev6.diag.error(
            "Export took longer than %s milliseconds and timed out.",
            this._exportTimeout,
          );
          return;
        }
        (0, eW1.globalErrorHandler)(A);
      }
    }
    async _doRun() {
      let { resourceMetrics: A, errors: K } = await this.collect({
        timeoutMillis: this._exportTimeout,
      });
      if (K.length > 0)
        Ev6.diag.error(
          "PeriodicExportingMetricReader: metrics collection errors",
          ...K,
        );
      if (A.resource.asyncAttributesPending)
        try {
          await A.resource.waitForAsyncAttributes?.();
        } catch (Y) {
          (Ev6.diag.debug(
            "Error while resolving async portion of resource: ",
            Y,
          ),
            (0, eW1.globalErrorHandler)(Y));
        }
      if (A.scopeMetrics.length === 0) return;
      let q = await eW1.internal._export(this._exporter, A);
      if (q.code !== eW1.ExportResultCode.SUCCESS)
        throw Error(
          
