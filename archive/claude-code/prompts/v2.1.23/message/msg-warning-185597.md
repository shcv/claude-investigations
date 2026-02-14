---
id: msg-warning-185597
name: Warning Message
category: message
subcategory: warning
source_line: 185597
---

;
      }
    }
    let z;
    try {
      if (((z = G6(Y)), !Array.isArray(z))) z = [];
    } catch {
      z = [];
    }
    return (
      z.push({
        context: "Terminal",
        bindings: { "shift-enter": ["terminal::SendText", "\x1B\r"] },
      }),
      x8(
        q,
        UA(z, null, 2) +
          
