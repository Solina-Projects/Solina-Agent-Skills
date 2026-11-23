---
name: eas-observe
description: Use for anything related to EAS Observe - adding `expo-observe` to an Expo project (AppMetricsRoot/ObserveRoot HOC, markInteractive and ObserveInteractiveMarker, the useObserve hook, the Expo Router / React Navigation integrations for per-route metrics, the expo-image and Reanimated integrations, user-defined events via `Observe.logEvent`, error reporting via ObserveErrorBoundary and `Observe.reportError`, native crash reporting, source map upload for symbolicated stack traces, and runtime config such as sampleRate and dispatchInDebug), querying via the EAS CLI (`eas observe:metrics-summary`, `observe:metrics`, `observe:routes`, `observe:events`, `observe:session`, `observe:versions`, `observe:errors`, `observe:event`) or the Expo MCP `observe_*` tools, interpreting the resulting metrics (cold/warm launch, TTR, TTI, navigation cold/warm TTR, update download, and the TTI frameRate/device/network params for triaging slow startups), or shipping an Observe integration inside a third-party package.
license: MIT
---

# EAS Observe

> **EAS service - costs apply.** EAS Observe is an Expo Application Services product. The free EAS plan allows up to 10,000 monthly active users, with a limited set of features; higher usage requires a paid subscription. For details, see https://expo.dev/pricing#plan-features.

EAS Observe tracks startup, navigation, and custom-event performance from production Expo apps, and records JavaScript errors and native crashes. It needs a development or production build — the native library is not in Expo Go.

> **Source of truth:** https://docs.expo.dev/eas/observe/ — always consult the canonical docs when API details matter, especially get-started, configuration, integrations, and the metrics reference. EAS Observe is evolving; this skill's references are written to stay accurate but may lag the docs.

<!-- MUSE-ADAPT -->

## Muse adaptation — read first

This skill runs inside Muse's own environment, for Nasser. Where the original instructions below conflict with these points, these points win.

- Host: Linux VM (4 CPU, ~7 GB RAM, x86_64), no GPU. Toolchains live under the home directory only; never rely on system installs. For npm, always set npm_config_cache=/tmp/npm-cache.
- The user (Nasser) is Persian-speaking and phone-only; he has no computer. Deliverables reach him as files in this chat. Explain everything in simple Persian and translate every English label - his English is effectively zero.
- Register: two-way, comfortable, street-style, blunt and honest. No formalities.
- Never ask design-detail questions. Decide, build, then report shortly.
- For Nasser's own apps (Solina-Player, Solina-Launcher), follow the design decisions already recorded in memory (Material 3 Expressive, RTL Persian, Vazirmatn) and never copy another app's branding.
- UI copy: Persian first, Western (English) digits only, no em dashes in UI copy.
- Apply quality gates silently. Never paste internal gate or lint reports to the user; report outcomes in a few lines.
- Secrets never go into files, memory or chat output. Publishing anything publicly needs his explicit approval first.
- The original skill may name Claude Code tools (Read, Write, Edit, Glob, Grep, Bash). Use Muse's own tools instead (file read/write/edit, shell, browser). Use the browser tools for live pages and real-site screenshots.
- Video generation on this host is limited; never promise video output that a code-only path cannot deliver.

Skill-specific note: No Expo or EAS account is connected yet; EAS build, submit and update flows need the user's sign-in first, arranged with Nasser when a real project starts. All work happens on this VM (Nasser has no computer); keep project files under ~/workspace.

## Which reference to read

The five reference files in `./references/` cover what people typically need this skill for:

- **Adding EAS Observe to a project** → [`./references/setup.md`](./references/setup.md). Install, wrap the root layout (`AppMetricsRoot` on SDK 55, `ObserveRoot` on SDK 56+), mark the app interactive (global `markInteractive()` on SDK 55, the `useObserve()` hook or `<ObserveInteractiveMarker />` on SDK 56+), optional per-route navigation metrics through the Expo Router / React Navigation integrations, user-defined events via `Observe.logEvent` (SDK 56+), error reporting, and runtime configuration (sampling, dispatch, environments, custom endpoint).
- **Querying metrics from the terminal** → [`./references/queries.md`](./references/queries.md). The `eas observe:*` commands — `metrics-summary`, `metrics`, `routes`, `events`, `session`, `versions`, `errors`, `event` — with flags, metric aliases, table layouts, JSON shapes, and common workflows. Also the matching `observe_*` tools in the Expo MCP Server, and how their inputs differ from the CLI flags.
- **Reading a dashboard or CLI output** → [`./references/metrics.md`](./references/metrics.md). Target thresholds per metric, what the automatic TTI params mean (`frameRate.*`, `device.*`, `network.*`), and diagnostic patterns for telling slow-but-smooth startup apart from main-thread contention, hard blocks, or throttled devices.
- **Reporting problems from library integrations** → [`./references/library-integrations.md`](./references/library-integrations.md). The current and future integrations that report problems a library detects as events or errors, with their options, limits, and how to query the reports. Currently: `expo-image` (`expo-image.oversized` events for images decoded far larger than the screen) and `react-native-reanimated` (`reanimated.error` errors and optional `reanimated.warning` events).
- **Shipping an Observe integration in a library** → [`./references/third-party.md`](./references/third-party.md). For package authors only (SDK 57+): optional peer dependency, config declaration merging, `Observe.registerIntegration()`, and event naming.

## Quick links to the docs

- Get started: https://docs.expo.dev/eas/observe/get-started/
- Dashboard guide: https://docs.expo.dev/eas/observe/dashboard/
- Querying with EAS CLI: https://docs.expo.dev/eas/observe/eas-cli/
- Querying with the Expo MCP Server: https://docs.expo.dev/eas/observe/mcp/
- Metrics reference: https://docs.expo.dev/eas/observe/reference/metrics/
- Expo Router integration: https://docs.expo.dev/eas/observe/integrations/expo-router/
- React Navigation integration: https://docs.expo.dev/eas/observe/integrations/react-navigation/
- Expo Image integration: https://docs.expo.dev/eas/observe/integrations/expo-image/
- Reanimated integration: https://docs.expo.dev/eas/observe/integrations/react-native-reanimated/
- User-defined events: https://docs.expo.dev/eas/observe/events/
- Error reporting: https://docs.expo.dev/eas/observe/errors/
- Configuration: https://docs.expo.dev/eas/observe/configuration/
- Third-party integrations: https://docs.expo.dev/eas/observe/integrations/third-party/
- EAS Update download performance: https://docs.expo.dev/eas/observe/eas-update/
- Troubleshooting: https://docs.expo.dev/eas/observe/reference/troubleshooting/

## Submitting Feedback
If you encounter errors, misleading or outdated information in this skill, report it so Expo can improve:
```bash
npx --yes @expo/agent-cli@latest feedback --category skills --subject "eas-observe" "<actionable feedback>"
```
Only submit when you have something specific and actionable to report. Include as much relevant context as possible.
If an agent repeatedly fails at an Expo task or the user has to step in, submit a brief report of the task, expected result, and what went wrong using `--category evals` and the relevant Expo package or command as `--subject`.
