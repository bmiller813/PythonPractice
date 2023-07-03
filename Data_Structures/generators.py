from sys import getsizeof
# Generators are iterable and generate a new value in each
# They do not store the values in memory
# This is useful for large range of numbers / infinite data streams

# List
#values = [x * 2 for x in range(10)]
#for x in values:
#    print(x)

# Generator Object
values = (x * 2 for x in range(1000000))
print("gen:", getsizeof(values))
values = [x * 2 for x in range(1000000)]
print("list:", getsizeof(values))

# Use a generator expression for situations when dealing with a large data set
# or potentially  infinite steam of data, to create a generator object
# You won't be able to get the total number of objects you're working with

print(len(values))