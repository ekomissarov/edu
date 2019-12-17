import socket
# https://docs.python.org/3/howto/sockets.html
# https://docs.python.org/3/library/socket.html#module-socket


def process_request(s):
    return "<<{}>>".format(s)


if __name__ == '__main__':
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(('', 33000))
    listen_socket.listen(1)
    while True:
        client_connection, client_address = listen_socket.accept()
        with client_connection:
            print('Connected by', client_address)
            while True:
                request_link = client_connection.recv(1024)
                if not request_link:
                    break
                result = process_request(request_link.decode('utf-8').strip())
                resp = str(result).encode('utf-8') + b'\n'
                client_connection.send(resp)
