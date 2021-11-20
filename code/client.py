import socket
import renderer

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def initialize():
    s.connect((HOST, PORT))

def send(data):
    s.sendall(bytes(data, 'utf-8'))

def get():
    return str(s.recv(1024).decode())
