n = 6
string = "ABCDEF"
for i in range(n):
    for j in range(n - i):
        print(string[j], end='')
    for j in range(n - i - 1, -1, -1):
        print(string[j], end='')
    print()