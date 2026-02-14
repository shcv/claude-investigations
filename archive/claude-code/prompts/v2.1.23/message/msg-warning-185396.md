---
id: msg-warning-185396
name: Warning Message
category: message
subcategory: warning
source_line: 185396
---

;
    let X = S28(w, {
      key: "shift+enter",
      command: "workbench.action.terminal.sendSequence",
      args: { text: "\x1B\r" },
      when: "terminalFocus",
    });
    return (
      x8(z, X, { encoding: "utf-8" }),
      
