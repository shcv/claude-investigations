---
id: msg-warning-275553
name: Warning Message
category: message
subcategory: warning
source_line: 275553
---

);
  }
  function X$Y(A) {
    let { schema: K, opts: q } = A;
    if (K.default !== void 0 && q.useDefaults && q.strictSchema)
      (0, Jp.checkStrictMode)(A, "default is ignored in the schema root");
  }
  function $$Y(A) {
    let K = A.schema[A.opts.schemaId];
    if (K) A.baseId = (0, A$Y.resolveUrl)(A.opts.uriResolver, A.baseId, K);
  }
  function _$Y(A) {
    if (A.schema.$async && !A.schemaEnv.$async)
      throw Error("async schema in sync schema");
  }
  function p27({ gen: A, schemaEnv: K, schema: q, errSchemaPath: Y, opts: z }) {
    let w = q.$comment;
    if (z.$comment === !0) A.code(TK._
