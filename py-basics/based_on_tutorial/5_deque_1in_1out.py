#https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue)
print(queue.popleft())                 # The first to arrive now leaves
print(queue.popleft())                 # The second to arrive now leaves

print(queue)                           # Remaining queue in order of arrival
