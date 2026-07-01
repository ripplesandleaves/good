---
name: good-plan
description: Use when about to implement any non-trivial feature or change — to think through approach, decompose the work, and produce a plan an engineer can execute without ambiguity
---

# Good Plan

## Plan Before You Build

**A plan is the cheapest place to find mistakes.** Change a plan in 5 minutes; change running code in hours.

## Two Levels of Planning

### Level 1: Technical Design (What and How)
Before decomposing tasks, answer:
1. **What is being built?** One sentence, in terms of user/system behavior
2. **What are the constraints?** Performance, security, compatibility, regulations (→ `good:good-requirements`)
3. **What approaches are possible?** List 2–3 options with tradeoffs
4. **Which approach and why?** Explicit decision with reasoning
5. **What are the risks?** What could go wrong, and how will you handle it?

Document the decision as an ADR (Architecture Decision Record):
- **Context:** why is this decision being made?
- **Decision:** what was chosen?
- **Consequences:** what does this enable, what does it constrain?

### Level 2: Implementation Plan (Tasks)

**File structure first:** map which files will be created or modified and what each is responsible for. This is where decomposition decisions get locked in. See `good:good-architecture` for boundary principles.

**Task sizing:** each task should be:
- The smallest unit that has its own test cycle
- Independently commit-able
- Independently review-able
- Clear enough that someone can pick it up cold

**Task structure:**
```
### Task N: [Name]
Files: [created/modified]
- [ ] Write failing test
- [ ] Run test — verify it fails
- [ ] Implement minimal code to pass
- [ ] Run test — verify it passes
- [ ] Commit
```

**TDD by default:** write the failing test first. Tests written after the fact verify the implementation you built, not the behavior you intended.

## Scope Control

**YAGNI is a planning discipline.** Every requirement must be traceable to a real need. At planning time, cut:
- Features not in the requirements
- Abstractions with only one current use
- Infrastructure for scale you don't have
- Options and configurability nobody asked for

If you find yourself planning for hypothetical future requirements, stop and ask: "Is this in scope?"

## Plan Quality Check

Before handing off a plan, verify:
- [ ] Every task produces a working, testable deliverable
- [ ] No task depends on another that hasn't been defined
- [ ] Every file path is exact and complete
- [ ] Every code example is complete — no "fill in here"
- [ ] No placeholders, no "TBD", no "similar to above"
- [ ] Security and quality requirements from `good:good-security` and `good:good-quality` are represented

## Red Flags
- "We'll figure it out as we go"
- Tasks that have no test
- File paths that say "somewhere in the codebase"
- No decision rationale documented
- Plan written by someone who won't implement it, without review from someone who will
