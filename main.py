list_org = ["banana", "cherry", "apple"]
# list_copy = list_org                    #both lists refer to the same memory location
# list_copy.append("lemon")

list_copy = list_org.copy()  # makes a copy
list_copy.append("lemon")

list_copy = list(list_org)  # makes a copy

list_copy = list_org[:]  # Slices from beginning to end --makes a copy

print(list_copy)
print(list_org)
