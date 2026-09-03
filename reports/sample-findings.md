# Sample Security Report

Generated from the demonstration fixture. This is human-readable evidence, not a live scan result.

| Tool | Finding | Severity | Gate at HIGH |
| --- | --- | --- | --- |
| Trivy | No findings in secure image fixture | Informational | Pass |
| Checkov | Resource limits and restricted pod controls present | Informational | Pass |
| Kyverno | Digest, non-root, and no privilege escalation | Informational | Pass |
| Gitleaks | No real credentials are stored | Informational | Pass |

Thresholds are configured through `SECURITY_THRESHOLD`; the gate blocks `HIGH` and `CRITICAL` by default.
