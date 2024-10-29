#How do you find all unique subsets of a given set?
s1={10,20,30,40,50}
s1 = list(s1)  
subsets = [[]]  
for element in s1: 
    new_subsets = [] 
    for subset in subsets: 
        new_subsets.append(subset + [element])   
    subsets.extend(new_subsets)  

subsets=[set(subset) for subset in subsets] 
print(subsets) 