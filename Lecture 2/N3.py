number = int(input("შეიყვანეთ მთელი რიცხვი: "))

if number <= 0 or number > 10:
    print("შეყვანილი რიცხვი აუცილებლად უნდა იყოს დადებითი და არაუმეტეს 10!")
    exit(1)
    
if number == 1:
    print("ამ რიცხვს არ აქვს მარტივი გამყოფ(ებ)ი")
elif number == 2:
    print("მარტივი გამყოფ(ებ)ია: 2")
elif number == 3:
    print("მარტივი გამყოფ(ებ)ია: 3")
elif number == 4:
    print("მარტივი გამყოფ(ებ)ია: 2")
elif number == 5:
    print("მარტივი გამყოფ(ებ)ია: 5")
elif number == 6:
    print("მარტივი გამყოფ(ებ)ია: 2, 3")
elif number == 7:
    print("მარტივი გამყოფ(ებ)ია: 7")
elif number == 8:
    print("მარტივი გამყოფ(ებ)ია: 2")
elif number == 9:
    print("მარტივი გამყოფ(ებ)ია: 3")
elif number == 10:
    print("მარტივი გამყოფ(ებ)ია: 2, 5")
