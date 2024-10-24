#How do you handle a tuple of unknown size when unpacking into variables?

t=(3,4,5,0,9,7,"hello") 
a,b,*c=t 
print(a) 
print(b) 
print(c) 