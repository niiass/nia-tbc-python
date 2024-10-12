import random

random_num = random.randint(0, 100)
guess = int(input("Please enter integer from 0 to 100: "))
count = 1

if guess < 0 or guess > 100:
    print("Input must be integer from 0 to 100!")
    exit(1)

while guess != random_num:
    if guess > random_num:
        print("High")
        guess = int(input("Please enter integer from 0 to 100: "))

        count += 1
    elif guess < random_num:
        print("Low")
        guess = int(input("Please enter integer from 0 to 100: "))

        count += 1
    
    if count == 10:
        print("You lost")
        break

if (guess == random_num):
     print("You are winner")