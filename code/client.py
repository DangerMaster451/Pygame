import socket
import renderer

HOST = '127.0.0.1'
PORT = 65432

def send(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bytes(data))
        data = s.recv(1024)