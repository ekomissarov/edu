class C:
    def __iter__(self):
        return iter("QWA")


c = C()
for i in c:
    print(i)

print(list(c))

# если нет метода __iter__, но есть __getitem__ и __len__ оба
# то из него тоже можно сделать итератор (он будет поддерживать протокол итерации)

# аналогично для __reversed__ может быть заменен на __getitem__ и __len__ оба
# __contains__ ==> a in x

