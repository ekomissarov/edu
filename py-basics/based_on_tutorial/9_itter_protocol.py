#https://docs.python.org/3/tutorial/classes.html#iterators
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
for char in rev:
    print(char)

#print(rev.__next__())  # одноразовый иттератор

rev1 = (1,2,3,4,5,6,7,8)
print("\nПроходим циклом первый раз")
for char in rev1:
    print(char, end=" ")

#print(rev.__next__())   # тоже одноразовый иттератор

print("\nПроходим циклом второй раз")
for char in rev1:
    print(char, end=" ")