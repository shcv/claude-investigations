---
id: msg-warning-304051
name: Warning Message
category: message
subcategory: warning
source_line: 304051
---


        : null,
    J;
  if (Array.isArray(Y)) {
    let O = Y.map((X, $) => {
      if (X.type === "image")
        return Tz.createElement(
          S,
          {
            key: $,
            justifyContent: "space-between",
            overflowX: "hidden",
            width: "100%",
          },
          Tz.createElement(
            k6,
            { height: 1 },
            Tz.createElement(V, null, "[Image]"),
          ),
        );
      let _ =
        X.type === "text" && "text" in X && X.text !== null && X.text !== void 0
          ? String(X.text)
          : "";
      return Tz.createElement(zB, { key: $, content: _, verbose: q });
    });
    J = Tz.createElement(S, { flexDirection: "column", width: "100%" }, O);
  } else if (!Y)
    J = Tz.createElement(
      S,
      { justifyContent: "space-between", overflowX: "hidden", width: "100%" },
      Tz.createElement(
        k6,
        { height: 1 },
        Tz.createElement(V, { dimColor: !0 }, "(No content)"),
      ),
    );
  else J = Tz.createElement(zB, { content: Y, verbose: q });
  if (H)
    return Tz.createElement(
      S,
      { flexDirection: "column" },
      Tz.createElement(
        k6,
        { height: 1 },
        Tz.createElement(V, { color: "warning" }, H),
      ),
      J,
    );
  return J;
}
var Tz,
  UkY = 1e4;
var $M6 = k(() => {
  mA();
  __();
  J0();
  rZA();
  Eq();
  g4();
  wX1();
  b1();
  Tz = o($A(), 1);
});
var pkY, dkY, HW7;
var JW7 = k(() => {
  z7();
  $M6();
  ((pkY = U.object({}).passthrough()),
    (dkY = U.string().describe("MCP tool execution result")),
    (HW7 = {
      isMcp: !0,
      isEnabled() {
        return !0;
      },
      isConcurrencySafe() {
        return !1;
      },
      isReadOnly() {
        return !1;
      },
      isDestructive() {
        return !1;
      },
      isOpenWorld() {
        return !1;
      },
      name: "mcp",
      maxResultSizeChars: 1e5,
      async description() {
        return UZ7;
      },
      async prompt() {
        return QZ7;
      },
      inputSchema: pkY,
      outputSchema: dkY,
      async call() {
        return { data: "" };
      },
      async checkPermissions() {
        return {
          behavior: "passthrough",
          message: "MCPTool requires permission.",
        };
      },
      renderToolUseMessage: qW7,
      userFacingName: () => "mcp",
      renderToolUseRejectedMessage: YW7,
      renderToolUseErrorMessage: zW7,
      renderToolUseProgressMessage: wW7,
      renderToolResultMessage: S$1,
      mapToolResultToToolResultBlockParam(A, K) {
        return { tool_use_id: K, type: "tool_result", content: A };
      },
    }));
});
var OW7 = 
