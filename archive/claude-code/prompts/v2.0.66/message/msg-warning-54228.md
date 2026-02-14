---
id: msg-warning-54228
name: Warning Message
category: message
subcategory: warning
source_line: 54228
---

), !0);
    };
  };
  NKA = { assertOptions: bw9, validators: hxA };
});
class qKA {
  constructor(A) {
    ((this.defaults = A),
      (this.interceptors = { request: new RX1(), response: new RX1() }));
  }
  async request(A, Q) {
    try {
      return await this._request(A, Q);
    } catch (B) {
      if (B instanceof Error) {
        let G = {};
        Error.captureStackTrace ? Error.captureStackTrace(G) : (G = Error());
        let Z = G.stack ? G.stack.replace(/^.+\n/, "") : "";
        try {
          if (!B.stack) B.stack = Z;
          else if (Z && !String(B.stack).endsWith(Z.replace(/^.+\n.+\n/, "")))
            B.stack +=
              
