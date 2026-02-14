---
id: msg-warning-437325
name: Warning Message
category: message
subcategory: warning
source_line: 437325
---

,
                  { level: "warn" },
                );
            } else if (J.isFile() && Z.endsWith(".md")) {
              let I = Y.readFileSync(Z, { encoding: "utf-8" }),
                { frontmatter: X, content: W } = dW(I),
                K,
                V;
              if (G.commandsMetadata) {
                for (let [F, C] of Object.entries(G.commandsMetadata))
                  if (C.source) {
                    let $ = hIA(G.path, C.source);
                    if (Z === $) {
                      ((K = 
