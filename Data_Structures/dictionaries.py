# Collection of key, value pairs
# Can only use immutable types for keys

# point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10# Index, access by the key, not numeric value
point["z"] = 20
if "a" in point:
    print(point["a"])


print(point.get("a"))
del point["x"]
print(point)

for key in point:
    print(key, point[key])

for x in point.items():
    print(x)    