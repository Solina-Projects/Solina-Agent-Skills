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

## Android-specific checks
- Verify manifest permissions, exported components, intent filters, foreground-service types and scoped storage behavior.
- Check lifecycle, configuration changes, process death, background restrictions, battery impact and network failure.
- Inspect minSdk/targetSdk/compileSdk compatibility and Play policy implications.
- Avoid main-thread I/O, leaked contexts, unbounded work and hard-coded secrets.
- For native/JNI or NDK work, inspect ABI filters, toolchain and packaging.

## Delivery
Summarize changed files, design decisions, tests/builds actually run, known limitations and next steps. Never state a build passed unless its output confirms success.
