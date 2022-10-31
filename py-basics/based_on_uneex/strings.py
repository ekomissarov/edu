mls = '''
qwerty qwerty
asdf asdf
xcvbxcvb xcvbcxvb
'''

print(r"\a/\b/\c/ для format существует целый мини-язык - {} \a/\b/\c/ ".format(mls))

s = 'asfiKHKLDFljshdflsdf'
print(s[0],s[1],s[2], s[3:8])  # строка - индексируемая последовательность
for i in s:
    print(i*30)

print("KHK" in s)  # алгоритм поиска используется "правильный" сложность линейная

# далее посмотрим размеры кодировок

import sys
s = "русские буквы юникод"
print(s, sys.getsizeof(s))
s+="Ы"
print(s, sys.getsizeof(s))

q = b"bite string"
print(q, sys.getsizeof(q))
q += b"Q"
print(q, sys.getsizeof(q))
print("Элементом байтовой строки является маленькое целое число, например", q[0])
# q[2] = 0 мы не можем написать для байтовой строки, т.к. она константная
# используем bytearray

Q = bytearray(b'qwerty')
Q[3] = 98
print(Q)

# преобразование байтовой строки в обучную
print(Q.decode('utf-8'), type(Q.decode('utf-8')))

