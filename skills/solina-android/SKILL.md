# Solina Android Development

## Settle the stack and design first

- Build the player with Kotlin and Jetpack Compose and Jetpack Media3 for both music and video.

- Use Material 3 Expressive with dynamic Material You colors from album art and rounded shapes and fluid transitions.

- Keep the interface right to left for Persian and bundle Vazirmatn as a font resource instead of leaving the default type scale in place.

- Add a wave or shimmer loading indicator for empty lists instead of leaving only a text placeholder.

- Treat PixelPlayer as a style reference for colors and animations and loading and settings only and never copy its name or branding into code.

## Build in chat and push to GitHub

- Let the user direct each step while Muse writes the code and pushes it to GitHub and the user does not open Android Studio.

- Resolve the repository and branch before acting and preserve unrelated work on other branches.

- Read the result back after every change and inspect the current state before retrying after a timeout or an uncertain write because the first attempt may have succeeded.

- Keep playback logic unchanged when only the theme changes and put the theme change in its own Theme file with the activity using that theme and a short design note beside it.

- Create design options as separate branches from main with one theme per branch and ask the user to test each APK on their own device before any merge.

- Never merge a design branch into main and never delete the losing branch until the user explicitly says to merge.

## Keep versions aligned

- Keep Kotlin and the Android Gradle Plugin and Gradle and the Compose BOM aligned and change them together when a compiler error points at version drift.

- Use Kotlin 2.2.20 with AGP 8.7.2 and Gradle 8.9 and Compose BOM 2025.10.00 as the known working set for this player.

- Treat a Kotlin internal compiler error in the K2 checker on the permission launcher lambda as a version signal first and check the alignment before rewriting the lambda.

- Verify every version change by re-reading the build files from GitHub after the push.

## Test with Actions and the user device

- Build the debug APK with GitHub Actions and report the run outcome and the commit hash so the user can download the exact APK they tested.

- Remember there is no emulator here and no direct way to list Actions runs so final testing depends on the user device and the user report of what failed.

- Read the Actions log to find whether a failure is resource linking or Kotlin compilation and fix only the stage that failed.

- Remember the GitHub App connection cannot write workflow files and returns 403 so workflow changes go through the browser instead of the API.

- Remember repo creation may need the live browser takeover when the GitHub App and the saved browser login cannot create it.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for code and issues and pull requests in the player and launcher repositories.

- [Figma](/opt/hatch/connectors/figma/CONNECTOR.md) for design context and tokens and assets to implement a supplied design.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [GitHub](https://github.com/) for workflow files and repo creation when the connector lacks that operation. Carry the repository name and branch and exact change into the browser task and verify the file saved there.

## Alternatives for better results

- Prototype a new screen as a mockup first and ask the user to pick a direction before writing production code.

- Ship the core playback flow first and add settings and library polish after the user has a working APK in hand.

- Ask one question when the audience or the next step is unclear and let that answer decide whether to build or to test.
