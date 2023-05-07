# tuple - ordered collection - objects that belong together
#       - cannot be changed
#       - needs to be more than one OR have comma at the end if it only has one item

mytuple = "Max",
print(mytuple)

print(type(mytuple))


mytuple1 = tuple(["Max", 28, "Boston"])
print(mytuple1)

item = mytuple1[2]
print(item)
