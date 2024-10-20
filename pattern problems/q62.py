n = 5
for i in range(1, n + 1):
    for j in range(i):
        print('A' if j % 2 == 0 else 'B', end='')
    print()
        