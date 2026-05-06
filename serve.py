import http.server, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
httpd = http.server.HTTPServer(('', 3000), http.server.SimpleHTTPRequestHandler)
httpd.serve_forever()
