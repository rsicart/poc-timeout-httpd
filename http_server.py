#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import datetime

class TimeoutHTTPServer(HTTPServer):

  def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
    super().__init__(server_address, RequestHandlerClass, bind_and_activate=True)
    self.timeout = 10
    print(time.asctime(), 'Init called !')


  def handle_timeout(self):
      print(time.asctime(), 'Handle timeout called !')

 
# HTTPRequestHandler class
class TimeoutHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "Hello world!\n"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

        return

  # POST
  def do_POST(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "Hello world POST!\n"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

        return

 
if __name__ == '__main__':
  print('Starting server...')
  server_address = ('127.0.0.1', 8081)
  httpd = TimeoutHTTPServer(server_address, TimeoutHTTPServer_RequestHandler)
  print(time.asctime(), 'Server Starts - %s:%s' % server_address)
  try:
      while True:
          httpd.handle_request()
  except KeyboardInterrupt:
      pass
  httpd.server_close()
  print(time.asctime(), 'Server Stops - %s:%s' % server_address)
