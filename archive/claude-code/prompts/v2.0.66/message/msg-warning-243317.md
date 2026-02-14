---
id: msg-warning-243317
name: Warning Message
category: message
subcategory: warning
source_line: 243317
---

;
            return { tool_use_id: Q, type: "tool_result", content: B };
          }
        }
      },
    }));
});
function N_() {}
function NWB(A, Q, B, G, Z) {
  var Y = [],
    J;
  while (Q)
    (Y.push(Q), (J = Q.previousComponent), delete Q.previousComponent, (Q = J));
  Y.reverse();
  var I = 0,
    X = Y.length,
    W = 0,
    K = 0;
  for (; I < X; I++) {
    var V = Y[I];
    if (!V.removed) {
      if (!V.added && Z) {
        var E = B.slice(W, W + V.count);
        ((E = E.map(function (D, H) {
          var F = G[K + H];
          return F.length > D.length ? F : D;
        })),
          (V.value = A.join(E)));
      } else V.value = A.join(B.slice(W, W + V.count));
      if (((W += V.count), !V.added)) K += V.count;
    } else ((V.value = A.join(G.slice(K, K + V.count))), (K += V.count));
  }
  return Y;
}
function qWB(A, Q) {
  var B;
  for (B = 0; B < A.length && B < Q.length; B++)
    if (A[B] != Q[B]) return A.slice(0, B);
  return A.slice(0, B);
}
function LWB(A, Q) {
  var B;
  if (!A || !Q || A[A.length - 1] != Q[Q.length - 1]) return "";
  for (B = 0; B < A.length && B < Q.length; B++)
    if (A[A.length - (B + 1)] != Q[Q.length - (B + 1)]) return A.slice(-B);
  return A.slice(-B);
}
function Sd1(A, Q, B) {
  if (A.slice(0, Q.length) != Q)
    throw Error(
      "string "
        .concat(JSON.stringify(A), " doesn't start with prefix ")
        .concat(JSON.stringify(Q), "; this is a bug"),
    );
  return B + A.slice(Q.length);
}
function xd1(A, Q, B) {
  if (!Q) return A + B;
  if (A.slice(-Q.length) != Q)
    throw Error(
      "string "
        .concat(JSON.stringify(A), " doesn't end with suffix ")
        .concat(JSON.stringify(Q), "; this is a bug"),
    );
  return A.slice(0, -Q.length) + B;
}
function VwA(A, Q) {
  return Sd1(A, Q, "");
}
function xoA(A, Q) {
  return xd1(A, Q, "");
}
function MWB(A, Q) {
  return Q.slice(0, nq6(A, Q));
}
function nq6(A, Q) {
  var B = 0;
  if (A.length > Q.length) B = A.length - Q.length;
  var G = Q.length;
  if (A.length < Q.length) G = A.length;
  var Z = Array(G),
    Y = 0;
  Z[0] = 0;
  for (var J = 1; J < G; J++) {
    if (Q[J] == Q[Y]) Z[J] = Z[Y];
    else Z[J] = Y;
    while (Y > 0 && Q[J] != Q[Y]) Y = Z[Y];
    if (Q[J] == Q[Y]) Y++;
  }
  Y = 0;
  for (var I = B; I < A.length; I++) {
    while (Y > 0 && A[I] != Q[Y]) Y = Z[Y];
    if (A[I] == Q[Y]) Y++;
  }
  return Y;
}
function OWB(A, Q, B, G) {
  if (Q && B) {
    var Z = Q.value.match(/^\s*/)[0],
      Y = Q.value.match(/\s*$/)[0],
      J = B.value.match(/^\s*/)[0],
      I = B.value.match(/\s*$/)[0];
    if (A) {
      var X = qWB(Z, J);
      ((A.value = xd1(A.value, J, X)),
        (Q.value = VwA(Q.value, X)),
        (B.value = VwA(B.value, X)));
    }
    if (G) {
      var W = LWB(Y, I);
      ((G.value = Sd1(G.value, I, W)),
        (Q.value = xoA(Q.value, W)),
        (B.value = xoA(B.value, W)));
    }
  } else if (B) {
    if (A) B.value = B.value.replace(/^\s*/, "");
    if (G) G.value = G.value.replace(/^\s*/, "");
  } else if (A && G) {
    var K = G.value.match(/^\s*/)[0],
      V = Q.value.match(/^\s*/)[0],
      E = Q.value.match(/\s*$/)[0],
      D = qWB(K, V);
    Q.value = VwA(Q.value, D);
    var H = LWB(VwA(K, D), E);
    ((Q.value = xoA(Q.value, H)),
      (G.value = Sd1(G.value, K, H)),
      (A.value = xd1(A.value, K, K.slice(0, K.length - H.length))));
  } else if (G) {
    var F = G.value.match(/^\s*/)[0],
      C = Q.value.match(/\s*$/)[0],
      $ = MWB(C, F);
    Q.value = xoA(Q.value, $);
  } else if (A) {
    var O = A.value.match(/\s*$/)[0],
      M = Q.value.match(/^\s*/)[0],
      L = MWB(O, M);
    Q.value = VwA(Q.value, L);
  }
}
function jWB(A, Q, B) {
  return TWB.diff(A, Q, B);
}
function voA(A, Q, B) {
  return foA.diff(A, Q, B);
}
function RWB(A, Q) {
  var B = Object.keys(A);
  if (Object.getOwnPropertySymbols) {
    var G = Object.getOwnPropertySymbols(A);
    (Q &&
      (G = G.filter(function (Z) {
        return Object.getOwnPropertyDescriptor(A, Z).enumerable;
      })),
      B.push.apply(B, G));
  }
  return B;
}
function _WB(A) {
  for (var Q = 1; Q < arguments.length; Q++) {
    var B = arguments[Q] != null ? arguments[Q] : {};
    Q % 2
      ? RWB(Object(B), !0).forEach(function (G) {
          eq6(A, G, B[G]);
        })
      : Object.getOwnPropertyDescriptors
        ? Object.defineProperties(A, Object.getOwnPropertyDescriptors(B))
        : RWB(Object(B)).forEach(function (G) {
            Object.defineProperty(A, G, Object.getOwnPropertyDescriptor(B, G));
          });
  }
  return A;
}
function sq6(A, Q) {
  if (typeof A != "object" || !A) return A;
  var B = A[Symbol.toPrimitive];
  if (B !== void 0) {
    var G = B.call(A, Q || "default");
    if (typeof G != "object") return G;
    throw TypeError("@@toPrimitive must return a primitive value.");
  }
  return (Q === "string" ? String : Number)(A);
}
function tq6(A) {
  var Q = sq6(A, "string");
  return typeof Q == "symbol" ? Q : Q + "";
}
function yd1(A) {
  return (
    (yd1 =
      typeof Symbol == "function" && typeof Symbol.iterator == "symbol"
        ? function (Q) {
            return typeof Q;
          }
        : function (Q) {
            return Q &&
              typeof Symbol == "function" &&
              Q.constructor === Symbol &&
              Q !== Symbol.prototype
              ? "symbol"
              : typeof Q;
          }),
    yd1(A)
  );
}
function eq6(A, Q, B) {
  if (((Q = tq6(Q)), Q in A))
    Object.defineProperty(A, Q, {
      value: B,
      enumerable: !0,
      configurable: !0,
      writable: !0,
    });
  else A[Q] = B;
  return A;
}
function Pd1(A) {
  return AL6(A) || QL6(A) || BL6(A) || GL6();
}
function AL6(A) {
  if (Array.isArray(A)) return vd1(A);
}
function QL6(A) {
  if (
    (typeof Symbol < "u" && A[Symbol.iterator] != null) ||
    A["@@iterator"] != null
  )
    return Array.from(A);
}
function BL6(A, Q) {
  if (!A) return;
  if (typeof A === "string") return vd1(A, Q);
  var B = Object.prototype.toString.call(A).slice(8, -1);
  if (B === "Object" && A.constructor) B = A.constructor.name;
  if (B === "Map" || B === "Set") return Array.from(A);
  if (B === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(B))
    return vd1(A, Q);
}
function vd1(A, Q) {
  if (Q == null || Q > A.length) Q = A.length;
  for (var B = 0, G = Array(Q); B < Q; B++) G[B] = A[B];
  return G;
}
function GL6() {
  throw TypeError(
