def greet(name):
    print(f"Hi {name}")


def get_greeting(name): # This is better because its not tied to only printing in the terminal
    return f"Hi {name}"


message = get_greeting("Bryan")