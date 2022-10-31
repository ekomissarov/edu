'''
В первой строке ввести координаты центра круга и его радиус
(числа x, y, r через запятую).
Во второй и последующих строках ввести пары чисел — координаты точек.
Ввод заканчивается парой 0,0 (она не входит в проверку!).
Вывести YES, если все точки принадлежат кругу и NO, если не все.

Input:

1,1,2
1,2
1,3
2,2
0,0
Output:

YES
'''

circle = input("Координаты центра круга и его радиус x, y, r:")
circle = tuple(float(i) for i in circle.replace(" ","").split(","))

flag = False
p = 0

while(p!=(0,0)):
    p = input("Координаты точки x, y:")
    p = tuple(float(i) for i in p.replace(" ","").split(","))
    if (p[0] - circle[0])**2 + (p[1] - circle[1])**2 > circle[2]**2:
        flag = True

if flag:
    print("No")
else:
    print("Yes")