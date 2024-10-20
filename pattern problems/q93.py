n=9
for i in range(5):
    for j in range(i+1):
        print(n,end=" ")
        n=n-2
    print()
    if i==0:
      n=n+1
    else:
        n=n+3
    if n<0:
        n*=-1