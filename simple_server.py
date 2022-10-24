from http.server import HTTPServer, SimpleHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
	server_address = ("0.0.0.0", 8000)
	httpd = server_class(server_address, handler_class)
	print("Launching Server...")
	httpd.serve_forever()

if __name__ == "__main__":
	run()
