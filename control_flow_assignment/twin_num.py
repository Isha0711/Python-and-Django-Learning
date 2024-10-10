a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if abs(a - b) == 2:
    prime_a = True
    prime_b = True
    #checking if 'a' is prime
    for i in range(2, int(a ** 0.5) + 1):  
        if a % i == 0:
            prime_a = False
            break
           
    #checking if 'b' is prime
    for i in range(2, int(b ** 0.5) + 1):  
        if b % i == 0:
            prime_b = False
            break

    if prime_a and prime_b:
        print(f"{a} and {b} are twin prime numbers")
    else:
        print(f"{a} and {b} are not twin prime numbers")
else:
    print(f"{a} and {b} are not twin prime numbers because their difference is not 2")
