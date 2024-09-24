import random

players = int(input("Please enter number of players: "))

for i in range(players):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    print("Player ", i+1, " rolled: ", dice_1, " ", dice_2)
