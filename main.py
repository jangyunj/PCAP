
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff1 = setA.difference(setB) #Takes from setA - setB
print(diff1)

diff2 = setB.difference(setA) #Takes from setB - setA
print(diff2)

diff3 = setA.symmetric_difference(setB) #Takes everything that's not overlapping
print(diff3)

diff4 = setB.symmetric_difference(setA) #Same as diff3
print(diff4)

setA.update(setB) #Without duplicates, adds elements found in another set
print(setA)

setA.intersection_update(setB) #Elements found in both sets
print(setA)

setA.difference_update(setB) #Updates the set by removing elements found in another set
print(setA)

setA.symmetric_difference_update(setB) #Updates the set by output of elements in A & B after removing duplicates
print(setA)