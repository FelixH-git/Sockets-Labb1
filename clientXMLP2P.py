import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
s1 = xmlrpc.client.ServerProxy('http://localhost:7999')


print("Welcome to simple MUD, the simple Multi-User Dungeon game.")
finished = 0
msg_log = []
name = input("Your Name: ")
while not finished:   
    command = input(': ')
    if command == "quit" or command == "q":
        finished = 1
    else:
        s.send_msg(name, command)
        s1.send_msg(name, command)
