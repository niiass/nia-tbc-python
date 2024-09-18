import random

suit_number = random.randint(1, 4)
value_number = random.randint(1, 13)

suit, value = "Not Defined", "Not Defined"

if suit_number == 1:
    suit = "Clubs"
elif suit_number == 2:
    suit = "Diamonds"
elif suit_number == 3:
    suit = "Hearts"
elif suit_number == 4:
    suit == "Spades"

if value_number == 1:
    value == "Ace"
elif value_number == 11:
    value = "Jack"
elif value_number == 12:
    value = "Queen"
elif value_number == 13:
    value = "King"
else:
    value = str(value_number)

if value == "Not Defined" or suit == "Not Defined":
    print("Something went wrong!")
    exit(1)

print("Randomly generated card of deck is ", value, " of ", suit)