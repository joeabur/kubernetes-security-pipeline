"""Evaluate machine-readable findings against configurable severity thresholds."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SEVERITY_ORDER = {"UNKNOWN": 0, "LOW": 1, "MEDIUM": 2, "HIGH": 3, "CRITICAL": 4}


def load_findings(path: Path) -> list[dict[str, Any]]:
    document = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(document, list):
        return [item for item in document if isinstance(item, dict)]
    findings = document.get("findings", [])
    if not isinstance(findings, list):
        raise ValueError("report must contain a findings list")
    return [item for item in findings if isinstance(item, dict)]


def blocked_findings(findings: list[dict[str, Any]], threshold: str) -> list[dict[str, Any]]:
    minimum = SEVERITY_ORDER[threshold]
    return [
        finding
        for finding in findings
        if SEVERITY_ORDER.get(str(finding.get("severity", "UNKNOWN")).upper(), 0) >= minimum
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument(
        "--threshold",
        default="HIGH",
        choices=tuple(SEVERITY_ORDER),
        help="minimum severity that blocks the pipeline",
    )
    args = parser.parse_args()
    findings = load_findings(args.report)
    blocked = blocked_findings(findings, args.threshold)
    summary = {severity: 0 for severity in SEVERITY_ORDER}
    for finding in findings:
        severity = str(finding.get("severity", "UNKNOWN")).upper()
        summary[severity if severity in summary else "UNKNOWN"] += 1
    print(json.dumps({"threshold": args.threshold, "summary": summary, "blocked": len(blocked)}))
    if blocked:
        for finding in blocked:
            print(
                f"BLOCKED {finding.get('severity', 'UNKNOWN')}: "
                f"{finding.get('id', 'unidentified')} - {finding.get('title', 'untitled')}",
                file=sys.stderr,
            )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
