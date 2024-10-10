n = int(input("Enter a number: "))
temp = n
reverse = 0
while temp > 0:
    num = temp % 10
    reverse = reverse * 10 + num
    temp //= 10

if reverse == n:
    print(n, "is a palindrome number")
else:
    print(n, "is not a palindrome number")
