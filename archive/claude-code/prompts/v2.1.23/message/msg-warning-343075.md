---
id: msg-warning-343075
name: Warning Message
category: message
subcategory: warning
source_line: 343075
---

, { error: K }),
          (() =>
            AsY(this, void 0, void 0, function* () {
              var Y, z, w, H, J, O, X;
              let $ = K ? K : Error(pS7),
                _ = $ instanceof Error,
                G = _ ? $.name : "No Name",
                Z = US7($);
              if (((this._lastSeenError = Z), this._seen.has(G))) return;
              if (
                (this._seen.add(G),
                (z =
                  (Y = this._options) === null || Y === void 0
                    ? void 0
                    : Y.networkConfig) === null || z === void 0
                  ? void 0
                  : z.preventAllNetworkTraffic)
              ) {
                (w = this._emitter) === null ||
                  w === void 0 ||
                  w.call(this, { name: "error", error: K, tag: A });
                return;
              }
              let W = qsY.SDKType._get(this._sdkKey),
                D = YsY.StatsigMetadataProvider.get(),
                j = _ ? $.stack : zsY($),
                M = JSON.stringify(
                  Object.assign(
                    { tag: A, exception: G, info: j },
                    Object.assign(Object.assign({}, D), { sdkType: W }),
                  ),
                );
              (yield (
                (O =
                  (J =
                    (H = this._options) === null || H === void 0
                      ? void 0
                      : H.networkConfig) === null || J === void 0
                    ? void 0
                    : J.networkOverrideFunc) !== null && O !== void 0
                  ? O
                  : fetch
              )(op.EXCEPTION_ENDPOINT, {
                method: "POST",
                headers: {
                  "STATSIG-API-KEY": this._sdkKey,
                  "STATSIG-SDK-TYPE": String(W),
                  "STATSIG-SDK-VERSION": String(D.sdkVersion),
                  "Content-Type": "application/json",
                },
                body: M,
              }),
                (X = this._emitter) === null ||
                  X === void 0 ||
                  X.call(this, { name: "error", error: K, tag: A }));
            }))()
            .then(() => {})
            .catch(() => {}));
      } catch (q) {}
    }
  }
  op.ErrorBoundary = dS7;
  function US7(A) {
    if (A instanceof Error) return A;
    else if (typeof A === "string") return Error(A);
    else return Error("An unknown error occurred.");
  }
  function zsY(A) {
    try {
      return JSON.stringify(A);
    } catch (K) {
      return pS7;
    }
  }
  function wsY(A) {
    let K = new Set(),
      q = Object.getPrototypeOf(A);
    while (q && q !== Object.prototype)
      (Object.getOwnPropertyNames(q)
        .filter(
          (Y) =>
            typeof (q === null || q === void 0 ? void 0 : q[Y]) === "function",
        )
        .forEach((Y) => K.add(Y)),
        (q = Object.getPrototypeOf(q)));
    return Array.from(K);
  }
});
var lS7 = v((cS7) => {
  Object.defineProperty(cS7, "__esModule", { value: !0 });
});
var nS7 = v((iS7) => {
  Object.defineProperty(iS7, "__esModule", { value: !0 });
});
var oS7 = v((rS7) => {
  Object.defineProperty(rS7, "__esModule", { value: !0 });
});
var oT6 = v((aS7) => {
  Object.defineProperty(aS7, "__esModule", { value: !0 });
  aS7.createMemoKey = aS7.MemoPrefix = void 0;
  aS7.MemoPrefix = {
    _gate: "g",
    _dynamicConfig: "c",
    _experiment: "e",
    _layer: "l",
    _paramStore: "p",
  };
  var HsY = new Set([]),
    JsY = new Set(["userPersistedValues"]);
  function OsY(A, K, q) {
    let Y = 
