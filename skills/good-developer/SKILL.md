---
name: good-developer
description: Use when you want to apply the full Good plugin developer toolkit — loads all good plugin skills for writing, designing, securing, planning, reviewing, and debugging software
---

# Good Developer

Load the complete Good plugin developer toolkit for this session.

## Skills Loaded

By invoking this skill you are committing to apply all of the following Good plugin skills throughout your work:

| Skill | Applies when |
|-------|-------------|
| `good:good-requirements` | Before designing or building — surface what is actually needed |
| `good:good-plan` | Before implementing — design the approach and decompose the work |
| `good:good-architecture` | Designing systems, boundaries, and dependencies |
| `good:good-code` | Writing or reviewing code at the function/module level |
| `good:good-security` | Handling input, auth, secrets, data, or external integrations |
| `good:good-quality` | Testing, CI, observability, or defining done |
| `good:good-debug` | Encountering a bug, failure, or unexpected behavior |
| `good:good-fix` | Fixing a bug from diagnosis through to verified resolution |
| `good:good-review` | Reviewing a code change or pull request |
| `good:good-pr` | Preparing or writing a pull request |
| `good:good-writing` | Writing commit messages, comments, docs, or any developer text |
| `good:good-sweep` | Auditing an existing codebase for security and robustness issues to fix proactively |

## How to Use

Invoke once at the start of a session or task. The skills remain active for the duration of your work. You do not need to invoke them individually.

When the situation calls for one of the skills above, apply its principles as if you had loaded it directly. Use the skill names in this table to guide you to the right principles for the task at hand.

## The Standard

These skills together define what "good" looks like for software development:

- Requirements are clear and testable before work begins
- Plans are explicit and decomposed before code is written
- Architecture has clean boundaries and an intentional dependency direction
- Code is readable, focused, and avoids premature abstraction
- Security is built in, not bolted on
- Quality is maintained by tests, review, and observability — not hope
- Bugs are diagnosed to root cause before any fix is attempted
- Fixes are minimal, complete, and verified
- Reviews are thorough, professional, and actionable
- PRs are clear, scoped, and respectful of reviewers' time
- All writing is plain, concise, and reader-first

## Red Flags

- Implementing before `good:good-requirements` has surfaced what's actually needed
- Writing code before `good:good-plan` has made the approach explicit
- Applying a fix without `good:good-debug` having found the root cause
- Merging without `good:good-review` having checked correctness, security, and design
- Opening a PR without reading your own diff and running the `good:good-pr` checklist
