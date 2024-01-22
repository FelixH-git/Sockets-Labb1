
import socket

def send_msg(username, message):
    return f"{username}: {message}"
host_list = ["127.0.0.1"]
host = "127.0.0.1"
port_list = [8000, 7999]

s = socket.socket()
s.connect((host, port_list[0])) 

s1 = socket.socket()
s1.connect((host, port_list[1])) 

finished = 0

name = input("Enter name")

while not finished:       
    command = input(': ')
    if command == "quit" or command == "q":
        finished = 1
    else:
        s.send(bytes(send_msg(name, command), 'utf-8'))
        s1.send(bytes(send_msg(name, command), 'utf-8'))

