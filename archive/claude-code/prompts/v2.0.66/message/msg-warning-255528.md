---
id: msg-warning-255528
name: Warning Message
category: message
subcategory: warning
source_line: 255528
---


        : null,
    I;
  if (Array.isArray(G)) {
    let X = G.map((W, K) => {
      if (W.type === "image")
        return AG.createElement(
          j,
          {
            key: K,
            justifyContent: "space-between",
            overflowX: "hidden",
            width: "100%",
          },
          AG.createElement(
            h0,
            { height: 1 },
            AG.createElement(z, null, "[Image]"),
          ),
        );
      let V =
        W.type === "text" && "text" in W && W.text !== null && W.text !== void 0
          ? String(W.text)
          : "";
      return AG.createElement(JU, { key: K, content: V, verbose: B });
    });
    I = AG.createElement(j, { flexDirection: "column", width: "100%" }, X);
  } else if (!G)
    I = AG.createElement(
      j,
      { justifyContent: "space-between", overflowX: "hidden", width: "100%" },
      AG.createElement(
        h0,
        { height: 1 },
        AG.createElement(z, { dimColor: !0 }, "(No content)"),
      ),
    );
  else I = AG.createElement(JU, { content: G, verbose: B });
  if (J)
    return AG.createElement(
      j,
      { flexDirection: "column" },
      AG.createElement(
        h0,
        { height: 1 },
        AG.createElement(z, { color: "warning" }, J),
      ),
      I,
    );
  return I;
}
var AG,
  LR6 = 1e4;
var Bp1 = q(() => {
  hA();
  lW();
  II();
  M7A();
  h4();
  y2();
  arA();
  AG = o(KA(), 1);
});
var MR6, OR6, ADB;
var QDB = q(() => {
  F2();
  Bp1();
  ((MR6 = P.object({}).passthrough()),
    (OR6 = P.string().describe("MCP tool execution result")),
    (ADB = {
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
      async description() {
        return oEB;
      },
      async prompt() {
        return aEB;
      },
      inputSchema: MR6,
      outputSchema: OR6,
      async call() {
        return { data: "" };
      },
      async checkPermissions() {
        return {
          behavior: "passthrough",
          message: "MCPTool requires permission.",
        };
      },
      renderToolUseMessage: rEB,
      userFacingName: () => "mcp",
      renderToolUseRejectedMessage: sEB,
      renderToolUseErrorMessage: tEB,
      renderToolUseProgressMessage: eEB,
      renderToolResultMessage: fwA,
      mapToolResultToToolResultBlockParam(A, Q) {
        return { tool_use_id: Q, type: "tool_result", content: A };
      },
    }));
});
var BDB = 
