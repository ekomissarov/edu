import socket
import json
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


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket.AF_INET - address family IPv4; socket.SOCK_STREAM - TCP
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # на случай прерывания работы скрипта, порт будет занят в течении таймаута от ОС (~3 мин),
    # чтобы данные в пути дошли до адресата, будем использовать переиспользование адреса
    server_socket.bind(('localhost', 33000))
    server_socket.listen(1)  # прослушивание порта на предмет входящего подключения
    while True:
        client_socket, client_address = server_socket.accept()  # блокирующая операция
        # accept метод серверного сокета, он принимает входящее подключение. Он читает данные из входящего буфера
        # и если на вход пришло что нибудь возвращает кортеж (сокет с другой стороны, адрес)
        # входящее подключение мы приняли
        with client_socket:  # client_socket.close() по завершении
            print('Connected by', client_address)
            while True:
                request_link = client_socket.recv(1024)  # блокирующая операция, дожидаемся входящего сообщения
                if not request_link:
                    break  # условие прерывание цикла
                result = process_incoming_message(request_link.decode('utf-8').strip())
                resp = str(result).encode('utf-8') + b'\n'
                client_socket.send(resp)  # если буфер отправки полный то это в некотором смысле блокирующая операция
