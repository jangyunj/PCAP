mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict["email"] = "max@abc.com"
print(mydict)

mydict["email"] = "coolmax@abc.com"
print(mydict)

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)