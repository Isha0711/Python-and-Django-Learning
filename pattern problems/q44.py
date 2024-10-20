for i in range(4):
    k=1
    for j in range(4):
        print(k,end="")
        k=k+1
        if(k==5-i):
            break
    for j in range((i-0)*2):
        print("_",end="")
    k=k-1
    for j in range(4):
        print(k,end="")
        k=k-1
        if(k==0):
            break
    print()