from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

Current_room = 0

description = [
    "You see a typical class room with a whiteboard in front of you.",
    "You are in a corridor at University West.",
    "You see a restaurant where people eat lunch."]

def parse_and_execute(command):
    global Current_room
    if command == "look" or command == "l":
        return description[Current_room]
    if command == "go east" or command == "e":
        if Current_room < 2:
            Current_room += 1
            return "You walk east!"
        return "You bump into the wall!"
    if command == "go west" or command == "w":
        if Current_room > 0:
            Current_room -= 1
            return "You walk west!"
        return "You bump into the wall!"
    if command == "help" or command == "h" or command == "?":
        return "Try looking around, go east, west, or quit!"
    return "I don't understand your command!"
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    server.register_function(parse_and_execute)

    # Run the server's main loop
    server.serve_forever()