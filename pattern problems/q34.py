n=5
for i in range(1,n):
    for k in range(1,n-i):
        print(' ', end = ' ')
    for j in range(1,2*i):
        print("*",end=' ')
    print()
for i in range(n-2,0,-1):
    for k in range(1,n-i):
        print(' ', end = ' ')
    for j in range(1,2*i):
        print("*",end=' ')
    print()    
