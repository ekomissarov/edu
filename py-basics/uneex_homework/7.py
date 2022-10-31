'''
Ввести последовательность S и вывести второй максимум этой последовательности,
т. е. элемент a∈S : ∃ b∈S : b>a и a⩾c ∀c∈S, c≠b.
Если второго максимума нет, вывести NO.
Пользоваться функциями наподобие max() или sorted() нельзя.

Input:

3,4,5,6,7
Output:

6
'''
S = tuple(eval(input("Введите последовательность S: ")))
print(S)

max = max_old = S[0]

for i in S:
    if i > max :
        max_old, max = max, i

print(max_old)