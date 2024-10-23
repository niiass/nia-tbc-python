n = int(input("Enter an integer: "))

if n <= 1:
    print("Input must be more than 1!")
    exit(1)

sum = 0

while n > 0:
    if n % 2 == 0:
        sum = sum - 1/(2*n-1)
    elif n % 1 == 0:
        sum = sum + 1/(2*n-1)
    n -= 1

print(4*sum)