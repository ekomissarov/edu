'''
Немного о кортежах (tuple)
это неизменяемый объект, индексируемая последовательность
'''

t = tuple(range(10))
print("id:", id(t), t)
t = t,(777,888,999)  # создается новый объект с другим id
print("id:", id(t), t)


t= ([1, 2, 3], [3, 2, 1])
print("id:", id(t), t)
t[0][1]="QKRQ"  # ссыка из tuple на список/list остается неизменной,
# поэтому нет попытки изменения tuple
print("id:", id(t), t)

# объявление кортежа из одного элемента
singleton = 'hello',
print("id:", id(singleton), "len:", len(singleton), singleton)

