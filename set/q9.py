#How do you check if one set is a superset of another set?

s1={10,20,30,40,50}
s2={10,20,30}
if s1.issuperset(s2): 
     print("s1 is superset of s2.") 
else: 
     print("s1 is not superset of s2.") 

if s2.issuperset(s1): 
     print("s2 is superset of s1.") 
else: 
    print("s2 is not superset of s1.") 