n = int(input("Please enter number from 0 to 10: "))

if n <= 0 or n >= 10:
    print("Input must be an integer from 0 to 10!")
    exit(1)

temp = n
line = ""

while n > 0:
    line = line + " " + str((temp + 1 -n))
    n -= 1
    print(line)

while n < temp - 1:
    print(line[:(2*(temp-n)-1)])
    n += 1