n = 5
start_num = 5
for i in range(1, n + 1):
    for k in range(1, n - i + 1):
        print('', end='')
    for j in range(start_num - i + 1, start_num + 1):
        print(j, end='')
    for j in range(start_num - 1, start_num - i, -1):
        print(j, end='')
    print()
    