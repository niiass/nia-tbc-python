import random

number = int(input("Please enter positive integer: "))

if number <= 0 or number >= 30:
    print("Number must be positive integer from 1 to 29!")
    exit(1)

max = 0

print("Generaed random numbers are: ", end = "")
for i in range(number):
    rand = random.randint(0, 1000)
    print(rand, end = " ")
    if (rand > max):
        max = rand

print('\n', "Maximum generated number is ", max)