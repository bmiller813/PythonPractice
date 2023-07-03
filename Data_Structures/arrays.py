from array import array

# Use arrays only when dealing with a large sequence of numbers & you encounter performance problems
# In other cases, use lists and tuples
numbers = array("i", [1, 2, 3])
numbers[0] = 1