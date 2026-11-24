---
name: superpowers-subagent-driven-development
description: Execute an implementation plan by dispatching a fresh subagent per task with a review after each task. Use when you have a written implementation plan with mostly independent tasks and the user chose subagent-driven execution (or the plan is long enough that later tasks would run on a compacted context). Use when each task needs its own implementer and reviewer. Do not use for tightly coupled tasks, or when the user chose inline execution.
---

# Subagent-Driven Development (Superpowers)

Execute the plan by dispatching a fresh implementer subagent per task, a task review (spec compliance + code quality) after each, and a broad whole-branch review at the end.

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
- Reports to Nasser are in simple Persian. Subagent briefs and reports are working documents in English.

## Why subagents

You delegate tasks to specialized agents with isolated context. By precisely crafting their instructions and context, you ensure they stay focused and succeed at their task. They never inherit your session's context or history — you construct exactly what they need. This also preserves your own context for coordination work.

**Core principle:** Fresh subagent per task + task review (spec + quality) + broad final review = high quality, fast iteration.

**Continuous execution:** Do not pause to check in with Nasser between tasks. Execute all tasks from the plan without stopping. "Should I continue?" prompts and progress summaries waste his time — he asked you to execute the plan, so execute it.

**Rulings, not stalls.** A running plan does not wait on a human. Conflicts, ambiguities, plan defects — decide them. The spec is the binding authority, the plan is its argument, and your judgment settles what neither answers. Record every decision in the ledger as `Ruling: <what you decided> — <why> — <what it costs if wrong>`, and keep going. A wrong ruling costs rework he can see and undo; a session parked on a question costs his whole day and buys nothing.

Four things stop you, and only these: an irreversible or destructive operation; a security-sensitive action; a side effect outside this work that norms say you ask about first (a merge, a push to a shared branch, a publish); and a plan so broken that every path forward is a guess. For those, stop and ask.

## When to use

- You have an implementation plan (see planning-and-task-breakdown) and its tasks are mostly independent.
- Nasser chose subagent-driven execution at the plan handoff, or the plan is long enough that later tasks would run on a compacted context.
- You want a review gate on every task, not just at the end.

**Prefer inline execution** (`incremental-implementation`) when Nasser chose it, or when tasks are tightly coupled. Inline costs one context plus one final reviewer; subagent-driven costs a fresh context per task and per review, and buys a fresh pair of eyes per task.

## Setup

- **Branch:** work on a branch, never on main/master without Nasser's explicit consent. For API-only repos (Solina-Files: GitHub API only, never a local clone) create the branch and push commits through the GitHub API / `gh`; for repos with a local clone, use git normally. No git worktrees for this user — his workflow does not use them.
- **Ledger:** conversation memory does not survive compaction. Track progress in a ledger file next to the plan (e.g. `tasks/progress.md`), not only in todos. Its first line names the plan: `# SDD ledger — plan: <plan file path>`. A task with a `Task <N>: complete` line is DONE — do not redo it; resume at the first task without one. After compaction, trust the ledger and the commit log over your own recollection.
- **Read the plan once**, note its context and Global Constraints, create a todo per task. If the plan names a spec, read that too: the spec is the authority the plan argues from, and conflicts inside the plan resolve against it. A plan with no reachable spec gets a ledger note saying so — rulings made without one are provisional.
- **Pre-flight scan:** before Task 1, scan the plan for conflicts between tasks using the Interfaces blocks — for every task that consumes what an earlier task produces, one ledger row (the two tasks, what one produces against what the other consumes, what you found). Rule on each conflict with the spec as the binding authority and record the ruling beside its row.

## The task loop

### 1. Dispatch the implementer

- **Task brief:** write the task's full text to a uniquely named file (e.g. `tasks/briefs/task-N-brief.md`) and put its path in the dispatch. Compose the dispatch so the brief stays the single source of requirements: (1) one line on where this task fits in the project; (2) the brief path — "read this first, it is your requirements, with the exact values to use verbatim"; (3) interfaces and decisions from earlier tasks that the brief cannot know; (4) your resolution of any ambiguity you noticed in the brief; (5) the report-file path and report contract. Exact values (numbers, strings, signatures, test cases) appear only in the brief. Never make a subagent read the whole plan file, and never paste accumulated prior-task summaries into later dispatches — a fresh subagent needs its task, the interfaces it touches, and the global constraints. Nothing else.
- **Report file:** name the implementer's report after the brief (`task-N-report.md`, same directory). The implementer writes the full report there and returns only status, commits, a one-line test summary, and concerns.
- **The implementer never dispatches subagents** — not helpers, never a reviewer. Review arrives from you, after the report.
- Record the base commit before dispatching — the review diff is cut from it, never from `HEAD~1` (which silently drops all but the last commit of a multi-commit task).
- **Never dispatch multiple implementation subagents in parallel** — they would conflict. Parallel dispatch is for independent investigations; see `superpowers-dispatching-parallel-agents`.

### 2. Handle the report

Statuses: DONE, DONE_WITH_CONCERNS, NEEDS_CONTEXT, BLOCKED. If the implementer asks questions — before starting or mid-task — answer clearly and completely, provide additional context if needed, and don't rush it into implementation.

### 3. Review the task

Per-task reviews are task-scoped gates; the broad review happens once, at the end. Never skip the task review, and never accept a report missing either verdict — spec compliance AND task quality are both required. Implementer self-review never replaces the task review.

- Hand the reviewer its diff as a file (produce it with `git diff` or `gh api` for API-only repos, redirected to one uniquely named file). Pass the reviewer three paths — the brief, the report, and the diff — plus the global constraints that bind the task, copied verbatim from the plan.
- Do not add open-ended directives ("check all uses") without a concrete, task-specific reason. Do not ask a reviewer to re-run tests the implementer already ran. Do not pre-judge findings — never instruct a reviewer to ignore or not flag a specific issue.

### 4. The fix loop

Triggers when the review reports spec failure, any Critical or Important finding, or a confirmed gap. Fix in rounds against the same reviewer scope: the implementer fixes, the reviewer re-checks only the fix diff. Cap the rounds (3 is the practical limit); past the cap, rounds don't converge — the failure is structural. Adjudicate: park the finding with a ledger ruling and move on, or route it back to Nasser. Every parked finding gets a ruling line; silent discards are forbidden.

### 5. Complete the task

When the review is clean — or every open finding is parked with a ruling at the cap — append the completion line to the ledger in the same message as your other bookkeeping:

- `Task <N>: complete (commits <base7>..<head7>, review clean)`
- `Task <N>: complete (commits <base7>..<head7>, <K> parked)` after a tripped breaker

Then mark the todo complete and move on. Never move to the next task while the review has open Critical/Important issues that are neither fixed nor parked-with-ruling at the cap.

## Final review

When every task is complete, a fresh reviewer reviews the whole branch against the plan and spec, with the plan's Review Focus section verbatim (the input classes and failure modes the plan's tests do not exercise — the reviewer checks each deliberately) and a pointer to the ledger's `Ruling:` lines. One fix wave for Critical/Important findings, each fix verified by TDD; Minor findings go to the ledger as deferred. Then finish with `git-workflow-and-versioning` (finishing a development branch) — the integration decision is Nasser's.

## Waiting on dispatched subagents

Never poll with short timeouts, and never sit in one silent, open-ended wait either. While you have local work — ledger updates, packaging the next review, reading reports — keep working; child results arrive on their own. When genuinely idle, wait in bounded stretches, and between stretches reconcile your live children: list them, and chase any that finished without reporting.

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "Close enough on spec compliance" | Reviewer found spec gaps = not done. Fix or hit the cap and adjudicate — those are the only exits. |
| "I'll fix it myself, dispatching is overhead" | Controller fixes pollute your context and skip review. Resume the implementer. |
| "One more round will converge" | Past the cap, rounds don't converge — the failure is structural. Adjudicate and route. |
| "This finding is obviously wrong, I'll drop it" | You adjudicate only at the cap, and every ruling is a ledger entry. Silent discards are forbidden. |
| "The fix was small, skip the re-review" | Unreviewed fixes are how regressions land. Every round ends with a scoped re-review. |
| "Reviews slow the loop down" | The loop without reviews is just unverified churn. Reviews are the loop's brakes and steering. |
| "Ledger bookkeeping is overhead" | The ledger is what survives compaction. Controllers without one have re-dispatched entire completed task sequences. |
| "The implementer spawned its own reviewer — free extra assurance" | It's a duplicate seat reviewing the same diff; the task review is the gate. A worker-spawned reviewer is a defect to flag, not rigor. |
