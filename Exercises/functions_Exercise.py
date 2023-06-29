# If %3 = Fizz, %5 = Buzz, %5 & 3 = FizzBuzz
def fizz_buzz(input):
    fizz = (input % 3 == 0)
    buzz = (input % 5 == 0)
    if fizz and buzz:
        return "FizzBuzz"
    elif fizz:
        return "Fizz"
    elif buzz:
        return "Buzz"


print(fizz_buzz(30))