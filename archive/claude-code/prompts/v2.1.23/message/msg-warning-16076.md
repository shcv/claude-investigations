---
id: msg-warning-16076
name: Warning Message
category: message
subcategory: warning
source_line: 16076
---

), !0);
    };
  };
  GTA = { assertOptions: u8q, validators: ZoA };
});
class ZTA {
  constructor(A) {
    ((this.defaults = A),
      (this.interceptors = { request: new JI1(), response: new JI1() }));
  }
  async request(A, K) {
    try {
      return await this._request(A, K);
    } catch (q) {
      if (q instanceof Error) {
        let Y = {};
        Error.captureStackTrace ? Error.captureStackTrace(Y) : (Y = Error());
        let z = Y.stack ? Y.stack.replace(/^.+\n/, "") : "";
        try {
          if (!q.stack) q.stack = z;
          else if (z && !String(q.stack).endsWith(z.replace(/^.+\n.+\n/, "")))
            q.stack +=
              
