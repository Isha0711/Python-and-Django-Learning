for i in range(6):
    for j in range(i,5):
        print(" ", end = ' ')
    for j in range(i):
        print("*", end = ' ')   
    for j in range(i+1,0,-1):
        print("*", end = ' ')    
    print(' ')