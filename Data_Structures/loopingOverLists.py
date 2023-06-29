# Built in function "enumerate" return the index of each item
# Returns an enumerate object which is iterable
# Gives us a topo (Like a read-only list)
letters = ["a", "b", "c"]

for index, letter in enumerate(letters): # Unpacking a topo created by the enumeration
    print(index, letter)