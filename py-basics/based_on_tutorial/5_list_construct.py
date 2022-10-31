#https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
from math import pi
squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

a = [(x, y) for x in [1,2,3] for y in [3,1,4] if x == y]
print(a)

a = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(a)

b = [str(round(pi, i)) for i in range(1, 6)]
print(b)
