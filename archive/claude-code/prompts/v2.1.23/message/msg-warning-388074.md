---
id: msg-warning-388074
name: Warning Message
category: message
subcategory: warning
source_line: 388074
---

,
          ));
      });
      return () => {
        (j(), W());
      };
    }, [W]),
    C$.default.createElement(
      $31,
      {
        bindings: K,
        pendingChordRef: H,
        pendingChord: J,
        setPendingChord: D,
        activeContexts: _.current,
        registerActiveContext: G,
        unregisterActiveContext: Z,
        handlerRegistryRef: $,
      },
      C$.default.createElement(v$2, {
        bindings: K,
        pendingChordRef: H,
        setPendingChord: D,
        activeContexts: _.current,
        handlerRegistryRef: $,
      }),
      A,
    )
  );
}
function v$2(A) {
  let K = s(6),
    {
      bindings: q,
      pendingChordRef: Y,
      setPendingChord: z,
      activeContexts: w,
      handlerRegistryRef: H,
    } = A,
    J;
  if (K[0] !== w || K[1] !== q || K[2] !== H || K[3] !== Y || K[4] !== z)
    ((J = (X, $, _) => {
      let G = H.current,
        Z = new Set();
      if (G) for (let M of G.values()) for (let P of M) Z.add(P.context);
      let W = [...Z, ...w, "Global"],
        D = Y.current !== null,
        j = O31(X, $, W, q, Y.current);
      A: switch (j.type) {
        case "chord_started": {
          (z(j.pending), _.stopImmediatePropagation());
          break A;
        }
        case "match": {
          if ((z(null), D)) {
            let M = new Set(W);
            if (G) {
              let P = G.get(j.action);
              if (P && P.size > 0) {
                for (let f of P)
                  if (M.has(f.context)) {
                    (f.handler(), _.stopImmediatePropagation());
                    break;
                  }
              }
            }
          }
          break A;
        }
        case "chord_cancelled": {
          z(null);
          break A;
        }
        case "unbound": {
          z(null);
          break A;
        }
        case "none":
      }
    }),
      (K[0] = w),
      (K[1] = q),
      (K[2] = H),
      (K[3] = Y),
      (K[4] = z),
      (K[5] = J));
  else J = K[5];
  return (K8(J), null);
}
var C$,
  V$2 = 1000;
var cB = k(() => {
  cA();
  mA();
  SQ();
  jr();
  Z1();
  kz();
  X31();
  C$ = o($A(), 1);
});
async function zt7(A, K) {
  if (!K || !_M1(xjA(K))) return "no_check_needed";
  if (!At7(A, K)) return "no_check_needed";
  if (!JzA()) return "no_check_needed";
  return (
    n("tengu_managed_settings_security_dialog_shown", {}),
    new Promise((q) => {
      (async () => {
        let { unmount: Y } = await M9(
          GM1.default.createElement(
            $Y,
            null,
            GM1.default.createElement(
              Ez,
              null,
              GM1.default.createElement(qt7, {
                settings: K,
                onAccept: () => {
                  (n("tengu_managed_settings_security_dialog_accepted", {}),
                    Y(),
                    q("approved"));
                },
                onReject: () => {
                  (n("tengu_managed_settings_security_dialog_rejected", {}),
                    Y(),
                    q("rejected"));
                },
              }),
            ),
          ),
          Iw(!1),
        );
      })();
    })
  );
}
function wt7(A) {
  if (A === "rejected") return (Y5(1), !1);
  return !0;
}
var GM1;
var Ht7 = k(() => {
  mA();
  Yt7();
  A4();
  q6();
  l1();
  Sw();
  oL6();
  dB();
  cB();
  GM1 = o($A(), 1);
});
import { join as E$2 } from "path";
import { createHash as k$2 } from "crypto";
import { existsSync as tL6, unlinkSync as Jt7 } from "fs";
function Ot7() {
  if (G3A) return;
  if (Gd())
    G3A = new Promise((A) => {
      ((_d = A),
        setTimeout(() => {
          if (_d)
            (h("Remote settings: Loading promise timed out, resolving anyway"),
              _d(),
              (_d = null));
        }, y$2));
    });
}
function ZM1() {
  return E$2(w8(), C$2);
}
function I$2() {
  return 
