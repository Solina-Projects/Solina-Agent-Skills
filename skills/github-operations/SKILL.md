---
name: github-operations
description: Manage GitHub repositories, branches, files, commits, issues, pull requests, reviews, releases and Actions using an authorized GitHub connection.
---

# GitHub Operations

## Inspect first
Confirm owner/repository, default branch, visibility, permissions, current branch head, working tree and relevant workflows. Read project instructions and contribution rules.

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

## Safe change workflow
- Prefer a feature branch for non-trivial work; never force-push or rewrite history unless explicitly requested.
- Make minimal, reviewable commits with clear messages.
- Preserve existing files and use current blob SHA when updating.
- Inspect diffs before opening PRs. Include purpose, implementation, tests, risks and screenshots where relevant.
- Do not merge, publish a release, change repository visibility, delete branches or alter access without explicit authorization.

## Actions and secrets
Use least-privilege workflow permissions, pin third-party actions to verified commit SHAs where practical, avoid printing secrets and use GitHub Secrets/Environments. Never commit tokens, keystores, signing keys or credentials.

## Communication
Report exact repository, branch, commit/PR links, files changed and verified CI status. A successful API call is not proof that downstream CI or a release succeeded.
