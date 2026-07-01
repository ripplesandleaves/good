---
name: good-sweep
description: Use when auditing an existing codebase for security and robustness issues — to find, prioritize, and fix the highest-impact problems proactively
---

# Good Sweep

## What It Does

Orchestrates a parallel subagent scan of an existing codebase, triages findings by severity, and fixes the top issues worth fixing. Accepts an optional count: `/good:good-sweep 5` fixes the top 5 qualifying issues. Without a count, fixes all critical and high issues.

## Severity Model

Priority = **blast radius × likelihood**. Only medium or higher severity is acted on; lower-severity findings are reported but not fixed.

| Severity | Definition | Blast radius | Fix when |
|----------|------------|--------------|----------|
| **Critical** | Exploitable without authentication; full compromise of confidentiality, integrity, or availability in normal operation | All users or all data | Immediately |
| **High** | Requires specific conditions or privileges; significant data exposure, unauthorized access, or service disruption | Many users or a sensitive data subset | This sprint |
| **Medium** | Requires user interaction or uncommon conditions; partial or limited exposure | Individual users or low-sensitivity data | Next cycle |
| *Low / Info* | Theoretical; negligible real-world impact | Minimal | Not in scope |

> Based on CVSS 3.1: Critical ≥ 9.0, High 7.0–8.9, Medium 4.0–6.9.

## Phase 1: Scan (Parallel Subagents)

Spawn two subagents simultaneously. Each returns a list of issues with: file path, line range, severity, blast radius estimate, likelihood, and a one-line description.

**Security subagent** — apply `good:good-security` across the codebase:
- Injection vectors (SQL, command, LDAP, template, path traversal)
- Hardcoded or committed secrets, API keys, credentials
- Authentication weaknesses (weak hashing, missing invalidation, session fixation)
- Missing or bypassable authorization (object-level, not just endpoint-level)
- Security misconfiguration (default credentials, exposed internals, missing headers)
- Sensitive data in logs, error messages, or responses

**Robustness subagent** — focus on failure modes:
- Unvalidated or untyped external input at system boundaries
- Missing error handling on I/O, network, and database calls
- Resource leaks (connections, file handles, locks, goroutines)
- Unsafe concurrency and race conditions
- Unchecked nulls, empty collections, integer overflow, or type assumptions
- Unbounded operations (loops, allocations, query results without limits)

## Phase 2: Triage

1. Merge findings from both subagents; deduplicate overlaps
2. Rank by severity, then blast radius, then likelihood
3. **Diminishing returns check:** If no medium-or-higher issues exist, report the full list with reasoning and stop — the cost of fixing low-severity issues (PR noise, regression risk) exceeds the benefit
4. Apply the count: take the top N issues from the ranked list

Do not attempt to fix issues where the root cause is architectural (wrong boundaries, circular dependencies, shared mutable global state). Flag these with a note and skip them — architectural sweeps require `good:good-architecture` and deliberate design work, not point fixes.

## Phase 3: Fix

For each selected issue, one at a time — never batch:

1. **Diagnose** — apply `good:good-debug`: understand root cause before writing a line of code; confirm exploitability, not just pattern-match
2. **Fix** — apply `good:good-fix`: minimal complete fix; no refactoring, no cleanup of adjacent code
3. **Quality check** — apply `good:good-code`: fix must not introduce its own smell or reduce clarity
4. **Verify** — run tests; confirm the fix passes and does not regress anything

If a fix attempt reveals the root cause is deeper than it appeared (requires changing more than 2–3 call sites, or touches core abstractions), stop. Flag it as architectural and move to the next issue.

## Phase 4: Communicate

Apply `good:good-review` — read the full diff before opening a PR, as a reviewer would. Catch anything that looks worse from the outside than it did while writing.

Apply `good:good-pr` to write the description:
- What was found, what was fixed, and why each was prioritized
- Severity and blast radius of each fix
- How each fix was verified
- What was found but not fixed, and why (too architectural, below the bar, or outside the count)

## Diminishing Returns — Stop and Report When

- All remaining issues are below medium severity
- Fixing an issue requires architectural change
- The blast radius of the fix (risk of regression) exceeds the blast radius of the issue
- The count has been reached

## Red Flags
- Fixing an issue based on code pattern alone without confirming exploitability
- Batching multiple issue fixes into a single change
- Skipping `good:good-debug` because "the fix is obvious"
- Treating architectural root causes as point fixes
- Fixing low-severity issues when medium-or-higher ones remain unfixed
