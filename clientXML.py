import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print("Welcome to simple MUD, the simple Multi-User Dungeon game.")
finished = 0
while not finished:   
    command = input(': ')
    if command == "quit" or command == "q":
        finished = 1
    else:
        print(s.parse_and_execute(command))