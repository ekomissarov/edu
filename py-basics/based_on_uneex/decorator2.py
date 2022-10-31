'''

пример приближенный к жизни с декораторами

'''

class C:
    val = 100500
    def method(self):
        print(self)
        return self.val

    @classmethod  # привел к тому что вместо self, в наш метод приехал его тип (класс его)
    def cmethod(cls):
        print(cls)
        return cls.val

    @staticmethod
    def smethod():
        print("QQ", dir())



c = C()
c.val = 42
print(c.method(), "\n")
print(c.cmethod(),"\n")
print(c.smethod(),"\n")

print(c.method, c.cmethod, c.smethod, sep="\n")