#https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, ' = ', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'простое число, делитель не найден')

print('\n------------------')
for num in range(2, 10):
    if num % 2 == 0:
        print("Четное число -", num)
        continue
    print("Не четное -", num)
