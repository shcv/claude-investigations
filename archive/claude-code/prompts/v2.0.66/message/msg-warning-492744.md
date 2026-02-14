---
id: msg-warning-492744
name: Warning Message
category: message
subcategory: warning
source_line: 492744
---

, {
          level: "warn",
        });
    } catch {}
  }),
    process.on("warning", N71));
}
var _u2,
  fV5,
  N71 = null;
var ju2 = q(() => {
  _0();
  Q0();
  J8();
  _u2 = new Map();
  fV5 = [
    /MaxListenersExceededWarning.*AbortSignal/,
    /MaxListenersExceededWarning.*EventTarget/,
  ];
});
import { createHash as hV5 } from "crypto";
function Pu2() {
  let A = !(
    C0(process.env.CLAUDE_CODE_USE_BEDROCK) ||
    C0(process.env.CLAUDE_CODE_USE_VERTEX) ||
    C0(process.env.CLAUDE_CODE_USE_FOUNDRY) ||
    process.env.CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC ||
    process.env.DISABLE_ERROR_REPORTING
  );
  ln.init({
    dsn: Eh0,
    enabled: A,
    environment: "external",
    release: {
      ISSUES_EXPLAINER:
        "report the issue at https://github.com/anthropics/claude-code/issues",
      PACKAGE_URL: "@anthropic-ai/claude-code",
      README_URL: "https://code.claude.com/docs/en/overview",
      VERSION: "2.0.66",
      FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
      BUILD_TIME: "2025-12-11T19:03:12Z",
    }.VERSION,
    integrations: [
      new ln.Integrations.OnUncaughtException({
        exitEvenIfOtherHandlersAreRegistered: !1,
      }),
      new ln.Integrations.OnUnhandledRejection({ mode: "warn" }),
      new ln.Integrations.Http({ tracing: !0 }),
      ln.rewriteFramesIntegration(),
    ],
    tracesSampleRate: 1,
    tracePropagationTargets: ["localhost"],
    beforeSend(Q) {
      try {
        let B = Fn();
        if (B.userID) {
          let G = hV5("sha256").update(B.userID).digest("hex");
          Q.user = { id: G };
        }
      } catch {}
      try {
        Q.tags = {
          ...Q.tags,
          terminal: QQ.terminal,
          userType: "external",
          ...kg2(),
        };
      } catch {}
      try {
        Q.extra = { ...Q.extra, sessionId: W0() };
      } catch {}
      return Q;
    },
  });
}
var ln;
var Su2 = q(() => {
  tk();
  T8();
  z4();
  u0();
  rQ();
  ln = o(C60(), 1);
});
import { join as xu2 } from "path";
function uV5() {
  return 
