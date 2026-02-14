---
id: msg-warning-284833
name: Warning Message
category: message
subcategory: warning
source_line: 284833
---

,
      );
    return Q;
  }
  o8.generateRandomPipeName = vh6;
  function kh6(A, Q = "utf-8") {
    let B,
      G = new Promise((Z, Y) => {
        B = Z;
      });
    return new Promise((Z, Y) => {
      let J = (0, ptA.createServer)((I) => {
        (J.close(), B([new TGA(I, Q), new jGA(I, Q)]));
      });
      (J.on("error", Y),
        J.listen(A, () => {
          (J.removeListener("error", Y),
            Z({
              onConnected: () => {
                return G;
              },
            }));
        }));
    });
  }
  o8.createClientPipeTransport = kh6;
  function fh6(A, Q = "utf-8") {
    let B = (0, ptA.createConnection)(A);
    return [new TGA(B, Q), new jGA(B, Q)];
  }
  o8.createServerPipeTransport = fh6;
  function bh6(A, Q = "utf-8") {
    let B,
      G = new Promise((Z, Y) => {
        B = Z;
      });
    return new Promise((Z, Y) => {
      let J = (0, ptA.createServer)((I) => {
        (J.close(), B([new TGA(I, Q), new jGA(I, Q)]));
      });
      (J.on("error", Y),
        J.listen(A, "127.0.0.1", () => {
          (J.removeListener("error", Y),
            Z({
              onConnected: () => {
                return G;
              },
            }));
        }));
    });
  }
  o8.createClientSocketTransport = bh6;
  function hh6(A, Q = "utf-8") {
    let B = (0, ptA.createConnection)(A, "127.0.0.1");
    return [new TGA(B, Q), new jGA(B, Q)];
  }
  o8.createServerSocketTransport = hh6;
  function gh6(A) {
    let Q = A;
    return Q.read !== void 0 && Q.addListener !== void 0;
  }
  function uh6(A) {
    let Q = A;
    return Q.write !== void 0 && Q.addListener !== void 0;
  }
  function mh6(A, Q, B, G) {
    if (!B) B = lw.NullLogger;
    let Z = gh6(A) ? new ei1(A) : A,
      Y = uh6(Q) ? new An1(Q) : Q;
    if (lw.ConnectionStrategy.is(G)) G = { connectionStrategy: G };
    return (0, lw.createMessageConnection)(Z, Y, B, G);
  }
  o8.createMessageConnection = mh6;
});
import { spawn as dh6 } from "child_process";
function XqB(A) {
  let Q,
    B,
    G,
    Z = !1,
    Y = !1,
    J,
    I = !1,
    X = [],
    W = [];
  function K() {
    if (Y) throw J || Error(
