# Detection and Response

1. **Triage:** identify the workflow, commit, image digest, namespace, and finding severity.
2. **Contain:** pause deployment, quarantine the image or namespace, and revoke exposed credentials through the owning system.
3. **Investigate:** preserve GitHub audit logs, Kubernetes audit events, Falco events, image metadata, and relevant pod logs.
4. **Eradicate:** patch the source or dependency, rebuild from a trusted base, rotate credentials, and redeploy through the gate.
5. **Recover:** validate admission, runtime, and network controls; monitor the repaired workload.
6. **Learn:** record root cause, detection gap, remediation, and whether policy or tests need strengthening.

A Falco event is a signal, not proof of compromise. Correlate it with Kubernetes audit logs and image provenance before closing an incident.
