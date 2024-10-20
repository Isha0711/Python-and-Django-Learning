n = 4  
for i in range(n):
    p = 65  

    for j in range(n - i - 1):
        print(" ", end='')

    for j in range(i + 1):
        print(chr(p), end='')
        p += 1

    p -= 1
    for j in range(i):
        p -= 1  
        print(chr(p), end='') 
    print() 

for i in range(n - 2, -1, -1):
    p = 65 
    
    for j in range(n - i - 1):
        print(" ", end='')
    
    for j in range(i + 1):
        print(chr(p), end='')
        p += 1

    p -= 1
    for j in range(i):
        p -= 1  
        print(chr(p), end='')
    print()  