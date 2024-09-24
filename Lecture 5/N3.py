number = int(input("Enter positive number: "))

if number < 0 or number > 20:
    print("Number must be non negative integer from 0 to 20")
    exit(1)

first = 0
second = 1
nth = 0
elements = 2

print(first, second, end = " ")

while elements <= number:
    nth = first + second
    first = second
    second = nth
    print(nth, end = " ")
    elements += 1