k=3
for i in range(1,5):
    for j in range(k):
        print(end=" ")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i,0,-1):
        if i==j:
            continue
        else:
            print(j,end="")
    print()
    k=k-1
k=k+1
for i in range (1,4):
    k=k+1
    for j in range(k):
        print(end=" ") 
    for j in range(1,5-i):
        print(j,end="")
    for j in range(3-i,0,-1):
        print(j,end="")
    print()