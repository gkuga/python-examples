#!/usr/bin/env python3

import http.server as SimpleHTTPServer
import socketserver as SocketServer
import logging
import json

PORT = 9000


class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        content_len = int(self.headers.get('content-length'))
        requestBody = json.loads(self.rfile.read(content_len).decode('utf-8'))
        logging.info(requestBody)
        logging.info(self.headers)
        response = {
            'status': 200,
            'message': 'ok',
        }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        responseBody = json.dumps(response)
        self.wfile.write(responseBody.encode('utf-8'))


httpd = SocketServer.TCPServer(("", PORT), Handler)
httpd.serve_forever()
