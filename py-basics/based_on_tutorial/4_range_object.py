#https://docs.python.org/3/tutorial/controlflow.html#the-range-function
a=range(0,10,3)
print(a, type(a))
for i in a:
    print(i)

print('range не \'одноразовый\'',a)

#использование range() для иттерации по индексам последовательности
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
    
#список может быть создан на основе иттерируемого объекта класса range
print(list(range(5)))
