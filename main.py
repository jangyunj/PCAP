my_string = "Hello World"
print(my_string.startswith("H"))
print(my_string.startswith("Hello"))
print(my_string.endswith("World"))

print(my_string.find("o"))
print(my_string.find("lo"))
print(my_string.find("p"))  #cannot find so results in -1

print(my_string.count("l"))

print(my_string.replace("Hello", "Hi"))