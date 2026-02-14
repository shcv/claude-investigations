---
id: msg-warning-484517
name: Warning Message
category: message
subcategory: warning
source_line: 484517
---

,
        );
      Y[W] = X.name;
    }
    let J = {
        clients: A.map(KW5),
        configs: Z,
        tools: G,
        resources: B,
        normalizedNames: Y,
      },
      I = i51();
    await IW5(I, JSON.stringify(J, null, 2));
  } catch {}
}
var qXA = q(() => {
  u0();
  fW();
  pE();
});
function n51() {
  if (TY0) return;
  (th2(), (TY0 = !0));
}
function th2() {
  let A = KiB();
  if (A)
    lW0(A, (B, G) => {
      let Z = A?.createCounter(B, G);
      return {
        add(Y, J = {}) {
          let X = { ...FYA(), ...J };
          Z?.add(Y, X);
        },
      };
    });
}
var TY0 = !1,
  sh2;
var jY0 = q(() => {
  da();
  u0();
  vQ();
  vQ();
  aTA();
  rZ();
  mh2();
  pY();
  fW();
  p2();
  u0();
  ce1();
  QFA();
  L01();
  Md();
  v3A();
  v8A();
  ms();
  V2();
  MYA();
  vQ();
  u0();
  qq();
  D10();
  l51();
  qXA();
  pE();
  fNA();
  mY();
  sh2 = Z0(() => {
    $9("init_function_start");
    try {
      (oTA(),
        $9("init_configs_enabled"),
        p51(),
        $9("init_safe_env_vars_applied"),
        SF.initialize(),
        $9("init_settings_detector_initialized"),
        eh2(),
        $9("init_after_graceful_shutdown"),
        ofQ(),
        $9("init_after_1p_event_logging"),
        Hu0(),
        $9("init_after_oauth_populate"));
      let A = CHA() && !tZ(!0) && !Y4(),
        Q = MiB(),
        B = A || Q;
      if (Q) LiB();
      if (($9("init_after_defer_check"), !B)) (th2(), (TY0 = !0));
      if (
        ($9("init_telemetry_setup"),
        Ag2(),
        gFQ(),
        pFQ(),
        $9("init_network_configured"),
        MaQ(),
        vrB(),
        dh2(),
        jqB(),
        _8(PqB),
        hZ())
      )
        ((process.env.CLAUDE_CODE_SESSION_ID = W0()), oh2());
      if (wXA()) Qg2();
      $9("init_function_end");
    } catch (A) {
      if (A instanceof Ez) return uh2({ error: A });
      else throw A;
    }
  });
});
function bn() {
  return {
    settings: dV(),
    tasks: {},
    verbose: !1,
    mainLoopModel: null,
    mainLoopModelForSession: null,
    statusLineText: void 0,
    showExpandedTodos: !1,
    toolPermissionContext: Uw(),
    agent: void 0,
    agentDefinitions: { activeAgents: [], allAgents: [] },
    fileHistory: { snapshots: [], trackedFiles: new Set() },
    mcp: { clients: [], tools: [], commands: [], resources: {} },
    plugins: {
      enabled: [],
      disabled: [],
      commands: [],
      agents: [],
      errors: [],
      installationStatus: { marketplaces: [], plugins: [] },
    },
    todos: {},
    notifications: { current: null, queue: [] },
    elicitation: { queue: [] },
    thinkingEnabled: LB1(),
    feedbackSurvey: { timeLastShown: null, submitCountAtLastAppearance: null },
    sessionHooks: {},
    inbox: { messages: [] },
    workerPermissions: { queue: [], selectedIndex: 0 },
    pendingWorkerRequest: null,
    promptSuggestion: { text: null, shownAt: 0, acceptedAt: 0 },
    queuedCommands: [],
    gitDiff: {
      stats: null,
      perFileStats: new Map(),
      hunks: new Map(),
      lastUpdated: 0,
    },
  };
}
function a5({ children: A, initialState: Q, onChangeAppState: B }) {
  if (rV.useContext(Bg2))
    throw Error(
      "AppStateProvider can not be nested within another AppStateProvider",
    );
  let [Z, Y] = rV.useState({ currentState: Q ?? bn(), previousState: null }),
    J = rV.useCallback(
      (X) => {
        Y(({ currentState: W }) => {
          let K = { currentState: X(W), previousState: W };
          return (
            B?.({ newState: K.currentState, oldState: K.previousState }),
            K
          );
        });
      },
      [B],
    ),
    I = rV.useMemo(() => {
      let X = [Z.currentState, J];
      return ((X.__IS_INITIALIZED__ = !0), X);
    }, [Z.currentState, J]);
  return (
    rV.useEffect(() => {
      let { toolPermissionContext: X } = Z.currentState;
      if (X.isBypassPermissionsModeAvailable && KTA())
        (f(
          "Disabling bypass permissions mode on mount (remote settings loaded before mount)",
        ),
          J((W) => ({
            ...W,
            toolPermissionContext: a_A(W.toolPermissionContext),
          })));
    }, []),
    I8A(
      rV.useCallback(
        (X, W) => {
          f(
