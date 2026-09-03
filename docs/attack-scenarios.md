# Attack Scenarios

## Privileged pod attempt

Deploying `kubernetes/intentionally-vulnerable/vulnerable.yaml` should be rejected by Pod Security and the Kyverno restricted-pods policy. If bypassed in an isolated lab, Falco should report suspicious shell or host-path activity.

## Mutable image attempt

Changing the secure workload to `nginx:latest` should fail the digest admission policy and be reported by IaC scanners.

## Secret commit attempt

Adding a high-entropy credential-shaped value should be detected by Gitleaks. Real credentials must be revoked immediately even when a scanner reports a false positive.

## Vulnerable dependency or image

Trivy SCA and image scanning should report known CVEs and fail at configured severities. Remediation is to upgrade, rebuild, retest, and preserve the SBOM for the released digest.
