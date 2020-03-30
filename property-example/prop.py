class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        print("GETTER")
        return self._x

    @x.setter
    def x(self, val):
        print("SETTER")
        self._x = val

    @x.deleter
    def x(self):
        print("DELETTER")
        del self._x

c=C()
print(dir(C))
print(dir(c))

print(c.x)
c.x = "QQ!"
print(c.x)
