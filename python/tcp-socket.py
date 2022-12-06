import socket

HOST = "172.20.241.9"
PORT = 20000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"70\n")
    connected = True
    data = []
    while 1:
        msg = s.recv(1024)
        if msg:
            data.append(msg)
        else:
            break
        # data = s.recv(1024)
        # data = []
        
    print(f"received {data}")
    
with open("./python/tcp_socket_data.csv", "w") as file:
    for i in range(len(data)):
        file.write(data[i].decode("utf-8"))
