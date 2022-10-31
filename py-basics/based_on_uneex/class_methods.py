import random

class C:
    def __init__(self, per1, per2):
        self.val, self.res = per1, per2

    def __str__(self):
        return "строковое представление для print <{}:{}>".format(self.val, self.res)

    def __repr__(self):
        return "repr представление <{}:{}> {}".format(self.val, self.res, type(self))

    def __bool__(self):
        return self.val != self.res  # плохая идея т.к. false - по умолчанию нулевой объект

    def __len__(self):
        return self.val+self.res  # довольно бессмысленно, так никто не делает, это для иллюстрации

    def __getattr__(self, item):
        if item == "random":  # обеспечение доступа пользователя к вычисляемым значениям
            return random.randrange(10)
        return "NOPE"  # опять же так никто не делает :)

    def __setattr__(self, key, value):
        # self.__dict__.update({key: value})
        self.__dict__[key] = value
        print("вызов __setattr__", self.__dict__)

    #def __del__(self): # вызывается когда refcounter на объект становится равным 0


c = C(12,56)
print(c)

if c:  # использует результат __bool__()
    print("QQ true")
else:
    print("QKRQ - false")


print("len(c) =", len(c))  # использует результат __len__()

# но с len будет работать еще и такая штука (если не описан __bool__()):
print(c or "NOT")  # c не пустое оно и вывелось
print(False or "NOT")  # для сравнения


print(c.__dict__, c.asdfg)  # отрабатывает метод __getattr__
# сначала он пошарит в __dict__ если не найдет обратится к __getattr__
# и попробует его скалькулировать
# метод __getattribute__ вызывается перед этим (очень опасная штука)
# __setattr__ - когда присваеваем значение какому либо атрибуту (возможно не существующему)
# __delattr__ - когда удаляем, можно удалить любое поле любого объекта, (если сами его сделали)
# __dir__ - можно переписать чтобы он все это показывал
# с этими методами требуется аккуратная работа, чтобы избегать рекурсивных вызовов и др. проблем, ЧИТАТЬ ДОКУМЕНТАЦИЮ

c.newvalue = 7
print(c.random, c.random, c.random)
c.random = 5
print(c.random, c.random, c.random) # теперь будет 5 5 5
del c.random
print(c.random, c.random, c.random)


print(hasattr(c, "newvalue"))
print(hasattr(c, "random")) # тоже True, так как функция обращается к __getattr__

