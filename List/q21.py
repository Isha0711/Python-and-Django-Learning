#How would you rotate a list by n positions to the left?
l=[10,20,30,40,50,60] 
n=int(input("Enter n to rotate elements to left: ")) 
rotate=l[n:]+l[:n] 
print(rotate) 