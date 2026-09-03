SHELL := /bin/bash
PYTHON ?= python3
SECURITY_THRESHOLD ?= HIGH

.PHONY: test lint gate app-build docker-build scan-local

test:
	$(PYTHON) -m unittest discover -s tests -v

lint:
	$(PYTHON) -m compileall -q app scripts tests

gate:
	$(PYTHON) scripts/security_gate.py reports/sample-findings.json --threshold $(SECURITY_THRESHOLD)

app-build:
	$(PYTHON) -m compileall -q app

docker-build:
	docker build --file docker/Dockerfile --tag secure-demo-api:local .

scan-local:
	trivy fs --scanners vuln,secret,misconfig --format json --output reports/trivy-fs.json .
	checkov --directory . --output json --output-file-path reports
