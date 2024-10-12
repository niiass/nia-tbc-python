number = int(input("Please enter integer from 0 to 1000: "))

if number <= 0 or number > 1000:
    print("Input must be an integer from 0 to 1000!")
    exit(1)

while number != 1:
    if (number % 2 == 0):
        number /= 2
    elif (number % 2 == 1):
        number = number * 3 + 1
    print(number, sep = "; ")