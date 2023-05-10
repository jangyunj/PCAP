greeting = "Hello"

for i in greeting:
    print(i)

if "ell" in greeting:
    print("yes")
else:
    print("no")

my_string = "      Hello World     "
my_string = my_string.strip()  #You have to assign it to the original one (make copy), because string is IMMUTABLE
print(my_string)

print(my_string.upper())
print(my_string.lower())