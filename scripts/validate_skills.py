#!/usr/bin/env python3
"""Validate Agent Skills directories and SKILL.md frontmatter."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

def fail(message):
    print(f"ERROR: {message}")
    return False

def main():
    ok = True
    if not SKILLS.is_dir():
        print("No .agents/skills directory found")
        return 1
    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    if not skill_files:
        print("No SKILL.md files found")
        return 1

    seen = set()
    for path in skill_files:
        folder = path.parent.name
        content = path.read_text(encoding="utf-8")
        if not content.startswith("---\n"):
            ok &= fail(f"{path.relative_to(ROOT)}: missing YAML frontmatter opening")
            continue
        parts = content.split("---", 2)
        if len(parts) < 3:
            ok &= fail(f"{path.relative_to(ROOT)}: malformed YAML frontmatter")
            continue
        front = parts[1]
        name = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", front)
        desc = re.search(r"(?m)^description:\s*(.+)$", front)
        if not name:
            ok &= fail(f"{path.relative_to(ROOT)}: missing/invalid name")
            continue
        if not desc or len(desc.group(1).strip()) < 20:
            ok &= fail(f"{path.relative_to(ROOT)}: missing or too-short description")
        skill_name = name.group(1)
        if not NAME_RE.fullmatch(skill_name):
            ok &= fail(f"{path.relative_to(ROOT)}: name must be lowercase kebab-case")
        if skill_name != folder:
            ok &= fail(f"{path.relative_to(ROOT)}: name '{skill_name}' must match folder '{folder}'")
        if skill_name in seen:
            ok &= fail(f"duplicate skill name: {skill_name}")
        seen.add(skill_name)
        if len(content.strip()) < 120:
            ok &= fail(f"{path.relative_to(ROOT)}: skill content is too short")
    if ok:
        print(f"Validated {len(skill_files)} skills successfully.")
        return 0
    return 1

if __name__ == "__main__":
    sys.exit(main())
