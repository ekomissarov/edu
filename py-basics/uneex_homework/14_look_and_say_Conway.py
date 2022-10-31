'''
Написать генератор цифр последовательности Конвея «Look and Say».
https://oeis.org/A005150
(Сама последовательность Конвея https://oeis.org/A034002).
Ввести N⩾0 и вывести N-ю цифру последовательности.

Input:

100500
Output:

2

'''

def generat_conoway1(seed):
    yield seed
    l = [int(seed)]
    s = 1
    y=''

    while True:
        x = str(l[len(l) - 1]) + 'Q'
        for i in range(len(x) - 1):
            if x[i] == x[i + 1]:
                s += 1  # счетчик количества одинаковых цифр
            else:  # как только цифры не совпадают, возвращаем счетчик к исходному состоянию сохраняем рез-т
                y += str(s)+str(x[i])
                yield s
                yield x[i]
                s = 1  # для последнего значения "Q" счетчик возвращается в 1

        l.append(int(y))
        y = ''

    # print(l) # A005150


def generat_conoway2(seed):
    yield seed
    previous = str(seed)
    seq = str(seed)
    while True:
        next = ''
        idx = 0  # счетчик количества одинаковых цифр
        l = len(previous)  # длина строки p
        while idx < l:  # проход по строке p
            start = idx
            idx += 1  # засчитываем первую цифру, изначально счетчик установлен в 0
            while idx < l and previous[idx] == previous[start]:
                idx += 1  # считаем количество цифр
            next = "{}{}{}".format(next, str(idx-start), previous[start])
        previous = next

        for i in next:
            yield i



#N = int(input("Введите N: "))
for N in range(100490, 100510):
# проход диапазона шагов: это вообще не оптимально т.к. на каждой итерации происходит
# новый пробег по всему генератору, но наглядно ))

    step = 0
    for i in generat_conoway1(9):
        N -= 1
        if N < 0:
            print("шаг {} цифра: {}".format(step, i))
            break
        step += 1

