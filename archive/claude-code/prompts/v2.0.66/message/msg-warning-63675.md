---
id: msg-warning-63675
name: Warning Message
category: message
subcategory: warning
source_line: 63675
---

,
      );
  return [...B, ...G.filter((Z) => !B.includes(Z))];
}
function oyA() {
  (uK1.cache?.clear?.(), d$.cache?.clear?.(), mK1.cache?.clear?.());
}
var Mu0, uK1, d$, mK1;
var Bk = q(() => {
  p2();
  ayA();
  nJ();
  V2();
  rQ();
  hW();
  z4();
  z4();
  Mu0 = [lyA];
  ((uK1 = Z0((A) => {
    let Q = [],
      B = A.includes("haiku"),
      G = T3(),
      Z = sR9();
    if (!B) Q.push(Nu0);
    if (LB()) Q.push(Fm);
    if (A.includes("[1m]")) Q.push(lyA);
    else if (A.includes("claude-sonnet-4-5")) {
      if (c7("sonnet_45_1m_header", "enabled", !1)) Q.push(lyA);
    }
    if (!C0(process.env.DISABLE_INTERLEAVED_THINKING) && oR9(A)) Q.push(qu0);
    let Y = Z && c7("preserve_thinking", "enabled", !1);
    if ((C0(process.env.USE_API_CONTEXT_MANAGEMENT) && !1) || Y) Q.push(iyA);
    let J = UG("tengu_tool_pear");
    if (gK1(A) && J) Q.push(Lu0);
    if (Z && c7("tool_use_examples", "enabled", !1)) Q.push(nyA);
    if (G === "vertex" && rR9(A)) Q.push(fK1);
    if (G === "foundry") Q.push(fK1);
    if (process.env.ANTHROPIC_BETAS && !B)
      Q.push(
        ...process.env.ANTHROPIC_BETAS.split(",")
          .map((I) => I.trim())
          .filter(Boolean),
      );
    return Q;
  })),
    (d$ = Z0((A) => {
      let Q = uK1(A);
      if (T3() === "bedrock") return Q.filter((B) => !hK1.has(B));
      return Q;
    })),
    (mK1 = Z0((A) => {
      return uK1(A).filter((B) => hK1.has(B));
    })));
});
var Ru0 = w((G_9) => {
  G_9.HttpAuthLocation = void 0;
  (function (A) {
    ((A.HEADER = "header"), (A.QUERY = "query"));
  })(G_9.HttpAuthLocation || (G_9.HttpAuthLocation = {}));
  G_9.HttpApiKeyAuthLocation = void 0;
  (function (A) {
    ((A.HEADER = "header"), (A.QUERY = "query"));
  })(G_9.HttpApiKeyAuthLocation || (G_9.HttpApiKeyAuthLocation = {}));
  G_9.EndpointURLScheme = void 0;
  (function (A) {
    ((A.HTTP = "http"), (A.HTTPS = "https"));
  })(G_9.EndpointURLScheme || (G_9.EndpointURLScheme = {}));
  G_9.AlgorithmId = void 0;
  (function (A) {
    ((A.MD5 = "md5"),
      (A.CRC32 = "crc32"),
      (A.CRC32C = "crc32c"),
      (A.SHA1 = "sha1"),
      (A.SHA256 = "sha256"));
  })(G_9.AlgorithmId || (G_9.AlgorithmId = {}));
  var tR9 = (A) => {
      let Q = [];
      if (A.sha256 !== void 0)
        Q.push({
          algorithmId: () => G_9.AlgorithmId.SHA256,
          checksumConstructor: () => A.sha256,
        });
      if (A.md5 != null)
        Q.push({
          algorithmId: () => G_9.AlgorithmId.MD5,
          checksumConstructor: () => A.md5,
        });
      return {
        addChecksumAlgorithm(B) {
          Q.push(B);
        },
        checksumAlgorithms() {
          return Q;
        },
      };
    },
    eR9 = (A) => {
      let Q = {};
      return (
        A.checksumAlgorithms().forEach((B) => {
          Q[B.algorithmId()] = B.checksumConstructor();
        }),
        Q
      );
    },
    A_9 = (A) => {
      return tR9(A);
    },
    Q_9 = (A) => {
      return eR9(A);
    };
  G_9.FieldPosition = void 0;
  (function (A) {
    ((A[(A.HEADER = 0)] = "HEADER"), (A[(A.TRAILER = 1)] = "TRAILER"));
  })(G_9.FieldPosition || (G_9.FieldPosition = {}));
  var B_9 = "__smithy_context";
  G_9.IniSectionType = void 0;
  (function (A) {
    ((A.PROFILE = "profile"),
      (A.SSO_SESSION = "sso-session"),
      (A.SERVICES = "services"));
  })(G_9.IniSectionType || (G_9.IniSectionType = {}));
  G_9.RequestHandlerProtocol = void 0;
  (function (A) {
    ((A.HTTP_0_9 = "http/0.9"),
      (A.HTTP_1_0 = "http/1.0"),
      (A.TDS_8_0 = "tds/8.0"));
  })(G_9.RequestHandlerProtocol || (G_9.RequestHandlerProtocol = {}));
  G_9.SMITHY_CONTEXT_KEY = B_9;
  G_9.getDefaultClientConfiguration = A_9;
  G_9.resolveDefaultRuntimeConfig = Q_9;
});
var Pu0 = w((E_9) => {
  var I_9 = Ru0(),
    X_9 = (A) => {
      return {
        setHttpHandler(Q) {
          A.httpHandler = Q;
        },
        httpHandler() {
          return A.httpHandler;
        },
        updateHttpClientConfig(Q, B) {
          A.httpHandler?.updateHttpClientConfig(Q, B);
        },
        httpHandlerConfigs() {
          return A.httpHandler.httpHandlerConfigs();
        },
      };
    },
    W_9 = (A) => {
      return { httpHandler: A.httpHandler() };
    };
  class _u0 {
    name;
    kind;
    values;
    constructor({
      name: A,
      kind: Q = I_9.FieldPosition.HEADER,
      values: B = [],
    }) {
      ((this.name = A), (this.kind = Q), (this.values = B));
    }
    add(A) {
      this.values.push(A);
    }
    set(A) {
      this.values = A;
    }
    remove(A) {
      this.values = this.values.filter((Q) => Q !== A);
    }
    toString() {
      return this.values
        .map((A) => (A.includes(",") || A.includes(" ") ? 
