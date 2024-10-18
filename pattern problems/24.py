n=65
for i in range(5):
    for j in range(i):
        print(" ", end = ' ')
    for j in range(i,5):
        print(chr(n+j), end = ' ')   
    for j in range(3,i-1,-1):
        print(chr(n+j), end = ' ')         
    print(' ')