'''
A heapsort can be implemented by pushing all values onto
a heap and then popping off the smallest values one at a time:

This is similar to sorted(iterable), but unlike sorted(), this implementation is not stable.
'''
from heapq import *
import itertools

def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

'''
Heap elements can be tuples. 
This is useful for assigning comparison values 
(such as task priorities) alongside the main record being tracked:

'''
h = []
heappush(h, (5, 'write code'))
heappush(h, (7, 'release product'))
heappush(h, (1, 'write spec'))
heappush(h, (3, 'create tests'))
print(h)
print(heappop(h))

heappush(h, (7, 'str1'))
heappush(h, (7, '123'))
heappush(h, (5, 'abc'))

print(h)
print(heappop(h))
print(heappop(h))
print(heappop(h))
print(heappop(h))
print(heappop(h))
print(heappop(h))



pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

pass
