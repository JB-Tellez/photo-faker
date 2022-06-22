from http.server import BaseHTTPRequestHandler

class PhotoModel:
    def __init__(self, id, photo_name, photo_url):
        self.id = id
        self.photo_name = photo_name
        self.photo_url = photo_url



class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        message = "Howdy Pardner"
        self.wfile.write(message.encode())
