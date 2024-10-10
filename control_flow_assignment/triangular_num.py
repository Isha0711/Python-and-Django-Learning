n = int(input("Enter a number: "))
i = 1
triangular = False
#the formula for calculating triangular number is (n(n+1))/2
while (i * (i + 1)) // 2 <= n:
    if (i * (i + 1)) // 2 == n:
        triangular = True
        break
    i += 1
    
if triangular:
    print(n, "is a triangular number")
else:
    print(n, "is not a triangular number")
