# tuple - ordered collection - objects that belong together
#       - cannot be changed - IMMUTABLE
#       - needs to be more than one OR have comma at the end if it only has one item

tuple1 = ("Max", 28, "Boston")

# Unpacking
name, age, city = tuple1
print(name)
print(age)
print(city)

tuple2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
i1, *i2, i3 = tuple2
print(i1)
print(i2)  # all of the elements in BETWEEN output in a list
print(i3)
