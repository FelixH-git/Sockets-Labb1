import socket

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

host = "192.168.1.111"
port = 65432
s = socket.socket()

s.bind((host,port))
s.listen()
conn, addr = s.accept()
# with conn:
#     print(f"connect by {addr}")
while True:
    data = conn.recv(1024)
    if not data:
        break
    data = data.decode('utf-8')
    print(data)
    conn.send(bytes(parse_and_execute(data), 'utf-8'))
conn.close()