n = int(input("Enter a number: "))
temp = n
sum = 0
while temp > 0:
    num = temp % 10
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    sum += fact
    temp //= 10
if sum == n:
    print(n, "is a strong number")
else:
    print(n, "is not a strong number")
