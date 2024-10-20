n = 4  
for i in range(1, n + 1):
    if i == 1:  
        print('1' + '3' * (n - 1))  
    elif i == 2:  
        print('2' * n) 
    elif i == 3: 
        print('3' * (n - 1) + '1')  
