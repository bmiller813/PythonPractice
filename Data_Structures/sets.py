# Removes dublicates
# Sets defined by {}
# Sets are not in sequence, unordered (no index)

numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second) # A union of 2 sets
print(first & second) # Intersects 
print(first - second) # Difference
print(first ^ second) # Either in first or second but not both

if 1 in first:
    print("yes")