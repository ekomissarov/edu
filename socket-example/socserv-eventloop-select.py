import socket
import json
from select import select  # работает со всем у чего есть файловый дескриптор .fileno()

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


def accept_connection(server_socket):
    client_socket, client_address = server_socket.accept()
    print('Connected by', client_address)
    to_monitor.append(client_socket)


def send_message(client_socket):
    request_link = client_socket.recv(1024)  # дожидаемся входящего сообщения
    if request_link:
        result = process_incoming_message(request_link.decode('utf-8').strip())
        resp = str(result).encode('utf-8') + b'\n'
        client_socket.send(resp)  # если буфер отправки полный то это в некотором смысле блокирующая операция
    else:
        client_socket.close()


def event_loop():
    global to_monitor
    while True:
        to_monitor = list(filter(lambda x: x.fileno() != -1, to_monitor))
        ready_to_read, _, _ = select(to_monitor, [], [])  # read, write, errors
        for soc in ready_to_read:
            if soc is server_socket:
                accept_connection(soc)
            else:
                send_message(soc)


to_monitor = []
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET - address family IPv4; socket.SOCK_STREAM - TCP
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# на случай прерывания работы скрипта, порт будет занят в течении таймаута от ОС (~3 мин),
# чтобы данные в пути дошли до адресата, будем использовать переиспользование адреса
server_socket.bind(('localhost', 33000))
server_socket.listen(1)  # прослушивание порта на предмет входящего подключения


if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
