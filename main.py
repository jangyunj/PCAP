#Double ended que - add/remove elements from both ends
from collections import deque

d = deque()

d.append(1)
d.append(2)
d.appendleft(3)
print(d)

# d.pop()
# d.popleft()
# d.clear()
# d.extend([4, 5, 6])
d.extendleft([4, 5, 6]) #adds backwards
print(d)

d.rotate(1) #rotates (moves) 1 place to the RIGHT
d.rotate(-1) #rotates 1 place to the LEFT
print(d)