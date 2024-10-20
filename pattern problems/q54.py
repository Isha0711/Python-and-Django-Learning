for i in range(9):
    print("*",end="")
    for j in range(i+1):
        if j+1==i:
            print('*',end=" ")
            break
        elif j<i:
            print(end=" ")
    print()
    if(i+1==9):
        for j in range(10):
            print('*',end="")