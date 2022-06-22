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
            {
                "id": 4,
                "photo_name": "fox",
                "photo_url": "https://via.placeholder.com/200x200/ddd",
            },
            {
                "id": 5,
                "photo_name": "weasel",
                "photo_url": "https://via.placeholder.com/200x200/ddd",
            },
            {
                "id": 6,
                "photo_name": "zebra",
                "photo_url": "https://via.placeholder.com/200x200/ddd",
            },
            {
                "id": 7,
                "photo_name": "dolphin",
                "photo_url": "https://via.placeholder.com/200x200/ddd",
            },
            {
                "id": 8,
                "photo_name": "rabbit",
                "photo_url": "https://via.placeholder.com/200x200/ddd",
            },
            {
                "id": 9,
                "photo_name": "owl",
                "photo_url": "https://via.placeholder.com/200x200/ddd",
            },
        ]

        message = json.dumps(photos)

        self.wfile.write(message.encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        message = json.dumps({"status": "photo accepted"})
        self.wfile.write(message.encode())
