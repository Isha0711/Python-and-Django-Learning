n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1:  
            print(3, end='')
        elif j == 0 or j == n - 1:  
            print(3, end='')
        elif i == 2 and j == 2:  
            print(1, end='')
        else:
            print(2, end='')
    print()
