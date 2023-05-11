from collections import Counter

a = "aaabbbccccc"
my_counter = Counter(a)
print(my_counter)

print(my_counter.most_common(1)) #returns list with tuples inside
print(my_counter.most_common(1)[0][0]) #access the first list, first item

print(list(my_counter.elements())) #iterable over all elements - so print as list 