#https://docs.python.org/3/tutorial/datastructures.html
a = [1,2,3]
a.append((1,2,3)) # a[len(a):] = [x], a.insert(len(a), x)
a.extend((1,2,3)) # a[len(a):] = iterable
print(a)

a.insert(2,'x') 
print(a)

a.remove('x')
print(a)

a.pop()
print(a)

a.pop(len(a)-2)
print(a)

print(a.index(3)) # возвращает индекс элемента list.index(x[, start[, end]])

a.clear() # del a[:]
print('#', a)

# list.count(x) Return the number of times x appears in the list.
# list.sort(key=None, reverse=False)
# list.reverse() Reverse the elements of the list in place.
# list.copy() Return a shallow copy of the list. Equivalent to a[:]
