#Set - unordered and mutable
#    - does not allow duplicates; gets rid of duplicates
#    - no key value pairs, just single elements

# myset = set("Hello") #you can find out how many unique characters are here
# print(myset)

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)

print(myset)

for i in myset: #iterate over each elements
    print(i)

if 2 in myset:
    print("yes")