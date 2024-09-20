velocity = float(input("Please enter velocity of car: "))

category = "Velocity not assigned"

if velocity < 0:
    print("Velocity must be positive!")
    exit(1)

if velocity > 120:
    category = "VERY FAST"
elif velocity > 60:
    category = "FAST"
elif velocity > 30:
    category = "MODERATE"
else:
    category = "SLOW"

print(category)
