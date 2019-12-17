import socket
import json

message = {"qq": 1, "ww": 2}
msg = json.dumps(message).encode()

HOST = 'localhost'    # The remote host
PORT = 33000         # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(msg)
    data = s.recv(1024)
print('Received', repr(data))
