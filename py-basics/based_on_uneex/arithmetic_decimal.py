#[UNИX][Python] Лекция 3. Стандартные типы данных и выражения-конструкторы
from decimal import Decimal
from fractions import Fraction

a=123123
a20=a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a
print('123123^80 =', a20*a20*a20*a20)

a=1.1+2.2
print('1.1+2.2 =', a)
a=4.4+8.8
print('4.4+8.8 =', a)
a=4.4+1.1
print('4.4+1.1 =', a)

'''
выход:
- не использовать вещественную арифметику там где можно использовать целочисленную
- использовать модуль decimal
'''

a=Decimal("1.1")+Decimal("2.2")
print('Decimal: 1.1+2.2 =', a)
print("Decimal(1.1) = ", Decimal(1.1)) #использование не строки, а числа

print('Fraction("1.1")', Fraction("1.1"))
print('Fraction(1.1)', Fraction(1.1))
