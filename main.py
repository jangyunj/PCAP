# tuple - ordered collection - objects that belong together
#       - cannot be changed - immutable
#       - needs to be more than one OR have comma at the end if it only has one item

mytuple = tuple(["Max", 28, "Boston"])  # converts from list to tuple
print(mytuple)

for i in mytuple:
    print(i)

if "Tim" in mytuple:
    print("yes")
else:
    print("no")
