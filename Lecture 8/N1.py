line = input("Enter word/sentence: ").lower()
line = line.replace(" ", "")
for i in line:
    if not (i.isalnum()):
        line = line.replace(i, "")

reversed = line[len(line):0:-1] + line[0]

if reversed == line:
    print("It is a palindrome")
else:
    print("It is not a palindrome")