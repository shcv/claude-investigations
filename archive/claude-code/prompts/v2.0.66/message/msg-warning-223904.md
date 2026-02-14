---
id: msg-warning-223904
name: Warning Message
category: message
subcategory: warning
source_line: 223904
---

);
    return;
  }
}
function nV6(A, Q) {
  try {
    if (
      (A.setStatus({ status: "error", error: $nA(Q) ? Q : void 0 }),
      zUA(Q) && Q.statusCode)
    )
      A.setAttribute("http.status_code", Q.statusCode);
    A.end();
  } catch (B) {
    rf.warning(
