---
id: msg-warning-261989
name: Warning Message
category: message
subcategory: warning
source_line: 261989
---

);
          return;
      }
    };
var Q$6 = k(() => {
  TM();
  YX();
  y_A();
  Po();
  oO6();
  wq7();
  vxA = tY("IdentityUtils");
});
function Xq7(A) {
  return Y06(
    [
      {
        name: "imdsRetryPolicy",
        retry: ({ retryCount: K, response: q }) => {
          if ((q === null || q === void 0 ? void 0 : q.status) !== 404)
            return { skipStrategy: !0 };
          return te4(K, {
            retryDelayInMs: A.startDelayInMs,
            maxRetryDelayInMs: UYY,
          });
        },
      },
    ],
    { maxRetries: A.maxRetries },
  );
}
var UYY = 64000;
var $q7 = k(() => {
  NU();
  Po();
});
function cYY(A) {
  var K;
  if (!phA(A)) throw Error(
