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
