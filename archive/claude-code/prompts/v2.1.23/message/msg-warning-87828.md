---
id: msg-warning-87828
name: Warning Message
category: message
subcategory: warning
source_line: 87828
---

);
    Object.assign(J, Y.def);
    let O = q.external?.defs ?? {};
    for (let X of this.seen.entries()) {
      let $ = X[1];
      if ($.def && $.defId) O[$.defId] = $.def;
    }
    if (!q.external && Object.keys(O).length > 0)
      if (this.target === "draft-2020-12") J.$defs = O;
      else J.definitions = O;
    try {
      return JSON.parse(JSON.stringify(J));
    } catch (X) {
      throw Error("Error converting schema to JSON.");
    }
  }
}
function MF(A, K) {
  if (A instanceof fEA) {
    let Y = new leA(K),
      z = {};
    for (let J of A._idmap.entries()) {
      let [O, X] = J;
      Y.process(X);
    }
    let w = {},
      H = { registry: A, uri: K?.uri || ((J) => J), defs: z };
    for (let J of A._idmap.entries()) {
      let [O, X] = J;
      w[O] = Y.emit(X, { ...K, external: H });
    }
    if (Object.keys(z).length > 0) {
      let J = Y.target === "draft-2020-12" ? "$defs" : "definitions";
      w.__shared = { [J]: z };
    }
    return { schemas: w };
  }
  let q = new leA(K);
  return (q.process(A), q.emit(A, K));
}
function e$(A, K) {
  let q = K ?? { seen: new Set() };
  if (q.seen.has(A)) return !1;
  q.seen.add(A);
  let z = A._zod.def;
  switch (z.type) {
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
      return e$(z.element, q);
    case "object": {
      for (let w in z.shape) if (e$(z.shape[w], q)) return !0;
      return !1;
    }
    case "union": {
      for (let w of z.options) if (e$(w, q)) return !0;
      return !1;
    }
    case "intersection":
      return e$(z.left, q) || e$(z.right, q);
    case "tuple": {
      for (let w of z.items) if (e$(w, q)) return !0;
      if (z.rest && e$(z.rest, q)) return !0;
      return !1;
    }
    case "record":
      return e$(z.keyType, q) || e$(z.valueType, q);
    case "map":
      return e$(z.keyType, q) || e$(z.valueType, q);
    case "set":
      return e$(z.valueType, q);
    case "promise":
    case "optional":
    case "nonoptional":
    case "nullable":
    case "readonly":
      return e$(z.innerType, q);
    case "lazy":
      return e$(z.getter(), q);
    case "default":
      return e$(z.innerType, q);
    case "prefault":
      return e$(z.innerType, q);
    case "custom":
      return !1;
    case "transform":
      return !0;
    case "pipe":
      return e$(z.in, q) || e$(z.out, q);
    case "success":
      return !1;
    case "catch":
      return !1;
    default:
  }
  throw Error(
