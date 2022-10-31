def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


g = reverse("любая индексируемая последовательность")
print(g)

for char in g:
    print(char, end = " ")

print(g.__next__())
