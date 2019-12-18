import socket
import json

message = {"description": "Структура данных для передачи через socket", "value": 3.1415926}
msg = json.dumps(message).encode()

HOST = 'localhost'    # The remote host
PORT = 33000         # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(msg)
    data = s.recv(1024)

data = json.loads(data)
print('Received', repr(data))
