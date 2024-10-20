n = 7  
for i in range(n):
    for j in range(n):
        if j == i:
            print('*', end='')  
        else:
            print('0', end='') 
    print()  
