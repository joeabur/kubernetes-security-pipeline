# Testing

## Local checks

- `make lint test` compiles Python and runs service/gate unit tests.
- `make gate` proves a low-severity report passes the default HIGH threshold.
- `docker build --file docker/Dockerfile --tag secure-demo-api:local .` verifies the image build.
- `trivy fs --scanners vuln,secret,misconfig .` scans the repository.
- `checkov --directory kubernetes/secure --framework kubernetes` scans secure manifests.
- `kyverno apply policies/kyverno --resource kubernetes/secure --table` validates admission policies.

## Negative tests

The vulnerable fixture should produce findings for privileged execution, root, host networking, hostPath, capabilities, latest tag, plaintext secret, missing limits, and cluster-admin binding. Keep it isolated and never use it as a deployment target.

For live admission testing, use kind or another disposable cluster. Kyverno and Falco are installed in dedicated system namespaces; the repository policies explicitly exclude those namespaces because Falco requires privileged host observability. The secure workload is admitted and the vulnerable Deployment is rejected.

## Gate behavior

`SECURITY_THRESHOLD=HIGH make gate` blocks HIGH and CRITICAL findings. Set `SECURITY_THRESHOLD=CRITICAL` for a stricter demonstration that only critical findings block. Real CI jobs fail directly on scanner exit codes and upload machine-readable SARIF/JSON artifacts.
