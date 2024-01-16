
import socket

host = "127.0.0.1"
port = 65432

"""
small_mud.py, Thomas Lundqvist, 2019-2023, use freely!

A small beginning of a MUD, Multi User Dungeon, game.
"""

finished = 0
print("Welcome to simple MUD, the simple Multi-User Dungeon game.")
while not finished:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))     
        command = input(': ')
        if command == "quit" or command == "q":
            finished = 1
        else:
            s.sendall(bytes(command, 'utf-8'))
            data = s.recv(1024)

    print(f"Recieved {data!r}")

