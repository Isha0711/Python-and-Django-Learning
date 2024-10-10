n = int(input("Enter a number: "))
temp = n
sum = 0
while temp > 0:
    num = temp % 10
    sum += num
    temp //= 10
if n % sum == 0:
    print(n, "is a Harshad number")
else:
    print(n, "is not a Harshad number")
