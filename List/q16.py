#How would you remove all occurrences of a specific element from a list?
l=[10,20,30,40,50,60,10,20,30,40,50,60,10,20,30,40]
x = int(input("Enter the no you want to remove:"))
while True:
    if x in l:
        l.remove(x)
    else:
        break
print(l)