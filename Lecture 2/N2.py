number_one = int(input("შეიყვანეთ პირველი რიცხვი: "))
number_two = int(input("შეიყვანეთ მეორე რიცხვი: "))

mod = number_one % number_two

if mod == 0:
    print(number_one, " არის ", number_two, "-ს ჯერადი")
else:
    print(number_one, " არ არის ", number_two, "-ს ჯერადი")