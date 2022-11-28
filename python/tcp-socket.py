import socket

HOST = "172.20.241.9"
PORT = 20000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"70\n")
    data = s.recv(1024)
    
print(f"received {data}")