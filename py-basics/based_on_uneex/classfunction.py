from modul import printlist

print("\n\nCLASS C илюстрация к bound method передача параметра self")

class C:
    pass

def fun(*par):
    print(par)


C.foon = fun

print(C.foon)
C.foon("qwerty")


b = C()
print(b.foon)
b.foon("asdfg")  # внезапно у метода класса есть еще 1 параметр (ссылка на экземпляр)
# это сделано чтобы можно было обращаться к своим собственным полям







print("\n\nCLASS B илюстрация к пространству имен")
class B:
    var = 100500
    def fun(self, a):
        self.Another = self.var*2+a
        return 42

b = B()
print(*(s for s in dir(b) if not s.startswith("_")))
print(b.fun(33))
print(*(s for s in dir(b) if not s.startswith("_")))  # образовалось еще одно поле Another

B.newAnother="one"
print("класс:", *(s for s in dir(B) if not s.startswith("_")))  # образовалось еще одно поле newAnother
print("экземпляр:", *(s for s in dir(b) if not s.startswith("_")))  # образовалось еще одно поле newAnother


# k = l = m = B() # создаст 3 ссылки на один и тот-же экземпляр класса

# создание трех разных экземпляров класса
k = B()
l = B()
m = B()
print("var внутри экземпляров класса:", k.var, l.var, m.var)
k.var = 777
print("var внутри экземпляров класса:", k.var, l.var, m.var)
print("id var внутри экземпляров класса:", id(k.var), id(l.var), id(m.var))
del k.var  # после удаления переменной в экземпляре класса она будет разрешаться за счет
# переменной внутри пространства имен объявления класса
# поле экземпляра убить можно, поле класса можно убить только через сам класс
print("var внутри экземпляров класса:", k.var, l.var, m.var)
print("id var внутри экземпляров класса:", id(k.var), id(l.var), id(m.var))






print("\n\nCLASS A __INIT__ илюстрация создания полей при инициализации экземпляра")
class A:
    def __init__(self, start):
        print("инициализация полей в момент создания экземпляра класса")
        self.start = start
        self.Another = 0

    def fun(self, a):
        self.start += 1
        self.Another += a

print(*(s for s in dir(A) if not s.startswith("_")))
a = A(100)
print(*(s for s in dir(a) if not s.startswith("_")))

