for i in range(5):
    for j in range(5-i):
        print("#",end="")
    print("*",end="")
    if i!=0:
        for j in range(i*2-1):    
            print("#",end="")
    print("*",end="")
    for j in range(5-i):
        print("#",end="")
    print()
for i in range(11):
    if i==0 or i==10:
        print("*",end="")
    else:
        print("#",end="")