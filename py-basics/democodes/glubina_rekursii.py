def fun(a):
    print(a)
    a+=1
    return fun(a)

try:
    fun(0)
except RecursionError as msg:
    print(msg)