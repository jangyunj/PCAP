from collections import defaultdict

#Returns specific type of value we specify
d = defaultdict(int)
d = defaultdict(float)
d = defaultdict(list)

d['a'] = 1
d['b'] = 2
print(d['c'])