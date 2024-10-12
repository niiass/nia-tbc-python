number = int(input("Please enter integer from 0 to 10000: "))
reversed = 0
sum = 0
digits = 0

if number <= 0 or number > 10000:
    print("Input must be an integer from 0 to 10000!")
    exit(1)

n = number

while number > 0:
    number = number // 10
    digits += 1

while n != 0:
    reversed += (n % 10) * pow(10, digits-1)
    sum += n % 10
    digits -= 1
    n = n // 10

print(" Reversed number is: ", reversed, '\n', "Sum of the digits is: ", sum)