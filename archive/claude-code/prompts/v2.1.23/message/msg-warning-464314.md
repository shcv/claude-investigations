---
id: msg-warning-464314
name: Warning Message
category: message
subcategory: warning
source_line: 464314
---

,
                  { level: "warn" },
                );
            } else if (J.isFile() && w.endsWith(".md")) {
              if (Uh(H, w, z)) continue;
              let O = H.readFileSync(w, { encoding: "utf-8" }),
                { frontmatter: X, content: $ } = J_(O),
                _,
                G;
              if (Y.commandsMetadata) {
                for (let [j, M] of Object.entries(Y.commandsMetadata))
                  if (M.source) {
                    let P = MPA(Y.path, M.source);
                    if (w === P) {
                      ((_ = 
