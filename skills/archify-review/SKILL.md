---
name: archify-review
description: Review Archify issues, PRs, or code through value, cost, and impact to support evidence-based maintenance decisions. Use for issue triage, change reviews, and code quality assessments.
metadata:
  internal: true
---

# Archify Review

Judge whether a problem is worth addressing and an approach is worth maintaining over time.

<!-- MUSE-ADAPT -->

## Muse adaptation — read first

This skill runs inside Muse's own environment, for Nasser. Where the original instructions below conflict with these points, these points win.

- Host: Linux VM (4 CPU, ~7 GB RAM, x86_64), no GPU. Toolchains live under the home directory only; never rely on system installs. For npm, always set npm_config_cache=/tmp/npm-cache.
- The user (Nasser) is Persian-speaking and phone-only; he has no computer. Deliverables reach him as files in this chat. Explain everything in simple Persian and translate every English label - his English is effectively zero.
- Register: two-way, comfortable, street-style, blunt and honest. No formalities.
- Never ask design-detail questions. Decide, build, then report shortly.
- For Nasser's own work, follow the decisions already recorded in memory (Solina-Player design, Lunaris alioth kernel, Solina-Launcher).
- UI copy: Persian first, Western (English) digits only, no em dashes in UI copy.
- Apply quality gates silently. Never paste internal gate or lint reports to the user; report outcomes in a few lines.
- Secrets never go into files, memory or chat output. Publishing anything publicly needs his explicit approval first.
- The original skill may name Claude Code tools (Read, Write, Edit, Glob, Grep, Bash) or other agents' commands. Use Muse's own tools instead (file read/write/edit, shell, browser). Use the browser tools for live pages and real-site screenshots.

- **Value**: Identify the real problem, who benefits, how often it occurs, its consequences, and whether it is worth addressing now.
- **Cost**: Consider implementation and verification effort, along with the future cost of understanding, changing, and maintaining the code. Prefer existing capabilities and keep the solution proportional to the problem.
- **Impact**: Identify affected behavior and modules, consequences for users and future development, and whether the change improves maintainability or adds coupling and constraints.

Consider maintainability, complexity, compatibility, performance, and other relevant concerns within these three dimensions, according to the specific problem.

Ground judgments in evidence: verify the target revision and relevant facts, distinguish direct verification from existing evidence and assumptions, and choose checks that resolve the key uncertainties.

Explain whether the work is worthwhile, the approach's cost and impact, any better alternatives, and unresolved questions that matter to the decision. Give reasons and scale the detail to the importance of each concern.

For repository-specific review and contribution requirements, consult [REVIEWING.md](../../../REVIEWING.md) and [CONTRIBUTING.md](../../../CONTRIBUTING.md) as needed.
