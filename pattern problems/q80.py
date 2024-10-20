n = 5 
for i in range(n):
    for j in range(i + 1):
        if i % 2 == 0:  
            if j % 2 == 0: 
                print(j + 1, end='')  
                print('*', end='') 
        else:  
            if j % 2 == 0:  
                print('*', end='') 
            else: 
                print(j + 1, end='') 
    print()  
