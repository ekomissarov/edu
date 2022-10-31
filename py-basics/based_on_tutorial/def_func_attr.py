'''
https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
учебный скрипт ===
Значения функций по умолчанию (иллюстрация вычасления аргументов один раз,
но не при каждом вызове функции)

для понимания лучше визуализировать код здесь http://pythontutor.com/visualize.html

Important warning: The default value is evaluated only once.
This makes a difference when the default is a mutable object such as a list,
dictionary, or instances of most classes.
For example, the following function accumulates the arguments passed
to it on subsequent calls: grow1

If you don’t want the default to be shared between subsequent calls,
you can write the function like grow2


'''
def grow1(a, b=[]):
    print(id(b), b, type(b), end=' - ')
    b.append(a)
    print(b)

print("пробуем первую функцию grow:")
grow1(1)
grow1(2)
grow1(3)
grow1(4,["qq","ww"])



def grow2(a, b=None):
    print(id(b), b, type(b), end=' - ')
    if b == None: b = []
    b.append(a)
    print(id(b), b)

print("пробуем вторую функцию grow:")
grow2(1)
grow2(2)
grow2(3)


def fun1(a, b=7777):
    print(id(b), b, type(b), end=' - ')
    b += a
    print(id(b), b)

print("пробуем первую функцию fun:")
fun1(100000)
fun1(200000)
fun1(300000)


def fun2(a, b=None):
    print(id(b), b, type(b), end=' - ')
    if b == None: b = 0
    b += a
    print(id(b), b)

print("пробуем вторую функцию fun:")
fun2(100000)
fun2(200000)
fun2(300000)
