from modul import printlist

#  класс это такое именованное пространство имен


class C:
    pass


print(C)
C.field = "QQ"
print(C.field)


def fun(a):
    return a+a


C.foon = fun
print(C.foon(100500))
printlist(dir(C))


class B:
    var1 = 123

    def fun(self, a):
        print(a+a)


print(B())
ex1 = B()
ex1.fun("qwerty")

#  функция type возвращает класс
a = type(23)("12345")  # равносильно a = int("12345")
#  тип объекта он же класс объекта является конструктором экземляра класса

#  экземпляр класса вообще говоря не обязательно свзывать именем
a=[]
a.append(B())
print(a[0], a[0].var1)  # кстати это тот случай когда не работают подсказки в PyCharm

B.newfield = "QWERTY"
ex1.newfield = 0
print(ex1.newfield)
print(a[0].newfield)


'''
можно удалить поле экземпляра класса (локальное), тогда оно будет выводится из глобального 
пространства имен самого класса
'''

del ex1.newfield
print(ex1.newfield)

# все эти вещи понадобятся скорее всего чуть чаще чем никогда, но эти вещи нужно понимать