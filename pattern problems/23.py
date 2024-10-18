n=65
for i in range(5):
    for j in range(i,5):
        print(" ", end = ' ')
    for j in range(i):
        print(chr(n+j), end = ' ')   
    for j in range(i+1,0,-1):
        print(chr(n-1+j), end = ' ') 
    print(' ')