
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}
print(setA.issubset(setB)) #Are all elements in first set in second set?

print(setB.issubset(setA))

print(setB.issuperset(setA)) #Opposite of subset

print(setA.isdisjoint(setB)) #Are there any common elements?

print(setA.isdisjoint(setC))