---
id: msg-warning-387997
name: Warning Message
category: message
subcategory: warning
source_line: 387997
---

;
      ((X = X + " · /doctor for details"),
        Y({
          key: "keybinding-config-warning",
          text: X,
          color: J > 0 ? "error" : "warning",
          priority: J > 0 ? "immediate" : "high",
          timeoutMs: 60000,
        }));
    }),
      (q[0] = Y),
      (q[1] = z),
      (q[2] = A),
      (q[3] = w));
  else w = q[3];
  let H;
  if (q[4] !== Y || q[5] !== K || q[6] !== z || q[7] !== A)
    ((H = [A, K, Y, z]),
      (q[4] = Y),
      (q[5] = K),
      (q[6] = z),
      (q[7] = A),
      (q[8] = H));
  else H = q[8];
  C$.useEffect(w, H);
}
function N$2(A) {
  return A.severity === "warning";
}
function T$2(A) {
  return A.severity === "error";
}
function Ez({ children: A }) {
  let [{ bindings: K, warnings: q }, Y] = C$.useState(() => {
      let j = qIA();
      return (
        h(
          
