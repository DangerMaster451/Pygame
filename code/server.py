import socket
import os
from _thread import *

HOST = '127.0.0.1'  
PORT = 65432        
DATA = {"PLAYERSONLINE":0, "Players":[]}
PLAYERDATA = {"Username":"", "uuid":"", "Pos":[]}

file = open("server.log", "w")
print("Server has Started. Waiting for connection...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((HOST, PORT))
except socket.error as e:
    file.write(str(e))

s.listen(0)
print("Waiting for a connection, Server Started")


def threaded_client(conn):
    DATA["PLAYERSONLINE"] += 1
    print("Successful Connection: ", addr)
    conn.sendall(bytes(str(DATA["PLAYERSONLINE"]), "utf-8")) #Player Number
    print(str(DATA["PLAYERSONLINE"]))
    while True:
        data = conn.recv(1024)
        if not data:
            file.close()
            DATA["PLAYERSONLINE"] -= 1
            break
        
        file.write(str(DATA["PLAYERSONLINE"]) + " Player(s) Online")
        file.write(f"{data.decode()}\n")
        conn.sendall(bytes(str(DATA["PLAYERSONLINE"]), "utf-8"))

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))      
        