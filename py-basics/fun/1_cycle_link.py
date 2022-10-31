a = [1, 2]
b = [3, 4]
c = [5, 6]
a[0] = b
b[0] = c
c[0] = a
del a[1]
del b[1]
del c[1]
print(a, b, c)
print(a[0], b[0], c[0])
print(id(a), id(b), id(c))

tmp = a[0]
i = 0
while i <= 10:
    tmp = tmp[0]
    print(i, tmp, id(tmp))
    i += 1
