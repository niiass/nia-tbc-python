number = int(input("Please enter positive integer: "))

if number <= 0 or number >= 1000:
    print("Number must be positive integer from 1 to 999!")
    exit(1)

print("Factors of ", number, " are: ", end = "")
for i in range(number):
    if number % (i+1) == 0:
        print(i+1, end = " ")