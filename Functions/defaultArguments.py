# If we don't supply a second argument, the default will be 1 in this case
# All Optional Parameters should come AFTER the required ones
def increment(number, by=1): 
    return number + by


print(increment(2, 5))