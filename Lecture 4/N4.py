number = int(input("Please enter non negative integer: "))

if number < 0 or number >= 20:
    print("Number must be integer from 0 to 19!")
    exit(1)

a = 0
b = 1
element = 0

if number == 0:
    print(a)
elif number == 1 or number == 2:
    print(b)
else:
    for i in range(number-1):
        element = a + b
        a = b
        b = element

print(element)