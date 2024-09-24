from datetime import date

birth_year = int(input("Please enter your birth year: "))
birth_month = int(input("Please enter number of your birth month: "))
birth_date = int(input("Please enter your birth date: "))

day = date(birth_year, birth_month, birth_date).weekday()

if day == 0:
    print("You were born on Monday")
elif day == 1:
    print("You were born on Tuesday")
elif day == 2:
    print("You were born on Wednesday")
elif day == 3:
    print("You were born on Thursday")
elif day == 4:
    print("You were born on Friday")
elif day == 5:
    print("You were born on Saturday")
elif day == 6:
    print("You were born on Sunday")