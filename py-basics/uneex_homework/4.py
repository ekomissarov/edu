'''
Ввести небольшое натуральное число 2⩽N⩽1000000 и проверить,
является ли оно степенью натурального числа (>1).
Вывести YES или NO соответственно.

Input:

1024
Output:

YES
'''
import itertools

def PowTest(val):
    '''
    алгоритм выдуманный за 5 минут, похоже он очень медленный
    не используйте его нигде, кроме учебных целей
    :param val:
    :return:
    '''

    # определяем максимальную степень
    t = val/2
    i_max = 1
    while t > 1:
        t /= 2
        i_max += 1


    for i in range(i_max,1,-1):  # цикл по степеням
        j_max = int(100000000 ** (1 / i) + 1)

        for j in range(2, j_max):
            res = j ** i
            if res == val:
                return (j,i)
            elif res > val:
                j_max = int(100000000**(1/i)+1)
                break

    return 0





digit = int(input("Введите целое число:"))
if 2<=digit<=100000000:
    powindex = PowTest(digit)
    print("Является степенью {}".format(powindex)
          if powindex
          else "Не является степенью натурального числа >1")

else:
    print("Введенное число выходит за границы 2⩽N⩽100000000")