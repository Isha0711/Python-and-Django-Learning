for i in range(5):
    k=1
    for j in range(5):
        print("*",end="")
        k=k+1
        if(k==6-i):
            break
    for j in range((i-0)*2):
        print(" ",end="")
    k=k-1
    for j in range(5):
        print("*",  end="")
        k=k-1
        if(k==0):
            break
    print() 