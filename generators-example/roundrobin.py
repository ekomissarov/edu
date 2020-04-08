from collections import deque


def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i


g1 = gen1("eugene")
g2 = gen2(10)

tasks = deque((g1, g2))

while tasks:
    task = tasks.popleft()
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass

# генераторы выполняются строго по очереди

