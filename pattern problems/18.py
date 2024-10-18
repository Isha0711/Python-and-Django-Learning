for i in range(5,0,-1):
    for j in range(i,5):
        print(" ", end = ' ')
    for j in range(i):
        print(j+1, end = ' ')   
    for j in range(i-1,0,-1):
        print(j, end = ' ')    
    print(' ')