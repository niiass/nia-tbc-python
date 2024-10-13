number = int(input("Enter positive number: "))

if number < 1 or number > 49:
    print("Number must be positive integer from 1 to 49")
    exit(1)

factors = 0

while number > 0:
    print(number, "- ", end="")
    for i in range(number):
        if number % (i+1) == 0:
            print(i+1, end = " ")
            factors += 1
            if factors == 3:
                break
    factors = 0
    number -= 1
    print()
