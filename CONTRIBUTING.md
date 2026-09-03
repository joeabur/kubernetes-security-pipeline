# Contributing

1. Create a short-lived branch from `main`.
2. Keep demo fixtures and secure configurations separate.
3. Run `make lint test` before opening a pull request.
4. Run the relevant local scanners when changing Docker, Kubernetes, policies, or dependencies.
5. Include the security impact, test evidence, and any accepted risk in the pull request.
6. Do not commit secrets, private keys, credentials, or unreviewed third-party action changes.

Pull requests require review from the owners in `CODEOWNERS` and passing security gates.
