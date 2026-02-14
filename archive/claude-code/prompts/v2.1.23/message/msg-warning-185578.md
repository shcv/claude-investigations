---
id: msg-warning-185578
name: Warning Message
category: message
subcategory: warning
source_line: 185578
---

;
}
function d89(A) {
  let K = mx(mq6(), ".config", "zed"),
    q = mx(K, "keymap.json");
  try {
    let Y = "[]";
    if (!BA().existsSync(K)) BA().mkdirSync(K);
    if (BA().existsSync(q)) {
      if (
        ((Y = BA().readFileSync(q, { encoding: "utf-8" })),
        Y.includes("shift-enter"))
      )
        return 
