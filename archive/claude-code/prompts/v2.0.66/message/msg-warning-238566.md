---
id: msg-warning-238566
name: Warning Message
category: message
subcategory: warning
source_line: 238566
---

);
          return;
      }
    };
var ym1 = q(() => {
  uF();
  sI();
  R5A();
  sc();
  dh1();
  kIB();
  QwA = i5("IdentityUtils");
});
function gIB(A) {
  return rh1(
    [
      {
        name: "imdsRetryPolicy",
        retry: ({ retryCount: Q, response: B }) => {
          if ((B === null || B === void 0 ? void 0 : B.status) !== 404)
            return { skipStrategy: !0 };
          return T8B(Q, {
            retryDelayInMs: A.startDelayInMs,
            maxRetryDelayInMs: EN6,
          });
        },
      },
    ],
    { maxRetries: A.maxRetries },
  );
}
var EN6 = 64000;
var uIB = q(() => {
  sf();
  sc();
});
function FN6(A) {
  var Q;
  if (!wUA(A)) throw Error(
