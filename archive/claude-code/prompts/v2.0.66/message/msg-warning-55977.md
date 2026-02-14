---
id: msg-warning-55977
name: Warning Message
category: message
subcategory: warning
source_line: 55977
---

, { error: Q }),
          (() =>
            Jq9(this, void 0, void 0, function* () {
              var G, Z, Y, J, I, X, W;
              let K = Q ? Q : Error(ff0),
                V = K instanceof Error,
                E = V ? K.name : "No Name",
                D = kf0(K);
              if (((this._lastSeenError = D), this._seen.has(E))) return;
              if (
                (this._seen.add(E),
                (Z =
                  (G = this._options) === null || G === void 0
                    ? void 0
                    : G.networkConfig) === null || Z === void 0
                  ? void 0
                  : Z.preventAllNetworkTraffic)
              ) {
                (Y = this._emitter) === null ||
                  Y === void 0 ||
                  Y.call(this, { name: "error", error: Q, tag: A });
                return;
              }
              let H = Xq9.SDKType._get(this._sdkKey),
                F = Wq9.StatsigMetadataProvider.get(),
                C = V ? K.stack : Kq9(K),
                $ = JSON.stringify(
                  Object.assign(
                    { tag: A, exception: E, info: C },
                    Object.assign(Object.assign({}, F), { sdkType: H }),
                  ),
                );
              (yield (
                (X =
                  (I =
                    (J = this._options) === null || J === void 0
                      ? void 0
                      : J.networkConfig) === null || I === void 0
                    ? void 0
                    : I.networkOverrideFunc) !== null && X !== void 0
                  ? X
                  : fetch
              )(sv.EXCEPTION_ENDPOINT, {
                method: "POST",
                headers: {
                  "STATSIG-API-KEY": this._sdkKey,
                  "STATSIG-SDK-TYPE": String(H),
                  "STATSIG-SDK-VERSION": String(F.sdkVersion),
                  "Content-Type": "application/json",
                },
                body: $,
              }),
                (W = this._emitter) === null ||
                  W === void 0 ||
                  W.call(this, { name: "error", error: Q, tag: A }));
            }))()
            .then(() => {})
            .catch(() => {}));
      } catch (B) {}
    }
  }
  sv.ErrorBoundary = bf0;
  function kf0(A) {
    if (A instanceof Error) return A;
    else if (typeof A === "string") return Error(A);
    else return Error("An unknown error occurred.");
  }
  function Kq9(A) {
    try {
      return JSON.stringify(A);
    } catch (Q) {
      return ff0;
    }
  }
  function Vq9(A) {
    let Q = new Set(),
      B = Object.getPrototypeOf(A);
    while (B && B !== Object.prototype)
      (Object.getOwnPropertyNames(B)
        .filter(
          (G) =>
            typeof (B === null || B === void 0 ? void 0 : B[G]) === "function",
        )
        .forEach((G) => Q.add(G)),
        (B = Object.getPrototypeOf(B)));
    return Array.from(Q);
  }
});
var gf0 = w((hf0) => {
  Object.defineProperty(hf0, "__esModule", { value: !0 });
});
var mf0 = w((uf0) => {
  Object.defineProperty(uf0, "__esModule", { value: !0 });
});
var cf0 = w((df0) => {
  Object.defineProperty(df0, "__esModule", { value: !0 });
});
var yW1 = w((pf0) => {
  Object.defineProperty(pf0, "__esModule", { value: !0 });
  pf0.createMemoKey = pf0.MemoPrefix = void 0;
  pf0.MemoPrefix = {
    _gate: "g",
    _dynamicConfig: "c",
    _experiment: "e",
    _layer: "l",
    _paramStore: "p",
  };
  var Eq9 = new Set([]),
    Dq9 = new Set(["userPersistedValues"]);
  function Hq9(A, Q, B) {
    let G = 
