n = 5  
current_num = 1  
for i in range(1, n + 1):
    print('' * (i - 1), end='')  
    for j in range(i):
        print(current_num, end=' ')
        current_num += 1  
        if current_num > 9:  
            current_num = 1
    print()  
