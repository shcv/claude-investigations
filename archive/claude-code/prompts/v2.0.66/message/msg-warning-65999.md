---
id: msg-warning-65999
name: Warning Message
category: message
subcategory: warning
source_line: 65999
---

;
          if (G) {
            let J = Object.assign(Error(Y), {
              name: "TimeoutError",
              code: "ETIMEDOUT",
            });
            (A.destroy(J), Q(J));
          } else
            ((Y +=
              " Init client requestHandler with throwOnRequestTimeout=true to turn this into an error."),
              Z?.warn?.(Y));
        }, B);
      return -1;
    },
    VS9 = 3000,
    ES9 = (A, { keepAlive: Q, keepAliveMsecs: B }, G = VS9) => {
      if (Q !== !0) return -1;
      let Z = () => {
        if (A.socket) A.socket.setKeepAlive(Q, B || 0);
        else
          A.on("socket", (Y) => {
            Y.setKeepAlive(Q, B || 0);
          });
      };
      if (G === 0) return (Z(), 0);
      return CF.setTimeout(Z, G);
    },
    Xd0 = 3000,
    DS9 = (A, Q, B = 0) => {
      let G = (Z) => {
        let Y = B - Z,
          J = () => {
            (A.destroy(),
              Q(
                Object.assign(
                  Error(
                    
