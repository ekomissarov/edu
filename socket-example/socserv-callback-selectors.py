import socket
import json
import selectors

# https://docs.python.org/3/howto/sockets.html
# https://docs.python.org/3/library/socket.html#module-socket
# https://www.youtube.com/watch?v=ZGfv_yRLBiY&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8&index=1
# можно подключиться через браузер, telnet или nc localhost 33000


def process_incoming_message(s):
    print(f"debug: {s}")
    try:
        s = json.loads(s)
        s['value'] = 2.718281828
    except json.decoder.JSONDecodeError:
        pass
    except TypeError:
        pass
    return json.dumps(s)


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 33000))
    server_socket.listen(1)

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)
    # зарегистрировали наш файловый объект, серверный сокет


def accept_connection(server_socket):
    client_socket, client_address = server_socket.accept()
    print('Connected by', client_address)

    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)
    # зарегистрировали наш файловый объект, клиентский сокет


def send_message(client_socket):
    request_link = client_socket.recv(1024)  # дожидаемся входящего сообщения
    if request_link:
        result = process_incoming_message(request_link.decode('utf-8').strip())
        resp = str(result).encode('utf-8') + b'\n'
        client_socket.send(resp)  # если буфер отправки полный то это в некотором смысле блокирующая операция
    else:
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    while True:

        events = selector.select()  # (key, events), events это битовая маска события чтение/запись, нужен первый элемент
        # SelectorKey - named tuple из collections

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


selector = selectors.DefaultSelector()

if __name__ == '__main__':
    server()
    event_loop()
