n=6
for i in range(1,n):
    for j in range(i):
        print('', end = ' ')
    for j in range(i,n):
        print(j,end='')
    for j in range(n-2,i-1,-1):
        print(j,end='')
    print()    
