line_one = input("Enter word/sentence N1: ")
line_two = input("Enter word/sentence N2: ")

line_one = sorted(line_one)
line_two = sorted(line_two)

if line_one == line_two:
    print("YES")
else:
    print("NO")
