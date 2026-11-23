---
name: software-engineering
description: Plan and implement maintainable software changes across languages and platforms, from requirements and architecture through delivery.
---

# Software Engineering

## Understand before coding
Restate the outcome, constraints, non-goals and acceptance tests. Inspect existing code and conventions. Ask one focused question only when a missing decision blocks safe progress.

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

## Design
Choose the simplest architecture that satisfies requirements. Consider module boundaries, API contracts, error handling, concurrency, observability, migration and backwards compatibility. Record trade-offs for consequential decisions.

## Implement
Keep changes cohesive and incremental. Avoid unrelated refactors, speculative abstractions, duplicated logic and hidden behavior changes. Validate untrusted inputs and fail safely.

## Quality
Add tests for expected behavior, edge cases and regressions. Run formatting, lint, type checks, tests and builds available in the environment. Review the diff for secrets, generated artifacts, accidental API changes and license issues.

## Handoff
Report changed files, tests and commands, results, limitations and follow-up work. Separate verified facts from assumptions.
