n = int(input("Enter a number: "))
if n > 1:
    prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if prime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")
else:
    print(n, "is not a prime number")