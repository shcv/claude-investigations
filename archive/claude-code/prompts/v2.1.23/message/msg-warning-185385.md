---
id: msg-warning-185385
name: Warning Message
category: message
subcategory: warning
source_line: 185385
---

;
      }
    }
    if (
      H.find(
        ($) =>
          $.key === "shift+enter" &&
          $.command === "workbench.action.terminal.sendSequence" &&
          $.when === "terminalFocus",
      )
    )
      return 
