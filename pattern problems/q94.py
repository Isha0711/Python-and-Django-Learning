for i in range(4):
    for j in range(4):
        if i==j:
            print("*",end="")
        else:
            print("0",end="")
    print("*",end="")
    for j in range(3,-1,-1):
        if i==j:
            print("*",end="")
        else:
            print("0",end="")
    print()