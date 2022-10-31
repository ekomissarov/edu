'''
Ввести строку, содержащую произвольные символы (кроме символа «@»).
Затем ввести строку-шаблон, которая может содержать символы @.
Проверить, содержится ли в исходной строке подстрока,
совпадающая со строкой-шаблоном везде, кроме символов @;
на месте @ в исходной строке должен стоять ровно один произвольный символ.

Вывести позицию в строке,
с которой начинается эта подстрока или -1, если её там нет.

Input:

исходной строке подстрока, совпадающая со строкой
ст@ок@
Output:

9
'''


#srch = input("Введите строку: ")
#needle = input("Введите шаблон @: ")

srch = "исходной стXроке подстрока, совпадающая со строкой"
needle = "ст@@ок@"

'''
pointer = absposition = 0
needle = needle.split("@")
notfound = True

while notfound:

    notfound = False
    p = srch[absposition:].find(needle[0])

    if p == -1:
        print(-1)
        exit(0)
    else:

        absposition += p
        result = absposition

        for i in needle:
            pointer = srch[absposition:].find(i)
            if pointer:
                notfound = True
                break
            absposition += pointer + len(i) + 1

print(result)
'''

patt = []
n = 0

for w in needle.split("@"):
    if w:
        patt.append((n, w))
        n += len(w)
    n += 1

for i in range(len(srch) -len(needle)):
    for k, w in patt:
        if srch[i+k:i+k+len(w)] != w:
            break
    else:
        print(i)
        break
else:
    if patt or len(srch)>len(needle):
        print(-1)
    else:
        print(0)