class Dsc:
    value = None

    def __get__(self, obj, cls):
        print(f"Get from {cls}:{obj}")
        return self.value

    def __set__(self, cls, val):
        print(f"Set {cls} to {val}")
        self.value = val

    def __delete__(self, cls):
        print("Delete {cls}")
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

