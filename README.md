# good

A Claude Code plugin of high-impact software development best practices. It contains clear principles and guardrails for writing, designing, securing, planning, and reviewing software.

Licensed under the [Apache License 2.0](LICENSE).

## What's Included

12 skills covering the full development lifecycle:

| Skill | Invoke with | What it does |
|-------|------------|--------------|
| good-developer | `/good:good-developer` | Loads all good plugin skills for software development — the full developer toolkit |
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
2. Add marketplace URL: `https://github.com/ripplesandleaves/good`
3. Find the **good** plugin and click Install

### Manual install via CLI

```bash
claude plugin install https://github.com/ripplesandleaves/good
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
