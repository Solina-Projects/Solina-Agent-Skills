---
name: superpowers-dispatching-parallel-agents
description: Dispatch parallel subagents for independent work. Use when facing 2+ independent tasks, failures, or investigations that can proceed without shared state or sequential dependencies. Use when multiple subsystems broke independently or several test files fail with different root causes. Do not use when failures are related, when agents would edit the same files, or when understanding needs the full system state.
---

# Dispatching Parallel Agents (Superpowers)

You delegate tasks to specialized agents with isolated context. By precisely crafting their instructions and context, you ensure they stay focused and succeed at their task. They never inherit your session's context or history — you construct exactly what they need. This also preserves your own context for coordination work.

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

**Core principle:** Dispatch one agent per independent problem domain. Let them work concurrently.

## When to use

- 3+ test files failing with different root causes
- Multiple subsystems broken independently
- Each problem can be understood without context from others
- No shared state between investigations

**Don't use when:**
- Failures are related (fix one might fix others) — investigate together first
- Understanding needs the full system state
- Agents would interfere with each other (editing the same files, using the same resources)
- The debugging is exploratory — you don't know what's broken yet

## The pattern

### 1. Identify independent domains

Group failures by what's broken. Each domain is independent — fixing one doesn't affect the others. If fixing one might fix another, they are one domain, not two.

### 2. Create focused agent tasks

Each agent gets:
- **Specific scope:** one test file, one subsystem, one failure domain
- **Clear goal:** make these tests pass / find the root cause
- **Constraints:** don't change other code, don't touch files outside the domain
- **Expected output:** summary of what it found and fixed

### 3. Dispatch in parallel

Issue all subagent dispatches in the same response — they run in parallel. Multiple dispatches in one response = parallel execution. One per response = sequential.

### 4. Review and integrate

When agents return:
- Read each summary and understand what changed
- Check for conflicts — did agents edit the same code?
- Run the full test suite to verify all fixes work together
- Spot-check — agents can make systematic errors

## Agent prompt structure

Good agent prompts are focused, self-contained, and specific about output:

```markdown
Fix the 3 failing tests in src/agents/agent-tool-abort.test.ts:

1. "should abort tool with partial output capture" - expects 'interrupted at' in message
2. "should handle mixed completed and aborted tools" - fast tool aborted instead of completed
3. "should properly track pendingToolCount" - expects 3 results but gets 0

These are timing/race condition issues. Your task:

1. Read the test file and understand what each test verifies
2. Identify the root cause - timing issues or actual bugs?
3. Fix by:
   - Replacing arbitrary timeouts with event-based waiting
   - Fixing bugs in abort implementation if found
   - Adjusting test expectations if testing changed behavior

Do NOT just increase timeouts - find the real issue.

Return: Summary of what you found and what you fixed.
```

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Too broad: "Fix all the tests" | Specific: "Fix agent-tool-abort.test.ts" — one focused scope |
| No context: "Fix the race condition" | Paste the error messages and test names |
| No constraints | "Do NOT change production code" or "Fix tests only" |
| Vague output: "Fix it" | Specific: "Return summary of root cause and changes" |

## Verification

After agents return:
- [ ] Each summary read and understood
- [ ] No two agents edited the same code
- [ ] Full test suite run — all fixes work together
- [ ] Spot-checked at least one fix per agent
