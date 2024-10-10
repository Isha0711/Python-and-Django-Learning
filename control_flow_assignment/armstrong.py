n = int(input("Enter a number: "))
temp = n
length = len(str(n))
sum = 0
while temp > 0:
    num = temp % 10
    sum += num ** length
    temp //= 10
if sum == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
