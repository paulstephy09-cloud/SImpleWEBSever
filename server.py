import http.server
import socketserver
import platform

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            with open("index.html", "r") as file:
                html = file.read()

            html = html.replace(
                "{{OS}}", platform.system()
            )
            html = html.replace(
                "{{VERSION}}", platform.version()
            )
            html = html.replace(
                "{{MACHINE}}", platform.machine()
            )
            html = html.replace(
                "{{PROCESSOR}}", platform.processor()
            )

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(html.encode())

with socketserver.TCPServer(("", PORT), MyHandler) as server:
    print(f"Server running at http://127.0.0.1:{PORT}")
    server.serve_forever()