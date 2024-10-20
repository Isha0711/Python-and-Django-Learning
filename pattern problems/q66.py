lists=['','A','B','C']
n = 3 
for i in range(1, n+1):
    for j in range(1, n - i + 2):
        print(lists[j], end="")
    if i > 1:
        print(" " * (2 * i - 3), end="")
    if i > 1:
        for j in range(n - i + 1, 0, -1):
            print(lists[j], end="")
    else:
        for j in range(2, 0, -1):
            print(lists[j], end="")
    print()
for i in range(n-1, 0, -1):
    for j in range(1, n - i + 2):
        print(lists[j], end="")
    if i > 1:
        print(" " * (2 * i - 3), end="")
    if i > 1:
        for j in range(n - i + 1, 0, -1):
            print(lists[j], end="")
    else:
        for j in range(2, 0, -1):
            print(lists[j], end="")
    print()