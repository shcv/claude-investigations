---
id: msg-warning-178484
name: Warning Message
category: message
subcategory: warning
source_line: 178484
---

;
    let W = Fg0(Y, {
      key: "shift+enter",
      command: "workbench.action.terminal.sendSequence",
      args: { text: "\x1B\r" },
      when: "terminalFocus",
    });
    return (
      jA().writeFileSync(Z, W, { encoding: "utf-8", flush: !1 }),
      
