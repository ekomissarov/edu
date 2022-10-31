import socket
from collections import deque
from select import select

tasks = deque()
to_read = {}
to_write = {}


def process_incoming_message(s):
    print(f"debug: {s}")
    return f"Hallo from server, {s}"


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 33000))
    server_socket.listen(1)
    while True:

        yield ("read", server_socket)
        client_socket, client_address = server_socket.accept()  # read

        print('Connected by', client_address)
        tasks.append(client(client_socket))


def client(client_socket):
    while True:

        yield ("read", client_socket)
        request_link = client_socket.recv(1024)  # read

        if not request_link:
            break

        result = process_incoming_message(request_link.decode('utf-8').strip())
        resp = str(result).encode('utf-8') + b'\n'

        yield ("write", client_socket)
        client_socket.send(resp)  # write

    client_socket.close()


def event_loop():
    while any([tasks, to_read, to_write]):
        while not tasks:  # здесь заполняем задания по готовности на чтение/запись
            ready_to_read, ready_to_write, _ = select(to_read, to_write, []) # блокирующая операция теперь здесь
            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))
            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:  # здесь разбираем задания по одному слева
            task = tasks.popleft()
            reason, sock = next(task)
            if reason == "read":
                to_read[sock] = task
            elif reason == "write":
                to_write[sock] = task
        except StopIteration:
            print("Done!")


if __name__ == '__main__':
    tasks.append(server())
    event_loop()
