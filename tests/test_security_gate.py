import json
import tempfile
import unittest
from pathlib import Path

from scripts.security_gate import blocked_findings, load_findings


class SecurityGateTests(unittest.TestCase):
    def test_high_and_critical_findings_block_high_threshold(self):
        findings = [{"severity": "LOW"}, {"severity": "HIGH"}, {"severity": "CRITICAL"}]
        self.assertEqual(len(blocked_findings(findings, "HIGH")), 2)

    def test_report_loader_accepts_wrapped_reports(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            path.write_text(json.dumps({"findings": [{"id": "TEST-1"}]}), encoding="utf-8")
            self.assertEqual(load_findings(path), [{"id": "TEST-1"}])


if __name__ == "__main__":
    unittest.main()
