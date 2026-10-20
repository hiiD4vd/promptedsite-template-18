import os
import sys
import mimetypes
from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse
import re

SITE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "site"))

# Register extra mimetypes
mimetypes.add_type("application/wasm", ".wasm")
mimetypes.add_type("model/gltf-binary", ".glb")
mimetypes.add_type("application/octet-stream", ".riv")
mimetypes.add_type("font/woff2", ".woff2")
mimetypes.add_type("image/avif", ".avif")
mimetypes.add_type("audio/mpeg", ".mp3")
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/css", ".css")

class PlanetonoHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SITE_DIR, **kwargs)

    def end_headers(self):
        # Enable CORS and caching headers
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, HEAD")
        self.send_header("Access-Control-Allow-Headers", "*")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        # Handle Storyblok API mock routes
        if "stories/global" in path:
            target = os.path.join(SITE_DIR, "api_storyblok", "global.json")
            return self.serve_custom_file(target, "application/json")
        elif "stories/home" in path:
            target = os.path.join(SITE_DIR, "api_storyblok", "home.json")
            return self.serve_custom_file(target, "application/json")

        # Range request support for audio streaming
        range_header = self.headers.get("Range")
        if range_header and path.endswith(".mp3"):
            return self.serve_audio_range(path, range_header)

        return super().do_GET()

    def serve_custom_file(self, filepath, content_type):
        if not os.path.exists(filepath):
            self.send_error(404, "File Not Found")
            return
        with open(filepath, "rb") as f:
            data = f.read()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def serve_audio_range(self, url_path, range_header):
        rel_path = url_path.lstrip("/").replace("/", os.sep)
        full_path = os.path.join(SITE_DIR, rel_path)
        if not os.path.exists(full_path):
            self.send_error(404, "Audio file not found")
            return

        file_size = os.path.getsize(full_path)
        m = re.match(r"bytes=(\d+)-(\d*)", range_header)
        if not m:
            return super().do_GET()

        start = int(m.group(1))
        end = int(m.group(2)) if m.group(2) else file_size - 1
        end = min(end, file_size - 1)
        length = end - start + 1

        self.send_response(206)
        self.send_header("Content-Type", "audio/mpeg")
        self.send_header("Content-Range", f"bytes {start}-{end}/{file_size}")
        self.send_header("Content-Length", str(length))
        self.send_header("Accept-Ranges", "bytes")
        self.end_headers()

        with open(full_path, "rb") as f:
            f.seek(start)
            self.wfile.write(f.read(length))

def run(port=8888):
    server_address = ("", port)
    httpd = HTTPServer(server_address, PlanetonoHandler)
    print(f"Planetono Local Server running on http://localhost:{port} (Root: {SITE_DIR})")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()

if __name__ == "__main__":
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 8888
    run(p)
