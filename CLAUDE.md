# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A Claude Code plugin ("good") containing 12 skills that codify high-impact software development best practices. Each skill is a Markdown file loaded by Claude Code at invocation time to guide an AI agent's behavior for a specific type of task.

## CI Checks

All three must pass on every PR:

```bash
# Validate skill file format
python3 scripts/validate-skills.py

# Validate JSON files
python3 -m json.tool .claude-plugin/plugin.json > /dev/null
python3 -m json.tool .claude-plugin/marketplace.json > /dev/null

# Lint Markdown
npx markdownlint-cli 'skills/**/*.md' '*.md'
```

## Skill File Format

Every skill lives at `skills/<skill-name>/SKILL.md`. The validator enforces:

1. **YAML frontmatter** with exactly these fields:
   - `name`: must match the directory name (e.g. `good-code`)
   - `description`: must start with `"Use when"`
2. **`## Red Flags` section** is required
3. No HTML comments (`<!-- ... -->`)
4. No bare `TBD` anywhere in the file

## Registry Sync

`good-developer/SKILL.md` contains a table listing every other skill via backtick references like `` `good:good-code` ``. The validator (`validate_registry` in `scripts/validate-skills.py`) diffs that table against the actual directories in `skills/`. Adding or removing a skill requires updating both the directory and the `good-developer` table.

## Skill Content Bar

A skill earns its place when: it covers principles that are genuinely high-impact, a developer can read it in 60 seconds and immediately apply it, and an AI agent loading it would make meaningfully better decisions. Avoid exhaustive coverage — each skill stays focused on the highest-impact principles only.
