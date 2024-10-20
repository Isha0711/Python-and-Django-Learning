first_number=7
for i in range(4):
    for j in range(2**i):
        if j==0:
            print(first_number,end=" ")
            number=first_number+1
        else:
            print(number,end=" ")
            number=number+1
    print()
    first_number=first_number*2