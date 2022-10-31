class Desc:
    var = 0
    def __set__(self, instance, value):
        print("Set {} of {}".format(value, instance))
        self.var = value

    def __get__(f, instance, owner):
        print("Get from {} (class {})".format(instance, owner))
        return self.var

    def __delete__(self, instance):
        print("Del from", instance)

    def qq(self):
        pass

class C:
    fld = Desc()

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

c = C("QKRQ")
print(c)
print ([i for i in dir(c) if not i.startswith("__")])
print (c.__dict__)

c.fld = 100500  # поле класса не перебивается локальным значением в экземпляре класса
print(c.fld)

'''
Бонусы:
1) контроль присваивания и отдачи поля
2) не распухает __dict__
'''

d = C("QQ")
print(d.fld)
d.fld = 7777  # изменится во всех экземплярах, если целенаправленно это не обработать
print(c.fld)
print(d.fld)

print(C.fld)  # вместо объекта просто приедет None
# C.fld = 3  # перебьет поле класса, был дескриптор, станет константа числовая

# так же операция с дескриптором имеет более высокий приоритет, чем с полем в __dict__
# это кстати говоря быстрее работает
c.__dict__["fld"] = "ZZZXZZZ"
print(c.__dict__)
print("операция с дескриптором имеет более высокий приоритет", c.fld)

