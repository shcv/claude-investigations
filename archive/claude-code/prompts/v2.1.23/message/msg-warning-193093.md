---
id: msg-warning-193093
name: Warning Message
category: message
subcategory: warning
source_line: 193093
---

,
    );
  return K.length > 0 ? K : void 0;
}
function NG9(A) {
  let K = c7();
  if (K === "foundry") return !0;
  if (K === "firstParty") return !A.includes("claude-3-");
  return A.includes("claude-opus-4") || A.includes("claude-sonnet-4");
}
function TG9(A) {
  let K = A.toLowerCase();
  return (
    K.includes("claude-opus-4") ||
    K.includes("claude-sonnet-4") ||
    K.includes("claude-haiku-4")
  );
}
function vG9(A) {
  let K = c7();
  if (K === "foundry") return !0;
  if (K === "firstParty") return !A.includes("claude-3-");
  return (
    A.includes("claude-opus-4") ||
    A.includes("claude-sonnet-4") ||
    A.includes("claude-haiku-4")
  );
}
function y36(A) {
  let K = c7();
  if (K !== "firstParty" && K !== "foundry") return !1;
  return (
    A.includes("claude-sonnet-4-5") ||
    A.includes("claude-opus-4-1") ||
    A.includes("claude-opus-4-5") ||
    A.includes("claude-haiku-4-5")
  );
}
function Ny4() {
  let A = c7();
  if (A === "vertex" || A === "bedrock") return mn6;
  return Bn6;
}
function EG9() {
  return (
    (c7() === "firstParty" || c7() === "foundry") &&
    !P1(process.env.CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS)
  );
}
function W91(A) {
  let K = RT(A),
    q = nP();
  if (!q || q.length === 0) return K;
  return [...K, ...q.filter((Y) => !K.includes(Y))];
}
function D91() {
  (I36.cache?.clear?.(), RT.cache?.clear?.(), S36.cache?.clear?.());
}
var Vy4, I36, RT, S36;
var ok = k(() => {
  p7();
  q6();
  z1A();
  B7();
  uz();
  x4();
  l6();
  IH();
  B7();
  Vy4 = [CNA];
  ((I36 = z6((A) => {
    let K = [],
      q = A.includes("haiku"),
      Y = c7(),
      z = EG9();
    if (!q) K.push(xn6);
    if (Z4()) K.push(LE);
    if (A.includes("[1m]")) K.push(CNA);
    if (!P1(process.env.DISABLE_INTERLEAVED_THINKING) && NG9(A)) K.push(un6);
    if (
      (P1(process.env.USE_API_CONTEXT_MANAGEMENT) && !1) ||
      (vG9(A) && G4("tengu_marble_anvil", !1))
    )
      K.push(vnA);
    let w = aY("tengu_tool_pear");
    if (y36(A) && w) K.push(jl);
    if (z && G4("tengu_scarf_coffee", !1)) K.push(EnA);
    if (Y === "vertex" && TG9(A)) K.push(YR1);
    if (Y === "foundry") K.push(YR1);
    if (Y === "firstParty") K.push(gn6);
    if (process.env.ANTHROPIC_BETAS && !q)
      K.push(
        ...process.env.ANTHROPIC_BETAS.split(",")
          .map((H) => H.trim())
          .filter(Boolean),
      );
    return K;
  })),
    (RT = z6((A) => {
      let K = I36(A);
      if (c7() === "bedrock") return K.filter((q) => !wR1.has(q));
      return K;
    })),
    (S36 = z6((A) => {
      return I36(A).filter((q) => wR1.has(q));
    })));
});
function b8() {
  if (J2(process.env.CLAUDE_CODE_AGENT_SWARMS)) return !1;
  if (!G4("tengu_brass_pebble", !1)) return !1;
  if (j91()) return !0;
  if (ak()) return !0;
  let A = Uq();
  if (A === "max" || A === "team") return $5()?.hasExtraUsageEnabled === !0;
  if (A === null) return !0;
  return !1;
}
var t9 = k(() => {
  B7();
  x4();
  l6();
});
import { AsyncLocalStorage as kG9 } from "async_hooks";
function vy4() {
  return Ty4.getStore();
}
function q$A(A, K) {
  return Ty4.run(A, K);
}
var Ty4;
var M91 = k(() => {
  t9();
  Ty4 = new kG9();
});
import { extname as CG9 } from "path";
function jK(A) {
  if (A.startsWith("mcp__")) return "mcp_tool";
  return A;
}
function h36() {
  return P1(process.env.OTEL_LOG_TOOL_DETAILS);
}
function b36(A) {
  if (!A.startsWith("mcp__")) return;
  let K = A.split("__");
  if (K.length < 3) return;
  let q = K[1],
    Y = K.slice(2).join("__");
  if (!q || !Y) return;
  return { serverName: q, mcpToolName: Y };
}
function x36(A, K) {
  if (A !== "Skill") return;
  if (
    typeof K === "object" &&
    K !== null &&
    "skill" in K &&
    typeof K.skill === "string"
  )
    return K.skill;
  return;
}
function SIA(A) {
  let K = CG9(A).toLowerCase();
  if (!K || K === ".") return;
  let q = K.slice(1);
  if (q.length > yG9) return "other";
  return q;
}
function Ey4(A, K) {
  if (!A.includes(".") && !K) return;
  let q,
    Y = new Set();
  if (K) {
    let z = SIA(K);
    if (z) (Y.add(z), (q = z));
  }
  for (let z of A.split(SG9)) {
    if (!z) continue;
    let w = z.split(hG9);
    if (w.length < 2) continue;
    let H = w[0],
      J = H.lastIndexOf("/"),
      O = J >= 0 ? H.slice(J + 1) : H;
    if (!IG9.has(O)) continue;
    for (let X = 1; X < w.length; X++) {
      let $ = w[X];
      if ($.charCodeAt(0) === 45) continue;
      let _ = SIA($);
      if (_ && !Y.has(_)) (Y.add(_), (q = q ? q + "," + _ : _));
    }
  }
  if (!q) return;
  return q;
}
function bG9() {
  let A = vy4();
  if (A) {
    let J = {
      agentId: A.agentId,
      parentSessionId: A.parentSessionId,
      agentType: A.agentType,
    };
    if (A.agentType === "teammate") J.teamName = A.teamName;
    return J;
  }
  let K = q_(),
    q = tn(),
    Y = T3(),
    w = m2() ? "teammate" : K ? "standalone" : void 0;
  if (K || w || q || Y)
    return {
      ...(K ? { agentId: K } : {}),
      ...(w ? { agentType: w } : {}),
      ...(q ? { parentSessionId: q } : {}),
      ...(Y ? { teamName: Y } : {}),
    };
  let H = cn6();
  if (H) return { parentSessionId: H };
  return {};
}
function BG9() {
  return;
}
async function yr(A = {}) {
  let K = A.model ? String(A.model) : J3(),
    q = RT(K),
    Y = await uG9(),
    z = BG9();
  return {
    model: K,
    sessionId: d1(),
    userType: "external",
    ...(q.length > 0 ? { betas: q.join(",") } : {}),
    envContext: Y,
    ...(process.env.CLAUDE_CODE_ENTRYPOINT && {
      entrypoint: process.env.CLAUDE_CODE_ENTRYPOINT,
    }),
    ...(process.env.CLAUDE_AGENT_SDK_VERSION && {
      agentSdkVersion: process.env.CLAUDE_AGENT_SDK_VERSION,
    }),
    isInteractive: String(JzA()),
    clientType: BnA(),
    ...(z && { processMetrics: z }),
    sweBenchRunId: process.env.SWE_BENCH_RUN_ID || "",
    sweBenchInstanceId: process.env.SWE_BENCH_INSTANCE_ID || "",
    sweBenchTaskId: process.env.SWE_BENCH_TASK_ID || "",
    ...bG9(),
  };
}
function ky4(A, K = {}) {
  let q = {};
  for (let [Y, z] of Object.entries(K)) if (z !== void 0) q[Y] = String(z);
  for (let [Y, z] of Object.entries(A)) {
    if (z === void 0) continue;
    if (Y === "envContext") q.env = UA(z);
    else if (Y === "processMetrics") q.process = UA(z);
    else q[Y] = String(z);
  }
  return q;
}
function Cy4(A, K = {}) {
  let { envContext: q, processMetrics: Y, ...z } = A;
  return { ...K, ...z, env: q, ...(Y && { process: Y }), surface: RG9 };
}
function Ly4(A, K, q = {}) {
  let { envContext: Y, processMetrics: z, ...w } = A,
    H = {
      platform: Y.platform,
      arch: Y.arch,
      node_version: Y.nodeVersion,
      terminal: Y.terminal || "unknown",
      package_managers: Y.packageManagers,
      runtimes: Y.runtimes,
      is_running_with_bun: Y.isRunningWithBun,
      is_ci: Y.isCi,
      is_claubbit: Y.isClaubbit,
      is_claude_code_remote: Y.isClaudeCodeRemote,
      is_local_agent_mode: Y.isLocalAgentMode,
      is_conductor: Y.isConductor,
      is_github_action: Y.isGithubAction,
      is_claude_code_action: Y.isClaudeCodeAction,
      is_claude_ai_auth: Y.isClaudeAiAuth,
      version: Y.version,
      build_time: Y.buildTime,
      deployment_environment: Y.deploymentEnvironment,
    };
  if (Y.remoteEnvironmentType)
    H.remote_environment_type = Y.remoteEnvironmentType;
  if (Y.claudeCodeContainerId)
    H.claude_code_container_id = Y.claudeCodeContainerId;
  if (Y.claudeCodeRemoteSessionId)
    H.claude_code_remote_session_id = Y.claudeCodeRemoteSessionId;
  if (Y.tags)
    H.tags = Y.tags
      .split(",")
      .map((O) => O.trim())
      .filter(Boolean);
  if (Y.githubEventName) H.github_event_name = Y.githubEventName;
  if (Y.githubActionsRunnerEnvironment)
    H.github_actions_runner_environment = Y.githubActionsRunnerEnvironment;
  if (Y.githubActionsRunnerOs)
    H.github_actions_runner_os = Y.githubActionsRunnerOs;
  if (Y.githubActionRef) H.github_action_ref = Y.githubActionRef;
  if (Y.wslVersion) H.wsl_version = Y.wslVersion;
  if (Y.versionBase) H.version_base = Y.versionBase;
  let J = {
    session_id: w.sessionId,
    model: w.model,
    user_type: w.userType,
    is_interactive: w.isInteractive === "true",
    client_type: w.clientType,
  };
  if (w.betas) J.betas = w.betas;
  if (w.entrypoint) J.entrypoint = w.entrypoint;
  if (w.agentSdkVersion) J.agent_sdk_version = w.agentSdkVersion;
  if (w.sweBenchRunId) J.swe_bench_run_id = w.sweBenchRunId;
  if (w.sweBenchInstanceId) J.swe_bench_instance_id = w.sweBenchInstanceId;
  if (w.sweBenchTaskId) J.swe_bench_task_id = w.sweBenchTaskId;
  if (w.agentId) J.agent_id = w.agentId;
  if (w.parentSessionId) J.parent_session_id = w.parentSessionId;
  if (w.agentType) J.agent_type = w.agentType;
  if (w.teamName) J.team_name = w.teamName;
  if (K.githubActionsMetadata) {
    let O = K.githubActionsMetadata;
    H.github_actions_metadata = {
      actor_id: O.actorId,
      repository_id: O.repositoryId,
      repository_owner_id: O.repositoryOwnerId,
    };
  }
  return { env: H, ...(z && { process: UA(z) }), core: J, additional: q };
}
var RG9 = "claude-code",
  yG9 = 10,
  IG9,
  SG9,
  hG9,
  xG9,
  uG9;
var sO = k(() => {
  p7();
  z3();
  Rr();
  ok();
  K7();
  q6();
  l6();
  x4();
  B5();
  M91();
  b1();
  W2();
  ((IG9 = new Set([
    "rm",
    "mv",
    "cp",
    "touch",
    "mkdir",
    "chmod",
    "chown",
    "cat",
    "head",
    "tail",
    "sort",
    "stat",
    "diff",
    "wc",
    "grep",
    "rg",
    "sed",
  ])),
    (SG9 = /\s*(?:&&|\|\||[;|])\s*/),
    (hG9 = /\s+/));
  ((xG9 = z6(() => {
    let A = {
      ISSUES_EXPLAINER:
        "report the issue at https://github.com/anthropics/claude-code/issues",
      PACKAGE_URL: "@anthropic-ai/claude-code",
      README_URL: "https://code.claude.com/docs/en/overview",
      VERSION: "2.1.23",
      FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
      BUILD_TIME: "2026-01-29T00:18:20Z",
    }.VERSION.match(/^\d+\.\d+\.\d+(?:-[a-z]+)?/);
    return A ? A[0] : void 0;
  })),
    (uG9 = z6(async () => {
      let [A, K] = await Promise.all([
        m6.getPackageManagers(),
        m6.getRuntimes(),
      ]);
      return {
        platform: m6.platform,
        arch: m6.arch,
        nodeVersion: m6.nodeVersion,
        terminal: QV.terminal,
        packageManagers: A.join(","),
        runtimes: K.join(","),
        isRunningWithBun: m6.isRunningWithBun(),
        isCi: P1(!1),
        isClaubbit: P1(process.env.CLAUBBIT),
        isClaudeCodeRemote: P1(process.env.CLAUDE_CODE_REMOTE),
        isLocalAgentMode: process.env.CLAUDE_CODE_ENTRYPOINT === "local-agent",
        isConductor: m6.isConductor(),
        ...(process.env.CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE && {
          remoteEnvironmentType:
            process.env.CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE,
        }),
        ...{},
        ...(process.env.CLAUDE_CODE_CONTAINER_ID && {
          claudeCodeContainerId: process.env.CLAUDE_CODE_CONTAINER_ID,
        }),
        ...(process.env.CLAUDE_CODE_REMOTE_SESSION_ID && {
          claudeCodeRemoteSessionId: process.env.CLAUDE_CODE_REMOTE_SESSION_ID,
        }),
        ...(process.env.CLAUDE_CODE_TAGS && {
          tags: process.env.CLAUDE_CODE_TAGS,
        }),
        isGithubAction: P1(process.env.GITHUB_ACTIONS),
        isClaudeCodeAction: P1(process.env.CLAUDE_CODE_ACTION),
        isClaudeAiAuth: Z4(),
        version: {
          ISSUES_EXPLAINER:
            "report the issue at https://github.com/anthropics/claude-code/issues",
          PACKAGE_URL: "@anthropic-ai/claude-code",
          README_URL: "https://code.claude.com/docs/en/overview",
          VERSION: "2.1.23",
          FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
          BUILD_TIME: "2026-01-29T00:18:20Z",
        }.VERSION,
        versionBase: xG9(),
        buildTime: {
          ISSUES_EXPLAINER:
            "report the issue at https://github.com/anthropics/claude-code/issues",
          PACKAGE_URL: "@anthropic-ai/claude-code",
          README_URL: "https://code.claude.com/docs/en/overview",
          VERSION: "2.1.23",
          FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
          BUILD_TIME: "2026-01-29T00:18:20Z",
        }.BUILD_TIME,
        deploymentEnvironment: m6.detectDeploymentEnvironment(),
        ...(P1(process.env.GITHUB_ACTIONS) && {
          githubEventName: process.env.GITHUB_EVENT_NAME,
          githubActionsRunnerEnvironment: process.env.RUNNER_ENVIRONMENT,
          githubActionsRunnerOs: process.env.RUNNER_OS,
          githubActionRef: process.env.GITHUB_ACTION_PATH?.includes(
            "claude-code-action/",
          )
            ? process.env.GITHUB_ACTION_PATH.split("claude-code-action/")[1]
            : void 0,
        }),
        ...(h1A() && { wslVersion: h1A() }),
      };
    })));
});
function mG9() {
  return { seconds: 0, nanos: 0 };
}
function Ry4(A) {
  return A !== null && A !== void 0;
}
var hIA;
var u36 = k(() => {
  hIA = {
    fromJSON(A) {
      return {
        seconds: Ry4(A.seconds) ? globalThis.Number(A.seconds) : 0,
        nanos: Ry4(A.nanos) ? globalThis.Number(A.nanos) : 0,
      };
    },
    toJSON(A) {
      let K = {};
      if (A.seconds !== void 0) K.seconds = Math.round(A.seconds);
      if (A.nanos !== void 0) K.nanos = Math.round(A.nanos);
      return K;
    },
    create(A) {
      return hIA.fromPartial(A ?? {});
    },
    fromPartial(A) {
      let K = mG9();
      return ((K.seconds = A.seconds ?? 0), (K.nanos = A.nanos ?? 0), K);
    },
  };
});
function gG9() {
  return { account_id: 0, organization_uuid: "", account_uuid: "" };
}
function B36(A) {
  return A !== null && A !== void 0;
}
var cQ;
var m36 = k(() => {
  cQ = {
    fromJSON(A) {
      return {
        account_id: B36(A.account_id) ? globalThis.Number(A.account_id) : 0,
        organization_uuid: B36(A.organization_uuid)
          ? globalThis.String(A.organization_uuid)
          : "",
        account_uuid: B36(A.account_uuid)
          ? globalThis.String(A.account_uuid)
          : "",
      };
    },
    toJSON(A) {
      let K = {};
      if (A.account_id !== void 0) K.account_id = Math.round(A.account_id);
      if (A.organization_uuid !== void 0)
        K.organization_uuid = A.organization_uuid;
      if (A.account_uuid !== void 0) K.account_uuid = A.account_uuid;
      return K;
    },
    create(A) {
      return cQ.fromPartial(A ?? {});
    },
    fromPartial(A) {
      let K = gG9();
      return (
        (K.account_id = A.account_id ?? 0),
        (K.organization_uuid = A.organization_uuid ?? ""),
        (K.account_uuid = A.account_uuid ?? ""),
        K
      );
    },
  };
});
function FG9() {
  return { actor_id: "", repository_id: "", repository_owner_id: "" };
}
function QG9() {
  return {
    platform: "",
    node_version: "",
    terminal: "",
    package_managers: "",
    runtimes: "",
    is_running_with_bun: !1,
    is_ci: !1,
    is_claubbit: !1,
    is_github_action: !1,
    is_claude_code_action: !1,
    is_claude_ai_auth: !1,
    version: "",
    github_event_name: "",
    github_actions_runner_environment: "",
    github_actions_runner_os: "",
    github_action_ref: "",
    wsl_version: "",
    github_actions_metadata: void 0,
    arch: "",
    is_claude_code_remote: !1,
    remote_environment_type: "",
    claude_code_container_id: "",
    claude_code_remote_session_id: "",
    tags: [],
    deployment_environment: "",
    is_conductor: !1,
    version_base: "",
  };
}
function UG9() {
  return {
    event_name: "",
    client_timestamp: void 0,
    model: "",
    session_id: "",
    user_type: "",
    betas: "",
    env: void 0,
    entrypoint: "",
    agent_sdk_version: "",
    is_interactive: !1,
    client_type: "",
    process: "",
    additional_metadata: "",
    auth: void 0,
    server_timestamp: void 0,
    event_id: "",
    device_id: "",
    swe_bench_run_id: "",
    swe_bench_instance_id: "",
    swe_bench_task_id: "",
    email: "",
    agent_id: "",
    parent_session_id: "",
    agent_type: "",
  };
}
function pG9(A) {
  let K = (A.seconds || 0) * 1000;
  return ((K += (A.nanos || 0) / 1e6), new globalThis.Date(K));
}
function yy4(A) {
  if (A instanceof globalThis.Date) return A;
  else if (typeof A === "string") return new globalThis.Date(A);
  else return pG9(hIA.fromJSON(A));
}
function tK(A) {
  return A !== null && A !== void 0;
}
var P91, V91, f91;
var Iy4 = k(() => {
  u36();
  m36();
  P91 = {
    fromJSON(A) {
      return {
        actor_id: tK(A.actor_id) ? globalThis.String(A.actor_id) : "",
        repository_id: tK(A.repository_id)
          ? globalThis.String(A.repository_id)
          : "",
        repository_owner_id: tK(A.repository_owner_id)
          ? globalThis.String(A.repository_owner_id)
          : "",
      };
    },
    toJSON(A) {
      let K = {};
      if (A.actor_id !== void 0) K.actor_id = A.actor_id;
      if (A.repository_id !== void 0) K.repository_id = A.repository_id;
      if (A.repository_owner_id !== void 0)
        K.repository_owner_id = A.repository_owner_id;
      return K;
    },
    create(A) {
      return P91.fromPartial(A ?? {});
    },
    fromPartial(A) {
      let K = FG9();
      return (
        (K.actor_id = A.actor_id ?? ""),
        (K.repository_id = A.repository_id ?? ""),
        (K.repository_owner_id = A.repository_owner_id ?? ""),
        K
      );
    },
  };
  V91 = {
    fromJSON(A) {
      return {
        platform: tK(A.platform) ? globalThis.String(A.platform) : "",
        node_version: tK(A.node_version)
          ? globalThis.String(A.node_version)
          : "",
        terminal: tK(A.terminal) ? globalThis.String(A.terminal) : "",
        package_managers: tK(A.package_managers)
          ? globalThis.String(A.package_managers)
          : "",
        runtimes: tK(A.runtimes) ? globalThis.String(A.runtimes) : "",
        is_running_with_bun: tK(A.is_running_with_bun)
          ? globalThis.Boolean(A.is_running_with_bun)
          : !1,
        is_ci: tK(A.is_ci) ? globalThis.Boolean(A.is_ci) : !1,
        is_claubbit: tK(A.is_claubbit) ? globalThis.Boolean(A.is_claubbit) : !1,
        is_github_action: tK(A.is_github_action)
          ? globalThis.Boolean(A.is_github_action)
          : !1,
        is_claude_code_action: tK(A.is_claude_code_action)
          ? globalThis.Boolean(A.is_claude_code_action)
          : !1,
        is_claude_ai_auth: tK(A.is_claude_ai_auth)
          ? globalThis.Boolean(A.is_claude_ai_auth)
          : !1,
        version: tK(A.version) ? globalThis.String(A.version) : "",
        github_event_name: tK(A.github_event_name)
          ? globalThis.String(A.github_event_name)
          : "",
        github_actions_runner_environment: tK(
          A.github_actions_runner_environment,
        )
          ? globalThis.String(A.github_actions_runner_environment)
          : "",
        github_actions_runner_os: tK(A.github_actions_runner_os)
          ? globalThis.String(A.github_actions_runner_os)
          : "",
        github_action_ref: tK(A.github_action_ref)
          ? globalThis.String(A.github_action_ref)
          : "",
        wsl_version: tK(A.wsl_version) ? globalThis.String(A.wsl_version) : "",
        github_actions_metadata: tK(A.github_actions_metadata)
          ? P91.fromJSON(A.github_actions_metadata)
          : void 0,
        arch: tK(A.arch) ? globalThis.String(A.arch) : "",
        is_claude_code_remote: tK(A.is_claude_code_remote)
          ? globalThis.Boolean(A.is_claude_code_remote)
          : !1,
        remote_environment_type: tK(A.remote_environment_type)
          ? globalThis.String(A.remote_environment_type)
          : "",
        claude_code_container_id: tK(A.claude_code_container_id)
          ? globalThis.String(A.claude_code_container_id)
          : "",
        claude_code_remote_session_id: tK(A.claude_code_remote_session_id)
          ? globalThis.String(A.claude_code_remote_session_id)
          : "",
        tags: globalThis.Array.isArray(A?.tags)
          ? A.tags.map((K) => globalThis.String(K))
          : [],
        deployment_environment: tK(A.deployment_environment)
          ? globalThis.String(A.deployment_environment)
          : "",
        is_conductor: tK(A.is_conductor)
          ? globalThis.Boolean(A.is_conductor)
          : !1,
        version_base: tK(A.version_base)
          ? globalThis.String(A.version_base)
          : "",
      };
    },
    toJSON(A) {
      let K = {};
      if (A.platform !== void 0) K.platform = A.platform;
      if (A.node_version !== void 0) K.node_version = A.node_version;
      if (A.terminal !== void 0) K.terminal = A.terminal;
      if (A.package_managers !== void 0)
        K.package_managers = A.package_managers;
      if (A.runtimes !== void 0) K.runtimes = A.runtimes;
      if (A.is_running_with_bun !== void 0)
        K.is_running_with_bun = A.is_running_with_bun;
      if (A.is_ci !== void 0) K.is_ci = A.is_ci;
      if (A.is_claubbit !== void 0) K.is_claubbit = A.is_claubbit;
      if (A.is_github_action !== void 0)
        K.is_github_action = A.is_github_action;
      if (A.is_claude_code_action !== void 0)
        K.is_claude_code_action = A.is_claude_code_action;
      if (A.is_claude_ai_auth !== void 0)
        K.is_claude_ai_auth = A.is_claude_ai_auth;
      if (A.version !== void 0) K.version = A.version;
      if (A.github_event_name !== void 0)
        K.github_event_name = A.github_event_name;
      if (A.github_actions_runner_environment !== void 0)
        K.github_actions_runner_environment =
          A.github_actions_runner_environment;
      if (A.github_actions_runner_os !== void 0)
        K.github_actions_runner_os = A.github_actions_runner_os;
      if (A.github_action_ref !== void 0)
        K.github_action_ref = A.github_action_ref;
      if (A.wsl_version !== void 0) K.wsl_version = A.wsl_version;
      if (A.github_actions_metadata !== void 0)
        K.github_actions_metadata = P91.toJSON(A.github_actions_metadata);
      if (A.arch !== void 0) K.arch = A.arch;
      if (A.is_claude_code_remote !== void 0)
        K.is_claude_code_remote = A.is_claude_code_remote;
      if (A.remote_environment_type !== void 0)
        K.remote_environment_type = A.remote_environment_type;
      if (A.claude_code_container_id !== void 0)
        K.claude_code_container_id = A.claude_code_container_id;
      if (A.claude_code_remote_session_id !== void 0)
        K.claude_code_remote_session_id = A.claude_code_remote_session_id;
      if (A.tags?.length) K.tags = A.tags;
      if (A.deployment_environment !== void 0)
        K.deployment_environment = A.deployment_environment;
      if (A.is_conductor !== void 0) K.is_conductor = A.is_conductor;
      if (A.version_base !== void 0) K.version_base = A.version_base;
      return K;
    },
    create(A) {
      return V91.fromPartial(A ?? {});
    },
    fromPartial(A) {
      let K = QG9();
      return (
        (K.platform = A.platform ?? ""),
        (K.node_version = A.node_version ?? ""),
        (K.terminal = A.terminal ?? ""),
        (K.package_managers = A.package_managers ?? ""),
        (K.runtimes = A.runtimes ?? ""),
        (K.is_running_with_bun = A.is_running_with_bun ?? !1),
        (K.is_ci = A.is_ci ?? !1),
        (K.is_claubbit = A.is_claubbit ?? !1),
        (K.is_github_action = A.is_github_action ?? !1),
        (K.is_claude_code_action = A.is_claude_code_action ?? !1),
        (K.is_claude_ai_auth = A.is_claude_ai_auth ?? !1),
        (K.version = A.version ?? ""),
        (K.github_event_name = A.github_event_name ?? ""),
        (K.github_actions_runner_environment =
          A.github_actions_runner_environment ?? ""),
        (K.github_actions_runner_os = A.github_actions_runner_os ?? ""),
        (K.github_action_ref = A.github_action_ref ?? ""),
        (K.wsl_version = A.wsl_version ?? ""),
        (K.github_actions_metadata =
          A.github_actions_metadata !== void 0 &&
          A.github_actions_metadata !== null
            ? P91.fromPartial(A.github_actions_metadata)
            : void 0),
        (K.arch = A.arch ?? ""),
        (K.is_claude_code_remote = A.is_claude_code_remote ?? !1),
        (K.remote_environment_type = A.remote_environment_type ?? ""),
        (K.claude_code_container_id = A.claude_code_container_id ?? ""),
        (K.claude_code_remote_session_id =
          A.claude_code_remote_session_id ?? ""),
        (K.tags = A.tags?.map((q) => q) || []),
        (K.deployment_environment = A.deployment_environment ?? ""),
        (K.is_conductor = A.is_conductor ?? !1),
        (K.version_base = A.version_base ?? ""),
        K
      );
    },
  };
  f91 = {
    fromJSON(A) {
      return {
        event_name: tK(A.event_name) ? globalThis.String(A.event_name) : "",
        client_timestamp: tK(A.client_timestamp)
          ? yy4(A.client_timestamp)
          : void 0,
        model: tK(A.model) ? globalThis.String(A.model) : "",
        session_id: tK(A.session_id) ? globalThis.String(A.session_id) : "",
        user_type: tK(A.user_type) ? globalThis.String(A.user_type) : "",
        betas: tK(A.betas) ? globalThis.String(A.betas) : "",
        env: tK(A.env) ? V91.fromJSON(A.env) : void 0,
        entrypoint: tK(A.entrypoint) ? globalThis.String(A.entrypoint) : "",
        agent_sdk_version: tK(A.agent_sdk_version)
          ? globalThis.String(A.agent_sdk_version)
          : "",
        is_interactive: tK(A.is_interactive)
          ? globalThis.Boolean(A.is_interactive)
          : !1,
        client_type: tK(A.client_type) ? globalThis.String(A.client_type) : "",
        process: tK(A.process) ? globalThis.String(A.process) : "",
        additional_metadata: tK(A.additional_metadata)
          ? globalThis.String(A.additional_metadata)
          : "",
        auth: tK(A.auth) ? cQ.fromJSON(A.auth) : void 0,
        server_timestamp: tK(A.server_timestamp)
          ? yy4(A.server_timestamp)
          : void 0,
        event_id: tK(A.event_id) ? globalThis.String(A.event_id) : "",
        device_id: tK(A.device_id) ? globalThis.String(A.device_id) : "",
        swe_bench_run_id: tK(A.swe_bench_run_id)
          ? globalThis.String(A.swe_bench_run_id)
          : "",
        swe_bench_instance_id: tK(A.swe_bench_instance_id)
          ? globalThis.String(A.swe_bench_instance_id)
          : "",
        swe_bench_task_id: tK(A.swe_bench_task_id)
          ? globalThis.String(A.swe_bench_task_id)
          : "",
        email: tK(A.email) ? globalThis.String(A.email) : "",
        agent_id: tK(A.agent_id) ? globalThis.String(A.agent_id) : "",
        parent_session_id: tK(A.parent_session_id)
          ? globalThis.String(A.parent_session_id)
          : "",
        agent_type: tK(A.agent_type) ? globalThis.String(A.agent_type) : "",
      };
    },
    toJSON(A) {
      let K = {};
      if (A.event_name !== void 0) K.event_name = A.event_name;
      if (A.client_timestamp !== void 0)
        K.client_timestamp = A.client_timestamp.toISOString();
      if (A.model !== void 0) K.model = A.model;
      if (A.session_id !== void 0) K.session_id = A.session_id;
      if (A.user_type !== void 0) K.user_type = A.user_type;
      if (A.betas !== void 0) K.betas = A.betas;
      if (A.env !== void 0) K.env = V91.toJSON(A.env);
      if (A.entrypoint !== void 0) K.entrypoint = A.entrypoint;
      if (A.agent_sdk_version !== void 0)
        K.agent_sdk_version = A.agent_sdk_version;
      if (A.is_interactive !== void 0) K.is_interactive = A.is_interactive;
      if (A.client_type !== void 0) K.client_type = A.client_type;
      if (A.process !== void 0) K.process = A.process;
      if (A.additional_metadata !== void 0)
        K.additional_metadata = A.additional_metadata;
      if (A.auth !== void 0) K.auth = cQ.toJSON(A.auth);
      if (A.server_timestamp !== void 0)
        K.server_timestamp = A.server_timestamp.toISOString();
      if (A.event_id !== void 0) K.event_id = A.event_id;
      if (A.device_id !== void 0) K.device_id = A.device_id;
      if (A.swe_bench_run_id !== void 0)
        K.swe_bench_run_id = A.swe_bench_run_id;
      if (A.swe_bench_instance_id !== void 0)
        K.swe_bench_instance_id = A.swe_bench_instance_id;
      if (A.swe_bench_task_id !== void 0)
        K.swe_bench_task_id = A.swe_bench_task_id;
      if (A.email !== void 0) K.email = A.email;
      if (A.agent_id !== void 0) K.agent_id = A.agent_id;
      if (A.parent_session_id !== void 0)
        K.parent_session_id = A.parent_session_id;
      if (A.agent_type !== void 0) K.agent_type = A.agent_type;
      return K;
    },
    create(A) {
      return f91.fromPartial(A ?? {});
    },
    fromPartial(A) {
      let K = UG9();
      return (
        (K.event_name = A.event_name ?? ""),
        (K.client_timestamp = A.client_timestamp ?? void 0),
        (K.model = A.model ?? ""),
        (K.session_id = A.session_id ?? ""),
        (K.user_type = A.user_type ?? ""),
        (K.betas = A.betas ?? ""),
        (K.env =
          A.env !== void 0 && A.env !== null ? V91.fromPartial(A.env) : void 0),
        (K.entrypoint = A.entrypoint ?? ""),
        (K.agent_sdk_version = A.agent_sdk_version ?? ""),
        (K.is_interactive = A.is_interactive ?? !1),
        (K.client_type = A.client_type ?? ""),
        (K.process = A.process ?? ""),
        (K.additional_metadata = A.additional_metadata ?? ""),
        (K.auth =
          A.auth !== void 0 && A.auth !== null
            ? cQ.fromPartial(A.auth)
            : void 0),
        (K.server_timestamp = A.server_timestamp ?? void 0),
        (K.event_id = A.event_id ?? ""),
        (K.device_id = A.device_id ?? ""),
        (K.swe_bench_run_id = A.swe_bench_run_id ?? ""),
        (K.swe_bench_instance_id = A.swe_bench_instance_id ?? ""),
        (K.swe_bench_task_id = A.swe_bench_task_id ?? ""),
        (K.email = A.email ?? ""),
        (K.agent_id = A.agent_id ?? ""),
        (K.parent_session_id = A.parent_session_id ?? ""),
        (K.agent_type = A.agent_type ?? ""),
        K
      );
    },
  };
});
function dG9() {
  return {
    event_id: "",
    timestamp: void 0,
    experiment_id: "",
    variation_id: 0,
    environment: "",
    user_attributes: "",
    experiment_metadata: "",
    device_id: "",
    auth: void 0,
    session_id: "",
    event_metadata_vars: "",
  };
}
function cG9(A) {
  let K = (A.seconds || 0) * 1000;
  return ((K += (A.nanos || 0) / 1e6), new globalThis.Date(K));
}
function lG9(A) {
  if (A instanceof globalThis.Date) return A;
  else if (typeof A === "string") return new globalThis.Date(A);
  else return cG9(hIA.fromJSON(A));
}
function By(A) {
  return A !== null && A !== void 0;
}
var g36;
var Sy4 = k(() => {
  u36();
  m36();
  g36 = {
    fromJSON(A) {
      return {
        event_id: By(A.event_id) ? globalThis.String(A.event_id) : "",
        timestamp: By(A.timestamp) ? lG9(A.timestamp) : void 0,
        experiment_id: By(A.experiment_id)
          ? globalThis.String(A.experiment_id)
          : "",
        variation_id: By(A.variation_id)
          ? globalThis.Number(A.variation_id)
          : 0,
        environment: By(A.environment) ? globalThis.String(A.environment) : "",
        user_attributes: By(A.user_attributes)
          ? globalThis.String(A.user_attributes)
          : "",
        experiment_metadata: By(A.experiment_metadata)
          ? globalThis.String(A.experiment_metadata)
          : "",
        device_id: By(A.device_id) ? globalThis.String(A.device_id) : "",
        auth: By(A.auth) ? cQ.fromJSON(A.auth) : void 0,
        session_id: By(A.session_id) ? globalThis.String(A.session_id) : "",
        event_metadata_vars: By(A.event_metadata_vars)
          ? globalThis.String(A.event_metadata_vars)
          : "",
      };
    },
    toJSON(A) {
      let K = {};
      if (A.event_id !== void 0) K.event_id = A.event_id;
      if (A.timestamp !== void 0) K.timestamp = A.timestamp.toISOString();
      if (A.experiment_id !== void 0) K.experiment_id = A.experiment_id;
      if (A.variation_id !== void 0)
        K.variation_id = Math.round(A.variation_id);
      if (A.environment !== void 0) K.environment = A.environment;
      if (A.user_attributes !== void 0) K.user_attributes = A.user_attributes;
      if (A.experiment_metadata !== void 0)
        K.experiment_metadata = A.experiment_metadata;
      if (A.device_id !== void 0) K.device_id = A.device_id;
      if (A.auth !== void 0) K.auth = cQ.toJSON(A.auth);
      if (A.session_id !== void 0) K.session_id = A.session_id;
      if (A.event_metadata_vars !== void 0)
        K.event_metadata_vars = A.event_metadata_vars;
      return K;
    },
    create(A) {
      return g36.fromPartial(A ?? {});
    },
    fromPartial(A) {
      let K = dG9();
      return (
        (K.event_id = A.event_id ?? ""),
        (K.timestamp = A.timestamp ?? void 0),
        (K.experiment_id = A.experiment_id ?? ""),
        (K.variation_id = A.variation_id ?? 0),
        (K.environment = A.environment ?? ""),
        (K.user_attributes = A.user_attributes ?? ""),
        (K.experiment_metadata = A.experiment_metadata ?? ""),
        (K.device_id = A.device_id ?? ""),
        (K.auth =
          A.auth !== void 0 && A.auth !== null
            ? cQ.fromPartial(A.auth)
            : void 0),
        (K.session_id = A.session_id ?? ""),
        (K.event_metadata_vars = A.event_metadata_vars ?? ""),
        K
      );
    },
  };
});
import { randomUUID as iG9 } from "crypto";
import { existsSync as nG9 } from "fs";
import {
  readFile as rG9,
  writeFile as oG9,
  appendFile as aG9,
  unlink as hy4,
  readdir as sG9,
  mkdir as by4,
} from "fs/promises";
import * as N91 from "path";
function Y$A() {
  return N91.join(w8(), "telemetry");
}
class F36 {
  endpoint;
  timeout;
  maxBatchSize;
  batchDelayMs;
  baseBackoffDelayMs;
  maxBackoffDelayMs;
  pendingExports = [];
  isShutdown = !1;
  backoffRetryTimer = null;
  backoffAttempt = 0;
  isRetrying = !1;
  lastExportErrorContext;
  constructor(A = {}) {
    let K =
      process.env.ANTHROPIC_BASE_URL === "https://api-staging.anthropic.com"
        ? "https://api-staging.anthropic.com"
        : "https://api.anthropic.com";
    ((this.endpoint = 
