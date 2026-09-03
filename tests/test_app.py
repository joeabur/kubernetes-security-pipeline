import json
import unittest
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from threading import Thread

from app.main import RequestHandler, health_payload, security_headers


class AppTests(unittest.TestCase):
    def test_health_payload_is_stable(self):
        self.assertEqual(health_payload(), {"status": "ok", "service": "secure-demo-api"})

    def test_security_headers_include_baseline(self):
        headers = security_headers()
        self.assertEqual(headers["X-Content-Type-Options"], "nosniff")
        self.assertEqual(headers["X-Frame-Options"], "DENY")
        self.assertIn("default-src 'none'", headers["Content-Security-Policy"])

    def test_health_endpoint(self):
        server = ThreadingHTTPServer(("127.0.0.1", 0), RequestHandler)
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            connection = HTTPConnection("127.0.0.1", server.server_port, timeout=2)
            connection.request("GET", "/healthz")
            response = connection.getresponse()
            self.assertEqual(response.status, 200)
            self.assertEqual(json.loads(response.read()), health_payload())
            self.assertEqual(response.getheader("X-Frame-Options"), "DENY")
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == "__main__":
    unittest.main()
