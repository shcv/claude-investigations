---
id: msg-warning-502174
name: Warning Message
category: message
subcategory: warning
source_line: 502174
---

,
        ),
      );
    }
  }
  return A && Q !== null;
}
class VjA extends Error {
  constructor(A) {
    super(A);
    this.name = "ConnectionFailedError";
  }
}
async function EjA(A, Q, B, G) {
  let Z = Date.now();
  try {
    let Y = await Q();
    if (!lH()) {
      let J = typeof B === "function" ? B(Y) : B || {};
      await yu("tengu_mcp_cli_command_executed", {
        command: A,
        success: !0,
        duration_ms: Date.now() - Z,
        ...J,
      });
    }
    return { success: !0, data: Y };
  } catch (Y) {
    let J = Y instanceof Error ? Y : Error(String(Y));
    if ((console.error(pA.red("Error:"), J.message), !lH())) {
      let I = typeof B === "object" ? B : {};
      await yu("tengu_mcp_cli_command_executed", {
        command: A,
        success: !1,
        error_type: J.constructor.name,
        duration_ms: Date.now() - Z,
        ...I,
        ...G,
      });
    }
    return { success: !1, error: J };
  }
}
function cn() {
  let A = i51();
  if (!NV5(A)) {
    let Q = NXA();
    throw Error(
      
