---
name: good-writing
description: Use when writing commit messages, PR descriptions, comments, documentation, READMEs, ADRs, or any text a developer produces — to communicate clearly and concisely in plain language
---

# Good Writing

## Core Principle

**Plain language. Minimum words. Maximum clarity.**

Say what you mean. Cut everything that doesn't add meaning. Prefer the simple word over the impressive one.

## Universal Rules

| Rule | Example |
|------|---------|
| Active voice | "The function validates input" not "Input is validated by the function" |
| Concrete over abstract | "Returns null" not "May not return a value" |
| Short sentences | One idea per sentence |
| Cut filler | Remove "basically", "simply", "just", "in order to" |
| Reader first | Write for someone reading cold, not someone who wrote the code |

## Comments

**Comment the why, not the what.**
```python
# ❌ Restates code
i += 1  # increment i

# ✅ Explains non-obvious reason
timeout = 31  # Exceeds Stripe's 30s webhook retry window
```

Only comment when:
- The code can't express the intent (a business rule, a workaround, a non-obvious constraint)
- The absence of a comment would surprise a future reader

## Commit Messages

Format: `<type>: <what changed and why in plain English>`

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`

```
# ❌
fix: bug fix

# ✅
fix: prevent double-charging when payment webhook retries

The Stripe webhook can fire twice if our 200 response is delayed.
Idempotency key now stored before processing, not after.
```

- First line ≤72 chars, imperative mood ("add", "fix", "remove")
- Body explains WHY the change was needed, not what changed (the diff shows that)

## READMEs

Structure: What it is → Why use it → How to install → How to use (with example) → How to contribute

- First paragraph: what the project does in one sentence, for someone who has never heard of it
- Working code example in the first screen — don't make people scroll to see how it works
- Keep it current — outdated READMEs damage trust more than no README

## Documentation

- Write for the task the reader is trying to complete, not the architecture you built
- One document, one purpose — don't combine "getting started" with "reference"
- ADRs (Architecture Decision Records): context → decision → consequences. Three sections, always. Short.

## Red Flags
- Jargon without definition (assume nothing)
- Passive voice throughout
- Paragraph-length sentences
- Documentation that describes what to do without showing how
- README that doesn't have a working example
