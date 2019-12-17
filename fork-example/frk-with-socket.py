import socket
import os
import signal
from time import sleep
# https://docs.python.org/3/howto/sockets.html
# https://docs.python.org/3/library/socket.html#module-socket


def handle_signal(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(-1, os.WNOHANG)
            if pid == 0:
                return None
            else:
                print('Child PID: {} terminated with status {}'.format(pid, status))

        except OSError as msg:
            return None


def process_request(s):
    sleep(10)
    return "<<{}>>".format(s)


def handle_request(conn, addr):
    with conn:
        print('Connected by', addr)
        while True:
            request_link = conn.recv(1024)
            if not request_link:
                break
            result = process_request(request_link.decode('utf-8').strip())
            resp = str(result).encode('utf-8') + b'\n'
            client_connection.send(resp)


if __name__ == '__main__':
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(('', 33000))
    listen_socket.listen(1)
    signal.signal(signal.SIGCHLD, handle_signal)
    while True:
        client_connection, client_address = listen_socket.accept()
        pid = os.fork()
        if pid == 0:
            listen_socket.close()  # close child copy listen
            handle_request(client_connection, client_address)
            client_connection.close()
            exit(0)
        else:
            client_connection.close()
