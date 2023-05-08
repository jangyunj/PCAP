odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u1 = odds.union(evens) #combination - no duplicates of same numbers
print("union: ", u1)

u2 = odds.union(primes) #combination - no duplicates of same numbers
print("union: ", u2)

i = evens.intersection(primes) #commonality
print(f"intersection: {i}")