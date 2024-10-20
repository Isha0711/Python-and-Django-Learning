n = 5  
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end='')
    print('' * (n - i) * 2, end=' ') 
    for j in range(i):
        print(chr(96 + (i - j)), end='')  
    print()  

    
    
 

   
    