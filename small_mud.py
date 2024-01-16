
import socket

host = "IP ADDR"
port = 65432

"""
small_mud.py, Thomas Lundqvist, 2019-2023, use freely!

A small beginning of a MUD, Multi User Dungeon, game.
"""
s = socket.socket()
s.connect((host, port)) 
finished = 0
print("Welcome to simple MUD, the simple Multi-User Dungeon game.")
while not finished:
       
    command = input(': ')
    if command == "quit" or command == "q":
        finished = 1
    else:
        s.send(bytes(command, 'utf-8'))
        data = s.recv(1024)

    print(f"Recieved {data!r}")

