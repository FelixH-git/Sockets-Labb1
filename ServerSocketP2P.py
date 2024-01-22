import socket

host = "127.0.0.1"



port = int(input("Enter Port: "))
s = socket.socket()

s.bind((host,port))
#s.listen()

#### FÖR FLERA CONNECTIONS #########

connections = int(input("Enter amount of connections: "))

s.listen(connections)
############################
conn, addr = s.accept()
# with conn:
#     print(f"connect by {addr}")
while True:
    data = conn.recv(1024)
    if not data:
        break
    data = data.decode('utf-8')
    print(data)
conn.close()
