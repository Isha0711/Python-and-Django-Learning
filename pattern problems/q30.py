n=5
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end =" ")
    for j in range(i+1,0,-1):
        print(j,end=" ")
    print()    
