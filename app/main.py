"""Minimal dependency-free HTTP service used by the security pipeline demo."""

from __future__ import annotations

import json
import os
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any


SERVICE_NAME = "secure-demo-api"


def health_payload() -> dict[str, str]:
    """Return the stable liveness payload used by probes and tests."""
    return {"status": "ok", "service": SERVICE_NAME}


def security_headers() -> dict[str, str]:
    """Return headers expected on every response."""
    return {
        "Content-Type": "application/json",
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "Referrer-Policy": "no-referrer",
        "Content-Security-Policy": "default-src 'none'",
        "Cache-Control": "no-store",
    }


class RequestHandler(BaseHTTPRequestHandler):
    """Expose only health and metadata endpoints for the demo workload."""

    server_version = "secure-demo-api"

    def _send_json(self, status: HTTPStatus, payload: dict[str, Any]) -> None:
        body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
        self.send_response(status)
        for name, value in security_headers().items():
            self.send_header(name, value)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802 - required by BaseHTTPRequestHandler
        if self.path == "/healthz":
            self._send_json(HTTPStatus.OK, health_payload())
            return
        if self.path == "/readyz":
            self._send_json(HTTPStatus.OK, {"status": "ready"})
            return
        self._send_json(HTTPStatus.NOT_FOUND, {"error": "not found"})

    def log_message(self, format_string: str, *args: Any) -> None:
        """Emit structured, minimal request logs without sensitive headers."""
        print(json.dumps({"message": format_string % args}), flush=True)


def serve() -> None:
    port = int(os.getenv("PORT", "8080"))
    server = ThreadingHTTPServer(("0.0.0.0", port), RequestHandler)
    print(json.dumps({"message": "server_started", "port": port}), flush=True)
    server.serve_forever()


if __name__ == "__main__":
    serve()
