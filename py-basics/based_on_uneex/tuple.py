# [UNИX][Python] Лекция 3. Стандартные типы данных и выражения-конструкторы
from math import sin

a,b,c = 1,2,3
print('(1,2,3) тип:', type((1,2,3)))

z=(1,2,'sfas',[1,2,3,4],sin)
print(z)
print(dir(z))
print(z[4])
print('\n\n')

s=((1,2),(3,4),(5,6))
for i in s: print(i)
for i,j in s: print(i,' * ',j, ' = ', i*j)
print('\n\n')

a=(1,1,32,215,56,43,65,75,756,7)
print(a)
print(a[3:6])
print(a[3::2])
print(a[9:2:-1])
print(a[-4:-1]) #от -4 с конца до -1 с конца
print(id(a),id(a[:]), a is a[:]) #копия - одно и то же т.к. список не изменяемый
