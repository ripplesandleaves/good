---
name: good-quality
description: Use when defining quality standards, writing tests, setting up CI, planning observability, or deciding what "done" means for a piece of work
---

# Good Quality

## Quality Is Not a Phase

Quality is built in continuously, not tested in at the end.

## Testing

**Test behavior, not implementation.**
- Test what the code *does*, not how it does it — tests that break on refactor are not tests, they're friction
- Every bug gets a test that would have caught it before the fix
- Test at the level that gives the most signal with the least coupling: usually integration > unit > e2e for coverage confidence

**Test design:**
```
Given [preconditions]
When [action]
Then [observable outcome]
```

- One assertion per test where practical; test one behavior per test
- Tests must be deterministic — flaky tests are worse than no tests
- Don't mock what you don't own; prefer real implementations at integration boundaries

**Coverage:** 100% coverage doesn't mean 100% correct. Coverage tells you what's executed, not what's verified. Aim for meaningful coverage of critical paths.

## Code Review

**Review for:** correctness first, then design, then style.

- Read the diff as a change to a living system, not code in isolation
- Ask: does this do what it says? does it break anything? is it safe? is it maintainable?
- Distinguish blocking issues (bugs, security, wrong behavior) from suggestions (style, preference)
- Approve when you'd be comfortable owning the code, not when it's perfect

## CI/CD

- All tests run on every PR — no merging red CI
- Security scanning and dependency audits in the pipeline
- Linting and formatting automated, not manual
- Main branch always deployable

## Observability

- Log events that matter for debugging and ops, not noise
- Structured logs (JSON) with consistent fields: timestamp, level, service, trace ID
- Metrics for SLOs: error rate, latency p95/p99, throughput
- Alerts on symptoms (user impact), not just causes (CPU %)

## Definition of Done

A feature is done when:
- [ ] Tests written and passing
- [ ] CI green
- [ ] Reviewed and approved
- [ ] Logging and error handling appropriate
- [ ] Deployed to staging and smoke tested

## Red Flags
- Merging with failing tests ("I'll fix it in a follow-up")
- Tests added after a bug reaches production
- No observability in a new service
- "Works on my machine" as an acceptance criterion
