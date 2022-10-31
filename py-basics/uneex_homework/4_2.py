'''
матрицы, вложенные структуры

https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
'''

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(len(matrix[0]))])

# оно же более подробно
transposed = []
for i in range(len(matrix[0])):  # цикл по столбцам
    transposed.append([row[i] for row in matrix])  # цикл по строкам
print(transposed)


# оно же еще подробнее
transposed = []
for i in range(len(matrix[0])):  # цикл по столбцам
    transposed_raw = []
    for raw in matrix:  # для каждого i-ого столбца разворачиваем строки
        transposed_raw.append(raw[i])
    transposed.append(transposed_raw)

print(transposed)

#  с помошью функции zip
transposed = list(zip(*matrix))
print(transposed)

#  по другому с предварительной распаковкой
a, *b = matrix
print(tuple(zip(a, *b)))


# пример использования del и
a = [i**2 for i in range(10)]
print(a)
del a[3:4] # удалит 3-ий элемент (это полуинтервал)
# удаление приводит к переиндексированию массива, см результат вывода массива
for k,v in enumerate(a):  # enumerate позволяет бесплатно получить сразу ключ, значение
    print(k,v)