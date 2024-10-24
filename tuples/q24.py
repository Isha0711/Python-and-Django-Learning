#How would you implement a tuple as an immutable list and handle operations like appending?

t1=(10,20,30,40,50)
t1=list(t1) 
print(t1) 
print(type(t1)) 
t1.append(60) 
t1=tuple(t1) 
print(t1) 
print(type(t1)) 