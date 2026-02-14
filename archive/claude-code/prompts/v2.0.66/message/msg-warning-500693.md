---
id: msg-warning-500693
name: Warning Message
category: message
subcategory: warning
source_line: 500693
---

,
            );
        }
        if (!ZA) {
          if ((await Kc2(TA, V, a0)) && J?.trim().toLowerCase() === "/login")
            J = "";
        }
        if (process.exitCode !== void 0) {
          f("Graceful shutdown initiated, skipping further initialization");
          return;
        }
        (KRB().catch((d0) => r(d0)), syQ(), GN2(), Zc2(), am2(Y4()));
        let G0 = xtA(N1),
          $0 =
            NA === void 0 && (_A || ZA)
              ? await G0
              : { clients: [], tools: [], commands: [] },
          F0 = MA ? MA : $0.clients,
          HA = NA ? NA : $0.tools,
          $A = NA ? [] : $0.commands,
          A1;
        if (NA !== void 0) A1 = new DjA(F0, HA);
        else if (_XA())
          ((A1 = new DjA(F0, HA)),
            A1.start()
              .then(({ url: d0 }) => {
                let OQ = A1.getSecret();
                (XjA({ url: d0, key: OQ }),
                  f(
