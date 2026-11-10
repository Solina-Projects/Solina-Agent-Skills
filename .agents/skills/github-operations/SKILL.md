---
name: github-operations
description: Manage GitHub repositories, branches, files, commits, issues, pull requests, reviews, releases and Actions using an authorized GitHub connection.
---

# GitHub Operations

## Inspect first
Confirm owner/repository, default branch, visibility, permissions, current branch head, working tree and relevant workflows. Read project instructions and contribution rules.

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
