---
id: msg-warning-536473
name: Warning Message
category: message
subcategory: warning
source_line: 536473
---

,
        ),
      );
    }
  }
  return A && K !== null;
}
async function hcA(A, K, q, Y) {
  let z = Date.now();
  try {
    let w = await K();
    if (!Rj()) {
      let H = typeof q === "function" ? q(w) : q || {};
      await Ll("tengu_mcp_cli_command_executed", {
        command: A,
        success: !0,
        duration_ms: Date.now() - z,
        ...H,
      });
    }
    return { success: !0, data: w };
  } catch (w) {
    let H = w instanceof Error ? w : Error(String(w));
    if ((console.error(O1.red("Error:"), H.message), !Rj())) {
      let J = typeof q === "object" ? q : {};
      await Ll("tengu_mcp_cli_command_executed", {
        command: A,
        success: !1,
        error_type: H.constructor.name,
        duration_ms: Date.now() - z,
        ...J,
        ...Y,
      });
    }
    return { success: !1, error: H };
  }
}
function AAA() {
  let A = gE1();
  if (!it2(A)) {
    let K = bVA();
    throw Error(
      
