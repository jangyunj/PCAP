from timeit import default_timer as timer

my_list = ['a'] * 6    #Creates a list with 6 elements

start = timer()

my_string = ''.join(my_list) #Good python code
print(my_string)

stop = timer()
print(start-stop)



my_list = ['a'] * 6
my_string = ''.join(my_list)
print(my_string)
