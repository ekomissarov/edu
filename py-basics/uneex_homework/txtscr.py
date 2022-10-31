#!/usr/bin/env python3
'''
Рисование фигур из символов на текстовом экране
'''
class txtscr():

    def __init__(self, width, height, paper="."):
        """Создаёт пустой экран (список строк) размером width×height,
        в качестве пустых элементов использовать строку paper.
        Сохраняет экран.
        """
        self.width = width
        self.height = height
        self.screen = [paper*width for i in range(height)]

    def __str__(self):
        """Преобразует экран в строку"""
        sep = "+" + "-" * len(self.screen[0]) + "+"
        #return sep + "\n" + "\n".join("{:>2}".format(n) + "|" + s + "|" for n, s in enumerate(self.screen)) + "\n" + sep
        return sep + "\n" + "\n".join("|" + s + "|" for s in self.screen) + "\n" + sep


    def dot(self, x, y, ink="*"):
        """Ставит точку (нулевой символ строки ink) на экран screen по координатам x:y
        Выход за границы экрана обрезается по модулю
        """
        x = x % self.width
        y = y % self.height
        self.screen[y] = "{}{}{}".format(self.screen[y][:x], ink[0], self.screen[y][x+1:])

    def t_dot(self, x0, y0, x1, y1, axis="y"):
        if axis == "y":
            xn, yn = x0+x0-x1, y1
        elif axis == "x":
            xn, yn = x1, y0+y0-y1
        else:
            xn, yn = x0 + x0 - x1, y0+y0-y1
        return (xn, yn)



    def get(self, x, y):
        """Возвращает символ экрана screen по координатам x,y
        Выход за границы экрана обрезается по модулю
        """
        x = x % self.width
        y = y % self.height
        return self.screen[y][x]

    def hline(self, x, y, x1, ink="*"):
        """Проводит горизонтальный отрезок из символов ink на экране screen
        начиная с точки x:y и заканчивая точкой x1:y (координаты неотрицательные)"""
        for x0 in range(x, x1+1) if x < x1 else range(x1, x+1):
            self.dot(x0, y, ink)

    def vline(self, x, y, y1, ink="*"):
        """Проводит вертикальный отрезок из символов ink на экране screen
        начиная с точки x:y и заканчивая точкой x:y1 (координаты неотрицательные)"""
        for y0 in range(y, y1+1) if y < y1 else range(y1, y+1):
            self.dot(x, y0, ink)

    def line(self, x0, y0, x1, y1, ink="*"):
        """Проводит произвольный отрезок из символов ink на экране screen
        начиная с точки x0:y0 и заканчивая точкой x1:y1 (координаты неотрицательные)"""
        x, y = x0, y0
        if x0 == x1:
            return self.vline(x, y0, y1, ink)
        if y0 == y1:
            return self.hline(x, y0, x1, ink)

        dx, dy = -1 if x1 < x0 else 1, -1 if y1 < y0 else 1
        self.dot(x, y, ink)
        n = max(abs(x0-x1), abs(y0-y1))
        for i in range(n+1):
            x, y = x0 + (x1 - x0) * i // n, y0 + (y1 - y0) * i // n
            self.dot(x, y, ink)

    def fill(self, x, y, ink="#", paper="."):
        """Закрашивает связную область экрана screen из символов paper
        символами ink
        """
        turn = (0, 1), (1, 0), (0, -1), (-1, 0)
        todo = [(x, y)]
        while todo:
            x, y = todo.pop()
            self.dot(x, y, ink)
            for dx, dy in turn:
                if self.get(x+dx, y+dy) == paper:
                    todo.append((x+dx, y+dy))

    def rectangle(self, x0, y0, w, h, ink="@"):
        """
        прямоугольник со сторонами, параллельными осям координат
        """
        for x in range(x0, x0 + w):
            self.dot(x, y0, ink)
            self.dot(x, y0 + h - 1, ink)
        for y in range(y0 + 1, y0 + h - 1):
            self.dot(x0, y, ink)
            self.dot(x0 + w - 1, y, ink)

    def zigzag(self, *values):
        v = iter(values)

        x0, y0 = next(v)
        try:
            while True:
                x1, y1 = next(v)
                self.line(x0, y0, x1, y1, "*")
                x0, y0 = x1, y1
        except StopIteration:
            pass
        finally:
            del v

    def circle(self, x0, y0, r, ink="0"):
        from math import sqrt
        from math import ceil

        x1, y1 = x0, y0 + r
        for x2 in range(x0, x0 + r + 1):
            y2 = ceil(sqrt(r**2 - (x2 - x0)**2) + y0)
            self.line(x1, y1, x2, y2, ink)

            self.line(*self.t_dot(x0, y0, x1, y1, "y"),
                      *self.t_dot(x0, y0, x2, y2, "y"),
                      ink)
            self.line(*self.t_dot(x0, y0, x1, y1, "x"),
                      *self.t_dot(x0, y0, x2, y2, "x"),
                      ink)
            self.line(*self.t_dot(x0, y0, x1, y1, "xy"),
                      *self.t_dot(x0, y0, x2, y2, "xy"),
                      ink)

            x1, y1 = x2, y2





def fish():
    scr = txtscr(80,20)
    scr.vline(4,2,18,"+")
    scr.hline(2,4,55,"@")
    scr.line(0,12,57,38)
    scr.line(10,19,58,7,"%")
    scr.line(10, 11, 11, 10, "`")
    scr.fill(20, 10)
    print(scr)

def rectangle():
    scr = txtscr(60,20)
    scr.rectangle(2,2,4,4)
    scr.rectangle(10, 10, 10, 4)
    scr.rectangle(30, 15, 8, 8)
    print(scr)

def zigzag():
    scr = txtscr(60,20)
    scr.zigzag((2,2),(4,4),(1,5),(6,8),(10,13),(13,19),(60,0))
    print(scr)

def circle():
    scr = txtscr(60,20)
    scr.circle(10, 10, 5)
    print(scr)


if __name__ == "__main__":
    circle()
