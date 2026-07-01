---
name: good-pr
description: Use when preparing to open a pull request — to verify the branch is ready, write a description reviewers can act on, and communicate clearly what changed and why
---

# Good PR

## Before You Open the PR

A PR is a request for someone else's time. Respect it.

**Readiness checklist:**
- [ ] All tests pass locally
- [ ] CI is green (or you know why it's red and it's unrelated)
- [ ] No debug code, commented-out code, or TODOs you don't intend to ship
- [ ] Scope is appropriate — one logical change per PR
- [ ] You've read your own diff (caught at least one thing you wanted to change)
- [ ] New or changed behavior has tests

**Scope:** A PR that does one thing is reviewed faster and merged sooner than one that does five. If you find yourself writing "also..." in the description, consider splitting.

## Writing the Description

**The reviewer is starting cold.** They don't have your context. Give it to them.

### Required sections:

**What this does** — one to three sentences, in plain language. What is the user/system behavior change? Not what files changed.
```
This adds rate limiting to the public API. Unauthenticated requests are now capped at 100/hour per IP.
```

**Why this change** — the motivation, business reason, or bug being fixed. What happens without this change?
```
Without this, the endpoint is vulnerable to abuse. We've seen bots hitting it ~2000 times/minute.
```

**How it works** — only if non-obvious. Implementation details that help the reviewer understand the approach.
```
Uses a sliding window counter in Redis with a 1-hour TTL. Key is `rate:{ip}`. Returns 429 with a Retry-After header when exceeded.
```

**Testing** — what did you do to verify this works? How can the reviewer verify it?
```
Unit tests cover the counter logic. Integration test covers the 429 response. Tested manually with `ab -n 200 /api/resource`.
```

### Optional but high-value:
- Screenshots for UI changes
- Link to the issue, ticket, or context that motivated this
- Known limitations or follow-up work

## Describing Decisions

If you made a non-obvious choice, say so and explain why. This saves review rounds.
```
I chose Redis over an in-memory store because we run multiple instances — in-memory counters wouldn't be shared. If Redis is unavailable, we fail open (allow the request) rather than blocking all traffic.
```

Reviewers can disagree with your decision; they can't engage with a decision they don't know was made.

## After Opening

- Respond to every comment, even if just to say "done" or "I've thought about it and I think the current approach is better because X"
- Don't silently push changes — note what you changed in response to feedback
- If a review conversation is going in circles, move it to a call

## Red Flags
- PR title is the branch name
- Description is empty or says "see ticket"
- 1000-line diff with one sentence of context
- "LGTM" from a reviewer with no comments on a complex change
- PR open for weeks without a merge or a close
