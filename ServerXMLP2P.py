from xmlrpc.server import SimpleXMLRPCServer
from multiprocessing import Pool



messages = ["",""]

def send_msg(username, message):
    print(f"{username}: {message}")

# Create server
port = int(input("Enter port: "))
with SimpleXMLRPCServer(('localhost', port), allow_none=True) as server:
    server.register_function(send_msg)
    server.serve_forever()
