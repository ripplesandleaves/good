---
name: good-debug
description: Use when encountering a bug, test failure, unexpected behavior, or error — before proposing or attempting any fix
---

# Good Debug

## Iron Law

```
NO FIX WITHOUT ROOT CAUSE FIRST
```

Random fixes waste time and introduce new bugs. A symptom fix is a failure, not a solution.

## The Four Phases

### Phase 1: Understand Before Acting

1. **Read the error completely** — stack traces, line numbers, error codes. They often contain the answer.
2. **Reproduce it** — can you trigger it reliably? If not, gather more data; don't guess.
3. **Check recent changes** — `git log`, `git diff`. What changed that could cause this?
4. **State what you know** — write: "I believe X is happening because Y." If you can't complete this sentence, you need more data.

### Phase 2: Find the Pattern

- Locate working code that does something similar — what's different?
- In multi-component systems, add instrumentation at each boundary before proposing a fix:
  ```
  Component A → [log input here] → Component B → [log output here] → Component C
  ```
  Run once to see where the behavior breaks. Then investigate that component.

### Phase 3: Form and Test One Hypothesis

- One hypothesis at a time: "I think X is the cause because Y"
- Make the **smallest possible change** to test it
- Did it work? → Phase 4. Didn't work? → Form a new hypothesis. **Never stack fixes.**

### Phase 4: Fix and Verify

- Fix the root cause, not the symptom
- Write a test that would have caught this before fixing
- Verify the test was failing before the fix, passes after
- Confirm no other tests broke

**If 3 fixes have failed:** Stop. The architecture may be wrong. Discuss before attempting fix #4.

## Red Flags — STOP and Return to Phase 1

- "Let me just try changing X and see what happens"
- Adding multiple changes at once
- "I don't fully understand why, but this might work"
- Proposing a fix before tracing where the bad value originates
- Each new fix reveals a new problem in a different place (→ architectural issue)

## Quick Reference

| Phase | Key action | Exit condition |
|-------|-----------|----------------|
| Understand | Read error, reproduce, check changes | Can explain what's happening and why |
| Pattern | Find working example, compare | Know what's different |
| Hypothesis | Form theory, test minimally | Hypothesis confirmed or eliminated |
| Fix | Fix root cause, write test, verify | Tests pass, no regressions |
