for i in range(4):
    for j in range(4-i):
        print(end= ' ')
    for j in range(i):
            if j==0 or j==i:
              print(1,end=' ')
            else:
              print(i,end= ' ')
    print(1,end=' ')
    print()