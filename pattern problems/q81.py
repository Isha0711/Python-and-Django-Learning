n = 5  
num = 1  
char = 65  
for i in range(n):
    if i % 2 == 0: 
        for j in range(i + 1):
            print(num, end=' ')
            num += 1  
    else:  
        for j in range(i + 1):
            print(chr(char), end=' ')
            char += 1 
    print()  
