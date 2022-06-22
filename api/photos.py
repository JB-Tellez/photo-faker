from http.server import BaseHTTPRequestHandler
import json


class PhotoModel:
    def __init__(
        self, id, photo_name, photo_url="https://via.placeholder.com/200x200/ddd"
    ):
        self.id = id
        self.photo_name = photo_name
        self.photo_url = photo_url


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        photos = [
            PhotoModel(1, "dog"),
            PhotoModel(2, "cat"),
            PhotoModel(3, "elephant"),
        ]

        message = json.dumps(photos)

        message = "whassup"

        self.wfile.write(message.encode())
