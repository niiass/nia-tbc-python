number = int(input("Enter positive number: "))

if number <= 0 or number >= 50:
    print("Number must be positive integer from 1 to 49")
    exit(1)

n = number

while number > 0:
    print(" " * number, "/", "*" * (2*(n-number)), "\\", sep = "")
    number -= 1

print(" " * n, "|", sep = "")