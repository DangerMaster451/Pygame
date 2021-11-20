import socket

HOST = '127.0.0.1'  
PORT = 65432        
PLAYERSONLINE = 0

print("Server has Started. Waiting for connection...")

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        PLAYERSONLINE += 1
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("Successful Connection: ", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    PLAYERSONLINE -= 1
                    break
                print(data.decode())
            