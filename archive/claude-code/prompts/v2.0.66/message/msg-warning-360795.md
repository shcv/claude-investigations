---
id: msg-warning-360795
name: Warning Message
category: message
subcategory: warning
source_line: 360795
---

);
    Object.assign(I, G.def);
    let X = B.external?.defs ?? {};
    for (let W of this.seen.entries()) {
      let K = W[1];
      if (K.def && K.defId) X[K.defId] = K.def;
    }
    if (!B.external && Object.keys(X).length > 0)
      if (this.target === "draft-2020-12") I.$defs = X;
      else I.definitions = X;
    try {
      return JSON.parse(JSON.stringify(I));
    } catch (W) {
      throw Error("Error converting schema to JSON.");
    }
  }
}
function Y00(A, Q) {
  if (A instanceof kQ1) {
    let G = new Z00(Q),
      Z = {};
    for (let I of A._idmap.entries()) {
      let [X, W] = I;
      G.process(W);
    }
    let Y = {},
      J = { registry: A, uri: Q?.uri || ((I) => I), defs: Z };
    for (let I of A._idmap.entries()) {
      let [X, W] = I;
      Y[X] = G.emit(W, { ...Q, external: J });
    }
    if (Object.keys(Z).length > 0) {
      let I = G.target === "draft-2020-12" ? "$defs" : "definitions";
      Y.__shared = { [I]: Z };
    }
    return { schemas: Y };
  }
  let B = new Z00(Q);
  return (B.process(A), B.emit(A, Q));
}
function ZK(A, Q) {
  let B = Q ?? { seen: new Set() };
  if (B.seen.has(A)) return !1;
  B.seen.add(A);
  let Z = A._zod.def;
  switch (Z.type) {
    case "string":
    case "number":
    case "bigint":
    case "boolean":
    case "date":
    case "symbol":
    case "undefined":
    case "null":
    case "any":
    case "unknown":
    case "never":
    case "void":
    case "literal":
    case "enum":
    case "nan":
    case "file":
    case "template_literal":
      return !1;
    case "array":
      return ZK(Z.element, B);
    case "object": {
      for (let Y in Z.shape) if (ZK(Z.shape[Y], B)) return !0;
      return !1;
    }
    case "union": {
      for (let Y of Z.options) if (ZK(Y, B)) return !0;
      return !1;
    }
    case "intersection":
      return ZK(Z.left, B) || ZK(Z.right, B);
    case "tuple": {
      for (let Y of Z.items) if (ZK(Y, B)) return !0;
      if (Z.rest && ZK(Z.rest, B)) return !0;
      return !1;
    }
    case "record":
      return ZK(Z.keyType, B) || ZK(Z.valueType, B);
    case "map":
      return ZK(Z.keyType, B) || ZK(Z.valueType, B);
    case "set":
      return ZK(Z.valueType, B);
    case "promise":
    case "optional":
    case "nonoptional":
    case "nullable":
    case "readonly":
      return ZK(Z.innerType, B);
    case "lazy":
      return ZK(Z.getter(), B);
    case "default":
      return ZK(Z.innerType, B);
    case "prefault":
      return ZK(Z.innerType, B);
    case "custom":
      return !1;
    case "transform":
      return !0;
    case "pipe":
      return ZK(Z.in, B) || ZK(Z.out, B);
    case "success":
      return !1;
    case "catch":
      return !1;
    default:
  }
  throw Error(
