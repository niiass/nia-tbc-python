line = input("Enter a line: ")

for i in range (0, len(line), 2):
    if line[i] != "e":
        print('\"', line[i], '\"', sep="")