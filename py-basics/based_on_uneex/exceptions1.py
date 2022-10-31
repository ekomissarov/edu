'''
исключения выполняют 2 ф-ии:
1) это такие ошибки, которые можно обработать

'''


def fun():
    print(zzz)

try:
    fun()
except Exception as e:
    print("Ooops!!", e)


print("QQ")



try:
    a = 2
    b = "qwe"
    print("step1")
    d = 1/0
    print("step2")
    c = a + b
except TypeError:
    print("Oooooops!")
except ZeroDivisionError:
    print("/ ZERO деление на 0")


# самостоятельное определение исключений (но не BaseException)
class A(Exception): pass
class B(A): pass
class C(B): pass

for E in A,B,C:
    try:
        if E is not A:
            raise E("Параметр исключения1", "парам2", "парам3")
    except C as EX:
        print("raising C:", type(EX), EX.args, EX)
    except B:
        print("raising B")
    except A:
        print("raising A")
    # Если поменять местами C, B то вывод будет: A->B->B т.к. исключение - дерево классов
    else:
        print ("Не возникло исключений!!!")
    finally:
        print ("Возникли исключения или не возникли, все равно это выполнится")
