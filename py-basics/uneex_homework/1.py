'''
Ввести два объекта Python и вывести первый непустой из них. Если оба пустые, вывести NO.

Input:
[]
123

Output:
123

'''

a = eval(input("Введите первый объект: "))
b = eval(input("Введите второй объект: "))

print("Первый не пустой объект -", a or b or "NO")