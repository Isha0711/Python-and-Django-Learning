#How do you find the Cartesian product of two sets?
s1={10,20,30,40} 
s2={10,20,30,40,50} 
result = set() 
for a in s1: 
    for b in s2: 
     result.add((a,b)) 
print(result) 