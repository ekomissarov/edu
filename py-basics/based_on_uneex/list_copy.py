# [UNИX][Python] Лекция 3. Стандартные типы данных и выражения-конструкторы
a=(1,1,32,215,56,43,65,75,756,7)
a=list(a)
print(a)

b=a[:]  # создание копии
c=b
d=a

print(a is b, b is c)
b[3]="!!!!" # изменяет b и c т.к. это один и тот же объект
print(a,b,c,sep='\n')
