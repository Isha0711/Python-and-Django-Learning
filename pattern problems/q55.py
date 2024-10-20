n=4
for i in range(1,n):
    for k in range(1,n-i):
        print('', end = '')
    for j in range(1,2*i):
        print("*",end='')
    print()

