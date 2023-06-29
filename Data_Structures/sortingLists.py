# numbers = [3, 51, 2, 7, 6]
# #numbers.sort(reverse=True) # Modifies the existing list
# print(sorted(numbers, reverse=True)) # Creates a new list with the modifications
# print(numbers)

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 13),
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)