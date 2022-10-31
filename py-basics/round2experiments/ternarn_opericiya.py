def fun1():
    print("fun1")


def fun2():
    print("fun2")


a = -5
b = fun1() if a>0 else fun2()

a = 5
b = fun1() if a>0 else fun2()
