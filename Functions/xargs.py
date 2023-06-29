# You want to use multiple arguments
# Create a parameter with a plural name (collection of arguments) & prefix with an asterix
# The only difference between [2, 3, 4, 5] and *numbers is the notation
# [] = lists, () = topo (collection of objects) -> iterable

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total   


print(multiply(2, 3, 4, 5))