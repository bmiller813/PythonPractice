#f9 to add a breakpoint
#f5 to run / stop
#f10 to execute 1 statement at a time
#f11 to step into
#shift+f11 to step out of 
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply(1, 2, 3))
