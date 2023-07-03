try:
    age = int(input("Age: "))
except ValueError as ex:
    print("Please enter a valid age my boy")
    print(ex)
    print(type(ex))
else:
    print("No exceptions thrown, proceed cuh")
print("Execution continues.")