#!/usr/bin/env python3
"""Validate skill files against the format spec in CONTRIBUTING.md."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
SKILLS_ROOT = ROOT / "skills"


def parse_frontmatter(content):
    """Return (fields_dict, body) or (None, content) if no valid frontmatter found."""
    if not content.startswith("---\n"):
        return None, content
    end = content.find("\n---\n", 4)
    if end == -1:
        return None, content
    frontmatter_text = content[4:end]
    body = content[end + 5:]
    fields = {}
    for line in frontmatter_text.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields, body


def validate_skill(skill_dir):
    errors = []
    skill_file = skill_dir / "SKILL.md"

    if not skill_file.exists():
        return [f"{skill_dir.name}: missing SKILL.md"]

    content = skill_file.read_text(encoding="utf-8")
    frontmatter, _ = parse_frontmatter(content)

    if frontmatter is None:
        errors.append(f"{skill_dir.name}: missing or malformed YAML frontmatter")
        return errors

    if "name" not in frontmatter:
        errors.append(f"{skill_dir.name}: frontmatter missing 'name' field")
    elif frontmatter["name"] != skill_dir.name:
        errors.append(
            f"{skill_dir.name}: frontmatter name '{frontmatter['name']}' "
            f"does not match directory name '{skill_dir.name}'"
        )

    if "description" not in frontmatter:
        errors.append(f"{skill_dir.name}: frontmatter missing 'description' field")
    elif not frontmatter["description"].startswith("Use when"):
        errors.append(
            f"{skill_dir.name}: description must start with 'Use when' "
            f"(got: '{frontmatter['description'][:60]}')"
        )

    if "## Red Flags" not in content:
        errors.append(f"{skill_dir.name}: missing required '## Red Flags' section")

    if re.search(r"<!--", content):
        errors.append(
            f"{skill_dir.name}: contains HTML comment — remove draft placeholders before merging"
        )

    if re.search(r"\bTBD\b", content):
        errors.append(
            f"{skill_dir.name}: contains 'TBD' — fill in or remove before merging"
        )

    return errors


def validate_registry(skill_dirs):
    """Check that good-developer's table and skill directories are in sync."""
    errors = []
    good_dev_file = SKILLS_ROOT / "good-developer" / "SKILL.md"
    if not good_dev_file.exists():
        errors.append("good-developer/SKILL.md not found")
        return errors

    content = good_dev_file.read_text(encoding="utf-8")
    listed = set(re.findall(r"`good:(good-[^`]+)`", content))
    actual = {d.name for d in skill_dirs if d.name != "good-developer"}

    for skill in sorted(listed - actual):
        errors.append(
            f"good-developer/SKILL.md references '{skill}' but no such directory exists"
        )
    for skill in sorted(actual - listed):
        errors.append(
            f"skill '{skill}' exists but is not listed in good-developer/SKILL.md"
        )

    return errors


def main():
    if not SKILLS_ROOT.is_dir():
        print(f"ERROR: skills/ directory not found at {SKILLS_ROOT}", file=sys.stderr)
        return 1

    skill_dirs = sorted(d for d in SKILLS_ROOT.iterdir() if d.is_dir())
    errors = []

    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    errors.extend(validate_registry(skill_dirs))

    if errors:
        print("Skill validation failed:\n")
        for error in errors:
            print(f"  ✗ {error}")
        print(f"\n{len(errors)} error(s) found.")
        return 1

    print(f"✓ {len(skill_dirs)} skills validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
