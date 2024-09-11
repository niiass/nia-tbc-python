import math

print("შეიყვანეთ სამკუთხედის გვერდები:")
print("პირველი:")
side_one = input()

print("მეორე:")
side_two = input()

print("მესამე:")
side_three = input()

perimeter = int(side_one) + int(side_two) + int(side_three)
half = perimeter/2
area = math.sqrt(half*(half - int(side_one))*(half - int(side_two))*(half - int(side_three)))

print("პერიმეტრი: ", perimeter)
print("ფართობი: ", area)