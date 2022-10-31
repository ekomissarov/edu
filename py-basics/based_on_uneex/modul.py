'''
пример документации к модулю
'''
var = 123


def fun(a):
    '''
    документация к функции пример
    :param a:
    :return:
    '''
    return a*a


def printlist(list):
    for i in list:
        print(i)

if __name__ == '__main__':
    # этот блок не выполнится при импортировании модуля
    # но выполнится при запуске
    print("Прямой запуск модуля. Пространство имен:")
    for n in dir():
        print(n)

