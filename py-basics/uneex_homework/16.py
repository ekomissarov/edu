'''
Ввести целые M и N, вывести последовательность
0 1 2 3 4 5 6 7 8 9 0 1 2 3 … в виде спирально
(по часовой стрелке, из верхнего левого угла)
заполненной таблицы M×N. Не забываем про то,
что M и N могут быть чётными, нечётными и неизвестно,
какое больше.

Input:

6,5
Output:

0 1 2 3 4 5
7 8 9 0 1 6
6 7 8 9 2 7
5 6 5 4 3 8
4 3 2 1 0 9
'''

M = 16
N = 8


def gen():
    while True:
        for i in range(0,10):
            yield i




mtr = [["Q" for i in range(M)] for i in range(N)]

z = gen()
y, x = 0, 0
mtr[y][x] = next(z)
step = M*N - 1
go = "right"

while step > 0:
    if go == "right":
        if x+1 >= M or mtr[y][x+1] != 'Q':
            go = "down"
        else:
            x += 1
            step -= 1
            mtr[y][x] = next(z)
    elif go == "down":
        if y+1 >= N or mtr[y+1][x] != 'Q':
            go = "left"
        else:
            y += 1
            step -= 1
            mtr[y][x] = next(z)
    elif go == "left":
        if x-1 < 0 or mtr[y][x-1] != 'Q':
            go = "up"
        else:
            x -= 1
            step -= 1
            mtr[y][x] = next(z)
    elif go == "up":
        if y-1 < 0 or mtr[y-1][x] != 'Q':
            go = "right"
        else:
            y -= 1
            step -= 1
            mtr[y][x] = next(z)


for line in mtr:
    print(*line, sep = ' ')

