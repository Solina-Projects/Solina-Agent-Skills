---
name: android-engineering
description: Build, debug, test, optimize and maintain Android applications and platform integrations using Kotlin, Java, Jetpack Compose, Gradle and Android SDK tools.
---

# Android Engineering

## Workflow
1. Inspect repository structure, README, Gradle wrapper, module graph, versions, build variants and existing conventions before editing.
2. Identify the user's target Android/API levels, device constraints, architecture and acceptance criteria. Do not silently upgrade dependencies or Gradle.
3. Make the smallest coherent change; preserve existing behavior and project style.
4. Prefer Kotlin, lifecycle-aware APIs, structured concurrency, immutable UI state and modular boundaries where appropriate.
5. For Compose, separate UI from state/business logic, use stable state holders, handle loading/error/empty states and provide accessibility semantics.
6. Add or update unit, instrumented, UI and regression tests appropriate to the change.
7. Run the narrowest relevant checks first, then assemble the requested variant. Report exact commands and results.

<!-- MUSE-ADAPT -->

## Muse adaptation — read first

This skill runs inside Muse's own environment, for Nasser. Where the original instructions below conflict with these points, these points win.

- Host: Linux VM (4 CPU, ~7 GB RAM, x86_64), no GPU. Toolchains live under the home directory only; never rely on system installs. For npm, always set npm_config_cache=/tmp/npm-cache.
- The user (Nasser) is Persian-speaking and phone-only; he has no computer. Deliverables reach him as files in this chat. Explain everything in simple Persian and translate every English label - his English is effectively zero.
- Register: two-way, comfortable, street-style, blunt and honest. No formalities.
- Never ask design-detail questions. Decide, build, then report shortly.
- For Nasser's own work, follow the decisions already recorded in memory (Solina-Player design, Lunaris alioth kernel and ROM, Solina-Launcher).
- UI copy: Persian first, Western (English) digits only, no em dashes in UI copy.
- Apply quality gates silently. Never paste internal gate or lint reports to the user; report outcomes in a few lines.
- Secrets never go into files, memory or chat output. Publishing anything publicly needs his explicit approval first.
- The original skill may name Claude Code tools (Read, Write, Edit, Glob, Grep, Bash) or other agents' commands. Use Muse's own tools instead (file read/write/edit, shell, browser). Use the browser tools for live pages and real-site screenshots.

## Android-specific checks
- Verify manifest permissions, exported components, intent filters, foreground-service types and scoped storage behavior.
- Check lifecycle, configuration changes, process death, background restrictions, battery impact and network failure.
- Inspect minSdk/targetSdk/compileSdk compatibility and Play policy implications.
- Avoid main-thread I/O, leaked contexts, unbounded work and hard-coded secrets.
- For native/JNI or NDK work, inspect ABI filters, toolchain and packaging.

## Delivery
Summarize changed files, design decisions, tests/builds actually run, known limitations and next steps. Never state a build passed unless its output confirms success.
