#!/usr/bin/env python

"""
Usage: python server.py ip port (e.g. pythong server.py 127.0.0.1 8080)
"""


import cgi
import logging
import SimpleHTTPServer
import SocketServer
import sys


if len(sys.argv) > 2:
    PORT = int(sys.argv[2])	# port (e.g. 8080)
    I = sys.argv[1]		# interface (e.g. '127.0.0.1')
elif len(sys.argv) > 1:
    PORT = int(sys.argv[1])	# port
    I = ''			# interface
else:
    PORT = 80			# default port
    I = ''			# default interface (all)


class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """
    This class creates an instance of a 'ServerHandler', which handles an HTTP
    request.
    """

    def do_GET(self):
        """
        This method handles HTTP GET requests.
        """

        logging.warning('======= GET STARTED =======')
        logging.warning(self.headers)
        # http.server.SimpleHTTPRequestHandler.do_GET(self)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        """
        This method handles HTTP POST requests.
        """

        logging.warning('======= POST STARTED =======')
        logging.warning(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        logging.warning('======= POST VALUES =======')
        for item in form.list:
            logging.warning(item)
        logging.warning('\n')
        # http.server.SimpleHTTPRequestHandler.do_GET(self)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

# Create an instance of 'ServerHandler'
Handler = ServerHandler

# Create a simple Python web server
httpd = SocketServer.TCPServer(('', PORT), Handler)

# Output the status to STDOUT (likely this will never be seen)
print('Python HTTP server')
print('Serving at: http://%(interface)s:%(port)s' % dict(interface=I or 'localhost', port=PORT))

# Listen for client connections
httpd.serve_forever()		# run forever

# 'run once' may not free the socket quickly enough for the host to respond to
# subsequent requests
#
# httpd.handle_request()	# run once
