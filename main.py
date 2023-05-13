from itertools import product
a = [1, 4]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))