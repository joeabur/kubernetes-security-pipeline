# Threat Model

## Assets

Source code, build provenance, container images, SBOMs, Kubernetes API access, cluster nodes, and security reports.

## Attack surface

Pull requests, GitHub Actions dependencies, Dockerfile and build context, image registry, Helm/Kustomize values, Kubernetes API, exposed HTTP endpoints, and runtime processes.

## Threats and controls

| Threat | Example | Controls |
| --- | --- | --- |
| Tainted source | Malicious pull request | CODEOWNERS, least-privilege token, Semgrep, review |
| Dependency compromise | Vulnerable or abandoned package | Dependabot, dependency review, Trivy SCA |
| Secret exposure | Credential committed to Git | Gitleaks, GitHub secret storage, no plaintext secrets |
| Image tampering | Mutable tag or vulnerable base | Digest pinning, Trivy, Syft SBOM, Kyverno |
| Cluster escape | Privileged pod or host mount | Restricted Pod Security, Kyverno, dropped capabilities |
| Lateral movement | Unrestricted pod network | Default-deny NetworkPolicy and scoped egress |
| Credential abuse | Overly broad service account | No token automount, namespaced Role, no ClusterRoleBinding |
| Runtime intrusion | Shell or host write | Falco rules, immutable filesystem, incident response |

## MITRE ATT&CK mapping

- T1190 Exploit Public-Facing Application: DAST and security headers.
- T1525 Implant Internal Image: registry controls, digest pinning, SBOM and image scans.
- T1611 Escape to Host: non-root pods, no privilege escalation, Kyverno and Falco.
- T1609 Container Administration Command: Kubernetes RBAC, admission and audit logs.
- T1613 Container Service: NetworkPolicies, restricted namespaces and service exposure.
