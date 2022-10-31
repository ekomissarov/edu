'''
https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
'''

a = [i*2 for i in "qwerty"]
print(a)

a.append("QQ")
a[len(a):] = ["QQ"]
print(a)

a.extend(range(3))
a[len(a):] = range(3)
print(a)

a.insert(1, "ZZ")
print(a)
a[1:1] = ["XX"]
print(a)

# a.insert(len(a), x) is equivalent to a.append(x)

# Remove the first item from the list whose value is x.
# It is an error if there is no such item.
a.remove("QQ")
print(a)
a.remove("QQ")
print(a)


del a[3:7]
print(a)

print(a.index("ZZ",1,4))
print(a.count(1))


