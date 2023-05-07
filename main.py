# tuple - ordered collection - objects that belong together
#       - cannot be changed - IMMUTABLE
#       - needs to be more than one OR have comma at the end if it only has one item
#       - can be efficient when working with large data

import sys

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

import timeit
print(timeit.timeit(stmt="[1, 2, 3]", number=1000000)) #TIME OF one million times we want to create this list
print(timeit.timeit(stmt="(1, 2, 3)", number=1000000)) #TIME OF one million times we want to create this tuple
