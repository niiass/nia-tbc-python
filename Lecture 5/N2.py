j = 1
for i in range(9):
    j = 1
    while j <= i+1:
        print(j, " * ", i+1, " = ", j*(i+1), end = " ")
        j += 1
    print()