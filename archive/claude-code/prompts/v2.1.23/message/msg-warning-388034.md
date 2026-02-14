---
id: msg-warning-388034
name: Warning Message
category: message
subcategory: warning
source_line: 388034
---

,
        ),
        j
      );
    }),
    [z, w] = C$.useState(!1);
  f$2(q, z);
  let H = C$.useRef(null),
    [J, O] = C$.useState(null),
    X = C$.useRef(null),
    $ = C$.useRef(new Map()),
    _ = C$.useRef(new Set()),
    G = C$.useCallback((j) => {
      _.current.add(j);
    }, []),
    Z = C$.useCallback((j) => {
      _.current.delete(j);
    }, []),
    W = C$.useCallback(() => {
      if (X.current) (clearTimeout(X.current), (X.current = null));
    }, []),
    D = C$.useCallback(
      (j) => {
        if ((W(), j !== null))
          X.current = setTimeout(() => {
            (h("[keybindings] Chord timeout - cancelling"),
              (H.current = null),
              O(null));
          }, V$2);
        ((H.current = j), O(j));
      },
      [W],
    );
  return (
    C$.useEffect(() => {
      i_4();
      let j = n_4((M) => {
        (w(!0),
          Y(M),
          h(
            
