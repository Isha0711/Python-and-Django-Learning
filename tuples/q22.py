#How do you perform element-wise addition of two tuples of the same length?

t1=(10,20,30,40,50) 
t2=(100,200,300,400,500,) 
sum=[] 
if (len(t1))==len(t2): 
    for i in range(len(t1)): 
     sum.append(t1[i]+t2[i]) 
    else: 
      print("Two tuples are not of same length.") 
sum=tuple(sum) 
print(sum) 
print(type(sum)) 