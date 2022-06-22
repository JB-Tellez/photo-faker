from http.server import BaseHTTPRequestHandler
import json


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        photos = [
            {
                "id": 1,
                "photo_name": "dog",
                "photo_url": "https://via.placeholder.com/200x200/ddd",
            },
            {
                "id": 2,
                "photo_name": "cat",
                "photo_url": "https://via.placeholder.com/200x200/ddd",
            },
            {
                "id": 3,
                "photo_name": "elephant",
                "photo_url": "https://via.placeholder.com/200x200/ddd",
            },
        ]

        message = json.dumps(photos)

        self.wfile.write(message.encode())
