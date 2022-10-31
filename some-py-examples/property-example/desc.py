class Dsc:
    value = None

    def __get__(self, obj, cls):
        print(f"Get from {cls}:{obj}")
        return self.value

    def __set__(self, obj, val):
        print(f"Set {obj} to {val}")
        self.value = val

    def __delete__(self, obj):
        print(f"Delete {obj}")
        self.value = None


class C:
    data = Dsc()

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"<objname: {self.name}>"


d = C("De")
print(d.data)
d.data = 777
print(d.data)

f = C("Ef")
print(f.data)

del d.data
print(f.data)

