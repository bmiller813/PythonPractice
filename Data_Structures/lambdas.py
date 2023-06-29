# Better way to do what "sortingLists" code does
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 13),
]


# Shorter & cleaner way to define a function we only use once
# as an argument to another function 
items.sort(key=lambda item:item[1])
print(items)