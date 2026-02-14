---
id: msg-warning-105519
name: Warning Message
category: message
subcategory: warning
source_line: 105519
---

;
          if (Y) {
            let H = Object.assign(Error(w), {
              name: "TimeoutError",
              code: "ETIMEDOUT",
            });
            (A.destroy(H), K(H));
          } else
            ((w +=
              " Init client requestHandler with throwOnRequestTimeout=true to turn this into an error."),
              z?.warn?.(w));
        }, q);
      return -1;
    },
    l_5 = 3000,
    i_5 = (A, { keepAlive: K, keepAliveMsecs: q }, Y = l_5) => {
      if (K !== !0) return -1;
      let z = () => {
        if (A.socket) A.socket.setKeepAlive(K, q || 0);
        else
          A.on("socket", (w) => {
            w.setKeepAlive(K, q || 0);
          });
      };
      if (Y === 0) return (z(), 0);
      return sj.setTimeout(z, Y);
    },
    EB8 = 3000,
    n_5 = (A, K, q = 0) => {
      let Y = (z) => {
        let w = q - z,
          H = () => {
            (A.destroy(),
              K(
                Object.assign(
                  Error(
                    
