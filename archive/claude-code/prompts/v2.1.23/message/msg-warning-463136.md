---
id: msg-warning-463136
name: Warning Message
category: message
subcategory: warning
source_line: 463136
---

;
            return { tool_use_id: K, type: "tool_result", content: q };
          }
        }
      },
    }));
});
function ty2(A) {
  let K = AI2(A),
    q = sy2.get(K);
  return q !== void 0 ? q : ay2;
}
function ey2(A) {
  return A.trim().split(/\s+/)[0] || "";
}
function AI2(A) {
  let K = R$(A),
    q = K[K.length - 1] || A;
  return ey2(q);
}
function lOK(A, K, q, Y) {
  let w = ty2(A)(K, q, Y);
  return { isError: w.isError, message: w.message };
}
var ay2 = (A, K, q) => ({
    isError: A !== 0,
    message: A !== 0 ? 
