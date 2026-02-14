---
id: msg-warning-277257
name: Warning Message
category: message
subcategory: warning
source_line: 277257
---

));
  }
  function x_Y(A) {
    let { metaSchema: K } = A;
    if (K === void 0) return;
    if (A.$data && this.opts.$data) K = Iz7(K);
    A.validateSchema = this.compile(K, !0);
  }
  var u_Y = {
    $ref: "https://raw.githubusercontent.com/ajv-validator/ajv/master/lib/refs/data.json#",
  };
  function Iz7(A) {
    return { anyOf: [A, u_Y] };
  }
});
var bz7 = v((hz7) => {
  Object.defineProperty(hz7, "__esModule", { value: !0 });
  var g_Y = {
    keyword: "id",
    code() {
      throw Error('NOT SUPPORTED: keyword "id", use "$id" for schema ID');
    },
  };
  hz7.default = g_Y;
});
var Fz7 = v((mz7) => {
  Object.defineProperty(mz7, "__esModule", { value: !0 });
  mz7.callRef = mz7.getValidate = void 0;
  var Q_Y = fuA(),
    xz7 = yC(),
    $f = B3(),
    sGA = Hp(),
    uz7 = G01(),
    P01 = hY(),
    U_Y = {
      keyword: "$ref",
      schemaType: "string",
      code(A) {
        let { gen: K, schema: q, it: Y } = A,
          { baseId: z, schemaEnv: w, validateName: H, opts: J, self: O } = Y,
          { root: X } = w;
        if ((q === "#" || q === "#/") && z === X.baseId) return _();
        let $ = uz7.resolveRef.call(O, X, z, q);
        if ($ === void 0) throw new Q_Y.default(Y.opts.uriResolver, z, q);
        if ($ instanceof uz7.SchemaEnv) return G($);
        return Z($);
        function _() {
          if (w === X) return V01(A, H, w, w.$async);
          let W = K.scopeValue("root", { ref: X });
          return V01(A, $f._
