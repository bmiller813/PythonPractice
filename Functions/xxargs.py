def save_user(**user):
    print(user["name"])


# We can pass arbitrary keyword arguments
# The object this produces is called a dictionary
save_user(id=1, name="Bryan", age=20) 