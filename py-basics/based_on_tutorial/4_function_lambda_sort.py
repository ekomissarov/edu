#https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[0], reverse=True)
print(pairs)

pairs.sort(key=lambda pair: pair[1])
print(pairs)
