n = int(input("Enter a number: "))
a, b = 0, 1
print(f"Fibonacci series upto {n} is: ")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
