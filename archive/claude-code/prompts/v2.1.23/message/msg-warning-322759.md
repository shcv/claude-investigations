---
id: msg-warning-322759
name: Warning Message
category: message
subcategory: warning
source_line: 322759
---

,
      );
    return K;
  }
  XY.generateRandomPipeName = DmY;
  function jmY(A, K = "utf-8") {
    let q,
      Y = new Promise((z, w) => {
        q = z;
      });
    return new Promise((z, w) => {
      let H = (0, FG1.createServer)((J) => {
        (H.close(), q([new BWA(J, K), new mWA(J, K)]));
      });
      (H.on("error", w),
        H.listen(A, () => {
          (H.removeListener("error", w),
            z({
              onConnected: () => {
                return Y;
              },
            }));
        }));
    });
  }
  XY.createClientPipeTransport = jmY;
  function MmY(A, K = "utf-8") {
    let q = (0, FG1.createConnection)(A);
    return [new BWA(q, K), new mWA(q, K)];
  }
  XY.createServerPipeTransport = MmY;
  function PmY(A, K = "utf-8") {
    let q,
      Y = new Promise((z, w) => {
        q = z;
      });
    return new Promise((z, w) => {
      let H = (0, FG1.createServer)((J) => {
        (H.close(), q([new BWA(J, K), new mWA(J, K)]));
      });
      (H.on("error", w),
        H.listen(A, "127.0.0.1", () => {
          (H.removeListener("error", w),
            z({
              onConnected: () => {
                return Y;
              },
            }));
        }));
    });
  }
  XY.createClientSocketTransport = PmY;
  function VmY(A, K = "utf-8") {
    let q = (0, FG1.createConnection)(A, "127.0.0.1");
    return [new BWA(q, K), new mWA(q, K)];
  }
  XY.createServerSocketTransport = VmY;
  function fmY(A) {
    let K = A;
    return K.read !== void 0 && K.addListener !== void 0;
  }
  function NmY(A) {
    let K = A;
    return K.write !== void 0 && K.addListener !== void 0;
  }
  function TmY(A, K, q, Y) {
    if (!q) q = qv.NullLogger;
    let z = fmY(A) ? new Of6(A) : A,
      w = NmY(K) ? new Xf6(K) : K;
    if (qv.ConnectionStrategy.is(Y)) Y = { connectionStrategy: Y };
    return (0, qv.createMessageConnection)(z, w, q, Y);
  }
  XY.createMessageConnection = TmY;
});
import { spawn as vmY } from "child_process";
function Av7(A) {
  let K,
    q,
    Y,
    z = !1,
    w = !1,
    H,
    J = !1,
    O = [],
    X = [];
  function $() {
    if (w) throw H || Error(
