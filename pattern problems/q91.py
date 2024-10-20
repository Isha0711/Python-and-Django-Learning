n = 5  
for i in range(n):
    print(' ' * i, end='')
    for j in range(n - i, 0, -1):
        print(j, end='')
    for j in range(2, n - i + 1):
        print(j, end='')
    print()  

