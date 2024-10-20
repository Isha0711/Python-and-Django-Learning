n = 4  
for i in range(n):
    p = 65  
    
    for j in range(i):
        print(" ", end='')
    
    for j in range(n - i):
        print(chr(p), end='')
        p =p+1

    p=p-1
    for j in range(n - i - 1):
        p=p-1  
        print(chr(p), end='')
    print() 