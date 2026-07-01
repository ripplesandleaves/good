---
name: good-fix
description: Use when fixing a bug, from the moment "something is broken" through to confirmed resolution and prevention of recurrence
---

# Good Fix

## The Minimal Complete Fix

**The right fix is the smallest change that fully resolves the root cause — no more, no less.**

A fix that is too small leaves the bug; a fix that is too large introduces new risk. Find the precise incision point and change only what must change.

## Full Fix Lifecycle

### 1. Diagnose First
Use `good:good-debug` before writing a single line of fix code. Do not skip diagnosis because the fix "seems obvious." Obvious fixes for misunderstood bugs create new bugs.

### 2. Write the Failing Test
Before touching the broken code, write a test that:
- Reproduces the bug reliably
- Fails now (verify it fails)
- Will pass when the bug is fixed

This is the contract that proves the fix works.

### 3. Apply the Minimal Fix

**Minimal means:**
- Change only what is necessary to make the failing test pass
- Don't refactor, clean up, or improve adjacent code in the same change
- Don't fix hypothetical similar bugs that aren't confirmed broken

**Complete means:**
- The root cause is addressed, not just the symptom
- The fix holds under the same conditions that triggered the original bug
- Edge cases of the same root cause are considered (add tests if uncertain)

```python
# Bug: function crashes when list is empty
# ❌ Symptom fix — hides the error
try:
    return items[0]
except IndexError:
    return None

# ✅ Root cause fix — handle the empty case explicitly
if not items:
    return None
return items[0]
```

### 4. Verify
- Failing test now passes
- All other tests still pass (no regression)
- Fix works in the actual environment, not just in tests

### 5. Prevent Recurrence
- Is this bug possible elsewhere? Add tests or a lint rule.
- Was this bug caught late because of a gap in test coverage? Add the missing coverage.
- If the bug reached production: add a monitoring alert for the symptom.

## Hotfix / Under Pressure

When speed matters:
1. **Smallest safe change** — the change that stops the bleeding with minimum blast radius
2. **Ship, then follow up** — the hotfix buys time for the correct fix
3. **Open a follow-up immediately** — don't let the hotfix become permanent
4. **Communicate** — what failed, what the temporary fix does, what the permanent fix will be

Do not skip diagnosis under pressure. Guessing under pressure is how outages get extended.

## Quality Gates
Align fix with `good:good-code` — a fix that introduces its own smell is a liability.
Align fix with `good:good-security` — security fixes must be reviewed against the checklist.
Align fix with `good:good-quality` — run the verification suite and confirm the fix holds under real conditions.

## Red Flags
- Fix committed without a test
- "I'll write the test later"
- Fixing symptoms in 3+ places (root cause likely elsewhere)
- Hotfix left in place for more than a sprint
- "I'm not sure why this works, but it does"
