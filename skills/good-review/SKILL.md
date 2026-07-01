---
name: good-review
description: Use when reviewing a code change, diff, or pull request — to give thorough, actionable, and constructive feedback
---

# Good Review

## Purpose of a Review

Find problems before they reach production. Improve the code. Strengthen the team. In that order.

## Review Order

Review from outermost to innermost:

1. **Does this solve the right problem?** Does the change match the stated goal?
2. **Correctness** — does it do what it says? Are there bugs, edge cases, or error paths missed?
3. **Security** — check against `good:good-security`: injection, auth, secrets, data exposure
4. **Design** — check against `good:good-architecture`: boundaries, dependencies, coupling
5. **Quality** — check against `good:good-quality`: tests present and meaningful, CI green
6. **Code clarity** — check against `good:good-code`: naming, function size, abstractions
7. **Communication** — check against `good:good-writing`: comments, docs, PR description

## Feedback That Helps

**Be specific.** Vague feedback creates work without direction.
```
❌ "This could be better"
✅ "This function handles three different responsibilities — consider extracting the validation into its own function so each part is testable independently"
```

**Separate severity.** Make it clear what must change vs. what's a suggestion.
- **Must fix:** bug, security issue, incorrect behavior, broken test
- **Should fix:** design smell, missing test for a non-trivial path
- **Suggestion:** style, preference, "I would have done it this way"

**Be kind.** You're reviewing code, not judging a person. Assume good intent and competence.
```
❌ "Why would you do it this way?"
✅ "I wonder if [alternative] might handle the empty case more explicitly — thoughts?"
```

**Explain the why.** A finding without reasoning creates cargo-culting, not learning.

## What to Look For

| Area | Key questions |
|------|--------------|
| Logic | Does the algorithm handle all inputs correctly? What happens at boundaries? |
| Error handling | What happens when things fail? Are errors surfaced or swallowed? |
| Security | Does this handle untrusted input safely? Any secrets exposed? |
| Tests | Is the behavior tested, not just the implementation? Do tests cover the non-trivial paths? |
| Performance | Any N+1 queries, unbounded loops, or memory issues in hot paths? |
| Dependencies | Are new dependencies justified? Are they trusted and maintained? |

## Approving

Approve when you'd be comfortable owning the code — not when it's perfect. Perfect is the enemy of shipped.

If you have only suggestions (no blocking issues), approve with suggestions and let the author decide.

## Red Flags in a Review
- Approving without reading the tests
- Blocking on style preferences without a linter rule to enforce them
- Feedback that only says what's wrong, not what to do
- Reviewing only the happy path
