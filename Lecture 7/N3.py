word = input("Enter a word: ")
mid = len(word)//2

count = 5
while count > 0:
    print("First letter - ", word[0], end = "; ")
    if (len(word) % 2 == 1):
        print("Middle letter - ", word[mid], end = "; ")
    elif (len(word) % 2 == 0):
        print("Middle letters - ", word[mid-1], ", ", word[mid], end = "; ")
    print("Last letter - ", word[len(word) - 1], end = ";\n")
    count -= 1