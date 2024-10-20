n="ABCD"
for i in range(4):
    for j in range(i+1):
        print(n[i], end = ' ')   
    print()
for i in range(3,0,-1):  
    for j in range(i):
        print(n[i-1], end = ' ')
    print(' ')