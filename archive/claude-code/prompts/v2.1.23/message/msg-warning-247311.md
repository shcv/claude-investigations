---
id: msg-warning-247311
name: Warning Message
category: message
subcategory: warning
source_line: 247311
---

);
    return;
  }
}
function T6Y(A, K) {
  try {
    if (
      (A.setStatus({ status: "error", error: Qw1(K) ? K : void 0 }),
      FhA(K) && K.statusCode)
    )
      A.setAttribute("http.status_code", K.statusCode);
    A.end();
  } catch (q) {
    fU.warning(
