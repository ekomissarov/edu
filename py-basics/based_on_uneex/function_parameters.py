def fun1(*arg1):
    print("FUN1---------------")
    print("arg1: ", arg1)
    print("*arg1: ", *arg1)

def fun2(**arg2):
    print("FUN2---------------")
    print("arg2: ", arg2)
    print("*arg2: ", *arg2)

    for k, v in arg2.items():
        print("arg2 key {} value {}".format(k,v))
        # последовательность аргументов не гарантируется до версии Python 3.6.х

def fun3(*arg1, **arg2):
    print("FUN3---------------")
    print("arg1: ", arg1)
    for k, v in arg2.items():
        print("arg2 key {} value {}".format(k, v))


a = tuple(i*2 for i in range(10))
b = {"val{}".format(i):list(range(i)) for i in range(3,7)}
print("before func:", a, b)
print("\n\n")
fun1(*a)
print("\n\n")
fun2(**b)
print("\n\n")
fun3(*a, **b)