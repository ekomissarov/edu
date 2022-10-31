'''
Ввести текст, состоящий из нескольких строк (заканчивается пустой строкой).
Каждая строка состоит из «слов» (последовательностей непробельных символов),
разделённых пробелами или табуляциями.

Некоторые слова — целые числа (возможно, отрицательные),
другие числами не являются (хотя могут содержать цифры).
Найти и вывести наибольшее из этих чисел.

Input:

enemies -565 glanduliform h252Tbeaic -tv5naa2re4 55 silicamortar eared
ra50ertc-8 -4 94 ohgutyd38 163 -562 u8e8qisn handout crossword 22s4cico
-v80s6eessl beaning en1A1i-2l 545 december flo ch00a0-h1t vignettist
­­
Output:

545
'''

'''
text = ""
inp = True

while inp:
    inp = input("#> ")
    text = "{} {}".format(text, inp)



result = []
text = text.split(" ")
for i in text:
    if i.startswith("-"):
        i = i.replace("-", "", 1)
        if i.isdigit():
            result.append(-1 * int(i))
    else:
        if i.isdigit():
            result.append(int(i))

print(max(result))
'''

inp = []
s  = input("#> ")
while s:
    inp.append(s)
    s = input("#> ")

res = "\n".join(inp)
Max = None

for w in res.split():
    if w.isdecimal() or w[0] == "-" and w[1:].isdecimal():
        if Max is None or Max < int(w):
            Max = int(w)

print(Max)