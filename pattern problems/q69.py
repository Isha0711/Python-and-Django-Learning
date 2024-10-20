n=4
for i in range(n):
    for j in range(n):
        print(chr((i + j) % n + 65), end='')  # 65 is the ASCII value for 'A'
    print()
