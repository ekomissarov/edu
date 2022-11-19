# https://docs.python.org/3/howto/descriptor.html
class Dsc:

    def __get__(self, obj, cls):
        print(f"Get from {cls}:{repr(obj)} \t\tself - {self}")
        return obj._value

    def __set__(self, obj, val):
        print(f"Set in {repr(obj)} to {val} \t\tself - {self}")
        obj._value = val

    def __delete__(self, obj):
        print(f"Delete from {repr(obj)} \t\tself - {self}")
        obj._value = None

class C:
        data = Dsc()

        def __init__(self, name):
            self.data = name

        def __str__(self):
            return f"<{self.data}>"


#>>> c = C("Obj")
#Set in <__main__.C object at 0x7f0ce74909d0> to Obj
#>>> c._value
#'Obj'
#>>> c.data = 100500
#Set in <__main__.C object at 0x7f0ce74909d0> to 100500
#>>> c.data
#Get from <class '__main__.C'>:<__main__.C object at 0x7f0ce74909d0>
#100500
#>>> c._value
#100500
#>>> del c.data
#Delete from <__main__.C object at 0x7f0ce74909d0>
#>>> print(c.data)
#Get from <class '__main__.C'>:<__main__.C object at 0x7f0ce74909d0>
#None
#>>> C.data = "muggle"
#>>> c.data
#'muggle'
#>>> c.data = 42
#>>> c.data
#42
#>>> del c.data
#>>> c.data
#'muggle'
