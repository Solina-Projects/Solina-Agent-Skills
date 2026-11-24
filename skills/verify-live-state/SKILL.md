---
name: verify-live-state
description: "Verify live state before claiming it: run the live check for the exact state first, correct the first reading openly, and report only what was actually checked. Also the verification-before-completion gate: no completion claim without fresh verification evidence."
---

# Verify live state before claiming it

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


## Run the live check first

- Run the live test for the exact state you will claim before you report it or act on it.

- Read the account identity shown in the console or session before you act in that session and stop when it does not match the intended account.

- Treat a panel indicator, a cached page, an earlier message or a first probe as a hint only until a live test confirms it.

## Correct the first reading openly

- State the correction in the same reply when a live test contradicts your first reading and name what changed and what the new evidence shows.

- Keep the corrected claim narrow to what the live test actually covered and do not extend it to related ports, accounts, quotas or credits.

- Re-run the live check after a fix instead of assuming the fix worked.

## Present only what you checked

- Report the method and the scope of the check in plain terms so the reader can see which port, account field, quota page or credit listing was actually checked.

- Say what remains untested when a live check could not run and do not claim that state.

- Ask for a live confirmation from the user when the browser session cannot show the identity field or the test result.

## Verification gate for work claims (from obra/superpowers verification-before-completion)

The same evidence-before-claims rule governs code work, not just live state:

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

Before claiming any status or expressing satisfaction:

1. **IDENTIFY:** what command proves this claim?
2. **RUN:** execute the FULL command, fresh and complete.
3. **READ:** the full output — check the exit code, count the failures.
4. **VERIFY:** does the output confirm the claim? If no, state the actual status with evidence. If yes, state the claim WITH the evidence.
5. **ONLY THEN:** make the claim. Skipping any step is lying, not verifying.

| Claim | Requires | Not sufficient |
|-------|----------|----------------|
| Tests pass | Test command output: 0 failures | A previous run, "should pass" |
| Linter clean | Linter output: 0 errors | A partial check, extrapolation |
| Build succeeds | Build command: exit 0 | Linter passing, logs look good |
| Bug fixed | Test of the original symptom: passes | Code changed, assumed fixed |
| Regression test works | Red-green cycle verified | Test passes once |
| Agent completed | Diff shows the changes | Agent reports "success" |
| Requirements met | Line-by-line checklist | Tests passing |

Red flags — stop: using "should", "probably", "seems to"; expressing satisfaction before verification ("Great!", "Done!"); committing, pushing or creating a PR without verification; trusting an agent's success report; relying on partial verification; thinking "just this once". This applies to exact phrases, paraphrases, synonyms, and any wording implying success without having run verification.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Ask the user for a screenshot of the live console state when you cannot read the identity field yourself.

- Check the same state from a second independent read when the first read and the live test disagree.
