number = int(input("შეიყვანეთ მთელი რიცხვი: "))

if number <= 0 or number > 10:
    print("შეყვანილი რიცხვი აუცილებლად უნდა იყოს დადებითი და არაუმეტეს 10!")
    exit(1)
    
if number == 1:
    print("არ აქვს მარტივი გამყოფი")
if number % 2 == 0:
    print(2, end=" ")
if number % 3 == 0:
    print(3, end=" ")
if number % 5 == 0:
    print(5, end=" ")
if number % 7 == 0:
    print(7, end=" ")
