n = 5 
for i in range(n):
    for j in range(i + 1):
        if (i % 2 == 0):
            print('1' if j % 2 == 0 else '0', end='')  
        else: 
            print('0' if j % 2 == 0 else '1', end='')  
    print()  

