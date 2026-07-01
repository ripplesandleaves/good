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
