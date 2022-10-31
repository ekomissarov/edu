'''
генераторы и различные варианты генераторов
https://docs.python.org/3/tutorial/datastructures.html
'''

# создание списка в результате вычислений внутри цикла
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
del squares

# создание списка однострочным генератором
squares = list(i*i for i in range(10))
print(squares)
del squares

# или так:
squares = [i*i for i in range(10)]
print(squares)
del squares

# создав lambda функцию и примению ее к генератору с помошью map
squares = list(map(lambda x: x**2, range(10)))
print(squares)
del squares

# создав lambds функцию и примению ее к иттерируемой последовательности с помошью map
l = tuple(range(10))
squares = list(map(lambda x: x**2, l))
print(squares)
del squares


# или так:
sq_generator = (i*i for i in range(10))
# генератор не индексируемый нельзя обратиться так: sq_generator[5]
# генератор "одноразовый" он разряжается как только поучаствует в цикле (протокол иттерации)
# генератор не занимает места в памяти, т.к. вычисления происходят на ходу
squares = list(sq_generator)  # генератор "разряжается"
print(squares)
del squares

# генератор может участвовать в операции распаковки, можно сделать так
sq_generator = (i**2 for i in range(10))
print("Пример распаковки генератора", *(sq_generator))

# можно написать свою функцию генератор
def sqg(val):
    for i in range(val):
        yield i*i

squares = list(sqg(10))  # генератор "разряжается"
print(squares)
del squares

# "усложненный многомерный" генератор
a = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(a)
del a

# некоторые другие примеры конструкций
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
print(*(s for s in dir() if not s.startswith("__")), sep=", ")