s = '0123456789'
obj = range(0, len(s))  #(start, stop, (step)) 
print(obj)
l = []
for i in obj:
    l.append(int(s[i]))
print(l)                #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

add = 0
for i in obj:
    add = add + l[i]    #Sums all numbers in l (above)
print(add)
