my_string = "How are you"
my_list = my_string.split()                #Each word becomes an element in a list
#SAME AS: my_list = my_string.split(" ")   #default delimiter is a space " "  
print(my_list)

#---------------------------------------
my_string = "How,are,you"
my_list = my_string.split(",")
print(my_list)

new_string = " ".join(my_list)            #Joins the list back into strings
print(new_string)



