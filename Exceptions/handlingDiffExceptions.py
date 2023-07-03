try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Must be a valid age.")
else:
    print("No exceptions was thrown my boy.")
