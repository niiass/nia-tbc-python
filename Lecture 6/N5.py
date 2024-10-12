n = int(input("Please enter number from 0 to 10: "))

if n <= 0 or n >= 10:
    print("Input must be an integer from 0 to 10!")
    exit(1)

line = ""
temp = n

while abs(n) <= temp:
    line = line + " " + str(abs(n))
    n -= 1

size = len(line)//2
while size < len(line):
    s = (len(line) - size) * " " + line[(len(line)-size):(size + 1)]
    print(s)
    size += 2
