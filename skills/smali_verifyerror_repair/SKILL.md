---
name: smali_verifyerror_repair
description: "Repair Android smali VerifyError crashes: read the logcat first, treat it as a type error in the smali, trace the register's wrong type to its branch, and fix it there."
---

# Smali VerifyError Repair

## Read the crash first

- Read the logcat lines for the exact method, the register name and the expected type.

- Treat a VerifyError as a type error in the smali, not a logic error in the app.

- Remember that ART rejects the method before any of its code runs, so the app never launches.

- Find the branch where the register holds the wrong type and trace every path that reaches it.

## Place the type fix before the dispatch

- Put the re-parse or type correction at the top of the shared handler, before the first branch that reads the value.

- Check every downstream branch after the fix and confirm each one now sees the corrected type.

- Never place the fix inside one branch when other branches read the same register, because the branches you skip keep the wrong type and crash again.

- When a fix works for one action and a new VerifyError names the same method and register, move the fix earlier instead of adding a second fix in the new branch.

## Verify the fix locally before shipping

- Assemble the full smali tree locally and baksmali round-trip it to confirm the fix is present in the dex.

- Confirm the corrected line sits before the dispatch check in the assembled output, not only in the source file.

- Wait for CI to go green and then run the APK on the real device through the apk-run skill, because CI green does not prove the app launches.

- Call the fix done only after the app opens on the device with no VerifyError in logcat.

## Report what you proved

- Report the method, the register, the wrong type and the right type in plain words.

- Say which launch the user tested and what the screen showed, and never claim the crash is fixed from a CI result alone.

- If the device link is down, say so plainly and name the one step the user takes to reconnect, instead of pretending the run happened.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for pushing the smali fix and reading the CI result.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Prefer fixing the smali source over patching the built dex when the source is available, because a dex patch is lost on the next build.

- When the same method keeps failing, rebuild the handler from the original smali instead of stacking more branches onto the patched one.

- Ask the user for a launch screenshot when logcat is not reachable, because a screenshot shows whether the app opened even when the log is missing.
