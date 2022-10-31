#[UNИX][Python] Лекция 4. Множества, словари, строки и функции
a=[(i,j) for i in range(3) for j in range(3)]
print('циклический конструктор [(i,j) for i in range(3) for j in range(3)]\n', a, '\n')

a=[(i,j) for i in range(3) for j in range(3) if j!=1]
print('циклический конструктор [(i,j) for i in range(3) for j in range(3) if j!=2]\n', a, '\n')
