---
id: msg-warning-343898
name: Warning Message
category: message
subcategory: warning
source_line: 343898
---

, z);
      }
    }
    _tryToCompressBody(A) {
      var K;
      return bDA(this, void 0, void 0, function* () {
        let q = A.body;
        if (
          !A.isCompressable ||
          this._options.disableCompression ||
          typeof q !== "string" ||
          bsY.SDKFlags.get(A.sdkKey, "enable_log_event_compression") !== !0 ||
          (0, Ph7._getStatsigGlobalFlag)("no-compress") != null ||
          typeof CompressionStream > "u" ||
          typeof TextEncoder > "u"
        )
          return;
        try {
          let Y = new TextEncoder().encode(q),
            z = new CompressionStream("gzip"),
            w = z.writable.getWriter();
          (w.write(Y).catch(h5A.Log.error), w.close().catch(h5A.Log.error));
          let H = z.readable.getReader(),
            J = [],
            O;
          while (!(O = yield H.read()).done) J.push(O.value);
          let X = J.reduce((G, Z) => G + Z.length, 0),
            $ = new Uint8Array(X),
            _ = 0;
          for (let G of J) ($.set(G, _), (_ += G.length));
          ((A.body = $),
            (A.params = Object.assign(
              Object.assign(
                {},
                (K = A.params) !== null && K !== void 0 ? K : {},
              ),
              { [_S.NetworkParam.IsGzipped]: "1" },
            )));
        } catch (Y) {
          h5A.Log.warn(
            
