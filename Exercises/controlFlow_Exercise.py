# print even  numbers up to 8, anything after prints "We have 4 even numbers"
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
    #elif count > 4:
        #print("We have 4 even numbers")
print(f"We have {count} even numbers")
