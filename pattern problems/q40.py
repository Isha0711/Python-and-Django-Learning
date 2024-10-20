n="ABCDE"
length=len(n)
for i in range(length):
    for j in range(length-i-1):
        print('', end = ' ')
    for j in range(i+1):
        print(n[j],end=' ')
    print()
for i in range(length-2,-1,-1):
    for j in range(length-i-1):
        print('', end = ' ')
    for j in range(i+1):
        print(n[j],end=' ')
    print()            
