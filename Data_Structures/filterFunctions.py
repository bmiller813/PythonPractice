items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 13),
]

x = list(filter(lambda item: item[1] >= 10, items))
print(x)