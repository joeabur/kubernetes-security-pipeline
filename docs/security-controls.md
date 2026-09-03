# Security Controls

| Layer | Control | Evidence |
| --- | --- | --- |
| Source | CODEOWNERS, Dependabot, read-only GITHUB_TOKEN | `.github/` |
| Code | Unit tests, Semgrep SAST, secure response headers | `app/`, CI workflow |
| Dependencies | Dependency review and Trivy SCA | Security workflow |
| Secrets | Gitleaks and GitHub Secrets guidance | `.gitleaks.toml`, `SECURITY.md` |
| Build | Non-root image, pinned base reference | `docker/Dockerfile` |
| Supply chain | Trivy image scan, Syft CycloneDX SBOM | Security workflow |
| IaC | Checkov and Trivy config scan | Kubernetes and Helm files |
| Admission | Kyverno enforce policies | `policies/kyverno/` |
| Runtime | Falco detection rules | `examples/falco-rules.yaml` |
| Kubernetes | PSS restricted, RBAC, NetworkPolicy, limits | `kubernetes/base/` |
| Response | Threshold gate, SARIF and artifact reports | `scripts/security_gate.py` |

Controls are demonstrative. Production adoption still requires signed provenance, protected environments, centralized logging, key management, registry policy, and tested incident playbooks.
