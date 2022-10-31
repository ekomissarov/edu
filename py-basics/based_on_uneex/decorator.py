def fun(*argp, **argn):
    print("INFUNC:", argp, argn)
    return 7777

def fwrap(f, *argp, **argn):
    print("WRAP:", argp, argn)
    res = f(*argp, **argn)
    print("WRAP:", res)
    return res

def fdec(f):
    def funct(*argp, **argn):
        print("WRAP:", argp, argn)
        res = f(*argp, **argn)
        print("WRAP:", res)
        return res
    return funct

def decorat(f):
    def fun(*argp, **argn):
        print("QQ")
        return f(*argp, **argn)
    return fun

a = tuple(i*2 for i in range(10))
b = {"val{}".format(i):list(range(i)) for i in range(3,7)}
z = fwrap(fun, *a, **b)
y = fdec(fun)(*a, **b)
print(z, y, "\n\n")

fun = fdec(fun)  # (*1)
fun(*a, **b)
print("-"*30,"\n")
# осталось только навести немного синтаксического сахара,
# который избавит нас от вот таких вот волшебств (*1)
# (*1) может быть силььно удалено в коде от описания функции, эту проблему тоже решим

@decorat
@fdec
def decfun(a,b,c):
    return a+b+c

decfun(1,2,3)

