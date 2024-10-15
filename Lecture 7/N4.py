keybord = "qwertyuiopasdfghjklzxcvbnm"

choice = input("Enter action (e/d): ").lower()

if (choice != "d" and choice != "e"):
    print("Action must be e(encode) or d(decode)!")
    exit(1)

word = input("Enter text: ")

if choice == "e":
    for i in range(len(word)):
        if word[i] == "p":
            word = word.replace(word[i], "q")
        elif word[i] == "l":
            word = word.replace(word[i], "a")
        elif word[i] == "m":
            word = word.replace(word[i], "z")
        else:
            word = word[:i] + keybord[keybord.index(word[i])+1] + word[i+1:]
elif choice == "d":
    for i in range(len(word)):
        if word[i] == "q":
            word = word.replace(word[i], "p")
        elif word[i] == "a":
            word = word.replace(word[i], "l")
        elif word[i] == "z":
            word = word.replace(word[i], "m")
        else:
            word = word[:i] + keybord[keybord.index(word[i])-1] + word[i+1:]

print(word)