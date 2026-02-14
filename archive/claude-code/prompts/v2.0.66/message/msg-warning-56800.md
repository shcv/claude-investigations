---
id: msg-warning-56800
name: Warning Message
category: message
subcategory: warning
source_line: 56800
---

, Z);
      }
    }
    _tryToCompressBody(A) {
      var Q;
      return J9A(this, void 0, void 0, function* () {
        let B = A.body;
        if (
          !A.isCompressable ||
          this._options.disableCompression ||
          typeof B !== "string" ||
          gq9.SDKFlags.get(A.sdkKey, "enable_log_event_compression") !== !0 ||
          (0, Eb0._getStatsigGlobalFlag)("no-compress") != null ||
          typeof CompressionStream > "u" ||
          typeof TextEncoder > "u"
        )
          return;
        try {
          let G = new TextEncoder().encode(B),
            Z = new CompressionStream("gzip"),
            Y = Z.writable.getWriter();
          (Y.write(G).catch(Ho.Log.error), Y.close().catch(Ho.Log.error));
          let J = Z.readable.getReader(),
            I = [],
            X;
          while (!(X = yield J.read()).done) I.push(X.value);
          let W = I.reduce((E, D) => E + D.length, 0),
            K = new Uint8Array(W),
            V = 0;
          for (let E of I) (K.set(E, V), (V += E.length));
          ((A.body = K),
            (A.params = Object.assign(
              Object.assign(
                {},
                (Q = A.params) !== null && Q !== void 0 ? Q : {},
              ),
              { [tO.NetworkParam.IsGzipped]: "1" },
            )));
        } catch (G) {
          Ho.Log.warn(
            
