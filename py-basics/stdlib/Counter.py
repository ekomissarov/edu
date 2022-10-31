'''
https://docs.python.org/3/library/collections.html#counter-objects


'''

from collections import Counter
import sys


c = Counter()
print(c)

c = Counter('gallahad')                     # a new counter from an iterable
print(c)
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
print(c)
c = Counter(cats=4, dogs=8)             # a new counter from keyword args
print(c)

print(*(i for i in dir(c) if not i.startswith("_")), sep = "\n")
print(c, sys.getsizeof(c))

for i in c.elements():
    print(i)

print(list(c), set(c), dict(c), c.items())
print(c)
c["dogs"] += 1
c["dogs"] /= 3
print(c)


print("\n\n\n")
# Find the ten most common words in Hamlet
import re
words = re.findall(r'\w+', open('../chehov.txt').read().lower())
print(Counter(words).most_common(20))
