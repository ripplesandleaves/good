---
name: good-code
description: Use when writing, reviewing, or refactoring code at the function, module, or file level — to apply high-impact principles for correctness, clarity, and maintainability
---

# Good Code

## Core Principles

**Clarity over cleverness.** Code is read far more than written. Optimize for the next reader.

### Naming
- Names reveal intent: `calculateTax()` not `calc()`, `isExpired` not `flag`
- Avoid abbreviations unless universally understood (`url`, `id`, `http`)
- Boolean names answer yes/no: `isValid`, `hasError`, `canRetry`
- Consistency beats cleverness: pick one term per concept and use it everywhere

### Functions
- **Do one thing.** If you need "and" to describe it, split it.
- Short is good; extractable is better. Extract when it has a name worth having.
- Prefer pure functions (same input → same output, no side effects) where practical
- Return early; avoid deep nesting

```python
# ❌ Nested
def process(user):
    if user:
        if user.active:
            if user.verified:
                return send_email(user)

# ✅ Early return
def process(user):
    if not user or not user.active or not user.verified:
        return
    return send_email(user)
```

### Principles
| Principle | Rule | Common violation |
|-----------|------|-----------------|
| **SRP** | One reason to change | `UserManager` does auth + email + billing |
| **OCP** | Open to extend, closed to modify | Switch on type instead of polymorphism |
| **DRY** | One source of truth | Copy-paste with minor variations |
| **KISS** | Simplest thing that works | Premature abstraction, over-engineering |
| **YAGNI** | Don't build it until you need it | Generic framework for one use case |

### Error Handling
- Validate at system boundaries (user input, external APIs); trust internal code
- Fail fast and explicitly — don't silently swallow errors
- Error messages say what went wrong AND what to do: `"Email required"` not `"Invalid input"`
- Use typed errors/exceptions over error codes where the language supports it

### Abstraction
- Three uses before abstracting (rule of three)
- Inline first; extract when the name adds value
- Abstractions should reduce complexity, not just reduce lines

## Red Flags
- Function longer than fits on one screen without a scroll
- Comment explaining *what* the code does (rename instead)
- Parameter list longer than 3-4 items (use an object/struct)
- `TODO` or `FIXME` committed to main
