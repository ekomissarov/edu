import datetime

# https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting
# https://docs.python.org/3/library/string.html#formatspec
# форматная строка - фактически генератор шаблона

# Python 3.6
a, b = 200, 4.4
print(f"{a} + {b} = {a+b}")

# можно даже так, но об этом больно думать
# print(f"{a} + {b + int(input())} = {a+b}")

# фактически для каждой скобки {} вызывается eval()
# главное выражение не вводится, вводится само содержимое объектов a, b
# все что питон может вычислить мы сами явно пишем в этой строке, поэтому это безопаснее чем eval(input()) ;)

b = 4.34523452345234532453245
print(f'в экспоненциальной форме {b:e}')
print(f'в фиксированной форме {b:f}')
print(f'50 символов поле, 3 значащих цифры {b:50.3}')
print(f'50 символов поле, 3 значащих цифры {b:050.3}')

a = 3
print(f'50 символов поле, 3 значащих цифры {a:03}')

a = 12
print(f'по правой границе #{a:7}#')
print(f'по правой границе #{a:=7}#')
print(f'по левой границе #{a:<7}#')
print(f'по центру #{a:^7}#')

coord = (3, 5)
print(f'X: {coord[0]};  Y: {coord[1]}')
print(f"repr() shows quotes: {'test'!r}; str() doesn't: {'test'!s}")


print('{:+f}; {:+f}'.format(3.14, -3.14))  # show it always
print('{: f}; {: f}'.format(3.14, -3.14))  # show a space for positive numbers
print('{:-f}; {:-f}'.format(3.14, -3.14))  # show only the minus -- same as '{:f}; {:f}'
print('{:.1f}; {:.1f}'.format(3.14, -3.14))  # show only the minus -- same as '{:f}; {:f}'

d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print(f'{d:%Y-%m-%d %H:%M:%S}')

for align, text in zip('<^>', ['left', 'center', 'right']):
    print(f'{text:{align}{align}32}')

print(f'{"QKRQ":z>32}')


name = "Eric"
profession = "comedian"
affiliation = "Monty Python"
message = (
    f"Hi {name.upper()}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
)
print(message)


import timeit
print(timeit.timeit("""name = "Eric"
age = 74
'%s is %s.' % (name, age)""", number = 10000))

print(timeit.timeit("""name = "Eric"
age = 74
'{} is {}.'.format(name, age)""", number = 10000))

print(timeit.timeit("""name = "Eric"
age = 74
f'{name} is {age}.'""", number = 10000))

