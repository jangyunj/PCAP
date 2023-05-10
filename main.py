
setA = {1, 2, 3, 4, 5, 6}

setB = setA    #both points to the same location
setB.add(7)

print(setB)
print(setA)    #also affected

#----OR----
setB = setA.copy()

#----OR----
setB = set(setA)
