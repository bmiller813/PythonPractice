items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 13),
]

#Takes a lambda function and applied it on each item on the iterable
prices = map(lambda item: item[1], items) #Iterable
print(prices)
