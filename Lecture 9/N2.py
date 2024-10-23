import random
import math

n = int(input("Enter an integer: "))

if n <= 1:
    print("Input must be more than 1!")
    exit(1)

counter = 0
for i in range(n):
    a = random.uniform(0, 1)
    b = random.uniform(0, 1)
    print("Value of a is - ", a, "; Value of b is - ", b)
    if (math.sqrt(a ** 2 + b ** 2) <= 1):
        counter += 1
    #     print("Is less than 1")
    # else:
    #     print("Is more than 1")

print(4*counter/n)