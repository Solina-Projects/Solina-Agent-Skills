#!/usr/bin/env python3
"""Regenerate README.md: full alphabetical list of all skills with their uses.

Reads each skills/*/SKILL.md frontmatter (name, description) with PyYAML,
collapses the description to one line, and writes README.md in place.
Run from the repo root:  python3 scripts/generate_readme.py
"""
from pathlib import Path
import re
import sys

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required (pip install pyyaml)")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, None
    try:
        data = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        print(f"WARNING: {path}: bad frontmatter: {exc}")
        return None, None
    name = (data.get("name") or "").strip()
    desc = (data.get("description") or "").strip()
    return name, desc


def one_line(desc):
    return re.sub(r"\s+", " ", desc).strip()


def main():
    entries = []
    problems = []
    for skill_file in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        folder = skill_file.parent.name
        name, desc = parse_frontmatter(skill_file)
        if not name:
            problems.append(f"{folder}: missing name in frontmatter")
            name = folder
        if name != folder:
            problems.append(f"{folder}: name '{name}' != folder")
        if not desc:
            problems.append(f"{folder}: missing description")
            desc = "(no description yet)"
        entries.append((name, one_line(desc)))
    entries.sort(key=lambda e: e[0])

    lines = []
    lines.append("# Solina Agent Skills")
    lines.append("")
    lines.append('<p align="center">')
    lines.append('  <img src="assets/icon-512.png" alt="Solina Agent Skills icon" width="120" height="120">')
    lines.append("</p>")
    lines.append("")
    lines.append("A practical, security-first skill collection for Android engineering, custom ROMs, device operations, software development, design, GitHub, Google services, browsers, messaging and social platforms.")
    lines.append("")
    lines.append("## Skill layout")
    lines.append("")
    lines.append("All skills use the Agent Skills format: a directory containing a `SKILL.md` with YAML frontmatter (`name`, `description`) and task-specific instructions.")
    lines.append("")
    lines.append("## Workflow")
    lines.append("")
    lines.append("The collection includes a Superpowers-derived workflow discipline (from [obra/superpowers](https://github.com/obra/superpowers)): brainstorm first, write a short plan, implement in small verifiable slices with tests, verify before claiming completion, and review after each task. The two dedicated skills are `superpowers-subagent-driven-development` and `superpowers-dispatching-parallel-agents`; the same discipline is woven into `brainstorming`, `planning-and-task-breakdown`, `incremental-implementation`, `test-driven-development`, `debugging-and-error-recovery`, `verify-live-state`, `code-review-and-quality`, `git-workflow-and-versioning`, `skill-creator` and `using-agent-skills`.")
    lines.append("")
    lines.append(f"**{len(entries)} skills:**")
    lines.append("")
    for name, desc in entries:
        lines.append(f"- `{name}` — {desc}")
    lines.append("")

    (ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote README.md with {len(entries)} skills.")
    for p in problems:
        print(f"WARNING: {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
