# Good Plugin Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the `good` plugin — an open-source Claude Code plugin providing 11 skills that codify high-impact software development best practices, distributed as a self-contained marketplace repository.

**Architecture:** Each skill lives in `skills/<skill-name>/SKILL.md` with YAML frontmatter. The repo is both the plugin and a marketplace, letting users add the GitHub URL as a marketplace source and install the `good` plugin from it. Skills are self-contained and reference each other within the plugin but have no external dependencies.

**Tech Stack:** Markdown, YAML frontmatter (plugin format), git, GitHub (hosting), Apache v2 license.

## Global Constraints

- License: Apache v2 — include header reference in README
- Plugin name: `good`
- Skill names: `good-code`, `good-architecture`, `good-security`, `good-quality`, `good-writing`, `good-debug`, `good-fix`, `good-requirements`, `good-plan`, `good-review`, `good-pr`
- Skill triggers: named as `/good-<name>` when invoked
- Each skill: focused on highest-impact principles only — not exhaustive
- Skills must be readable by humans at a glance AND token-efficient for AI
- Skills may cross-reference each other using `good:<skill-name>` format
- Skills must NOT depend on skills outside the good plugin
- Marketplace format: `.claude-plugin/marketplace.json` + `.claude-plugin/plugin.json`

---

### Task 1: Plugin Scaffold

**Files:**
- Create: `.claude-plugin/plugin.json`
- Create: `.claude-plugin/marketplace.json`

**Interfaces:**
- Produces: Plugin manifest and marketplace manifest that Claude Code can read to install the good plugin

- [ ] **Step 1: Create `.claude-plugin/` directory and `plugin.json`**

```json
{
  "name": "good",
  "description": "High-impact software development best practices — 11 skills covering code, architecture, security, quality, writing, debugging, fixing, requirements, planning, review, and PRs.",
  "version": "1.0.0",
  "author": {
    "name": "Andrea Ross",
    "email": "andrea@ripplesandleaves.ca"
  },
  "homepage": "https://github.com/andreaross/good",
  "repository": "https://github.com/andreaross/good",
  "license": "Apache-2.0",
  "keywords": [
    "best-practices",
    "code-quality",
    "architecture",
    "security",
    "debugging",
    "skills"
  ]
}
```

- [ ] **Step 2: Create `.claude-plugin/marketplace.json`**

```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "good",
  "description": "High-impact software development best practices for Claude Code",
  "owner": {
    "name": "Andrea Ross",
    "email": "andrea@ripplesandleaves.ca"
  },
  "plugins": [
    {
      "name": "good",
      "description": "11 skills codifying high-impact software development best practices: code, architecture, security, quality, writing, debugging, fixing, requirements, planning, review, and PRs.",
      "author": {
        "name": "Andrea Ross",
        "email": "andrea@ripplesandleaves.ca"
      },
      "category": "development",
      "source": "./"
    }
  ]
}
```

- [ ] **Step 3: Commit**

```bash
git add .claude-plugin/plugin.json .claude-plugin/marketplace.json
git commit -m "feat: add plugin and marketplace manifests"
```

---

### Task 2: good-code skill

**Files:**
- Create: `skills/good-code/SKILL.md`

**Interfaces:**
- Consumed by: `good-fix`, `good-review`
- Produces: Principles for writing clean, correct, maintainable code

- [ ] **Step 1: Create `skills/good-code/SKILL.md`**

```markdown
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
```

- [ ] **Step 2: Commit**

```bash
git add skills/good-code/SKILL.md
git commit -m "feat: add good-code skill"
```

---

### Task 3: good-architecture skill

**Files:**
- Create: `skills/good-architecture/SKILL.md`

**Interfaces:**
- Consumed by: `good-fix`, `good-review`, `good-plan`
- Produces: Principles for decomposing systems, defining boundaries, managing dependencies

- [ ] **Step 1: Create `skills/good-architecture/SKILL.md`**

```markdown
---
name: good-architecture
description: Use when designing systems, choosing component boundaries, deciding dependency direction, or evaluating whether a system structure is sound
---

# Good Architecture

## Core Principle

**Architecture is about what's hard to change.** Make the right things easy to change, and the wrong things hard to do by accident.

## System Decomposition

Split systems by **responsibility**, not by technical layer.

- Each component answers clearly: what does it do, how do you use it, what does it depend on?
- Components communicate through **well-defined interfaces** — change the internals without breaking consumers
- **Bounded contexts:** name things consistently within a boundary; translate explicitly at boundaries
- Prefer many small components over few large ones — large components are a signal of mixed concerns

**Monolith vs services:** Start with a monolith. Extract services when you have clear, stable boundaries AND a real operational reason (scale, deployment independence, team autonomy). Never as the first move.

## Dependency Direction

```
UI → Application → Domain ← Infrastructure
```

- Domain (core business logic) depends on nothing external
- Application orchestrates; domain decides
- Infrastructure (DB, HTTP, queues) implements interfaces defined by the domain
- Dependencies point inward, never outward

**The test:** can you run domain logic tests with no database, no HTTP, no filesystem? If not, the boundaries are wrong.

## Data Flow & State

- Prefer **immutable data** flowing through the system over shared mutable state
- Locate state as close to where it's used as possible
- Avoid global state; make dependencies explicit
- One source of truth per piece of data — duplication creates sync bugs

## Key Decisions (When Architecture Matters Most)

| Decision | Ask first |
|----------|-----------|
| Adding a service | Do we have a stable boundary AND operational need? |
| Shared database | Can we afford tight coupling between these components? |
| New abstraction | Does this reduce complexity or just add indirection? |
| Caching layer | Have we profiled? Is the source of truth still authoritative? |

## Red Flags
- Circular dependencies between components
- Components that know too much about each other's internals
- "God object" — one class/module that does everything
- Database as integration point between services
- Architecture chosen for résumé, not requirements
```

- [ ] **Step 2: Commit**

```bash
git add skills/good-architecture/SKILL.md
git commit -m "feat: add good-architecture skill"
```

---

### Task 4: good-security skill

**Files:**
- Create: `skills/good-security/SKILL.md`

**Interfaces:**
- Consumed by: `good-fix`, `good-review`, `good-requirements`
- Produces: Security principles and top developer-caused vulnerability patterns

- [ ] **Step 1: Create `skills/good-security/SKILL.md`**

```markdown
---
name: good-security
description: Use when writing code that handles user input, authentication, authorization, secrets, data storage, or external integrations — to apply security principles and avoid common developer-introduced vulnerabilities
---

# Good Security

## Core Principles

| Principle | What it means |
|-----------|---------------|
| **Defense in depth** | Multiple independent layers — no single point of failure |
| **Least privilege** | Grant the minimum access needed, nothing more |
| **Fail securely** | Errors default to deny, not allow |
| **Zero trust** | Verify every request; don't trust because it's internal |
| **Validate at boundaries** | All external input is untrusted until validated |

## Top Developer-Introduced Vulnerabilities

### 1. Injection (SQL, Command, LDAP)
Always use parameterized queries or prepared statements. Never concatenate user input into queries or commands.
```python
# ❌
query = f"SELECT * FROM users WHERE email = '{email}'"
# ✅
cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
```

### 2. Broken Authentication
- Use established auth libraries — never roll your own
- Hash passwords with bcrypt/argon2 (never MD5/SHA1)
- Enforce MFA for privileged access
- Invalidate sessions on logout and password change

### 3. Sensitive Data Exposure
- Never log passwords, tokens, PII, or payment data
- Encrypt sensitive data at rest and in transit (TLS 1.2+)
- Secrets in environment variables or vaults — never in code or git

### 4. Broken Access Control
- Enforce authorization server-side on every request
- Default deny — explicitly grant access, don't forget to restrict
- Check object-level permissions, not just endpoint-level

### 5. Security Misconfiguration
- No default credentials in production
- Disable unused features, endpoints, and services
- Security headers: CSP, HSTS, X-Frame-Options, X-Content-Type-Options
- Dependency scanning in CI (outdated packages carry known CVEs)

### 6. Secrets Management
```
❌ Never: hardcoded in source, committed to git, in logs
✅ Always: environment variables, secret managers (Vault, AWS Secrets Manager), .env files gitignored
```

## Security Review Checklist
- [ ] All external input validated and sanitized
- [ ] Parameterized queries used throughout
- [ ] Secrets not in code or logs
- [ ] Auth and authz enforced server-side
- [ ] Error messages don't leak stack traces or system info
- [ ] Dependencies up to date and scanned

## Red Flags
- `eval()` or `exec()` with user input
- `SELECT *` with string concatenation
- Credentials in source files or comments
- HTTP (not HTTPS) for any sensitive data
- `// TODO: add auth check`
```

- [ ] **Step 2: Commit**

```bash
git add skills/good-security/SKILL.md
git commit -m "feat: add good-security skill"
```

---

### Task 5: good-quality skill

**Files:**
- Create: `skills/good-quality/SKILL.md`

**Interfaces:**
- Consumed by: `good-review`, `good-fix`
- Produces: Holistic quality principles: testing, review, CI, observability, correctness

- [ ] **Step 1: Create `skills/good-quality/SKILL.md`**

```markdown
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
```

- [ ] **Step 2: Commit**

```bash
git add skills/good-quality/SKILL.md
git commit -m "feat: add good-quality skill"
```

---

### Task 6: good-writing skill

**Files:**
- Create: `skills/good-writing/SKILL.md`

**Interfaces:**
- Consumed by: `good-pr`, `good-review`
- Produces: Plain language writing principles for all developer communication

- [ ] **Step 1: Create `skills/good-writing/SKILL.md`**

```markdown
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
```

- [ ] **Step 2: Commit**

```bash
git add skills/good-writing/SKILL.md
git commit -m "feat: add good-writing skill"
```

---

### Task 7: good-debug skill

**Files:**
- Create: `skills/good-debug/SKILL.md`

**Interfaces:**
- Consumed by: `good-fix`
- Produces: Systematic debugging methodology — root cause first, evidence-based

- [ ] **Step 1: Create `skills/good-debug/SKILL.md`**

```markdown
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
```

- [ ] **Step 2: Commit**

```bash
git add skills/good-debug/SKILL.md
git commit -m "feat: add good-debug skill"
```

---

### Task 8: good-fix skill

**Files:**
- Create: `skills/good-fix/SKILL.md`

**Interfaces:**
- Consumes: `good-debug` (for diagnosis), `good-code` (for implementation), `good-quality` (for test and verification)
- Produces: Complete bug fix lifecycle — reproduce, diagnose, fix minimally, verify, prevent recurrence

- [ ] **Step 1: Create `skills/good-fix/SKILL.md`**

```markdown
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
- Was this caught late because of a gap in test coverage? Add the missing coverage.
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

## Red Flags
- Fix committed without a test
- "I'll write the test later"
- Fixing symptoms in 3+ places (root cause likely elsewhere)
- Hotfix left in place for more than a sprint
- "I'm not sure why this works, but it does"
```

- [ ] **Step 2: Commit**

```bash
git add skills/good-fix/SKILL.md
git commit -m "feat: add good-fix skill"
```

---

### Task 9: good-requirements skill

**Files:**
- Create: `skills/good-requirements/SKILL.md`

**Interfaces:**
- Consumes: `good-security` (for security/compliance requirements)
- Produces: Interview technique and requirements capture methodology

- [ ] **Step 1: Create `skills/good-requirements/SKILL.md`**

```markdown
---
name: good-requirements
description: Use when starting a new feature, project, or significant change — to surface what is actually needed before designing or building anything
---

# Good Requirements

## Core Principle

**Build the right thing before building it right.** Requirements are how you find out what "right" means.

## The Interview Approach

Ask one question at a time. Go deep before going broad.

### Layer 1: What and Why
- "What problem does this solve for the user?"
- "What does success look like? How will you know it's working?"
- "What's the most important thing this must do?"

### Layer 2: Who and When
- "Who are the users? What do they already know?"
- "Are there different user types with different needs?"
- "What's the timeline, and what drives it?"

### Layer 3: Constraints and Risks
- "What must this NOT do?"
- "What existing systems does this interact with?"
- "What happens when this fails?"
- "Are there regulatory, compliance, or data requirements?"

### Layer 4: Edge Cases
- "What's the unhappy path — what can go wrong?"
- "What's the scale? How many users, how much data?"
- "What inputs are possible, including unexpected ones?"

## Industry Standards to Surface

When the domain involves the following, ask explicitly and flag applicable standards for the design:

| Domain | Standards / Frameworks |
|--------|----------------------|
| Payment processing | PCI DSS — cardholder data, network segmentation, audit logs |
| Healthcare / medical | HIPAA (US), GDPR Article 9 (EU) — PHI handling, consent, breach notification |
| Privacy / personal data | GDPR, CCPA — data minimization, right to erasure, consent |
| Web / APIs | W3C, IETF RFCs (HTTP, OAuth 2.0, OIDC, JWT) |
| Accessibility | WCAG 2.1 AA — perceivable, operable, understandable, robust |
| Financial services | SOX, PSD2 (EU), relevant national banking regulation |

Security requirements → see `good:good-security` for the full security checklist.

## Documenting Requirements

Write requirements as **testable statements**:
```
✅ "Users can reset their password via email within 5 minutes"
❌ "Password reset should be easy"

✅ "The API returns a response within 500ms at p95 under normal load"
❌ "The API should be fast"
```

Use this structure:
- **Given** [context/precondition]
- **When** [action]  
- **Then** [observable, verifiable outcome]

## Red Flags
- "The user wants X" without talking to a user
- Requirements written as solutions ("we need a dropdown") not needs ("users need to select a country")
- No definition of done
- Compliance domain identified but applicable standards not reviewed
- No unhappy path considered
```

- [ ] **Step 2: Commit**

```bash
git add skills/good-requirements/SKILL.md
git commit -m "feat: add good-requirements skill"
```

---

### Task 10: good-plan skill

**Files:**
- Create: `skills/good-plan/SKILL.md`

**Interfaces:**
- Consumes: `good-requirements`, `good-architecture`, `good-code`
- Produces: Implementation planning and technical design methodology

- [ ] **Step 1: Create `skills/good-plan/SKILL.md`**

```markdown
---
name: good-plan
description: Use before implementing any non-trivial feature or change — to think through approach, decompose the work, and produce a plan an engineer can execute without ambiguity
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
```

- [ ] **Step 2: Commit**

```bash
git add skills/good-plan/SKILL.md
git commit -m "feat: add good-plan skill"
```

---

### Task 11: good-review skill

**Files:**
- Create: `skills/good-review/SKILL.md`

**Interfaces:**
- Consumes: `good-code`, `good-architecture`, `good-security`, `good-quality`, `good-writing`
- Produces: Code review methodology — holistic, actionable, professional feedback

- [ ] **Step 1: Create `skills/good-review/SKILL.md`**

```markdown
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
```

- [ ] **Step 2: Commit**

```bash
git add skills/good-review/SKILL.md
git commit -m "feat: add good-review skill"
```

---

### Task 12: good-pr skill

**Files:**
- Create: `skills/good-pr/SKILL.md`

**Interfaces:**
- Consumes: `good-writing`, `good-quality`
- Produces: PR readiness checklist and description template for clear, actionable PRs

- [ ] **Step 1: Create `skills/good-pr/SKILL.md`**

```markdown
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
```

- [ ] **Step 2: Commit**

```bash
git add skills/good-pr/SKILL.md
git commit -m "feat: add good-pr skill"
```

---

### Task 13: README

**Files:**
- Create: `README.md`

**Interfaces:**
- Produces: Public-facing documentation for the plugin — what it is, how to install, what each skill does

- [ ] **Step 1: Create `README.md`**

```markdown
# good

A Claude Code plugin of high-impact software development best practices — clear principles and guardrails for writing, designing, securing, planning, and reviewing software.

Licensed under the [Apache License 2.0](LICENSE).

## What's Included

11 skills covering the full development lifecycle:

| Skill | Invoke with | What it does |
|-------|------------|--------------|
| good-code | `/good:good-code` | Naming, function design, SOLID/KISS/DRY/YAGNI, error handling |
| good-architecture | `/good:good-architecture` | System decomposition, boundaries, dependency direction, data flow |
| good-security | `/good:good-security` | OWASP top risks, secrets, auth, defense in depth |
| good-quality | `/good:good-quality` | Testing, code review, CI, observability, definition of done |
| good-writing | `/good:good-writing` | Comments, commit messages, docs, READMEs — plain language |
| good-debug | `/good:good-debug` | Root cause first, systematic diagnosis before any fix |
| good-fix | `/good:good-fix` | Minimal complete fixes, test-first, prevent recurrence |
| good-requirements | `/good:good-requirements` | Interview technique, testable requirements, compliance flags |
| good-plan | `/good:good-plan` | Technical design decisions + task-level implementation planning |
| good-review | `/good:good-review` | Holistic code review: correctness, security, design, quality |
| good-pr | `/good:good-pr` | PR readiness, writing clear descriptions, communicating decisions |

## Install

### From the Claude Code marketplace

Add this repository as a marketplace source in Claude Code:

1. Open Claude Code settings → Marketplaces
2. Add marketplace URL: `https://github.com/andreaross/good`
3. Find the **good** plugin and click Install

### Manual install via CLI

```bash
claude plugin install https://github.com/andreaross/good
```

## Design Philosophy

- **High impact, not exhaustive.** Each skill covers the principles that matter most, not every possible rule.
- **Human-readable at a glance.** A developer should be able to scan a skill and apply it immediately.
- **Token-efficient for AI.** Structured, concise, and scannable — no padding, no redundancy.
- **Self-contained.** Skills cross-reference each other but have no external dependencies.

## Contributing

Contributions welcome. To propose a change:
1. Open an issue describing the principle you want to add or change, and why
2. Keep changes focused — one principle, one PR
3. Follow the existing skill format (frontmatter, headers, examples, red flags)

## License

Copyright 2026 Andrea Ross

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full text.
```

- [ ] **Step 2: Create `LICENSE` file with Apache 2.0 text**

Fetch the standard Apache 2.0 license text and save it to `LICENSE`. Replace the copyright year and holder with:
```
Copyright 2026 Andrea Ross
```

- [ ] **Step 3: Commit**

```bash
git add README.md LICENSE
git commit -m "feat: add README and Apache 2.0 license"
```

---

## Self-Review

### Spec coverage
- ✅ All 11 skills defined (good-code, good-architecture, good-security, good-quality, good-writing, good-debug, good-fix, good-requirements, good-plan, good-review, good-pr)
- ✅ Plugin manifest and marketplace manifest
- ✅ README with install instructions
- ✅ Apache v2 license
- ✅ Marketplace format (`.claude-plugin/marketplace.json`)
- ✅ Skills reference each other using `good:<skill-name>` format
- ✅ No external dependencies
- ✅ High-impact principles, not exhaustive

### Placeholder scan
- No TBDs, TODOs, or fill-in-the-blanks present

### Type consistency
- Skill cross-references use consistent format: `good:good-<name>`
- All file paths are exact
