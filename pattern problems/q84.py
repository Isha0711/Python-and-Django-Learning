number=1
for i in range(7):
    if i%2==0:
        print(number,end="")
        number+=1
    else:
        for j in range(2):
            print(number,end="")
            number+=1
    print()