n = int(input("Enter a number: "))
if n>1:
 print(f"Prime numbers upto {n} are:")
 for i in range(2, n + 1):  #since 2 is the smallest prime number
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i, end=" ")
 