# Changelog for version 2.1.251

## Summary

This release adds model-switch lifecycle hooks for custom automation and introduces feature-gated support for custom thumbnails on published Artifacts. It also strengthens edit safety, marketplace handling, and Remote Control’s first-use consent flow.

## New Features


### Model-Switch Hooks

What: Hook authors can now run automation before and after Claude Code changes models through `/model`, the model picker, SDK hosts, automatic fallback, or session resume.

Usage:

```json
{
  "hooks": {
    "PreModelSwitch": [
      {
        "hooks": [
          { "type": "command", "command": "./check-model-switch.sh" }
        ]
      }
    ],
    "PostModelSwitch": [
      {
        "hooks": [
          { "type": "command", "command": "./record-model-switch.sh" }
        ]
      }
    ]
  }
}
```

Details:

- `PreModelSwitch` receives the current and requested model, switch source, context-token count, and estimated cache re-write cost.
- A pre-switch hook can allow, deny, or request confirmation for a switch.
- `PostModelSwitch` can provide additional context to Claude’s next request after the new model is active.
- This applies to fast-mode promotions as well as explicit model changes.

Evidence: New hook events `PreModelSwitch` and `PostModelSwitch`; search for `"Before a requested model switch (/model, model picker, set_model)"` and `"Reaches the model with the next request the new model serves"`.

## Improvements


### Remote Control First-Use Consent

Remote Control now explicitly asks for one-time confirmation before it is first enabled. Non-interactive sessions refuse to enable it and direct users to an interactive Claude Code session, avoiding an unattended cross-device connection.

Evidence: Search for `"Remote Control asks for a one-time confirmation before it's first enabled"`.


### Plugin Evaluation Agent Mocks

The early-access plugin-evaluation harness now includes infrastructure for mock agent responders and relay errors, supporting evaluation cases that exercise an agent’s tool-use behavior rather than only static outputs.

Evidence: Search for `"plugin eval: agent mock responder"` and `"plugin eval: mock relay failed:"`.

## Bug Fixes

- Proposed edits are now revalidated immediately before writing. Claude Code refuses an edit if the target changed after preview or resolved outside writable working directories. Evidence: search for `"file changed since the edit was previewed"`.

- Marketplace updates now detect when a backup directory would collide with another registered marketplace instead of overwriting or misusing it. Evidence: search for `"the directory it would use as its backup"`.

- First-use Remote Control activation no longer proceeds silently when the session cannot display the required confirmation. Evidence: search for `"this session can't show it. Run /remote-control from an interactive Claude Code session."`.

## In Development

Features with infrastructure added but not yet enabled. These are shipped dark and may become available in future versions.


### Artifact Custom Thumbnails [In Development]

What: Published HTML Artifacts can declare a custom gallery and link-preview image, including an optional dark-mode variant.

Usage:

```html
<link rel="artifact-thumbnail" href="thumb.png">
<link rel="artifact-thumbnail" href="thumb-dark.jpg" media="(prefers-color-scheme: dark)">
```

Status: Feature-flagged.

Details:

- Thumbnail files must be adjacent PNG or JPEG images, with a default image required before adding a dark-mode variant.
- The declaration must appear near the top of the HTML document.
- The implementation validates image type, dimensions, and a 1 MB size limit.
- Artifact presence is gated by `tengu_brass_plover`, defaulting to disabled unless `CLAUDE_CODE_ARTIFACT_PRESENCE` is supplied.

Evidence: Search for `"<link rel=\"artifact-thumbnail\" href=\"thumb.png\">"` and `tengu_brass_plover`.


Generated with:
- tool: `harness-investigations@1a8fc5b-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.251.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.251.txt`
- source modules: `archive/claude-code/original/cli-v2.1.251.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
