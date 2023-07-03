## You want to print individual numbers from the list
## Use unpacking operator
# numbers = [1, 2 ,3]
# print(numbers)
# print(*numbers)
# print(1, 2, 3)

## Unpacking an interable
# values = list(range(5))
# values = [*range(5), *"Hello"]
# print(values)

## Combine Multiple Lists
# first = [1, 2]
# second = [3]
# values = [*first, "a", *second, *"Hello"]
# print(values)

## Unpack Dictionaries
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)