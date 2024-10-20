for i in range(4,0,-1):
    number=1 if i%2==0 else 3
    for j in range(i):
        print(number,end="")
        number=number+1
        if number>4:
            number=number%4
    print()

