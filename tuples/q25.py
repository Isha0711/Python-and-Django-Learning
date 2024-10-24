#How can you use a generator to create a tuple?
t=(x for x in range(10) ) 
print(tuple(t)) 
print(type(t))